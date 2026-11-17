#!/usr/bin/env python3
"""Thema terme.bruchterme – Bruchterme (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, L, Z, baue, bruch, cz, einsetzen, ist_endlich, kl, lin, mono, pot, zt  # noqa: E402

META = {'thema_schluessel': 'terme.bruchterme', 'thema_id': 31, 'block_id': 60, 'klasse': {'gym_by': 8, 'rs_by': 8}}

ETAPPEN = [
    {'lernziel': 'definitionsmenge', 'titel': 'Definitionsmenge bestimmen',
     'regel': 'Ein ⟦Bruchterm⟧ hat eine Variable im Nenner. Durch 0 darf man nicht teilen. Die ⟦Definitionsmenge⟧ D enthält alle Zahlen, für die ⟦kein Nenner 0⟧ wird.',
     'schritte': ['5/(x − 3): Nenner x − 3 = 0 für x = 3.', 'Also ⟦D = ℚ \\ {3}⟧ (alle rationalen Zahlen außer 3).'],
     'fehler': 'Bei (x − 2)/(x + 4) ist nicht 2 auszuschließen: Der ⟦Zähler⟧ darf 0 sein. Nur x = −4 macht den ⟦Nenner⟧ 0, also D = ℚ \\ {−4}.',
     '_verbot': ['5/(x − 3)']},
    {'lernziel': 'termwert', 'titel': 'Werte von Bruchtermen berechnen',
     'regel': 'Setze die Zahl für x ein und rechne ⟦Zähler und Nenner getrennt⟧ aus. Liegt die Zahl nicht in D, hat der Term ⟦keinen Wert⟧.',
     'schritte': ['T(x) = (2x + 1)/(x − 1) für x = 3', 'Zähler: 2 · 3 + 1 = 7, Nenner: 3 − 1 = 2', 'T(3) = 7/2 = ⟦3,5⟧'],
     'fehler': 'Für x = 1 ist T(1) nicht 3/0 = 0: Durch 0 teilen geht nicht. T(1) ist ⟦nicht definiert⟧.',
     '_verbot': ['(2x + 1)/(x − 1)']},
    {'lernziel': 'kuerzen', 'titel': 'Bruchterme kürzen',
     'regel': 'Kürzen heißt: Zähler und Nenner durch denselben ⟦Faktor⟧ teilen. Summen musst du vorher ⟦ausklammern⟧ – aus Summen darf man nicht kürzen.',
     'schritte': ['(3x + 6)/(5x + 10)', '= 3(x + 2)/(5(x + 2))', '(x + 2) kürzen: ⟦3/5⟧ (für x ≠ −2)'],
     'fehler': '(x + 6)/3 ist nicht x + 2: Die 6 ist ein ⟦Summand⟧, kein Faktor. Richtig wäre nur (3x + 6)/3 = x + 2.',
     '_verbot': ['(3x + 6)/(5x + 10)']},
    {'lernziel': 'erweitern', 'titel': 'Bruchterme erweitern',
     'regel': 'Erweitern heißt: Zähler und Nenner mit demselben Term ⟦multiplizieren⟧. So machst du Brüche ⟦gleichnamig⟧ (gleicher Nenner).',
     'schritte': ['3/(2x) soll den Nenner 8x² bekommen.', '8x² : (2x) = 4x, also mit 4x erweitern.', 'Neuer Zähler: 3 · 4x = ⟦12x⟧'],
     'fehler': 'Erweitert man 3/(2x) mit 4x, wird nicht nur der Nenner multipliziert. Auch der ⟦Zähler⟧ ändert sich: 12x/(8x²), nicht 3/(8x²).',
     '_verbot': ['3/(2x)']},
    {'lernziel': 'addieren', 'titel': 'Bruchterme addieren und subtrahieren',
     'regel': 'Es geht genau wie bei Zahlenbrüchen: 2/7 + 3/7 = 5/7. Gleicher Nenner: ⟦Zähler addieren⟧, der Nenner bleibt. Verschiedene Nenner: erst auf den ⟦Hauptnenner⟧ erweitern.',
     'schritte': ['2/x + 3/(4x): Hauptnenner 4x.', '2/x = 8/(4x)', '8/(4x) + 3/(4x) = ⟦11/(4x)⟧'],
     'fehler': '2/x + 3/x ist nicht 5/(2x): Die ⟦Nenner werden nicht addiert⟧. Prüfe mit x = 1: 2 + 3 = 5, aber 5/2 = 2,5. Richtig ist 5/x.',
     '_verbot': ['2/x + 3/(4x)']},
    {'lernziel': 'multiplizieren', 'titel': 'Bruchterme multiplizieren und dividieren',
     'regel': 'Multiplizieren: ⟦Zähler mal Zähler, Nenner mal Nenner⟧, dann kürzen. Dividieren: mit dem ⟦Kehrbruch⟧ multiplizieren.',
     'schritte': ['(4x/9) · (3/x²): Schreibe alles auf einen Bruchstrich: (4x · 3)/(9 · x²).', 'Erst kürzen, dann rechnen: 3 mit 9 kürzen gibt 1 und 3; x mit x² kürzen gibt 1 und x.', 'Übrig bleibt ⟦4/(3x)⟧.'],
     'fehler': 'Bei (2/x) : (4/x²) den Kehrbruch vom ⟦ersten⟧ Bruch nehmen: (x/2) · (4/x²) = 2/x ist falsch. Umgedreht wird der Bruch, ⟦durch den⟧ du teilst: (2/x) · (x²/4) = 2x²/(4x) = x/2.',
     '_verbot': ['(4x/9) · (3/x²)']},
    {'lernziel': 'fehler_finden', 'titel': 'Richtig oder falsch umgeformt?',
     'regel': 'Prüfe eine Umformung, indem du eine ⟦Zahl einsetzt⟧ (aus D). Kommt links und rechts etwas anderes heraus, ist die Umformung ⟦falsch⟧.',
     'schritte': ['Behauptung: (x + 4)/4 = x + 1', 'Teste x = 4: links 8/4 = 2, rechts 5.', '2 ≠ 5, also ⟦falsch⟧. Richtig: (x + 4)/4 = x/4 + 1.'],
     'fehler': 'Ein einziges passendes Beispiel beweist keine Umformung: (x + 4)/4 = x + 1 stimmt zufällig für x = 0. Ein ⟦Gegenbeispiel⟧ genügt aber, um sie zu widerlegen.',
     '_verbot': ['(x + 4)/4 = x + 1']},
]


# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'definitionsmenge': {
  'einstieg': 'Eine Klasse mietet für einen Ausflug einen Bus für 600 €. Jeder zahlt seinen Anteil: 600 € geteilt durch die Anzahl x der Mitfahrenden, also 600/x Euro. Bei 20 Mitfahrenden sind das 30 €. Aber was ist bei x = 0? Durch 0 kann man nicht teilen – diesen Wert gibt es nicht. Ein Term mit x im Nenner heißt ⟦Bruchterm⟧.',
  'woerter': [['Bruchterm', 'ein Bruch, in dessen Nenner ein x vorkommt, z. B. 600/x'], ['Zähler / Nenner', 'was über / unter dem Bruchstrich steht'],
              ['5/(x − 3)', '5 geteilt durch (x − 3)'], ['ℚ', 'alle Bruchzahlen (rationale Zahlen), positive und negative'],
              ['ℚ \\ {3}', 'alle diese Zahlen außer der 3'], ['Definitionsmenge D', 'alle Zahlen, die man für x einsetzen darf']],
  'schritte': ['Term: 5/(x − 3). Frage: Welche Zahl darf man für x nicht einsetzen?', 'Der Nenner x − 3 darf nicht 0 werden.',
               'x − 3 ist 0, wenn x = 3 ist. Diese Zahl muss also raus.', 'Ergebnis: ⟦D = ℚ \\ {3}⟧, also alle Zahlen außer 3.'],
  'regel': 'So bestimmst du die ⟦Definitionsmenge⟧: Jeden Nenner gleich 0 setzen und ausrechnen, für welches x das passiert. Diese Zahlen streichst du: D = ℚ \\ {…}.',
  'fehler': 'Bei (x − 2)/(x + 4) muss die 2 nicht raus: Ein ⟦Zähler⟧ 0 ist kein Problem – 0 € auf 6 Personen verteilt sind eben 0 € pro Person. Nur x = −4 macht den ⟦Nenner⟧ 0, also D = ℚ \\ {−4}.'},
 'termwert': {
  'einstieg': 'Beim Busausflug zahlt jeder 600/x Euro. Fahren 24 Kinder mit, rechnest du 600 : 24 = 25 € pro Person. Für jede Anzahl x kann man so einen Betrag ausrechnen – das ist der ⟦Termwert⟧. Nur für x = 0 gibt es keinen.',
  'woerter': [['T(x)', 'ein Name für den Term; T(3) heißt: der Wert, wenn man 3 für x einsetzt'], ['Termwert', 'das Ergebnis nach dem Einsetzen'],
              ['nicht definiert', 'es gibt keinen Wert, weil man durch 0 teilen müsste']],
  'schritte': ['T(x) = (2x + 1)/(x − 1). Gesucht ist T(3), also der Wert für x = 3.', 'Zuerst den Zähler ausrechnen: 2 · 3 + 1 = 7.',
               'Dann den Nenner ausrechnen: 3 − 1 = 2.', 'Zum Schluss teilen: T(3) = 7/2 = ⟦3,5⟧.'],
  'regel': 'So berechnest du einen ⟦Termwert⟧: Zahl für x einsetzen, ⟦Zähler und Nenner getrennt⟧ ausrechnen, dann teilen. Wird der Nenner 0, ist der Term dort ⟦nicht definiert⟧.',
  'fehler': 'T(1) ist nicht 3/0 = 0. Durch 0 teilen geht nicht – 600 € auf 0 Mitfahrende zu verteilen ergibt keinen Preis. T(1) ist ⟦nicht definiert⟧.'},
 'kuerzen': {
  'einstieg': 'Beim Bruch 6/10 teilst du oben und unten durch 2 und erhältst 3/5 – derselbe Anteil, nur einfacher geschrieben. Das klappt auch mit Termen. Allerdings nur mit Teilen, die oben und unten ⟦malgenommen⟧ werden, nicht mit Teilen, die addiert werden. Dieses Vereinfachen heißt ⟦Kürzen⟧.',
  'woerter': [['Kürzen', 'Zähler und Nenner durch dasselbe teilen; der Wert bleibt gleich'], ['Faktor', 'ein Teil, der malgenommen wird: in 3(x + 2) sind 3 und (x + 2) Faktoren'],
              ['Summand', 'ein Teil, der addiert wird: in x + 6 sind x und 6 Summanden'], ['ausklammern', 'eine gemeinsame Zahl vor eine Klammer ziehen: 3x + 6 = 3(x + 2)'],
              ['x ≠ −2', 'x darf nicht −2 sein']],
  'schritte': ['Aufgabe: (3x + 6)/(5x + 10) kürzen.', 'Oben steckt in beiden Teilen eine 3: 3x + 6 = 3(x + 2). Unten steckt eine 5: 5x + 10 = 5(x + 2).',
               'Jetzt steht oben und unten derselbe Faktor (x + 2). Den darf man kürzen.', 'Übrig bleibt ⟦3/5⟧. Das gilt für alle x außer −2, weil dort der Nenner 0 wäre.'],
  'regel': 'So kürzt du: Zähler und Nenner erst in ⟦Faktoren⟧ zerlegen (⟦ausklammern⟧), dann gleiche Faktoren oben und unten streichen. Aus Summen darf man nicht kürzen.',
  'fehler': '(x + 6)/3 ist nicht x + 2. Die 6 ist ein ⟦Summand⟧, kein Faktor. Das wäre, als würde man bei „Pizza plus 6 € Lieferung, durch 3 geteilt“ nur die Lieferung teilen. Richtig wäre nur (3x + 6)/3 = x + 2.'},
 'erweitern': {
  'einstieg': 'Aus 1/2 Pizza werden 4/8 Pizza, wenn du die Pizza in 8 statt in 2 Stücke schneidest: oben und unten mal 4. Der Anteil bleibt gleich, nur die Stücke sind kleiner. Dieses Malnehmen von Zähler und Nenner mit derselben Zahl heißt ⟦Erweitern⟧. Man braucht es, um Brüche auf denselben Nenner zu bringen.',
  'woerter': [['Erweitern', 'Zähler und Nenner mit demselben malnehmen; der Wert bleibt gleich'], ['gleichnamig', 'Brüche mit demselben Nenner'], ['x²', 'kurz für x · x'],
              ['8x² : (2x)', 'die Frage: Womit muss ich 2x malnehmen, um 8x² zu bekommen?']],
  'schritte': ['Aufgabe: 3/(2x) soll den Nenner 8x² bekommen.', 'Womit muss man 2x malnehmen, um 8x² zu erhalten? 8 : 2 = 4 und x² : x = x, also mit 4x.',
               'Auch der Zähler wird mit 4x malgenommen: 3 · 4x = 12x.', 'Ergebnis: 3/(2x) = 12x/(8x²). Der neue Zähler ist ⟦12x⟧.'],
  'regel': 'So erweiterst du: ⟦neuen Nenner durch alten Nenner⟧ teilen – mit dem Ergebnis nimmst du ⟦Zähler und Nenner⟧ mal. So machst du Brüche ⟦gleichnamig⟧.',
  'fehler': 'Nur den Nenner malnehmen ist falsch: 3/(8x²) ist viel weniger als 3/(2x) – wie wenn du die Pizza in mehr Stücke schneidest, aber trotzdem nur 3 Stücke nimmst. Auch der ⟦Zähler⟧ ändert sich: 12x/(8x²).'},
 'addieren': {
  'einstieg': '2/7 Kuchen plus 3/7 Kuchen sind 5/7 Kuchen: Die Stücke sind gleich groß, du zählst nur die Stücke zusammen. Bei verschieden großen Stücken, etwa Halben und Dritteln, schneidest du erst alles in gleich große Stücke. Mit Bruchtermen geht das genauso; der gemeinsame Nenner heißt ⟦Hauptnenner⟧.',
  'woerter': [['Hauptnenner', 'der kleinste gemeinsame Nenner aller Brüche'], ['2/x', '2 geteilt durch x'], ['4x', 'kurz für 4 · x']],
  'schritte': ['Aufgabe: 2/x + 3/(4x).', 'Der Hauptnenner ist 4x, denn x passt in 4x hinein: 4x : x = 4.', 'Den ersten Bruch mit 4 erweitern: 2/x = 8/(4x).',
               'Jetzt sind die Nenner gleich. Die Zähler addieren: 8 + 3 = 11. Ergebnis ⟦11/(4x)⟧.'],
  'regel': 'So addierst du Bruchterme: Bei gleichem Nenner die ⟦Zähler addieren⟧, der Nenner bleibt. Bei verschiedenen Nennern zuerst auf den ⟦Hauptnenner⟧ erweitern. Genau wie bei Zahlen: 2/7 + 3/7 = 5/7.',
  'fehler': '2/x + 3/x ist nicht 5/(2x): Die ⟦Nenner werden nicht addiert⟧ – aus 2 Siebteln und 3 Siebteln werden 5 Siebtel, keine Vierzehntel. Prüfe mit x = 1: 2 + 3 = 5, aber 5/2 = 2,5. Richtig ist 5/x.'},
 'multiplizieren': {
  'einstieg': 'Die Hälfte von einem Drittel einer Pizza ist ein Sechstel: 1/2 · 1/3 = 1/6. Beim Malnehmen von Brüchen rechnet man oben mal oben und unten mal unten. Beim Teilen durch einen Bruch dreht man ihn um und nimmt mal. Der umgedrehte Bruch heißt ⟦Kehrbruch⟧.',
  'woerter': [['Kehrbruch', 'der umgedrehte Bruch: von 4/x² ist es x²/4'], [':', 'geteilt durch'], ['(4x/9) · (3/x²)', '„4x Neuntel mal 3 durch x²“']],
  'schritte': ['Aufgabe: (4x/9) · (3/x²).', 'Alles auf einen Bruchstrich schreiben, oben mal oben, unten mal unten: (4x · 3)/(9 · x²).',
               'Vor dem Ausrechnen kürzen: 3 und 9 durch 3 teilen ergibt 1 und 3; x und x² durch x teilen ergibt 1 und x.', 'Übrig bleibt ⟦4/(3x)⟧.'],
  'regel': 'So rechnest du: Beim Malnehmen ⟦Zähler mal Zähler, Nenner mal Nenner⟧, dann kürzen. Beim Teilen mit dem ⟦Kehrbruch⟧ des zweiten Bruchs malnehmen.'},
 'fehler_finden': {
  'einstieg': 'Ein Mitschüler behauptet: „(x + 4)/4 ist dasselbe wie x + 1.“ Klingt praktisch – aber stimmt es? Statt lange zu überlegen, setzt du eine Zahl ein und rechnest beide Seiten aus. Kommt bei einer einzigen Zahl etwas Verschiedenes heraus, hast du ein ⟦Gegenbeispiel⟧ gefunden.',
  'woerter': [['Umformung', 'einen Term anders schreiben, ohne seinen Wert zu ändern'], ['Gegenbeispiel', 'eine Zahl, bei der beide Seiten verschieden herauskommen'], ['≠', '„ist nicht gleich“']],
  'schritte': ['Behauptung: (x + 4)/4 = x + 1.', 'Setze eine Zahl ein, zum Beispiel x = 4. Links: (4 + 4)/4 = 8/4 = 2.', 'Rechts: 4 + 1 = 5. Es ist 2 ≠ 5.',
               'Die Umformung ist also ⟦falsch⟧. Richtig wäre (x + 4)/4 = x/4 + 1.'],
  'regel': 'So prüfst du eine ⟦Umformung⟧: eine Zahl aus D ⟦einsetzen⟧ und beide Seiten ausrechnen. Kommt etwas Verschiedenes heraus, ist die Umformung ⟦falsch⟧.'},
}

for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))
# ---- KLAR ENDE ----


def nenner_lin(a, b):
    """a·x + b als Text in Klammern, falls Summe."""
    t = lin(a, b)
    return f'({t})' if b != 0 else t


def mengentext(xs):
    xs = sorted(set(xs))
    return 'ℚ' if not xs else 'ℚ \\ {' + '; '.join(zt(x) for x in xs) + '}'


def g_definitionsmenge(R, st):
    if st == 1:
        a, b = R.randint(1, 9), R.randint(-9, 9)
        if b == 0: b = 4
        z = R.choice([str(a), f'({lin(1, R.randint(1, 5))})', f'({lin(2, -R.randint(1, 5))})'])
        T = f'{z}/{nenner_lin(1, -b)}'
        if R.random() < .5:
            return Z(f'Für welche Zahl ist der Term {T} nicht definiert?', b, f'{b}', f'Nenner {lin(1, -b)} = 0 für x = {zt(b)}.',
                     'Setze den Nenner gleich 0 und löse nach x.')
        return A(R, f'Gib die Definitionsmenge von {T} an.', mengentext([b]), [mengentext([-b]), mengentext([0]), 'ℚ'],
                 f'Nenner {lin(1, -b)} = 0 für x = {zt(b)}, also D = {mengentext([b])}.', 'Welche Zahl macht den Nenner 0?')
    if st == 2 and R.random() < .3:
        return def_schwer(R, R.random() * .4)
    if st == 2:
        while True:
            k, m = R.choice([2, 3, 4, 5, -2, -4]), R.randint(-12, 12)
            if m and ist_endlich(Fr(m, k)) and Fr(m, k).denominator != 1 or R.random() < .3 and m and m % k == 0: break
        x0 = Fr(m, k)
        T = f'{R.randint(1, 9)}/{nenner_lin(k, -m)}'
        if R.random() < .6:
            return Z(f'Für welche Zahl ist der Term {T} nicht definiert?', x0, f'{m} / ({k})',
                     f'{lin(k, -m)} = 0 → {lin(k, 0)} = {zt(m)} → x = {zt(x0)}.', 'Setze den Nenner gleich 0 und löse die Gleichung.')
        b = R.randint(1, 8) * R.choice([-1, 1])
        T = f'{R.randint(1, 9)}/(x({lin(1, -b)}))'
        return A(R, f'Gib die Definitionsmenge von {T} an.', mengentext([0, b]), [mengentext([b]), mengentext([0, -b]), mengentext([-b])],
                 f'Ein Produkt ist 0, wenn ein Faktor 0 ist: x = 0 oder {lin(1, -b)} = 0, also x = {zt(b)}. D = {mengentext([0, b])}.',
                 'Ein Produkt im Nenner ist 0, wenn einer der Faktoren 0 ist.')
    # Stufe 3: zwei Nenner / Zähler mit Nullstelle als Falle / Nenner nie 0 / Umkehraufgabe
    return def_schwer(R, R.random())


def def_schwer(R, art):
    if art < .2:
        k, z = R.choice([1, 4, 9, 2, 5]), R.randint(1, 9)
        return A(R, f'Gib die Definitionsmenge von {z}/(x² + {k}) an.', 'ℚ',
                 [mengentext([-k]), mengentext([k]), mengentext([-2, 2]) if k == 4 else mengentext([-k, k])],
                 f'x² ist nie negativ, also ist x² + {k} mindestens {k} und nie 0. Es fehlt keine Zahl: D = ℚ.',
                 'Kann x² + eine positive Zahl überhaupt 0 werden?')
    if art < .4:
        while True:
            b, c = R.sample([k for k in range(-7, 8)], 2)
            if b != -c: break
        z = R.randint(1, 9)
        def nf(v): return 'x' if v == 0 else f'({lin(1, -v)})'
        richtig = f'{z}/({nf(b)}{nf(c)})' if 0 in (b, c) else f'{z}/({nf(b)}{nf(c)})'
        falsch = [f'{z}/({nf(-b)}{nf(-c)})' if (b, c) != (0, 0) else '', f'{nf(b)}/{nf(c)}' if c else f'{nf(c)}/{nf(b)}',
                  f'{z}/{nf(b)} + {lin(1, -c)}']
        return A(R, f'Welcher Term hat die Definitionsmenge {mengentext([b, c])}?', richtig, [f for f in falsch if f],
                 f'Der Nenner {nf(b)}{nf(c)} wird genau für x = {zt(min(b, c))} und x = {zt(max(b, c))} null. Bei den anderen Termen fehlen andere oder weniger Zahlen.',
                 'Setze die ausgeschlossenen Zahlen ein: Welcher Nenner wird bei beiden 0?')
    if art < .7:
        b, c = R.sample([k for k in range(-8, 9) if k], 2)
        z = R.choice([k for k in range(-8, 9) if k not in (b, c, 0)])
        T = f'{nenner_lin(1, -z)}/(({lin(1, -b)})({lin(1, -c)}))'
        return A(R, f'Gib die Definitionsmenge von {T} an.', mengentext([b, c]), [mengentext([b, c, z]), mengentext([-b, -c]), mengentext([z])],
                 f'Nenner 0 für x = {zt(b)} oder x = {zt(c)}. Der Zähler darf 0 sein. D = {mengentext([b, c])}.',
                 'Nur der Nenner zählt. Jeder Faktor im Nenner liefert eine ausgeschlossene Zahl.')
    b = R.randint(1, 8) * R.choice([-1, 1]); k = R.choice([2, 4, 5]); m = R.choice([j for j in range(-9, 10) if j % k])
    T = f'{R.randint(1, 9)}/{nenner_lin(1, -b)} + {R.randint(1, 9)}/{nenner_lin(k, -m)}'
    return A(R, f'Gib die Definitionsmenge von {T} an.', mengentext([b, Fr(m, k)]), [mengentext([b]), mengentext([-b, Fr(-m, k)]), mengentext([b, m])],
             f'Erster Nenner 0 für x = {zt(b)}, zweiter für {lin(k, 0)} = {zt(m)}, also x = {zt(Fr(m, k))}. D = {mengentext([b, Fr(m, k)])}.',
             'Bestimme für jeden Nenner die Zahl, die ihn 0 macht.')


def g_termwert(R, st):
    while True:
        a, b = R.randint(-5, 6), R.randint(-9, 9)
        c, d = R.choice([1, 1, 2, -1, 3]), R.randint(-8, 8)
        x0 = R.randint(-6, 8)
        if a == 0 or d == 0: continue
        nen = c * x0 + d
        if nen == 0: continue
        w = Fr(a * x0 + b, nen)
        if not ist_endlich(w) or len(zt(w)) > 6: continue
        if st == 1 and (c != 1 or w.denominator != 1): continue
        if st == 2 and w.denominator == 1 and R.random() < .5: continue
        break
    zx = lin(a, b); nx = lin(c, d)
    T = f'({zx})/({nx})' if b else f'{zx}/({nx})'
    art = R.choice(['undef', 'umkehr', 'bruch', 'normal', 'normal']) if st >= 2 else 'normal'
    if art == 'undef' and c not in (1, -1): c = R.choice([1, -1]); nx = lin(c, d); T = f'({zx})/({nx})' if b else f'{zx}/({nx})'
    if art == 'undef':
        # Wert außerhalb von D
        xn = Fr(-d, c)
        zw = a * xn + b
        andere = [zt(zw) if zw else '1', '0' if zw else '−1', zt(zw + 1) if zw + 1 else '2']
        return A(R, f'Welchen Wert hat T(x) = {T} für x = {zt(xn)}?', 'Keinen: T ist dort nicht definiert.', andere,
                 f'Nenner: {einsetzen(nx, xn)} = 0. Durch 0 teilen geht nicht.', 'Rechne zuerst den Nenner aus.')
    if art == 'umkehr':
        # Umkehraufgabe: T(x) = k/(x + d) hat den Wert v
        v, x1 = R.choice([-4, -3, -2, 2, 3, 4, 5, 6]), R.randint(-6, 8)
        d2 = R.choice([k for k in range(-6, 7) if k and k != -x1])
        k = v * (x1 + d2)
        T2 = f'{zt(k)}/({lin(1, d2)})'
        return Z(f'Für welches x hat T(x) = {T2} den Wert {zt(v)}?', x1, f'{k} / ({v}) - ({d2})',
                 f'{T2} = {zt(v)} → {lin(1, d2)} = {zt(k)} : {kl(v)} = {zt(Fr(k, v))} → x = {zt(x1)}. Probe: {zt(k)} : {kl(x1 + d2)} = {zt(v)}.',
                 'Der Nenner muss so groß sein, dass Zähler : Nenner den Wert ergibt. Bestimme erst den Nenner.')
    if art == 'bruch':
        # Ergebnis als Bruch (nicht abbrechend) → Lücke □/□
        for _ in range(200):
            a, b, c, d = R.randint(-5, 6) or 1, R.randint(-9, 9), R.choice([1, 2, 3, -1]), R.randint(-8, 8) or 5
            zx = lin(a, b); nx = lin(c, d)
            T = f'({zx})/({nx})' if b else f'{zx}/({nx})'
            x2 = R.randint(-6, 8)
            nen2 = c * x2 + d
            if nen2 == 0: continue
            w2 = Fr(a * x2 + b, nen2)
            if not ist_endlich(w2) and w2 > 0 and w2.denominator <= 12: break
        else:
            return g_termwert(R, st)
        return L(f'Berechne T({zt(x2)}) für T(x) = {T}. Gib das Ergebnis als vollständig gekürzten Bruch an.', '□/□',
                 [w2.numerator, w2.denominator], [f'{w2.numerator}', f'{w2.denominator}'],
                 f'Zähler: {einsetzen(zx, x2)} = {zt(a * x2 + b)}, Nenner: {einsetzen(nx, x2)} = {zt(nen2)}. T({zt(x2)}) = {zt(a * x2 + b)}/{kl(nen2)}' + (f' = {bruch(w2)}.' if (a * x2 + b, nen2) != (w2.numerator, w2.denominator) else '.'),
                 'Setze in Zähler und Nenner getrennt ein. Kürze am Ende.', hinweis='Zähler oben, Nenner unten.')
    return Z(f'Berechne T({zt(x0)}) für T(x) = {T}.', w, f'(({a}) * ({x0}) + ({b})) / (({c}) * ({x0}) + ({d}))',
             f'Zähler: {einsetzen(zx, x0)} = {zt(a * x0 + b)}, Nenner: {einsetzen(nx, x0)} = {zt(nen)}. T({zt(x0)}) = {zt(a * x0 + b)}/{kl(nen) if nen < 0 else zt(nen)} = {zt(w)}.',
             'Setze die Zahl in Zähler und Nenner getrennt ein. Achte auf Klammern bei negativen Zahlen.')


def g_kuerzen(R, st):
    if st == 1:
        while True:
            t = R.randint(2, 6)
            p, q = R.randint(1, 6) * t, R.randint(1, 6) * t
            e1, e2 = R.randint(1, 4), R.randint(1, 4)
            if p != q and e1 != e2: break
        c = Fr(p, q); e = e1 - e2
        T = f'{p}{pot("x", e1)}/({q}{pot("x", e2)})'
        r = mono(c, e)
        return A(R, f'Kürze vollständig: {T}', r, [mono(c, e1 + e2) if e1 + e2 <= 6 else mono(c, e + 1), mono(Fr(p - t, q - t), e) if p - t > 0 and q - t > 0 and Fr(p - t, q - t) != c else mono(3 * c, e), mono(c, -e), mono(c * 2, e)],
                 f'Zahlen: {p}/{q} = {bruch(c)}. Potenzen: {pot("x", e1)}/{pot("x", e2)} = {mono(1, e)}. Ergebnis: {r}.',
                 'Kürze Zahlen und Potenzen von x getrennt. Gleiche Faktoren x fallen weg.')
    if st == 2:
        art = R.choice(['faktor', 'x_ausklammern'])
        if art == 'faktor':
            while True:
                k, m, b = R.randint(2, 9), R.randint(2, 9), R.randint(-7, 7)
                if k != m and b: break
            T = f'({lin(k, k * b)})/({lin(m, m * b)})'
            r = bruch(Fr(k, m))
            g = gcd(abs(k * b), abs(m * b))
            nur_zahlen = f'({lin(k, k * b // g)})/({lin(m, m * b // g)})' if g > 1 else f'{zt(k)}x/({zt(m)}x)'
            return A(R, f'Kürze vollständig: {T}', r, [nur_zahlen, f'({lin(k, b)})/({lin(m, b)})', f'{bruch(Fr(k * b, m * b) + 1)}'],
                     f'Ausklammern: {k}({lin(1, b)})/({m}({lin(1, b)})). ({lin(1, b)}) kürzen: {r}.', 'Klammere im Zähler und im Nenner die Zahl vor x aus.')
        b, c = R.randint(-8, 8) or 3, R.randint(2, 9)
        T = f'({lin(1, 0)}² {"+" if b > 0 else "−"} {abs(b) if abs(b) != 1 else ""}x)/({c}x)'
        r = f'({lin(1, b)})/{c}'
        return A(R, f'Kürze vollständig: {T}', r, [lin(1, b), f'(x² {"+" if b > 0 else "−"} {abs(b)})/{c}', f'({lin(1, b)})/({c}x)'],
                 f'Zähler: x({lin(1, b)}). Mit x kürzen: {r}.', 'Klammere im Zähler x aus.')
    art = R.choice(['vorzeichen', 'binom', 'binom'])
    if art == 'vorzeichen' and R.random() < .5:
        b = R.randint(1, 9); k = R.choice([1, 2, 3])
        Zae = f'{k * b} − {k}x' if k > 1 else f'{b} − x'
        return A(R, f'Kürze vollständig: ({Zae})/(x − {b})', zt(-k), [zt(k), '0', f'x − {b}'],
                 f'{Zae} = −{"" if k == 1 else k}(x − {b}). Also ' + (f'−(x − {b})/(x − {b}) = −1.' if k == 1 else f'−{k}(x − {b})/(x − {b}) = −{k}.'),
                 'Klammere im Zähler eine negative Zahl aus. Dann steht dort dieselbe Klammer wie im Nenner.')
    if art == 'vorzeichen':
        k, b = R.randint(2, 9), R.randint(1, 9)
        T = f'({lin(k, -k * b)})/({b} − x)'
        return A(R, f'Kürze vollständig: {T}', zt(-k), [zt(k), f'{k}x', lin(k, -b)],
                 f'{lin(k, -k * b)} = {k}(x − {b}) und {b} − x = −(x − {b}). Also {k}(x − {b})/(−(x − {b})) = {zt(-k)}.',
                 'Im Nenner steht fast dasselbe wie in der Klammer im Zähler – nur mit umgekehrtem Vorzeichen.')
    b = R.randint(1, 9); s = R.choice([1, -1])
    T = f'(x² − {b * b})/({lin(1, s * b)})'
    r = lin(1, -s * b)
    return A(R, f'Kürze vollständig: {T}', r, [lin(1, s * b), f'x − {b * b}' if s > 0 else f'x + {b * b}', f'x² − {b}'],
             f'3. binomische Formel: x² − {b * b} = (x + {b})(x − {b}). Mit ({lin(1, s * b)}) kürzen: {r}.',
             'Erkenne die 3. binomische Formel: a² − b² = (a + b)(a − b).')


def g_erweitern(R, st):
    h = 'Teile den neuen Nenner durch den alten. Mit diesem Term multiplizierst du auch den Zähler.'
    if st >= 2 and R.random() < .3:
        if R.random() < .5:
            a, b, f, e = R.randint(1, 9), R.randint(2, 5), R.randint(2, 5), R.randint(1, 2)
            neu = f'{b * f}{pot("x", 1 + e)}'
            return L(f'Mit welchem Term wurde {a}/({b}x) erweitert, wenn der neue Nenner {neu} ist?', f'□{pot("x", e)}', [f], [f'{b * f} // {b}'],
                     f'{neu} : ({b}x) = {f}{pot("x", e)}. Mit {f}{pot("x", e)} wurde erweitert.', 'Teile den neuen Nenner durch den alten.')
        a, b, f = R.randint(1, 9), R.randint(1, 9) * R.choice([-1, 1]), R.randint(2, 6)
        neu = f'{f}x² {"+" if b > 0 else "−"} {abs(f * b)}x'
        return L(f'Mit welchem Term wurde {a}/({lin(1, b)}) erweitert, wenn der neue Nenner {neu} ist?', '□x', [f], [f'{f}'],
                 f'{neu} = {f}x({lin(1, b)}). Mit {f}x wurde erweitert.', 'Klammere im neuen Nenner so viel wie möglich aus.')
    if st == 1:
        a, b = R.randint(1, 9), R.randint(2, 6)
        f = R.randint(2, 5)
        alt, neu = f'{a}/({b}x)', f'{b * f}x²'
        return L(f'Erweitere {alt} auf den Nenner {neu}. Gib den neuen Zähler ein.', '□x', [a * f], [f'{a}*{f}'],
                 f'{neu} : ({b}x) = {f}x. Zähler: {a} · {f}x = {a * f}x.', h)
    if st == 2:
        b = R.randint(1, 9) * R.choice([-1, 1]); d, f = R.randint(2, 5), R.randint(2, 4)
        alt = f'({lin(1, b)})/{d}'
        return L(f'Erweitere {alt} auf den Nenner {d * f}. Gib den neuen Zähler ein.', '□x + □', [f, f * b], [f'{f}', f'{f}*({b})'],
                 f'{d * f} : {d} = {f}. Zähler: {f} · ({lin(1, b)}) = {lin(f, f * b)}.', h)
    if R.random() < .5:
        a, b = R.randint(1, 9), R.randint(1, 9) * R.choice([-1, 1])
        alt, neu = f'{a}/({lin(1, b)})', f'x² {"+" if b > 0 else "−"} {abs(b) if abs(b) != 1 else ""}x'
        return L(f'Erweitere {alt} auf den Nenner {neu}. Gib den neuen Zähler ein.', '□x', [a], [f'{a}'],
                 f'{neu} = x({lin(1, b)}). Mit x erweitern: Zähler {lin(a, 0)}.', 'Klammere im neuen Nenner x aus.')
    while True:
        b, c, f = R.randint(1, 9) * R.choice([-1, 1]), R.randint(1, 9) * R.choice([-1, 1]), R.randint(2, 5)
        if b != c: break
    alt, neu = f'({lin(1, b)})/({lin(1, c)})', f'{lin(f, f * c)}'
    return L(f'Erweitere {alt} auf den Nenner {neu}. Gib den neuen Zähler ein.', '□x + □', [f, f * b], [f'{f}', f'{f}*({b})'],
             f'{neu} = {f}({lin(1, c)}). Mit {f} erweitern: {f} · ({lin(1, b)}) = {lin(f, f * b)}.', 'Klammere im neuen Nenner eine Zahl aus.')


def g_addieren(R, st):
    if st == 1:
        a, b, c = R.randint(1, 9), R.randint(1, 9), R.randint(-6, 6)
        op = R.choice(['+', '−'])
        n = lin(1, c)
        r_z = a + b if op == '+' else a - b
        N = f'({n})' if c else 'x'
        return A(R, f'Fasse zusammen: {a}/{N} {op} {b}/{N}', f'{zt(r_z)}/{N}' if r_z else '0',
                 [f'{zt(r_z)}/(2{N})' if c else f'{zt(r_z)}/(2x)', f'{zt(r_z)}/{N}²' if c else f'{zt(r_z)}/x²', f'{zt(a + b if op == "−" else a - b)}/{N}'],
                 f'Gleicher Nenner: Zähler {a} {op} {b} = {zt(r_z)}, Nenner bleibt: {zt(r_z)}/{N}.', 'Gleicher Nenner: nur die Zähler verrechnen.')
    if st == 2:
        a, b, k = R.randint(1, 9), R.randint(1, 9), R.randint(2, 6)
        op = R.choice(['+', '−'])
        if R.random() < .5:
            z = k * a + b if op == '+' else k * a - b
            r = mono(Fr(z, k), -1) if z else '0'
            return A(R, f'Fasse zusammen: {a}/x {op} {b}/({k}x)', r, [f'{zt(a + b if op == "+" else a - b)}/({k + 1}x)', mono(Fr(a + b if op == '+' else a - b, k), -1), f'{zt(z)}/({k}x²)'],
                     f'Hauptnenner {k}x: {a}/x = {k * a}/({k}x). {k * a} {op} {b} = {zt(z)}. Ergebnis {zt(z)}/({k}x)' + (f' = {r}' if r != f'{zt(z)}/({k}x)' else '') + '.',
                     'Erweitere den ersten Bruch auf den Hauptnenner.')
        r = f'({lin(a, -b if op == "−" else b)})/x²'
        return A(R, f'Fasse zusammen: {a}/x {op} {b}/x²', r, [f'{zt(a - b if op == "−" else a + b)}/x²', f'{zt(a - b if op == "−" else a + b)}/x³', f'({lin(a, -b if op == "−" else b)})/x³'],
                 f'Hauptnenner x²: {a}/x = {lin(a, 0)}/x². Ergebnis: {r}.', 'Der Hauptnenner ist x². Erweitere den ersten Bruch mit x.')
    if R.random() < .45:
        while True:
            p1, q1, p2, q2 = R.randint(2, 7), R.randint(-9, 9), R.randint(1, 5), R.randint(-9, 9)
            if q1 and q2 and p1 != p2 and q1 != q2 and q1 + q2 != q1 - q2: break
        Nn = R.choice(['x', f'({lin(1, R.randint(1, 6))})'])
        r = f'({lin(p1 - p2, q1 - q2)})/{Nn}'
        return A(R, f'Fasse zusammen: ({lin(p1, q1)})/{Nn} − ({lin(p2, q2)})/{Nn}', r,
                 [f'({lin(p1 - p2, q1 + q2)})/{Nn}', f'({lin(p1 + p2, q1 - q2)})/{Nn}', f'({lin(p1 - p2, q1 - q2)})/(2{Nn})' if Nn == 'x' else f'({lin(p1 - p2, q1 - q2)})/(2{Nn})'],
                 f'Gleicher Nenner. Das Minus gilt für den ganzen zweiten Zähler: {lin(p1, q1)} − ({lin(p2, q2)}) = {lin(p1, q1)} − {lin(p2, -q2)} = {lin(p1 - p2, q1 - q2)}. Ergebnis: {r}.',
                 'Setze den zweiten Zähler in Klammern. Das Minus ändert jedes Vorzeichen darin.')
    a, b, c = R.randint(1, 6), R.randint(1, 6), R.randint(1, 8) * R.choice([-1, 1])
    r = f'({lin(a + b, a * c)})/(x({lin(1, c)}))'
    return A(R, f'Fasse zusammen: {a}/x + {b}/({lin(1, c)})', r,
             [f'{a + b}/(x + {lin(1, c)})', f'{a + b}/(x({lin(1, c)}))', f'({lin(a + b, c)})/(x({lin(1, c)}))'],
             f'Hauptnenner x({lin(1, c)}). Zähler: {a}({lin(1, c)}) + {lin(b, 0)} = {lin(a + b, a * c)}. Ergebnis: {r}.',
             'Der Hauptnenner ist das Produkt der beiden Nenner.')


def teile(c, e):
    """Bruch c·x^e als (Zählerzahl, x-Exponent oben, Nennerzahl, x-Exponent unten)."""
    c = Fr(c)
    return c.numerator, max(e, 0), c.denominator, max(-e, 0)


def roh(p, ez, q, en):
    """Ungekürzter Bruch, z. B. 28x/(40x²)."""
    zae = (str(p) if p != 1 or ez == 0 else '') + (pot('x', ez) if ez else '')
    nen = (str(q) if q != 1 or en == 0 else '') + (pot('x', en) if en else '')
    if nen == '1': return zae
    return f'{zae}/({nen})' if (en and q != 1) else f'{zae}/{nen}'


def faktor(p, e):
    return (str(p) if p != 1 or e == 0 else '') + (pot('x', e) if e else '')


def mal_weg(c1, e1, c2, e2):
    p1, z1, q1, n1 = teile(c1, e1)
    p2, z2, q2, n2 = teile(c2, e2)
    P, EZ, Q, EN = p1 * p2, z1 + z2, q1 * q2, n1 + n2
    k = min(EZ, EN)
    g = gcd(P, Q)
    kt = (str(g) if g != 1 or not k else '') + (pot('x', k) if k else '')
    erg = mono(Fr(P, Q), EZ - EN)
    zw = (f'Zähler: {faktor(p1, z1)} · {faktor(p2, z2)} = {faktor(P, EZ)}. Nenner: {faktor(q1, n1)} · {faktor(q2, n2)} = {faktor(Q, EN)}. ')
    if g == 1 and not k: return zw + f'Nichts zu kürzen: {erg}.', erg
    return zw + f'{roh(P, EZ, Q, EN)} mit {kt} kürzen: {erg}.', erg


def L_mono(c, e):
    """Lücke für ein Monom-Ergebnis c·x^e (c > 0)."""
    c = Fr(c)
    p, q = c.numerator, c.denominator
    if e > 0 and q == 1: return f'□{pot("x", e)}', [p]
    if e > 0: return f'□{pot("x", e)}/□', [p, q]
    if e < 0: return f'□/(□{pot("x", -e)})', [p, q]
    return '□/□', [p, q]


def g_multiplizieren(R, st):
    def zufall():
        while True:
            p, q, e = R.randint(1, 9), R.randint(2, 9), R.randint(-3, 3)
            if gcd(p, q) == 1 and e != 0: return Fr(p, q), e
    if st in (1, 2):
        (c1, e1), (c2, e2) = zufall(), zufall()
        if e1 * e2 > 0: e2 = -e2
        div = st == 2 and R.random() < .7
        if div:
            c, e = c1 / c2, e1 - e2
            op = ':'
            weg, erg = mal_weg(c1, e1, 1 / c2, -e2)
            weg = f'Mit dem Kehrbruch von {mono(c2, e2)} multiplizieren: {mono(c1, e1)} · {mono(1 / c2, -e2)}. ' + weg
            falsch = [mono(c1 * c2, e1 + e2), mono(c2 / c1, e2 - e1), mono(c1 / c2, e1 + e2)]
        else:
            c, e = c1 * c2, e1 + e2
            op = '·'
            weg, erg = mal_weg(c1, e1, c2, e2)
            falsch = [mono(c1 * c2, e1 - e2), mono(c1 / c2, e), mono(c1 * c2 * 2, e), mono(c1 + c2, e)]
        if e > 6 or e < -6 or c.denominator == 1 and e == 0: return g_multiplizieren(R, st)
        r = mono(c, e)
        assert r == erg
        h = 'Erst multiplizieren (bei „:“ mit dem Kehrbruch), dann Zahlen und x getrennt kürzen.'
        if R.random() < .4 and c.numerator != 1:
            sch, werte = L_mono(c, e)
            return L(f'Berechne und kürze vollständig: ({mono(c1, e1)}) {op} ({mono(c2, e2)})', sch, werte, [str(v) for v in werte], weg, h,
                     hinweis='Trage die gekürzten Zahlen in die Felder ein.')
        return A(R, f'Berechne und kürze: ({mono(c1, e1)}) {op} ({mono(c2, e2)})', r, falsch, weg, h)
    if R.random() < .5:
        # Stufe 3: erst faktorisieren, dann kürzen
        if R.random() < .5:
            k, b = R.randint(2, 6), R.randint(1, 8) * R.choice([-1, 1])
            r = f'{k}x'
            return A(R, f'Berechne und kürze: ({lin(k, k * b)})/x · x²/({lin(1, b)})', r, [f'{k}x²', f'{k}/x', f'({lin(k, k * b)})x'],
                     f'{lin(k, k * b)} = {k}({lin(1, b)}). Zähler: {k}({lin(1, b)}) · x², Nenner: x({lin(1, b)}). Mit x({lin(1, b)}) kürzen: {r}.',
                     'Klammere im ersten Zähler aus. Dann kürzt sich eine Klammer weg.')
        b, m, f = R.randint(1, 9), R.randint(2, 5), R.randint(2, 3)
        n = m * f
        r = f'{f}({lin(1, b)})'
        return A(R, f'Berechne und kürze: (x² − {b * b})/{m} : (x − {b})/{n}', r, [f'({lin(1, b)})/{f}', f'{f}({lin(1, -b)})', f'(x² − {b * b})/{f}'],
                 f'Mit dem Kehrbruch multiplizieren: (x² − {b * b})/{m} · {n}/(x − {b}). x² − {b * b} = (x + {b})(x − {b}). Mit (x − {b}) und {m} kürzen: {r}.',
                 'Erkenne die 3. binomische Formel im ersten Zähler.')
    b = R.randint(1, 9) * R.choice([-1, 1]); p, q = R.randint(2, 9), R.randint(2, 9)
    if p == q: q += 1
    g = gcd(p, q)
    K = f'({lin(1, b)})'
    r = f'{p // g}/({q // g}{K})' if q // g != 1 else f'{p // g}/{K}'
    return A(R, f'Berechne und kürze: ({lin(1, b)})/{q} · {p}/{K}²', r, [f'{p // g}{K}/{q // g}', f'{p}/({q}{K}²)', f'{p // g}/{q // g}'],
             f'Zähler: {p}{K}, Nenner: {q}{K}². Mit {"" if g == 1 else g}{K} kürzen: {r}.', f'{K}² = {K} · {K}. Ein Faktor {K} kürzt sich.')


def aussagen(R):
    """(Aussage, wahr?, Begründung) – Wahrheitswerte zusätzlich per Einsetzen geprüft."""
    a, b = R.sample(range(2, 10), 2)
    c = R.randint(2, 9)
    al = [
        (f'(x + {a})/{a} = x + 1', False, f'Aus der Summe x + {a} darf man nicht kürzen. Richtig: x/{a} + 1.', lambda x: ((x + a) / a, x + 1)),
        (f'({a}x)/{a} = x', True, f'{a} ist ein Faktor und darf gekürzt werden.', lambda x: (a * x / a, x)),
        (f'{a}/x + {b}/x = {a + b}/(2x)', False, f'Die Nenner werden nicht addiert. Richtig: {a + b}/x.', lambda x: (Fr(a) / x + Fr(b) / x, Fr(a + b) / (2 * x))),
        (f'{a}/x · {b}/x = {a * b}/x²', True, 'Zähler mal Zähler, Nenner mal Nenner.', lambda x: (Fr(a) / x * Fr(b) / x, Fr(a * b) / x ** 2)),
        (f'(x + {a})/(x + {b}) = {a}/{b}', False, 'x ist ein Summand und darf nicht gekürzt werden.', lambda x: ((x + a) / (x + b), Fr(a, b))),
        (f'({a}x + {a * b})/{a} = x + {b}', True, f'Zähler = {a}(x + {b}), dann {a} kürzen.', lambda x: ((a * x + a * b) / a, x + b)),
        (f'(x/{a}) : {b} = x/{a * b}', True, f'Durch {b} teilen heißt mit 1/{b} multiplizieren.', lambda x: (x / a / b, x / (a * b))),
        (f'(x/{a}) : {b} = {b}x/{a}', False, f'Durch {b} teilen ist nicht mal {b}. Richtig: x/{a * b}.', lambda x: (x / a / b, b * x / a)),
        (f'1/x + 1/{a} = 2/(x + {a})', False, f'Hauptnenner {a}x: richtig ist (x + {a})/({a}x).', lambda x: (1 / x + Fr(1, a), 2 / (x + a))),
        (f'x²/(x + {a}) = x − {a}', False, 'Im Zähler steht keine binomische Formel, nichts lässt sich kürzen.', lambda x: (x ** 2 / (x + a), x - a)),
        (f'(x² − {a * a})/(x − {a}) = x + {a}', True, f'3. binomische Formel: x² − {a * a} = (x + {a})(x − {a}).', lambda x: ((x ** 2 - a * a) / (x - a), x + a)),
        (f'{c}/({c}x) = 1/x', True, f'{c} ist Faktor in Zähler und Nenner.', lambda x: (Fr(c) / (c * x), 1 / x)),
        (f'{c}/({c} + x) = 1/x', False, f'Im Nenner ist {c} ein Summand, man darf nicht kürzen.', lambda x: (Fr(c) / (c + x), 1 / x)),
        (f'(−x − {a})/(x + {a}) = −1', True, f'Zähler = −(x + {a}).', lambda x: ((-x - a) / (x + a), Fr(-1))),
    ]
    for t, w, _, f in al:     # Kontrolle: wahr ⇔ für mehrere Testzahlen gleich
        gleich = all(f(Fr(x))[0] == f(Fr(x))[1] for x in (Fr(1, 3), Fr(17, 7), Fr(-23, 11), Fr(101, 13)))
        assert gleich == w, t
    return [(t, w, g) for t, w, g, _ in al]


BEGRUENDUNG = [
    (lambda a, b: f'Warum darf man in (x + {a})/(x + {b}) die x nicht kürzen?', 'Kürzen geht nur mit Faktoren, x ist hier ein Summand.',
     [lambda a, b: f'Weil {a} und {b} verschieden sind.', lambda a, b: 'Man darf es doch kürzen.', lambda a, b: 'Weil x auch 0 sein kann.'],
     lambda a, b: f'Teste x = 1: (1 + {a})/(1 + {b}) = {bruch(Fr(1 + a, 1 + b))}, aber {a}/{b} = {bruch(Fr(a, b))}. Kürzen darf man nur gemeinsame Faktoren.'),
    (lambda a, b: f'Warum ist x²/x = x nur für x ≠ 0 richtig?', 'Für x = 0 ist der linke Term nicht definiert.',
     [lambda a, b: 'Weil 0² = 0 ist.', lambda a, b: 'Für x = 0 ist der rechte Term nicht definiert.', lambda a, b: 'Es ist für alle x richtig.'],
     lambda a, b: 'Links steht x im Nenner. Für x = 0 hieße das 0/0 – durch 0 teilen geht nicht. Rechts wäre 0 erlaubt.'),
    (lambda a, b: f'Warum ist {a}/x + {b}/x nicht {a + b}/(2x)?', 'Beim Addieren bleibt der gemeinsame Nenner; nur die Zähler werden addiert.',
     [lambda a, b: 'Weil man die Zähler multiplizieren muss.', lambda a, b: f'Es stimmt doch: {a + b}/(2x) ist richtig.', lambda a, b: 'Weil x nicht 0 sein darf.'],
     lambda a, b: f'Teste x = 1: {a} + {b} = {a + b}, aber {a + b}/2 = {zt(Fr(a + b, 2))}. Richtig ist {a + b}/x.'),
    (lambda a, b: f'Warum ist ({a}x + {b})/{a} nicht x + {b}?', 'Die Zahl im Nenner teilt den ganzen Zähler, also auch den zweiten Summanden.',
     [lambda a, b: 'Es stimmt, man kürzt die gleichen Zahlen.', lambda a, b: f'Weil x durch {a} geteilt werden muss, nicht {a}x.', lambda a, b: 'Weil man aus Brüchen nie kürzen darf.'],
     lambda a, b: f'({a}x + {b})/{a} = x + {bruch(Fr(b, a))}. Teste x = 0: {bruch(Fr(b, a))} ≠ {b}.'),
]


def g_fehler_finden(R, st):
    if st >= 2 and R.random() < .3:
        frage, richtig, falsch, weg = R.choice(BEGRUENDUNG)
        while True:
            a, b = R.sample(range(2, 10), 2)
            if b % a: break
        return A(R, frage(a, b), richtig, [f(a, b) for f in falsch], weg(a, b), 'Teste mit einer einfachen Zahl, z. B. x = 1.')
    al = aussagen(R)
    wahr = [(t, g) for t, w, g in al if w]; falsch = [(t, g) for t, w, g in al if not w]
    if st == 1 or (st == 2 and R.random() < .5):
        t, g = R.choice(wahr)
        return A(R, 'Welche Umformung ist richtig (für alle x aus D)?', t, [x for x, _ in R.sample(falsch, 3)],
                 f'Richtig: {t}. {g} Bei den anderen findest du durch Einsetzen ein Gegenbeispiel.',
                 'Setze eine einfache Zahl ein, z. B. x = 1, und vergleiche beide Seiten.')
    t, g = R.choice(falsch)
    return A(R, 'Welche Umformung ist FALSCH?', t, [x for x, _ in R.sample(wahr, 3)],
             f'Falsch: {t}. {g}', 'Suche ein Gegenbeispiel durch Einsetzen.')


GEN = {'definitionsmenge': g_definitionsmenge, 'termwert': g_termwert, 'kuerzen': g_kuerzen, 'erweitern': g_erweitern,
       'addieren': g_addieren, 'multiplizieren': g_multiplizieren, 'fehler_finden': g_fehler_finden}


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl8.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl8 import mit_umbau  # noqa: E402

UMBAU = {
 'definitionsmenge': {
  'einstieg': 'Ein Bus kostet 600 €, die 2 Lehrkräfte zahlen nichts. Bei x Mitfahrenden zahlt jedes Kind 600/(x − 2) Euro. So ein Term mit x im Nenner heißt ⟦Bruchterm⟧.',
  'woerter': [['Bruchterm', 'ein Bruch mit x im Nenner'], ['Definitionsmenge D', 'alle Zahlen, die man für x einsetzen darf'], ['ℚ \\ {2}', 'alle Bruchzahlen außer der 2']],
  'bild': {'typ': 'koordinaten', 'x': [0, 12], 'y': [0, 700], 'graphen': [{'art': 'hyperbel', 'a': 600, 'b': -2, 'c': 0, 'name': 'Preis', 'bereich': [2.9, 12]}], 'schritt_y': 100, 'name_x': 'Personen', 'name_y': '€'},
  'schritte': [{'text': 'Der Nenner ist x − 2. Durch 0 kann man nicht teilen.'},
               {'text': 'x − 2 wird 0, wenn x = 2 ist.', 'bild': {'senkrecht': [2]}},
               {'text': 'Bei 2 Mitfahrenden zahlt kein Kind. ⟦x = 2 ist verboten.⟧'},
               {'text': 'Die Definitionsmenge D ist ⟦D = ℚ \\ {2}⟧: alle Zahlen außer 2.'}],
  'fehler': 'Bei (x − 2)/(x + 4) darf die 2 eingesetzt werden: Oben eine 0 ist kein Problem. Nur x = −4 macht den ⟦Nenner⟧ 0.',
  'regel': 'Setze ⟦jeden Nenner gleich 0⟧ und streiche diese Zahlen. Der Rest bildet die Definitionsmenge D.'},
 'termwert': {
  'einstieg': 'Fahren 26 Personen mit, zahlen 24 Kinder: 600 : 24 = 25 € pro Kind. So rechnest du für jede Anzahl einen Betrag aus, den ⟦Termwert⟧.',
  'woerter': [['Termwert', 'was herauskommt, wenn man für x eine Zahl einsetzt'], ['T(26)', 'der Termwert für x = 26'], ['nicht definiert', 'es gibt keinen Wert, weil man durch 0 teilen müsste']],
  'bild': {'typ': 'tabelle', 'kopf': ['x (Personen)', '10', '26', '2'], 'zeilen': [['600/(x − 2)', '?', '?', '?']]},
  'schritte': [{'text': 'Gesucht ist T(26). Erst den Nenner ausrechnen: 26 − 2 = 24.'},
               {'text': 'Dann teilen: T(26) = 600 : 24 = ⟦25⟧ Euro pro Kind.', 'bild': {'zeilen': [['600/(x − 2)', '?', '25', '?']]}},
               {'text': 'Genauso bei 10 Personen: 600 : 8 = 75 €.', 'bild': {'zeilen': [['600/(x − 2)', '75', '25', '?']]}},
               {'text': 'Bei x = 2 wäre der Nenner 0: T(2) ist ⟦nicht definiert⟧.', 'bild': {'zeilen': [['600/(x − 2)', '75', '25', '–']]}}],
  'fehler': 'T(2) ist nicht 0. 600 € auf 0 zahlende Kinder verteilt ergibt keinen Preis. Der Wert ist ⟦nicht definiert⟧.',
  'regel': 'Zahl einsetzen, ⟦Zähler und Nenner getrennt⟧ ausrechnen, dann teilen. Ist der Nenner 0, ist der Term dort nicht definiert.'},
 'kuerzen': {
  'einstieg': 'Bei 6/10 teilst du oben und unten durch 2 und erhältst 3/5 – derselbe Anteil. Das geht auch mit Termen, aber nur mit Faktoren. Dieses Vereinfachen heißt ⟦Kürzen⟧.',
  'woerter': [['Faktor', 'etwas, das malgenommen wird, z. B. die 3 in 3(x + 2)'], ['ausklammern', 'eine gemeinsame Zahl vor die Klammer ziehen: 3x + 6 = 3(x + 2)'], ['Kürzen', 'oben und unten durch denselben Faktor teilen']],
  'bild': {'typ': 'bruchstreifen', 'teile': 10, 'gefaerbt': 6, 'teil_text': '6/10', 'zeilen': [{'teile': 5, 'gefaerbt': 3}]},
  'schritte': [{'text': 'Kürze (3x + 6)/(5x + 10). Oben ausklammern: 3x + 6 = 3(x + 2).'},
               {'text': 'Unten ausklammern: 5x + 10 = 5(x + 2).'},
               {'text': 'Der Faktor (x + 2) steht oben und unten. Er fällt weg.'},
               {'text': 'Übrig bleibt ⟦3/5⟧ – für alle x außer −2.'}],
  'fehler': '(x + 6)/3 ist nicht x + 2. Die 6 ist nur dazugezählt, kein Faktor. Erst (3x + 6)/3 ergibt ⟦x + 2⟧.',
  'regel': 'Kürzen darfst du nur ⟦gleiche Faktoren⟧, nie Teile einer Summe. Darum zuerst ausklammern.'},
 'erweitern': {
  'einstieg': 'Schneidest du eine halbe Pizza in kleinere Stücke, hast du statt 1/2 nun 4/8. Oben und unten wurde mit 4 malgenommen, der Anteil blieb gleich. Das heißt ⟦Erweitern⟧.',
  'woerter': [['Erweitern', 'Zähler und Nenner mit derselben Zahl oder demselben Term malnehmen']],
  'bild': {'typ': 'bruchstreifen', 'teile': 2, 'gefaerbt': 1, 'teil_text': '1/2', 'zeilen': [{'teile': 8, 'gefaerbt': 4}]},
  'schritte': [{'text': '3/(2x) soll den Nenner 8x² bekommen.'},
               {'text': '8x² : (2x) = 4x. Mit 4x musst du erweitern.'},
               {'text': 'Auch den Zähler mal 4x: 3 · 4x = 12x.'},
               {'text': 'Ergebnis: ⟦12x/(8x²)⟧ – der Wert ist gleich geblieben.'}],
  'fehler': 'Nur den Nenner ändern ist falsch: 3/(8x²) ist viel weniger. Das wären kleinere Pizzastücke, aber trotzdem nur ⟦3 davon⟧.',
  'fehler_bild': {'zeilen': [{'teile': 8, 'gefaerbt': 1}]},
  'regel': 'Erweitern heißt: ⟦Zähler und Nenner mit demselben Term⟧ malnehmen. Den Term findest du mit neuer Nenner : alter Nenner.'},
 'addieren': {
  'einstieg': '2/7 Kuchen plus 3/7 Kuchen sind 5/7 Kuchen – gleich große Stücke zählst du zusammen. Sind die Stücke verschieden, schneidest du erst gleich große. Der gemeinsame Nenner heißt ⟦Hauptnenner⟧.',
  'woerter': [['Hauptnenner', 'ein gemeinsamer Nenner für alle Brüche']],
  'bild': {'typ': 'bruchstreifen', 'teile': 7, 'gefaerbt': 5, 'teil_text': '2/7 + 3/7'},
  'schritte': [{'text': 'Aufgabe 2/x + 3/(4x). Der Hauptnenner ist 4x.'},
               {'text': 'Den ersten Bruch mit 4 erweitern: 2/x = 8/(4x).'},
               {'text': 'Jetzt die Zähler addieren, der Nenner bleibt: ⟦11/(4x)⟧.'}],
  'fehler': '2/x + 3/x ist nicht 5/(2x). Aus 2 Siebteln und 3 Siebteln werden 5 Siebtel, keine Vierzehntel. Die Nenner ⟦nicht addieren⟧.',
  'fehler_bild': {'zeilen': [{'teile': 14, 'gefaerbt': 5}]},
  'regel': 'Bei gleichen Nennern nur die ⟦Zähler addieren⟧. Sonst zuerst auf den Hauptnenner erweitern.'},
 'multiplizieren': {
  'einstieg': 'Die Hälfte von einem Drittel Pizza ist ein Sechstel: 1/2 · 1/3 = 1/6. Beim Teilen nimmst du mit dem umgedrehten Bruch mal, dem ⟦Kehrbruch⟧.',
  'woerter': [['Kehrbruch', 'der umgedrehte Bruch: aus 3/x² wird x²/3']],
  'bild': {'typ': 'bruchstreifen', 'teile': 3, 'gefaerbt': 1, 'teil_text': '1/3', 'zeilen': [{'teile': 6, 'gefaerbt': 1}]},
  'schritte': [{'text': 'Aufgabe (4x/9) · (3/x²). Oben mal oben, unten mal unten: 12x/(9x²).'},
               {'text': 'Kürzen: 12 und 9 durch 3, x und x² durch x.'},
               {'text': 'Übrig bleibt ⟦4/(3x)⟧.'},
               {'text': 'Beim Teilen durch 3/x² nimmst du stattdessen mit x²/3 mal.'}],
  'fehler': 'Bei (2/x) : (4/x²) wird der ⟦zweite⟧ Bruch umgedreht, nicht der erste: (2/x) · (x²/4) = x/2.',
  'regel': 'Malnehmen: ⟦Zähler mal Zähler, Nenner mal Nenner⟧. Teilen: mit dem Kehrbruch des zweiten Bruchs malnehmen.'},
 'fehler_finden': {
  'einstieg': 'Ein Mitschüler behauptet, zwei Terme seien gleich. Ob es stimmt, prüfst du mit einer eingesetzten Zahl. Kommt Verschiedenes heraus, hast du ein ⟦Gegenbeispiel⟧.',
  'woerter': [['Gegenbeispiel', 'eine Zahl, bei der die Behauptung nicht stimmt'], ['≠', '„ist nicht gleich“']],
  'bild': {'typ': 'tabelle', 'kopf': ['x', '(x + 4)/4', 'x + 1'], 'zeilen': [['4', '?', '?']]},
  'schritte': [{'text': 'Behauptung: (x + 4)/4 = x + 1. Setze x = 4 ein.'},
               {'text': 'Links: (4 + 4)/4 = 8/4 = 2. Rechts: 4 + 1 = 5.', 'bild': {'zeilen': [['4', '2', '5']]}},
               {'text': '2 ≠ 5. Das ist ein Gegenbeispiel, die Umformung ist ⟦falsch⟧.'}],
  'fehler': 'Mit x = 0 kommt zufällig beide Male 1 heraus. Ein passendes Beispiel beweist nichts – ein ⟦Gegenbeispiel⟧ widerlegt.',
  'fehler_bild': {'zeilen': [['4', '2', '5'], ['0', '1', '1']]},
  'regel': 'Eine Umformung prüfst du durch ⟦Einsetzen⟧. Ein einziges Gegenbeispiel zeigt, dass sie falsch ist.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---- SCHWER (Zehnte Runde: schwerere Aufgaben nach Prüfungsvorbild, siehe _schwer_kl8.py) ----
# Vorbilder (Typ und Niveau, nicht Wortlaut/Zahlen): BMT10 2024 (Potenzbruch vereinfachen), Grundwissen 8 verschiedener Gymnasien
# (Bruchterme kürzen nach Ausklammern, „zu einem Bruch zusammenfassen“ mit Summanden ohne Nenner, Hauptnenner), Stegreifaufgaben-Typ
# „maximale Definitionsmenge“, BMT8 2022/2025 (Tabellenkalkulation, Punkt vor Strich), RS-Jahrgangsstufentest 8 2023 (Fehler in einer Rechnung finden).
from _schwer_kl8 import Neu, mit_schwer  # noqa: E402

N = Neu(10_8_4)

# definitionsmenge
N.z('definitionsmenge', 2, 'Für welche Zahl ist der Term 6/(9 − 3x) nicht definiert?', 3, '9 / 3', '9 − 3x = 0 ⇔ 3x = 9 ⇔ x = 3.', 'Setze den Nenner gleich 0.')
N.a('definitionsmenge', 2, 'Gib die Definitionsmenge von 1/x + 1/(x + 1) an.', 'ℚ \\ {−1; 0}', ['ℚ \\ {0}', 'ℚ \\ {1}', 'ℚ \\ {0; 1}'],
    'Beide Nenner dürfen nicht 0 werden: x ≠ 0 und x + 1 ≠ 0, also x ≠ −1.', 'Prüfe jeden Nenner einzeln.')
N.a('definitionsmenge', 3, 'Gib die Definitionsmenge von (x + 2)/(x² − 4x) an.', 'ℚ \\ {0; 4}', ['ℚ \\ {4}', 'ℚ \\ {−2; 0; 4}', 'ℚ \\ {−4; 0}'],
    'Nenner ausklammern: x² − 4x = x(x − 4). Ein Produkt ist 0, wenn ein Faktor 0 ist: x = 0 oder x = 4. Der Zähler spielt keine Rolle.',
    'Klammere im Nenner x aus. Wann wird das Produkt 0?', art='P')
N.a('definitionsmenge', 3, 'Ein Term hat die Definitionsmenge ℚ \\ {−2; 0}. Welcher kann es sein?', '3/(x² + 2x)', ['3/(x² − 2x)', '(x + 2)/x', '3/(x + 2) + x'],
    'x² + 2x = x(x + 2) ist 0 für x = 0 und x = −2. Bei x² − 2x wären es 0 und 2. (x + 2)/x schließt nur 0 aus, 3/(x + 2) + x nur −2.',
    'Klammere in jedem Nenner aus und bestimme die verbotenen Zahlen.', art='P')
N.a('definitionsmenge', 3, 'Gib die Definitionsmenge von x/(2x + 1) : (x − 3)/x an.', 'ℚ \\ {−0,5; 0; 3}', ['ℚ \\ {−0,5; 0}', 'ℚ \\ {−0,5; 3}', 'ℚ \\ {0; 0,5; 3}'],
    'Nenner 2x + 1 ≠ 0 (x ≠ −0,5) und x ≠ 0. Außerdem teilt man durch (x − 3)/x – dieser Bruch darf nicht 0 sein: x ≠ 3.',
    'Beim Teilen darf auch der ganze zweite Bruch nicht 0 sein.', art='K')
N.z('definitionsmenge', 3, 'Für welchen Wert von a hat der Term 5/(x² + a) die Definitionsmenge ℚ \\ {−3; 3}?', -9, '-(3**2)',
    'Ausgeschlossen sind 3 und −3: Dort muss x² + a = 0 sein. 9 + a = 0 ⇔ a = −9. Probe: x² − 9 = 0 für x = ±3.', 'Setze x = 3 in den Nenner ein. Er muss 0 werden.', art='K')

# termwert
N.z('termwert', 2, 'Berechne T(−3) für T(x) = (x² − 1)/(x + 2).', -8, '((-3)**2 - 1) / (-3 + 2)', 'Zähler: 9 − 1 = 8. Nenner: −3 + 2 = −1. T(−3) = 8 : (−1) = −8.',
    'Rechne Zähler und Nenner getrennt. (−3)² ist positiv.')
N.z('termwert', 2, 'Berechne T(0,5) für T(x) = (2x + 3)/(4x).', 2, '(2 * 0.5 + 3) / (4 * 0.5)', 'Zähler: 1 + 3 = 4. Nenner: 2. T(0,5) = 4 : 2 = 2.', 'Zähler und Nenner getrennt.')
N.z('termwert', 3, 'Der Term T(x) = (a · x + 4)/(x − 2) hat an der Stelle x = 3 den Wert 10. Bestimme a.', 2, '(10 * (3 - 2) - 4) / 3',
    'T(3) = (3a + 4)/(3 − 2) = 3a + 4. Aus 3a + 4 = 10 folgt a = 2.', 'Setze x = 3 ein. Dann bleibt eine Gleichung für a.', art='P')
N.z('termwert', 3, 'In Zelle A1 steht 4. In B1 steht =(A1+2)/(A1-1)/2. Welchen Wert zeigt B1? (Der Computer rechnet gleichrangige Rechenarten von links nach rechts.)', 1,
    '((4 + 2) / (4 - 1)) / 2', 'Klammern zuerst: 6 und 3. Dann von links: 6 / 3 = 2, danach 2 / 2 = 1. Nicht 6 : (3 : 2) = 4.',
    'Rechne die beiden Klammern aus. Dann teile von links nach rechts.', art='P')
N.z('termwert', 3, 'Für welches x hat T(x) = (x + 1)/(x − 1) den Wert −1?', 0, '0', 'x + 1 = −(x − 1) = −x + 1 ⇔ 2x = 0 ⇔ x = 0. Probe: 1/(−1) = −1.',
    'Multipliziere mit dem Nenner. Achte auf das Minus vor der Klammer.', art='K')
N.a('termwert', 3, 'Welchen Wert kann T(x) = (2x + 1)/x für kein x annehmen?', '2', ['0', '1', '3'],
    'Aufteilen: (2x + 1)/x = 2 + 1/x. Der Bruch 1/x ist nie 0, also ist T(x) nie 2. 0 gibt es bei x = −0,5, 1 bei x = −1, 3 bei x = 1.',
    'Teile den Bruch in 2x/x + 1/x auf.', art='K')

# kuerzen
N.a('kuerzen', 2, 'Kürze vollständig: 12x²y/(18xy²)', '2x/(3y)', ['2/3', '2xy/3', '6x/(9y)'], '12 : 6 = 2, 18 : 6 = 3. x²/x = x, y/y² = 1/y. Ergebnis 2x/(3y).',
    'Kürze Zahlen und jede Variable einzeln.')
N.a('kuerzen', 2, 'Kürze vollständig: (6x + 4)/(9x + 6)', '2/3', ['(6x + 2)/(9x + 3)', '4/6', '(2x + 4)/(3x + 6)'],
    'Ausklammern: 6x + 4 = 2(3x + 2) und 9x + 6 = 3(3x + 2). Der gleiche Faktor (3x + 2) kürzt sich: 2/3.', 'Klammere im Zähler 2 und im Nenner 3 aus.')
N.a('kuerzen', 3, 'Kürze vollständig: (3x² + 9x)/(6x)', '(x + 3)/2', ['(x + 9)/2', '(x² + 3x)/2', 'x + 3/2'],
    'Zähler ausklammern: 3x² + 9x = 3x(x + 3). Dann 3x(x + 3)/(6x) = (x + 3)/2. Man darf nicht nur 3x² kürzen.', 'Klammere im Zähler 3x aus.', art='P')
N.a('kuerzen', 3, 'Kürze vollständig: (x − 4)/(4 − x)', '−1', ['1', '0', 'nicht kürzbar'],
    '4 − x = −(x − 4). Also (x − 4)/(−(x − 4)) = −1 (für x ≠ 4). Probe mit x = 6: 2/(−2) = −1.', 'Klammere im Nenner −1 aus.', art='P')
N.a('kuerzen', 3, 'Kürze vollständig: (x² + 6x + 9)/(2x + 6)', '(x + 3)/2', ['(x + 9)/2', 'x/2 + 9/6', '(x² + 3)/2'],
    'Zähler: binomische Formel x² + 6x + 9 = (x + 3)². Nenner: 2(x + 3). Kürzen mit (x + 3): (x + 3)/2.', 'Erkennst du im Zähler eine binomische Formel?', art='K')
N.z('kuerzen', 3, 'Für welchen Wert von a lässt sich (x + a)/(3x + 12) vollständig zu 1/3 kürzen?', 4, '12 / 3',
    '3x + 12 = 3(x + 4). Damit 1/3 übrig bleibt, muss der Zähler x + 4 sein: a = 4.', 'Klammere im Nenner 3 aus.', art='K')

# erweitern
N.l('erweitern', 2, 'Erweitere 3/(x + 2) auf den Nenner x² + 2x. Gib den neuen Zähler ein.', '□x', [3], ['3'],
    'x² + 2x = x(x + 2). Also mit x erweitern: neuer Zähler 3x.', 'Wie entsteht x² + 2x aus x + 2?', 'Tippe den Term ein, z. B. 3x.')
N.l('erweitern', 2, 'Mit welchem Term wurde (x + 1)/3 erweitert, wenn der neue Nenner 6x ist?', '□x', [2], ['6 / 3'], '6x : 3 = 2x. Erweitert wurde mit 2x.',
    'Neuer Nenner : alter Nenner.', 'Tippe den Term ein, z. B. 2x.')
N.l('erweitern', 3, 'Gib den Hauptnenner von 1/(4x) und 5/(6x²) an.', '□x²', [12], ['12'],
    'Zahlen: kleinstes gemeinsames Vielfaches von 4 und 6 ist 12. Variablen: x² enthält x. Hauptnenner 12x² (nicht 24x³).',
    'kgV der Zahlen, höchste Potenz von x.', 'Tippe den Term ein, z. B. 12x².', art='P')
N.l('erweitern', 3, 'Gib den Hauptnenner von 2/(x + 1) und 3/(x² + x) an.', '□x² + □x', [1, 1], ['1', '1'],
    'x² + x = x(x + 1) enthält schon x + 1. Hauptnenner ist x(x + 1) = x² + x.', 'Klammere im zweiten Nenner aus.', 'Tippe den Term ein, z. B. x² + x.', art='P')
N.z('erweitern', 3, 'Erweitere 2/(x − 1) auf den Nenner 1 − x. Wie heißt der neue Zähler?', -2, '2 * (-1)',
    '1 − x = (−1) · (x − 1). Erweitert wird also mit −1: neuer Zähler 2 · (−1) = −2. 2/(x − 1) = −2/(1 − x).', 'Mit welcher Zahl wird x − 1 zu 1 − x?', art='K')
N.l('erweitern', 3, 'Der Bruch (x + 3)/(2x) wurde erweitert. Er heißt jetzt (x² + 3x)/(□x²). Ergänze den Nenner.', '□x²', [2], ['2'],
    'Der Zähler x + 3 wurde zu x² + 3x = x(x + 3). Erweitert wurde mit x, also wird der Nenner 2x · x = 2x².', 'Womit wurde der Zähler multipliziert?',
    'Tippe den Term ein, z. B. 2x².', art='K')

# addieren
N.a('addieren', 2, 'Fasse zusammen: 3/(2x) + 1/(4x)', '7/(4x)', ['4/(6x)', '4/(4x)', '7/(8x²)'], 'Hauptnenner 4x: 3/(2x) = 6/(4x). 6/(4x) + 1/(4x) = 7/(4x).',
    'Erweitere den ersten Bruch auf 4x.')
N.a('addieren', 2, 'Fasse zu einem Bruch zusammen: 1 + 2/x', '(x + 2)/x', ['3/x', '(1 + 2)/x', '2/(x + 1)'], '1 = x/x. Also x/x + 2/x = (x + 2)/x.', 'Schreibe 1 als Bruch mit Nenner x.')
N.a('addieren', 3, 'Fasse zusammen und vereinfache: (x + 2)/x² − 1/x', '2/x²', ['(x + 1)/x²', '(x + 2)/x', '(2 − x)/x²'],
    'Hauptnenner x²: 1/x = x/x². (x + 2 − x)/x² = 2/x².', 'Erweitere 1/x auf x². Achte beim Abziehen auf alle Glieder.', art='P')
N.a('addieren', 3, 'Fasse zu einem Bruch zusammen: 3x/(x − 2) − 1', '(2x + 2)/(x − 2)', ['(2x − 2)/(x − 2)', '(3x − 1)/(x − 2)', '3x/(x − 3)'],
    '1 = (x − 2)/(x − 2). 3x − (x − 2) = 3x − x + 2 = 2x + 2. Ergebnis (2x + 2)/(x − 2).', 'Schreibe 1 mit dem Nenner x − 2. Das Minus gilt für den ganzen Zähler.', art='P')
N.a('addieren', 3, 'Fasse zusammen: 1/(x − 2) + 1/(2 − x)', '0', ['2/(x − 2)', '2/(x² − 4)', '1/(2x − 4)'],
    '2 − x = −(x − 2), also 1/(2 − x) = −1/(x − 2). Dann 1/(x − 2) − 1/(x − 2) = 0.', 'Vergleiche die Nenner genau. Was ist 2 − x im Vergleich zu x − 2?', art='K')
N.z('addieren', 3, 'Es gilt a/x + 3/(x + 1) = (5x + 2)/(x(x + 1)). Bestimme a.', 2, '2',
    'a/x + 3/(x + 1) = (a(x + 1) + 3x)/(x(x + 1)) = ((a + 3)x + a)/(x(x + 1)). Vergleich mit 5x + 2: a = 2 (und a + 3 = 5 passt).',
    'Bringe die linke Seite auf den Hauptnenner und vergleiche die Zähler.', art='K')

# multiplizieren
N.a('multiplizieren', 2, 'Berechne und kürze: (2x/3) · (9/(4x²))', '3/(2x)', ['18x/(12x²)', '3x/2', '2/(3x)'], '2x · 9 = 18x, 3 · 4x² = 12x². 18x/(12x²) = 3/(2x).',
    'Zähler mal Zähler, Nenner mal Nenner, dann kürzen.')
N.a('multiplizieren', 2, 'Berechne und kürze: (x + 1)/x : (x + 1)/x²', 'x', ['1/x', '(x + 1)²/x³', '1'], 'Mit dem Kehrbruch malnehmen: (x + 1)/x · x²/(x + 1) = x²/x = x.',
    'Teilen heißt: mit dem Kehrbruch malnehmen.')
N.a('multiplizieren', 3, 'Berechne und kürze: 2x : (4/x)', 'x²/2', ['8/x', '1/(2x²)', '8x²'], '2x · x/4 = 2x²/4 = x²/2.', 'Schreibe 2x als 2x/1 und nimm mit dem Kehrbruch mal.', art='P')
N.a('multiplizieren', 3, 'Berechne und kürze: (x² − 9)/(2x) · 4x/(x + 3)', '2(x − 3)', ['2(x + 3)', '4(x − 3)/2x', '2x − 9'],
    'x² − 9 = (x + 3)(x − 3). Dann (x + 3)(x − 3) · 4x/(2x(x + 3)) = 2(x − 3).', 'Zerlege x² − 9 mit der binomischen Formel, dann kürzen.', art='P')
N.z('multiplizieren', 3, 'Das Ergebnis von (3x − 6)/(x + 1) : (x − 2)/(2x + 2) ist eine Zahl. Welche?', 6, '3 * 2',
    '3x − 6 = 3(x − 2) und 2x + 2 = 2(x + 1). Kehrbruch: 3(x − 2)/(x + 1) · 2(x + 1)/(x − 2) = 3 · 2 = 6.', 'Klammere zuerst aus. Dann kürzt sich alles mit x weg.', art='K')
N.a('multiplizieren', 3, 'Mit welchem Bruchterm muss man x/(x + 1) multiplizieren, um 1 zu erhalten?', '(x + 1)/x', ['1/(x + 1)', '(x − 1)/x', 'x/(x + 1)'],
    'Ein Bruch mal sein Kehrbruch ergibt 1: x/(x + 1) · (x + 1)/x = 1.', 'Was ergibt 2/3 · 3/2?', art='K')

# fehler_finden
N.a('fehler_finden', 2, 'Welche Umformung ist richtig (für alle x aus D)?', '(2x + 4)/2 = x + 2', ['(2x + 4)/2 = x + 4', 'x/(x + 4) = 1/4', '(x + 4)/x = 4'],
    '(2x + 4)/2 = 2(x + 2)/2 = x + 2. Die anderen kürzen Summanden statt Faktoren.', 'Kürzen geht nur mit gemeinsamen Faktoren.')
N.a('fehler_finden', 2, 'Welche Umformung ist FALSCH (für alle x aus D)?', '(x² + 4)/(x + 2) = x + 2', ['x/(2x) = 1/2', '(x − 3)/(3 − x) = −1', '(x + 2)²/(x + 2) = x + 2'],
    'x² + 4 ist keine binomische Formel; (x + 2)² wäre x² + 4x + 4. Gegenbeispiel x = 1: 5/3 ≠ 3.', 'Setze eine Zahl ein, z. B. x = 1.')
N.a('fehler_finden', 3, 'Tim rechnet: 2/x − (x − 1)/x = (2 − x − 1)/x = (1 − x)/x. Was stimmt?', 'Falsch: Das Minus gilt für den ganzen Zähler. Richtig ist (3 − x)/x.',
    ['Richtig gerechnet.', 'Falsch: Man darf nur gleiche Nenner subtrahieren.', 'Falsch: Richtig ist (1 − x)/(2x).'],
    'Vor (x − 1) steht ein Minus: 2 − (x − 1) = 2 − x + 1 = 3 − x. Tim hat die Klammer weggelassen.', 'Setze den zweiten Zähler in Klammern.', art='P')
N.a('fehler_finden', 3, 'Lena prüft (x² + x)/x = x + 1 mit x = 0 und sagt: „Stimmt nicht.“ Was stimmt?', 'Lenas Probe zählt nicht: x = 0 gehört nicht zu D. Für alle x ≠ 0 stimmt die Umformung.',
    ['Lena hat recht: Ein Gegenbeispiel genügt.', 'Lena hat recht: Kürzen mit x ist verboten.', 'Die Umformung stimmt nur für x = 1.'],
    'Für x = 0 ist der linke Term gar nicht definiert. (x² + x)/x = x(x + 1)/x = x + 1 gilt für jedes x aus D = ℚ \\ {0}.',
    'Darf man x = 0 überhaupt einsetzen?', art='P')
N.z('fehler_finden', 3, 'Die Umformung (x + 6)/(x + 2) = 6/2 ist falsch. Für welches x ergibt sie trotzdem eine wahre Aussage?', 0, '0',
    '(x + 6)/(x + 2) = 3 ⇔ x + 6 = 3x + 6 ⇔ x = 0. Nur bei x = 0 stimmt es zufällig: 6/2 = 3.', 'Löse (x + 6)/(x + 2) = 3.', art='K')
N.a('fehler_finden', 3, 'Mit welcher Zahl kannst du zeigen, dass 1/x + 1/2 = 2/(x + 2) falsch ist?', 'x = 2', ['x = 0', 'x = −2', 'mit keiner, die Umformung stimmt'],
    'x = 2: links 1/2 + 1/2 = 1, rechts 2/4 = 0,5. Ungleich – Gegenbeispiel. x = 0 und x = −2 darf man nicht einsetzen.',
    'Ein Gegenbeispiel muss erlaubt sein (in D liegen).', art='K')

baue = mit_schwer(baue, N)
# ---- SCHWER ENDE ----

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, mit_befunden  # noqa: E402

BF = Befunde('terme.bruchterme', 13_8_4)
# a) gleicher Typ wie Stufe 2
BF.stufe('erweitern', 'Mit welchem Term wurde 2/(4x) erweitert, wenn der neue Nenner 8x³ ist?', 2)
BF.stufe('addieren', 'Fasse zusammen: (5x − 7)/x − (2x + 1)/x', 2)
BF.stufe('addieren', 'Fasse zusammen: (5x + 5)/(x + 1) − (4x − 1)/(x + 1)', 2)
BF.stufe('fehler_finden', 'Warum ist 5/x + 2/x nicht 7/(2x)?', 2)
BF.nicht_umgesetzt('kuerzen S3 (x² − 49)/(x − 7) setzt die 3. binomische Formel voraus',
                   'Aufgaben sind richtig und echte Stufe 3. Offen ist nur, ob die binomischen Formeln im Plan vor diesem Thema stehen (Reihenfolge, Haupt-Chat).')

baue = mit_befunden(baue, BF)
# ---- BEFUNDE ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Teil A: Gesamtdurchsicht Kl. 8, siehe _durchsicht_kl8.py) ----
from _durchsicht_kl8 import Durchsicht, mit_durchsicht  # noqa: E402

DSX = Durchsicht('terme.bruchterme', 19_8_7)
DSX.stufe('termwert', 'Berechne T(−6) für T(x) = (−x + 9)/(x + 2).', 2)
DSX.stufe('termwert', 'Berechne T(4) für T(x) = (−x − 6)/(−x − 2). Gib das Ergebnis als vollständig gekürzten Bruch an.', 2)
DSX.stufe('termwert', 'Für welches x hat T(x) = 4/(x − 3) den Wert 4?', 2)
DSX.stufe('termwert', 'Für welches x hat T(x) = −18/(x − 5) den Wert 3?', 2)
DSX.stufen('termwert', 'S1 einsetzen; S2 Bruch als Ergebnis, x gesucht; S3 teils dieselben Aufgaben wie S2',
           'S1 einsetzen; S2 Ergebnis als Bruch, x zu gegebenem Wert; S3 Parameter a, Tabellenkalkulation (Rechenreihenfolge), Wert −1, unerreichbarer Wert')
# kuerzen: viermal (x² − a²)/(x ± a) in Reihe → zwei durch andere Stufe-3-Gedanken ersetzt
DSX.ersetze('kuerzen', 'Kürze vollständig: (x² − 16)/(x − 4)', DSX.A(
    'Kürze vollständig: (2x² − 18)/(x + 3)', '2x − 6', ['2x − 3', 'x − 3', '2x² − 6'],
    'Erst 2 ausklammern: 2x² − 18 = 2(x² − 9) = 2(x + 3)(x − 3) (dritte binomische Formel). (x + 3) kürzen: 2(x − 3) = 2x − 6.',
    'Klammere zuerst eine Zahl aus. Erkennst du danach eine binomische Formel?'))
DSX.ersetze('kuerzen', 'Kürze vollständig: (x² − 25)/(x + 5)', DSX.A(
    'Tom kürzt (x² + 4)/(x + 2) zu x + 2. Was stimmt?', 'Falsch: x² + 4 lässt sich nicht in (x + 2) · … zerlegen. Der Bruch ist nicht kürzbar.',
    ['Richtig: x² + 4 = (x + 2)².', 'Richtig: x² + 4 = (x + 2)(x − 2).', 'Falsch: Richtig ist x − 2.'],
    '(x + 2)² = x² + 4x + 4 und (x + 2)(x − 2) = x² − 4 – beides ist nicht x² + 4. Probe mit x = 1: 5/3 ≠ 3.',
    'Multipliziere (x + 2)² und (x + 2)(x − 2) aus und vergleiche mit x² + 4.'))
DSX.stufen('kuerzen', 'S1 Potenzen kürzen; S2 ausklammern; S3 viermal dieselbe binomische Formel',
           'S1 Potenzen kürzen; S2 ausklammern, zwei Variablen; S3 binomische Formel (auch nach Ausklammern), Fehler finden, (x − 4)/(4 − x), Parameter')
DSX.stufe('fehler_finden', 'Welche Umformung ist FALSCH?', 2, enthaelt='(x/3) : 9 = 9x/3')
DSX.stufe('fehler_finden', 'Welche Umformung ist FALSCH?', 2, enthaelt='6/x + 8/x = 14/(2x)')
DSX.stufen('fehler_finden', 'S1 richtige Umformung wählen; S2 falsche wählen, begründen; S3 teils dieselbe Wahl wie S2',
           'S1 richtige Umformung wählen; S2 falsche wählen, Fehler begründen; S3 Fehler in einer Rechnung, Probe außerhalb von D, Sonderfall x = 0, Gegenbeispiel finden')
DSX.stufen('definitionsmenge', 'S1 ein Nenner x − a; S2 Nenner ax + b, Produkt; S3 zwei Brüche, x² + c, Parameter, Division')
DSX.stufen('erweitern', 'S1 neuer Zähler; S2 Erweiterungsterm, Zähler mit Summe; S3 Nenner faktorisieren, Hauptnenner, 1 − x')
DSX.stufen('addieren', 'S1 gleicher Nenner; S2 Hauptnenner x bzw. x²; S3 Nenner x − a, 1 als Bruch, (x − 2) und (2 − x), Parameter')
DSX.stufen('multiplizieren', 'S1 Malnehmen; S2 Teilen mit Kehrbruch; S3 Klammerterme kürzen, binomische Formel, Ergebnis eine Zahl, Kehrbruch gesucht')
baue = mit_durchsicht(baue, DSX)
# ---- DURCHSICHT ENDE ----

# ---- STUFEN (Zwanzigste Runde: echte Stufe 3 und Knobel-Bordkarten, siehe _stufen_kl8.py) ----
from _stufen_kl8 import Stufen, mit_stufen  # noqa: E402

ST = Stufen('terme.bruchterme', 20_8_3)
SA, SZ, SL = ST.A, ST.Z, ST.L
def T(lz, *regeln):
    for m, g in regeln: ST.typ(lz, m, g)

# --- definitionsmenge ---
ST.leiter('definitionsmenge', 'die Zahl finden, für die ein einfacher Nenner 0 wird, und D angeben',
          'Nenner mit Faktor oder Produkt, Sachterm deuten, zu einer Definitionsmenge den Term finden',
          'mehrere Nenner verknüpfen, Nenner, der nie 0 wird, begründen, Fehler beim Vorzeichen, Parameter, rückwärts, Sachmodell')
T('definitionsmenge', (r'^Gib die Definitionsmenge von [^/]+/\(x [−+] \d+\) an', 'direkt'), (r'^Für welche Zahl ist der Term [^/]+/\(x [−+]', 'erkennen'),
  (r'x² \+ \d\)', 'begruenden'), (r'\) \+ \d/\(|\) : \(|x² − \dx', 'verknuepfen'), (r'^Welcher Term hat', 'umkehr'), (r'^Ein Term hat', 'rueckwaerts'), (r'Wert von a', 'parameter'),
  (r'^Für welche Zahl|^Gib die Definitionsmenge', 'mehrschritt'))
ST.neu('definitionsmenge', 'einkleidung', SZ('Bei einer Feier zahlen alle Gäste gleich viel, nur die zwei Gastgeber nicht: Jeder zahlt 240/(n − 2) €, wenn n Personen da sind. Für welche Personenzahl n ergibt der Term keinen Sinn?', 2, '2',
    'Der Nenner n − 2 ist für n = 2 null – dann gäbe es niemanden, der zahlt.', 'Wann wird der Nenner 0?'))
ST.neu('definitionsmenge', 'fehler', SA('Jemand sagt: „Die Definitionsmenge von 4/(x + 5) ist ℚ \\ {5}.“ Was stimmt?', 'Falsch: Der Nenner ist 0 für x = −5, also ℚ \\ {−5}.',
    ['Richtig.', 'Falsch: D = ℚ \\ {4}.', 'Falsch: D = ℚ, der Nenner wird nie 0.'], 'x + 5 = 0 ⇒ x = −5. Für x = 5 ist der Nenner 10, das ist erlaubt.', 'Setze 5 und −5 in den Nenner ein.'))
ST.neu('definitionsmenge', 'begruenden', SA('Haben 1/(x − 2) und x/(x² − 2x) dieselbe Definitionsmenge?', 'Nein: Der zweite Term ist auch für x = 0 nicht definiert.',
    ['Ja, beide ℚ \\ {2}.', 'Ja, man kann den zweiten zu 1/(x − 2) kürzen.', 'Nein: Der erste ist für x = 0 nicht definiert.'],
    'x² − 2x = x(x − 2) ist für x = 0 und x = 2 null, also D = ℚ \\ {0; 2}. Beim ersten fehlt nur die 2. Kürzen ändert die Werte, aber nicht die ursprüngliche Definitionsmenge.', 'Zerlege den Nenner x² − 2x in Faktoren.'))
ST.neu('definitionsmenge', 'transfer', SZ('Am Hebel gilt: Die nötige Kraft ist 600/a Newton, wenn man im Abstand a (in m) von der Drehachse drückt. a = 0 ergibt keinen Sinn. Wie groß ist die Kraft bei a = 1,5 m?', 400, '600 / (15/10)',
    'F = 600/1,5 = 400 N. Bei a = 0 (genau an der Achse) wäre der Nenner 0 – dort kann man den Hebel nicht drehen.', 'Setze 1,5 für a ein.', einheit='N'))
ST.knobel('definitionsmenge', SZ('Der Term 1/((x − 1)(x − 2)(x − 3)) ist für drei Zahlen nicht definiert. Für wie viele ganze Zahlen x von −5 bis 5 ist sein Wert positiv?', 2, '5 - 4 + 1',
    'Der Bruch ist positiv, wenn der Nenner positiv ist. Ein Produkt aus drei Faktoren ist positiv, wenn keiner oder genau zwei negativ sind. Keiner negativ: x > 3, also x = 4, 5. Genau zwei negativ: 1 < x < 2 – dort gibt es keine ganze Zahl. Antwort: 2.',
    'Wann ist ein Produkt aus drei Zahlen positiv? Zähle die negativen Faktoren.'))
ST.knobel('definitionsmenge', SA('Der Term 1/(x − a) + 1/(x − b) hat die Definitionsmenge ℚ \\ {2}. Was folgt?', 'a = b = 2', ['a = 2, b beliebig', 'a + b = 2', 'a = −b'],
    'Ausgeschlossen sind genau a und b. Wenn nur die 2 fehlt, müssen beide Zahlen 2 sein. Wäre b ≠ 2, fehlte auch b.', 'Welche Zahlen schließt jeder der beiden Nenner aus?'))

# --- termwert ---
ST.leiter('termwert', 'eine Zahl in einen Bruchterm einsetzen und ausrechnen',
          'Ergebnis als gekürzter Bruch, Sachterm auswerten, gesuchtes x zu einem Wert bestimmen',
          'rückwärts aus dem Wert, verketten T(T(x)), Fehler beim Einsetzen, Parameter, Tabellenkalkulation, unmöglichen Wert begründen')
T('termwert', (r'gekürzten Bruch', 'mehrschritt'), (r'^Berechne T\([^)]*\) für T\(x\) = ', 'direkt'), (r'^Für welches x hat T\(x\) = −?\d+/', 'umkehr'), (r'den Wert −1', 'umkehr'),
  (r'gekürzten Bruch', 'mehrschritt'), (r'Bestimme a', 'parameter'), (r'Zelle', 'transfer'), (r'für kein x', 'begruenden'))
ST.neu('termwert', 'erkennen', SA('Welcher Term hat für x = 2 den Wert 1?', '(x + 4)/6', ['(x + 4)/(x + 4) − 1', 'x/4', '3/(x + 4)'],
    '(2 + 4)/6 = 1. Die anderen ergeben 0, 1/2 und 1/2.', 'Setze 2 in jeden Term ein.'))
ST.neu('termwert', 'einkleidung', SZ('Bei n Personen kostet eine Busfahrt jeden (300 + 15n)/n Euro. Was zahlt jeder bei 20 Personen?', 30, '(300 + 15 * 20) / 20',
    '(300 + 300)/20 = 600/20 = 30 €.', 'Setze n = 20 ein.', einheit='€'))
ST.neu('termwert', 'fehler', SA('Für T(x) = (x + 6)/(x − 2) rechnet jemand: T(−2) = (−2 + 6)/(−2 − 2) = 4/0 – „nicht definiert“. Was stimmt?', 'Falsch: −2 − 2 = −4, also T(−2) = 4/(−4) = −1.',
    ['Richtig, T(−2) gibt es nicht.', 'Falsch: T(−2) = 1.', 'Falsch: T(−2) = 4.'], 'Der Nenner ist −2 − 2 = −4, nicht 0. Nicht definiert ist T nur bei x = 2.', 'Rechne den Nenner langsam nach.'))
ST.neu('termwert', 'rueckwaerts', SZ('Für T(x) = 12/(x − 3) gilt T(a) = −4. Bestimme a.', 0, '3 + 12 / (-4)',
    '12/(a − 3) = −4 ⇒ a − 3 = 12 : (−4) = −3 ⇒ a = 0. Probe: 12/(−3) = −4.', 'Welche Zahl muss im Nenner stehen, damit −4 herauskommt?'))
ST.neu('termwert', 'verknuepfen', SZ('Für T(x) = (x + 1)/(x − 1): Berechne T(T(3)).', 3, '((4/2) + 1) / ((4/2) - 1)',
    'Innen: T(3) = 4/2 = 2. Außen: T(2) = 3/1 = 3.', 'Rechne zuerst T(3) aus und setze das Ergebnis wieder ein.'))
ST.neu('termwert', 'pruefung', SZ('Gegeben ist T(x) = (2x − 1)/(x + 4). Für welches x hat T den Wert 0?', 0.5, '1 / 2',
    'Ein Bruch ist 0, wenn der Zähler 0 ist (und der Nenner nicht): 2x − 1 = 0 ⇒ x = 0,5. Der Nenner ist dort 4,5.', 'Wann ist ein Bruch gleich null?'))
ST.neu('termwert', 'begruenden', SA('Stimmt: „T(x) = 1/x wird umso kleiner, je größer x ist“?', 'Nicht für alle x: T(−1) = −1 ist kleiner als T(2) = 0,5.',
    ['Ja, für alle x ≠ 0.', 'Nein, 1/x wird immer größer.', 'Ja, aber nur für negative x.'],
    'Für positive x stimmt es, aber nicht, wenn man eine negative und eine positive Zahl vergleicht: −1 < 2, trotzdem T(−1) < T(2).', 'Probiere eine negative und eine positive Zahl.'))
ST.knobel('termwert', SZ('Für wie viele ganze Zahlen x ist (x + 7)/(x + 1) eine ganze Zahl?', 8, '2 * 4',
    '(x + 7)/(x + 1) = (x + 1 + 6)/(x + 1) = 1 + 6/(x + 1). Ganz ist das genau dann, wenn x + 1 ein Teiler von 6 ist: ±1, ±2, ±3, ±6. Das sind 8 Möglichkeiten (x = 0, −2, 1, −3, 2, −4, 5, −7).',
    'Zerlege den Zähler so, dass der Nenner darin vorkommt.'))
ST.knobel('termwert', SZ('Für T(x) = x/(x + 1): Berechne T(1) · T(2) · T(3) · … · T(9).', 0.1, '1 / 10',
    'Das Produkt ist 1/2 · 2/3 · 3/4 · … · 9/10. Jeder Nenner kürzt sich mit dem nächsten Zähler, übrig bleiben 1 oben und 10 unten: 1/10 = 0,1.',
    'Schreib die ersten drei Faktoren nebeneinander und schau, was sich kürzt.'))

# --- kuerzen ---
ST.leiter('kuerzen', 'gemeinsame Faktoren (Zahl, Potenz von x) in Zähler und Nenner kürzen',
          'erst ausklammern, dann kürzen; den Term finden, der gekürzt ein Ergebnis ergibt; Tabellenwerte durch Kürzen erklären',
          'binomische Formeln verknüpfen, „Summen kürzen“ als Fehler deuten, begründen, Parameter, ungekürzten Term rekonstruieren')
T('kuerzen', (r'^Kürze vollständig: \d+x[⁰¹²³⁴⁵⁶⁷⁸⁹]*/\(\d+x', 'direkt'), (r'^Tom', 'fehler'), (r'x²', 'verknuepfen'), (r'\(x − \d+\)/\(\d+ − x\)', 'transfer'), (r'Wert von a', 'parameter'), (r'^Kürze', 'mehrschritt'))
ST.neu('kuerzen', 'erkennen', SA('Welcher Bruchterm lässt sich durch x kürzen?', '3x/(5x²)', ['(x + 3)/(5x)', '3/(x + 5)', '(3 + x)/(5 + x)'],
    'Nur in 3x/(5x²) ist x in Zähler UND Nenner ein Faktor: 3x/(5x²) = 3/(5x). In den anderen steht x in einer Summe.', 'Kürzen darf man nur Faktoren.'))
ST.neu('kuerzen', 'umkehr', SA('Welcher Term ergibt vollständig gekürzt 2/x?', '6x/(3x²)', ['6x/(3x)', '(2 + x)/(x + x)', '2x/(x + x²)'],
    '6x/(3x²): durch 3x kürzen ergibt 2/x. 6x/(3x) = 2, (2 + x)/(2x) lässt sich nicht kürzen, 2x/(x + x²) = 2/(1 + x).', 'Kürze jeden Term und vergleiche.'))
ST.neu('kuerzen', 'darstellung', SA('Für T(x) = (2x + 4)/(x + 2) zeigt eine Tabelle: x = 1 → 2, x = 3 → 2, x = 10 → 2. Welche gekürzte Form erklärt das?', 'T(x) = 2 (für x ≠ −2)', ['T(x) = 2x', 'T(x) = x + 2', 'T(x) = 4'],
    '2x + 4 = 2(x + 2). Kürzen durch (x + 2) ergibt 2 – für jedes erlaubte x.', 'Klammere im Zähler aus.'))
ST.neu('kuerzen', 'einkleidung', SA('Ein Rechteck hat den Flächeninhalt (6x² + 3x) cm² und ist 3x cm breit. Wie lang ist es?', '(2x + 1) cm', ['(2x + 3x) cm', '(6x + 1) cm', '(2x² + x) cm'],
    'Länge = Fläche : Breite = (6x² + 3x)/(3x) = 3x(2x + 1)/(3x) = 2x + 1.', 'Teile die Fläche durch die Breite und kürze.'))
ST.neu('kuerzen', 'begruenden', SA('Darf man (x + 5)/(x + 5)² zu 1/(x + 5) kürzen?', 'Ja: (x + 5) ist in Zähler und Nenner ein Faktor (für x ≠ −5).',
    ['Nein: Summen darf man nie kürzen.', 'Nein: Es kommt 1/5 heraus.', 'Ja: Es kommt x + 5 heraus.'],
    '(x + 5)² = (x + 5)(x + 5). Die ganze Klammer ist ein Faktor; einmal gekürzt bleibt 1/(x + 5).', 'Ist die Klammer hier Summand oder Faktor?'))
ST.neu('kuerzen', 'rueckwaerts', SL('Ein Bruchterm wurde durch (x − 2) gekürzt und ergab 3/(x + 1). Der ungekürzte Nenner war (x + 1)(x − 2). Wie hieß der ungekürzte Zähler (ausmultipliziert)?', '□x − □', [3, 6], ['3', '6'],
    'Zum Rückgängigmachen erweitert man mit (x − 2): Zähler 3 · (x − 2) = 3x − 6.', 'Kürzen rückgängig machen heißt erweitern.'))
ST.neu('kuerzen', 'pruefung', SZ('Kürze (4x² − 8x)/(2x) und berechne dann den Wert für x = 5.', 6, '2 * 5 - 4',
    '4x² − 8x = 4x(x − 2). Durch 2x gekürzt: 2(x − 2) = 2x − 4. Für x = 5: 10 − 4 = 6.', 'Klammere im Zähler zuerst 4x aus.'))
ST.knobel('kuerzen', SZ('Für wie viele natürliche Zahlen n von 1 bis 20 lässt sich der Bruch (n + 4)/(n + 1) noch kürzen?', 7, '(20 - 2) // 3 + 1',
    'Ein gemeinsamer Teiler von n + 4 und n + 1 teilt auch ihre Differenz 3. Kürzbar ist der Bruch also genau, wenn 3 beide teilt, d. h. wenn n + 1 durch 3 teilbar ist: n = 2, 5, 8, 11, 14, 17, 20 – sieben Zahlen.',
    'Was teilt ein gemeinsamer Teiler zweier Zahlen außer den Zahlen selbst noch?'))
ST.knobel('kuerzen', SZ('Der Bruchterm (x² − 1)/(x² + 2x + 1) wird vollständig gekürzt. Welchen Wert hat das Ergebnis für x = 3?', 0.5, '(3 - 1) / (3 + 1)',
    'Zähler: x² − 1 = (x + 1)(x − 1). Nenner: x² + 2x + 1 = (x + 1)². Gekürzt: (x − 1)/(x + 1). Für x = 3: 2/4 = 0,5.',
    'Zähler und Nenner sind beide binomische Formeln.'))

# --- erweitern ---
ST.leiter('erweitern', 'einen Bruchterm auf einen vorgegebenen Nenner erweitern',
          'den Erweiterungsfaktor bestimmen, Zähler mit Klammer erweitern, gleichwertigen Term mit gegebenem Nenner finden',
          'Nenner erst faktorisieren, Hauptnenner, Erweitern mit −1, Fehler beim Ausmultiplizieren, begründen, rückwärts zum ursprünglichen Term')
T('erweitern', (r'4x² \+ \d+x|3x \+ 27', 'verknuepfen'), (r'Hauptnenner|1 − x', 'transfer'), (r'Ergänze den Nenner', 'rueckwaerts'),
  (r'^Mit welchem Term', 'umkehr'), (r'^Erweitere \d+/', 'direkt'), (r'^Erweitere', 'mehrschritt'))
ST.neu('erweitern', 'erkennen', SA('Welcher Bruch ist eine Erweiterung von 3/x?', '6/(2x)', ['6/(x + 2)', '(3 + x)/(x + x)', '3x/x'],
    '6/(2x): Zähler und Nenner wurden mit 2 multipliziert. Bei den anderen wurde addiert oder nur ein Teil verändert.', 'Erweitern = Zähler UND Nenner mit demselben Faktor malnehmen.'))
ST.neu('erweitern', 'darstellung', SA('Welcher Term hat für jedes x ≠ 0 denselben Wert wie 2/(5x) und den Nenner 15x³?', '6x²/(15x³)', ['6/(15x³)', '2x²/(15x³)', '6x/(15x³)'],
    '15x³ = 5x · 3x². Also auch den Zähler mit 3x² malnehmen: 2 · 3x² = 6x².', 'Womit muss man 5x malnehmen, um 15x³ zu erhalten?'))
ST.neu('erweitern', 'fehler', SA('Jemand erweitert 2/(x + 3) mit x und schreibt 2x/(x² + 3). Was ist falsch?', 'Der ganze Nenner muss mit x multipliziert werden: x(x + 3) = x² + 3x.',
    ['Nichts.', 'Man darf nur den Nenner erweitern.', 'Der Zähler müsste 2 + x heißen.'], 'Beim Erweitern wird jeder Summand des Nenners mit x multipliziert: x · x + x · 3.', 'Multipliziere die Klammer (x + 3) vollständig mit x.'))
ST.neu('erweitern', 'begruenden', SA('Verändert das Erweitern eines Bruchterms seinen Wert?', 'Nein: Zähler und Nenner werden mit demselben Faktor (≠ 0) multipliziert – das ist wie · 1.',
    ['Ja, er wird größer.', 'Ja, wenn man mit x erweitert.', 'Nur bei negativen Zahlen.'], 'a/b = (a · k)/(b · k), weil k/k = 1 ist. Nur k = 0 ist verboten (beim Erweitern mit x also x ≠ 0).', 'Was ist k/k?'))
ST.knobel('erweitern', SZ('Der Bruch 3/7 wird so erweitert, dass Zähler und Nenner zusammen 150 ergeben. Wie heißt der neue Nenner?', 105, '7 * 150 / 10',
    'Mit dem Faktor k: Zähler 3k, Nenner 7k, zusammen 10k = 150 ⇒ k = 15. Neuer Nenner 7 · 15 = 105 (der Bruch heißt 45/105).',
    'Schreibe Zähler und Nenner mit dem unbekannten Erweiterungsfaktor.'))
ST.knobel('erweitern', SZ('Der Bruchterm x/(x + 2) wird mit (x − 1) erweitert. Für welches x ist der neue Term nicht definiert, der alte aber schon?', 1, '1',
    'Neu: x(x − 1)/((x + 2)(x − 1)). Der neue Nenner ist 0 für x = −2 und x = 1, der alte nur für x = −2. Also x = 1: Erweitern mit einem Term kann die Definitionsmenge verkleinern.',
    'Vergleiche, wann der alte und wann der neue Nenner 0 wird.'))

# --- addieren ---
ST.leiter('addieren', 'gleichnamige Bruchterme addieren/subtrahieren und den Hauptnenner erkennen',
          'auf Hauptnenner bringen, Zahl und Bruch zusammenfassen, Sachsituation (Anteile), fehlenden Zähler bestimmen',
          'verschiedene Nenner mit Klammer, Fehler 1/x + 1/y = 2/(x + y) widerlegen, Parameter, rückwärts, Prüfungsaufgabe mit Vereinfachen')
T('addieren', (r'^Fasse zusammen: \d+/\((x [−+] \d+)\) [+−] \d+/\(\1\)$', 'direkt'), (r'^Fasse zusammen: \d+/x [+−] \d+/\(x [−+] \d+\)$', 'verknuepfen'), (r'\(2 − x\)', 'begruenden'), (r'vereinfache', 'pruefung'),
  (r'− 1$', 'transfer'), (r'Bestimme a', 'parameter'), (r'^Fasse', 'mehrschritt'))
ST.neu('addieren', 'erkennen', SA('Welcher Hauptnenner passt zu 1/x + 1/(3x)?', '3x', ['3x²', '4x', 'x'], '3x ist durch x und durch 3x teilbar – der kleinste gemeinsame Nenner.', 'Welcher Nenner enthält beide Nenner?'))
ST.neu('addieren', 'einkleidung', SA('Pumpe A füllt ein Becken in x Stunden, Pumpe B in 2x Stunden. Welchen Anteil füllen beide zusammen in einer Stunde?', '3/(2x)', ['2/(3x)', '1/(3x)', '3/x'],
    'In einer Stunde: A schafft 1/x, B schafft 1/(2x). Zusammen 2/(2x) + 1/(2x) = 3/(2x).', 'Welchen Teil schafft jede Pumpe in einer Stunde?'))
ST.neu('addieren', 'umkehr', SL('Ergänze die Zahl im Zähler: 5/x − □/x = 2/x', '□', [3], ['5 - 2'], 'Gleicher Nenner: 5 − □ = 2, also □ = 3.', 'Bei gleichem Nenner rechnet man nur mit den Zählern.', hinweis='Eine ganze Zahl.'))
ST.neu('addieren', 'fehler', SA('Jemand rechnet 1/x + 1/y = 2/(x + y). Mit welchen Zahlen sieht man, dass das falsch ist?', 'x = 1, y = 1: links 2, rechts 1.',
    ['x = 2, y = 2: links 1, rechts 1/2 – also richtig.', 'Gar nicht, es ist richtig.', 'Nur mit x = 0 und y = 0.'],
    'Ein Gegenbeispiel genügt: 1/1 + 1/1 = 2, aber 2/(1 + 1) = 1. Richtig wäre (x + y)/(xy).', 'Setze einfache Zahlen ein und vergleiche beide Seiten.'))
ST.neu('addieren', 'rueckwaerts', SL('Zu 5/x wurde ein Bruchterm addiert, das Ergebnis ist (5x + 3)/x². Wie heißt der addierte Term?', '□/x²', [3], ['3'],
    '5/x = 5x/x². Von (5x + 3)/x² bleibt nach Abziehen 3/x².', 'Bring 5/x auf den Nenner x² und vergleiche die Zähler.', hinweis='Ganze Zahl im Zähler.'))
ST.knobel('addieren', SZ('Berechne 1/(1 · 2) + 1/(2 · 3) + 1/(3 · 4) + … + 1/(9 · 10).', 0.9, '1 - 1/10',
    'Jeder Summand lässt sich als Differenz schreiben: 1/(n(n + 1)) = 1/n − 1/(n + 1), z. B. 1/2 = 1 − 1/2, 1/6 = 1/2 − 1/3. In der Summe heben sich alle mittleren Glieder auf: 1 − 1/10 = 0,9.',
    'Schreibe 1/(1 · 2) und 1/(2 · 3) jeweils als Differenz zweier Stammbrüche.'))
ST.knobel('addieren', SA('Welcher Term ist für jedes x > 0 größer: 1/x + 1/(x + 2) oder 2/(x + 1)?', '1/x + 1/(x + 2)', ['2/(x + 1)', 'beide sind gleich', 'das hängt von x ab'],
    'Zieht man 2/(x + 1) von 1/x + 1/(x + 2) ab, ergibt sich nach dem Gleichnamigmachen 2/(x(x + 1)(x + 2)). Für x > 0 ist das positiv. Beispiel x = 1: 1 + 1/3 = 4/3 > 1.',
    'Bilde die Differenz der beiden Terme und bestimme ihr Vorzeichen.'))

# --- multiplizieren ---
ST.leiter('multiplizieren', 'zwei Bruchterme multiplizieren und kürzen, Kehrwert erkennen',
          'dividieren (mit dem Kehrwert malnehmen), Flächen mit Bruchtermen, fehlenden Faktor finden',
          'Klammerterme kürzen, Fehler beim Dividieren deuten, Aussagen widerlegen, Parameter, rückwärts, Ergebnis als Zahl')
T('multiplizieren', (r'^Berechne und kürze: \(\d+/\(\d+x[⁰¹²³⁴⁵⁶⁷⁸⁹]*\)\) · ', 'direkt'), (r'\(x [−+] \d+\)²|\(x² − 9\)', 'verknuepfen'), (r'eine Zahl', 'pruefung'),
  (r'^Mit welchem Bruchterm', 'umkehr'), (r'^Berechne', 'mehrschritt'))
ST.neu('multiplizieren', 'erkennen', SA('Was ist der Kehrwert von (x + 2)/(3x)?', '3x/(x + 2)', ['(x + 2)/(3x)', '−(x + 2)/(3x)', '(3x + 2)/x'],
    'Beim Kehrwert tauschen Zähler und Nenner die Plätze.', 'Zähler und Nenner tauschen.'))
ST.neu('multiplizieren', 'einkleidung', SA('Ein Rechteck ist (x + 1)/2 m lang und 4/(x + 1) m breit. Wie groß ist sein Flächeninhalt?', '2 m²', ['(x + 1)²/8 m²', '2(x + 1) m²', '(x + 5)/2 m²'],
    'A = (x + 1)/2 · 4/(x + 1) = 4(x + 1)/(2(x + 1)) = 2 – unabhängig von x.', 'Multipliziere und kürze die Klammer.'))
ST.neu('multiplizieren', 'fehler', SA('Jemand rechnet (2/x) : (4/x) = 8/x². Was stimmt?', 'Falsch: Man multipliziert mit dem Kehrwert: 2/x · x/4 = 1/2.', ['Richtig.', 'Falsch: Es kommt 2 heraus.', 'Falsch: Es kommt x/2 heraus.'],
    'Geteilt durch einen Bruch heißt mal den Kehrwert: (2/x) · (x/4) = 2x/(4x) = 1/2.', 'Was macht man beim Dividieren durch einen Bruch?'))
ST.neu('multiplizieren', 'begruenden', SA('Stimmt: „Das Produkt zweier Bruchterme mit x ist nie eine ganze Zahl“?', 'Falsch: z. B. 2/x · x/1 = 2 (für x ≠ 0).',
    ['Richtig.', 'Richtig, weil immer ein x übrig bleibt.', 'Falsch, aber nur für x = 1.'], 'Ein Gegenbeispiel genügt: Das x kann sich wegkürzen, dann bleibt eine Zahl.', 'Such zwei Bruchterme, bei denen sich x wegkürzt.'))
ST.neu('multiplizieren', 'parameter', SZ('Für welche Zahl a gilt (a/x) · (x²/6) = x für alle x ≠ 0?', 6, '6',
    '(a/x) · (x²/6) = a · x²/(6x) = a · x/6. Das soll x sein, also a/6 = 1 ⇒ a = 6.', 'Rechne das Produkt allgemein mit a aus.'))
ST.neu('multiplizieren', 'rueckwaerts', SL('Ein Term wurde durch 3/x geteilt, heraus kam 2x². Wie hieß der Term?', '□x', [6], ['2 * 3'],
    'Rückwärts: mit 3/x malnehmen. 2x² · 3/x = 6x.', 'Das Gegenteil von „durch 3/x teilen“ ist „mal 3/x“.', hinweis='Eine ganze Zahl vor x.'))
ST.knobel('multiplizieren', SZ('Berechne (1 + 1/2) · (1 + 1/3) · (1 + 1/4) · … · (1 + 1/9).', 5, '10 / 2',
    'Jede Klammer ist ein Bruch: 3/2 · 4/3 · 5/4 · … · 10/9. Jeder Zähler kürzt sich mit dem nächsten Nenner, übrig bleibt 10/2 = 5.',
    'Schreib jede Klammer als einen einzigen Bruch.'))
ST.knobel('multiplizieren', SA('Für x ≠ 0 und x ≠ 1 ist T(x) = 1/(1 − x). Was ergibt T(T(T(x)))?', 'x', ['1/(1 − x)', '(x − 1)/x', '1'],
    'T(T(x)) = 1/(1 − 1/(1 − x)) = 1/((1 − x − 1)/(1 − x)) = (1 − x)/(−x) = (x − 1)/x. Dann T((x − 1)/x) = 1/(1 − (x − 1)/x) = 1/(1/x) = x. Dreimal angewendet kommt man zurück zum Anfang.',
    'Rechne Schritt für Schritt und vereinfache nach jedem Schritt den Doppelbruch.'))

# --- fehler_finden ---
ST.leiter('fehler_finden', 'eine richtige Umformung erkennen bzw. eine einfache auf Richtigkeit prüfen',
          'die falsche Umformung finden, mit einer Probezahl prüfen, Tabelle und Definitionsmenge zusammendenken',
          'begründen, warum Summanden nicht gekürzt werden, Fehler im Rechenweg deuten, Gegenbeispiele, binomische Formeln verknüpfen')
T('fehler_finden', (r'^Warum', 'begruenden'), (r'Umformung ist richtig', 'erkennen'), (r'FALSCH', 'umkehr'), (r'^Tim|^Lena', 'fehler'),
  (r'trotzdem eine wahre', 'transfer'), (r'^Mit welcher Zahl', 'pruefung'))
ST.neu('fehler_finden', 'direkt', SA('Ist 4x/(2x) = 2 für alle x ≠ 0 richtig?', 'Ja, man kürzt durch 2x.', ['Nein, es kommt 2x heraus.', 'Nein, es kommt 1/2 heraus.'],
    '4x/(2x): Zähler und Nenner durch 2x teilen ergibt 2/1 = 2.', 'Kürze Zahl und x getrennt.'))
ST.neu('fehler_finden', 'direkt', SA('Ist 3/x + 2/x = 5/x richtig (für x ≠ 0)?', 'Ja: Bei gleichem Nenner addiert man nur die Zähler.', ['Nein, es ist 5/(2x).', 'Nein, es ist 6/x.'],
    '3/x + 2/x = (3 + 2)/x = 5/x. Der Nenner bleibt gleich.', 'Was passiert beim Addieren gleichnamiger Brüche mit dem Nenner?'))
ST.neu('fehler_finden', 'einkleidung', SA('Eine Torte ist in x gleiche Stücke geteilt. Anna isst 1 Stück, Ben 2 Stücke. Jemand schreibt für den gegessenen Anteil 1/x + 2/x = 3/(2x). Was stimmt?', 'Falsch: Es sind 3/x – der Nenner bleibt x.',
    ['Richtig.', 'Falsch: Es sind 2/x.', 'Falsch: Es sind 3/x².'], 'Zusammen wurden 3 von x Stücken gegessen, also 3/x. Den Nenner addiert man nicht.', 'Wie viele Stücke von wie vielen wurden gegessen?'))
ST.neu('fehler_finden', 'mehrschritt', SA('Prüfe mit x = 2: Welche Umformung kann NICHT stimmen?', '(x + 4)/(x + 2) = 4/2', ['(x² + 2x)/x = x + 2', '3/x + 1/x = 4/x', 'x/(2x) = 1/2'],
    'Für x = 2: (2 + 4)/(2 + 2) = 6/4 = 1,5, aber 4/2 = 2. Die anderen stimmen für x = 2 (4 = 4, 2 = 2, 1/2 = 1/2).', 'Setze in beide Seiten jeder Umformung 2 ein.'))
ST.neu('fehler_finden', 'darstellung', SA('Eine Tabelle zeigt für (x² + x)/x und x + 1 dieselben Werte bei x = 1, 2, 3 und 4. Gibt es ein x, für das sich die Terme trotzdem unterscheiden?', 'Ja, x = 0: Dort ist der linke Term nicht definiert.',
    ['Nein, für kein x.', 'Ja, x = −1.', 'Ja, für alle negativen x.'], '(x² + x)/x = x + 1 gilt nur für x ≠ 0. Bei x = 0 hat der rechte Term den Wert 1, der linke keinen.', 'Denk an die Definitionsmenge.'))
ST.neu('fehler_finden', 'verknuepfen', SA('Welche Umformung ist richtig?', '(x² + 2x + 1)/(x + 1) = x + 1', ['(x² + 1)/(x + 1) = x + 1', '(x² + 4)/(x + 2) = x + 2', '(x + 1)²/(x + 1) = x² + 1'],
    'x² + 2x + 1 = (x + 1)² (binomische Formel). Gekürzt durch (x + 1) bleibt x + 1. x² + 1 und x² + 4 lassen sich nicht zerlegen.', 'Welcher Zähler ist eine binomische Formel?'))
ST.knobel('fehler_finden', SA('Für welche Zahlen x stimmt die falsche „Kürzung“ (x + 3)/(x + 5) = 3/5 trotzdem?', 'nur für x = 0', ['für keine Zahl', 'für alle x ≠ −5', 'für x = 0 und x = −5'],
    'Über Kreuz: 5(x + 3) = 3(x + 5) ⇒ 5x + 15 = 3x + 15 ⇒ 2x = 0 ⇒ x = 0. Nur dort stimmt es zufällig.', 'Wann sind zwei Brüche gleich? Multipliziere über Kreuz.'))
ST.knobel('fehler_finden', SA('Jemand „kürzt“ 16/64, indem er die beiden Sechsen streicht, und erhält zufällig richtig 1/4. Bei welchem Bruch klappt dieser falsche Trick auch?', '19/95 = 1/5', ['12/24 = 1/4', '13/39 = 1/9', '15/56 = 1/6'],
    '19/95 = 1/5 stimmt wirklich (95 = 5 · 19). 12/24 = 1/2, 13/39 = 1/3, 15/56 ist nicht 1/6. Der Trick funktioniert nur in seltenen Zufällen.',
    'Rechne jeden Bruch wirklich aus und vergleiche.'))
baue = mit_stufen(baue, ST)
# ---- STUFEN ENDE ----

# ---------- TEXT: Zweiundzwanzigste Runde (18.11., Auftrag des Lehrers) – mehr Textaufgaben, siehe _text_kl8.py ----------
from _text_kl8 import Text, mit_text, text_auf_datei  # noqa: E402
TX = Text('terme.bruchterme', 22_8_3)
TZ, TA, TL, TW = TX.Z, TX.A, TX.L, TX.W

# --- definitionsmenge ---
TX.u('definitionsmenge', 'direkt', TZ('Bei einer Feier zahlen die 2 Gastgeber nichts; die anderen teilen 360 €. Jeder zahlt 360/(x − 2) Euro (x = alle Personen). Für welches x ist der Term nicht definiert?', '2',
    TW('Nenner x − 2.', 'ausgeschlossenes x.', 'Nenner = 0.', 'x − 2 = 0 ⇒ x = 2.', 'Für x = 2 ist der Term nicht definiert.'), 'Wann wird der Nenner 0?'))
TX.u('definitionsmenge', 'einkleidung', TZ('Ein Radfahrer fährt 30 km gegen den Wind, der ihn um 5 km/h bremst. Seine Fahrzeit ist 30/(v − 5) Stunden. Welches v ist ausgeschlossen?', '5',
    TW('Nenner v − 5.', 'ausgeschlossenes v.', 'Nenner = 0.', 'v = 5.', 'v = 5 km/h ist ausgeschlossen.'), 'Setze den Nenner gleich 0.', einheit='km/h'))
TX.u('definitionsmenge', 'mehrschritt', TX.A('Für Hin- und Rückweg gilt die Gesamtzeit 40/v + 40/(v − 8) Stunden. Welche Zahlen sind ausgeschlossen?', '0 und 8', ['nur 0', 'nur 8', '0 und −8'],
    TW('Nenner v und v − 8.', 'ausgeschlossene Zahlen.', 'Jeden Nenner = 0 setzen.', 'v = 0, v = 8.', 'D = ℝ \\ {0; 8}.'), 'Es gibt zwei Nenner.'))
TX.u('definitionsmenge', 'pruefung', TZ('Ein 2 m tiefer Teich wird mit zwei Pumpen geleert; die zweite braucht 3 Stunden länger. Pro Stunde schaffen sie zusammen 1/x + 1/(x + 3) des Teichs. Welche negative Zahl ist ausgeschlossen?', '-3',
    TW('Nenner x und x + 3; die Tiefe spielt keine Rolle.', 'negative ausgeschlossene Zahl.', 'Nenner = 0.', 'x + 3 = 0 ⇒ x = −3.', 'x = −3 ist ausgeschlossen.'), 'Welche Angabe gehört nicht zum Term?'), huerde='ueberfluessig')
TX.u('definitionsmenge', 'fehler', TX.A('Pro Kind kostet ein Ausflug (240 + 4x)/x Euro. Jemand sagt: „x = −60 ist ausgeschlossen, weil dann 240 + 4x = 0 ist.“ Was stimmt?',
    'Falsch: Nur der Nenner zählt; ausgeschlossen ist x = 0.', ['Richtig.', 'Falsch: x = 240 ist ausgeschlossen.', 'Falsch: Es ist nichts ausgeschlossen.'],
    TW('(240 + 4x)/x.', 'ausgeschlossene Zahl.', 'Nur der Nenner darf nicht 0 sein.', 'x = 0.', 'Die Aussage ist falsch.'), 'Darf ein Zähler 0 sein?'), huerde='entscheidung')
TX.u('definitionsmenge', 'transfer', TX.A('Eine Gruppe teilt 300 € Hüttenmiete; 4 Betreuer zahlen nichts: Jeder andere zahlt 300/(x − 4) Euro (x = alle Personen). In die Hütte passen höchstens 30 Personen. Welche Definitionsmenge ist sinnvoll?',
    '{5; 6; …; 30}', ['ℝ \\ {4}', '{4; 5; …; 30}', '{0; 1; …; 30}'],
    TW('Nenner x − 4, ganze Personen, höchstens 30.', 'D.', 'Nenner ≠ 0, mindestens ein Zahler, Obergrenze.', '5 ≤ x ≤ 30.', 'D = {5; 6; …; 30}.'), 'Welche Bedingungen gibt die Situation zusätzlich zum Nenner?'), huerde='zwei')
TX.s('definitionsmenge', TZ('Jeder zahlt 150/(x + 1) Euro. Welche Zahl ist ausgeschlossen?', '-1',
    TW('Nenner x + 1.', 'ausgeschlossene Zahl.', 'x + 1 = 0.', 'x = −1.', 'x = −1.')))
TX.s('definitionsmenge', TZ('Mit Rückenwind gilt für die Fahrzeit 50/(v + 10) Stunden. Welche Zahl ist ausgeschlossen?', '-10',
    TW('Nenner v + 10.', 'ausgeschlossene Zahl.', 'v + 10 = 0.', 'v = −10.', 'v = −10.')))
TX.k('definitionsmenge', TZ('Gegen die Strömung gilt für die Fahrzeit 24/(v − 6) Stunden. Welches v ist ausgeschlossen?', '6',
    TW('Nenner v − 6.', 'ausgeschlossenes v.', 'v − 6 = 0.', 'v = 6.', 'v = 6.')))

# --- termwert ---
TX.u('termwert', 'direkt', TZ('Ein Flyer kostet pro Stück (50 + 0,1x)/x Euro bei x Flyern. Was kostet ein Flyer bei 500 Stück?', '(50 + 0.1 * 500) / 500',
    TW('x = 500.', 'Termwert.', 'Einsetzen.', '(50 + 50) : 500 = 0,2.', 'Ein Flyer kostet 0,20 €.'), 'Setze 500 für x ein.', einheit='€'))
TX.u('termwert', 'einkleidung', TZ('Für Hin- und Rückweg gilt die Gesamtzeit 60/v + 60/(v + 20) Stunden. Wie lange dauert es bei v = 40 km/h?', '60 / 40 + 60 / 60',
    TW('v = 40.', 'Gesamtzeit.', 'Einsetzen.', '1,5 + 1 = 2,5.', 'Es dauert 2,5 Stunden.'), 'Berechne beide Brüche einzeln.', einheit='h'))
TX.u('termwert', 'mehrschritt', TZ('Zwei Kinder streichen einen Zaun. Das erste schafft 1/6, das zweite 1/x des Zauns pro Stunde. Für x = 3: Wie viele Stunden brauchen sie zusammen?', '1 / (1/6 + 1/3)',
    TW('1/6 + 1/x, x = 3.', 'Zeit zusammen.', 'Anteil pro Stunde, dann Kehrwert.', '1/6 + 2/6 = 1/2 ⇒ 2 h.', 'Zusammen brauchen sie 2 Stunden.'), 'Welcher Anteil wird zusammen in einer Stunde fertig?', einheit='h'))
TX.u('termwert', 'pruefung', TZ('Ein Kurs findet dienstags statt. Er kostet pro Person (420 + 15x)/x Euro bei x Teilnehmern. Was zahlt jeder bei 12 Personen?', '(420 + 15 * 12) / 12',
    TW('x = 12; der Wochentag spielt keine Rolle.', 'Termwert.', 'Einsetzen.', '600 : 12 = 50.', 'Jeder zahlt 50 €.'), 'Welche Angabe brauchst du nicht?', einheit='€'), huerde='ueberfluessig')
TX.u('termwert', 'transfer', TZ('Für eine Klassenfahrt gilt pro Person (600 + 8x)/x Euro. Ab wie vielen Personen sind es höchstens 20 €?', '600 / (20 - 8)',
    TW('(600 + 8x)/x ≤ 20.', 'kleinste Personenzahl.', 'Aufteilen: 600/x + 8 ≤ 20.', '600/x ≤ 12 ⇒ x ≥ 50.', 'Ab 50 Personen.'), 'Teile den Bruch in 600/x + 8 auf.'), huerde='deuten')
TX.u('termwert', 'fehler', TX.A('Der Durchschnittspreis ist (36 + 2x)/x Euro. Jemand rechnet für x = 6: „(36 + 2 · 6)/6 = 36 + 2 = 38 €.“ Was stimmt?',
    'Falsch: (36 + 12) : 6 = 8 €.', ['Richtig.', 'Falsch: 36 : 6 + 2 = 8, aber man muss mit 6 malnehmen.', 'Falsch: 48 €.'],
    TW('x = 6.', 'richtiger Wert.', 'Erst Zähler ausrechnen, dann teilen.', '48 : 6 = 8.', 'Es sind 8 €, nicht 38 €.'), 'Darf man nur den Teil 2x durch x teilen?'), huerde='entscheidung')
TX.s('termwert', TZ('Pro Stück gilt (80 + 3x)/x Euro. Berechne den Wert für x = 20.', '(80 + 3 * 20) / 20',
    TW('x = 20.', 'Termwert.', 'Einsetzen.', '140 : 20 = 7.', '7 €.'), einheit='€'))
TX.s('termwert', TZ('Die Fahrzeit für 120 km ist 120/v Stunden. Wie lange dauert es bei 80 km/h?', '120 / 80',
    TW('v = 80.', 'Termwert.', 'Einsetzen.', '1,5.', '1,5 Stunden.'), einheit='h'))
TX.k('termwert', TZ('Pro Person gilt (200 + 5x)/x Euro. Berechne den Wert für x = 40.', '(200 + 5 * 40) / 40',
    TW('x = 40.', 'Termwert.', 'Einsetzen.', '400 : 40 = 10.', '10 €.'), einheit='€'))

# --- kuerzen ---
TX.u('kuerzen', 'direkt', TX.A('Eine Rechnung über (12x + 36) € wird auf 12 Personen verteilt. Welcher gekürzte Term gibt an, was jeder zahlt?', 'x + 3', ['12x + 3', 'x + 36', 'x + 36/12x'],
    TW('(12x + 36)/12.', 'gekürzter Term.', '12 ausklammern, kürzen.', '12(x + 3)/12 = x + 3.', 'Jeder zahlt x + 3 Euro.'), 'Klammere im Zähler 12 aus.'))
TX.u('kuerzen', 'einkleidung', TZ('Ein Rechteck hat die Fläche (6x² + 9x) cm² und die Breite 3x cm. Kürze Fläche : Breite und berechne die Länge für x = 4.', '2 * 4 + 3',
    TW('(6x² + 9x)/(3x).', 'Länge bei x = 4.', '3x ausklammern, kürzen.', '2x + 3 = 11.', 'Die Länge ist 11 cm.'), 'Klammere 3x im Zähler aus.', einheit='cm'))
TX.u('kuerzen', 'mehrschritt', TX.A('Die Kosten von (5x² + 10x) € werden gleich auf 5x Personen verteilt. Was zahlt jeder?', 'x + 2 Euro', ['x² + 2 Euro', '5x + 2 Euro', 'x + 10 Euro'],
    TW('(5x² + 10x)/(5x).', 'Betrag pro Person.', '5x ausklammern, kürzen.', '5x(x + 2)/(5x) = x + 2.', 'Jeder zahlt x + 2 Euro.'), 'Welcher gemeinsame Faktor steckt in beiden Summanden?'))
TX.u('kuerzen', 'pruefung', TZ('Eine Wiese hat die Fläche (8x² + 4x) m² und die Breite 4x m. Ein Zaun kostet 12 € pro Meter. Wie lang ist die Wiese für x = 5?', '2 * 5 + 1',
    TW('(8x² + 4x)/(4x); der Zaunpreis spielt keine Rolle.', 'Länge bei x = 5.', 'Kürzen, einsetzen.', '2x + 1 = 11.', 'Die Wiese ist 11 m lang.'), 'Welche Angabe gehört nicht zur Länge?', einheit='m'), huerde='ueberfluessig')
TX.u('kuerzen', 'fehler', TX.A('Kosten von (4x + 8) € werden auf 4 Personen verteilt. Jemand kürzt: (4x + 8)/4 = x + 8. Was stimmt?',
    'Falsch: Beide Summanden durch 4 teilen – x + 2.', ['Richtig.', 'Falsch: 4x + 2.', 'Falsch: x + 4.'],
    TW('(4x + 8)/4.', 'richtiger Term.', '4 ausklammern.', '4(x + 2)/4 = x + 2.', 'Jeder zahlt x + 2 Euro.'), 'Wurde auch die 8 durch 4 geteilt?'), huerde='entscheidung')
TX.u('kuerzen', 'begruenden', TX.A('Für eine Durchschnittsgeschwindigkeit ergibt sich (2x² + 6x)/(2x) km/h. Jemand sagt: „Das ist für jedes x > 0 dasselbe wie x + 3.“ Was stimmt?',
    'Richtig: 2x ausklammern und kürzen.', ['Falsch: Es ist x² + 3.', 'Falsch: Man darf nur x² kürzen.', 'Falsch: Es ist 2x + 6.'],
    TW('(2x² + 6x)/(2x).', 'Ist x + 3 richtig?', '2x ausklammern.', '2x(x + 3)/(2x) = x + 3.', 'Die Aussage stimmt.'), 'Klammere 2x aus.'))
TX.u('kuerzen', 'transfer', TZ('Ein Becken enthält (9x² + 3x) Liter und wird mit 3x Litern pro Minute geleert. Wie viele Minuten dauert es für x = 10?', '3 * 10 + 1',
    TW('(9x² + 3x)/(3x).', 'Zeit bei x = 10.', 'Kürzen, einsetzen.', '3x + 1 = 31.', 'Es dauert 31 Minuten.'), 'Klammere 3x aus.', einheit='min'))
TX.s('kuerzen', TZ('Kosten von (10x + 20) € werden auf 10 Personen verteilt. Wie viel zahlt jeder für x = 7?', '7 + 2',
    TW('(10x + 20)/10 = x + 2.', 'Wert bei 7.', 'Kürzen, einsetzen.', '9.', '9 €.'), einheit='€'))
TX.s('kuerzen', TZ('Ein Beet hat die Fläche (4x² + 2x) m² und die Breite 2x m. Wie lang ist es für x = 3?', '2 * 3 + 1',
    TW('(4x² + 2x)/(2x) = 2x + 1.', 'Länge.', 'Kürzen, einsetzen.', '7.', '7 m.'), einheit='m'))
TX.k('kuerzen', TZ('Kosten von (6x + 18) € werden auf 6 Personen verteilt. Wie viel zahlt jeder für x = 4?', '4 + 3',
    TW('(6x + 18)/6 = x + 3.', 'Wert bei 4.', 'Kürzen, einsetzen.', '7.', '7 €.'), einheit='€'))

# --- erweitern ---
TX.u('erweitern', 'direkt', TZ('Ein Kind schafft pro Stunde 1/x eines Puzzles. Um das mit 1/(2x) zu vergleichen, erweitert man 1/x auf den Nenner 2x. Wie heißt der neue Zähler?', '2',
    TW('1/x → □/(2x).', 'neuer Zähler.', 'Mit 2 erweitern.', '1 · 2 = 2.', '2/(2x).'), 'Womit muss der Nenner x multipliziert werden?'))
TX.u('erweitern', 'einkleidung', TL('Zwei Pumpen leeren pro Stunde 1/x und 1/(3x) eines Beckens. Bringe beide Anteile auf den Nenner 3x.', '□/(3x) und □/(3x)', ['3', '1'],
    TW('1/x und 1/(3x).', 'Zähler beim Nenner 3x.', '1/x mit 3 erweitern.', '3/(3x) und 1/(3x).', 'Die Zähler sind 3 und 1.'), 'Der zweite Bruch hat den Nenner schon.'))
TX.u('erweitern', 'mehrschritt', TZ('Die Hinfahrt dauert 30/x Stunden, die Rückfahrt 45/(2x) Stunden. Erweitere 30/x auf den Nenner 2x. Wie heißt der neue Zähler?', '30 * 2',
    TW('30/x → □/(2x).', 'neuer Zähler.', 'Mit 2 erweitern.', '30 · 2 = 60.', '60/(2x).'), 'Zähler und Nenner mit derselben Zahl multiplizieren.'))
TX.u('erweitern', 'umkehr', TZ('Ein Anteil wurde vom Nenner 2x auf den Nenner 6x erweitert und lautet jetzt 18/(6x). Wie hieß der Zähler vorher?', '18 / 3',
    TW('□/(2x) = 18/(6x).', 'alter Zähler.', 'Es wurde mit 3 erweitert; zurückrechnen.', '18 : 3 = 6.', 'Der Anteil war 6/(2x).'), 'Womit wurde erweitert?'))
TX.u('erweitern', 'pruefung', TX.A('Pumpe A leert pro Stunde 1/(4x), Pumpe B 1/(6x) eines 50-m³-Beckens. Auf welchen kleinsten gemeinsamen Nenner bringt man beide Anteile?', '12x', ['24x', '10x', '24x²'],
    TW('Nenner 4x und 6x; das Volumen spielt keine Rolle.', 'kleinster gemeinsamer Nenner.', 'kgV von 4 und 6, mal x.', 'kgV(4; 6) = 12.', 'Hauptnenner 12x.'), 'Welche Angabe brauchst du nicht?'), huerde='ueberfluessig')
TX.u('erweitern', 'begruenden', TX.A('Ein Kind liest pro Tag 3/(4x) eines Buches. Jemand sagt: „Erweitert man 3/(4x) mit 5, liest es mehr pro Tag.“ Was stimmt?',
    'Falsch: 15/(20x) ist derselbe Anteil; nur die Darstellung ändert sich.', ['Richtig: 15 ist größer als 3.', 'Falsch: Es liest dann weniger.', 'Richtig: fünfmal so viel.'],
    TW('3/(4x) = 15/(20x).', 'Ändert sich der Wert?', 'Erweitern: Zähler und Nenner mal 5.', 'Wert bleibt gleich.', 'Die Aussage ist falsch.'), 'Was passiert beim Erweitern mit dem Wert?'), huerde='entscheidung')
TX.s('erweitern', TZ('Ein Kind liest pro Tag 2/(3x) eines Buches. Schreibe den Anteil mit dem Nenner 12x. Wie heißt der Zähler?', '2 * 4',
    TW('2/(3x) → □/(12x).', 'Zähler.', 'Mit 4 erweitern.', '8.', '8/(12x).')))
TX.s('erweitern', TZ('Eine Pumpe leert pro Stunde 1/(5x) eines Beckens. Schreibe den Anteil mit dem Nenner 10x. Wie heißt der Zähler?', '1 * 2',
    TW('1/(5x) → □/(10x).', 'Zähler.', 'Mit 2 erweitern.', '2.', '2/(10x).')))
TX.k('erweitern', TZ('Ein Garten wird pro Woche zu 3/(2x) umgegraben. Schreibe den Anteil mit dem Nenner 8x. Wie heißt der Zähler?', '3 * 4',
    TW('3/(2x) → □/(8x).', 'Zähler.', 'Mit 4 erweitern.', '12.', '12/(8x).')))

# --- addieren ---
TX.u('addieren', 'direkt', TX.A('Zwei Pumpen leeren pro Stunde 1/x und 2/x eines Beckens. Welchen Anteil schaffen sie zusammen?', '3/x', ['3/(2x)', '2/x²', '3/x²'],
    TW('1/x + 2/x.', 'Summe.', 'Gleicher Nenner: Zähler addieren.', '3/x.', 'Zusammen 3/x pro Stunde.'), 'Die Nenner sind gleich.'))
TX.u('addieren', 'einkleidung', TZ('Der Hinweg dauert 12/v Stunden, der Rückweg mit Rückenwind 12/(v + 2) Stunden. Wie lange dauert beides für v = 4?', '12 / 4 + 12 / 6',
    TW('v = 4.', 'Gesamtzeit.', 'Einsetzen und addieren.', '3 + 2 = 5.', 'Insgesamt 5 Stunden.'), 'Berechne beide Brüche.', einheit='h'))
TX.u('addieren', 'mehrschritt', TX.A('Pumpe A leert pro Stunde 1/x, Pumpe B 1/(2x) eines Beckens. Welchen Anteil schaffen beide zusammen?', '3/(2x)', ['2/(3x)', '2/(2x)', '1/(3x)'],
    TW('1/x + 1/(2x).', 'Summe.', 'Hauptnenner 2x.', '2/(2x) + 1/(2x) = 3/(2x).', 'Zusammen 3/(2x).'), 'Bringe beide auf den Nenner 2x.'))
TX.u('addieren', 'pruefung', TZ('Zwei Rohre füllen einen 3 000-l-Tank. Rohr A allein braucht 6 h, Rohr B allein 12 h. Wie viele Stunden brauchen beide zusammen?', '1 / (1/6 + 1/12)',
    TW('1/6 + 1/12 pro Stunde; das Volumen spielt keine Rolle.', 'Zeit zusammen.', 'Anteile addieren, Kehrwert.', '2/12 + 1/12 = 3/12 = 1/4 ⇒ 4 h.', 'Zusammen brauchen sie 4 Stunden.'), 'Welche Angabe brauchst du nicht?', einheit='h'), huerde='ueberfluessig')
TX.u('addieren', 'transfer', TZ('Ein Radfahrer fährt 30 km mit v km/h hin und wegen Gegenwind mit (v − 5) km/h zurück: 30/v + 30/(v − 5) Stunden. Wie viele Minuten ist er für v = 15 unterwegs?', '(30 / 15 + 30 / 10) * 60',
    TW('v = 15.', 'Gesamtzeit in Minuten.', 'Einsetzen, addieren, umrechnen.', '2 + 3 = 5 h = 300 min.', 'Er ist 300 Minuten unterwegs.'), 'Achte auf die Einheit.', einheit='min'), huerde='deuten')
TX.u('addieren', 'fehler', TX.A('Zwei Pumpen schaffen pro Stunde 1/x und 1/(2x) eines Beckens. Jemand rechnet: 1/x + 1/(2x) = 2/(3x). Was stimmt?',
    'Falsch: Nenner nicht addieren – 2/(2x) + 1/(2x) = 3/(2x).', ['Richtig.', 'Falsch: 2/(2x).', 'Falsch: 1/(3x).'],
    TW('1/x + 1/(2x).', 'Fehler.', 'Hauptnenner bilden.', '3/(2x).', 'Richtig ist 3/(2x).'), 'Darf man Nenner addieren?'), huerde='entscheidung')
TX.s('addieren', TZ('Hinweg 20/v Stunden, Rückweg 20/v Stunden. Wie lange insgesamt bei v = 8?', '40 / 8',
    TW('20/v + 20/v = 40/v.', 'Wert bei 8.', 'Addieren, einsetzen.', '5.', '5 Stunden.'), einheit='h'))
TX.s('addieren', TZ('Zwei Maler schaffen pro Tag 1/4 und 1/12 eines Hauses. Wie viele Tage brauchen sie zusammen?', '1 / (1/4 + 1/12)',
    TW('1/4 + 1/12.', 'Tage.', 'Addieren, Kehrwert.', '4/12 = 1/3 ⇒ 3.', '3 Tage.'), einheit='Tage'))
TX.k('addieren', TZ('Zwei Hähne füllen eine Wanne allein in 10 bzw. 15 Minuten. Wie viele Minuten brauchen beide zusammen?', '1 / (1/10 + 1/15)',
    TW('1/10 + 1/15.', 'Zeit.', 'Addieren, Kehrwert.', '5/30 = 1/6 ⇒ 6.', '6 Minuten.'), einheit='min'))

# --- multiplizieren ---
TX.u('multiplizieren', 'direkt', TZ('Ein Stoff kostet 24/x Euro pro Meter. Man kauft x/3 Meter. Was kostet das?', '24 / 3',
    TW('(24/x) · (x/3).', 'Preis.', 'Multiplizieren, x kürzen.', '24x/(3x) = 8.', 'Es kostet 8 €.'), 'Multipliziere Zähler mit Zähler, Nenner mit Nenner.', einheit='€'))
TX.u('multiplizieren', 'einkleidung', TZ('Ein Zug fährt 90/x km pro Minute, und zwar 2x Minuten lang. Wie weit fährt er?', '90 * 2',
    TW('(90/x) · 2x.', 'Strecke.', 'Multiplizieren, kürzen.', '180x/x = 180.', 'Er fährt 180 km.'), 'Strecke = Geschwindigkeit · Zeit.', einheit='km'))
TX.u('multiplizieren', 'mehrschritt', TZ('Ein Rechteck ist 6x/5 m lang und 10/(3x) m breit. Wie groß ist seine Fläche?', '6 * 10 / (5 * 3)',
    TW('(6x/5) · (10/(3x)).', 'Fläche.', 'Multiplizieren, kürzen.', '60x/(15x) = 4.', 'Die Fläche ist 4 m².'), 'Was kürzt sich weg?', einheit='m²'))
TX.u('multiplizieren', 'pruefung', TZ('Ein Drucker druckt 60/x Seiten pro Sekunde, und zwar 5x/2 Sekunden lang. Das Papier wiegt 80 g pro m². Wie viele Seiten druckt er?', '60 * 5 / 2',
    TW('(60/x) · (5x/2); das Papiergewicht spielt keine Rolle.', 'Seitenzahl.', 'Multiplizieren, kürzen.', '300x/(2x) = 150.', 'Er druckt 150 Seiten.'), 'Welche Angabe brauchst du nicht?'), huerde='ueberfluessig')
TX.u('multiplizieren', 'fehler', TX.A('Ein Saft kostet 4/x Euro pro Liter, man kauft x/2 Liter. Jemand rechnet: (4/x) · (x/2) = 4x/(2x²) = 2/x. Was stimmt?',
    'Falsch: x · 2 ist kein x²; richtig ist 4x/(2x) = 2 €.', ['Richtig.', 'Falsch: 2x €.', 'Falsch: 8 €.'],
    TW('(4/x) · (x/2).', 'richtiges Ergebnis.', 'Nenner x · 2 = 2x.', '4x/(2x) = 2.', 'Es kostet 2 €.'), 'Was ergibt x · 2 im Nenner?'), huerde='entscheidung')
TX.u('multiplizieren', 'begruenden', TX.A('Ein Radfahrer fährt 36/x km pro Minute genau x Minuten lang. Jemand sagt: „Wie weit er kommt, hängt von x ab.“ Was stimmt?',
    'Falsch: (36/x) · x = 36 km, für jedes x.', ['Richtig: Je größer x, desto weiter.', 'Richtig: Je größer x, desto kürzer.', 'Falsch: Er kommt 36x km weit.'],
    TW('(36/x) · x.', 'Abhängig von x?', 'Kürzen.', '36.', 'Er fährt immer 36 km.'), 'Was kürzt sich?'), huerde='entscheidung')
TX.u('multiplizieren', 'transfer', TZ('Ein Becken wird erst 2x/3 Minuten lang mit 300/x Litern pro Minute gefüllt, danach 4 Minuten mit 50 Litern pro Minute. Wie viele Liter sind dann darin?', '300 * 2 / 3 + 50 * 4',
    TW('(300/x) · (2x/3) + 50 · 4.', 'Gesamtmenge.', 'Beide Abschnitte berechnen, addieren.', '200 + 200 = 400.', 'Es sind 400 Liter darin.'), 'Rechne die beiden Abschnitte getrennt.', einheit='l'), huerde='zwei')
TX.s('multiplizieren', TZ('Ein Stoff kostet 10/x Euro pro Meter, man kauft x/2 Meter. Was kostet das?', '10 / 2',
    TW('(10/x) · (x/2).', 'Preis.', 'Kürzen.', '5.', '5 €.'), einheit='€'))
TX.s('multiplizieren', TZ('Ein Beet ist 9x/4 m lang und 8/(3x) m breit. Wie groß ist die Fläche?', '9 * 8 / (4 * 3)',
    TW('(9x/4) · (8/(3x)).', 'Fläche.', 'Kürzen.', '72/12 = 6.', '6 m².'), einheit='m²'))
TX.k('multiplizieren', TZ('Käse kostet 18/x Euro pro kg, man kauft x/6 kg. Was kostet das?', '18 / 6',
    TW('(18/x) · (x/6).', 'Preis.', 'Kürzen.', '3.', '3 €.'), einheit='€'))

# --- fehler_finden ---
TX.u('fehler_finden', 'erkennen', TX.A('Zwei Pumpen leeren pro Stunde 2/x und 3/x eines Beckens. Welche Rechnung für den gemeinsamen Anteil stimmt?', '2/x + 3/x = 5/x', ['2/x + 3/x = 5/(2x)', '2/x + 3/x = 6/x', '2/x + 3/x = 5/x²'],
    TW('2/x + 3/x.', 'richtige Rechnung.', 'Gleicher Nenner bleibt.', '5/x.', '5/x ist richtig.'), 'Was passiert mit dem Nenner bei gleichnamigen Brüchen?'))
TX.u('fehler_finden', 'einkleidung', TX.A('Kosten von (30 + 6x) € werden auf 6 Personen verteilt. Jemand kürzt: (30 + 6x)/6 = 30 + x. Was stimmt?',
    'Falsch: Jeder Summand wird geteilt – 5 + x.', ['Richtig.', 'Falsch: 5 + 6x.', 'Falsch: 36x : 6 = 6x.'],
    TW('(30 + 6x)/6.', 'richtiger Term.', '6 ausklammern.', '6(5 + x)/6 = 5 + x.', 'Jeder zahlt 5 + x Euro.'), 'Wurde die 30 auch durch 6 geteilt?'))
TX.u('fehler_finden', 'mehrschritt', TZ('Jemand rechnet die Gesamtzeit für Hin- und Rückweg 10/v + 10/v bei v = 5 so: „10/10 = 1 Stunde.“ Wie viele Stunden sind es richtig?', '10 / 5 + 10 / 5',
    TW('10/v + 10/v = 20/v, v = 5.', 'richtige Zeit.', 'Zähler addieren, Nenner bleibt.', '2 + 2 = 4.', 'Es sind 4 Stunden.'), 'Was passiert beim Addieren mit dem Nenner?', einheit='h'))
TX.u('fehler_finden', 'pruefung', TX.A('Ein Radfahrer (Rad 12 kg) fährt 24 km mit v km/h hin und mit (v + 4) km/h zurück. Jemand schreibt für die Gesamtzeit 48/(2v + 4). Was stimmt?',
    'Falsch: Brüche nicht durch Addieren von Zählern und Nennern zusammenfassen; richtig ist 24/v + 24/(v + 4).', ['Richtig.', 'Falsch: 48/(v + 4).', 'Falsch: 24/(2v + 4).'],
    TW('24/v + 24/(v + 4); das Radgewicht spielt keine Rolle.', 'Fehler.', 'Probe mit v = 4: 6 + 3 = 9; 48/12 = 4.', 'Die Werte stimmen nicht überein.', 'Die Umformung ist falsch.'), 'Mache eine Probe mit einer Zahl.'), huerde='ueberfluessig')
TX.u('fehler_finden', 'transfer', TZ('Jemand rechnet die Kosten pro Person (200 + 10x)/x bei 25 Personen so: „200 + 10 = 210 €.“ Wie viel Euro sind es richtig?', '(200 + 10 * 25) / 25',
    TW('x = 25.', 'richtiger Wert.', 'Einsetzen, dann teilen.', '450 : 25 = 18.', 'Es sind 18 € pro Person.'), 'Darf man x einfach wegkürzen?', einheit='€'), huerde='deuten')
TX.u('fehler_finden', 'verknuepfen', TX.A('Maler A braucht allein 6 Stunden für eine Wand, Maler B 3 Stunden. Jemand sagt: „Zusammen brauchen sie 6 + 3 = 9 Stunden.“ Was stimmt?',
    'Falsch: 1/6 + 1/3 = 1/2 pro Stunde – zusammen 2 Stunden.', ['Richtig.', 'Falsch: 4,5 Stunden.', 'Falsch: 3 Stunden.'],
    TW('1/6 + 1/3 pro Stunde.', 'Zeit zusammen.', 'Anteile addieren, Kehrwert.', '1/6 + 2/6 = 1/2 ⇒ 2 h.', 'Zusammen 2 Stunden.'), 'Werden zwei Maler langsamer als einer?'), huerde='entscheidung')
TX.s('fehler_finden', TZ('Ein Stoff kostet 12/x Euro pro Meter, man kauft x/4 Meter. Jemand rechnet 12/(4x). Was kostet es richtig?', '12 / 4',
    TW('(12/x) · (x/4).', 'Preis.', 'Kürzen.', '3.', '3 €.'), einheit='€'))
TX.s('fehler_finden', TZ('Kosten von (8x + 16) € werden auf 8 Personen verteilt. Jemand kürzt zu x + 16. Was zahlt jeder richtig für x = 3?', '3 + 2',
    TW('(8x + 16)/8 = x + 2.', 'Wert bei 3.', 'Richtig kürzen, einsetzen.', '5.', '5 €.'), einheit='€'))
TX.k('fehler_finden', TZ('Zwei Pumpen schaffen je 1/4 eines Beckens pro Stunde. Jemand rechnet 1/4 + 1/4 = 2/8. Welcher Anteil ist es richtig (als Dezimalzahl)?', '1/4 + 1/4',
    TW('1/4 + 1/4.', 'Summe.', 'Zähler addieren.', '2/4 = 0,5.', '0,5, also die Hälfte.')))
baue = mit_text(baue, TX)
# ---- TEXT ENDE ----

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Grundlagen', ['definitionsmenge', 'termwert']), ('Kürzen und Erweitern', ['kuerzen', 'erweitern']),
          ('Rechnen', ['addieren', 'multiplizieren', 'fehler_finden'])],
         'Bruchterme verstehen: Definitionsmenge bestimmen, Werte berechnen, kürzen, erweitern und mit Bruchtermen rechnen.',
         ['Nenner darf nie 0 sein: Diese Zahlen fehlen in D.', 'Kürzen nur aus Produkten, nie aus Summen.',
          'Addieren: erst gleichnamig machen. Multiplizieren: Zähler · Zähler, Nenner · Nenner. Dividieren: mal Kehrbruch.'],
         offen=['Bruch-Ergebnisse jetzt teils als Lücken (□/□, □/(□x), □x²/□); Ergebnisse mit Klammer-Faktoren (z. B. 5/(7(x + 1))) bleiben Auswahl, '
                'weil die Lückenfelder nur ganze Zahlen aufnehmen.',
                'Vorschlag aus der Prüfung (Anknüpfen an Zahlenbrüche aus Klasse 6) ist in der Regel der Karte „addieren“ umgesetzt.'])
