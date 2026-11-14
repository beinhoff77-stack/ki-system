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

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Faktoren', ['faktor', 'vermehrt', 'vermindert']), ('Rückwärts rechnen', ['zurueck', 'prozentsatz']), ('Komplexere Aufgaben', ['mehrfach', 'argumente'])],
         'Mit dem Wachstumsfaktor vermehrte und verminderte Grundwerte berechnen, auf den Grundwert zurückrechnen, prozentuale Änderungen bestimmen und Aussagen über Prozente mathematisch prüfen.',
         ['Plus p %: mal (1 + p/100). Minus p %: mal (1 − p/100).', 'Zurück zum Grundwert: durch den Faktor teilen.',
          'Mehrere Änderungen: Faktoren multiplizieren, nicht Prozente addieren.'],
)
