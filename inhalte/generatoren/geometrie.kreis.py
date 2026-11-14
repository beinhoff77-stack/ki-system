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
    """Thaleskreis: AB Durchmesser (r = 3), C auf dem Kreis mit ∠CAB = α (Mittelpunktswinkel 2α)."""
    phi = math.radians(180 - 2 * al)
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
     'bild': thales_bild(35, ('35°', 'β', '90°')),
     '_verbot': ['α = 35°']},
    {'lernziel': 'umkehrung', 'titel': 'Umkehrung: Wo liegt der Thaleskreis?',
     'regel': '⟦Umkehrung⟧: Hat das Dreieck ABC bei C einen rechten Winkel, dann liegt C auf dem Kreis mit dem ⟦Durchmesser [AB]⟧. Sein Mittelpunkt ist die ⟦Mitte von [AB]⟧, sein Radius die halbe Länge von [AB].',
     'schritte': ['A(−2 | 1), B(6 | 1), ∠ACB = 90°', 'Mitte von [AB]: M((−2 + 6) : 2 | 1) = M(2 | 1)', 'Radius: 8 : 2 = ⟦4⟧. C liegt auf dem Kreis um M(2 | 1) mit r = 4.'],
     'fehler': 'Der Mittelpunkt des Thaleskreises ist nicht C, sondern die ⟦Mitte der Hypotenuse⟧ [AB] – der Seite gegenüber dem rechten Winkel.',
     'bild': ksys([(-2, 1, 'A'), (6, 1, 'B'), (2, 1, 'M'), (2, 5, 'C')], strecken=[(-2, 1, 6, 1), (-2, 1, 2, 5), (6, 1, 2, 5)]),
     '_verbot': ['A(−2 | 1), B(6 | 1)']},
    {'lernziel': 'tangente', 'titel': 'Tangenten und Berührradius',
     'regel': 'Eine ⟦Tangente⟧ berührt den Kreis in genau einem Punkt B. Sie steht ⟦senkrecht⟧ auf dem Berührradius [MB]. Von einem Punkt P außerhalb gibt es ⟦zwei⟧ Tangenten; sie sind von P bis zum Berührpunkt gleich lang.',
     'schritte': ['Die Tangenten von P bilden den Winkel φ = 50°.', 'Viereck MBPB\': zwei rechte Winkel bei B und B\', Winkelsumme 360°.', '∠BMB\' = 360° − 90° − 90° − 50° = ⟦130°⟧'],
     'fehler': 'Der Winkel zwischen Tangente und Berührradius ist nicht „irgendein spitzer Winkel“: Er ist ⟦immer 90°⟧.',
     'bild': tangenten_bild(50, ('50°', '?')),
     '_verbot': ['φ = 50°']},
    {'lernziel': 'umkreis_inkreis', 'titel': 'Umkreis und Inkreis',
     'regel': 'Der ⟦Umkreismittelpunkt⟧ ist der Schnittpunkt der ⟦Mittelsenkrechten⟧ (gleich weit von allen Ecken). Der ⟦Inkreismittelpunkt⟧ ist der Schnittpunkt der ⟦Winkelhalbierenden⟧ (gleich weit von allen Seiten).',
     'schritte': ['Dreieck mit γ = 90°', 'Nach Thales liegt C auf dem Kreis mit Durchmesser [AB].', 'Der Umkreismittelpunkt ist die ⟦Mitte der Seite [AB]⟧.'],
     'fehler': 'Der Inkreismittelpunkt entsteht nicht aus den Mittelsenkrechten: Er muss von den ⟦Seiten⟧ gleich weit weg sein – dafür braucht man die ⟦Winkelhalbierenden⟧.'},
    {'lernziel': 'lage', 'titel': 'Passante, Tangente oder Sekante?',
     'regel': 'Vergleiche den Abstand d der Geraden vom Mittelpunkt mit dem Radius r: ⟦d > r⟧ Passante (kein Punkt), ⟦d = r⟧ Tangente (ein Punkt), ⟦d < r⟧ Sekante (zwei Punkte).',
     'schritte': ['r = 4 cm, Abstand der Geraden von M: d = 3 cm', '3 cm < 4 cm', 'Die Gerade ist eine ⟦Sekante⟧ – sie schneidet den Kreis zweimal.'],
     'fehler': 'Eine Gerade mit d = r schneidet den Kreis nicht zweimal: Sie ⟦berührt⟧ ihn nur in einem Punkt.',
     'bild': figur({'M': [0, 0], '_1': [-5, 3], '_2': [5, 3], '_F': [0, 3]}, linien=[['_1', '_2', 'g'], ['M', '_F', 'd = 3', 'gestrichelt']], rechter_winkel=[['_F', 'M', '_2']],
                   kreise=[{'m': 'M', 'r': 4}]),
     '_verbot': ['d = 3 cm']},
    {'lernziel': 'beweis', 'titel': 'Vermuten und Beweisen',
     'regel': 'Messungen mit Geometriesoftware führen zu ⟦Vermutungen⟧. Ein ⟦Beweis⟧ zeigt mit Begründungen, dass eine Aussage ⟦immer⟧ gilt. Beim Thalessatz: MA = MB = MC (Radien) ergibt zwei ⟦gleichschenklige Dreiecke⟧.',
     'schritte': ['Dreieck AMC ist gleichschenklig: ∠ACM = α. Dreieck BMC: ∠BCM = β.', 'Also γ = α + β. Winkelsumme: α + β + (α + β) = 180°.', '2(α + β) = 180° → ⟦γ = α + β = 90°⟧'],
     'fehler': 'Hundert gemessene Beispiele mit 90° sind ⟦kein Beweis⟧: Sie zeigen nur, dass die Aussage für diese Beispiele stimmt.'},
]


def g_thales(R, st):
    al = R.randint(15, 75)
    if al == 45: al = 40
    if st == 1:
        a = Z(f'[AB] ist ein Durchmesser, C liegt auf dem Kreis. Es ist α = {al}°. Wie groß ist γ?', 90, '180 - 90',
              f'Nach dem Satz des Thales ist der Winkel bei C ein rechter Winkel: γ = 90°.', 'Was sagt der Satz des Thales über den Winkel bei C?', '°')
        a['f']['grafik'] = thales_bild(al, (f'{al}°', '', ''))
        return a
    if st == 2:
        a = Z(f'[AB] ist ein Durchmesser, C liegt auf dem Kreis. Es ist α = {al}°. Wie groß ist β?', 90 - al, f'180 - 90 - {al}',
              f'Thales: γ = 90°. β = 180° − 90° − {al}° = {90 - al}°.', 'Erst γ mit Thales, dann die Winkelsumme.', '°')
        a['f']['grafik'] = thales_bild(al, (f'{al}°', 'β', '90°'))
        return a
    # Stufe 3: Winkel am Mittelpunkt / gleichschenklig
    art = R.choice(['mitte', 'verhaeltnis'])
    if art == 'mitte':
        a = Z(f'[AB] ist Durchmesser des Kreises um M, C liegt auf dem Kreis, α = {al}°. Wie groß ist der Winkel ∠BMC?', 2 * al, f'2 * {al}',
              f'Dreieck AMC ist gleichschenklig (MA = MC): ∠ACM = {al}°. ∠AMC = 180° − 2 · {al}° = {180 - 2 * al}°. ∠BMC = 180° − {180 - 2 * al}° = {2 * al}°.',
              'MA und MC sind Radien. Nutze das gleichschenklige Dreieck AMC.', '°')
        a['f']['grafik'] = figur({'A': [-3, 0], 'B': [3, 0], 'M': [0, 0], 'C': [rd(3 * math.cos(math.radians(2 * al))), rd(3 * math.sin(math.radians(2 * al)))]},
                                 linien=[['A', 'B'], ['B', 'C'], ['C', 'A'], ['M', 'C', '', 'gestrichelt']], winkel=[['A', 'B', 'C', f'{al}°'], ['M', 'B', 'C', '?']], kreise=[{'m': 'M', 'r': 3}])
        return a
    k = R.choice([2, 3, 4, 5])
    return Z(f'[AB] ist Durchmesser, C liegt auf dem Kreis. β ist {k}-mal so groß wie α. Wie groß ist α?', Fr(90, k + 1), f'90 / ({k} + 1)',
             f'Thales: γ = 90°, also α + β = 90°. α + {k}α = 90° → α = 90° : {k + 1} = {zt(Fr(90, k + 1))}°.', 'α + β = 90°.', '°')


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
    r = 'Ja, denn γ = 90° (Umkehrung des Thalessatzes).' if lieg else f'Nein, denn γ = {180 - al - be}° ist kein rechter Winkel.'
    return A(R, f'Im Dreieck ABC ist α = {al}° und β = {be}°. Liegt C auf dem Kreis mit dem Durchmesser [AB]?', r,
             [f'Nein, denn γ = {180 - al - be}° ist kein rechter Winkel.' if lieg else 'Ja, denn γ = 90° (Umkehrung des Thalessatzes).',
              'Ja, jeder Punkt C liegt auf diesem Kreis.', 'Das kann man ohne Zeichnung nicht entscheiden.'],
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
                 [x for x in ['innerhalb des Dreiecks', 'auf der längsten Seite (Mitte der Hypotenuse)', 'außerhalb des Dreiecks'] if x != r] + ['immer im Schwerpunkt'],
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
    return Z(f'Eine Gerade soll den Kreis mit dem Radius {zt(r)} cm berühren. Welchen Abstand muss sie vom Mittelpunkt haben?', r, cz_(r),
             f'Tangente: d = r = {zt(r)} cm.', 'Bei einer Tangente ist der Abstand gleich dem Radius.', 'cm')


def cz_(x):
    x = Fr(x)
    return str(x.numerator) if x.denominator == 1 else f'{x.numerator} / {x.denominator}'


BEWEIS = [
    ('Dreieck AMC ist gleichschenklig.', 'MA und MC sind Radien desselben Kreises.'),
    ('∠ACM ist genauso groß wie α.', 'Basiswinkel im gleichschenkligen Dreieck AMC sind gleich.'),
    ('γ = α + β.', 'Die Strecke [MC] teilt γ in die Winkel ∠ACM = α und ∠BCM = β.'),
    ('α + β + γ = 180°.', 'Winkelsumme im Dreieck ABC.'),
    ('2γ = 180°, also γ = 90°.', 'In der Winkelsumme wird α + β durch γ ersetzt.'),
    ('Die Tangente steht senkrecht auf [MB].', 'Eigenschaft der Tangente: Sie steht senkrecht auf dem Berührradius.'),
    ('Der Berührpunkt B liegt auf dem Thaleskreis über [MP].', 'Bei B ist ein rechter Winkel zwischen MB und PB (Umkehrung des Thalessatzes).'),
]


def g_beweis(R, st):
    if st == 3 or (st == 2 and R.random() < .5):
        aussage, grund = R.choice(BEWEIS)
        andere = [g for a, g in BEWEIS if g != grund]
        return A(R, f'Im Beweis (Thales bzw. Tangentenkonstruktion) steht: „{aussage}“ Welche Begründung passt?', grund, R.sample(andere, 3), f'Begründung: {grund}',
                 'Welche bekannte Eigenschaft rechtfertigt genau diesen Schritt?')
    al = [('Eine Behauptung, die in vielen gemessenen Beispielen stimmt, ist damit bewiesen.', False), ('Ein einziges Gegenbeispiel widerlegt eine Vermutung.', True),
          ('Mit Geometriesoftware kann man Vermutungen finden, ein Beweis braucht Begründungen.', True), ('Ein Beweis gilt für alle Fälle, nicht nur für gezeichnete.', True),
          ('Wenn eine Messung 89,8° ergibt, ist der Satz des Thales widerlegt.', False), ('Ein Beweis darf sich auf schon bewiesene Sätze stützen.', True),
          ('Wenn der Satz des Thales gilt, gilt automatisch jede Umkehrung.', False), ('Eine Zeichnung allein ist ein Beweis.', False)]
    wahr = [t for t, w in al if w]; falsch = [t for t, w in al if not w]
    if st == 1 or R.random() < .5:
        t = R.choice(wahr)
        return A(R, 'Welche Aussage über Vermutung und Beweis ist richtig?', t, R.sample(falsch, 3), f'Richtig: {t}', 'Was unterscheidet Messen von Begründen?')
    t = R.choice(falsch)
    return A(R, 'Welche Aussage über Vermutung und Beweis ist FALSCH?', t, R.sample(wahr, 3), f'Falsch: {t} Messungen sind ungenau und decken nie alle Fälle ab.',
             'Was unterscheidet Messen von Begründen?')


GEN = {'thales': g_thales, 'umkehrung': g_umkehrung, 'tangente': g_tangente, 'umkreis_inkreis': g_umkreis_inkreis, 'lage': g_lage, 'beweis': g_beweis}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Satz des Thales', ['thales', 'umkehrung', 'beweis']), ('Tangenten', ['lage', 'tangente']), ('Besondere Kreise', ['umkreis_inkreis'])],
         'Den Satz des Thales und seine Umkehrung anwenden und begründen, Tangenten und ihre Eigenschaften nutzen, Umkreis und Inkreis von Dreiecken bestimmen.',
         ['Thales: C auf dem Kreis über dem Durchmesser [AB] ⇔ γ = 90°.', 'Tangente ⊥ Berührradius. Von außen: zwei gleich lange Tangentenabschnitte.',
          'Umkreis: Mittelsenkrechten. Inkreis: Winkelhalbierende.', 'Passante d > r, Tangente d = r, Sekante d < r.'],
         offen=['Die Konstruktion der Tangente von einem äußeren Punkt (Thaleskreis über [MP]) wird nur begründet (Lernkarte „beweis“), nicht vom Kind gezeichnet – Zeichnen durch das Kind kann die App nicht.',
                'Experimentieren mit dynamischer Geometriesoftware (Lehrplan) ist in der App nicht möglich.',
                'Kreiswinkel (Umfangs-/Mittelpunktswinkelsatz) aus dem Feld „umfang“ weggelassen: nicht im lehrplan_gym für Klasse 7; nur der Spezialfall am Thaleskreis kommt vor.'])
