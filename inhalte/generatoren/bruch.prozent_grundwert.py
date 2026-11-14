#!/usr/bin/env python3
"""Thema bruch.prozent_grundwert – Vermehrter und verminderter Grundwert (Gymnasium Bayern, Klasse 7)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl7 import A, Z, baue, cz, eur, ist_endlich, zt  # noqa: E402

META = {'thema_schluessel': 'bruch.prozent_grundwert', 'thema_id': 94, 'block_id': 108, 'klasse': {'gym_by': 7, 'rs_by': 7}}

ETAPPEN = [
    {'lernziel': 'faktor', 'titel': 'Den Wachstumsfaktor bestimmen',
     'regel': 'Steigt ein Wert um p %, ist der neue Wert (100 + p) % des alten: Man multipliziert mit dem ⟦Wachstumsfaktor 1 + p/100⟧. Sinkt er um p %, multipliziert man mit ⟦1 − p/100⟧.',
     'schritte': ['Erhöhung um 15 %: 100 % + 15 % = 115 %', 'Faktor ⟦1,15⟧', 'Senkung um 15 %: 100 % − 15 % = 85 %, Faktor ⟦0,85⟧'],
     'fehler': 'Der Faktor für „um 15 % mehr“ ist nicht 0,15. Mit 0,15 erhältst du nur die ⟦Zunahme⟧, nicht den neuen Wert. Der neue Wert braucht 1,15.',
     '_verbot': ['um 15 %']},
    {'lernziel': 'vermehrt', 'titel': 'Den vermehrten Grundwert berechnen',
     'regel': 'Vermehrter Grundwert = ⟦Grundwert · (1 + p/100)⟧. So rechnest du in einem Schritt, statt erst die Zunahme auszurechnen und dann zu addieren.',
     'schritte': ['Ein Fahrrad kostet 480 €, der Preis steigt um 5 %.', 'Neuer Preis: 480 € · 1,05', '= ⟦504 €⟧'],
     'probe': 'Zunahme 5 % von 480 € = 24 €; 480 € + 24 € = 504 € ✓',
     'fehler': '480 € + 5 = 485 € ist falsch: 5 % sind ⟦nicht 5 Euro⟧, sondern 5 Hundertstel des Grundwerts.',
     '_verbot': ['480 €']},
    {'lernziel': 'vermindert', 'titel': 'Den verminderten Grundwert berechnen',
     'regel': 'Verminderter Grundwert = ⟦Grundwert · (1 − p/100)⟧. Typisch sind ⟦Rabatt⟧ und Preissenkungen.',
     'schritte': ['Eine Jacke kostet 120 €, es gibt 30 % Rabatt.', 'Faktor: 1 − 0,30 = 0,70', '120 € · 0,7 = ⟦84 €⟧'],
     'fehler': '120 € · 0,3 = 36 € ist nicht der neue Preis, sondern der ⟦Rabatt⟧. Zu zahlen sind 120 € − 36 € = 84 €.',
     '_verbot': ['120 €']},
    {'lernziel': 'zurueck', 'titel': 'Zurück zum Grundwert',
     'regel': 'Kennst du den vermehrten oder verminderten Wert, ⟦teilst⟧ du durch den Faktor: Grundwert = neuer Wert : (1 ± p/100).',
     'schritte': ['Ein Preis mit 19 % Mehrwertsteuer ist 59,50 €.', 'Netto · 1,19 = 59,50 € → Netto = 59,50 € : 1,19', '= ⟦50 €⟧'],
     'probe': '50 € · 1,19 = 59,50 € ✓',
     'fehler': 'Der Nettopreis ist nicht 59,50 € − 19 % von 59,50 € = 48,20 €. Die 19 % beziehen sich auf den ⟦Nettopreis⟧, nicht auf den Endpreis. Darum wird geteilt.',
     '_verbot': ['59,50 €']},
    {'lernziel': 'prozentsatz', 'titel': 'Um wie viel Prozent geändert?',
     'regel': 'Teile den neuen Wert durch den ⟦alten⟧ Wert. Liegt der Faktor über 1, ist es eine Zunahme, sonst eine Abnahme: ⟦p % = (Faktor − 1) · 100 %⟧.',
     'schritte': ['Preis vorher 40 €, nachher 46 €', '46 : 40 = 1,15', 'Zunahme um ⟦15 %⟧'],
     'fehler': 'Steigt der Preis von 40 € auf 46 €, sind es nicht 6 %. Die Änderung 6 € wird auf den ⟦alten Wert 40 €⟧ bezogen: 6 : 40 = 0,15 = 15 %.',
     '_verbot': ['vorher 40 €']},
    {'lernziel': 'mehrfach', 'titel': 'Mehrere Änderungen nacheinander',
     'regel': 'Bei mehreren Änderungen nacheinander werden die ⟦Faktoren multipliziert⟧, nicht die Prozentsätze addiert.',
     'schritte': ['200 €, erst +10 %, dann −10 %', '200 € · 1,1 · 0,9 = 200 € · 0,99', '= ⟦198 €⟧ – weniger als vorher!'],
     'fehler': '+10 % und dann −10 % heben sich nicht auf: Die −10 % beziehen sich auf den ⟦schon erhöhten⟧ Preis 220 €. Ergebnis 198 €, nicht 200 €.',
     '_verbot': ['200 €, erst']},
    {'lernziel': 'argumente', 'titel': 'Aussagen zu Prozenten prüfen',
     'regel': 'Prüfe eine Aussage ⟦rechnerisch⟧ (mathematisches Argument). Gründe wie „das klingt fair“ oder „das macht jeder Laden so“ sind ⟦außermathematische⟧ Argumente – sie beweisen rechnerisch nichts.',
     'schritte': ['Aussage: „20 % Rabatt und dann noch 10 % sind zusammen 30 %.“', 'Faktor: 0,8 · 0,9 = 0,72 → Ersparnis 28 %', 'Die Aussage ist ⟦falsch⟧.'],
     'fehler': '„Der Laden wirbt doch mit 30 %, also stimmt es“ ist ⟦kein mathematisches⟧ Argument. Nur die Rechnung entscheidet.',
     '_verbot': ['20 % Rabatt und dann noch 10 %']},
]

PROZ = {1: [5, 10, 20, 25, 30, 40, 50], 2: [2, 3, 4, 5, 8, 12, 15, 16, 18, 19, 35, 45, 60, 75], 3: [Fr(5, 2), Fr(15, 2), 7, 11, 13, 17, 19, 22, 24, 28, 33, 36]}


def pt(p): return zt(p) + ' %'


def geld_ok(x): return ist_endlich(x) and Fr(x) * 100 == int(Fr(x) * 100)


def g_faktor(R, st):
    p = Fr(R.choice(PROZ[st]))
    rauf = R.random() < .5
    q = 1 + p / 100 if rauf else 1 - p / 100
    if st == 3 and R.random() < .5:
        # umgekehrt: Faktor → Prozent
        return Z(f'Ein Wert wird mit dem Faktor {zt(q)} multipliziert. Um wie viel Prozent ändert er sich? (Zunahme positiv, Abnahme negativ angeben)',
                 (q - 1) * 100, f'({cz(q)} - 1) * 100', f'{zt(q)} = {zt(q * 100)} %. Änderung: {zt(q * 100)} % − 100 % = {zt((q - 1) * 100)} %.',
                 'Schreibe den Faktor als Prozentzahl und vergleiche mit 100 %.', '%')
    return Z(f'Ein Wert wird um {pt(p)} {"erhöht" if rauf else "verringert"}. Mit welchem Faktor multiplizierst du?', q, f'1 {"+" if rauf else "-"} {cz(p)} / 100',
             f'100 % {"+" if rauf else "−"} {pt(p)} = {zt(q * 100)} % = {zt(q)}.', 'Rechne erst 100 % plus oder minus p %, dann in eine Dezimalzahl umwandeln.')


# (Anfang, Satz mit {p}, Einheit, größter sinnvoller Prozentsatz)
KONTEXT_RAUF = [('Ein Fahrrad kostet', 'Der Preis steigt um {p}.', '€', 20), ('Eine Monatsmiete beträgt', 'Sie wird um {p} erhöht.', '€', 15),
                ('Ein Netto-Preis ist', 'Dazu kommen {p} Mehrwertsteuer.', '€', 19), ('Ein Verein hat', 'Die Mitgliederzahl wächst um {p}.', 'Mitglieder', 50),
                ('Ein Sparguthaben beträgt', 'In einem Jahr kommen {p} Zinsen dazu.', '€', 5)]
KONTEXT_RUNTER = [('Eine Jacke kostet', 'Im Ausverkauf gibt es {p} Rabatt.', '€', 70), ('Ein Handy kostet', 'Der Preis sinkt um {p}.', '€', 40),
                  ('Ein Auto hat einen Wert von', 'In einem Jahr sinkt der Wert um {p}.', '€', 25), ('Eine Schule hat', 'Die Schülerzahl sinkt um {p}.', 'Schüler', 15),
                  ('Ein Tank enthält', 'Der Inhalt nimmt um {p} ab.', 'Liter', 80)]


BEREICH = {'Ein Fahrrad kostet': [380, 450, 480, 560, 640, 720, 850, 900, 1200], 'Eine Monatsmiete beträgt': [480, 560, 640, 750, 800, 900, 950, 1100, 1200],
           'Ein Netto-Preis ist': [20, 40, 50, 60, 80, 120, 150, 200, 240, 350, 400, 500], 'Ein Sparguthaben beträgt': [800, 1200, 1500, 2000, 2400, 3000, 4000, 5000],
           'Eine Jacke kostet': [40, 60, 80, 95, 120, 150, 180, 220, 250], 'Ein Handy kostet': [180, 240, 300, 360, 450, 500, 640, 800, 900],
           'Ein Auto hat einen Wert von': [8000, 12000, 15000, 18000, 20000, 24000, 30000]}


def grund(R, st, einheit, k0=''):
    if einheit in ('Mitglieder', 'Schüler'): return Fr(R.choice([200, 250, 300, 400, 500, 600, 800, 1000, 1200]))
    if einheit == 'Liter': return Fr(R.choice([40, 50, 60, 80]))
    return Fr(R.choice(BEREICH[k0]))


def g_wert(R, st, rauf):
    for _ in range(500):
        k = R.choice(KONTEXT_RAUF if rauf else KONTEXT_RUNTER)
        if k[1].startswith('Dazu kommen'): p = Fr(19)
        elif k[0].startswith('Ein Sparguthaben'): p = Fr(R.choice([1, Fr(3, 2), 2, Fr(5, 2), 3, 4, 5]))
        else: p = Fr(R.choice([x for x in PROZ[st] if x <= k[3]] or [5, 10]))
        G = grund(R, st, k[2], k[0])
        neu = G * (1 + p / 100) if rauf else G * (1 - p / 100)
        if k[2] in ('Mitglieder', 'Schüler'):
            if neu.denominator != 1: continue
        elif not geld_ok(neu): continue
        break
    g_txt = (eur(G) + ' €') if k[2] == '€' else f'{zt(G)} {k[2]}'
    q = 1 + p / 100 if rauf else 1 - p / 100
    neu_txt = eur(neu) if k[2] == '€' else zt(neu)
    frage = ('Wie hoch ist der neue Preis?' if k[2] == '€' and 'kostet' in k[0] else 'Wie hoch ist der Preis mit Mehrwertsteuer?' if 'Netto' in k[0]
             else 'Wie hoch ist das Guthaben danach?' if 'Spar' in k[0] else 'Wie groß ist der neue Wert?')
    return Z(f'{k[0]} {g_txt}. {k[1].format(p=pt(p))} {frage}', neu, f'{cz(G)} * (1 {"+" if rauf else "-"} {cz(p)} / 100)',
             f'Faktor {zt(q)}: {zt(G)} · {zt(q)} = {neu_txt} {k[2]}.', 'Bestimme den Faktor 1 ± p/100 und multipliziere.', k[2] if k[2] != '€' else '€')


def g_vermehrt(R, st):
    if st == 3 and R.random() < .4:
        # Zunahme + neuer Wert vergleichen: Zinsen über zwei Jahre ohne Zinseszins? -> Lohn mit Erhöhung in € und %
        G = Fr(R.choice([2400, 2800, 3200, 3600]))
        p = Fr(R.choice([2, 3, 4, 5])); extra = Fr(R.choice([50, 80, 100, 120]))
        neu = G * (1 + p / 100) + extra
        return Z(f'Ein Monatsgehalt von {eur(G)} € steigt erst um {pt(p)}, danach kommt eine feste Zulage von {eur(extra)} € dazu. Wie hoch ist das neue Gehalt?', neu,
                 f'{cz(G)} * (1 + {cz(p)} / 100) + {cz(extra)}', f'{eur(G)} · {zt(1 + p / 100)} = {eur(G * (1 + p / 100))} €; + {eur(extra)} € = {eur(neu)} €.',
                 'Erst die prozentuale Erhöhung, dann die feste Zulage.', '€')
    return g_wert(R, st, True)


def g_vermindert(R, st):
    if st == 3 and R.random() < .4:
        G = Fr(R.choice([80, 120, 150, 240, 360])); p = Fr(R.choice([10, 20, 25, 30])); s = Fr(R.choice([2, 3]))
        neu = G * (1 - p / 100) * (1 - s / 100)
        if not geld_ok(neu): return g_vermindert(R, st)
        return Z(f'Ein Sofa kostet {eur(G)} €. Es gibt {pt(p)} Rabatt, und bei Barzahlung zusätzlich {pt(s)} Skonto auf den reduzierten Preis. Was zahlt man bar?', neu,
                 f'{cz(G)} * (1 - {cz(p)} / 100) * (1 - {cz(s)} / 100)', f'{eur(G)} · {zt(1 - p / 100)} = {eur(G * (1 - p / 100))} €; · {zt(1 - s / 100)} = {eur(neu)} €.',
                 'Zwei Abzüge nacheinander: zwei Faktoren.', '€')
    return g_wert(R, st, False)


def g_zurueck(R, st):
    for _ in range(500):
        rauf = R.random() < .5
        p = Fr(19) if (rauf and R.random() < .4) else Fr(R.choice(PROZ[min(st, 2)]))
        G = Fr(R.choice([20, 25, 40, 50, 60, 80, 100, 120, 150, 200, 240, 300, 360, 400, 500]))
        if st == 3: G = G + Fr(R.choice([0, 5, 10, 15]))
        neu = G * (1 + p / 100) if rauf else G * (1 - p / 100)
        if geld_ok(neu): break
    q = 1 + p / 100 if rauf else 1 - p / 100
    if rauf and p == 19:
        text = f'Ein Preis mit 19 % Mehrwertsteuer beträgt {eur(neu)} €. Wie hoch ist der Preis ohne Mehrwertsteuer?'
    elif rauf:
        text = f'Nach einer Erhöhung um {pt(p)} kostet eine Ware {eur(neu)} €. Wie viel kostete sie vorher?'
    else:
        text = f'Nach {pt(p)} Rabatt kostet eine Ware {eur(neu)} €. Wie viel kostete sie ursprünglich?'
    return Z(text, G, f'{cz(neu)} / (1 {"+" if rauf else "-"} {cz(p)} / 100)', f'Grundwert · {zt(q)} = {eur(neu)} € → Grundwert = {eur(neu)} € : {zt(q)} = {eur(G)} €.',
             'Der neue Wert ist Grundwert mal Faktor. Rechne rückwärts: teilen.', '€')


def g_prozentsatz(R, st):
    for _ in range(500):
        G = Fr(R.choice([20, 25, 40, 50, 80, 120, 150, 200, 250, 400, 500, 800]))
        p = Fr(R.choice(PROZ[st])) * R.choice([1, -1])
        neu = G * (1 + p / 100)
        if geld_ok(neu) and neu > 0: break
    if st == 3 and R.random() < .5:
        return Z(f'Ein Preis fällt von {eur(G)} € auf {eur(neu)} € und steigt danach wieder auf {eur(G)} €. Um wie viel Prozent steigt er im zweiten Schritt? Runde auf eine Nachkommastelle.',
                 Fr(str(round(float((G / neu - 1) * 100), 1))), f'round(({cz(G)} / {cz(neu)} - 1) * 100, 1)',
                 f'{eur(G)} : {eur(neu)} ≈ {zt(Fr(str(round(float(G / neu), 4))))}. Zunahme ≈ {zt(Fr(str(round(float((G / neu - 1) * 100), 1))))} % – mehr als die Abnahme, weil der Bezugswert kleiner ist.',
                 'Bezugswert ist jetzt der gesunkene Preis.', '%', toleranz=Fr(1, 10)) if p < 0 else g_prozentsatz(R, st)
    return Z(f'Ein Preis ändert sich von {eur(G)} € auf {eur(neu)} €. Um wie viel Prozent ändert er sich? (Zunahme positiv, Abnahme negativ)', p,
             f'({cz(neu)} / {cz(G)} - 1) * 100', f'{eur(neu)} : {eur(G)} = {zt(neu / G)}. ({zt(neu / G)} − 1) · 100 % = {zt(p)} %.',
             'Teile neu durch alt. Was fehlt oder fehlt zu 1?', '%')


def g_mehrfach(R, st):
    for _ in range(500):
        G = Fr(R.choice([100, 200, 250, 400, 500, 800, 1000]))
        n = 2 if st < 3 else R.choice([2, 3])
        ps = [Fr(R.choice([5, 10, 20, 25, 50])) * R.choice([1, -1]) for _ in range(n)]
        f = Fr(1)
        for p in ps: f *= 1 + p / 100
        neu = G * f
        if geld_ok(neu): break
    teile = ', dann '.join(f'{"+" if p > 0 else "−"}{zt(abs(p))} %' for p in ps)
    fk = ' · '.join(zt(1 + p / 100) for p in ps)
    if st == 1:
        return Z(f'Ein Preis von {eur(G)} € ändert sich um {teile}. Wie hoch ist der Endpreis?', neu, f'{cz(G)} * ' + ' * '.join(f'(1 + {cz(p)} / 100)' for p in ps),
                 f'{eur(G)} € · {fk} = {eur(neu)} €.', 'Für jede Änderung einen Faktor, dann alle multiplizieren.', '€')
    if st == 2 or R.random() < .5:
        return Z(f'Ein Preis ändert sich nacheinander um {teile}. Um wie viel Prozent hat er sich insgesamt geändert? (Zunahme positiv, Abnahme negativ)', (f - 1) * 100,
                 '(' + ' * '.join(f'(1 + {cz(p)} / 100)' for p in ps) + ' - 1) * 100', f'Gesamtfaktor {fk} = {zt(f)}. Änderung ({zt(f)} − 1) · 100 % = {zt((f - 1) * 100)} %.',
                 'Multipliziere die Faktoren. Addiere nicht die Prozente.', '%')
    return Z(f'Ein Preis ändert sich um {teile} und beträgt dann {eur(neu)} €. Wie hoch war er ursprünglich?', G, f'{cz(neu)} / ' + '(' + ' * '.join(f'(1 + {cz(p)} / 100)' for p in ps) + ')',
             f'Gesamtfaktor {fk} = {zt(f)}. Ursprünglich: {eur(neu)} € : {zt(f)} = {eur(G)} €.', 'Bestimme den Gesamtfaktor und rechne rückwärts.', '€')


def g_argumente(R, st):
    a, b = R.sample([10, 20, 25, 30, 40, 50], 2)
    G = R.choice([100, 200, 400, 500])
    up = Fr(100 * a, 100 - a)
    al = [
        (f'{a} % Rabatt und dann noch {b} % Rabatt sind zusammen {a + b} % Rabatt.', False, f'Faktor {zt(Fr(100 - a, 100))} · {zt(Fr(100 - b, 100))} = {zt(Fr((100 - a) * (100 - b), 10000))}, also {zt(100 - Fr((100 - a) * (100 - b), 100))} % Ersparnis.'),
        (f'Erst +{a} %, dann −{a} %: Der Preis ist danach niedriger als vorher.', True, f'Faktor {zt(Fr(100 + a, 100))} · {zt(Fr(100 - a, 100))} = {zt(Fr((100 + a) * (100 - a), 10000))} < 1.'),
        (f'Erst +{a} %, dann −{a} %: Der Preis ist danach wieder genau gleich.', False, f'Faktor {zt(Fr(100 + a, 100))} · {zt(Fr(100 - a, 100))} = {zt(Fr((100 + a) * (100 - a), 10000))} ≠ 1.'),
        (f'Erst {a} % Rabatt, dann {b} % Rabatt ergibt denselben Preis wie erst {b} %, dann {a} %.', True, 'Die Faktoren werden multipliziert – die Reihenfolge ist egal.'),
        (f'Sinkt ein Preis um {a} %, muss er um {a} % steigen, um wieder den alten Wert zu erreichen.', False, f'Nötig sind {zt(up) if ist_endlich(up) else "≈ " + zt(Fr(str(round(float(up), 1))))} %, weil der Bezugswert kleiner ist.'),
        (f'{G} € mit 19 % Mehrwertsteuer ergeben {zt(Fr(G * 119, 100))} €.', True, f'{G} · 1,19 = {zt(Fr(G * 119, 100))}.'),
        (f'Aus einem Bruttopreis von {zt(Fr(G * 119, 100))} € erhält man den Nettopreis, indem man 19 % davon abzieht.', False, 'Die 19 % beziehen sich auf den Nettopreis. Man muss durch 1,19 teilen.'),
        (f'Der Preis wurde reduziert, weil das Geschäft Kunden anlocken will. Also ist der neue Preis {a} % niedriger.', False, 'Der Grund für die Senkung ist ein außermathematisches Argument und sagt nichts über die Prozentzahl.'),
        (f'Steigt ein Wert um 100 %, verdoppelt er sich.', True, 'Faktor 1 + 1 = 2.'),
        (f'Sinkt ein Wert um 100 %, halbiert er sich.', False, 'Faktor 1 − 1 = 0: Der Wert ist dann 0.'),
    ]
    wahr = [(t, g) for t, w, g in al if w]; falsch = [(t, g) for t, w, g in al if not w]
    if st == 1 or (st == 2 and R.random() < .5):
        t, g = R.choice(wahr)
        return A(R, 'Welche Aussage ist mathematisch richtig?', t, [x for x, _ in R.sample(falsch, 3)], f'Richtig: {t} {g}', 'Rechne jede Aussage mit Faktoren nach.')
    t, g = R.choice(falsch)
    return A(R, 'Welche Aussage ist FALSCH oder kein mathematisches Argument?', t, [x for x, _ in R.sample(wahr, 3)], f'Nicht haltbar: {t} {g}',
             'Prüfe mit einer Rechnung – nicht mit Begründungen aus dem Alltag.')


GEN = {'faktor': g_faktor, 'vermehrt': g_vermehrt, 'vermindert': g_vermindert, 'zurueck': g_zurueck, 'prozentsatz': g_prozentsatz, 'mehrfach': g_mehrfach, 'argumente': g_argumente}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Faktoren', ['faktor', 'vermehrt', 'vermindert']), ('Rückwärts rechnen', ['zurueck', 'prozentsatz']), ('Komplexere Aufgaben', ['mehrfach', 'argumente'])],
         'Mit dem Wachstumsfaktor vermehrte und verminderte Grundwerte berechnen, auf den Grundwert zurückrechnen, prozentuale Änderungen bestimmen und Aussagen über Prozente mathematisch prüfen.',
         ['Plus p %: mal (1 + p/100). Minus p %: mal (1 − p/100).', 'Zurück zum Grundwert: durch den Faktor teilen.',
          'Mehrere Änderungen: Faktoren multiplizieren, nicht Prozente addieren.'],
         offen=['Prozentstreifen / Prozentkreis als Bild wären für die Lernkarten „faktor“ und „zurueck“ hilfreich; die App kann sie noch nicht zeichnen.'])
