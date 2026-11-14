#!/usr/bin/env python3
"""Thema funktionen.betrag – Betragsfunktion (IB MYP 4, etwa Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403

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
    g = [{'art': 'linear', 'm': -a, 't': a * d + e, 'bereich': [lo, d]}, {'art': 'linear', 'm': a, 't': -a * d + e, 'bereich': [d, hi]}]
    if name: g[1]['name'] = name
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
                       (f'Für {bed} ist x {plus(-d)} {"≥ 0, der Betrag fällt weg" if seite == "rechts" else "< 0, also |x " + plus(-d) + "| = −(x " + plus(-d) + ")"}. '
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
    art = R.choice({1: ['zwei', 'zwei'], 2: ['zwei', 'keine', 'faktor'], 3: ['ungleich', 'sach', 'faktor', 'keine']}[s])
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
                       f'Auch {dz(d - c)} hat von {dz(d)} den Abstand {c}: |{dz(d - c)} {plus(-d)}| = {c}.', 'Gibt es links von der Mitte auch eine Zahl mit diesem Abstand?')
    r = 'Für alle x ≥ 0.'
    return auswahl('Für welche Zahlen x gilt |x| = x?', r, ['Für alle x.', 'Nur für x = 0.', 'Für alle x ≤ 0.'],
                   'Für x ≥ 0 bleibt x beim Betrag unverändert. Für negative x ist |x| = −x > x.', 'Teste eine positive, eine negative Zahl und 0.')


GEN = {'betrag': g_betrag, 'graph': g_graph, 'stueckweise': g_stueckweise, 'gleichung': g_gleichung, 'verstehen': g_verstehen}

bauen('funktionen.betrag',
      'Beträge berechnen, die Betragsfunktion zeichnen, stückweise beschreiben und Betragsgleichungen lösen.',
      ['|a| (absolute value) ist der Abstand von 0 – nie negativ. |a − b| ist der Abstand von a und b.',
       'f(x) = a · |x − d| + e: V-förmiger Graph mit Knickpunkt S(d | e); a < 0: nach unten geöffnet.',
       'Stückweise (piecewise): Inhalt ≥ 0 bleibt, Inhalt < 0 wird negiert.',
       '|x − d| = c: zwei Lösungen d ± c (c > 0), keine für c < 0.'],
      [('Betrag und Graph', ['betrag', 'graph']), ('Ohne Betrag schreiben', ['stueckweise']), ('Gleichungen und Aussagen', ['gleichung', 'verstehen'])],
      ETAPPEN, GEN,
      offen=['Der Betragsgraph wird aus zwei Geradenstücken gezeichnet (Graphart „linear“ mit Bereich). Eine eigene Graphart „betrag“ wäre bequemer, ist aber nicht nötig.',
             'Lehrplan-Feld leer: Umfang nach Themenliste (Graph, stückweise Beschreibung) plus einfache Betragsgleichungen und eine Betragsungleichung als Anwendung (Toleranzbereich). Annahme MYP 4.'])
