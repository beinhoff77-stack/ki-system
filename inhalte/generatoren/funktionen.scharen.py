#!/usr/bin/env python3
"""Thema funktionen.scharen – Parameter und Funktionenscharen (Realschule Bayern, Klasse 8, lineare Funktionen)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _rs import *  # noqa: E402,F403

start(7801)
LT = '□x + □'
HT = 'Tippe den Term ein, z. B. 3x − 2.'
STEIG = [Fr(x, 2) for x in range(-8, 9) if x != 0] + [Fr(x, 4) for x in (-3, -1, 1, 3)]


def m_zuf(ganz=False):
    if ganz: return Fr(R.choice([i for i in range(-5, 6) if i != 0]))
    return R.choice(STEIG)


def gl(m, t):
    return 'y = ' + poly(m, t)


def nz(n):
    return R.choice([i for i in range(-n, n + 1) if i != 0])


def schar_bild(funcs, x=(-5, 5), y=(-5, 5)):
    return {'typ': 'koordinaten', 'x': list(x), 'y': list(y),
            'graphen': [{'art': 'linear', 'm': float(m), 't': float(t), 'name': n} for m, t, n in funcs]}


ETAPPEN = [
    {'lernziel': 'einsetzen', 'titel': 'Einen Parameterwert einsetzen',
     'regel': 'In y = k · x + 2 ist k ein ⟦Parameter⟧: eine Zahl, die du frei wählen darfst. Jeder Wert von k liefert eine andere Gerade. Alle zusammen heißen ⟦Geradenschar⟧. Wie bei einem Rezept mit „k Löffeln Zucker“: Erst wenn du k festlegst, ist das Rezept eindeutig.',
     'schritte': ['Schar g_k: y = k · x + 2. Für k = −3 erhältst du g₋₃: ⟦y = −3x + 2⟧.',
                  'Der Punkt dieser Geraden mit x = 4: y = −3 · 4 + 2 = ⟦−10⟧.'],
     'fehler': 'Für k = −3 statt y = −3x + 2 die Gleichung y = −3x − 3 zu schreiben ist falsch: Der Parameter ersetzt ⟦nur das k⟧, die 2 bleibt.'},
    {'lernziel': 'parallelenschar', 'titel': 'Parallele Geraden: y = m · x + t',
     'regel': 'Ist der ⟦y-Achsenabschnitt⟧ der Parameter (y = 2x + t), haben alle Geraden die ⟦gleiche Steigung⟧. Sie sind ⟦parallel⟧ – wie Treppengeländer in verschiedenen Stockwerken. Durch einen Punkt P geht genau eine davon: ⟦t = y_P − m · x_P⟧.',
     'bild': schar_bild([(2, -2, 't = −2'), (2, 0, 't = 0'), (2, 2, 't = 2')]),
     'schritte': ['Schar y = 2x + t. Welche Gerade geht durch P(3 | 1)? Einsetzen: 1 = 2 · 3 + t.', '1 = 6 + t ⇒ ⟦t = −5⟧. Die Gerade ist y = 2x − 5.'],
     'probe': '2 · 3 − 5 = 1 ✓',
     'fehler': 'Aus 1 = 6 + t zu folgern t = 7 ist falsch: Du musst 6 ⟦abziehen⟧, nicht addieren. t = 1 − 6 = −5.'},
    {'lernziel': 'bueschel', 'titel': 'Geraden durch einen Punkt',
     'regel': 'Ist die ⟦Steigung⟧ der Parameter, z. B. y = m · (x − 1) + 3, gehen alle Geraden durch ⟦denselben Punkt⟧, hier Z(1 | 3) – wie die Speichen eines Rads um die Nabe. Diese Schar heißt ⟦Geradenbüschel⟧. Den gemeinsamen Punkt findest du dort, wo der Parameter ⟦keinen Einfluss⟧ hat.',
     'bild': schar_bild([(-1, 4, 'm = −1'), (Fr(1, 2), Fr(5, 2), 'm = 0,5'), (2, 1, 'm = 2')], (-3, 5), (-2, 7)),
     'schritte': ['Büschel y = m · (x − 1) + 3. Für x = 1 wird die Klammer 0, also y = 3 – egal, welches m.',
                  'Gemeinsamer Punkt ⟦Z(1 | 3)⟧. Durch Q(3 | 7): 7 = m · 2 + 3 ⇒ ⟦m = 2⟧.'],
     'fehler': 'Bei y = m · (x − 1) + 3 den Punkt Z(−1 | 3) abzulesen ist falsch: Die Klammer ist null für ⟦x = +1⟧ – das Vorzeichen dreht sich um.'},
    {'lernziel': 'wirkung', 'titel': 'Was bewirkt der Parameter?',
     'regel': 'Schau, ⟦wo⟧ der Parameter steht: Vor dem x verändert er die ⟦Steigung⟧ (die Gerade dreht sich), als Zahlglied verschiebt er die Gerade ⟦nach oben oder unten⟧. Für den Wert, der die Steigung 0 macht, ist die Gerade ⟦parallel zur x-Achse⟧.',
     'schritte': ['Schar y = (k − 2) · x + 1: Die Steigung ist k − 2, der y-Achsenabschnitt immer 1.',
                  'Parallel zur x-Achse: k − 2 = 0 ⇒ ⟦k = 2⟧. Fallende Geraden: k − 2 < 0, also ⟦k < 2⟧.'],
     'fehler': '„Bei y = (k − 2)x + 1 ist k die Steigung“ ist falsch: Die Steigung ist der ⟦ganze Faktor vor x⟧, also k − 2. Für k = 5 ist sie 3, nicht 5.'},
    {'lernziel': 'loesung_parameter', 'titel': 'Lösungen, die vom Parameter abhängen',
     'regel': 'Bei einer Gleichung mit Parameter, z. B. k · x = 6, hängt die Lösung von k ab: ⟦x = 6 : k⟧. Achtung: Durch ⟦0 darfst du nicht teilen⟧. Für k = 0 heißt die Gleichung 0 = 6 – sie hat ⟦keine Lösung⟧. Genauso beim Schnittpunkt zweier Geraden: Gleiche Steigung heißt ⟦parallel⟧, also kein Schnittpunkt.',
     'schritte': ['Schnittpunkt von y = 2x + 1 und y = kx − 3: 2x + 1 = kx − 3 ⇔ (2 − k)x = −4 ⇔ x = −4 : (2 − k).',
                  'Für k = 4: x = −4 : (−2) = ⟦2⟧. Für ⟦k = 2⟧ sind die Geraden parallel – kein Schnittpunkt.'],
     'probe': 'k = 4, x = 2: 2 · 2 + 1 = 5 und 4 · 2 − 3 = 5 ✓',
     'fehler': 'Bei (k − 3) · x = 5 einfach „x = 5 : (k − 3)“ hinzuschreiben ist unvollständig: Für ⟦k = 3⟧ ist das Teilen verboten, die Gleichung hat dann keine Lösung.'},
    {'lernziel': 'sachaufgabe', 'titel': 'Parameter in Sachaufgaben',
     'regel': 'In Tarifen steckt oft ein Parameter: ⟦Kosten = Preis pro Einheit · Menge + Grundgebühr⟧. Ist eine Größe noch offen, ist sie der Parameter. Mit einer ⟦Bedingung⟧ (z. B. „10 km kosten 24 €“) bestimmst du ihn.',
     'schritte': ['Taxi: y = m · x + 4 (x in km, y in €, Grundgebühr 4 €). Für 10 km zahlt man 24 €.',
                  '24 = m · 10 + 4 ⇒ 10m = 20 ⇒ ⟦m = 2⟧: 2 € pro Kilometer.'],
     'probe': '2 · 10 + 4 = 24 ✓',
     'fehler': '24 : 10 = 2,40 € pro km ist falsch: Die ⟦Grundgebühr⟧ von 4 € muss zuerst abgezogen werden.'},
]


# ---------- Generatoren ----------
def g_einsetzen(s):
    form = R.choice(['k_steigung', 'k_abschnitt', 'k_beides'])
    k = nz(6)
    if form == 'k_steigung':
        b = nz(6)
        schar, m, t, sm = f'y = k · x {plus(b)}', Fr(k), Fr(b), f'k · x {plus(b)}'
    elif form == 'k_abschnitt':
        a = m_zuf(True)
        schar, m, t = f'y = {poly(a, 0)} + k', a, Fr(k)
    else:
        c = nz(4)
        if c == k: return None
        schar, m, t = f'y = (k {plus(-c)}) · x + 2k', Fr(k - c), Fr(2 * k)
    if s == 1:
        return luecken(f'Gegeben ist die Schar {schar}. Gib die Gleichung für k = {dz(k)} an: y = ?', LT, HT, [m, t],
                       f'k = {dz(k)} einsetzen: {gl(m, t)}.', 'Ersetze jedes k durch die Zahl.',
                       c=[cz(m), cz(t)])
    x = nz(6)
    y = m * x + t
    if s == 2:
        return zahl(f'Gegeben ist die Schar {schar}. Berechne für k = {dz(k)} den y-Wert an der Stelle x = {dz(x)}.',
                    f'Gerade für k = {dz(k)}: {gl(m, t)}. y = {dz(m)} · {kl(x)} {plus(t)} = {dz(y)}.',
                    'Erst k einsetzen, dann x einsetzen.', y, f'{cz(m)} * ({x}) + {cz(t)}')
    if R.random() < 0.5:
        # Liegt P auf g_k?
        yp = y + R.choice([0, 0, 1, -1, 2])
        ja = yp == y
        return auswahl(f'Liegt der Punkt P({dz(x)} | {dz(yp)}) auf der Geraden der Schar {schar} mit k = {dz(k)}?',
                       'Ja' if ja else 'Nein', ['Nein' if ja else 'Ja', 'Das hängt nicht von k ab.'],
                       f'{gl(m, t)}: für x = {dz(x)} ist y = {dz(y)}' + (' – stimmt.' if ja else f', nicht {dz(yp)}.'),
                       'Setze k ein und prüfe, ob P die Gleichung erfüllt.')
    # Fehler finden: k nur teilweise ersetzt
    if form == 'k_steigung': return None
    if form == 'k_abschnitt':
        return auswahl(f'Welche Gleichung gehört in der Schar {schar} zu k = {dz(k)}?', gl(m, t),
                       [gl(m, -t), gl(Fr(k), m), gl(m + k, 0)],
                       f'k = {dz(k)} ersetzt nur das k am Ende: {gl(m, t)}.', 'Wo genau steht das k?')
    return auswahl(f'Welche Gleichung gehört in der Schar {schar} zu k = {dz(k)}?', gl(m, t),
                   [gl(Fr(k), 2), gl(m, 2), gl(Fr(k - c), k)],
                   f'Beide k ersetzen: Steigung {dz(k)} {plus(-c)} = {dz(m)}, Zahlglied 2 · {kl(k)} = {dz(t)}. Also {gl(m, t)}.',
                   'Jedes k wird ersetzt – auch das in 2k.')


def g_parallelenschar(s):
    m = m_zuf(s == 1)
    xp = nz(6)
    yp = Fr(nz(8))
    t = yp - m * xp
    if not endlich(t): return None
    schar = f'y = {poly(m, 0)} + t'
    w = f'{dz(yp)} = {dz(m)} · {kl(xp)} + t ⇔ {dz(yp)} = {dz(m * xp)} + t ⇔ t = {dz(t)}.'
    if s == 1:
        return zahl(f'Welche Gerade der Schar {schar} geht durch P({dz(xp)} | {dz(yp)})? Berechne t.', w,
                    'Setze die Koordinaten von P ein und löse nach t auf.', t, f'{cz(yp)} - {cz(m)} * ({xp})')
    if s == 2:
        if R.random() < 0.5:
            return zahl(f'Die Schar lautet {schar}. Bestimme t so, dass die Gerade durch P({dz(xp)} | {dz(yp)}) verläuft.', w,
                        'P einsetzen, nach t auflösen.', t, f'{cz(yp)} - {cz(m)} * ({xp})')
        tt = nz(4)
        a = zahl(f'Die gezeichnete Gerade gehört zur Schar {schar}. Lies t ab.',
                 f'Alle Geraden der Schar haben die Steigung {dz(m)}; t ist der y-Achsenabschnitt. Die Gerade schneidet die y-Achse bei {dz(tt)}, also t = {dz(tt)}.',
                 'Wo schneidet die Gerade die y-Achse?', tt, str(tt))
        return bild(a, schar_bild([(m, tt, '')], (-5, 5), (-6, 6)))
    art = R.random()
    if art < 0.4:
        # Parallele zu einer gegebenen Geraden durch P
        m2 = m_zuf()
        t2 = nz(5)
        t = yp - m2 * xp
        if not endlich(t): return None
        return luecken(f'Gib die Gleichung der Geraden an, die parallel zu y = {poly(m2, t2)} ist und durch P({dz(xp)} | {dz(yp)}) geht. y = ?',
                       LT, HT,
                       [m2, t], f'Parallel heißt gleiche Steigung {dz(m2)}. {dz(yp)} = {dz(m2)} · {kl(xp)} + t ⇒ t = {dz(t)}. Also {gl(m2, t)}.',
                       'Parallel = gleiche Steigung. Dann t mit P bestimmen.', c=[cz(m2), cz(t)]) if m2.denominator == 1 and t.denominator == 1 else None
    if art < 0.7:
        return auswahl(f'Was haben alle Geraden der Schar {schar} gemeinsam?', f'Sie haben alle die Steigung {dz(m)} und sind parallel.',
                       ['Sie gehen alle durch den Ursprung.', f'Sie schneiden die y-Achse alle bei {dz(m)}.', 'Sie schneiden sich alle in einem Punkt.'],
                       f't verschiebt nur nach oben oder unten; die Steigung {dz(m)} bleibt gleich. Darum sind alle Geraden parallel und haben keinen gemeinsamen Punkt.',
                       'Welche Zahl ändert sich, welche bleibt gleich?')
    # Fehler finden
    tf = yp + m * xp
    if tf == t: return None
    return auswahl(f'Jemand rechnet für die Schar {schar} und P({dz(xp)} | {dz(yp)}): t = {dz(tf)}. Was stimmt?',
                   f'Falsch, richtig ist t = {dz(t)}.', ['Richtig.', f'Falsch, richtig ist t = {dz(-tf)}.', f'Falsch, richtig ist t = {dz(yp)}.'],
                   w + f' Der Fehler: {dz(m * xp)} wurde addiert statt abgezogen.', 'Setze ein und prüfe: Ergibt sich die y-Koordinate von P?')


def g_bueschel(s):
    a, b = nz(4), nz(5)
    schar = f'y = m · {minus_klammer(a)} {plus(b)}'
    if s == 1:
        return luecken(f'Alle Geraden der Schar {schar} gehen durch einen gemeinsamen Punkt Z. Gib Z an.', 'Z(□ | □)', 'x-Wert, y-Wert', [a, b],
                       f'Für x = {dz(a)} ist die Klammer 0, also y = {dz(b)} für jedes m. Z({dz(a)} | {dz(b)}).',
                       'Für welches x verschwindet der Einfluss von m?', c=[str(a), str(b)])
    dx = nz(4)
    xq = a + dx
    m = m_zuf()
    yq = b + m * dx
    if not endlich(yq): return None
    w = f'{dz(yq)} = m · ({dz(xq)} {plus(-a)}) {plus(b)} ⇔ {dz(yq - b)} = m · {kl(dx)} ⇔ m = {dz(m)}.'
    if s == 2:
        if R.random() < 0.5:
            return zahl(f'Für welches m geht die Gerade der Schar {schar} durch Q({dz(xq)} | {dz(yq)})?', w,
                        'Setze Q ein. Die Klammer wird zu einer Zahl.', m, f'({cz(yq)} - ({b})) / ({dx})')
        t = nz(5)
        return luecken(f'Die Schar y = m · x {plus(t)} hat einen gemeinsamen Punkt. Gib ihn an.', 'Z(□ | □)', 'x-Wert, y-Wert', [0, t],
                       f'Für x = 0 ist m · 0 = 0, also y = {dz(t)} für alle m: Z(0 | {dz(t)}), der Punkt auf der y-Achse.',
                       'Setze x = 0 ein.', c=['0', str(t)])
    art = R.random()
    if art < 0.35:
        return auswahl(f'Welchen Punkt haben alle Geraden der Schar {schar} gemeinsam?', f'Z({dz(a)} | {dz(b)})',
                       [f'Z({dz(-a)} | {dz(b)})', f'Z({dz(b)} | {dz(a)})', f'Z(0 | {dz(b)})'],
                       f'Für x = {dz(a)} ist {minus_klammer(a)} = 0, dann y = {dz(b)}.', 'Achte auf das Vorzeichen in der Klammer.')
    if art < 0.7:
        # Büschel aus Zentrum und Punkt aufstellen: Steigung durch zwei Punkte
        return zahl(f'Eine Gerade geht durch Z({dz(a)} | {dz(b)}) und Q({dz(xq)} | {dz(yq)}). Welche Steigung m hat sie?',
                    f'm = (y_Q − y_Z) : (x_Q − x_Z) = ({dz(yq)} − {kl(b)}) : ({dz(xq)} − {kl(a)}) = {dz(yq - b)} : {kl(dx)} = {dz(m)}.',
                    'Steigungsdreieck: Höhenunterschied geteilt durch Breitenunterschied.', m, f'({cz(yq)} - ({b})) / (({xq}) - ({a}))')
    # Gehört die parallele zur y-Achse dazu?
    return auswahl(f'Gehört die Parallele zur y-Achse durch Z({dz(a)} | {dz(b)}) zum Büschel {schar}?',
                   'Nein, sie hat keine Steigung und lässt sich nicht als y = m · … schreiben.',
                   ['Ja, für m = 0.', f'Ja, für m = {dz(a)}.', 'Ja, für jedes m.'],
                   f'm = 0 liefert die Parallele zur x-Achse y = {dz(b)}. Eine senkrechte Gerade (x = {dz(a)}) ist keine Funktion der Form y = m · x + t.',
                   'Welche Gerade entsteht für m = 0?')


def g_wirkung(s):
    c = nz(5)
    b = nz(5)
    schar = f'y = (k {plus(-c)}) · x {plus(b)}'
    if s == 1:
        return zahl(f'Für welches k ist die Gerade der Schar {schar} parallel zur x-Achse?',
                    f'Parallel zur x-Achse heißt Steigung 0: k {plus(-c)} = 0 ⇒ k = {dz(c)}.',
                    'Welche Steigung hat eine waagrechte Gerade?', c, str(c))
    if s == 2:
        art = R.random()
        if art < 0.35:
            return auswahl(f'Für welche k fallen die Geraden der Schar {schar}?', f'k < {dz(c)}',
                           [f'k > {dz(c)}', 'k < 0', f'k < {dz(-c)}'],
                           f'Fallen heißt Steigung negativ: k {plus(-c)} < 0 ⇔ k < {dz(c)}.', 'Wann ist die Steigung negativ?')
        if art < 0.7:
            m0 = m_zuf(True)
            if m0 == 0: return None
            return zahl(f'Für welches k ist die Gerade der Schar {schar} parallel zu y = {poly(m0, nz(4))}?',
                        f'Gleiche Steigung: k {plus(-c)} = {dz(m0)} ⇒ k = {dz(m0 + c)}.', 'Parallel heißt: gleiche Steigung.',
                        m0 + c, f'{cz(m0)} + ({c})')
        mt = R.choice(['k', 'tk'])
        if mt == 'k':
            return auswahl('Was passiert mit den Geraden y = 2x + k, wenn k größer wird?', 'Sie werden nach oben verschoben.',
                           ['Sie werden steiler.', 'Sie drehen sich um den Ursprung.', 'Sie werden nach unten verschoben.'],
                           'k ist das Zahlglied (y-Achsenabschnitt). Größeres k: Die Gerade schneidet die y-Achse weiter oben, die Steigung 2 bleibt.',
                           'Wo steht das k – vor dem x oder allein?') if R.random() < 0.5 else \
                auswahl(f'Was passiert mit den Geraden y = k · x {plus(b)}, wenn k größer wird (k > 0)?', 'Sie werden steiler.',
                        ['Sie werden nach oben verschoben.', 'Sie werden flacher.', 'Sie bleiben parallel.'],
                        f'k ist die Steigung; alle Geraden drehen sich um den Punkt (0 | {dz(b)}). Größeres k heißt steiler.',
                        'Wo steht das k – vor dem x oder allein?')
        return auswahl(f'Welche Steigung hat die Gerade der Schar {schar} für k = {dz(c + 3)}?', '3', [dz(c + 3), dz(-3), dz(b)],
                       f'Steigung = k {plus(-c)} = {dz(c + 3)} {plus(-c)} = 3.', 'Die Steigung ist der ganze Faktor vor x.')
    art = R.random()
    if art < 0.4:
        # Bild: Gerade der Schar mit ablesbarer Steigung, k bestimmen
        mm = nz(3)
        a = zahl(f'Die gezeichnete Gerade gehört zur Schar {schar}. Bestimme k.',
                 f'Aus der Zeichnung: y-Achsenabschnitt {dz(b)}, Steigung {dz(mm)} (1 nach rechts, {dz(mm)} nach oben/unten). k {plus(-c)} = {dz(mm)} ⇒ k = {dz(mm + c)}.',
                 f'Lies die Steigung mit einem Steigungsdreieck ab. Dann gilt k {plus(-c)} = Steigung.', mm + c, f'{mm} + ({c})')
        return bild(a, schar_bild([(mm, b, '')], (-5, 5), (-7, 7)))
    if art < 0.7:
        k0 = c + R.choice([-2, -1, 1, 2, 3])
        st = k0 - c
        return auswahl(f'Für k = {dz(k0)} gehört zur Schar {schar} eine Gerade. Welche Aussage stimmt?',
                       f'Sie {"steigt" if st > 0 else "fällt"} mit Steigung {dz(st)} und schneidet die y-Achse bei {dz(b)}.',
                       [f'Sie {"steigt" if st > 0 else "fällt"} mit Steigung {dz(k0)} und schneidet die y-Achse bei {dz(b)}.',
                        f'Sie {"fällt" if st > 0 else "steigt"} mit Steigung {dz(-st)} und schneidet die y-Achse bei {dz(b)}.',
                        f'Sie {"steigt" if st > 0 else "fällt"} mit Steigung {dz(st)} und schneidet die y-Achse bei {dz(k0)}.'],
                       f'Steigung k {plus(-c)} = {dz(k0)} {plus(-c)} = {dz(st)}, y-Achsenabschnitt {dz(b)} (hängt nicht von k ab).',
                       'Erst die Steigung ausrechnen, dann den y-Achsenabschnitt ablesen.')
    return auswahl(f'Gibt es in der Schar {schar} eine Gerade durch den Ursprung?', 'Nein, alle schneiden die y-Achse bei ' + dz(b) + '.',
                   [f'Ja, für k = {dz(c)}.', 'Ja, für k = 0.', f'Ja, für k = {dz(-b)}.'],
                   f'Durch den Ursprung heißt y-Achsenabschnitt 0. Er ist aber immer {dz(b)}, egal welches k.',
                   'Welcher Teil der Gleichung entscheidet über den Schnitt mit der y-Achse?')


def g_loesung_parameter(s):
    if s == 1:
        c = R.choice([2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24])
        k = R.choice([d for d in range(-6, 7) if d != 0 and endlich(Fr(c, d))])
        return zahl(f'Löse k · x = {c} für k = {dz(k)}.', f'x = {c} : {kl(k)} = {dz(Fr(c, k))}.',
                    'Teile durch k.', Fr(c, k), f'{c} / ({k})')
    if s == 2:
        art = R.random()
        if art < 0.4:
            c = nz(5)
            r = R.choice([2, 3, 4, 5, 6, 8, 10, 12])
            return auswahl(f'Für welches k hat die Gleichung (k {plus(-c)}) · x = {r} keine Lösung?', f'k = {dz(c)}',
                           [f'k = {dz(-c)}', 'k = 0', f'k = {dz(r)}'],
                           f'Für k = {dz(c)} wird die Klammer 0: 0 · x = {r} ist nie erfüllt. Sonst ist x = {r} : (k {plus(-c)}).',
                           'Wann wird der Faktor vor x null?')
        m1, t1 = nz(3), nz(4)
        t2 = nz(4)
        if t1 == t2: return None
        k = R.choice([d for d in range(-4, 6) if d not in (m1, 0)])
        x = Fr(t2 - t1, m1 - k)
        if not endlich(x): return None
        return zahl(f'Die Geraden y = {poly(m1, t1)} und y = k · x {plus(t2)} schneiden sich. Berechne die x-Koordinate des Schnittpunkts für k = {dz(k)}.',
                    f'{poly(m1, t1)} = {poly(k, t2) if k else dz(t2)} ⇔ {poly(m1 - k, 0)} = {dz(t2 - t1)} ⇔ x = {dz(x)}.',
                    'Gleichsetzen, alle x auf eine Seite, dann teilen.', x, f'(({t2}) - ({t1})) / (({m1}) - ({k}))')
    art = R.random()
    if art < 0.35:
        m1, t1, t2 = nz(4), nz(4), nz(4)
        if t1 == t2: return None
        return zahl(f'Für welchen Wert von k haben die Geraden y = {poly(m1, t1)} und y = k · x {plus(t2)} keinen Schnittpunkt?',
                    f'Keinen Schnittpunkt haben parallele Geraden (verschiedene y-Achsenabschnitte {dz(t1)} und {dz(t2)}): k = {dz(m1)}.',
                    'Wann sind zwei Geraden parallel?', m1, str(m1))
    if art < 0.7:
        c = nz(5)
        r = nz(8)
        if r == 0: return None
        k = c + R.choice([d for d in (-4, -2, -1, 1, 2, 4, 5) if endlich(Fr(r, d))])
        x = Fr(r, k - c)
        return auswahl(f'Wie viele Lösungen hat (k {plus(-c)}) · x = {dz(r)}?',
                       f'Für k ≠ {dz(c)} genau eine (x = {dz(r)} : (k {plus(-c)})), für k = {dz(c)} keine.',
                       [f'Immer genau eine: x = {dz(r)} : (k {plus(-c)}).', f'Für k = {dz(c)} unendlich viele, sonst eine.', f'Für k = 0 keine, sonst eine.'],
                       f'Für k = {dz(c)} steht 0 · x = {dz(r)} da – unmöglich. Sonst darf man durch k {plus(-c)} teilen.',
                       'Was passiert, wenn der Faktor vor x null wird?')
    c = nz(4)
    a = R.choice([2, 3, 4])
    k = R.choice([d for d in range(-5, 7) if d != c and endlich(Fr(a * d, d - c)) and d != 0])
    x = Fr(a * k, k - c)
    return zahl(f'Löse (k {plus(-c)}) · x = {a}k für k = {dz(k)}.',
                f'k = {dz(k)}: ({dz(k)} {plus(-c)}) · x = {a} · {kl(k)} ⇔ {dz(k - c)}x = {dz(a * k)} ⇔ x = {dz(x)}.',
                'Erst k überall einsetzen, dann nach x auflösen.', x, f'{a} * ({k}) / (({k}) - ({c}))')


TARIFE = [('Ein Taxi kostet {g} € Grundgebühr plus m € pro Kilometer.', 'km', '€', 'Kilometerpreis', ' km'),
          ('Ein Stromtarif kostet {g} € Grundgebühr im Monat plus m € pro kWh.', 'kWh', '€', 'Preis pro kWh', ' kWh'),
          ('Ein Fahrradverleih nimmt {g} € Grundgebühr plus m € pro Stunde.', 'h', '€', 'Stundenpreis', ' Stunden'),
          ('Ein Handwerker berechnet {g} € Anfahrt plus m € pro Stunde.', 'h', '€', 'Stundenlohn', ' Stunden')]


def g_sachaufgabe(s):
    tx, ex, ey, name, einh = R.choice(TARIFE)
    if 'kWh' in einh:
        g = R.choice([8, 10, 12, 15])
        m = R.choice([Fr(25, 100), Fr(3, 10), Fr(32, 100), Fr(35, 100), Fr(4, 10)])
        x = R.choice([100, 150, 200, 250, 300])
    elif 'km' in einh:
        g = R.choice([3, 4, 5])
        m = R.choice([Fr(2), Fr(5, 2), Fr(21, 10), Fr(12, 5), Fr(3)])
        x = R.choice([4, 5, 8, 10, 12, 15])
    elif 'Stunden' in einh and 'Fahrrad' in tx:
        g = R.choice([2, 3, 5])
        m = R.choice([Fr(3), Fr(7, 2), Fr(4), Fr(9, 2), Fr(6)])
        x = R.choice([2, 3, 4, 5, 6])
    else:
        g = R.choice([30, 40, 45, 50])
        m = R.choice([Fr(40), Fr(45), Fr(50), Fr(55), Fr(60)])
        x = R.choice([2, 3, 4, 5, 6])
    y = m * x + g
    t = tx.format(g=g)
    if s == 1:
        return zahl(t + f' Der {name} beträgt m = {eur(m)} €. Wie viel kostet es für {dz(x)}{einh}?',
                    f'y = {eur(m)} · {dz(x)} + {g} = {eur(y)} €.', 'Preis pro Einheit mal Menge, dann Grundgebühr dazu.',
                    y, f'{cz(m)} * {x} + {g}', einheit='€')
    w = f'{eur(y)} = m · {dz(x)} + {g} ⇔ m · {dz(x)} = {eur(y - g)} ⇔ m = {eur(m)} €.'
    if s == 2:
        return zahl(t + f' Für {dz(x)}{einh} bezahlt man {eur(y)} €. Berechne m.', w,
                    'Grundgebühr abziehen, dann durch die Menge teilen.', m, f'({cz(y)} - {g}) / {x}', einheit='€')
    art = R.random()
    if art < 0.4:
        falsch = y / x
        return auswahl(t + f' Für {dz(x)}{einh} bezahlt man {eur(y)} €. Wie hoch ist m?', f'{eur(m)} €',
                       [f'{eur(v)} €' for v in (falsch, (y + g) / x, y - g, m + 1) if (v * 100).denominator == 1],
                       w, 'Vergiss die Grundgebühr nicht.')
    # Vergleich zweier Tarife: ab welcher Menge ist B günstiger? Lösung ganzzahlig
    g2 = g + R.choice([5, 10, 15, 20]) if g >= 10 else g + R.choice([2, 3, 4])
    d = R.choice([Fr(1, 2), Fr(1), Fr(2), Fr(5, 2), Fr(5)]) if g >= 10 else R.choice([Fr(1, 2), Fr(1)])
    if 'kWh' in einh: d = R.choice([Fr(5, 100), Fr(1, 10)])
    m2 = m - d
    if m2 <= 0: return None
    xs = Fr(g2 - g) / d
    if xs.denominator != 1: return None
    pro = {'km': 'Kilometer', 'kWh': 'kWh', 'h': 'Stunde'}[ex]
    return zahl(t + f' Bei Tarif A ist m = {eur(m)} €. Tarif B kostet {g2} € Grundgebühr und nur {eur(m2)} € pro {pro}. Bei welcher Menge kosten beide gleich viel?',
                f'{eur(m)} · x + {g} = {eur(m2)} · x + {g2} ⇔ ' + (f'x = {g2 - g}.' if d == 1 else f'{eur(d)} · x = {g2 - g} ⇔ x = {dz(xs)}.'),
                'Beide Kostenterme gleichsetzen und nach x auflösen.', xs, f'({g2} - {g}) / ({cz(m)} - {cz(m2)})', einheit=einh.strip())


GEN = {'einsetzen': g_einsetzen, 'parallelenschar': g_parallelenschar, 'bueschel': g_bueschel, 'wirkung': g_wirkung,
       'loesung_parameter': g_loesung_parameter, 'sachaufgabe': g_sachaufgabe}

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import ko, pkte  # noqa: E402


def _g(m, t, name=None):
    g = {'art': 'linear', 'm': m, 't': t}
    if name:
        g['name'] = name
    return g


def _taxi(x1=5, y1=18, **kw):
    return ko([0, x1], [0, y1], schritt=0, name_x='km', name_y='€', **kw)


UMBAU = {
    'einsetzen': {
        'einstieg': 'Ein Taxi kostet 2 € Grundgebühr plus einen Preis pro Kilometer. Jede Stadt legt diesen Preis anders fest. '
                    'Die offene Zahl k heißt ⟦Parameter⟧.',
        'woerter': [['Parameter', 'eine Zahl in der Gleichung, die man frei wählen kann, hier k'],
                    ['Geradenschar', 'alle Geraden, die zu den verschiedenen Werten von k gehören']],
        'bild': _taxi(graphen=[_g(1, 2, 'k = 1'), _g(2, 2, 'k = 2'), _g(3, 2, 'k = 3')]),
        'schritte': [
            {'text': 'Der Tarif y = k · x + 2 ist eine Geradenschar.'},
            {'text': 'Die Stadt legt k = 3 fest: ⟦y = 3x + 2⟧.', 'bild': {'graphen': [_g(3, 2, 'k = 3')]}},
            {'text': 'Für 4 km: y = 3 · 4 + 2 = ⟦14⟧, also 14 €.', 'bild': {'punkte': pkte({'(4|14)': (4, 14)})}},
        ],
        'fehler': 'Für k = 3 nicht y = 3x + 3 schreiben. Der Parameter ersetzt ⟦nur das k⟧, die Grundgebühr 2 bleibt.',
        'fehler_bild': {'graphen': [_g(3, 2, 'richtig'), _g(3, 3, 'falsch')], 'punkte': None},
        'regel': 'Parameter einsetzen: nur k ersetzen, alles andere bleibt. Jedes k gibt eine Gerade der ⟦Geradenschar⟧.',
    },
    'parallelenschar': {
        'einstieg': 'Drei Taxis kosten alle 2 € pro Kilometer, aber verschiedene Grundgebühren. '
                    'Ihre Preis-Geraden steigen gleich steil, nur höher oder tiefer. Sie sind ⟦parallel⟧.',
        'woerter': [['y-Achsenabschnitt t', 'wo die Gerade die y-Achse trifft; hier die Grundgebühr'],
                    ['parallel', 'gleich steil; die Geraden treffen sich nie']],
        'bild': _taxi(graphen=[_g(2, 1, 't = 1'), _g(2, 4, 't = 4'), _g(2, 7, 't = 7')]),
        'schritte': [
            {'text': 'In y = 2x + t ist der y-Achsenabschnitt t der Parameter.'},
            {'text': 'Welche Gerade geht durch P(3 | 10)? Einsetzen: 10 = 2 · 3 + t.', 'bild': {'punkte': pkte({'P': (3, 10)})}},
            {'text': '10 = 6 + t, also ⟦t = 4⟧.', 'bild': {'graphen': [_g(2, 4, 't = 4')]}},
            {'text': 'Die Gerade ist y = 2x + 4: 4 € Grundgebühr.'},
        ],
        'fehler': 'Aus 10 = 6 + t folgt nicht t = 16. Du musst 6 ⟦abziehen⟧: t = 10 − 6 = 4.',
        'fehler_bild': {'graphen': [_g(2, 4, 't = 4'), _g(2, 16, 't = 16')]},
        'regel': 'Parameter t: Alle Geraden sind ⟦parallel⟧. Für die Gerade durch P setzt du P ein und löst nach t auf.',
    },
    'bueschel': {
        'einstieg': 'Ein Leuchtturm schickt Lichtstrahlen in viele Richtungen. Alle Strahlen starten am selben Punkt, '
                    'nur die Steigung ist anders. So eine Schar heißt ⟦Geradenbüschel⟧.',
        'woerter': [['Geradenbüschel', 'alle Geraden der Schar gehen durch denselben Punkt'],
                    ['Z', 'der gemeinsame Punkt aller Geraden – der Leuchtturm']],
        'bild': ko([-3, 5], [-2, 7], schritt=0, graphen=[_g(-1, 4, 'm = −1'), _g(0.5, 2.5, 'm = 0,5'), _g(2, 1, 'm = 2')]),
        'schritte': [
            {'text': 'Büschel y = m · (x − 1) + 3. Setze x = 1.'},
            {'text': 'Die Klammer wird 0, also y = 3 für jedes m.'},
            {'text': 'Gemeinsamer Punkt: ⟦Z(1 | 3)⟧.', 'bild': {'punkte': pkte({'Z': (1, 3)})}},
            {'text': 'Durch Q(3 | 7): 7 = m · 2 + 3, also ⟦m = 2⟧.',
             'bild': {'punkte': pkte({'Z': (1, 3), 'Q': (3, 7)}), 'graphen': [_g(2, 1, 'm = 2')]}},
        ],
        'fehler': 'Z(−1 | 3) ist falsch. Die Klammer (x − 1) wird null bei ⟦x = +1⟧, das Vorzeichen dreht sich um.',
        'fehler_bild': {'punkte': pkte({'Z': (1, 3), 'falsch': (-1, 3)}),
                        'graphen': [_g(-1, 4, 'm = −1'), _g(0.5, 2.5, 'm = 0,5'), _g(2, 1, 'm = 2')]},
        'regel': 'Parameter in der Steigung: Alle Geraden gehen durch einen Punkt Z. Z liegt dort, wo der Parameter ⟦keinen Einfluss⟧ hat.',
    },
    'wirkung': {
        'einstieg': 'Ein Schieberegler in einer Mathe-App verändert die Zahl k. Je nachdem, wo k steht, '
                    '⟦dreht⟧ sich die Gerade oder sie rutscht hoch und runter.',
        'woerter': [['Faktor vor x', 'die ganze Zahl oder Klammer, mit der x malgenommen wird – die Steigung'],
                    ['parallel zur x-Achse', 'waagrecht, Steigung 0']],
        'bild': ko([-3, 3], [-4, 6], schritt=0, graphen=[_g(-2, 1, 'k = 0'), _g(0, 1, 'k = 2'), _g(2, 1, 'k = 4')]),
        'schritte': [
            {'text': 'In y = (k − 2)x + 1 steht k im Faktor vor x.'},
            {'text': 'Das Zahlglied ist immer 1: Alle Geraden gehen durch (0 | 1).', 'bild': {'punkte': pkte({'(0|1)': (0, 1)})}},
            {'text': 'Parallel zur x-Achse heißt Steigung 0: k − 2 = 0, ⟦k = 2⟧.', 'bild': {'graphen': [_g(0, 1, 'k = 2')]}},
            {'text': 'Fallend heißt k − 2 < 0, also ⟦k < 2⟧.', 'bild': {'graphen': [_g(-2, 1, 'k = 0'), _g(-1, 1, 'k = 1')]}},
        ],
        'fehler': '„k ist die Steigung“ ist falsch. Die Steigung ist der ⟦ganze Faktor vor x⟧: für k = 5 also 3, nicht 5.',
        'fehler_bild': {'graphen': [_g(3, 1, 'k = 5')]},
        'regel': 'Schau, wo der Parameter steht. Vor dem x ⟦dreht⟧ er die Gerade, als Zahlglied verschiebt er sie.',
    },
    'loesung_parameter': {
        'einstieg': 'Taxi A kostet 4 € Grundgebühr und 2 € pro Kilometer. Taxi B hat keine Grundgebühr, aber k € pro Kilometer. '
                    'Ab wann sind beide gleich teuer? Das hängt von k ab.',
        'woerter': [['Schnittpunkt', 'die Stelle, an der beide Taxis gleich viel kosten'],
                    ['durch 0', 'durch null teilen ist verboten; dann gibt es keine Lösung']],
        'bild': _taxi(graphen=[_g(2, 4, 'A'), _g(4, 0, 'k = 4')]),
        'schritte': [
            {'text': 'Gleich teuer: 2x + 4 = kx, also (k − 2) · x = 4.'},
            {'text': 'Lösung: x = 4 : (k − 2).'},
            {'text': 'Für k = 4: x = 4 : 2 = ⟦2⟧. Schnittpunkt bei 2 km.', 'bild': {'punkte': pkte({'S': (2, 8)})}},
            {'text': 'Für k = 2 teilst du durch 0: ⟦keine Lösung⟧, die Geraden sind parallel.',
             'bild': {'punkte': None, 'graphen': [_g(2, 4, 'A'), _g(2, 0, 'k = 2')]}},
        ],
        'fehler': 'Nur „x = 4 : (k − 2)“ hinschreiben ist unvollständig. Für ⟦k = 2⟧ ist das Teilen verboten, es gibt keine Lösung.',
        'regel': 'Vor dem Teilen prüfen: Wann ist der Term mit k gleich 0? Dann gibt es ⟦keine Lösung⟧.',
    },
    'sachaufgabe': {
        'einstieg': 'Ein Taxi kostet 4 € Grundgebühr und einen unbekannten Preis pro Kilometer. Für 10 km hast du 24 € bezahlt. '
                    'Diese Angabe ist eine ⟦Bedingung⟧: Mit ihr berechnest du den Kilometerpreis.',
        'woerter': [['Grundgebühr', 'Betrag, den man immer zahlt, auch für 0 km'],
                    ['Bedingung', 'eine bekannte Angabe, mit der man den Parameter ausrechnet']],
        'bild': ko([0, 12], [0, 30], schritt=0, schritt_x=2, schritt_y=5, name_x='km', name_y='€', punkte=pkte({'Start': (0, 4)})),
        'schritte': [
            {'text': 'Der Tarif ist y = m · x + 4, gesucht ist m.'},
            {'text': 'Bedingung einsetzen: 24 = m · 10 + 4.', 'bild': {'punkte': pkte({'Start': (0, 4), 'P': (10, 24)})}},
            {'text': '4 abziehen: 20 = 10m, also ⟦m = 2⟧.', 'bild': {'graphen': [_g(2, 4, 'm = 2')]}},
            {'text': 'Kontrolle: 2 · 10 + 4 = 24. Es stimmt.'},
        ],
        'fehler': '24 : 10 = 2,40 € pro km ist falsch. Die ⟦Grundgebühr⟧ von 4 € steckt im Preis und muss zuerst weg.',
        'fehler_bild': {'graphen': [_g(2, 4, 'richtig'), _g(2.4, 0, 'falsch')]},
        'regel': 'Bedingung in den Tarif einsetzen und nach dem Parameter auflösen. Die ⟦Grundgebühr⟧ zuerst abziehen.',
    },
}
UMBAU_OFFEN = []
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-1) ----------
# Prüfungsvorbilder: Jahrgangsstufentest 8 I und Realschul-Abschlussprüfung Mathematik I (Bayern): Geradenscharen, Parameter aus
# einer Punktprobe bestimmen, gemeinsamer Punkt eines Büschels nach Umformen, Tarifvergleich mit zwei Bedingungen.
# Typ übernommen, Wortlaut und Zahlen eigen.
def durchsicht(d):
    from _rsib1 import Z, A, L, nachtrag, finde
    T = lambda teil: finde(d, teil)
    LT, HT = '□x + □', 'Tippe den Term ein, z. B. 3x − 2.'
    nachtrag(d,
        umstufen={
            T('Welche Gleichung gehört in der Schar y = 3x + k zu k = 5?'): 1,
            T('Welche Gleichung gehört in der Schar y = −2x + k zu k = 1?'): 1,
            T('Liegt der Punkt P(−6 | −26)'): 2,
            T('Liegt der Punkt P(−4 | 1)'): 2,
            T('Welchen Punkt haben alle Geraden der Schar y = m · (x − 2) + 4 gemeinsam?'): 1,
            T('Löse (k + 2) · x = 4k für k = −4.'): 2,
            T('Ein Handwerker berechnet 50 € Anfahrt plus m € pro Stunde. Für 4 Stunden bezahlt man 290 €.'): 2,
            T('Ein Fahrradverleih nimmt 2 € Grundgebühr plus m € pro Stunde. Für 4 Stunden bezahlt man 14 €. Wie hoch'): 2,
        },
        ersetzen={
            T('Liegt der Punkt P(−2 | −4)'):
                A(3, 'Liegt der Punkt P(0 | 5) auf irgendeiner Geraden der Schar y = k · x + 3?',
                  'Nein: Bei x = 0 ist y immer 3.', ['Ja, für k = 5.', 'Ja, für k = 2.', 'Ja, für jedes k.'],
                  'Setze x = 0 ein: y = k · 0 + 3 = 3 – für jedes k. Der Punkt (0 | 5) liegt auf keiner Geraden der Schar.',
                  'Was passiert mit k · x, wenn x = 0 ist?'),
            T('Liegt der Punkt P(1 | −18)'):
                L(3, 'In der Schar y = k · x − 1 gehört zu k = 1,5 eine Gerade. Gib die Gerade der Schar an, die doppelt so steil ist.',
                  LT, [3, -1], ['2*1.5', '-1'], 'Doppelt so steil: Steigung 2 · 1,5 = 3, also k = 3. Die Gerade: y = 3x − 1.',
                  'Welche Zahl in der Gleichung ist die Steigung?', hinweis=HT),
            T('Jemand rechnet für die Schar y = 2,5x + t und P(4 | −1)'):
                Z(3, 'Zwei Geraden der Schar y = −x + t gehen durch P(1 | 4) bzw. Q(3 | 1). Um wie viel unterscheiden sich ihre y-Achsenabschnitte?',
                  1, '(4 + 1) - (1 + 3)', 'Durch P: 4 = −1 + t, t = 5. Durch Q: 1 = −3 + t, t = 4. Unterschied 5 − 4 = 1.',
                  'Bestimme t für jeden Punkt einzeln.'),
            T('Ein Handwerker berechnet 40 € Anfahrt plus m € pro Stunde. Für 4 Stunden bezahlt man 240 €.'):
                Z(3, 'Ein Handwerker berechnet eine feste Anfahrt plus einen Stundenlohn. 4 Stunden kosten 290 €, 6 Stunden kosten 410 €. Wie hoch ist die Anfahrt?',
                  50, '290 - 4*(410 - 290)/2', '2 Stunden mehr kosten 120 € mehr: Stundenlohn 60 €. Anfahrt: 290 − 4 · 60 = 50 €.',
                  'Was kosten die 2 zusätzlichen Stunden?', einheit='€'),
            T('Ein Stromtarif kostet 12 € Grundgebühr im Monat plus m € pro kWh. Für 250 kWh bezahlt man 74,50 €. Wie hoch'):
                Z(3, 'Ein Stromtarif kostet 12 € Grundgebühr im Monat plus 0,25 € pro kWh. Eine Familie zahlt 74,50 €. Wie viele kWh hat sie verbraucht?',
                  250, '(74.5 - 12)/0.25', 'Ohne Grundgebühr: 74,50 − 12 = 62,50 €. 62,50 : 0,25 = 250 kWh.',
                  'Zieh zuerst die Grundgebühr ab.', einheit='kWh'),
        },
        neu={
            'einsetzen': [
                Z(3, 'Für welchen Wert von k geht die Gerade der Schar y = k · x + 2 durch den Punkt P(4 | 14)?',
                  3, '(14 - 2)/4', 'P einsetzen: 14 = k · 4 + 2 ⇒ 4k = 12 ⇒ k = 3.', 'Setze die Koordinaten von P ein und löse nach k auf.'),
                Z(3, 'Gegeben ist die Schar y = (k − 1) · x + 2k. Für welches k geht die Gerade durch P(2 | 10)?',
                  3, '(10 + 2)/4', 'Einsetzen: 10 = (k − 1) · 2 + 2k = 2k − 2 + 2k = 4k − 2 ⇒ 4k = 12 ⇒ k = 3.',
                  'Setze x = 2 und y = 10 ein, multipliziere die Klammer aus.'),
                A(3, 'Gegeben ist die Schar y = k · x + 3. Für welche k liegt der y-Wert an der Stelle x = 2 über 9?',
                  'für k > 3', ['für k < 3', 'für k > 9', 'für k > 6'],
                  'An der Stelle 2: y = 2k + 3 > 9 ⇒ 2k > 6 ⇒ k > 3.', 'Setze x = 2 ein und vergleiche mit 9.'),
                Z(3, 'Die Geraden der Schar y = k · x + 1 zu k = 2 und zu k = −2 werden gezeichnet. An welcher Stelle x haben beide denselben y-Wert?',
                  0, '0', '2x + 1 = −2x + 1 ⇒ 4x = 0 ⇒ x = 0. Alle Geraden der Schar gehen durch (0 | 1).',
                  'Setze die beiden Terme gleich.'),
                Z(3, 'Taxi-Tarif y = k · x + 2 (x in km, y in €). In Stadt A kosten 5 km genau 17 €. Wie viel kosten dort 8 km?',
                  26, '(17 - 2)/5*8 + 2', '17 = 5k + 2 ⇒ k = 3. Für 8 km: 3 · 8 + 2 = 26 €.',
                  'Bestimme zuerst k für Stadt A.', einheit='€'),
                Z(3, 'Gegeben ist die Schar y = k · x + 4. Um wie viel ist bei x = 4 der y-Wert für k = 5 größer als für k = 3?',
                  8, '(5 - 3)*4', 'k = 5: 24, k = 3: 16. Unterschied 8 = (5 − 3) · 4. Die 4 fällt weg.',
                  'Rechne beide y-Werte aus – oder überlege, was sich ändert.'),
            ],
            'parallelenschar': [
                Z(3, 'Für welches t schneidet die Gerade der Schar y = 0,5x + t die x-Achse bei x = 6?',
                  -3, '0 - 0.5*6', 'Schnitt mit der x-Achse heißt y = 0: 0 = 0,5 · 6 + t ⇒ t = −3.', 'Welchen y-Wert hat ein Punkt auf der x-Achse?'),
                L(3, 'Eine Gerade der Schar y = 2x + t liegt 3 Einheiten unterhalb der Geraden y = 2x + 1. Gib ihre Gleichung an.',
                  LT, [2, -2], ['2', '1 - 3'], 'Gleiche Steigung 2, y-Achsenabschnitt 1 − 3 = −2: y = 2x − 2.',
                  'Parallele Geraden unterscheiden sich nur im y-Achsenabschnitt.', hinweis=HT),
            ],
            'bueschel': [
                L(3, 'Alle Geraden der Schar y = m · x + 2m − 1 gehen durch einen gemeinsamen Punkt Z. Gib Z an.',
                  'Z(□ | □)', [-2, -1], ['-2', '-1'], 'Umformen: y = m · (x + 2) − 1. Für x = −2 wird die Klammer 0, dann ist y = −1: Z(−2 | −1).',
                  'Klammere m aus: m · x + 2m = m · (x + 2).'),
                L(3, 'Welche Gerade des Büschels y = m · (x − 1) + 3 geht durch den Ursprung?',
                  LT, [3, 0], ['3', '0'], 'O(0 | 0) einsetzen: 0 = m · (−1) + 3 ⇒ m = 3. Gerade: y = 3 · (x − 1) + 3 = 3x.',
                  'Setze x = 0 und y = 0 ein.', hinweis='Tippe den Term ein, z. B. 3x + 0 oder 3x.'),
                Z(3, 'Für welches m schneidet die Gerade des Büschels y = m · (x − 2) + 4 die x-Achse bei x = 4?',
                  -2, '-4/2', 'Punkt (4 | 0) einsetzen: 0 = m · 2 + 4 ⇒ m = −2.', 'Welcher Punkt liegt bei x = 4 auf der x-Achse?'),
            ],
            'wirkung': [
                A(3, 'Für welche k steigt die Gerade der Schar y = (2k − 6) · x + 1 steiler an als y = 2x?',
                  'für k > 4', ['für k > 3', 'für k > 2', 'für k > 8'],
                  'Steigung 2k − 6 > 2 ⇒ 2k > 8 ⇒ k > 4.', 'Vergleiche die Steigung 2k − 6 mit 2.'),
                A(3, 'Gibt es in der Schar y = k · x + k eine Gerade durch den Ursprung?',
                  'Ja, für k = 0: Das ist die x-Achse.', ['Nein, alle schneiden die y-Achse bei k.', 'Ja, für jedes k.', 'Ja, für k = 1.'],
                  'Durch (0 | 0): 0 = k · 0 + k ⇒ k = 0. Dann lautet die Gleichung y = 0 – die x-Achse.',
                  'Hier steckt k auch im y-Achsenabschnitt.'),
            ],
            'loesung_parameter': [
                Z(3, 'Für welches k schneiden sich die Geraden y = 2x + 4 und y = k · x genau bei x = 4?',
                  3, '(2*4 + 4)/4', 'Bei x = 4 hat die erste Gerade y = 12. Dann muss 12 = k · 4 sein, also k = 3.',
                  'Welchen y-Wert hat die erste Gerade bei x = 4?'),
                Z(3, 'Für welches k hat die Gleichung (k − 2) · x = k − 2 unendlich viele Lösungen?',
                  2, '2', 'Für k = 2 steht da 0 · x = 0. Das stimmt für jedes x: unendlich viele Lösungen. Für k ≠ 2 ist x = 1 die einzige Lösung.',
                  'Setze den Wert ein, für den die Klammer 0 wird. Was steht dann da?'),
                A(3, 'Für welche k ist die Lösung der Gleichung (k + 1) · x = 6 positiv?',
                  'für k > −1', ['für k > 0', 'für k < −1', 'für k > 6'],
                  'x = 6 : (k + 1) ist positiv, wenn k + 1 positiv ist: k > −1.', 'Wann ist 6 geteilt durch eine Zahl positiv?'),
            ],
            'sachaufgabe': [
                Z(3, 'Handytarif A: 5 € im Monat plus 0,10 € pro Minute. Tarif B: keine Grundgebühr, 0,15 € pro Minute. Wie viel spart man mit A bei 300 Minuten?',
                  10, '0.15*300 - (5 + 0.1*300)', 'A: 5 + 0,10 · 300 = 35 €. B: 0,15 · 300 = 45 €. Ersparnis 10 €.',
                  'Rechne beide Tarife für 300 Minuten aus.', einheit='€'),
                Z(3, 'Ein Taxi hat eine Grundgebühr und einen festen Kilometerpreis. 8 km kosten 22 €, 12 km kosten 30 €. Wie hoch ist die Grundgebühr?',
                  6, '22 - 8*(30 - 22)/4', '4 km mehr kosten 8 € mehr: 2 € pro km. Grundgebühr: 22 − 8 · 2 = 6 €.',
                  'Was kosten die 4 zusätzlichen Kilometer?', einheit='€'),
                L(3, 'Ein Fahrradverleih hat einen festen Tarif: Für 3 Stunden zahlt man 17 €, für 5 Stunden 25 €. Gib den Tarif als y = m · x + t an (x in Stunden, y in €).',
                  LT, [4, 5], ['(25 - 17)/2', '17 - 3*4'], '2 Stunden mehr kosten 8 € mehr: m = 4. t = 17 − 3 · 4 = 5. y = 4x + 5.',
                  'Bestimme m aus dem Unterschied, dann t.', hinweis=HT),
                Z(3, 'Ein Taxiunternehmen erhöht den Kilometerpreis um 0,50 € und senkt die Grundgebühr um 3 €. Bei wie vielen Kilometern kostet eine Fahrt genauso viel wie vorher?',
                  6, '3/0.5', 'Pro Kilometer kommen 0,50 € dazu, insgesamt fallen 3 € weg. Gleich viel: 0,5 · x = 3 ⇒ x = 6 km. Ab mehr als 6 km wird es teurer.',
                  'Wie viele Kilometer braucht es, bis die 3 € wieder „aufgefressen“ sind?', einheit='km'),
            ],
        })


if __name__ == '__main__':
    d = bauen('funktionen.scharen',
          'Geradenscharen mit Parameter verstehen: Parameter einsetzen und bestimmen, Parallelenscharen und Geradenbüschel erkennen, parameterabhängige Lösungen untersuchen.',
          ['Ein Parameter ist eine frei wählbare Zahl; jeder Wert liefert eine Gerade der Schar.',
           'y = m · x + t mit Parameter t: parallele Geraden. Mit Parameter m: Geradenbüschel durch einen gemeinsamen Punkt.',
           'Parameter bestimmen: Punkt einsetzen und nach dem Parameter auflösen.',
           'Nie durch null teilen: Wird der Faktor vor x null, gibt es keine oder unendlich viele Lösungen.'],
          [('Scharen kennenlernen', ['einsetzen', 'parallelenschar', 'bueschel']),
           ('Parameter untersuchen', ['wirkung', 'loesung_parameter', 'sachaufgabe'])],
          ETAPPEN, GEN,
          offen=['Lehrplan-Feld leer: Annahme RS 8 (WPF I) = Scharen linearer Funktionen (Parallelenschar, Geradenbüschel), Parameter bestimmen, parameterabhängige Lösungen linearer Gleichungen. Scharen quadratischer Funktionen (RS 9) weggelassen.',
                 'Schreibweise der Scharen: g_k bzw. „Schar y = k · x + 2“; Indizes wie g₋₃ nur in der Erklärung.'])
    umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
    durchsicht(d)
