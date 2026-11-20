#!/usr/bin/env python3
"""Thema funktionen.betrag – Betragsfunktion (IB MYP 4, etwa Klasse 9)."""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403
from _rsib2 import PLAN2, art3  # noqa: E402

start(7504)

HS = 'Koordinaten des Punktes'


def inn(d):
    return 'x' if d == 0 else f'x {plus(-d)}'


def bterm(a, d, e):
    """Text a·|x − d| + e."""
    innen = 'x' if d == 0 else (f'x − {dz(d)}' if d > 0 else f'x + {dz(-d)}')
    vor = '' if a == 1 else ('−' if a == -1 else dz(a) + ' · ' if a not in (1, -1) else '')
    if a not in (1, -1): vor = (dz(a) if a > 0 else '−' + dz(-a)) + ' · '
    t = f'{vor}|{innen}|'
    if e: t += f' {plus(e)}'
    return t


def bgraph(a, d, e, x=(-6, 6), name=None, y=None):
    lo, hi = x
    # Durchsicht 19: eigene Graph-Art „betrag“ (seit 15.11.) statt zwei Geradenstücken
    g = [{'art': 'betrag', 'a': int(a) if a == int(a) else float(a), 'b': d, 'c': e}]
    if name: g[0]['name'] = name
    if y is None:
        ws = [a * abs(t - d) + e for t in (lo, hi)] + [e]
        y = (math.floor(min(ws)) - 1, math.ceil(max(ws)) + 1)
    return koord(g, x=x, y=y, punkte=[{'x': d, 'y': e, 'name': 'S'}] if name is None else None)


ETAPPEN = [
    {'lernziel': 'betrag', 'titel': 'Betrag berechnen',
     'regel': 'Der ⟦Betrag⟧ (absolute value) |a| ist der ⟦Abstand der Zahl a von 0⟧ auf dem Zahlenstrahl. Er ist nie negativ: |5| = 5 und |−5| = 5. |a − b| ist der ⟦Abstand⟧ der Zahlen a und b.',
     'schritte': ['f(x) = |x − 3| + 1 an der Stelle x = −2.', 'Innen zuerst: −2 − 3 = −5. Betrag: |−5| = 5.', 'f(−2) = 5 + 1 = ⟦6⟧.'],
     'probe': 'Abstand von −2 zu 3 sind 5 Schritte ✓',
     'bild': {'typ': 'zahlenstrahl', 'start': -5, 'ende': 5, 'abschnitte': 10, 'beschriftet': 'anfang_ende'},
     'fehler': '|−2 − 3| = |−2| − |3| = −1 ist falsch: Erst ⟦innen ausrechnen⟧ (−5), dann den Betrag nehmen: 5. Beträge darf man nicht einzeln abziehen.'},
    {'lernziel': 'graph', 'titel': 'Graph und Knickpunkt',
     'regel': 'Der Graph von f(x) = |x| ist ein ⟦V⟧ mit Spitze im Ursprung. f(x) = a · |x − d| + e ist dieses V, ⟦um d nach rechts und um e nach oben verschoben⟧, mit ⟦Knickpunkt⟧ (vertex) S(d | e). Der Faktor a macht das V steiler (|a| > 1) oder flacher; bei a < 0 ⟦öffnet es nach unten⟧.',
     'schritte': ['f(x) = 2 · |x − 1| − 3.', 'Innen steht x − 1: Verschiebung um 1 nach rechts; −3: um 3 nach unten.', 'Knickpunkt ⟦S(1 | −3)⟧; Steigung rechts 2, links −2.'],
     'probe': 'f(1) = 2 · 0 − 3 = −3 ✓',
     'bild': {'typ': 'koordinaten', 'x': [-4, 6], 'y': [-4, 6], 'graphen': [{'art': 'linear', 'm': -2, 't': -1, 'bereich': [-4, 1]}, {'art': 'linear', 'm': 2, 't': -5, 'bereich': [1, 6]}],
              'punkte': [{'x': 1, 'y': -3, 'name': 'S'}]},
     'fehler': 'Bei f(x) = |x − 1| den Knick bei x = −1 zu suchen ist falsch: Der Knick liegt dort, wo ⟦innen 0⟧ herauskommt: x − 1 = 0, also ⟦x = 1⟧.'},
    {'lernziel': 'stueckweise', 'titel': 'Stückweise ohne Betrag schreiben',
     'regel': 'Ohne Betragsstriche schreibt man f ⟦stückweise⟧ (piecewise): Ist der Inhalt ⟦≥ 0⟧, bleibt er wie er ist; ist er ⟦< 0⟧, nimmt man sein ⟦Gegenteil⟧. Die Grenze ist der Knick.',
     'schritte': ['f(x) = |x − 2|. Grenze: x − 2 = 0, also x = 2.', 'Für x ≥ 2: f(x) = x − 2.', 'Für x < 2: f(x) = −(x − 2) = ⟦−x + 2⟧.'],
     'probe': 'x = 0: |0 − 2| = 2 und −0 + 2 = 2 ✓',
     'fehler': 'Für x < 2 einfach f(x) = x + 2 zu schreiben ist falsch: Man muss die ⟦ganze Klammer negieren⟧: −(x − 2) = −x + 2. Probe mit x = 0: |0 − 2| = 2, aber 0 + 2 = 2 nur zufällig – bei x = 1 ergibt x + 2 = 3, richtig ist 1.'},
    {'lernziel': 'gleichung', 'titel': 'Betragsgleichungen lösen',
     'regel': '|x − d| = c bedeutet: x hat von d den ⟦Abstand c⟧. Für c > 0 gibt es ⟦zwei Lösungen⟧: x = d − c und x = d + c. Für c = 0 eine Lösung, für ⟦c < 0 keine⟧ (ein Betrag ist nie negativ).',
     'schritte': ['|x − 4| = 3: Abstand 3 von der Zahl 4.', 'x = 4 − 3 = ⟦1⟧ oder x = 4 + 3 = ⟦7⟧.'],
     'probe': '|1 − 4| = 3 und |7 − 4| = 3 ✓',
     'fehler': 'Bei |x − 4| = 3 nur x = 7 anzugeben ist falsch: Es gibt ⟦zwei Zahlen⟧ mit Abstand 3 von 4 – auch x = 1 links davon.'},
    {'lernziel': 'verstehen', 'titel': 'Aussagen über Beträge prüfen',
     'regel': 'Prüfe Aussagen mit ⟦Zahlenbeispielen⟧, auch mit ⟦negativen Zahlen⟧. Wichtig: |a| ≥ 0, |−a| = |a|, aber im Allgemeinen ⟦|a + b| ≠ |a| + |b|⟧.',
     'schritte': ['Behauptung: |a + b| = |a| + |b|. Teste a = 3, b = −5.', '|3 + (−5)| = |−2| = 2, aber |3| + |−5| = 8. ⟦Die Aussage ist falsch⟧.'],
     'probe': 'Ein Gegenbeispiel genügt, um eine Allaussage zu widerlegen ✓',
     'fehler': '„|−x| = x für alle x“ ist falsch: Für x = −4 ist |−(−4)| = 4, aber x = −4. Richtig ist ⟦|−x| = |x|⟧.'},
]


def g_betrag(s):
    art = R.choice({1: ['zahl', 'abstand'], 2: ['f_wert', 'abstand', 'f_wert'], 3: ['f_wert_a', 'term', 'vergleich']}[s])
    if art == 'zahl':
        a, b = R.randint(-20, 20), R.randint(-20, 20)
        if a == 0 or b == 0: return None
        return zahl(f'Berechne |{dz(a)}| + |{dz(b)}|.', f'|{dz(a)}| = {abs(a)}, |{dz(b)}| = {abs(b)}. Summe: {abs(a) + abs(b)}.',
                    'Der Betrag ist der Abstand von 0 – immer positiv oder 0.', abs(a) + abs(b), f'abs({a}) + abs({b})')
    if art == 'abstand':
        a, b = R.randint(-15, 15), R.randint(-15, 15)
        if a == b: return None
        return zahl(f'Berechne |{dz(a)} − {kl(b)}|. Das ist der Abstand der Zahlen {dz(a)} und {dz(b)}.', f'{dz(a)} − {kl(b)} = {dz(a - b)}. Betrag: {abs(a - b)}.',
                    'Erst innen ausrechnen, dann den Betrag nehmen.', abs(a - b), f'abs({a} - ({b}))')
    if art in ('f_wert', 'f_wert_a'):
        a = R.choice([1, 2, 3, -1, -2, Fr(1, 2)]) if art == 'f_wert_a' else 1
        d, e = R.randint(-5, 5), R.randint(-6, 6)
        x = R.randint(-8, 8)
        if x == d: return None
        y = a * abs(x - d) + e
        return zahl(f'f(x) = {bterm(a, d, e)}. Berechne f({dz(x)}).',
                    (f'Innen: {dz(x)} {plus(-d)} = {dz(x - d)}.' if d else f'Innen: {dz(x)}.') + f' Betrag: {abs(x - d)}. f({dz(x)}) = {"" if a == 1 else dz(a) + " · "}{abs(x - d)} {plus(e) if e else ""} = {dz(y)}.'.replace('  ', ' '),
                    'Reihenfolge: innen rechnen, Betrag, dann mal a und plus e.', y, f'{float(a)} * abs({x} - ({d})) + ({e})')
    if art == 'term':
        a, b = R.randint(-9, 9), R.randint(-9, 9)
        if a == 0 or b == 0 or (a > 0) == (b > 0): return None
        return zahl(f'Berechne |{dz(a)} + {kl(b)}| − |{dz(a)}| − |{dz(b)}|.', f'|{dz(a + b)}| − {abs(a)} − {abs(b)} = {abs(a + b)} − {abs(a) + abs(b)} = {dz(abs(a + b) - abs(a) - abs(b))}.',
                    'Jeden Betrag einzeln auswerten; innen zuerst rechnen.', abs(a + b) - abs(a) - abs(b), f'abs({a} + ({b})) - abs({a}) - abs({b})')
    x, y = R.sample(range(-12, 13), 2)
    if abs(x) == abs(y): return None
    r = f'|{dz(x)}|' if abs(x) > abs(y) else f'|{dz(y)}|'
    return auswahl(f'Was ist größer: |{dz(x)}| oder |{dz(y)}|?', r, [f'|{dz(x)}|', f'|{dz(y)}|', 'Beide sind gleich'],
                   f'|{dz(x)}| = {abs(x)}, |{dz(y)}| = {abs(y)}.', 'Vergleiche die Abstände von 0, nicht die Zahlen selbst.')


def g_graph(s):
    a = 1 if s == 1 else R.choice([1, 2, 3, -1, -2, Fr(1, 2)])
    d, e = R.randint(-4, 4), R.randint(-4, 4)
    art = R.choice({1: ['knick', 'knick'], 2: ['knick', 'offen', 'ablesen'], 3: ['ablesen', 'steigung', 'nullstellen', 'welcher']}[s])
    if art == 'knick':
        return luecken(f'Gib den Knickpunkt des Graphen von f(x) = {bterm(a, d, e)} an.', 'S(□ | □)', HS, [d, e],
                       f'Innen = 0 bei x = {dz(d)}. f({dz(d)}) = {dz(e)}. Knickpunkt S({dz(d)} | {dz(e)}).',
                       'Wo wird der Inhalt der Betragsstriche 0?', c=[str(d), str(e)])
    if art == 'offen':
        r = 'nach unten' if a < 0 else 'nach oben'
        return auswahl(f'Wie ist der Graph von f(x) = {bterm(a, d, e)} geöffnet?', r, ['nach oben', 'nach unten', 'nach rechts'],
                       f'Der Faktor vor dem Betrag ist {dz(a)} – {"negativ: Das V steht auf dem Kopf." if a < 0 else "positiv: ein normales V."}',
                       'Achte auf das Vorzeichen vor den Betragsstrichen.')
    if art == 'ablesen':
        if a not in (1, -1): a = R.choice([1, -1])
        return mit_grafik(luecken('Der Graph zeigt f(x) = a · |x − d| + e mit a = 1 oder a = −1. Lies den Knickpunkt ab.', 'S(□ | □)', HS, [d, e],
                                  f'Die Spitze des V liegt bei ({dz(d)} | {dz(e)}). Also f(x) = {bterm(a, d, e)}.',
                                  'Der Knickpunkt ist die Spitze des V.', c=[str(d), str(e)]), bgraph(a, d, e, x=(-7, 7), name='f'))
    if art == 'steigung':
        if d == 0: return None  # Durchsicht 19: sonst „x + 0“ im Lösungsweg
        if a == Fr(1, 2): a = 2
        x = d + R.randint(1, 4)
        return zahl(f'f(x) = {bterm(a, d, e)}. Welche Steigung hat der Graph rechts vom Knick (für x > {dz(d)})?',
                    f'Für x > {dz(d)} ist |{inn(d)}| = x {plus(-d)}, also f(x) = {dz(a)} · (x {plus(-d)}) {plus(e) if e else ""} mit Steigung {dz(a)}.',
                    'Rechts vom Knick fallen die Betragsstriche einfach weg.', a, f'{float(a)}')
    if art == 'nullstellen':
        a = R.choice([1, -1])
        c = R.randint(1, 5)
        e = -a * c
        return luecken(f'Bestimme die Nullstellen von f(x) = {bterm(a, d, e)} (kleinere zuerst).', 'x₁ = □; x₂ = □', 'zwei ganze Zahlen', [d - c, d + c],
                       f'f(x) = 0 ⇒ |{inn(d)}| = {c} ⇒ x = {dz(d)} − {c} = {dz(d - c)} oder x = {dz(d)} + {c} = {dz(d + c)}.',
                       'Setze f(x) = 0 und forme nach dem Betrag um.', c=[str(d - c), str(d + c)])
    # welcher Term passt zum Graphen
    if a not in (1, -1): a = 1
    if d == 0: d = R.choice([-2, 2])
    r = f'f(x) = {bterm(a, d, e)}'
    return mit_grafik(auswahl('Welcher Funktionsterm gehört zum Graphen?', r, [f'f(x) = {bterm(a, -d, e)}', f'f(x) = {bterm(-a, d, e)}', f'f(x) = {bterm(a, e, d)}' if e != d else f'f(x) = {bterm(a, d, -e)}'],
                              f'Knickpunkt S({dz(d)} | {dz(e)}), {"nach oben" if a > 0 else "nach unten"} geöffnet: {r}.',
                              'Lies den Knickpunkt ab. Achtung: Bei x − d wird nach rechts verschoben.'), bgraph(a, d, e, x=(-7, 7), name='f'))


def g_stueckweise(s):
    d = R.randint(-6, 6)
    a = 1 if s == 1 else R.choice([1, 2, 3, -1, -2])
    e = 0 if s == 1 else R.randint(-5, 5)
    seite = R.choice(['links', 'rechts']) if s > 1 else 'links'
    art = R.choice({1: ['term'], 2: ['term', 'grenze'], 3: ['term', 'wert_links', 'fehler']}[s])
    if d == 0 and art == 'term' and s == 1: return None
    if art == 'grenze':
        return zahl(f'f(x) = {bterm(a, d, e)} soll stückweise ohne Betrag geschrieben werden. Bei welchem x liegt die Grenze zwischen den beiden Stücken?',
                    f'Grenze: Inhalt = 0 ⇒ {inn(d)} = 0 ⇒ x = {dz(d)}.', 'Wo wechselt der Inhalt des Betrags das Vorzeichen?', d, f'{d}')
    if art == 'term':
        if seite == 'rechts':
            m, t = a, -a * d + e
            bed = f'x ≥ {dz(d)}'
        else:
            m, t = -a, a * d + e
            bed = f'x < {dz(d)}'
        return luecken(f'Schreibe f(x) = {bterm(a, d, e)} für {bed} ohne Betragsstriche.', '□x + □', 'Term eintippen, z. B. -2x + 5', [m, t],
                       (f'Für {bed} ist {inn(d)} {"≥ 0, der Betrag fällt weg" if seite == "rechts" else "< 0, also |" + inn(d) + "| = −(" + inn(d) + ")"}. '
                        f'f(x) = {poly(m, t)}.'),
                       'Ist der Inhalt in diesem Bereich positiv oder negativ? Negativ: ganze Klammer mit −1 malnehmen.', c=[str(m), str(t)])
    if art == 'wert_links':
        x = d - R.randint(1, 5)
        m, t = -a, a * d + e
        return zahl(f'Für x < {dz(d)} gilt f(x) = {poly(m, t)}, für x ≥ {dz(d)} gilt f(x) = {poly(a, -a * d + e)}. Berechne f({dz(x)}).',
                    f'{dz(x)} < {dz(d)}: erstes Stück. f({dz(x)}) = {kl(m)} · {kl(x)} {plus(t)} = {dz(m * x + t)}.',
                    'Prüfe zuerst, in welchem Bereich der x-Wert liegt.', m * x + t, f'({m}) * ({x}) + ({t})')
    if d == 0: return None
    falsch_t = -d if a == 1 else None
    r = f'Falsch: Für x < {dz(d)} gilt f(x) = {poly(-1, d)}.'
    return auswahl(f'Tim schreibt f(x) = |{inn(d)}| für x < {dz(d)} als f(x) = {poly(-1, -d)}. Stimmt das?', r,
                   ['Richtig, das Minus kommt nur vor das x.', f'Falsch: Für x < {dz(d)} gilt f(x) = {poly(1, -d)}.', f'Falsch: Für x < {dz(d)} gilt f(x) = {poly(1, d)}.'],
                   f'Für x < {dz(d)} ist der Inhalt negativ; die ganze Klammer wird negiert: −(x {plus(-d)}) = {poly(-1, d)}. Probe x = {dz(d - 1)}: |{dz(d - 1)} {plus(-d)}| = 1.',
                   'Setze eine Zahl links vom Knick ein und vergleiche.')


def g_gleichung(s):
    d = R.randint(-8, 8)
    c = R.randint(1, 9)
    art = R.choice({1: ['zwei', 'zwei'], 2: ['keine', 'faktor', 'faktor'], 3: ['ungleich', 'sach', 'faktor', 'keine']}[s])  # Durchsicht 19: Stufe 2 ohne die Grundform
    if art == 'zwei':
        return luecken(f'Löse |{inn(d)}| = {c} (kleinere Lösung zuerst).' if d else f'Löse |x| = {c} (kleinere Lösung zuerst).', 'x₁ = □; x₂ = □', 'zwei ganze Zahlen',
                       [d - c, d + c], f'Abstand {c} von {dz(d)}: x = {dz(d)} − {c} = {dz(d - c)} oder x = {dz(d)} + {c} = {dz(d + c)}.',
                       f'Welche Zahlen haben von {dz(d)} den Abstand {c}?', c=[str(d - c), str(d + c)])
    if art == 'keine':
        cc = -c if R.random() < .7 else 0
        r = 'keine Lösung' if cc < 0 else f'genau eine Lösung: x = {dz(d)}'
        return auswahl(f'Wie viele Lösungen hat |{inn(d)}| = {dz(cc)}?', r,
                       ['keine Lösung', f'genau eine Lösung: x = {dz(d)}', f'zwei Lösungen: x = {dz(d - abs(cc))} und x = {dz(d + abs(cc))}' if cc else f'zwei Lösungen: x = {dz(d - 1)} und x = {dz(d + 1)}', 'unendlich viele'],
                       'Ein Betrag ist nie negativ: |…| = negative Zahl hat keine Lösung.' if cc < 0 else f'Nur x = {dz(d)} hat den Abstand 0 von {dz(d)}.',
                       'Kann ein Betrag negativ sein?')
    if art == 'faktor':
        k = R.choice([2, 3, 4])
        e = R.randint(-5, 5)
        if e == 0: return None  # Durchsicht 19: kein „+ 0“ im Aufgabentext
        return luecken(f'Löse {k} · |{inn(d)}| {plus(e)} = {k * c + e} (kleinere Lösung zuerst).', 'x₁ = □; x₂ = □', 'zwei ganze Zahlen',
                       [d - c, d + c], f'{k} · |{inn(d)}| = {k * c + e} {plus(-e)} = {k * c} ⇒ |{inn(d)}| = {c} ⇒ x = {dz(d - c)} oder x = {dz(d + c)}.',
                       'Stelle zuerst nach dem Betrag um, dann zwei Fälle.', c=[str(d - c), str(d + c)])
    if art == 'ungleich':
        return luecken(f'Für welche x gilt |{inn(d)}| ≤ {c}? Gib die Grenzen an.', '□ ≤ x ≤ □', 'zwei ganze Zahlen', [d - c, d + c],
                       f'Abstand höchstens {c} von {dz(d)}: von {dz(d - c)} bis {dz(d + c)}.', f'Alle Zahlen mit Abstand höchstens {c} von {dz(d)}.',
                       c=[str(d - c), str(d + c)])
    soll = R.choice([250, 500, 750, 1000])
    tol = R.choice([5, 10, 15, 20])
    return luecken(f'Eine Maschine füllt Flaschen mit {soll} ml. Erlaubt ist eine Abweichung von höchstens {tol} ml, also |x − {soll}| ≤ {tol}. Zwischen welchen Füllmengen x liegt eine erlaubte Flasche?',
                   '□ ml ≤ x ≤ □ ml', 'zwei ganze Zahlen', [soll - tol, soll + tol], f'{soll} − {tol} = {soll - tol} und {soll} + {tol} = {soll + tol}.',
                   'Abstand höchstens … vom Sollwert – nach unten und nach oben.', c=[f'{soll} - {tol}', f'{soll} + {tol}'])


def g_verstehen(s):
    art = R.choice({1: ['nie_neg', 'gegen'], 2: ['summe', 'gegen', 'loesung_fehlt'], 3: ['summe', 'produkt', 'loesung_fehlt', 'immer']}[s])
    if art == 'nie_neg':
        x = R.randint(2, 15)
        return auswahl(f'Kann |x| = −{x} für eine Zahl x gelten?', 'Nein, ein Betrag ist nie negativ.', [f'Ja, für x = −{x}.', f'Ja, für x = {x}.', f'Ja, für x = 0.'],
                       f'|−{x}| = {x} und |{x}| = {x}. Ein Abstand kann nicht negativ sein.', 'Was bedeutet der Betrag anschaulich?')
    if art == 'gegen':
        x = R.randint(2, 15)
        return auswahl(f'Stimmt |−a| = a für jede Zahl a? Teste mit a = −{x}.', f'Nein: Für a = −{x} ist |−a| = {x}, aber a = −{x}.',
                       ['Ja, das Minus verschwindet immer.', f'Ja: |−(−{x})| = −{x}.', 'Nein, |−a| ist immer negativ.'],
                       f'|−(−{x})| = |{x}| = {x} ≠ −{x}. Richtig ist |−a| = |a|.', 'Setze die negative Zahl wirklich ein.')
    if art == 'summe':
        a, b = R.randint(2, 9), -R.randint(2, 9)
        r = f'Nein: |{dz(a)} + {kl(b)}| = {abs(a + b)}, aber |{dz(a)}| + |{dz(b)}| = {abs(a) + abs(b)}.'
        return auswahl(f'Gilt |a + b| = |a| + |b| für a = {dz(a)} und b = {dz(b)}?', r,
                       [f'Ja: beide Seiten ergeben {abs(a) + abs(b)}.', f'Ja: beide Seiten ergeben {abs(a + b)}.', 'Nein, weil |a + b| immer größer ist.'],
                       f'Bei verschiedenen Vorzeichen heben sich a und b teilweise auf. Allgemein gilt nur |a + b| ≤ |a| + |b|.', 'Rechne beide Seiten getrennt aus.')
    if art == 'produkt':
        a, b = R.randint(-9, 9), R.randint(-9, 9)
        if a * b == 0: return None
        return ja_nein(f'Gilt |a · b| = |a| · |b| für a = {dz(a)} und b = {dz(b)}?', True,
                       f'|{kl(a)} · {kl(b)}| = {abs(a * b)} und {abs(a)} · {abs(b)} = {abs(a * b)}. Beim Multiplizieren gilt das sogar immer.', 'Rechne beide Seiten aus.')
    if art == 'loesung_fehlt':
        d, c = R.randint(-6, 6), R.randint(2, 8)
        r = f'Falsch: Es fehlt x = {dz(d - c)}.'
        return auswahl(f'Ali löst |{inn(d)}| = {c} und schreibt: „x = {dz(d + c)}“. Ist das vollständig?', r,
                       ['Ja, das ist die einzige Lösung.', f'Falsch: Richtig ist nur x = {dz(d - c)}.', f'Falsch: Es fehlt x = {dz(-d - c)}.'],
                       f'Auch {dz(d - c)} hat von {dz(d)} den Abstand {c}: |{dz(d - c)}{"" if d == 0 else " " + plus(-d)}| = {c}.', 'Gibt es links von der Mitte auch eine Zahl mit diesem Abstand?')
    r = 'Für alle x ≥ 0.'
    return auswahl('Für welche Zahlen x gilt |x| = x?', r, ['Für alle x.', 'Nur für x = 0.', 'Für alle x ≤ 0.'],
                   'Für x ≥ 0 bleibt x beim Betrag unverändert. Für negative x ist |x| = −x > x.', 'Teste eine positive, eine negative Zahl und 0.')


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-2) ----------
# Prüfungsvorbilder: IB MYP Extended (Transformationen: Parameter aus einem Punkt, Graph ↔ Term; Toleranz |x − Soll| ≤ t;
# Betragsungleichungen), Realschule Bayern Abschlussprüfung Teil A (Größenvergleich, Term mit Betrag). Eigene Zahlen.
def betrag3(art):
    if art == 'ordnen':
        a, b, c, d = R.randint(2, 9), R.randint(2, 9), R.randint(1, 6), R.randint(7, 15)
        werte = {f'|−{a}|': a, f'−|−{b}|': -b, f'|{c} − {d}|': d - c, f'−|{c}|': -c}
        if len(set(werte.values())) < 4: return None
        klein = min(werte, key=werte.get)
        return auswahl(f'Welcher Ausdruck hat den kleinsten Wert: |−{a}|, −|−{b}|, |{c} − {d}| oder −|{c}|?', klein, [k for k in werte if k != klein],
                       'Werte: ' + ', '.join(f'{k} = {dz(v)}' for k, v in werte.items()) + f'. Am kleinsten: {klein}.',
                       'Ein Minus vor den Betragsstrichen wirkt erst nach dem Betrag.')
    if art == 'verschachtelt':
        a, b = R.randint(1, 9), R.randint(-15, -2)
        r = abs(a - abs(b))
        if a == abs(b): return None
        return zahl(f'Berechne |{a} − |{dz(b)}||.', f'Innen zuerst: |{dz(b)}| = {abs(b)}. Dann {a} − {abs(b)} = {dz(a - abs(b))}. Betrag: {r}.',
                    'Von innen nach außen: erst der innere Betrag, dann rechnen, dann der äußere Betrag.', r, f'abs({a} - abs({b}))')
    if art == 'anzahl_ganz':
        d, c = R.randint(-5, 5), R.randint(2, 6)
        echt = R.random() < .5
        n = 2 * c - 1 if echt else 2 * c + 1
        return zahl(f'Wie viele ganze Zahlen x erfüllen |{inn(d)}| {"<" if echt else "≤"} {c}?' if d else f'Wie viele ganze Zahlen x erfüllen |x| {"<" if echt else "≤"} {c}?',
                    f'Gesucht sind ganze Zahlen mit Abstand {"kleiner als" if echt else "höchstens"} {c} von {dz(d)}: von {dz(d - c + (1 if echt else 0))} bis {dz(d + c - (1 if echt else 0))}, das sind {n} Zahlen.',
                    f'Zeichne einen Zahlenstrahl um {dz(d)} und zähle die ganzen Zahlen in passendem Abstand.', n, f'{n}')
    # abstand_umkehr
    a, k = R.randint(-9, 9), R.randint(2, 9)
    if a == 0: return None
    rechts = R.random() < .5
    x = a + k if rechts else a - k
    return zahl(f'Eine Zahl x liegt {"rechts" if rechts else "links"} von {dz(a)} auf dem Zahlenstrahl. Es gilt |x − {kl(a)}| = {k}. Welche Zahl ist x?',
                f'Abstand {k} von {dz(a)} nach {"rechts" if rechts else "links"}: x = {dz(a)} {"+" if rechts else "−"} {k} = {dz(x)}.',
                '|x − a| ist der Abstand von x und a. Gehe auf dem Zahlenstrahl in die richtige Richtung.', x, f'{a} {"+" if rechts else "-"} {k}')


def graph3(art):
    if art == 'a_bestimmen':
        a, d, e = R.choice([2, 3, -1, -2, Fr(1, 2)]), R.randint(-3, 3), R.randint(-4, 4)
        x = d + R.choice([-4, -2, 2, 4])
        y = a * abs(x - d) + e
        if y != int(y): return None
        return zahl(f'Der Graph von f(x) = a · |{inn(d)}| {plus(e) if e else ""} geht durch den Punkt P({dz(x)} | {dz(int(y))}). Bestimme a.'.replace('  ', ' '),
                    f'Einsetzen: {dz(int(y))} = a · |{dz(x)} {plus(-d) if d else ""}| {plus(e) if e else ""} = a · {abs(x - d)} {plus(e) if e else ""}. '.replace('  ', ' ') + f'Also a · {abs(x - d)} = {dz(int(y) - e)} und a = {dz(a)}.'.replace(' .', '.'),
                    'Setze die Koordinaten von P ein und löse nach a auf.', a, f'({int(y)} - ({e})) / abs({x} - ({d}))')
    if art == 'schnitt_waagrecht':
        a, d, e = R.choice([1, -1]), R.randint(-3, 3), R.randint(-3, 3)
        k = e + R.choice([-2, -1, 0, 1, 2])
        n = 1 if k == e else (2 if (k > e) == (a > 0) else 0)
        return auswahl(f'Wie viele Schnittpunkte hat der Graph von f(x) = {bterm(a, d, e)} mit der waagrechten Geraden y = {dz(k)}?', {0: 'keinen', 1: 'genau einen', 2: 'genau zwei'}[n],
                       ['keinen', 'genau einen', 'genau zwei', 'unendlich viele'],
                       f'Das V hat die Spitze S({dz(d)} | {dz(e)}) und ist nach {"oben" if a > 0 else "unten"} geöffnet. '
                       + ('Die Gerade geht genau durch die Spitze: ein Schnittpunkt.' if n == 1 else 'Die Gerade liegt im Inneren des V: zwei Schnittpunkte.' if n == 2 else 'Die Gerade verfehlt das V: kein Schnittpunkt.'),
                       'Skizziere das V und die waagrechte Gerade.')
    if art == 'wertebereich':
        a, d, e = R.choice([1, 2, -1, -2]), R.randint(-4, 4), R.randint(-5, 5)
        r = f'alle y {"≥" if a > 0 else "≤"} {dz(e)}'
        return auswahl(f'Welche y-Werte nimmt f(x) = {bterm(a, d, e)} an?', r,
                       [f'alle y {"≤" if a > 0 else "≥"} {dz(e)}', f'alle y {"≥" if a > 0 else "≤"} {dz(d)}', 'alle Zahlen'],
                       f'Der Betrag ist nie negativ. {"Mit a > 0 ist der tiefste Punkt" if a > 0 else "Mit a < 0 ist der höchste Punkt"} die Spitze S({dz(d)} | {dz(e)}).',
                       'Wo liegt die Spitze des V, und wohin ist es geöffnet?')
    return None


def stueck3(art):
    if art == 'beide_stuecke':
        k, d = R.choice([2, 3]), R.randint(-4, 4)
        if d == 0: return None
        return luecken(f'Schreibe f(x) = |{k}x {plus(-k * d)}| stückweise. Gib die Grenze und den Term links davon an.', 'Grenze x = □; links: f(x) = □x + □', 'drei ganze Zahlen',
                       [d, -k, k * d], f'Grenze: {k}x {plus(-k * d)} = 0 ⇒ x = {dz(d)}. Links ist der Inhalt negativ: f(x) = −({k}x {plus(-k * d)}) = {poly(-k, k * d)}.',
                       'Grenze: Inhalt = 0. Links vom Knick wird die ganze Klammer negiert.', c=[str(d), str(-k), str(k * d)])
    if art == 'rueck_betrag':
        a, d, e = R.choice([1, 2, 3]), R.randint(-3, 3), R.randint(-4, 4)
        return luecken(f'Für x < {dz(d)} gilt f(x) = {poly(-a, a * d + e)}, für x ≥ {dz(d)} gilt f(x) = {poly(a, -a * d + e)}. Schreibe f mit einem Betrag.',
                       'f(x) = □ · |x − □| + □', 'drei ganze Zahlen', [a, d, e],
                       f'Die Stücke treffen sich bei x = {dz(d)} mit f({dz(d)}) = {dz(e)}: Knickpunkt ({dz(d)} | {dz(e)}). Steigung rechts {a}: f(x) = {bterm(a, d, e)}.',
                       'Wo treffen sich die beiden Stücke? Welche Steigung hat das rechte Stück?', c=[str(a), str(d), str(e)])
    # zwei_betraege
    p = R.randint(2, 9)
    x = R.randint(1, p - 1)
    return zahl(f'f(x) = |x| + |x − {p}|. Für alle x zwischen 0 und {p} hat f denselben Wert. Welchen?',
                f'Für 0 ≤ x ≤ {p} ist |x| = x und |x − {p}| = {p} − x. Zusammen: x + {p} − x = {p}. Probe x = {x}: {x} + {p - x} = {p}.',
                'Schreibe beide Beträge für x zwischen 0 und ' + str(p) + ' ohne Striche.', p, f'abs({x}) + abs({x} - {p})')


def gleichung3(art):
    if art == 'toleranz':
        ding, soll, tol, e = R.choice([('Schrauben sollen', 40, 1, 'mm'), ('Ein Brötchen soll', 60, 3, 'g'), ('Im Kühlschrank sollen', 5, 2, '°C'),
                                       ('Flaschen sollen', 500, 5, 'ml'), ('Pakete sollen', 2000, 50, 'g'), ('Bretter sollen', 120, 2, 'cm')])
        x = soll + R.choice([-1, 1]) * (tol + R.randint(1, 3))
        return luecken(f'{ding} {soll} {e} haben. Erlaubt ist |x − {soll}| ≤ {tol}. Ein Stück hat {x} {e}. Welche Grenze wird verletzt, und um wie viel?',
                    f'Grenze □ {e}; daneben um □ {e}', 'zwei ganze Zahlen',
                    [soll + tol if x > soll else soll - tol, abs(x - soll) - tol],
                    f'Erlaubt von {soll - tol} bis {soll + tol} {e}. {x} liegt {"über" if x > soll else "unter"} der Grenze {soll + tol if x > soll else soll - tol}, um {abs(x - soll) - tol} {e}.',
                       'Bestimme zuerst die beiden Grenzen: Sollwert minus und plus Toleranz.', c=[str(soll + tol if x > soll else soll - tol), str(abs(x - soll) - tol)])
    if art == 'groesser':
        d, c = R.randint(-6, 6), R.randint(1, 7)
        return luecken(f'Für welche x gilt |{inn(d)}| > {c}?' if d else f'Für welche x gilt |x| > {c}?', 'x < □ oder x > □', 'zwei ganze Zahlen', [d - c, d + c],
                       f'Abstand größer als {c} von {dz(d)}: links von {dz(d - c)} oder rechts von {dz(d + c)}.',
                       f'Zeichne {dz(d)} und die Zahlen im Abstand {c}. Wo ist der Abstand größer?', c=[str(d - c), str(d + c)])
    if art == 'mitte':
        p, q = sorted(R.sample(range(-8, 12), 2))
        if (p + q) % 2 or 0 in (p, q): return None
        return zahl(f'Löse |x − {kl(p)}| = |x − {kl(q)}|.', f'Gesucht ist die Zahl, die von {dz(p)} und {dz(q)} gleich weit entfernt ist: die Mitte ({dz(p)} + {dz(q)}) : 2 = {dz((p + q) // 2)}.',
                    'Beide Seiten sind Abstände. Welche Zahl ist von beiden Zahlen gleich weit weg?', (p + q) // 2, f'({p} + {q}) / 2')
    # param
    d = R.randint(-6, 6)
    r = 'c = 0'
    return auswahl(f'Für welchen Wert von c hat |{inn(d)}| = c genau eine Lösung?' if d else 'Für welchen Wert von c hat |x| = c genau eine Lösung?', r,
                   ['für jedes c > 0', 'für jedes c < 0', f'c = {dz(d)}' if d else 'c = 1'],
                   f'c > 0: zwei Lösungen, c < 0: keine. Nur bei c = 0 gibt es genau eine: x = {dz(d)}.',
                   'Wie viele Zahlen haben einen bestimmten Abstand zu einer Zahl – und wann nur eine?')


def verstehen3(art):
    if art == 'immer_wahr':
        return auswahl('Welche Aussage gilt für alle Zahlen a?', '|a| ≥ a', ['|a| = a', '|a| > 0', '−|a| ≥ 0'],
                       '|a| = a für a ≥ 0 und |a| > a für a < 0, also immer |a| ≥ a. |a| > 0 scheitert an a = 0; |a| = a an a = −1; −|a| ≥ 0 an a = 1.',
                       'Prüfe jede Aussage mit einer positiven Zahl, einer negativen Zahl und 0.')
    if art == 'gegenbeispiel':
        k = R.randint(2, 9)
        cand = [k + 2, k, k + 7, k - R.randint(1, 4)]
        r = str(cand[3])
        return auswahl(f'Welche Zahl a ist ein Gegenbeispiel zur Behauptung „|a − {k}| = a − {k} für alle a“?', f'a = {r}', [f'a = {cand[0]}', f'a = {cand[1]}', f'a = {cand[2]}'],
                       f'Für a ≥ {k} stimmt die Gleichung. Für a = {r}: |{r} − {k}| = {dz(k - int(r))}, aber {r} − {k} = {dz(int(r) - k)}.',
                       'Für welche a ist der Inhalt negativ?')
    if art == 'minus_a':
        return auswahl('Für welche Zahlen a gilt |a| = −a?', 'für alle a ≤ 0', ['für keine Zahl', 'nur für a = 0', 'für alle a ≥ 0'],
                       'Für a < 0 ist −a positiv und gleich |a|, z. B. |−3| = 3 = −(−3). Für a = 0 stimmt es auch. Für a > 0 wäre −a negativ.',
                       'Setze a = −3, a = 0 und a = 3 ein.')
    return None


def g2_betrag(s):
    if s == 1:
        if R.random() < .3:  # „Was ist größer?“ war Stufe 3, ist aber ein direkter Vergleich
            return _vergleich()
        return g_betrag(1)
    if s == 2:
        for _ in range(50):
            a = g_betrag(R.choice([2, 3]))
            if a and 'größer' not in a['f']['text']: return a
        return None
    return betrag3(art3('ordnen', 'verschachtelt', 'anzahl_ganz', ['ordnen', 'verschachtelt', 'anzahl_ganz', 'abstand_umkehr']))


def _vergleich():
    x, y = R.sample(range(-12, 13), 2)
    if abs(x) == abs(y): return None
    r = f'|{dz(x)}|' if abs(x) > abs(y) else f'|{dz(y)}|'
    return auswahl(f'Was ist größer: |{dz(x)}| oder |{dz(y)}|?', r, [f'|{dz(x)}|', f'|{dz(y)}|', 'Beide sind gleich'],
                   f'|{dz(x)}| = {abs(x)}, |{dz(y)}| = {abs(y)}.', 'Vergleiche die Abstände von 0, nicht die Zahlen selbst.')


def g2_graph(s):
    if s < 3: return g_graph(s)
    art = art3('welcher', 'a_bestimmen', 'schnitt_waagrecht', ['welcher', 'a_bestimmen', 'schnitt_waagrecht', 'steigung', 'wertebereich'])
    if art in ('welcher', 'steigung'):
        for _ in range(80):
            a = g_graph(3)
            if a and (('Welcher Funktionsterm' in a['f']['text']) == (art == 'welcher')) and ('Steigung' in a['f']['text'] or art == 'welcher'): return a
        return None
    return graph3(art)


def g2_stueckweise(s):
    if s == 1: return g_stueckweise(1)
    if s == 2:  # Stufe 2: mit Faktor/Verschiebung, Grenze, Wert aus stückweiser Darstellung (vorher Stufe 3)
        for _ in range(50):
            a = g_stueckweise(R.choice([2, 3]))
            if a and 'Tim' not in a['f']['text']: return a
        return None
    art = art3('beide_stuecke', 'rueck_betrag', 'zwei_betraege', ['beide_stuecke', 'rueck_betrag', 'zwei_betraege', 'tim'])
    if art == 'tim':
        for _ in range(80):
            a = g_stueckweise(3)
            if a and 'Tim' in a['f']['text']: return a
        return None
    return stueck3(art)


def g2_gleichung(s):
    if s < 3: return g_gleichung(s)
    art = art3('toleranz', 'ungleich', 'mitte', ['toleranz', 'ungleich', 'mitte', 'groesser', 'param'])
    if art == 'ungleich':
        for _ in range(80):
            a = g_gleichung(3)
            if a and '≤' in a['f']['text'] and 'Maschine' not in a['f']['text']: return a
        return None
    return gleichung3(art)


def g2_verstehen(s):
    if s == 1: return g_verstehen(1)
    if s == 2:  # Stufe 2: Summenregel testen, unvollständige Lösung finden (vorher auch Stufe 3)
        return g_verstehen(2)
    art = art3('immer_wahr', 'gegenbeispiel', 'minus_a', ['gegenbeispiel', 'produkt', 'immer', 'produkt', 'gegenbeispiel'])
    if art in ('produkt', 'immer'):
        for _ in range(80):
            a = g_verstehen(3)
            if a and (('a · b' in a['f']['text']) == (art == 'produkt')) and ('|x| = x' in a['f']['text'] or art == 'produkt'): return a
        return None
    return verstehen3(art)


GEN = {'betrag': g2_betrag, 'graph': g2_graph, 'stueckweise': g2_stueckweise, 'gleichung': g2_gleichung, 'verstehen': g2_verstehen}

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import ko, pkte  # noqa: E402


def _zs(a, b, n, **kw):
    return {'typ': 'zahlenstrahl', 'start': a, 'ende': b, 'abschnitte': n, 'beschriftet': 'anfang_ende', **kw}


def _pk(*w):
    return [{'wert': x, 'name': n} for x, n in w]


def _b(a, b, c, name=None):
    g = {'art': 'betrag', 'a': a, 'b': b, 'c': c}
    if name:
        g['name'] = name
    return g


def _l(m, t, ber, name=None):
    g = {'art': 'linear', 'm': m, 't': t, 'bereich': ber}
    if name:
        g['name'] = name
    return g


UMBAU = {
    'betrag': {
        'einstieg': 'Ein Bus hält bei Kilometer 3, du stehst bei Kilometer −2. Wie weit ist es bis zum Bus? '
                    'Ein Abstand ist nie negativ. Man misst ihn mit dem ⟦Betrag⟧.',
        'woerter': [['Betrag', '|a|: Abstand der Zahl a von 0; nie negativ'],
                    ['Abstand', 'wie weit zwei Zahlen auseinanderliegen; geschrieben |a − b|']],
        'bild': _zs(-5, 5, 10, punkte=_pk((-2, 'du'), (3, 'Bus'))),
        'schritte': [
            {'text': 'Abstand von −2 bis 3: |−2 − 3|.'},
            {'text': 'Innen zuerst: −2 − 3 = −5. Betrag: |−5| = 5.', 'bild': {'boegen': [{'von': -2, 'bis': 3, 'name': '5'}]}},
            {'text': 'Für x = −2: |x − 3| + 1 = 5 + 1 = ⟦6⟧.'},
        ],
        'fehler': '|−2 − 3| = |−2| − |3| = −1 ist falsch. Erst ⟦innen ausrechnen⟧, dann den Betrag nehmen: 5.',
        'regel': 'Betrag = ⟦Abstand von 0⟧, nie negativ. |a − b| ist der Abstand von a und b.',
    },
    'graph': {
        'einstieg': 'Läufst du am Bus vorbei, wird der Abstand erst kleiner, dann wieder größer. '
                    'Im Graphen entsteht ein V. Seine Spitze heißt ⟦Knickpunkt⟧.',
        'woerter': [['Knickpunkt', 'die Spitze des V; dort ist der Inhalt des Betrags 0']],
        'bild': ko([-4, 6], [-4, 6], schritt=0, graphen=[_b(1, 0, 0, '|x|')]),
        'schritte': [
            {'text': 'f(x) = |x| ist ein V mit Spitze in (0 | 0).'},
            {'text': 'In 2 · |x − 1| − 3: 1 nach rechts, 3 nach unten.', 'bild': {'graphen': [dict(_b(1, 0, 0, '|x|'), name_x=-3), _b(2, 1, -3, 'f')]}},
            {'text': 'Knickpunkt ⟦S(1 | −3)⟧. Der Faktor 2 macht das V steiler.', 'bild': {'punkte': pkte({'S': (1, -3)})}},
        ],
        'fehler': 'Bei |x − 1| liegt der Knick nicht bei x = −1. Er liegt, wo ⟦innen 0⟧ herauskommt: x = 1.',
        'fehler_bild': {'graphen': [_b(1, 1, 0, '|x − 1|')], 'punkte': pkte({'falsch': (-1, 0), 'Knick': (1, 0)})},
        'regel': 'Der Knickpunkt ist ⟦S(d | e)⟧. Das gilt für a · |x − d| + e. Bei a < 0 öffnet das V nach unten.',
    },
    'stueckweise': {
        'einstieg': 'Der Abstand zum Bus bei 2 geht auch ohne Betragsstriche. Rechts vom Bus rechnet man x − 2, '
                    'links davon 2 − x. Das heißt ⟦stückweise⟧ schreiben.',
        'woerter': [['stückweise', 'für verschiedene Bereiche von x verschiedene Terme']],
        'bild': ko([-2, 6], [-1, 5], schritt=0, graphen=[_b(1, 2, 0, '|x − 2|')]),
        'schritte': [
            {'text': 'Grenze: x − 2 = 0, also x = 2.', 'bild': {'senkrecht': [2]}},
            {'text': 'Für x ≥ 2: f(x) = x − 2.', 'bild': {'graphen': [_l(1, -2, [2, 6], 'x − 2')]}},
            {'text': 'Für x < 2: f(x) = −(x − 2) = ⟦−x + 2⟧.', 'bild': {'graphen': [_l(1, -2, [2, 6], 'x − 2'), _l(-1, 2, [-2, 2], '−x + 2')]}},
        ],
        'fehler': 'Für x < 2 ist x + 2 falsch. Die ⟦ganze Klammer negieren⟧: −(x − 2) = −x + 2. Probe mit x = 1.',
        'fehler_bild': {'graphen': [_l(1, -2, [2, 6], 'x − 2'), _l(1, 2, [-2, 2], 'falsch')]},
        'regel': 'Die Grenze liegt, wo innen 0 ist. Rechts bleibt der Inhalt, links nimmt man ⟦sein Gegenteil⟧.',
    },
    'gleichung': {
        'einstieg': 'Welche Haltestellen liegen genau 3 km von Kilometer 4 entfernt? Eine links, eine rechts. '
                    'Die ⟦Betragsgleichung⟧ |x − 4| = 3 hat deshalb zwei Lösungen.',
        'woerter': [['Betragsgleichung', 'eine Gleichung, in der x im Betrag steht']],
        'bild': _zs(0, 8, 8, beschriftet='alle', punkte=_pk((4, '4'))),
        'schritte': [
            {'text': '|x − 4| = 3 heißt: Abstand 3 von der Zahl 4.'},
            {'text': 'Nach links: x = 4 − 3 = ⟦1⟧.', 'bild': {'punkte': _pk((4, '4'), (1, 'x₁')), 'boegen': [{'von': 4, 'bis': 1, 'name': '3'}]}},
            {'text': 'Nach rechts: x = 4 + 3 = ⟦7⟧.',
             'bild': {'punkte': _pk((4, '4'), (1, 'x₁'), (7, 'x₂')), 'boegen': [{'von': 4, 'bis': 1, 'name': '3'}, {'von': 4, 'bis': 7, 'name': '3'}]}},
            {'text': 'Ist rechts 0, gibt es nur x = 4. Ist rechts etwas Negatives, keine.',
             'bild': {'punkte': _pk((4, '4')), 'boegen': None}},
        ],
        'fehler': 'Nur x = 7 ist unvollständig. Es gibt ⟦zwei Zahlen⟧ mit Abstand 3 von 4, auch x = 1.',
        'fehler_bild': {'punkte': _pk((4, '4'), (1, 'fehlt'), (7, 'x = 7')), 'boegen': [{'von': 4, 'bis': 7, 'name': '3'}]},
        'regel': '|x − d| = c heißt Abstand c von d. Für c > 0 gibt es ⟦zwei Lösungen⟧: d − c und d + c.',
    },
    'verstehen': {
        'einstieg': 'Du läufst 3 km vor und 5 km zurück. Vom Start bist du nur 2 km entfernt, gelaufen bist du 8 km. '
                    'Beträge darf man also nicht stur ⟦addieren⟧.',
        'woerter': [['Gegenbeispiel', 'ein Beispiel, bei dem eine Behauptung nicht stimmt']],
        'bild': _zs(-5, 5, 10, punkte=_pk((0, 'Start'))),
        'schritte': [
            {'text': 'Behauptung: |a + b| = |a| + |b|. Teste a = 3, b = −5.',
             'bild': {'boegen': [{'von': 0, 'bis': 3, 'name': '3'}, {'von': 3, 'bis': -2, 'name': '−5'}]}},
            {'text': '|3 + (−5)| = |−2| = 2.', 'bild': {'punkte': _pk((0, 'Start'), (-2, 'Ziel'))}},
            {'text': 'Aber |3| + |−5| = 8. ⟦Die Aussage ist falsch⟧.'},
            {'text': 'a = 3, b = −5 ist also ein Gegenbeispiel.'},
        ],
        'fehler': '„|−x| = x für alle x“ ist falsch. Für x = −4 ist |−x| = 4, nicht −4. Richtig ist ⟦|−x| = |x|⟧.',
        'regel': 'Aussagen auch mit ⟦negativen Zahlen⟧ testen. Im Allgemeinen gilt |a + b| ≠ |a| + |b|.',
    },
}
UMBAU_OFFEN = []
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


d = bauen('funktionen.betrag',
      'Beträge berechnen, die Betragsfunktion zeichnen, stückweise beschreiben und Betragsgleichungen lösen.',
      ['|a| (absolute value) ist der Abstand von 0 – nie negativ. |a − b| ist der Abstand von a und b.',
       'f(x) = a · |x − d| + e: V-förmiger Graph mit Knickpunkt S(d | e); a < 0: nach unten geöffnet.',
       'Stückweise (piecewise): Inhalt ≥ 0 bleibt, Inhalt < 0 wird negiert.',
       '|x − d| = c: zwei Lösungen d ± c (c > 0), keine für c < 0.'],
      [('Betrag und Graph', ['betrag', 'graph']), ('Ohne Betrag schreiben', ['stueckweise']), ('Gleichungen und Aussagen', ['gleichung', 'verstehen'])],
      ETAPPEN, GEN,
      offen=['Lehrplan-Feld leer: Umfang nach Themenliste (Graph, stückweise Beschreibung) plus einfache Betragsgleichungen und eine Betragsungleichung als Anwendung (Toleranzbereich). Annahme MYP 4.'],
      plan=PLAN2)
umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)


# ---- STUFEN (Zwanzigste Runde, Zusatz Realschule/IB, Zweig stufen-rsib-2) ----
from _stufen_rsib2 import Stufen, stufen  # noqa: E402

ST = Stufen('funktionen.betrag', 20_2_4)
Z, A, L = ST.Z, ST.A, ST.L
X2 = 'x₁ = □; x₂ = □'
ST.vorbild += ['IB MYP eAssessment Mathematics (Extended): Betragsfunktion, Knickpunkt, Gleichungen und Ungleichungen mit Beträgen',
               'Toleranz-Aufgaben („erlaubte Abweichung“) aus Realschul-Abschlussprüfungen und Berufsschul-Eingangstests, nachgebaut']

# betrag
ST.stufenleiter('betrag', 'Betrag einer Zahl, Abstand zweier Zahlen als |a − b|.',
                'Funktionswerte von |x − d| + e, mehrere Beträge in einem Term, Abstände in Sachsituationen, Zahl aus Betrag und Vorzeichen.',
                'Ausdrücke vergleichen, ganze Zahlen im Abstand zählen, Zahl aus Abstand und Lage, Fehler |a| + |b| = |a + b|, Parameter, Wege mit Vorzeichen.')
ST.typ('betrag', '/^Was ist größer/', 'erkennen')
ST.typ('betrag', '/^/', 'direkt', s=1)
ST.typ('betrag', '/^/', 'mehrschritt', s=2)
ST.typ('betrag', '/^Welcher Ausdruck/', 'begruenden')
ST.typ('betrag', '/^Berechne \\|# − \\|/'.replace('#', '\\d+'), 'mehrschritt')
ST.typ('betrag', '/Wie viele ganze Zahlen/', 'verknuepfen')
ST.typ('betrag', '/^/', 'rueckwaerts', s=3)
ST.neu('betrag', 'einkleidung', Z('Ein Thermometer zeigt morgens −7 °C und mittags 5 °C. Um wie viel Grad ist es wärmer geworden?', 12, 'abs(5 - (-7))',
       'Abstand der Temperaturen: |5 − (−7)| = |12| = 12 °C.', 'Abstand zweier Zahlen: Betrag der Differenz.', einheit='°C'))
ST.neu('betrag', 'umkehr', Z('Für eine Zahl a gilt |a| = 6 und a < 0. Welche Zahl ist a?', -6, '-6',
       '|a| = 6 haben die Zahlen 6 und −6. Weil a negativ ist: a = −6.', 'Welche zwei Zahlen haben den Betrag 6?'))
ST.neu('betrag', 'fehler', A('Jemand rechnet: |−3| + |5| = |−3 + 5| = 2. Was stimmt?', 'Falsch: |−3| + |5| = 3 + 5 = 8.', ['Richtig.', 'Falsch: Es ergibt −8.', 'Falsch: Es ergibt −2.'],
       'Man darf die Beträge nicht zusammenfassen: Erst jeden Betrag berechnen (3 und 5), dann addieren.', 'Rechne jeden Betrag einzeln aus.'))
ST.neu('betrag', 'parameter', Z('Für welche Zahl a gilt |a − 3| = |a + 3|?', 0, '0',
       '|a − 3| ist der Abstand zu 3, |a + 3| der Abstand zu −3. Gleich weit von 3 und −3 liegt nur die Mitte: a = 0.', 'Deute beide Beträge als Abstände.'))
ST.neu('betrag', 'transfer', Z('Ein Aufzug fährt vom 2. Untergeschoss (−2) in den 5. Stock und dann ins 1. Untergeschoss (−1). Wie viele Stockwerke legt er insgesamt zurück?', 13, 'abs(5 - (-2)) + abs(-1 - 5)',
       'Erste Fahrt |5 − (−2)| = 7, zweite |−1 − 5| = 6. Zusammen 13 Stockwerke.', 'Rechne jede Fahrt als Abstand.'))
ST.knobel('betrag', Z('Wie viele ganze Zahlen x erfüllen |x| + |x − 3| = 3?', 4, '4',
          '|x| + |x − 3| ist die Summe der Abstände zu 0 und zu 3. Liegt x zwischen 0 und 3, ist sie genau 3; außerhalb ist sie größer. Ganze Zahlen: 0, 1, 2, 3 – vier.',
          'Deute die Summe als zwei Abstände auf dem Zahlenstrahl.'))
ST.knobel('betrag', Z('Für welche Zahl x ist |x − 1| + |x − 5| + |x − 6| am kleinsten?', 5, '5',
          'Summe der Abstände zu 1, 5 und 6. Bei x = 5: 4 + 0 + 1 = 5. Rückt x nach links, wachsen zwei Abstände und nur einer schrumpft; nach rechts ebenso. Am kleinsten ist die Summe bei der mittleren Zahl 5.',
          'Probiere x = 4, 5 und 6.'))

# graph
ST.stufenleiter('graph', 'Knickpunkt von |x − d| + e ablesen.',
                'Öffnung und Faktor, Knickpunkt am Bild ablesen, Gleichung aus Knickpunkt aufstellen.',
                'Term zum Graphen, a aus einem Punkt, Schnittpunkte mit Waagrechten, Steigung der Äste, Wertemenge.')
ST.typ('graph', '/^/', 'direkt', s=1)
ST.typ('graph', '/Knickpunkt des Graphen von f\\(x\\) = \\d/', 'mehrschritt')
ST.typ('graph', '/^/', 'darstellung', s=2)
ST.typ('graph', '/Welcher Funktionsterm/', 'rueckwaerts')
ST.typ('graph', '/Bestimme a/', 'parameter')
ST.typ('graph', '/Schnittpunkte|Steigung/', 'verknuepfen')
ST.typ('graph', '/^/', 'begruenden', s=3)
ST.neu('graph', 'erkennen', A('Welche Form hat der Graph von f(x) = |x|?', 'ein V mit der Spitze im Ursprung', ['eine Gerade durch den Ursprung', 'eine Parabel', 'ein umgedrehtes V mit Spitze bei (0 | 1)'],
       'Für x ≥ 0 ist f(x) = x, für x < 0 ist f(x) = −x: zwei Halbgeraden, die sich in (0 | 0) treffen.', 'Rechne f(−2), f(0) und f(2) aus.'))
ST.neu('graph', 'umkehr', L('Ein V-förmiger Graph mit Faktor 1 hat den Knickpunkt (3 | −2). Gib seine Gleichung an.', 'f(x) = |x − □| − □', [3, 2], ['3', '2'],
       'Knick bei x = 3: |x − 3|. Um 2 nach unten: − 2. f(x) = |x − 3| − 2.', 'Wie verschiebt d, wie e?'))
ST.knobel('graph', Z('Der Graph von f(x) = |x − 2| und die Gerade y = 4 schließen ein Dreieck ein. Wie groß ist sein Flächeninhalt?', 16, '8*4/2',
          'Schnittpunkte: |x − 2| = 4 ⇒ x = −2 und x = 6. Die Grundseite auf y = 4 ist 8 lang, die Spitze (2 | 0) liegt 4 tiefer: A = 8 · 4 : 2 = 16.',
          'Bestimme die Ecken des Dreiecks.', einheit='FE'))
ST.knobel('graph', A('Wie viele gemeinsame Punkte haben die Graphen von f(x) = |x| und g(x) = −|x − 4| + 4?', 'unendlich viele', ['keinen', 'genau einen', 'genau zwei'],
          'Für 0 ≤ x ≤ 4 ist f(x) = x und g(x) = −(4 − x) + 4 = x. Die Graphen haben die ganze Strecke von (0 | 0) bis (4 | 4) gemeinsam.',
          'Schreibe beide Funktionen für 0 ≤ x ≤ 4 ohne Betrag.'))

# stueckweise
ST.stufenleiter('stueckweise', 'Für einen Bereich den Term ohne Betrag angeben.',
                'Grenze bestimmen, Funktionswert der stückweisen Funktion, Betrag mit Summand.',
                'Grenze und Term bei |2x − 4|, stückweise Funktion mit einem Betrag schreiben, |x| + |x − 9| deuten, Fehler beim Minus, Parameter a.')
ST.typ('stueckweise', '/^/', 'direkt', s=1)
ST.typ('stueckweise', '/Bei welchem x liegt die Grenze/', 'umkehr')
ST.typ('stueckweise', '/^Für x </', 'darstellung', s=2)
ST.typ('stueckweise', '/^/', 'mehrschritt', s=2)
ST.typ('stueckweise', '/Gib die Grenze und den Term/', 'verknuepfen')
ST.typ('stueckweise', '/Schreibe f mit einem Betrag/', 'rueckwaerts')
ST.typ('stueckweise', '/\\|x\\| \\+ \\|x − /', 'transfer')
ST.typ('stueckweise', '/^/', 'fehler', s=3)
ST.neu('stueckweise', 'erkennen', A('f(x) = |x − 5|. Welcher Term gilt für x ≥ 5?', 'x − 5', ['−x + 5', '−x − 5', 'x + 5'],
       'Für x ≥ 5 ist x − 5 nicht negativ; der Betrag ändert nichts.', 'Ist x − 5 für x ≥ 5 positiv oder negativ?'))
ST.neu('stueckweise', 'parameter', Z('f(x) = |x − a| + 1 hat für x ≥ a den Term x − 3. Wie groß ist a?', 4, '1 + 3',
       'Für x ≥ a gilt f(x) = x − a + 1. Gleich x − 3 ⇒ −a + 1 = −3 ⇒ a = 4.', 'Schreibe f für x ≥ a ohne Betrag.'))
ST.knobel('stueckweise', L('f(x) = |x − 1| + |x − 3| hat für x > 3 den Term 2x − 4. Welchen Term hat f für x < 1?', '□x + □', [-2, 4], ['-2', '4'],
          'Für x < 1 sind beide Klammern negativ: −(x − 1) − (x − 3) = −x + 1 − x + 3 = −2x + 4. (Zwischen 1 und 3 ist f konstant 2.)',
          'Welche Vorzeichen haben x − 1 und x − 3 für x < 1?', hinweis='Tippe den Term ein, z. B. −2x + 4.'))
ST.knobel('stueckweise', Z('Wie viele ganze Zahlen x mit −10 ≤ x ≤ 10 erfüllen |x − 2| + |x + 2| = 4?', 5, '5',
          'Zwischen −2 und 2 ist die Summe der Abstände zu 2 und −2 immer 4; außerhalb größer. Ganze Zahlen −2, −1, 0, 1, 2: fünf.',
          'Deute die beiden Beträge als Abstände.'))

# gleichung
ST.stufenleiter('gleichung', '|x − a| = r durch „Abstand r von a“ lösen.',
                'Gleichung erst umformen, Sonderfälle (rechts 0 oder negativ), Sachsituation, Gleichung zu gegebenen Lösungen.',
                'Toleranzen deuten, Ungleichungen |x − a| ≤ r, gleich weit von zwei Zahlen, Parameter c.')
ST.typ('gleichung', '/Wie viele Lösungen/', 'erkennen')
ST.typ('gleichung', '/^/', 'direkt', s=1)
ST.typ('gleichung', '/^/', 'mehrschritt', s=2)
ST.typ('gleichung', '/Welche Grenze wird verletzt/', 'transfer')
ST.typ('gleichung', '/Für welche x gilt/', 'verknuepfen')
ST.typ('gleichung', '/^Löse \\|x − \\(/', 'begruenden')
ST.typ('gleichung', '/^/', 'parameter', s=3)
ST.neu('gleichung', 'erkennen', Z('Wie viele Lösungen hat |x − 5| = 0?', 1, '1', 'Abstand 0 von 5 hat nur x = 5: eine Lösung.', 'Welcher Punkt hat von 5 den Abstand 0?'))
ST.neu('gleichung', 'einkleidung', L('Ein Haus steht an einer geraden Straße 3 km von einem Bahnhof bei Kilometer 12 entfernt. Bei welchen Kilometern kann es stehen? (kleinere zuerst)', X2, [9, 15], ['12 - 3', '12 + 3'],
       '|x − 12| = 3 ⇒ x = 9 oder x = 15.', 'Abstand 3 nach links und nach rechts.'))
ST.neu('gleichung', 'umkehr', L('Die Gleichung |x − m| = r hat die Lösungen 2 und 10. Wie groß sind m und r?', 'm = □; r = □', [6, 4], ['(2 + 10)/2', '(10 - 2)/2'],
       'm liegt genau in der Mitte: (2 + 10) : 2 = 6. Der Abstand zu jeder Lösung ist r = 4.', 'Wo liegt m zwischen den Lösungen?'))
ST.knobel('gleichung', Z('Löse |x − 1| = 2x − 4.', 3, '3',
          'Fall x ≥ 1: x − 1 = 2x − 4 ⇒ x = 3 (passt). Fall x < 1: −x + 1 = 2x − 4 ⇒ x = 5/3, das ist nicht kleiner als 1 – fällt weg. Probe: |3 − 1| = 2 = 2 · 3 − 4.',
          'Unterscheide zwei Fälle und prüfe jede Lösung.'))
ST.knobel('gleichung', Z('Wie viele Lösungen hat die Gleichung ||x| − 3| = 1?', 4, '4',
          'Innen: |x| − 3 = 1 oder |x| − 3 = −1, also |x| = 4 oder |x| = 2. Jede hat zwei Lösungen: x = ±4, ±2. Vier Lösungen.',
          'Löse zuerst nach |x| auf.'))

# verstehen
ST.stufenleiter('verstehen', 'Erkennen, dass ein Betrag nie negativ ist; eine Aussage mit einer Zahl testen.',
                'Unvollständige Lösungen erkennen, Formeln an Beispielen prüfen, Abstände in Wegen.',
                'Aussagen für alle a, Gegenbeispiele, Bereiche wie |a| = −a, |a · b| = |a| · |b|, Fehler „ein Beispiel beweist“.')
ST.typ('verstehen', '/^Kann/', 'erkennen')
ST.typ('verstehen', '/^/', 'direkt', s=1)
ST.typ('verstehen', '/^Ali/', 'umkehr')
ST.typ('verstehen', '/^/', 'mehrschritt', s=2)
ST.typ('verstehen', '/Gegenbeispiel|für alle Zahlen/', 'begruenden')
ST.typ('verstehen', '/^Für welche/', 'parameter')
ST.typ('verstehen', '/^/', 'verknuepfen', s=3)
ST.neu('verstehen', 'einkleidung', A('Zwei Kinder starten am selben Punkt einer geraden Straße: eines geht 3 km nach Westen (−3), das andere 5 km nach Osten (5). Wie weit sind sie dann voneinander entfernt?',
       '8 km = |5 − (−3)|', ['2 km = |5 + (−3)|', '−8 km', '15 km'],
       'Der Abstand ist der Betrag der Differenz der Positionen: |5 − (−3)| = 8 km.', 'Zeichne die Straße als Zahlenstrahl.'))
ST.neu('verstehen', 'fehler', A('Jemand prüft |a − b| = |a| − |b| mit a = 5, b = 2: 3 = 3. Er schreibt: „Also stimmt es immer.“ Was ist falsch?',
       'Ein Beispiel beweist nichts: a = 2, b = 5 gibt 3 = −3, falsch.', ['Nichts, die Rechnung stimmt.', 'Er hätte a = b nehmen müssen.', '|a − b| ist nie gleich |a| − |b|.'],
       'Um „immer“ zu zeigen, reicht kein Beispiel; ein einziges Gegenbeispiel widerlegt die Aussage. Mit a = 2, b = 5: |−3| = 3, aber 2 − 5 = −3.',
       'Vertausche die Zahlen.'))
ST.knobel('verstehen', Z('Für wie viele ganze Zahlen a mit −10 ≤ a ≤ 10 gilt |a + 3| = |a| + 3?', 11, '11',
          'Für a ≥ 0 sind a + 3 und a positiv: beide Seiten sind a + 3. Für a < 0 ist |a| + 3 > |a + 3| (z. B. a = −1: 2 ≠ 4). Also a = 0, 1, …, 10: elf Zahlen.',
          'Teste ein negatives und ein positives a.'))
ST.knobel('verstehen', A('Wann gilt |a + b| = |a| + |b| genau?', 'wenn a und b nicht verschiedene Vorzeichen haben (eine darf 0 sein)',
          ['immer', 'nur wenn a = b', 'nur wenn beide negativ sind'],
          'Haben a und b gleiche Vorzeichen, zeigen beide in dieselbe Richtung: Die Längen addieren sich. Bei verschiedenen Vorzeichen heben sie sich teilweise auf, dann ist |a + b| kleiner.',
          'Denk an Pfeile auf dem Zahlenstrahl.'))

if __name__ == '__main__':
    stufen('funktionen.betrag', ST)
