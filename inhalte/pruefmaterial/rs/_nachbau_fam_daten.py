"""Aufgabenfamilien: Daten (Mittelwert, Häufigkeiten, Diagramme, Stichproben) und Stochastik (Laplace, Kombinatorik)."""
from fractions import Fraction as Fr
import itertools
import math

from _nachbau_kern import Kern, check, wissen, z, NAMEN


def tabelle(kopf, zeilen):
    s = '| ' + ' | '.join(kopf) + ' |\n|' + '---|' * len(kopf) + '\n'
    for zl in zeilen:
        s += '| ' + ' | '.join(str(x) for x in zl) + ' |\n'
    return s


def f_daten(rng, niv, info, et):
    if et in ('mittelwert', 'mittel_rueckwaerts', 'kennwerte', 'median'):
        n = rng.randint(5, 8)
        for _ in range(500):
            werte = [rng.randint(2, 40) for _ in range(n)]
            if sum(werte) % n == 0:
                break
        mw = Fr(sum(werte), n)
        kont = rng.choice(['Punkte bei einem Quiz', 'Minuten für den Schulweg', 'Anzahl gelesener Seiten an einem Tag', 'Anzahl der Liegestütze in einer Minute'])
        if et == 'mittel_rueckwaerts':
            fehlt = werte[-1]
            bek = werte[:-1]
            return Kern(f'Für {n} Kinder wird notiert: {kont}. Bekannt sind {"; ".join(map(str, bek))}, ein Wert fehlt. Der Mittelwert aller {n} Werte ist {z(mw)}.', 'Bestimme den fehlenden Wert.', str(fehlt),
                        [f'Summe aller Werte: {n} · {z(mw)} = {z(mw * n)}', f'Summe der bekannten: {sum(bek)}', f'fehlender Wert: {z(mw * n)} − {sum(bek)} = {fehlt}'],
                        [(z(mw), 'Mittelwert als fehlenden Wert angenommen'), (str(z(mw * (n - 1)) and int(mw * (n - 1)) - sum(bek)), 'mit n − 1 statt n gerechnet')], [check('Mittelwert', Fr(sum(bek) + fehlt, n) == mw)])
        s = sorted(werte)
        med = Fr(s[n // 2]) if n % 2 else Fr(s[n // 2 - 1] + s[n // 2], 2)
        if et in ('median', 'kennwerte'):
            return Kern(f'Erhoben wurde: {kont}. Werte: {"; ".join(map(str, werte))}.', 'Bestimme Minimum, Maximum, Spannweite und Median (Zentralwert).',
                        f'Min {s[0]}, Max {s[-1]}, Spannweite {s[-1] - s[0]}, Median {z(med)}', ['Werte ordnen: ' + '; '.join(map(str, s)), f'Median = mittlerer Wert bzw. Mittel der beiden mittleren = {z(med)}'],
                        [(f'Median {z(Fr(werte[n // 2]))}', 'ohne Ordnen den mittleren Wert genommen'), (f'Median {z(mw)}', 'Mittelwert statt Median')], [check('Median', med == (Fr(s[n // 2]) if n % 2 else Fr(s[n // 2 - 1] + s[n // 2], 2)))])
        return Kern(f'Erhoben wurde: {kont}. Werte: {"; ".join(map(str, werte))}.', 'Berechne den Mittelwert.', z(mw), [f'Summe: {sum(werte)}', f'{sum(werte)} : {n} = {z(mw)}'],
                    [(z(Fr(sum(werte), n - 1)), 'durch n − 1 geteilt'), (z(med), 'Median statt Mittelwert')], [check('Mittelwert', mw * n == sum(werte))])
    if et == 'mittel_tabelle':
        werte = sorted(rng.sample(range(1, 7), 4))
        haeuf = [rng.randint(1, 9) for _ in werte]
        n = sum(haeuf)
        mw = Fr(sum(w * h for w, h in zip(werte, haeuf)), n)
        tab = tabelle(['Note', *map(str, werte)], [['Anzahl', *map(str, haeuf)]])
        return Kern(f'Notenverteilung einer Probearbeit:\n\n{tab}', 'Berechne den Notendurchschnitt (auf zwei Dezimalen).', z(Fr(round(mw * 100), 100), 2),
                    [f'Summe der Noten: {sum(w * h for w, h in zip(werte, haeuf))}', f'Anzahl: {n}', f'Durchschnitt ≈ {z(Fr(round(mw * 100), 100), 2)}'],
                    [(z(Fr(sum(werte), len(werte)), 2), 'Häufigkeiten nicht berücksichtigt')], [check('gewichtetes Mittel', mw * n == sum(w * h for w, h in zip(werte, haeuf)))])
    if et in ('relative_haeufigkeit', 'absolute_haeufigkeit'):
        n = rng.choice([20, 25, 40, 50, 80, 200])
        k = rng.randint(1, n - 1)
        r = Fr(k, n)
        return Kern(f'Bei einer Umfrage unter {n} Jugendlichen gaben {k} an, ein Instrument zu spielen.', 'Gib die relative Häufigkeit als Bruch, Dezimalzahl und in Prozent an.',
                    f'{r.numerator}/{r.denominator} = {z(r, True)} = {z(r * 100)} %', [f'relative Häufigkeit = absolute Häufigkeit : Gesamtzahl = {k} : {n}'],
                    [(f'{n}/{k} = {z(Fr(n, k), True)}', 'Gesamtzahl durch Anzahl geteilt'), (f'{r.numerator}/{r.denominator} = {z(r * 10, True)} = {z(r * 10)} %', 'Komma falsch gesetzt'),
                     (f'{k}/{n - k} = {z(Fr(k, n - k), True)}', 'durch die Anzahl der anderen geteilt')], [check('Anteil', r * n == k)])
    if et in ('tabelle_auswerten',):
        m1, m2, w1, w2 = (rng.randint(3, 15) for _ in range(4))
        tab = tabelle(['', 'Ausflug Zoo', 'Ausflug Museum', 'gesamt'], [['Mädchen', m1, '___', m1 + m2], ['Jungen', '___', w2, w1 + w2], ['gesamt', m1 + w1, m2 + w2, m1 + m2 + w1 + w2]])
        return Kern(f'Eine Klasse stimmt über das Ausflugsziel ab.\n\n{tab}', 'Ergänze die fehlenden Einträge und gib an, wie viel Prozent der Klasse (auf ganze Prozent) für den Zoo gestimmt haben.',
                    f'Mädchen Museum: {m2}; Jungen Zoo: {w1}; Zoo: {round(100 * (m1 + w1) / (m1 + m2 + w1 + w2))} %', [f'{m1 + m2} − {m1} = {m2}', f'{m1 + w1} − {m1} = {w1}', f'{m1 + w1} : {m1 + m2 + w1 + w2} ≈ {round(100 * (m1 + w1) / (m1 + m2 + w1 + w2))} %'],
                    [(f'Zoo: {round(100 * m1 / (m1 + m2 + w1 + w2))} %', 'nur Mädchen gezählt')], [check('Summen', m1 + m2 + w1 + w2 == (m1 + w1) + (m2 + w2))])
    if et in ('saeulendiagramm', 'irrefuehrend'):
        tage = ['Mo', 'Di', 'Mi', 'Do', 'Fr']
        w = [rng.randint(40, 60) for _ in tage]
        if et == 'irrefuehrend':
            return Kern(f'Ein Säulendiagramm zeigt die Besucherzahlen eines Bads: ' + ', '.join(f'{t} {x}' for t, x in zip(tage, w)) + '. Die Hochachse beginnt bei 38.',
                        'Warum wirkt das Diagramm irreführend? Begründe.', 'Weil die Hochachse nicht bei 0 beginnt, wirken kleine Unterschiede sehr groß.',
                        [f'Größter Wert {max(w)}, kleinster {min(w)}: Unterschied nur {max(w) - min(w)}, also etwa {round(100 * (max(w) - min(w)) / min(w))} %.'],
                        [('Weil die Säulen unterschiedlich breit sind.', 'Breite war gleich')], [wissen('Daten')])
        mx = tage[w.index(max(w))]
        return Kern(f'Ein Säulendiagramm (Beschreibung) zeigt die Anzahl ausgeliehener Bücher: ' + ', '.join(f'{t} {x}' for t, x in zip(tage, w)) + '.',
                    'An welchem Tag wurden die meisten Bücher ausgeliehen? Wie viele waren es insgesamt in der Woche?', f'{mx}; insgesamt {sum(w)}', [f'Maximum {max(w)} am {mx}', f'Summe: {sum(w)}'],
                    [(f'{tage[w.index(min(w))]}', 'Minimum statt Maximum')], [wissen('Summe')])
    if et == 'kreisdiagramm':
        anteile = rng.choice([[Fr(1, 2), Fr(1, 4), Fr(1, 8), Fr(1, 8)], [Fr(2, 5), Fr(3, 10), Fr(1, 5), Fr(1, 10)], [Fr(1, 3), Fr(1, 3), Fr(1, 6), Fr(1, 6)], [Fr(3, 8), Fr(1, 4), Fr(1, 4), Fr(1, 8)]])
        namen = rng.sample(['Fußball', 'Schwimmen', 'Tanzen', 'Klettern', 'Radfahren', 'Turnen'], 4)
        winkel = [a * 360 for a in anteile]
        return Kern('Die Lieblingssportarten einer Klasse verteilen sich so: ' + ', '.join(f'{n} {z(a * 100)} %' for n, a in zip(namen, anteile)) + '.',
                    'Berechne die Mittelpunktswinkel für ein Kreisdiagramm und zeichne es.', '; '.join(f'{n} {z(w)}°' for n, w in zip(namen, winkel)),
                    ['Mittelpunktswinkel = Anteil · 360°'] + [f'{n}: {z(a * 100)} % · 360° = {z(w)}°' for n, a, w in zip(namen[:2], anteile, winkel)],
                    [('; '.join(f'{n} {z(a * 100)}°' for n, a in zip(namen, anteile)), 'Prozentzahl als Winkel genommen')], [check('Summe 360°', sum(winkel) == 360)])
    if et in ('repraesentativ', 'aussagen', 'hochrechnen', 'begriffe', 'fehlerquellen'):
        if et == 'hochrechnen':
            n, k, N = rng.choice([50, 80, 100, 120]), None, rng.choice([600, 800, 1200, 1500])
            k = rng.randint(5, n - 5)
            hoch = Fr(k, n) * N
            return Kern(f'Von {n} zufällig befragten Schülerinnen und Schülern einer Schule mit {N} Kindern fahren {k} mit dem Rad.', 'Schätze, wie viele Kinder der ganzen Schule mit dem Rad fahren.',
                        f'etwa {z(hoch, 0) if hoch.denominator != 1 else z(hoch)}', [f'Anteil {k}/{n} = {z(Fr(k, n), True)}', f'· {N} ≈ {z(hoch, 0)}'], [(f'{k}', 'Stichprobe nicht hochgerechnet')],
                        [check('Hochrechnung', hoch * n == k * N)])
        bsp = [('Um herauszufinden, wie lange Realschülerinnen und Realschüler in Bayern für den Schulweg brauchen, befragt man nur eine Klasse einer Stadtschule.', False,
                'die Stichprobe ist zu klein und nicht zufällig; Kinder vom Land fehlen.'),
               ('Um die Lieblingsfarbe der Kinder einer Schule zu ermitteln, lost man aus jeder Klasse fünf Kinder aus.', True, 'die Auswahl ist zufällig und deckt alle Klassen ab.')]
        b, w, g = rng.choice(bsp)
        return Kern('', 'Beurteile, ob die Stichprobe repräsentativ ist. Begründe.', ('repräsentativ' if w else 'nicht repräsentativ') + ', weil ' + g, [g],
                    [('nicht repräsentativ' if w else 'repräsentativ', 'Auswahlverfahren nicht bedacht')], [wissen('Begründung')], aussage=(b + ' Ist die Stichprobe repräsentativ? Begründe.', w, g),
                    antwort_kurz='repräsentativ' if w else 'nicht repräsentativ')
    return f_daten(rng, niv, info, 'mittelwert')


def f_stoch(rng, niv, info, et):
    if et in ('laplace', 'laplace_pruefen', 'begriffe', 'gegenereignis'):
        art = rng.choice(['urne', 'wuerfel', 'rad'])
        if art == 'urne':
            r, b, g = rng.randint(1, 8), rng.randint(1, 8), rng.randint(1, 8)
            n = r + b + g
            if niv != 'I' and rng.random() < .5:
                p = Fr(r, n) * Fr(r - 1, n - 1) if r > 1 else Fr(b, n) * Fr(r, n - 1)
                was = 'zweimal rot' if r > 1 else 'zuerst blau, dann rot'
                wege = [f'1. Zug: {r if r > 1 else b}/{n}', f'2. Zug (ohne Zurücklegen): {r - 1 if r > 1 else r}/{n - 1}', f'P = {z(p, False)}']
                return Kern(f'In einer Box liegen {r} rote, {b} blaue und {g} grüne Kugeln. Es wird zweimal ohne Zurücklegen gezogen.', f'Berechne die Wahrscheinlichkeit für „{was}“.', z(p, False),
                            wege, [(z(Fr(r if r > 1 else b, n) * Fr(r, n), False), 'mit Zurücklegen gerechnet')], [check('Abzählen', p == _abz(r, b, g, was))])
            p = Fr(b, n)
            return Kern(f'In einer Box liegen {r} rote, {b} blaue und {g} grüne Kugeln. Eine Kugel wird zufällig gezogen.', 'Berechne P(blau) und P(nicht blau).', f'P(blau) = {z(p, False)}; P(nicht blau) = {z(1 - p, False)}',
                        ['Laplace: günstige : mögliche Ergebnisse', f'{b} : {n}', 'Gegenereignis: 1 − P'], [(z(Fr(b, r + g), False), 'günstige durch ungünstige geteilt')], [check('Summe 1', p + (1 - p) == 1)])
        if art == 'wuerfel':
            mengen = {'eine Primzahl': [2, 3, 5], 'eine Zahl größer als 4': [5, 6], 'eine gerade Zahl': [2, 4, 6], 'ein Teiler von 6': [1, 2, 3, 6]}
            e, m = rng.choice(list(mengen.items()))
            p = Fr(len(m), 6)
            return Kern('Ein fairer Spielwürfel wird einmal geworfen.', f'Wie groß ist die Wahrscheinlichkeit, {e} zu werfen?', z(p, False), [f'Günstige Ergebnisse: {", ".join(map(str, m))}', f'P = {len(m)}/6 = {z(p, False)}'],
                        [(z(Fr(len(m), 5), False), 'mit 5 möglichen Ergebnissen gerechnet')], [check('Abzählen', p == Fr(sum(1 for w in range(1, 7) if w in m), 6))])
        sek = rng.choice([[90, 90, 180], [120, 120, 120], [60, 120, 180], [45, 135, 180]])
        farben = ['rot', 'gelb', 'grün']
        lap = len(set(sek)) == 1
        return Kern(f'Ein Glücksrad hat drei Felder mit den Mittelpunktswinkeln {sek[0]}° (rot), {sek[1]}° (gelb) und {sek[2]}° (grün).',
                    'Ist das Glücksrad ein Laplace-Experiment (bezogen auf die Farbe)? Gib P(grün) an.', ('Ja' if lap else 'Nein') + f'; P(grün) = {z(Fr(sek[2], 360), False)}',
                    ['Laplace nur, wenn alle Ergebnisse gleich wahrscheinlich sind (gleiche Winkel).', f'P(grün) = {sek[2]}/360 = {z(Fr(sek[2], 360), False)}'], [('Ja; P(grün) = 1/3', 'Anzahl der Felder statt Winkel betrachtet')],
                    [check('Summe 360', sum(sek) == 360)], antwort_kurz=('Ja' if lap else 'Nein') + f'; P(grün) = {z(Fr(sek[2], 360), False)}')
    if et in ('rel_haeufigkeit', 'grosse_zahlen'):
        n = rng.choice([50, 100, 200, 400])
        k = rng.randint(n // 8, n // 3)
        aus = (f'{rng.choice(NAMEN)} würfelt {n}-mal und erhält {k}-mal eine Sechs. Sie/er sagt: „Bei den nächsten {n} Würfen kommt die Sechs sicher genau {k}-mal.“', False,
               'relative Häufigkeiten schwanken; erst bei sehr vielen Würfen nähern sie sich der Wahrscheinlichkeit 1/6 an, ein genaues Ergebnis ist nie sicher.')
        return Kern(f'Ein Würfel wird {n}-mal geworfen, dabei fällt {k}-mal eine Sechs.', 'Berechne die relative Häufigkeit der Sechs und vergleiche mit der Wahrscheinlichkeit.',
                    f'{z(Fr(k, n), True)} ≈ {round(100 * k / n)} %; Wahrscheinlichkeit 1/6 ≈ 16,7 %', [f'{k} : {n} = {z(Fr(k, n), True)}', 'Bei vielen Würfen nähert sich die relative Häufigkeit der Wahrscheinlichkeit (Gesetz der großen Zahlen).'],
                    [(z(Fr(n, k), True), 'Kehrwert')], [check('rel. Häufigkeit', Fr(k, n) * n == k)], aussage=(aus[0] + ' Stimmt das? Begründe.', aus[1], aus[2]))
    if et in ('zaehlprinzip', 'reihenfolgen'):
        a, b, c = rng.randint(2, 5), rng.randint(2, 6), rng.randint(2, 4)
        return Kern(f'{rng.choice(NAMEN)} hat {a} Hosen, {b} T-Shirts und {c} Paar Schuhe.', 'Wie viele verschiedene Kombinationen aus Hose, T-Shirt und Schuhen gibt es?', str(a * b * c),
                    ['Zählprinzip: Anzahlen multiplizieren', f'{a} · {b} · {c} = {a * b * c}'], [(str(a + b + c), 'addiert statt multipliziert')], [check('Abzählen', a * b * c == len(list(itertools.product(range(a), range(b), range(c)))))])
    if et == 'baumdiagramm':
        p = Fr(rng.randint(1, 4), 5)
        q = Fr(rng.randint(1, 3), 4)
        return Kern(f'Ein Bus ist mit Wahrscheinlichkeit {z(p, False)} pünktlich, die Anschlussbahn unabhängig davon mit {z(q, False)}.', 'Zeichne ein Baumdiagramm und berechne die Wahrscheinlichkeit, dass beide pünktlich sind.',
                    z(p * q, False), ['Pfadregel: Wahrscheinlichkeiten entlang des Pfades multiplizieren', f'{z(p, False)} · {z(q, False)} = {z(p * q, False)}'], [(z(p + q, False), 'addiert statt multipliziert')],
                    [check('Pfadregel', p * q <= 1)])
    # systematisch / bedingungen / grenzen
    s = rng.randint(3, 7)
    anz = sum(1 for n in range(100, 1000) if sum(map(int, str(n))) == s)
    return Kern('', f'Wie viele dreistellige Zahlen haben die Quersumme {s}? Gehe systematisch vor.', str(anz),
                ['Nach der Hunderterziffer ordnen (1, 2, …) und jeweils alle Möglichkeiten für Zehner und Einer aufschreiben.', f'Anzahl: {anz}'], [(str(anz - 1), 'eine Möglichkeit mit 0 vergessen')],
                [check('Brute Force', anz == len([n for n in range(100, 1000) if sum(map(int, str(n))) == s]))])


def _abz(r, b, g, was):
    kugeln = ['r'] * r + ['b'] * b + ['g'] * g
    paare = list(itertools.permutations(range(len(kugeln)), 2))
    if was == 'zweimal rot':
        gut = sum(1 for i, j in paare if kugeln[i] == 'r' and kugeln[j] == 'r')
    else:
        gut = sum(1 for i, j in paare if kugeln[i] == 'b' and kugeln[j] == 'r')
    return Fr(gut, len(paare))
