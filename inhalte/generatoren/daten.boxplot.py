#!/usr/bin/env python3
"""Thema daten.boxplot – Median, Quartile, Boxplot (Gymnasium Bayern, Klasse 7)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl7 import A, L, Z, baue, zt  # noqa: E402

META = {'thema_schluessel': 'daten.boxplot', 'thema_id': 95, 'block_id': 111, 'klasse': {'gym_by': 7, 'rs_by': 7}}


def median(xs):
    s = sorted(xs); n = len(s)
    return Fr(s[n // 2]) if n % 2 else Fr(s[n // 2 - 1] + s[n // 2], 2)


def quartile(xs):
    """Q1/Q3 als Median der unteren/oberen Hälfte (bei ungerader Anzahl ohne den Median)."""
    s = sorted(xs); n = len(s)
    return median(s[:n // 2]), median(s[(n + 1) // 2:])


def liste(xs): return '; '.join(zt(x) for x in xs)


def tab5(werte, titel=''):
    mn, q1, me, q3, mx = werte
    return {'typ': 'tabelle', 'kopf': ([titel] if titel else []) + ['Minimum', 'unteres Quartil', 'Median', 'oberes Quartil', 'Maximum'],
            'zeilen': [([''] if titel else []) + [zt(mn), zt(q1), zt(me), zt(q3), zt(mx)]]}


ETAPPEN = [
    {'lernziel': 'median', 'titel': 'Den Median bestimmen',
     'regel': 'Der ⟦Median⟧ (Zentralwert) ist der Wert in der ⟦Mitte der geordneten Liste⟧. Bei einer geraden Anzahl nimmt man den ⟦Mittelwert der beiden mittleren⟧ Werte.',
     'schritte': ['Werte: 7; 3; 9; 4; 12; 5', 'Geordnet: 3; 4; 5; 7; 9; 12 (6 Werte)', 'Median = (5 + 7) : 2 = ⟦6⟧'],
     'fehler': 'Der Median von 7; 3; 9; 4; 12 ist nicht 9 (der mittlere Wert der ⟦ungeordneten⟧ Liste). Erst ordnen: 3; 4; 7; 9; 12 → Median 7.',
     '_verbot': ['7; 3; 9; 4; 12; 5']},
    {'lernziel': 'kennwerte', 'titel': 'Modalwert, Spannweite, Mittelwert',
     'regel': '⟦Modalwert⟧: der häufigste Wert. ⟦Spannweite⟧: größter minus kleinster Wert. ⟦Arithmetisches Mittel⟧: Summe aller Werte geteilt durch ihre Anzahl.',
     'schritte': ['Werte: 2; 5; 5; 6; 12', 'Modalwert 5, Spannweite 12 − 2 = 10', 'Mittel: 30 : 5 = ⟦6⟧'],
     'fehler': 'Die Spannweite von 2; 5; 5; 6; 12 ist nicht 12. Es ist der ⟦Abstand⟧ zwischen größtem und kleinstem Wert: 12 − 2 = 10.',
     'bild': {'typ': 'saeulen', 'einheit': 'Anzahl', 'werte': [{'name': '2', 'wert': 1}, {'name': '5', 'wert': 2}, {'name': '6', 'wert': 1}, {'name': '12', 'wert': 1}], 'zahlen': True},
     '_verbot': ['2; 5; 5; 6; 12']},
    {'lernziel': 'quartile', 'titel': 'Quartile bestimmen',
     'regel': 'Der Median teilt die geordnete Liste in eine untere und eine obere Hälfte. Das ⟦untere Quartil⟧ ist der Median der unteren Hälfte, das ⟦obere Quartil⟧ der Median der oberen Hälfte. Bei ungerader Anzahl gehört der Median ⟦zu keiner Hälfte⟧.',
     'schritte': ['Geordnet: 1; 3; 4; 6; 8; 9; 11', 'Median 6. Untere Hälfte 1; 3; 4 → Q₁ = 3', 'Obere Hälfte 8; 9; 11 → ⟦Q₃ = 9⟧. Quartilsabstand 9 − 3 = 6'],
     'fehler': 'Das untere Quartil ist nicht „ein Viertel vom größten Wert“. Es ist der Wert, unter dem etwa ⟦ein Viertel der Daten⟧ liegt.',
     '_verbot': ['1; 3; 4; 6; 8; 9; 11']},
    {'lernziel': 'boxplot', 'titel': 'Informationen aus Boxplots',
     'regel': 'Ein ⟦Boxplot⟧ zeigt die fünf Kennwerte Minimum, unteres Quartil, Median, oberes Quartil, Maximum. In der ⟦Box⟧ (zwischen den Quartilen) liegt etwa die ⟦Hälfte⟧ der Daten, in jeder ⟦Antenne⟧ und jeder Boxhälfte etwa ein ⟦Viertel⟧.',
     'schritte': ['Kennwerte: 12 | 18 | 23 | 30 | 41', 'Spannweite 41 − 12 = 29, Quartilsabstand 30 − 18 = 12', 'Etwa ⟦75 %⟧ der Werte liegen unter 30.'],
     'fehler': 'Eine längere Antenne bedeutet nicht mehr Werte: In jeder Antenne liegt etwa ⟦ein Viertel⟧ der Daten, nur ⟦weiter gestreut⟧.',
     'bild': tab5([12, 18, 23, 30, 41]),
     '_verbot': ['12 | 18 | 23 | 30 | 41']},
    {'lernziel': 'mittel_median', 'titel': 'Mittelwert und Median vergleichen',
     'regel': 'Der ⟦Mittelwert⟧ reagiert stark auf ⟦Ausreißer⟧ (einzelne extreme Werte), der ⟦Median⟧ kaum. Bei Ausreißern beschreibt der Median die „typische Mitte“ meist besser.',
     'schritte': ['Taschengeld (€): 10; 12; 12; 15; 101', 'Mittelwert: 150 : 5 = 30 €; Median: 12 €', 'Der ⟦Median⟧ passt besser – vier von fünf bekommen höchstens 15 €.'],
     'fehler': 'Der Mittelwert 30 € ist nicht „das, was die meisten bekommen“: Ein einziger großer Wert (101 €) ⟦zieht ihn nach oben⟧.',
     '_verbot': ['10; 12; 12; 15; 101']},
    {'lernziel': 'vergleichen', 'titel': 'Datensätze vergleichen und beurteilen',
     'regel': 'Vergleiche zuerst die ⟦Mitte⟧ (Median), dann die ⟦Streuung⟧ (Spannweite, Quartilsabstand). Eine Aussage über „die meisten“ oder „ein Viertel“ prüfst du mit den Quartilen.',
     'schritte': ['Klasse A: Median 24 s, Quartilsabstand 4 s. Klasse B: Median 22 s, Quartilsabstand 9 s.', 'B ist in der Mitte schneller (kleinere Zeit), streut aber stärker.',
                  'Aussage „In A sind die Zeiten einheitlicher“: ⟦richtig⟧.'],
     'fehler': 'Eine größere Spannweite heißt nicht, dass die Gruppe insgesamt besser oder schlechter ist. Sie sagt nur etwas über die ⟦Streuung⟧ aus.',
     'bild': {'typ': 'tabelle', 'kopf': ['', 'Min', 'Q₁', 'Median', 'Q₃', 'Max'], 'zeilen': [['Klasse A', '19', '22', '24', '26', '31'], ['Klasse B', '15', '18', '22', '27', '35']]}},
]


def daten(R, n, lo=1, hi=30):
    return [R.randint(lo, hi) for _ in range(n)]


def g_median(R, st):
    n = R.choice({1: [5, 7, 9], 2: [6, 8, 10, 11], 3: [12, 14, 15, 16]}[st])
    kontext, lo, hi = R.choice([('Punkte in einem Test (höchstens 30)', 0, 30), ('Tore pro Spiel', 0, 6), ('Minuten Schulweg', 3, 45),
                                ('Seiten gelesen pro Tag', 2, 60), ('Liegestütze', 4, 40), ('Körpergröße in cm', 138, 176)])
    xs = daten(R, n, lo, hi)
    m = median(xs); s = sorted(xs)
    weg = f'Geordnet: {liste(s)}. ' + (f'Mittlerer ({n // 2 + 1}.) Wert: {zt(m)}.' if n % 2 else f'Mittlere Werte {zt(s[n // 2 - 1])} und {zt(s[n // 2])}: ({zt(s[n // 2 - 1])} + {zt(s[n // 2])}) : 2 = {zt(m)}.')
    a = Z(f'{kontext}: {liste(xs)}. Bestimme den Median.', m, f'{s[n // 2]}' if n % 2 else f'({s[n // 2 - 1]} + {s[n // 2]}) / 2', weg,
          'Ordne die Werte zuerst der Größe nach.')
    return a


def g_kennwerte(R, st):
    n = R.choice([5, 6, 7, 8, 10])
    while True:
        xs = daten(R, n, 1, 25)
        mod = max(set(xs), key=xs.count)
        if [xs.count(v) for v in set(xs)].count(xs.count(mod)) == 1 and xs.count(mod) > 1: break
    welches = R.choice({1: ['Modalwert', 'Spannweite'], 2: ['Spannweite', 'Mittelwert', 'Modalwert'], 3: ['Mittelwert', 'fehlend']}[st])
    if welches == 'Modalwert':
        return Z(f'Werte: {liste(xs)}. Bestimme den Modalwert.', mod, f'{mod}', f'{zt(mod)} kommt {xs.count(mod)}-mal vor, öfter als jeder andere Wert.', 'Welcher Wert kommt am häufigsten vor?')
    if welches == 'Spannweite':
        return Z(f'Werte: {liste(xs)}. Bestimme die Spannweite.', max(xs) - min(xs), f'{max(xs)} - {min(xs)}', f'Größter Wert {max(xs)}, kleinster {min(xs)}: {max(xs)} − {min(xs)} = {max(xs) - min(xs)}.',
                 'Größter minus kleinster Wert.')
    if welches == 'Mittelwert':
        mw = Fr(sum(xs), n)
        if mw.denominator not in (1, 2, 4, 5, 8, 10): return g_kennwerte(R, st)
        return Z(f'Werte: {liste(xs)}. Berechne das arithmetische Mittel.', mw, f'({" + ".join(map(str, xs))}) / {n}', f'Summe {sum(xs)}, Anzahl {n}: {sum(xs)} : {n} = {zt(mw)}.',
                 'Alle Werte addieren und durch ihre Anzahl teilen.')
    mw = R.randint(8, 20); k = n - 1
    teil = daten(R, k, 1, 25)
    fehl = mw * n - sum(teil)
    if fehl < 0 or fehl > 60: return g_kennwerte(R, st)
    return Z(f'Von {n} Werten kennt man {k}: {liste(teil)}. Das arithmetische Mittel aller {n} Werte ist {mw}. Wie groß ist der fehlende Wert?', fehl, f'{mw} * {n} - ({" + ".join(map(str, teil))})',
             f'Summe aller Werte: {mw} · {n} = {mw * n}. Bekannte Summe {sum(teil)}. Fehlender Wert: {mw * n} − {sum(teil)} = {fehl}.', 'Mittelwert · Anzahl = Summe.')


def g_quartile(R, st):
    n = R.choice({1: [7, 11], 2: [8, 9, 10, 12], 3: [13, 15, 16]}[st])
    xs = sorted(daten(R, n, 1, 50)) if st == 1 else daten(R, n, 1, 50)
    q1, q3 = quartile(xs); s = sorted(xs)
    welches = R.choice({1: ['Q₁', 'Q₃'], 2: ['Q₁', 'Q₃', 'Abstand'], 3: ['Abstand', 'Q₁', 'Q₃']}[st])
    unten, oben = s[:n // 2], s[(n + 1) // 2:]
    weg = f'Geordnet: {liste(s)}. Untere Hälfte {liste(unten)} → Q₁ = {zt(q1)}; obere Hälfte {liste(oben)} → Q₃ = {zt(q3)}.'
    if welches == 'Abstand':
        return Z(f'Werte: {liste(xs)}. Bestimme den Quartilsabstand Q₃ − Q₁.', q3 - q1, f'{q3.numerator}/{q3.denominator} - {q1.numerator}/{q1.denominator}', weg + f' Abstand {zt(q3 - q1)}.',
                 'Erst ordnen, dann die Hälften bilden, dann jeweils den Median.')
    q = q1 if welches == 'Q₁' else q3
    name = 'untere' if welches == 'Q₁' else 'obere'
    return Z(f'Werte: {liste(xs)}. Bestimme das {name} Quartil.', q, f'{q.numerator}/{q.denominator}', weg,
             f'Bilde die {name} Hälfte (ohne den Median, falls die Anzahl ungerade ist) und bestimme ihren Median.')


def fuenf(R, lo=0, k=1):
    mn = lo + k * R.randint(0, 10)
    q1 = mn + k * R.randint(2, 12); me = q1 + k * R.randint(1, 10); q3 = me + k * R.randint(1, 12); mx = q3 + k * R.randint(2, 20)
    return [mn, q1, me, q3, mx]


def g_boxplot(R, st):
    kontext, lo, k = R.choice([('Körpergröße in cm', 135, 1), ('Punkte im Test', 0, 1), ('Weitsprung in cm', 220, 5), ('Wartezeit in min', 0, 1), ('Taschengeld in €', 5, 1)])
    w = fuenf(R, lo, k)
    gr = tab5(w)
    if st == 1:
        was = R.choice(['Spannweite', 'Quartilsabstand', 'Median'])
        val = {'Spannweite': w[4] - w[0], 'Quartilsabstand': w[3] - w[1], 'Median': w[2]}[was]
        c = {'Spannweite': f'{w[4]} - {w[0]}', 'Quartilsabstand': f'{w[3]} - {w[1]}', 'Median': f'{w[2]}'}[was]
        a = Z(f'Kennwerte eines Boxplots ({kontext}): Minimum {w[0]}, unteres Quartil {w[1]}, Median {w[2]}, oberes Quartil {w[3]}, Maximum {w[4]}. Gib {"den" if was != "Spannweite" else "die"} {was} an.',
              val, c, {'Spannweite': f'Maximum − Minimum = {w[4]} − {w[0]} = {val}.', 'Quartilsabstand': f'Q₃ − Q₁ = {w[3]} − {w[1]} = {val}.', 'Median': f'Der Strich in der Box: {val}.'}[was],
              'Spannweite: ganze Länge. Quartilsabstand: Länge der Box.')
    elif st == 2:
        frage, proz = R.choice([(f'unter {w[2]}', 50), (f'über {w[3]}', 25), (f'zwischen {w[1]} und {w[3]}', 50), (f'unter {w[1]}', 25), (f'unter {w[3]}', 75), (f'über {w[1]}', 75)])
        a = Z(f'Kennwerte eines Boxplots ({kontext}): Minimum {w[0]}, unteres Quartil {w[1]}, Median {w[2]}, oberes Quartil {w[3]}, Maximum {w[4]}. Etwa wie viel Prozent der Werte liegen {frage}?',
              proz, f'{proz}', f'Quartile und Median teilen die Daten in Viertel. {frage[0].upper() + frage[1:]} liegen etwa {proz} %.', 'Jeder der vier Abschnitte enthält etwa ein Viertel der Daten.', '%')
    else:
        n = R.choice([20, 40, 60, 80, 100, 120, 200])
        frage, anteil = R.choice([(f'über {w[3]}', Fr(1, 4)), (f'zwischen {w[1]} und {w[3]}', Fr(1, 2)), (f'unter {w[1]}', Fr(1, 4)), (f'über {w[1]}', Fr(3, 4))])
        a = Z(f'{n} Personen wurden befragt ({kontext}). Kennwerte: Minimum {w[0]}, unteres Quartil {w[1]}, Median {w[2]}, oberes Quartil {w[3]}, Maximum {w[4]}. Etwa wie viele Personen liegen {frage}?',
              anteil * n, f'{n} * {anteil.numerator} / {anteil.denominator}', f'{frage[0].upper() + frage[1:]} liegt etwa {zt(anteil * 100)} % der Daten: {zt(anteil * 100)} % von {n} = {zt(anteil * n)}.',
              'Welcher Anteil (Viertel, Hälfte, drei Viertel) ist gemeint?')
    a['f']['grafik'] = gr
    return a


def g_mittel_median(R, st):
    n = R.choice([5, 6, 7])
    while True:
        xs = daten(R, n - 1, 8, 20)
        aus = R.choice([60, 75, 90, 120, 150]) if R.random() < .7 else R.randint(0, 2)
        xs = xs + [aus]
        mw, me = Fr(sum(xs), n), median(xs)
        if mw.denominator in (1, 2, 4, 5) and abs(mw - me) >= 3: break
    R.shuffle(xs)
    if st == 1:
        return Z(f'Werte: {liste(xs)}. Berechne den Mittelwert.', mw, f'({" + ".join(map(str, xs))}) / {n}', f'Summe {sum(xs)} : {n} = {zt(mw)}.', 'Summe durch Anzahl.')
    if st == 2:
        return Z(f'Werte: {liste(xs)}. Um wie viel unterscheiden sich Mittelwert und Median? (größerer minus kleinerer Wert)', abs(mw - me),
                 f'abs(({" + ".join(map(str, xs))}) / {n} - {me.numerator}/{me.denominator})', f'Mittelwert {zt(mw)}, Median {zt(me)} (geordnet: {liste(sorted(xs))}). Unterschied {zt(abs(mw - me))}.',
                 'Berechne beide Werte. Für den Median zuerst ordnen.')
    r = 'Der Median, weil der Ausreißer den Mittelwert stark verschiebt.'
    return A(R, f'Werte: {liste(xs)}. Welcher Wert beschreibt die typische Mitte besser?', r,
             ['Der Mittelwert, weil er alle Werte berücksichtigt.', 'Beide sind gleich gut, sie sind ja gleich groß.', 'Die Spannweite, weil sie alle Werte umfasst.'],
             f'Mittelwert {zt(mw)}, Median {zt(me)}. Der Wert {aus} ist ein Ausreißer und verschiebt den Mittelwert.', 'Gibt es einen Wert, der weit von den anderen entfernt ist?')


def g_vergleichen(R, st):
    while True:
        a_, b_ = fuenf(R), fuenf(R)
        if a_[2] != b_[2] and a_[3] - a_[1] != b_[3] - b_[1] and a_[4] - a_[0] != b_[4] - b_[0]: break
    gr = {'typ': 'tabelle', 'kopf': ['', 'Min', 'Q₁', 'Median', 'Q₃', 'Max'], 'zeilen': [['Gruppe A'] + [zt(v) for v in a_], ['Gruppe B'] + [zt(v) for v in b_]]}
    al = [
        (f'Der Median von A ist {"größer" if a_[2] > b_[2] else "kleiner"} als der von B.', True),
        (f'Der Median von A ist {"kleiner" if a_[2] > b_[2] else "größer"} als der von B.', False),
        (f'Die Spannweite von A ist {"größer" if a_[4] - a_[0] > b_[4] - b_[0] else "kleiner"} als die von B.', True),
        (f'Die Spannweite von A ist {"kleiner" if a_[4] - a_[0] > b_[4] - b_[0] else "größer"} als die von B.', False),
        (f'In A liegt etwa die Hälfte der Werte zwischen {a_[1]} und {a_[3]}.', True),
        (f'In A liegen etwa drei Viertel der Werte unter {a_[1]}.', False),
        (f'In B liegt etwa ein Viertel der Werte über {b_[3]}.', True),
        (f'In B liegen alle Werte über {b_[1]}.', False),
        (f'Die mittlere Hälfte der Werte streut in A {"stärker" if a_[3] - a_[1] > b_[3] - b_[1] else "weniger"} als in B.', True),
        (f'Weil die Spannweite von {"A" if a_[4] - a_[0] > b_[4] - b_[0] else "B"} größer ist, hat diese Gruppe mehr Werte.', False),
    ]
    wahr = [t for t, w in al if w]; falsch = [t for t, w in al if not w]
    if st == 1 or (st == 2 and R.random() < .5):
        t = R.choice(wahr)
        a = A(R, 'Vergleiche die Gruppen A und B (siehe Tabelle). Welche Aussage ist richtig?', t, R.sample(falsch, 3), f'Richtig: {t}', 'Lies Median, Spannweite und Quartile aus der Tabelle.')
    else:
        t = R.choice(falsch)
        a = A(R, 'Vergleiche die Gruppen A und B (siehe Tabelle). Welche Aussage ist FALSCH?', t, R.sample(wahr, 3),
              f'Falsch: {t} Quartile teilen die Daten in Viertel; die Spannweite sagt nichts über die Anzahl.', 'Prüfe jede Aussage mit den Kennwerten.')
    a['f']['grafik'] = gr
    a['f']['text'] += ' ' + ' / '.join(f'{n}: {"; ".join(zt(v) for v in w)}' for n, w in (('A', a_), ('B', b_)))
    return a


GEN = {'median': g_median, 'kennwerte': g_kennwerte, 'quartile': g_quartile, 'boxplot': g_boxplot, 'mittel_median': g_mittel_median, 'vergleichen': g_vergleichen}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Kennwerte', ['median', 'kennwerte', 'mittel_median']), ('Quartile und Boxplot', ['quartile', 'boxplot']), ('Vergleichen', ['vergleichen'])],
         'Median, Modalwert, Spannweite, Mittelwert und Quartile bestimmen, Informationen aus Boxplot-Kennwerten gewinnen und Datensätze vergleichen und beurteilen.',
         ['Median: Mitte der geordneten Liste.', 'Q₁ und Q₃: Mediane der unteren und oberen Hälfte.', 'Box: mittlere Hälfte der Daten; jede Antenne: ein Viertel.',
          'Bei Ausreißern ist der Median aussagekräftiger als der Mittelwert.'],
         offen=['Boxplots selbst kann die App noch nicht zeichnen. Die fünf Kennwerte werden als Tabelle gezeigt; Aufgaben „Lies aus dem Boxplot ab“ und „Welcher Boxplot passt?“ fehlen.',
                'Quartile werden als Median der unteren bzw. oberen Hälfte bestimmt (bei ungerader Anzahl ohne den Median). Schulbücher verwenden teils andere Verfahren; bitte mit dem Buch des Kindes abgleichen.'])
