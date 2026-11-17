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

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import ko, pkte  # noqa: E402


def _p(k, name=None):
    g = {'art': 'poly', 'k': list(k)}
    if name:
        g['name'] = name
    return g


_N = _p([0, 0, 1], 'y = x²')
UMBAU = {
    'nach_oben': {
        'einstieg': 'Eine Schablone in Form der Normalparabel liegt auf Karopapier. Du schiebst sie 3 Kästchen nach oben. '
                    'Jeder Punkt wandert gleich weit mit. Das ist eine ⟦Verschiebung⟧.',
        'woerter': [['Normalparabel', 'der Graph von y = x², Scheitel im Ursprung'],
                    ['Scheitel', 'der tiefste (oder höchste) Punkt der Parabel']],
        'bild': ko([-4, 4], [-1, 9], schritt=0, graphen=[_N], punkte=pkte({'S': (0, 0)})),
        'schritte': [
            {'text': 'Die Normalparabel y = x² hat den Scheitel S(0 | 0).'},
            {'text': '3 nach oben: Zu jedem y-Wert kommt 3 dazu.',
             'bild': {'graphen': [_N, _p([3, 0, 1], 'y = x² + 3')], 'pfeile': [[0, 0, 0, 3], [2, 4, 2, 7], [-2, 4, -2, 7]]}},
            {'text': 'Neue Gleichung: ⟦y = x² + 3⟧, Scheitel ⟦S(0 | 3)⟧.',
             'bild': {'pfeile': None, 'punkte': pkte({'S': (0, 0), 'S′': (0, 3)})}},
        ],
        'fehler': 'y = (x + 3)² ist nicht „3 nach oben“. Eine Zahl ⟦in der Klammer⟧ verschiebt nach links. Nach oben wird hinten addiert.',
        'fehler_bild': {'graphen': [_N, _p([9, 6, 1], 'falsch')], 'punkte': None},
        'regel': 'Plus e hinten schiebt die Parabel um e nach oben. Scheitel: ⟦S(0 | e)⟧, bei e < 0 geht es nach unten.',
    },
    'nach_rechts': {
        'einstieg': 'Jetzt schiebst du die Schablone 2 Kästchen nach rechts. Der Scheitel liegt dann bei x = 2. '
                    'Überraschung: In der Gleichung steht dafür ⟦x − 2⟧, mit Minus.',
        'woerter': [['Klammer wird 0', 'an dieser Stelle x liegt der Scheitel; bei (x − 2) ist das x = 2']],
        'bild': ko([-5, 5], [-1, 9], schritt=0, graphen=[_N], punkte=pkte({'S': (0, 0)})),
        'schritte': [
            {'text': 'Bei y = (x − 2)²: Die Klammer wird 0 für x = 2.'},
            {'text': 'Dort liegt der tiefste Punkt: ⟦S(2 | 0)⟧.',
             'bild': {'graphen': [_N, _p([4, -4, 1], 'neu')], 'punkte': pkte({'S′': (2, 0)})}},
            {'text': 'Die Parabel ist also um 2 ⟦nach rechts⟧ verschoben.', 'bild': {'pfeile': [[0, 0, 2, 0], [-2, 4, 0, 4]]}},
        ],
        'fehler': 'y = (x + 4)² heißt nicht „4 nach rechts“. Die Klammer wird 0 für x = −4, also ⟦4 nach links⟧.',
        'fehler_bild': {'graphen': [_N, _p([16, 8, 1], '(x + 4)²')], 'pfeile': [[0, 0, -4, 0]], 'punkte': pkte({'S′': (-4, 0)})},
        'regel': 'Die Zahl in der Klammer schiebt nach links oder rechts. Bei ⟦(x − d)²⟧ liegt der Scheitel bei S(d | 0).',
    },
    'strecken': {
        'einstieg': 'Nun nimmst du eine Schablone, die doppelt so steil ist. Jeder y-Wert ist doppelt so groß wie bei x². '
                    'Die Parabel wird enger, sie ist ⟦gestreckt⟧.',
        'woerter': [['gestreckt', 'enger und steiler: alle y-Werte mal eine Zahl größer als 1'],
                    ['gestaucht', 'weiter und flacher: alle y-Werte mal eine Zahl zwischen 0 und 1'],
                    ['nach unten geöffnet', 'bei negativem a hängt die Parabel wie ein Bogen nach unten']],
        'bild': ko([-4, 4], [-9, 9], schritt=0, graphen=[_N]),
        'schritte': [
            {'text': 'Bei y = 2x² und x = 2: 2 · 4 = ⟦8⟧ statt 4.',
             'bild': {'graphen': [_N, _p([0, 0, 2], 'y = 2x²')], 'punkte': pkte({'(2|4)': (2, 4), '(2|8)': (2, 8)})}},
            {'text': 'Doppelt so hoch, also enger: Die Parabel ist gestreckt.'},
            {'text': 'y = −0,5x²: Für x = 4 ist y = −0,5 · 16 = ⟦−8⟧.',
             'bild': {'graphen': [_N, _p([0, 0, 2], 'y = 2x²'), _p([0, 0, -0.5], '−0,5x²')], 'punkte': pkte({'_R': (4, -8)})}},
            {'text': 'Halb so hoch, also gestaucht, und nach unten geöffnet.'},
        ],
        'fehler': 'y = 2x² für x = 2 nicht als (2 · 2)² = 16 rechnen. Erst ⟦quadrieren⟧, dann mal 2: 2 · 4 = 8.',
        'regel': 'Mal a streckt oder staucht die Parabel. ⟦|a| > 1⟧ heißt enger, |a| < 1 weiter, negatives a nach unten geöffnet.',
    },
    'spiegeln': {
        'einstieg': 'Drehst du die Schablone um wie eine Buchseite, wird sie gespiegelt. Klappst du um die senkrechte Achse, '
                    'tauschen links und rechts. Das heißt ⟦Spiegeln an der y-Achse⟧.',
        'woerter': [['Spiegeln an der y-Achse', 'links und rechts tauschen: (x | y) wird (−x | y)'],
                    ['Spiegeln an der x-Achse', 'oben und unten tauschen: (x | y) wird (x | −y)']],
        'bild': ko([-5, 5], [-2, 8], schritt=0, graphen=[_p([5, -4, 1], 'f')], punkte=pkte({'S': (2, 1)})),
        'schritte': [
            {'text': 'Die Parabel y = (x − 2)² + 1 hat den Scheitel S(2 | 1).'},
            {'text': 'Spiegeln an der y-Achse: x durch −x ersetzen.'},
            {'text': '(−x − 2)² = (x + 2)², also ⟦y = (x + 2)² + 1⟧.',
             'bild': {'graphen': [_p([5, -4, 1], 'f'), _p([5, 4, 1], 'Bild')]}},
            {'text': 'Neuer Scheitel ⟦S′(−2 | 1)⟧. Spiegeln an der x-Achse ändert dagegen nur y.',
             'bild': {'punkte': pkte({'S': (2, 1), 'S′': (-2, 1)})}},
        ],
        'fehler': 'S′(−2 | −1) ist falsch. An der ⟦y-Achse⟧ ändert sich nur x, die Höhe bleibt gleich.',
        'fehler_bild': {'punkte': pkte({'S': (2, 1), 'S′': (-2, 1), 'falsch': (-2, -1)})},
        'regel': 'An der y-Achse spiegeln: x wird −x. An der ⟦x-Achse⟧ spiegeln: y wird −y.',
    },
    'kombiniert': {
        'einstieg': 'Jetzt machst du alles nacheinander: Schablone tauschen, umdrehen, verschieben. '
                    'Die Gleichung y = a(x − d)² + e erzählt das ganze Rezept. Sie heißt ⟦Scheitelform⟧.',
        'woerter': [['Scheitelform', 'y = a(x − d)² + e; daraus liest man S(d | e) und die Form a ab']],
        'bild': ko([-3, 7], [-5, 6], schritt=0, graphen=[_N]),
        'schritte': [
            {'text': 'In y = −0,5(x − 3)² + 4 ist a = −0,5.'},
            {'text': 'Also gestaucht und nach unten geöffnet.', 'bild': {'graphen': [_N, _p([0, 0, -0.5], 'a = −0,5')]}},
            {'text': 'Dann 3 nach rechts und 4 nach oben.',
             'bild': {'graphen': [_N, _p([0, 0, -0.5], 'a = −0,5'), _p([-0.5, 3, -0.5], 'fertig')], 'pfeile': [[0, 0, 3, 4]]}},
            {'text': 'Der Scheitel ist ⟦S(3 | 4)⟧.', 'bild': {'pfeile': None, 'punkte': pkte({'S': (3, 4)})}},
        ],
        'fehler': 'Bei y = 2(x + 1)² − 5 ist S(1 | −5) falsch. Die Klammer wird 0 für ⟦x = −1⟧, also S(−1 | −5).',
        'regel': 'Scheitelform: den ⟦Scheitel S(d | e)⟧ direkt ablesen. Dann sagt a, ob gestreckt, gestaucht oder nach unten geöffnet.',
    },
    'punkte': {
        'einstieg': 'Auf der Schablone ist ein Punkt P markiert. Verschiebst du die Schablone, wandert P mit. '
                    'Sein Ziel kannst du ausrechnen, ohne die Gleichung zu kennen. Es heißt ⟦Bildpunkt⟧.',
        'woerter': [['Bildpunkt', 'wohin P nach dem Abbilden kommt; geschrieben P′'],
                    ['f(x − 3)', 'der Graph von f, um 3 nach rechts verschoben']],
        'bild': ko([-1, 6], [-1, 9], punkte=pkte({'P': (1, 4)})),
        'schritte': [
            {'text': 'Gegeben: P(1 | 4) und g(x) = 2 · f(x − 3) − 1.'},
            {'text': 'x: f(x − 3) heißt 3 nach rechts, 1 + 3 = 4.',
             'bild': {'punkte': pkte({'P': (1, 4), '_Q': (4, 4)}), 'pfeile': [[1, 4, 4, 4]]}},
            {'text': 'y: erst mal 2, dann minus 1: 2 · 4 − 1 = 7.',
             'bild': {'punkte': pkte({'P': (1, 4), '_Q': (4, 4), 'P′': (4, 7)}), 'pfeile': [[1, 4, 4, 4], [4, 4, 4, 7]]}},
            {'text': 'Der Bildpunkt ist ⟦P′(4 | 7)⟧.'},
        ],
        'fehler': 'f(x − 3) schiebt nicht nach links. Es heißt ⟦3 nach rechts⟧, also x + 3, wie bei (x − 3)².',
        'fehler_bild': {'punkte': pkte({'P': (1, 4), 'falsch': (-2, 7)}), 'pfeile': [[1, 4, -2, 7]]},
        'regel': 'x-Wert plus d, y-Wert mal a plus e. So wird P(x | y) zu ⟦P′(x + d | a · y + e)⟧.',
    },
}
UMBAU_OFFEN = []
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-1) ----------
# Prüfungsvorbilder: Realschul-Abschlussprüfung Mathematik I (Bayern), Teil A „Funktionen“: Parabelgleichung aus Scheitel und Punkt,
# Parabel durch Verschiebung so abbilden, dass sie durch einen Punkt geht, Brückenbögen als Parabeln; Jahrgangsstufentest 9 I.
# Typ übernommen, Wortlaut und Zahlen eigen.
def durchsicht(d):
    from _rsib1 import Z, A, L, nachtrag, finde
    T = lambda teil: finde(d, teil)
    # Die Ablese-Aufgaben haben denselben Text (verschiedene Grafiken): je Karte zwei davon auf Stufe 2 setzen.
    idx_oben = [i for i, a in enumerate(d['aufgaben']) if a['l'] == 'nach_oben' and a['p'] == 'uebung' and a['s'] == 3 and 'gezeichnete Parabel' in a['f']['text']][:2]
    idx_rechts = [i for i, a in enumerate(d['aufgaben']) if a['l'] == 'nach_rechts' and a['p'] == 'uebung' and a['s'] == 3 and 'gezeichnete Parabel' in a['f']['text']][:2]
    for i in idx_oben + idx_rechts:
        d['aufgaben'][i]['s'] = 2
    nachtrag(d,
        umstufen={
            T('Die Normalparabel wird um 6 nach unten verschoben. Welchen y-Wert'): 2,
            T('Welcher Punkt liegt auf g(x) = 2 · f(x − 4) + 2?'): 2,
            T('Berechne den y-Wert von y = 3(x − 4)² − 6 an der Stelle x = 3.'): 2,
        },
        ersetzen={
            T('Berechne den y-Wert der Parabel y = (x + 3)² an der Stelle x = 1.'):
                L(3, 'Die Parabel y = (x − d)² hat an der Stelle x = 0 den y-Wert 16. Welche zwei Werte kann d haben? (kleineren zuerst)',
                  'd₁ = □; d₂ = □', [-4, 4], ['-4', '4'], 'x = 0: (0 − d)² = d² = 16 ⇒ d = −4 oder d = 4.',
                  'Setze x = 0 ein. Welche Zahlen ergeben im Quadrat 16?'),
            T('Berechne den y-Wert der Parabel y = (x + 4)² an der Stelle x = −5.'):
                A(3, 'Jemand sagt: „y = (x + 5)² ist die Normalparabel, um 5 nach rechts verschoben.“ Was stimmt?',
                  'Falsch: Die Klammer ist 0 für x = −5, also 5 nach links.', ['Richtig.', 'Falsch: 5 nach oben.', 'Falsch: 25 nach rechts.'],
                  'Der Scheitel liegt dort, wo die Klammer 0 wird: x + 5 = 0 ⇒ x = −5. Das ist links.',
                  'Für welches x wird die Klammer null?'),
            T('Die Parabel y = (x − 3)² − 5 wird an der x-Achse gespiegelt.'):
                L(3, 'Die Parabel y = (x − 1)² + 2 wird erst an der x-Achse und dann an der y-Achse gespiegelt. Gib den Scheitel des Bildes an.',
                  'S(□ | □)', [-1, -2], ['-1', '-2'], 'Scheitel S(1 | 2). x-Achse: (1 | −2). y-Achse: (−1 | −2).',
                  'Verfolge nur den Scheitel durch beide Spiegelungen.'),
            T('Die Parabel y = (x − 2)² − 2 wird an der x-Achse gespiegelt.'):
                A(3, 'Die Parabel y = x² + 1 wird an der x-Achse gespiegelt. Liegt der Punkt P(2 | −5) auf dem Bild?',
                  'Ja, denn (2 | 5) liegt auf y = x² + 1.', ['Nein, das Bild ist nach oben geöffnet.', 'Nein, (2 | −5) liegt unter dem Scheitel.', 'Ja, denn 2² − 1 = −5.'],
                  'Gespiegelt wird y zu −y: Das Bild ist y = −x² − 1. Für x = 2: y = −4 − 1 = −5. Ja.',
                  'Spiegle P zurück und prüfe auf der ursprünglichen Parabel.'),
            T('Jemand liest bei y = 2(x + 5)² + 2 den Scheitel S(5 | 2) ab.'):
                L(3, 'Eine Parabel hat den Scheitel S(2 | −3) und geht durch P(4 | 5). Gib ihre Gleichung in Scheitelform an.',
                  'y = □ · (x − □)² − □', [2, 2, 3], ['(5 + 3)/(4 - 2)**2', '2', '3'],
                  'Ansatz y = a(x − 2)² − 3. P einsetzen: 5 = a · 4 − 3 ⇒ a = 2. y = 2(x − 2)² − 3.',
                  'Setze den Scheitel ein und bestimme a mit P.'),
            T('P(−2 | −4) liegt auf f. Jemand rechnet für g(x) = f(x − 2)'):
                L(3, 'Der Punkt P′(5 | 1) liegt auf dem Graphen von g(x) = f(x − 2) + 3. Welcher Punkt P des Graphen von f gehört dazu?',
                  'P(□ | □)', [3, -2], ['5 - 2', '1 - 3'], 'Zurück: x − 2 und y − 3. P(3 | −2).', 'Mache beide Verschiebungen rückgängig.'),
            T('P(2 | −3) liegt auf f. Jemand rechnet für g(x) = f(x − 1)'):
                L(3, 'Der Graph von f hat den Scheitel S(1 | 2). Gib den Scheitel des Graphen von g(x) = −f(x + 3) + 1 an.',
                  'S′(□ | □)', [-2, -1], ['1 - 3', '-2 + 1'], 'x: f(x + 3) schiebt 3 nach links: 1 − 3 = −2. y: mal −1, dann plus 1: −2 + 1 = −1.',
                  'Erst x, dann y: Vorzeichen umdrehen, dann 1 dazu.'),
        },
        neu={
            'nach_oben': [
                Z(3, 'Die Normalparabel wird so nach oben oder unten verschoben, dass sie durch P(3 | 4) geht. Um wie viel muss man sie nach oben verschieben? (Nach unten: negative Zahl.)',
                  -5, '4 - 3**2', 'Gleichung y = x² + e. P einsetzen: 4 = 9 + e ⇒ e = −5, also 5 nach unten.', 'Setze P in y = x² + e ein.'),
                Z(3, 'Die Parabel y = x² + e schneidet die x-Achse bei x = −3 und x = 3. Wie groß ist e?',
                  -9, '0 - 3**2', 'Punkt (3 | 0) einsetzen: 0 = 9 + e ⇒ e = −9.', 'Welcher Punkt liegt auf der x-Achse?'),
                Z(3, 'Die Parabeln y = x² + 2 und y = x² − 3 werden gezeichnet. Wie weit liegen sie an jeder Stelle senkrecht auseinander?',
                  5, '2 - (-3)', 'An jeder Stelle x: (x² + 2) − (x² − 3) = 5. Die Parabeln sind übereinander verschoben.', 'Ziehe die Terme voneinander ab.'),
                A(3, 'Hat die Parabel y = x² + 1 Schnittpunkte mit der x-Achse?',
                  'Nein, ihr tiefster Punkt liegt bei y = 1.', ['Ja, bei x = 1 und x = −1.', 'Ja, bei x = −1.', 'Ja, im Ursprung.'],
                  'x² ist nie negativ, also ist x² + 1 immer mindestens 1. Die Parabel bleibt über der x-Achse.', 'Wo liegt der Scheitel?'),
                L(3, 'Der Punkt P(2 | 7) liegt auf einer Parabel y = x² + e. Welcher andere Punkt mit dem gleichen y-Wert liegt auch auf ihr?',
                  'Q(□ | □)', [-2, 7], ['-2', '7'], 'Die Parabel ist symmetrisch zur y-Achse: (−2)² = 2². Also Q(−2 | 7).',
                  'Die Parabel ist zur y-Achse symmetrisch.'),
            ],
            'nach_rechts': [
                A(3, 'Die Normalparabel wird nur nach links oder rechts verschoben, sodass sie durch P(1 | 9) geht. Welche Gleichung ist möglich?',
                  'y = (x + 2)²', ['y = (x − 2)²', 'y = (x + 3)²', 'y = x² + 8'],
                  '(1 − d)² = 9 ⇒ 1 − d = 3 oder −3 ⇒ d = −2 oder d = 4. Möglich sind y = (x + 2)² und y = (x − 4)²; von den Antworten passt y = (x + 2)².',
                  'Setze P in y = (x − d)² ein. Es gibt zwei Möglichkeiten.'),
                Z(3, 'Die Parabel y = (x − d)² geht durch P(5 | 4), und ihr Scheitel liegt rechts von P. Wie groß ist d?',
                  7, '5 + 2', '(5 − d)² = 4 ⇒ 5 − d = ±2 ⇒ d = 3 oder d = 7. Rechts von P (x > 5): d = 7.', 'Setze P ein. Welche Lösung liegt rechts von x = 5?'),
                L(3, 'Wo schneidet die Parabel y = (x − 3)² die y-Achse?', 'S(□ | □)', [0, 9], ['0', '(0 - 3)**2'],
                  'Auf der y-Achse ist x = 0: y = (0 − 3)² = 9.', 'Welchen x-Wert haben Punkte auf der y-Achse?'),
                Z(3, 'An welcher Stelle x haben die Parabeln y = (x + 2)² und y = (x − 4)² denselben y-Wert?',
                  1, '(-2 + 4)/2', 'Die Scheitel liegen bei −2 und 4. In der Mitte, bei x = 1, sind beide Abstände 3: y = 9 bei beiden.',
                  'Wo liegt die Mitte zwischen den beiden Scheiteln?'),
            ],
            'strecken': [
                Z(3, 'Ein Brückenbogen hat die Form y = a · x² mit dem Scheitel oben im Ursprung. Er ist 20 m breit und 5 m hoch. Berechne a.',
                  -0.05, '-5/10**2', 'Die Enden liegen bei (10 | −5) und (−10 | −5). −5 = a · 100 ⇒ a = −0,05.',
                  'Zeichne eine Skizze: Wo liegen die Enden des Bogens?'),
                Z(3, 'Die Parabel y = a · x² geht durch P(2 | 3). Welchen y-Wert hat sie an der Stelle x = −4?',
                  12, '3/2**2*(-4)**2', 'a = 3 : 4 = 0,75. Bei x = −4: 0,75 · 16 = 12.', 'Bestimme zuerst a.'),
            ],
            'spiegeln': [
                L(3, 'Die Parabel y = (x − 3)² − 4 wird an der y-Achse gespiegelt. In welchem Punkt schneiden sich Parabel und Bild?',
                  'S(□ | □)', [0, 5], ['0', '(0 - 3)**2 - 4'],
                  'Das Bild ist y = (x + 3)² − 4. Beide sind zueinander spiegelbildlich und treffen sich auf der y-Achse: y = 9 − 4 = 5.',
                  'Wo treffen sich ein Bild und sein Spiegelbild?'),
                A(3, 'Welche Spiegelung bildet y = (x − 2)² auf y = (x + 2)² ab?',
                  'Spiegelung an der y-Achse', ['Spiegelung an der x-Achse', 'Verschiebung um 2 nach links', 'Spiegelung an der Geraden y = x'],
                  'Der Scheitel wandert von (2 | 0) nach (−2 | 0), die Öffnung bleibt: x wird zu −x. Eine Verschiebung um 4 nach links ginge auch – aber keine der anderen Antworten.',
                  'Was passiert mit dem Scheitel?'),
            ],
            'kombiniert': [
                L(3, 'Die Parabel y = −(x − 1)² + 4 schneidet die x-Achse zweimal. Gib beide Stellen an. (kleinere zuerst)',
                  'x₁ = □; x₂ = □', [-1, 3], ['1 - 2', '1 + 2'], '−(x − 1)² + 4 = 0 ⇒ (x − 1)² = 4 ⇒ x − 1 = ±2 ⇒ x = −1 oder x = 3.',
                  'Setze y = 0 und forme nach der Klammer um.'),
                L(3, 'Eine Parabel y = a(x − 1)² + e geht durch die Punkte (0 | −1) und (3 | 5). Bestimme a und e.',
                  'a = □; e = □', [2, -3], ['(5 + 1)/(4 - 1)', '-1 - 2'],
                  '(0 | −1): a + e = −1. (3 | 5): 4a + e = 5. Abziehen: 3a = 6 ⇒ a = 2, e = −3.',
                  'Setze beide Punkte ein und vergleiche die beiden Gleichungen.'),
                L(3, 'Um welchen Vektor muss man y = 2(x + 1)² − 3 verschieben, damit der Scheitel im Ursprung liegt?',
                  'Vektor (□ | □)', [1, 3], ['0 - (-1)', '0 - (-3)'], 'Scheitel S(−1 | −3). Zum Ursprung: 1 nach rechts, 3 nach oben.',
                  'Wo liegt der Scheitel jetzt?'),
            ],
            'punkte': [
                L(3, 'Es ist f(x) = x² und g(x) = 2 · f(x − 1) − 3. Gib g in Scheitelform an.',
                  'g(x) = □ · (x − □)² − □', [2, 1, 3], ['2', '1', '3'], 'f(x − 1) = (x − 1)². Also g(x) = 2(x − 1)² − 3.',
                  'Ersetze in f das x durch (x − 1).'),
                Z(3, 'Der Punkt P(2 | 4) liegt auf dem Graphen von g(x) = f(x − 2). Welchen Wert hat f(0)?',
                  4, '4', 'g(2) = f(2 − 2) = f(0). Weil P auf g liegt, ist g(2) = 4. Also f(0) = 4.', 'Setze x = 2 in g(x) = f(x − 2) ein.'),
                A(3, 'Es ist g(x) = f(x − 3) + 2. Welcher Punkt des Graphen von f wird auf sich selbst abgebildet?',
                  'Keiner: Jeder Punkt wandert 3 nach rechts und 2 nach oben.', ['Der Scheitel', 'Der Punkt (3 | 2)', 'Alle Punkte auf der x-Achse'],
                  'Jeder Punkt (x | y) wird zu (x + 3 | y + 2). Das ist nie derselbe Punkt.', 'Was passiert mit einem beliebigen Punkt (x | y)?'),
            ],
        })


if __name__ == '__main__':
    d = bauen('funktionen.transformation',
          'Graphen verschieben, strecken und an den Achsen spiegeln – an der Normalparabel und an beliebigen Graphen über Bildpunkte.',
          ['f(x) + e: um e nach oben (e < 0: nach unten).', 'f(x − d): um d nach rechts – das Vorzeichen in der Klammer ist umgekehrt.',
           'a · f(x): |a| > 1 gestreckt, |a| < 1 gestaucht, a < 0 zusätzlich an der x-Achse gespiegelt.',
           '−f(x): Spiegelung an der x-Achse; f(−x): Spiegelung an der y-Achse.', 'y = a(x − d)² + e hat den Scheitel S(d | e).'],
          [('Verschieben', ['nach_oben', 'nach_rechts']), ('Strecken und Spiegeln', ['strecken', 'spiegeln']),
           ('Alles zusammen', ['kombiniert', 'punkte'])],
          ETAPPEN, GEN,
          offen=['Klasse laut Liste RS 9; gebaut an Normalparabel und allgemeinen Graphen (Bildpunkte). Die RS-10-Erweiterung (transformierte Potenz-, Exponential- und Logarithmusfunktionen, Spiegelung an y = x) ist weggelassen; die Spiegelung an y = x steht im Thema funktionen.umkehr.'])
    umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
    durchsicht(d)
