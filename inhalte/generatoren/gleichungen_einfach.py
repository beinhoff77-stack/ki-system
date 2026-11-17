#!/usr/bin/env python3
"""Thema gleichungen.einfach – Einfache Gleichungen (Gymnasium Bayern, Klasse 5). Nachbau Runde 5.

Waage-Modell, Umkehraufgaben (Plus/Minus, Mal/Geteilt, zwei Schritte), Probe und Fehler finden,
Textaufgaben als Gleichung, Vertiefung: Gleichungen ohne Lösung in ℕ.
Schreibweise Klasse 5: Malpunkt sichtbar (3 · x), Variable x als Platzhalter für eine unbekannte Zahl.
"""
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _nachbau import A, Z, baue, gl, mit_bild, tabelle, waage, zt  # noqa: E402

META = {'thema_schluessel': 'gleichungen.einfach', 'thema_id': 1, 'block_id': 64, 'klasse': {'gym_by': 5, 'rs_by': 6, 'ib_myp': 1}}

ETAPPEN = [
    {'lernziel': 'waage', 'titel': 'Eine Gleichung ist wie eine Waage',
     'regel': 'Eine ⟦Gleichung⟧ ist wie eine Waage im Gleichgewicht: Links ist genauso viel wie rechts. Das x steht für eine ⟦unbekannte Zahl⟧. '
              'Die Zahl, die die Waage im Gleichgewicht hält, heißt ⟦Lösung⟧. Nimmst du auf ⟦beiden Seiten⟧ dasselbe weg, bleibt die Waage im Gleichgewicht.',
     'schritte': ['Links liegen eine Dose mit x Murmeln und 3 einzelne Murmeln. Rechts liegen 10 Murmeln. Die Waage ist im Gleichgewicht: x + 3 = 10.',
                  'Nimm auf beiden Seiten 3 Murmeln weg. Links bleibt nur die Dose, rechts bleiben 7 Murmeln: ⟦x = 7⟧.'],
     'probe': '7 + 3 = 10 ✓',
     'fehler': 'Nur auf einer Seite etwas wegnehmen: Wer links die 3 Murmeln wegnimmt und rechts nicht, bekommt x = 10. '
               'Aber 10 + 3 = 13, nicht 10 – die Waage kippt. Was du links tust, tust du auch ⟦rechts⟧.',
     'bild': waage('x + 3', '10'),
     '_verbot': ['x + 3 = 10']},
    {'lernziel': 'umkehr_plus', 'titel': 'Plus und Minus rückwärts rechnen',
     'regel': 'Bei x + 8 = 20 fragst du: Welche Zahl plus 8 ergibt 20? Du rechnest ⟦rückwärts⟧. Die Umkehrung von Plus ist ⟦Minus⟧: x = 20 − 8. '
              'Die Umkehrung von Minus ist ⟦Plus⟧: Bei x − 15 = 27 ist x = 27 + 15.',
     'schritte': ['Im Geldbeutel war Geld. Nach einem Einkauf für 15 € sind noch 27 € darin: x − 15 = 27.',
                  'Rückwärts: Leg die 15 € wieder hinein. 27 + 15 = ⟦42⟧. Vorher waren 42 € im Geldbeutel.'],
     'probe': '42 − 15 = 27 ✓',
     'fehler': 'Bei x − 15 = 27 rechnen viele 27 − 15 = 12. Probe: 12 − 15 ergibt nicht 27. '
               'Wer etwas ausgegeben hat, hatte vorher ⟦mehr⟧ Geld. Die Umkehrung von Minus ist Plus: 27 + 15 = 42.',
     '_verbot': ['x − 15 = 27']},
    {'lernziel': 'umkehr_mal', 'titel': 'Mal und Geteilt rückwärts rechnen',
     'regel': 'Die Umkehrung von Mal ist ⟦Geteilt⟧: Bei 4 · x = 12 ist x = 12 : 4. Die Umkehrung von Geteilt ist ⟦Mal⟧: Bei x : 4 = 12 ist x = 12 · 4.',
     'schritte': ['4 gleich teure Hefte kosten zusammen 12 €: 4 · x = 12.',
                  'Rückwärts: Verteile die 12 € auf 4 Hefte. 12 : 4 = ⟦3⟧. Ein Heft kostet 3 €.'],
     'probe': '4 · 3 = 12 ✓',
     'fehler': 'Bei x : 4 = 12 rechnen viele 12 : 4 = 3. Probe: 3 : 4 ergibt nicht 12. '
               'Eine Pizza wurde in 4 gleiche Teile geteilt, jedes Teil wiegt 12 dag – die ganze Pizza wiegt ⟦mehr⟧, nämlich 12 · 4 = 48 dag.',
     '_verbot': ['4 · x = 12', 'x : 4 = 12']},
    {'lernziel': 'zwei_schritte', 'titel': 'Zwei Rechenschritte rückwärts',
     'regel': 'Bei 3 · x + 4 = 19 wurde x erst ⟦mal 3⟧ genommen, dann ⟦plus 4⟧ gerechnet. Du gehst die Rechenkette rückwärts: '
              'Den ⟦letzten⟧ Schritt kehrst du zuerst um. Also erst − 4, dann : 3.',
     'schritte': ['3 Kinokarten und eine Tüte Popcorn für 4 € kosten zusammen 19 €: 3 · x + 4 = 19.',
                  'Erst das Popcorn abziehen: 19 − 4 = 15. So viel kosten die 3 Karten.',
                  'Dann auf 3 Karten verteilen: 15 : 3 = ⟦5⟧. Eine Karte kostet 5 €.'],
     'probe': '3 · 5 + 4 = 15 + 4 = 19 ✓',
     'fehler': 'Die Schritte in der falschen Reihenfolge umkehren. Bei 2 · x + 6 = 20 rechnet man falsch 20 : 2 = 10 und dann 10 − 6 = 4. '
               'Probe: 2 · 4 + 6 = 14, nicht 20. Richtig ist ⟦erst − 6, dann : 2⟧: 20 − 6 = 14, 14 : 2 = 7.',
     'bild': tabelle(['', 'Start', '1. Schritt', 'Zwischenwert', '2. Schritt', 'Ende'],
                     [['vorwärts', 'x', '· 3', '?', '+ 4', '19'], ['rückwärts', '5', ': 3', '15', '− 4', '19']]),
     '_verbot': ['3 · x + 4 = 19', '2 · x + 6 = 20']},
    {'lernziel': 'probe', 'titel': 'Probe machen und Fehler finden',
     'regel': 'Mit der ⟦Probe⟧ prüfst du eine Lösung: Setze die Zahl für x in die ⟦ursprüngliche Gleichung⟧ ein und rechne links aus. '
              'Kommt dasselbe heraus wie rechts, ist die Waage im Gleichgewicht und die Lösung ⟦stimmt⟧.',
     'schritte': ['Jemand hat 5 · x − 8 = 27 gelöst und x = 7 herausbekommen.',
                  'Probe: 5 · 7 − 8 = 35 − 8 = 27. Rechts steht auch 27, also ⟦stimmt⟧ die Lösung.'],
     'fehler': 'Die Probe mit der eigenen Rechnung statt mit der Gleichung machen. Wer bei x − 15 = 27 falsch 27 − 15 = 12 rechnet und dann prüft '
               '„27 − 15 = 12 ✓“, findet seinen Fehler nie. Setze immer in die ⟦Gleichung⟧ ein: 12 − 15 ergibt nicht 27.',
     '_verbot': ['5 · x − 8 = 27']},
    {'lernziel': 'aufstellen', 'titel': 'Textaufgaben als Gleichung',
     'regel': 'Die gesuchte Zahl nennst du ⟦x⟧. Dann übersetzt du den Text Stück für Stück: „das Dreifache“ heißt 3 · x, „vermehrt um 5“ heißt + 5, '
              '„ergibt“ oder „kostet zusammen“ heißt ⟦=⟧. Stell dir die Waage vor: Was liegt links, was rechts?',
     'schritte': ['Eine Packung Sammelkarten und ein Album für 2 € kosten zusammen 9 €. Wie teuer ist die Packung?',
                  'Links: Packung x und 2 €. Rechts: 9 €. Gleichung: x + 2 = 9.',
                  'Rückwärts: 9 − 2 = ⟦7⟧. Die Packung kostet 7 €.'],
     'probe': '7 + 2 = 9 ✓',
     'fehler': '„Das Doppelte einer Zahl, vermindert um 4, ergibt 10“ ist nicht 2 · (x − 4) = 10. Erst wird verdoppelt, dann 4 abgezogen: '
               '⟦2 · x − 4 = 10⟧, also x = 7. Mit der falschen Gleichung käme 9 heraus – aber 2 · 9 − 4 = 14, nicht 10.',
     '_verbot': ['x + 2 = 9']},
    {'lernziel': 'ohne_loesung', 'titel': 'Gibt es immer eine Lösung?',
     'regel': 'Nicht jede Gleichung hat eine Lösung in den ⟦natürlichen Zahlen⟧ ℕ = {0; 1; 2; 3; …}. x + 9 = 4 hat dort keine: Eine natürliche Zahl plus 9 ist mindestens 9. '
              'Mit den ⟦ganzen Zahlen⟧ geht es: x = −5. Auch 3 · x = 10 hat in ℕ keine Lösung, denn 10 ist ⟦nicht durch 3 teilbar⟧.',
     'schritte': ['Ein Aufzug fährt 9 Stockwerke nach oben und hält im 4. Stock: x + 9 = 4.',
                  'Rückwärts: 4 − 9. Das ist keine natürliche Zahl. Mit ganzen Zahlen: 4 − 9 = ⟦−5⟧. Der Aufzug ist im 5. Untergeschoss losgefahren.'],
     'probe': '(−5) + 9 = 4 ✓',
     'fehler': 'Bei x + 9 = 4 einfach 9 − 4 = 5 rechnen. Probe: 5 + 9 = 14, nicht 4. Die Umkehrung ist 4 − 9, und das ist ⟦keine natürliche Zahl⟧.',
     '_verbot': ['x + 9 = 4']},
]


# ---------------- Waage ----------------
def g_waage(R, s):
    if s == 1:
        a, x = R.randint(2, 9), R.randint(1, 15)
        b = x + a
        if R.random() < .6:
            return mit_bild(Z(f'Die Waage ist im Gleichgewicht: x + {a} = {b}. Welche Zahl ist x?', x, f'{b} - {a}',
                              f'Auf beiden Seiten {a} wegnehmen: x = {b} − {a} = {x}. Probe: {x} + {a} = {b} ✓',
                              'Was musst du auf beiden Seiten wegnehmen, damit links nur x bleibt?'), waage(f'x + {a}', str(b)))
        n = R.choice([x, x, b, b + a])
        if n == x:
            return A(R, f'Ist {n} eine Lösung von x + {a} = {b}?', f'Ja, denn {n} + {a} = {b}.',
                     [f'Nein, denn {n} ist kleiner als {b}.', f'Nein, die Lösung muss {b} sein.'],
                     f'Einsetzen: {n} + {a} = {b}. Links und rechts steht dasselbe, die Waage ist im Gleichgewicht.',
                     'Setze die Zahl für x ein und rechne die linke Seite aus.')
        return A(R, f'Ist {n} eine Lösung von x + {a} = {b}?', f'Nein, denn {n} + {a} = {n + a}, nicht {b}.',
                 [f'Ja, denn {n} + {a} = {b}.', f'Ja, x ist immer die Zahl rechts.'],
                 f'Einsetzen: {n} + {a} = {n + a}. Rechts steht aber {b}. Die Lösung ist {x}, denn {x} + {a} = {b}.',
                 'Setze die Zahl für x ein und rechne die linke Seite aus.')
    if s == 2:
        art = R.choice(['bild', 'bild', 'umgekehrt', 'beide', 'probieren'])
        a, x = R.randint(5, 30), R.randint(4, 40)
        b = x + a
        if art == 'bild':
            return mit_bild(Z(f'Die Waage ist im Gleichgewicht: x + {a} = {b}. Welche Zahl ist x?', x, f'{b} - {a}',
                              f'Auf beiden Seiten {a} wegnehmen: x = {b} − {a} = {x}. Probe: {x} + {a} = {b} ✓',
                              'Nimm auf beiden Seiten dasselbe weg.'), waage(f'x + {a}', str(b)))
        if art == 'umgekehrt':
            return mit_bild(Z(f'Die Waage ist im Gleichgewicht: {b} = x + {a}. Welche Zahl ist x?', x, f'{b} - {a}',
                              f'Jetzt liegt x rechts. Auf beiden Seiten {a} wegnehmen: {b} − {a} = x, also x = {x}.',
                              'Die Gleichung steht andersherum. Das ändert nichts: Nimm auf beiden Seiten dasselbe weg.'), waage(str(b), f'x + {a}'))
        if art == 'beide':
            return A(R, f'Auf der Waage liegt links x + {a}, rechts {b}. Du nimmst links {a} weg. Was musst du rechts tun, damit die Waage im Gleichgewicht bleibt?',
                     f'Rechts auch {a} wegnehmen.', ['Rechts nichts ändern.', f'Rechts {a} dazulegen.', f'Rechts alles wegnehmen.'],
                     f'Was links passiert, muss auch rechts passieren: {b} − {a} = {x}. Dann gilt x = {x}.',
                     'Eine Waage bleibt nur im Gleichgewicht, wenn beide Seiten gleich verändert werden.')
        return A(R, f'Welche Zahl ist die Lösung von {a} + x = {b}? Probiere aus.', str(x), [str(b), str(b + a), str(a)],
                 f'{a} + {x} = {b} ✓. Mit {b} käme {a + b} heraus, mit {a} nur {2 * a}.',
                 'Setze jede Zahl für x ein und rechne nach.')
    art = R.choice(['zwei', 'drei', 'x_beide'])
    if art == 'zwei':
        x, a = R.randint(2, 15), R.randint(2, 9)
        b = 2 * x + a
        return mit_bild(Z(f'Links liegen zwei gleiche Dosen mit je x Murmeln und {a} Murmeln, rechts {b} Murmeln. Die Waage ist im Gleichgewicht. Wie viele Murmeln sind in einer Dose?',
                          x, f'({b} - {a}) // 2', f'Erst auf beiden Seiten {a} Murmeln wegnehmen: In zwei Dosen sind zusammen {b - a} Murmeln. In einer Dose: {b - a} : 2 = {x}.',
                          'Nimm zuerst die einzelnen Murmeln weg. Dann teile auf die Dosen auf.'), waage(f'x + x + {a}', str(b)))
    if art == 'drei':
        x = R.randint(2, 12)
        b = 3 * x
        return mit_bild(Z(f'Links liegen drei gleiche Dosen mit je x Murmeln, rechts {b} Murmeln. Die Waage ist im Gleichgewicht. Wie viele Murmeln sind in einer Dose?',
                          x, f'{b} // 3', f'In drei Dosen sind zusammen {b} Murmeln. In einer Dose ist ein Drittel davon: {b} : 3 = {x}.',
                          'Verteile die Murmeln rechts gleichmäßig auf die Dosen.'), waage('x + x + x', str(b)))
    x, a = R.randint(2, 20), R.randint(2, 9)
    b = x + a
    return mit_bild(Z(f'Links liegen zwei gleiche Dosen und {a} Murmeln, rechts eine solche Dose und {b} Murmeln. Die Waage ist im Gleichgewicht. Wie viele Murmeln sind in einer Dose?',
                      x, f'{b} - {a}', f'Auf beiden Seiten eine Dose wegnehmen: links x + {a}, rechts {b}. Dann {a} wegnehmen: x = {b} − {a} = {x}.',
                      'Auf beiden Seiten liegt mindestens eine Dose. Was kannst du wegnehmen?'), waage(f'x + x + {a}', f'x + {b}'))


# ---------------- Plus und Minus ----------------
def g_umkehr_plus(R, s):
    if s == 1:
        a, x = R.randint(2, 20), R.randint(1, 40)
        if R.random() < .5:
            b = x + a
            return Z(f'Löse x + {a} = {b}.', x, f'{b} - {a}', f'Umkehrung von Plus ist Minus: x = {b} − {a} = {x}. Probe: {x} + {a} = {b} ✓',
                     'Welche Zahl plus ' + str(a) + ' ergibt ' + str(b) + '? Rechne rückwärts.')
        x = x + a
        b = x - a
        return Z(f'Löse x − {a} = {b}.', x, f'{b} + {a}', f'Umkehrung von Minus ist Plus: x = {b} + {a} = {x}. Probe: {x} − {a} = {b} ✓',
                 'Rechne rückwärts. Was ist die Umkehrung von Minus?')
    if s == 2:
        art = R.choice(['plus', 'minus', 'vorne', 'rechnung'])
        a, x = R.randint(12, 250), R.randint(10, 400)
        if art == 'plus':
            b = x + a
            return Z(f'Löse x + {a} = {b}.', x, f'{b} - {a}', f'x = {b} − {a} = {x}. Probe: {x} + {a} = {b} ✓', 'Umkehrung von Plus ist Minus.')
        if art == 'vorne':
            b = x + a
            return Z(f'Löse {a} + x = {b}.', x, f'{b} - {a}', f'Ob x vorne oder hinten steht, ist bei Plus egal: x = {b} − {a} = {x}. Probe: {a} + {x} = {b} ✓',
                     'Die Reihenfolge beim Addieren ist egal. Rechne rückwärts.')
        if art == 'minus':
            x = x + a
            b = x - a
            return Z(f'Löse x − {a} = {b}.', x, f'{b} + {a}', f'x = {b} + {a} = {x}. Probe: {x} − {a} = {b} ✓', 'Umkehrung von Minus ist Plus.')
        x = x + a
        b = x - a
        return A(R, f'Welche Rechnung führt zur Lösung von x − {a} = {b}?', f'{b} + {a}', [f'{b} − {a}', f'{a} − {b}', f'{a} + {a}'],
                 f'Von x wurde {a} abgezogen. Rückwärts wird {a} wieder addiert: x = {b} + {a} = {x}.',
                 'Was ist die Umkehrung von Minus?')
    art = R.choice(['a_minus_x', 'a_minus_x', 'rechnung', 'rechts_summe'])
    if art == 'a_minus_x':
        a = R.randint(30, 200)
        b = R.randint(5, a - 5)
        x = a - b
        return Z(f'Löse {a} − x = {b}.', x, f'{a} - {b}', f'Von {a} wird x abgezogen, es bleibt {b}. Also ist x der Unterschied: x = {a} − {b} = {x}. Probe: {a} − {x} = {b} ✓',
                 f'Achtung, x wird hier abgezogen. Wie viel musst du von {a} wegnehmen, damit {b} übrig bleibt?')
    if art == 'rechnung':
        a = R.randint(30, 200)
        b = R.randint(5, a - 5)
        return A(R, f'Welche Rechnung führt zur Lösung von {a} − x = {b}?', f'{a} − {b}', [f'{a} + {b}', f'{b} − {a}'],
                 f'x ist das, was von {a} weggenommen wird, damit {b} bleibt: x = {a} − {b} = {a - b}. Mit {a} + {b} = {a + b} wäre {a} − {a + b} gar nicht {b}.',
                 'Probiere mit kleinen Zahlen: 10 − x = 3. Welche Zahl ist x, und wie hast du sie gerechnet?')
    a, p, q = R.randint(5, 60), R.randint(10, 80), R.randint(10, 80)
    x = p + q - a
    if x <= 0: return g_umkehr_plus(R, s)
    return Z(f'Löse x + {a} = {p} + {q}.', x, f'{p} + {q} - {a}', f'Erst die rechte Seite ausrechnen: {p} + {q} = {p + q}. Dann x = {p + q} − {a} = {x}.',
             'Rechne zuerst aus, was rechts steht.')


# ---------------- Mal und Geteilt ----------------
def g_umkehr_mal(R, s):
    if s == 1:
        a, x = R.randint(2, 10), R.randint(2, 12)
        if R.random() < .5:
            b = a * x
            return Z(f'Löse {a} · x = {b}.', x, f'{b} // {a}', f'Umkehrung von Mal ist Geteilt: x = {b} : {a} = {x}. Probe: {a} · {x} = {b} ✓',
                     f'Welche Zahl mal {a} ergibt {b}?')
        b = x
        x = a * b
        return Z(f'Löse x : {a} = {b}.', x, f'{b} * {a}', f'Umkehrung von Geteilt ist Mal: x = {b} · {a} = {x}. Probe: {x} : {a} = {b} ✓',
                 'Rechne rückwärts. Was ist die Umkehrung von Geteilt?')
    if s == 2:
        art = R.choice(['mal', 'geteilt', 'rechnung', 'mal'])
        a, x = R.choice([3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 20, 25]), R.randint(6, 30)
        if a == x: return g_umkehr_mal(R, s)
        if art == 'mal':
            b = a * x
            return Z(f'Löse {a} · x = {b}.', x, f'{b} // {a}', f'x = {b} : {a} = {x}. Probe: {a} · {x} = {b} ✓', 'Umkehrung von Mal ist Geteilt.')
        if art == 'geteilt':
            return Z(f'Löse x : {a} = {x}.', a * x, f'{x} * {a}', f'x = {x} · {a} = {a * x}. Probe: {a * x} : {a} = {x} ✓', 'Umkehrung von Geteilt ist Mal.')
        return A(R, f'Welche Rechnung führt zur Lösung von x : {a} = {x}?', f'{x} · {a}', [f'{x} : {a}', f'{x} − {a}', f'{a} : {x}'],
                 f'x wurde durch {a} geteilt. Rückwärts wird mit {a} malgenommen: x = {x} · {a} = {a * x}.', 'Was ist die Umkehrung von Geteilt?')
    art = R.choice(['a_durch_x', 'a_durch_x', 'rechnung', 'produkt_rechts'])
    if art == 'a_durch_x':
        x, b = R.randint(2, 12), R.randint(2, 12)
        a = x * b
        return Z(f'Löse {a} : x = {b}.', x, f'{a} // {b}', f'{a} wird durch x geteilt, es kommt {b} heraus. Also ist x = {a} : {b} = {x}. Probe: {a} : {x} = {b} ✓',
                 f'Achtung, hier wird durch x geteilt. In wie viele Teile musst du {a} teilen, damit jedes Teil {b} ist?')
    if art == 'rechnung':
        x, b = R.randint(2, 12), R.randint(2, 12)
        a = x * b
        if x == b: return g_umkehr_mal(R, s)
        return A(R, f'Welche Rechnung führt zur Lösung von {a} : x = {b}?', f'{a} : {b}', [f'{a} · {b}', f'{b} : {a}', f'{a} − {b}'],
                 f'x ist die Zahl, durch die du {a} teilen musst, um {b} zu bekommen: x = {a} : {b} = {x}. Mit {a} · {b} = {a * b} wäre {a} : {a * b} viel kleiner als {b}.',
                 'Probiere mit kleinen Zahlen: 12 : x = 3. Welche Zahl ist x, und wie hast du sie gerechnet?')
    a, p, q = R.randint(2, 9), R.randint(2, 12), R.randint(2, 12)
    if (p * q) % a or p == a or q == a: return g_umkehr_mal(R, s)
    x = p * q // a
    return Z(f'Löse {a} · x = {p} · {q}.', x, f'{p} * {q} // {a}', f'Erst rechts ausrechnen: {p} · {q} = {p * q}. Dann x = {p * q} : {a} = {x}.',
             'Rechne zuerst aus, was rechts steht.')


# ---------------- Zwei Schritte ----------------
def kette(a, op1, b, op2, ende):
    return tabelle(['', 'Start', '1. Schritt', 'Zwischenwert', '2. Schritt', 'Ende'], [['vorwärts', 'x', f'{op1} {a}', '?', f'{op2} {b}', str(ende)]])


def g_zwei_schritte(R, s):
    if s == 1:
        a, x, b = R.randint(2, 6), R.randint(1, 10), R.randint(1, 15)
        if R.random() < .5:
            c = a * x + b
            return Z(f'Löse {gl(a, b)} = {c}.', x, f'({c} - {b}) // {a}', f'Erst − {b}: {c} − {b} = {c - b}. Dann : {a}: {c - b} : {a} = {x}. Probe: {a} · {x} + {b} = {c} ✓',
                     f'Kehre zuerst das „+ {b}“ um, dann das „· {a}“.')
        if a * x <= b: return g_zwei_schritte(R, s)
        c = a * x - b
        return Z(f'Löse {gl(a, -b)} = {c}.', x, f'({c} + {b}) // {a}', f'Erst + {b}: {c} + {b} = {c + b}. Dann : {a}: {c + b} : {a} = {x}. Probe: {a} · {x} − {b} = {c} ✓',
                 f'Kehre zuerst das „− {b}“ um, dann das „· {a}“.')
    if s == 2:
        art = R.choice(['plus', 'geteilt', 'reihenfolge', 'kette', 'kette'])
        a, x, b = R.randint(2, 12), R.randint(2, 25), R.randint(2, 40)
        if art == 'plus':
            c = a * x + b
            return Z(f'Löse {gl(a, b)} = {c}.', x, f'({c} - {b}) // {a}', f'{c} − {b} = {c - b}; {c - b} : {a} = {x}. Probe: {a} · {x} + {b} = {c} ✓',
                     'Den letzten Rechenschritt zuerst umkehren.')
        if art == 'geteilt':
            q = x
            c = q + b
            return Z(f'Löse x : {a} + {b} = {c}.', q * a, f'({c} - {b}) * {a}', f'Erst − {b}: {c} − {b} = {q}. Dann · {a}: {q} · {a} = {q * a}. Probe: {q * a} : {a} + {b} = {c} ✓',
                     f'Kehre zuerst das „+ {b}“ um, dann das „: {a}“.')
        if art == 'reihenfolge':
            c = a * x + b
            return A(R, f'Wie löst du {gl(a, b)} = {c}?', f'Erst − {b}, dann : {a}', [f'Erst : {a}, dann − {b}', f'Erst + {b}, dann · {a}', f'Erst − {a}, dann : {b}'],
                     f'Vorwärts wurde erst · {a}, dann + {b} gerechnet. Rückwärts: erst − {b}, dann : {a}. Das ergibt x = {x}.',
                     'Welcher Rechenschritt wurde zuletzt gemacht?')
        if R.random() < .5:
            c = a * x - b
            if c <= 0: return g_zwei_schritte(R, s)
            return mit_bild(Z(f'Rechne die Rechenkette rückwärts: x · {a} − {b} = {c}. Welche Zahl ist x?', x, f'({c} + {b}) // {a}',
                              f'Rückwärts: {c} + {b} = {c + b}, dann {c + b} : {a} = {x}.', 'Fange am Ende an und kehre jeden Schritt um.'), kette(a, '·', b, '−', c))
        c = a * x + b
        return mit_bild(Z(f'Rechne die Rechenkette rückwärts: x · {a} + {b} = {c}. Welche Zahl ist x?', x, f'({c} - {b}) // {a}',
                          f'Rückwärts: {c} − {b} = {c - b}, dann {c - b} : {a} = {x}.', 'Fange am Ende an und kehre jeden Schritt um.'), kette(a, '·', b, '+', c))
    art = R.choice(['klammer_plus', 'klammer_minus', 'geteilt_minus', 'wahl'])
    a, x, b = R.randint(2, 9), R.randint(2, 20), R.randint(2, 15)
    if art == 'klammer_plus':
        c = (x + b) * a
        return Z(f'Löse (x + {b}) · {a} = {c}.', x, f'{c} // {a} - {b}', f'Hier wurde zuerst + {b}, dann · {a} gerechnet. Rückwärts: erst : {a}: {c} : {a} = {c // a}. Dann − {b}: x = {x}.',
                 'Die Klammer wird zuerst gerechnet. Welcher Schritt kommt also zuletzt?')
    if art == 'klammer_minus':
        x = x + b
        c = (x - b) * a
        return Z(f'Löse (x − {b}) · {a} = {c}.', x, f'{c} // {a} + {b}', f'Rückwärts: erst : {a}: {c} : {a} = {c // a}. Dann + {b}: x = {x}. Probe: ({x} − {b}) · {a} = {c} ✓',
                 'Die Klammer wird zuerst gerechnet. Welcher Schritt kommt also zuletzt?')
    if art == 'geteilt_minus':
        q = x
        c = q - b
        if c <= 0: return g_zwei_schritte(R, s)
        return Z(f'Löse x : {a} − {b} = {c}.', q * a, f'({c} + {b}) * {a}', f'Rückwärts: erst + {b}: {c} + {b} = {q}. Dann · {a}: x = {q * a}. Probe: {q * a} : {a} − {b} = {c} ✓',
                 'Kehre zuerst das Minus um, dann das Geteilt.')
    c = (x + b) * a
    return A(R, f'Welche Rechnung löst (x + {b}) · {a} = {c}?', f'{c} : {a} − {b}', [f'{c} − {b} : {a}', f'({c} − {b}) : {a}', f'{c} · {a} − {b}'],
             f'In der Klammer wird zuerst + {b} gerechnet, danach · {a}. Rückwärts also erst : {a}, dann − {b}: {c} : {a} − {b} = {x}.',
             'Was wurde zuletzt gerechnet: das Plus in der Klammer oder das Mal?')


# ---------------- Probe ----------------
def g_probe(R, s):
    if s == 1:
        a, x, b = R.randint(2, 9), R.randint(2, 12), R.randint(1, 20)
        c = a * x + b
        art = R.choice(['ja', 'nein', 'links'])
        if art == 'links':
            n = x + R.choice([-1, 1, 2])
            return Z(f'Mache die Probe für x = {n} bei {gl(a, b)} = {c}. Welche Zahl kommt links heraus?', a * n + b, f'{a} * {n} + {b}',
                     f'{a} · {n} + {b} = {a * n} + {b} = {a * n + b}. ' + ('Das ist auch rechts, die Lösung stimmt.' if a * n + b == c else f'Rechts steht {c}, also ist {n} keine Lösung.'),
                     'Setze die Zahl für x ein. Punkt vor Strich!')
        if art == 'ja':
            return A(R, f'Ist x = {x} eine Lösung von {gl(a, b)} = {c}?', f'Ja: {a} · {x} + {b} = {c}.',
                     [f'Nein: {a} · {x} + {b} = {c + a}.', f'Nein: {a} · {x} + {b} = {a * (x + b)}.'],
                     f'Einsetzen: {a} · {x} + {b} = {a * x} + {b} = {c}. Links und rechts steht dasselbe.',
                     'Setze die Zahl für x ein. Punkt vor Strich!')
        n = R.choice([(c - b) // a + 1 if (c - b) // a + 1 != x else x + 2, x - 1 if x > 2 else x + 3])
        L = a * n + b
        if a * (n + b) in (L, c): return g_probe(R, s)
        return A(R, f'Ist x = {n} eine Lösung von {gl(a, b)} = {c}?', f'Nein: {a} · {n} + {b} = {L}, nicht {c}.',
                 [f'Ja: {a} · {n} + {b} = {c}.', f'Nein: {a} · {n} + {b} = {a * (n + b)}, nicht {c}.'],
                 f'Einsetzen: {a} · {n} + {b} = {a * n} + {b} = {L}. Rechts steht {c}, also keine Lösung. Richtig wäre x = {x}.',
                 'Setze die Zahl für x ein. Punkt vor Strich!')
    if s == 2:
        art = R.choice(['schritt', 'schritt', 'richtig', 'welche'])
        a, x, b = R.randint(2, 8), R.randint(2, 15), R.randint(2, 20)
        c = a * x + b
        if art == 'schritt':
            if R.random() < .5 and x + 1 > a:
                b = a
                c = a * x + b
                q = c // a
                return A(R, f'So wurde {gl(a, b)} = {c} gelöst: Schritt 1: {c} : {a} = {q}. Schritt 2: {q} − {b} = {q - b}. Ergebnis: x = {q - b}. Wo steckt der Fehler?',
                         f'Schritt 1: Zuerst muss {b} abgezogen werden.', [f'Schritt 2: Es muss + {b} heißen.', 'Kein Fehler, die Lösung stimmt.', f'Schritt 1: Es muss {c} · {a} heißen.'],
                         f'Der letzte Schritt (+ {b}) wird zuerst umgekehrt: {c} − {b} = {c - b}, dann {c - b} : {a} = {x}. Probe mit {q - b}: {a} · {q - b} + {b} = {a * (q - b) + b}, nicht {c}.',
                         'Mache die Probe mit dem Ergebnis. Welcher Rechenschritt wurde vorwärts zuletzt gemacht?')
            if (c + b) % a: return g_probe(R, s)
            f = (c + b) // a
            return A(R, f'So wurde {gl(a, b)} = {c} gelöst: Schritt 1: {c} + {b} = {c + b}. Schritt 2: {c + b} : {a} = {f}. Ergebnis: x = {f}. Wo steckt der Fehler?',
                     f'Schritt 1: Es muss {c} − {b} heißen.', [f'Schritt 2: Es muss {c + b} · {a} heißen.', 'Kein Fehler, die Lösung stimmt.', f'Schritt 1: Zuerst muss durch {a} geteilt werden.'],
                     f'Die Umkehrung von + {b} ist − {b}: {c} − {b} = {c - b}, dann {c - b} : {a} = {x}. Probe mit {f}: {a} · {f} + {b} = {a * f + b}, nicht {c}.',
                     'Mache die Probe. Was ist die Umkehrung von Plus?')
        if art == 'richtig':
            x2 = R.randint(10, 60)
            a2 = R.randint(5, 40)
            b2 = x2 - a2
            if b2 <= a2 or b2 - a2 == x2: return g_probe(R, s)
            return Z(f'Bei x − {a2} = {b2} hat jemand x = {b2 - a2} herausbekommen. Die Probe geht nicht auf. Wie heißt die richtige Lösung?',
                     x2, f'{b2} + {a2}', f'Probe mit {b2 - a2}: {b2 - a2} − {a2} ergibt nicht {b2}. Die Umkehrung von Minus ist Plus: x = {b2} + {a2} = {x2}.',
                     'Welche Umkehrung wurde verwechselt?')
        opts = [x, (c - b) // a + 1 if (c - b) // a + 1 != x else x + 1, c // a if c // a not in (x,) else x + 2, c - b]
        opts = [str(o) for o in opts]
        return A(R, f'Welche Zahl ist die Lösung von {gl(a, b)} = {c}? Mache die Probe.', str(x), opts[1:],
                 f'Probe mit {x}: {a} · {x} + {b} = {c} ✓.', 'Setze jede Zahl ein und vergleiche mit der rechten Seite.')
    art = R.choice(['wer', 'groesser', 'groesser'])
    a, x, b = R.randint(2, 6), R.randint(3, 12), R.randint(2, 9)
    if art == 'wer':
        c = (x + b) * a
        f = (c - b) // a if (c - b) % a == 0 else None
        if f is None or f == x: return g_probe(R, s)
        return A(R, f'Ben und Ida lösen (x + {b}) · {a} = {c}. Ben erhält x = {x}, Ida erhält x = {f}. Wer hat recht?',
                 f'Ben, denn ({x} + {b}) · {a} = {c}.', [f'Ida, denn ({f} + {b}) · {a} = {c}.', 'Beide, es gibt zwei Lösungen.', 'Keiner von beiden.'],
                 f'Probe Ben: ({x} + {b}) · {a} = {x + b} · {a} = {c} ✓. Probe Ida: ({f} + {b}) · {a} = {(f + b) * a}, nicht {c}. Ida hat zuerst {b} abgezogen statt zuerst durch {a} zu teilen.',
                 'Mache bei beiden die Probe.')
    c = a * x + b
    n = x + R.choice([-2, -1, 1, 2])
    if n < 1: return g_probe(R, s)
    L = a * n + b
    richtig = 'Größer als ' + str(n) if L < c else 'Kleiner als ' + str(n)
    return A(R, f'Bei {gl(a, b)} = {c} wird x = {n} getestet. Links kommt {L} heraus. Ist die Lösung größer oder kleiner als {n}?',
             richtig, ['Kleiner als ' + str(n) if L < c else 'Größer als ' + str(n), f'Genau {n}', 'Das kann man nicht sagen.'],
             f'Links kommt {L} heraus, rechts steht {c}. ' + (f'Links ist zu wenig, also muss x größer sein. ' if L < c else f'Links ist zu viel, also muss x kleiner sein. ')
             + f'Die Lösung ist x = {x}.', 'Ist links zu viel oder zu wenig? Was passiert, wenn x größer wird?')


# ---------------- Textaufgaben ----------------
VERB = {'+': ('addiere', 'zu ihr'), '-': ('subtrahiere', 'von ihr')}


def g_aufstellen(R, s):
    if s == 1:
        op = R.choice(['+', '-', '*', ':'])
        if op == '+':
            a, x = R.randint(3, 40), R.randint(2, 60)
            t, gle, c, w = f'Ich denke mir eine Zahl und addiere {a}. Ich erhalte {x + a}. Welche Zahl habe ich mir gedacht?', f'x + {a} = {x + a}', f'{x + a} - {a}', f'x = {x + a} − {a} = {x}'
        elif op == '-':
            a, x = R.randint(3, 40), R.randint(45, 99)
            t, gle, c, w = f'Ich denke mir eine Zahl und subtrahiere {a}. Ich erhalte {x - a}. Welche Zahl habe ich mir gedacht?', f'x − {a} = {x - a}', f'{x - a} + {a}', f'x = {x - a} + {a} = {x}'
        elif op == '*':
            a, x = R.randint(2, 9), R.randint(2, 15)
            t, gle, c, w = f'Ich denke mir eine Zahl und multipliziere sie mit {a}. Ich erhalte {a * x}. Welche Zahl habe ich mir gedacht?', f'{a} · x = {a * x}', f'{a * x} // {a}', f'x = {a * x} : {a} = {x}'
        else:
            a, q = R.randint(2, 9), R.randint(2, 15)
            x = a * q
            t, gle, c, w = f'Ich denke mir eine Zahl und teile sie durch {a}. Ich erhalte {q}. Welche Zahl habe ich mir gedacht?', f'x : {a} = {q}', f'{q} * {a}', f'x = {q} · {a} = {x}'
        if R.random() < .4 and op in '+-':
            a_ = a
            b = x + a_ if op == '+' else x - a_
            richtig = f'x + {a_} = {b}' if op == '+' else f'x − {a_} = {b}'
            falsch = [f'x − {a_} = {b}' if op == '+' else f'x + {a_} = {b}', f'{a_} − x = {b}', f'x = {a_} + {b}' if op == '+' else f'x = {b} − {a_}']
            return A(R, t.replace('Welche Zahl habe ich mir gedacht?', 'Welche Gleichung passt?'), richtig, falsch,
                     f'Die gedachte Zahl heißt x. „{VERB[op][0]} {a_}“ heißt {op.replace("-", "−")} {a_}, „ich erhalte“ heißt =. Also {richtig}.',
                     'Nenne die gedachte Zahl x und schreibe den Text Stück für Stück als Rechnung.')
        return Z(t, x, c, f'Gleichung: {gle}. Rückwärts: {w}.', 'Nenne die gedachte Zahl x. Schreibe eine Gleichung und rechne rückwärts.')
    if s == 2:
        art = R.choice(['raetsel', 'kauf', 'kauf', 'gleichung'])
        if art == 'raetsel':
            a, x, b = R.randint(2, 9), R.randint(2, 20), R.randint(2, 30)
            c = a * x + b
            return Z(f'Ich denke mir eine Zahl, nehme sie mal {a} und addiere dann {b}. Ich erhalte {c}. Welche Zahl habe ich mir gedacht?', x, f'({c} - {b}) // {a}',
                     f'Gleichung: {gl(a, b)} = {c}. Rückwärts: {c} − {b} = {c - b}, {c - b} : {a} = {x}.', 'Schreibe die Gleichung auf. Kehre dann den letzten Schritt zuerst um.')
        if art == 'kauf':
            ding, eins, preis, extra, extra_p = R.choice([('Kinokarten', 'eine Kinokarte', (6, 12), 'eine Tüte Popcorn', (3, 6)),
                                                           ('Hefte', 'ein Heft', (1, 3), 'einen Füller', (8, 15)),
                                                           ('Eintrittskarten fürs Schwimmbad', 'eine Eintrittskarte', (3, 7), 'ein Eis', (2, 4)),
                                                           ('Bälle', 'ein Ball', (6, 15), 'eine Pumpe', (5, 12)),
                                                           ('Busfahrkarten', 'eine Busfahrkarte', (2, 4), 'einen Stadtplan', (3, 8))])
            n, x, e = R.randint(2, 6), R.randint(*preis), R.randint(*extra_p)
            c = n * x + e
            return Z(f'Für {n} gleich teure {ding} und {extra} für {e} € zahlt man zusammen {c} €. Wie viel kostet {eins}?', x, f'({c} - {e}) // {n}',
                     f'Gleichung: {n} · x + {e} = {c}. Erst − {e}: {c - e}. Dann : {n}: {x} €.', 'Der Preis für eins ist x. Was kosten dann alle zusammen?', einheit='€')
        a, x, b = R.randint(2, 9), R.randint(2, 20), R.randint(2, 30)
        c = a * x - b
        if c <= 0: return g_aufstellen(R, s)
        return A(R, f'„Das {({2: "Doppelte", 3: "Dreifache", 4: "Vierfache", 5: "Fünffache"}).get(a, f"{a}-Fache")} einer Zahl, vermindert um {b}, ergibt {c}.“ Welche Gleichung passt?',
                 f'{gl(a, -b)} = {c}', [f'{a} · (x − {b}) = {c}', f'{gl(a, b)} = {c}', f'x − {a} · {b} = {c}'],
                 f'Erst wird die Zahl mal {a} genommen, dann {b} abgezogen: {gl(a, -b)} = {c}. Die Lösung ist x = {x}.',
                 'Was passiert zuerst mit der Zahl, was danach?')
    art = R.choice(['text_zu_gl', 'rechteck', 'alter'])
    if art == 'text_zu_gl':
        a, x, b = R.randint(2, 6), R.randint(3, 12), R.randint(2, 10)
        c = a * x + b
        return A(R, f'Welche Geschichte passt zur Gleichung {gl(a, b)} = {c}?',
                 f'{a} gleich teure Bücher und eine Tasche für {b} € kosten {c} €.',
                 [f'{a} Bücher kosten zusammen {c} €, eines davon {b} €.', f'Ein Buch und eine Tasche für {b} € kosten {c} €.', f'{b} gleich teure Bücher und eine Tasche für {a} € kosten {c} €.'],
                 f'{a} · x steht für {a} gleiche Dinge, die je x kosten. + {b} ist ein Ding für {b} €. Zusammen = {c}. Ein Buch kostet {x} €.',
                 'Was bedeutet die Zahl vor dem x? Was bedeutet das „+“?')
    if art == 'rechteck':
        b, x = R.randint(2, 15), R.randint(3, 25)
        if b == x: return g_aufstellen(R, s)
        u = 2 * x + 2 * b
        return Z(f'Ein Rechteck ist {b} cm breit. Sein Umfang beträgt {u} cm. Wie lang ist es?', x, f'({u} - 2 * {b}) // 2',
                 f'Umfang = zweimal Länge + zweimal Breite: 2 · x + {2 * b} = {u}. Erst − {2 * b}: {u - 2 * b}. Dann : 2: x = {x} cm.',
                 'Der Umfang ist zweimal die Länge plus zweimal die Breite. Stelle eine Gleichung auf.', einheit='cm')
    k, x = R.choice([(3, R.randint(9, 14)), (4, R.randint(7, 11)), (5, R.randint(6, 8))])
    S = x + k * x
    return Z(f'Eine Mutter ist {k}-mal so alt wie ihre Tochter. Zusammen sind sie {S} Jahre alt. Wie alt ist die Tochter?', x, f'{S} // {k + 1}',
             f'Tochter x, Mutter {k} · x. Zusammen: x + {k} · x = {S}. Das sind {k + 1} gleiche Teile wie {k + 1} Dosen auf der Waage: x = {S} : {k + 1} = {x} Jahre.',
             f'Die Mutter zählt wie {k} Töchter. Wie viele „Töchter-Alter“ sind es zusammen?', einheit='Jahre')


# ---------------- Ohne Lösung (Vertiefung) ----------------
def g_ohne_loesung(R, s):
    if s == 1:
        art = R.choice(['plus_nein', 'plus_ja', 'mal_nein', 'mal_ja'])
        if art.startswith('plus'):
            a = R.randint(5, 30)
            b = R.randint(0, a - 1) if art == 'plus_nein' else R.randint(a, a + 30)
            if art == 'plus_nein':
                return A(R, f'Hat x + {a} = {b} eine Lösung in ℕ?', f'Nein: x + {a} ist immer mindestens {a}.', [f'Ja: x = {a - b}', f'Ja: x = {a + b}'],
                         f'Eine natürliche Zahl plus {a} ist mindestens {a}, also nie {b}. Probe mit {a - b}: {a - b} + {a} = {2 * a - b}, nicht {b}.',
                         'Wie klein kann x + ' + str(a) + ' höchstens werden, wenn x eine natürliche Zahl ist?')
            return A(R, f'Hat x + {a} = {b} eine Lösung in ℕ?', f'Ja: x = {b - a}', ['Nein, keine natürliche Zahl passt.', f'Ja: x = {a + b}'],
                     f'x = {b} − {a} = {b - a} ist eine natürliche Zahl. Probe: {b - a} + {a} = {b} ✓', 'Rechne rückwärts. Ist das Ergebnis eine natürliche Zahl?')
        a = R.randint(2, 9)
        if art == 'mal_nein':
            b = a * R.randint(2, 9) + R.randint(1, a - 1)
            return A(R, f'Hat {a} · x = {b} eine Lösung in ℕ?', f'Nein: {b} ist nicht durch {a} teilbar.', [f'Ja: x = {b // a}', f'Ja: x = {b // a + 1}'],
                     f'{a} · {b // a} = {a * (b // a)} und {a} · {b // a + 1} = {a * (b // a + 1)}. {b} liegt dazwischen, also gibt es keine natürliche Zahl x.',
                     f'Ist {b} in der {a}er-Reihe?')
        q = R.randint(2, 12)
        return A(R, f'Hat {a} · x = {a * q} eine Lösung in ℕ?', f'Ja: x = {q}', ['Nein, keine natürliche Zahl passt.', f'Ja: x = {a * q * a}'],
                 f'{a * q} : {a} = {q}. Probe: {a} · {q} = {a * q} ✓', f'Ist {a * q} in der {a}er-Reihe?')
    if s == 2:
        art = R.choice(['welche', 'ganz', 'temperatur', 'gruppen'])
        if art == 'welche':
            a = R.randint(3, 9)
            nein = f'{a} · x = {a * R.randint(3, 9) + R.randint(1, a - 1)}'
            p = R.randint(10, 40)
            ja = [f'x + {p} = {p + R.randint(1, 30)}', f'{a} · x = {a * R.randint(2, 12)}', f'x − {R.randint(5, 20)} = {R.randint(1, 30)}']
            return A(R, 'Welche Gleichung hat keine Lösung in ℕ?', nein, ja,
                     f'{nein}: Die Zahl rechts ist nicht durch {a} teilbar. Die anderen Gleichungen lassen sich rückwärts in ℕ lösen.',
                     'Rechne jede Gleichung rückwärts. Wo kommt keine natürliche Zahl heraus?')
        if art == 'ganz':
            a = R.randint(6, 30)
            b = R.randint(0, a - 1)
            return Z(f'Löse x + {a} = {b} mit ganzen Zahlen.', b - a, f'{b} - {a}', f'Rückwärts: x = {b} − {a} = {zt(b - a)}. Probe: ({zt(b - a)}) + {a} = {b} ✓',
                     'Rechne rückwärts wie immer. Das Ergebnis darf negativ sein.')
        if art == 'temperatur':
            a, b = R.randint(5, 15), R.randint(1, 4)
            return Z(f'Bis mittags steigt die Temperatur um {a} Grad auf {b} °C. Wie warm war es morgens?', b - a, f'{b} - {a}',
                     f'x + {a} = {b}. Rückwärts: x = {b} − {a} = {zt(b - a)} °C. In ℕ gäbe es keine Lösung, mit ganzen Zahlen schon.',
                     'Stelle eine Gleichung auf. Die Lösung darf unter null liegen.', einheit='°C')
        g = R.randint(3, 6)
        n = g * R.randint(4, 8) + R.randint(1, g - 1)
        return A(R, f'{n} Kinder sollen in Gruppen zu je {g} Kindern eingeteilt werden, ohne dass jemand übrig bleibt: {g} · x = {n}. Geht das?',
                 f'Nein: {n} ist nicht durch {g} teilbar.', [f'Ja: Es gibt {n // g} Gruppen.', f'Ja: Es gibt {n // g + 1} Gruppen.'],
                 f'{g} · {n // g} = {g * (n // g)}, dann {"bleibt 1 Kind" if n % g == 1 else f"bleiben {n % g} Kinder"} übrig. Die Gleichung hat keine Lösung in ℕ.',
                 f'Ist {n} in der {g}er-Reihe?')
    art = R.choice(['null', 'kleinste', 'naechste'])
    if art == 'null':
        c = R.choice([0, R.randint(1, 20)])
        if c == 0:
            return A(R, '0 · x = 0. Wie viele Lösungen hat diese Gleichung?', 'Jede Zahl ist eine Lösung.', ['Keine Lösung.', 'Genau eine: x = 0.', 'Genau eine: x = 1.'],
                     '0 mal irgendeine Zahl ist immer 0. Also passt jede Zahl für x.', 'Probiere ein paar Zahlen für x aus.')
        return A(R, f'0 · x = {c}. Wie viele Lösungen hat diese Gleichung?', 'Keine Lösung.', ['Jede Zahl ist eine Lösung.', f'Genau eine: x = {c}.', 'Genau eine: x = 0.'],
                 f'0 mal irgendeine Zahl ist immer 0, nie {c}. Also gibt es keine Lösung.', 'Probiere ein paar Zahlen für x aus.')
    if art == 'kleinste':
        a = R.randint(5, 50)
        return Z(f'Für welche kleinste natürliche Zahl b hat x + {a} = b eine Lösung in ℕ?', a, f'{a}',
                 f'Die kleinste natürliche Zahl ist x = 0. Dann ist b = 0 + {a} = {a}. Für kleinere b müsste x negativ sein.',
                 'Welches ist die kleinste natürliche Zahl, die du für x einsetzen kannst?')
    a = R.randint(3, 9)
    b = a * R.randint(3, 9) + R.randint(1, a - 1)
    nb = (b // a + 1) * a
    return Z(f'{a} · x = {b} hat keine Lösung in ℕ. Welche ist die nächstgrößere Zahl statt {b}, für die es eine Lösung gibt?', nb, f'({b} // {a} + 1) * {a}',
             f'Gesucht ist die nächste Zahl der {a}er-Reihe nach {b}: {nb}. Dann ist x = {nb // a}.', f'Zähle die {a}er-Reihe weiter.')


GEN = {'waage': g_waage, 'umkehr_plus': g_umkehr_plus, 'umkehr_mal': g_umkehr_mal, 'zwei_schritte': g_zwei_schritte,
       'probe': g_probe, 'aufstellen': g_aufstellen, 'ohne_loesung': g_ohne_loesung}

TEIL = {'waage': 'verstehen', 'umkehr_plus': 'umkehren', 'umkehr_mal': 'umkehren', 'zwei_schritte': 'umkehren',
        'probe': 'verstehen', 'aufstellen': 'anwenden', 'ohne_loesung': 'loesbarkeit',
        '_texte': [('verstehen', 'Gleichungen als Waage verstehen, Lösungen durch die Probe prüfen'),
                   ('umkehren', 'Gleichungen durch Umkehraufgaben lösen'),
                   ('anwenden', 'Textaufgaben als Gleichung aufstellen und lösen'),
                   ('loesbarkeit', 'Erkennen, ob eine Gleichung in ℕ lösbar ist')]}

# Umbau U5 (Achte Runde, Vorgabe 16.11.): Lernkarten nach dem neuen Muster – einstieg, woerter (≤ 3), Kartenbild,
# Bildergeschichte (schritte mit bild), „Pass auf!“ (fehler + fehler_bild), MERKE (regel).
# Situationen: Balkenwaage mit Murmeln, Geldbeutel, Hefte, Kino, Sammelkarten, Aufzug.
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl5.py, mit_umbau) – die Aufgaben bleiben wörtlich gleich.
from _nachbau import waage as waage_bild  # noqa: E402
from _umbau_kl5 import mit_umbau  # noqa: E402

# Gekippte Waage (links schwerer): für den Fehler „nur auf einer Seite wegnehmen“
KIPPT = {'punkte': {'_A': [1.5, 1.5], '_B': [8.5, 2.5], '_S': [5, 2], '_F1': [4, 0], '_F2': [6, 0], '_L1': [-0.5, 2.1], '_L2': [3.5, 2.1],
                    '_R1': [6.5, 3.1], '_R2': [10.5, 3.1], '_LA': [1.5, 2.1], '_RA': [8.5, 3.1]},
         'linien': [['_A', '_B'], ['_A', '_LA'], ['_B', '_RA'], ['_L1', '_L2', '10 + 3'], ['_R1', '_R2', '10']], 'label': 'Waage kippt nach links: links 13, rechts 10'}
KETTE = lambda zv, sr, zr: {'zeilen': [['vorwärts', 'x', '· 3', zv, '+ 4', '19'], ['rückwärts', sr, ': 3', zr, '− 4', '19']]}

KARTEN = {
 'waage': {
  'einstieg': 'Auf einer Waage liegen links eine Dose und 3 Murmeln, rechts 10 Murmeln. Die Waage hängt gerade. Kurz geschrieben: x + 3 = 10, eine ⟦Gleichung⟧.',
  'woerter': [['x', 'die unbekannte Zahl, hier die Murmeln in der Dose'], ['Gleichgewicht', 'beide Seiten sind gleich schwer, die Waage hängt gerade'],
              ['Lösung', 'die Zahl für x, bei der beide Seiten gleich sind']],
  'bild': waage_bild('x + 3', '10'),
  'schritte': [{'text': 'Nimm auf beiden Seiten 3 Murmeln weg. Das Gleichgewicht bleibt.', 'bild': waage_bild('x', '10 − 3')},
               {'text': 'Links bleibt die Dose, rechts bleiben 10 − 3 = 7 Murmeln.', 'bild': waage_bild('x', '7')},
               {'text': 'Also ist die Lösung ⟦x = 7⟧: In der Dose sind 7 Murmeln.'}],
  'fehler': 'Nur links 3 wegnehmen ergibt x = 10. Aber 10 + 3 = 13, nicht 10: Die Waage kippt.',
  'fehler_bild': KIPPT,
  'regel': 'Tu auf ⟦beiden Seiten⟧ dasselbe. Dann bleibt die Waage im Gleichgewicht.'},
 'umkehr_plus': {
  'einstieg': 'In deinem Geldbeutel war Geld. Du kaufst etwas für 15 € und hast noch 27 €. Rückwärts kommen die 15 € wieder hinein: Das ist die ⟦Umkehrung⟧.',
  'woerter': [['Umkehrung', 'eine Rechnung, die eine andere rückgängig macht'], ['x', 'die gesuchte Zahl, hier das Geld vorher']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 50, 'abschnitte': 10, 'beschriftet': 'alle'},
  'schritte': [{'text': 'Als Gleichung: x − 15 = 27. Nachher sind 27 € übrig.', 'bild': {'punkte': [{'wert': 27, 'name': 'nachher'}]}},
               {'text': 'Die Umkehrung von minus ist plus: von 27 aus 15 nach rechts.', 'bild': {'boegen': [{'von': 27, 'bis': 42, 'name': '+15'}]}},
               {'text': '27 + 15 = ⟦42⟧. Vorher waren 42 € im Geldbeutel.', 'bild': {'punkte': [{'wert': 27, 'name': 'nachher'}, {'wert': 42, 'name': 'vorher'}]}}],
  'fehler': 'x − 15 = 27 mit 27 − 15 = 12 lösen ist falsch. Wer etwas ausgegeben hat, hatte vorher mehr Geld.',
  'fehler_bild': {'punkte': [{'wert': 27, 'name': 'nachher'}], 'boegen': [{'von': 27, 'bis': 12, 'name': 'falsche Richtung'}]},
  'regel': 'Die ⟦Umkehrung⟧ von plus ist minus, von minus ist plus. Bei x − 15 = 27 ist x = 27 + 15.'},
 'umkehr_mal': {
  'einstieg': '4 gleich teure Hefte kosten zusammen 12 €. Was kostet ein Heft? Du verteilst die 12 € auf 4 Hefte: Teilen ist die ⟦Umkehrung⟧ von Malnehmen.',
  'woerter': [['4 · x', '4-mal der Preis eines Hefts'], ['Umkehrung', 'eine Rechnung, die eine andere rückgängig macht']],
  'bild': {'typ': 'bruchstreifen', 'teile': 4, 'gefaerbt': 0, 'ganzes': '12 € für 4 Hefte'},
  'schritte': [{'text': 'Als Gleichung: 4 · x = 12.'},
               {'text': 'Die Umkehrung von mal ist geteilt: 12 € in 4 gleiche Teile.', 'bild': {'gefaerbt': 1}},
               {'text': '12 : 4 = ⟦3⟧. Ein Heft kostet 3 €.', 'bild': {'teil_text': '3 €'}}],
  'fehler': 'Bei x : 4 = 12 rechnen viele 12 : 4 = 3. Doch jedes von 4 Kindern bekam 12 €: Vorher waren es 48 €.',
  'fehler_bild': {'gefaerbt': 1, 'teil_text': '12 €', 'ganzes': 'vorher: 4 · 12 € = 48 €'},
  'regel': 'Die ⟦Umkehrung⟧ von mal ist geteilt, von geteilt ist mal. Bei x : 4 = 12 ist x = 12 · 4.'},
 'zwei_schritte': {
  'einstieg': '3 Kinokarten und ein Popcorn für 4 € kosten 19 €. Gerechnet wurde erst mal 3, dann plus 4. Rückwärts baust du die ⟦Rechenkette⟧ von hinten ab.',
  'woerter': [['Rechenkette', 'mehrere Rechenschritte hintereinander']],
  'bild': {'typ': 'tabelle', 'kopf': ['', 'Start', '1. Schritt', 'Zwischenwert', '2. Schritt', 'Ende'], **KETTE('?', '?', '?')},
  'schritte': [{'text': '3 · x + 4 = 19: vorwärts erst mal 3, dann plus 4.'},
               {'text': 'Den letzten Schritt zuerst umkehren: 19 − 4 = 15.', 'bild': KETTE('?', '?', '15')},
               {'text': 'Dann den ersten: 15 : 3 = ⟦5⟧. Eine Karte kostet 5 €.', 'bild': KETTE('15', '5', '15')}],
  'fehler': 'Bei 2 · x + 6 = 20 erst teilen: 10 − 6 = 4. Probe: 2 · 4 + 6 = 14, nicht 20.',
  'regel': 'Kehre den ⟦letzten Schritt zuerst⟧ um. Bei 3 · x + 4 = 19: erst − 4, dann : 3.'},
 'probe': {
  'einstieg': 'Deine Freundin ruft: „x = 7!“ Stimmt das? Du setzt die 7 in die Gleichung ein und schaust, ob die Waage gerade hängt. Das heißt ⟦Probe⟧.',
  'woerter': [['einsetzen', 'statt x die Zahl hinschreiben'], ['Probe', 'Kontrolle: Lösung einsetzen und beide Seiten vergleichen']],
  'bild': waage_bild('5 · x − 8', '27'),
  'schritte': [{'text': 'Die Gleichung: 5 · x − 8 = 27. Behauptet wird x = 7.'},
               {'text': 'Einsetzen: 7 für x, also 5 · 7 − 8.', 'bild': waage_bild('5 · 7 − 8', '27')},
               {'text': 'Links: 35 − 8 = 27. Rechts steht auch 27.', 'bild': waage_bild('27', '27')},
               {'text': 'Beide Seiten sind gleich: Die Lösung ⟦stimmt⟧.'}],
  'fehler': 'Die Probe mit der eigenen Rechnung statt mit der Gleichung machen. So findest du deinen Fehler nie.',
  'regel': 'Setze die Lösung in die ⟦Gleichung⟧ ein. Sind beide Seiten gleich, stimmt sie.'},
 'aufstellen': {
  'einstieg': 'Sammelkarten und ein Album für 2 € kosten zusammen 9 €. Was kosten die Karten? Erst übersetzt du den Text in eine ⟦Gleichung⟧.',
  'woerter': [['aufstellen', 'einen Text in eine Gleichung übersetzen']],
  'bild': waage_bild('?', '?'),
  'schritte': [{'text': 'Nenne die gesuchte Zahl x: den Preis der Karten.', 'bild': waage_bild('x', '?')},
               {'text': '„Zusammen kosten“ heißt =. Gleichung aufstellen: x + 2 = 9.', 'bild': waage_bild('x + 2', '9')},
               {'text': 'Rückwärts: 9 − 2 = ⟦7⟧. Die Karten kosten 7 €.', 'bild': waage_bild('x', '7')}],
  'fehler': '„Das Doppelte, vermindert um 4“ heißt 2 · x − 4. Falsch ist 2 · (x − 4): Erst wird verdoppelt, dann abgezogen.',
  'regel': 'Gesuchte Zahl ⟦x⟧ nennen und Stück für Stück übersetzen. „Das Dreifache“ ist 3 · x, „ergibt“ ist =.'},
 'ohne_loesung': {
  'einstieg': 'Ein Aufzug fährt 9 Stockwerke nach oben und hält im vierten Stock. Wo ist er losgefahren? Mit 0, 1, 2, 3 … allein gibt es ⟦keine Lösung⟧.',
  'woerter': [['ℕ', 'die natürlichen Zahlen 0, 1, 2, 3 …'], ['ganze Zahlen', 'auch die negativen: … −2, −1, 0, 1, 2 …']],
  'bild': {'typ': 'zahlenstrahl', 'start': -6, 'ende': 6, 'abschnitte': 12, 'beschriftet': 'anfang_ende', 'punkte': [{'wert': 4, 'name': 'Ziel'}]},
  'schritte': [{'text': 'Die Gleichung: x + 9 = 4. Rückwärts: x = 4 − 9.'},
               {'text': 'Von 4 aus 9 nach unten: Unter 0 gibt es in ℕ keine Zahl.',
                'bild': {'boegen': [{'von': 4, 'bis': -5, 'name': '−9'}], 'bereich': {'von': -6, 'bis': 0}}},
               {'text': 'Ganze Zahlen helfen: ⟦x = −5⟧, das 5. Untergeschoss.', 'bild': {'punkte': [{'wert': 4, 'name': 'Ziel'}, {'wert': -5, 'name': 'Start'}]}}],
  'fehler': 'Bei x + 9 = 4 die Zahlen tauschen: 9 − 4 = 5. Probe: 5 + 9 = 14, nicht 4.',
  'regel': 'In ℕ gibt es keine Lösung, wenn rückwärts etwas ⟦unter 0⟧ herauskommt. Ebenso, wenn Teilen nicht ohne Rest aufgeht.'},
}
baue = mit_umbau(baue, KARTEN)


# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl5) ----------
# Neue Übungen nach Prüfungsvorbild (Jahrgangsstufentest 6 Bayern: 3 · (□ − 15) = 18, −23 + x = −12, □ : □ = −70; Mathematik-Test 2005:
# 5 · 3 + 4 · x = 35; Bayerischer Mathematik-Test 2004: Zahl von 1 000 subtrahieren; Känguru 5/6: 23 Kinder in 7 Zimmern). Eigene Zahlen.
# Hier läuft baue() erst unter __main__; darum wird baue umhüllt: erst alles wie bisher erzeugen, dann die neuen Übungen anhängen.
# Die Helfer werden als Modul _S eingebunden, damit die Namen A und Z aus _nachbau (von den alten Generatoren benutzt) unverändert bleiben.
import _schwer_kl5 as _S  # noqa: E402
from _nachbau import THEMEN as _THEMEN  # noqa: E402


def _schwer():
    Z, A, L, wahl, einzig = _S.Z, _S.A, _S.L, _S.wahl, _S.einzig
    N = {}
    N['waage'] = [
        Z(2, 'Die Waage ist im Gleichgewicht: links x + x + 6, rechts 20. Welche Zahl ist x?', '(20 - 6) / 2', 'Auf beiden Seiten 6 wegnehmen: x + x = 14. Also x = 7.',
          'Nimm zuerst auf beiden Seiten 6 weg.'),
        Z(2, 'Links liegen 3 gleiche Dosen, rechts 1 solche Dose und 12 Murmeln. Die Waage ist im Gleichgewicht. Wie viele Murmeln sind in einer Dose?', '12 / 2',
          'Auf beiden Seiten 1 Dose wegnehmen: 2 Dosen = 12 Murmeln. Eine Dose: 6 Murmeln.', 'Nimm auf beiden Seiten dieselbe Dose weg.'),
        Z(3, 'Löse 4 · 3 + 5 · x = 47.', '(47 - 4 * 3) / 5', '4 · 3 = 12. 12 + 5 · x = 47, also 5 · x = 35 und x = 7. Probe: 12 + 35 = 47.',
          'Rechne zuerst 4 · 3 aus. Was bleibt für 5 · x?'),
        Z(3, 'Auf einer Waage gilt: 2 Äpfel wiegen so viel wie 3 Birnen. Eine Birne wiegt 120 g. Wie viel wiegt ein Apfel?', '3 * 120 / 2',
          '3 Birnen: 360 g. Das wiegen auch 2 Äpfel. Ein Apfel: 360 g : 2 = 180 g.', 'Was wiegen 3 Birnen zusammen?', einheit='g'),
        Z(3, 'Eine Waage ist im Gleichgewicht: links 5 gleiche Würfel, rechts 2 solche Würfel und ein 60-g-Gewicht. Wie schwer ist ein Würfel?', '60 / 3',
          'Auf beiden Seiten 2 Würfel wegnehmen: 3 Würfel = 60 g. Ein Würfel: 20 g.', 'Nimm auf beiden Seiten gleich viele Würfel weg.', einheit='g'),
        A(3, 'Bei x + 7 = 15 nimmt jemand nur links 7 weg und schreibt x = 15. Was ist falsch?', 'Die 7 muss auch rechts weg: x = 15 − 7 = 8.',
          ['Nichts, x = 15 stimmt.', 'Man muss rechts 7 dazulegen: x = 22.', 'Man muss durch 7 teilen.'],
          'Nur links wegnehmen bringt die Waage aus dem Gleichgewicht. Beide Seiten minus 7: x = 8. Probe: 8 + 7 = 15.', 'Was passiert mit der Waage, wenn nur eine Seite leichter wird?'),
    ]
    N['umkehr_plus'] = [
        Z(2, 'Löse 63 = x − 28.', '63 + 28', 'Umkehrung von minus ist plus: x = 63 + 28 = 91. Probe: 91 − 28 = 63.', 'Es ist egal, auf welcher Seite x steht.'),
        Z(2, 'Löse 250 − x = 175.', '250 - 175', 'Von 250 muss man so viel abziehen, dass 175 bleibt: x = 250 − 175 = 75.', 'Achtung: x wird abgezogen. Wie groß ist der Unterschied zwischen 250 und 175?'),
        Z(3, 'Löse −23 + x = −12.', '-12 - (-23)', 'Umkehrung: x = −12 − (−23) = −12 + 23 = 11. Probe: −23 + 11 = −12.', 'Von −23 bis −12: wie viele Schritte nach rechts?'),
        Z(3, 'Welche Zahl muss man von 1 000 subtrahieren, um 2 026 zu erhalten?', '1000 - 2026',
          '1 000 − x = 2 026. Das Ergebnis ist größer, also ist x negativ: x = 1 000 − 2 026 = −1 026. Probe: 1 000 − (−1 026) = 2 026.',
          'Schreibe die Gleichung 1 000 − x = 2 026 auf. Was muss x sein, damit das Ergebnis größer wird?'),
        Z(3, 'Ich denke mir eine Zahl, ziehe 45 ab und addiere dann 17. Ich erhalte 30. Welche Zahl habe ich mir gedacht?', '30 - 17 + 45',
          'Rückwärts: 30 − 17 = 13, dann 13 + 45 = 58. Probe: 58 − 45 + 17 = 30.', 'Kehre den letzten Schritt zuerst um.'),
        A(3, 'Jemand löst x − 15 = 40 so: x = 40 − 15 = 25. Was ist falsch?', 'Die Umkehrung von minus ist plus: x = 40 + 15 = 55.',
          ['Nichts, x = 25 stimmt.', 'Richtig ist x = 15 − 40.', 'Richtig ist x = 40 : 15.'], 'Probe mit 25: 25 − 15 = 10, nicht 40. Mit 55: 55 − 15 = 40.', 'Mach die Probe mit x = 25.'),
    ]
    N['umkehr_mal'] = [
        Z(2, 'Löse 7 · x = 0.', '0 / 7', 'Ein Produkt ist 0, wenn ein Faktor 0 ist: x = 0 : 7 = 0. Probe: 7 · 0 = 0.', 'Welche Zahl mal 7 ergibt 0?'),
        Z(2, 'Löse x : 12 = 15.', '15 * 12', 'Umkehrung von geteilt ist mal: x = 15 · 12 = 180.', 'Rückwärts mit Malnehmen.'),
        Z(3, 'Löse x : (−4) = 15.', '15 * (-4)', 'Umkehrung: x = 15 · (−4) = −60. Probe: (−60) : (−4) = 15.', 'Rechne rückwärts mit Malnehmen. Achte auf das Vorzeichen.'),
        A(3, 'Jemand löst 96 : x = 8 mit x = 96 · 8 = 768. Was ist falsch?', 'x ist der Teiler: x = 96 : 8 = 12.',
          ['Nichts, x = 768 stimmt.', 'Richtig ist x = 8 : 96.', 'Richtig ist x = 96 − 8 = 88.'], 'Probe: 96 : 768 ist nicht 8. Richtig: 96 : 12 = 8.',
          'Mach die Probe. Durch welche Zahl muss man 96 teilen, damit 8 herauskommt?'),
        Z(3, 'Das Fünffache einer Zahl ist um 48 größer als die Zahl selbst. Wie heißt die Zahl?', str(einzig([x for x in range(1, 100) if 5 * x - x == 48])),
          '5 · x − x = 4 · x. Also 4 · x = 48 und x = 12. Probe: 60 ist um 48 größer als 12.', 'Wie viel mal die Zahl ist der Unterschied?'),
        Z(3, 'Ein Seil wird ohne Rest in 12 gleich lange Stücke von 35 cm geschnitten. Wie lang war das Seil in m?', '12 * 35 / 100',
          'Gleichung: x : 35 = 12, also x = 12 · 35 = 420 cm = 4,2 m.', 'Rechne zuerst in cm, dann in m.', einheit='m'),
    ]
    N['zwei_schritte'] = [
        Z(2, 'Löse 7 · x − 12 = 51.', '(51 + 12) / 7', 'Erst + 12: 7 · x = 63. Dann : 7: x = 9.', 'Den letzten Schritt (− 12) zuerst umkehren.'),
        Z(2, 'Löse x : 5 − 3 = 9.', '(9 + 3) * 5', 'Erst + 3: x : 5 = 12. Dann · 5: x = 60.', 'Den letzten Schritt zuerst umkehren.'),
        L(3, 'Ergänze die Lücke: 6 · (□ − 12) = 42', '6 · (□ − 12) = 42', 'Trage die fehlende Zahl ein.', ['42 // 6 + 12'],
          'Die Klammer muss 42 : 6 = 7 ergeben. □ − 12 = 7, also □ = 19. Probe: 6 · 7 = 42.', 'Was muss in der Klammer herauskommen?'),
        Z(3, 'Löse (x + 7) : 3 = 11.', '11 * 3 - 7', 'Erst · 3: x + 7 = 33. Dann − 7: x = 26. Probe: 33 : 3 = 11.', 'Die Klammer wird zuletzt geteilt – kehre das zuerst um.'),
        Z(3, 'Ich denke mir eine Zahl, verdopple sie, addiere 9 und teile das Ergebnis durch 5. Ich erhalte 7. Welche Zahl habe ich mir gedacht?', '(7 * 5 - 9) / 2',
          'Rückwärts: 7 · 5 = 35, 35 − 9 = 26, 26 : 2 = 13. Probe: 13 · 2 + 9 = 35, 35 : 5 = 7.', 'Drei Schritte rückwärts: den letzten zuerst.'),
        A(3, 'Jemand löst 4 · x + 8 = 40 so: zuerst 40 : 4 = 10, dann 10 − 8 = 2. Was ist falsch?', 'Die Reihenfolge: zuerst − 8 (letzter Schritt), dann : 4. Richtig ist x = 8.',
          ['Nichts, x = 2 stimmt.', 'Man muss 40 · 4 rechnen.', 'Richtig ist x = 40 − 8 − 4 = 28.'], 'Probe mit 2: 4 · 2 + 8 = 16. Richtig: 40 − 8 = 32, 32 : 4 = 8.',
          'Mach die Probe mit x = 2.'),
    ]
    welche = [x for x in (3, 4, 5, 6) if 2 * x + 7 == 4 * x - 3]
    N['probe'] = [
        wahl(2, 'Ist x = 7 eine Lösung von 3 · (x − 2) = 15?', ['Ja: 3 · (7 − 2) = 3 · 5 = 15.', 'Nein: 3 · 7 − 2 = 19.', 'Nein: 3 · (7 − 2) = 21.'],
             lambda o: o.startswith('Ja') and 3 * (7 - 2) == 15, 'Einsetzen: 3 · (7 − 2) = 3 · 5 = 15. Beide Seiten sind gleich.', 'Rechne zuerst die Klammer aus.'),
        Z(2, 'Mache die Probe für x = 4 bei 50 − 6 · x = 26. Welche Zahl kommt links heraus?', '50 - 6 * 4', '50 − 6 · 4 = 50 − 24 = 26. Links steht auch 26: Die Lösung stimmt.',
          'Punkt vor Strich.'),
        Z(3, 'Für welche der Zahlen 3, 4, 5 und 6 gilt 2 · x + 7 = 4 · x − 3?', str(_S.einzig(welche)),
          'Probe mit 5: links 2 · 5 + 7 = 17, rechts 4 · 5 − 3 = 17. Gleich! (Bei 3, 4, 6 sind die Seiten verschieden.)', 'Setze jede Zahl links und rechts ein.'),
        wahl(3, 'Zwei Kinder lösen 5 · x − 20 = 30. Eins erhält x = 2, das andere x = 10. Wer hat recht?', ['Das Kind mit x = 10.', 'Das Kind mit x = 2.', 'Beide.', 'Keins von beiden.'],
             lambda o: o == 'Das Kind mit x = 10.' and 5 * 10 - 20 == 30, 'Probe: 5 · 10 − 20 = 30 stimmt. 5 · 2 − 20 = −10 stimmt nicht.', 'Mach mit beiden Zahlen die Probe.'),
        Z(3, 'Bei 7 · x − 4 = 59 wird x = 10 getestet. Links kommt 66 heraus – zu viel. Wie heißt die richtige Lösung?', '(59 + 4) / 7',
          '66 ist 7 zu viel, also ist x um 1 zu groß: x = 9. Probe: 63 − 4 = 59.', 'Um wie viel ändert sich die linke Seite, wenn x um 1 kleiner wird?'),
        Z(3, 'Bei 4 · x + 1 = 33 wird x = 7 getestet. Links kommt 29 heraus. Um wie viel muss x noch größer werden?', '(33 - 1) / 4 - 7',
          'Es fehlen 33 − 29 = 4. Jede 1 bei x bringt links 4 mehr. Also x um 1 größer: x = 8.', 'Um wie viel wächst die linke Seite, wenn x um 1 größer wird?'),
    ]
    zimmer = _S.einzig([v for v in range(0, 9) if 4 * v + 3 * (8 - v) == 26])
    N['aufstellen'] = [
        Z(2, 'Ein Kind ist 4 Jahre älter als sein Bruder. Zusammen sind sie 22 Jahre alt. Wie alt ist der Bruder?', '(22 - 4) / 2',
          'x + (x + 4) = 22, also 2 · x = 18 und x = 9. Der Bruder ist 9, das Kind 13.', 'Nimm zuerst die 4 Jahre Unterschied weg.', einheit='Jahre'),
        wahl(2, '„Die Hälfte einer Zahl, vermehrt um 8, ergibt 20.“ Welche Gleichung passt?', ['x : 2 + 8 = 20', '(x + 8) : 2 = 20', 'x · 2 + 8 = 20', 'x : 2 − 8 = 20'],
             lambda o: o == 'x : 2 + 8 = 20', 'Erst die Hälfte (x : 2), dann vermehrt um 8 (+ 8): x : 2 + 8 = 20.', 'Was passiert zuerst mit der Zahl?'),
        Z(3, '26 Kinder schlafen in 8 Zimmern. In jedem Zimmer schlafen 3 oder 4 Kinder. Wie viele Viererzimmer gibt es?', str(zimmer),
          'Wären alle 8 Zimmer Dreierzimmer, schliefen dort 24 Kinder. 2 Kinder fehlen – jedes Viererzimmer bringt 1 mehr: 2 Viererzimmer. Probe: 2 · 4 + 6 · 3 = 26.',
          'Stell dir zuerst vor, alle Zimmer wären Dreierzimmer.'),
        Z(3, 'Subtrahiert man von 100 das Dreifache einer Zahl, erhält man 37. Wie heißt die Zahl?', '(100 - 37) / 3',
          '100 − 3 · x = 37. Also 3 · x = 63 und x = 21. Probe: 100 − 63 = 37.', 'Schreibe die Gleichung auf: 100 − 3 · x = 37.'),
        Z(3, 'Drei aufeinanderfolgende natürliche Zahlen haben die Summe 72. Wie heißt die kleinste?', str(_S.einzig([n for n in range(1, 100) if n + (n + 1) + (n + 2) == 72])),
          'x + (x + 1) + (x + 2) = 72, also 3 · x + 3 = 72, 3 · x = 69, x = 23. Probe: 23 + 24 + 25 = 72.', 'Die mittlere Zahl ist ein Drittel der Summe.'),
        Z(3, 'Ein Vater ist heute 40 Jahre alt, sein Sohn 10. In wie vielen Jahren ist der Vater doppelt so alt wie der Sohn?', str(_S.einzig([t for t in range(0, 60) if 40 + t == 2 * (10 + t)])),
          '40 + t = 2 · (10 + t). Probieren: In 20 Jahren ist der Vater 60, der Sohn 30 – doppelt so alt.', 'Der Altersunterschied bleibt immer 30 Jahre.', einheit='Jahre'),
    ]
    vier = {'30': 30, '31': 31, '32': 32, '33': 33}
    N['ohne_loesung'] = [
        wahl(2, 'Welche Gleichung hat eine Lösung in ℕ?', ['7 · x = 50', 'x + 12 = 5', '7 · x = 56', '20 − x = 25'], lambda o: o == '7 · x = 56',
             '7 · 8 = 56. Bei 50 bleibt beim Teilen ein Rest, bei den anderen müsste x negativ sein.', 'Prüfe jede Gleichung mit Rückwärtsrechnen.'),
        Z(2, 'Löse mit ganzen Zahlen: x + 12 = 5.', '5 - 12', 'x = 5 − 12 = −7. Probe: −7 + 12 = 5. In ℕ gäbe es keine Lösung.', 'Rechne rückwärts – das Ergebnis darf negativ sein.'),
        Z(3, 'Ein 368 cm langes Band soll in Stücke von 15 cm geschnitten werden. Ohne Rest geht das nicht (15 · x = 368 hat keine Lösung in ℕ). Wie viele cm bleiben übrig, wenn man möglichst viele Stücke schneidet?',
          '368 % 15', '368 : 15 = 24 Rest 8. Es bleiben 8 cm übrig.', 'Teile mit Rest.', einheit='cm'),
        wahl(3, 'Für welche Zahl rechts hat 4 · x = □ eine Lösung in ℕ?', list(vier), lambda o: vier[o] % 4 == 0,
             'Nur 32 ist durch 4 teilbar: x = 8. 30, 31 und 33 lassen beim Teilen durch 4 einen Rest.', 'Welche Zahl ist durch 4 teilbar?'),
        Z(3, 'Wie viele der Gleichungen 6 · x = 1, 6 · x = 2, 6 · x = 3, … , 6 · x = 50 haben eine Lösung in ℕ?', str(sum(1 for n in range(1, 51) if n % 6 == 0)),
          'Eine Lösung gibt es, wenn rechts ein Vielfaches von 6 steht: 6, 12, 18, 24, 30, 36, 42, 48. Das sind 8.', 'Welche Zahlen bis 50 sind durch 6 teilbar?'),
        wahl(3, 'Welche Gleichung hat jede Zahl als Lösung?', ['0 · x = 0', '0 · x = 5', 'x + 0 = 5', '1 · x = 0'], lambda o: o == '0 · x = 0',
             '0 mal jede Zahl ist 0. Also stimmt 0 · x = 0 für jedes x. 0 · x = 5 hat keine Lösung, die anderen genau eine.', 'Setze verschiedene Zahlen ein.'),
    ]
    return N


def _mit_schwer(baue_alt):
    def baue_neu(meta, *args, **kwargs):
        d = baue_alt(meta, *args, **kwargs)
        _S.ergaenze(d, _schwer(), 1001)
        (_THEMEN / f"{meta['thema_schluessel']}.json").write_text(_S.json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(f"  + Zehnte Runde: jetzt {len(d['aufgaben'])} Aufgaben")
        return d
    return baue_neu


baue = _mit_schwer(baue)

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, mit_befunden  # noqa: E402

BF = Befunde('gleichungen.einfach', 13_5_12)
# a) „Zahl : x“ mit Ergebnis im Kopf sofort sichtbar → Stufe 2
BF.stufe('umkehr_mal', 'Löse 9 : x = 3.', 2)
BF.stufe('umkehr_mal', 'Löse 20 : x = 2.', 2)
# c) fünfmal „größer oder kleiner?“ (Antwort erratbar) → zwei davon mit anderem Gedanken
BF.ersetze('probe', 'Bei 3 · x + 5 = 38 wird x = 12 getestet. Links kommt 41 heraus. Ist die Lösung größer oder kleiner als 12?', BF.Z(
    'Bei 3 · x + 5 = 38 ergibt die Probe mit x = 12 links 41 und mit x = 10 links 35. Die Lösung ist eine ganze Zahl. Welche?', 11, '(38 - 5) / 3',
    '41 ist zu viel, 35 zu wenig – die Lösung liegt zwischen 10 und 12. Probe mit 11: 3 · 11 + 5 = 38. Also x = 11.',
    'Mit 12 ist links zu viel, mit 10 zu wenig. Welche Zahl liegt dazwischen? Mach die Probe.'))
BF.ersetze('probe', 'Bei 5 · x + 9 = 29 wird x = 3 getestet. Links kommt 24 heraus. Ist die Lösung größer oder kleiner als 3?', BF.A(
    'Welche der Zahlen 2, 4, 6 und 8 löst die Gleichung 5 · x + 9 = 29? Entscheide mit der Probe.', '4', ['2', '6', '8'],
    'Probe: 5 · 2 + 9 = 19, 5 · 4 + 9 = 29 ✓, 5 · 6 + 9 = 39, 5 · 8 + 9 = 49. Nur x = 4 passt.',
    'Setze jede Zahl für x ein und rechne die linke Seite aus.'))
# c) zweimal dieselbe Alters-Aufgabe → anderer Aufbau
BF.ersetze('aufstellen', 'Eine Mutter ist 3-mal so alt wie ihre Tochter. Zusammen sind sie 36 Jahre alt. Wie alt ist die Tochter?', BF.Z(
    'Ein Vater ist 28 Jahre älter als sein Sohn. Zusammen sind sie 46 Jahre alt. Wie alt ist der Sohn?', 9, '(46 - 28) / 2',
    'Sohn x, Vater x + 28. Zusammen: x + x + 28 = 46, also 2 · x = 18 und x = 9 Jahre. Probe: 9 + 37 = 46.',
    'Nimm die 28 Jahre Unterschied weg. Der Rest verteilt sich auf zwei gleich große Alter.', einheit='Jahre'))
# c) zweimal derselbe Gedanke (0 · x = Zahl ≠ 0) → umgekehrt gefragt
BF.ersetze('ohne_loesung', '0 · x = 14. Wie viele Lösungen hat diese Gleichung?', BF.Z(
    'Für welche Zahl a hat die Gleichung a · x = 7 keine Lösung?', 0, '0',
    'Für a = 0 steht da 0 · x = 7. 0 mal jede Zahl ist 0, nie 7: keine Lösung. Für jedes andere a gibt es x = 7 : a.',
    'Für welches a kommt links immer dasselbe heraus, egal was x ist?'))
BF.nicht_umgesetzt('probe S3 „Für welche der Zahlen 3, 4, 5, 6 gilt 2 · x + 7 = 4 · x − 3?“', 'Hinweis aus der Liste, kein Mangel: Die Aufgabe passt zur Lernkarte „Probe machen“.')

baue = mit_befunden(baue, BF)
# ---- BEFUNDE ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl5, siehe _durchsicht_kl5.py) ----
from _durchsicht_kl5 import Durchsicht, mit_durchsicht  # noqa: E402

DS = Durchsicht('gleichungen.einfach', 19_5_10)
# a) Stufe 3 mit derselben Gleichungsform wie Stufe 2 (a : x = b, a − x = b) → Stufe 2
for _lz, _t in [('umkehr_mal', 'Löse 72 : x = 9.'), ('umkehr_mal', 'Löse 110 : x = 11.'), ('umkehr_mal', 'Löse 40 : x = 10.'),
                ('umkehr_plus', 'Löse 131 − x = 57.'), ('umkehr_plus', 'Löse 127 − x = 10.')]:
    DS.stufe(_lz, _t, 2, enthaelt=lambda x: x['s'] == 3)
baue = mit_durchsicht(baue, DS)
# ---- DURCHSICHT ENDE ----
# ---- STUFEN (Zwanzigste Runde) ----
from _stufen_kl5 import stufen_anwenden  # noqa: E402
_baue_ds = baue


def baue(meta, *args, **kwargs):
    d = _baue_ds(meta, *args, **kwargs)
    stufen_anwenden(d, meta['thema_schluessel'])
    (_THEMEN_ST / f"{meta['thema_schluessel']}.json").write_text(_json_st.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return d


import json as _json_st  # noqa: E402
from _befunde import THEMEN as _THEMEN_ST  # noqa: E402
# ---- STUFEN ENDE ----

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Was ist eine Gleichung?', ['waage']), ('Rückwärts rechnen', ['umkehr_plus', 'umkehr_mal', 'zwei_schritte']),
          ('Prüfen und anwenden', ['probe', 'aufstellen']), ('Vertiefung', ['ohne_loesung'])],
         'Einfache Gleichungen mit dem Waage-Modell und durch Rückwärtsrechnen lösen, mit der Probe prüfen, aus Texten aufstellen und erkennen, wann es in ℕ keine Lösung gibt.',
         ['Eine Gleichung ist wie eine Waage im Gleichgewicht. Was du links tust, tust du auch rechts.',
          'Umkehrung: Plus ↔ Minus, Mal ↔ Geteilt.',
          'Bei zwei Schritten: den letzten Schritt zuerst umkehren.',
          'Probe: Lösung in die Gleichung einsetzen – links und rechts muss dasselbe stehen.'],
         offen=['Lehrplanbezug: Das Feld lehrplan_gym ist leer. Umgesetzt nach dem Feld „umfang“ (Umkehrrechnung, erste Äquivalenzumformung an der Waage, Sachzusammenhang); Klammern nur in der Form (x + b) · a, keine Variable auf beiden Seiten außer in der Waage-Anschauung (Stufe 3).',
                'Vertiefung ohne_loesung nutzt negative Zahlen (Thema zahlen.ganz, Kl. 5) für „Lösung in ℤ statt in ℕ“; sollte zeitlich nach zahlen.ganz kommen.',
                'Waage als Figur gezeichnet (Balken, Drehpunkt, zwei Schalen mit Beschriftung). Einzelne Gewichte/Dosen als Symbole kann die App nicht zeichnen; die Schalen tragen deshalb Terme wie „x + x + 3“.'],
         vertiefung=['ohne_loesung'], teil=TEIL)
