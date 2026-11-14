#!/usr/bin/env python3
"""Thema stochastik.grundbegriffe – Zufall und Laplace (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, L, Z, baue, bruch, ist_endlich, mit_bild, runde, sicher_rundbar, zt  # noqa: E402

META = {'thema_schluessel': 'stochastik.grundbegriffe', 'thema_id': 61, 'block_id': 92, 'klasse': {'gym_by': 8, 'rs_by': 8}}

ETAPPEN = [
    {'lernziel': 'begriffe', 'titel': 'Ergebnis, Ergebnisraum, Ereignis',
     'regel': 'Ein ⟦Zufallsexperiment⟧ hat mehrere mögliche ⟦Ergebnisse⟧; welches eintritt, ist nicht vorhersagbar. Alle Ergebnisse zusammen bilden den ⟦Ergebnisraum Ω⟧. Ein ⟦Ereignis⟧ ist eine Teilmenge von Ω.',
     'schritte': ['Würfeln: Ω = {1; 2; 3; 4; 5; 6}', 'Ereignis E: „Augenzahl größer als 4“', '⟦E = {5; 6}⟧'],
     'fehler': 'Zweimal eine Münze werfen hat nicht 3 Ergebnisse (WW, WZ, ZZ). Stell dir eine 1-€- und eine 2-€-Münze vor: „1 € Wappen, 2 € Zahl“ ist etwas anderes als „1 € Zahl, 2 € Wappen“. Der Baum zeigt ⟦vier⟧ Wege: Ω = {WW; WZ; ZW; ZZ}.',
     'bild': {'typ': 'baum', 'aeste': [{'text': 'W', 'p': '1/2', 'aeste': [{'text': 'WW', 'p': '1/2'}, {'text': 'WZ', 'p': '1/2'}]},
                                       {'text': 'Z', 'p': '1/2', 'aeste': [{'text': 'ZW', 'p': '1/2'}, {'text': 'ZZ', 'p': '1/2'}]}]},
     '_verbot': ['Augenzahl größer als 4']},
    {'lernziel': 'rel_haeufigkeit', 'titel': 'Relative Häufigkeit',
     'regel': 'Die ⟦absolute Häufigkeit⟧ zählt, wie oft ein Ergebnis eintrat. Die ⟦relative Häufigkeit⟧ ist der Anteil: ⟦absolute Häufigkeit : Anzahl der Versuche⟧. Sie liegt zwischen 0 und 1.',
     'schritte': ['50 Würfe, 12-mal eine Sechs', 'relative Häufigkeit = 12 : 50', '= ⟦0,24 = 24 %⟧'],
     'fehler': 'Die relative Häufigkeit von 12 Sechsen bei 50 Würfen ist nicht 12. Das ist die ⟦absolute⟧ Häufigkeit. Relativ heißt: im Verhältnis zur Gesamtzahl.',
     '_verbot': ['50 Würfe, 12-mal']},
    {'lernziel': 'laplace', 'titel': 'Laplace-Wahrscheinlichkeit',
     'regel': 'Sind alle Ergebnisse ⟦gleich wahrscheinlich⟧ (Laplace-Experiment), gilt: ⟦P(E) = Anzahl der günstigen Ergebnisse : Anzahl aller Ergebnisse⟧.',
     'schritte': ['Urne: 3 rote, 5 blaue, 2 grüne Kugeln, eine wird gezogen.', 'Günstig für „rot“: 3, möglich: 10', '⟦P(rot) = 3/10 = 0,3⟧'],
     'fehler': 'P(rot) ist nicht 3/7 (rot zu nicht-rot). Im Nenner steht die Anzahl ⟦aller⟧ Kugeln: 3/10.',
     '_verbot': ['3 rote, 5 blaue, 2 grüne']},
    {'lernziel': 'laplace_pruefen', 'titel': 'Ist es ein Laplace-Experiment?',
     'regel': 'Ein Experiment ist nur dann ein ⟦Laplace-Experiment⟧, wenn ⟦alle Ergebnisse gleich wahrscheinlich⟧ sind. Ungleich große Glücksradfelder oder eine Reißzwecke sind kein Laplace-Experiment.',
     'schritte': ['Glücksrad: Feld A 180°, Feld B 90°, Feld C 90°', 'A ist doppelt so groß wie B und C.', '⟦Kein⟧ Laplace-Experiment: P(A) = 1/2, nicht 1/3.'],
     'fehler': 'Drei mögliche Ergebnisse bedeuten nicht automatisch P = 1/3 für jedes. Das gilt nur, wenn sie ⟦gleich wahrscheinlich⟧ sind.',
     'bild': {'typ': 'kreisdiagramm', 'einheit': '°', 'werte': [{'name': 'A', 'wert': 180}, {'name': 'B', 'wert': 90}, {'name': 'C', 'wert': 90}], 'zahlen': True},
     '_verbot': ['180°, Feld B 90°']},
    {'lernziel': 'gegenereignis', 'titel': 'Das Gegenereignis',
     'regel': 'Das ⟦Gegenereignis⟧ Ē tritt genau dann ein, wenn E ⟦nicht⟧ eintritt. Es gilt ⟦P(Ē) = 1 − P(E)⟧.',
     'schritte': ['E: „Sechs würfeln“, P(E) = 1/6', 'Ē: „keine Sechs“', '⟦P(Ē) = 1 − 1/6 = 5/6⟧'],
     'fehler': 'Das Gegenereignis zu „mindestens eine Sechs“ ist nicht „höchstens eine Sechs“, sondern ⟦„keine Sechs“⟧.',
     '_verbot': ['„Sechs würfeln“']},
    {'lernziel': 'grosse_zahlen', 'titel': 'Gesetz der großen Zahlen',
     'regel': 'Bei ⟦vielen⟧ Wiederholungen nähert sich die relative Häufigkeit meist der ⟦Wahrscheinlichkeit⟧ an. Bei n Versuchen erwartet man etwa ⟦n · P(E)⟧ Treffer – genau vorhersagen kann man es nie.',
     'schritte': ['Münze 1000-mal werfen, P(Wappen) = 0,5', 'Erwartet: 1000 · 0,5 = ⟦etwa 500-mal Wappen⟧', 'Tatsächlich z. B. 488 oder 513 – nicht genau 500.'],
     'fehler': 'Kam fünfmal keine Sechs, ist die Sechs beim nächsten Wurf ⟦nicht⟧ wahrscheinlicher. Der Würfel hat kein Gedächtnis: P bleibt 1/6.'},
]


def frac_opts(p, guenstig, alle):
    """Richtige Wahrscheinlichkeit als Bruch + typische Fehler."""
    f = [bruch(Fr(guenstig, max(1, alle - guenstig))) if alle - guenstig else '1/2', bruch(1 - p) if p != Fr(1, 2) else '1/3',
         bruch(Fr(alle - guenstig + 1, alle)) if Fr(alle - guenstig + 1, alle) != p else '2/3', f'{guenstig}/{alle + 1}']
    return [x for x in f if x != bruch(p)]


def g_begriffe(R, st):
    if st == 1:
        art = R.choice(['wuerfel', 'rad', 'urne', 'muenze2'])
        if art == 'wuerfel':
            n = R.choice([4, 6, 8, 10, 12, 20])
            return Z(f'Ein Spielwürfel hat {n} gleich große Flächen mit den Zahlen 1 bis {n}. Wie viele Ergebnisse hat der Ergebnisraum beim einmaligen Werfen?', n, f'{n}',
                     f'Ω = {{1; 2; …; {n}}}: {n} Ergebnisse.', 'Zähle, welche Zahlen oben liegen können.')
        if art == 'rad':
            n = R.randint(3, 12)
            return Z(f'Ein Glücksrad hat {n} Felder mit den Nummern 1 bis {n}. Wie viele Ergebnisse hat der Ergebnisraum bei einer Drehung?', n, f'{n}',
                     f'Jede Nummer ist ein Ergebnis: {n} Ergebnisse.', 'Jedes Feld ist ein mögliches Ergebnis.')
        if art == 'urne':
            farben = R.sample(['rot', 'blau', 'grün', 'gelb', 'weiß', 'schwarz'], R.randint(2, 5))
            anz = [R.randint(1, 6) for _ in farben]
            return Z(f'In einer Urne liegen {", ".join(f"{a} {f}e" for a, f in zip(anz, farben))} Kugeln. Man zieht eine Kugel und notiert die Farbe. Wie viele Ergebnisse hat der Ergebnisraum?',
                     len(farben), f'{len(farben)}', f'Ergebnis ist die Farbe: Ω = {{{"; ".join(farben)}}}, also {len(farben)} Ergebnisse (nicht {sum(anz)}).',
                     'Notiert wird nur die Farbe – wie viele verschiedene Farben gibt es?')
        k = R.choice([2, 3])
        return Z(f'Eine Münze wird {k}-mal geworfen, die Reihenfolge wird notiert. Wie viele Ergebnisse hat der Ergebnisraum?', 2 ** k, f'2 ** {k}',
                 f'Bei jedem Wurf 2 Möglichkeiten: 2{"²" if k == 2 else "³"} = {2 ** k}.', 'Schreibe alle Möglichkeiten auf: WW, WZ, …')
    if st == 2:
        n = R.choice([6, 8, 10, 12])
        ereig = R.choice([('gerade Zahl', lambda x: x % 2 == 0), ('ungerade Zahl', lambda x: x % 2 == 1), ('Primzahl', lambda x: x in (2, 3, 5, 7, 11)),
                          ('Zahl größer als 4', lambda x: x > 4), ('Teiler von 12', lambda x: 12 % x == 0), ('Vielfaches von 3', lambda x: x % 3 == 0),
                          ('Zahl kleiner als 3', lambda x: x < 3)])
        E = [x for x in range(1, n + 1) if ereig[1](x)]
        r = '{' + '; '.join(map(str, E)) + '}'
        rest = [x for x in range(1, n + 1) if x not in E]
        f = ['{' + '; '.join(map(str, rest)) + '}', '{' + '; '.join(map(str, E[:-1] or rest[:1])) + '}', '{' + '; '.join(map(str, sorted(set(E + rest[:1])))) + '}']
        if ereig[0] == 'Primzahl': f[1] = '{' + '; '.join(map(str, [1] + E)) + '}'
        return A(R, f'Ein Würfel mit den Zahlen 1 bis {n} wird geworfen. Welche Menge beschreibt das Ereignis „{ereig[0]}“?', r, f,
                 f'Alle Ergebnisse aus Ω, die passen: {r}.', 'Gehe Ω = {1; …; ' + str(n) + '} durch und prüfe jede Zahl.')
    if R.random() < .35:
        E, ri, fa = R.choice([('{1; 2; 3}', 'Augenzahl kleiner als 4', ['Augenzahl ungerade', 'Augenzahl höchstens 2', 'Augenzahl größer als 3']),
                              ('{2; 3; 5}', 'Augenzahl ist eine Primzahl', ['Augenzahl ungerade', 'Augenzahl kleiner als 5', 'Augenzahl größer als 1']),
                              ('{1; 3; 5}', 'Augenzahl ungerade', ['Augenzahl kleiner als 5', 'Augenzahl ist eine Primzahl', 'Augenzahl gerade']),
                              ('{3; 6}', 'Augenzahl ist durch 3 teilbar', ['Augenzahl größer als 2', 'Augenzahl gerade', 'Augenzahl ist eine Primzahl']),
                              ('{5; 6}', 'Augenzahl mindestens 5', ['Augenzahl größer als 5', 'Augenzahl gerade', 'Augenzahl höchstens 5']),
                              ('{1; 2; 3; 6}', 'Augenzahl ist ein Teiler von 6', ['Augenzahl kleiner als 4', 'Augenzahl gerade', 'Augenzahl ist durch 3 teilbar'])])
        return A(R, f'Beim Werfen eines Spielwürfels (1 bis 6) ist E = {E}. Wie kann man E in Worten beschreiben?', ri, fa,
                 f'{E} sind genau die Zahlen von 1 bis 6, für die gilt: {ri}. Bei den anderen Beschreibungen fehlt eine Zahl oder es ist eine zu viel.',
                 'Prüfe jede Beschreibung mit allen Zahlen von 1 bis 6.')
    if R.random() < .5:
        r = 'Ω = {WW; WZ; ZW; ZZ}'
        return A(R, f'Zwei Münzen werden nacheinander geworfen ({R.choice(["1-€ und 2-€", "zwei gleiche Münzen", "eine Münze zweimal"])}). Welcher Ergebnisraum ist richtig?', r,
                 ['Ω = {WW; WZ; ZZ}', 'Ω = {W; Z}', 'Ω = {WW; ZZ}'], 'Erst Wappen, dann Zahl (WZ) und erst Zahl, dann Wappen (ZW) sind verschiedene Ergebnisse.',
                 'Achte auf die Reihenfolge der Würfe.')
    n1, n2 = R.choice([(6, 6), (4, 6), (6, 8), (4, 4), (2, 6), (3, 4)])
    return Z(f'Ein Würfel mit {n1} Flächen und einer mit {n2} Flächen werden geworfen, notiert wird das Zahlenpaar. Wie viele Ergebnisse gibt es?', n1 * n2, f'{n1} * {n2}',
             f'Zu jeder der {n1} Zahlen des ersten Würfels gibt es {n2} Zahlen des zweiten: {n1} · {n2} = {n1 * n2}.', 'Denke an eine Tabelle: Zeilen mal Spalten.')


def sechsen(R, n):
    """Realistische Anzahl Sechsen bei n Würfen eines fairen Würfels (zwischen 0,12 · n und 0,22 · n)."""
    lo, hi = max(1, int(Fr(12, 100) * n)), max(2, int(Fr(22, 100) * n))
    return R.randint(lo, hi)


def g_rel_haeufigkeit(R, st):
    n = R.choice([20, 25, 40, 50, 80, 100, 125, 200, 250, 400, 500, 1000])
    k = sechsen(R, n)
    h = Fr(k, n)
    if st == 2 and R.random() < .35:
        if R.random() < .5:
            anz = [R.randint(7, 13) for _ in range(6)]
            n_ = sum(anz)
            while Fr(1, n_).denominator % 3 == 0 or any(c in (3, 7, 11, 13) for c in [n_ % 100]) and False: break
            z = R.randint(1, 6)
            hz = Fr(anz[z - 1], n_)
            gr = {'typ': 'tabelle', 'kopf': ['Augenzahl', '1', '2', '3', '4', '5', '6'], 'zeilen': [['Anzahl'] + [str(a) for a in anz]]}
            if not (ist_endlich(hz) and len(zt(hz)) <= 6):
                return mit_bild(Z(f'Die Tabelle zeigt {n_} Würfe. Wie groß ist die relative Häufigkeit der {z} in Prozent? (Runde auf eine Nachkommastelle.)', runde(hz * 100, 1),
                                  f'round({anz[z - 1]} / {n_} * 100, 1)', f'Gesamt: {n_} Würfe. {anz[z - 1]} : {n_} ≈ {zt(runde(hz * 100, 1))} %.', 'Addiere erst alle Anzahlen.', '%', toleranz=0.1), gr)
            return mit_bild(Z(f'Die Tabelle zeigt {n_} Würfe. Wie groß ist die relative Häufigkeit der {z}? Gib sie als Dezimalzahl an.', hz, f'{anz[z - 1]} / {n_}',
                              f'Gesamt: {" + ".join(map(str, anz))} = {n_} Würfe. {anz[z - 1]} : {n_} = {zt(hz)}.', 'Addiere erst alle Anzahlen.'), gr)
        farben = R.sample(['Blau', 'Rot', 'Grün', 'Gelb', 'Lila'], 4)
        while True:
            w = [R.randint(2, 12) for _ in farben]
            if sum(w) in (20, 25, 40, 50): break
        f0 = R.randrange(4)
        gr = {'typ': 'saeulen', 'einheit': 'Kinder', 'werte': [{'name': f, 'wert': x} for f, x in zip(farben, w)], 'zahlen': True}
        return mit_bild(Z(f'Das Säulendiagramm zeigt die Lieblingsfarben einer Gruppe. Welcher Anteil der Kinder mag {farben[f0]} am liebsten? Gib ihn in Prozent an.', Fr(w[f0] * 100, sum(w)),
                          f'{w[f0]} / {sum(w)} * 100', f'Insgesamt {" + ".join(map(str, w))} = {sum(w)} Kinder. {w[f0]} : {sum(w)} = {zt(Fr(w[f0], sum(w)))} = {zt(Fr(w[f0] * 100, sum(w)))} %.',
                          'Zähle erst alle Kinder zusammen.', '%'), gr)
    if st == 1:
        return Z(f'Bei {n} Würfen kam {k}-mal die Sechs. Berechne die relative Häufigkeit als Dezimalzahl.', h, f'{k} / {n}', f'Relative Häufigkeit = {k} : {n} = {zt(h)}.',
                 'Absolute Häufigkeit durch Anzahl der Versuche.')
    if st == 2:
        if R.random() < .5:
            k = R.randint(int(Fr(55, 100) * n), int(Fr(68, 100) * n)); h = Fr(k, n)
            return Z(f'Eine Reißzwecke wurde {n}-mal geworfen und landete {k}-mal auf dem Kopf. Gib die relative Häufigkeit in Prozent an.', h * 100, f'{k} / {n} * 100',
                     f'{k} : {n} = {zt(h)} = {zt(h * 100)} %.', 'Erst den Anteil berechnen, dann mal 100.', '%')
        p = Fr(R.choice([5, 10, 12, 15, 20, 24, 25, 30, 35, 40, 45, 60, 75]), 100)
        if not (p * n).denominator == 1: return g_rel_haeufigkeit(R, st)
        return Z(f'Bei {n} Versuchen beträgt die relative Häufigkeit eines Ergebnisses {zt(p * 100)} %. Wie oft trat es ein?', p * n, f'{n} * {zt(p).replace(",", ".")}',
                 f'{zt(p * 100)} % von {n} = {zt(p)} · {n} = {zt(p * n)}.', 'Absolute Häufigkeit = relative Häufigkeit · Anzahl der Versuche.')
    n1, n2 = R.sample([20, 25, 40, 50, 80, 100, 200], 2)
    k1, k2 = sechsen(R, n1), sechsen(R, n2)
    k = k1 + k2; n = n1 + n2
    h = Fr(k, n)
    if not sicher_rundbar(h * 100, 1): return g_rel_haeufigkeit(R, st)
    glatt = ist_endlich(h * 100) and (',' not in zt(h * 100) or len(zt(h * 100).split(',')[-1]) <= 1)
    se = lambda x: f'{x} Sechs' if x == 1 else f'{x} Sechsen'
    if glatt:
        return Z(f'Zwei Gruppen werfen einen Würfel: Gruppe A {n1}-mal mit {se(k1)}, Gruppe B {n2}-mal mit {se(k2)}. Wie groß ist die relative Häufigkeit der Sechs insgesamt in Prozent?',
                 h * 100, f'{k} / {n} * 100', f'Insgesamt {k} Sechsen bei {n} Würfen: {k} : {n} = {zt(h * 100)} %.',
                 'Addiere die Sechsen und die Würfe – nicht die Prozentsätze mitteln.', '%')
    return Z(f'Zwei Gruppen werfen einen Würfel: Gruppe A {n1}-mal mit {se(k1)}, Gruppe B {n2}-mal mit {se(k2)}. Wie groß ist die relative Häufigkeit der Sechs insgesamt in Prozent? (Runde auf eine Nachkommastelle.)',
             runde(h * 100, 1), f'round({k} / {n} * 100, 1)', f'Insgesamt {k} Sechsen bei {n} Würfen: {k} : {n} ≈ {zt(runde(h * 100, 1))} %.',
             'Addiere die Sechsen und die Würfe – nicht die Prozentsätze mitteln.', '%', toleranz=0.1)


def g_laplace(R, st):
    if st == 1:
        r, b, g = R.randint(1, 9), R.randint(1, 9), R.randint(0, 6)
        alle = r + b + g
        farbe, gn = R.choice([('rot', r), ('blau', b)] + ([('grün', g)] if g else []))
        p = Fr(gn, alle)
        txt = f'In einer Urne liegen {r} rote, {b} blaue{"" if not g else f" und {g} grüne"} Kugeln. Eine wird zufällig gezogen. Wie groß ist P({farbe})?'
        if ist_endlich(p) and len(zt(p)) <= 5 and R.random() < .5:
            return Z(txt + ' Gib sie als Dezimalzahl an.', p, f'{gn} / {alle}', f'{gn} günstige von {alle} Kugeln: P = {gn}/{alle} = {zt(p)}.', 'Günstige durch alle Kugeln.')
        return A(R, txt, bruch(p), frac_opts(p, gn, alle) + ([bruch(Fr(gn, alle - gn))] if alle != gn else []), f'{gn} günstige von {alle} Kugeln: P({farbe}) = {gn}/{alle}' + ('' if bruch(p) == f'{gn}/{alle}' else f' = {bruch(p)}') + '.',
                 'Im Nenner stehen alle Kugeln.')
    if st == 2:
        art = R.choice(['wuerfel', 'karten', 'rad'])
        if art == 'wuerfel':
            n = R.choice([6, 8, 10, 12, 20])
            name, f = R.choice([('eine gerade Zahl', lambda x: x % 2 == 0), ('eine Zahl größer als 3', lambda x: x > 3), ('eine Primzahl', lambda x: x in (2, 3, 5, 7, 11, 13, 17, 19)),
                                ('ein Vielfaches von 3', lambda x: x % 3 == 0), ('eine Zahl kleiner als 5', lambda x: x < 5)])
            guenstig = [x for x in range(1, n + 1) if f(x)]
            gn = len(guenstig); p = Fr(gn, n)
            auf = f'{", ".join(map(str, guenstig))} – das sind {gn} von {n} Ergebnissen' if gn <= 10 else f'{gn} von {n} Ergebnissen'
            txt = f'Ein fairer Würfel mit den Zahlen 1 bis {n} wird geworfen. Wie groß ist die Wahrscheinlichkeit für {name}?'
        elif art == 'karten':
            name, gn = R.choice([('eine Herz-Karte', 8), ('ein Ass', 4), ('eine rote Karte', 16), ('ein Bube oder eine Dame', 8), ('die Kreuz-Dame', 1), ('eine Bildkarte (Bube, Dame, König)', 12)])
            n = 32; p = Fr(gn, n)
            txt = f'Aus einem Skatblatt (32 Karten: 4 Farben, je 7, 8, 9, 10, Bube, Dame, König, Ass) wird eine Karte gezogen. Wie groß ist die Wahrscheinlichkeit für {name}?'
        else:
            n = R.choice([5, 8, 10, 12, 16, 20]); gn = R.randint(1, n - 1); p = Fr(gn, n)
            txt = f'Ein Glücksrad hat {n} gleich große Felder, {gn} davon sind rot. Wie groß ist die Wahrscheinlichkeit für „rot“?'
        if art != 'wuerfel': auf = f'{gn} günstige von {n} gleich wahrscheinlichen Ergebnissen'
        gekuerzt = '' if (p.numerator, p.denominator) == (gn, n) else f' = {bruch(p)}'
        if ist_endlich(p) and len(zt(p)) <= 6 and R.random() < .5:
            return Z(txt + ' Gib sie als Dezimalzahl an.', p, f'{gn} / {n}', f'{auf}: P = {gn}/{n} = {zt(p)}.', 'Zähle die günstigen Ergebnisse.')
        if R.random() < .5:
            return L(txt + ' Gib sie als vollständig gekürzten Bruch an.', '□/□', [p.numerator, p.denominator], [str(p.numerator), str(p.denominator)],
                     f'{auf}: P = {gn}/{n}{gekuerzt}.', 'Zähle die günstigen Ergebnisse. Kürze am Ende.', hinweis='Zähler oben, Nenner unten.')
        return A(R, txt, bruch(p), frac_opts(p, gn, n), f'{auf}: P = {gn}/{n}{gekuerzt}.', 'Zähle die günstigen Ergebnisse.')
    # Stufe 3: zwei Würfel / Urne ergänzen
    if R.random() < .5:
        s = R.randint(3, 11)
        gn = sum(1 for a in range(1, 7) for b in range(1, 7) if a + b == s); p = Fr(gn, 36)
        return A(R, f'Zwei faire Würfel werden geworfen. Wie groß ist die Wahrscheinlichkeit, dass die Augensumme {s} ist?', bruch(p),
                 [x for x in ['1/11', bruch(Fr(gn, 21)) if Fr(gn, 21) != p else '1/21', bruch(Fr(1, 6)) if p != Fr(1, 6) else '1/12', bruch(Fr(gn, 12))] if x != bruch(p)],
                 f'36 gleich wahrscheinliche Paare. Summe {s}: {gn} Paare. P = {gn}/36 = {bruch(p)}.', 'Schreibe alle 36 Paare als Tabelle. Die 11 möglichen Summen sind nicht gleich wahrscheinlich!')
    r, b = R.randint(2, 9), R.randint(1, 9)
    p = Fr(R.choice([1, 2, 3, 4]), R.choice([5, 10]))
    # Wie viele blaue Kugeln muss man dazulegen, damit P(rot) = p?  r/(r+b+x) = p -> x = r/p - r - b
    x = r / p - r - b
    if x.denominator != 1 or x <= 0: return g_laplace(R, st)
    return Z(f'In einer Urne liegen {r} rote und {b} blaue Kugeln. Wie viele blaue Kugeln muss man dazulegen, damit P(rot) = {zt(p)} ist?', x, f'{r} / {zt(p).replace(",", ".")} - {r} - {b}',
             f'{r} : (Gesamtzahl) = {zt(p)} → Gesamtzahl = {r} : {zt(p)} = {zt(r / p)}. Dazulegen: {zt(r / p)} − {r + b} = {zt(x)}.', 'Wie viele Kugeln muss es insgesamt geben?')


def g_gegenereignis(R, st):
    if st == 1:
        p = Fr(R.randint(60, 98), 100)
        return Z(f'Die Wahrscheinlichkeit, dass ein Bus pünktlich ist, beträgt {zt(p * 100)} %. Wie groß ist die Wahrscheinlichkeit, dass er nicht pünktlich ist (in %)?', 100 - p * 100,
                 f'100 - {zt(p * 100).replace(",", ".")}', f'P(Ē) = 100 % − {zt(p * 100)} % = {zt(100 - p * 100)} %.', 'P(Ē) = 1 − P(E), also 100 % − P(E).', '%')
    if st == 2 and R.random() < .5:
        pos, neg, lo, hi = R.choice([('ein Zug pünktlich ist', 'er nicht pünktlich ist', 75, 95), ('ein Elfmeter verwandelt wird', 'er nicht verwandelt wird', 70, 85),
                                     ('ein Samenkorn keimt', 'es nicht keimt', 80, 95), ('ein Los gewinnt', 'es nicht gewinnt', 3, 20)])
        pz = R.randint(lo, hi)
        return Z(f'Die Wahrscheinlichkeit, dass {pos}, beträgt {pz} %. Wie groß ist die Wahrscheinlichkeit, dass {neg} (in %)?', 100 - pz, f'100 - {pz}',
                 f'Gegenereignis: P(Ē) = 100 % − {pz} % = {100 - pz} %.', 'P(Ē) = 1 − P(E), also 100 % − P(E).', '%')
    if st == 2:
        paare = [('Zwei Würfe mit einem Spielwürfel', 'mindestens eine Sechs', 'keine Sechs', ['genau eine Sechs', 'höchstens eine Sechs', 'zwei Sechsen']),
                 ('Fünf Würfe auf eine Torwand', 'höchstens zwei Treffer', 'mindestens drei Treffer', ['mindestens zwei Treffer', 'weniger als zwei Treffer', 'genau drei Treffer']),
                 ('Drei Kugeln werden aus einer Urne gezogen', 'alle Kugeln sind rot', 'mindestens eine Kugel ist nicht rot', ['keine Kugel ist rot', 'genau eine Kugel ist nicht rot', 'alle Kugeln sind blau']),
                 ('Ein Spielwürfel wird geworfen', 'die Augenzahl ist gerade', 'die Augenzahl ist ungerade', ['die Augenzahl ist größer als 3', 'die Augenzahl ist 1', 'die Augenzahl ist 6']),
                 ('Zehn Würfe auf einen Korb', 'mehr als 4 Treffer', 'höchstens 4 Treffer', ['weniger als 4 Treffer', 'mindestens 4 Treffer', 'genau 5 Treffer']),
                 ('Zwei Würfe mit einem Spielwürfel', 'genau eine Sechs', 'keine oder zwei Sechsen', ['keine Sechs', 'zwei Sechsen', 'mindestens eine Sechs']),
                 ('Drei Münzwürfe', 'mindestens zwei Wappen', 'höchstens ein Wappen', ['höchstens zwei Wappen', 'genau ein Wappen', 'kein Wappen']),
                 ('Ein Spielwürfel wird geworfen', 'die Augenzahl ist größer als 2', 'die Augenzahl ist 1 oder 2', ['die Augenzahl ist kleiner als 2', 'die Augenzahl ist 3, 4, 5 oder 6', 'die Augenzahl ist höchstens 3'])]
        exp, e, g, falsch = R.choice(paare)
        return A(R, f'{exp}. Wie heißt das Gegenereignis zu „{e}“?', g, falsch, f'Das Gegenereignis umfasst genau die Fälle, in denen „{e}“ nicht eintritt: {g}.',
                 'Welche Fälle bleiben übrig, wenn E nicht eintritt? Zähle alle Möglichkeiten auf.')
    if R.random() < .4:
        if R.random() < .5:
            p1, p2 = Fr(R.choice([10, 15, 20, 25, 30]), 100), Fr(R.choice([15, 25, 35, 40]), 100)
            return Z(f'Bei einem Glücksrad ist P(rot) = {zt(p1)} und P(blau) = {zt(p2)}. Wie groß ist P(weder rot noch blau)?', 1 - p1 - p2, f'1 - {zt(p1).replace(",", ".")} - {zt(p2).replace(",", ".")}',
                     f'„Weder rot noch blau“ ist das Gegenereignis zu „rot oder blau“: 1 − ({zt(p1)} + {zt(p2)}) = {zt(1 - p1 - p2)}.', 'Was ist das Gegenereignis? Rechne 1 minus dessen Wahrscheinlichkeit.')
        k = R.choice([2, 3])
        p = 1 - Fr(5, 6) ** k
        return A(R, f'Ein Spielwürfel wird {k}-mal geworfen. Wie groß ist P(mindestens eine Sechs)?', bruch(p),
                 [bruch(Fr(5, 6) ** k), bruch(Fr(k, 6)), bruch(Fr(1, 6) ** k)],
                 f'Gegenereignis: keine Sechs. P(keine Sechs) = (5/6){"²" if k == 2 else "³"} = {bruch(Fr(5, 6) ** k)}. Also P = 1 − {bruch(Fr(5, 6) ** k)} = {bruch(p)}.',
                 '„Mindestens eine“ ist schwer zu zählen. Das Gegenereignis „keine“ ist leicht.')
    n = R.choice([6, 8, 10, 12, 20])
    k = R.randint(1, n - 1)
    p = 1 - Fr(k, n)
    if ist_endlich(p) and len(zt(p)) <= 5:
        return Z(f'Ein fairer Würfel hat die Zahlen 1 bis {n}. Wie groß ist die Wahrscheinlichkeit, KEINE Zahl kleiner oder gleich {k} zu werfen? Gib sie als Dezimalzahl an.', p,
                 f'1 - {k} / {n}', f'P(Zahl ≤ {k}) = {k}/{n}. Gegenereignis: 1 − {k}/{n} = {zt(p)}.', 'Berechne erst P(E) und nimm dann 1 − P(E).')
    return A(R, f'Ein fairer Würfel hat die Zahlen 1 bis {n}. Wie groß ist die Wahrscheinlichkeit, KEINE Zahl kleiner oder gleich {k} zu werfen?', bruch(p),
             [bruch(Fr(k, n)), bruch(Fr(n - k, n + 1)), bruch(Fr(n - k + 1, n)) if Fr(n - k + 1, n) != p else '1/2'],
             f'P(Zahl ≤ {k}) = {k}/{n}. Gegenereignis: 1 − {k}/{n} = {bruch(p)}.', 'Berechne erst P(E) und nimm dann 1 − P(E).')


def g_grosse_zahlen(R, st):
    if st >= 2 and R.random() < .3:
        ding, n, lo, hi = R.choice([('Eine Reißzwecke landete', 1000, 560, 660), ('Ein Legostein lag', 400, 70, 110), ('Ein Kronkorken landete', 500, 220, 300)])
        k = R.randint(lo, hi)
        lage = {'Eine Reißzwecke landete': 'auf dem Kopf', 'Ein Legostein lag': 'auf der Seite', 'Ein Kronkorken landete': 'mit der Öffnung nach oben'}[ding]
        return Z(f'{ding} bei {n} Würfen {k}-mal {lage}. Schätze die Wahrscheinlichkeit dafür auf zwei Nachkommastellen.', runde(Fr(k, n), 2), f'round({k} / {n}, 2)',
                 f'Bei vielen Würfen ist die relative Häufigkeit eine gute Schätzung: {k} : {n} = {zt(Fr(k, n))} ≈ {zt(runde(Fr(k, n), 2))}.',
                 'Relative Häufigkeit bei vielen Versuchen = Schätzwert für die Wahrscheinlichkeit.', toleranz=0.01)
    if st in (1, 2):
        art = R.choice(['muenze', 'wuerfel', 'rad'])
        if art == 'muenze':
            n = R.choice([100, 200, 500, 1000, 2000]); p = Fr(1, 2); was = 'Wappen beim Münzwurf'
        elif art == 'wuerfel':
            n = R.choice([60, 120, 300, 600, 1200, 3000]); p = Fr(1, 6); was = 'eine Sechs beim Würfeln'
        else:
            k = R.choice([4, 5, 8, 10]); g = R.randint(1, k - 1); n = R.choice([40, 80, 100, 200, 400]); p = Fr(g, k)
            was = f'„rot“ beim Glücksrad mit {k} gleichen Feldern, davon {g} rot'
            if (n * p).denominator != 1: return g_grosse_zahlen(R, st)
        return Z(f'Wie oft erwartest du bei {n} Versuchen ungefähr {was}?', n * p, f'{n} * {p.numerator} / {p.denominator}',
                 f'Erwartet: n · P = {n} · {bruch(p)} = {zt(n * p)}. Das tatsächliche Ergebnis schwankt um diesen Wert.', 'Anzahl der Versuche mal Wahrscheinlichkeit.')
    al = [('Bei 6000 Würfen eines fairen Würfels kommt die Sechs ungefähr 1000-mal.', True),
          ('Bei 6 Würfen eines fairen Würfels kommt die Sechs genau einmal.', False),
          ('Nach fünf Würfen ohne Sechs ist eine Sechs beim nächsten Wurf wahrscheinlicher.', False),
          ('Je öfter man eine Münze wirft, desto näher liegt meist der Anteil der Wappen bei 0,5.', True),
          ('Bei 10 Münzwürfen gibt es immer genau 5-mal Wappen.', False),
          ('Die relative Häufigkeit kann bei wenigen Versuchen stark von der Wahrscheinlichkeit abweichen.', True),
          ('Mit vielen Versuchen kann man eine unbekannte Wahrscheinlichkeit gut schätzen.', True),
          ('Wenn beim Roulette fünfmal Rot kam, muss jetzt Schwarz kommen.', False),
          ('Die absolute Anzahl der Wappen liegt bei vielen Würfen immer genau bei der Hälfte.', False)]
    wahr = [t for t, w in al if w]; falsch = [t for t, w in al if not w]
    if R.random() < .5:
        t = R.choice(wahr)
        return A(R, 'Welche Aussage zum Gesetz der großen Zahlen ist richtig?', t, R.sample(falsch, 3), f'Richtig: {t} Zufall hat kein Gedächtnis; erst bei vielen Versuchen stabilisiert sich die relative Häufigkeit.',
                 'Achte auf Wörter wie „genau“, „immer“ und „muss“.')
    t = R.choice(falsch)
    return A(R, 'Welche Aussage ist FALSCH?', t, R.sample(wahr, 3), f'Falsch: {t} Die relative Häufigkeit nähert sich nur ungefähr an, genaue Vorhersagen sind unmöglich.',
             'Achte auf Wörter wie „genau“, „immer“ und „muss“.')


def g_laplace_pruefen(R, st):
    if st == 3 or (st == 2 and R.random() < .5):
        k = R.randint(3, 6)
        gleich = R.random() < .4
        if gleich: w = [360 // k] * k if 360 % k == 0 else None
        else:
            while True:
                w = sorted([R.choice([30, 45, 60, 90, 120, 150, 180]) for _ in range(k - 1)])
                rest = 360 - sum(w)
                if rest > 0 and rest % 15 == 0 and len(set(w + [rest])) > 1: w = w + [rest]; break
        if w is None: return g_laplace_pruefen(R, st)
        felder = ', '.join(f'{chr(65 + i)} {x}°' for i, x in enumerate(w))
        rad = {'typ': 'kreisdiagramm', 'einheit': '°', 'werte': [{'name': chr(65 + i), 'wert': x} for i, x in enumerate(w)], 'zahlen': True}
        if st == 3 and not gleich:
            i = R.randrange(len(w))
            p = Fr(w[i], 360)
            if ist_endlich(p) and len(zt(p)) <= 6:
                return mit_bild(Z(f'Glücksrad mit den Feldern {felder} (siehe Bild). Wie groß ist die Wahrscheinlichkeit für Feld {chr(65 + i)}? Gib sie als Dezimalzahl an.', p, f'{w[i]} / 360',
                                  f'Kein Laplace-Experiment, aber P ist der Anteil am Vollwinkel: {w[i]}° : 360° = {zt(p)}.', 'Die Wahrscheinlichkeit ist der Anteil des Feldes am ganzen Kreis (360°).'), rad)
        r = 'Ja, alle Felder sind gleich groß.' if gleich else 'Nein, die Felder sind verschieden groß.'
        return mit_bild(A(R, f'Ein Glücksrad hat die Felder {felder}. Ist eine Drehung (Ergebnis: Feldname) ein Laplace-Experiment?', r,
                 ['Nein, die Felder sind verschieden groß.', 'Nein, ein Glücksrad ist nie ein Laplace-Experiment.', 'Nein, dafür braucht man genau 6 Felder.' if k != 6 else 'Nein, dafür braucht man eine gerade Anzahl Felder.'] if gleich else
                 ['Ja, alle Felder sind gleich groß.', 'Ja, jedes Glücksrad ist ein Laplace-Experiment.', f'Ja, weil es {k} Felder gibt.'], 'Gleich große Felder → gleich wahrscheinlich.' if gleich else 'Größere Felder werden häufiger getroffen.',
                 'Vergleiche die Winkel der Felder.'), rad)
    bank = [('Werfen eines fairen Spielwürfels', True), ('Werfen einer Reißzwecke (Kopf oder Seite)', False), ('Werfen einer fairen Münze', True),
            ('Ziehen einer Kugel aus 3 roten und 5 blauen Kugeln, notiert wird die Farbe', False),
            ('Ziehen einer von 8 gleichen, durchnummerierten Kugeln, notiert wird die Nummer', True),
            ('Werfen eines Quaders mit verschieden großen Seitenflächen', False), ('Ziehen einer Karte aus einem gut gemischten Skatblatt', True),
            ('Würfeln mit zwei Würfeln, notiert wird die Augensumme', False), ('Würfeln mit zwei Würfeln, notiert wird das Zahlenpaar', True),
            ('Werfen eines Kronkorkens', False), ('Ein Glücksrad mit 10 gleich großen Feldern', True), ('Werfen eines Legosteins', False)]
    t, w = R.choice(bank)
    r = 'Ja' if w else 'Nein'
    return A(R, f'Ist das ein Laplace-Experiment? {t}.', f'{r}, ' + ('alle Ergebnisse sind gleich wahrscheinlich.' if w else 'die Ergebnisse sind nicht gleich wahrscheinlich.'),
             ['Ja, alle Ergebnisse sind gleich wahrscheinlich.' if not w else 'Nein, die Ergebnisse sind nicht gleich wahrscheinlich.',
              'Nein, bei Zufallsexperimenten weiß man das nie.', 'Ja, weil es zwei oder mehr Ergebnisse gibt.'],
             'Alle Ergebnisse sind gleich wahrscheinlich.' if w else 'Die Ergebnisse haben verschiedene Wahrscheinlichkeiten (z. B. wegen Form, Anzahl oder Summenbildung).',
             'Sind wirklich alle Ergebnisse gleich wahrscheinlich?')


GEN = {'begriffe': g_begriffe, 'rel_haeufigkeit': g_rel_haeufigkeit, 'laplace': g_laplace, 'gegenereignis': g_gegenereignis,
       'grosse_zahlen': g_grosse_zahlen, 'laplace_pruefen': g_laplace_pruefen}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Grundbegriffe', ['begriffe', 'rel_haeufigkeit']), ('Wahrscheinlichkeiten', ['laplace', 'laplace_pruefen', 'gegenereignis']), ('Zufall auf Dauer', ['grosse_zahlen'])],
         'Zufallsexperimente beschreiben, relative Häufigkeiten bestimmen und Laplace-Wahrscheinlichkeiten berechnen; das Gesetz der großen Zahlen verstehen.',
         ['Ω = alle Ergebnisse, Ereignis = Teilmenge von Ω.', 'Relative Häufigkeit = absolute Häufigkeit : Anzahl der Versuche.',
          'Laplace: P(E) = günstige : alle (nur bei gleich wahrscheinlichen Ergebnissen).', 'P(Ē) = 1 − P(E).'],
         offen=['Urnen werden nur in Worten beschrieben (kein passender Bildtyp); Glücksräder als Kreisdiagramm, Häufigkeiten als Tabelle oder Säulendiagramm.'])
