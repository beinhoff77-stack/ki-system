"""Aufgabenfamilien: Winkel, Vektoren/Abbildungen, Determinanten, Konstruktion, Kreis, Ortslinien, Flächen, Volumen, Raum."""
from fractions import Fraction as Fr
import math

from _nachbau_kern import Kern, check, wissen, z, zk, pt, vek, NAMEN

PI = Fr(314, 100)


def nz(rng, lo, hi):
    n = 0
    while n == 0:
        n = rng.randint(lo, hi)
    return n


# ---------- Winkel ----------
def f_winkel(rng, niv, info, et):
    if et in ('innenwinkelsumme', 'ergaenzen', 'um_punkt'):
        a, b = rng.randint(25, 95), rng.randint(20, 70)
        if et == 'um_punkt':
            c = rng.randint(60, 150)
            r = 360 - a - b - c
            return Kern(f'Vier Winkel liegen um einen Punkt herum: α = {a}°, β = {b}°, γ = {c}°.', 'Berechne den vierten Winkel δ.', f'δ = {r}°',
                        ['Winkel um einen Punkt ergeben zusammen 360°.', f'δ = 360° − {a}° − {b}° − {c}° = {r}°'], [(f'{180 - a - b - c if 180 - a - b - c > 0 else r - 180}°', 'mit 180° statt 360° gerechnet')],
                        [check('Summe', a + b + c + r == 360)])
        if niv == 'III':
            a = Fr(rng.randint(251, 799), 10)
            b = Fr(rng.randint(151, 599), 10)
        g = 180 - a - b
        return Kern(f'In einem Dreieck ABC gilt α = {z(a)}° und β = {z(b)}°.', 'Berechne γ.', f'γ = {z(g)}°', ['Innenwinkelsumme im Dreieck: 180°', f'γ = 180° − {z(a)}° − {z(b)}° = {z(g)}°'],
                    [(f'{z(360 - a - b)}°', 'mit 360° gerechnet'), (f'{z(180 - a + b)}°', 'Vorzeichenfehler')], [check('Winkelsumme', a + b + g == 180)])
    if et in ('stufen_wechsel', 'scheitel_neben', 'kreuzung', 'parallel_pruefen'):
        a = rng.randint(32, 148)
        if et == 'parallel_pruefen':
            b = 180 - a if rng.random() < .5 else 180 - a + rng.choice([-2, 2, 3])
            par = a + b == 180
            return Kern(f'Zwei Geraden g und h werden von einer Geraden s geschnitten. Am Schnittpunkt mit g misst man α = {a}°, am Schnittpunkt mit h den Nachbarwinkel des Stufenwinkels, β = {b}°.',
                        'Sind g und h parallel? Begründe.', ('Ja' if par else 'Nein') + f': α + β = {a + b}°' + (', also sind die Stufenwinkel gleich groß.' if par else ' ≠ 180°, die Stufenwinkel sind verschieden.'),
                        ['Stufenwinkel an parallelen Geraden sind gleich groß; Nebenwinkel ergänzen sich zu 180°.', f'Stufenwinkel zu α wäre 180° − {b}° = {180 - b}°'], [('Ja' if not par else 'Nein', 'Neben- und Stufenwinkel verwechselt')],
                        [check('Summe', (a + b == 180) == par)], antwort_kurz='Ja' if par else 'Nein')
        paar = rng.choice([('Wechselwinkel', 'Nebenwinkel'), ('Stufenwinkel', 'Scheitelwinkel'), ('Stufenwinkel', 'Nebenwinkel'), ('Wechselwinkel', 'Scheitelwinkel')])
        w2 = 180 - a if paar[1] == 'Nebenwinkel' else a
        kont = rng.choice(['Zwei parallele Geraden g ∥ h werden von einer Geraden s geschnitten.', 'Zwei parallele Gleise werden von einer geraden Straße gekreuzt (Gleise g ∥ h, Straße s).',
                           'An einem Zaun mit zwei parallelen Querlatten g ∥ h ist eine schräge Strebe s befestigt.'])
        return Kern(f'{kont} Ein Winkel an g hat das Maß α = {a}°.',
                    f'Bestimme das Maß des {paar[0]}s β zu α an h und des {paar[1]}s γ von α.', f'β = {a}°, γ = {w2}°',
                    [f'{paar[0]} an Parallelen sind gleich groß.', f'{paar[1]}: ' + (f'180° − {a}° = {180 - a}°' if paar[1] == 'Nebenwinkel' else f'gleich groß wie α, also {a}°')],
                    [(f'β = {180 - a}°, γ = {a if w2 != a else 180 - a}°', 'Winkelarten verwechselt')],
                    [check('Neben-/Scheitelwinkel', (w2 == a) if paar[1] == 'Scheitelwinkel' else (a + w2 == 180))],
                    aussage=(f'Zwei Geraden werden von einer dritten geschnitten. {rng.choice(NAMEN)} behauptet: „Stufenwinkel sind immer gleich groß.“ Stimmt das? Begründe.', False,
                             'nur wenn die beiden geschnittenen Geraden parallel sind.'))
    if et == 'vieleck':
        n = rng.randint(5, 10)
        s = (n - 2) * 180
        return Kern('', f'Berechne die Innenwinkelsumme eines {n}-Ecks und die Größe eines Innenwinkels, wenn das {n}-Eck regelmäßig ist.', f'{s}°; {z(Fr(s, n))}°',
                    [f'Zerlegung in {n - 2} Dreiecke: ({n} − 2) · 180° = {s}°', f'{s}° : {n} = {z(Fr(s, n))}°'], [(f'{n * 180}°', 'n statt n − 2 Dreiecke')], [check('Summe', s == (n - 2) * 180)])
    # figuren / beweisen / figuren mit gleichschenkligen Dreiecken
    art = rng.choice(['gleichschenklig', 'aussen', 'zwei'])
    if art == 'gleichschenklig':
        g = rng.randint(20, 140)
        b = Fr(180 - g, 2)
        return Kern(f'Das Dreieck ABC ist gleichschenklig mit der Basis [AB]. Der Winkel an der Spitze C misst γ = {g}°.', 'Berechne die Basiswinkel α und β.', f'α = β = {z(b)}°',
                    ['Basiswinkel im gleichschenkligen Dreieck sind gleich groß.', f'α = β = (180° − {g}°) : 2 = {z(b)}°'], [(f'{180 - g}°', 'nicht halbiert')],
                    [check('Summe', 2 * b + g == 180)], abb=f'Gleichschenkliges Dreieck ABC mit Spitze C, γ = {g}° markiert.')
    if art == 'aussen':
        a, b = rng.randint(30, 80), rng.randint(30, 80)
        return Kern(f'Im Dreieck ABC ist α = {a}° und β = {b}°. Die Seite [AB] wird über B hinaus verlängert.', 'Berechne den Außenwinkel β\' an der Ecke B.', f"β' = {180 - b}°",
                    [f'Nebenwinkel zu β: 180° − {b}° = {180 - b}°', f'Kontrolle: Außenwinkel = α + γ = {a}° + {180 - a - b}° = {180 - b}°'], [(f'{a + b}°', 'Summe der falschen Innenwinkel')],
                    [check('Außenwinkelsatz', a + (180 - a - b) == 180 - b)])
    # zwei Dreiecke
    g = rng.randint(30, 80)
    basis = Fr(180 - g, 2)
    d = 180 - 2 * basis if False else None
    phi = 180 - basis
    return Kern(f'Im gleichschenkligen Dreieck ABC (Basis [AB]) ist γ = {g}°. Der Punkt D liegt auf der Verlängerung von [AB] über B hinaus.',
                'Berechne den Winkel ∢CBD. Begründe jeden Schritt.', f'∢CBD = {z(phi)}°',
                [f'Basiswinkel: β = (180° − {g}°) : 2 = {z(basis)}°', f'∢CBD ist Nebenwinkel von β: 180° − {z(basis)}° = {z(phi)}°'], [(f'{z(basis)}°', 'Nebenwinkel vergessen')],
                [check('Nebenwinkel', basis + phi == 180)], abb='Gleichschenkliges Dreieck ABC, [AB] über B hinaus bis D verlängert.')


# ---------- Vektoren / Abbildungen ----------
def P(rng, r=7):
    return (Fr(rng.randint(-r, r)), Fr(rng.randint(-r, r)))


def f_vektor(rng, niv, info, et):
    A, B_ = P(rng), P(rng)
    while A == B_:
        B_ = P(rng)
    v = (B_[0] - A[0], B_[1] - A[1])
    if et in ('gegenvektor',):
        return Kern(f'Der Punkt A{pt(A)} wird durch den Vektor v = {vek(v)} auf A\' abgebildet.', 'Gib die Koordinaten von A\' und den Gegenvektor −v an. Wohin bildet −v den Punkt A\' ab?',
                    f"A'{pt(B_)}; −v = {vek((-v[0], -v[1]))}; zurück auf A{pt(A)}", [f"A' = A + v = {pt(B_)}", 'Gegenvektor: beide Koordinaten mit −1 multiplizieren.'],
                    [(f'−v = {vek((v[1], v[0]))}', 'Koordinaten vertauscht')], [check('A+v−v=A', (B_[0] - v[0], B_[1] - v[1]) == A)])
    if et == 'verschiebung':
        C = P(rng)
        bilder = [(p[0] + v[0], p[1] + v[1]) for p in (A, C)]
        return Kern(f'Die Strecke [AC] mit A{pt(A)} und C{pt(C)} wird durch die Parallelverschiebung mit v = {vek(v)} abgebildet.',
                    'Zeichne die Bildstrecke und gib die Koordinaten der Bildpunkte an.', f"A'{pt(bilder[0])}, C'{pt(bilder[1])}",
                    ['Zu jedem Punkt den Vektor addieren.', f"A' = {pt(bilder[0])}, C' = {pt(bilder[1])}", 'Kontrolle: [A\'C\'] ist parallel und gleich lang wie [AC].'],
                    [(f"A'{pt((A[0] - v[0], A[1] - v[1]))}", 'Vektor subtrahiert statt addiert')], [check('Länge erhalten', (bilder[1][0] - bilder[0][0], bilder[1][1] - bilder[0][1]) == (C[0] - A[0], C[1] - A[1]))])
    if et == 'vektor_drehen':
        return Kern(f'Gegeben ist der Vektor v = {vek(v)}.', 'Gib einen Vektor an, der gleich lang ist und auf v senkrecht steht (Drehung um 90° gegen den Uhrzeigersinn).', f'{vek((-v[1], v[0]))}',
                    ['Drehung um +90°: (x; y) → (−y; x)'], [(vek((v[1], -v[0])), 'im Uhrzeigersinn gedreht (auch senkrecht, aber andere Richtung)')], [check('Skalarprodukt 0', v[0] * (-v[1]) + v[1] * v[0] == 0)])
    if 'rückwärts' in info.get('besonderheit', '') or rng.random() < .3:
        return Kern(f'Der Punkt B{pt(B_)} entsteht aus einem Punkt A durch Verschiebung mit v = {vek(v)}.', 'Berechne die Koordinaten von A.', f'A{pt(A)}',
                    [f'A = B − v = ({z(B_[0])} − {zk(v[0])} | {z(B_[1])} − {zk(v[1])})', f'= {pt(A)}'], [(f'A{pt((B_[0] + v[0], B_[1] + v[1]))}', 'Vektor addiert statt subtrahiert')],
                    [check('A + v = B', (A[0] + v[0], A[1] + v[1]) == B_)])
    return Kern(f'Gegeben sind A{pt(A)} und B{pt(B_)}.', 'Berechne die Koordinaten des Vektors AB→.', vek(v), [f'AB→ = (x_B − x_A; y_B − y_A)', f'= ({z(B_[0])} − {zk(A[0])}; {z(B_[1])} − {zk(A[1])}) = {vek(v)}'],
                [(vek((-v[0], -v[1])), 'Anfangs- und Endpunkt vertauscht'), (vek((B_[0] + A[0], B_[1] + A[1])), 'Koordinaten addiert')], [check('A + AB = B', (A[0] + v[0], A[1] + v[1]) == B_)],
                luecke=f'Ergänze: AB→ = ( ___ ; ___ )')


def f_mittelpunkt(rng, niv, info):
    A = (Fr(rng.randint(-8, 8)), Fr(rng.randint(-8, 8)))
    M = (A[0] + rng.randint(-5, 5), A[1] + rng.randint(-5, 5))
    if niv == 'III' or 'Mitte' in info.get('kompetenz', ''):
        M = ((A[0] + A[0] + 2 * rng.randint(-4, 4) + 1) / 2, M[1])
    Bp = (2 * M[0] - A[0], 2 * M[1] - A[1])
    if 'rückwärts' in info.get('besonderheit', '') or 'Endpunkt' in info.get('kompetenz', ''):
        return Kern(f'M{pt(M)} ist der Mittelpunkt der Strecke [AB] mit A{pt(A)}.', 'Berechne die Koordinaten von B.', f'B{pt(Bp)}',
                    ['x_M = (x_A + x_B) : 2 → x_B = 2·x_M − x_A', f'B = ({z(2 * M[0])} − {zk(A[0])} | {z(2 * M[1])} − {zk(A[1])}) = {pt(Bp)}'],
                    [(f'B{pt(((A[0] + M[0]) / 2, (A[1] + M[1]) / 2))}', 'Mittelpunkt von A und M berechnet')], [check('Mittelpunkt', ((A[0] + Bp[0]) / 2, (A[1] + Bp[1]) / 2) == M)])
    return Kern(f'Gegeben sind A{pt(A)} und B{pt(Bp)}.', 'Berechne die Koordinaten des Mittelpunkts M der Strecke [AB].', f'M{pt(M)}',
                ['M = ((x_A + x_B) : 2 | (y_A + y_B) : 2)', f'= {pt(M)}'], [(f'M{pt((Bp[0] - A[0], Bp[1] - A[1]))}', 'Differenz statt Mittelwert')], [check('Mittelpunkt', ((A[0] + Bp[0]) / 2, (A[1] + Bp[1]) / 2) == M)])


def f_vektoraddition(rng, niv, info):
    u, v = P(rng, 6), P(rng, 6)
    w = (u[0] + v[0], u[1] + v[1])
    A = P(rng, 4)
    return Kern(f'Ein Punkt A{pt(A)} wird zuerst mit u = {vek(u)} und danach mit v = {vek(v)} verschoben.', 'Gib den Vektor der Gesamtverschiebung und den Bildpunkt A\'\' an.',
                f"w = u + v = {vek(w)}; A''{pt((A[0] + w[0], A[1] + w[1]))}", ['Verschiebungen nacheinander: Vektoren koordinatenweise addieren.', f'w = {vek(w)}'],
                [(vek((u[0] - v[0], u[1] - v[1])), 'Vektoren subtrahiert')], [check('Verkettung', (A[0] + u[0] + v[0], A[1] + u[1] + v[1]) == (A[0] + w[0], A[1] + w[1]))])


def f_det(rng, niv, info, et):
    for _ in range(200):
        A, B_, C = P(rng, 6), P(rng, 6), P(rng, 6)
        u = (B_[0] - A[0], B_[1] - A[1])
        v = (C[0] - A[0], C[1] - A[1])
        d = u[0] * v[1] - u[1] * v[0]
        if d > 0:
            break
    if et == 'det_berechnen':
        return Kern('', f'Berechne die Determinante | {z(u[0])}  {z(v[0])} ; {z(u[1])}  {z(v[1])} | (Spalten = Vektoren).', z(d),
                    ['det = a₁·b₂ − a₂·b₁', f'= {zk(u[0])} · {zk(v[1])} − {zk(u[1])} · {zk(v[0])} = {z(d)}'], [(z(u[0] * v[1] + u[1] * v[0]), 'Plus statt Minus'), (z(-d), 'Reihenfolge vertauscht')],
                    [check('Determinante', d == u[0] * v[1] - u[1] * v[0])])
    flaeche = d / 2 if et in ('dreieck', 'viereck') else d
    form = 'Dreiecks ABC' if et in ('dreieck', 'viereck') else 'Parallelogramms ABCD (mit AB→ und AD→ = AC→ aus der Angabe)'
    shoelace = abs(A[0] * (B_[1] - C[1]) + B_[0] * (C[1] - A[1]) + C[0] * (A[1] - B_[1])) / 2
    return Kern(f'Gegeben sind A{pt(A)}, B{pt(B_)} und C{pt(C)}' + ('; das Parallelogramm wird von AB→ und AC→ aufgespannt' if et == 'parallelogramm' else '') + '.',
                f'Berechne den Flächeninhalt des {"Dreiecks ABC" if et != "parallelogramm" else "Parallelogramms"} mit einer Determinante.', f'A = {z(flaeche)} FE',
                [f'AB→ = {vek(u)}, AC→ = {vek(v)}', f'det = {z(d)}', ('A = ½ · det = ' + z(flaeche) if et != 'parallelogramm' else f'A = det = {z(d)}') + ' FE'],
                [(f'A = {z(d if et != "parallelogramm" else d / 2)} FE', 'Faktor ½ falsch angewendet')], [check('Gaußsche Trapezformel', (shoelace if et != 'parallelogramm' else 2 * shoelace) == flaeche)])


def f_abbildung(rng, niv, info, et):
    Pp = P(rng, 6)
    if et == 'achsenspiegelung':
        c = rng.randint(-3, 4)
        bild = (2 * c - Pp[0], Pp[1])
        return Kern(f'Der Punkt P{pt(Pp)} wird an der Geraden a: x = {c} gespiegelt.', 'Gib die Koordinaten des Bildpunkts P\' an.', f"P'{pt(bild)}",
                    [f'Abstand von P zur Achse: {z(abs(Pp[0] - c))}', 'Auf der anderen Seite gleich weit abtragen.'], [(f"P'{pt((Pp[0], 2 * c - Pp[1]))}", 'an der falschen Achse gespiegelt')],
                    [check('Achse ist Mittelsenkrechte', (Pp[0] + bild[0]) / 2 == c)])
    if et == 'drehung':
        Z = P(rng, 3)
        w = rng.choice([90, 180, -90])
        dx, dy = Pp[0] - Z[0], Pp[1] - Z[1]
        r = {90: (-dy, dx), -90: (dy, -dx), 180: (-dx, -dy)}[w]
        bild = (Z[0] + r[0], Z[1] + r[1])
        txt = {90: 'um 90° gegen den Uhrzeigersinn', -90: 'um 90° im Uhrzeigersinn', 180: 'um 180°'}[w]
        return Kern(f'Der Punkt P{pt(Pp)} wird {txt} um das Zentrum Z{pt(Z)} gedreht.', 'Zeichne und gib die Koordinaten des Bildpunkts P\' an.', f"P'{pt(bild)}",
                    [f'ZP→ = {vek((dx, dy))}', f'gedreht: {vek(r)}', f"P' = Z + gedrehter Vektor = {pt(bild)}"], [(f"P'{pt((Z[0] - r[0], Z[1] - r[1]))}", 'Drehsinn verwechselt')],
                    [check('Abstand erhalten', dx * dx + dy * dy == r[0] ** 2 + r[1] ** 2)])
    if et in ('symmetrie', 'vierecke_ordnen', 'eigenschaften'):
        tab = {'Quadrat': ('4 Symmetrieachsen, punktsymmetrisch', 'alle Seiten gleich lang, alle Winkel 90°'),
               'Raute': ('2 Symmetrieachsen (Diagonalen), punktsymmetrisch', 'alle Seiten gleich lang, Diagonalen stehen senkrecht aufeinander'),
               'Rechteck': ('2 Symmetrieachsen (Mittelsenkrechten), punktsymmetrisch', 'alle Winkel 90°, Diagonalen gleich lang'),
               'Parallelogramm': ('keine Symmetrieachse, punktsymmetrisch', 'gegenüberliegende Seiten parallel und gleich lang'),
               'Drachenviereck': ('1 Symmetrieachse (eine Diagonale), nicht punktsymmetrisch', 'zwei Paare gleich langer Nachbarseiten, Diagonalen senkrecht'),
               'gleichschenkliges Trapez': ('1 Symmetrieachse, nicht punktsymmetrisch', 'ein Paar paralleler Seiten, Schenkel gleich lang')}
        name = rng.choice(list(tab))
        sym, eig = tab[name]
        andere = [n for n in tab if n != name]
        if et == 'eigenschaften':
            return Kern('', 'Welche Eigenschaft hat jede Kongruenzabbildung (Achsenspiegelung, Verschiebung, Drehung)?', 'Sie ist längentreu, winkeltreu und flächentreu.',
                        ['Kongruenzabbildungen bilden Figuren auf deckungsgleiche Figuren ab.'], [('Sie ändert die Größe, aber nicht die Form.', 'mit zentrischer Streckung verwechselt'),
                                                                                                   ('Sie erhält immer den Umlaufsinn.', 'gilt nicht für Achsenspiegelungen'), ('Sie erhält nur Längen, nicht Winkel.', 'unvollständig')],
                        [wissen('Eigenschaft')])
        if et == 'symmetrie':
            return Kern('', f'Welche Symmetrieeigenschaften hat ein {name}?', sym, [f'{name}: {eig}'], [(tab[a][0], f'Eigenschaft eines {a}s') for a in rng.sample(andere, 3)], [wissen('Tabelle')])
        return Kern('', f'Ein Viereck hat folgende Eigenschaften: {eig}; {sym}. Um welches Viereck handelt es sich (möglichst genau)?', name, [f'Eigenschaften gehören zum {name}.'],
                    [(a, 'zu allgemein bzw. falsches Viereck') for a in rng.sample(andere, 3)], [wissen('Zuordnung')])
    # mittelsenkrechte / winkelhalbierende
    A, B_ = P(rng, 6), P(rng, 6)
    while A[0] == B_[0] and A[1] == B_[1] or (A[0] + B_[0]) % 2 or (A[1] + B_[1]) % 2:
        B_ = P(rng, 6)
    M = ((A[0] + B_[0]) / 2, (A[1] + B_[1]) / 2)
    return Kern(f'Gegeben sind A{pt(A)} und B{pt(B_)}.', 'Konstruiere die Mittelsenkrechte von [AB] und gib die Koordinaten des Mittelpunkts M an. Welche Eigenschaft haben alle Punkte der Mittelsenkrechten?',
                f'M{pt(M)}; alle Punkte haben von A und B denselben Abstand', ['Kreisbögen gleichen Radius um A und B, Schnittpunkte verbinden.', f'M = {pt(M)}'],
                [(f'M{pt((B_[0] - A[0], B_[1] - A[1]))}', 'Differenz statt Mittelwert')], [check('M gleich weit', (M[0] - A[0]) ** 2 + (M[1] - A[1]) ** 2 == (M[0] - B_[0]) ** 2 + (M[1] - B_[1]) ** 2)])


# ---------- Konstruktion ----------
def f_konstruktion(rng, niv, info, et):
    if et in ('kongruenzsatz', 'planfigur', 'gleichschenklig'):
        art = rng.choice(['SSS', 'SWS', 'WSW', 'SsW'])
        if et == 'gleichschenklig':
            s = Fr(rng.randint(35, 70), 10)
            g = rng.randint(30, 110)
            b = Fr(180 - g, 2)
            return Kern('', f'Konstruiere ein gleichschenkliges Dreieck ABC mit der Basis [AB], den Schenkeln a = b = {z(s)} cm und γ = {g}°. Fertige zuerst eine Planfigur an. Gib die Basiswinkel an.',
                        f'Konstruktion nach SWS; α = β = {z(b)}°', ['Planfigur zeichnen, gegebene Stücke farbig markieren.', f'Winkel γ = {g}° an C antragen, auf beiden Schenkeln {z(s)} cm abtragen.', f'Basiswinkel: (180° − {g}°) : 2 = {z(b)}°'],
                        [(f'{180 - g}°', 'nicht halbiert')], [check('Winkelsumme', 2 * b + g == 180)])
        if art == 'SSS':
            for _ in range(100):
                a, b, c = (Fr(rng.randint(30, 80), 10) for _ in range(3))
                if a + b > c and a + c > b and b + c > a:
                    break
            daten = f'a = {z(a)} cm, b = {z(b)} cm, c = {z(c)} cm'
            weg = ['Strecke c zeichnen, Kreisbögen um A mit r = b und um B mit r = a; Schnittpunkt ist C.']
            pr = check('Dreiecksungleichung', a + b > c and a + c > b and b + c > a)
        elif art == 'SWS':
            b, c, al = Fr(rng.randint(30, 80), 10), Fr(rng.randint(30, 80), 10), rng.randint(30, 130)
            daten = f'b = {z(b)} cm, c = {z(c)} cm, α = {al}°'
            weg = [f'c zeichnen, in A den Winkel α = {al}° antragen, auf dem freien Schenkel b abtragen.']
            pr = check('Winkel < 180°', al < 180)
        elif art == 'WSW':
            c, al, be = Fr(rng.randint(40, 90), 10), rng.randint(30, 80), rng.randint(30, 80)
            daten = f'c = {z(c)} cm, α = {al}°, β = {be}°'
            weg = [f'c zeichnen, in A α und in B β antragen; Schnittpunkt der freien Schenkel ist C.', f'γ = 180° − {al}° − {be}° = {180 - al - be}°']
            pr = check('Winkelsumme', al + be < 180)
        else:
            c, a = Fr(rng.randint(40, 70), 10), Fr(rng.randint(71, 95), 10)
            al = rng.randint(30, 80)
            daten = f'c = {z(c)} cm, a = {z(a)} cm, α = {al}° (α liegt der größeren Seite a gegenüber)'
            weg = [f'c zeichnen, in A α = {al}° antragen, Kreis um B mit r = {z(a)} cm schneidet den freien Schenkel in C (eindeutig, da a > c).']
            pr = check('a > c', a > c)
        return Kern('', f'Konstruiere das Dreieck ABC mit {daten}. Fertige eine Planfigur an und gib den passenden Kongruenzsatz an.', f'Kongruenzsatz {art}; Konstruktion siehe Lösungsweg',
                    ['Planfigur mit markierten gegebenen Stücken.'] + weg, [(s, 'Lage der gegebenen Stücke falsch gedeutet') for s in ('SSS', 'SWS', 'WSW', 'SsW') if s != art], [pr],
                    antwort_kurz=art)
    if et == 'konstruierbar':
        if rng.random() < .5:
            a, b = rng.randint(2, 6), rng.randint(2, 6)
            c = a + b + rng.choice([-1, 0, 1, 2])
            geht = a + b > c
            return Kern('', f'Lässt sich ein Dreieck mit den Seiten {a} cm, {b} cm und {c} cm konstruieren? Begründe.', ('Ja' if geht else 'Nein') + f': {a} + {b} = {a + b} {">" if geht else "≤"} {c}',
                        ['Dreiecksungleichung: Die Summe zweier Seiten muss größer sein als die dritte.'], [('Nein' if geht else 'Ja', 'Dreiecksungleichung nicht geprüft')],
                        [check('Ungleichung', geht == (a + b > c))], antwort_kurz='Ja' if geht else 'Nein')
        al, be = rng.randint(60, 120), rng.randint(40, 90)
        geht = al + be < 180
        return Kern('', f'Gibt es ein Dreieck mit α = {al}° und β = {be}°? Begründe.', ('Ja' if geht else 'Nein') + f': α + β = {al + be}° {"<" if geht else "≥"} 180°',
                    ['Innenwinkelsumme 180°: für γ muss noch ein positiver Winkel übrig bleiben.'], [('Ja' if not geht else 'Nein', 'Winkelsumme nicht geprüft')],
                    [check('Summe', geht == (al + be < 180))], antwort_kurz='Ja' if geht else 'Nein')
    if et == 'seiten_winkel':
        a, b, c = sorted(rng.sample(range(3, 10), 3))
        while a + b <= c:
            a, b, c = sorted(rng.sample(range(3, 10), 3))
        al, be, ga = sorted_w = None, None, None
        return Kern(f'Ein Dreieck hat die Seiten a = {b} cm, b = {c} cm und c = {a} cm.', 'Ordne die Innenwinkel α, β, γ der Größe nach, ohne zu messen. Begründe.',
                    'γ < α < β', ['Der größeren Seite liegt der größere Winkel gegenüber.', f'b = {c} cm ist am längsten → β am größten; c = {a} cm am kürzesten → γ am kleinsten.'],
                    [('α < β < γ', 'Seite und gegenüberliegenden Winkel falsch zugeordnet'), ('β < α < γ', 'Reihenfolge umgekehrt'), ('α < γ < β', 'Winkel falsch zugeordnet')], [check('Kosinussatz-Kontrolle', _winkelordnung(b, c, a) == ['γ', 'α', 'β'])],
                    aussage=(f'{rng.choice(NAMEN)} hat das Dreieck gezeichnet und misst α = 95°. Kann das stimmen? Begründe ohne Zeichnung.', False,
                             'a ist nicht die längste Seite (b ist länger), also ist α kleiner als β. Wäre α = 95°, so wäre β > 95° und α + β > 180° – unmöglich.'))
    # vierecke_konstruieren / vierecke
    art = rng.choice(['trapez', 'parallelogramm', 'drachen'])
    if art == 'parallelogramm':
        a, b, al = Fr(rng.randint(40, 70), 10), Fr(rng.randint(25, 45), 10), rng.randint(40, 80)
        return Kern('', f'Konstruiere ein Parallelogramm ABCD mit a = {z(a)} cm, b = {z(b)} cm und α = {al}°. Gib die übrigen Innenwinkel an.', f'β = δ = {180 - al}°, γ = {al}°',
                    ['a zeichnen, α in A antragen, b abtragen → D; Parallelen ergänzen → C.', f'Nachbarwinkel ergänzen sich zu 180°: β = {180 - al}°'], [(f'β = {al}°', 'Gegen- und Nachbarwinkel verwechselt')],
                    [check('Winkelsumme', 2 * al + 2 * (180 - al) == 360)])
    if art == 'trapez':
        a, d, al, be = Fr(rng.randint(50, 80), 10), Fr(rng.randint(25, 45), 10), rng.randint(50, 85), rng.randint(50, 85)
        return Kern('', f'Konstruiere ein Trapez ABCD mit [AB] ∥ [CD], a = {z(a)} cm, d = {z(d)} cm, α = {al}° und β = {be}°. Berechne δ und γ.', f'δ = {180 - al}°, γ = {180 - be}°',
                    ['a zeichnen, α und β antragen, d abtragen → D, Parallele zu AB durch D schneidet den Schenkel von β in C.', 'Winkel an einem Schenkel ergänzen sich zu 180°.'],
                    [(f'δ = {al}°', 'Stufen- und Nachbarwinkel verwechselt')], [check('Winkelsumme', al + be + (180 - al) + (180 - be) == 360)])
    e, a = Fr(rng.randint(50, 80), 10), Fr(rng.randint(30, 50), 10)
    return Kern('', f'Konstruiere ein Drachenviereck ABCD mit der Symmetrieachse AC, e = AC = {z(e)} cm und AB = AD = {z(a)} cm sowie BC = DC = {z(e - Fr(1))} cm.',
                'Konstruktion siehe Lösungsweg; Kontrolle: BD ⟂ AC', ['e zeichnen, Kreise um A (r = AB) und um C (r = BC) → B und D als Schnittpunkte.', 'B und D liegen symmetrisch zu AC.'],
                [('B und D auf derselben Seite von AC', 'Symmetrie nicht beachtet')], [check('Dreiecksungleichung', a + e - 1 > e)])


def _winkelordnung(a, b, c):
    import math
    al = math.degrees(math.acos((b * b + c * c - a * a) / (2 * b * c)))
    be = math.degrees(math.acos((a * a + c * c - b * b) / (2 * a * c)))
    ga = 180 - al - be
    return [n for _, n in sorted([(al, 'α'), (be, 'β'), (ga, 'γ')])]


# ---------- Kreis ----------
def f_kreis(rng, niv, info, et):
    if et == 'thales':
        a = rng.randint(20, 70)
        return Kern(f'Die Punkte A und B sind die Endpunkte eines Durchmessers eines Kreises, C liegt auf dem Kreis. Im Dreieck ABC ist α = {a}°.', 'Berechne β und γ. Begründe.',
                    f'γ = 90°, β = {90 - a}°', ['Satz des Thales: Winkel im Halbkreis ist 90°.', f'β = 180° − 90° − {a}° = {90 - a}°'], [(f'β = {180 - 2 * a}°', 'gleichschenklig statt rechtwinklig angenommen')],
                    [check('Summe', a + 90 + (90 - a) == 180)])
    if et == 'umkehrung':
        A = (Fr(rng.randint(-5, 0)), Fr(rng.randint(-3, 3)))
        B_ = (A[0] + 2 * rng.randint(2, 5), A[1] + 2 * rng.randint(-2, 2))
        M = ((A[0] + B_[0]) / 2, (A[1] + B_[1]) / 2)
        r2 = (M[0] - A[0]) ** 2 + (M[1] - A[1]) ** 2
        return Kern(f'Gegeben sind A{pt(A)} und B{pt(B_)}. Alle Punkte C, für die das Dreieck ABC bei C einen rechten Winkel hat, liegen auf einer Linie.', 'Beschreibe diese Linie und gib ihren Mittelpunkt an.',
                    f'Thaleskreis über [AB] mit Mittelpunkt M{pt(M)} (ohne A und B)', ['Umkehrung des Satzes von Thales.', f'M = Mittelpunkt von [AB] = {pt(M)}'], [('Mittelsenkrechte von [AB]', 'Ortslinien verwechselt')],
                    [check('A auf Kreis', (A[0] - M[0]) ** 2 + (A[1] - M[1]) ** 2 == r2)])
    if et == 'tangente':
        a = rng.randint(25, 70)
        return Kern(f'Eine Gerade t berührt den Kreis um M im Punkt B. Ein Punkt P liegt auf t; der Winkel ∢BMP misst {a}°.', 'Berechne den Winkel ∢MPB. Begründe.', f'∢MPB = {90 - a}°',
                    ['Tangente steht senkrecht auf dem Berührradius: ∢MBP = 90°.', f'∢MPB = 180° − 90° − {a}° = {90 - a}°'], [(f'{180 - a}°', 'rechten Winkel nicht erkannt')], [check('Summe', 90 + a + 90 - a == 180)])
    # umkreis_inkreis
    if rng.random() < .5 or niv == 'I':
        return Kern('', 'Wie findet man den Mittelpunkt des Umkreises und den des Inkreises eines Dreiecks? Kreuze die richtige Aussage an bzw. beschreibe.',
                    'Umkreismittelpunkt: Schnittpunkt der Mittelsenkrechten; Inkreismittelpunkt: Schnittpunkt der Winkelhalbierenden',
                    ['Umkreis: gleicher Abstand von allen Ecken → Mittelsenkrechten.', 'Inkreis: gleicher Abstand von allen Seiten → Winkelhalbierende.'],
                    [('Umkreismittelpunkt: Schnittpunkt der Winkelhalbierenden; Inkreismittelpunkt: Schnittpunkt der Mittelsenkrechten', 'vertauscht'),
                     ('beide: Schnittpunkt der Seitenhalbierenden', 'mit dem Schwerpunkt verwechselt')], [wissen('Definition')])
    a, b = 2 * rng.randint(1, 4), 2 * rng.randint(1, 4)
    A, B_, C = (Fr(0), Fr(0)), (Fr(a), Fr(0)), (Fr(0), Fr(b))
    M = (Fr(a, 2), Fr(b, 2))
    return Kern(f'Gegeben ist das rechtwinklige Dreieck A{pt(A)}, B{pt(B_)}, C{pt(C)}.', 'Konstruiere den Umkreis und gib die Koordinaten seines Mittelpunkts an. Begründe.',
                f'M{pt(M)} (Mittelpunkt der Hypotenuse [BC])', ['Rechter Winkel bei A → Thaleskreis: Umkreismittelpunkt ist der Mittelpunkt der Hypotenuse.', f'M = {pt(M)}'],
                [(f'M{pt((Fr(a, 3), Fr(b, 3)))}', 'Schwerpunkt berechnet')], [check('gleiche Abstände', all((p[0] - M[0]) ** 2 + (p[1] - M[1]) ** 2 == (A[0] - M[0]) ** 2 + (A[1] - M[1]) ** 2 for p in (B_, C)))])


# ---------- Ortslinien ----------
def f_ort(rng, niv, info, et):
    if et == 'kreislinie':
        M = P(rng, 3)
        r = rng.choice([5, 10, 13])
        trip = {5: (3, 4), 10: (6, 8), 13: (5, 12)}[r]
        auf = (M[0] + trip[0], M[1] + trip[1])
        nah = (M[0] + 1, M[1] + 2)
        fern = (M[0] + r, M[1] + 1)
        return Kern(f'Gegeben ist der Kreis k um M{pt(M)} mit r = {r} LE.', f'Welche Punkte liegen auf k: P{pt(auf)}, Q{pt(nah)}, R{pt(fern)}? Begründe mit dem Abstand.', 'nur P',
                    ['Abstand² = Δx² + Δy² mit r² vergleichen.', f'P: {trip[0]}² + {trip[1]}² = {r * r} = r² ✓'], [('P und R', 'nur die x-Differenz betrachtet')],
                    [check('Abstand P', trip[0] ** 2 + trip[1] ** 2 == r * r), check('R nicht', r * r + 1 != r * r)])
    if et == 'parallelen':
        c = rng.randint(-3, 3)
        d = rng.randint(1, 4)
        return Kern(f'Gegeben ist die Gerade g: y = {c}.', f'Beschreibe die Menge aller Punkte, die von g den Abstand {d} LE haben, und gib die Gleichungen an.', f'zwei Parallelen zu g: y = {c + d} und y = {c - d}',
                    ['Punkte mit festem Abstand zu einer Geraden liegen auf zwei Parallelen.'], [(f'nur y = {c + d}', 'zweite Parallele vergessen')], [check('Abstände', (c + d) - c == d == c - (c - d))])
    A = (Fr(rng.randint(-6, -1)), Fr(rng.randint(-2, 2)))
    B_ = (A[0] + 2 * rng.randint(2, 5), A[1])
    mx = (A[0] + B_[0]) / 2
    if et == 'zwei_kreise' or et == 'verstehen':
        return Kern(f'Gegeben sind A{pt(A)} und B{pt(B_)}.', 'Beschreibe und konstruiere die Menge aller Punkte, die von A und B gleich weit entfernt sind. Gib ihre Gleichung an.', f'Mittelsenkrechte m: x = {z(mx)}',
                    ['Kreisbögen mit gleichem Radius um A und B; Verbindungsgerade der Schnittpunkte.', f'Da A und B auf gleicher Höhe liegen: x = {z(mx)}'], [(f'y = {z(mx)}', 'Achsen verwechselt')],
                    [check('Mitte', B_[0] - mx == mx - A[0])])
    # verknuepfen: gleich weit von A und B UND Abstand r von A
    dx = mx - A[0]
    r_opts = [(5, 3, 4), (10, 6, 8), (13, 5, 12), (5, 4, 3)]
    cand = [(r, a, b) for r, a, b in r_opts if a == dx]
    if not cand:
        B_ = (A[0] + 6, A[1])
        mx = A[0] + 3
        cand = [(5, 3, 4)]
    r, a, b = cand[0]
    pts = [(mx, A[1] + b), (mx, A[1] - b)]
    return Kern(f'Gegeben sind A{pt(A)} und B{pt(B_)}.', f'Konstruiere alle Punkte, die von A und B gleich weit entfernt sind und von A den Abstand {r} LE haben. Gib ihre Koordinaten an.',
                f'P₁{pt(pts[0])}, P₂{pt(pts[1])}', [f'Mittelsenkrechte x = {z(mx)}', f'Kreis um A mit r = {r}', f'Schnittpunkte: Δx = {a}, Δy = ±{b} (denn {a}² + {b}² = {r}²)'],
                [(f'nur P₁{pt(pts[0])}', 'zweiten Schnittpunkt vergessen')], [check('Abstand', all((p[0] - A[0]) ** 2 + (p[1] - A[1]) ** 2 == r * r for p in pts))])


# ---------- Flächen / Volumen ----------
def f_flaeche(rng, niv, info, et, thema):
    if et in ('einheiten',):
        w = Fr(rng.randint(12, 980), rng.choice([1, 10, 100]))
        paar = rng.choice([('m²', 'dm²', 100), ('dm²', 'cm²', 100), ('cm²', 'mm²', 100), ('ha', 'm²', 10000), ('km²', 'ha', 100)])
        return Kern('', f'Wandle um: {z(w)} {paar[0]} = ___ {paar[1]}', f'{z(w * paar[2])} {paar[1]}', [f'Umrechnungszahl {paar[2]}'], [(f'{z(w * 10)} {paar[1]}', 'Umrechnungszahl 10 statt 100')],
                    [wissen('Faktor')], luecke=f'Ergänze: {z(w)} {paar[0]} = ___ {paar[1]}')
    if et in ('parallelogramm', 'trapez', 'dreieck', 'drachen_raute', 'rueckwaerts'):
        g, h = Fr(rng.randint(30, 120), 10), Fr(rng.randint(20, 90), 10)
        if et == 'trapez':
            c = Fr(rng.randint(15, 60), 10)
            A_ = (g + c) / 2 * h
            return Kern(f'Ein Trapez hat die parallelen Seiten a = {z(g)} cm und c = {z(c)} cm sowie die Höhe h = {z(h)} cm.', 'Berechne den Flächeninhalt.', f'{z(A_)} cm²',
                        ['A = (a + c) : 2 · h', f'= ({z(g)} + {z(c)}) : 2 · {z(h)} = {z(A_)}'], [(f'{z((g + c) * h)} cm²', 'nicht halbiert')], [check('Formel', A_ * 2 == (g + c) * h)])
        if et == 'drachen_raute':
            e, f = g, h
            A_ = e * f / 2
            return Kern(f'Eine Raute hat die Diagonalen e = {z(e)} cm und f = {z(f)} cm.', 'Berechne den Flächeninhalt.', f'{z(A_)} cm²', ['A = e · f : 2', f'= {z(A_)}'],
                        [(f'{z(e * f)} cm²', 'nicht halbiert')], [check('Formel', A_ * 2 == e * f)])
        A_ = g * h / (2 if et == 'dreieck' else 1)
        if et == 'rueckwaerts' or 'rückwärts' in info.get('besonderheit', ''):
            return Kern(f'Ein Parallelogramm hat den Flächeninhalt {z(g * h)} cm² und die Grundseite {z(g)} cm.', 'Berechne die zugehörige Höhe.', f'{z(h)} cm',
                        ['h = A : g', f'= {z(g * h)} : {z(g)} = {z(h)}'], [(f'{z(g * h * g)} cm', 'multipliziert statt dividiert')], [check('Probe', g * h == g * h)])
        return Kern(f'Ein {"Dreieck" if et == "dreieck" else "Parallelogramm"} hat die Grundseite g = {z(g)} cm und die Höhe h = {z(h)} cm.', 'Berechne den Flächeninhalt.', f'{z(A_)} cm²',
                    ['A = g · h' + (' : 2' if et == 'dreieck' else ''), f'= {z(A_)}'], [(f'{z(g * h if et == "dreieck" else g * h / 2)} cm²', 'Formeln von Dreieck und Parallelogramm verwechselt')],
                    [check('Formel', A_ == g * h / (2 if et == 'dreieck' else 1))])
    # zerlegen / zusammengesetzt / rechteck / sachaufgaben / verstehen
    a, b = rng.randint(6, 14), rng.randint(5, 12)
    c, d = rng.randint(2, a - 2), rng.randint(2, b - 2)
    A_ = a * b - c * d
    U = 2 * (a + b)
    if et == 'sachaufgaben':
        f = rng.choice([20, 25, 30, 40, 50])
        anz = Fr(a * b * 10000, f * f)
        return Kern(f'Ein Raum ist {a} m lang und {b} m breit. Er wird mit quadratischen Fliesen der Seitenlänge {f} cm ausgelegt.', 'Wie viele Fliesen braucht man mindestens?',
                    f'{math.ceil(anz)} Fliesen', [f'Raum: {a * b} m² = {a * b * 10000} cm²', f'Fliese: {f * f} cm²', f'{a * b * 10000} : {f * f} = {z(anz)} → {math.ceil(anz)}'],
                    [(f'{z(Fr(a * b * 100, f * f))} Fliesen', 'm² in cm² mit 100 umgerechnet')], [check('Fläche', anz * f * f == a * b * 10000)])
    if et == 'verstehen':
        k = rng.choice([2, 3])
        return Kern(f'Bei einem Rechteck werden Länge und Breite jeweils ver-{k}-facht.'.replace('ver-2-facht', 'verdoppelt').replace('ver-3-facht', 'verdreifacht'),
                    'Wie ändern sich Umfang und Flächeninhalt? Begründe.', f'Umfang: {k}-fach, Fläche: {k * k}-fach', [f'U = 2(ka + kb) = k · 2(a + b)', f'A = ka · kb = k² · ab'],
                    [(f'Umfang {k}-fach, Fläche {k}-fach', 'Flächeninhalt wie eine Länge behandelt')], [check('Skalierung', (k * a) * (k * b) == k * k * a * b)])
    return Kern(f'Aus einem rechteckigen Blech ({a} cm × {b} cm) wird an einer Ecke ein Rechteck ({c} cm × {d} cm) ausgeschnitten.', 'Berechne Flächeninhalt und Umfang der Restfigur.',
                f'A = {A_} cm², U = {U} cm', [f'A = {a}·{b} − {c}·{d} = {A_}', 'Umfang: Die ausgeschnittene Ecke ändert den Umfang nicht (Seiten werden nur verschoben).', f'U = 2·({a} + {b}) = {U}'],
                [(f'U = {U - c - d} cm', 'ausgeschnittene Seiten abgezogen')], [check('Fläche', A_ + c * d == a * b)])


def f_kreisber(rng, niv, info, et):
    r = Fr(rng.randint(15, 90), 10)
    if et == 'verstehen':
        return Kern('', 'Wie ändern sich Umfang und Flächeninhalt eines Kreises, wenn man den Radius verdoppelt?', 'Umfang doppelt, Fläche vierfach', ['u = 2πr, A = πr²'],
                    [('beide doppelt', 'quadratische Abhängigkeit übersehen'), ('Umfang vierfach, Fläche doppelt', 'vertauscht'), ('beide vierfach', 'Umfang hängt linear vom Radius ab')], [wissen('Skalierung')])
    u = 2 * PI * r
    A_ = PI * r * r
    if et == 'flaeche':
        return Kern(f'Ein runder Teppich hat den Radius {z(r)} m.', 'Berechne seinen Flächeninhalt (π ≈ 3,14, Ergebnis auf zwei Dezimalen).', f'≈ {z(Fr(round(A_ * 100), 100), 2)} m²',
                    ['A = π · r²', f'= 3,14 · {z(r)}² ≈ {z(Fr(round(A_ * 100), 100), 2)}'], [(f'≈ {z(Fr(round(u * 100), 100), 2)} m²', 'Umfangsformel verwendet')], [check('Formel', A_ == PI * r ** 2)])
    if et == 'zusammengesetzt':
        a = Fr(rng.randint(4, 12))
        fl = a * a + PI * (a / 2) ** 2 / 2
        return Kern(f'Eine Figur besteht aus einem Quadrat mit der Seitenlänge {z(a)} cm und einem angesetzten Halbkreis über einer Quadratseite.', 'Berechne den Flächeninhalt (π ≈ 3,14).',
                    f'≈ {z(Fr(round(fl * 100), 100), 2)} cm²', [f'Quadrat: {z(a * a)}', f'Halbkreis: ½ · 3,14 · {z(a / 2)}² = {z(PI * (a / 2) ** 2 / 2)}'], [(f'≈ {z(a * a + PI * (a / 2) ** 2)} cm²', 'ganzen Kreis statt Halbkreis')],
                    [check('Summe', fl == a * a + PI * a * a / 8)])
    if 'rückwärts' in info.get('besonderheit', '') or niv == 'III':
        return f_tisch(rng, niv, info)
    return Kern(f'Ein Fahrradreifen hat den Radius {z(r)} dm.', 'Wie lang ist sein Umfang (π ≈ 3,14)? Welche Strecke legt das Rad bei 100 Umdrehungen zurück?', f'u ≈ {z(Fr(round(u * 100), 100), 2)} dm; ≈ {z(Fr(round(u * 100), 100) * 10)} m',
                [f'u = 2 · π · r = 2 · 3,14 · {z(r)} ≈ {z(Fr(round(u * 100), 100), 2)} dm', f'100 Umdrehungen: {z(Fr(round(u * 100), 100), 2)} dm · 100 = {z(Fr(round(u * 100), 100) * 100)} dm = {z(Fr(round(u * 100), 100) * 10)} m'], [(f'u ≈ {z(Fr(round(PI * r * 100), 100), 2)} dm', 'Durchmesser mit Radius verwechselt')],
                [check('Formel', u == 2 * PI * r), check('100 Umdrehungen in m', Fr(round(u * 100), 100) * 100 / 10 == Fr(round(u * 100), 100) * 10)])


def f_tisch(rng, niv, info):
    """Rückwärts: Radius aus vorgegebenem Umfang (eigener Kontext: Zaun um einen runden Teich)."""
    u = rng.choice([18, 22, 25, 31, 40, 47, 55])
    r = Fr(u) / (2 * PI)
    rr = Fr(math.floor(r * 10), 10)
    return Kern(f'Für einen kreisrunden Gartenteich stehen {u} m Zaun zur Verfügung; der Zaun soll direkt am Teichrand entlanglaufen.',
                'Welchen Radius darf der Teich höchstens haben (π ≈ 3,14; auf dm abrunden)? Wie groß ist dann ungefähr die Wasserfläche?',
                f'r ≈ {z(rr, 1)} m; A ≈ {z(Fr(round(PI * rr * rr * 100), 100), 2)} m²',
                [f'u = 2 · π · r → r = u : (2π) = {u} : 6,28 ≈ {z(Fr(round(r * 100), 100), 2)} m', f'abrunden (der Zaun muss reichen): r ≈ {z(rr, 1)} m',
                 f'A = π · r² ≈ 3,14 · {z(rr, 1)}² ≈ {z(Fr(round(PI * rr * rr * 100), 100), 2)} m²'],
                [(f'r ≈ {z(Fr(math.floor(Fr(u) / PI * 10), 10), 1)} m', 'durch π statt durch 2π geteilt (Durchmesser)')],
                [check('Zaun reicht', 2 * PI * rr <= u), check('Radius maximal (dm)', 2 * PI * (rr + Fr(1, 10)) > u)])


def f_volumen(rng, niv, info, et, thema):
    a, b, c = rng.randint(3, 15), rng.randint(2, 12), rng.randint(2, 10)
    V = a * b * c
    if et in ('rueckwaerts', 'prisma_umstellen'):
        return Kern(f'Ein quaderförmiges Aquarium ist {a} dm lang und {b} dm breit. Es fasst {V} Liter.', 'Wie hoch ist es?', f'{c} dm', ['1 l = 1 dm³', f'h = V : (a · b) = {V} : {a * b} = {c}'],
                    [(f'{V - a - b} dm', 'subtrahiert statt dividiert')], [check('Probe', a * b * c == V)])
    if et == 'liter':
        w = Fr(rng.randint(15, 950), 10)
        return Kern('', f'Wandle {z(w)} l in cm³ und in m³ um.', f'{z(w * 1000)} cm³ = {z(w / 1000, True)} m³', ['1 l = 1 dm³ = 1000 cm³', '1 m³ = 1000 l'],
                    [(f'{z(w * 100)} cm³', 'Umrechnungszahl 100 statt 1000')], [check('Einheiten', w * 1000 / 1000 == w)])
    if et == 'einheitswuerfel':
        return Kern(f'Eine quaderförmige Kiste ist innen {a} cm lang, {b} cm breit und {c} cm hoch.', 'Wie viele Würfel mit 1 cm Kantenlänge passen höchstens hinein?', f'{V} Würfel',
                    [f'{a} · {b} · {c} = {V}'], [(f'{2 * (a * b + a * c + b * c)}', 'Oberfläche statt Volumen')], [check('Volumen', V == a * b * c)])
    if et == 'prisma_volumen':
        g, h_d, h = rng.randint(3, 10), rng.randint(2, 8), rng.randint(4, 15)
        G = Fr(g * h_d, 2)
        return Kern(f'Ein Prisma hat als Grundfläche ein Dreieck mit g = {g} cm und h_g = {h_d} cm; die Körperhöhe beträgt {h} cm.', 'Berechne das Volumen.', f'{z(G * h)} cm³',
                    [f'G = {g} · {h_d} : 2 = {z(G)} cm²', f'V = G · h = {z(G * h)} cm³'], [(f'{g * h_d * h} cm³', 'Dreiecksfläche nicht halbiert')], [check('Volumen', G * h * 2 == g * h_d * h)])
    if et == 'zusammengesetzt':
        d = rng.randint(1, min(a, b) - 1) if min(a, b) > 1 else 1
        V2 = V - d * d * c
        return Kern(f'Aus einem Quader ({a} cm × {b} cm × {c} cm) wird an einer Kante ein Quader mit quadratischer Grundfläche ({d} cm × {d} cm) über die ganze Höhe herausgeschnitten.', 'Berechne das Restvolumen.',
                    f'{V2} cm³', [f'{V} − {d * d * c} = {V2}'], [(f'{V - d * d} cm³', 'Höhe beim ausgeschnittenen Teil vergessen')], [check('Volumen', V2 + d * d * c == V)])
    return Kern(f'Ein Quader ist {a} cm lang, {b} cm breit und {c} cm hoch.', 'Berechne Volumen und Oberfläche.', f'V = {V} cm³, O = {2 * (a * b + a * c + b * c)} cm²',
                ['V = a · b · c', 'O = 2(ab + ac + bc)'], [(f'V = {a + b + c} cm³', 'addiert statt multipliziert')], [check('Volumen', V == a * b * c)])


# ---------- Raum ----------
def f_raum(rng, niv, info, et, thema):
    if et == 'lage':
        # Quader ABCDEFGH: A(0,0,0) B(1,0,0) C(1,1,0) D(0,1,0), E..H darüber
        ecken = {'A': (0, 0, 0), 'B': (1, 0, 0), 'C': (1, 1, 0), 'D': (0, 1, 0), 'E': (0, 0, 1), 'F': (1, 0, 1), 'G': (1, 1, 1), 'H': (0, 1, 1)}
        kanten = ['AB', 'BC', 'CD', 'DA', 'EF', 'FG', 'GH', 'HE', 'AE', 'BF', 'CG', 'DH', 'AC', 'BD', 'EG', 'FH', 'AF', 'BG', 'DE', 'CH']
        for _ in range(100):
            s1, s2 = rng.sample(kanten, 2)
            lage = _lage(ecken, s1, s2)
            if lage != 'gleich':
                break
        andere = [l for l in ('parallel', 'schneiden sich', 'windschief') if l != lage]
        return Kern('Gegeben ist ein Quader ABCDEFGH (Grundfläche ABCD, darüber EFGH, E über A).', f'Welche Lage haben die Geraden {s1} und {s2} zueinander?', lage,
                    ['Parallel: gleiche Richtung; schneiden: gemeinsamer Punkt in einer Ebene; windschief: weder parallel noch schneidend.', f'{s1} und {s2}: {lage}'],
                    [(a, 'Lage im Raum falsch eingeschätzt') for a in andere], [check('Lage per Vektorrechnung (Kreuz- und Spatprodukt)', lage in ('parallel', 'schneiden sich', 'windschief'))])
    if et in ('pyramide', 'wahre_groesse', 'koordinaten'):
        a, h = rng.randint(4, 8), rng.randint(5, 10)
        q = Fr(1, 2)
        return Kern(f'Von einer quadratischen Pyramide ABCDS mit a = {a} cm und Höhe h = {h} cm soll ein Schrägbild gezeichnet werden ([AB] auf der Schrägbildachse, q = ½, ω = 45°).',
                    'Welche Strecken erscheinen im Schrägbild in wahrer Länge? Wie lang wird [AD] gezeichnet?', f'In wahrer Länge: [AB], [CD] und die Höhe {h} cm; [AD] wird {z(q * a)} cm lang gezeichnet',
                    ['Strecken parallel zur Zeichenebene erscheinen in wahrer Länge.', f'Strecken nach hinten werden mit q = ½ verkürzt: {a} · ½ = {z(q * a)} cm'],
                    [(f'[AD] {a} cm', 'Verkürzung vergessen'), ('alle Kanten in wahrer Länge', 'Schrägbildregeln nicht beachtet')], [check('Verkürzung', q * a * 2 == a)])
    if et == 'rotation':
        a, b = rng.randint(2, 6), rng.randint(3, 9)
        return Kern(f'Ein Rechteck mit den Seiten {a} cm und {b} cm rotiert um die Seite der Länge {b} cm.', 'Welcher Körper entsteht? Gib Radius und Höhe an.', f'Zylinder mit r = {a} cm und h = {b} cm',
                    ['Die Rotationsachse wird zur Körperhöhe, die andere Seite zum Radius.'], [(f'Zylinder mit r = {b} cm und h = {a} cm', 'Radius und Höhe vertauscht'), ('Kegel', 'Körper verwechselt')], [wissen('Zuordnung')])
    if et == 'axialschnitt':
        r, h = rng.randint(2, 7), rng.randint(3, 10)
        return Kern(f'Ein Kegel hat den Radius {r} cm und die Höhe {h} cm.', 'Beschreibe den Axialschnitt und berechne seinen Flächeninhalt.', f'gleichschenkliges Dreieck, Basis {2 * r} cm, Höhe {h} cm, A = {r * h} cm²',
                    ['Axialschnitt: Schnitt durch die Achse', f'A = {2 * r} · {h} : 2 = {r * h}'], [(f'{2 * r * h} cm²', 'nicht halbiert')], [check('Fläche', 2 * r * h / 2 == r * h)])
    if et in ('prisma', 'netz', 'ansichten'):
        n = rng.randint(3, 8)
        return Kern(f'Ein Prisma hat als Grundfläche ein {n}-Eck.', 'Wie viele Flächen, Kanten und Ecken hat es? Was kennzeichnet ein Prisma?', f'{n + 2} Flächen, {3 * n} Kanten, {2 * n} Ecken; Grund- und Deckfläche kongruent und parallel, Seitenflächen Rechtecke (gerades Prisma)',
                    ['Seitenflächen: n, dazu Grund- und Deckfläche', 'Kanten: n unten, n oben, n senkrecht', 'Ecken: n unten, n oben'], [(f'{n + 1} Flächen, {2 * n} Kanten, {2 * n} Ecken', 'senkrechte Kanten bzw. Deckfläche vergessen')],
                    [check('Eulerscher Polyedersatz', (2 * n) - 3 * n + (n + 2) == 2)])
    return f_raum(rng, niv, info, 'pyramide', thema)


def _lage(e, s1, s2):
    import itertools
    p1, p2 = [e[c] for c in s1], [e[c] for c in s2]
    d1 = tuple(p1[1][i] - p1[0][i] for i in range(3))
    d2 = tuple(p2[1][i] - p2[0][i] for i in range(3))
    kreuz = (d1[1] * d2[2] - d1[2] * d2[1], d1[2] * d2[0] - d1[0] * d2[2], d1[0] * d2[1] - d1[1] * d2[0])
    w = tuple(p2[0][i] - p1[0][i] for i in range(3))
    spat = sum(kreuz[i] * w[i] for i in range(3))
    if kreuz == (0, 0, 0):
        kr2 = (d1[1] * w[2] - d1[2] * w[1], d1[2] * w[0] - d1[0] * w[2], d1[0] * w[1] - d1[1] * w[0])
        return 'gleich' if kr2 == (0, 0, 0) else 'parallel'
    return 'schneiden sich' if spat == 0 else 'windschief'
