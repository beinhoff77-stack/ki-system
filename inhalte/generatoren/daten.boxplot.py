#!/usr/bin/env python3
"""Thema daten.boxplot – Median, Quartile, Boxplot (Gymnasium Bayern, Klasse 7)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl7 import A, L, Z, baue, jw, zt  # noqa: E402

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
    {'lernziel': 'mittel_median', 'titel': 'Mittelwert und Median vergleichen',
     'regel': 'Der ⟦Mittelwert⟧ reagiert stark auf ⟦Ausreißer⟧ (einzelne extreme Werte), der ⟦Median⟧ kaum. Bei Ausreißern beschreibt der Median die „typische Mitte“ meist besser.',
     'schritte': ['Taschengeld (€): 10; 12; 12; 15; 101', 'Mittelwert: 150 : 5 = 30 €; Median: 12 €', 'Der ⟦Median⟧ passt besser – vier von fünf bekommen höchstens 15 €.'],
     'fehler': 'Der Mittelwert 30 € ist nicht „das, was die meisten bekommen“: Ein einziger großer Wert (101 €) ⟦zieht ihn nach oben⟧.',
     '_verbot': ['10; 12; 12; 15; 101']},
    {'lernziel': 'quartile', 'titel': 'Quartile bestimmen',
     'regel': 'Der Median teilt die geordnete Liste in eine untere und eine obere Hälfte. Das ⟦untere Quartil⟧ ist der Median der unteren Hälfte, das ⟦obere Quartil⟧ der Median der oberen Hälfte. Bei ungerader Anzahl gehört der Median ⟦zu keiner Hälfte⟧.',
     'schritte': ['Geordnet: 1; 3; 4; 6; 8; 9; 11', 'Median 6. Untere Hälfte 1; 3; 4 → Q₁ = 3', 'Obere Hälfte 8; 9; 11 → ⟦Q₃ = 9⟧. Quartilsabstand 9 − 3 = 6'],
     'fehler': 'Das untere Quartil ist nicht „ein Viertel vom größten Wert“. Es ist der Wert, unter dem etwa ⟦ein Viertel der Daten⟧ liegt.',
     'bild': {'typ': 'boxplot', 'achse': [0, 12], 'reihen': [{'min': 1, 'q1': 3, 'median': 6, 'q3': 9, 'max': 11}]},
     '_verbot': ['1; 3; 4; 6; 8; 9; 11']},
    {'lernziel': 'boxplot', 'titel': 'Informationen aus Boxplots',
     'regel': 'Ein ⟦Boxplot⟧ zeigt die fünf Kennwerte Minimum, unteres Quartil, Median, oberes Quartil, Maximum. In der ⟦Box⟧ (zwischen den Quartilen) liegt etwa die ⟦Hälfte⟧ der Daten, in jeder ⟦Antenne⟧ und jeder Boxhälfte etwa ein ⟦Viertel⟧.',
     'schritte': ['Kennwerte: 12 | 18 | 23 | 30 | 41', 'Spannweite 41 − 12 = 29, Quartilsabstand 30 − 18 = 12', 'Etwa ⟦75 %⟧ der Werte liegen unter 30.'],
     'fehler': 'Eine längere Antenne bedeutet nicht mehr Werte: In jeder Antenne liegt etwa ⟦ein Viertel⟧ der Daten, nur ⟦weiter gestreut⟧.',
     'bild': {'typ': 'boxplot', 'achse': [10, 45], 'reihen': [{'min': 12, 'q1': 18, 'median': 23, 'q3': 30, 'max': 41}]},
     '_verbot': ['12 | 18 | 23 | 30 | 41']},
    {'lernziel': 'vergleichen', 'titel': 'Datensätze vergleichen und beurteilen',
     'regel': 'Vergleiche zuerst die ⟦Mitte⟧ (Median), dann die ⟦Streuung⟧ (Spannweite, Quartilsabstand). Eine Aussage über „die meisten“ oder „ein Viertel“ prüfst du mit den Quartilen.',
     'schritte': ['Klasse A: Median 24 s, Quartilsabstand 4 s. Klasse B: Median 22 s, Quartilsabstand 9 s.', 'B ist in der Mitte schneller (kleinere Zeit), streut aber stärker.',
                  'Aussage „In A sind die Zeiten einheitlicher“: ⟦richtig⟧.'],
     'fehler': 'Eine größere Spannweite heißt nicht, dass die Gruppe insgesamt besser oder schlechter ist. Sie sagt nur etwas über die ⟦Streuung⟧ aus.',
     'bild': {'typ': 'boxplot', 'achse': [10, 40], 'einheit': 's', 'reihen': [{'name': 'Klasse A', 'min': 19, 'q1': 22, 'median': 24, 'q3': 26, 'max': 31}, {'name': 'Klasse B', 'min': 15, 'q1': 18, 'median': 22, 'q3': 27, 'max': 35}]}},
]


def daten(R, n, lo=1, hi=30):
    return [R.randint(lo, hi) for _ in range(n)]


ZYK = {}


def zyklus(name, liste):
    ZYK[name] = ZYK.get(name, -1) + 1
    return liste[ZYK[name] % len(liste)]


HAEUF = [('Note', [1, 2, 3, 4, 5, 6], 'Kinder'), ('Tore', [0, 1, 2, 3, 4], 'Spiele'), ('Geschwister', [0, 1, 2, 3, 4], 'Kinder'), ('Augenzahl', [1, 2, 3, 4, 5, 6], 'Würfe')]


def g_median(R, st):
    if st == 3 and zyklus('med3', [1, 0]):
        merkmal, werte, wer = R.choice(HAEUF)
        anz = [R.randint(0, 9) for _ in werte]
        if sum(anz) < 12: anz = [a + 2 for a in anz]
        xs = [w for w, a in zip(werte, anz) for _ in range(a)]
        n = len(xs); m = median(xs)
        mitte = f'{n // 2 + 1}. Wert' if n % 2 else f'{n // 2}. und {n // 2 + 1}. Wert'
        a = Z(f'Die Tabelle zeigt, wie oft jeder Wert vorkommt ({merkmal}, Anzahl der {wer}). Bestimme den Median.', m,
              f'{xs[n // 2]}' if n % 2 else f'({xs[n // 2 - 1]} + {xs[n // 2]}) / 2',
              f'Insgesamt {n} Werte. Die Mitte ist der {mitte}. Von unten gezählt: ' + ', '.join(f'bis {w}: {sum(anz[:i + 1])}' for i, w in enumerate(werte)) + f'. Median: {zt(m)}.',
              'Zähle alle Werte. Welcher Platz ist die Mitte? Zähle in der Tabelle von unten bis dorthin.')
        a['f']['grafik'] = {'typ': 'tabelle', 'kopf': [merkmal] + [str(w) for w in werte], 'zeilen': [[f'Anzahl {wer}'] + [str(x) for x in anz]]}
        return a
    n = R.choice({1: [5, 7, 9], 2: [6, 8, 10, 11], 3: [12, 14, 15, 16]}[st])
    kontext, lo, hi = R.choice([('Punkte in einem Test (höchstens 30)', 0, 30), ('Tore pro Spiel', 0, 6), ('Minuten Schulweg', 3, 45),
                                ('Seiten gelesen pro Tag', 2, 60), ('Liegestütze', 4, 40), ('Körpergröße in cm', 138, 176)])
    xs = daten(R, n, lo, hi)
    m = median(xs); s_ = sorted(xs)
    weg = f'Geordnet: {liste(s_)}. ' + (f'Mittlerer ({n // 2 + 1}.) Wert: {zt(m)}.' if n % 2 else f'Mittlere Werte {zt(s_[n // 2 - 1])} und {zt(s_[n // 2])}: ({zt(s_[n // 2 - 1])} + {zt(s_[n // 2])}) : 2 = {zt(m)}.')
    return Z(f'{kontext}: {liste(xs)}. Bestimme den Median.', m, f'{s_[n // 2]}' if n % 2 else f'({s_[n // 2 - 1]} + {s_[n // 2]}) / 2', weg,
             'Ordne die Werte zuerst der Größe nach.')


KW_KONTEXT = ['Punkte beim Ballwurf', 'Minuten Hausaufgaben', 'Gelesene Bücher im Jahr', 'Tore in der Saison', 'Liegestütze in einer Minute', 'Euro Taschengeld']


def g_kennwerte(R, st):
    n = R.choice([5, 6, 7, 8, 10])
    kon = R.choice(KW_KONTEXT)
    while True:
        xs = daten(R, n, 1, 25)
        mod = max(set(xs), key=xs.count)
        if [xs.count(v) for v in set(xs)].count(xs.count(mod)) == 1 and xs.count(mod) > 1: break   # Modalwert eindeutig
    welches = R.choice({1: ['Modalwert', 'Spannweite'], 2: ['Spannweite', 'Mittelwert', 'Modalwert'], 3: ['Mittelwert', 'fehlend']}[st])
    if welches == 'Modalwert':
        return Z(f'{kon} von {n} Kindern: {liste(xs)}. Bestimme den Modalwert.', mod, f'{mod}', f'{zt(mod)} kommt {xs.count(mod)}-mal vor, öfter als jeder andere Wert.', 'Welcher Wert kommt am häufigsten vor?')
    if welches == 'Spannweite':
        return Z(f'{kon} von {n} Kindern: {liste(xs)}. Bestimme die Spannweite.', max(xs) - min(xs), f'{max(xs)} - {min(xs)}', f'Größter Wert {max(xs)}, kleinster {min(xs)}: {max(xs)} − {min(xs)} = {max(xs) - min(xs)}.',
                 'Größter minus kleinster Wert.')
    if welches == 'Mittelwert':
        mw = Fr(sum(xs), n)
        if mw.denominator not in (1, 2, 4, 5, 8, 10): return g_kennwerte(R, st)
        return Z(f'{kon} von {n} Kindern: {liste(xs)}. Berechne das arithmetische Mittel.', mw, f'({" + ".join(map(str, xs))}) / {n}', f'Summe {sum(xs)}, Anzahl {n}: {sum(xs)} : {n} = {zt(mw)}.',
                 'Alle Werte addieren und durch ihre Anzahl teilen.')
    mw = R.randint(8, 20); k = n - 1
    teil = daten(R, k, 1, 25)
    fehl = mw * n - sum(teil)
    if fehl < 0 or fehl > 60: return g_kennwerte(R, st)
    return Z(f'{kon}: Von {n} Kindern kennt man {k} Werte: {liste(teil)}. Das arithmetische Mittel aller {n} Werte ist {mw}. Wie groß ist der fehlende Wert?', fehl,
             f'{mw} * {n} - ({" + ".join(map(str, teil))})',
             f'Summe aller Werte: {mw} · {n} = {mw * n}. Bekannte Summe {sum(teil)}. Fehlender Wert: {mw * n} − {sum(teil)} = {fehl}.', 'Mittelwert · Anzahl = Summe.')


FESTLEGUNG = ' (Festlegung hier: Bei ungerader Anzahl gehört der Median zu keiner Hälfte. Manche Bücher rechnen etwas anders; dann kann das Ergebnis leicht abweichen.)'


def g_quartile(R, st):
    n = R.choice({1: [7, 11], 2: [8, 9, 10, 12], 3: [13, 15, 16]}[st])
    xs = sorted(daten(R, n, 1, 50)) if st == 1 else daten(R, n, 1, 50)
    q1, q3 = quartile(xs); s_ = sorted(xs)
    welches = R.choice({1: ['Q₁', 'Q₃'], 2: ['Q₁', 'Q₃', 'Abstand'], 3: ['Abstand', 'Q₁', 'Q₃']}[st])
    unten, oben = s_[:n // 2], s_[(n + 1) // 2:]
    weg = f'Geordnet: {liste(s_)}. Untere Hälfte {liste(unten)} → Q₁ = {zt(q1)}; obere Hälfte {liste(oben)} → Q₃ = {zt(q3)}.' + (FESTLEGUNG if n % 2 else '')
    if welches == 'Abstand':
        return Z(f'Werte: {liste(xs)}. Bestimme den Quartilsabstand Q₃ − Q₁.', q3 - q1, f'{q3.numerator}/{q3.denominator} - {q1.numerator}/{q1.denominator}', weg + f' Abstand {zt(q3 - q1)}.',
                 'Erst ordnen, dann die Hälften bilden, dann jeweils den Median.')
    q = q1 if welches == 'Q₁' else q3
    name = 'untere' if welches == 'Q₁' else 'obere'
    return Z(f'Werte: {liste(xs)}. Bestimme das {name} Quartil.', q, f'{q.numerator}/{q.denominator}', weg,
             f'Bilde die {name} Hälfte (ohne den Median, falls die Anzahl ungerade ist) und bestimme ihren Median.')


# Kontext, Achsenanfang, Schritt (Teilstrich), Einheit – alle Kennwerte liegen auf Teilstrichen
BP_KONTEXT = [('Körpergröße', 130, 5, 'cm'), ('Punkte im Test', 0, 3, 'Punkte'), ('Weitsprung', 200, 20, 'cm'), ('Wartezeit', 0, 2, 'min'),
              ('Taschengeld', 0, 4, '€'), ('Zeit für 1 000 m', 200, 10, 's'), ('Weitwurf', 0, 5, 'm')]


def fuenf_raster(R):
    while True:
        pos = sorted(R.sample(range(0, 11), 5))
        if pos[4] - pos[0] >= 6: return pos


def bp(reihen, lo, u, einheit):
    return {'typ': 'boxplot', 'achse': [lo, lo + 10 * u], 'schritt': u, 'einheit': einheit,
            'reihen': [{**({'name': n} if n else {}), 'min': w[0], 'q1': w[1], 'median': w[2], 'q3': w[3], 'max': w[4]} for n, w in reihen]}


def _zuordnen(R):
    n = R.choice([7, 9, 11])
    xs = sorted(daten(R, n, 1, 30))
    while len(set(xs)) < n - 1: xs = sorted(daten(R, n, 1, 30))
    q1, q3 = quartile(xs); me = median(xs)
    richtig = [xs[0], q1, me, q3, xs[-1]]
    mit_median = [xs[0], median(xs[:n // 2 + 1]), me, median(xs[n // 2:]), xs[-1]]           # andere Quartilsregel – hier nicht gemeint
    mittel = Fr(sum(xs), n)
    falsch_mitte = [xs[0], q1, mittel, q3, xs[-1]] if mittel != me and q1 < mittel < q3 and mittel.denominator in (1, 2, 4, 5, 10) else [xs[0], xs[1], me, xs[-2], xs[-1]]
    falsch_rand = [xs[1], q1, me, q3, xs[-2]]
    kand = [richtig, falsch_mitte, falsch_rand] if mit_median == richtig or R.random() < .5 else [richtig, falsch_mitte, mit_median]
    if len({tuple(k) for k in kand}) < 3: kand = [richtig, falsch_mitte, falsch_rand]
    if len({tuple(k) for k in kand}) < 3: return None
    R.shuffle(kand)
    namen = ['A', 'B', 'C']
    r = namen[kand.index(richtig)]
    a = A(R, f'Daten: {liste(xs)}. Welcher Boxplot passt zu diesen Daten?', f'Boxplot {r}', [f'Boxplot {x}' for x in namen if x != r] + ['keiner der drei'],
          f'Minimum {xs[0]}, Q₁ = {zt(q1)}, Median {zt(me)}, Q₃ = {zt(q3)}, Maximum {xs[-1]}: Das ist Boxplot {r}.' + FESTLEGUNG,
          'Bestimme Minimum, Median und Maximum zuerst – oft scheiden damit schon Boxplots aus.')
    a['f']['grafik'] = {'typ': 'boxplot', 'achse': [0, 30], 'schritt': 5, 'reihen': [{'name': nm, 'min': jw(k[0]), 'q1': jw(k[1]), 'median': jw(k[2]), 'q3': jw(k[3]), 'max': jw(k[4])}
                                                                             for nm, k in zip(namen, kand)]}
    return a


def g_boxplot(R, st):
    if st == 3 and zyklus('bp3', [1, 0]):
        for _ in range(50):
            a = _zuordnen(R)
            if a: return a
    kontext, lo, u, einh = R.choice(BP_KONTEXT)
    w = [lo + u * p for p in fuenf_raster(R)]
    gr = bp([('', w)], lo, u, einh)
    if st == 1:
        was = R.choice(['den Median', 'das untere Quartil', 'das obere Quartil', 'das Maximum', 'die Spannweite', 'den Quartilsabstand'])
        val = {'den Median': w[2], 'das untere Quartil': w[1], 'das obere Quartil': w[3], 'das Maximum': w[4], 'die Spannweite': w[4] - w[0], 'den Quartilsabstand': w[3] - w[1]}[was]
        c = {'die Spannweite': f'{w[4]} - {w[0]}', 'den Quartilsabstand': f'{w[3]} - {w[1]}'}.get(was, f'{val}')
        weg = {'den Median': f'Der Strich in der Box steht bei {val}.', 'das untere Quartil': f'Der linke Rand der Box steht bei {val}.',
               'das obere Quartil': f'Der rechte Rand der Box steht bei {val}.', 'das Maximum': f'Das rechte Ende der Antenne steht bei {val}.',
               'die Spannweite': f'Maximum − Minimum = {w[4]} − {w[0]} = {val}.', 'den Quartilsabstand': f'Q₃ − Q₁ = {w[3]} − {w[1]} = {val}.'}[was]
        a = Z(f'Der Boxplot zeigt die Ergebnisse einer Erhebung ({kontext}{"" if einh == "Punkte" else " in " + einh}). ' + (f'Lies {was} ab.' if 'abstand' not in was and 'Spannweite' not in was else f'Bestimme {was}.'), val, c, weg,
              'Box: von Q₁ bis Q₃, Strich in der Box: Median, Antennen: bis Minimum und Maximum.', einh if einh in ('cm', 'min', 's', 'm', '€') else None)
    elif st == 2:
        frage, proz = R.choice([(f'unter {w[2]} {einh}', 50), (f'über {w[3]} {einh}', 25), (f'zwischen {w[1]} {einh} und {w[3]} {einh}', 50), (f'unter {w[1]} {einh}', 25),
                                (f'unter {w[3]} {einh}', 75), (f'über {w[1]} {einh}', 75), (f'über {w[2]} {einh}', 50)])
        a = Z(f'Der Boxplot zeigt die Ergebnisse einer Erhebung ({kontext}). Etwa wie viel Prozent der Werte liegen {frage}?',
              proz, f'{proz}', f'Quartile und Median teilen die Daten in Viertel. {frage[0].upper() + frage[1:]} liegen etwa {proz} %.', 'Jeder der vier Abschnitte enthält etwa ein Viertel der Daten.', '%')
    else:
        n = R.choice([20, 40, 60, 80, 100, 120, 200])
        frage, anteil = R.choice([(f'über {w[3]} {einh}', Fr(1, 4)), (f'zwischen {w[1]} {einh} und {w[3]} {einh}', Fr(1, 2)), (f'unter {w[1]} {einh}', Fr(1, 4)), (f'über {w[1]} {einh}', Fr(3, 4))])
        a = Z(f'{n} Personen wurden erfasst ({kontext}, siehe Boxplot). Etwa wie viele Personen liegen {frage}?',
              anteil * n, f'{n} * {anteil.numerator} / {anteil.denominator}', f'{frage[0].upper() + frage[1:]} liegen etwa {zt(anteil * 100)} % der Daten: {zt(anteil * 100)} % von {n} = {zt(anteil * n)}.',
              'Lies ab, wo die Grenze liegt (Quartil oder Median), und welcher Anteil gemeint ist.')
    a['f']['grafik'] = gr
    return a


def g_mittel_median(R, st):
    if st == 3:
        art = zyklus('mm3', ['firma', 'ohne', 'aus', 'ohne'])
        if art == 'firma':
            k = R.choice([5, 7, 9]); g = R.choice([2800, 3000, 3200, 3500]); chef = R.choice([20000, 24000, 30000])
            mw = Fr(k * g + chef, k + 1)
            if mw.denominator != 1: return g_mittel_median(R, st)
            r = f'Der Median ({g} €), denn der Mittelwert ({zt(mw)} €) wird vom Chefgehalt hochgezogen.'
            return A(R, f'In einer kleinen Firma verdienen {k} Personen je {zt(g)} € im Monat, die Chefin {zt(chef)} €. Welche Angabe beschreibt das typische Gehalt?', r,
                     [f'Der Mittelwert ({zt(mw)} €), weil er alle Gehälter berücksichtigt.', 'Mittelwert und Median sind fast gleich, beide passen.',
                      f'Die Spannweite ({zt(chef - g)} €), weil sie alle Gehälter umfasst.'],
                     f'Mittelwert: ({k} · {zt(g)} + {zt(chef)}) : {k + 1} = {zt(mw)} €. Median: {zt(g)} €. Nur der Median trifft, was die meisten verdienen.',
                     'Gibt es einen Wert, der weit von den anderen entfernt ist?')
        if art == 'ohne':
            while True:
                xs = daten(R, R.choice([5, 6, 7]), 4, 12)
                mw, me = Fr(sum(xs), len(xs)), median(xs)
                if abs(mw - me) <= 1 and max(xs) - min(xs) <= 7 and mw.denominator in (1, 2, 4, 5): break
            r = 'Mittelwert und Median sind fast gleich, beide passen.'
            return A(R, f'Wartezeiten an einer Kasse (min): {liste(xs)}. Welcher Wert beschreibt die typische Mitte besser?', r,
                     ['Nur der Median, weil der Mittelwert immer durch Ausreißer verfälscht wird.', 'Nur der Mittelwert, weil der Median Werte weglässt.',
                      'Die Spannweite, weil sie alle Werte umfasst.'],
                     f'Mittelwert {zt(mw)}, Median {zt(me)}. Es gibt keinen Ausreißer, die beiden Werte liegen dicht beieinander.', 'Gibt es einen Ausreißer? Berechne beide Werte.')
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
             ['Der Mittelwert, weil er alle Werte berücksichtigt.', 'Mittelwert und Median sind fast gleich, beide passen.', 'Die Spannweite, weil sie alle Werte umfasst.'],
             f'Mittelwert {zt(mw)}, Median {zt(me)}. Der Wert {aus} ist ein Ausreißer und verschiebt den Mittelwert.', 'Gibt es einen Wert, der weit von den anderen entfernt ist?')


VG_KONTEXT = [('beim Weitwurf', 0, 5, 'm', 'warf insgesamt weiter', True), ('beim Sprint über 50 m', 6, 1, 's', 'lief insgesamt schneller', False),
              ('im Mathetest', 0, 3, 'Punkte', 'schnitt insgesamt besser ab', True), ('beim 1 000-m-Lauf', 200, 10, 's', 'lief insgesamt schneller', False),
              ('beim Hochsprung', 80, 5, 'cm', 'sprang insgesamt höher', True)]


def g_vergleichen(R, st):
    kontext, lo, u, einh, besser, gross_gut = R.choice(VG_KONTEXT)
    while True:
        pa, pb = fuenf_raster(R), fuenf_raster(R)
        if pa[2] != pb[2] and pa[3] - pa[1] != pb[3] - pb[1] and pa[4] - pa[0] != pb[4] - pb[0]: break
    a_, b_ = [lo + u * p for p in pa], [lo + u * p for p in pb]
    A_, B_ = '7a', '7b'
    gr = bp([(f'Klasse {A_}', a_), (f'Klasse {B_}', b_)], lo, u, einh)
    einl = f'Ergebnisse zweier Klassen {kontext} ({einh if einh == "Punkte" else "in " + einh}), siehe Boxplots.'
    if st >= 2 and zyklus('vg', [0, 1, 0, 1, 1]):
        if R.random() < .5:
            sieger = A_ if (a_[2] > b_[2]) == gross_gut else B_
            r = f'Klasse {sieger}, denn ihr Median ist {"größer" if gross_gut else "kleiner"}.'
            a = A(R, f'{einl} Welche Klasse {besser}?', r,
                  [f'Klasse {A_ if sieger == B_ else B_}, denn ihr Median ist {"größer" if not gross_gut else "kleiner"}.',
                   f'Klasse {A_ if sieger == B_ else B_}, denn dort gibt es den besten Einzelwert.',
                   'Das kann man nicht sagen, weil die Spannweiten verschieden sind.'],
                  f'Die Mitte vergleicht man mit dem Median: {A_} {zt(a_[2])} {einh}, {B_} {zt(b_[2])} {einh}.', 'Vergleiche die Mitte (Median), nicht einzelne Extremwerte.')
        else:
            ga = a_[3] - a_[1] < b_[3] - b_[1]
            sieger = A_ if ga else B_
            r = f'Klasse {sieger}, denn ihr Quartilsabstand (Länge der Box) ist kleiner.'
            a = A(R, f'{einl} In welcher Klasse sind die Leistungen gleichmäßiger?', r,
                  [f'Klasse {B_ if ga else A_}, denn ihre Box ist länger.', f'Klasse {A_ if a_[2] > b_[2] else B_}, denn ihr Median ist größer.',
                   'In beiden gleich, weil beide Klassen gleich viele Kinder haben.'],
                  f'Gleichmäßiger heißt: weniger Streuung. Quartilsabstand {A_}: {zt(a_[3] - a_[1])} {einh}, {B_}: {zt(b_[3] - b_[1])} {einh}.', 'Welche Box ist kürzer?')
        a['f']['grafik'] = gr
        return a
    al = [
        (f'Der Median der {A_} ist {"größer" if a_[2] > b_[2] else "kleiner"} als der der {B_}.', True),
        (f'Der Median der {A_} ist {"kleiner" if a_[2] > b_[2] else "größer"} als der der {B_}.', False),
        (f'Die Spannweite der {A_} ist {"größer" if a_[4] - a_[0] > b_[4] - b_[0] else "kleiner"} als die der {B_}.', True),
        (f'Die Spannweite der {A_} ist {"kleiner" if a_[4] - a_[0] > b_[4] - b_[0] else "größer"} als die der {B_}.', False),
        (f'In der {A_} liegt etwa die Hälfte der Werte zwischen {a_[1]} und {a_[3]} {einh}.', True),
        (f'In der {A_} liegen etwa drei Viertel der Werte unter {a_[1]} {einh}.', False),
        (f'In der {B_} liegt etwa ein Viertel der Werte über {b_[3]} {einh}.', True),
        (f'In der {B_} liegen alle Werte über {b_[1]} {einh}.', False),
        (f'Die mittlere Hälfte der Werte streut in der {A_} {"stärker" if a_[3] - a_[1] > b_[3] - b_[1] else "weniger"} als in der {B_}.', True),
        (f'Weil die Spannweite der {A_ if a_[4] - a_[0] > b_[4] - b_[0] else B_} größer ist, hat diese Klasse mehr Kinder.', False),
    ]
    wahr = [t for t, w in al if w]; falsch = [t for t, w in al if not w]
    if st == 1 or R.random() < .5:
        t = R.choice(wahr)
        a = A(R, f'{einl} Welche Aussage ist richtig?', t, R.sample(falsch, 3), f'Richtig: {t}', 'Lies Median, Box und Antennen aus den Boxplots ab.')
    else:
        t = R.choice(falsch)
        a = A(R, f'{einl} Welche Aussage stimmt nicht?', t, R.sample(wahr, 3),
              f'Stimmt nicht: {t} Quartile teilen die Daten in Viertel; die Spannweite sagt nichts über die Anzahl.', 'Prüfe jede Aussage am Boxplot.')
    a['f']['grafik'] = gr
    return a


GEN = {'median': g_median, 'kennwerte': g_kennwerte, 'quartile': g_quartile, 'boxplot': g_boxplot, 'mittel_median': g_mittel_median, 'vergleichen': g_vergleichen}

# Verständliche Fassung (Runde 7, Maßstab inhalte/README.md „Verständliche Erklärungen“):
# Alltagssituation zuerst (einstieg), jedes neue Wort erklärt (woerter), Beispiel in kleinen Schritten, Merksatz am Ende (regel).
# Situationen: Umfragen in einer Schule (Schulweg, gelesene Bücher, Taschengeld, Quiz-Punkte, Laufzeiten zweier Klassen).
KLAR = {
 'median': {
  'einstieg': 'Sechs Kinder einer Klasse sagen, wie viele Minuten ihr Schulweg dauert: 7, 3, 9, 4, 12 und 5. Welche Zahl beschreibt einen „typischen“ Schulweg? Man stellt die Kinder der Reihe nach auf, vom kürzesten bis zum längsten Weg, und schaut, wer in der Mitte steht. Der Wert in der Mitte heißt ⟦Median⟧.',
  'woerter': [['Daten / Werte', 'die gesammelten Zahlen, hier die Minuten'], ['geordnete Liste', 'die Werte der Größe nach, vom kleinsten zum größten'],
              ['Median (Zentralwert)', 'der Wert in der Mitte der geordneten Liste'], ['7; 3; 9', 'Strichpunkte trennen die Werte, damit man sie nicht mit Kommazahlen verwechselt']],
  'schritte': ['Die Werte sind 7; 3; 9; 4; 12; 5 Minuten.',
               'Ordne sie der Größe nach: 3; 4; 5; 7; 9; 12. Das sind 6 Werte.',
               'Bei 6 Werten gibt es keinen einzelnen mittleren Wert. In der Mitte stehen zwei: 5 und 7.',
               'Nimm die Zahl genau zwischen beiden: (5 + 7) : 2 = ⟦6⟧. Der Median ist 6 Minuten.'],
  'regel': 'So bestimmst du den ⟦Median⟧: Ordne die Werte der Größe nach und nimm den Wert in der ⟦Mitte⟧. Bei einer geraden Anzahl nimmst du die ⟦Zahl genau zwischen den beiden mittleren⟧ Werten.',
  'fehler': 'Der Median von 7; 3; 9; 4; 12 ist nicht 9, nur weil die 9 in der ungeordneten Liste in der Mitte steht – das wäre, als würde man die Kinder irgendwie aufstellen. Erst ⟦ordnen⟧: 3; 4; 7; 9; 12 → Median 7.'},
 'kennwerte': {
  'einstieg': 'Fünf Kinder zählen, wie viele Bücher sie in den Ferien gelesen haben: 2, 5, 5, 6 und 12. Man kann fragen: Welche Zahl kommt am häufigsten vor? Wie weit liegen das wenigste und das meiste auseinander? Und wie viele Bücher wären es pro Kind, wenn alle gleich viel gelesen hätten? Solche Zahlen, die eine Liste zusammenfassen, heißen ⟦Kennwerte⟧.',
  'woerter': [['Kennwerte', 'Zahlen, die eine ganze Liste kurz beschreiben'], ['Modalwert', 'der Wert, der am häufigsten vorkommt'], ['Spannweite', 'größter Wert minus kleinster Wert'],
              ['arithmetisches Mittel (Mittelwert)', 'alle Werte zusammenzählen und durch ihre Anzahl teilen – so viel hätte jeder bei gleicher Verteilung']],
  'schritte': ['Die Werte sind 2; 5; 5; 6; 12 Bücher.',
               'Die 5 kommt zweimal vor, jede andere Zahl nur einmal. Der Modalwert ist 5.',
               'Der größte Wert ist 12, der kleinste 2. Die Spannweite ist 12 − 2 = 10.',
               'Für den Mittelwert alle zusammenzählen: 2 + 5 + 5 + 6 + 12 = 30. Durch die Anzahl 5 teilen: 30 : 5 = ⟦6⟧.'],
  'regel': 'So findest du die ⟦Kennwerte⟧: ⟦Modalwert⟧ – der häufigste Wert. ⟦Spannweite⟧ – größter minus kleinster Wert. ⟦Arithmetisches Mittel⟧ – Summe aller Werte geteilt durch ihre Anzahl.',
  'fehler': 'Die Spannweite von 2; 5; 5; 6; 12 ist nicht 12. Sie ist der ⟦Abstand⟧ zwischen dem größten und dem kleinsten Wert: 12 − 2 = 10 – so viele Bücher mehr hat das Kind mit den meisten gelesen als das mit den wenigsten.',
  'bild': {'typ': 'saeulen', 'einheit': 'Anzahl Kinder', 'werte': [{'name': '2 Bücher', 'wert': 1}, {'name': '5 Bücher', 'wert': 2}, {'name': '6 Bücher', 'wert': 1}, {'name': '12 Bücher', 'wert': 1}], 'zahlen': True}},
 'mittel_median': {
  'einstieg': 'Fünf Kinder sagen, wie viel Taschengeld sie im Monat bekommen: 10 €, 12 €, 12 €, 15 € – und eines bekommt 101 €. Rechnet man den Mittelwert aus, kommt 30 € heraus, obwohl vier von fünf viel weniger bekommen. Ein einzelner Wert, der weit von allen anderen entfernt liegt, heißt ⟦Ausreißer⟧.',
  'woerter': [['Ausreißer', 'ein einzelner Wert, der weit weg von allen anderen liegt'], ['typische Mitte', 'ein Wert, der beschreibt, was für die meisten gilt']],
  'schritte': ['Die Werte sind 10; 12; 12; 15; 101 Euro.',
               'Mittelwert: 10 + 12 + 12 + 15 + 101 = 150, und 150 : 5 = 30 €.',
               'Median: Die Liste ist schon geordnet, in der Mitte steht 12 €.',
               'Vier von fünf Kindern bekommen höchstens 15 €. Die typische Mitte beschreibt also der ⟦Median⟧ besser.'],
  'regel': 'So entscheidest du: Der ⟦Mittelwert⟧ reagiert stark auf ⟦Ausreißer⟧, der ⟦Median⟧ kaum. Gibt es einen Ausreißer, beschreibt meist der Median die typische Mitte besser. Ohne Ausreißer passen oft beide.',
  'fehler': 'Der Mittelwert 30 € ist nicht „das, was die meisten bekommen“. Das eine Kind mit 101 € ⟦zieht ihn nach oben⟧ – so wie ein einziger sehr großer Mensch die Durchschnittsgröße einer kleinen Gruppe deutlich anhebt.'},
 'quartile': {
  'einstieg': 'Sieben Kinder machen bei einem Quiz mit und bekommen 1, 3, 4, 6, 8, 9 und 11 Punkte. Der Median teilt sie in eine untere und eine obere Hälfte. Teilt man jede Hälfte noch einmal in der Mitte, hat man vier Viertel. Die Werte an diesen Trennstellen heißen ⟦Quartile⟧.',
  'woerter': [['Quartil', 'Trennstelle zwischen zwei Vierteln der geordneten Daten'], ['Q₁, Q₃', 'die kleine Zahl unten ist nur eine Nummer: erstes und drittes Quartil'],
              ['unteres Quartil Q₁', 'der Median der unteren Hälfte; etwa ein Viertel der Werte liegt darunter'],
              ['oberes Quartil Q₃', 'der Median der oberen Hälfte; etwa drei Viertel der Werte liegen darunter'], ['Quartilsabstand', 'Q₃ − Q₁; so breit ist die mittlere Hälfte der Daten']],
  'schritte': ['Die geordneten Werte sind 1; 3; 4; 6; 8; 9; 11. Der Median ist 6.',
               'Bei einer ungeraden Anzahl gehört der Median zu keiner Hälfte. Die untere Hälfte ist 1; 3; 4, ihr Median ist Q₁ = 3.',
               'Die obere Hälfte ist 8; 9; 11, ihr Median ist ⟦Q₃ = 9⟧.',
               'Der Quartilsabstand ist 9 − 3 = 6.'],
  'regel': 'So bestimmst du die ⟦Quartile⟧: Teile die geordnete Liste am Median in eine untere und eine obere Hälfte. Das ⟦untere Quartil⟧ ist der Median der unteren Hälfte, das ⟦obere Quartil⟧ der Median der oberen Hälfte. Bei ungerader Anzahl gehört der Median ⟦zu keiner Hälfte⟧.',
  'fehler': 'Das untere Quartil ist nicht „ein Viertel vom größten Wert“ (11 : 4). Es ist eine Trennstelle in der geordneten Liste: Etwa ⟦ein Viertel der Daten⟧ liegt darunter, drei Viertel darüber.',
  'bild': {'typ': 'boxplot', 'achse': [0, 12], 'einheit': 'Punkte', 'reihen': [{'min': 1, 'q1': 3, 'median': 6, 'q3': 9, 'max': 11}]}},
 'boxplot': {
  'einstieg': 'Bei einer großen Umfrage an der Schule haben 200 Kinder ihren Schulweg in Minuten angegeben. Eine Liste mit 200 Zahlen ist unübersichtlich. Man zeichnet stattdessen ein Bild aus einer Box und zwei Linien, das die fünf wichtigsten Werte auf einen Blick zeigt. So ein Bild heißt ⟦Boxplot⟧.',
  'woerter': [['Minimum / Maximum', 'kleinster / größter Wert'], ['Box', 'das Rechteck von Q₁ bis Q₃; der Strich darin ist der Median'],
              ['Antennen', 'die Linien links und rechts der Box bis zum Minimum und zum Maximum'], ['fünf Kennwerte', 'Minimum, Q₁, Median, Q₃, Maximum']],
  'schritte': ['Lies die fünf Werte ab: Minimum 12, Q₁ = 18, Median 23, Q₃ = 30, Maximum 41 (in Minuten).',
               'Die Spannweite ist die ganze Länge: 41 − 12 = 29 Minuten.',
               'Der Quartilsabstand ist die Länge der Box: 30 − 18 = 12 Minuten.',
               'Links von Q₃ liegen drei Viertel der Daten: Etwa ⟦75 %⟧ der Kinder brauchen weniger als 30 Minuten.'],
  'regel': 'So liest du einen ⟦Boxplot⟧: Er zeigt Minimum, unteres Quartil, Median, oberes Quartil und Maximum. In der ⟦Box⟧ liegt etwa die ⟦Hälfte⟧ der Daten, in jeder ⟦Antenne⟧ und in jeder Hälfte der Box etwa ein ⟦Viertel⟧.',
  'fehler': 'Eine längere Antenne bedeutet nicht, dass dort mehr Kinder sind. In jeder Antenne liegt etwa ⟦ein Viertel⟧ der Daten – nur ⟦weiter auseinander⟧: Die Kinder mit langem Schulweg unterscheiden sich stärker voneinander.',
  'bild': {'typ': 'boxplot', 'achse': [10, 45], 'einheit': 'min', 'reihen': [{'min': 12, 'q1': 18, 'median': 23, 'q3': 30, 'max': 41}]}},
 'vergleichen': {
  'einstieg': 'Zwei Klassen laufen dieselbe Strecke durch den Pausenhof, jede Zeit wird gestoppt. Welche Klasse war schneller? Und in welcher Klasse waren die Kinder ähnlich schnell, in welcher sehr unterschiedlich? Zwei Boxplots übereinander zeigen beides auf einen Blick. So kann man ⟦Datensätze vergleichen⟧.',
  'woerter': [['Datensatz', 'alle Werte einer Gruppe, hier die Zeiten einer Klasse'], ['Mitte', 'wo die Werte ungefähr liegen; man vergleicht sie mit dem Median'],
              ['Streuung', 'wie weit die Werte auseinanderliegen; man vergleicht sie mit Spannweite und Quartilsabstand'], ['einheitlich', 'die Werte liegen nah beieinander'], ['s', 'Sekunden']],
  'schritte': ['Lies aus den Boxplots ab: Klasse A hat den Median 24 s und den Quartilsabstand 26 − 22 = 4 s.',
               'Klasse B hat den Median 22 s und den Quartilsabstand 27 − 18 = 9 s.',
               'Der Median von B ist die kleinere Zeit: B war in der Mitte schneller. Die Box von B ist aber länger: B streut stärker.',
               'Die Aussage „In A sind die Zeiten einheitlicher“ ist also ⟦richtig⟧.'],
  'regel': 'So vergleichst du ⟦Datensätze⟧: Vergleiche zuerst die ⟦Mitte⟧ (Median), dann die ⟦Streuung⟧ (Spannweite, Quartilsabstand). Aussagen über „die meisten“ oder „ein Viertel“ prüfst du mit den Quartilen.',
  'fehler': 'Eine größere Spannweite heißt nicht, dass eine Klasse insgesamt besser oder schlechter ist – und auch nicht, dass sie mehr Kinder hat. Sie sagt nur etwas über die ⟦Streuung⟧: Die Zeiten liegen weiter auseinander.'},
}
for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl7.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl7 import mit_umbau  # noqa: E402


def _strahl(start, ende, abschnitte, werte, extra=(), bereich=None):
    b = {'typ': 'zahlenstrahl', 'start': start, 'ende': ende, 'abschnitte': abschnitte, 'beschriftet': 'anfang_ende',
         'punkte': [{'wert': w} for w in werte] + list(extra)}
    if bereich: b['bereich'] = bereich
    return b


_WEG = [7, 3, 9, 4, 12, 5]
_GELD = [10, 12, 12, 15, 101]
_QUIZ = [1, 3, 4, 6, 8, 9, 11]
_BP_QUIZ = {'typ': 'boxplot', 'achse': [0, 12], 'einheit': 'Punkte', 'reihen': [{'min': 1, 'q1': 3, 'median': 6, 'q3': 9, 'max': 11}]}

UMBAU = {
 'median': {
  'einstieg': 'Sechs Kinder sagen, wie lange ihr Schulweg dauert: 7, 3, 9, 4, 12 und 5 Minuten. Welcher Wert ist typisch? Man ordnet und schaut in die Mitte. Dieser Wert heißt ⟦Median⟧.',
  'woerter': [['geordnet', 'der Größe nach, vom kleinsten zum größten Wert'], ['Median', 'der Wert in der Mitte der geordneten Liste']],
  'bild': _strahl(0, 14, 14, _WEG),
  'schritte': [{'text': 'Geordnet: 3; 4; 5; 7; 9; 12. Das sind 6 Werte.'},
               {'text': 'In der Mitte stehen zwei Werte: 5 und 7.', 'bild': {'bereich': {'von': 5, 'bis': 7}}},
               {'text': 'Die Zahl genau dazwischen: (5 + 7) : 2 = ⟦6⟧ Minuten.', 'bild': {'punkte': [{'wert': w} for w in _WEG] + [{'wert': 6, 'name': 'Median'}]}}],
  'fehler': 'Nicht die Mitte der ungeordneten Liste nehmen. Bei 7; 3; 9; 4; 12 ist der Median nicht 9. Erst ordnen: Er ist ⟦7⟧.',
  'regel': 'Werte ⟦ordnen⟧ und die Mitte nehmen. Bei gerader Anzahl liegt der Median genau zwischen den beiden mittleren Werten.'},
 'kennwerte': {
  'einstieg': 'Fünf Kinder zählen ihre Ferienbücher: 2, 5, 5, 6 und 12. Welche Zahl ist am häufigsten? Wie weit liegen die Werte auseinander? Wie viel wäre es gerecht verteilt? Das sagen ⟦Kennwerte⟧.',
  'woerter': [['Modalwert', 'der häufigste Wert'], ['Spannweite', 'größter minus kleinster Wert'], ['Mittelwert', 'Summe aller Werte geteilt durch ihre Anzahl']],
  'bild': {'typ': 'saeulen', 'einheit': 'Kinder', 'werte': [{'name': '2', 'wert': 1}, {'name': '5', 'wert': 2}, {'name': '6', 'wert': 1}, {'name': '12', 'wert': 1}], 'zahlen': True},
  'schritte': [{'text': 'Die 5 kommt zweimal vor, alle anderen einmal: Modalwert 5.'},
               {'text': 'Spannweite: 12 − 2 = 10 Bücher.'},
               {'text': 'Summe: 2 + 5 + 5 + 6 + 12 = 30.'},
               {'text': 'Mittelwert: 30 : 5 = ⟦6⟧ Bücher pro Kind.'}],
  'fehler': 'Die Spannweite ist nicht 12. Sie ist der ⟦Abstand⟧ zwischen größtem und kleinstem Wert: 12 − 2 = 10.',
  'regel': 'Modalwert: ⟦häufigster Wert⟧. Spannweite: größter minus kleinster Wert. Mittelwert: Summe durch Anzahl.'},
 'mittel_median': {
  'einstieg': 'Fünf Kinder bekommen Taschengeld: 10 €, 12 €, 12 €, 15 € und eines 101 €. Der Mittelwert ist 30 €, mehr als vier von fünf bekommen. Schuld ist ein ⟦Ausreißer⟧.',
  'woerter': [['Ausreißer', 'ein Wert weit weg von allen anderen']],
  'bild': _strahl(0, 110, 11, _GELD),
  'schritte': [{'text': 'Mittelwert: 150 € : 5 = 30 €.', 'bild': {'punkte': [{'wert': w} for w in _GELD] + [{'wert': 30, 'name': 'Mittelwert'}]}},
               {'text': 'Median: In der Mitte der Liste steht 12 €.', 'bild': {'punkte': [{'wert': w} for w in _GELD] + [{'wert': 30, 'name': 'Mittelwert'}, {'wert': 12, 'name': 'Median'}]}},
               {'text': 'Vier Kinder liegen nahe bei 12 €. Der ⟦Median⟧ beschreibt sie besser.'}],
  'fehler': 'Der Mittelwert ist nicht „das, was die meisten bekommen“. Der eine Ausreißer mit 101 € ⟦zieht ihn hoch⟧.',
  'regel': 'Bei Ausreißern beschreibt der ⟦Median⟧ die Mitte besser. Der Mittelwert wird vom Ausreißer weggezogen.'},
 'quartile': {
  'einstieg': 'Sieben Kinder machen ein Quiz: 1, 3, 4, 6, 8, 9 und 11 Punkte. Man teilt die geordnete Liste in vier Viertel. Die Trennstellen heißen ⟦Quartile⟧.',
  'woerter': [['Quartil', 'Trennstelle zwischen zwei Vierteln der geordneten Werte'], ['Q₁', 'unteres Quartil: Median der unteren Hälfte'], ['Q₃', 'oberes Quartil: Median der oberen Hälfte']],
  'bild': _strahl(0, 12, 12, _QUIZ),
  'schritte': [{'text': 'Der Median der sieben Werte ist 6.', 'bild': {'punkte': [{'wert': w} for w in _QUIZ] + [{'wert': 6, 'name': 'Median'}]}},
               {'text': 'Untere Hälfte 1; 3; 4. Ihr Median ist Q₁ = 3.', 'bild': {'bereich': {'von': 1, 'bis': 4}}},
               {'text': 'Obere Hälfte 8; 9; 11. Ihr Median ist ⟦Q₃ = 9⟧.', 'bild': {'bereich': {'von': 8, 'bis': 11}}},
               {'text': 'Mit Q₁ und Q₃ entsteht der Boxplot.', 'bild': _BP_QUIZ}],
  'fehler': 'Q₁ ist nicht ein Viertel vom größten Wert (11 : 4). Es ist eine Trennstelle: Etwa ⟦ein Viertel⟧ der Werte liegt darunter.',
  'regel': 'Q₁ und Q₃ sind die ⟦Mediane der Hälften⟧. Bei ungerader Anzahl gehört der Median zu keiner Hälfte.'},
 'boxplot': {
  'einstieg': '200 Kinder geben ihren Schulweg in Minuten an. 200 Zahlen sind unübersichtlich. Ein Bild aus Box und zwei Linien zeigt die fünf wichtigsten Werte: der ⟦Boxplot⟧.',
  'woerter': [['Box', 'Rechteck von Q₁ bis Q₃; der Strich darin ist der Median'], ['Antenne', 'Linie von der Box bis zum kleinsten bzw. größten Wert']],
  'bild': {'typ': 'boxplot', 'achse': [10, 45], 'einheit': 'min', 'reihen': [{'min': 12, 'q1': 18, 'median': 23, 'q3': 30, 'max': 41}]},
  'schritte': [{'text': 'Ablesen: kleinster Wert 12, Q₁ = 18, Median 23, Q₃ = 30, größter 41.'},
               {'text': 'Die Box reicht von 18 bis 30. Darin liegt die mittlere Hälfte.'},
               {'text': 'Jede Antenne enthält etwa ein Viertel der Kinder.'},
               {'text': 'Links von 30 liegen drei Viertel: ⟦75 %⟧ brauchen höchstens 30 Minuten.'}],
  'fehler': 'Eine lange Antenne heißt nicht, dort seien mehr Kinder. In jeder Antenne liegt ⟦ein Viertel⟧, nur weiter gestreut.',
  'regel': 'Die ⟦Box⟧ enthält die mittlere Hälfte der Werte. Jede Antenne enthält ein Viertel, der Strich ist der Median.'},
 'vergleichen': {
  'einstieg': 'Zwei Klassen laufen dieselbe Strecke, jede Zeit wird gestoppt. Welche Klasse war schneller, welche gleichmäßiger? Zwei Boxplots übereinander zeigen es. So kann man ⟦Daten vergleichen⟧.',
  'woerter': [['Streuung', 'wie weit die Werte auseinanderliegen'], ['gleichmäßig', 'die Werte liegen nah beieinander']],
  'bild': {'typ': 'boxplot', 'achse': [10, 40], 'einheit': 's', 'reihen': [{'name': 'Klasse A', 'min': 19, 'q1': 22, 'median': 24, 'q3': 26, 'max': 31},
                                                                          {'name': 'Klasse B', 'min': 15, 'q1': 18, 'median': 22, 'q3': 27, 'max': 35}]},
  'schritte': [{'text': 'Median A: 24 s, Median B: 22 s. B ist in der Mitte schneller.'},
               {'text': 'Box A reicht von 22 bis 26 s, Box B von 18 bis 27 s.'},
               {'text': 'B hat mehr Streuung. In A sind die Zeiten ⟦gleichmäßiger⟧.'}],
  'fehler': 'Eine größere Spannweite heißt nicht, dass eine Klasse mehr Kinder hat. Sie zeigt nur die ⟦Streuung⟧.',
  'regel': 'Vergleiche zuerst die ⟦Mitte⟧ mit dem Median. Dann die Streuung mit Box und Antennen.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---------- Zehnte Runde (schwer-kl7): schwerere Übungen nach Prüfungsvorbild ----------
# Vorbilder (nur Typ und Niveau, eigene Zahlen und Einkleidung): Bayerischer Mathematik-Test 8 (ISB) 2021 A7 (Median von 13 Werten, Boxplot),
# 2022 A5c (Durchschnittsnote aus Anteilen), 2023 A5 (Median und Mittelwert aus Anteilen, Änderung des Mittelwerts), 2024 A3b (Aussagen zu einem Diagramm
# beurteilen), 2025 A5 (Mittelwert per Tabellenkalkulation) und A6c/d (Median aus Säulendiagramm; Anteile ohne Gesamtzahl). Eigener Zufallsstart.
from _schwer_kl7 import Neu, anhaengen  # noqa: E402


def _med(w):
    w = sorted(w)
    n = len(w)
    return Fr(w[n // 2]) if n % 2 else Fr(w[n // 2 - 1] + w[n // 2], 2)


def _quart(w):
    w = sorted(w)
    n = len(w)
    return _med(w[:n // 2]), _med(w), _med(w[(n + 1) // 2:])


def _bp(achse, einheit, *reihen):
    return {'typ': 'boxplot', 'achse': list(achse), 'einheit': einheit,
            'reihen': [{'name': r[0], 'min': r[1], 'q1': r[2], 'median': r[3], 'q3': r[4], 'max': r[5]} for r in reihen]}


def schwer():
    N = Neu(7095)
    P = 'pruefung'
    K = 'knobel'
    # median
    N.Z('median', 2, 'In einer Klasse sind 25 Kinder; alle haben verschieden viele Punkte. Wie viele Kinder liegen unter dem Median?', 12, '(25 - 1) / 2',
        'Bei 25 Werten ist der 13. Wert der Median. Davor liegen 12 Werte, dahinter auch 12.', 'Welcher Platz in der geordneten Liste ist die Mitte?')
    N.Z('median', 2, 'Die geordnete Liste 4; 7; x; 12; 15 hat den Median 9. Wie groß ist x?', 9, '9',
        'Bei 5 Werten ist der 3. Wert der Median. Der 3. Wert ist x, also x = 9.', 'Welcher Wert steht bei 5 Werten in der Mitte?')
    buch = [('0', 12), ('1', 30), ('2', 25), ('3', 13)]
    liste = [int(k) for k, n in buch for _ in range(n)]
    N.Z('median', 3, 'Das Diagramm zeigt, wie viele Bücher 80 Kinder im letzten Monat gelesen haben. Bestimme den Median.', _med(liste), '1',
        '80 Werte: Der Median liegt zwischen dem 40. und 41. Wert. 0 Bücher: Plätze 1–12, 1 Buch: Plätze 13–42. Beide mittleren Werte sind 1, also Median 1.',
        'Zähle die Säulen von links zusammen, bis du über Platz 40 kommst.', art=P,
        grafik={'typ': 'saeulen', 'einheit': 'Kinder', 'werte': [{'name': f'{k} Bücher' if k != '1' else '1 Buch', 'wert': n} for k, n in buch], 'zahlen': True})
    N.Z('median', 3, 'An einer Schule zahlen 45 % der Kinder 6 € Kopiergeld, 30 % zahlen 9 € und der Rest 12 €. Alle Beträge werden der Größe nach geordnet. Wie groß ist der Median?', 9, '9',
        'Bis 45 % stehen 6-€-Beträge, von 45 % bis 75 % die 9-€-Beträge. Die Mitte (50 %) liegt im 9-€-Bereich: Median 9 €.',
        'Wo in der geordneten Liste liegt die Mitte, also 50 %?', einheit='€', art=P)
    N.Z('median', 3, 'Sieben Zahlen haben den Median 20. Die größte Zahl wird durch 1 000 ersetzt. Wie groß ist der Median jetzt?', 20, '20',
        'Der Median ist der 4. Wert der geordneten Liste. Die größte Zahl bleibt auch als 1 000 auf Platz 7; der 4. Wert ändert sich nicht: 20.',
        'Ändert sich durch die neue größte Zahl die Mitte der Liste?', art=K)
    N.Z('median', 3, 'Zu den Werten 3; 8; 8; 11; 14; 20 kommt ein siebter Wert dazu. Danach ist der Median 11. Wie groß muss der neue Wert mindestens sein?', 11, '11',
        'Mit 7 Werten ist der 4. Wert der Median. Ist der neue Wert mindestens 11, bleibt 11 auf Platz 4. Ist er kleiner (z. B. 10), rutscht er auf Platz 4 und der Median wird kleiner als 11.',
        'Probiere einen neuen Wert unter 11 und einen über 11.')
    # kennwerte
    N.Z('kennwerte', 2, 'Der Mittelwert von 5 Zahlen ist 12. Wie groß ist ihre Summe?', 60, '5 * 12', 'Mittelwert = Summe : Anzahl, also Summe = 12 · 5 = 60.', 'Rechne die Formel für den Mittelwert rückwärts.')
    N.Z('kennwerte', 2, 'Daten: 4; 9; 9; 12; 16. Jeder Wert wird um 3 erhöht. Wie groß ist danach die Spannweite?', 12, '(16 + 3) - (4 + 3)',
        'Größter und kleinster Wert steigen beide um 3: 19 − 7 = 12. Die Spannweite bleibt gleich.', 'Was passiert mit dem Abstand von größtem und kleinstem Wert?')
    N.Z('kennwerte', 3, 'Bei einer Umfrage zur Mathenote gaben 10 % Note 1, 40 % Note 2, 30 % Note 3 und 20 % Note 4 an. Wie groß ist die Durchschnittsnote?', Fr('2.6'), '0.1 * 1 + 0.4 * 2 + 0.3 * 3 + 0.2 * 4',
        'Jede Note mit ihrem Anteil malnehmen: 0,1 · 1 + 0,4 · 2 + 0,3 · 3 + 0,2 · 4 = 0,1 + 0,8 + 0,9 + 0,8 = 2,6.',
        'Stell dir 100 Befragte vor: 10 mal die 1, 40 mal die 2 …', art=P)
    N.Z('kennwerte', 3, 'In den Zellen A1 bis A4 einer Tabellenkalkulation stehen 12, 15, 9 und 20. Welchen Wert zeigt die Zelle mit der Formel =(A1+A2+A3+A4)/4?', 14, '(12 + 15 + 9 + 20) / 4',
        'Die Klammer zuerst: 12 + 15 + 9 + 20 = 56. Dann geteilt durch 4: 14. Das ist der Mittelwert.', 'Erst die Klammer, dann teilen.', art=P)
    N.Z('kennwerte', 3, 'In A1 bis A4 stehen 12, 15, 9 und 20. Jemand tippt für den Mittelwert =A1+A2+A3+A4/4 (ohne Klammer). Um wie viel ist das Ergebnis zu groß?', 27, '(12 + 15 + 9 + 20 / 4) - (12 + 15 + 9 + 20) / 4',
        'Ohne Klammer wird nur A4 geteilt: 12 + 15 + 9 + 5 = 41. Richtig wäre 14. Unterschied: 41 − 14 = 27.', 'Punkt vor Strich: Was wird hier durch 4 geteilt?', art=P)
    N.Z('kennwerte', 3, 'Nach 4 Tests hat jemand im Mittel 7 Punkte. Wie viele Punkte braucht er im 5. Test, damit der Mittelwert aller 5 Tests 8 ist?', 12, '5 * 8 - 4 * 7',
        'Bisher: 4 · 7 = 28 Punkte. Für Mittelwert 8 bei 5 Tests braucht man 5 · 8 = 40 Punkte. Im 5. Test also 40 − 28 = 12.',
        'Rechne mit Summen statt mit Mittelwerten.', art=K)
    # mittel_median
    N.Z('mittel_median', 2, 'Werte: 2; 3; 4; 5; 100. Um wie viel ist der Mittelwert größer als der Median?', Fr('18.8'), '(2 + 3 + 4 + 5 + 100) / 5 - 4',
        'Mittelwert: 114 : 5 = 22,8. Median: 4. Unterschied: 18,8. Der Ausreißer 100 zieht den Mittelwert hoch.', 'Berechne beide Werte einzeln.')
    N.A('mittel_median', 2, 'Der größte Wert einer Datenreihe wird noch größer. Welcher Kennwert ändert sich dadurch sicher NICHT?', 'der Median', ['der Mittelwert', 'die Spannweite', 'das Maximum'],
        'Der Median hängt nur von der Mitte der geordneten Liste ab. Mittelwert, Spannweite und Maximum werden größer.', 'Welcher Kennwert schaut nur auf die Mitte?')
    N.Z('mittel_median', 3, 'An einer Schule zahlen 45 % der Kinder 5 €, 35 % zahlen 7 € und 20 % zahlen 10 €. Um wie viel Euro ist der Mittelwert kleiner als der Median?', Fr('0.3'),
        '7 - (0.45 * 5 + 0.35 * 7 + 0.2 * 10)',
        'Median: 50 % liegt im 7-€-Bereich (45 % bis 80 %), also 7 €. Mittelwert: 0,45 · 5 + 0,35 · 7 + 0,2 · 10 = 2,25 + 2,45 + 2 = 6,70 €. Unterschied: 0,30 €.',
        'Median: Wo liegt die 50-%-Marke? Mittelwert: jeden Betrag mit seinem Anteil malnehmen.', einheit='€', art=P)
    N.A('mittel_median', 3, 'In einem Verein zahlen 60 % der Mitglieder 20 € und 40 % zahlen 30 €. Im nächsten Jahr zahlen je 50 % 20 € und 30 €. Wie ändert sich der durchschnittliche Beitrag?',
        'Er steigt von 24 € auf 25 €.', ['Er bleibt gleich, weil die Beträge gleich bleiben.', 'Er sinkt von 25 € auf 24 €.', 'Er steigt von 25 € auf 30 €.'],
        'Vorher: 0,6 · 20 € + 0,4 · 30 € = 24 €. Nachher: 0,5 · 20 € + 0,5 · 30 € = 25 €. Mehr Mitglieder zahlen den höheren Betrag.', 'Rechne den Durchschnitt für beide Jahre mit den Anteilen.', art=P)
    N.Z('mittel_median', 3, 'Daten: 4; 6; 7; 9; 14. Der größte Wert wird so geändert, dass der Median gleich bleibt und der Mittelwert 12 wird. Welchen Wert bekommt er?', 34, '5 * 12 - (4 + 6 + 7 + 9)',
        'Für Mittelwert 12 braucht man die Summe 60. Die anderen vier ergeben 26, also wird der größte Wert 34. Der Median (7) bleibt, weil sich die Mitte nicht ändert.',
        'Welche Summe brauchen alle 5 Werte für den Mittelwert 12?', art=K)
    N.Z('mittel_median', 3, 'Sechs Werte haben den Mittelwert 15. Der Ausreißer 40 wird entfernt. Wie groß ist der Mittelwert der restlichen fünf Werte?', 10, '(6 * 15 - 40) / 5',
        'Summe vorher: 6 · 15 = 90. Ohne 40: 50. Neuer Mittelwert: 50 : 5 = 10.', 'Rechne mit der Summe aller Werte.')
    # quartile
    N.Z('quartile', 2, 'Werte: 2; 4; 6; 8; 10; 12; 14; 16. Bestimme das untere Quartil.', 5, '(4 + 6) / 2',
        'Untere Hälfte: 2; 4; 6; 8. Ihr Median ist (4 + 6) : 2 = 5.', 'Teile die 8 Werte in zwei Hälften.')
    N.Z('quartile', 2, 'Werte: 10; 20; 30; 40; 50; 60; 70. Bestimme den Quartilsabstand Q₃ − Q₁.', 40, '60 - 20',
        'Median 40 (gehört zu keiner Hälfte). Untere Hälfte 10; 20; 30 → Q₁ = 20. Obere Hälfte 50; 60; 70 → Q₃ = 60. Q₃ − Q₁ = 40.', 'Bei 7 Werten bleibt der Median beim Teilen außen vor.')
    d13 = [3, 5, 5, 6, 8, 9, 11, 12, 12, 14, 15, 18, 21]
    q1, me, q3 = _quart(d13)
    assert (q1, me, q3) == (Fr(11, 2), 11, Fr(29, 2))
    N.Z('quartile', 3, '13 Kinder notieren ihre Bildschirmzeit am Wochenende (in Stunden): 3; 5; 5; 6; 8; 9; 11; 12; 12; 14; 15; 18; 21. Bestimme das obere Quartil.', q3, '(14 + 15) / 2',
        'Median: 7. Wert = 11. Obere Hälfte (ohne Median): 12; 12; 14; 15; 18; 21. Ihr Median: (14 + 15) : 2 = 14,5.', 'Erst den Median finden, dann die obere Hälfte ohne ihn betrachten.', einheit='h', art=P)
    N.Z('quartile', 3, 'Bildschirmzeiten (in Stunden): 3; 5; 5; 6; 8; 9; 11; 12; 12; 14; 15; 18; 21. Wie viele der 13 Werte liegen innerhalb der Box, also zwischen Q₁ und Q₃?', 7,
        '7', 'Q₁ = (5 + 6) : 2 = 5,5 und Q₃ = 14,5. Dazwischen liegen 6; 8; 9; 11; 12; 12; 14 – das sind 7 Werte.', 'Bestimme Q₁ und Q₃ und zähle die Werte dazwischen.', art=P)
    assert sum(1 for v in d13 if q1 < v < q3) == 7
    N.Z('quartile', 3, 'Die geordnete Liste 4; 6; x; 10; 13; 15; 18; 20 hat das untere Quartil 7. Wie groß ist x?', 8, '2 * 7 - 6',
        'Untere Hälfte: 4; 6; x; 10. Q₁ = (6 + x) : 2 = 7, also 6 + x = 14 und x = 8.', 'Welche beiden Werte bestimmen das untere Quartil?', art=K)
    d12 = [1, 2, 4, 4, 5, 7, 8, 10, 11, 11, 15, 20]
    a1, _, a3 = _quart(d12)
    N.Z('quartile', 3, 'Werte: 1; 2; 4; 4; 5; 7; 8; 10; 11; 11; 15; 20. Bestimme den Quartilsabstand Q₃ − Q₁.', a3 - a1, '11 - 4',
        'Untere Hälfte 1; 2; 4; 4; 5; 7 → Q₁ = (4 + 4) : 2 = 4. Obere Hälfte 8; 10; 11; 11; 15; 20 → Q₃ = (11 + 11) : 2 = 11. Q₃ − Q₁ = 7.', 'Teile in zwei Hälften zu je 6 Werten.')
    # boxplot
    B1 = _bp((0, 22), 'Punkte', ('Test', 2, 6, 9, 13, 20))
    N.Z('boxplot', 2, 'Der Boxplot zeigt die Punkte in einem Test. Wie groß ist die Spannweite?', 18, '20 - 2', 'Maximum 20, Minimum 2: Spannweite 20 − 2 = 18 Punkte.', 'Spannweite = Maximum − Minimum.', grafik=B1)
    N.Z('boxplot', 2, 'Der Boxplot zeigt die Punkte in einem Test. Etwa wie viel Prozent der Werte liegen zwischen 6 und 20 Punkten?', 75, '25 + 25 + 25',
        'Von Q₁ (6) bis zum Maximum (20): Box (50 %) und rechte Antenne (25 %) zusammen 75 %.', 'Jeder Abschnitt des Boxplots enthält etwa ein Viertel.', einheit='%', grafik=B1)
    B2 = _bp((0, 65), 'min', ('Schulweg', 2, 8, 15, 25, 60))
    N.Z('boxplot', 3, '200 Kinder wurden nach ihrem Schulweg gefragt (in Minuten, siehe Boxplot). Etwa wie viele brauchen zwischen 8 und 15 Minuten?', 50, '200 / 4',
        'Von Q₁ (8) bis zum Median (15) liegt etwa ein Viertel der Werte: 200 : 4 = 50 Kinder.', 'Welcher Teil des Boxplots ist das, und welcher Anteil gehört dazu?', einheit='Kinder', art=P, grafik=B2)
    N.A('boxplot', 3, 'Welche Aussage passt NICHT zum Boxplot (Schulweg von 200 Kindern in Minuten)?', 'Die meisten Kinder brauchen 25 bis 60 Minuten, weil die rechte Antenne so lang ist.',
        ['Die Hälfte der Kinder braucht höchstens 15 Minuten.', 'Etwa ein Viertel braucht mehr als 25 Minuten.', 'Mindestens drei Viertel brauchen 8 Minuten oder mehr.'],
        'Die rechte Antenne enthält nur etwa ein Viertel der Werte – sie ist lang, weil diese Werte weit gestreut sind, nicht weil es viele sind.',
        'Eine lange Antenne heißt: weit gestreut, nicht: viele Werte.', art=P, grafik=B2)
    kand = {'1; 2; 4; 5; 5; 6; 8; 9': [1, 2, 4, 5, 5, 6, 8, 9], '1; 3; 3; 5; 6; 7; 7; 9': [1, 3, 3, 5, 6, 7, 7, 9],
            '1; 2; 3; 5; 5; 7; 8; 9': [1, 2, 3, 5, 5, 7, 8, 9], '1; 3; 5; 5; 5; 5; 7; 9': [1, 3, 5, 5, 5, 5, 7, 9]}
    ziel = (3, 5, 7)
    passend = [k for k, v in kand.items() if _quart(v) == ziel and min(v) == 1 and max(v) == 9]
    assert passend == ['1; 2; 4; 5; 5; 6; 8; 9']
    N.A('boxplot', 3, 'Ein Boxplot zu 8 Werten zeigt: Minimum 1, Q₁ = 3, Median 5, Q₃ = 7, Maximum 9. Welche Datenreihe passt dazu?', passend[0], [k for k in kand if k != passend[0]],
        '1; 2; 4; 5 | 5; 6; 8; 9: Q₁ = (2 + 4) : 2 = 3, Median (5 + 5) : 2 = 5, Q₃ = (6 + 8) : 2 = 7. Bei den anderen stimmt jeweils ein Kennwert nicht.',
        'Prüfe bei jeder Reihe Q₁, Median und Q₃.', art=K, grafik=_bp((0, 10), '', ('Daten', 1, 3, 5, 7, 9)))
    N.Z('boxplot', 3, 'Zu einem Boxplot gehören 40 Werte. Etwa wie viele Werte liegen auf der rechten Antenne (zwischen Q₃ und dem Maximum)?', 10, '40 / 4',
        'Jede Antenne enthält etwa ein Viertel der Werte: 40 : 4 = 10.', 'Wie viel Prozent der Werte gehören zu einer Antenne?')
    # vergleichen
    V = _bp((0, 22), 'Punkte', ('7a', 4, 9, 12, 15, 19), ('7b', 2, 7, 13, 17, 20))
    N.A('vergleichen', 2, 'Die Boxplots zeigen die Punkte zweier Klassen. In welcher Klasse hat mindestens die Hälfte der Kinder 13 Punkte oder mehr?', 'in der 7b',
        ['in der 7a', 'in beiden Klassen', 'in keiner Klasse'],
        'Median der 7b: 13 – mindestens die Hälfte hat 13 oder mehr. Median der 7a: 12 – dort hat höchstens die Hälfte mehr als 12.', 'Vergleiche die Mediane mit 13.', grafik=V)
    N.A('vergleichen', 2, 'Welche Größe vergleicht man, um zu sagen, in welcher Gruppe die mittlere Hälfte der Werte enger beieinanderliegt?', 'den Quartilsabstand (Länge der Box)',
        ['den Median', 'das Maximum', 'den Modalwert'], 'Die Box enthält die mittlere Hälfte. Je kürzer sie ist, desto enger liegen diese Werte zusammen.', 'Welcher Teil des Boxplots zeigt die mittlere Hälfte?')
    N.A('vergleichen', 3, 'Welche Aussage zu den beiden Boxplots (Punkte der 7a und 7b) ist richtig?', 'In der 7b liegen die mittleren 50 % weiter auseinander als in der 7a.',
        ['Die 7a hat den größeren Median.', 'In der 7a hat niemand mehr als 15 Punkte.', 'Die 7b hat weniger Kinder, weil ihre Box länger ist.'],
        'Quartilsabstand 7a: 15 − 9 = 6, 7b: 17 − 7 = 10. Median 7a (12) < 7b (13). In der 7a gibt es Werte bis 19. Über die Anzahl der Kinder sagt ein Boxplot nichts.',
        'Prüfe jede Aussage am Bild: Median, Box, Antennen.', art=P, grafik=V)
    N.Z('vergleichen', 3, 'Die 7a hat 28 Kinder, die 7b 20 Kinder. Bei beiden liegt das obere Quartil bei 15 Punkten. Etwa wie viele Kinder beider Klassen zusammen haben mehr als 15 Punkte?', 12, '28 / 4 + 20 / 4',
        'Über Q₃ liegt jeweils etwa ein Viertel: 28 : 4 = 7 und 20 : 4 = 5. Zusammen etwa 12 Kinder. Gleiche Anteile bedeuten bei verschieden großen Klassen verschiedene Anzahlen.',
        'Rechne für jede Klasse ein Viertel aus.', einheit='Kinder', art=P)
    N.A('vergleichen', 3, 'Zwei Klassen haben im Test denselben Median und dieselbe Spannweite. Folgt daraus, dass die Ergebnisse gleich verteilt sind?', 'Nein: Die Quartile und damit die Boxen können verschieden sein.',
        ['Ja: Median und Spannweite legen alles fest.', 'Ja, wenn die Klassen gleich groß sind.', 'Nein: Die Klassen haben verschiedene Mittelwerte, also sind sie sicher verschieden.'],
        'Beispiel: Min 0, Median 10, Max 20 bei beiden – aber Q₁/Q₃ = 8/12 in der einen und 3/17 in der anderen Klasse. Die Verteilung ist ganz anders.',
        'Welche Kennwerte des Boxplots sind dann noch frei?', art=K)
    N.Z('vergleichen', 3, 'Um wie viele Punkte ist der Quartilsabstand der 7b größer als der der 7a (siehe Boxplots)?', 4, '(17 - 7) - (15 - 9)',
        '7a: 15 − 9 = 6. 7b: 17 − 7 = 10. Unterschied: 4 Punkte.', 'Quartilsabstand = Q₃ − Q₁ für jede Klasse.', grafik=V)
    return N


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('daten.boxplot', 13_7_7)
# a) nur längere Rechnung mit mehr Zahlen, kein anderer Gedanke
for _t in ['Minuten Hausaufgaben von 8 Kindern: 3; 24; 20; 13; 15; 1; 6; 24. Berechne das arithmetische Mittel.',
           'Gelesene Bücher im Jahr von 6 Kindern: 5; 19; 2; 2; 13; 25. Berechne das arithmetische Mittel.',
           'Tore in der Saison von 10 Kindern: 14; 3; 20; 13; 16; 21; 7; 24; 22; 7. Berechne das arithmetische Mittel.']:
    BF.stufe('kennwerte', _t, 2)
# a) Lösung „beide fast gleich“ – eher Stufe 2
BF.stufe('mittel_median', 'Wartezeiten an einer Kasse (min): 10; 10; 8; 9; 7; 10. Welcher Wert beschreibt die typische Mitte besser?', 2)
BF.nicht_umgesetzt('vergleichen: Stufe 1 und 2 gleich gebaut („Welche Aussage ist richtig?“ zu zwei Boxplots)',
                   'Lösungen richtig; Stufe 2 fragt zusätzlich nach Streuung und Gesamtvergleich. Ein einzelner falsch eingestufter Fall ist nicht benannt.')

# ---- BEFUNDE ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Teil A: Gesamtdurchsicht Klasse 7, siehe _durchsicht_kl7.py) ----
# Hauptmangel: Stufen unterschieden sich oft nur in der Länge der Datenliste. Umgestuft; bei quartile neue Stufe-3-Gedanken (Anteile, Wirkung von Änderungen).
from _durchsicht_kl7 import Durchsicht, durchsicht_datei  # noqa: E402

DS = Durchsicht('daten.boxplot', 19_7_7)
# median: Stufe 2 = Stufe 1 mit längerer Liste, Stufe 3 = noch längere Liste
for _t in ['Seiten gelesen pro Tag: 27; 48; 58; 38; 17; 40; 47; 59; 54; 45; 59. Bestimme den Median.',
           'Punkte in einem Test (höchstens 30): 2; 12; 9; 19; 16; 19. Bestimme den Median.',
           'Seiten gelesen pro Tag: 23; 4; 45; 14; 27; 31; 23; 6; 10; 38. Bestimme den Median.']:
    DS.stufe('median', _t, 1)
for _t in ['Körpergröße in cm: 156; 170; 143; 160; 158; 157; 161; 149; 138; 150; 149; 173; 155; 158; 164. Bestimme den Median.',
           'Seiten gelesen pro Tag: 38; 44; 20; 54; 12; 38; 38; 5; 33; 30; 56; 21. Bestimme den Median.']:
    DS.stufe('median', _t, 2)
DS.neu('median', 2, DS.Z('Zu den Werten 4; 6; 9; 11 kommt der Wert 20 dazu. Um wie viel steigt der Median?', 1.5, '9 - (6 + 9) / 2',
                         'Vorher: (6 + 9) : 2 = 7,5. Nachher 4; 6; 9; 11; 20 mit Median 9. Er steigt um 1,5.', 'Bestimme den Median vorher und nachher.'))
# kennwerte: „Bestimme Modalwert/Spannweite“ ist das Beispiel mit anderen Zahlen → Stufe 1
for _t in ['Minuten Hausaufgaben von 6 Kindern: 7; 24; 9; 24; 4; 10. Bestimme die Spannweite.',
           'Tore in der Saison von 6 Kindern: 12; 8; 24; 19; 6; 6. Bestimme den Modalwert.',
           'Liegestütze in einer Minute von 8 Kindern: 11; 15; 14; 21; 17; 18; 25; 25. Bestimme den Modalwert.',
           'Euro Taschengeld von 6 Kindern: 14; 12; 11; 9; 10; 12. Bestimme den Modalwert.',
           'Gelesene Bücher im Jahr von 5 Kindern: 1; 9; 20; 9; 16. Bestimme den Modalwert.',
           'Gelesene Bücher im Jahr von 5 Kindern: 6; 14; 22; 10; 6. Bestimme die Spannweite.']:
    DS.stufe('kennwerte', _t, 1)
# mittel_median: „Welcher Wert beschreibt die Mitte besser?“ steht genauso in Stufe 2
DS.stufe('mittel_median', 'Werte: 12; 10; 17; 90; 20. Welcher Wert beschreibt die typische Mitte besser?', 2)
DS.stufe('mittel_median', 'Wartezeiten an einer Kasse (min): 7; 4; 11; 5; 9. Welcher Wert beschreibt die typische Mitte besser?', 2)
# quartile: Stufe 3 waren vor allem längere Listen → Stufe 2; neue Stufe-3-Gedanken
for _t in ['Werte: 3; 6; 42; 32; 15; 19; 45; 22; 43; 30; 3; 18; 45; 25; 38. Bestimme das untere Quartil.',
           'Werte: 32; 22; 22; 17; 18; 42; 47; 1; 37; 19; 11; 36; 8; 4; 50. Bestimme den Quartilsabstand Q₃ − Q₁.',
           'Werte: 23; 36; 30; 13; 33; 46; 9; 10; 37; 48; 26; 31; 26. Bestimme das obere Quartil.',
           'Werte: 48; 32; 47; 2; 23; 5; 25; 38; 10; 48; 24; 5; 47; 40; 36. Bestimme das untere Quartil.',
           '13 Kinder notieren ihre Bildschirmzeit am Wochenende (in Stunden): 3; 5; 5; 6; 8; 9; 11; 12; 12; 14; 15; 18; 21. Bestimme das obere Quartil.',
           'Werte: 1; 2; 4; 4; 5; 7; 8; 10; 11; 11; 15; 20. Bestimme den Quartilsabstand Q₃ − Q₁.']:
    DS.stufe('quartile', _t, 2)
DS.neu('quartile', 3, DS.Z('Eine Datenreihe hat 20 verschiedene Werte. Wie viele davon sind kleiner als das untere Quartil Q₁?', 5, '20 / 4',
                           'Untere Hälfte: die 10 kleinsten Werte. Q₁ liegt zwischen dem 5. und 6. Wert, also sind genau 5 Werte kleiner.',
                           'Bei 20 Werten hat die untere Hälfte 10 Werte. Wo liegt deren Mitte?'))
DS.neu('quartile', 3, DS.A('Eine Datenreihe hat 7 Werte. Der größte Wert wird verdoppelt. Was passiert mit dem oberen Quartil Q₃?',
                           'Q₃ bleibt gleich: Es ist der mittlere der drei oberen Werte, nicht der größte.',
                           ['Q₃ verdoppelt sich ebenfalls.', 'Q₃ wird größer, aber nicht doppelt so groß.', 'Q₃ wird kleiner.'],
                           'Bei 7 Werten ist die obere Hälfte der 5., 6. und 7. Wert; Q₃ ist der 6. Wert. Der 7. (größte) Wert ändert ihn nicht.',
                           'Welcher Wert der geordneten Liste ist bei 7 Werten Q₃?'))
DS.neu('quartile', 3, DS.Z('Eine Datenreihe hat Q₁ = 12 und Q₃ = 20. Jeder Wert wird um 5 erhöht. Wie groß ist jetzt der Quartilsabstand?', 8, '(20 + 5) - (12 + 5)',
                           'Beide Quartile wachsen um 5: 17 und 25. Der Abstand bleibt 25 − 17 = 8.', 'Was passiert mit Q₁ und Q₃, wenn alle Werte gleich stark wachsen?'))
# vergleichen: „gleichmäßiger“/„insgesamt höher“ stehen schon in Stufe 2; eine Stufe-2-Aufgabe ist gleich gebaut wie Stufe 1
DS.stufe('vergleichen', 'Ergebnisse zweier Klassen beim 1 000-m-Lauf (in s), siehe Boxplots. In welcher Klasse sind die Leistungen gleichmäßiger?', 2)
DS.stufe('vergleichen', 'Ergebnisse zweier Klassen beim Hochsprung (in cm), siehe Boxplots. Welche Klasse sprang insgesamt höher?', 2, anzahl=2)
DS.stufe('vergleichen', 'Ergebnisse zweier Klassen beim 1 000-m-Lauf (in s), siehe Boxplots. Welche Aussage ist richtig?', 1, enthaelt='"s": 2')
# ---- DURCHSICHT ENDE ----


if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Kennwerte', ['median', 'kennwerte', 'mittel_median']), ('Quartile und Boxplot', ['quartile', 'boxplot']), ('Vergleichen', ['vergleichen'])],
         'Median, Modalwert, Spannweite, Mittelwert und Quartile bestimmen, Boxplots lesen und zuordnen und Datensätze vergleichen und beurteilen.',
         ['Median: Mitte der geordneten Liste.', 'Q₁ und Q₃: Mediane der unteren und oberen Hälfte.', 'Box: mittlere Hälfte der Daten; jede Antenne: ein Viertel.',
          'Bei Ausreißern ist der Median aussagekräftiger als der Mittelwert.'],
         offen=['Quartile werden als Median der unteren bzw. oberen Hälfte bestimmt (bei ungerader Anzahl ohne den Median). Schulbücher verwenden teils andere Verfahren; bitte mit dem Buch des Kindes abgleichen.'])
    anhaengen(META['thema_schluessel'], schwer())
    befunde_datei(META['thema_schluessel'], BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden
    durchsicht_datei(META['thema_schluessel'], DS)  # Neunzehnte Runde: zuletzt
