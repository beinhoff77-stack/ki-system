#!/usr/bin/env python3
"""Thema gleichungen.bruch – Bruch- und Verhältnisgleichungen (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, Z, baue, bruch, cz, ist_endlich, kl, lin, mit_bild, zt  # noqa: E402

META = {'thema_schluessel': 'gleichungen.bruch', 'thema_id': 5, 'block_id': 60, 'klasse': {'gym_by': 8, 'rs_by': 8}}

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

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Bruchgleichungen lösen', ['definitionsmenge', 'ein_bruch', 'ueber_kreuz', 'hauptnenner']), ('Prüfen', ['scheinloesung']), ('Verhältnisse und Graphen', ['verhaeltnis', 'graphisch'])],
         'Bruchgleichungen lösen, dabei die Definitionsmenge beachten, und Verhältnisgleichungen mit der Produktgleichheit lösen.',
         ['Erst D bestimmen: Kein Nenner darf 0 werden.', 'Mit dem (Haupt-)Nenner multiplizieren, dann linear lösen.',
          'Lösung nicht in D → Scheinlösung, L = { }.', 'a : b = c : d ⇔ a · d = b · c.'],
         offen=['Prüfvorschlag „grafisch deuten“ für ein_bruch ist in der neuen Karte „graphisch“ umgesetzt (dort passt er zum Lernziel).'])
