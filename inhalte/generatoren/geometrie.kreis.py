#!/usr/bin/env python3
"""Thema geometrie.kreis – Kreis und Tangenten (Gymnasium Bayern, Klasse 7)."""
import math
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl7 import A, L, Z, baue, figur, jw, kl, ksys, zt  # noqa: E402

META = {'thema_schluessel': 'geometrie.kreis', 'thema_id': 45, 'block_id': 79, 'klasse': {'gym_by': 7, 'rs_by': 7}}


def rd(v): return round(v, 2)


def thales_bild(al, texte=('α', 'β', 'γ')):
    """Thaleskreis: AB Durchmesser (r = 3), C auf dem Kreis mit ∠CAB = α (∠BMC = 2α, von B aus gemessen)."""
    phi = math.radians(2 * al)
    C = [rd(3 * math.cos(phi)), rd(3 * math.sin(phi))]
    return figur({'A': [-3, 0], 'B': [3, 0], 'C': C, 'M': [0, 0]}, linien=[['A', 'B'], ['B', 'C'], ['C', 'A']], flaeche=['A', 'B', 'C'],
                 winkel=[w for w in [['A', 'B', 'C', texte[0]], ['B', 'C', 'A', texte[1]]] if w[3]], rechter_winkel=[['C', 'A', 'B']] if texte[2] == '90°' else [],
                 kreise=[{'m': 'M', 'r': 3}])


def tangenten_bild(phi, texte=('φ', '')):
    """Kreis um M (r = 2), Punkt P außen; Tangenten berühren in B und B'. ∠BPB' = φ."""
    d = 2 / math.sin(math.radians(phi / 2))
    t = math.acos(2 / d)
    B, B2 = [rd(2 * math.cos(t)), rd(2 * math.sin(t))], [rd(2 * math.cos(t)), rd(-2 * math.sin(t))]
    w = [['P', 'B', "B'", texte[0]]]
    if texte[1]: w.append(['M', "B'", 'B', texte[1]])
    return figur({'M': [0, 0], 'P': [rd(d), 0], 'B': B, "B'": B2}, linien=[['P', 'B'], ['P', "B'"], ['M', 'B', 'r'], ['M', "B'", 'r'], ['M', 'P', '', 'gestrichelt']],
                 rechter_winkel=[['B', 'M', 'P'], ["B'", 'M', 'P']], winkel=w, kreise=[{'m': 'M', 'r': 2}])


ETAPPEN = [
    {'lernziel': 'thales', 'titel': 'Satz des Thales anwenden',
     'regel': '⟦Satz des Thales⟧: Liegt C auf einem Kreis mit dem Durchmesser [AB], dann hat das Dreieck ABC bei C einen ⟦rechten Winkel⟧. Den Kreis nennt man ⟦Thaleskreis⟧.',
     'schritte': ['[AB] ist Durchmesser, C liegt auf dem Kreis, α = 35°.', 'Nach Thales: γ = 90°.', 'β = 180° − 90° − 35° = ⟦55°⟧'],
     'fehler': 'Liegt C auf dem Kreis, aber [AB] ist ⟦kein Durchmesser⟧ (sondern nur eine Sehne), gilt der Satz des Thales nicht – γ ist dann im Allgemeinen kein rechter Winkel.',
     'bild': {'typ': 'figur', 'punkte': {'A': [-3, 0], 'B': [3, 0], 'C': [1.03, 2.82], 'M': [0, 0]}, 'flaeche': ['A', 'B', 'C'], 'linien': [['A', 'B'], ['B', 'C'], ['C', 'A']], 'rechter_winkel': [['C', 'A', 'B']], 'winkel': [['A', 'B', 'C', '35°'], ['B', 'C', 'A', 'β']], 'kreise': [{'m': 'M', 'r': 3}]},
     '_verbot': ['α = 35°']},
    {'lernziel': 'umkehrung', 'titel': 'Umkehrung: Wo liegt der Thaleskreis?',
     'regel': '⟦Umkehrung⟧: Hat das Dreieck ABC bei C einen rechten Winkel, dann liegt C auf dem Kreis mit dem ⟦Durchmesser [AB]⟧. Sein Mittelpunkt ist die ⟦Mitte von [AB]⟧, sein Radius die halbe Länge von [AB].',
     'schritte': ['A(−2 | 1), B(6 | 1), ∠ACB = 90°', 'Mitte von [AB]: M((−2 + 6) : 2 | 1) = M(2 | 1)', 'Radius: 8 : 2 = ⟦4⟧. C liegt auf dem Kreis um M(2 | 1) mit r = 4.'],
     'fehler': 'Der Mittelpunkt des Thaleskreises ist nicht C, sondern die ⟦Mitte der Hypotenuse⟧ [AB] – der Seite gegenüber dem rechten Winkel.',
     'bild': ksys([(-2, 1, 'A'), (6, 1, 'B'), (2, 1, 'M'), (2, 5, 'C')], strecken=[(-2, 1, 6, 1), (-2, 1, 2, 5), (6, 1, 2, 5)]),
     '_verbot': ['A(−2 | 1), B(6 | 1)']},
    {'lernziel': 'beweis', 'titel': 'Vermuten und Beweisen',
     'regel': 'Messungen mit Geometriesoftware führen zu ⟦Vermutungen⟧. Ein ⟦Beweis⟧ zeigt mit Begründungen, dass eine Aussage ⟦immer⟧ gilt. Beim Thalessatz: MA = MB = MC (Radien) ergibt zwei ⟦gleichschenklige Dreiecke⟧.',
     'schritte': ['Dreieck AMC ist gleichschenklig: ∠ACM = α. Dreieck BMC: ∠BCM = β.', 'Also γ = α + β. Winkelsumme: α + β + (α + β) = 180°.', '2(α + β) = 180° → ⟦γ = α + β = 90°⟧'],
     'fehler': 'Hundert gemessene Beispiele mit 90° sind ⟦kein Beweis⟧: Sie zeigen nur, dass die Aussage für diese Beispiele stimmt.',
     'bild': {'typ': 'figur', 'punkte': {'A': [-3, 0], 'B': [3, 0], 'C': [1.03, 2.82], 'M': [0, 0]}, 'linien': [['A', 'B'], ['B', 'C'], ['C', 'A'], ['M', 'C', 'r', 'gestrichelt']], 'winkel': [['A', 'B', 'C', 'α'], ['C', 'A', 'M', 'α'], ['B', 'C', 'A', 'β'], ['C', 'M', 'B', 'β']], 'kreise': [{'m': 'M', 'r': 3}]}},
    {'lernziel': 'lage', 'titel': 'Passante, Tangente oder Sekante?',
     'regel': 'Vergleiche den Abstand d der Geraden vom Mittelpunkt mit dem Radius r: ⟦d > r⟧ Passante (kein Punkt), ⟦d = r⟧ Tangente (ein Punkt), ⟦d < r⟧ Sekante (zwei Punkte).',
     'schritte': ['r = 4 cm, Abstand der Geraden von M: d = 3 cm', '3 cm < 4 cm', 'Die Gerade ist eine ⟦Sekante⟧ – sie schneidet den Kreis zweimal.'],
     'fehler': 'Eine Gerade mit d = r schneidet den Kreis nicht zweimal: Sie ⟦berührt⟧ ihn nur in einem Punkt.',
     'bild': figur({'M': [0, 0], '_1': [-5, 3], '_2': [5, 3], '_F': [0, 3]}, linien=[['_1', '_2', 'g'], ['M', '_F', 'd = 3', 'gestrichelt']], rechter_winkel=[['_F', 'M', '_2']],
                   kreise=[{'m': 'M', 'r': 4}]),
     '_verbot': ['d = 3 cm']},
    {'lernziel': 'tangente', 'titel': 'Tangenten und Berührradius',
     'regel': 'Eine ⟦Tangente⟧ berührt den Kreis in genau einem Punkt B. Sie steht ⟦senkrecht⟧ auf dem Berührradius [MB]. Von einem Punkt P außerhalb gibt es ⟦zwei⟧ Tangenten; sie sind von P bis zum Berührpunkt gleich lang.',
     'schritte': ['Die Tangenten von P bilden den Winkel φ = 50°.', 'Viereck MBPB\': zwei rechte Winkel bei B und B\', Winkelsumme 360°.', '∠BMB\' = 360° − 90° − 90° − 50° = ⟦130°⟧'],
     'fehler': 'Der Winkel zwischen Tangente und Berührradius ist nicht „irgendein spitzer Winkel“: Er ist ⟦immer 90°⟧.',
     'bild': tangenten_bild(50, ('50°', '?')),
     '_verbot': ['φ = 50°']},
    {'lernziel': 'umkreis_inkreis', 'titel': 'Umkreis und Inkreis',
     'regel': 'Der ⟦Umkreismittelpunkt⟧ ist der Schnittpunkt der ⟦Mittelsenkrechten⟧ (gleich weit von allen Ecken). Der ⟦Inkreismittelpunkt⟧ ist der Schnittpunkt der ⟦Winkelhalbierenden⟧ (gleich weit von allen Seiten).',
     'schritte': ['Dreieck mit γ = 90°', 'Nach Thales liegt C auf dem Kreis mit Durchmesser [AB].', 'Der Umkreismittelpunkt ist die ⟦Mitte der Seite [AB]⟧.'],
     'fehler': 'Der Inkreismittelpunkt entsteht nicht aus den Mittelsenkrechten: Er muss von den ⟦Seiten⟧ gleich weit weg sein – dafür braucht man die ⟦Winkelhalbierenden⟧.',
     'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [6, 0], 'C': [2, 4], 'M': [3, 1]}, 'flaeche': ['A', 'B', 'C'], 'linien': [['A', 'B'], ['B', 'C'], ['C', 'A'], ['M', 'A', 'r', 'gestrichelt'], ['M', 'C', 'r', 'gestrichelt']], 'kreise': [{'m': 'M', 'r': 3.162}]}},
]


ZYK = {}


def zyklus(name, liste):
    ZYK[name] = ZYK.get(name, -1) + 1
    return liste[ZYK[name] % len(liste)]


def g_thales(R, st):
    al = R.randint(15, 75)
    if al == 45: al = 40
    if st == 1:
        if ZYK.get('gamma', 0) < 2:
            ZYK['gamma'] = ZYK.get('gamma', 0) + 1
            a = Z(f'[AB] ist ein Durchmesser, C liegt auf dem Kreis. Es ist α = {al}°. Wie groß ist γ?', 90, '180 - 90',
                  f'Nach dem Satz des Thales ist der Winkel bei C ein rechter Winkel: γ = 90°.', 'Was sagt der Satz des Thales über den Winkel bei C?', '°')
            a['f']['grafik'] = thales_bild(al, (f'{al}°', '', ''))
            return a
        a = Z(f'[AB] ist ein Durchmesser, C liegt auf dem Kreis. Es ist α = {al}°. Wie groß ist β?', 90 - al, f'180 - 90 - {al}',
              f'Thales: γ = 90°. β = 180° − 90° − {al}° = {90 - al}°.', 'Erst γ mit Thales, dann die Winkelsumme.', '°')
        a['f']['grafik'] = thales_bild(al, (f'{al}°', 'β', '90°'))
        return a
    if st == 2:
        if R.random() < .5:
            a = Z(f'[AB] ist ein Durchmesser, C liegt auf dem Kreis. Es ist β = {90 - al}°. Wie groß ist α?', al, f'180 - 90 - {90 - al}',
                  f'Thales: γ = 90°. α = 180° − 90° − {90 - al}° = {al}°.', 'Erst γ mit Thales, dann die Winkelsumme.', '°')
            a['f']['grafik'] = thales_bild(al, ('α', f'{90 - al}°', '90°'))
            return a
        s_ = R.choice([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15])
        return Z(f'Über einer {s_} cm langen Strecke [AB] wird der Thaleskreis gezeichnet. Wie groß ist sein Radius?', Fr(s_, 2), f'{s_} / 2',
                 f'[AB] ist der Durchmesser: r = {s_} cm : 2 = {zt(Fr(s_, 2))} cm.', 'Die Strecke ist der Durchmesser des Thaleskreises.', 'cm')
    art = zyklus('th3', ['mitte', 'fenster', 'verhaeltnis', 'leiter'])
    if art == 'mitte':
        a = Z(f'[AB] ist Durchmesser des Kreises um M, C liegt auf dem Kreis, α = {al}°. Wie groß ist der Winkel ∠BMC?', 2 * al, f'2 * {al}',
              f'Dreieck AMC ist gleichschenklig (MA = MC): ∠ACM = {al}°. ∠AMC = 180° − 2 · {al}° = {180 - 2 * al}°. ∠BMC = 180° − {180 - 2 * al}° = {2 * al}°.',
              'MA und MC sind Radien. Nutze das gleichschenklige Dreieck AMC.', '°')
        a['f']['grafik'] = figur({'A': [-3, 0], 'B': [3, 0], 'M': [0, 0], 'C': [rd(3 * math.cos(math.radians(2 * al))), rd(3 * math.sin(math.radians(2 * al)))]},
                                 linien=[['A', 'B'], ['B', 'C'], ['C', 'A'], ['M', 'C', '', 'gestrichelt']], winkel=[['A', 'B', 'C', f'{al}°'], ['M', 'B', 'C', '?']], kreise=[{'m': 'M', 'r': 3}])
        return a
    if art == 'fenster':
        dm = R.choice([Fr(1), Fr(12, 10), Fr(15, 10), Fr(8, 10), Fr(2)])
        w = R.choice([30, 40, 50, 60, 70])
        return Z(f'Ein Halbkreisfenster hat {zt(dm)} m Durchmesser. Zwei Streben verbinden die Enden des Durchmessers mit einem Punkt auf dem Bogen; '
                 f'eine Strebe bildet mit dem Durchmesser einen Winkel von {w}°. Welchen Winkel bilden die beiden Streben an dem Punkt auf dem Bogen?', 90, '90',
                 'Die Streben bilden mit dem Durchmesser ein Dreieck, dessen dritte Ecke auf dem Halbkreis liegt. Nach Thales ist der Winkel dort 90° – egal wie groß das Fenster ist.',
                 'Welcher Satz handelt von einem Punkt auf einem Halbkreis über einem Durchmesser?', '°')
    if art == 'verhaeltnis':
        k = R.choice([2, 3, 4, 5])
        return Z(f'[AB] ist Durchmesser, C liegt auf dem Kreis. β ist {k}-mal so groß wie α. Wie groß ist α?', Fr(90, k + 1), f'90 / ({k} + 1)',
                 f'Thales: γ = 90°, also α + β = 90°. α + {k}α = 90° → α = 90° : {k + 1} = {zt(Fr(90, k + 1))}°.', 'α + β = 90°.', '°')
    s_ = R.choice([6, 8, 10, 12, 14])
    return Z(f'Eine Ecke eines Zeichendreiecks (rechter Winkel) wird so zwischen zwei Nägel A und B gelegt, dass die Schenkel an den Nägeln anliegen. A und B sind {s_} cm voneinander entfernt. '
             f'Auf welchem Kreis wandert die Ecke, wenn man das Dreieck verschiebt? Gib seinen Radius an.', Fr(s_, 2), f'{s_} / 2',
             f'Umkehrung des Thalessatzes: Die Ecke mit dem rechten Winkel liegt auf dem Thaleskreis über [AB], r = {s_} : 2 = {zt(Fr(s_, 2))} cm.',
             'Rechter Winkel bei der Ecke – an welchen Satz erinnert das?', 'cm')


def g_umkehrung(R, st):
    while True:
        ax, ay = R.randint(-6, 4), R.randint(-4, 4)
        L_ = 2 * R.randint(1, 5)
        horiz = R.random() < .5
        bx, by = (ax + L_, ay) if horiz else (ax, ay + L_)
        if st == 3: bx, by = ax + 2 * R.randint(-4, 4), ay + 2 * R.randint(-4, 4)
        if (bx, by) != (ax, ay): break
    mx, my = (ax + bx) // 2, (ay + by) // 2
    gr = ksys([(ax, ay, 'A'), (bx, by, 'B')], strecken=[(ax, ay, bx, by)])
    if st == 1:
        a = L(f'Das Dreieck ABC hat bei C einen rechten Winkel, A({zt(ax)} | {zt(ay)}), B({zt(bx)} | {zt(by)}). Gib den Mittelpunkt des Kreises an, auf dem C liegt.', 'M(□ | □)',
              [mx, my], [f'({ax} + {bx}) // 2', f'({ay} + {by}) // 2'], f'Thaleskreis über [AB]: Mittelpunkt = Mitte von [AB] = (({zt(ax)} + {kl(bx)}) : 2 | ({zt(ay)} + {kl(by)}) : 2) = M({zt(mx)} | {zt(my)}).',
              'Der Mittelpunkt ist die Mitte der Seite gegenüber dem rechten Winkel.')
        a['f']['grafik'] = gr
        return a
    if st == 2:
        a = Z(f'Das Dreieck ABC hat bei C einen rechten Winkel, A({zt(ax)} | {zt(ay)}), B({zt(bx)} | {zt(by)}). Welchen Radius hat der Kreis, auf dem C liegen muss? (1 Einheit = 1 cm)',
              Fr(L_, 2), f'{L_} / 2', f'[AB] ist {L_} cm lang (Durchmesser). r = {L_} : 2 = {zt(Fr(L_, 2))} cm.', 'Der Radius ist die halbe Länge von [AB].', 'cm')
        a['f']['grafik'] = gr
        return a
    al, be = R.randint(20, 80), R.randint(20, 80)
    if al + be == 90: be += 3
    if R.random() < .5:
        be = 90 - al
    lieg = al + be == 90
    ja, nein = 'Ja, denn γ = 90° (Umkehrung des Thalessatzes).', f'Nein, denn γ = {180 - al - be}° ist kein rechter Winkel.'
    if lieg:
        r, f = ja, ['Nein, denn C müsste auf der Mittelsenkrechten von [AB] liegen.', 'Das kann man ohne Zeichnung nicht entscheiden.', 'Nein, denn α und β sind verschieden groß.']
    else:
        r, f = nein, ['Ja, denn α + β < 180°.', 'Ja, weil jedes Dreieck einen Umkreis hat.', 'Das kann man ohne Zeichnung nicht entscheiden.']
    return A(R, f'Im Dreieck ABC ist α = {al}° und β = {be}°. Liegt C auf dem Kreis mit dem Durchmesser [AB]?', r, f,
             f'γ = 180° − {al}° − {be}° = {180 - al - be}°. ' + ('Rechter Winkel bei C → C liegt auf dem Thaleskreis.' if lieg else 'Kein rechter Winkel → C liegt nicht darauf.'),
             'Berechne γ. C liegt genau dann auf dem Thaleskreis, wenn γ = 90° ist.')


def g_tangente(R, st):
    phi = R.choice(range(30, 121, 2))
    if st == 1:
        a = Z('Eine Tangente berührt einen Kreis um M im Punkt B. Wie groß ist der Winkel zwischen der Tangente und dem Radius [MB]?', 90, '90',
              'Tangente und Berührradius stehen immer senkrecht aufeinander: 90°.', 'Erinnere dich an die Eigenschaft der Tangente.', '°') if R.random() < .3 else \
            Z(f'Von P aus werden zwei Tangenten an den Kreis um M gelegt; sie bilden den Winkel ∠BPB\' = {phi}°. Wie groß ist ∠BPM?', Fr(phi, 2), f'{phi} / 2',
              f'MP ist Symmetrieachse der Figur, sie halbiert den Winkel: {phi}° : 2 = {zt(Fr(phi, 2))}°.', 'Die Figur ist symmetrisch zur Geraden MP.', '°')
        a['f']['grafik'] = tangenten_bild(phi, (f'{phi}°', '') if 'BPM' in a['f']['text'] else ('', ''))
        if not a['f']['grafik']['winkel'][0][3]: a['f']['grafik']['winkel'] = []
        return a
    if st == 2:
        a = Z(f'Von P aus werden zwei Tangenten an den Kreis um M gelegt, Berührpunkte B und B\'. Es ist ∠BPB\' = {phi}°. Wie groß ist ∠BMB\'?', 180 - phi, f'360 - 90 - 90 - {phi}',
              f'Im Viereck MBPB\' sind die Winkel bei B und B\' je 90°. ∠BMB\' = 360° − 180° − {phi}° = {180 - phi}°.', 'Winkelsumme im Viereck: 360°. Wo sind rechte Winkel?', '°')
        a['f']['grafik'] = tangenten_bild(phi, (f'{phi}°', '?'))
        return a
    if R.random() < .5:
        w = R.choice(range(20, 71, 2))
        a = Z(f'Von P aus berührt eine Tangente den Kreis um M in B. Der Winkel ∠BPM ist {w}°. Wie groß ist ∠BMP?', 90 - w, f'180 - 90 - {w}',
              f'Dreieck MBP hat bei B einen rechten Winkel: ∠BMP = 180° − 90° − {w}° = {90 - w}°.', 'Im Dreieck MBP ist der Winkel bei B ein rechter.', '°')
        a['f']['grafik'] = tangenten_bild(2 * w, ('', ''))
        a['f']['grafik']['winkel'] = []
        return a
    t = R.randint(3, 15)
    return Z(f'Von P aus werden zwei Tangenten an einen Kreis gelegt. Der Abschnitt von P bis zum ersten Berührpunkt ist {t} cm lang. Wie lang ist der Abschnitt bis zum zweiten Berührpunkt?', t, f'{t}',
             f'Die beiden Tangentenabschnitte sind gleich lang (Symmetrie zur Geraden MP): {t} cm.', 'Die Figur ist symmetrisch zur Geraden durch P und M.', 'cm')


def g_umkreis_inkreis(R, st):
    if st == 1:
        bank = [('Welche Linien braucht man, um den Mittelpunkt des Umkreises eines Dreiecks zu konstruieren?', 'die Mittelsenkrechten',
                 ['die Winkelhalbierenden', 'die Höhen', 'die Seitenhalbierenden'], 'Der Umkreismittelpunkt ist von allen Ecken gleich weit entfernt – das liefern die Mittelsenkrechten.'),
                ('Welche Linien braucht man, um den Mittelpunkt des Inkreises eines Dreiecks zu konstruieren?', 'die Winkelhalbierenden',
                 ['die Mittelsenkrechten', 'die Höhen', 'die Seitenhalbierenden'], 'Der Inkreismittelpunkt ist von allen Seiten gleich weit entfernt – das liefern die Winkelhalbierenden.'),
                ('Von welchen Teilen des Dreiecks ist der Umkreismittelpunkt gleich weit entfernt?', 'von den drei Ecken',
                 ['von den drei Seiten', 'von den drei Seitenmitten', 'von keinem Teil'], 'Der Umkreis geht durch alle drei Ecken.'),
                ('Von welchen Teilen des Dreiecks ist der Inkreismittelpunkt gleich weit entfernt?', 'von den drei Seiten',
                 ['von den drei Ecken', 'von den drei Seitenmitten', 'von keinem Teil'], 'Der Inkreis berührt alle drei Seiten.'),
                ('Was macht der Inkreis eines Dreiecks?', 'Er berührt alle drei Seiten von innen.',
                 ['Er geht durch alle drei Ecken.', 'Er schneidet jede Seite zweimal.', 'Er liegt immer außerhalb des Dreiecks.'], 'Die Seiten sind Tangenten des Inkreises.'),
                ('Was macht der Umkreis eines Dreiecks?', 'Er geht durch alle drei Ecken.',
                 ['Er berührt alle drei Seiten von innen.', 'Er geht nur durch zwei Ecken.', 'Er liegt immer innerhalb des Dreiecks.'], 'Alle Ecken sind gleich weit vom Umkreismittelpunkt entfernt.'),
                ('Wo liegt der Umkreismittelpunkt eines rechtwinkligen Dreiecks?', 'in der Mitte der Hypotenuse',
                 ['im rechten Winkel', 'außerhalb des Dreiecks', 'im Inkreismittelpunkt'], 'Nach Thales ist die Hypotenuse Durchmesser des Umkreises.')]
        q, r, f, w = R.choice(bank)
        return A(R, q, r, f, w, 'Gleich weit von den Ecken → Mittelsenkrechten. Gleich weit von den Seiten → Winkelhalbierende.')
    if st == 2:
        al, be = R.randint(20, 100), R.randint(20, 100)
        if R.random() < .3: be = 90 - al if al < 90 else be
        ga = 180 - al - be
        if ga <= 0: return g_umkreis_inkreis(R, st)
        m = max(al, be, ga)
        r = 'innerhalb des Dreiecks' if m < 90 else ('auf der längsten Seite (Mitte der Hypotenuse)' if m == 90 else 'außerhalb des Dreiecks')
        return A(R, f'Ein Dreieck hat α = {al}°, β = {be}°. Wo liegt der Umkreismittelpunkt?', r,
                 [x for x in ['innerhalb des Dreiecks', 'auf der längsten Seite (Mitte der Hypotenuse)', 'außerhalb des Dreiecks'] if x != r] + ['auf der kürzesten Seite'],
                 f'γ = {ga}°. Größter Winkel {m}°: ' + ('spitzwinklig → innen.' if m < 90 else 'rechtwinklig → Thales: Mitte der Hypotenuse.' if m == 90 else 'stumpfwinklig → außen.'),
                 'Bestimme den größten Winkel: spitz, rechter oder stumpf?')
    be, ga = R.choice(range(30, 121, 2)), R.choice(range(30, 121, 2))
    if be + ga >= 170: return g_umkreis_inkreis(R, st)
    return Z(f'In einem Dreieck ABC ist β = {be}° und γ = {ga}°. I ist der Inkreismittelpunkt. Wie groß ist der Winkel ∠BIC?', 180 - Fr(be, 2) - Fr(ga, 2), f'180 - {be} / 2 - {ga} / 2',
             f'BI und CI halbieren β und γ: Dreieck BIC hat die Winkel {zt(Fr(be, 2))}° und {zt(Fr(ga, 2))}°. ∠BIC = 180° − {zt(Fr(be, 2))}° − {zt(Fr(ga, 2))}° = {zt(180 - Fr(be, 2) - Fr(ga, 2))}°.',
             'Der Inkreismittelpunkt liegt auf den Winkelhalbierenden.', '°')


ARTEN = ['Passante', 'Tangente', 'Sekante']


def lage_bild(r, d):
    return figur({'M': [0, 0], '_1': [-r - 2, d], '_2': [r + 2, d], '_F': [0, d]}, linien=[['_1', '_2', 'g'], ['M', '_F', f'd = {zt(d)}', 'gestrichelt']],
                 rechter_winkel=[['_F', 'M', '_2']], kreise=[{'m': 'M', 'r': jw(r)}])


def g_lage(R, st):
    r = Fr(R.randint(2, 9)) if st < 3 else Fr(R.randint(15, 90), 10)
    art = R.choice(ARTEN)
    d = r + R.choice([1, 2, Fr(1, 2)]) if art == 'Passante' else (r if art == 'Tangente' else r - R.choice([1, Fr(1, 2), Fr(3, 2)]))
    if d < 0: d = r / 2
    if st == 1:
        a = A(R, f'Ein Kreis hat den Radius r = {zt(r)} cm. Eine Gerade g hat vom Mittelpunkt den Abstand d = {zt(d)} cm. Wie heißt g?', art, [x for x in ARTEN if x != art] + ['Durchmesser'],
              f'd {">" if d > r else "=" if d == r else "<"} r → {art}.', 'Vergleiche d mit r.')
        a['f']['grafik'] = lage_bild(r, d)
        return a
    if st == 2:
        n = {'Passante': 0, 'Tangente': 1, 'Sekante': 2}[art]
        return Z(f'Ein Kreis hat den Durchmesser {zt(2 * r)} cm. Eine Gerade hat vom Mittelpunkt den Abstand {zt(d)} cm. Wie viele gemeinsame Punkte haben Kreis und Gerade?', n, f'{n}',
                 f'r = {zt(2 * r)} : 2 = {zt(r)} cm. d {">" if d > r else "=" if d == r else "<"} r → {art}, also {n} gemeinsame Punkte.', 'Achtung: Gegeben ist der Durchmesser, nicht der Radius.')
    mx, my, rr = R.randint(-3, 4), R.randint(-3, 4), R.randint(2, 5)
    art = R.choice(ARTEN); senk = R.random() < .5
    abst = rr + R.choice([1, 2]) if art == 'Passante' else rr if art == 'Tangente' else R.randint(0, rr - 1)
    c = (mx if senk else my) + R.choice([1, -1]) * abst
    g = f'x = {zt(c)}' if senk else f'y = {zt(c)}'
    n = {'Passante': 0, 'Tangente': 1, 'Sekante': 2}[art]
    w = f'Abstand von M zur Geraden {g}: |{zt(c)} − {kl(mx if senk else my)}| = {abst}. ' + f'd {">" if abst > rr else "=" if abst == rr else "<"} r = {rr} → {art}.'
    if R.random() < .5:
        a = A(R, f'Ein Kreis hat den Mittelpunkt M({zt(mx)} | {zt(my)}) und den Radius r = {rr}. Welche Lage hat die Gerade {g}?', art, [x for x in ARTEN if x != art] + ['Durchmesser'], w,
              f'Die Gerade {g} ist {"senkrecht" if senk else "waagrecht"}. Wie weit ist sie von M entfernt? Vergleiche mit r.')
    else:
        a = Z(f'Ein Kreis hat den Mittelpunkt M({zt(mx)} | {zt(my)}) und den Radius r = {rr}. Wie viele gemeinsame Punkte haben der Kreis und die Gerade {g}?', n, f'{n}', w,
              f'Die Gerade {g} ist {"senkrecht" if senk else "waagrecht"}. Wie weit ist sie von M entfernt? Vergleiche mit r.')
    e1, e2 = ([c, my - rr - 2], [c, my + rr + 2]) if senk else ([mx - rr - 2, c], [mx + rr + 2, c])
    a['f']['grafik'] = figur({'M': [mx, my], '_1': e1, '_2': e2}, linien=[['_1', '_2', g]], kreise=[{'m': 'M', 'r': rr}])
    return a


def cz_(x):
    x = Fr(x)
    return str(x.numerator) if x.denominator == 1 else f'{x.numerator} / {x.denominator}'


THALES_BEWEIS = [  # (Schritt, Begründung)
    ('MA = MB = MC.', 'A, B und C liegen auf dem Kreis um M; die Strecken sind Radien.'),
    ('Die Dreiecke AMC und BMC sind gleichschenklig.', 'Je zwei ihrer Seiten sind gleich lang (Schritt 1).'),
    ('∠ACM = α und ∠BCM = β.', 'Basiswinkel im gleichschenkligen Dreieck sind gleich groß.'),
    ('γ = α + β.', 'Die Strecke [MC] teilt den Winkel γ in die beiden Teilwinkel.'),
    ('α + β + γ = 180°, also 2γ = 180° und γ = 90°.', 'Winkelsumme im Dreieck ABC; α + β wird durch γ ersetzt.'),
]
TANGENTE_BEWEIS = [
    ('Zeichne den Thaleskreis über [MP]. Er schneidet den Kreis um M in B.', 'Konstruktionsschritt (keine Begründung nötig).'),
    ('Der Winkel ∠MBP ist 90°.', 'B liegt auf dem Thaleskreis über [MP] (Satz des Thales).'),
    ('[PB] steht senkrecht auf dem Radius [MB].', 'Das folgt direkt aus Schritt 2: Der Winkel bei B ist ein rechter.'),
    ('Also ist die Gerade PB eine Tangente an den Kreis.', 'Tangente und Berührradius stehen senkrecht aufeinander (und umgekehrt).'),
]
FALSCH_GRUND = ['Stufenwinkel an Parallelen sind gleich groß.', 'Scheitelwinkel sind gleich groß.', 'Nebenwinkel ergänzen sich zu 180°.',
                'Weil man es in der Zeichnung messen kann.', 'Die Diagonalen eines Rechtecks sind gleich lang.']


def _beweis_liste(schritte, mark=None):
    return ' '.join(f'({i + 1}) {t}' + (' ◀' if i == mark else '') for i, (t, _) in enumerate(schritte))


def _beweis_begruenden(R):
    welcher, k = zyklus('bwk', [('t', 2), ('g', 1), ('t', 0), ('g', 3), ('t', 3), ('g', 2), ('t', 1), ('t', 4)])
    if welcher == 't':
        name, B = 'Beweis des Thalessatzes', THALES_BEWEIS
        frage = f'Welche Begründung gehört zu Schritt ({k + 1})?'
    else:
        name, B = 'Begründung der Tangentenkonstruktion von P aus', TANGENTE_BEWEIS
        frage = 'Welcher bekannte Satz wird bei Schritt (4) benutzt?' if k == 3 else f'Welche Begründung gehört zu Schritt ({k + 1})?'
    grund = B[k][1]
    spaeter = [g for j, (_, g) in enumerate(B) if j > k + 1]
    f = R.sample(FALSCH_GRUND, 3 - min(len(spaeter), 1)) + spaeter[:1]
    return A(R, f'{name}: {_beweis_liste(B, k)} {frage}', grund, f, f'Schritt ({k + 1}): {B[k][0]} Begründung: {grund}',
             'Welche bekannte Eigenschaft rechtfertigt genau diesen Schritt – nicht einen früheren oder späteren?')


def _beweis_ordnen(R):
    if R.random() < .6:
        kaert = [('γ = 90°', 3), ('Die Dreiecke AMC und BMC sind gleichschenklig, weil MA = MB = MC.', 0), ('α + β + (α + β) = 180°', 2),
                 ('∠ACM = α und ∠BCM = β (Basiswinkel)', 1)]
        name = 'Beweis des Thalessatzes'
    else:
        kaert = [('PB ist Tangente.', 2), ('Der Winkel bei B ist 90°.', 1), ('B liegt auf dem Thaleskreis über [MP].', 0)]
        name = 'Tangente von P aus'
    R.shuffle(kaert)
    n = len(kaert)
    reihe = [None] * n
    for nr, (_, pos) in enumerate(kaert): reihe[pos] = nr + 1
    text = f'{name}: Bringe die Kärtchen in die richtige Reihenfolge. ' + ' '.join(f'Kärtchen {i + 1}: „{t}“' for i, (t, _) in enumerate(kaert))
    schab = '; '.join(f'{i + 1}. Schritt: □' for i in range(n))
    return L(text, schab, reihe, [str(v) for v in reihe], 'Richtige Reihenfolge: ' + ' → '.join(f'„{kaert[v - 1][0]}“' for v in reihe) + '.',
             'Womit fängt der Beweis an? Was folgt woraus?', 'Trage in jedes Feld die Nummer des Kärtchens ein.')


def g_beweis(R, st):
    if st == 3:
        return _beweis_ordnen(R) if zyklus('bw3', [1, 0]) else _beweis_begruenden(R)
    if st == 2 and R.random() < .5:
        return _beweis_begruenden(R)
    al = [('Eine Behauptung, die in vielen gemessenen Beispielen stimmt, ist damit bewiesen.', False), ('Ein einziges Gegenbeispiel widerlegt eine Vermutung.', True),
          ('Mit Geometriesoftware kann man Vermutungen finden, ein Beweis braucht Begründungen.', True), ('Ein Beweis gilt für alle Fälle, nicht nur für gezeichnete.', True),
          ('Wenn eine Messung 89,8° ergibt, ist der Satz des Thales widerlegt.', False), ('Ein Beweis darf sich auf schon bewiesene Sätze stützen.', True),
          ('Wenn der Satz des Thales gilt, gilt automatisch jede Umkehrung.', False), ('Eine Zeichnung allein ist ein Beweis.', False)]
    wahr = [t for t, w in al if w]; falsch = [t for t, w in al if not w]
    if st == 1 or R.random() < .5:
        t = R.choice(wahr)
        return A(R, 'Welche Aussage über Vermutung und Beweis ist richtig?', t, R.sample(falsch, 3), f'Richtig: {t}', 'Was unterscheidet Messen von Begründen?')
    t = R.choice(falsch)
    return A(R, 'Welche Aussage über Vermutung und Beweis ist falsch?', t, R.sample(wahr, 3), f'Falsch: {t} Messungen sind ungenau und decken nie alle Fälle ab.',
             'Was unterscheidet Messen von Begründen?')


GEN = {'thales': g_thales, 'umkehrung': g_umkehrung, 'tangente': g_tangente, 'umkreis_inkreis': g_umkreis_inkreis, 'lage': g_lage, 'beweis': g_beweis}

# Verständliche Fassung (Runde 7, Maßstab inhalte/README.md „Verständliche Erklärungen“):
# Alltagssituation zuerst (einstieg), jedes neue Wort erklärt (woerter), Beispiel in kleinen Schritten, Merksatz am Ende (regel).
# Situationen: Freilichtbühne, Geodreieck zwischen zwei Nägeln, Messen mit einem Geometrieprogramm, Ball und Pfütze, Fahrrad auf der Straße, Treffpunkt dreier Freunde.
KLAR = {
 'thales': {
  'einstieg': 'Eine Freilichtbühne hat vorne eine gerade Bühnenkante. Die Zuschauerplätze stehen auf einem Halbkreis, dessen Durchmesser genau diese Kante ist. Von jedem dieser Plätze aus sieht man die beiden Enden der Bühne unter demselben Winkel: genau 90°. Der Überlieferung nach kannte das schon der griechische Mathematiker Thales – darum heißt es ⟦Satz des Thales⟧.',
  'woerter': [['Kreis mit Mittelpunkt M', 'alle Punkte, die vom Mittelpunkt M gleich weit entfernt sind'], ['Radius r', 'der Abstand vom Mittelpunkt bis zum Kreisrand'],
              ['Durchmesser', 'Strecke durch den Mittelpunkt von Rand zu Rand; doppelt so lang wie der Radius'],
              ['Sehne', 'Strecke zwischen zwei Punkten auf dem Kreis; der Durchmesser ist die längste Sehne'],
              ['rechter Winkel', 'ein Winkel von 90°, wie eine Zimmerecke'], ['Thaleskreis', 'der Kreis über einer Strecke [AB], bei dem [AB] der Durchmesser ist']],
  'schritte': ['[AB] ist ein Durchmesser des Kreises, C liegt auf dem Kreis. Bei A ist α = 35°.',
               'Nach dem Satz des Thales hat das Dreieck bei C einen rechten Winkel: γ = 90°.',
               'Die drei Winkel ergeben zusammen 180°. Also ist β = 180° − 90° − 35°.',
               'Ausrechnen: ⟦β = 55°⟧.'],
  'regel': 'So nutzt du den ⟦Satz des Thales⟧: Liegt C auf einem Kreis und ist [AB] ein ⟦Durchmesser⟧, dann hat das Dreieck ABC bei C einen ⟦rechten Winkel⟧. Den Kreis nennt man ⟦Thaleskreis⟧.',
  'fehler': 'Ist [AB] nur eine Sehne und ⟦kein Durchmesser⟧, gilt der Satz nicht – γ ist dann im Allgemeinen kein rechter Winkel. Bei der Bühne hieße das: Die Plätze stehen auf einem Bogen, dessen Durchmesser nicht die Bühnenkante ist, und man sieht die Bühne unter einem anderen Winkel.'},
 'umkehrung': {
  'einstieg': 'Leg ein Geodreieck mit der rechtwinkligen Ecke nach oben so zwischen zwei Nägel, dass jede der beiden kurzen Kanten an einem Nagel anliegt. Schiebst du es hin und her, wandert die Ecke auf einem Halbkreis. Dass ein Punkt mit rechtem Winkel immer auf so einem Kreis liegt, ist die ⟦Umkehrung des Satzes des Thales⟧.',
  'woerter': [['Umkehrung', 'der Satz andersherum: aus dem rechten Winkel folgt, dass C auf dem Kreis liegt'], ['∠ACB', 'der Winkel bei C zwischen den Seiten zu A und zu B'],
              ['Hypotenuse', 'im rechtwinkligen Dreieck die längste Seite; sie liegt dem rechten Winkel gegenüber'], ['A(−2 | 1)', 'Punkt A mit x-Koordinate −2 und y-Koordinate 1']],
  'schritte': ['Gegeben sind A(−2 | 1) und B(6 | 1), und bei C ist ein rechter Winkel: ∠ACB = 90°.',
               'Nach der Umkehrung liegt C auf dem Kreis mit dem Durchmesser [AB]. Sein Mittelpunkt ist die Mitte von [AB].',
               'Die Mitte findest du, indem du die beiden x-Werte addierst und halbierst: (−2 + 6) : 2 = 2. Der y-Wert bleibt 1, also M(2 | 1).',
               '[AB] reicht von x = −2 bis x = 6 und ist damit 8 lang. Der Radius ist die Hälfte: ⟦r = 4⟧.'],
  'regel': 'So findest du den Kreis zu einem rechten Winkel: Hat das Dreieck ABC bei C einen ⟦rechten Winkel⟧, dann liegt C auf dem Kreis mit dem ⟦Durchmesser [AB]⟧. Der Mittelpunkt ist die ⟦Mitte von [AB]⟧, der Radius die halbe Länge von [AB].',
  'fehler': 'Der Mittelpunkt des Thaleskreises ist nicht C, sondern die ⟦Mitte der Hypotenuse⟧ [AB]. Beim Geodreieck zwischen den Nägeln sieht man es: Die Ecke wandert, der Mittelpunkt bleibt fest genau zwischen den beiden Nägeln.'},
 'beweis': {
  'einstieg': 'Miss mit einem Geometrieprogramm zehn verschiedene Dreiecke auf dem Halbkreis: Jedes Mal zeigt es bei C 90°. Das ist ein guter Hinweis, aber noch keine Sicherheit – vielleicht gibt es ein Dreieck, das du nicht gemessen hast. Eine Begründung, die für alle Fälle gleichzeitig gilt, heißt ⟦Beweis⟧.',
  'woerter': [['Vermutung', 'eine Aussage, die nach Beispielen stimmt, aber noch nicht begründet ist'], ['Beweis', 'eine Begründung aus bekannten Regeln, die für alle Fälle gilt'],
              ['gleichschenkliges Dreieck', 'Dreieck mit zwei gleich langen Seiten; die Winkel an der dritten Seite sind gleich groß'],
              ['MA = MC', 'die Strecken von M nach A und von M nach C sind gleich lang (beides Radien)'], ['Winkelsumme', 'die drei Winkel eines Dreiecks ergeben zusammen 180°'], ['∠ACM', 'der Winkel bei C zwischen den Strecken zu A und zu M']],
  'schritte': ['M ist der Mittelpunkt des Kreises. MA, MB und MC sind Radien, also gleich lang.',
               'Darum ist das Dreieck AMC gleichschenklig: Der Winkel ∠ACM ist so groß wie α. Genauso ist im Dreieck BMC der Winkel ∠BCM so groß wie β.',
               'Der ganze Winkel bei C besteht aus diesen beiden Teilen: γ = α + β.',
               'Winkelsumme im Dreieck ABC: α + β + γ = 180°, also γ + γ = 180°. Damit ist ⟦γ = 90°⟧.'],
  'regel': 'So unterscheidest du: Messungen führen zu ⟦Vermutungen⟧. Ein ⟦Beweis⟧ zeigt mit Begründungen, dass eine Aussage ⟦immer⟧ gilt. Beim Thalessatz liefern die gleich langen Radien zwei ⟦gleichschenklige Dreiecke⟧ – daraus folgt γ = 90°.',
  'fehler': 'Hundert gemessene Beispiele mit 90° sind ⟦kein Beweis⟧. Sie zeigen nur, dass die Aussage für diese hundert Dreiecke stimmt – so wie hundert weiße Schwäne nicht beweisen, dass alle Schwäne weiß sind.'},
 'lage': {
  'einstieg': 'Ein Ball rollt geradeaus an einer runden Pfütze vorbei. Er kann sie verfehlen, sie gerade so am Rand streifen oder mitten hindurchrollen. Bei einem Kreis und einer Geraden gibt es genau diese drei Möglichkeiten. Sie heißen ⟦Passante⟧, ⟦Tangente⟧ und ⟦Sekante⟧.',
  'woerter': [['Abstand d', 'die kürzeste Entfernung vom Mittelpunkt M zur Geraden, senkrecht gemessen'], ['Passante', 'Gerade, die am Kreis vorbeigeht (kein gemeinsamer Punkt)'],
              ['Tangente', 'Gerade, die den Kreis in genau einem Punkt berührt'], ['Sekante', 'Gerade, die den Kreis in zwei Punkten schneidet'],
              ['d > r, d = r, d < r', 'd größer als r, d gleich r, d kleiner als r']],
  'schritte': ['Der Kreis hat den Radius r = 4 cm. Die Gerade ist vom Mittelpunkt d = 3 cm entfernt.',
               'Vergleiche d mit r: 3 cm ist kleiner als 4 cm.',
               'Die Gerade kommt dem Mittelpunkt also näher als der Kreisrand. Sie muss durch den Kreis hindurchgehen.',
               'Sie schneidet den Kreis zweimal und ist eine ⟦Sekante⟧.'],
  'regel': 'So bestimmst du die Lage: Vergleiche den Abstand d der Geraden vom Mittelpunkt mit dem Radius r. ⟦d > r⟧: Passante (kein Punkt). ⟦d = r⟧: Tangente (ein Punkt). ⟦d < r⟧: Sekante (zwei Punkte).',
  'fehler': 'Eine Gerade mit d = r schneidet den Kreis nicht zweimal. Sie ⟦berührt⟧ ihn nur in einem Punkt – wie der Ball, der die Pfütze gerade so am Rand streift.'},
 'tangente': {
  'einstieg': 'Ein Fahrrad steht auf der Straße. Das Rad ist ein Kreis, die Straße eine Gerade, die es genau an einer Stelle berührt. Die Speiche, die von der Nabe senkrecht nach unten zu dieser Stelle zeigt, steht im rechten Winkel auf der Straße. So eine Berührgerade heißt ⟦Tangente⟧.',
  'woerter': [['Berührpunkt B', 'die einzige Stelle, an der Tangente und Kreis sich treffen'], ['Berührradius [MB]', 'der Radius vom Mittelpunkt zum Berührpunkt – wie die senkrechte Speiche'],
              ['φ', 'Phi, griechischer Buchstabe als Name für einen Winkel'], ["B'", 'ein zweiter Berührpunkt']],
  'schritte': ["Von einem Punkt P außerhalb des Kreises gehen zwei Tangenten aus. Sie berühren den Kreis in B und B' und bilden bei P den Winkel φ = 50°.",
               "Betrachte das Viereck MBPB'. Bei B und bei B' steht die Tangente senkrecht auf dem Radius: Das sind zwei rechte Winkel.",
               'Die Winkel im Viereck ergeben zusammen 360°. Für den Winkel bei M bleibt: 360° − 90° − 90° − 50°.',
               "Ausrechnen: ∠BMB' = ⟦130°⟧."],
  'regel': 'So nutzt du Tangenten: Eine ⟦Tangente⟧ berührt den Kreis in genau einem Punkt B und steht ⟦senkrecht⟧ auf dem Berührradius [MB]. Von einem Punkt P außerhalb gibt es ⟦zwei⟧ Tangenten; von P bis zu den Berührpunkten sind sie gleich lang.',
  'fehler': 'Der Winkel zwischen Tangente und Berührradius ist nicht irgendein spitzer Winkel: Er ist ⟦immer 90°⟧ – genau wie bei der Speiche, die senkrecht auf die Straße zeigt.'},
 'umkreis_inkreis': {
  'einstieg': 'Drei Freunde wohnen an drei verschiedenen Orten und suchen einen Treffpunkt, der von allen drei Häusern gleich weit entfernt ist. Zeichnet man um diesen Treffpunkt einen Kreis, geht er durch alle drei Häuser. Der Kreis durch die drei Ecken eines Dreiecks heißt ⟦Umkreis⟧.',
  'woerter': [['Umkreis', 'Kreis, der durch alle drei Ecken des Dreiecks geht'],
              ['Mittelsenkrechte', 'Gerade, die eine Seite in ihrer Mitte senkrecht schneidet; jeder ihrer Punkte ist von beiden Enden der Seite gleich weit weg'],
              ['Inkreis', 'Kreis innen im Dreieck, der alle drei Seiten berührt'],
              ['Winkelhalbierende', 'Gerade, die einen Winkel in zwei gleich große Hälften teilt; jeder ihrer Punkte ist von beiden Schenkeln gleich weit weg'],
              ['Schnittpunkt', 'der Punkt, in dem sich Linien treffen']],
  'schritte': ['Das Dreieck hat bei C einen rechten Winkel: γ = 90°.',
               'Nach dem Satz des Thales liegt C dann auf dem Kreis mit dem Durchmesser [AB]. A und B liegen ohnehin darauf.',
               'Dieser Kreis geht also durch alle drei Ecken: Er ist der Umkreis.',
               'Sein Mittelpunkt ist die ⟦Mitte der Seite [AB]⟧. Mittelsenkrechten muss man hier nicht zeichnen.'],
  'regel': 'So findest du die Mittelpunkte: Den ⟦Umkreismittelpunkt⟧ liefert der Schnittpunkt der ⟦Mittelsenkrechten⟧ – er ist von allen Ecken gleich weit weg. Den ⟦Inkreismittelpunkt⟧ liefert der Schnittpunkt der ⟦Winkelhalbierenden⟧ – er ist von allen Seiten gleich weit weg.',
  'fehler': 'Der Inkreismittelpunkt entsteht nicht aus den Mittelsenkrechten. Er muss von den ⟦Seiten⟧ gleich weit weg sein, nicht von den Ecken – dafür braucht man die ⟦Winkelhalbierenden⟧. Beim Treffpunkt der Freunde zählen die Häuser (Ecken), beim Inkreis wären es drei gerade Zäune (Seiten).'},
}
for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl7.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl7 import mit_umbau  # noqa: E402

_TH = {'A': [-3, 0], 'B': [3, 0], 'C': [1.03, 2.82], 'M': [0, 0]}


def _beweis(mc=False, winkel=False):
    li = [['A', 'B'], ['B', 'C'], ['C', 'A']] + ([['M', 'C', 'Radius', 'gestrichelt']] if mc else [])
    w = [['A', 'B', 'C', 'α'], ['C', 'A', 'M', 'α'], ['B', 'C', 'A', 'β'], ['C', 'M', 'B', 'β']] if winkel else None
    return figur(_TH, linien=li, winkel=w, kreise=[{'m': 'M', 'r': 3}])


def _lage(abstand=None, punkte=False, hoehe=3):
    pk = {'M': [0, 0], '_1': [-5, hoehe], '_2': [5, hoehe], '_F': [0, hoehe]}
    li = [['_1', '_2', 'g']]
    if abstand: li.append(['M', '_F', abstand, 'gestrichelt'])
    if punkte: pk.update({'P': [-2.65, 3], 'Q': [2.65, 3]})
    return figur(pk, linien=li, kreise=[{'m': 'M', 'r': 4}])


_TG = {'M': [0, 0], 'P': [4.73, 0], 'B': [0.85, 1.81], "B'": [0.85, -1.81]}


def _tangente(rechte=False, m=False):
    return figur(_TG, linien=[['P', 'B'], ['P', "B'"], ['M', 'B', 'r'], ['M', "B'", 'r'], ['M', 'P', '', 'gestrichelt']],
                 rechter_winkel=[['B', 'M', 'P'], ["B'", 'M', 'P']] if rechte else None,
                 winkel=[['P', 'B', "B'", '50°']] + ([['M', "B'", 'B', '130°']] if m else []), kreise=[{'m': 'M', 'r': 2}])


def _pt(x, y, n): return {'x': x, 'y': y, 'name': n}


_ABC = [_pt(0, 0, 'A'), _pt(6, 0, 'B'), _pt(2, 4, 'C')]
_ABC_S = [[0, 0, 6, 0], [6, 0, 2, 4], [2, 4, 0, 0]]

UMBAU = {
 'thales': {
  'einstieg': 'Auf einer Freilichtbühne stehen die Plätze auf einem Halbkreis vor der Bühnenkante. Von jedem Platz sieht man die Kante unter genau 90°. Das ist der ⟦Satz des Thales⟧.',
  'woerter': [['Durchmesser', 'Strecke durch den Mittelpunkt von Rand zu Rand'], ['rechter Winkel', '90°, wie eine Zimmerecke'],
              ['Thaleskreis', 'Kreis, bei dem [AB] der Durchmesser ist']],
  'bild': thales_bild(35, ('35°', '', '')),
  'schritte': [{'text': '[AB] ist ein Durchmesser, C liegt auf dem Kreis. Bei A sind es 35°.'},
               {'text': 'C liegt auf dem Thaleskreis. Darum ist bei C ein rechter Winkel.', 'bild': thales_bild(35, ('35°', '', '90°'))},
               {'text': 'Also ist β = 180° − 90° − 35° = ⟦55°⟧.', 'bild': thales_bild(35, ('35°', '55°', '90°'))}],
  'fehler': 'Geht [AB] nicht durch den Mittelpunkt, gilt der Satz nicht. Der Winkel bei C ist dann meist ⟦kein rechter⟧.',
  'fehler_bild': figur({'A': [-2.82, -1.03], 'B': [2.82, -1.03], 'C': [0, 3], 'M': [0, 0]}, linien=[['A', 'B'], ['B', 'C'], ['C', 'A']],
                       winkel=[['C', 'A', 'B', '?']], kreise=[{'m': 'M', 'r': 3}]),
  'regel': 'C auf dem Thaleskreis über [AB]: Bei C ist ein ⟦rechter Winkel⟧. [AB] muss ein Durchmesser sein.'},
 'umkehrung': {
  'einstieg': 'Leg ein Geodreieck zwischen zwei Nägel. Jede kurze Kante berührt einen Nagel. Schiebst du es, wandert die rechtwinklige Ecke auf einem Halbkreis. Das ist die ⟦Umkehrung⟧ des Thalessatzes.',
  'woerter': [['Umkehrung', 'der Satz andersherum: rechter Winkel bei C, also liegt C auf dem Kreis'], ['Mittelpunkt M', 'die Mitte von [AB]'],
              ['Radius r', 'Abstand vom Mittelpunkt zum Kreis']],
  'bild': {'typ': 'koordinaten', 'x': [-3, 7], 'y': [-4, 6], 'punkte': [_pt(-2, 1, 'A'), _pt(6, 1, 'B'), _pt(2, 5, 'C')], 'strecken': [[-2, 1, 6, 1], [-2, 1, 2, 5], [6, 1, 2, 5]]},
  'schritte': [{'text': 'Gegeben sind A(−2 | 1) und B(6 | 1). Bei C ist ein rechter Winkel.'},
               {'text': 'Der Mittelpunkt M ist die Mitte von [AB]: M(2 | 1).', 'bild': {'punkte': [_pt(-2, 1, 'A'), _pt(6, 1, 'B'), _pt(2, 5, 'C'), _pt(2, 1, 'M')]}},
               {'text': '[AB] ist 8 lang, also ist der Radius r = ⟦4⟧.', 'bild': {'kreise': [{'m': [2, 1], 'r': 4}]}},
               {'text': 'C liegt genau auf diesem Kreis.'}],
  'fehler': 'Der Mittelpunkt ist nicht C, sondern die ⟦Mitte von [AB]⟧. Beim Geodreieck wandert die Ecke, die Mitte zwischen den Nägeln bleibt.',
  'regel': 'Rechter Winkel bei C: C liegt auf dem ⟦Kreis über [AB]⟧. Sein Mittelpunkt ist die Mitte von [AB].'},
 'beweis': {
  'einstieg': 'Ein Geometrieprogramm misst bei zehn Dreiecken auf dem Halbkreis jedes Mal 90°. Aber gilt das wirklich immer? Eine Begründung für alle Fälle heißt ⟦Beweis⟧.',
  'woerter': [['Beweis', 'Begründung aus bekannten Regeln, die für alle Fälle gilt'], ['Radius', 'Strecke vom Mittelpunkt zum Kreis; alle Radien sind gleich lang'],
              ['gleichschenklig', 'zwei gleich lange Seiten, deshalb zwei gleich große Winkel']],
  'bild': _beweis(),
  'schritte': [{'text': 'MA, MB und MC sind jeweils ein Radius, also gleich lang.', 'bild': _beweis(mc=True)},
               {'text': 'Die Dreiecke AMC und BMC sind gleichschenklig. Bei C stecken α und β.', 'bild': _beweis(mc=True, winkel=True)},
               {'text': 'Der ganze Winkel bei C ist also α + β.'},
               {'text': 'Winkelsumme im Dreieck ABC: α + β + (α + β) = 180°.'},
               {'text': 'Also 2 · (α + β) = 180° und ⟦α + β = 90°⟧.'}],
  'fehler': 'Hundert gemessene Beispiele sind ⟦kein Beweis⟧. Sie zeigen nur, dass es für diese hundert Dreiecke stimmt.',
  'regel': 'Messen liefert eine Vermutung, erst der ⟦Beweis⟧ zeigt: immer. Beim Thalessatz helfen die gleich langen Radien.'},
 'lage': {
  'einstieg': 'Ein Ball rollt geradeaus an einer runden Pfütze vorbei. Er kann sie verfehlen, am Rand streifen oder durchrollen. Die drei Fälle heißen Passante, Tangente und ⟦Sekante⟧.',
  'woerter': [['Passante', 'geht vorbei, kein gemeinsamer Punkt'], ['Tangente', 'berührt den Kreis in genau einem Punkt'], ['Sekante', 'schneidet den Kreis in zwei Punkten']],
  'bild': _lage(),
  'schritte': [{'text': 'Der Radius ist 4 cm, der Abstand der Geraden von M ist 3 cm.', 'bild': _lage('d = 3')},
               {'text': '3 cm ist kleiner als 4 cm. Die Gerade kommt näher als der Rand.'},
               {'text': 'Sie schneidet den Kreis zweimal: ⟦Sekante⟧.', 'bild': _lage('d = 3', punkte=True)}],
  'fehler': 'Ist der Abstand gleich dem Radius, schneidet die Gerade nicht zweimal. Sie ⟦berührt⟧ nur – wie ein Ball am Pfützenrand.',
  'fehler_bild': _lage('d = 4', hoehe=4),
  'regel': 'Vergleiche den ⟦Abstand mit dem Radius⟧. Größer: Passante, gleich: Tangente, kleiner: Sekante.'},
 'tangente': {
  'einstieg': 'Ein Fahrrad steht auf der Straße. Das Rad berührt sie an genau einer Stelle. Die Speiche zu dieser Stelle steht senkrecht auf der Straße. Die Straße ist eine ⟦Tangente⟧.',
  'woerter': [['Berührpunkt', 'die eine Stelle, an der Tangente und Kreis sich treffen'], ['Berührradius', 'der Radius zum Berührpunkt – wie die Speiche']],
  'bild': _tangente(),
  'schritte': [{'text': 'Von P gehen zwei Tangenten aus. Bei P ist der Winkel 50°.'},
               {'text': "In jedem Berührpunkt steht der Berührradius senkrecht: zweimal 90°.", 'bild': _tangente(rechte=True)},
               {'text': 'Im Viereck sind es zusammen 360°: 360° − 90° − 90° − 50° = ⟦130°⟧.', 'bild': _tangente(rechte=True, m=True)}],
  'fehler': 'Der Winkel zwischen Tangente und Berührradius ist nicht irgendein Winkel. Er ist ⟦immer 90°⟧, wie bei der senkrechten Speiche.',
  'regel': 'Tangente und Berührradius bilden ⟦immer 90°⟧. Von einem Punkt außen gibt es zwei Tangenten.'},
 'umkreis_inkreis': {
  'einstieg': 'Drei Freunde suchen einen Treffpunkt, der von allen drei Häusern gleich weit weg ist. Ein Kreis um diesen Punkt geht durch alle drei Häuser. Er heißt ⟦Umkreis⟧.',
  'woerter': [['Umkreis', 'Kreis durch alle drei Ecken'], ['Mittelsenkrechte', 'Gerade, die eine Seite in der Mitte senkrecht schneidet']],
  'bild': {'typ': 'koordinaten', 'x': [-2, 7], 'y': [-3, 5], 'punkte': _ABC, 'strecken': _ABC_S},
  'schritte': [{'text': 'Die Häuser sind A, B und C. Gesucht ist ein Punkt, gleich weit von allen.'},
               {'text': 'Auf der Mittelsenkrechten von [AB] ist man A und B gleich nah.', 'bild': {'strecken': _ABC_S + [[3, -2.5, 3, 4.5, 'gestrichelt']]}},
               {'text': 'Die Mittelsenkrechte von [AC] trifft sie im Punkt ⟦M(3 | 1)⟧.',
                'bild': {'strecken': _ABC_S + [[3, -2.5, 3, 4.5, 'gestrichelt'], [-1, 3, 5, 0, 'gestrichelt']], 'punkte': _ABC + [_pt(3, 1, 'M')]}},
               {'text': 'Der Kreis um M durch A geht auch durch B und C: der Umkreis.', 'bild': {'kreise': [{'m': [3, 1], 'r': 3.162}]}}],
  'fehler': 'Der Inkreis (Kreis innen, berührt alle Seiten) braucht gleichen Abstand zu den Seiten. Dafür nimmt man die ⟦Winkelhalbierenden⟧, nicht die Mittelsenkrechten.',
  'regel': 'Umkreismittelpunkt: Schnitt der ⟦Mittelsenkrechten⟧. Inkreismittelpunkt: Schnitt der Winkelhalbierenden.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Satz des Thales', ['thales', 'umkehrung', 'beweis']), ('Tangenten', ['lage', 'tangente']), ('Besondere Kreise', ['umkreis_inkreis'])],
         'Den Satz des Thales und seine Umkehrung anwenden und begründen, Tangenten und ihre Eigenschaften nutzen, Umkreis und Inkreis von Dreiecken bestimmen.',
         ['Thales: C auf dem Kreis über dem Durchmesser [AB] ⇔ γ = 90°.', 'Tangente ⊥ Berührradius. Von außen: zwei gleich lange Tangentenabschnitte.',
          'Umkreis: Mittelsenkrechten. Inkreis: Winkelhalbierende.', 'Passante d > r, Tangente d = r, Sekante d < r.'],
         offen=['Die Konstruktion der Tangente von einem äußeren Punkt (Thaleskreis über [MP]) wird nur begründet (Lernkarte „beweis“), nicht vom Kind gezeichnet – Zeichnen durch das Kind kann die App nicht.',
                'Experimentieren mit dynamischer Geometriesoftware (Lehrplan) ist in der App nicht möglich.',
                'Kreiswinkel (Umfangs-/Mittelpunktswinkelsatz) aus dem Feld „umfang“ weggelassen: nicht im lehrplan_gym für Klasse 7; nur der Spezialfall am Thaleskreis kommt vor.'])
