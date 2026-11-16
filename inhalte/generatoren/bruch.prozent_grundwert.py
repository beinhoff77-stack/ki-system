#!/usr/bin/env python3
"""Thema bruch.prozent_grundwert – Vermehrter und verminderter Grundwert (Gymnasium Bayern, Klasse 7)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl7 import A, Z, baue, cz, eur, ist_endlich, zt  # noqa: E402

TAB = lambda kopf, zeilen: {'typ': 'tabelle', 'kopf': kopf, 'zeilen': zeilen}

META = {'thema_schluessel': 'bruch.prozent_grundwert', 'thema_id': 94, 'block_id': 108, 'klasse': {'gym_by': 7, 'rs_by': 7}}

ETAPPEN = [
    {'lernziel': 'faktor', 'titel': 'Den Wachstumsfaktor bestimmen',
     'regel': 'Steigt ein Wert um p %, ist der neue Wert (100 + p) % des alten: Man multipliziert mit dem ⟦Wachstumsfaktor 1 + p/100⟧. Sinkt er um p %, multipliziert man mit ⟦1 − p/100⟧.',
     'schritte': ['Erhöhung um 15 %: 100 % + 15 % = 115 %', 'Faktor ⟦1,15⟧', 'Senkung um 15 %: 100 % − 15 % = 85 %, Faktor ⟦0,85⟧'],
     'fehler': 'Der Faktor für „um 15 % mehr“ ist nicht 0,15. Mit 0,15 erhältst du nur die ⟦Zunahme⟧, nicht den neuen Wert. Der neue Wert braucht 1,15.',
     'bild': {'typ': 'figur', 'punkte': {'_a': [0, 0], '_b': [10, 0], '_c': [11.5, 0], '_d': [11.5, 1.5], '_e': [10, 1.5], '_f': [0, 1.5]}, 'flaeche': ['_b', '_c', '_d', '_e'], 'linien': [['_a', '_b', '100 % = Grundwert'], ['_b', '_c', '+15 %'], ['_c', '_d'], ['_d', '_e'], ['_e', '_f', '115 % → Faktor 1,15'], ['_f', '_a'], ['_b', '_e']]},
     '_verbot': ['um 15 %']},
    {'lernziel': 'vermehrt', 'titel': 'Den vermehrten Grundwert berechnen',
     'regel': 'Vermehrter Grundwert = ⟦Grundwert · (1 + p/100)⟧. So rechnest du in einem Schritt, statt erst die Zunahme auszurechnen und dann zu addieren.',
     'schritte': ['Ein Fahrrad kostet 480 €, der Preis steigt um 5 %.', 'Neuer Preis: 480 € · 1,05', '= ⟦504 €⟧'],
     'probe': 'Zunahme 5 % von 480 € = 24 €; 480 € + 24 € = 504 € ✓',
     'fehler': '480 € + 5 = 485 € ist falsch: 5 % sind ⟦nicht 5 Euro⟧, sondern 5 Hundertstel des Grundwerts.',
     'bild': {'typ': 'saeulen', 'einheit': '€', 'werte': [{'name': 'vorher', 'wert': 480}, {'name': 'nachher (+5 %)', 'wert': 504}], 'y_start': 0, 'zahlen': True},
     '_verbot': ['480 €']},
    {'lernziel': 'vermindert', 'titel': 'Den verminderten Grundwert berechnen',
     'regel': 'Verminderter Grundwert = ⟦Grundwert · (1 − p/100)⟧. Typisch sind ⟦Rabatt⟧ und Preissenkungen.',
     'schritte': ['Eine Jacke kostet 120 €, es gibt 30 % Rabatt.', 'Faktor: 1 − 0,30 = 0,70', '120 € · 0,7 = ⟦84 €⟧'],
     'fehler': '120 € · 0,3 = 36 € ist nicht der neue Preis, sondern der ⟦Rabatt⟧. Zu zahlen sind 120 € − 36 € = 84 €.',
     'bild': {'typ': 'saeulen', 'einheit': '€', 'werte': [{'name': 'vorher', 'wert': 120}, {'name': 'Rabatt', 'wert': 36}, {'name': 'zu zahlen', 'wert': 84}], 'y_start': 0, 'zahlen': True},
     '_verbot': ['120 €']},
    {'lernziel': 'zurueck', 'titel': 'Zurück zum Grundwert',
     'regel': 'Kennst du den vermehrten oder verminderten Wert, ⟦teilst⟧ du durch den Faktor: Grundwert = neuer Wert : (1 ± p/100).',
     'schritte': ['Ein Preis mit 19 % Mehrwertsteuer ist 59,50 €.', 'Netto · 1,19 = 59,50 € → Netto = 59,50 € : 1,19', '= ⟦50 €⟧'],
     'probe': '50 € · 1,19 = 59,50 € ✓',
     'fehler': 'Der Nettopreis ist nicht 59,50 € − 19 % von 59,50 € = 48,20 €. Die 19 % beziehen sich auf den ⟦Nettopreis⟧, nicht auf den Endpreis. Darum wird geteilt.',
     'bild': TAB(['', 'Prozent', 'Betrag'], [['Nettopreis (Grundwert)', '100 %', '?'], ['Mehrwertsteuer', '19 %', ''], ['Endpreis', '119 %', '59,50 €']]),
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
     'bild': TAB(['Schritt', 'Faktor', 'Preis'], [['Start', '', '200 €'], ['+10 %', '· 1,1', '220 €'], ['−10 %', '· 0,9', '198 €']]),
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


ZYKLUS = {'faktor': -1}


def _faktor_fehler(R):
    """Fehler finden: falsche Faktor-Behauptung prüfen (Stufe 3)."""
    art = R.choice(['ab_zehntel', 'ab_rest', 'auf_rest', 'gross'])
    if art == 'gross':
        p = R.choice([110, 120, 125, 130, 140, 150, 175, 180, 250])
        q = Fr(p, 100)
        return A(R, f'Jemand sagt: „{p} % des Grundwerts bedeutet den Faktor {p}.“ Was stimmt?', f'Falsch: {p} % = {zt(q)}, der Faktor ist {zt(q)}.',
                 [f'Richtig: {p} % heißt mal {p}.', f'Falsch: Der Faktor ist {zt(Fr(p - 100, 100))}.', f'Falsch: Der Faktor ist {zt(1 - Fr(p - 100, 100))}.'],
                 f'{p} % = {p}/100 = {zt(q)}. Der neue Wert ist {zt(q)}-mal so groß wie der Grundwert.', 'Prozent heißt „von Hundert“: teile durch 100.')
    p = R.choice([2, 3, 4, 5, 6, 7, 8, 9])
    if art == 'ab_zehntel':
        behaupt, wort = Fr(p, 10), 'Abnahme'
    elif art == 'ab_rest':
        behaupt, wort = Fr(p, 100), 'Abnahme'
    else:
        behaupt, wort = Fr(p, 100), 'Zunahme'
    q = 1 - Fr(p, 100) if wort == 'Abnahme' else 1 + Fr(p, 100)
    falsche = [f'Richtig: {p} % = {zt(behaupt)}.', f'Falsch: Der Faktor ist {zt(2 - q)}.', f'Falsch: Der Faktor ist {zt(Fr(p, 100) if behaupt != Fr(p, 100) else Fr(p, 10))}.']
    return A(R, f'Jemand sagt: „Eine {wort} um {p} % bedeutet den Faktor {zt(behaupt)}.“ Was stimmt?',
             f'Falsch: Der Faktor ist 1 {"−" if wort == "Abnahme" else "+"} {zt(Fr(p, 100))} = {zt(q)}.', falsche,
             f'{p} % = {zt(Fr(p, 100))}. Der neue Wert ist 100 % {"−" if wort == "Abnahme" else "+"} {p} % = {zt(q * 100)} % = {zt(q)}.',
             'Der Faktor beschreibt den neuen Wert, nicht nur die Änderung.')


def _faktor_deuten(R, q):
    return Z(f'Ein Wert wird mit dem Faktor {zt(q)} multipliziert. Um wie viel Prozent ändert er sich? (Zunahme positiv, Abnahme negativ angeben)',
             (q - 1) * 100, f'({cz(q)} - 1) * 100', f'{zt(q)} = {zt(q * 100)} %. Änderung: {zt(q * 100)} % − 100 % = {zt((q - 1) * 100)} %.',
             'Schreibe den Faktor als Prozentzahl und vergleiche mit 100 %.', '%')


def g_faktor(R, st):
    if st == 3:
        ZYKLUS['faktor'] += 1
        art = ['fehler', 'gross', 'deuten', 'komma'][ZYKLUS['faktor'] % 4]
        if art == 'fehler': return _faktor_fehler(R)
        if art == 'deuten':
            return _faktor_deuten(R, R.choice([Fr(x, 1000) for x in (1025, 1075, 1125, 975, 925, 2500, 3000, 2250, 1005)]))
        if art == 'gross':
            p = Fr(R.choice([110, 120, 125, 150, 175, 200, 250, 300]))
            return Z(f'Ein Wert wird um {pt(p)} erhöht. Mit welchem Faktor multiplizierst du?', 1 + p / 100, f'1 + {cz(p)} / 100',
                     f'100 % + {pt(p)} = {zt(100 + p)} % = {zt(1 + p / 100)}. Der Wert wird mehr als verdoppelt.', 'Auch über 100 % gilt: 100 % + p %, dann durch 100 teilen.')
        p = Fr(R.choice([Fr(5, 2), Fr(15, 2), Fr(25, 2), Fr(1, 2), Fr(35, 2), Fr(45, 2)]))
        rauf = R.random() < .5
        q = 1 + p / 100 if rauf else 1 - p / 100
        return Z(f'Ein Wert wird um {pt(p)} {"erhöht" if rauf else "verringert"}. Mit welchem Faktor multiplizierst du?', q, f'1 {"+" if rauf else "-"} {cz(p)} / 100',
                 f'100 % {"+" if rauf else "−"} {pt(p)} = {zt(q * 100)} % = {zt(q)}.', 'Rechne erst 100 % plus oder minus p %, dann in eine Dezimalzahl umwandeln.')
    p = Fr(R.choice(PROZ[st]))
    rauf = R.random() < .5
    q = 1 + p / 100 if rauf else 1 - p / 100
    if st == 2 and R.random() < .35:
        # Faktor deuten: Faktor → Prozent
        return Z(f'Ein Wert wird mit dem Faktor {zt(q)} multipliziert. Um wie viel Prozent ändert er sich? (Zunahme positiv, Abnahme negativ angeben)',
                 (q - 1) * 100, f'({cz(q)} - 1) * 100', f'{zt(q)} = {zt(q * 100)} %. Änderung: {zt(q * 100)} % − 100 % = {zt((q - 1) * 100)} %.',
                 'Schreibe den Faktor als Prozentzahl und vergleiche mit 100 %.', '%')
    return Z(f'Ein Wert wird um {pt(p)} {"erhöht" if rauf else "verringert"}. Mit welchem Faktor multiplizierst du?', q, f'1 {"+" if rauf else "-"} {cz(p)} / 100',
             f'100 % {"+" if rauf else "−"} {pt(p)} = {zt(q * 100)} % = {zt(q)}.', 'Rechne erst 100 % plus oder minus p %, dann in eine Dezimalzahl umwandeln.')


# (Anfang, Satz mit {p}, Einheit, größter sinnvoller Prozentsatz)
KONTEXT_RAUF = [('Ein Fahrrad kostet', 'Der Preis steigt um {p}.', '€', 20), ('Eine Monatsmiete beträgt', 'Sie wird um {p} erhöht.', '€', 15),
                ('Ein Nettopreis beträgt', 'Dazu kommen {p} Mehrwertsteuer.', '€', 19), ('Ein Verein hat', 'Die Mitgliederzahl wächst um {p}.', 'Mitglieder', 50),
                ('Ein Sparguthaben beträgt', 'In einem Jahr kommen {p} Zinsen dazu.', '€', 5)]
KONTEXT_RUNTER = [('Eine Jacke kostet', 'Im Ausverkauf gibt es {p} Rabatt.', '€', 70), ('Ein Handy kostet', 'Der Preis sinkt um {p}.', '€', 40),
                  ('Ein Auto hat einen Wert von', 'In einem Jahr sinkt der Wert um {p}.', '€', 25), ('Eine Schule hat', 'Die Schülerzahl sinkt um {p}.', 'Schüler', 15),
                  ('Ein Tank enthält', 'Der Inhalt nimmt um {p} ab.', 'Liter', 80)]


BEREICH = {'Ein Fahrrad kostet': [380, 450, 480, 560, 640, 720, 850, 900, 1200], 'Eine Monatsmiete beträgt': [480, 560, 640, 750, 800, 900, 950, 1100, 1200],
           'Ein Nettopreis beträgt': [20, 40, 50, 60, 80, 120, 150, 200, 240, 350, 400, 500], 'Ein Sparguthaben beträgt': [800, 1200, 1500, 2000, 2400, 3000, 4000, 5000],
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
    frage = ('Wie hoch ist der neue Preis?' if k[2] == '€' and 'kostet' in k[0] else 'Wie hoch ist der Preis mit Mehrwertsteuer?' if 'Nettopreis' in k[0]
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


DINGE_SKONTO = [('Ein Sofa', [400, 600, 800, 900, 1200]), ('Ein Fahrrad', [400, 500, 600, 800]), ('Eine Jacke', [80, 120, 150, 200]),
                ('Ein Schreibtisch', [200, 250, 300, 400]), ('Eine Waschmaschine', [400, 500, 600, 700])]


def g_vermindert(R, st):
    if st == 3:
        # neuer Gedanke: zwei Abzüge nacheinander (Rabatt, dann Skonto auf den reduzierten Preis)
        for _ in range(200):
            ding, preise = R.choice(DINGE_SKONTO)
            G = Fr(R.choice(preise)); p = Fr(R.choice([10, 15, 20, 25, 30])); sk = Fr(R.choice([2, 3]))
            zw = G * (1 - p / 100); neu = zw * (1 - sk / 100)
            if geld_ok(neu): break
        return Z(f'{ding} kostet {eur(G)} €. Es gibt {pt(p)} Rabatt, auf den reduzierten Preis bei Barzahlung noch {pt(sk)} Skonto. Was zahlt man bar?', neu,
                 f'{cz(G)} * (1 - {cz(p)} / 100) * (1 - {cz(sk)} / 100)', f'{eur(G)} € · {zt(1 - p / 100)} = {eur(zw)} €; {eur(zw)} € · {zt(1 - sk / 100)} = {eur(neu)} €.',
                 'Zwei Abzüge nacheinander: zwei Faktoren. Das Skonto bezieht sich auf den schon reduzierten Preis.', '€')
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


BEZUG = [(80, 100), (100, 80), (40, 50), (50, 40), (200, 250), (250, 200), (160, 200), (200, 160), (75, 100), (100, 75), (120, 150), (150, 120), (60, 75), (75, 60)]


def _bezugswert(R):
    """Falle „falscher Grundwert“: Änderung auf den neuen statt auf den alten Wert bezogen."""
    alt, neu = R.choice(BEZUG)
    d = abs(neu - alt)
    wort = 'steigt' if neu > alt else 'fällt'
    richtig_p, falsch_p = Fr(d * 100, alt), Fr(d * 100, neu)
    p1 = lambda x: zt(x) if ist_endlich(x) and len(zt(x).partition(',')[2]) <= 1 else '≈ ' + zt(Fr(str(round(float(x), 1))))
    q3 = lambda x: ('= ' + zt(x)) if ist_endlich(x) and len(zt(x).partition(',')[2]) <= 3 else '≈ ' + zt(Fr(str(round(float(x), 3))))
    if R.random() < .6:
        text = f'Ein Preis {wort} von {alt} € auf {neu} €. Jemand sagt: „Das sind {p1(falsch_p)} %, denn {d} : {neu} {q3(Fr(d, neu))}.“ Was stimmt?'
        richtig = f'Falsch: Man teilt durch den alten Wert: {d} : {alt}, also {p1(richtig_p)} %.'
        falsche = [f'Richtig: Man teilt durch den neuen Wert {neu} €.', f'Richtig: Eine Änderung um {d} € sind immer {d} %.',
                   f'Falsch: Es sind {p1(Fr(neu * 100, alt))} %.']
    else:
        text = f'Ein Preis {wort} von {alt} € auf {neu} €. Jemand sagt: „Das sind {p1(richtig_p)} %, denn {d} : {alt} {q3(Fr(d, alt))}.“ Was stimmt?'
        richtig = f'Richtig: Die Änderung {d} € wird auf den alten Wert {alt} € bezogen.'
        falsche = [f'Falsch: Man teilt durch den neuen Wert, also {p1(falsch_p)} %.', f'Richtig: Eine Änderung um {d} € sind immer {d} %.',
                   f'Falsch: Man teilt durch {alt + neu} €, die Summe der Preise.']
    return A(R, text, richtig, falsche, f'Grundwert ist der alte Preis {alt} €. Änderung {d} €; {d} : {alt} = {p1(richtig_p)} %.',
             'Worauf bezieht sich die Änderung – auf den Preis vorher oder nachher?')


def g_prozentsatz(R, st):
    if st == 3 and R.random() < .5: return _bezugswert(R)
    for _ in range(500):
        G = Fr(R.choice([20, 25, 40, 50, 80, 120, 150, 200, 250, 400, 500, 800]))
        p = Fr(R.choice(PROZ[st])) * R.choice([1, -1])
        neu = G * (1 + p / 100)
        if geld_ok(neu) and neu > 0 and (st < 3 or p < 0): break
    if st == 3:
        return Z(f'Ein Preis fällt von {eur(G)} € auf {eur(neu)} € und steigt danach wieder auf {eur(G)} €. Um wie viel Prozent steigt er im zweiten Schritt? Runde auf eine Nachkommastelle.',
                 Fr(str(round(float((G / neu - 1) * 100), 1))), f'round(({cz(G)} / {cz(neu)} - 1) * 100, 1)',
                 f'{eur(G)} : {eur(neu)} ≈ {zt(Fr(str(round(float(G / neu), 4))))}. Zunahme ≈ {zt(Fr(str(round(float((G / neu - 1) * 100), 1))))} % – mehr als die Abnahme, weil der Bezugswert kleiner ist.',
                 'Bezugswert ist jetzt der gesunkene Preis.', '%', toleranz=Fr(1, 10))
    return Z(f'Ein Preis ändert sich von {eur(G)} € auf {eur(neu)} €. Um wie viel Prozent ändert er sich? (Zunahme positiv, Abnahme negativ)', p,
             f'({cz(neu)} / {cz(G)} - 1) * 100', f'{eur(neu)} : {eur(G)} = {zt(neu / G)}. ({zt(neu / G)} − 1) · 100 % = {zt(p)} %.',
             'Teile neu durch alt und vergleiche das Ergebnis mit 1.', '%')


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


ZAEHLER = {'pool': 0}
AUSSER = ['Das steht so auf dem Werbeschild.', 'Das macht jedes Geschäft so.', 'Die Verkäuferin hat es gesagt.', 'Das klingt fair.',
          'Rabatte rechnet man immer so.', 'Das hat schon immer gestimmt.']


def _pool(R, st):
    a, b = R.sample([10, 20, 25, 30, 40, 50], 2)
    G = R.choice([100, 200, 400, 500])
    up = Fr(100 * a, 100 - a)
    wahr = [f'Erst +{a} %, dann −{a} %: Der Preis ist danach niedriger als vorher, denn {zt(Fr(100 + a, 100))} · {zt(Fr(100 - a, 100))} = {zt(Fr((100 + a) * (100 - a), 10000))} < 1.',
            f'Erst {a} % Rabatt, dann {b} % Rabatt ergibt denselben Preis wie erst {b} %, dann {a} %, denn beim Multiplizieren der Faktoren ist die Reihenfolge egal.',
            f'{G} € mit 19 % Mehrwertsteuer ergeben {zt(Fr(G * 119, 100))} €, denn {G} · 1,19 = {zt(Fr(G * 119, 100))}.',
            'Steigt ein Wert um 100 %, verdoppelt er sich, denn der Faktor ist 1 + 1 = 2.']
    falsch = [f'{a} % Rabatt und dann noch {b} % Rabatt sind zusammen {a + b} % Rabatt, denn {a} + {b} = {a + b}.',
              f'Erst +{a} %, dann −{a} %: Der Preis ist danach wieder genau gleich, denn die Prozente heben sich auf.',
              f'Sinkt ein Preis um {a} %, muss er um {a} % steigen, um den alten Wert zu erreichen, denn es ist dieselbe Änderung.',
              f'Aus {zt(Fr(G * 119, 100))} € brutto erhält man den Nettopreis, indem man 19 % davon abzieht, denn die Steuer beträgt 19 %.',
              'Sinkt ein Wert um 100 %, halbiert er sich, denn 100 % ist die Hälfte von 200 %.',
              f'Der neue Preis ist {a} % niedriger, denn das Geschäft will Kunden anlocken.']
    t = R.choice(wahr)
    return A(R, 'Welche Aussage ist mathematisch richtig begründet?', t, R.sample(falsch, 3), f'Richtig begründet: {t}',
             'Rechne jede Aussage mit Faktoren nach. Eine Begründung aus dem Alltag beweist nichts.')


def _begruendung(R):
    G = R.choice([40, 60, 80, 120, 150, 200, 250]); a = R.choice([10, 20, 25, 30, 40])
    N = Fr(G * (100 - a), 100)
    richtig = f'{G} € · {zt(Fr(100 - a, 100))} = {eur(N)} €'
    return A(R, f'Ein Preis von {G} € sinkt um {a} % auf {eur(N)} €. Welche Begründung zeigt das mathematisch?', richtig, R.sample(AUSSER, 3),
             f'Nur die Rechnung ist ein mathematisches Argument: {richtig}. Die anderen Gründe sind außermathematisch.', 'Ein mathematisches Argument ist eine Rechnung.')


def _szenario(R):
    art = R.choice(['doppel', 'auf_ab', 'netto'])
    if art == 'doppel':
        a, b = R.choice([(20, 20), (10, 10), (30, 10), (20, 10), (25, 20), (50, 50), (10, 20), (30, 20)])
        f = Fr((100 - a) * (100 - b), 10000)
        richtig = f'Nein: {zt(Fr(100 - a, 100))} · {zt(Fr(100 - b, 100))} = {zt(f)}, man spart {zt(100 - f * 100)} %.'
        return A(R, f'Ein Laden wirbt: „Erst {a} % Rabatt, an der Kasse noch einmal {b} %.“ Spart man {a + b} %?', richtig,
                 [f'Ja: {a} + {b} = {a + b}.', f'Nein: Man spart nur {max(a, b)} %.', 'Ja: Rabatte addiert man immer.'],
                 f'Der zweite Rabatt bezieht sich auf den schon reduzierten Preis. Faktor {zt(f)}, Ersparnis {zt(100 - f * 100)} %.', 'Schreibe jeden Rabatt als Faktor.')
    if art == 'auf_ab':
        a = R.choice([5, 10, 20, 25, 30, 40, 50]); erst_ab = R.random() < .5
        f = Fr((100 + a) * (100 - a), 10000)
        d = zt(100 - f * 100)
        folge = f'erst um {a} %, dann steigt er um {a} %' if erst_ab else f'erst um {a} %, dann sinkt er um {a} %'
        richtig = f'Nein: {zt(Fr(100 - a, 100)) if erst_ab else zt(Fr(100 + a, 100))} · {zt(Fr(100 + a, 100)) if erst_ab else zt(Fr(100 - a, 100))} = {zt(f)}, also {d} % weniger.'
        return A(R, f'Ein Lohn ändert sich {folge.replace("dann steigt er", "dann steigt er").replace("erst um", "erst um", 1)}. Ist er danach so hoch wie vorher?'.replace('ändert sich erst', f'{"sinkt" if erst_ab else "steigt"} erst'), richtig,
                 [f'Ja: −{a} % und +{a} % heben sich auf.', f'Nein: Er ist danach {d} % höher.', 'Ja: Der Lohn steigt ja wieder.'],
                 f'Gesamtfaktor {zt(f)} < 1. Der Lohn ist danach {d} % niedriger als vorher.', 'Multipliziere die beiden Faktoren.')
    B = Fr(R.choice([119, 238, 357, 476, 595, 714, 1190]))
    Nn = B / Fr(119, 100)
    richtig = f'Nein: Netto = {eur(B)} € : 1,19 = {eur(Nn)} €.'
    return A(R, f'Ein Preis mit 19 % Mehrwertsteuer beträgt {eur(B)} €. Bekommt man den Nettopreis, wenn man 19 % von {eur(B)} € abzieht?', richtig,
             [f'Ja: {eur(B)} € · 0,81 = {eur(B * Fr(81, 100))} €.', 'Ja: So steht es auf jeder Rechnung.', f'Nein: Man zieht 19 € ab, also {eur(B - 19)} €.'],
             f'Die 19 % beziehen sich auf den Nettopreis. Netto · 1,19 = {eur(B)} €, also Netto = {eur(Nn)} €.', 'Worauf beziehen sich die 19 %?')


def g_argumente(R, st):
    if st == 1:
        ZAEHLER['pool'] += 1
        return _pool(R, st)
    if st == 3: return _szenario(R)
    x = R.random()
    if x < .3 and ZAEHLER['pool'] < 9:
        ZAEHLER['pool'] += 1
        return _pool(R, st)
    return _begruendung(R) if x < .65 else _szenario(R)


GEN = {'faktor': g_faktor, 'vermehrt': g_vermehrt, 'vermindert': g_vermindert, 'zurueck': g_zurueck, 'prozentsatz': g_prozentsatz, 'mehrfach': g_mehrfach, 'argumente': g_argumente}

# Verständliche Fassung (Runde 7, Maßstab inhalte/README.md „Verständliche Erklärungen“):
# Alltagssituation zuerst (einstieg), jedes neue Wort erklärt (woerter), Beispiel in kleinen Schritten, Merksatz am Ende (regel).
# Durchgehende Situation: Preise in einem Sportgeschäft.
KLAR = {
 'faktor': {
  'einstieg': 'Im Sportgeschäft hängt ein Schild: „Ab Montag steigen alle Preise um 15 %.“ Ein Ball, der bisher 100 € gekostet hat, kostet dann 115 €. Statt jedes Mal erst die Erhöhung auszurechnen und dazuzuzählen, kann man den alten Preis mit einer einzigen Zahl malnehmen. Diese Zahl heißt ⟦Wachstumsfaktor⟧.',
  'woerter': [['Prozent (%)', 'Hundertstel: 15 % heißt 15 von 100, also 0,15'], ['Grundwert', 'der Wert vorher, von dem man ausgeht – hier der alte Preis; er zählt als 100 %'],
              ['Wachstumsfaktor', 'die Zahl, mit der man den alten Wert malnimmt, um gleich den neuen zu bekommen'], ['p %', 'Platzhalter für irgendeinen Prozentsatz, zum Beispiel 15 %'],
              ['1 + p/100', 'der Faktor für eine Erhöhung um p %: bei 15 % also 1 + 15/100 = 1,15'], ['1 − p/100', 'der Faktor für eine Senkung um p %: bei 15 % also 1 − 0,15 = 0,85']],
  'schritte': ['Der alte Preis ist der Grundwert. Er zählt als 100 %.',
               'Die Preise steigen um 15 %. Der neue Preis ist also 100 % + 15 % = 115 % des alten Preises.',
               '115 % als Dezimalzahl: 115 durch 100 teilen ergibt 1,15. Das ist der Wachstumsfaktor: ⟦Faktor 1,15⟧.',
               'Bei einer Senkung um 15 % bleiben 100 % − 15 % = 85 % übrig. Der Faktor ist dann ⟦0,85⟧.'],
  'regel': 'So findest du den ⟦Wachstumsfaktor⟧: Bei einer Erhöhung um p % rechnest du ⟦1 + p/100⟧, bei einer Senkung um p % rechnest du ⟦1 − p/100⟧. Mit diesem Faktor nimmst du den Grundwert mal.',
  'fehler': 'Der Faktor für „15 % mehr“ ist nicht 0,15. Mit 0,15 malgenommen kommt nur die ⟦Erhöhung⟧ heraus: Beim 100-€-Ball wären das 15 € – als ob der Ball danach nur noch 15 € kosten würde. Für den neuen Preis braucht man 1,15.'},
 'vermehrt': {
  'einstieg': 'Ein Fahrrad im selben Geschäft kostet 480 €. Nächsten Monat steigt sein Preis um 5 %. Was kostet es dann? Mit dem Faktor von der letzten Karte geht das in einem Schritt. Der neue, höhere Wert heißt ⟦vermehrter Grundwert⟧.',
  'woerter': [['vermehrter Grundwert', 'der Wert nach einer Erhöhung – hier der neue Fahrradpreis'], ['Zunahme', 'um wie viel der Wert größer wird, hier in Euro'], ['·', 'Malzeichen']],
  'schritte': ['Der Grundwert ist der alte Preis: 480 €.',
               'Der Preis steigt um 5 %. Der Faktor ist deshalb 1 + 5/100 = 1,05.',
               'Nimm den alten Preis mal den Faktor: 480 € · 1,05.',
               'Ausrechnen ergibt den neuen Preis: ⟦504 €⟧.'],
  'regel': 'So rechnest du den ⟦vermehrten Grundwert⟧ aus: ⟦Grundwert · (1 + p/100)⟧. Das ist ein einziger Schritt, statt erst die Zunahme auszurechnen und sie dann dazuzuzählen.',
  'fehler': '480 € + 5 = 485 € ist falsch: 5 % sind ⟦nicht 5 Euro⟧, sondern 5 Hundertstel des Preises. Bei einem teuren Fahrrad sind 5 % viel mehr Geld als bei einer Fahrradklingel.',
  'bild': {'typ': 'saeulen', 'einheit': '€', 'werte': [{'name': 'Preis vorher', 'wert': 480}, {'name': 'Preis nachher (+5 %)', 'wert': 504}], 'y_start': 0, 'zahlen': True}},
 'vermindert': {
  'einstieg': 'Im Schlussverkauf kostet eine Jacke eigentlich 120 €, aber es gibt 30 % Rabatt. Man zahlt also weniger als den alten Preis. Auch hier hilft ein Faktor – diesmal einer, der kleiner als 1 ist. Der neue, kleinere Wert heißt ⟦verminderter Grundwert⟧.',
  'woerter': [['Rabatt', 'Preisnachlass: so viel Prozent zieht der Laden vom Preis ab'], ['verminderter Grundwert', 'der Wert nach einer Senkung – hier der Preis, den man an der Kasse zahlt']],
  'schritte': ['Der Grundwert ist der alte Preis der Jacke: 120 €.',
               'Bei 30 % Rabatt bleiben 100 % − 30 % = 70 % zu zahlen. Der Faktor ist 1 − 0,30 = 0,70.',
               'Nimm den alten Preis mal den Faktor: 120 € · 0,7 = ⟦84 €⟧.',
               'Zur Kontrolle: Der Rabatt beträgt 120 € · 0,3 = 36 €, und 120 € − 36 € = 84 €. Das passt.'],
  'regel': 'So rechnest du den ⟦verminderten Grundwert⟧ aus: ⟦Grundwert · (1 − p/100)⟧. Das brauchst du bei Rabatt und anderen Preissenkungen.',
  'fehler': '120 € · 0,3 = 36 € ist nicht der neue Preis, sondern der ⟦Rabatt⟧ – also das, was du sparst, und nicht das, was du an der Kasse zahlst. Zu zahlen sind 120 € − 36 € = 84 €.',
  'bild': {'typ': 'saeulen', 'einheit': '€', 'werte': [{'name': 'Preis vorher', 'wert': 120}, {'name': 'Rabatt (30 %)', 'wert': 36}, {'name': 'zu zahlen', 'wert': 84}], 'y_start': 0, 'zahlen': True}},
 'zurueck': {
  'einstieg': 'Auf dem Kassenzettel steht für ein T-Shirt 59,50 €. Darin steckt die Mehrwertsteuer von 19 %, die der Laden an den Staat weitergibt. Wie viel kostet das T-Shirt ohne Steuer? Diesmal kennst du den Wert nachher und suchst den Wert vorher – du rechnest ⟦zurück zum Grundwert⟧.',
  'woerter': [['Mehrwertsteuer', 'Steuer, die auf den Preis aufgeschlagen wird; meist 19 % vom Preis ohne Steuer'], ['Nettopreis', 'der Preis ohne Steuer; er ist hier der Grundwert (100 %)'],
              ['Endpreis', 'der Preis mit Steuer, der an der Kasse steht (hier 119 %)'], [':', 'Geteiltzeichen'], ['±', 'plus oder minus – je nachdem, ob der Wert gestiegen oder gesunken ist']],
  'schritte': ['Der Nettopreis ist der Grundwert, also 100 %. Mit Steuer sind es 100 % + 19 % = 119 %. Der Faktor ist 1,19.',
               'Es gilt also: Nettopreis · 1,19 = 59,50 €.',
               'Rückwärts rechnen heißt: Statt malzunehmen wird geteilt. Nettopreis = 59,50 € : 1,19.',
               'Ausrechnen ergibt den Nettopreis: ⟦50 €⟧.'],
  'regel': 'So kommst du ⟦zurück zum Grundwert⟧: Teile den neuen Wert durch den Faktor. ⟦Grundwert = neuer Wert : (1 ± p/100)⟧ – plus bei einer Erhöhung, minus bei einer Senkung.',
  'fehler': 'Der Nettopreis ist nicht 59,50 € minus 19 % von 59,50 € (das wären etwa 48,20 €). Die 19 % wurden auf den ⟦Nettopreis⟧ aufgeschlagen, also auf den kleineren Betrag, nicht auf den Endpreis. Darum wird durch 1,19 geteilt.',
  'bild': {'typ': 'tabelle', 'kopf': ['', 'Anteil', 'Betrag'], 'zeilen': [['Nettopreis (ohne Steuer, Grundwert)', '100 %', '? (gesucht)'], ['Mehrwertsteuer', '19 %', ''], ['Endpreis (mit Steuer)', '119 %', '59,50 €']]}},
 'prozentsatz': {
  'einstieg': 'Ein Paar Turnschuhe hat letzte Woche 40 € gekostet, heute kostet es 46 €. Um wie viel Prozent ist der Preis gestiegen? Du kennst beide Preise und suchst die Änderung in Prozent. Diese Prozentzahl heißt ⟦Prozentsatz der Änderung⟧.',
  'woerter': [['Prozentsatz', 'die Prozentzahl, zum Beispiel 15 %'], ['Abnahme', 'der Wert wird kleiner (Gegenteil von Zunahme)'],
              ['(Faktor − 1) · 100 %', 'vom Faktor 1 abziehen und mit 100 malnehmen: aus 1,15 wird 0,15, also 15 %']],
  'schritte': ['Der alte Preis 40 € ist der Grundwert. Auf ihn bezieht man die Änderung.',
               'Teile den neuen Preis durch den alten: 46 : 40 = 1,15. Das ist der Faktor.',
               'Der Faktor ist größer als 1. Der Preis ist also gestiegen.',
               'Ziehe 1 ab und nimm mal 100: (1,15 − 1) · 100 % = ⟦15 % Zunahme⟧.'],
  'regel': 'So findest du den ⟦Prozentsatz der Änderung⟧: Teile den neuen Wert durch den ⟦alten⟧ Wert. Liegt der Faktor über 1, ist es eine Zunahme, unter 1 eine Abnahme. Dann gilt ⟦p % = (Faktor − 1) · 100 %⟧; ein Minus im Ergebnis bedeutet Abnahme.',
  'fehler': 'Von 40 € auf 46 € sind es nicht 6 %. 6 € ist die Änderung in Euro. In Prozent musst du sie auf den ⟦alten Preis 40 €⟧ beziehen: 6 : 40 = 0,15 = 15 %. Nur wenn der alte Preis 100 € gewesen wäre, wären 6 € auch 6 %.',
  'bild': {'typ': 'tabelle', 'kopf': ['', 'Preis'], 'zeilen': [['vorher (Grundwert)', '40 €'], ['nachher', '46 €'], ['Faktor = nachher : vorher', '1,15']]}},
 'mehrfach': {
  'einstieg': 'Eine Spielkonsole kostet 200 €. Im Herbst steigt ihr Preis um 10 %, im Januar sinkt er wieder um 10 %. Viele denken: Dann kostet sie wieder 200 €. Das stimmt aber nicht! Ändert sich ein Preis mehrmals hintereinander, rechnet man mit ⟦mehreren Faktoren nacheinander⟧.',
  'woerter': [['nacheinander', 'erst die eine Änderung, dann die nächste – jede bezieht sich auf den gerade aktuellen Preis'], ['Gesamtfaktor', 'alle Faktoren miteinander malgenommen; er ersetzt alle Schritte auf einmal']],
  'schritte': ['Erste Änderung, plus 10 %: Faktor 1,1. Also 200 € · 1,1 = 220 €.',
               'Zweite Änderung, minus 10 %: Faktor 0,9. Sie bezieht sich auf die 220 €: 220 € · 0,9 = 198 €.',
               'Schneller geht es mit dem Gesamtfaktor: 1,1 · 0,9 = 0,99. Also 200 € · 0,99 = 198 €.',
               'Ergebnis: ⟦198 €⟧ – das sind 2 € weniger als am Anfang.'],
  'regel': 'So rechnest du bei Änderungen ⟦nacheinander⟧: Schreibe für jede Änderung den Faktor auf und ⟦nimm die Faktoren mal⟧. Die Prozentsätze darfst du nicht zusammenzählen.',
  'fehler': '+10 % und danach −10 % heben sich nicht auf. Die −10 % werden vom ⟦schon erhöhten⟧ Preis 220 € abgezogen – das sind 22 €, also mehr als die 20 €, um die er vorher gestiegen ist. Darum landet man bei 198 € und nicht bei 200 €.',
  'bild': {'typ': 'tabelle', 'kopf': ['Schritt', 'Faktor', 'Preis danach'], 'zeilen': [['Start', '—', '200 €'], ['+10 %', '· 1,1', '220 €'], ['−10 %', '· 0,9', '198 €']]}},
 'argumente': {
  'einstieg': 'Ein Laden wirbt: „Heute 20 % Rabatt – und an der Kasse noch einmal 10 %. Zusammen 30 %!“ Stimmt das? Um so eine Behauptung zu prüfen, rechnest du nach. Eine Begründung, die mit einer Rechnung zeigt, ob etwas stimmt, heißt ⟦mathematisches Argument⟧.',
  'woerter': [['Aussage', 'ein Satz, der wahr oder falsch sein kann'], ['mathematisches Argument', 'eine Begründung mit Rechnung, die jeder nachprüfen kann'],
              ['außermathematisches Argument', 'ein Grund ohne Rechnung, zum Beispiel „das klingt fair“ oder „das steht auf dem Schild“'], ['Ersparnis', 'wie viel Prozent man insgesamt weniger zahlt']],
  'schritte': ['Die Aussage lautet: „20 % Rabatt und dann noch 10 % sind zusammen 30 %.“',
               'Die Faktoren sind 0,8 (für 20 % weniger) und 0,9 (für 10 % weniger). Nacheinander malnehmen: 0,8 · 0,9 = 0,72.',
               'Man zahlt also 72 % des alten Preises. Die Ersparnis ist 100 % − 72 % = 28 %.',
               '28 % ist weniger als 30 %. Die Aussage ist ⟦falsch⟧.'],
  'regel': 'So prüfst du eine Aussage: ⟦rechnerisch⟧, also mit einem mathematischen Argument. Gründe ohne Rechnung („klingt fair“, „macht jeder Laden so“) sind ⟦außermathematische⟧ Argumente – sie beweisen nichts.',
  'fehler': '„Der Laden wirbt doch mit 30 %, also stimmt es“ ist ⟦kein mathematisches⟧ Argument. Ein Werbeschild kann sich irren – nur die Rechnung entscheidet.'},
}
for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl7.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl7 import mit_umbau  # noqa: E402


def _streifen(neu=None, oben=''):
    """Prozentstreifen: 100 % als Rechteck (Länge 10); neu = Prozentwert danach (z. B. 115 oder 85)."""
    pk = {'_a': [0, 0], '_b': [10, 0], '_e': [10, 1.5], '_f': [0, 1.5]}
    li = [['_a', '_b', '100 % = Grundwert'], ['_b', '_e'], ['_f', '_a']]
    fl = None
    if neu is None:
        li.append(['_e', '_f'])
    elif neu > 100:
        x = 10 + (neu - 100) / 10
        pk.update({'_c': [x, 0], '_d': [x, 1.5]})
        li += [['_b', '_c', f'+{neu - 100} %'], ['_c', '_d'], ['_d', '_f', oben]]
        fl = ['_b', '_c', '_d', '_e']
    else:
        x = neu / 10
        pk.update({'_c': [x, 0], '_d': [x, 1.5]})
        li += [['_c', '_d', '', 'gestrichelt'], ['_e', '_f', oben]]
        fl = ['_c', '_b', '_e', '_d']
    b = {'typ': 'figur', 'punkte': pk, 'linien': li}
    if fl: b['flaeche'] = fl
    return b


UMBAU = {
 'faktor': {
  'einstieg': 'Im Sportgeschäft steigen alle Preise um 15 %. Ein Ball für 100 € kostet dann 115 €. Mit einer einzigen Zahl rechnest du jeden neuen Preis aus: dem ⟦Wachstumsfaktor⟧.',
  'woerter': [['%', 'Prozent, also Hundertstel: 15 % = 15/100 = 0,15'], ['Grundwert', 'der Wert vorher; er zählt als 100 %'],
              ['Wachstumsfaktor', 'die Zahl, mit der man den alten Wert malnimmt']],
  'bild': _streifen(),
  'schritte': [{'text': 'Der alte Preis ist der Grundwert. Er zählt als 100 %.'},
               {'text': 'Dazu kommen 15 %. Neu sind es 100 % + 15 % = 115 %.', 'bild': _streifen(115, '115 %')},
               {'text': '115 % = 115/100 = ⟦1,15⟧. Das ist der Wachstumsfaktor.', 'bild': _streifen(115, '115 % → Faktor 1,15')},
               {'text': 'Bei 15 % weniger bleiben 85 %. Der Faktor ist ⟦0,85⟧.', 'bild': _streifen(85, '85 % → Faktor 0,85')}],
  'fehler': 'Der Faktor für 15 % mehr ist nicht 0,15. Mal 0,15 ergibt nur die Erhöhung: 15 € statt 115 € für den Ball.',
  'regel': 'Der ⟦Wachstumsfaktor⟧ ist der neue Prozentwert geteilt durch 100. Plus 15 % ergibt 1,15, minus 15 % ergibt 0,85.'},
 'vermehrt': {
  'einstieg': 'Ein Fahrrad kostet 480 €. Nächsten Monat wird es 5 % teurer. Mit dem Faktor rechnest du den neuen Preis in einem Schritt aus. Er heißt ⟦vermehrter Grundwert⟧.',
  'woerter': [['vermehrter Grundwert', 'der Wert nach einer Erhöhung'], ['·', 'Malzeichen']],
  'bild': {'typ': 'saeulen', 'einheit': '€', 'werte': [{'name': 'vorher', 'wert': 480}], 'y_start': 0, 'zahlen': True},
  'schritte': [{'text': 'Der alte Preis ist der Grundwert: 480 €.'},
               {'text': '5 % mehr heißt: Faktor 1 + 5/100 = 1,05.'},
               {'text': 'Neuer Preis: 480 € · 1,05 = ⟦504 €⟧. Das ist der vermehrte Grundwert.',
                'bild': {'werte': [{'name': 'vorher', 'wert': 480}, {'name': 'nachher', 'wert': 504}]}}],
  'fehler': '480 € + 5 = 485 € ist falsch. 5 % sind nicht 5 €, sondern 5 Hundertstel von 480 €, also ⟦24 €⟧.',
  'fehler_bild': {'werte': [{'name': 'vorher', 'wert': 480}, {'name': 'falsch', 'wert': 485}, {'name': 'richtig', 'wert': 504}]},
  'regel': 'Neuer Wert = ⟦Grundwert · Faktor⟧. Bei 5 % mehr ist der Faktor 1,05.'},
 'vermindert': {
  'einstieg': 'Eine Jacke kostet 120 €. Im Schlussverkauf gibt es 30 % Rabatt. Was zahlst du? Der neue, kleinere Preis heißt ⟦verminderter Grundwert⟧.',
  'woerter': [['Rabatt', 'Preisnachlass in Prozent'], ['verminderter Grundwert', 'der Wert nach einer Senkung']],
  'bild': {'typ': 'bruchstreifen', 'teile': 10, 'gefaerbt': 10, 'ganzes': '120 €', 'teil_text': '100 %'},
  'schritte': [{'text': 'Teile den Preis in 10 gleiche Teile. Jeder Teil sind 10 % = 12 €.'},
               {'text': '30 % Rabatt nehmen 3 Teile weg. Es bleiben 70 %, also Faktor 0,7.', 'bild': {'gefaerbt': 7, 'teil_text': '70 %'}},
               {'text': 'Du zahlst 120 € · 0,7 = ⟦84 €⟧. Das ist der verminderte Grundwert.', 'bild': {'teil_text': '84 €'}}],
  'fehler': '120 € · 0,3 = 36 € ist der Rabatt, nicht der Preis. Das sparst du nur. Zahlen musst du ⟦84 €⟧.',
  'fehler_bild': {'gefaerbt': 3, 'teil_text': '36 € gespart'},
  'regel': 'Bei Rabatt nimmst du mal den ⟦Rest-Anteil⟧. 30 % Rabatt heißt: mal 0,7.'},
 'zurueck': {
  'einstieg': 'Auf dem Kassenzettel steht 59,50 € für ein T-Shirt. Darin stecken 19 % Steuer. Wie viel kostet es ohne Steuer? Du rechnest ⟦zurück zum Grundwert⟧.',
  'woerter': [['Mehrwertsteuer', 'Steuer, die auf den Preis aufgeschlagen wird, meist 19 %'], ['Nettopreis', 'der Preis ohne Steuer; er ist hier der Grundwert']],
  'bild': {'typ': 'tabelle', 'kopf': ['', 'Anteil', 'Betrag'], 'zeilen': [['ohne Steuer', '100 %', '?'], ['Steuer', '19 %', '?'], ['mit Steuer', '119 %', '59,50 €']]},
  'schritte': [{'text': 'Der Nettopreis ist 100 %. Mit Mehrwertsteuer sind es 119 %.'},
               {'text': 'Also gilt: Nettopreis · 1,19 = 59,50 €.'},
               {'text': 'Rückwärts wird geteilt: 59,50 € : 1,19 = ⟦50 €⟧.',
                'bild': {'zeilen': [['ohne Steuer', '100 %', '50 €'], ['Steuer', '19 %', '9,50 €'], ['mit Steuer', '119 %', '59,50 €']]}}],
  'fehler': 'Nicht 19 % von 59,50 € abziehen: Das ergibt 48,20 €. Die 19 % kamen auf den kleineren Nettopreis. Darum ⟦durch 1,19 teilen⟧.',
  'regel': 'Zurück zum Grundwert: ⟦neuer Wert : Faktor⟧. Teilen macht das Malnehmen rückgängig.'},
 'prozentsatz': {
  'einstieg': 'Turnschuhe kosteten letzte Woche 40 €, heute 46 €. Um wie viel Prozent ist der Preis gestiegen? Gesucht ist der ⟦Prozentsatz⟧ der Änderung.',
  'woerter': [['Prozentsatz', 'die Prozentzahl, zum Beispiel 15 %']],
  'bild': {'typ': 'saeulen', 'einheit': '€', 'werte': [{'name': 'vorher', 'wert': 40}, {'name': 'heute', 'wert': 46}], 'y_start': 0, 'zahlen': True},
  'schritte': [{'text': 'Teile den neuen Preis durch den alten: 46 : 40 = 1,15.'},
               {'text': '1,15 ist größer als 1. Der Preis ist also gestiegen.'},
               {'text': '1,15 = 115 %. Das sind ⟦15 % mehr⟧ als vorher.'}],
  'fehler': '6 € mehr sind nicht 6 %. Die 6 € beziehen sich auf die alten 40 €: 6 : 40 = ⟦15 %⟧.',
  'regel': 'Teile neu durch ⟦alt⟧ und vergleiche mit 100 %. Mehr als 100 % heißt Zunahme, weniger heißt Abnahme.'},
 'mehrfach': {
  'einstieg': 'Eine Spielkonsole kostet 200 €. Im Herbst wird sie 10 % teurer, im Januar wieder 10 % billiger. Kostet sie dann 200 €? Nein – man rechnet mit ⟦Faktoren nacheinander⟧.',
  'woerter': [['Gesamtfaktor', 'alle Faktoren miteinander malgenommen']],
  'bild': {'typ': 'saeulen', 'einheit': '€', 'werte': [{'name': 'Start', 'wert': 200}], 'y_start': 0, 'zahlen': True},
  'schritte': [{'text': 'Plus 10 %: 200 € · 1,1 = 220 €.', 'bild': {'werte': [{'name': 'Start', 'wert': 200}, {'name': 'Herbst', 'wert': 220}]}},
               {'text': 'Minus 10 % vom neuen Preis: 220 € · 0,9 = ⟦198 €⟧.',
                'bild': {'werte': [{'name': 'Start', 'wert': 200}, {'name': 'Herbst', 'wert': 220}, {'name': 'Januar', 'wert': 198}]}},
               {'text': 'Schneller mit dem Gesamtfaktor: 1,1 · 0,9 = 0,99.'}],
  'fehler': '+10 % und −10 % heben sich nicht auf. Die 10 % Abzug rechnet man von 220 €: Das sind 22 €, nicht 20 €.',
  'regel': 'Bei mehreren Änderungen ⟦Faktoren malnehmen⟧. Die Prozentsätze darfst du nicht addieren.'},
 'argumente': {
  'einstieg': 'Ein Laden wirbt: „20 % Rabatt und an der Kasse noch einmal 10 %. Zusammen 30 %!“ Stimmt das? Eine Begründung mit Rechnung heißt ⟦mathematisches Argument⟧.',
  'woerter': [['mathematisches Argument', 'eine Begründung mit Rechnung, die jeder nachprüfen kann'],
              ['außermathematisch', 'ein Grund ohne Rechnung, zum Beispiel „das klingt fair“']],
  'bild': {'typ': 'saeulen', 'einheit': '%', 'werte': [{'name': 'vorher', 'wert': 100}], 'y_start': 0, 'zahlen': True},
  'schritte': [{'text': 'Nach 20 % Rabatt zahlst du noch 80 % des Preises.', 'bild': {'werte': [{'name': 'vorher', 'wert': 100}, {'name': '−20 %', 'wert': 80}]}},
               {'text': 'Davon gehen noch 10 % weg: 0,8 · 0,9 = 0,72.',
                'bild': {'werte': [{'name': 'vorher', 'wert': 100}, {'name': '−20 %', 'wert': 80}, {'name': '−10 %', 'wert': 72}]}},
               {'text': 'Du zahlst 72 % und sparst 28 %. Die Werbung ist ⟦falsch⟧.'},
               {'text': 'Das Werbeschild selbst ist nur ein außermathematisches Argument.'}],
  'fehler': '„Der Laden schreibt doch 30 %, also stimmt es“ ist kein mathematisches Argument. Nur die ⟦Rechnung⟧ entscheidet.',
  'regel': 'Prüfe Aussagen mit einer ⟦Rechnung⟧. Gründe wie „klingt fair“ beweisen nichts.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---------- Zehnte Runde (schwer-kl7): schwerere Übungen nach Prüfungsvorbild ----------
# Vorbilder (nur Typ und Niveau, eigene Zahlen und Einkleidung): Bayerischer Mathematik-Test 8 (ISB) 2019 B6, 2021 A5/A6,
# 2023 A6, 2024 A3, 2025 A6; Jahrgangsstufentest Realschule 8 (2025, Nr. 17/19). Eigener Zufallsstart, alte Aufgaben bleiben gleich.
from _schwer_kl7 import Neu, anhaengen  # noqa: E402


def schwer():
    N = Neu(7094)
    P = 'pruefung'
    K = 'knobel'
    # faktor
    N.Z('faktor', 2, 'Ein Preis sinkt AUF 85 % des alten Preises. Mit welchem Faktor multiplizierst du?', Fr('0.85'), '85/100',
        '„Auf 85 %“ heißt: Der neue Preis ist 85 % vom alten. Faktor 85 : 100 = 0,85 (nicht 0,15 wie bei „um 85 %“).',
        'Achte auf das kleine Wort: „auf“ oder „um“?')
    N.Z('faktor', 2, 'Ein Wert wird verdoppelt. Um wie viel Prozent ist er gestiegen?', 100, '(2 - 1) * 100',
        'Verdoppeln heißt Faktor 2 = 200 %. Gegenüber 100 % sind das 100 % mehr.', 'Faktor 2 bedeutet 200 % des alten Werts. Wie viel ist dazugekommen?', einheit='%')
    N.Z('faktor', 3, 'Ein Wert wird verdreifacht. Um wie viel Prozent ist er gestiegen?', 200, '(3 - 1) * 100',
        'Verdreifachen: Faktor 3 = 300 %. Dazugekommen sind 300 % − 100 % = 200 %, nicht 300 %.',
        'Der alte Wert ist 100 %. Rechne aus, wie viel Prozent DAZUkommen.', einheit='%', art=K)
    N.Z('faktor', 3, 'Eine Filteranlage entfernt 99 % der Staubteilchen aus der Luft. Vorher sind es 3 000 000 Teilchen pro Kubikmeter. '
        'Wie viele Teilchen pro Kubikmeter bleiben übrig?', 30000, '3000000 * (1 - 99/100)',
        'Es bleiben 100 % − 99 % = 1 % übrig. Faktor 0,01: 3 000 000 · 0,01 = 30 000.',
        'Nicht die entfernten Teilchen sind gefragt. Wie viel Prozent bleiben?', art=P)
    N.A('faktor', 3, 'In einem Chor sind 20 % weniger Männer als Frauen. m ist die Zahl der Männer, f die Zahl der Frauen. Welche Gleichung passt?',
        'm = 0,8 · f', ['f = 0,8 · m', 'm = f − 0,2', 'f = 1,2 · m'],
        'Die Frauen sind der Grundwert (100 %). Die Männer sind 80 % davon: m = 0,8 · f. f = 1,2 · m stimmt nicht: Dann wären es 20 % mehr Frauen als Männer – das ist eine andere Aussage.',
        'Wer ist hier der Grundwert, also 100 %? Die Gruppe nach „als“.', art=P)
    N.L('faktor', 3, 'Ein Wert wird um 20 % erhöht. Mit welchem Faktor musst du das Ergebnis multiplizieren, um wieder beim Ausgangswert zu sein? Gib den Faktor als gekürzten Bruch an.',
        '□/□', [5, 6], ['5', '6'],
        'Erhöhen um 20 %: mal 1,2 = 6/5. Rückgängig machen: mal 5/6 (der Kehrbruch). 5/6 ≈ 0,833, also nicht 0,8.',
        'Teilen durch 1,2 ist dasselbe wie mal den Kehrbruch. Schreibe 1,2 als Bruch.', 'Zähler und Nenner eintragen.', art=K)
    # vermehrt
    N.Z('vermehrt', 2, 'Eine Gemeinde hat 12 500 Einwohner. Die Zahl wächst um 4 %. Wie viele Einwohner sind es danach?', 13000, '12500 * 1.04',
        'Faktor 1,04: 12 500 · 1,04 = 13 000 Einwohner.', 'Plus 4 % heißt mal 1,04.', einheit='Einwohner')
    N.Z('vermehrt', 2, 'Eine Kinokarte kostet 9,50 €. Der Preis steigt um 20 %. Wie viel kostet sie danach?', Fr('11.4'), '9.5 * 1.2',
        'Faktor 1,2: 9,50 € · 1,2 = 11,40 €.', 'Plus 20 % heißt mal 1,2.', einheit='€')
    N.A('vermehrt', 3, 'Was berechnet der Term 250 · 1,08 in diesem Satz: „Ein Fahrrad kostet 250 €, der Preis steigt um 8 %.“?',
        'den neuen Preis nach der Erhöhung', ['nur die Erhöhung in Euro', 'den Preis nach einer Erhöhung um 108 %', 'den alten Preis vor der Erhöhung'],
        '1,08 = 100 % + 8 %. 250 · 1,08 = 270 ist der neue Preis. Die Erhöhung allein wäre 250 · 0,08 = 20 €.',
        'Zerlege 1,08 in 1 + 0,08. Wofür steht die 1, wofür die 0,08?', art=P)
    N.Z('vermehrt', 3, 'Eine Handwerkerin berechnet 600 € für Material und 4 Arbeitsstunden zu je 55 € (alles ohne Mehrwertsteuer). Dazu kommen 19 % Mehrwertsteuer. '
        'Wie hoch ist der Rechnungsbetrag?', Fr('975.8'), '(600 + 4 * 55) * 1.19',
        'Netto: 600 € + 4 · 55 € = 820 €. Mit Mehrwertsteuer: 820 € · 1,19 = 975,80 €.',
        'Erst alles zusammenzählen, dann einmal mal 1,19.', einheit='€', art=P)
    N.Z('vermehrt', 3, 'Bei 3 % Zinsen bekommt jemand nach einem Jahr 54 € Zinsen. Wie hoch ist das Guthaben nach der Zinsgutschrift?', 1854, '54 / 0.03 * 1.03',
        '54 € sind 3 % des Guthabens. 54 € : 0,03 = 1 800 € (Grundwert). Danach: 1 800 € · 1,03 = 1 854 €.',
        'Erst den Grundwert aus den Zinsen bestimmen, dann die Zinsen dazurechnen.', einheit='€', art=P)
    N.Z('vermehrt', 3, 'Ein Händler schlägt 25 % auf den Einkaufspreis auf. Der Verkaufspreis ist dadurch 15 € höher als der Einkaufspreis. Wie hoch ist der Verkaufspreis?', 75, '15 / 0.25 * 1.25',
        '15 € sind 25 % des Einkaufspreises: 15 € : 0,25 = 60 €. Verkaufspreis: 60 € · 1,25 = 75 €.',
        'Die 15 € sind der Aufschlag. Welcher Anteil vom Einkaufspreis ist das?', einheit='€', art=K)
    # vermindert
    N.Z('vermindert', 2, 'Ein Fahrradhelm kostet 64 €. Vereinsmitglieder bekommen 12,5 % Rabatt. Was zahlt ein Mitglied?', 56, '64 * (1 - 0.125)',
        'Faktor 1 − 0,125 = 0,875: 64 € · 0,875 = 56 €.', 'Minus 12,5 % heißt mal 0,875.', einheit='€')
    N.A('vermindert', 2, 'Tom soll den Preis einer Jacke für 240 € nach 15 % Rabatt berechnen. Er rechnet 240 · 0,15 = 36. Was stimmt?',
        'Er hat nur den Rabatt berechnet. Der neue Preis ist 204 €.', ['Richtig, die Jacke kostet jetzt 36 €.', 'Der neue Preis ist 240 € − 15 € = 225 €.', 'Der neue Preis ist 240 € · 1,15 = 276 €.'],
        '240 · 0,15 = 36 € ist der Rabatt. Neuer Preis: 240 € · 0,85 = 204 €.', 'Was bedeutet 15 % von 240 € – den Rabatt oder den Rest?')
    N.Z('vermindert', 3, 'Früher brauchte eine Familie im Jahr 80 Plastiktüten. Durch Stoffbeutel sinkt der Verbrauch um 65 %. Wie viele Tüten sind es danach?', 28, '80 * (1 - 65/100)',
        'Es bleiben 100 % − 65 % = 35 %: 80 · 0,35 = 28 Tüten.', 'Wie viel Prozent bleiben übrig?', einheit='Tüten', art=P)
    N.Z('vermindert', 3, 'Das Diagramm zeigt verkaufte Eintrittskarten. Am Mittwoch wurden 25 % weniger Karten verkauft als am Dienstag. Wie viele waren es am Mittwoch?', 240, '320 * 0.75',
        'Am Dienstag: 320 Karten (abgelesen). Minus 25 %: 320 · 0,75 = 240 Karten.', 'Lies zuerst den Dienstag ab. Grundwert ist der Dienstag.', einheit='Karten', art=P,
        grafik={'typ': 'saeulen', 'einheit': 'Karten', 'werte': [{'name': 'Mo', 'wert': 200}, {'name': 'Di', 'wert': 320}], 'zahlen': True})
    N.Z('vermindert', 3, 'Ein Preis wird erst um 20 % gesenkt. Um wie viel Prozent muss der neue Preis noch einmal gesenkt werden, damit er insgesamt halb so groß ist wie am Anfang?', Fr('37.5'), '(1 - 0.5 / 0.8) * 100',
        'Nach −20 %: Faktor 0,8. Gesucht ist x mit 0,8 · x = 0,5, also x = 0,625. Das ist eine Senkung um 37,5 % (nicht um 30 %).',
        'Schreibe es mit Faktoren: 0,8 · ? = 0,5.', einheit='%', art=K)
    N.Z('vermindert', 3, 'Ein Akku hat neu 4 000 mAh. Jedes Jahr verliert er 10 % seiner Kapazität vom Jahresanfang. Wie groß ist die Kapazität nach 2 Jahren?', 3240, '4000 * 0.9 * 0.9',
        'Jahr 1: 4 000 · 0,9 = 3 600. Jahr 2: 3 600 · 0,9 = 3 240 mAh (nicht 4 000 · 0,8 = 3 200).', 'Im zweiten Jahr ist der Grundwert schon kleiner.', einheit='mAh')
    # zurueck
    N.Z('zurueck', 2, 'Nach 25 % Rabatt zahlt man 63 €. Wie hoch war der Preis vorher?', 84, '63 / 0.75',
        '63 € sind 75 % des alten Preises: 63 € : 0,75 = 84 €.', 'Durch den Faktor teilen, nicht 25 % dazurechnen.', einheit='€')
    N.Z('zurueck', 2, 'Eine Monatskarte kostet jetzt 57,20 €. Das sind 4 % mehr als vorher. Wie viel kostete sie vorher?', 55, '57.2 / 1.04',
        '57,20 € sind 104 % des alten Preises: 57,20 € : 1,04 = 55 €.', 'Der neue Preis ist 104 % des alten.', einheit='€', art=P)
    N.Z('zurueck', 3, '1 368 Kinder haben die Fahrradprüfung bestanden. Das sind 72 % aller Kinder, die teilgenommen haben. Wie viele Kinder haben teilgenommen?', 1900, '1368 / 0.72',
        '1 368 sind 72 % von allen: 1 368 : 0,72 = 1 900 Kinder.', 'Die 1 368 sind der Prozentwert. Gesucht ist der Grundwert.', einheit='Kinder', art=P)
    N.Z('zurueck', 3, 'Ein Preis mit 19 % Mehrwertsteuer beträgt 99,96 €. Wie viel Euro Mehrwertsteuer sind darin enthalten?', Fr('15.96'), '99.96 - 99.96 / 1.19',
        'Netto: 99,96 € : 1,19 = 84 €. Steuer: 99,96 € − 84 € = 15,96 € (nicht 19 % von 99,96 €).',
        'Die 19 % beziehen sich auf den Nettopreis, nicht auf 99,96 €.', einheit='€', art=P)
    N.Z('zurueck', 3, 'Ein Schild sagt: „Jetzt 20 % billiger: 48 €“. Ein Kunde rechnet den alten Preis so aus: 48 € + 20 % = 57,60 €. Um wie viel Euro liegt er daneben?', Fr('2.4'), '48 / 0.8 - 48 * 1.2',
        'Richtig: 48 € : 0,8 = 60 €. Der Kunde hat 57,60 €. Unterschied: 60 € − 57,60 € = 2,40 €.',
        'Rechne zuerst den richtigen alten Preis aus. Die 20 % gehören zum alten Preis.', einheit='€', art=K)
    N.Z('zurueck', 3, 'Ein Preis wurde erst um 10 % gesenkt, das Ergebnis dann um 10 % erhöht. Jetzt kostet die Ware 99 €. Wie viel kostete sie am Anfang?', 100, '99 / (0.9 * 1.1)',
        'Gesamtfaktor 0,9 · 1,1 = 0,99. Anfangspreis: 99 € : 0,99 = 100 €.', 'Fasse beide Änderungen zu einem Faktor zusammen.', einheit='€')
    # prozentsatz
    N.Z('prozentsatz', 2, 'Ein Verein hatte 160 Mitglieder, jetzt sind es 136. Um wie viel Prozent hat sich die Zahl geändert? (Zunahme positiv, Abnahme negativ)', -15, '(136 / 160 - 1) * 100',
        '136 : 160 = 0,85 = 85 %. Das sind 15 % weniger: −15 %.', 'Teile neu durch alt.', einheit='%')
    N.Z('prozentsatz', 2, 'In Woche 1 waren 12 von 40 verkauften Äpfeln Bio-Äpfel. In Woche 2 wurden 70 Äpfel verkauft, der Bio-Anteil war gleich. Wie viele Bio-Äpfel waren es in Woche 2?', 21, '70 * 12 / 40',
        'Bio-Anteil: 12 : 40 = 0,3 = 30 %. Woche 2: 70 · 0,3 = 21 Bio-Äpfel.', 'Bestimme zuerst den Anteil in Prozent.', einheit='Äpfel', art=P)
    N.Z('prozentsatz', 3, 'Ein Kleinbus hat 36 Sitzplätze, ein Reisebus 45. Um wie viel Prozent hat der Kleinbus WENIGER Plätze als der Reisebus?', 20, '(45 - 36) / 45 * 100',
        'Grundwert ist der Reisebus (nach „als“): 9 : 45 = 0,2 = 20 %.', 'Der Vergleichswert nach „als“ ist 100 %.', einheit='%', art=P)
    N.Z('prozentsatz', 3, 'Ein Kleinbus hat 36 Sitzplätze, ein Reisebus 45. Um wie viel Prozent hat der Reisebus MEHR Plätze als der Kleinbus?', 25, '(45 - 36) / 36 * 100',
        'Jetzt ist der Kleinbus der Grundwert: 9 : 36 = 0,25 = 25 %. Gleicher Unterschied, anderer Grundwert – darum nicht 20 %.',
        'Wer steht nach „als“? Der ist jetzt 100 %.', einheit='%', art=P)
    N.Z('prozentsatz', 3, 'Der Anteil der Kinder, die mit dem Rad zur Schule fahren, steigt von 20 % auf 25 %. Um wie viel PROZENT ist der Anteil gestiegen?', 25, '(25 - 20) / 20 * 100',
        'Der Anteil steigt um 5 Prozentpunkte. In Prozent: 5 : 20 = 0,25 = 25 %.', 'Prozentpunkte und Prozent sind nicht dasselbe. Bezieh die Änderung auf den alten Anteil.', einheit='%', art=P)
    N.Z('prozentsatz', 3, 'Eine Größe steigt um 25 %. Um wie viel Prozent ist der alte Wert kleiner als der neue?', 20, '(1 - 1 / 1.25) * 100',
        'Neu = 1,25 · alt, also alt = neu : 1,25 = 0,8 · neu. Der alte Wert ist 20 % kleiner als der neue.',
        'Nimm einen Beispielwert, z. B. alt = 100. Dann ist neu = 125. Grundwert ist jetzt der neue Wert.', einheit='%', art=K)
    # mehrfach
    N.Z('mehrfach', 2, 'Eine Miete von 800 € steigt zwei Jahre nacheinander um je 5 %. Wie hoch ist sie danach?', 882, '800 * 1.05 * 1.05',
        '800 € · 1,05 · 1,05 = 882 € (nicht 800 € · 1,10 = 880 €).', 'Zweimal mal 1,05.', einheit='€')
    N.Z('mehrfach', 2, 'Ein Fernseher kostet ohne Mehrwertsteuer 500 €. Erst gibt es 20 % Rabatt, danach kommen 19 % Mehrwertsteuer dazu. Wie viel kostet er?', 476, '500 * 0.8 * 1.19',
        '500 € · 0,8 · 1,19 = 476 €.', 'Beide Änderungen als Faktoren nacheinander.', einheit='€')
    N.Z('mehrfach', 3, 'Ein Laden wirbt: „Zweimal 25 % Rabatt – also halber Preis!“ Ein Pulli kostet 80 €. Wie viel kostet er nach beiden Rabatten wirklich?', 45, '80 * 0.75 * 0.75',
        '80 € · 0,75 · 0,75 = 45 €. Halber Preis wären 40 €. Die Werbung stimmt nicht.', 'Rabatte nacheinander: Faktoren malnehmen.', einheit='€', art=P)
    N.Z('mehrfach', 3, '2 000 € werden 3 Jahre lang mit 2 % pro Jahr verzinst; die Zinsen bleiben auf dem Konto. Wie hoch ist das Guthaben danach? Runde auf Cent.', Fr('2122.42'), 'round(2000 * 1.02**3, 2)',
        '2 000 € · 1,02 · 1,02 · 1,02 ≈ 2 122,42 €. Ohne Zinseszins wären es nur 2 120 €.', 'Jedes Jahr mal 1,02 – auch auf die Zinsen vom Vorjahr.', einheit='€', toleranz=0.01, art=P)
    N.Z('mehrfach', 3, 'Ein Preis sinkt um 25 %. Um wie viel Prozent muss er danach steigen, damit er wieder so hoch ist wie vorher? Runde auf eine Nachkommastelle.', Fr('33.3'), 'round((1 / 0.75 - 1) * 100, 1)',
        'Nach dem Senken: Faktor 0,75. Zurück: mal 1 : 0,75 ≈ 1,333. Das sind etwa 33,3 % Erhöhung, nicht 25 %.',
        'Welcher Faktor macht mal 0,75 wieder rückgängig?', einheit='%', toleranz=0.1, art=K)
    assert (1 + Fr(20, 100)) * (1 - Fr(20, 100)) == Fr('0.96')
    N.Z('mehrfach', 3, 'Ein Preis steigt um p % und sinkt danach um p %. Danach ist er 4 % niedriger als am Anfang. Wie groß ist p?', 20, '100 * 0.2',
        '(1 + p/100) · (1 − p/100) = 0,96. Ausprobieren: p = 20 gibt 1,2 · 0,8 = 0,96. Also p = 20.',
        'Probiere Werte für p aus und rechne die Faktoren aus: p = 10, p = 20, …', einheit='%', art=K)
    # argumente
    N.A('argumente', 2, 'Zwei Angebote für dieselbe Hose: A kostet 60 € mit 15 % Rabatt, B kostet 54 €. Welche Begründung ist mathematisch?',
        'A ist günstiger, denn 60 € · 0,85 = 51 € < 54 €.', ['B ist günstiger, denn bei B gibt es keine versteckten Kosten.', 'A ist günstiger, denn Rabatt ist immer gut.', 'B ist günstiger, denn 54 € ist eine runde Zahl.'],
        'Nur eine Rechnung beweist etwas: A kostet 60 € · 0,85 = 51 €, B 54 €. Gefühle oder Werbung sind keine mathematischen Argumente.',
        'Rechne beide Preise aus und vergleiche.')
    N.A('argumente', 2, 'Ein Händler sagt: „Ich senke den Preis um 100 %.“ Was bedeutet das mathematisch?', 'Die Ware kostet danach 0 €.',
        ['Der Preis halbiert sich.', 'Der Preis sinkt um 100 €.', 'Der Preis bleibt gleich.'],
        'Minus 100 % heißt Faktor 1 − 1 = 0. Jeder Preis mal 0 ergibt 0 €.', 'Bestimme den Faktor für „minus 100 %“.')
    N.A('argumente', 3, 'Die Wahlbeteiligung stieg von 60 % auf 66 %. Welche Aussage stimmt?', 'Sie stieg um 6 Prozentpunkte, das sind 10 %.',
        ['Sie stieg um 6 %.', 'Sie stieg um 10 Prozentpunkte.', 'Sie stieg um 66 %.'],
        'Unterschied der Anteile: 66 − 60 = 6 Prozentpunkte. Bezogen auf 60 %: 6 : 60 = 0,1 = 10 %.',
        'Unterscheide Prozentpunkte (Differenz der Anteile) und Prozent (Änderung bezogen auf den alten Anteil).', art=P)
    N.A('argumente', 3, 'An Schule A kommen 30 % von 600 Kindern mit dem Rad, an Schule B 40 % von 400 Kindern. Jemand sagt: „An Schule B fahren mehr Kinder Rad.“ Stimmt das?',
        'Nein: An A sind es 180, an B nur 160 Kinder.', ['Ja: 40 % ist mehr als 30 %.', 'Ja: An B sind es 40 Kinder mehr.', 'Man kann es nicht wissen.'],
        'Anteile allein sagen nichts über Anzahlen. A: 600 · 0,3 = 180, B: 400 · 0,4 = 160. Der größere Anteil gehört hier zur kleineren Anzahl.',
        'Rechne die Anzahlen aus. Ein größerer Anteil heißt nicht automatisch mehr Kinder.', art=P)
    N.A('argumente', 3, 'Im Jahr 1 hatten 24 % der Befragten ein Haustier, im Jahr 2 nur 22 %. Darf man sagen, dass es im Jahr 2 weniger Haustierbesitzer gab?',
        'Nein, denn man weiß nicht, wie viele Personen jeweils befragt wurden.', ['Ja, denn 22 % ist weniger als 24 %.', 'Ja, genau 2 Personen weniger.', 'Nein, es gab sicher 2 % mehr.'],
        'Prozente sind Anteile. Wurden im Jahr 2 mehr Personen befragt, können 22 % mehr Personen sein als 24 % im Jahr 1. Ohne Gesamtzahl gibt es keine Aussage über Anzahlen.',
        'Denke an zwei verschieden große Befragungen.', art=P)
    N.A('argumente', 3, 'Laden A: „Nimm 3, zahl 2.“ Laden B: „30 % auf alles.“ Der Stückpreis ist gleich, du brauchst 3 Stück. Wo sparst du mehr?',
        'Bei A, denn dort sparst du 1/3 ≈ 33,3 %.', ['Bei B, denn 30 % ist ein fester Rabatt.', 'Gleich viel, denn beides ist etwa ein Drittel.', 'Bei B, denn bei A zahlst du für 2 Stück.'],
        'Bei A zahlst du 2 von 3 Stück: Du sparst 1/3 ≈ 33,3 % > 30 %. Bei gleichem Stückpreis ist A günstiger.',
        'Wie viel Prozent sparst du bei „3 für 2“?')
    N.A('argumente', 3, 'Ein Preis steigt um 50 %, dann sinkt er um 50 %. Das Ganze wird mehrmals wiederholt. Jemand behauptet: „Nach jedem solchen Paar ist der Preis kleiner als vorher.“ Was stimmt?',
        'Richtig, denn jedes Paar bedeutet mal 1,5 · 0,5 = 0,75.', ['Falsch, denn +50 % und −50 % heben sich auf.', 'Falsch, denn der Preis wird jedes Mal größer.', 'Richtig, aber nur beim ersten Paar.'],
        'Ein Paar: mal 1,5, dann mal 0,5, zusammen mal 0,75. Jedes Paar macht den Preis um 25 % kleiner – immer wieder.',
        'Fasse ein Paar zu einem Faktor zusammen.', art=K)
    return N


if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Faktoren', ['faktor', 'vermehrt', 'vermindert']), ('Rückwärts rechnen', ['zurueck', 'prozentsatz']), ('Komplexere Aufgaben', ['mehrfach', 'argumente'])],
         'Mit dem Wachstumsfaktor vermehrte und verminderte Grundwerte berechnen, auf den Grundwert zurückrechnen, prozentuale Änderungen bestimmen und Aussagen über Prozente mathematisch prüfen.',
         ['Plus p %: mal (1 + p/100). Minus p %: mal (1 − p/100).', 'Zurück zum Grundwert: durch den Faktor teilen.',
          'Mehrere Änderungen: Faktoren multiplizieren, nicht Prozente addieren.'],
)
    anhaengen(META['thema_schluessel'], schwer())
