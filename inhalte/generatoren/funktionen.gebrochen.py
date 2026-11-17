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


# ---- SCHWER (Zehnte Runde: schwerere Aufgaben nach Prüfungsvorbild, siehe _schwer_kl8.py) ----
# Vorbilder (Typ und Niveau, nicht Wortlaut/Zahlen): BMT10 2024 (Rechtecke unter einer Hyperbel haben gleichen Flächeninhalt;
# Schnitt Hyperbel–Gerade), Grundwissen 8 (Wippe/Hebelgesetz als indirekte Proportionalität; D bestimmen und Hyperbel mit Asymptoten;
# Funktionsgleichung aus dem Graphen), Stegreifaufgaben-Typ Kl. 8 (Graphen und Terme zuordnen, Achsenschnittpunkte), BMT8 2025 (Aussage begründet widerlegen).
from _schwer_kl8 import Neu, mit_schwer  # noqa: E402

N = Neu(10_8_3)
_k = lambda **k: {'typ': 'koordinaten', **k}
_h = lambda a, b, c, **k: {'art': 'hyperbel', 'a': a, 'b': b, 'c': c, **k}

# indirekt
N.z('indirekt', 2, 'Bei einer Zuordnung bleibt x · y immer gleich. Für x = 4 ist y = 7,5. Berechne y für x = 6.', 5, '4 * 7.5 / 6', 'x · y = 4 · 7,5 = 30. Also y = 30 : 6 = 5.',
    'Berechne zuerst das feste Produkt.')
N.z('indirekt', 2, 'Ein Rechteck hat den Flächeninhalt 36 cm². Es ist 4,8 cm lang. Wie breit ist es?', 7.5, '36 / 4.8', 'Länge · Breite = 36. Breite = 36 : 4,8 = 7,5 cm.',
    'Bei festem Flächeninhalt ist die Breite indirekt proportional zur Länge.', einheit='cm')
N.z('indirekt', 3, 'Eine Wippe ist im Gleichgewicht, wenn auf beiden Seiten „Gewicht · Abstand zum Drehpunkt“ gleich ist. Ein Kind mit 30 kg sitzt 2 m vom Drehpunkt. Wie weit muss ein Kind mit 40 kg sitzen?',
    1.5, '30 * 2 / 40', '30 · 2 = 60. Also 40 · Abstand = 60, Abstand = 1,5 m. Das schwerere Kind sitzt näher am Drehpunkt.',
    'Gewicht und Abstand sind indirekt proportional.', einheit='m', art='P')
N.a('indirekt', 3, 'P liegt auf dem Graphen von f(x) = 12/x (x > 0). P, der Ursprung und die beiden Lotfußpunkte auf den Achsen bilden ein Rechteck (Bild: P(3 | 4)). Was gilt für seinen Flächeninhalt, wenn P auf dem Graphen wandert?',
    'Er ist immer 12, denn x · y = 12.', ['Er ist am größten für P(1 | 12).', 'Er wird immer kleiner, je weiter P nach rechts wandert.', 'Er ist nur für P(3 | 4) gleich 12.'],
    'Das Rechteck ist x breit und y hoch. Sein Flächeninhalt ist x · y. Für jeden Punkt des Graphen gilt y = 12/x, also x · y = 12.',
    'Der Flächeninhalt ist Breite · Höhe = x · y. Was weißt du über x · y?',
    grafik=_k(x=[0, 8], y=[0, 8], graphen=[_h(12, 0, 0, bereich=[1.5, 8])], punkte=[{'x': 3, 'y': 4, 'name': 'P'}], flaechen=[{'punkte': [[0, 0], [3, 0], [3, 4], [0, 4]]}]), art='P')
N.z('indirekt', 3, 'x und y sind indirekt proportional. x wird um 25 % erhöht. Um wie viel Prozent sinkt y?', 20, '(1 - 1 / 1.25) * 100',
    'Neues x = 1,25 · x. Damit x · y gleich bleibt, wird y durch 1,25 geteilt: y · 0,8. Das ist eine Abnahme um 20 %, nicht um 25 %.',
    'Teste mit Zahlen: x = 4, y = 10. Was ist y, wenn x = 5?', einheit='%', art='K')
N.z('indirekt', 3, '8 Arbeiter brauchen für einen Auftrag 15 Tage. Nach 5 Tagen kommen 2 Arbeiter dazu. Wie viele Tage dauert der Auftrag insgesamt?', 13, '5 + (8 * 15 - 8 * 5) / 10',
    'Der Auftrag braucht 8 · 15 = 120 Arbeitstage. Nach 5 Tagen sind 40 erledigt, 80 fehlen. 10 Arbeiter brauchen dafür 8 Tage. Insgesamt 5 + 8 = 13 Tage.',
    'Rechne in „Arbeitstagen“ (Arbeiter · Tage).', einheit='Tage', art='K')

# definitionsmenge
N.a('definitionsmenge', 2, 'Gib die Definitionsmenge von f(x) = 2/(3 − x) + 1 an.', 'D = ℚ \\ {3}', ['D = ℚ \\ {−3}', 'D = ℚ \\ {1}', 'D = ℚ'],
    'Nenner 0: 3 − x = 0 ⇔ x = 3. Also D = ℚ \\ {3}.', 'Hier steht x mit Minus im Nenner. Setze den Nenner gleich 0.')
N.z('definitionsmenge', 2, 'Welche Zahl gehört nicht zur Definitionsmenge von f(x) = 5/(x + 0,5) − 2?', -0.5, '-0.5', 'x + 0,5 = 0 ⇔ x = −0,5.', 'Wann wird der Nenner 0?')
N.a('definitionsmenge', 3, 'Gib die maximale Definitionsmenge von f(x) = 4/(x − 2) + 3/(x + 1) an.', 'D = ℚ \\ {−1; 2}', ['D = ℚ \\ {2}', 'D = ℚ \\ {−2; 1}', 'D = ℚ \\ {−1; 2; 3; 4}'],
    'Beide Nenner dürfen nicht 0 sein: x − 2 ≠ 0 und x + 1 ≠ 0. Ausgeschlossen sind 2 und −1.', 'Es gibt zwei Nenner. Prüfe jeden.', art='P')
N.a('definitionsmenge', 3, 'Die Abbildung zeigt den Graphen einer Funktion f(x) = a/(x + b) + c. Welche Definitionsmenge hat f?', 'D = ℚ \\ {−3}', ['D = ℚ \\ {3}', 'D = ℚ \\ {1}', 'D = ℚ \\ {−3; 1}'],
    'Ausgeschlossen ist nur die Stelle der senkrechten Asymptote: x = −3. Die waagrechte Asymptote y = 1 betrifft die Werte, nicht die Definitionsmenge.',
    'Welche Asymptote zeigt eine verbotene x-Stelle?', grafik=_k(x=[-8, 4], y=[-4, 6], graphen=[_h(2, 3, 1)], senkrecht=[-3], waagrecht=[1]), art='P')
N.z('definitionsmenge', 3, 'f(x) = 6/(x + b) − 1 hat die Definitionsmenge D = ℚ \\ {4}. Bestimme b.', -4, '-4',
    'Ausgeschlossen ist x = −b. Aus −b = 4 folgt b = −4. Probe: Nenner x − 4 ist bei x = 4 null.', 'Für welches x wird x + b null? Rückwärts denken.', art='K')
N.z('definitionsmenge', 3, 'Für welche Zahl a ist f(x) = 3/(2x − a) an der Stelle x = 1,5 nicht definiert?', 3, '2 * 1.5',
    'Nicht definiert heißt: Nenner 0. 2 · 1,5 − a = 0 ⇔ 3 − a = 0 ⇔ a = 3.', 'Setze x = 1,5 in den Nenner ein und verlange 0.', art='K')

# asymptoten
N.z('asymptoten', 2, 'Gib die senkrechte Asymptote von f(x) = 3/(x + 2,5) − 1 an. x = □', -2.5, '-2.5', 'Senkrechte Asymptote bei x = −b = −2,5.', 'Wo wird der Nenner 0?')
N.z('asymptoten', 2, 'Gib die waagrechte Asymptote von f(x) = 5/x an. y = □', 0, '0', 'Es wird nichts addiert: c = 0. Die waagrechte Asymptote ist die x-Achse, y = 0. Die 5 ist kein c.',
    'Welche Zahl wird hinter dem Bruch addiert?')
N.l('asymptoten', 3, 'Der Graph gehört zu f(x) = a/(x − b) + c und geht durch den Punkt P. Lies die Asymptoten ab und bestimme den Term.', 'f(x) = □/(x − □) + □', [3, 1, 2],
    ['5 - 2', '1', '2'], 'Asymptoten: x = 1 und y = 2, also f(x) = a/(x − 1) + 2. P(2 | 5) einsetzen: 5 = a/1 + 2 ⇔ a = 3.',
    'Lies erst die beiden Asymptoten ab. a bekommst du durch Einsetzen von P.', 'Je Lücke eine ganze Zahl.',
    grafik=_k(x=[-4, 6], y=[-3, 8], graphen=[_h(3, -1, 2)], senkrecht=[1], waagrecht=[2], punkte=[{'x': 2, 'y': 5, 'name': 'P'}]), art='P')
N.z('asymptoten', 3, 'An welcher Stelle x schneidet die Gerade y = 2 den Graphen von f(x) = 4/(x − 1) + 3?', -3, '1 + 4 / (2 - 3)',
    '4/(x − 1) + 3 = 2 ⇔ 4/(x − 1) = −1 ⇔ x − 1 = −4 ⇔ x = −3. Probe: 4/(−4) + 3 = 2.', 'Setze f(x) = 2 und löse nach x auf.', art='P')
N.a('asymptoten', 3, 'Kann der Graph von f(x) = a/(x + b) + c (mit a ≠ 0) die Gerade y = c schneiden?', 'Nein: a/(x + b) ist nie 0, also ist f(x) nie gleich c.',
    ['Ja: genau an der Stelle x = −b.', 'Ja: wenn x groß genug ist.', 'Nur wenn c = 0 ist.'],
    'f(x) = c würde bedeuten a/(x + b) = 0. Ein Bruch ist nur 0, wenn der Zähler 0 ist – a ist aber nicht 0. Darum berührt der Graph die Asymptote nie.',
    'Was müsste für a/(x + b) gelten, damit f(x) = c ist?', art='K')
N.z('asymptoten', 3, 'Eine Hyperbel f(x) = a/(x + b) + c hat die Asymptoten x = −2 und y = 1 und geht durch den Ursprung. Bestimme a.', -2, '-1 * 2',
    'b = 2 und c = 1: f(x) = a/(x + 2) + 1. f(0) = 0 ⇔ a/2 + 1 = 0 ⇔ a = −2.', 'Setze zuerst b und c ein. Dann nutze den Punkt (0 | 0).', art='K')

# achsenpunkte
N.z('achsenpunkte', 2, 'In welchem Punkt schneidet der Graph von f(x) = 6/(x − 3) + 4 die y-Achse? Gib den y-Wert an.', 2, '6 / (0 - 3) + 4', 'f(0) = 6/(−3) + 4 = −2 + 4 = 2.',
    'Setze x = 0 ein.')
N.z('achsenpunkte', 2, 'Berechne die Nullstelle von f(x) = 3/(x + 1) + 1,5.', -3, '3 / (-1.5) - 1', '3/(x + 1) = −1,5 ⇔ x + 1 = 3 : (−1,5) = −2 ⇔ x = −3.',
    'Bringe 1,5 auf die andere Seite. Dann multipliziere mit dem Nenner.')
N.l('achsenpunkte', 3, 'Bestimme beide Achsenschnittpunkte des Graphen von f(x) = 2/(x − 1) + 1.', 'N(□ | 0); S(0 | □)', [-1, -1], ['1 + 2 / (-1)', '2 / (0 - 1) + 1'],
    'Nullstelle: 2/(x − 1) = −1 ⇔ x − 1 = −2 ⇔ x = −1. y-Achse: f(0) = 2/(−1) + 1 = −1. N(−1 | 0), S(0 | −1).',
    'Für N setzt du f(x) = 0, für S setzt du x = 0.', 'Je Lücke eine ganze Zahl.', art='P')
N.a('achsenpunkte', 3, 'Welche Funktion hat KEINE Nullstelle?', 'f(x) = 3/(x − 2)', ['f(x) = 3/(x − 2) + 1', 'f(x) = −3/x + 2', 'f(x) = 1/(x + 4) − 1'],
    'Ohne +c ist f(x) = 3/(x − 2) nie 0 (der Zähler ist 3). Die anderen haben Nullstellen: −1, 1,5 und −3.', 'Ein Bruch ist nur 0, wenn sein Zähler 0 ist.', art='P')
N.z('achsenpunkte', 3, 'Für welchen Wert von c hat f(x) = 4/(x − 2) + c die Nullstelle x = 4?', -2, '-(4 / (4 - 2))', 'f(4) = 4/2 + c = 2 + c = 0 ⇔ c = −2.',
    'Setze x = 4 ein und verlange f(4) = 0.', art='K')
N.a('achsenpunkte', 3, 'Für welche Werte von c schneidet der Graph von f(x) = 2/x + c die y-Achse?', 'für keinen Wert von c', ['nur für c = 0', 'für jeden Wert von c', 'nur für c = 2'],
    'Die y-Achse ist die Stelle x = 0. Dort ist 2/x nicht definiert – egal, wie groß c ist. Der Graph schneidet die y-Achse nie.',
    'Welches x hat die y-Achse? Darf man es einsetzen?', art='K')

# parameter
N.a('parameter', 2, 'Der Graph von g(x) = 2/x wird um 3 nach unten verschoben. Wie heißt der neue Term?', 'f(x) = 2/x − 3', ['f(x) = 2/(x − 3)', 'f(x) = 2/(x + 3)', 'f(x) = 2/x + 3'],
    'Nach unten heißt: Von jedem Funktionswert 3 abziehen: f(x) = 2/x − 3.', 'Oben/unten ändert c, links/rechts ändert b.')
N.a('parameter', 2, 'Wie entsteht der Graph von f(x) = 5/(x + 1) aus dem Graphen von g(x) = 5/x?', 'Verschiebung um 1 nach links', ['Verschiebung um 1 nach rechts',
    'Verschiebung um 1 nach oben', 'Verschiebung um 1 nach unten'],
    'Die Lücke liegt jetzt bei x = −1 statt bei 0: um 1 nach links verschoben.', 'Wo liegt die senkrechte Asymptote jetzt?')
N.a('parameter', 3, 'Lies die Asymptoten der gezeichneten Hyperbel ab. Welcher Term gehört zu ihr?', 'f(x) = 1/(x − 2) − 1', ['f(x) = 1/(x + 2) − 1', 'f(x) = 1/(x − 2) + 1', 'f(x) = −1/(x − 2) − 1'],
    'Senkrechte Asymptote x = 2: Nenner x − 2. Waagrechte Asymptote y = −1: − 1. Der Graph liegt rechts oben und links unten wie bei 1/x: Zähler positiv.',
    'Lies beide Asymptoten ab. Liegen die Äste wie bei 1/x oder wie bei −1/x?',
    grafik=_k(x=[-3, 7], y=[-5, 3], graphen=[_h(1, -2, -1)], senkrecht=[2], waagrecht=[-1]), art='P')
N.a('parameter', 3, 'Der Graph von f(x) = 3/(x − 1) + 2 wird um 4 nach links und um 5 nach unten verschoben. Wie heißt der neue Term?', 'g(x) = 3/(x + 3) − 3',
    ['g(x) = 3/(x − 5) − 3', 'g(x) = 3/(x + 4) − 5', 'g(x) = 3/(x + 3) + 7'],
    'Senkrechte Asymptote: von x = 1 um 4 nach links zu x = −3, also Nenner x + 3. Waagrechte: von y = 2 um 5 nach unten zu y = −3.',
    'Verschiebe die Asymptoten. Sie bestimmen den neuen Term.', art='P')
N.l('parameter', 3, 'Der Graph von f(x) = a/(x + b) + c ist punktsymmetrisch zum Punkt Z(−2 | 3). Bestimme b und c.', 'b = □; c = □', [2, 3], ['2', '3'],
    'Eine Hyperbel ist punktsymmetrisch zum Schnittpunkt ihrer Asymptoten. Also x = −2 (b = 2) und y = 3 (c = 3).',
    'Welcher Punkt ist bei 1/x das Symmetriezentrum? Wohin wandert er beim Verschieben?', 'Je Lücke eine ganze Zahl.', art='K')
N.a('parameter', 3, 'Der Graph von g(x) = 4/x wird an der x-Achse gespiegelt. Welche Funktion gehört zum neuen Graphen?', 'f(x) = −4/x', ['f(x) = 4/x − 4', 'f(x) = 4/(x − 4)', 'f(x) = 1/(4x)'],
    'Beim Spiegeln an der x-Achse wechselt jeder Funktionswert das Vorzeichen: aus 4/x wird −4/x. Die Äste liegen dann im 2. und 4. Feld.',
    'Was passiert beim Spiegeln an der x-Achse mit dem Punkt (1 | 4)?', art='K')

# beurteilen
N.a('beurteilen', 2, 'Welche Aussage über f(x) = 2/x ist richtig?', 'Wird x verdoppelt, so halbiert sich f(x).', ['Der Graph geht durch (0 | 2).', 'f(x) ist nie negativ.',
                                                                                                     'f(−1) = 2'],
    'f(2x) = 2/(2x) = (2/x) : 2. Doppeltes x, halbes f(x). Für x = 0 gibt es keinen Wert, f(−1) = −2 ist negativ.', 'Teste jede Aussage mit einer Zahl.')
N.a('beurteilen', 2, 'Welche Aussage über f(x) = −1/(x + 2) + 3 ist FALSCH?', 'Die senkrechte Asymptote ist x = 2.', ['f ist für x = −2 nicht definiert.', 'f(−1) = 2',
                                                                                                         'Der Graph schneidet die Gerade y = 3 nie.'],
    'Senkrechte Asymptote: x + 2 = 0 ⇔ x = −2, nicht 2. f(−1) = −1/1 + 3 = 2 stimmt. y = 3 ist Asymptote und wird nie erreicht.', 'Prüfe jede Aussage einzeln.')
N.a('beurteilen', 3, 'Ben sagt: „Der Graph von f(x) = 1/x fällt. Also ist f(−1) größer als f(1).“ Was stimmt?',
    'Falsch: f(−1) = −1 ist kleiner als f(1) = 1. Der Graph fällt nur in jedem Ast für sich.',
    ['Richtig: Fallende Graphen haben links größere Werte.', 'Richtig: f(−1) = 1 und f(1) = −1.', 'Falsch: Der Graph von 1/x steigt.'],
    'f(−1) = −1 und f(1) = 1. Links der Lücke sind alle Werte negativ, rechts positiv. „Fällt“ gilt nur innerhalb jedes Astes, nicht über die Lücke bei x = 0 hinweg.',
    'Rechne f(−1) und f(1) wirklich aus.', art='P')
N.a('beurteilen', 3, 'Ina behauptet: „Für sehr große x liegen die Werte von f(x) = 6/(x − 1) + 2 ganz nahe bei 2.“ Was stimmt?',
    'Richtig: 6/(x − 1) wird für große x fast 0.', ['Falsch: Sie liegen nahe bei 6.', 'Falsch: Sie werden immer größer.', 'Richtig: f(2) = 2.'],
    'Für x = 1 001 ist 6/(x − 1) = 0,006. Der Bruch wird immer kleiner, f(x) nähert sich 2 – der waagrechten Asymptote. f(2) = 8, nicht 2.',
    'Setze eine große Zahl ein, z. B. x = 1 001.', art='P')
N.a('beurteilen', 3, 'Wie viele Schnittpunkte haben der Graph von f(x) = 6/x und die Gerade y = x + 1?', 'zwei', ['keinen', 'einen', 'drei'],
    'Probieren: x = 2 gibt 6/2 = 3 und 2 + 1 = 3. x = −3 gibt 6/(−3) = −2 und −3 + 1 = −2. Zwei Schnittpunkte: (2 | 3) und (−3 | −2). Die Gerade schneidet jeden Ast einmal.',
    'Skizziere beide Graphen. Probiere dann ganze Zahlen als x.', art='K')
N.a('beurteilen', 3, 'Welcher Punkt kann auf KEINEM Graphen einer Funktion f(x) = a/x mit a > 0 liegen?', 'P(−2 | 3)', ['P(2 | 3)', 'P(−2 | −3)', 'P(0,5 | 12)'],
    'Für a > 0 haben x und f(x) immer dasselbe Vorzeichen (Äste im 1. und 3. Feld). P(−2 | 3) hat verschiedene Vorzeichen. Die anderen passen zu a = 6.',
    'Welche Vorzeichen haben x und y, wenn a positiv ist?', art='K')

baue = mit_schwer(baue, N)
# ---- SCHWER ENDE ----

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, mit_befunden  # noqa: E402

BF = Befunde('funktionen.gebrochen', 13_8_3)
# a) direkt ablesen → Stufe 1
BF.stufe('asymptoten', 'Gib die waagrechte Asymptote von f(x) = −9/(x − 8) + 2 an. y = □', 1)
BF.stufe('asymptoten', 'Gib die waagrechte Asymptote von f(x) = 1/(x + 5) − 3 an. y = □', 1)
# a) gleicher Typ wie Stufe 2
BF.stufe('achsenpunkte', 'Welche Nullstelle hat f(x) = 3/(x − 4)?', 2)
BF.stufe('achsenpunkte', 'Welche Nullstelle hat f(x) = −7/(x + 3)?', 2)
BF.stufe('parameter', 'Wie unterscheidet sich der Graph von f(x) = −3/x vom Graphen von g(x) = 3/x?', 2)
BF.nicht_umgesetzt('indirekt: Überschneidung mit groessen.indirekt', 'Kein Mangel an einer Aufgabe; betrifft die Reihenfolge im Plan (Haupt-Chat).')

baue = mit_befunden(baue, BF)
# ---- BEFUNDE ENDE ----

# ---- LÜCKEN (Achtzehnte Runde, Teil B: neue Lernkarte „indirekt_sach“ nach „indirekt“, siehe _luecken_kl8.py) ----
# LehrplanPLUS M8 3: Spezialfall y = a/x als indirekt proportionale Zuordnung zweier Größen, auch in naturwissenschaftlichen Kontexten
# (ISB, Schwerpunktsetzungen Jgst. 8). Sachaufgaben mit Produktgleichheit und Dreisatz „umgekehrt“.
# Vorbilder (Typ und Niveau, nicht Wortlaut/Zahlen): BMT8 (Fahrzeit bei geringerer Geschwindigkeit, Verspätung), Grundwissen 8 (Vorrat/Arbeiter/Pumpen,
# Boyle-Mariotte als Physik-Beispiel), RS-Jahrgangsstufentest 8 (direkt, indirekt oder keins von beiden erkennen).
import collections  # noqa: E402

from _bausatz import eur  # noqa: E402
from _luecken_kl8 import K as _K, P as _P, Luecken, mit_luecken  # noqa: E402

LK = Luecken('funktionen.gebrochen', 18_8_3)
_LZ = 'indirekt_sach'
_TAB = lambda kopf, zeile: {'typ': 'tabelle', 'kopf': kopf, 'zeilen': [zeile]}

_KARTE = {
    'lernziel': _LZ, 'titel': 'Sachaufgaben: umgekehrter Dreisatz',
    'einstieg': 'Ein Reisebus für die Klassenfahrt kostet zusammen 960 €. Fahren 24 Kinder mit, zahlt jedes 40 €. '
                'Fahren mehr mit, zahlt jedes weniger. Die Rechnung dafür heißt ⟦umgekehrter Dreisatz⟧.',
    'woerter': [['umgekehrter Dreisatz', 'Dreisatz über die 1, bei dem man erst malnimmt und dann teilt'],
                ['Gesamtpreis', 'was alle zusammen zahlen; er bleibt gleich, egal wie viele mitfahren']],
    'bild': _TAB(['Kinder', '24', '1', '30'], ['€ je Kind', '40', '?', '?']),
    'schritte': [{'text': 'Das Produkt bleibt gleich: 24 · 40 € = 960 € Gesamtpreis.', 'bild': _TAB(['Kinder', '24', '1', '30'], ['€ je Kind', '40', '960', '?'])},
                 {'text': 'Ein Kind allein müsste alles zahlen: 960 €. Hier wird mal 24 gerechnet.'},
                 {'text': 'Bei 30 Kindern teilen sich alle die 960 €: je ⟦32 €⟧.', 'bild': _TAB(['Kinder', '24', '1', '30'], ['€ je Kind', '40', '960', '32'])}],
    'probe': '30 · 32 € = 960 € ✓',
    'fehler': 'Nicht wie beim normalen Dreisatz rechnen. 40 € : 24 · 30 = 50 € wäre mehr je Kind, obwohl mehr mitfahren.',
    'fehler_bild': _TAB(['Kinder', '24', '30'], ['€ je Kind', '40', '50 ✗ (richtig: 32)']),
    'regel': 'Bei „je mehr, desto weniger“: erst malnehmen, dann teilen. Prüfe vorher, ob das ⟦Produkt⟧ wirklich gleich bleibt.',
}
_W = collections.Counter()


def _wahl(R, st, arten):
    n = min(_W[(st, a)] for a in arten)
    a = R.choice([x for x in arten if _W[(st, x)] == n])
    _W[(st, a)] += 1
    return a


def _teiler(n, lo, hi):
    return [d for d in range(lo, hi + 1) if n % d == 0]


# Zuordnungen zum Erkennen: (Text, Art)
_ERKENNEN = [('Anzahl gleicher Brötchen → Gesamtpreis', 'direkt proportional'), ('Anzahl gleicher Pumpen → Zeit, bis ein Becken leer ist', 'indirekt proportional'),
             ('Alter eines Kindes → Körpergröße', 'weder noch'), ('Geschwindigkeit → Fahrzeit für dieselbe Strecke', 'indirekt proportional'),
             ('Zahl der Gäste → Stücke je Gast bei einem Blech Kuchen', 'indirekt proportional'), ('getankte Liter → Preis an der Zapfsäule', 'direkt proportional'),
             ('gefahrene Kilometer → Taxipreis mit 4 € Grundgebühr', 'weder noch'), ('Breite eines Rechtecks → Länge bei 24 cm² Fläche', 'indirekt proportional'),
             ('Zahl der Zähne eines Zahnrads → Umdrehungen beim Mitdrehen eines festen Rads', 'indirekt proportional'),
             ('Seitenlänge eines Quadrats → Flächeninhalt', 'weder noch'), ('Arbeitsstunden → Lohn bei festem Stundenlohn', 'direkt proportional')]


def g_indirekt_sach(R, st):
    if st == 1:
        art = _wahl(R, 1, ['teilen', 'vorrat', 'fahrt'])
        if art == 'teilen':
            gesamt = R.choice([360, 480, 600, 720, 840, 960, 1080, 1200])
            n1, n2 = R.sample(_teiler(gesamt, 10, 40), 2)
            t = f'Ein Ausflug kostet zusammen {zt(gesamt)} €. Bei {n1} Teilnehmern zahlt jeder {zt(gesamt // n1)} €. Wie viel zahlt jeder bei {n2} Teilnehmern?'
            return Z(t, Fr(gesamt, n2), f'{n1} * {gesamt // n1} / {n2}', f'Gesamtpreis {n1} · {zt(gesamt // n1)} € = {zt(gesamt)} €. Geteilt durch {n2}: {zt(Fr(gesamt, n2))} €.',
                     'Rechne zuerst den Gesamtpreis aus. Er bleibt gleich.', einheit='€')
        if art == 'vorrat':
            tiere, tage = R.choice([(4, 30), (6, 20), (5, 24), (8, 15), (3, 40), (10, 12), (12, 10)])
            k = tiere * tage
            neu = R.choice([d for d in _teiler(k, 2, 20) if d != tiere])
            return Z(f'Ein Futtervorrat reicht für {tiere} Pferde {tage} Tage. Wie viele Tage reicht er für {neu} Pferde?', Fr(k, neu), f'{tiere} * {tage} / {neu}',
                     f'Der Vorrat reicht für {tiere} · {tage} = {k} Pferdetage. {k} : {neu} = {zt(Fr(k, neu))} Tage.', 'Wie viele Tage würde er für 1 Pferd reichen?', einheit='Tage')
        v1 = R.choice([40, 50, 60, 80, 90, 100, 120])
        t1 = R.choice([2, 3, 4, 5, 6])
        s = v1 * t1
        v2 = R.choice([v for v in (30, 40, 45, 50, 60, 75, 80, 90, 100, 120, 150) if v != v1 and Fr(s, v).denominator in (1, 2, 4)])
        return Z(f'Mit {v1} km/h dauert eine Fahrt {t1} h. Wie viele Stunden dauert sie mit {v2} km/h?', Fr(s, v2), f'{v1} * {t1} / {v2}',
                 f'Die Strecke ist {v1} · {t1} = {s} km. {s} : {v2} = {zt(Fr(s, v2))} h.', 'Berechne zuerst die Strecke. Sie bleibt gleich.', einheit='h')
    if st == 2:
        art = _wahl(R, 2, ['erkennen', 'zahnrad', 'rechteck', 'tabelle'])
        if art == 'erkennen':
            text, richtig = R.choice(_ERKENNEN)
            grund = {'direkt proportional': 'Doppelt so viel Eingabe ergibt doppelt so viel Ausgabe; der Quotient bleibt gleich.',
                     'indirekt proportional': 'Doppelt so viel Eingabe ergibt halb so viel Ausgabe; das Produkt bleibt gleich.',
                     'weder noch': 'Weder der Quotient noch das Produkt bleibt gleich. Verdoppeln führt weder zum Doppelten noch zur Hälfte.'}[richtig]
            return LK.A(f'Wie ist die Zuordnung „{text}“?', richtig, [x for x in ['direkt proportional', 'indirekt proportional', 'weder noch'] if x != richtig],
                        f'{grund} Also: {richtig}.', 'Was passiert, wenn du die erste Größe verdoppelst?')
        if art == 'zahnrad':
            za, ua = R.choice([(24, 10), (36, 8), (30, 12), (48, 5), (40, 9), (20, 18)])
            k = za * ua
            zb = R.choice([z for z in (12, 15, 16, 18, 20, 24, 30, 36, 40, 45, 60) if z != za and k % z == 0])
            return Z(f'Zwei Zahnräder greifen ineinander. Rad A hat {za} Zähne und dreht sich {ua}-mal. Rad B hat {zb} Zähne. Wie oft dreht sich Rad B?', Fr(k, zb), f'{za} * {ua} / {zb}',
                     f'Es greifen gleich viele Zähne ineinander: {za} · {ua} = {k} Zähne. Rad B: {k} : {zb} = {zt(Fr(k, zb))} Umdrehungen.',
                     'Wie viele Zähne laufen insgesamt am Berührpunkt vorbei? Diese Zahl ist für beide Räder gleich.')
        if art == 'rechteck':
            f = R.choice([24, 36, 48, 60, 72, 90, 120])
            a1, a2 = R.sample(_teiler(f, 2, 15), 2)
            return Z(f'Ein Beet soll {f} m² groß sein. Ist es {a1} m breit, wird es {zt(Fr(f, a1))} m lang. Wie lang wird es bei {a2} m Breite?', Fr(f, a2), f'{a1} * {f // a1} / {a2}',
                     f'Breite · Länge = {f} m² bleibt gleich. {f} : {a2} = {zt(Fr(f, a2))} m.', 'Die Fläche ist das Produkt aus Breite und Länge.', einheit='m')
        k = R.choice([36, 48, 60, 72, 120])
        xs = R.sample(_teiler(k, 2, 12), 3)
        i = R.randrange(3)
        kopf = ['Pumpen'] + [str(x) for x in xs]
        zeile = ['Stunden'] + [zt(Fr(k, x)) if j != i else '?' for j, x in enumerate(xs)]
        t = 'Gleiche Pumpen leeren ein Becken. Ergänze die Tabelle: Wie viele Stunden brauchen die Pumpen an der Stelle „?“'
        j = (i + 1) % 3
        return Z(t, Fr(k, xs[i]), f'{xs[j]} * {cz(Fr(k, xs[j]))} / {xs[i]}',
                 f'Produkt aus einer vollen Spalte: {xs[j]} · {zt(Fr(k, xs[j]))} = {k} Pumpenstunden. {k} : {xs[i]} = {zt(Fr(k, xs[i]))} h.',
                 'Nimm eine vollständige Spalte und bilde das Produkt.', einheit='h') | {'f': {'text': t, 'grafik': _TAB(kopf, zeile)}}
    art = _wahl(R, 3, ['ausfall', 'doppel', 'weniger_tiere', 'verspaetung'])
    if art == 'ausfall':
        while True:
            n, h = R.choice([(6, 10), (5, 12), (8, 9), (4, 15), (10, 6), (6, 8)])
            k = n * h
            nach = R.randint(1, h - 2)
            aus = R.choice([1, 2])
            rest = k - n * nach
            if rest % (n - aus) == 0: break
        gesamt = nach + rest // (n - aus)
        return Z(f'{n} gleiche Pumpen leeren ein Becken in {h} h. Nach {nach} h {"fallen" if aus > 1 else "fällt"} {aus} Pumpe{"n" if aus > 1 else ""} aus. Wie viele Stunden dauert das Leeren insgesamt?',
                 gesamt, f'{nach} + ({n} * {h} - {n} * {nach}) / ({n} - {aus})',
                 f'Arbeit: {n} · {h} = {k} Pumpenstunden. Nach {nach} h sind {n * nach} erledigt, {rest} bleiben. {n - aus} Pumpen brauchen dafür {rest} : {n - aus} = {rest // (n - aus)} h. '
                 f'Insgesamt {nach} + {rest // (n - aus)} = {gesamt} h.', 'Rechne in Pumpenstunden: Wie viel ist schon geschafft, wie viel bleibt?', einheit='h')
    if art == 'doppel':
        n1, h1, m1 = R.choice([(4, 6, 120), (3, 5, 90), (5, 4, 100), (6, 3, 72), (2, 9, 108)])
        je = Fr(m1, n1 * h1)
        n2 = R.choice([x for x in (2, 3, 4, 5, 6, 8) if x != n1])
        m2 = R.choice([m for m in range(30, 181, 6) if Fr(m, n2 * je).denominator in (1, 2) and m != m1])
        return Z(f'{n1} gleiche Pumpen fördern in {h1} h zusammen {m1} m³ Wasser. Wie viele Stunden brauchen {n2} Pumpen für {m2} m³?', Fr(m2, n2 * je),
                 f'{m2} / ({n2} * {m1} / ({n1} * {h1}))',
                 f'Eine Pumpe schafft in 1 h {m1} : ({n1} · {h1}) = {zt(je)} m³. {n2} Pumpen schaffen {zt(n2 * je)} m³ pro Stunde. {m2} : {zt(n2 * je)} = {zt(Fr(m2, n2 * je))} h.',
                 'Rechne zuerst aus, wie viel 1 Pumpe in 1 Stunde schafft.', einheit='h')
    if art == 'weniger_tiere':
        while True:
            tiere, tage = R.choice([(12, 30), (10, 24), (8, 45), (15, 20), (20, 18)])
            nach = R.randint(2, tage // 2)
            weg = R.choice([2, 3, 4, 5])
            rest = tiere * (tage - nach)
            if rest % (tiere - weg) == 0: break
        return Z(f'Ein Futtervorrat reicht für {tiere} Schafe {tage} Tage. Nach {nach} Tagen werden {weg} Schafe verkauft. Wie viele Tage reicht der Rest noch?', Fr(rest, tiere - weg),
                 f'{tiere} * ({tage} - {nach}) / ({tiere} - {weg})',
                 f'Nach {nach} Tagen reicht der Rest für {tiere} Schafe noch {tage - nach} Tage, das sind {rest} Schaftage. Für {tiere - weg} Schafe: {rest} : {tiere - weg} = {zt(Fr(rest, tiere - weg))} Tage.',
                 'Wie viele Tage würde der Rest für die ursprüngliche Herde noch reichen?', einheit='Tage')
    v1, t1 = R.choice([(90, 2), (100, 3), (80, Fr(3, 2)), (150, 2), (120, 3), (100, Fr(3, 2))])
    s = v1 * t1
    v2 = R.choice([v for v in (60, 75, 80, 90, 100, 120) if v < v1 and (Fr(s, v) * 60).denominator == 1])
    d = (Fr(s, v2) - t1) * 60
    return Z(f'Ein Zug fährt eine Strecke normalerweise mit {v1} km/h in {zt(t1)} h. Wegen Bauarbeiten fährt er nur {v2} km/h. Wie viele Minuten braucht er länger?', d,
             f'({v1} * {cz(t1)} / {v2} - {cz(t1)}) * 60',
             f'Strecke {v1} · {zt(t1)} = {zt(s)} km. Neue Fahrzeit {zt(s)} : {v2} = {zt(Fr(s, v2))} h. Unterschied {zt(Fr(s, v2) - t1)} h = {zt(d)} min.',
             'Berechne zuerst die Strecke, dann die neue Fahrzeit.', einheit='min')


_FEST = [
    lambda: Z('Für eine eingeschlossene Luftmenge gilt bei gleicher Temperatur: Druck · Volumen bleibt gleich. Bei 2 bar nimmt sie 6 l ein. Welches Volumen hat sie bei 3 bar?',
              4, '2 * 6 / 3', 'Produkt: 2 bar · 6 l = 12. Bei 3 bar: 12 : 3 = 4 l. Mehr Druck, weniger Volumen.', 'Das Produkt aus Druck und Volumen bleibt gleich.', einheit='l') | {'_art': _P},
    lambda: Z('Ein Zug fährt 300 km mit 120 km/h. Wegen einer Baustelle darf er auf der ganzen Strecke nur 100 km/h fahren. Wie viele Minuten Verspätung hat er?', 30,
              '(300 / 100 - 300 / 120) * 60', 'Geplant: 300 : 120 = 2,5 h. Jetzt: 300 : 100 = 3 h. Unterschied 0,5 h = 30 min.',
              'Berechne beide Fahrzeiten für dieselbe Strecke.', einheit='min') | {'_art': _P},
    lambda: Z('x und y sind indirekt proportional. Wird x um 2 größer, halbiert sich y. Wie groß war x?', 2, '2',
              'Das Produkt bleibt gleich: (x + 2) · y/2 = x · y. Also (x + 2) : 2 = x, das heißt x + 2 = 2x und x = 2. Probe: 2 · y = 4 · y/2 ✓',
              'Halbiert sich y, muss sich x verdoppeln. Welche Zahl verdoppelt sich, wenn man 2 dazuzählt?') | {'_art': _K},
]
LK.karte(_KARTE, nach='indirekt', abschnitt='Indirekte Proportionalität', gen=g_indirekt_sach, fest=_FEST)
baue = mit_luecken(baue, LK)
# ---- LÜCKEN ENDE ----


# ---- DURCHSICHT (Neunzehnte Runde, Teil A: Gesamtdurchsicht Kl. 8, siehe _durchsicht_kl8.py) ----
from _durchsicht_kl8 import Durchsicht, mit_durchsicht  # noqa: E402

DSX = Durchsicht('funktionen.gebrochen', 19_8_6)
for _t in ['Wie ist die Zuordnung (3 | 8), (8 | 3), (12 | 2)?', 'Wie ist die Zuordnung (3 | 6), (6 | 12), (9 | 18)?',
           'Wie ist die Zuordnung (2 | 15), (3 | 13), (5 | 12)?', 'Wie ist die Zuordnung (1 | 18), (2 | 16), (3 | 15)?']:
    DSX.stufe('indirekt', _t, 2)
DSX.stufen('indirekt', 'S1 Dreisatz umgekehrt; S2 Fehler, Fahrzeit, Tabelle; S3 viermal Zuordnung einordnen',
           'S1 Dreisatz umgekehrt; S2 Fehler, Fahrzeit, Tabelle, Zuordnung einordnen; S3 Wippe, Rechteck unter der Hyperbel, Prozent, Arbeiter kommen dazu')
# definitionsmenge: D von a/(x ± b) + c auf allen Stufen derselbe Gedanke
for _t in ['Gib die Definitionsmenge von f(x) = 7/(x + 2) − 1 an.', 'Gib die Definitionsmenge von f(x) = −4/(x + 5) + 3 an.', 'Gib die Definitionsmenge von f(x) = −4/(x − 1) an.',
           'Welche Zahl gehört nicht zur Definitionsmenge von f(x) = 6/(x − 3) − 2?', 'Welche Zahl gehört nicht zur Definitionsmenge von f(x) = −8/(x − 2) − 1?',
           'Welche Zahl gehört nicht zur Definitionsmenge von f(x) = −2/(x − 5) + 6?']:
    DSX.stufe('definitionsmenge', _t, 1)
for _t in ['Welche Zahl gehört nicht zur Definitionsmenge von f(x) = −4/(2x − 3) − 3?', 'Welche Zahl gehört nicht zur Definitionsmenge von f(x) = −7/(5x − 2) + 1?',
           'Welche Zahl gehört nicht zur Definitionsmenge von f(x) = 3/(5x + 6) − 5?', 'Welche Zahl gehört nicht zur Definitionsmenge von f(x) = −1/(4x + 2) − 1?']:
    DSX.stufe('definitionsmenge', _t, 2)
DSX.stufen('definitionsmenge', 'S1 und S2 dieselbe Aufgabe x ± b; S3 viermal Nenner ax + b (nur etwas längere Rechnung)',
           'S1 Nenner x ± b; S2 Nenner 3 − x, ax + b, Dezimalzahl; S3 zwei Brüche, aus dem Graphen, Parameter b und a')
# asymptoten: Stufe 1 und 2 waren dieselbe Ablese-Aufgabe
for _t in ['Gib die waagrechte Asymptote von f(x) = −6/(x + 3) − 6 an. y = □', 'Gib die waagrechte Asymptote von f(x) = 1/(x + 8) + 3 an. y = □',
           'Gib die senkrechte Asymptote von f(x) = 3/(x − 2) + 5 an. x = □', 'Gib die senkrechte Asymptote von f(x) = −2/(x − 7) + 5 an. x = □',
           'Gib die waagrechte Asymptote von f(x) = −5/(x − 4) − 3 an. y = □', 'Gib die waagrechte Asymptote von f(x) = −5/(x + 1) − 4 an. y = □']:
    DSX.stufe('asymptoten', _t, 1)
DSX.stufe('asymptoten', 'Lies die Asymptoten der Hyperbel ab.', 2, enthaelt='"werte": [3, 0]')
DSX.neu('asymptoten', 2, DSX.L('Gib beide Asymptoten von f(x) = −2/(5 + x) + 1 an.', 'x = □; y = □', [-5, 1], ['-5', '1'],
                               'Umsortieren: 5 + x = x + 5, also b = 5. Senkrechte Asymptote x = −5, waagrechte y = 1.', 'Schreibe den Nenner als x + b.'))
DSX.neu('asymptoten', 2, DSX.L('Gib beide Asymptoten von f(x) = 4/x − 3 an.', 'x = □; y = □', [0, -3], ['0', '-3'],
                               'Der Nenner ist x, also b = 0: senkrechte Asymptote x = 0 (die y-Achse). Die Verschiebung −3 gibt y = −3.', 'Wo wird der Nenner 0? Was bleibt für große x?'))
DSX.stufen('asymptoten', 'S1 und S2 dieselbe Aufgabe „Asymptote ablesen“; S3 Term aus Asymptoten, Graph',
           'S1 eine Asymptote aus dem Term; S2 umsortierter Nenner, b = 0, aus dem Graphen; S3 Term aus Asymptoten und Punkt, Schnitt mit y = c, Parameter a')
DSX.stufe('achsenpunkte', 'Berechne die Nullstelle von f(x) = −6/(x + 1) − 1.', 2)
DSX.stufe('achsenpunkte', 'Berechne die Nullstelle von f(x) = 4/(x − 5) − 1.', 2)
DSX.stufen('achsenpunkte', 'S1 y-Achse; S2 Nullstelle; S3 teils dieselbe Nullstelle',
           'S1 Schnitt mit der y-Achse; S2 Nullstelle, Sonderfälle (keine, x = 0 nicht in D); S3 beide Punkte, Funktion ohne Nullstelle, Parameter c')
for _t in ['Der Graph von g(x) = 3/x wird um 5 nach rechts und um 2 nach oben verschoben. Wie heißt der neue Funktionsterm?',
           'Der Graph von g(x) = 6/x wird um 5 nach rechts und um 6 nach oben verschoben. Wie heißt der neue Funktionsterm?',
           'Der Graph von g(x) = 2/x wird um 4 nach links und um 5 nach oben verschoben. Wie heißt der neue Funktionsterm?']:
    DSX.stufe('parameter', _t, 2)
DSX.stufen('parameter', 'S1 nach oben/unten; S2 beide Richtungen; S3 dreimal nur umgekehrt (Term zur Verschiebung)',
           'S1 nach oben/unten; S2 beide Richtungen, auch rückwärts (Term zur Verschiebung), Streckung/Spiegelung erkennen; S3 Term aus dem Graphen, doppelt verschoben, Symmetriepunkt, Spiegelung')
for _t in ['Welche Aussage über f(x) = −3/(x + 4) − 1 ist FALSCH?', 'Welche Aussage über f(x) = 3/(x − 2) − 3 ist FALSCH?',
           'Welche Aussage über f(x) = −2/(x + 6) + 1 ist FALSCH?', 'Welche Aussage über f(x) = −1/(x − 6) − 5 ist FALSCH?']:
    DSX.stufe('beurteilen', _t, 2)
DSX.stufen('beurteilen', 'S1 richtige Aussage; S2 und S3 dieselbe „FALSCH“-Aufgabe',
           'S1 richtige Aussage; S2 falsche Aussage finden; S3 Fehlvorstellungen (fällt also kleiner), Grenzverhalten, Schnittpunkte durch Probieren, Punkt ausschließen')
DSX.stufen('indirekt_sach', 'S1 umgekehrter Dreisatz; S2 Art erkennen, Zahnräder, Tabelle; S3 Ausfall/Verkauf mitten im Vorgang, zwei Größen, Physik, Knobelaufgabe')
DSX.fuer_sebastian('funktionen.gebrochen/indirekt und indirekt_sach überschneiden sich mit dem Flug groessen.indirekt (siehe dort).')
baue = mit_durchsicht(baue, DSX)
# ---- DURCHSICHT ENDE ----

# ---- STUFEN (Zwanzigste Runde: echte Stufe 3 und Knobel-Bordkarten, siehe _stufen_kl8.py) ----
from _stufen_kl8 import Stufen, mit_stufen  # noqa: E402

ST = Stufen('funktionen.gebrochen', 20_8_9)
SA, SZ, SL = ST.A, ST.Z, ST.L
def T(lz, *regeln):
    for m, g in regeln: ST.typ(lz, m, g)

# --- indirekt ---
ST.leiter('indirekt', 'mit „doppelt so viele – halb so lange“ rechnen, direkte und indirekte Proportionalität erkennen',
          'Geschwindigkeit und Zeit, Tabelle ergänzen, x · y = konstant nutzen, Rechteckseite zur festen Fläche',
          'Wippe modellieren, Rechteck unter der Hyperbel, Prozent verknüpfen, Fehler (Pumpen) deuten, Graph begründen, Parameter, rückwärts zur Gruppengröße')
T('indirekt', (r'^Wie ist die Zuordnung', 'erkennen'), (r'^Jemand rechnet', 'fehler'), (r'km/h', 'einkleidung'), (r'^Die Tabelle', 'darstellung'),
  (r'x · y immer gleich', 'mehrschritt'), (r'Rechteck hat', 'umkehr'), (r'Wippe', 'transfer'), (r'Lotfußpunkte|25 %', 'verknuepfen'), (r'Arbeiter', 'pruefung'), (r'.', 'direkt'))
ST.neu('indirekt', 'begruenden', SA('Stimmt: „Der Graph einer indirekten Proportionalität ist eine fallende Gerade“?', 'Falsch: Er ist eine Kurve (Hyperbel), weil x · y gleich bleibt.',
    ['Richtig.', 'Richtig, aber nur für x > 0.', 'Falsch: Er ist eine steigende Gerade.'], 'Bei 1 ↦ 12, 2 ↦ 6, 3 ↦ 4 nimmt y erst um 6, dann um 2 ab – nicht gleichmäßig wie bei einer Geraden.', 'Rechne drei Werte von y = 12/x aus und vergleiche die Abnahmen.'))
ST.neu('indirekt', 'parameter', SZ('Für welche Zahl a ist die Zuordnung (2 | 9), (3 | 6), (a | 4) indirekt proportional?', 4.5, '18 / 4', 'x · y = 18 bei den ersten beiden Paaren. Also a · 4 = 18 ⇒ a = 4,5.', 'Welches Produkt ist bei den bekannten Paaren gleich?'))
ST.neu('indirekt', 'rueckwaerts', SZ('Ein Vorrat reicht für eine Gruppe 20 Tage. Kommen 5 Personen dazu, reicht er nur noch 16 Tage. Wie viele Personen waren es ursprünglich?', 20, '16 * 5 / (20 - 16)',
    'Personen · Tage bleibt gleich: 20n = 16(n + 5) ⇒ 4n = 80 ⇒ n = 20.', 'Das Produkt Personen · Tage ändert sich nicht.'))
ST.knobel('indirekt', SZ('Ein Vorrat reicht für 10 Tiere 30 Tage. Nach 6 Tagen kommen 2 Tiere dazu, nach weiteren 10 Tagen werden 4 Tiere abgegeben. Wie viele Tage reicht der Vorrat insgesamt?', 31, '6 + 10 + (300 - 60 - 120) / 8',
    'Der Vorrat sind 10 · 30 = 300 „Tiertage“. 6 Tage mit 10 Tieren: 60. 10 Tage mit 12 Tieren: 120. Rest 120 für 8 Tiere: 15 Tage. Insgesamt 6 + 10 + 15 = 31 Tage.',
    'Rechne mit „Tiertagen“ wie mit einer Menge, die verbraucht wird.'))
ST.knobel('indirekt', SZ('Zwei Zahnräder greifen ineinander: Rad A hat 24 Zähne, Rad B hat 18. Nach wie vielen Umdrehungen von A stehen beide zum ersten Mal wieder wie am Anfang?', 3, '72 / 24',
    'Es greifen gleich viele Zähne ineinander. Beide stehen wieder am Anfang, wenn die Zahl der durchgelaufenen Zähne ein Vielfaches von 24 und von 18 ist: kgV = 72. A dreht sich dann 3-mal, B 4-mal.',
    'Zähle die Zähne, die an der Berührstelle vorbeilaufen.'))

# --- indirekt_sach ---
ST.leiter('indirekt_sach', 'den umgekehrten Dreisatz in einer vertrauten Situation anwenden',
          'Zuordnungsart begründet wählen, Tabelle ergänzen, Zahnräder und Beete, gesuchte Anzahl statt gesuchter Zeit, Mindestanzahl',
          'Gasgesetz übertragen, Verspätung in Minuten verknüpfen, Parameter x, Mischaufgaben mit zwei Größen, Ausfall unterwegs wie in einer Prüfung')
T('indirekt_sach', (r'^Wie ist die Zuordnung', 'erkennen'), (r'Ergänze die Tabelle', 'darstellung'), (r'Zahnräder|Beet', 'einkleidung'), (r'Luftmenge|fördern in', 'transfer'),
  (r'Zug fährt', 'verknuepfen'), (r'Wird x um 2 größer', 'parameter'), (r'verkauft|fällt 1 Pumpe aus', 'pruefung'), (r'.', 'direkt'))
ST.neu('indirekt_sach', 'umkehr', SZ('Ein Vorrat reicht für 6 Pferde 20 Tage. Für wie viele Pferde reicht er 24 Tage?', 5, '6 * 20 / 24', '6 · 20 = 120 Pferdetage. 120 : 24 = 5 Pferde.', 'Gesucht ist diesmal die Anzahl der Pferde.'))
ST.neu('indirekt_sach', 'mehrschritt', SZ('4 gleiche Pumpen leeren ein Becken in 9 h. Wie viele Pumpen braucht man mindestens, um in höchstens 5 h fertig zu sein?', 8, '36 // 5 + 1',
    '4 · 9 = 36 Pumpenstunden. 36 : 5 = 7,2 – mit 7 Pumpen dauert es 5,1 h, also braucht man 8.', 'Runde passend: Reicht 7?'))
ST.knobel('indirekt_sach', SZ('3 gleiche Pumpen füllen ein Becken in 10 h. Nach 4 h fällt eine aus, nach weiteren 3 h kommt sie zurück und eine vierte dazu. Wie lange dauert das Füllen insgesamt?', 10, '4 + 3 + (30 - 12 - 6) / 4',
    'Arbeit: 3 · 10 = 30 Pumpenstunden. 4 h mit 3 Pumpen: 12. 3 h mit 2 Pumpen: 6. Rest 12 mit 4 Pumpen: 3 h. Insgesamt 4 + 3 + 3 = 10 h – zufällig wie geplant.',
    'Rechne mit Pumpenstunden.', einheit='h'))
ST.knobel('indirekt_sach', SZ('Fährt ein Bus 20 % schneller als sonst, spart er auf seiner Strecke 15 Minuten. Wie viele Minuten braucht er normalerweise?', 90, '15 / (1 - 1 / (12/10))',
    'Bei 1,2-facher Geschwindigkeit braucht er t : 1,2 = 5/6 · t. Ersparnis: t − 5/6 · t = t/6 = 15 ⇒ t = 90 Minuten.', 'Wie viel Zeit braucht man bei 1,2-facher Geschwindigkeit?', einheit='min'))

# --- definitionsmenge ---
ST.leiter('definitionsmenge', 'die Zahl ausschließen, bei der x + b null wird',
          'Nenner mit Faktor (2x − 3), Nenner 3 − x, Sachfunktion, Funktion zu einer Definitionsmenge finden, Graph lesen',
          'zwei Brüche verknüpfen, x² − 4, Fehler (Konstante mitgezählt), begründen, Parameter b und a, Party-Modell, Vergleich zweier Funktionen')
T('definitionsmenge', (r'^Gib die Definitionsmenge von f\(x\) = −?\d+/\(x [−+] \d+\)( [−+] \d+)? an', 'direkt'), (r'^Welche Zahl gehört nicht zur Definitionsmenge von f\(x\) = −?\d+/\(x [−+] \d+\)', 'erkennen'),
  (r'Abbildung', 'darstellung'), (r'\) \+ \d/\(', 'verknuepfen'), (r'Bestimme b', 'parameter'), (r'Zahl a', 'rueckwaerts'), (r'.', 'mehrschritt'))
ST.neu('definitionsmenge', 'einkleidung', SA('Für 120 km braucht man t(v) = 120/v Stunden. Welche Zahl gehört nicht zur Definitionsmenge, und welche v sind im Sachzusammenhang sinnvoll?', 'v = 0; sinnvoll sind nur v > 0.',
    ['v = 120; sinnvoll sind alle v.', 'v = 1; sinnvoll sind v > 1.', 'Keine; alle v sind sinnvoll.'], 'Bei v = 0 wäre der Nenner 0. Negative Geschwindigkeiten ergeben hier keinen Sinn.', 'Wann wird der Nenner 0 – und was bedeutet v?'))
ST.neu('definitionsmenge', 'umkehr', SA('Welche Funktion hat die Definitionsmenge ℚ \\ {−4}?', 'f(x) = 2/(x + 4) − 1', ['f(x) = 2/(x − 4) − 1', 'f(x) = 2/x − 4', 'f(x) = −4/(x + 1)'],
    'x + 4 = 0 bei x = −4. Die anderen schließen 4, 0 bzw. −1 aus.', 'Bei welchem x wird jeder Nenner 0?'))
ST.neu('definitionsmenge', 'fehler', SA('Jemand gibt für f(x) = 3/(x + 2) − 5 die Definitionsmenge ℚ \\ {−2; 5} an. Was stimmt?', 'Falsch: Nur der Nenner zählt, D = ℚ \\ {−2}.', ['Richtig.', 'Falsch: D = ℚ \\ {2}.', 'Falsch: D = ℚ \\ {5}.'],
    'Das „− 5“ steht nicht im Nenner, es verschiebt den Graphen nur nach unten.', 'Welche Zahl macht wirklich einen Nenner zu 0?'))
ST.neu('definitionsmenge', 'begruenden', SA('Warum gehört x = 0 zur Definitionsmenge von f(x) = 1/(x − 1) + 3?', 'Weil der Nenner bei x = 0 den Wert −1 hat, nicht 0.', ['Weil 0 nie ausgeschlossen wird.', 'Gehört sie nicht.', 'Weil der Zähler 1 ist.'],
    'Ausgeschlossen ist nur x = 1. f(0) = −1 + 3 = 2 existiert.', 'Setze 0 in den Nenner ein.'))
ST.neu('definitionsmenge', 'transfer', SZ('180 € Kosten teilen sich die Gäste einer Feier, die zwei Gastgeber zahlen nichts: p(n) = 180/(n − 2) bei n Personen. Wie viele Personen sind da, wenn jeder Gast 15 € zahlt?', 14, '180 / 15 + 2',
    '180/(n − 2) = 15 ⇒ n − 2 = 12 ⇒ n = 14 (12 Gäste zahlen, 2 Gastgeber nicht).', 'Löse nach n auf.'))
ST.neu('definitionsmenge', 'pruefung', SA('f(x) = 2/(x − 3) + 1 und g(x) = 1/(x + 3). Welche Zahl gehört zur Definitionsmenge von f, aber nicht zu der von g?', '−3', ['3', '0', '1'],
    'f schließt 3 aus, g schließt −3 aus. −3 darf man in f einsetzen (f(−3) = 2/(−6) + 1), in g nicht.', 'Bestimme beide Definitionsmengen.'))
ST.neu('definitionsmenge', 'verknuepfen', SA('Welche Definitionsmenge hat f(x) = 1/(x² − 4)?', 'ℚ \\ {−2; 2}', ['ℚ \\ {2}', 'ℚ \\ {4}', 'ℚ \\ {−4; 4}'], 'x² − 4 = (x − 2)(x + 2) = 0 für x = 2 und x = −2.', 'Zerlege den Nenner mit der binomischen Formel.'))
ST.knobel('definitionsmenge', SZ('f(x) = 1/(x − a) + 1/(x − b) hat die Definitionsmenge ℚ \\ {1; 5}, und es gilt a < b. Berechne f(3).', 0, '1/2 + 1/(-2)',
    'Ausgeschlossen sind a und b, also a = 1, b = 5. f(3) = 1/2 + 1/(−2) = 0. Die 3 liegt genau in der Mitte – die beiden Brüche heben sich auf.', 'Bestimme a und b aus der Definitionsmenge.'))
ST.knobel('definitionsmenge', SZ('Für wie viele ganze Zahlen x von −10 bis 10 ist f(x) = 1/(x² − 9) definiert?', 19, '21 - 2',
    'Von −10 bis 10 gibt es 21 ganze Zahlen. Nicht definiert ist f für x² = 9, also x = 3 und x = −3. Es bleiben 19.', 'Für welche x ist x² − 9 = 0? Denk an beide Vorzeichen.'))

# --- asymptoten ---
ST.leiter('asymptoten', 'senkrechte und waagrechte Asymptote aus a/(x + b) + c ablesen',
          'beide Asymptoten, Kommazahlen, Asymptoten am Bild ablesen, Sachbedeutung der waagrechten Asymptote',
          'Term aus Asymptoten rückwärts, Schnitt mit einer Geraden, begründen warum y = c nie erreicht wird, Parameter, Vorzeichenfehler, Prüfungsaufgabe mit Nullstelle')
T('asymptoten', (r'^Gib die (senkrechte|waagrechte) Asymptote von f\(x\) = −?\d+/\(x [−+] \d+\) [−+] \d+ an', 'direkt'), (r'^Lies die Asymptoten', 'darstellung'),
  (r'Wie heißt der Term|bestimme den Term', 'rueckwaerts'), (r'schneidet die Gerade', 'verknuepfen'), (r'^Kann der Graph', 'begruenden'), (r'Ursprung', 'parameter'),
  (r'.', 'mehrschritt'))
ST.neu('asymptoten', 'erkennen', SA('Welche Gerade ist die waagrechte Asymptote von f(x) = 2/(x + 1) + 4?', 'y = 4', ['y = 2', 'x = −1', 'y = 1'], 'Für große x wird 2/(x + 1) fast 0, f(x) nähert sich 4.', 'Was bleibt übrig, wenn der Bruch fast 0 ist?'))
ST.neu('asymptoten', 'einkleidung', SZ('Bei n Mitfahrern kostet eine Fahrt pro Person p(n) = 200/n + 8 €. Welchem Betrag nähert sich der Preis, wenn sehr viele mitfahren?', 8, '8',
    'Für großes n wird 200/n sehr klein; übrig bleiben die 8 € (waagrechte Asymptote).', 'Was passiert mit 200/n, wenn n riesig wird?', einheit='€'))
ST.neu('asymptoten', 'fehler', SA('Jemand gibt für f(x) = 3/(x − 2) + 5 die senkrechte Asymptote x = −2 an. Was stimmt?', 'Falsch: Der Nenner ist 0 für x = 2, also x = 2.', ['Richtig.', 'Falsch: x = 5.', 'Falsch: x = 3.'],
    'x − 2 = 0 ⇒ x = 2. Das Vorzeichen in der Klammer kehrt sich beim Ablesen um.', 'Setze den Nenner gleich 0.'))
ST.neu('asymptoten', 'transfer', SA('Mit n gleichen Pumpen dauert das Leeren t(n) = 24/n Stunden. Was bedeutet die waagrechte Asymptote y = 0?', 'Mit immer mehr Pumpen geht die Zeit gegen 0, wird aber nie 0.',
    ['Mit 24 Pumpen dauert es 0 Stunden.', 'Ohne Pumpen dauert es 0 Stunden.', 'Die Zeit wird irgendwann negativ.'], '24/n ist für jedes n > 0 positiv, wird aber beliebig klein.', 'Kann 24/n jemals 0 sein?'))
ST.neu('asymptoten', 'pruefung', SZ('Gegeben f(x) = 6/(x + 2) − 3. Gib die Asymptoten an und berechne die Nullstelle. Gib die Nullstelle an.', 0, '6 / 3 - 2',
    'Asymptoten: x = −2 und y = −3. Nullstelle: 6/(x + 2) = 3 ⇒ x + 2 = 2 ⇒ x = 0 (der Graph geht durch den Ursprung).', 'Setze f(x) = 0 und löse.'))
ST.knobel('asymptoten', SZ('Die Hyperbel f(x) = a/(x − 1) + 2 geht durch (3 | 5). Wie weit ist ihr Punkt mit x = 7 von der waagrechten Asymptote entfernt?', 1, '6 / (7 - 1)',
    'Aus (3 | 5): a/2 + 2 = 5 ⇒ a = 6. f(7) = 6/6 + 2 = 3. Die waagrechte Asymptote ist y = 2, der Abstand also 1.', 'Bestimme zuerst a.'))
ST.knobel('asymptoten', SZ('Wie viele Punkte mit ganzzahligen Koordinaten liegen auf dem Graphen von f(x) = 4/(x − 1) + 2?', 6, '2 * 3',
    'f(x) ist ganz, wenn x − 1 ein Teiler von 4 ist: ±1, ±2, ±4. Das ergibt 6 Werte für x (2, 0, 3, −1, 5, −3) und jeweils einen ganzen y-Wert.', 'Wann ist 4/(x − 1) eine ganze Zahl?'))

# --- achsenpunkte ---
ST.leiter('achsenpunkte', 'den Schnittpunkt mit der y-Achse durch Einsetzen von x = 0 bestimmen',
          'Nullstelle berechnen, „keine Nullstelle“ erkennen, Sachfunktion auswerten, Funktion zu einem Achsenpunkt finden',
          'Lücken bei x = 0 begründen, Fehler (x = 0 statt f(x) = 0), Parameter c, rückwärts zu a, Dreiecksfläche verknüpfen, beide Achsenpunkte wie in einer Prüfung')
T('achsenpunkte', (r'^In welchem Punkt schneidet der Graph', 'direkt'), (r'^Wo schneidet|Welche Funktion hat KEINE|Für welche Werte von c', 'begruenden'),
  (r'Bestimme beide', 'pruefung'), (r'Wert von c', 'parameter'), (r'.', 'mehrschritt'))
ST.neu('achsenpunkte', 'erkennen', SA('Wie findet man den Schnittpunkt eines Graphen mit der y-Achse?', 'x = 0 einsetzen', ['f(x) = 0 setzen', 'den Nenner gleich 0 setzen', 'x = 1 einsetzen'],
    'Alle Punkte der y-Achse haben x = 0.', 'Welche Koordinate ist auf der y-Achse null?'))
ST.neu('achsenpunkte', 'einkleidung', SZ('Ein Tank wird geleert. Die Restmenge ist V(t) = 120/(t + 2) − 10 (t in h, V in hl). Wie viel ist am Anfang darin?', 50, '120 / 2 - 10', 'V(0) = 60 − 10 = 50 hl.', 'Am Anfang ist t = 0.', einheit='hl'))
ST.neu('achsenpunkte', 'umkehr', SA('Welche Funktion schneidet die y-Achse bei 3?', 'f(x) = 4/(x + 2) + 1', ['f(x) = 4/(x − 2) + 1', 'f(x) = 3/(x + 3)', 'f(x) = 6/x + 3'],
    'f(0) = 4/2 + 1 = 3. Die anderen: −1, 1, und 6/x ist bei 0 nicht definiert.', 'Setze in jede Funktion x = 0 ein.'))
ST.neu('achsenpunkte', 'fehler', SA('Für die Nullstelle von f(x) = 4/(x − 1) − 2 setzt jemand x = 0 ein und erhält −6. Was stimmt?', 'Falsch: Für die Nullstelle setzt man f(x) = 0; das ergibt x = 3.',
    ['Richtig, die Nullstelle ist −6.', 'Falsch: Die Nullstelle ist 1.', 'Falsch: Es gibt keine Nullstelle.'], 'f(0) = −6 ist der y-Achsenabschnitt. 4/(x − 1) = 2 ⇒ x − 1 = 2 ⇒ x = 3.', 'Was ist bei einer Nullstelle null: x oder f(x)?'))
ST.neu('achsenpunkte', 'rueckwaerts', SZ('f(x) = a/(x + 1) − 3 hat die Nullstelle x = 1. Bestimme a.', 6, '3 * 2', 'a/2 − 3 = 0 ⇒ a = 6.', 'Setze x = 1 und f(x) = 0 ein.'))
ST.neu('achsenpunkte', 'verknuepfen', SZ('Der Graph von f(x) = 6/(x + 2) − 1 schneidet die Achsen in N und S. Wie groß ist die Fläche des Dreiecks aus N, S und dem Ursprung?', 4, '4 * 2 / 2',
    'S: f(0) = 3 − 1 = 2, also (0 | 2). N: 6/(x + 2) = 1 ⇒ x = 4, also (4 | 0). Rechtwinkliges Dreieck: A = 4 · 2 : 2 = 4.', 'Bestimme beide Achsenpunkte.', einheit='FE'))
ST.knobel('achsenpunkte', SZ('Für wie viele ganze Zahlen c hat f(x) = 12/(x − 1) + c eine ganzzahlige Nullstelle?', 12, '2 * 6',
    '12/(x − 1) = −c ⇒ x − 1 = −12/c. Ganz, wenn c ein Teiler von 12 ist (c ≠ 0, für c = 0 gibt es keine Nullstelle): ±1, ±2, ±3, ±4, ±6, ±12 – zwölf Werte.', 'Löse die Gleichung f(x) = 0 nach x auf.'))
ST.knobel('achsenpunkte', SA('Kann eine Funktion f(x) = a/(x + b) + c mit a ≠ 0 zwei Nullstellen haben?', 'Nein: a/(x + b) = −c hat höchstens eine Lösung.', ['Ja, wenn c = 0 ist.', 'Ja, wenn b negativ ist.', 'Ja, immer.'],
    'Aus a/(x + b) = −c folgt x + b = a/(−c) – genau ein Wert (für c ≠ 0), für c = 0 gar keiner.', 'Löse a/(x + b) + c = 0 allgemein.'))

# --- parameter ---
ST.leiter('parameter', 'eine Verschiebung nach oben/unten am Term erkennen',
          'Verschiebung nach links/rechts und oben/unten, Einfluss von a (Streckung, Spiegelung), Term zu einer Verschiebung aufstellen',
          'Term aus Asymptoten, Verschiebungen verketten, Symmetriezentrum, Spiegelung, Fehler bei „+ b nach rechts“, begründen, Spiegelung an y = x')
T('parameter', (r'^Wie entsteht der Graph von f\(x\) = −?\d+/x [+−] \d+ aus', 'direkt'), (r'^Wie entsteht', 'mehrschritt'), (r'Wie unterscheidet sich', 'darstellung'),
  (r'^Der Graph von g\(x\) = \d+/x wird um', 'umkehr'), (r'Lies die Asymptoten', 'rueckwaerts'), (r'f\(x\) = 3/\(x − 1\) \+ 2 wird', 'verknuepfen'), (r'punktsymmetrisch', 'parameter'),
  (r'gespiegelt', 'transfer'))
ST.neu('parameter', 'erkennen', SA('Welcher Parameter in f(x) = a/(x + b) + c verschiebt den Graphen nach oben oder unten?', 'c', ['a', 'b', 'x'], 'c wird zu jedem Funktionswert addiert – das hebt oder senkt den ganzen Graphen.', 'Welche Zahl wird am Ende addiert?'))
ST.neu('parameter', 'fehler', SA('Jemand sagt: „Der Graph von f(x) = 2/(x + 3) ist der von 2/x, um 3 nach rechts verschoben.“ Was stimmt?', 'Falsch: + 3 im Nenner verschiebt um 3 nach links.',
    ['Richtig.', 'Falsch: um 3 nach oben.', 'Falsch: um 3 nach unten.'], 'Die Lücke liegt bei x + 3 = 0, also x = −3 – links vom Ursprung.', 'Wo ist die neue Definitionslücke?'))
ST.neu('parameter', 'begruenden', SA('Warum verschiebt „x − 2“ im Nenner den Graphen nach rechts?', 'Bei x = 2 ist der Nenner jetzt 0 – die Lücke liegt bei 2 statt bei 0.',
    ['Weil Minus immer nach rechts bedeutet.', 'Weil 2 positiv ist und man nach oben schiebt.', 'Das tut es nicht, es verschiebt nach links.'],
    'f(x) = a/(x − 2) nimmt bei x die Werte an, die a/x bei x − 2 hat – alles passiert 2 Einheiten später, also weiter rechts.', 'Wo ist die Definitionslücke von a/(x − 2)?'))
ST.neu('parameter', 'pruefung', SA('Der Graph von g(x) = 1/x wird um 2 nach links und um 1 nach unten verschoben. Welche Asymptoten hat der neue Graph?', 'x = −2 und y = −1', ['x = 2 und y = −1', 'x = −2 und y = 1', 'x = −1 und y = −2'],
    'Neuer Term f(x) = 1/(x + 2) − 1: senkrecht x = −2, waagrecht y = −1.', 'Stelle zuerst den neuen Term auf.'))
ST.neu('parameter', 'transfer', SA('Der Graph von f(x) = 1/(x − 1) + 1 wird an der Geraden y = x gespiegelt. Welche Funktion gehört zum gespiegelten Graphen?', 'wieder f(x) = 1/(x − 1) + 1',
    ['f(x) = 1/(x + 1) − 1', 'f(x) = −1/(x − 1) + 1', 'f(x) = x − 1'], 'Beim Spiegeln an y = x vertauscht man x und y: x − 1 = 1/(y − 1) ⇒ y − 1 = 1/(x − 1). Es kommt derselbe Term heraus – der Graph ist zu y = x symmetrisch.',
    'Vertausche x und y und löse nach y auf.'))
ST.knobel('parameter', SZ('Der Graph von f(x) = 2/(x − 3) + 1 wird erst um 5 nach links, dann um 2 nach unten verschoben und danach an der x-Achse gespiegelt. Welchen Wert hat der neue Term bei x = 0?', 0, '-(2 / (0 + 2) - 1)',
    'Nach links um 5: 2/(x + 2) + 1. Nach unten um 2: 2/(x + 2) − 1. Spiegeln an der x-Achse: −2/(x + 2) + 1. Bei x = 0: −1 + 1 = 0.', 'Mache die drei Schritte nacheinander am Term.'))
ST.knobel('parameter', SA('Für welche b und c geht der Graph von f(x) = 1/(x + b) + c durch den Ursprung und hat die waagrechte Asymptote y = 1?', 'b = −1, c = 1', ['b = 1, c = 1', 'b = −1, c = −1', 'b = 1, c = −1'],
    'Asymptote y = 1 ⇒ c = 1. Ursprung: 1/b + 1 = 0 ⇒ b = −1. Probe: f(0) = 1/(−1) + 1 = 0.', 'Die waagrechte Asymptote verrät c sofort.'))

# --- beurteilen ---
ST.leiter('beurteilen', 'eine richtige Aussage über Definitionslücke oder Nullstelle erkennen',
          'die falsche Aussage finden, Werte berechnen und vergleichen, Stückkosten-Sachaussage beurteilen',
          'Fehlschlüsse (fällt ⇒ größer) widerlegen, Verhalten für große x begründen, Schnittpunkte mit Geraden, Parameter, rückwärts, Abstand-Modell, Prüfungsaufgabe')
T('beurteilen', (r'ist richtig\?$', 'erkennen'), (r'FALSCH\?$', 'umkehr'), (r'^Ben', 'fehler'), (r'^Ina|KEINEM Graphen', 'begruenden'), (r'Wie viele Schnittpunkte', 'verknuepfen'))
ST.neu('beurteilen', 'direkt', SA('Stimmt: f(x) = 4/(x − 2) + 1 ist bei x = 2 nicht definiert?', 'Ja, dort ist der Nenner 0.', ['Nein, das ist bei x = −2.', 'Nein, f ist überall definiert.'], 'x − 2 = 0 bei x = 2.', 'Setze 2 in den Nenner ein.'))
ST.neu('beurteilen', 'mehrschritt', SA('Für f(x) = 6/(x − 1) + 2: Welche Aussage stimmt?', 'f(4) = 4 und f(−2) = 0', ['f(4) = 4 und f(−2) = 4', 'f(4) = 8 und f(−2) = 0', 'f(4) = 2 und f(−2) = −2'],
    'f(4) = 6/3 + 2 = 4. f(−2) = 6/(−3) + 2 = 0.', 'Berechne beide Werte.'))
ST.neu('beurteilen', 'einkleidung', SA('Die Kosten pro Stück sind k(n) = 500/n + 2 € bei n Stück. Welche Aussage stimmt?', 'Bei mehr Stück sinken die Stückkosten, bleiben aber über 2 €.',
    ['Ab 250 Stück kostet jedes Stück genau 2 €.', 'Die Stückkosten steigen mit n.', 'Bei 500 Stück ist ein Stück kostenlos.'], '500/n wird kleiner, bleibt aber positiv: k(n) > 2. Bei 500 Stück: 3 €.', 'Was macht 500/n, wenn n wächst?'))
ST.neu('beurteilen', 'darstellung', SA('Ein Graph hat die Asymptoten x = 3 und y = −1; seine Äste liegen rechts oben und links unten vom Asymptotenkreuz. Welcher Term passt?', 'f(x) = 2/(x − 3) − 1',
    ['f(x) = −2/(x − 3) − 1', 'f(x) = 2/(x + 3) − 1', 'f(x) = 2/(x − 3) + 1'], 'Senkrecht x = 3 ⇒ (x − 3), waagrecht y = −1 ⇒ − 1. Äste rechts oben/links unten ⇒ a > 0.', 'Lies b und c an den Asymptoten ab, das Vorzeichen von a an der Lage der Äste.'))
ST.neu('beurteilen', 'parameter', SA('Für welche a liegt der Graph von f(x) = a/x im 2. und 4. Quadranten?', 'für alle a < 0', ['für alle a > 0', 'nur für a = −1', 'für alle a ≠ 0'],
    'Für a < 0 ist f(x) negativ bei positiven x (4. Quadrant) und positiv bei negativen x (2. Quadrant).', 'Probiere a = −2 mit x = 1 und x = −1.'))
ST.neu('beurteilen', 'rueckwaerts', SZ('Eine Hyperbel f(x) = a/x geht durch (3 | −4). Welchen Wert hat f(6)?', -2, '(3 * -4) / 6', 'a = 3 · (−4) = −12. f(6) = −12/6 = −2.', 'Bestimme a aus dem Punkt.'))
ST.neu('beurteilen', 'transfer', SA('Vereinfacht gilt für die Helligkeit einer Lampe H = 100/d (d Abstand). Wie ändert sich H, wenn man den Abstand verdreifacht?', 'H wird ein Drittel so groß.',
    ['H wird dreimal so groß.', 'H bleibt gleich.', 'H wird um 3 kleiner.'], '100/(3d) = (1/3) · 100/d.', 'Setze 3d statt d ein.'))
ST.neu('beurteilen', 'pruefung', SA('Welche Aussage über f(x) = 2/(x + 1) − 2 ist richtig?', 'Nullstelle 0, Asymptoten x = −1 und y = −2', ['Nullstelle 1, Asymptoten x = 1 und y = −2', 'keine Nullstelle, Asymptoten x = −1 und y = 2', 'Nullstelle 0, Asymptoten x = 1 und y = 2'],
    '2/(x + 1) = 2 ⇒ x = 0. Senkrecht x = −1, waagrecht y = −2.', 'Bestimme Nullstelle und beide Asymptoten.'))
ST.knobel('beurteilen', SZ('Wie viele Schnittpunkte hat der Graph von f(x) = 1/x mit der Geraden y = −x + 2,5?', 2, '2',
    'Probieren: x = 2 ergibt 1/2 und −2 + 2,5 = 0,5 ✓. x = 0,5 ergibt 2 und 2 ✓. Beide Graphen sind spiegelbildlich zu y = x, deshalb gehört zu (2 | 0,5) auch (0,5 | 2). Für x < 0 ist 1/x negativ, die Gerade aber positiv – dort gibt es keinen Schnitt. Also 2.',
    'Probiere einfache Zahlen und nutze die Symmetrie zu y = x.'))
ST.knobel('beurteilen', SZ('Wie viele Punkte mit positiven ganzzahligen Koordinaten liegen auf dem Graphen von f(x) = 6/x?', 4, '4',
    'x muss ein positiver Teiler von 6 sein: 1, 2, 3, 6. Das ergibt (1 | 6), (2 | 3), (3 | 2), (6 | 1).', 'Wann ist 6/x eine ganze Zahl?'))
baue = mit_stufen(baue, ST)
# ---- STUFEN ENDE ----

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Indirekte Proportionalität', ['indirekt']), ('Hyperbeln untersuchen', ['definitionsmenge', 'asymptoten', 'achsenpunkte']),
          ('Parameter und Verstehen', ['parameter', 'beurteilen'])],
         'Indirekte Proportionalitäten erkennen und Funktionen f(x) = a/(x + b) + c untersuchen: Definitionsmenge, Asymptoten, Achsenschnittpunkte, Verschiebungen.',
         ['Indirekt proportional: x · y = konstant, y = k/x.', 'f(x) = a/(x + b) + c: D = ℚ \\ {−b}, Asymptoten x = −b und y = c.',
          'x − 3 in der Klammer: 3 nach rechts. + c: c nach oben.'],
         offen=['Hyperbeln selbst zeichnen lassen (Kind zeichnet) kann die App noch nicht; Ablesen von Asymptoten und „Term zum Graphen“ sind eingebaut.'])


# ---- BEREINIGEN (Einundzwanzigste Runde) ----
if __name__ == '__main__':
    from _bereinigen import bereinigen_datei
    bereinigen_datei('funktionen.gebrochen')
# ---- BEREINIGEN ENDE ----
