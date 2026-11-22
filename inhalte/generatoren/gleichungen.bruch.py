#!/usr/bin/env python3
"""Thema gleichungen.bruch – Bruch- und Verhältnisgleichungen (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, Z, baue, bruch, cz, ist_endlich, kl, lin, mit_bild, zt  # noqa: E402

META = {'thema_schluessel': 'gleichungen.bruch', 'thema_id': 5, 'block_id': 60, 'klasse': {'gym_by': 8, 'rs_by': 8, 'ib_myp': 4}}

ETAPPEN = [
    {'lernziel': 'definitionsmenge', 'titel': 'Definitionsmenge einer Bruchgleichung',
     'regel': 'Bei einer ⟦Bruchgleichung⟧ steht x im Nenner. Bevor du rechnest, schließt du alle Zahlen aus, die einen ⟦Nenner 0⟧ machen.',
     'schritte': ['2/(x − 1) = 3/(x + 4)', 'x − 1 = 0 für x = 1; x + 4 = 0 für x = −4.', '⟦D = ℚ \\ {−4; 1}⟧'],
     'fehler': 'Bei 2/(x − 1) = 3/(x + 4) reicht es nicht, nur x = 1 auszuschließen. ⟦Jeder⟧ Nenner zählt, auch der auf der rechten Seite.',
     '_verbot': ['2/(x − 1) = 3/(x + 4)']},
    {'lernziel': 'ein_bruch', 'titel': 'Bruchgleichungen mit einem Bruch',
     'regel': 'Multipliziere beide Seiten mit dem ⟦Nenner⟧. Dann ist der Bruch weg und du löst eine lineare Gleichung. Zum Schluss prüfst du, ob die Lösung in ⟦D⟧ liegt.',
     'schritte': ['12/(x − 2) = 3. Zuerst D = ℚ \\ {2}.', 'Beide Seiten · (x − 2): 12 = 3 · (x − 2) = 3x − 6.', '18 = 3x, also ⟦x = 6⟧. 6 liegt in D.',
                  'Schneller mit der Umkehrfrage: 12 geteilt durch was ergibt 3? Durch 4. Also x − 2 = 4 und x = 6.'],
     'probe': '12/(6 − 2) = 12/4 = 3 ✓',
     'fehler': 'Aus 12/(x − 2) = 3 wird nicht 12 = 3x − 2. Der Nenner wird als ⟦Ganzes⟧ multipliziert: 3 · (x − 2) = 3x − 6.',
     '_verbot': ['12/(x − 2) = 3']},
    {'lernziel': 'ueber_kreuz', 'titel': 'Zwei Brüche: über Kreuz multiplizieren',
     'regel': 'Steht auf jeder Seite ⟦genau ein⟧ Bruch, multiplizierst du ⟦über Kreuz⟧: aus a/b = c/d wird a · d = c · b. Warum? Du nimmst beide Seiten mit b und mit d mal – dann kürzt sich links das b und rechts das d weg.',
     'schritte': ['4/(x + 1) = 2/(x − 3)   D = ℚ \\ {−1; 3}', 'Über Kreuz: 4(x − 3) = 2(x + 1)', '4x − 12 = 2x + 2 → 2x = 14 → ⟦x = 7⟧'],
     'probe': '4/8 = 0,5 und 2/4 = 0,5 ✓',
     'fehler': 'Über Kreuz heißt Zähler links mal Nenner ⟦rechts⟧. 4 · (x + 1) = 2 · (x − 3) ist falsch – da wurde jeder Zähler mit dem eigenen Nenner malgenommen. Und Vorsicht: Bei 4/(x + 1) + 1 = 2/(x − 3) steht links eine Summe, dann geht über Kreuz ⟦nicht⟧ – nimm den Hauptnenner.',
     '_verbot': ['4/(x + 1) = 2/(x − 3)']},
    {'lernziel': 'hauptnenner', 'titel': 'Mit dem Hauptnenner multiplizieren',
     'regel': 'Stehen mehrere Brüche in der Gleichung, multiplizierst du ⟦jedes Glied⟧ mit dem ⟦Hauptnenner⟧. Danach kommt kein Bruch mehr vor.',
     'schritte': ['5/x + 1/(2x) = 2   HN = 2x', '| · 2x: 10 + 1 = 4x', '11 = 4x → ⟦x = 2,75⟧'],
     'fehler': 'Ein Glied vergessen: Wer bei 5/x + 1/(2x) = 2 nur die Brüche mit 2x malnimmt, bekommt 10 + 1 = 2 – das x ist verschwunden und die Gleichung ist Unsinn. Auch die ⟦2 auf der rechten Seite⟧ wird mit 2x multipliziert: 11 = 4x.',
     '_verbot': ['5/x + 1/(2x) = 2']},
    {'lernziel': 'scheinloesung', 'titel': 'Lösung prüfen: Gehört sie zu D?',
     'regel': 'Eine errechnete Zahl ist nur dann Lösung, wenn sie in ⟦D⟧ liegt. Sonst ist sie eine ⟦Scheinlösung⟧ und die Lösungsmenge ist leer: L = { }.',
     'schritte': ['(x + 1)/(x − 3) = 4/(x − 3)   D = ℚ \\ {3}', '| · (x − 3): x + 1 = 4 → x = 3', '3 liegt nicht in D: ⟦L = { }⟧'],
     'fehler': 'L = {3} ist hier falsch: Für x = 3 wird der Nenner 0, die Gleichung hat dort ⟦keinen Sinn⟧. Deshalb immer zuerst D bestimmen.',
     '_verbot': ['(x + 1)/(x − 3) = 4/(x − 3)']},
    {'lernziel': 'verhaeltnis', 'titel': 'Verhältnisgleichungen',
     'regel': 'Eine ⟦Verhältnisgleichung⟧ hat die Form a : b = c : d. Es gilt die ⟦Produktgleichheit⟧: a · d = b · c (Außenglieder mal Außenglieder = Innenglieder mal Innenglieder).',
     'schritte': ['Pfannkuchen: Auf 4 Eier kommen 10 Esslöffel Mehl. Wie viel Mehl für 6 Eier? Das Verhältnis Mehl : Eier bleibt gleich: x : 6 = 10 : 4.',
                  'Produktgleichheit: 4 · x = 6 · 10 = 60.', '⟦x = 15⟧ Esslöffel Mehl.'],
     'probe': 'Mit dem Faktor: Auf 1 Ei kommen 10 : 4 = 2,5 EL, also 6 · 2,5 = 15 ✓',
     'fehler': 'x = 6 · 4 : 10 = 2,4 ist falsch – mit mehr Eiern braucht man nicht weniger Mehl! Die ⟦Außenglieder⟧ x und 4 werden miteinander multipliziert, ebenso die Innenglieder 6 und 10: 4x = 60.',
     '_verbot': ['x : 6 = 10 : 4']},
    {'lernziel': 'graphisch', 'titel': 'Bruchgleichung am Graphen lösen',
     'regel': 'Jede Seite einer Gleichung ist ein Funktionsterm. Zeichne ⟦beide Graphen⟧. Wo sie sich ⟦schneiden⟧, sind beide Seiten gleich: Die x-Werte der Schnittpunkte sind die Lösungen.',
     'schritte': ['Gleichung 6/x = x − 1. Links die Hyperbel y = 6/x, rechts die Gerade y = x − 1.', 'Die Graphen schneiden sich in (3 | 2) und in (−2 | −3).',
                  'Die Lösungen sind ⟦x = 3⟧ und ⟦x = −2⟧.'],
     'probe': '6/3 = 2 und 3 − 1 = 2 ✓. 6/(−2) = −3 und −2 − 1 = −3 ✓',
     'fehler': 'Die y-Werte als Lösung angeben: L = {2; −3} ist falsch. Gesucht sind die ⟦x-Werte⟧ der Schnittpunkte, denn x ist die Unbekannte der Gleichung.',
     'bild': {'typ': 'koordinaten', 'x': [-6, 6], 'y': [-6, 6],
              'graphen': [{'art': 'hyperbel', 'a': 6, 'b': 0, 'c': 0, 'name': 'y = 6/x'}, {'art': 'linear', 'm': 1, 't': -1, 'name': 'y = x − 1'}],
              'punkte': [{'x': 3, 'y': 2, 'name': '(3 | 2)'}, {'x': -2, 'y': -3, 'name': '(−2 | −3)'}]},
     '_verbot': ['6/x = x − 1']},
]


# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'definitionsmenge': {
  'einstieg': 'Eine Klasse mietet einen Bus für 600 €. Fahren x Kinder mit, zahlt jedes 600/x Euro. Die Lehrerin sagt: „Jeder zahlt 25 €.“ Wie viele fahren mit? Das ist eine Gleichung mit x im Nenner – eine ⟦Bruchgleichung⟧. Bevor man rechnet, streicht man alle Zahlen, für die ein Nenner 0 würde.',
  'woerter': [['Bruchgleichung', 'eine Gleichung, in der x im Nenner eines Bruchs steht'], ['Nenner', 'was unter dem Bruchstrich steht; er darf nie 0 sein'],
              ['D', 'Definitionsmenge: alle Zahlen, die man für x einsetzen darf'], ['ℚ \\ {−4; 1}', 'alle Bruchzahlen außer −4 und 1']],
  'schritte': ['Gleichung: 2/(x − 1) = 3/(x + 4).', 'Linker Nenner: x − 1 ist 0 für x = 1. Diese Zahl muss raus.', 'Rechter Nenner: x + 4 ist 0 für x = −4. Auch diese Zahl muss raus.',
               'Also ⟦D = ℚ \\ {−4; 1}⟧.'],
  'regel': 'So bestimmst du D bei einer ⟦Bruchgleichung⟧: ⟦jeden⟧ Nenner gleich 0 setzen und diese x-Werte streichen – noch bevor du irgendetwas anderes rechnest.'},
 'ein_bruch': {
  'einstieg': 'Zurück zum Bus: 600/x = 25. Du fragst: 600 geteilt durch wie viele ergibt 25? Rechnerisch nimmst du beide Seiten mit dem Nenner x mal. Dann ist der Bruch verschwunden: 600 = 25 · x, also x = 24. Übrig bleibt eine ⟦lineare Gleichung⟧, wie du sie schon lösen kannst.',
  'woerter': [['lineare Gleichung', 'eine Gleichung, in der x ohne Hochzahl vorkommt, z. B. 3x − 6 = 12'], ['· (x − 2)', 'beide Seiten mit der ganzen Klammer malnehmen'],
              ['liegt in D', 'die Zahl ist erlaubt, kein Nenner wird 0']],
  'schritte': ['Gleichung: 12/(x − 2) = 3. Zuerst D: x − 2 darf nicht 0 sein, also D = ℚ \\ {2}.',
               'Beide Seiten mit (x − 2) malnehmen. Links fällt der Nenner weg: 12 = 3 · (x − 2) = 3x − 6.',
               'Auf beiden Seiten 6 dazuzählen: 18 = 3x. Durch 3 teilen: ⟦x = 6⟧.',
               'Kontrolle: 6 liegt in D. Schneller geht es mit der Frage „12 geteilt durch was ergibt 3?“ – durch 4, also x − 2 = 4.'],
  'regel': 'So löst du: D bestimmen, dann beide Seiten mit dem ⟦Nenner⟧ malnehmen. Es bleibt eine ⟦lineare Gleichung⟧. Zum Schluss prüfen, ob die Lösung in ⟦D⟧ liegt.'},
 'ueber_kreuz': {
  'einstieg': 'Ob zwei Brüche gleich groß sind, kann man ohne Kommazahlen prüfen: 2/3 und 4/6 sind gleich, weil 2 · 6 und 3 · 4 beide 12 ergeben. Dieses Malnehmen „über Kreuz“ klappt auch, wenn x in den Nennern steht. Es heißt ⟦über Kreuz multiplizieren⟧.',
  'woerter': [['über Kreuz multiplizieren', 'Zähler links mal Nenner rechts = Zähler rechts mal Nenner links'], ['a/b = c/d', 'zwei Brüche, die gleich sein sollen'],
              ['ausmultiplizieren', 'Klammer auflösen, z. B. 4(x − 3) = 4x − 12']],
  'schritte': ['Gleichung: 4/(x + 1) = 2/(x − 3). Zuerst D = ℚ \\ {−1; 3}.',
               'Über Kreuz: Zähler links mal Nenner rechts, Zähler rechts mal Nenner links: 4(x − 3) = 2(x + 1).', 'Ausmultiplizieren: 4x − 12 = 2x + 2.',
               '2x abziehen und 12 dazuzählen: 2x = 14, also ⟦x = 7⟧. 7 liegt in D.']},
 'hauptnenner': {
  'einstieg': 'Stehen in einer Gleichung mehrere Brüche, ist es mühsam, mit jedem einzeln zu rechnen. Besser: alles mit einem Term malnehmen, in den jeder Nenner hineinpasst – dann verschwinden alle Brüche auf einmal. Dieser Term ist der ⟦Hauptnenner⟧ (HN).',
  'woerter': [['Hauptnenner (HN)', 'der kleinste Term, durch den jeder Nenner teilbar ist'], ['Glied', 'jeder durch + oder − getrennte Teil einer Seite'],
              ['| · 2x', 'Randnotiz: Jedes Glied auf beiden Seiten wird mit 2x malgenommen.']],
  'schritte': ['Gleichung: 5/x + 1/(2x) = 2. Die Nenner sind x und 2x; beide passen in 2x. Also HN = 2x.',
               'Jedes Glied mal 2x: 5/x · 2x = 10, 1/(2x) · 2x = 1 und 2 · 2x = 4x.', 'Es bleibt 10 + 1 = 4x, also 11 = 4x.',
               'Durch 4 teilen: ⟦x = 2,75⟧. 2,75 ist nicht 0, liegt also in D.'],
  'regel': 'So gehst du vor: den ⟦Hauptnenner⟧ suchen und ⟦jedes Glied⟧ auf beiden Seiten damit malnehmen. Danach steht kein Bruch mehr da.'},
 'scheinloesung': {
  'einstieg': 'Stell dir vor, eine Rechnung zum Busausflug ergibt: „Es fahren 0 Kinder mit.“ Dann müsste jedes 600/0 € zahlen – das ergibt keinen Sinn, obwohl die Zahl ausgerechnet wurde. Auch Bruchgleichungen liefern manchmal eine Zahl, die gar nicht eingesetzt werden darf. So eine Zahl heißt ⟦Scheinlösung⟧.',
  'woerter': [['Scheinlösung', 'eine ausgerechnete Zahl, die nicht in D liegt – also keine echte Lösung'], ['L', 'Lösungsmenge: alle echten Lösungen'],
              ['L = { }', 'leere Menge: Es gibt keine Lösung.']],
  'schritte': ['Gleichung: (x + 1)/(x − 3) = 4/(x − 3). Zuerst D: x darf nicht 3 sein.', 'Beide Seiten mit (x − 3) malnehmen: x + 1 = 4.', 'Auf beiden Seiten 1 abziehen: x = 3.',
               'Aber 3 liegt nicht in D. Es ist eine Scheinlösung, also ⟦L = { }⟧.']},
 'verhaeltnis': {
  'einstieg': 'Für Pfannkuchen nimmst du auf 4 Eier 10 Esslöffel Mehl. Du hast aber 6 Eier und willst mehr Teig. Das Verhältnis von Mehl zu Eiern soll gleich bleiben, sonst wird der Teig zu dünn oder zu fest. Setzt man zwei gleiche Verhältnisse gleich, entsteht eine ⟦Verhältnisgleichung⟧.',
  'woerter': [['Verhältnis a : b', '„a zu b“, z. B. 10 Löffel Mehl zu 4 Eiern'], ['Außenglieder', 'die beiden äußeren Zahlen in a : b = c : d, also a und d'],
              ['Innenglieder', 'die beiden inneren Zahlen, also b und c'], ['Produktgleichheit', 'Außenglieder mal Außenglieder = Innenglieder mal Innenglieder'], ['EL', 'Esslöffel']],
  'schritte': ['Gesucht sind x Esslöffel Mehl für 6 Eier. Das Verhältnis Mehl : Eier bleibt gleich: x : 6 = 10 : 4.',
               'Außenglieder x und 4 malnehmen, Innenglieder 6 und 10 malnehmen: 4 · x = 6 · 10 = 60.', 'Beide Seiten durch 4 teilen: ⟦x = 15⟧ Esslöffel Mehl.'],
  'regel': 'So löst du eine ⟦Verhältnisgleichung⟧ a : b = c : d: Schreibe die ⟦Produktgleichheit⟧ a · d = b · c auf und löse nach x auf.'},
 'graphisch': {
  'einstieg': 'Statt zu rechnen, kannst du beide Seiten einer Gleichung zeichnen. Wo sich die beiden Linien treffen, haben beide Seiten denselben Wert – dort ist die Gleichung erfüllt. Die Stellen, an denen sich zwei Graphen treffen, heißen ⟦Schnittpunkte⟧.',
  'woerter': [['Graph', 'die Linie, die man zu einer Funktion zeichnet'], ['Hyperbel', 'der Graph von y = 6/x: zwei geschwungene Äste'], ['Gerade', 'der Graph von y = x − 1'],
              ['Schnittpunkt', 'ein Punkt, der auf beiden Graphen liegt'], ['(3 | 2)', 'der Punkt mit x = 3 und y = 2']],
  'schritte': ['Gleichung: 6/x = x − 1. Die linke Seite zeichnest du als Hyperbel y = 6/x, die rechte als Gerade y = x − 1.',
               'Im Bild schneiden sich die Graphen in (3 | 2) und in (−2 | −3).', 'Gesucht ist x. Also nimmst du die x-Werte der Schnittpunkte.',
               'Die Lösungen sind ⟦x = 3⟧ und ⟦x = −2⟧.']},
}

for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))
# ---- KLAR ENDE ----


def quad1(p, q):
    """x² + p·x + q mit richtigen Vorzeichen."""
    t = lin(p, q) if p else zt(q)
    if t == '0': return 'x²'
    return 'x² ' + ('− ' + t[1:] if t.startswith('−') else '+ ' + t)


def N(a, b):
    """Nenner a·x + b mit Klammern."""
    return f'({lin(a, b)})' if b else lin(a, b) if a != 1 else 'x'


def mengentext(xs):
    xs = sorted(set(xs))
    return 'ℚ' if not xs else 'ℚ \\ {' + '; '.join(zt(x) for x in xs) + '}'


def g_definitionsmenge(R, st):
    if st == 1:
        b, a, c = R.choice([k for k in range(-9, 10) if k]), R.randint(1, 12), R.randint(1, 9)
        G = f'{a}/{N(1, -b)} = {c}'
        return A(R, f'Bestimme die Definitionsmenge von {G}.', mengentext([b]), [mengentext([-b]), mengentext([0]), mengentext([b, c])],
                 f'Nenner {lin(1, -b)} = 0 für x = {zt(b)}. D = {mengentext([b])}.', 'Setze den Nenner gleich 0.')
    if st == 2:
        b, d = R.sample([k for k in range(-9, 10) if k], 2)
        G = f'{R.randint(1, 9)}/{N(1, -b)} = {R.randint(1, 9)}/{N(1, -d)}'
        return A(R, f'Bestimme die Definitionsmenge von {G}.', mengentext([b, d]), [mengentext([b]), mengentext([d]), mengentext([-b, -d])],
                 f'Linker Nenner 0 für x = {zt(b)}, rechter für x = {zt(d)}. D = {mengentext([b, d])}.', 'Jeder Nenner liefert eine ausgeschlossene Zahl.')
    k = R.choice([2, 3, 4, 5]); m = R.choice([j for j in range(-12, 13) if j and j % k == 0])
    b = R.choice([j for j in range(-6, 7) if j and j != m // k])
    G = f'{R.randint(1, 9)}/{N(k, -m)} = {R.randint(1, 9)}/(x{N(1, -b)})'
    return A(R, f'Bestimme die Definitionsmenge von {G}.', mengentext([m // k, 0, b]), [mengentext([m, 0, b]), mengentext([m // k, b]), mengentext([-(m // k), 0, -b])],
             f'{lin(k, -m)} = 0 für x = {zt(m // k)}; x({lin(1, -b)}) = 0 für x = 0 oder x = {zt(b)}. D = {mengentext([m // k, 0, b])}.',
             'Ein Produkt im Nenner ist 0, wenn ein Faktor 0 ist.')


def g_ein_bruch(R, st):
    h = 'Multipliziere mit dem Nenner und löse dann die lineare Gleichung.'
    while True:
        vorlage = R.choice(['bruch_zahl', 'zahl_bruch'] if st == 1 else ['bruch_zahl', 'zahl_bruch', 'faktor'])
        if st == 1:
            x = Fr(R.choice([j for j in range(-12, 13) if j])); c = Fr(R.choice([2, 3, 4, 5, -2, -3]))
            a = c * x; b = 0
            text = f'{zt(a)}/x = {zt(c)}' if vorlage == 'bruch_zahl' else f'{zt(c)} = {zt(a)}/x'
            weg = f'D = ℚ \\ {{0}}. · x: {zt(a)} = {zt(c)}x → x = {zt(a)} : {kl(c)} = {zt(x)}. Umkehrfrage: {zt(a)} geteilt durch {zt(x)} ergibt {zt(c)}.'
            cc = f'{cz(a)} / {cz(c)}'
        elif st == 2 and vorlage == 'faktor':
            k = R.choice([2, 3, 4, 5]); c = Fr(R.choice([2, 3, 4, 6, -2, -3])); x = Fr(R.choice([j for j in range(-9, 10) if j]))
            a = c * k * x
            text = f'{zt(a)}/({k}x) = {zt(c)}'
            weg = f'D = ℚ \\ {{0}}. · {k}x: {zt(a)} = {zt(c * k)}x → x = {zt(a)} : {kl(c * k)} = {zt(x)}.'
            cc = f'{cz(a)} / ({cz(c)} * {k})'
        elif st == 2:
            b = R.choice([j for j in range(-9, 10) if j]); c = Fr(R.choice([2, 3, 4, 5, -2, -4])); x = Fr(R.randint(-10, 12))
            if x == -b or x + b == 0: continue
            a = c * (x + b)
            text = f'{zt(a)}/{N(1, b)} = {zt(c)}' if vorlage == 'bruch_zahl' else f'{zt(c)} = {zt(a)}/{N(1, b)}'
            weg = (f'D = ℚ \\ {{{zt(-b)}}}. · {N(1, b)}: {zt(a)} = {zt(c)}({lin(1, b)}) = {lin(c, c * b)} → {lin(c, 0)} = {zt(a - c * b)} → x = {zt(x)}. '
                   f'Umkehrfrage: {zt(a)} geteilt durch {zt(x + b)} ergibt {zt(c)}, also {lin(1, b)} = {zt(x + b)}.')
            cc = f'({cz(a)} - ({cz(c * b)})) / {cz(c)}'
        elif R.random() < .4:
            # x im Zähler mit Faktor: (k·x + a0)/(x − b) = c
            k = R.choice([2, 3, 4]); a0, b = R.randint(-9, 9), R.choice([j for j in range(-9, 10) if j]); c = Fr(R.choice([1, 5, 6, -1, -2]))
            if c == k or a0 == 0: continue
            x = (c * b + a0) / (c - k)
            if x == b or not ist_endlich(x) or abs(x) > 50 or len(zt(x)) > 6: continue
            text = f'({lin(k, a0)})/{N(1, -b)} = {zt(c)}'
            weg = f'D = ℚ \\ {{{zt(b)}}}. · {N(1, -b)}: {lin(k, a0)} = {lin(c, -c * b)} → {lin(k - c, 0)} = {zt(-c * b - a0)} → x = {zt(x)}. {zt(x)} liegt in D.'
            cc = f'({cz(c * b)} + ({a0})) / ({cz(c)} - {k})'
        else:
            a0, b = R.randint(-9, 9), R.choice([j for j in range(-9, 10) if j]); c = Fr(R.choice([2, 3, 4, 5, -1, -2, -3]))
            if c == 1: continue
            x = (c * b + a0) / (c - 1)
            if x == b or not ist_endlich(x) or abs(x) > 50 or a0 == 0: continue
            text = f'{N(1, a0)}/{N(1, -b)} = {zt(c)}'
            weg = (f'D = ℚ \\ {{{zt(b)}}}. · {N(1, -b)}: {lin(1, a0)} = {lin(c, -c * b)} → {lin(1 - c, 0) if 1 - c != 0 else "0"} = {zt(-c * b - a0)} → x = {zt(x)}.')
            cc = f'({cz(c * b)} + ({a0})) / ({cz(c)} - 1)'
        if st != 3 or x != b: break
    return Z(f'Löse {text}.', x, cc, weg, h)


def g_ueber_kreuz(R, st):
    h = 'Bestimme zuerst D. Dann über Kreuz multiplizieren und die lineare Gleichung lösen.'
    while True:
        if st == 1:
            a, c, d = R.randint(1, 9), R.randint(1, 9), R.choice([j for j in range(-9, 10) if j])
            if a == c: continue
            x = Fr(a * d, c - a)
            text = f'{a}/x = {c}/{N(1, d)}'
            ex = [0, -d]
            weg = f'Über Kreuz: {a}({lin(1, d)}) = {lin(c, 0)} → {lin(a, a * d)} = {lin(c, 0)} → {zt(a * d)} = {lin(c - a, 0)} → x = {zt(x)}.'
            cc = f'{a} * ({d}) / ({c} - {a})'
        elif st == 2:
            a, c = R.randint(1, 9), R.randint(1, 9); b, d = R.sample([j for j in range(-9, 10) if j], 2)
            if a == c: continue
            x = Fr(c * b - a * d, a - c)
            text = f'{a}/{N(1, b)} = {c}/{N(1, d)}'
            ex = [-b, -d]
            weg = f'Über Kreuz: {a}({lin(1, d)}) = {c}({lin(1, b)}) → {lin(a, a * d)} = {lin(c, c * b)} → {lin(a - c, 0)} = {zt(c * b - a * d)} → x = {zt(x)}.'
            cc = f'({c} * ({b}) - {a} * ({d})) / ({a} - {c})'
        else:
            a, b, c, d = [R.choice([j for j in range(-8, 9) if j]) for _ in range(4)]
            if a + d - c - b == 0 or len({b, d}) < 2: continue
            x = Fr(c * b - a * d, a + d - c - b)
            text = f'{N(1, a)}/{N(1, b)} = {N(1, c)}/{N(1, d)}'
            ex = [-b, -d]
            weg = (f'Über Kreuz: ({lin(1, a)})({lin(1, d)}) = ({lin(1, c)})({lin(1, b)}). Ausmultiplizieren: {quad1(a + d, a * d)} = {quad1(c + b, c * b)}. '
                   f'x² fällt weg: {lin(a + d - c - b, 0)} = {zt(c * b - a * d)} → x = {zt(x)}.')
            cc = f'({c} * ({b}) - ({a}) * ({d})) / (({a}) + ({d}) - ({c}) - ({b}))'
        if x not in ex and ist_endlich(x) and abs(x) <= 60 and len(zt(x)) <= 6: break
    weg = f'D = {mengentext(ex)}. ' + weg.replace(' → x → x =', ' → x =')
    weg = re_doppelt(weg) + f' {zt(x)} liegt in D.'
    return Z(f'Löse {text}.', x, cc, weg, h)


def re_doppelt(w):
    """„… → x = 47 → x = 47.“ und „x = 47 → x = 47“ vermeiden."""
    import re
    return re.sub(r'(x = [^ →]+) → \1\.', r'\1.', w)


def g_hauptnenner(R, st):
    h = 'Bestimme den Hauptnenner und multipliziere jedes Glied damit.'
    while True:
        if st == 1:
            a, b, c = R.randint(1, 12), R.randint(1, 12), R.choice([1, 2, 3, 4, 5])
            x = Fr(a + b, c)
            text = f'{a}/x + {b}/x = {c}'
            weg = f'HN = x. · x: {a} + {b} = {lin(c, 0)} → ' + (f'x = {a + b} : {c} = {zt(x)}.' if c != 1 else f'x = {a + b}.')
            cc = f'({a} + {b}) / {c}'
        elif st == 2:
            a, b, k, c = R.randint(1, 9), R.randint(1, 9), R.choice([2, 3, 4, 5]), R.choice([1, 2, 3, 4, -1, -2])
            op = R.choice(['+', '−'])
            z = k * a + b if op == '+' else k * a - b
            x = Fr(z, c * k)
            text = f'{a}/x {op} {b}/({k}x) = {zt(c)}'
            weg = f'HN = {k}x. · {k}x: {k * a} {op} {b} = {lin(c * k, 0)} → {zt(z)} = {lin(c * k, 0)} → x = {zt(x)}.'
            cc = f'({k} * {a} {"+" if op == "+" else "-"} {b}) / ({c} * {k})'
        elif R.random() < .35:
            t1, t2 = R.choice([(12, 6), (6, 3), (10, 15), (12, 4), (20, 30), (6, 12), (8, 24), (15, 10), (9, 18), (12, 12)])
            x = Fr(t1 * t2, t1 + t2)
            if not ist_endlich(x) or len(zt(x)) > 5: continue
            kontext = R.choice([('Ein Wasserhahn füllt eine Wanne allein in {a} Minuten, ein zweiter in {b} Minuten. Wie viele Minuten dauert es mit beiden zusammen?', 'min'),
                                ('Zwei Kinder streichen einen Zaun. Das erste bräuchte allein {a} Stunden, das zweite {b} Stunden. Wie lange brauchen sie zusammen (in Stunden)?', 'h'),
                                ('Zwei Pumpen leeren einen Teich. Die erste allein schafft es in {a} Stunden, die zweite in {b} Stunden. Wie lange dauert es mit beiden (in Stunden)?', 'h')])
            text_s = kontext[0].format(a=t1, b=t2) + f' Löse 1/{t1} + 1/{t2} = 1/x.'
            return Z(text_s, x, f'{t1} * {t2} / ({t1} + {t2})',
                     f'HN = {t1 * t2 // __import__("math").gcd(t1, t2)}x. In einer Zeiteinheit schafft der erste 1/{t1}, der zweite 1/{t2} der Arbeit. '
                     f'1/{t1} + 1/{t2} = {bruch(Fr(1, t1) + Fr(1, t2))} = 1/x → x = {zt(x)} {kontext[1]}.',
                     'Jeder schafft pro Minute bzw. Stunde einen Bruchteil der Arbeit. Zusammen schaffen sie die Summe davon.', einheit=kontext[1])
        else:
            if R.random() < .5:
                a, b, c = R.randint(1, 9), R.randint(1, 9), R.choice([1, 2, 3, 4, 6])
                x = Fr(3 * a + 2 * b, 6 * c)
                text = f'{a}/(2x) + {b}/(3x) = {c}'
                weg = f'HN = 6x. · 6x: {3 * a} + {2 * b} = {6 * c}x → x = {3 * a + 2 * b} : {6 * c} = {zt(x)}.'
                cc = f'(3 * {a} + 2 * {b}) / (6 * {c})'
            else:
                a, b, c, d = R.randint(2, 12), R.randint(1, 9), R.choice([1, 2, 3, 4, -1, -2]), R.choice([j for j in range(-5, 6) if j])
                if a == b: continue
                x = Fr(a - b, c) - d
                sg = '+' if c > 0 else '−'
                text = f'{a}/{N(1, d)} = {b}/{N(1, d)} {sg} {zt(abs(c))}'
                weg = (f'HN = {lin(1, d)}. · {N(1, d)}: {a} = {b} {sg} {"" if abs(c) == 1 else zt(abs(c))}({lin(1, d)}) → {a - b} = {lin(c, c * d)} → '
                       + (f'{lin(c, 0)} = {zt(a - b - c * d)} → ' if c != 1 else '') + f'x = {zt(x)}.')
                cc = f'({a} - {b}) / ({c}) - ({d})'
                if x == -d: continue
        if x != 0 and ist_endlich(x) and len(zt(x)) <= 6: break
    return Z(f'Löse {text}.', x, cc, weg, h)


def g_scheinloesung(R, st):
    if st >= 2 and R.random() < .25:
        b = R.choice([j for j in range(-8, 9) if j]); a = R.choice([j for j in range(-8, 9) if j and j != -b])
        c = a + b
        if c == 0: return g_scheinloesung(R, st)
        text = f'{N(1, a)}/{N(1, -b)} = {zt(c)}/{N(1, -b)}'
        return A(R, f'Warum ist x = {zt(b)} keine Lösung von {text}, obwohl die Rechnung x = {zt(b)} ergibt?',
                 f'Für x = {zt(b)} ist der Nenner 0, die Gleichung ist dort nicht definiert.',
                 ['Weil man falsch gerechnet hat.', f'Weil {zt(b)} {"positiv" if b > 0 else "negativ"} ist.', f'Weil {zt(b)} nicht im Zähler vorkommt.'],
                 f'D = ℚ \\ {{{zt(b)}}}: Für x = {zt(b)} wird {lin(1, -b)} = 0. Die Rechnung ist richtig, aber {zt(b)} ist eine Scheinlösung. L = {{ }}.',
                 'Setze die Zahl in den Nenner ein.')
    a, b = R.choice([j for j in range(-8, 9) if j]), R.choice([j for j in range(-8, 9) if j])
    if a == -b: return g_scheinloesung(R, st)
    schein = R.random() < (.6 if st >= 2 else .5)
    c = a + b if schein else R.choice([j for j in range(-12, 13) if j not in (a + b, 0)])
    if c == 0: return g_scheinloesung(R, st)
    x = c - a
    if st == 3 and R.random() < .5:
        # Variante mit Faktor im Zähler
        k = R.choice([2, 3, 4])
        c = k * b if schein else R.choice([j for j in range(-12, 13) if j not in (k * b, 0)])
        x = Fr(c, k)
        if not schein and (not ist_endlich(x) or x == b): return g_scheinloesung(R, st)
        text = f'{k}x/{N(1, -b)} = {zt(c)}/{N(1, -b)}'
        weg0 = f'D = ℚ \\ {{{zt(b)}}}. · {N(1, -b)}: {k}x = {zt(c)} → x = {zt(x)}.'
    else:
        if not schein and x == b: return g_scheinloesung(R, st)
        text = f'{N(1, a)}/{N(1, -b)} = {zt(c)}/{N(1, -b)}'
        weg0 = f'D = ℚ \\ {{{zt(b)}}}. · {N(1, -b)}: {lin(1, a)} = {zt(c)} → x = {zt(x)}.'
    if x == b:
        richtig, falsch = 'L = { }', [f'L = {{{zt(b)}}}', f'L = {{{zt(-b)}}}', 'L = ℚ']
        weg = weg0 + f' {zt(b)} liegt nicht in D, also Scheinlösung: L = {{ }}.'
    else:
        richtig, falsch = f'L = {{{zt(x)}}}', ['L = { }', f'L = {{{zt(b)}}}', f'L = {{{zt(-x)}}}' if x else 'L = {1}']
        weg = weg0 + f' {zt(x)} liegt in D: L = {{{zt(x)}}}.'
    return A(R, f'Gib die Lösungsmenge von {text} an.', richtig, falsch, weg,
             'Bestimme zuerst D. Prüfe am Ende, ob deine Lösung in D liegt.')


def g_verhaeltnis(R, st):
    h = 'Produktgleichheit: Außenglieder mal = Innenglieder mal.'
    if st == 1:
        while True:
            a, b, c = R.randint(2, 15), R.randint(2, 20), R.randint(2, 10)
            x = Fr(a * b, c)
            if ist_endlich(x) and len(zt(x)) <= 5 and a != c and b != c: break
        return Z(f'Löse die Verhältnisgleichung x : {a} = {b} : {c}.', x, f'{a} * {b} / {c}',
                 f'{c}x = {a} · {b} = {a * b} → x = {a * b} : {c} = {zt(x)}.', h)
    if st == 2 and R.random() < .4:
        art = R.choice(['saft', 'beton', 'farbe'])
        if art == 'saft':
            a, b = R.choice([(1, 4), (1, 3), (1, 5), (2, 3)]); m = R.choice([100, 150, 200, 250, 300])
            x = Fr(m * b, a)
            return Z(f'Saft und Wasser werden im Verhältnis {a} : {b} gemischt. Wie viel Wasser (in ml) brauchst du für {m} ml Saft?', x, f'{m} * {b} / {a}',
                     f'Saft : Wasser = {a} : {b} = {m} : x → {a}x = {m * b} → x = {zt(x)} ml.', 'Stelle die Verhältnisgleichung Saft : Wasser auf.', einheit='ml')
        if art == 'beton':
            a, b = R.choice([(1, 5), (1, 4), (1, 3)]); k = R.choice([15, 20, 30, 40, 60])
            x = Fr(k * a, b)
            if not ist_endlich(x): return g_verhaeltnis(R, st)
            return Z(f'Für Beton mischt man Zement und Kies im Verhältnis {a} : {b}. Wie viel kg Zement braucht man für {k} kg Kies?', x, f'{k} * {a} / {b}',
                     f'Zement : Kies = {a} : {b} = x : {k} → {b}x = {k * a} → x = {zt(x)} kg.', 'Zement steht vorne, Kies hinten – in beiden Verhältnissen gleich.', einheit='kg')
        a, b = R.choice([(2, 3), (3, 5), (1, 2), (3, 4)]); w = R.choice([6, 9, 12, 15, 20])
        x = Fr(w * a, b)
        if not ist_endlich(x): return g_verhaeltnis(R, st)
        return Z(f'Für ein Grün mischt man gelbe und blaue Farbe im Verhältnis {a} : {b}. Wie viele Liter gelbe Farbe braucht man für {w} Liter blaue?', x, f'{w} * {a} / {b}',
                 f'Gelb : Blau = {a} : {b} = x : {w} → {b}x = {w * a} → x = {zt(x)} l.', 'Stelle die Verhältnisgleichung Gelb : Blau auf.', einheit='l')
    if st == 2:
        while True:
            a, b, c = R.randint(2, 15), R.randint(2, 12), R.randint(2, 20)
            x = Fr(a * c, b)
            if ist_endlich(x) and len(zt(x)) <= 5: break
        return Z(f'Löse die Verhältnisgleichung {a} : x = {b} : {c}.', x, f'{a} * {c} / {b}',
                 f'Außenglieder: {a} · {c} = {a * c}. Innenglieder: {b}x. Also x = {a * c} : {b} = {zt(x)}.', h)
    art = R.choice(['rezept', 'karte', 'mischung', 'gleichung'])
    if art == 'rezept':
        p1, m1 = R.choice([4, 6, 8]), R.choice([200, 250, 300, 400, 500, 600])
        p2 = R.choice([j for j in (2, 3, 5, 9, 10, 12) if j != p1])
        x = Fr(m1 * p2, p1)
        if not ist_endlich(x): return g_verhaeltnis(R, st)
        return Z(f'Für {p1} Personen braucht man {m1} g Mehl. Wie viel Mehl braucht man für {p2} Personen?', x, f'{m1} * {p2} / {p1}',
                 f'x : {p2} = {m1} : {p1} → {p1}x = {m1 * p2} → x = {zt(x)} g.', 'Stelle eine Verhältnisgleichung auf: Mehl : Personen.', einheit='g')
    if art == 'karte':
        M = R.choice([10000, 20000, 25000, 50000])
        cm = Fr(R.choice([2, 3, 4, 5, 6, 8, 12, 15]), R.choice([1, 2]))
        km = cm * M / 100000
        return Z(f'Eine Karte hat den Maßstab 1 : {zt(M)}. Zwei Orte sind auf der Karte {zt(cm)} cm voneinander entfernt. Wie weit sind sie in Wirklichkeit entfernt (in km)?', km,
                 f'{cz(cm)} * {M} / 100000', f'1 : {zt(M)} = {zt(cm)} : x → x = {zt(cm * M)} cm = {zt(km)} km.', 'Rechne erst in cm, dann in km um (1 km = 100 000 cm).', einheit='km')
    if art == 'mischung':
        a, b = R.choice([(1, 3), (1, 4), (2, 3), (1, 5), (2, 5), (3, 4)])
        gesamt = (a + b) * R.choice([50, 100, 150, 200, 250])
        x = Fr(gesamt * a, a + b)
        return Z(f'Saftschorle wird im Verhältnis Saft : Wasser = {a} : {b} gemischt. Wie viel Saft (in ml) braucht man für {gesamt} ml Schorle?', x,
                 f'{gesamt} * {a} / ({a} + {b})', f'Saft : Gesamt = {a} : {a + b}. x : {gesamt} = {a} : {a + b} → x = {zt(x)} ml.',
                 'Saft und Wasser zusammen sind die Gesamtmenge: Saft : Gesamt = a : (a + b).', einheit='ml')
    while True:
        a, b, c = R.randint(2, 9), R.randint(2, 9), R.choice([j for j in range(-8, 9) if j])
        x = Fr(a * c, b - a) if b != a else None
        if x is not None and ist_endlich(x) and len(zt(x)) <= 5: break
    return Z(f'Löse die Verhältnisgleichung x : {a} = {N(1, c)} : {b}.', x, f'{a} * ({c}) / ({b} - {a})',
             f'{b}x = {a}({lin(1, c)}) = {lin(a, a * c)} → {lin(b - a, 0)} = {zt(a * c)} → x = {zt(x)}.', h)


def hyp_name(a, p, c=0):
    n = f'{zt(a)}/{"x" if p == 0 else "(" + lin(1, -p) + ")"}'
    return f'y = {n}' + (f' {"+" if c > 0 else "−"} {zt(abs(c))}' if c else '')


def g_graphisch(R, st):
    h = 'Suche den Schnittpunkt der Graphen. Die Lösung ist sein x-Wert.'
    if st == 1:
        # a/(x − p) = c mit waagrechter Gerade
        while True:
            p, c = R.randint(-3, 3), R.choice([-3, -2, -1, 1, 2, 3, 4])
            d = R.choice([j for j in range(-4, 5) if j])          # x0 − p
            a = c * d; x0 = p + d
            if abs(x0) <= 6 and a != 0: break
        gr = {'typ': 'koordinaten', 'x': [-7, 7], 'y': [-6, 6],
              'graphen': [{'art': 'hyperbel', 'a': a, 'b': -p, 'c': 0, 'name': hyp_name(a, p)}, {'art': 'linear', 'm': 0, 't': c, 'name': f'y = {zt(c)}'}]}
        G = f'{zt(a)}/{"x" if p == 0 else "(" + lin(1, -p) + ")"} = {zt(c)}'
        return mit_bild(A(R, f'Lies die Lösung von {G} am Schnittpunkt ab.', f'x = {zt(x0)}',
                          [f'x = {zt(c)}' if c != x0 else f'x = {zt(-x0)}', f'x = {zt(p)}' if p != x0 else f'x = {zt(x0 + 1)}', f'x = {zt(a)}' if a != x0 else f'x = {zt(-a)}'],
                          f'Die Hyperbel trifft die Gerade y = {zt(c)} bei x = {zt(x0)}. Probe: {zt(a)} : {kl(x0 - p)} = {zt(c)} ✓', h), gr)
    if st == 2:
        # a/x = x + t mit zwei Schnittpunkten
        while True:
            r1, r2 = R.sample([j for j in range(-5, 6) if j], 2)
            a, t = -r1 * r2, -(r1 + r2)
            if a != 0 and abs(a) <= 12 and all(abs(r + t) <= 6 for r in (r1, r2)): break
        r1, r2 = sorted((r1, r2))
        gr = {'typ': 'koordinaten', 'x': [-6, 6], 'y': [-7, 7],
              'graphen': [{'art': 'hyperbel', 'a': a, 'b': 0, 'c': 0, 'name': hyp_name(a, 0)}, {'art': 'linear', 'm': 1, 't': t, 'name': f'y = {lin(1, t)}'}]}
        G = f'{zt(a)}/x = {lin(1, t)}'
        y1, y2 = r1 + t, r2 + t
        if R.random() < .35:
            gr['punkte'] = [{'x': r1, 'y': y1}, {'x': r2, 'y': y2}]
            return mit_bild(Z(f'Die Graphen zu {G} schneiden sich zweimal. Gib die größere Lösung an.', r2, f'{r2}',
                              f'Schnittpunkte ({zt(r1)} | {zt(y1)}) und ({zt(r2)} | {zt(y2)}). Lösungen x = {zt(r1)} und x = {zt(r2)}; die größere ist {zt(r2)}. '
                              f'Probe: {zt(a)} : {kl(r2)} = {zt(Fr(a, r2))} und {zt(r2)} {"+" if t >= 0 else "−"} {zt(abs(t))} = {zt(y2)} ✓', h), gr)
        richtig = f'L = {{{zt(r1)}; {zt(r2)}}}'
        falsch = [f'L = {{{"; ".join(zt(v) for v in sorted({y1, y2}))}}}' if {y1, y2} != {r1, r2} else f'L = {{{zt(-r2)}; {zt(-r1)}}}',
                  f'L = {{{zt(r2)}}}', f'L = {{{zt(-r2)}; {zt(-r1)}}}' if {-r1, -r2} != {r1, r2} else f'L = {{{zt(r1)}}}']
        return mit_bild(A(R, f'Löse {G} mit den Graphen.', richtig, falsch,
                          f'Schnittpunkte ({zt(r1)} | {zt(y1)}) und ({zt(r2)} | {zt(y2)}). Die x-Werte sind die Lösungen: {richtig}.', h), gr)
    # Stufe 3: Anzahl der Lösungen / keine Lösung an der Asymptote
    art = R.choice(['asymptote', 'eine', 'zwei'])
    a = R.choice([2, 3, 4, 6, -2, -4])
    c = R.choice([-2, -1, 1, 2])
    gr = {'typ': 'koordinaten', 'x': [-6, 6], 'y': [-6, 6], 'graphen': [{'art': 'hyperbel', 'a': a, 'b': 0, 'c': c, 'name': hyp_name(a, 0, c)}]}
    G0 = f'{zt(a)}/x {"+" if c > 0 else "−"} {zt(abs(c))}'
    if art == 'asymptote':
        gr['graphen'].append({'art': 'linear', 'm': 0, 't': c, 'name': f'y = {zt(c)}'})
        n, w = 0, f'Die Hyperbel kommt der Geraden y = {zt(c)} beliebig nahe, trifft sie aber nie: {zt(a)}/x wäre 0, das geht nicht. L = {{ }}.'
        G = f'{G0} = {zt(c)}'
    elif art == 'eine':
        k = R.choice([j for j in range(-4, 5) if j and j != c])
        if (k - c) == 0 or Fr(a, k - c).denominator != 1: return g_graphisch(R, st)
        gr['graphen'].append({'art': 'linear', 'm': 0, 't': k, 'name': f'y = {zt(k)}'})
        n, w = 1, f'Die waagrechte Gerade y = {zt(k)} schneidet die Hyperbel genau einmal, bei x = {zt(Fr(a, k - c))}.'
        G = f'{G0} = {zt(k)}'
    else:
        # Gerade y = −x·sign(a) … : a/x + c = m·x + c, zwei Schnittpunkte, wenn a/m > 0
        m = 1 if a > 0 else -1
        gr['graphen'].append({'art': 'linear', 'm': m, 't': c, 'name': f'y = {lin(m, c)}'})
        n, w = 2, f'Die Gerade y = {lin(m, c)} schneidet beide Äste der Hyperbel: zwei Schnittpunkte, also zwei Lösungen.'
        G = f'{G0} = {lin(m, c)}'
    return mit_bild(A(R, f'Wie viele Lösungen hat die Gleichung {G}? Entscheide am Bild.', f'{n} Lösung{"en" if n != 1 else ""}',
                      [f'{k} Lösung{"en" if k != 1 else ""}' for k in (0, 1, 2) if k != n] + ['unendlich viele Lösungen'], w,
                      'Zähle die Schnittpunkte der beiden Graphen.'), gr)


GEN = {'definitionsmenge': g_definitionsmenge, 'ein_bruch': g_ein_bruch, 'ueber_kreuz': g_ueber_kreuz, 'hauptnenner': g_hauptnenner,
       'scheinloesung': g_scheinloesung, 'verhaeltnis': g_verhaeltnis, 'graphisch': g_graphisch}


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl8.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl8 import mit_umbau  # noqa: E402

def _hn(a, b, c):
    return {'typ': 'tabelle', 'kopf': ['Glied', 'mal', 'ergibt'], 'zeilen': [['5/x', '2x', a], ['1/(2x)', '2x', b], ['2', '2x', c]]}


def _pf(m):
    return {'typ': 'tabelle', 'kopf': ['', 'Rezept', 'du'], 'zeilen': [['Eier', '4', '6'], ['Mehl (EL)', '10', m]]}


UMBAU = {
 'definitionsmenge': {
  'einstieg': 'Bei einer Bruchgleichung steht x im Nenner, etwa 2/(x − 1) = 3/(x + 4). Ein Nenner darf nie 0 werden. Darum streichst du zuerst verbotene Zahlen aus der ⟦Definitionsmenge⟧.',
  'woerter': [['Bruchgleichung', 'eine Gleichung mit x im Nenner'], ['Definitionsmenge', 'alle Zahlen, die man für x einsetzen darf'], ['ℚ \\ {−4; 1}', 'alle Bruchzahlen außer −4 und 1']],
  'bild': {'typ': 'zahlenstrahl', 'start': -6, 'ende': 4, 'abschnitte': 10, 'beschriftet': 'alle'},
  'schritte': [{'text': 'Linker Nenner: x − 1 = 0 bei x = 1. Die 1 ist verboten.', 'bild': {'punkte': [{'wert': 1, 'name': '1 verboten'}]}},
               {'text': 'Rechter Nenner: x + 4 = 0 bei x = −4. Auch verboten.', 'bild': {'punkte': [{'wert': -4, 'name': '−4 verboten'}, {'wert': 1, 'name': '1 verboten'}]}},
               {'text': 'Also ⟦D = ℚ \\ {−4; 1}⟧.'}],
  'fehler': 'Nur x = 1 auszuschließen reicht nicht. ⟦Jeder⟧ Nenner zählt, auch der auf der rechten Seite.',
  'fehler_bild': {'punkte': [{'wert': -4, 'name': 'vergessen!'}, {'wert': 1, 'name': '1 verboten'}]},
  'regel': 'Setze ⟦jeden Nenner gleich 0⟧ und streiche diese Zahlen. Das machst du, bevor du rechnest.'},
 'ein_bruch': {
  'einstieg': 'Ein Bus kostet 600 €, jedes Kind zahlt 25 €. Wie viele Kinder fahren mit? Die Gleichung heißt 600/x = 25. Dafür musst du den Nenner ⟦wegmultiplizieren⟧.',
  'woerter': [['wegmultiplizieren', 'beide Seiten mit dem Nenner malnehmen – dann ist der Bruch weg']],
  'bild': {'typ': 'koordinaten', 'x': [0, 40], 'y': [0, 100], 'graphen': [{'art': 'hyperbel', 'a': 600, 'b': 0, 'c': 0, 'name': '600/x', 'bereich': [6, 40]}], 'schritt_x': 5, 'schritt_y': 25, 'name_x': 'Kinder', 'name_y': '€'},
  'schritte': [{'text': 'Zuerst D: x darf nicht 0 sein.'},
               {'text': 'Beide Seiten mal x: 600 = 25 · x. Der Bruch ist weg.', 'bild': {'waagrecht': [25]}},
               {'text': 'Durch 25 teilen: ⟦x = 24⟧. 24 Kinder fahren mit.', 'bild': {'punkte': [{'x': 24, 'y': 25, 'name': '(24 | 25)'}], 'senkrecht': [24]}},
               {'text': 'Kontrolle: 600 : 24 = 25. Und 24 liegt in D.'}],
  'fehler': 'Aus 12/(x − 2) = 3 wird nicht 12 = 3x − 2. Der ganze Nenner wird malgenommen: 3 · (x − 2) = ⟦3x − 6⟧.',
  'regel': 'Beide Seiten ⟦mit dem Nenner malnehmen⟧, dann weiter wie gewohnt lösen. Zum Schluss prüfen, ob die Lösung in D liegt.'},
 'ueber_kreuz': {
  'einstieg': '2/3 und 4/6 sind gleich groß, denn 2 · 6 und 3 · 4 ergeben beide 12. Dieses Malnehmen geht auch mit x im Nenner. Es heißt ⟦über Kreuz multiplizieren⟧.',
  'woerter': [['über Kreuz multiplizieren', 'Zähler links mal Nenner rechts = Zähler rechts mal Nenner links'], ['ausmultiplizieren', 'die Klammer auflösen: 4(x − 3) = 4x − 12']],
  'bild': {'typ': 'bruchstreifen', 'teile': 3, 'gefaerbt': 2, 'teil_text': '2/3', 'zeilen': [{'teile': 6, 'gefaerbt': 4}]},
  'schritte': [{'text': 'Aufgabe: 4/(x + 1) = 2/(x − 3). Verboten sind −1 und 3.'},
               {'text': 'Über Kreuz: 4 · (x − 3) = 2 · (x + 1).'},
               {'text': 'Ausmultiplizieren: 4x − 12 = 2x + 2.'},
               {'text': '2x abziehen, 12 dazuzählen: 2x = 14, also ⟦x = 7⟧.'}],
  'fehler': 'Jeden Zähler mit dem ⟦eigenen⟧ Nenner malnehmen ist falsch. Über Kreuz heißt: Zähler links mal Nenner rechts.',
  'regel': 'Steht je Seite ein Bruch: ⟦über Kreuz multiplizieren⟧. Aus a/b = c/d wird a · d = c · b. Bei Summen geht das nicht.'},
 'hauptnenner': {
  'einstieg': 'Stehen mehrere Brüche in einer Gleichung, nimmst du alles mit einem Term mal, in den jeder Nenner passt. Dann verschwinden alle Brüche auf einmal. Dieser Term ist der ⟦Hauptnenner⟧.',
  'woerter': [['Hauptnenner', 'ein Term, in den alle Nenner hineinpassen'], ['Glied', 'ein Teil der Gleichung, abgetrennt durch + oder −']],
  'bild': _hn('?', '?', '?'),
  'schritte': [{'text': 'Aufgabe 5/x + 1/(2x) = 2. Beide Nenner passen in 2x.'},
               {'text': 'Jedes Glied mal 2x: 10 + 1 = 4x.', 'bild': _hn('10', '1', '4x')},
               {'text': 'Also 11 = 4x. Durch 4 teilen: ⟦x = 2,75⟧.'}],
  'fehler': 'Die 2 rechts wird auch mit 2x malgenommen. Wer sie vergisst, erhält 10 + 1 = 2 – ganz ohne x, also ⟦Unsinn⟧.',
  'fehler_bild': _hn('10', '1', '2 ?'),
  'regel': '⟦Jedes Glied⟧ auf beiden Seiten mit dem Hauptnenner malnehmen. Danach steht kein Bruch mehr da.'},
 'scheinloesung': {
  'einstieg': 'Ergibt eine Rechnung „0 Kinder fahren mit“, müsste jedes 600/0 € zahlen – Unsinn. Auch Bruchgleichungen liefern manchmal eine verbotene Zahl. Sie heißt ⟦Scheinlösung⟧.',
  'woerter': [['Scheinlösung', 'eine errechnete Zahl, die nicht in D liegt'], ['L = { }', 'leere Lösungsmenge: Es gibt keine Lösung']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 6, 'abschnitte': 6, 'beschriftet': 'alle', 'punkte': [{'wert': 3, 'name': '3 verboten'}]},
  'schritte': [{'text': 'Aufgabe (x + 1)/(x − 3) = 4/(x − 3). x darf nicht 3 sein.'},
               {'text': 'Beide Seiten mal (x − 3): x + 1 = 4, also x = 3.', 'bild': {'punkte': [{'wert': 3, 'name': 'x = 3?'}]}},
               {'text': 'Die 3 ist verboten, also eine Scheinlösung. Es gilt ⟦L = { }⟧.'}],
  'fehler': 'L = {3} ist falsch: Für x = 3 wird der Nenner 0. Darum bestimmst du D ⟦zuerst⟧.',
  'regel': 'Eine Zahl ist nur Lösung, wenn sie ⟦in D liegt⟧. Sonst ist sie eine Scheinlösung.'},
 'verhaeltnis': {
  'einstieg': 'Für Pfannkuchen nimmst du auf 4 Eier 10 Esslöffel Mehl. Du hast 6 Eier, das Verhältnis soll gleich bleiben. Das ergibt eine ⟦Verhältnisgleichung⟧.',
  'woerter': [['Verhältnisgleichung', 'zwei gleiche Verhältnisse: a : b = c : d'], ['Außenglieder', 'die äußeren Zahlen: x und 4 in x : 6 = 10 : 4'], ['Innenglieder', 'die inneren Zahlen: 6 und 10']],
  'bild': _pf('?'),
  'schritte': [{'text': 'Mehl zu Eiern bleibt gleich: x : 6 = 10 : 4.'},
               {'text': 'Außenglieder mal, Innenglieder mal: 4 · x = 6 · 10 = 60.'},
               {'text': 'Durch 4 teilen: ⟦x = 15⟧ Esslöffel Mehl.', 'bild': _pf('15')}],
  'fehler': 'x = 6 · 4 : 10 = 2,4 ist falsch – mehr Eier brauchen nicht weniger Mehl. Die Außenglieder gehören ⟦zusammen⟧.',
  'fehler_bild': _pf('2,4 ?'),
  'regel': 'Rechne ⟦Außenglieder mal Außenglieder = Innenglieder mal Innenglieder⟧. Aus a : b = c : d wird a · d = b · c.'},
 'graphisch': {
  'einstieg': 'Du kannst beide Seiten einer Gleichung zeichnen. Wo sich die Linien treffen, haben beide Seiten denselben Wert. Diese Stellen heißen ⟦Schnittpunkte⟧.',
  'woerter': [['Hyperbel', 'der Graph von y = 6/x, zwei geschwungene Äste'], ['Schnittpunkt', 'ein Punkt, der auf beiden Graphen liegt']],
  'bild': {'typ': 'koordinaten', 'x': [-6, 6], 'y': [-6, 6], 'graphen': [{'art': 'hyperbel', 'a': 6, 'b': 0, 'c': 0, 'name': '6/x', 'name_x': 1.5}, {'art': 'linear', 'm': 1, 't': -1, 'name': 'x − 1'}]},
  'schritte': [{'text': 'Aufgabe 6/x = x − 1. Links zeichnest du die Hyperbel, rechts die Gerade.'},
               {'text': 'Die Graphen schneiden sich in (3 | 2) und (−2 | −3).', 'bild': {'punkte': [{'x': 3, 'y': 2, 'name': '(3 | 2)'}, {'x': -2, 'y': -3, 'name': '(−2 | −3)'}]}},
               {'text': 'Gesucht ist x. Die Lösungen sind ⟦x = 3 und x = −2⟧.', 'bild': {'senkrecht': [3, -2]}}],
  'fehler': 'Nicht die y-Werte angeben: L = {2; −3} ist falsch. Gesucht sind die ⟦x-Werte⟧ der Schnittpunkte.',
  'fehler_bild': {'senkrecht': [], 'waagrecht': [2, -3]},
  'regel': 'Wo sich die Graphen ⟦schneiden⟧, sind beide Seiten gleich. Die x-Werte der Schnittpunkte sind die Lösungen.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---- SCHWER (Zehnte Runde: schwerere Aufgaben nach Prüfungsvorbild, siehe _schwer_kl8.py) ----
# Vorbilder (Typ und Niveau, nicht Wortlaut/Zahlen): Känguru 2014 Kl. 7/8 (Platzhalter in zwei Brüchen, Verhältnisgleichung),
# ISB-Lehrplanmaterial M 8.3 (G8: „über Kreuz multiplizieren“ begründen), Lernumgebung Uni Bayreuth (Textaufgaben, die auf Bruchgleichungen führen),
# BMT8 2024 (Rückwärts: Zahl ersetzen, damit eine Lösung herauskommt), BMT8 2025 (Maßstab: Volumen/Fläche), BMT10 2024 (Schnitt Hyperbel–Gerade),
# Schulaufgaben-Typ Kl. 8 (Hauptnenner aus x² − 4, Lösung mit D abgleichen).
from _schwer_kl8 import Neu, mit_schwer  # noqa: E402

SW = Neu(10_8_5)
_k = lambda **k: {'typ': 'koordinaten', **k}
_h = lambda a, b=0, c=0, **k: {'art': 'hyperbel', 'a': a, 'b': b, 'c': c, **k}

# definitionsmenge
SW.a('definitionsmenge', 2, 'Bestimme die Definitionsmenge von 3/(2x − 1) = 1/x.', 'ℚ \\ {0; 0,5}', ['ℚ \\ {0; 1}', 'ℚ \\ {0,5}', 'ℚ \\ {0; 2}'],
    '2x − 1 = 0 ⇔ x = 0,5. Der zweite Nenner ist x, also auch x ≠ 0.', 'Prüfe beide Nenner.')
SW.a('definitionsmenge', 2, 'Bestimme die Definitionsmenge von 5/x − 2/(x − 5) = 1/(3x).', 'ℚ \\ {0; 5}', ['ℚ \\ {5}', 'ℚ \\ {0; 3; 5}', 'ℚ \\ {−5; 0}'],
    'Nenner x, x − 5 und 3x. 3x = 0 gilt auch nur für x = 0. Ausgeschlossen: 0 und 5.', 'Wann wird 3x null?')
SW.a('definitionsmenge', 3, 'Bestimme die Definitionsmenge von 1/(x² − 2x) = 4/(x − 2).', 'ℚ \\ {0; 2}', ['ℚ \\ {2}', 'ℚ \\ {−2; 0}', 'ℚ \\ {0; 2; 4}'],
    'x² − 2x = x(x − 2) ist 0 für x = 0 und x = 2. Der zweite Nenner schließt auch 2 aus.', 'Klammere im ersten Nenner aus.', art='P')
SW.a('definitionsmenge', 3, 'Welche Gleichung hat die Definitionsmenge ℚ \\ {−3; 3}?', '2/(x − 3) = 5/(x + 3)', ['(x + 3)/(x − 3) = 1', 'x/3 = 3/x', '2/(x − 3) = 5'],
    'Nur bei 2/(x − 3) = 5/(x + 3) stehen x − 3 und x + 3 im Nenner. (x + 3)/(x − 3) schließt nur 3 aus, x/3 = 3/x nur 0.', 'Nur Nenner zählen, Zähler nicht.', art='P')
SW.z('definitionsmenge', 3, 'Für welchen Wert von a hat die Gleichung 2/(x − a) = 3/(x + 1) die Definitionsmenge ℚ \\ {−1}?', -1, '-1',
    'Ausgeschlossen sind a und −1. Damit nur −1 übrig bleibt, muss a = −1 sein (beide Nenner gleich).', 'Welche Zahlen schließen die beiden Nenner aus?', art='K')
SW.z('definitionsmenge', 3, 'Wie viele Zahlen schließt die Definitionsmenge von 1/x + 1/(x + 2) = 1/(2x) aus?', 2, '1 + 1',
    'Nenner x und 2x schließen beide nur 0 aus, x + 2 schließt −2 aus. D = ℚ \\ {−2; 0}: 2 Zahlen.', 'Gleiche ausgeschlossene Zahlen zählen nur einmal.', art='K')

# ein_bruch
SW.z('ein_bruch', 2, 'Löse 15/(2x) = 6.', 1.25, '15 / 12', '15 = 12x ⇔ x = 15 : 12 = 1,25. x = 1,25 liegt in D.', 'Multipliziere mit 2x.')
SW.z('ein_bruch', 2, 'Löse 7/(x − 1) = −0,5.', -13, '1 + 7 / (-0.5)', '7 = −0,5(x − 1) ⇔ x − 1 = −14 ⇔ x = −13.', 'Multipliziere mit (x − 1), dann teile durch −0,5.')
SW.z('ein_bruch', 3, 'Die Gleichung 6/(x + 2) = 2 hat die Lösung x = 1. Durch welche Zahl muss man die 6 ersetzen, damit x = 4 die Lösung ist?', 12, '2 * (4 + 2)',
    'x = 4 einsetzen: a/(4 + 2) = 2 ⇔ a/6 = 2 ⇔ a = 12. Probe: 12/6 = 2.', 'Setze x = 4 ein und bestimme die gesuchte Zahl.', art='P')
SW.z('ein_bruch', 3, 'Ein Geschenk für 180 € wird gleichmäßig auf alle Kinder einer Gruppe verteilt. Jedes Kind zahlt 7,50 €. Wie viele Kinder sind es?', 24, '180 / 7.5',
    'Bei x Kindern zahlt jedes 180/x €. 180/x = 7,5 ⇔ x = 180 : 7,5 = 24.', 'Stelle den Anteil pro Kind als Bruch mit x auf.', einheit='Kinder', art='P')
SW.a('ein_bruch', 3, 'Löse (2x + 1)/(x − 3) = 2.', 'L = { }', ['L = {3}', 'L = {−3,5}', 'L = ℚ \\ {3}'],
    'Mal (x − 3): 2x + 1 = 2x − 6 ⇔ 1 = −6. Das ist falsch für jedes x. Die Gleichung hat keine Lösung.', 'Nach dem Malnehmen fällt x weg. Was bleibt übrig?', art='K')
SW.z('ein_bruch', 3, 'Teilt man 30 durch eine Zahl und subtrahiert 2, erhält man die Hälfte des Quotienten „30 durch die Zahl“. Welche Zahl ist es?', 7.5, '15 / 2',
    '30/x − 2 = 15/x ⇔ 15/x = 2 ⇔ x = 7,5. Probe: 30 : 7,5 = 4, 4 − 2 = 2 = Hälfte von 4.', 'Übersetze Satz für Satz in eine Gleichung mit 30/x.', art='K')

# ueber_kreuz
SW.z('ueber_kreuz', 2, 'Löse 3/(2x) = 5/(x + 7).', 3, '21 / 7', '3(x + 7) = 5 · 2x ⇔ 3x + 21 = 10x ⇔ 21 = 7x ⇔ x = 3.', 'Über Kreuz multiplizieren.')
SW.z('ueber_kreuz', 2, 'Löse (x + 1)/4 = (x − 2)/3.', 11, '3 + 8', '3(x + 1) = 4(x − 2) ⇔ 3x + 3 = 4x − 8 ⇔ x = 11.', 'Auch hier hilft über Kreuz: Klammern setzen!')
SW.z('ueber_kreuz', 3, 'Für welche Zahl z gilt (z + 2)/10 = (12 + z)/30?', 3, '60 / 20',
    'Über Kreuz: 30(z + 2) = 10(12 + z) ⇔ 30z + 60 = 120 + 10z ⇔ 20z = 60 ⇔ z = 3. Probe: 5/10 = 15/30.', 'Multipliziere über Kreuz. Oder: erweitere den linken Bruch auf 30.', art='P')
SW.a('ueber_kreuz', 3, 'Warum darf man a/b = c/d (b, d ≠ 0) zu a · d = c · b umformen?', 'Man multipliziert beide Seiten mit b · d.',
    ['Weil man Zähler und Nenner vertauschen darf.', 'Weil gleiche Brüche immer gleiche Zähler haben.', 'Das gilt nur für positive Zahlen.'],
    'a/b · bd = ad und c/d · bd = cb. Beide Seiten werden mit derselben Zahl b · d (≠ 0) multipliziert – eine erlaubte Umformung.', 'Mit welchem Term musst du multiplizieren, damit beide Nenner verschwinden?', art='P')
SW.a('ueber_kreuz', 3, 'Tom rechnet 2/x = 3/(x + 1) + 1 über Kreuz: 2(x + 1) = 3x + 1. Was stimmt?', 'Falsch: Über Kreuz geht nur, wenn auf jeder Seite genau ein Bruch steht.',
    ['Richtig gerechnet.', 'Falsch: Es muss 2(x + 1) = 3x heißen.', 'Falsch: Es muss 2x = 3(x + 1) + 1 heißen.'],
    'Rechts steht eine Summe aus Bruch und 1. Richtig: mit x(x + 1) multiplizieren: 2(x + 1) = 3x + x(x + 1).', 'Steht auf der rechten Seite nur ein Bruch?', art='K')
SW.z('ueber_kreuz', 3, 'Für welchen Wert von a hat a/(x − 1) = 3/(x + 1) die Lösung x = 2?', 1, '3 * (2 - 1) / (2 + 1)', 'x = 2 einsetzen: a/1 = 3/3 = 1. Also a = 1.',
    'Setze die Lösung ein. Dann ist nur noch a unbekannt.', art='K')

# hauptnenner
SW.z('hauptnenner', 2, 'Löse 1/2 + 1/x = 5/6.', 3, '1 / (5/6 - 1/2)', 'Mal 6x: 3x + 6 = 5x ⇔ 6 = 2x ⇔ x = 3.', 'Hauptnenner ist 6x.')
SW.z('hauptnenner', 2, 'Löse 4/x − 1 = 3/x.', 1, '4 - 3', 'Mal x: 4 − x = 3 ⇔ x = 1.', 'Vergiss nicht, auch die 1 mit x zu multiplizieren.')
SW.z('hauptnenner', 3, 'Ein Becken wird über zwei Rohre gefüllt. Rohr A allein braucht 4 h, beide zusammen 2,4 h. Wie lange bräuchte Rohr B allein?', 6, '1 / (1 / 2.4 - 1 / 4)',
    'Pro Stunde: 1/4 + 1/x = 1/2,4. 1/2,4 = 5/12, also 1/x = 5/12 − 3/12 = 2/12 ⇔ x = 6.', 'Rechne mit „Teil des Beckens pro Stunde“.', einheit='h', art='P')
SW.z('hauptnenner', 3, 'Löse 3/(x − 2) + 1/(x + 2) = 4/(x² − 4).', 0, '0',
    'x² − 4 = (x − 2)(x + 2) ist Hauptnenner. Mal HN: 3(x + 2) + (x − 2) = 4 ⇔ 4x + 4 = 4 ⇔ x = 0. 0 liegt in D = ℚ \\ {−2; 2}.',
    'Zerlege x² − 4 mit der binomischen Formel.', art='P')
SW.a('hauptnenner', 3, 'Löse x/(x − 1) − 1 = 1/(x − 1).', 'L = ℚ \\ {1}', ['L = { }', 'L = {1}', 'L = ℚ'],
    'Mal (x − 1): x − (x − 1) = 1 ⇔ 1 = 1. Das stimmt immer. Jede Zahl aus D ist Lösung: L = ℚ \\ {1}.', 'Rechne zu Ende. Was bedeutet eine immer wahre Aussage?', art='K')
SW.a('hauptnenner', 3, 'Löse 2/(x − 3) − 1/x = 6/(x(x − 3)).', 'L = { }', ['L = {3}', 'L = {0; 3}', 'L = {−3}'],
    'Mal x(x − 3): 2x − (x − 3) = 6 ⇔ x + 3 = 6 ⇔ x = 3. Aber 3 ∉ D = ℚ \\ {0; 3}. Keine Lösung.', 'Bestimme D zuerst. Prüfe am Ende.', art='K')

# scheinloesung
SW.a('scheinloesung', 2, 'Gib die Lösungsmenge von 2x/(x − 1) = 2/(x − 1) an.', 'L = { }', ['L = {1}', 'L = {−1}', 'L = ℚ \\ {1}'],
    '2x = 2 ⇔ x = 1. Aber für x = 1 ist der Nenner 0. Scheinlösung, L = { }.', 'Rechne und vergleiche mit D.')
SW.a('scheinloesung', 2, 'Gib die Lösungsmenge von 6/(x − 2) = 3/(x − 2) + 3 an.', 'L = {3}', ['L = { }', 'L = {2}', 'L = {−3}'],
    '3/(x − 2) = 3 ⇔ x − 2 = 1 ⇔ x = 3. 3 liegt in D = ℚ \\ {2}. L = {3}.', 'Nicht jede Bruchgleichung hat eine Scheinlösung. Prüfe.')
SW.a('scheinloesung', 3, 'Gib die Lösungsmenge von 1/(x − 1) + 1/(x + 1) = 2/(x² − 1) an.', 'L = { }', ['L = {1}', 'L = {−1; 1}', 'L = {0}'],
    'HN (x − 1)(x + 1) = x² − 1: (x + 1) + (x − 1) = 2 ⇔ 2x = 2 ⇔ x = 1. Aber 1 ∉ D = ℚ \\ {−1; 1}. L = { }.', 'Zerlege x² − 1. Prüfe das Ergebnis mit D.', art='P')
SW.a('scheinloesung', 3, 'Mia löst 2x/(x + 3) = −6/(x + 3) und schreibt L = {−3}. Was stimmt?', 'Falsch: −3 gehört nicht zu D. Richtig ist L = { }.',
    ['Richtig gerechnet.', 'Falsch: Richtig ist L = {3}.', 'Falsch: Richtig ist L = ℚ \\ {−3}.'],
    'Die Rechnung 2x = −6 ⇔ x = −3 stimmt. Aber für x = −3 ist der Nenner 0. Mia hat die Probe mit D vergessen.', 'Prüfe Mias Ergebnis mit der Definitionsmenge.', art='P')
SW.a('scheinloesung', 3, 'Gib die Lösungsmenge von (x² − 1)/(x − 1) = 2 an.', 'L = { }', ['L = {1}', 'L = {−1; 1}', 'L = {3}'],
    'Kürzen: (x − 1)(x + 1)/(x − 1) = x + 1 (für x ≠ 1). x + 1 = 2 ⇔ x = 1. Aber 1 ∉ D. Keine Lösung.', 'Zerlege den Zähler. Was ist mit x = 1?', art='K')
SW.z('scheinloesung', 3, 'Für welchen Wert von a hat (x + a)/(x − 5) = 3/(x − 5) KEINE Lösung?', -2, '3 - 5',
    'Mal (x − 5): x + a = 3 ⇔ x = 3 − a. Keine Lösung, wenn das die verbotene Zahl 5 ist: 3 − a = 5 ⇔ a = −2.', 'Löse allgemein nach x auf. Wann ist das eine Scheinlösung?', art='K')

# verhaeltnis
SW.z('verhaeltnis', 2, 'Löse die Verhältnisgleichung x : 2,5 = 6 : 5.', 3, '2.5 * 6 / 5', 'x · 5 = 2,5 · 6 = 15 ⇔ x = 3.', 'Außenglieder mal Außenglieder = Innenglieder mal Innenglieder.')
SW.z('verhaeltnis', 2, 'Beton wird aus Zement und Kies im Verhältnis 1 : 4 gemischt. Wie viel Kies steckt in 60 kg Mischung?', 48, '60 * 4 / 5',
    '1 : 4 heißt 5 Teile insgesamt, davon 4 Teile Kies. 60 kg : 5 = 12 kg pro Teil, Kies 4 · 12 = 48 kg.', 'Wie viele Teile hat die ganze Mischung?', einheit='kg')
SW.z('verhaeltnis', 3, 'Auf einer Wanderkarte im Maßstab 1 : 50 000 liegen zwei Hütten 7 cm auseinander. Wie weit ist das in Wirklichkeit?', 3.5, '7 * 50000 / 100000',
    '7 cm · 50 000 = 350 000 cm = 3 500 m = 3,5 km.', '1 km = 100 000 cm.', einheit='km', art='P')
SW.z('verhaeltnis', 3, 'Ein Hausmodell ist im Maßstab 1 : 20 gebaut. Eine Wand hat im Modell 30 cm² Fläche. Wie groß ist die Fläche in Wirklichkeit?', 12000, '30 * 20 * 20',
    'Jede Länge wird 20-mal so groß, eine Fläche also 20 · 20 = 400-mal so groß: 30 cm² · 400 = 12 000 cm² (= 1,2 m²).', 'Länge und Breite werden beide vergrößert.', einheit='cm²', art='P')
SW.z('verhaeltnis', 3, 'Zwei Zahlen stehen im Verhältnis 3 : 5. Ihre Differenz ist 14. Wie groß ist die kleinere Zahl?', 21, '3 * 14 / 2',
    'Die Zahlen sind 3k und 5k. Differenz 2k = 14 ⇔ k = 7. Kleinere Zahl 3 · 7 = 21 (größere 35).', 'Schreibe die Zahlen als 3k und 5k.', art='K')
SW.z('verhaeltnis', 3, 'In einer Gruppe ist das Verhältnis Jungen : Mädchen = 4 : 5. Kommen 2 Jungen dazu, ist es 1 : 1. Wie viele Mädchen sind in der Gruppe?', 10, '5 * 2',
    'Jungen 4k, Mädchen 5k. 4k + 2 = 5k ⇔ k = 2. Mädchen: 5 · 2 = 10 (Jungen 8, dann 10).', 'Schreibe Jungen und Mädchen mit einem gemeinsamen k.', einheit='Mädchen', art='K')

# graphisch
SW.z('graphisch', 2, 'Das Bild zeigt die Graphen von f(x) = 6/x und g(x) = 2. Lies die Lösung von 6/x = 2 ab.', 3, '6 / 2', 'Die Graphen schneiden sich bei x = 3. Probe: 6/3 = 2.',
    'Lies den x-Wert des Schnittpunkts ab.', grafik=_k(x=[-5, 7], y=[-4, 6], graphen=[_h(6, name='f'), {'art': 'linear', 'm': 0, 't': 2, 'name': 'g'}]))
SW.a('graphisch', 2, 'Welche Gleichung löst man, wenn man den Schnittpunkt der Graphen von f(x) = 4/(x − 1) und g(x) = 2 sucht?', '4/(x − 1) = 2',
    ['4/(x − 1) = 0', '4/x − 1 = 2', '4 = 2(x + 1)'], 'Am Schnittpunkt sind die Funktionswerte gleich: f(x) = g(x), also 4/(x − 1) = 2.', 'Was gilt für f(x) und g(x) im Schnittpunkt?')
SW.l('graphisch', 3, 'Die Gleichung 4/x = x hat zwei Lösungen. Lies sie am Bild ab, die kleinere zuerst.', 'x₁ = □; x₂ = □', [-2, 2], ['-2', '2'],
    'Die Gerade y = x schneidet beide Äste der Hyperbel: bei (−2 | −2) und (2 | 2). Probe: 4/2 = 2.', 'Suche beide Schnittpunkte, auch links.', 'Je Lücke eine ganze Zahl.',
    grafik=_k(x=[-5, 5], y=[-5, 5], graphen=[_h(4, name='f'), {'art': 'linear', 'm': 1, 't': 0, 'name': 'g'}]), art='P')
SW.a('graphisch', 3, 'Für welche Zahl c hat 2/(x − 1) = c keine Lösung? Entscheide am Bild.', 'c = 0', ['c = 1', 'c = −2', 'c = 2'],
    'Die Hyperbel nähert sich der waagrechten Asymptote y = 0, berührt sie aber nie. Jede andere waagrechte Gerade trifft einen Ast.',
    'Welche waagrechte Gerade trifft die Hyperbel nie?', grafik=_k(x=[-4, 6], y=[-5, 5], graphen=[_h(2, -1)], senkrecht=[1]), art='P')
SW.a('graphisch', 3, 'Wie viele Lösungen hat die Gleichung 1/x = −x? Entscheide am Bild.', '0 Lösungen', ['1 Lösung', '2 Lösungen', 'unendlich viele Lösungen'],
    'Die Hyperbel 1/x liegt im 1. und 3. Feld, die Gerade y = −x im 2. und 4. Feld. Sie treffen sich nie. (Rechnerisch: x² = −1 geht nicht.)',
    'In welchen Feldern liegt welcher Graph?', grafik=_k(x=[-4, 4], y=[-4, 4], graphen=[_h(1, name='f'), {'art': 'linear', 'm': -1, 't': 0, 'name': 'g'}]), art='K')
SW.z('graphisch', 3, 'Die Ursprungsgerade y = m · x schneidet die Hyperbel f(x) = 9/x an der Stelle x = 3. Bestimme m.', 1, '9 / 3 / 3',
    'Schnittpunkt: f(3) = 3, also P(3 | 3). P liegt auf der Geraden: 3 = m · 3 ⇔ m = 1. Wegen der Symmetrie ist auch (−3 | −3) ein Schnittpunkt.',
    'Berechne zuerst den y-Wert des Schnittpunkts.', art='K')

baue = mit_schwer(baue, SW)
# ---- SCHWER ENDE ----

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, mit_befunden  # noqa: E402

BF = Befunde('gleichungen.bruch', 13_8_5)
# a) Verhältnis 1 : 1 – sofort ablesbar → Stufe 1
BF.stufe('verhaeltnis', 'Löse die Verhältnisgleichung 6 : x = 6 : 6.', 1)
BF.stufe('verhaeltnis', 'Löse die Verhältnisgleichung 12 : x = 3 : 3.', 1)
# a) einfacher Dreisatz → Stufe 2
BF.stufe('verhaeltnis', 'Für 6 Personen braucht man 200 g Mehl. Wie viel Mehl braucht man für 9 Personen?', 2)

baue = mit_befunden(baue, BF)
# ---- BEFUNDE ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Teil A: Gesamtdurchsicht Kl. 8, siehe _durchsicht_kl8.py) ----
from _durchsicht_kl8 import Durchsicht, mit_durchsicht  # noqa: E402

DSX = Durchsicht('gleichungen.bruch', 19_8_8)
for _t in ['Löse (x − 3)/(x + 7) = −3.', 'Löse (x + 3)/(x − 9) = 3.', 'Löse (3x + 5)/(x − 3) = −1.', 'Löse (x + 3)/(x + 7) = 3.']:
    DSX.stufe('ein_bruch', _t, 2)
DSX.stufen('ein_bruch', 'S1 a/x = c; S2 a/(bx) und a/(x + b); S3 viermal (x + a)/(x + b) = c (zwei Schritte mehr)',
           'S1 a/x = c; S2 a/(x + b) = c, auch x im Zähler; S3 Zahl in der Gleichung rückwärts bestimmen, Sachaufgabe, leere Lösungsmenge, Zahlenrätsel')
DSX.stufe('ueber_kreuz', 'Löse (x − 7)/(x − 6) = (x + 2)/(x + 8).', 2)
DSX.stufe('ueber_kreuz', 'Löse (x + 5)/(x + 1) = (x − 8)/(x − 7).', 2)
DSX.stufen('ueber_kreuz', 'S1 a/x = b/(x − c); S2 beide Nenner x ± c; S3 viermal x² hebt sich weg (längere Rechnung)',
           'S1 a/x = b/(x − c); S2 beide Nenner x ± c, auch x im Zähler; S3 x² hebt sich weg, Begründung des Verfahrens, Fehler finden, Parameter')
for _t in ['Gib die Lösungsmenge von (x − 6)/(x − 7) = 1/(x − 7) an.', 'Gib die Lösungsmenge von 3x/(x + 2) = −6/(x + 2) an.',
           'Warum ist x = 6 keine Lösung von (x − 4)/(x − 6) = 2/(x − 6), obwohl die Rechnung x = 6 ergibt?',
           'Warum ist x = 2 keine Lösung von (x − 8)/(x − 2) = −6/(x − 2), obwohl die Rechnung x = 2 ergibt?']:
    DSX.stufe('scheinloesung', _t, 2)
DSX.stufen('scheinloesung', 'S1 Lösungsmenge wählen; S2 und S3 dieselben Aufgaben (L angeben, „Warum keine Lösung?“)',
           'S1 Lösungsmenge wählen; S2 Scheinlösung erkennen und begründen; S3 Nenner x² − 1, Fehler finden, kürzbarer Bruch, Parameter a')
DSX.stufe('verhaeltnis', 'Eine Karte hat den Maßstab 1 : 25 000. Zwei Orte sind auf der Karte 1 cm voneinander entfernt. Wie weit sind sie in Wirklichkeit entfernt (in km)?', 2)
DSX.stufen('verhaeltnis', 'S1 Verhältnisgleichung lösen; S2 x im Nenner, Mischungen; S3 teils einfacher Maßstab',
           'S1 x im Zähler; S2 x im Nenner, Mischungen, Maßstab; S3 x auf beiden Seiten, Flächen-Maßstab, Differenz, Verhältnis ändert sich')
DSX.stufen('definitionsmenge', 'S1 ein Nenner; S2 zwei Nenner; S3 Produktnenner, x² − 2x, Gleichung zu D, Parameter')
DSX.stufen('hauptnenner', 'S1 gleiche Nenner; S2 x und kx; S3 gemeinsame Arbeit, Nenner x² − 4, L = ℚ \\ {1}, leere Menge')
DSX.stufen('graphisch', 'S1 Schnitt mit waagrechter Linie; S2 Hyperbel und Gerade; S3 Anzahl der Lösungen, Parameter c, Ursprungsgerade')
baue = mit_durchsicht(baue, DSX)
# ---- DURCHSICHT ENDE ----

# ---- STUFEN (Zwanzigste Runde: echte Stufe 3 und Knobel-Bordkarten, siehe _stufen_kl8.py) ----
from _stufen_kl8 import Stufen, mit_stufen  # noqa: E402

ST = Stufen('gleichungen.bruch', 20_8_5)
SA, SZ, SL = ST.A, ST.Z, ST.L
def T(lz, *regeln):
    for m, g in regeln: ST.typ(lz, m, g)

# --- definitionsmenge ---
ST.leiter('definitionsmenge', 'die eine Zahl ausschließen, für die ein einfacher Nenner 0 wird',
          'mehrere Nenner, Gleichung zu einer Definitionsmenge finden, Sachgleichung und Tabelle deuten',
          'Nenner faktorisieren, Nenner ohne Nullstelle begründen, Fehler beim Nullsetzen, Parameter, rückwärts zum Nenner, Anzahl ausgeschlossener Zahlen')
T('definitionsmenge', (r'^Bestimme die Definitionsmenge von [−\d]+/\(x [−+] \d+\) = \d+\.$', 'direkt'), (r'x\(x|x² − 2x', 'verknuepfen'),
  (r'^Welche Gleichung hat', 'umkehr'), (r'Wert von a', 'parameter'), (r'^Wie viele Zahlen', 'transfer'), (r'^Bestimme', 'mehrschritt'))
ST.neu('definitionsmenge', 'erkennen', SA('Welche Zahl darf man in 4/(x − 7) = 2 nicht für x einsetzen?', '7', ['−7', '4', '2'], 'Für x = 7 wird der Nenner 7 − 7 = 0.', 'Wann wird der Nenner 0?'))
ST.neu('definitionsmenge', 'direkt', SA('Gib für die Gleichung x/(x − 5) = 2 die Menge D aller erlaubten Zahlen an.', 'ℚ \\ {5}', ['ℚ \\ {−5}', 'ℚ \\ {0}', 'ℚ \\ {2}'], 'Der Nenner x − 5 ist 0 für x = 5.', 'Setze den Nenner gleich 0.'))
ST.neu('definitionsmenge', 'einkleidung', SA('36 € werden auf x Personen und eine zusätzliche Person verteilt; jede bekommt 4 €: 36/(x + 1) = 4. Welche Zahl ist für x ausgeschlossen?', 'x = −1 – im Sachzusammenhang kommt sie ohnehin nicht vor.',
    ['x = 1', 'x = 4', 'keine'], 'x + 1 = 0 für x = −1. Da x eine Personenzahl ist, wäre −1 sowieso sinnlos.', 'Setze den Nenner gleich 0.'))
ST.neu('definitionsmenge', 'darstellung', SA('In einer Wertetabelle zu 5/(x + 4) steht bei x = −4 „Fehler“. Was bedeutet das für die Gleichung 5/(x + 4) = 1?', 'D = ℚ \\ {−4}: dort ist der Nenner 0.',
    ['Die Lösung ist x = −4.', 'D = ℚ \\ {4}.', 'Die Gleichung hat keine Lösung.'], 'Der Rechner meldet „Fehler“, weil durch 0 geteilt würde. Diese Zahl gehört nicht zur Definitionsmenge.', 'Was passiert im Nenner bei x = −4?'))
ST.neu('definitionsmenge', 'fehler', SA('Jemand bestimmt für 3/(2x − 6) = 1/x die Definitionsmenge ℚ \\ {0; 6}. Was stimmt?', 'Falsch: 2x − 6 = 0 gilt für x = 3, also D = ℚ \\ {0; 3}.',
    ['Richtig.', 'Falsch: D = ℚ \\ {6}.', 'Falsch: D = ℚ \\ {−3; 0}.'], '2x − 6 = 0 ⇒ 2x = 6 ⇒ x = 3. Die 6 macht den Nenner zu 6, nicht zu 0.', 'Löse 2x − 6 = 0 wirklich nach x auf.'))
ST.neu('definitionsmenge', 'begruenden', SA('Kann eine Bruchgleichung mit x im Nenner die Definitionsmenge ℚ haben?', 'Ja, z. B. 1/(x² + 1) = 1/2 – der Nenner wird nie 0.',
    ['Nein, nie.', 'Ja, aber nur wenn x auch im Zähler steht.', 'Nein, x = 0 ist immer ausgeschlossen.'], 'x² + 1 ist immer mindestens 1. Dann muss keine Zahl ausgeschlossen werden.', 'Gibt es Nenner, die nie 0 werden?'))
ST.neu('definitionsmenge', 'rueckwaerts', SA('Eine Gleichung hat die Definitionsmenge ℚ \\ {−4; 0}. Welcher Nenner kann darin vorkommen?', 'x² + 4x', ['x² − 4x', 'x + 4', 'x² + 4'],
    'x² + 4x = x(x + 4) ist 0 für x = 0 und x = −4. x² − 4x schließt 0 und 4 aus, x + 4 nur −4, x² + 4 gar nichts.', 'Zerlege jeden Nenner in Faktoren.'))
ST.knobel('definitionsmenge', SZ('Wie viele Zahlen schließt die Definitionsmenge von 1/(x − 1) + 1/(x² − 1) + 1/(x³ − x) = 0 aus?', 3, '3',
    'x − 1 = 0 bei 1. x² − 1 = (x − 1)(x + 1) = 0 bei 1 und −1. x³ − x = x(x − 1)(x + 1) = 0 bei 0, 1 und −1. Zusammen: −1, 0, 1 – drei Zahlen.',
    'Zerlege jeden Nenner in Faktoren und sammle alle Nullstellen, ohne doppelt zu zählen.'))
ST.knobel('definitionsmenge', SA('Für welche Zahlen a schließt die Definitionsmenge von 1/(x − a) = 1/(x + a) nur eine einzige Zahl aus?', 'nur für a = 0', ['für alle a', 'für kein a', 'nur für a = 1'],
    'Ausgeschlossen sind a und −a. Das ist nur eine Zahl, wenn a = −a, also a = 0 (dann ist es die 0).', 'Wann sind a und −a dieselbe Zahl?'))

# --- ein_bruch ---
ST.leiter('ein_bruch', 'a/x = b durch Malnehmen mit x lösen',
          'Nenner mit Faktor oder Summand, Sachsituation als Bruchgleichung, Gleichung zu einem Satz finden, fehlenden Zähler bestimmen',
          'leere Lösungsmenge begründen, Fehler beim Malnehmen deuten, rückwärts aus einer Denkaufgabe, Prozent verknüpfen, Parameter, Lösen mit Probe')
T('ein_bruch', (r'^Löse \S+ = \S+/x\.$|^Löse \S+/x = \S+\.$', 'direkt'), (r'Geschenk', 'einkleidung'), (r'ersetzen', 'parameter'), (r'\(2x \+ 1\)/\(x − 3\) = 2', 'begruenden'),
  (r'^Teilt man', 'transfer'), (r'^Löse', 'mehrschritt'))
ST.neu('ein_bruch', 'erkennen', SA('Welche Zahl löst 12/x = 4?', '3', ['48', '8', '16'], '12 : 3 = 4. (48 wäre 12 · 4.)', 'Durch welche Zahl muss man 12 teilen, um 4 zu erhalten?'))
ST.neu('ein_bruch', 'umkehr', SZ('Für welche Zahl a hat a/x = 5 die Lösung x = 1,2?', 6, '5 * 12/10', 'a = 5 · x = 5 · 1,2 = 6.', 'Setze x = 1,2 ein und löse nach a auf.'))
ST.neu('ein_bruch', 'darstellung', SA('Welche Gleichung beschreibt: „Teilt man 24 durch eine Zahl, erhält man 6“?', '24/x = 6', ['x/24 = 6', '24 · x = 6', '24 − x = 6'], '„24 geteilt durch die Zahl“ ist 24/x.', 'Was wird durch was geteilt?'))
ST.neu('ein_bruch', 'fehler', SA('Jemand löst 8/(x − 2) = 4 so: 8 = 4x − 2, also x = 2,5. Was stimmt?', 'Falsch: 8 = 4(x − 2) = 4x − 8, also x = 4.',
    ['Richtig.', 'Falsch: x = 6.', 'Falsch: x = 0,5.'], 'Mal (x − 2) heißt: die ganze Klammer mal 4. Probe mit 4: 8/2 = 4 ✓, mit 2,5: 8/0,5 = 16 ✗.', 'Mach die Probe mit x = 2,5.'))
ST.neu('ein_bruch', 'rueckwaerts', SZ('Man denkt sich eine Zahl, addiert 3, teilt 60 durch das Ergebnis und erhält 4. Welche Zahl war es?', 12, '60 / 4 - 3',
    '60/(x + 3) = 4 ⇒ x + 3 = 15 ⇒ x = 12.', 'Rückwärts: Durch welche Zahl wurde 60 geteilt?'))
ST.neu('ein_bruch', 'verknuepfen', SZ('Ein Betrag wird in x gleiche Raten geteilt. Jede Rate ist 12,5 % des Betrags. Wie viele Raten sind es?', 8, '100 / (125/10)',
    'Eine Rate ist 1/x des Betrags: 1/x = 0,125 ⇒ x = 1 : 0,125 = 8.', 'Schreibe den Anteil einer Rate als Bruch mit x.'))
ST.neu('ein_bruch', 'begruenden', SA('Kann eine Gleichung a/x = 0 mit a ≠ 0 eine Lösung haben?', 'Nein: Ein Bruch ist nur 0, wenn sein Zähler 0 ist – und a ist nicht 0.',
    ['Ja, x = 0.', 'Ja, x = a.', 'Nur wenn a negativ ist.'], 'Malnehmen mit x ergäbe a = 0, ein Widerspruch. x = 0 ist zudem gar nicht erlaubt.', 'Wann ist ein Bruch gleich 0?'))
ST.neu('ein_bruch', 'pruefung', SZ('Löse 2 + 6/x = 5 und mache die Probe. Gib x an.', 2, '6 / (5 - 2)',
    '6/x = 3 ⇒ x = 2. D = ℚ \\ {0}, 2 gehört dazu. Probe: 2 + 6/2 = 5 ✓.', 'Bring zuerst die 2 auf die andere Seite.'))
ST.knobel('ein_bruch', SZ('Für wie viele natürliche Zahlen x ist 24/x + x eine natürliche Zahl kleiner als 15?', 6, '6',
    '24/x muss ganz sein, also ist x ein Teiler von 24: 1, 2, 3, 4, 6, 8, 12, 24. Werte von 24/x + x: 25, 14, 11, 10, 10, 11, 14, 25. Kleiner als 15 sind sie für x = 2, 3, 4, 6, 8, 12 – sechs Zahlen.',
    'Wann ist 24/x überhaupt eine natürliche Zahl?'))
ST.knobel('ein_bruch', SZ('Ein Bruch hat den Zähler 7. Vergrößert man den Nenner um 4, wird der Bruch halb so groß. Wie heißt der Nenner?', 4, '4',
    '7/(n + 4) = 1/2 · 7/n = 7/(2n). Gleicher Zähler ⇒ gleicher Nenner: n + 4 = 2n ⇒ n = 4. Probe: 7/8 ist die Hälfte von 7/4.',
    'Wie schreibt man „halb so groß“ bei einem Bruch mit dem Zähler 7?'))

# --- ueber_kreuz ---
ST.leiter('ueber_kreuz', 'a/x = b/(x + c) über Kreuz multiplizieren und lösen',
          'zwei Klammernenner, Zähler mit x, Sachsituation und Satz als Gleichung',
          'x² hebt sich weg, begründen warum über Kreuz erlaubt ist, Fehler (über Kreuz bei Summe), Parameter, rückwärts, Anteils-Transfer')
T('ueber_kreuz', (r'^Löse \d+/x = \d+/\(x [−+] \d+\)\.$', 'direkt'), (r'^Löse \(x [−+] \d+\)/\(x [−+] \d+\) = \(x [−+] \d+\)/\(x [−+] \d+\)\.$', 'verknuepfen'),
  (r'^Warum', 'begruenden'), (r'^Tom', 'fehler'), (r'Wert von a', 'parameter'), (r'^Löse|^Für welche Zahl z', 'mehrschritt'))
ST.neu('ueber_kreuz', 'erkennen', SA('Welche Gleichung entsteht aus 3/x = 5/(x + 2) durch Multiplizieren über Kreuz?', '3(x + 2) = 5x', ['3x = 5(x + 2)', '3 · 5 = x(x + 2)', '3(x + 2) = 5'],
    'Zähler links mal Nenner rechts = Zähler rechts mal Nenner links: 3 · (x + 2) = 5 · x.', 'Welcher Zähler wird mit welchem Nenner multipliziert?'))
ST.neu('ueber_kreuz', 'erkennen', SA('Welche Zahl löst 6/x = 3/2?', '4', ['9', '2', '1'], '6/4 = 3/2 ✓. Über Kreuz: 3x = 12, x = 4.', 'Probiere die Zahlen aus oder multipliziere über Kreuz.'))
ST.neu('ueber_kreuz', 'einkleidung', SZ('Läufer A schafft 10 km in derselben Zeit wie Läufer B 8 km. B ist 2 km/h langsamer als A. Wie schnell ist A? (10/v = 8/(v − 2))', 10, '2 * 10 / (10 - 8)',
    '10(v − 2) = 8v ⇒ 10v − 20 = 8v ⇒ v = 10 km/h. Probe: 10/10 = 1 h und 8/8 = 1 h.', 'Zeit = Strecke : Geschwindigkeit – beide Zeiten sind gleich.', einheit='km/h'))
ST.neu('ueber_kreuz', 'darstellung', SA('Welche Gleichung beschreibt: „Der Bruch mit Zähler 2 und Nenner x ist so groß wie der Bruch mit Zähler 3 und Nenner x + 4“?', '2/x = 3/(x + 4)',
    ['x/2 = (x + 4)/3', '2/x = 3/x + 4', '2x = 3(x + 4)'], 'Zähler über Nenner: 2/x und 3/(x + 4); „so groß wie“ heißt =.', 'Schreibe beide Brüche einzeln auf.'))
ST.neu('ueber_kreuz', 'rueckwaerts', SZ('Die Gleichung 4/x = 6/(x + c) hat die Lösung x = 8. Bestimme c.', 4, '6 * 8 / 4 - 8',
    'Einsetzen: 4/8 = 6/(8 + c) ⇒ 4(8 + c) = 48 ⇒ 8 + c = 12 ⇒ c = 4.', 'Setze die bekannte Lösung ein.'))
ST.neu('ueber_kreuz', 'transfer', SZ('In Klasse A tragen 6 von x Kindern eine Brille, in Klasse B 9 von x + 10 Kindern. Der Anteil ist gleich. Wie viele Kinder hat Klasse A?', 20, '6 * 10 / (9 - 6)',
    '6/x = 9/(x + 10) ⇒ 6x + 60 = 9x ⇒ x = 20. Probe: 6/20 = 0,3 und 9/30 = 0,3.', 'Stelle für jede Klasse den Anteil als Bruch auf.'))
ST.neu('ueber_kreuz', 'pruefung', SZ('Löse 2/(x − 1) = 3/(x + 1), prüfe, ob die Lösung zu D gehört, und gib sie an.', 5, '(2 + 3) / (3 - 2)',
    'D = ℚ \\ {−1; 1}. 2(x + 1) = 3(x − 1) ⇒ 2x + 2 = 3x − 3 ⇒ x = 5. 5 ∈ D. Probe: 2/4 = 3/6 ✓.', 'Erst D, dann über Kreuz, dann die Probe.'))
ST.knobel('ueber_kreuz', SZ('Zum Zähler und zum Nenner von 5/8 wird dieselbe Zahl x addiert. Der neue Bruch hat den Wert 3/4. Bestimme x.', 4, '(3 * 8 - 4 * 5) / (4 - 3)',
    '(5 + x)/(8 + x) = 3/4 ⇒ 4(5 + x) = 3(8 + x) ⇒ 20 + 4x = 24 + 3x ⇒ x = 4. Probe: 9/12 = 3/4.', 'Stelle die Gleichung auf und multipliziere über Kreuz.'))
ST.knobel('ueber_kreuz', SZ('Für welche Zahl x gilt x/(x + 1) = (x + 2)/(x + 4)?', 2, '2',
    'Über Kreuz: x(x + 4) = (x + 2)(x + 1) ⇒ x² + 4x = x² + 3x + 2. Das x² fällt weg: x = 2. Probe: 2/3 = 4/6 ✓.', 'Trau dich auszumultiplizieren – vielleicht verschwindet etwas.'))

# --- hauptnenner ---
ST.leiter('hauptnenner', 'gleichnamige Brüche zusammenfassen und mit x malnehmen',
          'Hauptnenner wie 5x, Zahl und Bruch gemischt, Arbeitsaufgaben (Pumpen, Streichen), fehlenden Zähler bestimmen',
          'gleicher Nenner als Block, binomische Formel im Nenner, Identität und leere Menge begründen, Fehler beim Malnehmen, Parameter, drei Leitungen')
T('hauptnenner', (r'^Löse \d+/x [+−] \d+/x = −?\d+\.$', 'direkt'), (r'Pumpen|Zaun', 'einkleidung'), (r'Rohr A', 'rueckwaerts'),
  (r'\(x \+ 5\) \+ 1|x² − 4', 'verknuepfen'), (r'x/\(x − 1\) − 1|2/\(x − 3\) − 1/x', 'begruenden'), (r'^Löse', 'mehrschritt'))
ST.neu('hauptnenner', 'erkennen', SA('Welcher Hauptnenner passt zu 2/x + 1/(3x) = 1?', '3x', ['x', '4x', '3x²'], '3x enthält x und 3x – der kleinste gemeinsame Nenner.', 'Welcher Nenner ist durch beide Nenner teilbar?'))
ST.neu('hauptnenner', 'erkennen', SA('Wie lautet 3/x + 5/x zusammengefasst?', '8/x', ['8/(2x)', '15/x', '8/x²'], 'Gleicher Nenner: Zähler addieren, Nenner bleibt: 8/x.', 'Was passiert bei gleichem Nenner mit dem Nenner?'))
ST.neu('hauptnenner', 'umkehr', SZ('Für welche Zahl a hat a/x + 2/x = 1 die Lösung x = 7?', 5, '7 - 2', '(a + 2)/x = 1 ⇒ a + 2 = x = 7 ⇒ a = 5.', 'Fasse die Brüche zusammen und setze x = 7 ein.'))
ST.neu('hauptnenner', 'fehler', SA('Jemand multipliziert 2/x + 1 = 5/x mit x und schreibt 2 + 1 = 5. Was stimmt?', 'Falsch: Auch die 1 muss mit x malgenommen werden: 2 + x = 5, also x = 3.',
    ['Richtig, die Gleichung hat keine Lösung.', 'Falsch: 2x + x = 5x.', 'Falsch: Man darf nicht mit x malnehmen.'], 'Jeder Summand wird mit x multipliziert: 2 + 1 · x = 5. Probe mit 3: 2/3 + 1 = 5/3 ✓.', 'Wird beim Malnehmen jeder Summand erfasst?'))
ST.neu('hauptnenner', 'parameter', SZ('Für welche Zahl a hat 1/x + a/(2x) = 1 die Lösung x = 3?', 4, '2 * 3 - 2', 'Hauptnenner 2x: (2 + a)/(2x) = 1 ⇒ 2 + a = 2x = 6 ⇒ a = 4.', 'Bring beide Brüche auf den Nenner 2x.'))
ST.neu('hauptnenner', 'transfer', SZ('Kopierer A schafft einen Auftrag in x Minuten, Kopierer B braucht doppelt so lange. Zusammen sind sie in 20 Minuten fertig. Wie lange bräuchte A allein?', 30, '20 * 3 / 2',
    'In einer Minute: A schafft 1/x, B 1/(2x), zusammen 1/20. 1/x + 1/(2x) = 3/(2x) = 1/20 ⇒ 2x = 60 ⇒ x = 30 Minuten.', 'Stelle die Anteile pro Minute auf.', einheit='min'))
ST.neu('hauptnenner', 'pruefung', SZ('Drei Leitungen füllen ein Becken: allein bräuchten sie 6 h, 4 h und 12 h. Wie lange dauert es mit allen dreien?', 2, '1 / (1/6 + 1/4 + 1/12)',
    'In einer Stunde: 1/6 + 1/4 + 1/12 = 2/12 + 3/12 + 1/12 = 6/12 = 1/2 des Beckens. Für das ganze Becken: 2 Stunden.', 'Welchen Teil schafft jede Leitung in einer Stunde?', einheit='h'))
ST.knobel('hauptnenner', SZ('Löse 1/x + 1/(2x) + 1/(3x) + 1/(6x) = 1.', 2, '(6 + 3 + 2 + 1) / 6',
    'Hauptnenner 6x: (6 + 3 + 2 + 1)/(6x) = 12/(6x) = 2/x. Also 2/x = 1 ⇒ x = 2.', 'Bring alle Brüche auf einen gemeinsamen Nenner.'))
ST.knobel('hauptnenner', SZ('Ein Meister braucht für eine Wand 4 h, sein Lehrling 12 h. Der Meister fängt allein an, nach 1 h hilft der Lehrling mit. Wie lange dauert die Arbeit insgesamt?', 3.25, '1 + (1 - 1/4) / (1/4 + 1/12)',
    'Nach 1 h ist 1/4 geschafft, es fehlen 3/4. Zusammen schaffen sie pro Stunde 1/4 + 1/12 = 1/3. Für 3/4 brauchen sie (3/4) : (1/3) = 9/4 = 2,25 h. Insgesamt 3,25 h.',
    'Teile die Arbeit in zwei Abschnitte: allein und zu zweit.', einheit='h'))

# --- scheinloesung ---
ST.leiter('scheinloesung', 'lösen und prüfen, ob die Lösung zu D gehört',
          'Scheinlösung erkennen und L = { } schreiben, Bruch und Zahl gemischt, Gleichung mit Scheinlösung finden',
          'begründen, warum die Scheinlösung fällt, binomische Formeln verknüpfen, Fehler beim Aufschreiben, Parameter für leere Lösungsmenge')
T('scheinloesung', (r'^Gib die Lösungsmenge von \S+/\(x [−+] \d+\) = \S+/\(x [−+] \d+\) an\.$', 'direkt'), (r'^Warum ist', 'begruenden'),
  (r'x² − 1', 'verknuepfen'), (r'^Mia', 'fehler'), (r'KEINE Lösung', 'parameter'), (r'^Gib die Lösungsmenge', 'mehrschritt'))
ST.neu('scheinloesung', 'erkennen', SA('Die Rechnung ergibt x = 5, die Definitionsmenge ist ℚ \\ {5}. Wie heißt die Lösungsmenge?', 'L = { }', ['L = {5}', 'L = ℚ \\ {5}', 'L = {0}'],
    '5 gehört nicht zu D – sie ist eine Scheinlösung. Es bleibt keine Lösung.', 'Gehört die gefundene Zahl zu D?'))
ST.neu('scheinloesung', 'direkt', SZ('Löse (x + 3)/(x − 1) = 5/(x − 1) und gib x an, falls es zu D gehört.', 2, '5 - 3', 'D = ℚ \\ {1}. x + 3 = 5 ⇒ x = 2, und 2 gehört zu D.', 'Gleicher Nenner: Die Zähler müssen gleich sein.'))
ST.neu('scheinloesung', 'einkleidung', SZ('In (x − 2) Flaschen werden (x + 6) Liter Saft gleichmäßig verteilt; in jede kommen 3 Liter. Wie viele Liter Saft sind es?', 12, '(6 + 2 * 3) / (3 - 1) + 6',
    '(x + 6)/(x − 2) = 3 ⇒ x + 6 = 3x − 6 ⇒ x = 6. Saft: x + 6 = 12 Liter (in 4 Flaschen zu je 3 Liter).', 'Stelle die Gleichung auf – gefragt ist am Ende x + 6.', einheit='l'))
ST.neu('scheinloesung', 'umkehr', SA('Welche Gleichung liefert beim Rechnen x = 4, obwohl 4 nicht zu D gehört?', '(x + 2)/(x − 4) = 6/(x − 4)',
    ['(x + 2)/(x − 3) = 6/(x − 3)', '(x − 2)/(x + 4) = 2/(x + 4)', 'x/(x − 4) = 1'],
    'Bei (x + 2)/(x − 4) = 6/(x − 4) folgt x + 2 = 6, also x = 4 – aber 4 ist ausgeschlossen. Bei den ersten beiden ist 4 erlaubt, bei x/(x − 4) = 1 kommt gar nicht 4 heraus (x = x − 4 ist falsch).', 'Rechne jede Gleichung und vergleiche mit D.'))
ST.neu('scheinloesung', 'mehrschritt', SZ('Löse 4/(x + 1) = 2/(x + 1) + 1 und gib die Lösung an.', 1, '2 - 1', '2/(x + 1) = 1 ⇒ x + 1 = 2 ⇒ x = 1. 1 ∈ D (nur −1 ist ausgeschlossen).', 'Fasse die Brüche mit gleichem Nenner zuerst zusammen.'))
ST.neu('scheinloesung', 'mehrschritt', SZ('Löse 10/(x − 3) = 2 + 4/(x − 3).', 6, '6 / 2 + 3', '6/(x − 3) = 2 ⇒ x − 3 = 3 ⇒ x = 6. 6 ∈ D = ℚ \\ {3}.', 'Bring den Bruch rechts auf die linke Seite.'))
ST.neu('scheinloesung', 'pruefung', SA('Löse x/(x − 2) = 2/(x − 2) + 3 und gib die Lösungsmenge an.', 'L = { }', ['L = {2}', 'L = {3}', 'L = ℚ \\ {2}'],
    'Mal (x − 2): x = 2 + 3(x − 2) = 3x − 4 ⇒ 2x = 4 ⇒ x = 2. Aber 2 ∉ D: Scheinlösung, L = { }.', 'Nach dem Lösen: Gehört die Zahl zu D?'))
ST.knobel('scheinloesung', SA('Wie viele Lösungen hat x/(x − 1) + 1/(1 − x) = 1?', 'unendlich viele: alle x ≠ 1', ['keine', 'genau eine', 'genau zwei'],
    '1/(1 − x) = −1/(x − 1). Also links (x − 1)/(x − 1) = 1 für jedes x ≠ 1. Die Gleichung stimmt für alle erlaubten x.', 'Schreibe den Nenner 1 − x mit dem Nenner x − 1.'))
ST.knobel('scheinloesung', SZ('Die Gleichung (x² − 9)/(x − 3) = c hat für genau einen Wert von c keine Lösung. Für welchen?', 6, '3 + 3',
    'Für x ≠ 3 ist (x² − 9)/(x − 3) = x + 3. Aus x + 3 = c folgt x = c − 3. Das ist nur verboten, wenn c − 3 = 3, also c = 6. Dann gibt es keine Lösung.',
    'Kürze den Bruch mit einer binomischen Formel – welcher x-Wert ist verboten?'))

# --- verhaeltnis ---
ST.leiter('verhaeltnis', 'eine Verhältnisgleichung x : a = b : c lösen und erkennen',
          'x im zweiten Glied, Mischungen und Maßstab, fehlendes Glied bestimmen',
          'x auf beiden Seiten, Flächen im Maßstab, Differenz/Verhältnis verknüpfen, Fehler, Umordnen begründen, Parameter, Verhältnis ändert sich')
T('verhaeltnis', (r'^Löse die Verhältnisgleichung x : [\d,]+ = \d+ : \d+\.$|^Löse die Verhältnisgleichung \d+ : x = (\d+) : \1\.$', 'direkt'),
  (r'\(x [−+] \d+\) : \d', 'verknuepfen'), (r'Saft|[Kk]arte|Mehl|Beton', 'einkleidung'), (r'Hausmodell|Differenz', 'transfer'), (r'Jungen', 'pruefung'),
  (r'^Löse', 'mehrschritt'))
ST.neu('verhaeltnis', 'erkennen', SA('Welche Verhältnisgleichung passt zu „3 Teile Saft auf 5 Teile Wasser – also 12 Teile Saft auf x Teile Wasser“?', '3 : 5 = 12 : x', ['3 : 5 = x : 12', '5 : 3 = 12 : x', '3 : 12 = x : 5'],
    'Saft : Wasser bleibt gleich: 3 : 5 = 12 : x.', 'Auf beiden Seiten muss die gleiche Reihenfolge stehen: Saft : Wasser.'))
ST.neu('verhaeltnis', 'umkehr', SZ('In x : 8 = 3 : □ soll x = 12 herauskommen. Welche Zahl gehört ins Kästchen?', 2, '3 * 8 / 12', '12 : 8 = 3 : k ⇒ 12k = 24 ⇒ k = 2.', 'Setze x = 12 ein und löse nach dem Kästchen auf.'))
ST.neu('verhaeltnis', 'fehler', SA('Jemand löst x : 4 = 6 : 8 so: x = 6 · 8 : 4 = 12. Was stimmt?', 'Falsch: x = 4 · 6 : 8 = 3.', ['Richtig.', 'Falsch: x = 8 · 4 : 6.', 'Falsch: x = 6 + 8 − 4 = 10.'],
    'x : 4 = 0,75 ⇒ x = 3. Probe: 3 : 4 = 6 : 8 ✓, 12 : 4 = 3 ≠ 0,75.', 'Mach die Probe mit beiden Werten.'))
ST.neu('verhaeltnis', 'begruenden', SA('Stimmt: „Aus a : b = c : d folgt a : c = b : d“ (alle Zahlen ≠ 0)?', 'Ja: Beide Gleichungen sind gleichwertig zu a · d = b · c.', ['Nein, das gilt nie.', 'Nur wenn a = c ist.', 'Nur für ganze Zahlen.'],
    'Über Kreuz: a : b = c : d ⇔ a · d = b · c ⇔ a : c = b : d. Beispiel 2 : 4 = 3 : 6 und 2 : 3 = 4 : 6.', 'Multipliziere beide Gleichungen über Kreuz.'))
ST.neu('verhaeltnis', 'parameter', SZ('Für welche positive Zahl k gilt 2 : k = k : 8?', 4, '4', 'Über Kreuz: k · k = 16 ⇒ k = 4 (positiv). Probe: 2 : 4 = 4 : 8 = 0,5.', 'Multipliziere über Kreuz.'))
ST.knobel('verhaeltnis', SZ('Rote, blaue und grüne Kugeln: Rot : Blau = 3 : 4 und Blau : Grün = 2 : 5. Es sind 68 Kugeln. Wie viele sind grün?', 40, '68 * 10 / 17',
    'Blau in beiden Verhältnissen gleich machen: Rot : Blau = 3 : 4, Blau : Grün = 4 : 10. Also Rot : Blau : Grün = 3 : 4 : 10, zusammen 17 Teile. 68 : 17 = 4 Kugeln je Teil, grün 10 · 4 = 40.',
    'Bring die Zahl für Blau in beiden Verhältnissen auf denselben Wert.'))
ST.knobel('verhaeltnis', SZ('500 ml Saft sind im Verhältnis Sirup : Wasser = 1 : 4 gemischt. Wie viel ml Sirup muss man dazugeben, damit das Verhältnis 1 : 2 wird?', 100, '400 / 2 - 100',
    'Jetzt: 100 ml Sirup, 400 ml Wasser. Das Wasser bleibt gleich. Für 1 : 2 braucht man 200 ml Sirup, also 100 ml mehr.', 'Welche der beiden Mengen ändert sich nicht?', einheit='ml'))

# --- graphisch ---
ST.leiter('graphisch', 'die Lösung am Schnittpunkt einer Hyperbel mit einer waagrechten Geraden ablesen',
          'Hyperbel und schräge Gerade, passende Gleichung zum Bild, Sachgraph',
          'Anzahl der Lösungen begründen, Ablesefehler (x und y vertauscht), Parameter c ohne Lösung, rückwärts zur Geraden, Prüfungsaufgabe mit Punkt')
T('graphisch', (r'^Lies die Lösung|^Das Bild zeigt', 'erkennen'), (r'größere Lösung', 'mehrschritt'), (r'^Welche Gleichung löst', 'umkehr'),
  (r'Zahl c', 'parameter'), (r'Entscheide am Bild\.$', 'begruenden'), (r'4/x = x hat', 'transfer'), (r'Ursprungsgerade', 'rueckwaerts'), (r'mit den Graphen', 'darstellung'))
ST.neu('graphisch', 'direkt', SZ('Der Graph von y = 12/x schneidet die Gerade y = 3. Berechne die x-Koordinate des Schnittpunkts.', 4, '12 / 3', '12/x = 3 ⇒ x = 12 : 3 = 4.', 'Mal x, dann durch 3.'))
ST.neu('graphisch', 'einkleidung', SZ('Für 120 km braucht man t = 120/v Stunden (v in km/h). Am Graphen sucht man die Stelle mit t = 1,5. Welche Geschwindigkeit ist das?', 80, '120 / (15/10)',
    '120/v = 1,5 ⇒ v = 120 : 1,5 = 80 km/h.', 'Schnitt des Graphen mit der Geraden t = 1,5.', einheit='km/h'))
ST.neu('graphisch', 'fehler', SA('Bei 6/x = 3 liest jemand den Schnittpunkt (3 | 2) ab und schreibt x = 3. Was stimmt?', 'Falsch: Der Schnittpunkt mit y = 3 ist (2 | 3), also x = 2.',
    ['Richtig.', 'Falsch: x = 6.', 'Falsch: x = 1/2.'], 'Auf der Geraden y = 3 hat jeder Punkt die y-Koordinate 3. Der Schnittpunkt ist (2 | 3), weil 6/2 = 3.', 'Welche Koordinate muss auf der Geraden y = 3 gleich 3 sein?'))
ST.neu('graphisch', 'pruefung', SZ('Der Graph von f(x) = a/x geht durch (2 | 5). An welcher Stelle x hat f den Wert 4?', 2.5, '2 * 5 / 4', 'a = 2 · 5 = 10. 10/x = 4 ⇒ x = 2,5.', 'Bestimme zuerst a mit dem Punkt.'))
ST.knobel('graphisch', SZ('Für wie viele ganze Zahlen x liegt der Graph von f(x) = 6/x oberhalb der Geraden y = 1?', 5, '5 - 1 + 1',
    'Für negative x ist 6/x negativ, also unter y = 1. Für positive x: 6/x > 1 ⇔ x < 6. Ganze Zahlen: 1, 2, 3, 4, 5 – fünf.',
    'Unterscheide positive und negative x.'))
ST.knobel('graphisch', SA('Die Hyperbel y = k/x und die Gerade y = −x + 5 schneiden sich in (1 | 4). Wo liegt der zweite Schnittpunkt?', '(4 | 1)', ['(−1 | −4)', '(4 | −1)', '(2 | 3)'],
    'k = 1 · 4 = 4. Gesucht x mit 4/x = −x + 5. x = 4 passt: 4/4 = 1 und −4 + 5 = 1. Beide Graphen sind spiegelbildlich zur Geraden y = x – deshalb sind die Koordinaten vertauscht.',
    'Bestimme k und probiere, ob das Vertauschen der Koordinaten hilft.'))
baue = mit_stufen(baue, ST)
# ---- STUFEN ENDE ----

# ---------- TEXT: Zweiundzwanzigste Runde (18.11., Auftrag des Lehrers) – mehr Textaufgaben, siehe _text_kl8.py ----------
from _text_kl8 import Text, mit_text, text_auf_datei  # noqa: E402
TX = Text('gleichungen.bruch', 22_8_5)
TZ, TA, TL, TW = TX.Z, TX.A, TX.L, TX.W

# --- definitionsmenge ---
TX.u('definitionsmenge', 'direkt', TZ('Für eine Busfahrt gilt: Jeder zahlt 480/x Euro. Man löst 480/x = 16. Welche Zahl gehört nicht zur Definitionsmenge?', '0',
    TW('Nenner x.', 'ausgeschlossene Zahl.', 'Nenner = 0.', 'x = 0.', 'D = ℚ \\ {0}.'), 'Wann wird der Nenner 0?'))
TX.u('definitionsmenge', 'einkleidung', TZ('Gegen die Strömung braucht ein Boot für 36 km die Zeit 36/(v − 3) Stunden. Man löst 36/(v − 3) = 4. Welche Zahl ist ausgeschlossen?', '3',
    TW('Nenner v − 3.', 'ausgeschlossene Zahl.', 'Nenner = 0.', 'v = 3.', 'D = ℚ \\ {3}.'), 'Setze den Nenner gleich 0.'))
TX.u('definitionsmenge', 'mehrschritt', TX.A('Ein Radfahrer fährt hin mit v, zurück mit (v + 2) km/h; Gesamtzeit 12/v + 12/(v + 2) = 5. Welche Definitionsmenge hat die Gleichung?', 'ℚ \\ {−2; 0}', ['ℚ \\ {0}', 'ℚ \\ {2; 0}', 'ℚ \\ {5}'],
    TW('Nenner v und v + 2.', 'D.', 'Jeden Nenner = 0.', 'v = 0, v = −2.', 'D = ℚ \\ {−2; 0}.'), 'Es gibt zwei Nenner.'))
TX.u('definitionsmenge', 'pruefung', TZ('Ein 25-m-Becken wird mit zwei Leitungen gefüllt; die erste allein braucht 6 h. Für die zweite gilt 1/6 + 1/(x − 2) = 1/3. Welche Zahl ist ausgeschlossen?', '2',
    TW('Nenner 6, 3 und x − 2; die Beckenlänge spielt keine Rolle.', 'ausgeschlossene Zahl.', 'Nur x − 2 kann 0 werden.', 'x = 2.', 'D = ℚ \\ {2}.'), 'Welche Nenner enthalten x?'), huerde='ueberfluessig')
TX.u('definitionsmenge', 'fehler', TX.A('Für die Kosten pro Kind gilt (240 + 4x)/x = 10. Jemand sagt: „D = ℚ \\ {−60}, weil 240 + 4x dort 0 wird.“ Was stimmt?',
    'Falsch: Nur der Nenner zählt – D = ℚ \\ {0}.', ['Richtig.', 'Falsch: D = ℚ \\ {10}.', 'Falsch: D = ℚ.'],
    TW('Nenner x.', 'richtige D.', 'Nur Nenner prüfen.', 'x ≠ 0.', 'D = ℚ \\ {0}.'), 'Welcher Teil eines Bruchs darf nicht 0 sein?'), huerde='entscheidung')
TX.u('definitionsmenge', 'transfer', TX.A('300 € Hüttenmiete werden geteilt, 4 Betreuer zahlen nichts: 300/(x − 4) = 15 (x = alle Personen). In die Hütte passen 30 Personen. Was gilt?', 'x ≠ 4 – und die Lösung x = 24 passt auch zur Hütte.', ['x ≠ 0; Lösung 20.', 'x ≠ 4; Lösung 20.', 'x ≠ 15; Lösung 24.'],
    TW('D = ℚ \\ {4}; höchstens 30 Personen.', 'D und sinnvolle Lösung.', 'Nenner prüfen, lösen, mit 30 vergleichen.', 'x − 4 = 20 ⇒ x = 24 ≤ 30.', 'x ≠ 4; Lösung 24 Personen.'), 'Löse und vergleiche mit der Hüttengröße.'), huerde='zwei')
TX.s('definitionsmenge', TZ('Für eine Fahrt gilt 150/(v + 10) = 2. Welche Zahl ist ausgeschlossen?', '-10',
    TW('Nenner v + 10.', 'ausgeschlossene Zahl.', 'v + 10 = 0.', 'v = −10.', 'D = ℚ \\ {−10}.')))
TX.s('definitionsmenge', TZ('Für die Kosten pro Person gilt 360/(x − 2) = 20. Welche Zahl ist ausgeschlossen?', '2',
    TW('Nenner x − 2.', 'ausgeschlossene Zahl.', 'x − 2 = 0.', 'x = 2.', 'D = ℚ \\ {2}.')))
TX.k('definitionsmenge', TZ('Für eine Fahrzeit gilt 80/(v − 5) = 4. Welche Zahl ist ausgeschlossen?', '5',
    TW('Nenner v − 5.', 'ausgeschlossene Zahl.', 'v − 5 = 0.', 'v = 5.', 'D = ℚ \\ {5}.')))

# --- ein_bruch ---
TX.u('ein_bruch', 'direkt', TZ('480 € Busmiete werden geteilt, jeder zahlt 16 €: 480/x = 16. Wie viele Personen fahren mit?', '480 / 16',
    TW('480/x = 16.', 'x.', 'Mit x multiplizieren, durch 16 teilen.', 'x = 30.', 'Es fahren 30 Personen mit.'), 'Multipliziere mit x.'))
TX.u('ein_bruch', 'einkleidung', TZ('Ein Zug braucht für 270 km genau 2,25 Stunden. Mit welcher Durchschnittsgeschwindigkeit fährt er? (270/v = 2,25)', '270 / 2.25',
    TW('270/v = 2,25.', 'v.', 'Mit v multiplizieren.', '2,25v = 270 ⇒ v = 120.', 'Er fährt 120 km/h.'), 'Stelle nach v um.', einheit='km/h'))
TX.u('ein_bruch', 'mehrschritt', TZ('Ein Fotobuch kostet pro Stück (90 + 12x)/x Euro bei x Exemplaren. Bei wie vielen Exemplaren kostet jedes 15 €?', '90 / (15 - 12)',
    TW('(90 + 12x)/x = 15.', 'x.', 'Mit x multiplizieren.', '90 + 12x = 15x ⇒ x = 30.', 'Bei 30 Exemplaren.'), 'Multipliziere beide Seiten mit x.'))
TX.u('ein_bruch', 'pruefung', TZ('Ein Klassenfoto kostet pro Kind 90/x + 2 Euro. Der Fotograf kommt um 8 Uhr, jedes Kind bekommt 2 Abzüge. Bei wie vielen Kindern zahlt jedes 5,60 €?', '90 / (5.6 - 2)',
    TW('90/x + 2 = 5,6; Uhrzeit und Abzüge spielen keine Rolle.', 'x.', '2 abziehen, nach x umstellen.', '90/x = 3,6 ⇒ x = 25.', 'Bei 25 Kindern.'), 'Welche Angaben stehen in der Gleichung?'), huerde='ueberfluessig')
TX.u('ein_bruch', 'transfer', TZ('Gibt man zu 3 l Saft x Liter Wasser, ist der Saftanteil 3/(3 + x). Er soll höchstens 20 % betragen. Wie viele Liter Wasser braucht man mindestens?', '3 / 0.2 - 3',
    TW('3/(3 + x) = 0,2 als Grenze.', 'kleinstes x.', 'Gleichung lösen, dann deuten.', '3 = 0,6 + 0,2x ⇒ x = 12.', 'Mindestens 12 l Wasser.'), 'Mehr Wasser – kleinerer Anteil.', einheit='l'), huerde='deuten')
TX.u('ein_bruch', 'fehler', TX.A('Ein Auto fährt eine Strecke in 3/4 Stunden mit 80 km/h. Jemand löst s/80 = 3/4 so: s = 80 : 3/4 ≈ 106,7 km. Was stimmt?',
    'Falsch: s = 80 · 3/4 = 60 km.', ['Richtig.', 'Falsch: s = 3/4 : 80.', 'Falsch: s = 120 km.'],
    TW('s/80 = 3/4.', 'richtiges s.', 'Mit 80 multiplizieren.', '80 · 0,75 = 60.', 'Die Strecke ist 60 km.'), 'Was ist die Umkehrung von „durch 80“?'), huerde='entscheidung')
TX.s('ein_bruch', TZ('Jeder zahlt 360/x = 12 Euro. Wie viele Personen sind es?', '360 / 12',
    TW('360/x = 12.', 'x.', 'Umstellen.', 'x = 30.', '30 Personen.')))
TX.s('ein_bruch', TZ('Für eine Fahrt gilt 200/v = 2,5. Wie schnell ist man?', '200 / 2.5',
    TW('200/v = 2,5.', 'v.', 'Umstellen.', 'v = 80.', '80 km/h.'), einheit='km/h'))
TX.k('ein_bruch', TZ('Pro Stück gilt 120/x + 3 = 7 Euro. Wie viele Stück sind es?', '120 / 4',
    TW('120/x = 4.', 'x.', 'Umstellen.', 'x = 30.', '30 Stück.')))

# --- ueber_kreuz ---
TX.u('ueber_kreuz', 'direkt', TZ('Ein Auto fährt 120 km in derselben Zeit wie ein Rad 30 km. Das Auto ist 45 km/h schneller: 120/(v + 45) = 30/v. Wie schnell ist das Rad?', '30 * 45 / 90',
    TW('120/(v + 45) = 30/v.', 'v.', 'Über Kreuz multiplizieren.', '120v = 30v + 1 350 ⇒ 90v = 1 350 ⇒ v = 15.', 'Das Rad fährt 15 km/h.'), 'Multipliziere über Kreuz.', einheit='km/h'))
TX.u('ueber_kreuz', 'einkleidung', TZ('Ein Lkw fährt 90 km, ein Pkw in derselben Zeit 120 km; der Pkw ist 10 km/h schneller. Wie schnell ist der Lkw? (90/v = 120/(v + 10))', '900 / 30',
    TW('90/v = 120/(v + 10).', 'v.', 'Über Kreuz.', '90v + 900 = 120v ⇒ v = 30.', 'Der Lkw fährt 30 km/h.'), 'Gleiche Zeit – die Brüche sind gleich.', einheit='km/h'))
TX.u('ueber_kreuz', 'mehrschritt', TZ('Saft und Wasser: In Glas A sind 2 dl Saft in x dl Getränk, in Glas B 3 dl Saft in (x + 2) dl Getränk. Beide schmecken gleich stark: 2/x = 3/(x + 2). Wie viele dl enthält Glas A?', '4',
    TW('2/x = 3/(x + 2).', 'x.', 'Über Kreuz.', '2x + 4 = 3x ⇒ x = 4.', 'Glas A enthält 4 dl.'), 'Gleich stark heißt gleicher Anteil.', einheit='dl'))
TX.u('ueber_kreuz', 'pruefung', TZ('Zwei Wanderer starten um 8 Uhr mit gleich schwerem Gepäck. A läuft 12 km in derselben Zeit wie B 15 km; B ist 1 km/h schneller. Wie schnell ist A? (12/v = 15/(v + 1))', '4',
    TW('12/v = 15/(v + 1); Uhrzeit und Gepäck spielen keine Rolle.', 'v.', 'Über Kreuz.', '12v + 12 = 15v ⇒ v = 4.', 'A läuft 4 km/h.'), 'Welche Angaben brauchst du nicht?', einheit='km/h'), huerde='ueberfluessig')
TX.u('ueber_kreuz', 'fehler', TX.A('Für zwei Boote gilt 24/(v − 2) = 36/(v + 2). Jemand multipliziert über Kreuz und schreibt: 24(v − 2) = 36(v + 2). Was stimmt?',
    'Falsch: Richtig ist 24(v + 2) = 36(v − 2), also v = 10.', ['Richtig.', 'Falsch: 24 · 36 = (v − 2)(v + 2).', 'Falsch: 24 + (v + 2) = 36 + (v − 2).'],
    TW('24/(v − 2) = 36/(v + 2).', 'richtiger Ansatz.', 'Zähler links mal Nenner rechts.', '24v + 48 = 36v − 72 ⇒ v = 10.', 'Der Ansatz ist vertauscht; v = 10.'), 'Was wird beim Über-Kreuz-Multiplizieren mit was multipliziert?'), huerde='entscheidung')
TX.u('ueber_kreuz', 'begruenden', TX.A('Für zwei Fahrten gilt 60/v = 90/(v + 20). Jemand erhält v = 40 und sagt: „Der Roller fährt 40 km/h, das Auto 60 km/h.“ Was stimmt?',
    'Richtig: 60/40 = 1,5 h und 90/60 = 1,5 h.', ['Falsch: v = 20.', 'Falsch: Das Auto fährt 90 km/h.', 'Falsch: Die Zeiten sind verschieden.'],
    TW('60/v = 90/(v + 20).', 'Prüfen.', 'Probe mit v = 40.', '60/40 = 1,5; 90/60 = 1,5.', 'Die Aussage stimmt.'), 'Mache die Probe.'), huerde='entscheidung')
TX.s('ueber_kreuz', TZ('Löse 20/v = 30/(v + 5) (zwei Läufer, gleiche Zeit). Wie groß ist v?', '10',
    TW('20/v = 30/(v + 5).', 'v.', 'Über Kreuz.', '20v + 100 = 30v ⇒ v = 10.', 'v = 10.'), einheit='km/h'))
TX.s('ueber_kreuz', TZ('Löse 40/x = 60/(x + 10) (zwei Gruppen, gleicher Betrag pro Person). Wie groß ist x?', '20',
    TW('40/x = 60/(x + 10).', 'x.', 'Über Kreuz.', '40x + 400 = 60x ⇒ x = 20.', 'x = 20.')))
TX.k('ueber_kreuz', TZ('Löse 30/v = 45/(v + 10) (zwei Fahrzeuge, gleiche Zeit). Wie groß ist v?', '20',
    TW('30/v = 45/(v + 10).', 'v.', 'Über Kreuz.', '30v + 300 = 45v ⇒ v = 20.', 'v = 20.'), einheit='km/h'))

# --- hauptnenner ---
TX.u('hauptnenner', 'direkt', TZ('Rohr A füllt einen Tank allein in 6 h, zusammen mit Rohr B dauert es 4 h: 1/6 + 1/x = 1/4. Wie lange braucht Rohr B allein?', '1 / (1/4 - 1/6)',
    TW('1/6 + 1/x = 1/4.', 'x.', 'Hauptnenner 12x.', '2x + 12 = 3x ⇒ x = 12.', 'Rohr B braucht 12 h.'), 'Multipliziere mit dem Hauptnenner 12x.', einheit='h'))
TX.u('hauptnenner', 'pruefung', TZ('Zwei Mähroboter mähen einen 800 m² großen Rasen. Der erste allein braucht 3 h, zusammen brauchen sie 2 h. Wie lange braucht der zweite allein?', '1 / (1/2 - 1/3)',
    TW('1/3 + 1/x = 1/2; die Fläche spielt keine Rolle.', 'x.', 'Hauptnenner 6x.', '2x + 6 = 3x ⇒ x = 6.', 'Der zweite braucht allein 6 h.'), 'Welche Angabe gehört nicht in die Gleichung?', einheit='h'), huerde='ueberfluessig')
TX.u('hauptnenner', 'transfer', TZ('Ein Radfahrer fährt 24 km hin mit v km/h und zurück mit 2v km/h, insgesamt in 3 Stunden: 24/v + 24/(2v) = 3. Wie viele Minuten dauert die Rückfahrt?', '24 / 24 * 60',
    TW('24/v + 12/v = 3.', 'Rückfahrzeit in Minuten.', 'Lösen, dann Rückfahrt berechnen.', '36/v = 3 ⇒ v = 12; zurück 24 : 24 = 1 h.', 'Die Rückfahrt dauert 60 Minuten.'), 'Gefragt ist nur die Rückfahrt.', einheit='min'), huerde='deuten')
TX.s('hauptnenner', TZ('Zwei Hähne füllen eine Wanne: A allein in 10 min, zusammen in 6 min: 1/10 + 1/x = 1/6. Wie lange braucht B allein?', '1 / (1/6 - 1/10)',
    TW('1/10 + 1/x = 1/6.', 'x.', 'Hauptnenner 30x.', '3x + 30 = 5x ⇒ x = 15.', '15 min.'), einheit='min'))
TX.s('hauptnenner', TZ('Zwei Maler: A allein 4 Tage, zusammen 3 Tage: 1/4 + 1/x = 1/3. Wie lange braucht B allein?', '1 / (1/3 - 1/4)',
    TW('1/4 + 1/x = 1/3.', 'x.', 'Hauptnenner 12x.', '3x + 12 = 4x ⇒ x = 12.', '12 Tage.'), einheit='Tage'))
TX.k('hauptnenner', TZ('Zwei Pumpen: A allein 5 h, zusammen 4 h: 1/5 + 1/x = 1/4. Wie lange braucht B allein?', '1 / (1/4 - 1/5)',
    TW('1/5 + 1/x = 1/4.', 'x.', 'Hauptnenner 20x.', '4x + 20 = 5x ⇒ x = 20.', '20 h.'), einheit='h'))

# --- scheinloesung (Lösung im Sachzusammenhang prüfen) ---
TX.u('scheinloesung', 'erkennen', TX.A('Für die Fahrzeit gegen die Strömung gilt 24/(v − 4) = 3. Man erhält v = 12. Gehört die Lösung zur Definitionsmenge?', 'Ja, nur v = 4 ist ausgeschlossen.', ['Nein, 12 ist ausgeschlossen.', 'Nein, man muss v = 4 nehmen.'],
    TW('D = ℚ \\ {4}, Lösung 12.', 'Ist 12 erlaubt?', 'Mit D vergleichen.', '12 ≠ 4.', 'Die Lösung ist gültig.'), 'Welche Zahl ist ausgeschlossen?'))
TX.u('scheinloesung', 'einkleidung', TX.A('Gibt man zu 3 l Saft x Liter Wasser, ist der Saftanteil 3/(3 + x). Jemand möchte einen Anteil von 1,5 und löst 3/(3 + x) = 1,5. Er erhält x = −1. Was bedeutet das?',
    'Keine sinnvolle Lösung: Man kann kein Wasser wegnehmen – ein Anteil über 1 ist unmöglich.', ['Man gibt 1 l Wasser dazu.', 'Man gibt 1,5 l Wasser dazu.'],
    TW('3/(3 + x) = 1,5 ⇒ x = −1.', 'Deutung.', 'Lösung mit der Situation vergleichen.', 'x < 0 ist im Sachzusammenhang unmöglich.', 'Die Gleichung hat keine sinnvolle Lösung.'), 'Kann man −1 Liter Wasser dazugeben?'))
TX.u('scheinloesung', 'mehrschritt', TZ('Für die Kosten pro Person gilt 200/(x − 5) = 8 (x = alle Personen, 5 zahlen nichts). Löse und prüfe, ob die Lösung zu D gehört. Gib x an.', '200 / 8 + 5',
    TW('D = ℚ \\ {5}.', 'x.', 'Umstellen, mit D vergleichen.', 'x − 5 = 25 ⇒ x = 30 ≠ 5.', 'x = 30 ist gültig.'), 'Erst lösen, dann prüfen.'))
TX.u('scheinloesung', 'fehler', TX.A('Jemand löst (x − 4)/(x − 4) = 1 und sagt: „Jede Zahl ist eine Lösung.“ Was stimmt?', 'Falsch: Alle Zahlen außer 4.', ['Richtig.', 'Falsch: Nur x = 4.', 'Falsch: Keine Zahl.'],
    TW('D = ℚ \\ {4}.', 'Lösungsmenge.', 'Für x ≠ 4 ist der Bruch 1.', 'L = ℚ \\ {4}.', 'Alle Zahlen außer 4.'), 'Was ist bei x = 4 mit dem Nenner?'), huerde='entscheidung')
TX.u('scheinloesung', 'pruefung', TZ('Eine Gruppe von 12 Personen fährt mit einem 50-Sitzer-Bus. Für die Kosten pro Person gilt 600/(x + 12) = 20, wobei x Personen später dazukommen. Wie viele kommen dazu?', '600 / 20 - 12',
    TW('600/(x + 12) = 20; D = ℚ \\ {−12}; die Sitzzahl prüft nur die Obergrenze.', 'x.', 'Umstellen, prüfen.', 'x + 12 = 30 ⇒ x = 18; 30 ≤ 50 ✓.', 'Es kommen 18 Personen dazu.'), 'Prüfe die Lösung mit D und mit der Sitzzahl.'), huerde='zwei')
TX.u('scheinloesung', 'parameter', TX.A('Für die Fahrzeit gilt 60/(v − 10) = t. Für welches t ist v = 10 eine Lösung der Gleichung?', 'für kein t – v = 10 ist immer ausgeschlossen', ['für t = 0', 'für t = 6', 'für t = 60'],
    TW('D = ℚ \\ {10}.', 'Kann v = 10 Lösung sein?', 'v = 10 macht den Nenner 0.', 'Für kein t.', 'v = 10 kann nie Lösung sein.'), 'Darf v = 10 überhaupt eingesetzt werden?'))
TX.u('scheinloesung', 'transfer', TZ('Ein Becken wird von zwei Pumpen geleert: 1/x + 1/(x + 6) = 1/4 (x in h). Jemand erhält x = 6 und x = −4. Wie viele Stunden braucht die schnellere Pumpe allein?', '6',
    TW('x = 6 oder x = −4.', 'sinnvolle Lösung.', 'Negative Zeiten ausschließen.', 'x = −4 ist sinnlos.', 'Die schnellere Pumpe braucht 6 Stunden.'), 'Welche der beiden Zahlen kann eine Zeit sein?', einheit='h'), huerde='deuten')
TX.s('scheinloesung', TZ('Für eine Fahrt gilt 45/(v − 5) = 3. Löse und gib v an.', '45 / 3 + 5',
    TW('D = ℚ \\ {5}.', 'v.', 'Umstellen.', 'v − 5 = 15 ⇒ v = 20.', 'v = 20 ist gültig.'), einheit='km/h'))
TX.s('scheinloesung', TX.A('Für den Saftanteil gilt 2/(2 + x) = 2. Was gilt für die Lösung?', 'x = −1, im Sachzusammenhang sinnlos.', ['x = 1, gültig.', 'x = 0, gültig.'],
    TW('2 = 4 + 2x.', 'x.', 'Umstellen, deuten.', 'x = −1.', 'Keine sinnvolle Lösung.')))
TX.k('scheinloesung', TZ('Für die Kosten pro Person gilt 120/(x − 3) = 10. Löse und gib x an.', '120 / 10 + 3',
    TW('D = ℚ \\ {3}.', 'x.', 'Umstellen.', 'x − 3 = 12 ⇒ x = 15.', 'x = 15.')))

# --- verhaeltnis ---
TX.u('verhaeltnis', 'pruefung', TZ('Für eine Limonade werden Sirup und Wasser im Verhältnis 1 : 7 gemischt. Die Flasche ist 30 cm hoch. Wie viel ml Sirup braucht man für 1,2 l Limonade?', '1200 / 8',
    TW('1 : 7, also 1 von 8 Teilen; 1,2 l = 1 200 ml; die Flaschenhöhe spielt keine Rolle.', 'Sirup.', '1 200 : 8.', '150.', 'Man braucht 150 ml Sirup.'), 'Wie viele Teile hat die Mischung insgesamt?', einheit='ml'), huerde='ueberfluessig')
TX.u('verhaeltnis', 'fehler', TX.A('Beton wird aus Zement und Kies im Verhältnis 1 : 4 gemischt. Jemand will 50 kg Beton und nimmt 12,5 kg Zement. Was stimmt?', 'Falsch: 1 von 5 Teilen – 10 kg Zement.', ['Richtig: Zement ist ein Viertel des Betons.', 'Falsch: 40 kg Zement.', 'Falsch: 5 kg Zement.'],
    TW('1 : 4 → 5 Teile.', 'Zementmenge.', '50 : 5.', '10.', 'Man braucht 10 kg Zement.'), 'Wie viele Teile gibt es insgesamt?'), huerde='entscheidung')
TX.s('verhaeltnis', TZ('Saft und Wasser werden im Verhältnis 2 : 3 gemischt. Wie viel ml Saft sind in 500 ml Schorle?', '500 / 5 * 2',
    TW('2 von 5 Teilen.', 'Saft.', '500 : 5 · 2.', '200.', '200 ml.'), einheit='ml'))
TX.s('verhaeltnis', TZ('Ein Gewinn von 360 € wird im Verhältnis 4 : 5 geteilt. Wie viel bekommt der kleinere Teil?', '360 / 9 * 4',
    TW('4 von 9 Teilen.', 'kleinerer Teil.', '360 : 9 · 4.', '160.', '160 €.'), einheit='€'))

# --- graphisch ---
TX.u('graphisch', 'direkt', TZ('Die Kosten pro Person sind f(x) = 240/x Euro. Am Graphen liest man ab, wo f(x) = 8 ist. Für welches x ist das?', '240 / 8',
    TW('240/x = 8.', 'x.', 'Schnittpunkt mit y = 8.', 'x = 30.', 'Bei 30 Personen.'), 'Wo schneidet der Graph die Gerade y = 8?'))
TX.u('graphisch', 'einkleidung', TZ('Für eine 180-km-Fahrt gilt t(v) = 180/v. Am Graphen sucht man den Punkt mit t = 2. Welches v gehört dazu?', '180 / 2',
    TW('180/v = 2.', 'v.', 'Ablesen oder rechnen.', 'v = 90.', 'v = 90 km/h.'), 'Welcher x-Wert gehört zu y = 2?', einheit='km/h'))
TX.u('graphisch', 'darstellung', TZ('Ein Graph zeigt die Stückkosten k(x) = 300/x + 5. Er schneidet die Gerade y = 11. Bei welcher Stückzahl?', '300 / 6',
    TW('300/x + 5 = 11.', 'x.', 'Gleichung zum Schnittpunkt lösen.', '300/x = 6 ⇒ x = 50.', 'Bei 50 Stück.'), 'Stelle die Gleichung zum Schnittpunkt auf.'))
TX.u('graphisch', 'pruefung', TZ('Ein Klassenzimmer hat 30 Plätze. Für eine Klassenfahrt zeigt der Graph f(x) = 450/x + 12 die Kosten pro Kind. Bei welcher Kinderzahl schneidet er die Gerade y = 30?', '450 / 18',
    TW('450/x + 12 = 30; die Platzzahl spielt keine Rolle.', 'x.', 'Schnittpunkt berechnen.', '450/x = 18 ⇒ x = 25.', 'Bei 25 Kindern.'), 'Welche Angabe brauchst du nicht?'), huerde='ueberfluessig')
TX.u('graphisch', 'transfer', TX.A('Die Graphen von k(x) = 600/x + 4 (Anbieter A) und der Geraden y = 10 (Anbieter B, fester Preis) schneiden sich. Für welche Stückzahlen ist A günstiger?', 'ab mehr als 100 Stück', ['bis 100 Stück', 'ab 60 Stück', 'nie'],
    TW('600/x + 4 = 10 ⇒ x = 100.', 'Bereich, in dem A unten liegt.', 'Schnittpunkt, dann rechts davon.', 'Für x > 100 ist 600/x + 4 < 10.', 'A ist ab mehr als 100 Stück günstiger.'), 'Liegt der Graph von A rechts vom Schnittpunkt über oder unter y = 10?'), huerde='entscheidung')
TX.u('graphisch', 'fehler', TX.A('Für die Fahrzeit gilt t(v) = 120/v. Jemand liest am Graphen ab: „Bei t = 3 ist v = 360.“ Was stimmt?', 'Falsch: 120/v = 3 ⇒ v = 40.', ['Richtig.', 'Falsch: v = 3.', 'Falsch: v = 117.'],
    TW('120/v = 3.', 'richtiges v.', 'Umstellen.', 'v = 40.', 'v = 40 km/h.'), 'Hat man multipliziert statt geteilt?'), huerde='deuten')
TX.s('graphisch', TZ('Der Graph von f(x) = 360/x schneidet y = 12. Bei welchem x?', '360 / 12',
    TW('360/x = 12.', 'x.', 'Umstellen.', '30.', 'x = 30.')))
TX.s('graphisch', TZ('Der Graph von k(x) = 200/x + 3 schneidet y = 7. Bei welchem x?', '200 / 4',
    TW('200/x = 4.', 'x.', 'Umstellen.', '50.', 'x = 50.')))
TX.k('graphisch', TZ('Der Graph von t(v) = 150/v schneidet t = 2,5. Bei welchem v?', '150 / 2.5',
    TW('150/v = 2,5.', 'v.', 'Umstellen.', '60.', 'v = 60.'), einheit='km/h'))
baue = mit_text(baue, TX)
# ---- TEXT ENDE ----

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Bruchgleichungen lösen', ['definitionsmenge', 'ein_bruch', 'ueber_kreuz', 'hauptnenner']), ('Prüfen', ['scheinloesung']), ('Verhältnisse und Graphen', ['verhaeltnis', 'graphisch'])],
         'Bruchgleichungen lösen, dabei die Definitionsmenge beachten, und Verhältnisgleichungen mit der Produktgleichheit lösen.',
         ['Erst D bestimmen: Kein Nenner darf 0 werden.', 'Mit dem (Haupt-)Nenner multiplizieren, dann linear lösen.',
          'Lösung nicht in D → Scheinlösung, L = { }.', 'a : b = c : d ⇔ a · d = b · c.'],
         offen=['Prüfvorschlag „grafisch deuten“ für ein_bruch ist in der neuen Karte „graphisch“ umgesetzt (dort passt er zum Lernziel).'])
