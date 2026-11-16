#!/usr/bin/env python3
"""Thema funktionen.gebrochen – Gebrochen-rationale Funktionen (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, L, Z, baue, cz, ist_endlich, kl, lin, mit_bild, zt  # noqa: E402

META = {'thema_schluessel': 'funktionen.gebrochen', 'thema_id': 34, 'block_id': 71, 'klasse': {'gym_by': 8}}

ETAPPEN = [
    {'lernziel': 'indirekt', 'titel': 'Indirekte Proportionalität',
     'regel': 'Bei einer ⟦indirekten Proportionalität⟧ gehört zum Doppelten von x die Hälfte von y. Das ⟦Produkt x · y⟧ ist immer gleich: y = k/x. Der Graph ist eine ⟦Hyperbel⟧.',
     'schritte': ['4 Pumpen leeren ein Becken in 6 Stunden. Wie lange brauchen 3 Pumpen?', 'Die ganze Arbeit sind 4 · 6 = 24 Pumpen-Stunden. Das bleibt gleich, egal wie viele Pumpen arbeiten.',
                  '3 Pumpen brauchen 24 : 3 = ⟦8 Stunden⟧.'],
     'probe': 'Weniger Pumpen, also mehr Zeit: 8 h > 6 h ✓. Und 3 · 8 = 24 ✓',
     'fehler': '6 : 4 · 3 = 4,5 h ist falsch – damit wäre das Becken mit weniger Pumpen schneller leer! Das ist die Rechnung für direkte Proportionalität. Hier bleibt das ⟦Produkt⟧ gleich: 3 · 8 = 4 · 6.',
     'bild': {'typ': 'koordinaten', 'x': [0, 12], 'y': [0, 12], 'graphen': [{'art': 'hyperbel', 'a': 24, 'b': 0, 'c': 0, 'bereich': [1, 12]}],
              'punkte': [{'x': 3, 'y': 8, 'name': '(3 | 8)'}, {'x': 4, 'y': 6, 'name': '(4 | 6)'}], 'name_x': 'Pumpen', 'name_y': 'h'},
     '_verbot': ['4 Pumpen']},
    {'lernziel': 'definitionsmenge', 'titel': 'Definitionsmenge von a/(x + b) + c',
     'regel': 'f(x) = a/(x + b) + c ist für ⟦x = −b⟧ nicht definiert, weil dann der Nenner 0 ist. Also ⟦D = ℚ \\ {−b}⟧.',
     'schritte': ['f(x) = 3/(x − 2) + 1', 'Nenner x − 2 = 0 für x = 2', '⟦D = ℚ \\ {2}⟧'],
     'fehler': 'Bei f(x) = 3/(x − 2) + 1 fehlt nicht −2 in D: Der Nenner x − 2 wird für ⟦x = +2⟧ null. Das Vorzeichen dreht sich um.',
     '_verbot': ['3/(x − 2) + 1']},
    {'lernziel': 'asymptoten', 'titel': 'Asymptoten bestimmen',
     'regel': 'Eine ⟦Asymptote⟧ ist eine Gerade, der sich der Graph immer mehr nähert. Bei f(x) = a/(x + b) + c: ⟦senkrechte⟧ Asymptote x = −b, ⟦waagrechte⟧ Asymptote y = c.',
     'schritte': ['f(x) = 2/(x + 4) − 3', 'Senkrecht: x + 4 = 0 → ⟦x = −4⟧', 'Waagrecht: ⟦y = −3⟧ (für große x wird 2/(x + 4) fast 0)'],
     'fehler': 'Die waagrechte Asymptote von 2/(x + 4) − 3 ist nicht y = 2. Der Zähler a bestimmt sie nicht, sondern die ⟦Verschiebung c = −3⟧.',
     'bild': {'typ': 'koordinaten', 'x': [-10, 4], 'y': [-8, 3], 'graphen': [{'art': 'hyperbel', 'a': 2, 'b': 4, 'c': -3, 'name': 'f'}], 'senkrecht': [-4], 'waagrecht': [-3]},
     '_verbot': ['2/(x + 4) − 3']},
    {'lernziel': 'achsenpunkte', 'titel': 'Schnittpunkte mit den Achsen',
     'regel': '⟦y-Achse⟧: x = 0 einsetzen (falls 0 in D). ⟦x-Achse⟧ (Nullstelle): f(x) = 0 lösen. Ist c = 0, gibt es ⟦keine⟧ Nullstelle, weil a/(x + b) nie 0 ist.',
     'schritte': ['f(x) = 6/(x + 1) − 2', 'y-Achse: f(0) = 6 − 2 = 4 → (0 | 4)', 'Nullstelle: 6/(x + 1) = 2 → x + 1 = 3 → ⟦x = 2⟧'],
     'fehler': 'Für die Nullstelle x = 0 einsetzen: f(0) = 4 ist der Schnittpunkt mit der ⟦y-Achse⟧. Die Nullstelle ist dort, wo ⟦y = 0⟧ ist. Merke: Achse x heißt y = 0, Achse y heißt x = 0.',
     'bild': {'typ': 'koordinaten', 'x': [-6, 6], 'y': [-8, 8], 'graphen': [{'art': 'hyperbel', 'a': 6, 'b': 1, 'c': -2, 'name': 'f'}], 'senkrecht': [-1], 'waagrecht': [-2],
              'punkte': [{'x': 0, 'y': 4, 'name': '(0 | 4)'}, {'x': 2, 'y': 0, 'name': '(2 | 0)'}]},
     '_verbot': ['6/(x + 1) − 2']},
    {'lernziel': 'parameter', 'titel': 'Verschieben: Einfluss von b und c',
     'regel': 'Der Graph von a/(x + b) + c entsteht aus a/x durch Verschieben. Die Lücke liegt dort, wo der Nenner 0 ist: Bei 1/(x − 3) ist das ⟦x = 3⟧, also ist der Graph um 3 nach ⟦rechts⟧ gerutscht. Das +c verschiebt um c nach ⟦oben⟧ (negatives c nach unten).',
     'schritte': ['f(x) = 1/(x − 3) + 2 aus g(x) = 1/x', 'x − 3: um 3 nach rechts', '+ 2: um 2 nach oben. ⟦Asymptoten x = 3, y = 2⟧'],
     'fehler': 'Bei 1/(x − 3) geht es nicht nach links: Das Minus in der Klammer bedeutet eine Verschiebung nach ⟦rechts⟧ (die Lücke liegt bei x = 3).',
     'bild': {'typ': 'koordinaten', 'x': [-4, 8], 'y': [-4, 6], 'graphen': [{'art': 'hyperbel', 'a': 1, 'b': 0, 'c': 0, 'name': 'g'}, {'art': 'hyperbel', 'a': 1, 'b': -3, 'c': 2, 'name': 'f'}],
              'senkrecht': [3], 'waagrecht': [2]},
     '_verbot': ['1/(x − 3) + 2']},
    {'lernziel': 'beurteilen', 'titel': 'Aussagen über Hyperbeln prüfen',
     'regel': 'Prüfe Aussagen mit D, den Asymptoten und Funktionswerten. Wichtig: Der Graph von a/(x + b) + c berührt ⟦keine⟧ seiner beiden Asymptoten.',
     'schritte': ['Aussage: „f(x) = 4/x + 1 nimmt den Wert 1 an.“', '4/x = 0 hat keine Lösung.', 'Die Aussage ist ⟦falsch⟧: y = 1 ist die waagrechte Asymptote.'],
     'fehler': 'Dass sich der Graph der Asymptote nähert, heißt nicht, dass er sie irgendwann erreicht. a/(x + b) wird ⟦nie genau 0⟧.',
     '_verbot': ['4/x + 1']},
]


# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'indirekt': {
  'einstieg': 'Ein Teich soll leer gepumpt werden. Mit 4 Pumpen dauert es 6 Stunden. Mit mehr Pumpen geht es schneller, mit weniger langsamer: doppelt so viele Pumpen, halb so viel Zeit. So eine Zuordnung heißt ⟦indirekt proportional⟧.',
  'woerter': [['indirekt proportional', 'doppelt so viel von x → halb so viel von y; das Produkt x · y bleibt gleich'], ['Pumpen-Stunden', 'Pumpen mal Stunden: so groß ist die ganze Arbeit'],
              ['y = k/x', 'k ist das gleichbleibende Produkt, hier k = 24'], ['Hyperbel', 'der geschwungene Graph von y = k/x']],
  'schritte': ['4 Pumpen leeren ein Becken in 6 Stunden. Wie lange brauchen 3 Pumpen?', 'Die ganze Arbeit sind 4 · 6 = 24 Pumpen-Stunden. Das bleibt gleich, egal wie viele Pumpen arbeiten.',
               'Weniger Pumpen brauchen mehr Zeit: 3 Pumpen brauchen 24 : 3 = ⟦8 Stunden⟧.'],
  'regel': 'So rechnest du bei ⟦indirekter Proportionalität⟧: Das ⟦Produkt x · y⟧ bleibt immer gleich. Erst dieses Produkt berechnen, dann durch das neue x teilen: y = k/x. Der Graph ist eine ⟦Hyperbel⟧.'},
 'definitionsmenge': {
  'einstieg': 'Eine Pizza für 12 € wird unter x Freunden aufgeteilt; jeder zahlt 12/x €. Kommen pro Person noch 2 € für Getränke dazu, sind es 12/x + 2 €. Funktionen mit x im Nenner heißen ⟦gebrochen-rationale Funktionen⟧. Für x = 0 ergeben sie keinen Sinn – diese Zahl gehört nicht zur ⟦Definitionsmenge⟧.',
  'woerter': [['gebrochen-rationale Funktion', 'eine Funktion mit x im Nenner, z. B. f(x) = 3/(x − 2) + 1'], ['a/(x + b) + c', 'die allgemeine Form; a, b und c sind feste Zahlen'],
              ['Definitionsmenge D', 'alle x, die man einsetzen darf'], ['ℚ \\ {2}', 'alle Bruchzahlen außer 2']],
  'schritte': ['f(x) = 3/(x − 2) + 1. Welches x ist verboten?', 'Der Nenner ist x − 2. Er wird 0, wenn x = 2 ist.', 'Durch 0 darf man nicht teilen. Also muss die 2 heraus.',
               'Ergebnis: ⟦D = ℚ \\ {2}⟧.'],
  'regel': 'So findest du D: den ⟦Nenner gleich 0⟧ setzen. Bei a/(x + b) + c ist das ⟦x = −b⟧, also D = ℚ \\ {−b}. Achte auf das Vorzeichen.'},
 'asymptoten': {
  'einstieg': 'Je mehr Freunde sich die Pizza für 12 € teilen, desto weniger zahlt jeder: bei 12 Freunden 1 €, bei 1200 Freunden 1 Cent – aber nie ganz 0 €. Der Betrag nähert sich der 0 immer mehr, ohne sie zu erreichen. Eine Linie, der sich ein Graph so immer mehr nähert, heißt ⟦Asymptote⟧.',
  'woerter': [['Asymptote', 'eine Gerade, der sich der Graph immer mehr nähert, ohne sie zu berühren'], ['senkrechte Asymptote', 'senkrechte Linie dort, wo der Nenner 0 wird, z. B. x = −4'],
              ['waagrechte Asymptote', 'waagrechte Linie, der sich der Graph für sehr große x nähert, z. B. y = −3']],
  'schritte': ['f(x) = 2/(x + 4) − 3.', 'Senkrechte Asymptote: Der Nenner x + 4 wird 0 bei x = −4. Dort hat der Graph eine Lücke: ⟦x = −4⟧.',
               'Waagrechte Asymptote: Für sehr große x ist 2/(x + 4) fast 0. Übrig bleibt −3: ⟦y = −3⟧.', 'Im Bild siehst du beide Asymptoten als Linien, an die sich der Graph anschmiegt.'],
  'regel': 'So bestimmst du die ⟦Asymptoten⟧ von f(x) = a/(x + b) + c: ⟦senkrecht⟧ bei x = −b (dort ist der Nenner 0), ⟦waagrecht⟧ bei y = c.'},
 'achsenpunkte': {
  'einstieg': 'Wo ein Graph die Achsen trifft, steckt oft eine wichtige Information: der Wert ganz am Anfang, also bei x = 0, und die Stelle, an der der Wert genau 0 wird. Bei einem Kontostand wäre das: Wie viel ist am Anfang da, und wann ist er bei 0? Diese Punkte heißen ⟦Achsenschnittpunkte⟧.',
  'woerter': [['Achsenschnittpunkt', 'ein Punkt, an dem der Graph eine Achse trifft'], ['Nullstelle', 'das x, bei dem f(x) = 0 ist – dort wird die x-Achse geschnitten'],
              ['f(0)', 'der Wert bei x = 0 – dort wird die y-Achse geschnitten']],
  'schritte': ['f(x) = 6/(x + 1) − 2.', 'y-Achse: x = 0 einsetzen: f(0) = 6/1 − 2 = 4. Der Punkt ist (0 | 4).',
               'Nullstelle: f(x) = 0 setzen, also 6/(x + 1) − 2 = 0. Auf beiden Seiten 2 dazuzählen: 6/(x + 1) = 2.',
               '6 geteilt durch 3 ergibt 2, also ist x + 1 = 3 und ⟦x = 2⟧. Der Punkt ist (2 | 0).']},
 'parameter': {
  'einstieg': 'Ein Bild an der Wand kannst du nach rechts oder nach oben verschieben – es bleibt dasselbe Bild, nur an anderer Stelle. Mit Graphen geht das auch: Der Graph von 1/(x − 3) + 2 sieht genauso aus wie der von 1/x, nur ⟦verschoben⟧.',
  'woerter': [['verschieben', 'den ganzen Graphen versetzen, ohne seine Form zu ändern'], ['g(x) = 1/x', 'die Grundform der Hyperbel'],
              ['b und c', 'die Zahlen in a/(x + b) + c, die die Verschiebung festlegen']],
  'schritte': ['f(x) = 1/(x − 3) + 2 soll aus g(x) = 1/x entstehen.', 'Der Nenner x − 3 wird bei x = 3 null. Die Lücke ist von 0 nach 3 gewandert: Verschiebung um 3 nach rechts.',
               'Das + 2 hebt jeden Punkt um 2 an: Verschiebung um 2 nach oben.', 'Die Asymptoten sind jetzt ⟦x = 3 und y = 2⟧.']},
 'beurteilen': {
  'einstieg': 'Bei der Pizza zahlt jeder 12/x Euro. Jemand behauptet: „Bei genug Freunden zahlt jeder 0 €.“ Das stimmt nicht – der Betrag wird immer kleiner, aber nie genau 0. Solche Aussagen über Hyperbeln prüfst du mit dem, was du über D und die ⟦Asymptoten⟧ weißt.',
  'woerter': [['Aussage', 'ein Satz, der entweder wahr oder falsch ist'], ['berühren', 'einen gemeinsamen Punkt haben']],
  'schritte': ['Aussage: „f(x) = 4/x + 1 nimmt den Wert 1 an.“', 'Wäre f(x) = 1, dann müsste 4/x = 0 sein.', '4 geteilt durch irgendeine Zahl ist nie 0. Also gibt es kein solches x.',
               'Die Aussage ist ⟦falsch⟧: y = 1 ist die waagrechte Asymptote, die der Graph nie erreicht.']},
}

for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))
# ---- KLAR ENDE ----


def nz(R, lo=-6, hi=6):
    return R.choice([k for k in range(lo, hi + 1) if k])


def ft(a, b, c):
    """a/(x + b) + c als Text."""
    s = f'{zt(a)}/x' if b == 0 else f'{zt(a)}/({lin(1, b)})'
    if c: s += f' {"+" if c > 0 else "−"} {zt(abs(c))}'
    return s


def g_indirekt(R, st):
    if st >= 2 and R.random() < .25:
        art = R.choice(['pumpen', 'pizza'])
        if art == 'pumpen':
            p1, h1 = R.choice([(4, 6), (3, 8), (2, 12), (6, 4)]); p2 = R.choice([q for q in (2, 3, 4, 6, 8, 12) if q != p1 and (p1 * h1) % q == 0])
            falsch = Fr(h1 * p2, p1)
            return A(R, f'Jemand rechnet: {p1} Pumpen brauchen {h1} h, also brauchen {p2} Pumpen {zt(falsch)} h. Was ist falsch?',
                     f'{"Mehr" if p2 > p1 else "Weniger"} Pumpen brauchen {"weniger" if p2 > p1 else "mehr"} Zeit: {p1} · {h1} = {p1 * h1}, {p1 * h1} : {p2} = {zt(Fr(p1 * h1, p2))} h.',
                     ['Richtig gerechnet.', f'Es müssten {zt(falsch + 2)} h sein.', f'Man muss {h1} + {p2} rechnen.'],
                     f'Indirekt proportional: Das Produkt Pumpen · Stunden bleibt gleich ({p1 * h1}). Gerechnet wurde wie bei einer direkten Proportionalität.',
                     'Mehr Pumpen – mehr oder weniger Zeit?')
        k1, s1 = R.choice([(6, 2), (4, 3), (8, 3), (6, 4)]); k2 = R.choice([q for q in (2, 3, 4, 6, 8, 12) if q != k1 and (k1 * s1) % q == 0])
        falsch = Fr(s1 * k2, k1)
        return A(R, f'{k1} Kinder teilen Pizzastücke, jedes bekommt {s1} Stücke. Jemand rechnet: {k2} Kinder bekommen je {zt(falsch)} Stücke. Was ist falsch?',
                 f'{"Weniger" if k2 < k1 else "Mehr"} Kinder bekommen {"mehr" if k2 < k1 else "weniger"}: {k1 * s1} : {k2} = {zt(Fr(k1 * s1, k2))} Stücke.',
                 ['Richtig gerechnet.', f'Es müssten {zt(falsch + 1)} Stücke sein.', 'Man kann es nicht ausrechnen.'],
                 f'Alle Stücke zusammen: {k1} · {s1} = {k1 * s1}. Die Zahl bleibt gleich, also wird durch die Zahl der Kinder geteilt.',
                 'Wie viele Stücke gibt es insgesamt?')
    if st == 1:
        k = R.choice([12, 18, 24, 30, 36, 48, 60, 72, 120])
        x1 = R.choice([d for d in range(2, 13) if k % d == 0]); x2 = R.choice([d for d in range(1, 25) if k % d == 0 and d != x1])
        art = R.choice(['maler', 'pumpen', 'kiste'])
        if art == 'maler':
            t = f'{x1} Maler streichen ein Haus in {k // x1} Tagen. Wie viele Tage brauchen {x2} Maler (bei gleicher Arbeitsweise)?'
        elif art == 'pumpen':
            t = f'{x1} gleiche Pumpen leeren einen Teich in {k // x1} Stunden. Wie viele Stunden brauchen {x2} Pumpen?'
        else:
            t = f'Ein Vorrat reicht für {x1} Tiere {k // x1} Tage. Wie viele Tage reicht er für {x2} Tiere?'
        return Z(t, Fr(k, x2), f'{x1} * {k // x1} / {x2}', f'Produkt: {x1} · {k // x1} = {k}. {k} : {x2} = {zt(Fr(k, x2))}.',
                 'Mehr ... – weniger ...: Berechne zuerst das konstante Produkt.')
    if st == 2:
        if R.random() < .5:
            v1 = R.choice([40, 50, 60, 80, 90, 100, 120]); t1 = Fr(R.choice([2, 3, 4, 5, 6]), R.choice([1, 2]))
            s = v1 * t1; v2 = R.choice([v for v in (30, 40, 45, 50, 60, 75, 80, 100, 120, 150) if v != v1])
            t2 = s / v2
            if not ist_endlich(t2): return g_indirekt(R, st)
            return Z(f'Mit {v1} km/h dauert eine Fahrt {zt(t1)} h. Wie lange dauert sie mit {v2} km/h?', t2, f'{v1} * {cz(t1)} / {v2}',
                     f'v · t ist die Strecke: {v1} · {zt(t1)} = {zt(s)} km. t = {zt(s)} : {v2} = {zt(t2)} h.', 'Geschwindigkeit · Zeit = Strecke bleibt gleich.', einheit='h')
        k = R.choice([12, 24, 36, 48, 60]); xs = R.sample([d for d in range(1, 13) if k % d == 0], 3)
        x0 = R.choice([d for d in range(1, 61) if k % d == 0 and d not in xs])
        ps = ', '.join(f'({x} | {k // x})' for x in xs)
        return Z(f'Die Tabelle {ps} gehört zu einer indirekten Proportionalität. Welcher y-Wert gehört zu x = {x0}?', Fr(k, x0), f'{xs[0]} * {k // xs[0]} / {x0}',
                 f'x · y = {xs[0]} · {k // xs[0]} = {k}. y = {k} : {x0} = {zt(Fr(k, x0))}.', 'Berechne das Produkt x · y.')
    k = R.choice([12, 18, 24, 30, 36])
    xs = sorted(R.sample([d for d in range(1, 13) if k % d == 0], 3))
    art = R.choice(['indirekt', 'direkt', 'keine'])
    if art == 'indirekt': ys = [k // x for x in xs]
    elif art == 'direkt': ys = [2 * x for x in xs]
    else: ys = [k // xs[0], k // xs[0] - 2, k // xs[0] - 3]
    ps = ', '.join(f'({x} | {y})' for x, y in zip(xs, ys))
    opts = {'indirekt': 'indirekt proportional', 'direkt': 'direkt proportional', 'keine': 'weder direkt noch indirekt proportional'}
    prod = ', '.join(str(x * y) for x, y in zip(xs, ys)); quot = ', '.join(zt(Fr(y, x)) for x, y in zip(xs, ys))
    return A(R, f'Wie ist die Zuordnung {ps}?', opts[art], [v for kk, v in opts.items() if kk != art] + ['indirekt, weil y kleiner wird'] if art == 'keine' else [v for kk, v in opts.items() if kk != art],
             f'Produkte x · y: {prod}. Quotienten y : x: {quot}. ' + {'indirekt': 'Produkte gleich → indirekt.', 'direkt': 'Quotienten gleich → direkt.', 'keine': 'Weder Produkte noch Quotienten sind gleich.'}[art],
             'Prüfe: Sind alle Produkte x · y gleich? Sind alle Quotienten y : x gleich?')


def g_definitionsmenge(R, st):
    a, b, c = nz(R, -9, 9), nz(R, -8, 8), R.randint(-6, 6)
    if st == 3:
        k = R.choice([2, 4, 5]); m = R.choice([j for j in range(-9, 10) if j % k])
        T = f'{zt(a)}/({lin(k, m)}){"" if not c else (" + " if c > 0 else " − ") + str(abs(c))}'
        x0 = Fr(-m, k)
        return Z(f'Welche Zahl gehört nicht zur Definitionsmenge von f(x) = {T}?', x0, f'-({m}) / {k}',
                 f'{lin(k, m)} = 0 → x = {zt(x0)}. D = ℚ \\ {{{zt(x0)}}}.', 'Setze den Nenner gleich 0 und löse.')
    if st == 1 or R.random() < .5:
        return A(R, f'Gib die Definitionsmenge von f(x) = {ft(a, b, c)} an.', f'D = ℚ \\ {{{zt(-b)}}}',
                 [f'D = ℚ \\ {{{zt(b)}}}', 'D = ℚ', f'D = ℚ \\ {{{zt(c)}}}' if c not in (b, -b) else 'D = ℚ \\ {0}'],
                 f'Nenner {lin(1, b)} = 0 für x = {zt(-b)}. D = ℚ \\ {{{zt(-b)}}}.', 'Welche Zahl macht den Nenner 0? Achte auf das Vorzeichen.')
    return Z(f'Welche Zahl gehört nicht zur Definitionsmenge von f(x) = {ft(a, b, c)}?', -b, f'-({b})',
             f'Nenner {lin(1, b)} = 0 für x = {zt(-b)}.', 'Welche Zahl macht den Nenner 0?')


def g_asymptoten(R, st):
    if st >= 2 and R.random() < .35:
        a, b, c = R.choice([1, 2, 3, -1, -2]), R.randint(-3, 3), R.randint(-3, 3)
        gr = {'typ': 'koordinaten', 'x': [-b - 6, -b + 6], 'y': [c - 6, c + 6], 'graphen': [{'art': 'hyperbel', 'a': a, 'b': b, 'c': c, 'name': 'f'}]}
        if R.random() < .55:
            return mit_bild(L('Lies die Asymptoten der Hyperbel ab.', 'x = □; y = □', [-b, c], [str(-b), str(c)],
                              f'Der Graph nähert sich der senkrechten Linie x = {zt(-b)} und der waagrechten Linie y = {zt(c)}, ohne sie zu berühren.',
                              'Wo ist die Lücke zwischen den beiden Ästen? Welcher Höhe nähert sich der Graph links und rechts?', hinweis='Senkrechte Asymptote x, waagrechte Asymptote y.'), gr)
        if b == 0 and c == 0: c = R.choice([1, 2, -2])
        gr['graphen'][0]['c'] = c; gr['y'] = [c - 6, c + 6]
        return mit_bild(A(R, 'Welcher Term gehört zum gezeichneten Graphen?', f'f(x) = {ft(a, b, c)}',
                          [f'f(x) = {ft(a, -b, c)}' if b else f'f(x) = {ft(a, c, 0)}', f'f(x) = {ft(a, c, b)}' if c != b else f'f(x) = {ft(a, -c, -b)}', f'f(x) = {ft(-a, b, c)}'],
                          f'Senkrechte Asymptote x = {zt(-b)} → Nenner {lin(1, b)}. Waagrechte Asymptote y = {zt(c)} → + {kl(c)}. Lage der Äste: a {"positiv (1. und 3. Feld um die Asymptoten)" if a > 0 else "negativ (2. und 4. Feld)"}.',
                          'Lies erst die Asymptoten ab. Dann prüfe, in welchen Feldern die Äste liegen.'), gr)
    a, b, c = nz(R, -9, 9), R.choice([0] + [k for k in range(-8, 9) if k]) if st == 1 else nz(R, -8, 8), nz(R, -6, 6)
    if st == 3 and R.random() < .5:
        # Term aus Asymptoten bestimmen
        r = ft(a, b, c)
        f = [ft(a, -b, c), ft(a, b, -c), ft(a, c, b) if c != b else ft(a, -c, -b)]
        return A(R, f'Eine Hyperbel f(x) = {zt(a)}/(x + b) + c hat die Asymptoten x = {zt(-b)} und y = {zt(c)}. Wie heißt der Term?', f'f(x) = {r}', [f'f(x) = {t}' for t in f],
                 f'x = {zt(-b)} → b = {zt(b)}; y = {zt(c)} → c = {zt(c)}. f(x) = {r}.', 'Die senkrechte Asymptote liegt bei x = −b, die waagrechte bei y = c.')
    if R.random() < .5:
        return Z(f'Gib die senkrechte Asymptote von f(x) = {ft(a, b, c)} an. x = □', -b, f'-({b})',
                 f'Nenner {lin(1, b)} = 0 für x = {zt(-b)}. Senkrechte Asymptote: x = {zt(-b)}.', 'Wo ist der Nenner 0?')
    return Z(f'Gib die waagrechte Asymptote von f(x) = {ft(a, b, c)} an. y = □', c, f'{c}',
             f'Für sehr große x wird {zt(a)}/({lin(1, b)}) fast 0. Also nähert sich f dem Wert {zt(c)}: y = {zt(c)}.', 'Was bleibt übrig, wenn der Bruch fast 0 wird?')


ACH = {'null': 0}


def g_achsenpunkte(R, st):
    if st >= 2 and (R.random() < .3 or ACH['null'] >= 10):
        if R.random() < .5:
            a, b = nz(R, -9, 9), R.randint(-6, 6)
            return A(R, f'Welche Nullstelle hat f(x) = {ft(a, b, 0)}?', 'keine Nullstelle', [f'x = {zt(-b)}' if b else f'x = {zt(a)}', 'x = 0' if b else f'x = {zt(-a)}', f'x = {zt(a)}' if b and a != -b else 'x = 1'],
                     f'{zt(a)}/{"x" if not b else "(" + lin(1, b) + ")"} = 0 wäre nur möglich, wenn der Zähler {zt(a)} null wäre. Keine Nullstelle.', 'Wann ist ein Bruch gleich 0?')
        a, c = nz(R, -6, 6), nz(R, -5, 5)
        return A(R, f'Wo schneidet f(x) = {ft(a, 0, c)} die y-Achse?', 'gar nicht, x = 0 gehört nicht zu D', [f'bei y = {zt(c)}', f'bei y = {zt(a + c)}', f'bei y = {zt(a)}'],
                 f'Auf der y-Achse ist x = 0. Aber {zt(a)}/0 ist nicht definiert: D = ℚ \\ {{0}}. Die y-Achse ist hier die senkrechte Asymptote.', 'Darf man x = 0 einsetzen?')
    while True:
        a, b, c = nz(R, -12, 12), nz(R, -6, 6), R.randint(-6, 6)
        y0 = Fr(a, b) + c
        x0 = Fr(-a, c) - b if c else None
        if st == 1:
            if ist_endlich(y0) and len(zt(y0)) <= 5: break
        else:
            if c and ist_endlich(x0) and len(zt(x0)) <= 5 and x0 != -b: break
    if st == 1:
        return Z(f'In welchem Punkt schneidet der Graph von f(x) = {ft(a, b, c)} die y-Achse? Gib den y-Wert an.', y0, f'{a} / ({b}) + ({c})',
                 f'f(0) = {zt(a)}/{kl(b)}{"" if not c else (" + " if c > 0 else " − ") + str(abs(c))} = {zt(y0)}.', 'Auf der y-Achse ist x = 0.')
    if st == 3 and R.random() < .35:
        a, b = nz(R, -9, 9), nz(R, -6, 6)
        return A(R, f'Welche Nullstelle hat f(x) = {ft(a, b, 0)}?', 'keine Nullstelle', [f'x = {zt(-b)}', 'x = 0', f'x = {zt(a)}'],
                 f'{zt(a)}/({lin(1, b)}) = 0 wäre nur möglich, wenn der Zähler {zt(a)} null wäre. Keine Nullstelle.', 'Wann ist ein Bruch gleich 0?')
    ACH['null'] += 1
    return Z(f'Berechne die Nullstelle von f(x) = {ft(a, b, c)}.', x0, f'-({a}) / ({c}) - ({b})',
             f'{zt(a)}/({lin(1, b)}) = {zt(-c)} → {lin(1, b)} = {zt(a)} : {kl(-c)} = {zt(Fr(-a, c))} → x = {zt(x0)}.',
             'Setze f(x) = 0, bringe c auf die andere Seite und multipliziere mit dem Nenner.')


def verschiebung(b, c):
    t = []
    if b: t.append(f'um {zt(abs(b))} nach {"links" if b > 0 else "rechts"}')
    if c: t.append(f'um {zt(abs(c))} nach {"oben" if c > 0 else "unten"}')
    return ' und '.join(t)


def g_parameter(R, st):
    if st >= 2 and R.random() < .25:
        k = R.choice([2, 3, 4, 5])
        if R.random() < .5:
            gr = {'typ': 'koordinaten', 'x': [-5, 5], 'y': [-5, 5], 'graphen': [{'art': 'hyperbel', 'a': k, 'name': 'g'}, {'art': 'hyperbel', 'a': -k, 'name': 'f'}]}
            return mit_bild(A(R, f'Wie unterscheidet sich der Graph von f(x) = −{k}/x vom Graphen von g(x) = {k}/x?', 'Er liegt im 2. und 4. Feld statt im 1. und 3.',
                              ['Er ist nach unten verschoben.', 'Kein Unterschied.', 'Er ist nach links verschoben.'],
                              f'Das Minus macht aus jedem Funktionswert die Gegenzahl: f(1) = −{k}, g(1) = {k}. Der Graph wird an der x-Achse gespiegelt; die Asymptoten bleiben x = 0 und y = 0.',
                              'Vergleiche f(1) und g(1).'), gr)
        return A(R, f'Wie unterscheidet sich der Graph von f(x) = {k}/x vom Graphen von g(x) = 1/x?', 'Er ist weiter vom Ursprung entfernt (gestreckt).',
                 ['Er ist nach oben verschoben.', 'Er liegt im 2. und 4. Feld.', 'Er hat andere Asymptoten.'],
                 f'f(1) = {k}, g(1) = 1: Jeder Funktionswert ist {k}-mal so groß. Die Asymptoten x = 0 und y = 0 bleiben gleich, der Graph rückt nach außen.',
                 'Vergleiche f(1) und g(1). Ändern sich die Asymptoten?')
    a, b, c = nz(R, -6, 6), nz(R, -7, 7), nz(R, -6, 6)
    if st == 1:
        c = 0 if R.random() < .5 else c
        if c: b = 0
        T = ft(a, b, c)
        r = verschiebung(b, c)
        f = [verschiebung(-b, -c), verschiebung(c, b) if b else verschiebung(-c, 0) or 'um 1 nach oben', 'gar nicht – der Graph ist gleich']
        return A(R, f'Wie entsteht der Graph von f(x) = {T} aus dem Graphen von g(x) = {zt(a)}/x?', f'Verschiebung {r}', [x if x.startswith('gar') else f'Verschiebung {x}' for x in f if x],
                 (f'Im Nenner steht {lin(1, b)}: Verschiebung {verschiebung(b, 0)}.' if b else f'{"+" if c > 0 else "−"} {abs(c)} hinter dem Bruch: Verschiebung {verschiebung(0, c)}.'),
                 'Steht in der Klammer x − 3, geht es nach rechts. + c verschiebt nach oben.')
    if st == 2:
        T = ft(a, b, c)
        r = verschiebung(b, c)
        f = [verschiebung(-b, c), verschiebung(b, -c), verschiebung(-b, -c)]
        return A(R, f'Wie entsteht der Graph von f(x) = {T} aus dem Graphen von g(x) = {zt(a)}/x?', f'Verschiebung {r}', [f'Verschiebung {x}' for x in f],
                 f'Asymptoten von f: x = {zt(-b)}, y = {zt(c)}. Bei g: x = 0, y = 0. Also Verschiebung {r}.', 'Vergleiche die Asymptoten von f und g.')
    r = ft(a, b, c)
    f = [ft(a, -b, c), ft(a, b, -c), ft(a, -b, -c)]
    return A(R, f'Der Graph von g(x) = {zt(a)}/x wird {verschiebung(b, c)} verschoben. Wie heißt der neue Funktionsterm?', f'f(x) = {r}', [f'f(x) = {x}' for x in f],
             f'{verschiebung(b, 0)}: x wird zu {lin(1, b)}. {verschiebung(0, c)}: + {kl(c)}. f(x) = {r}.', 'Nach rechts um d: x − d in die Klammer. Nach oben um e: + e.')


def g_beurteilen(R, st):
    while True:
        a, b, c = nz(R, -8, 8), nz(R, -6, 6), nz(R, -5, 5)
        x0 = Fr(-a, c) - b
        if ist_endlich(x0) and x0 != -b and len(zt(x0)) <= 5 and a != c: break
    f = lambda x: Fr(a) / (x + b) + c
    T = ft(a, b, c)
    while True:
        x1 = R.choice([k for k in range(-5, 6) if k != -b])
        if ist_endlich(f(Fr(x1))): break
    y0 = f(Fr(0))
    # (Typ, Aussage, wahr, Richtigstellung) – je Aufgabe höchstens eine Aussage je Typ
    al = [
        ('gerade_c', f'Der Graph schneidet die Gerade y = {zt(c)}.', False, f'y = {zt(c)} ist die waagrechte Asymptote; {zt(a)}/({lin(1, b)}) wird nie 0.'),
        ('d', f'f ist für x = {zt(-b)} nicht definiert.', True, ''),
        ('d', f'f ist für x = {zt(b)} nicht definiert.', False, f'Nicht definiert ist f nur für x = {zt(-b)}.'),
        ('null', f'Die Nullstelle ist x = {zt(x0)}.', True, ''),
        ('null', 'Der Graph hat zwei Nullstellen.', False, f'Es gibt genau eine Nullstelle, x = {zt(x0)}.'),
        ('wert', f'f({zt(x1)}) = {zt(f(Fr(x1)))}', True, ''),
        ('wert', f'f({zt(x1)}) = {zt(f(Fr(x1)) + 1)}', False, f'Richtig ist f({zt(x1)}) = {zt(a)}/{kl(x1 + b)} {"+" if c > 0 else "−"} {zt(abs(c))} = {zt(f(Fr(x1)))}.'),
        ('waag', f'Die waagrechte Asymptote ist y = {zt(a)}.', False, f'Die waagrechte Asymptote ist y = {zt(c)}, nicht y = {zt(a)}.'),
        ('senk', f'Die senkrechte Asymptote ist x = {zt(-b)}.', True, ''),
        ('yachse', f'Der Graph schneidet die y-Achse bei y = {zt(y0)}.', True, ''),
    ]
    al = [x for x in al if not (x[0] == 'yachse' and not ist_endlich(y0))]
    def waehle(richtig_wahr):
        kand = [x for x in al if x[2] == richtig_wahr]
        ziel = R.choice(kand)
        rest = [x for x in al if x[2] != richtig_wahr and x[0] != ziel[0]]
        R.shuffle(rest)
        andere, typen = [], {ziel[0]}
        for x in rest:
            if x[0] in typen: continue
            andere.append(x); typen.add(x[0])
            if len(andere) == 3: break
        return ziel, andere
    if st == 1 or (st == 2 and R.random() < .5):
        ziel, andere = waehle(True)
        return A(R, f'Welche Aussage über f(x) = {T} ist richtig?', ziel[1], [x[1] for x in andere],
                 f'Richtig: {ziel[1]} Asymptoten x = {zt(-b)}, y = {zt(c)}; Nullstelle {zt(x0)}.', 'Bestimme D, Asymptoten und Nullstelle, dann vergleiche.')
    ziel, andere = waehle(False)
    return A(R, f'Welche Aussage über f(x) = {T} ist FALSCH?', ziel[1], [x[1] for x in andere],
             f'Falsch ist: {ziel[1].rstrip(".")}. {ziel[3]} Die anderen Aussagen stimmen: Asymptoten x = {zt(-b)} und y = {zt(c)}, Nullstelle {zt(x0)}.',
             'Bestimme D, Asymptoten und Nullstelle, dann vergleiche.')


GEN = {'indirekt': g_indirekt, 'definitionsmenge': g_definitionsmenge, 'asymptoten': g_asymptoten, 'achsenpunkte': g_achsenpunkte,
       'parameter': g_parameter, 'beurteilen': g_beurteilen}


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl8.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl8 import mit_umbau  # noqa: E402

_KO = lambda **k: {'typ': 'koordinaten', **k}
_H = lambda a, b, c, name=None, **k: {'art': 'hyperbel', 'a': a, 'b': b, 'c': c, **({'name': name} if name else {}), **k}
UMBAU = {
 'indirekt': {
  'einstieg': 'Ein Teich soll leer gepumpt werden. 4 Pumpen brauchen 6 Stunden, doppelt so viele Pumpen brauchen halb so lange. So eine Zuordnung heißt ⟦indirekt proportional⟧.',
  'woerter': [['indirekt proportional', 'doppelt so viel → halb so viel'], ['Hyperbel', 'der gebogene Graph von y = k/x'], ['Produkt', 'das Ergebnis einer Malrechnung']],
  'bild': _KO(x=[0, 12], y=[0, 12], graphen=[_H(24, 0, 0, bereich=[2, 12])], name_x='Pumpen', name_y='h'),
  'schritte': [{'text': '4 Pumpen brauchen 6 h. Wie lange brauchen 3 Pumpen?', 'bild': {'punkte': [{'x': 4, 'y': 6, 'name': '(4 | 6)'}]}},
               {'text': 'Die Arbeit ist 4 · 6 = 24 Pumpen-Stunden. Dieses Produkt bleibt gleich.'},
               {'text': '3 Pumpen brauchen 24 : 3 = ⟦8 Stunden⟧.', 'bild': {'punkte': [{'x': 4, 'y': 6, 'name': '(4 | 6)'}, {'x': 3, 'y': 8, 'name': '(3 | 8)'}]}},
               {'text': 'Alle Paare liegen auf der Hyperbel y = 24/x.'}],
  'fehler': '6 : 4 · 3 = 4,5 h ist falsch: Mit weniger Pumpen wäre der Teich schneller leer. Hier bleibt das ⟦Produkt⟧ gleich.',
  'fehler_bild': {'punkte': [{'x': 4, 'y': 6, 'name': '(4 | 6)'}, {'x': 3, 'y': 4.5, 'name': '4,5 h?', 'offen': True}]},
  'regel': 'Bei indirekter Proportionalität bleibt ⟦x · y gleich⟧. Der Graph ist eine Hyperbel y = k/x.'},
 'definitionsmenge': {
  'einstieg': 'Eine Pizza für 12 € teilen sich x Freunde, dazu zahlt jeder 2 € für Getränke: 12/x + 2 Euro. So eine Funktion mit x im Nenner heißt ⟦gebrochen-rational⟧.',
  'woerter': [['gebrochen-rational', 'eine Funktion mit x im Nenner'], ['D', 'die Definitionsmenge: alle erlaubten x'], ['ℚ \\ {2}', 'alle Bruchzahlen außer 2']],
  'bild': _KO(x=[-4, 8], y=[-5, 7], graphen=[_H(3, -2, 1, 'f')]),
  'schritte': [{'text': 'f(x) = 3/(x − 2) + 1. Welches x ist verboten?'},
               {'text': 'Der Nenner x − 2 wird 0, wenn x = 2 ist.', 'bild': {'senkrecht': [2]}},
               {'text': 'Durch 0 teilt man nicht: ⟦D = ℚ \\ {2}⟧.'}],
  'fehler': 'Nicht −2 streichen: Der Nenner x − 2 wird bei ⟦x = +2⟧ null. Das Vorzeichen dreht sich um.',
  'fehler_bild': {'senkrecht': [-2], 'punkte': [{'x': -2, 'y': -3, 'name': '−2?', 'offen': True}]},
  'regel': 'Setze ⟦den Nenner gleich 0⟧ und streiche dieses x. Bei a/(x + b) + c ist das x = −b.'},
 'asymptoten': {
  'einstieg': 'Je mehr Freunde sich die 12-€-Pizza teilen, desto weniger zahlt jeder. Bei 1200 Freunden ist es 1 Cent, aber nie ganz 0 €. Eine Linie, der sich ein Graph so nähert, heißt ⟦Asymptote⟧.',
  'woerter': [['Asymptote', 'eine Linie, der sich der Graph immer mehr nähert, ohne sie zu erreichen'], ['senkrecht', 'von oben nach unten, wie eine Hauswand'], ['waagrecht', 'von links nach rechts, wie der Horizont']],
  'bild': _KO(x=[-10, 4], y=[-8, 3], graphen=[_H(2, 4, -3, 'f')]),
  'schritte': [{'text': 'f(x) = 2/(x + 4) − 3.'},
               {'text': 'Der Nenner wird 0 bei x = −4: senkrechte Asymptote ⟦x = −4⟧.', 'bild': {'senkrecht': [-4]}},
               {'text': 'Für große x ist 2/(x + 4) fast 0. Waagrecht bleibt ⟦y = −3⟧.', 'bild': {'waagrecht': [-3]}}],
  'fehler': 'Die waagrechte Asymptote ist nicht y = 2. Nicht der Zähler zählt, sondern die ⟦Verschiebung −3⟧ am Ende.',
  'fehler_bild': {'waagrecht': [-3, 2], 'punkte': [{'x': 1, 'y': 2, 'name': 'y = 2?'}]},
  'regel': 'Asymptoten: ⟦x = −b⟧ und ⟦y = c⟧. Das gilt für f(x) = a/(x + b) + c.'},
 'achsenpunkte': {
  'einstieg': 'Wo ein Graph die Achsen trifft, steckt oft das Wichtigste. Dort liest du den Startwert ab und die Stelle, an der der Wert 0 wird. Diese Punkte heißen ⟦Achsenschnittpunkte⟧.',
  'woerter': [['Achsenschnittpunkt', 'ein Punkt, an dem der Graph eine Achse trifft'], ['Nullstelle', 'ein x-Wert, bei dem f(x) = 0 ist']],
  'bild': _KO(x=[-6, 6], y=[-8, 8], graphen=[_H(6, 1, -2, 'f')], senkrecht=[-1], waagrecht=[-2]),
  'schritte': [{'text': 'f(x) = 6/(x + 1) − 2.'},
               {'text': 'y-Achse: f(0) = 6/1 − 2 = 4. Punkt (0 | 4).', 'bild': {'punkte': [{'x': 0, 'y': 4, 'name': '(0 | 4)'}]}},
               {'text': 'Nullstelle: 6/(x + 1) − 2 = 0, also 6/(x + 1) = 2.'},
               {'text': 'Das gilt für x + 1 = 3, also ⟦x = 2⟧.', 'bild': {'punkte': [{'x': 0, 'y': 4, 'name': '(0 | 4)'}, {'x': 2, 'y': 0, 'name': '(2 | 0)'}]}}],
  'fehler': 'f(0) = 4 ist nicht die Nullstelle, sondern der Schnitt mit der ⟦y-Achse⟧. Die Nullstelle liegt dort, wo y = 0 ist.',
  'fehler_bild': {'punkte': [{'x': 0, 'y': 4, 'name': 'y-Achse'}, {'x': 2, 'y': 0, 'name': 'Nullstelle'}]},
  'regel': 'y-Achse: ⟦x = 0 einsetzen⟧. Nullstelle: f(x) = 0 lösen. Ist c = 0, gibt es keine Nullstelle.'},
 'parameter': {
  'einstieg': 'Ein Bild an der Wand kannst du nach rechts oder nach oben rücken – es bleibt dasselbe Bild. Graphen kann man genauso ⟦verschieben⟧.',
  'woerter': [['verschieben', 'den ganzen Graphen rücken, ohne ihn zu verändern'], ['Lücke', 'die Stelle, an der der Graph nicht definiert ist']],
  'bild': _KO(x=[-4, 8], y=[-4, 6], graphen=[_H(1, 0, 0, 'g')]),
  'schritte': [{'text': 'Aus g(x) = 1/x soll f(x) = 1/(x − 3) + 2 werden.'},
               {'text': 'Die Lücke liegt jetzt bei x = 3: 3 nach rechts.', 'bild': {'graphen': [_H(1, 0, 0, 'g'), _H(1, -3, 0)], 'senkrecht': [3]}},
               {'text': '+ 2 hebt jeden Punkt um 2 an.', 'bild': {'graphen': [_H(1, 0, 0, 'g'), _H(1, -3, 2, 'f')], 'waagrecht': [2]}},
               {'text': 'Die Asymptoten sind ⟦x = 3 und y = 2⟧.'}],
  'fehler': 'Bei 1/(x − 3) geht es nicht nach links. Die Lücke liegt bei ⟦x = 3⟧, also rechts.',
  'fehler_bild': {'graphen': [_H(1, 0, 0, 'g'), _H(1, 3, 2, 'links?')], 'senkrecht': [-3]},
  'regel': 'Die Lücke liegt bei ⟦x = −b⟧. +c schiebt nach oben, −c nach unten.'},
 'beurteilen': {
  'einstieg': 'Jemand behauptet: „Bei genug Freunden zahlt jeder 0 € für die Pizza.“ Der Betrag wird kleiner, aber nie 0. Solche Aussagen prüfst du mit den ⟦Asymptoten⟧.',
  'woerter': [['Asymptote', 'eine Linie, der sich der Graph nähert, ohne sie zu erreichen']],
  'bild': _KO(x=[-6, 6], y=[-4, 6], graphen=[_H(4, 0, 1, 'f')], waagrecht=[1]),
  'schritte': [{'text': 'Aussage: „4/x + 1 nimmt den Wert 1 an.“'},
               {'text': 'Dann müsste 4/x = 0 sein.'},
               {'text': '4 geteilt durch eine Zahl ist nie 0. Die Aussage ist ⟦falsch⟧.'},
               {'text': 'y = 1 ist die Asymptote. Der Graph erreicht sie nie.'}],
  'fehler': 'Nah heran heißt nicht erreichen. a/(x + b) wird ⟦nie genau 0⟧ – wie der Pizzapreis pro Person.',
  'regel': 'Der Graph ⟦berührt keine Asymptote⟧. Prüfe Aussagen mit D, Asymptoten und Funktionswerten.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Indirekte Proportionalität', ['indirekt']), ('Hyperbeln untersuchen', ['definitionsmenge', 'asymptoten', 'achsenpunkte']),
          ('Parameter und Verstehen', ['parameter', 'beurteilen'])],
         'Indirekte Proportionalitäten erkennen und Funktionen f(x) = a/(x + b) + c untersuchen: Definitionsmenge, Asymptoten, Achsenschnittpunkte, Verschiebungen.',
         ['Indirekt proportional: x · y = konstant, y = k/x.', 'f(x) = a/(x + b) + c: D = ℚ \\ {−b}, Asymptoten x = −b und y = c.',
          'x − 3 in der Klammer: 3 nach rechts. + c: c nach oben.'],
         offen=['Hyperbeln selbst zeichnen lassen (Kind zeichnet) kann die App noch nicht; Ablesen von Asymptoten und „Term zum Graphen“ sind eingebaut.'])
