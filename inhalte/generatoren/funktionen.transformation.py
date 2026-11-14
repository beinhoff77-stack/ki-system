#!/usr/bin/env python3
"""Thema funktionen.transformation – Graphentransformation (Realschule Bayern, Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _rs import *  # noqa: E402,F403

start(4001)
LS, HS = 'S(□ | □)', 'x-Koordinate, y-Koordinate des Scheitels'
LP, HP = "P'(□ | □)", 'Trage die x- und die y-Koordinate des Bildpunkts ein.'


def nz(n):
    return R.choice([i for i in range(-n, n + 1) if i != 0])


def par(a, d, e):
    """y = a(x − d)² + e als Text"""
    a = Fr(a)
    vor = '' if a == 1 else ('−' if a == -1 else dz(a))
    k = minus_klammer(d) if d != 0 else 'x'
    t = f'{vor}{k}²' if d != 0 else f'{vor}x²'
    return 'y = ' + t + (f' {plus(e)}' if e != 0 else '')


def par_bild(liste, x=(-6, 6), y=(-6, 8)):
    gs = []
    for a, d, e, n in liste:
        a = Fr(a)
        gs.append({'art': 'poly', 'k': [float(a * d * d + e), float(-2 * a * d), float(a)], 'name': n})
    return {'typ': 'koordinaten', 'x': list(x), 'y': list(y), 'graphen': gs}


ETAPPEN = [
    {'lernziel': 'nach_oben', 'titel': 'Nach oben oder unten verschieben',
     'regel': 'Addierst du zum Funktionsterm eine Zahl e, wird jeder Punkt um e ⟦nach oben⟧ verschoben (bei e < 0 ⟦nach unten⟧): y = f(x) + e. Aus der Normalparabel y = x² wird ⟦y = x² + e⟧ mit Scheitel ⟦S(0 | e)⟧. Wie ein Aufzug: Alles fährt gleich weit.',
     'bild': par_bild([(1, 0, 0, 'y = x²'), (1, 0, 3, 'y = x² + 3')], (-4, 4), (-1, 9)),
     'schritte': ['Die Normalparabel wird um 3 nach oben verschoben: ⟦y = x² + 3⟧.', 'Der Scheitel wandert von S(0 | 0) nach ⟦S(0 | 3)⟧.'],
     'fehler': 'y = (x + 3)² für „3 nach oben“ ist falsch: Eine Zahl ⟦in der Klammer⟧ verschiebt nach links oder rechts. Nach oben wird ⟦hinten addiert⟧: x² + 3.'},
    {'lernziel': 'nach_rechts', 'titel': 'Nach links oder rechts verschieben',
     'regel': 'Ersetzt du x durch ⟦(x − d)⟧, wird der Graph um d ⟦nach rechts⟧ verschoben, bei (x + d) ⟦nach links⟧. Aus y = x² wird ⟦y = (x − d)²⟧ mit Scheitel ⟦S(d | 0)⟧. Merke: Das Vorzeichen in der Klammer ist ⟦umgekehrt⟧ – bei x − 2 ist der Scheitel bei +2, denn dort wird die Klammer 0.',
     'bild': par_bild([(1, 0, 0, 'y = x²'), (1, 2, 0, 'y = (x − 2)²')], (-3, 5), (-1, 9)),
     'schritte': ['y = (x − 2)²: Die Klammer wird 0 für x = 2.', 'Scheitel ⟦S(2 | 0)⟧ – die Parabel ist um 2 ⟦nach rechts⟧ verschoben.'],
     'fehler': 'y = (x + 4)² als „4 nach rechts“ zu lesen ist falsch: Die Klammer ist 0 für x = −4, also ⟦4 nach links⟧.'},
    {'lernziel': 'strecken', 'titel': 'Strecken, stauchen, nach unten öffnen',
     'regel': 'Multiplizierst du den Funktionsterm mit a, werden alle y-Werte mal a genommen: y = a · x². Für ⟦|a| > 1⟧ wird die Parabel ⟦gestreckt⟧ (enger), für ⟦0 < |a| < 1⟧ ⟦gestaucht⟧ (weiter). Ein ⟦negatives a⟧ spiegelt zusätzlich an der ⟦x-Achse⟧: Die Parabel ist nach unten geöffnet.',
     'bild': par_bild([(1, 0, 0, 'y = x²'), (2, 0, 0, 'y = 2x²'), (Fr(-1, 2), 0, 0, 'y = −0,5x²')], (-4, 4), (-5, 8)),
     'schritte': ['y = 2x²: An der Stelle x = 3 ist y = 2 · 9 = ⟦18⟧ statt 9 – doppelt so hoch.',
                  'y = −0,5x²: Für x = 4 ist y = −0,5 · 16 = ⟦−8⟧. Halb so hoch und nach unten geöffnet.'],
     'fehler': 'y = 2x² für x = 3 als (2 · 3)² = 36 zu rechnen ist falsch: Erst ⟦quadrieren⟧, dann mit 2 multiplizieren: 2 · 9 = 18.'},
    {'lernziel': 'spiegeln', 'titel': 'An den Achsen spiegeln',
     'regel': 'Spiegeln an der ⟦x-Achse⟧: y-Werte bekommen das andere Vorzeichen, ⟦y = −f(x)⟧, Punkt (x | y) → (x | −y). Spiegeln an der ⟦y-Achse⟧: x wird durch −x ersetzt, ⟦y = f(−x)⟧, Punkt (x | y) → (−x | y). Wie im Spiegel: Was links war, ist rechts.',
     'bild': par_bild([(1, 2, 1, 'y = (x − 2)² + 1'), (1, -2, 1, 'y = (x + 2)² + 1')], (-5, 5), (-1, 8)),
     'schritte': ['Parabel y = (x − 2)² + 1 mit S(2 | 1) an der y-Achse spiegeln: x durch −x ersetzen.',
                  '(−x − 2)² = (x + 2)², also ⟦y = (x + 2)² + 1⟧ mit ⟦S(−2 | 1)⟧.'],
     'fehler': 'Beim Spiegeln an der y-Achse auch y umzudrehen, also S(−2 | −1), ist falsch: An der ⟦y-Achse⟧ ändert sich ⟦nur x⟧.'},
    {'lernziel': 'kombiniert', 'titel': 'Mehrere Schritte: y = a(x − d)² + e',
     'regel': 'Die Gleichung ⟦y = a(x − d)² + e⟧ verrät alles: Scheitel ⟦S(d | e)⟧, Form a (gestreckt, gestaucht, nach unten geöffnet). Sie entsteht aus der Normalparabel durch ⟦Strecken mit a⟧, dann ⟦Verschieben um d nach rechts und e nach oben⟧.',
     'bild': par_bild([(1, 0, 0, 'y = x²'), (Fr(-1, 2), 3, 4, 'y = −0,5(x − 3)² + 4')], (-3, 7), (-4, 6)),
     'schritte': ['y = −0,5(x − 3)² + 4: a = −0,5, also gestaucht und nach unten geöffnet.', 'Scheitel ⟦S(3 | 4)⟧: 3 nach rechts, 4 nach oben.'],
     'fehler': 'Bei y = 2(x + 1)² − 5 den Scheitel S(1 | −5) abzulesen ist falsch: Die Klammer ist 0 für ⟦x = −1⟧, also S(−1 | −5).'},
    {'lernziel': 'punkte', 'titel': 'Punkte mit abbilden',
     'regel': 'Kennst du einen Punkt P(x | y) auf dem Graphen von f, findest du sein Bild auf g(x) = a · f(x − d) + e ohne den Term von f: ⟦P\'(x + d | a · y + e)⟧. Erst ⟦strecken⟧ (y mal a), dann ⟦verschieben⟧.',
     'schritte': ['P(1 | 4) liegt auf dem Graphen von f. g(x) = 2 · f(x − 3) − 1.', "x: 1 + 3 = 4; y: 2 · 4 − 1 = 7. Also ⟦P'(4 | 7)⟧."],
     'probe': 'g(4) = 2 · f(4 − 3) − 1 = 2 · f(1) − 1 = 2 · 4 − 1 = 7 ✓',
     'fehler': "Bei g(x) = f(x − 3) den Punkt nach links zu schieben (x − 3) ist falsch: f(x − 3) heißt ⟦3 nach rechts⟧, also x + 3."},
]


# ---------- Generatoren ----------
def g_nach_oben(s):
    e = nz(7)
    if s == 1:
        if R.random() < 0.5:
            return luecken(f'Die Normalparabel y = x² wird um {abs(e)} nach {"oben" if e > 0 else "unten"} verschoben. Gib den Scheitel an.', LS, HS, [0, e],
                           f'Verschieben nach {"oben" if e > 0 else "unten"} ändert nur y: S(0 | {dz(e)}). Gleichung {par(1, 0, e)}.',
                           'Der Scheitel der Normalparabel ist S(0 | 0).', c=['0', str(e)])
        return auswahl(f'Die Normalparabel wird um {abs(e)} nach {"oben" if e > 0 else "unten"} verschoben. Welche Gleichung gehört dazu?', par(1, 0, e),
                       [par(1, -e, 0), par(1, e, 0), par(1, 0, -e)],
                       f'Nach {"oben" if e > 0 else "unten"}: hinten {dz(e)} addieren: {par(1, 0, e)}.', 'Verschiebt eine Zahl in der Klammer nach oben?')
    d, e0 = nz(4), R.randint(-5, 5)
    if s == 2:
        if R.random() < 0.5:
            return luecken(f'Die Parabel {par(1, d, e0)} wird um {abs(e)} nach {"oben" if e > 0 else "unten"} verschoben. Gib den neuen Scheitel an.', LS, HS, [d, e0 + e],
                           f'Alter Scheitel S({dz(d)} | {dz(e0)}). Nur y ändert sich: {dz(e0)} {plus(e)} = {dz(e0 + e)}. S({dz(d)} | {dz(e0 + e)}).',
                           'Lies zuerst den alten Scheitel ab.', c=[str(d), f'{e0} + ({e})'])
        x0 = nz(4)
        y0 = x0 * x0
        return luecken(f'P({dz(x0)} | {dz(y0)}) liegt auf y = x². Wohin kommt P, wenn die Parabel um {abs(e)} nach {"oben" if e > 0 else "unten"} verschoben wird?', LP, HP,
                       [x0, y0 + e], f"Nur y ändert sich: {dz(y0)} {plus(e)} = {dz(y0 + e)}. P'({dz(x0)} | {dz(y0 + e)}).",
                       'Bei einer Verschiebung nach oben/unten bleibt x gleich.', c=[str(x0), f'{y0} + ({e})'])
    art = R.random()
    if art < 0.4:
        a = luecken('Die gezeichnete Parabel ist eine nach oben oder unten verschobene Normalparabel. Gib ihren Scheitel an.', LS, HS, [0, e],
                    f'Die Parabel schneidet die y-Achse im Scheitel S(0 | {dz(e)}). Gleichung {par(1, 0, e)}.', 'Wo liegt der tiefste Punkt?', c=['0', str(e)])
        return bild(a, par_bild([(1, 0, e, '')], (-4, 4), (min(-2, e - 1), max(8, e + 6))))
    if art < 0.7:
        x0 = nz(5)
        return zahl(f'Die Normalparabel wird um {abs(e)} nach {"oben" if e > 0 else "unten"} verschoben. Welchen y-Wert hat die neue Parabel bei x = {dz(x0)}?',
                    f'{par(1, 0, e)}: y = {kl(x0)}² {plus(e)} = {dz(x0 * x0)} {plus(e)} = {dz(x0 * x0 + e)}.', 'Stelle zuerst die Gleichung auf.',
                    x0 * x0 + e, f'({x0}) ** 2 + ({e})')
    e2 = nz(6)
    if e2 == e: return None
    return zahl(f'Die Parabel {par(1, 0, e)} soll so verschoben werden, dass ihr Scheitel bei S(0 | {dz(e2)}) liegt. Um wie viel muss man sie nach oben verschieben? (Nach unten: negative Zahl.)',
                f'Von {dz(e)} nach {dz(e2)}: {dz(e2)} − {kl(e)} = {dz(e2 - e)}.', 'Differenz der y-Koordinaten der Scheitel.', e2 - e, f'({e2}) - ({e})')


def g_nach_rechts(s):
    d = nz(6)
    r = 'rechts' if d > 0 else 'links'
    if s == 1:
        if R.random() < 0.5:
            return luecken(f'Gib den Scheitel der Parabel {par(1, d, 0)} an.', LS, HS, [d, 0],
                           f'Die Klammer ist 0 für x = {dz(d)}: S({dz(d)} | 0). Die Parabel ist um {abs(d)} nach {r} verschoben.',
                           'Für welches x wird die Klammer null?', c=[str(d), '0'])
        return auswahl(f'Die Normalparabel wird um {abs(d)} nach {r} verschoben. Welche Gleichung gehört dazu?', par(1, d, 0),
                       [par(1, -d, 0), par(1, 0, d), par(1, 0, -d)],
                       f'Nach {r} um {abs(d)}: Scheitel S({dz(d)} | 0), Gleichung {par(1, d, 0)}.', 'Achtung: Das Vorzeichen in der Klammer ist umgekehrt.')
    if s == 2:
        e = R.randint(-5, 5)
        if R.random() < 0.5:
            return luecken(f'Gib den Scheitel der Parabel {par(1, d, e)} an.', LS, HS, [d, e],
                           f'Klammer 0 für x = {dz(d)}, dahinter {dz(e)}: S({dz(d)} | {dz(e)}).', 'Klammer null setzen; die Zahl hinten ist die y-Koordinate.',
                           c=[str(d), str(e)])
        return auswahl(f'Wie entsteht {par(1, d, 0)} aus der Normalparabel?', f'Verschiebung um {abs(d)} nach {r}',
                       [f'Verschiebung um {abs(d)} nach {"links" if d > 0 else "rechts"}', f'Verschiebung um {abs(d)} nach oben', f'Verschiebung um {d * d} nach oben'],
                       f'Klammer 0 für x = {dz(d)}: Der Scheitel liegt bei S({dz(d)} | 0), also {abs(d)} nach {r}.', 'Wo liegt der Scheitel?')
    art = R.random()
    if art < 0.35:
        a = luecken('Die gezeichnete Parabel ist eine verschobene Normalparabel. Gib ihren Scheitel an.', LS, HS, [d, 0],
                    f'Tiefster Punkt auf der x-Achse bei x = {dz(d)}: S({dz(d)} | 0). Gleichung {par(1, d, 0)}.', 'Wo liegt der tiefste Punkt?',
                    c=[str(d), '0'])
        return bild(a, par_bild([(1, d, 0, '')], (min(-3, d - 3), max(3, d + 3)), (-1, 8)))
    if art < 0.7:
        x0 = nz(5)
        return zahl(f'Berechne den y-Wert der Parabel {par(1, d, 0)} an der Stelle x = {dz(x0)}.',
                    f'y = ({dz(x0)} {plus(-d)})² = {kl(x0 - d)}² = {dz((x0 - d) ** 2)}.', 'Erst die Klammer ausrechnen, dann quadrieren.',
                    (x0 - d) ** 2, f'(({x0}) - ({d})) ** 2')
    d2 = nz(5)
    if d2 == d: return None
    return auswahl(f'Die Parabel {par(1, d, 0)} wird um {abs(d2)} nach {"rechts" if d2 > 0 else "links"} verschoben. Wie lautet die neue Gleichung?',
                   par(1, d + d2, 0), [par(1, d - d2, 0), par(1, d, d2), par(1, -(d + d2), 0)],
                   f'Alter Scheitel bei x = {dz(d)}, neuer bei {dz(d)} {plus(d2)} = {dz(d + d2)}: {par(1, d + d2, 0)}.',
                   'Wo liegt der Scheitel vorher, wo nachher?')


A_WERTE = [Fr(2), Fr(3), Fr(4), Fr(1, 2), Fr(1, 4), Fr(-1), Fr(-2), Fr(-3), Fr(-1, 2), Fr(-1, 4), Fr(3, 2), Fr(5, 2)]


def g_strecken(s):
    a = R.choice(A_WERTE)
    x0 = nz(4)
    if s == 1:
        if a < 0: a = -a
        return zahl(f'Berechne den y-Wert von {par(a, 0, 0)} an der Stelle x = {dz(x0)}.',
                    f'y = {dz(a)} · {kl(x0)}² = {dz(a)} · {dz(x0 * x0)} = {dz(a * x0 * x0)}.', 'Erst quadrieren, dann mit a multiplizieren.',
                    a * x0 * x0, f'{cz(a)} * ({x0}) ** 2')
    if s == 2:
        art = R.random()
        if art < 0.5:
            r = 'nach unten geöffnet, ' if a < 0 else ''
            form = 'gestreckt' if abs(a) > 1 else ('gestaucht' if abs(a) < 1 else 'weder gestreckt noch gestaucht')
            richtig = f'{r}{form}'.strip(', ')
            alle = ['gestreckt', 'gestaucht', 'nach unten geöffnet, gestreckt', 'nach unten geöffnet, gestaucht',
                    'nach unten geöffnet, weder gestreckt noch gestaucht']
            return auswahl(f'Wie sieht die Parabel {par(a, 0, 0)} im Vergleich zur Normalparabel aus?', richtig, [x for x in alle if x != richtig][:3] if R.random() < 0.5 else R.sample([x for x in alle if x != richtig], 3),
                           f'a = {dz(a)}: ' + ('a < 0 heißt nach unten geöffnet; ' if a < 0 else '') + f'|a| {"> 1: gestreckt" if abs(a) > 1 else ("< 1: gestaucht" if abs(a) < 1 else "= 1: gleiche Form")}.',
                           'Schau auf das Vorzeichen und auf den Betrag von a.')
        y0 = a * x0 * x0
        return zahl(f'Die Parabel y = a · x² geht durch P({dz(x0)} | {dz(y0)}). Berechne a.',
                    f'{dz(y0)} = a · {kl(x0)}² = a · {dz(x0 * x0)} ⇒ a = {dz(y0)} : {dz(x0 * x0)} = {dz(a)}.', 'Setze P ein und teile durch x².',
                    a, f'{cz(y0)} / ({x0}) ** 2')
    art = R.random()
    if art < 0.35:
        y0 = a * x0 * x0
        if y0.denominator != 1 or abs(y0) > 8: return None
        b = luecken('Die gezeichnete Parabel hat die Form y = a · x². Lies einen Punkt mit ganzen Koordinaten ab und bestimme a. Gib a als Bruch an.', '□/□',
                    'Zähler und Nenner (gekürzt); Minus in den Zähler; ganze Zahl mit Nenner 1.', [a.numerator, a.denominator],
                    f'Zum Beispiel P({dz(x0)} | {dz(y0)}): a = {dz(y0)} : {dz(x0 * x0)} = {br(a)}.',
                    'Suche einen Punkt auf einem Kästchenkreuz und teile y durch x².', c=[str(a.numerator), str(a.denominator)])
        return bild(b, par_bild([(a, 0, 0, '')], (-4, 4), (-8, 8) if a < 0 else (-1, 9)))
    if art < 0.7:
        f = (a * x0) ** 2
        return auswahl(f'Jemand berechnet für {par(a, 0, 0)} bei x = {dz(x0)}: y = ({dz(a)} · {kl(x0)})² = {dz(f)}. Was stimmt?',
                       f'Falsch: y = {dz(a)} · {dz(x0 * x0)} = {dz(a * x0 * x0)}.', ['Richtig.', f'Falsch: y = {dz(-f)}.', f'Falsch: y = {dz(a * x0 * 2)}.'],
                       f'Nur x wird quadriert, a nicht: y = {dz(a)} · {kl(x0)}² = {dz(a * x0 * x0)}.', 'Was wird zuerst gerechnet – Potenz oder Produkt?')
    a2 = R.choice([x for x in A_WERTE if x != a])
    return auswahl(f'Welche Parabel ist enger: {par(a, 0, 0)} oder {par(a2, 0, 0)}?',
                   par(a, 0, 0) if abs(a) > abs(a2) else (par(a2, 0, 0) if abs(a2) > abs(a) else 'Beide sind gleich weit.'),
                   [par(a2, 0, 0) if abs(a) > abs(a2) else par(a, 0, 0), 'Beide sind gleich weit.', 'Das hängt vom Vorzeichen ab.'],
                   f'Entscheidend ist der Betrag: |{dz(a)}| = {dz(abs(a))}, |{dz(a2)}| = {dz(abs(a2))}. Größerer Betrag heißt enger.',
                   'Vergleiche die Beträge von a.')


def g_spiegeln(s):
    x0, y0 = nz(6), nz(6)
    if s == 1:
        if R.random() < 0.5:
            return luecken(f'Spiegle P({dz(x0)} | {dz(y0)}) an der x-Achse.', LP, HP, [x0, -y0], f"An der x-Achse ändert sich nur y: P'({dz(x0)} | {dz(-y0)}).",
                           'Welche Koordinate bekommt das andere Vorzeichen?', c=[str(x0), f'-({y0})'])
        return luecken(f'Spiegle P({dz(x0)} | {dz(y0)}) an der y-Achse.', LP, HP, [-x0, y0], f"An der y-Achse ändert sich nur x: P'({dz(-x0)} | {dz(y0)}).",
                       'Welche Koordinate bekommt das andere Vorzeichen?', c=[f'-({x0})', str(y0)])
    d, e = nz(5), nz(5)
    if s == 2:
        if R.random() < 0.5:
            return luecken(f'Die Parabel {par(1, d, e)} wird an der y-Achse gespiegelt. Gib den Scheitel der Bildparabel an.', LS, HS, [-d, e],
                           f"Alter Scheitel S({dz(d)} | {dz(e)}), an der y-Achse: S'({dz(-d)} | {dz(e)}). Gleichung {par(1, -d, e)}.",
                           'Spiegle den Scheitel.', c=[f'-({d})', str(e)])
        return luecken(f'Die Parabel {par(1, d, e)} wird an der x-Achse gespiegelt. Gib den Scheitel der Bildparabel an.', LS, HS, [d, -e],
                       f"Alter Scheitel S({dz(d)} | {dz(e)}), an der x-Achse: S'({dz(d)} | {dz(-e)}). Gleichung {par(-1, d, -e)}.",
                       'Spiegle den Scheitel.', c=[str(d), f'-({e})'])
    art = R.random()
    if art < 0.4:
        return auswahl(f'Die Parabel {par(1, d, e)} wird an der x-Achse gespiegelt. Welche Gleichung hat das Bild?', par(-1, d, -e),
                       [par(-1, d, e), par(1, -d, e), par(1, d, -e)],
                       f'y = −f(x) = −({minus_klammer(d)}² {plus(e)}) = {par(-1, d, -e)[4:]}. Beide Teile bekommen ein Minus.',
                       'Das Minus gilt für den ganzen Term – auch für die Zahl hinten.')
    if art < 0.7:
        return auswahl(f'Die Parabel {par(1, d, e)} wird an der y-Achse gespiegelt. Welche Gleichung hat das Bild?', par(1, -d, e),
                       [par(1, d, -e), par(-1, d, e), par(-1, -d, -e)],
                       f'x durch −x ersetzen: (−x {plus(-d)})² = {minus_klammer(-d)}². Bild: {par(1, -d, e)}, Scheitel S({dz(-d)} | {dz(e)}).',
                       'Nur der Scheitel wandert auf die andere Seite der y-Achse.')
    return auswahl('Welche Parabel ändert sich NICHT, wenn man sie an der y-Achse spiegelt?', par(R.choice([2, -1, Fr(1, 2)]), 0, e),
                   [par(1, d, e), par(1, d, 0), par(-1, d, e)],
                   'Parabeln mit Scheitel auf der y-Achse (d = 0) sind symmetrisch zur y-Achse und bleiben gleich.',
                   'Wo muss der Scheitel liegen, damit der Spiegel nichts ändert?')


def g_kombiniert(s):
    a = R.choice([1, -1, 2, -2, Fr(1, 2), Fr(-1, 2), 3])
    d, e = nz(5), nz(6)
    if s == 1:
        return luecken(f'Gib den Scheitel der Parabel {par(a, d, e)} an.', LS, HS, [d, e],
                       f'Klammer 0 für x = {dz(d)}, y = {dz(e)}: S({dz(d)} | {dz(e)}).', 'Klammer null setzen, hinten ablesen.', c=[str(d), str(e)])
    beschr = (f'{"an der x-Achse gespiegelt, " if a < 0 else ""}' +
              (f'mit dem Faktor {dz(abs(a))} {"gestreckt" if abs(a) > 1 else "gestaucht"}, ' if abs(a) != 1 else '') +
              f'um {abs(d)} nach {"rechts" if d > 0 else "links"} und um {abs(e)} nach {"oben" if e > 0 else "unten"} verschoben')
    if s == 2:
        if R.random() < 0.5:
            return auswahl(f'Die Normalparabel wird {beschr}. Welche Gleichung entsteht?', par(a, d, e),
                           [par(a, -d, e), par(a, e, d), par(-a, d, e)],
                           f'Form a = {dz(a)}, Scheitel S({dz(d)} | {dz(e)}): {par(a, d, e)}.', 'Erst a bestimmen, dann den Scheitel.')
        return luecken(f'Die Normalparabel wird {beschr}. Gib a und den Scheitel an.', 'a = □; S(□ | □)', 'a ganzzahlig; dann x und y des Scheitels',
                       [a, d, e], f'a = {dz(a)}, Scheitel S({dz(d)} | {dz(e)}). Gleichung {par(a, d, e)}.', 'Spiegeln heißt a negativ.',
                       c=[cz(a), str(d), str(e)]) if Fr(a).denominator == 1 else None
    art = R.random()
    if art < 0.35:
        b = luecken('Die gezeichnete Parabel hat die Form y = a(x − d)² + e mit a = 1 oder a = −1. Gib a und den Scheitel an.', 'a = □; S(□ | □)', 'a; dann x und y des Scheitels',
                    [1 if a > 0 else -1, d, e], f'Scheitel S({dz(d)} | {dz(e)}); geöffnet nach {"oben" if a > 0 else "unten"}, Form der Normalparabel: a = {1 if a > 0 else -1}.',
                    'Lies den Scheitel ab und prüfe: einen Schritt nach rechts, wie weit nach oben/unten?', c=['1' if a > 0 else '-1', str(d), str(e)])
        aa = 1 if a > 0 else -1
        return bild(b, par_bild([(aa, d, e, '')], (d - 4, d + 4), (min(e - 1, -1) if aa > 0 else e - 8, e + 8 if aa > 0 else max(e + 1, 1))))
    if art < 0.7:
        x0 = nz(4)
        y = a * (x0 - d) ** 2 + e
        return zahl(f'Berechne den y-Wert von {par(a, d, e)} an der Stelle x = {dz(x0)}.',
                    f'y = {dz(a)} · ({dz(x0)} {plus(-d)})² {plus(e)} = {dz(a)} · {dz((x0 - d) ** 2)} {plus(e)} = {dz(y)}.',
                    'Klammer, dann Quadrat, dann mal a, dann plus e.', y, f'{cz(a)} * (({x0}) - ({d})) ** 2 + ({e})')
    return auswahl(f'Jemand liest bei {par(a, d, e)} den Scheitel S({dz(-d)} | {dz(e)}) ab. Was stimmt?',
                   f'Falsch: Die Klammer ist 0 für x = {dz(d)}, also S({dz(d)} | {dz(e)}).',
                   ['Richtig.', f'Falsch: S({dz(-d)} | {dz(-e)}).', f'Falsch: S({dz(e)} | {dz(d)}).'],
                   f'{minus_klammer(d)} = 0 ⇔ x = {dz(d)}. Scheitel S({dz(d)} | {dz(e)}).', 'Setze x = ' + dz(-d) + ' ein: Wird die Klammer null?')


def g_punkte(s):
    x0, y0 = nz(5), nz(6)
    if s == 1:
        d = nz(5)
        if R.random() < 0.5:
            return luecken(f'P({dz(x0)} | {dz(y0)}) liegt auf dem Graphen von f. Wohin kommt P auf dem Graphen von g(x) = f({minus_klammer(d)[1:-1]})?', LP, HP,
                           [x0 + d, y0], f"f({minus_klammer(d)[1:-1]}) ist um {abs(d)} nach {'rechts' if d > 0 else 'links'} verschoben: P'({dz(x0 + d)} | {dz(y0)}).",
                           'Klammer mit x − d heißt: nach rechts um d.', c=[f'({x0}) + ({d})', str(y0)])
        e = d
        return luecken(f'P({dz(x0)} | {dz(y0)}) liegt auf dem Graphen von f. Wohin kommt P auf dem Graphen von g(x) = f(x) {plus(e)}?', LP, HP,
                       [x0, y0 + e], f"Verschiebung um {abs(e)} nach {'oben' if e > 0 else 'unten'}: P'({dz(x0)} | {dz(y0 + e)}).",
                       'Eine Zahl hinter f(x) verschiebt nach oben oder unten.', c=[str(x0), f'({y0}) + ({e})'])
    a = R.choice([2, 3, -1, -2, Fr(1, 2)])
    d, e = nz(4), nz(5)
    gx = f'{"" if a == 1 else ("−" if a == -1 else dz(a) + " · ")}f({minus_klammer(d)[1:-1]}) {plus(e)}'
    nx, ny = x0 + d, a * y0 + e
    if not endlich(ny) or Fr(ny).denominator != 1: return None
    if s == 2:
        return luecken(f'P({dz(x0)} | {dz(y0)}) liegt auf dem Graphen von f. Wohin kommt P auf dem Graphen von g(x) = {gx}?', LP, HP, [nx, ny],
                       f"x: {dz(x0)} {plus(d)} = {dz(nx)}. y: {dz(a)} · {kl(y0)} {plus(e)} = {dz(ny)}. P'({dz(nx)} | {dz(ny)}).",
                       'x: um d verschieben. y: erst mal a, dann plus e.', c=[f'({x0}) + ({d})', f'{cz(a)} * ({y0}) + ({e})'])
    art = R.random()
    if art < 0.4:
        f1 = f"P'({dz(x0 - d)} | {dz(ny)})"
        f2 = f"P'({dz(nx)} | {dz(a * (y0 + e))})"
        f3 = f"P'({dz(x0 - d)} | {dz(a * y0 - e)})"
        return auswahl(f'P({dz(x0)} | {dz(y0)}) liegt auf dem Graphen von f. Welcher Punkt liegt auf g(x) = {gx}?', f"P'({dz(nx)} | {dz(ny)})",
                       [f1, f2, f3], f"x: {dz(x0)} {plus(d)} = {dz(nx)}; y: {dz(a)} · {kl(y0)} {plus(e)} = {dz(ny)}.",
                       'Reihenfolge bei y: erst strecken, dann verschieben.')
    if art < 0.7:
        # Umkehr: Bildpunkt gegeben, Urpunkt gesucht
        return luecken(f"Auf dem Graphen von g(x) = {gx} liegt P'({dz(nx)} | {dz(ny)}). Welcher Punkt P auf dem Graphen von f gehört dazu?", 'P(□ | □)', 'x, y',
                       [x0, y0], f'Rückwärts: x = {dz(nx)} {plus(-d)} = {dz(x0)}; y = ({dz(ny)} {plus(-e)}) : {kl(a)} = {dz(y0)}.',
                       'Schritte rückwärts: erst e abziehen, dann durch a teilen; x um d zurückschieben.', c=[f'({nx}) - ({d})', f'(({ny}) - ({e})) / {cz(a)}'])
    return auswahl(f'P({dz(x0)} | {dz(y0)}) liegt auf f. Jemand rechnet für g(x) = f({minus_klammer(d)[1:-1]}) den Bildpunkt P\'({dz(x0 - d)} | {dz(y0)}). Was stimmt?',
                   f"Falsch: f({minus_klammer(d)[1:-1]}) schiebt nach {'rechts' if d > 0 else 'links'}, also P'({dz(x0 + d)} | {dz(y0)}).",
                   ['Richtig.', f"Falsch: P'({dz(x0)} | {dz(y0 - d)}).", f"Falsch: P'({dz(x0 + d)} | {dz(y0 + d)})."],
                   f'g({dz(x0 + d)}) = f({dz(x0 + d)} {plus(-d)}) = f({dz(x0)}) = {dz(y0)}. Also liegt ({dz(x0 + d)} | {dz(y0)}) auf g.',
                   'Probe: Setze den vermuteten x-Wert in g ein.')


GEN = {'nach_oben': g_nach_oben, 'nach_rechts': g_nach_rechts, 'strecken': g_strecken, 'spiegeln': g_spiegeln,
       'kombiniert': g_kombiniert, 'punkte': g_punkte}

if __name__ == '__main__':
    bauen('funktionen.transformation',
          'Graphen verschieben, strecken und an den Achsen spiegeln – an der Normalparabel und an beliebigen Graphen über Bildpunkte.',
          ['f(x) + e: um e nach oben (e < 0: nach unten).', 'f(x − d): um d nach rechts – das Vorzeichen in der Klammer ist umgekehrt.',
           'a · f(x): |a| > 1 gestreckt, |a| < 1 gestaucht, a < 0 zusätzlich an der x-Achse gespiegelt.',
           '−f(x): Spiegelung an der x-Achse; f(−x): Spiegelung an der y-Achse.', 'y = a(x − d)² + e hat den Scheitel S(d | e).'],
          [('Verschieben', ['nach_oben', 'nach_rechts']), ('Strecken und Spiegeln', ['strecken', 'spiegeln']),
           ('Alles zusammen', ['kombiniert', 'punkte'])],
          ETAPPEN, GEN,
          offen=['Klasse laut Liste RS 9; gebaut an Normalparabel und allgemeinen Graphen (Bildpunkte). Die RS-10-Erweiterung (transformierte Potenz-, Exponential- und Logarithmusfunktionen, Spiegelung an y = x) ist weggelassen; die Spiegelung an y = x steht im Thema funktionen.umkehr.'])
