#!/usr/bin/env python3
"""Direkte Proportionalität und Dreisatz (Gymnasium Kl. 5): proportionale Zuordnungen erkennen, Tabellen ergänzen,
auf die Einheit schließen, Dreisatz, geschickte Zwischenschritte, Sachaufgaben mit Fallen.
Indirekte Proportionalität (Produktgleichheit) gehört zum Thema groessen.indirekt (Kl. 8)."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl5 import baue, mische, schreibe, zt  # noqa: E402

R = random.Random(26)

# (Ding Einzahl, Mehrzahl, Einheit vorn, Größe hinten, Einheit hinten, Preis je Stück wählbar)
WAREN = [('Heft', 'Hefte', '', 'kosten', '€', [1, 2, 3]), ('kg Äpfel', 'kg Äpfel', '', 'kosten', '€', [2, 3, 4]), ('Brötchen', 'Brötchen', '', 'kosten', 'ct', [30, 40, 45, 60]),
         ('Liter Farbe', 'Liter Farbe', '', 'reichen für', 'm²', [6, 8, 12]), ('Stunde', 'Stunden', '', 'fährt ein Radfahrer', 'km', [12, 15, 18]),
         ('Packung', 'Packungen', '', 'enthalten', 'Kekse', [12, 16, 24]), ('Minute', 'Minuten', '', 'laufen aus dem Hahn', 'Liter', [6, 8, 9]),
         ('Schritt', 'Schritte', '', 'sind', 'cm', [60, 65, 70, 75]), ('Karte', 'Eintrittskarten', '', 'kosten', '€', [7, 9, 12, 14])]


def satz(w, n, wert, frage=False):
    ding = w[0] if n == 1 else w[1]
    if w[3] == 'fährt ein Radfahrer': return f'In {n} {ding if n > 1 else "Stunde"} fährt ein Radfahrer {"wie viele" if frage else zt(wert)} km'
    if w[3] == 'laufen aus dem Hahn': return f'In {n} {ding} {"laufen" if frage or wert != 1 else "läuft"} {"wie viele" if frage else zt(wert)} Liter aus dem Hahn'
    verb = {'kosten': 'kostet' if n == 1 else 'kosten', 'reichen für': 'reicht für' if n == 1 else 'reichen für', 'enthalten': 'enthält' if n == 1 else 'enthalten', 'sind': 'ist' if n == 1 else 'sind'}[w[3]]
    return f'{n} {ding} {verb} {"wie viel" if frage and w[4] in ("€", "ct") else ("wie viele" if frage else zt(wert))} {w[4]}'


ETAPPEN = [
    {'lernziel': 'erkennen', 'titel': 'Was heißt proportional?',
     'regel': 'Eine Zuordnung ist ⟦proportional⟧, wenn gilt: doppelte Menge → doppelter Wert, dreifache Menge → dreifacher Wert, halbe Menge → halber Wert.',
     'schritte': ['1 Brötchen kostet 40 ct. 2 Brötchen kosten 80 ct, 3 Brötchen 120 ct.', 'Doppelt so viele Brötchen kosten doppelt so viel: Die Zuordnung ist ⟦proportional⟧.'],
     'fehler': '„Je mehr, desto mehr“ reicht nicht. Ein Kind wird älter und größer, aber mit 10 Jahren ist es nicht doppelt so groß wie mit 5. Es muss ⟦genau das Doppelte⟧ sein.'},
    {'lernziel': 'vervielfachen', 'titel': 'Verdoppeln, verdreifachen, halbieren',
     'regel': 'Bei proportionalen Zuordnungen machst du auf ⟦beiden Seiten dasselbe⟧: Menge mal 3 → Wert mal 3. Menge geteilt durch 2 → Wert geteilt durch 2.',
     'schritte': ['3 kg Äpfel kosten 6 €. Gesucht: 9 kg.', '9 kg sind 3-mal so viel wie 3 kg.', 'Also auch der Preis mal 3: 6 € · 3 = ⟦18 €⟧.'],
     'fehler': 'Auf beiden Seiten dieselbe Zahl ⟦addieren⟧: Von 3 kg auf 9 kg sind es +6 kg, aber der Preis steigt nicht um 6 €. Gerechnet wird mit ⟦mal und geteilt⟧.'},
    {'lernziel': 'einheit', 'titel': 'Auf die Einheit schließen',
     'regel': 'Teile durch die Anzahl, dann weißt du den Wert für ⟦1 Stück⟧ (für 1 kg, 1 Stunde …). Das nennt man: auf die Einheit schließen.',
     'schritte': ['5 Hefte kosten 10 €.', 'Beide Seiten geteilt durch 5: 1 Heft kostet 10 € : 5 = ⟦2 €⟧.'],
     'probe': '5 · 2 € = 10 € ✓',
     'fehler': 'Falsch herum teilen: 5 : 10 statt 10 : 5. Geteilt wird der ⟦Wert⟧ durch die ⟦Anzahl⟧.'},
    {'lernziel': 'dreisatz', 'titel': 'Der Dreisatz',
     'regel': 'Der Dreisatz hat ⟦drei Zeilen⟧: 1. Was du weißt. 2. Auf die Einheit schließen (geteilt). 3. Auf das Gesuchte schließen (mal).',
     'schritte': ['4 kg kosten 12 €.', '1 kg kostet 12 € : 4 = 3 €.', '7 kg kosten 3 € · 7 = ⟦21 €⟧.'],
     'probe': 'Überschlag: 7 kg ist etwas weniger als das Doppelte von 4 kg, 21 € etwas weniger als 24 € ✓',
     'fehler': 'Die mittlere Zeile überspringen und raten. Schreibe ⟦immer alle drei Zeilen⟧ auf, dann siehst du, was du teilen und malnehmen musst.'},
    {'lernziel': 'geschickt', 'titel': 'Geschickte Zwischenschritte',
     'regel': 'Du musst nicht immer auf 1 gehen. Suche eine Zwischenmenge, die ⟦in beiden Zahlen steckt⟧: von 6 auf 9 geht es bequem über 3.',
     'schritte': ['6 Karten kosten 42 €. Gesucht: 9 Karten.', '3 Karten kosten 42 € : 2 = 21 €.', '9 Karten kosten 21 € · 3 = ⟦63 €⟧.'],
     'probe': 'Über die Einheit: 1 Karte kostet 7 €, 9 Karten 63 € ✓',
     'fehler': 'Einen Zwischenschritt wählen, der nicht in beide Zahlen passt (z. B. von 6 über 4 auf 9). Der Zwischenschritt muss ein ⟦gemeinsamer Teiler⟧ sein.'},
    {'lernziel': 'pruefen', 'titel': 'Ist die Tabelle proportional?',
     'regel': 'In einer proportionalen Tabelle ist ⟦Wert geteilt durch Menge⟧ immer gleich. Dieser Quotient ist der Wert für 1 Stück.',
     'schritte': ['2 kg → 6 €, 5 kg → 15 €, 8 kg → 24 €.', '6 : 2 = 3, 15 : 5 = 3, 24 : 8 = 3.', 'Immer 3 € pro kg: Die Tabelle ist ⟦proportional⟧.'],
     'fehler': 'Nur das erste Paar prüfen. Erst wenn ⟦alle⟧ Quotienten gleich sind, ist die Zuordnung proportional.'},
    {'lernziel': 'sach', 'titel': 'Sachaufgaben mit Dreisatz',
     'regel': 'Prüfe zuerst: Ist die Zuordnung überhaupt ⟦proportional⟧? Erst dann rechnest du mit dem Dreisatz. Manche Aufgaben sind Fallen.',
     'schritte': ['Für 4 Personen braucht man 600 g Nudeln. Wie viel für 6 Personen?', 'Doppelt so viele Personen essen doppelt so viel: proportional.', '2 Personen: 300 g. 6 Personen: 300 g · 3 = ⟦900 g⟧.'],
     'fehler': '„1 Ei kocht 8 Minuten, also kochen 3 Eier 24 Minuten“: falsch. Die Kochzeit hängt ⟦nicht⟧ von der Anzahl der Eier ab.'},
]
TEIL = {'erkennen': 'begriff', 'pruefen': 'begriff', 'vervielfachen': 'tabelle', 'einheit': 'dreisatz', 'dreisatz': 'dreisatz', 'geschickt': 'dreisatz', 'sach': 'anwenden'}

PROP = ['Anzahl gleicher Brötchen → Preis', 'Benzinmenge → Preis an der Tankstelle', 'Anzahl gleicher Fliesen → bedeckte Fläche', 'Zeit bei gleichem Tempo → gefahrene Strecke',
        'Anzahl gleicher Flaschen → Gewicht der Flaschen', 'Seitenlänge eines Quadrats → Umfang', 'Anzahl gleicher Schritte → zurückgelegter Weg', 'Menge Wasser aus einem Hahn → Zeit, die der Hahn läuft']
NICHT = ['Alter eines Kindes → Körpergröße', 'Anzahl der Eier im Topf → Kochzeit', 'Seitenlänge eines Quadrats → Flächeninhalt', 'Anzahl der Geschwister → Taschengeld',
         'Tageszeit → Temperatur', 'Anzahl der Kerzen → Brenndauer der Kerzen', 'Anzahl der Musiker → Dauer des Liedes', 'Alter eines Autos → Wert des Autos',
         'Parkdauer → Parkgebühr, wenn die erste Stunde frei ist', 'Anzahl der Handtücher auf der Leine → Trockenzeit']


def g_erkennen(s):
    if s == 1:
        if R.random() < .5:
            a, i = mische(R, R.choice(PROP), R.sample(NICHT, 2))
            return {'y': 'auswahl', 'f': {'text': 'Welche Zuordnung ist proportional?'}, 'a': a, 'o': {'index': i},
                    'w': f'Nur bei „{a[i]}“ gehört zum Doppelten immer genau das Doppelte.', 'h': 'Prüfe: Gehört zur doppelten Menge genau der doppelte Wert?'}
        a, i = mische(R, R.choice(NICHT), R.sample(PROP, 2))
        return {'y': 'auswahl', 'f': {'text': 'Welche Zuordnung ist nicht proportional?'}, 'a': a, 'o': {'index': i},
                'w': f'Bei „{a[i]}“ gehört zum Doppelten nicht das Doppelte. Die beiden anderen sind proportional.', 'h': 'Prüfe: Gehört zur doppelten Menge genau der doppelte Wert?'}
    if s == 2:
        w = R.choice(WAREN); p = R.choice(w[5]); n = R.randint(2, 6); k = R.choice([2, 3, 4, 5, 10])
        ri = f'{zt(p * n * k)} {w[4]}'
        a, i = mische(R, ri, [f'{zt(p * n + k)} {w[4]}', f'{zt(p * n * k + p)} {w[4]}', f'{zt(p * (n + k))} {w[4]}'] if len({p * n * k, p * n + k, p * n * k + p, p * (n + k)}) == 4 else [f'{zt(p * n + k)} {w[4]}', f'{zt(p * n * k * 2)} {w[4]}'])
        return {'y': 'auswahl', 'f': {'text': f'Eine Zuordnung ist proportional. {satz(w, n, p * n)}. Was gilt dann für {n * k} {w[1]}?'}, 'a': a, 'o': {'index': i},
                'w': f'{n * k} ist das {k}-Fache von {n}. Also auch der Wert mal {k}: {zt(p * n)} · {k} = {ri}.', 'h': 'Wie oft passt die erste Menge in die zweite? Der Wert wird genauso oft genommen.'}
    art = R.choice(['fix', 'quadrat', 'ok'])
    if art == 'fix':
        g, p, n = R.choice([5, 10, 20]), R.choice([2, 3, 4]), R.randint(2, 5)
        a, i = mische(R, 'Nein, wegen der festen Grundgebühr', ['Ja, weil jede Stunde gleich viel kostet', 'Ja, weil der Preis immer steigt'])
        return {'y': 'auswahl', 'f': {'text': f'Ein Bootsverleih verlangt {g} € Grundgebühr und dazu {p} € pro Stunde. Ist die Zuordnung Stunden → Preis proportional?'}, 'a': a, 'o': {'index': i},
                'w': f'1 Stunde kostet {g + p} €, 2 Stunden kosten {g + 2 * p} €. Das ist nicht das Doppelte ({2 * (g + p)} €). Die Grundgebühr stört.', 'h': 'Rechne den Preis für 1 Stunde und für 2 Stunden aus. Ist es das Doppelte?'}
    if art == 'quadrat':
        x = R.randint(2, 9)
        a, i = mische(R, 'Der Umfang verdoppelt sich, der Flächeninhalt vervierfacht sich', ['Umfang und Flächeninhalt verdoppeln sich', 'Umfang und Flächeninhalt vervierfachen sich'])
        return {'y': 'auswahl', 'f': {'text': f'Ein Quadrat hat die Seitenlänge {x} cm. Die Seitenlänge wird verdoppelt. Was stimmt?'}, 'a': a, 'o': {'index': i},
                'w': f'Umfang: 4 · {x} = {4 * x} cm, danach 4 · {2 * x} = {8 * x} cm (doppelt). Fläche: {x * x} cm², danach {4 * x * x} cm² (vierfach). Nur der Umfang ist proportional zur Seitenlänge.',
                'h': 'Rechne Umfang und Flächeninhalt vorher und nachher aus.'}
    w = R.choice(WAREN); p = R.choice(w[5]); n = R.randint(3, 8)
    a, i = mische(R, f'Ja, {n} {w[1]}: {zt(p * n)} {w[4]}', [f'Ja, {n} {w[1]}: {zt(p + n)} {w[4]}', 'Nein, das kann man nicht wissen'])
    return {'y': 'auswahl', 'f': {'text': f'{satz(w, 1, p)}. Es gibt keinen festen Grundbetrag. Ist die Zuordnung proportional, und was gilt für {n} {w[1]}?'}, 'a': a, 'o': {'index': i},
            'w': f'Jede Einheit bringt {zt(p)} {w[4]}, ohne festen Anteil: proportional. {n} · {zt(p)} = {zt(p * n)} {w[4]}.', 'h': 'Gibt es einen festen Anteil, der nicht von der Menge abhängt? Wenn nicht, ist es proportional.'}


def g_vervielfachen(s):
    w = R.choice(WAREN); p = R.choice(w[5])
    if s == 1:
        n, k = R.randint(2, 5), R.choice([2, 3, 10])
        return {'y': 'zahl', 'f': {'text': f'{satz(w, n, p * n)}. {satz(w, n * k, 0, True)}?'}, 'o': {'wert': p * n * k, 'einheit': w[4]}, 'c': f'{p * n}*{k}',
                'w': f'{n * k} ist das {k}-Fache von {n}. Also: {zt(p * n)} · {k} = {zt(p * n * k)} {w[4]}.', 'h': 'Mit welcher Zahl musst du die Menge malnehmen? Nimm den Wert mit derselben Zahl mal.'}
    if s == 2:
        k = R.choice([2, 3, 4, 5]); n = R.randint(2, 6)
        return {'y': 'zahl', 'f': {'text': f'{satz(w, n * k, p * n * k)}. {satz(w, n, 0, True)}?'}, 'o': {'wert': p * n, 'einheit': w[4]}, 'c': f'{p * n * k}/{k}',
                'w': f'{n} ist der {k}. Teil von {n * k}. Also: {zt(p * n * k)} : {k} = {zt(p * n)} {w[4]}.', 'h': 'Durch welche Zahl musst du die Menge teilen? Teile den Wert durch dieselbe Zahl.'}
    n = R.choice([2, 3, 4, 5]); k1, k2 = R.sample([2, 3, 4, 5, 6], 2)
    return {'y': 'zahl', 'f': {'text': f'{satz(w, n * k1, p * n * k1)}. {satz(w, n * k2, 0, True)}?'}, 'o': {'wert': p * n * k2, 'einheit': w[4]}, 'c': f'{p * n * k1}/{k1}*{k2}',
            'w': f'Erst durch {k1}: {n} {w[1] if n > 1 else w[0]} → {zt(p * n)} {w[4]}. Dann mal {k2}: {zt(p * n * k2)} {w[4]}.', 'h': 'Gehe über eine kleinere Menge, die in beiden Mengen steckt.'}


def g_einheit(s):
    w = R.choice(WAREN); p = R.choice(w[5])
    n = {1: R.randint(2, 6), 2: R.randint(7, 12), 3: R.choice([15, 20, 25, 30, 40, 50])}[s]
    return {'y': 'zahl', 'f': {'text': f'{satz(w, n, p * n)}. {satz(w, 1, 0, True)}?'}, 'o': {'wert': p, 'einheit': w[4]}, 'c': f'{p * n}/{n}',
            'w': f'Beide Seiten geteilt durch {n}: {zt(p * n)} : {n} = {zt(p)} {w[4]}.', 'h': 'Teile den Wert durch die Anzahl.'}


def g_dreisatz(s):
    w = R.choice(WAREN); p = R.choice(w[5])
    a, b = {1: (R.randint(2, 5), R.randint(6, 9)), 2: (R.randint(3, 9), R.randint(4, 12)), 3: (R.choice([12, 15, 20, 25]), R.choice([7, 9, 11, 13, 30, 35]))}[s]
    if a == b or b % a == 0: return g_dreisatz(s)
    return {'y': 'zahl', 'f': {'text': f'{satz(w, a, p * a)}. {satz(w, b, 0, True)}?'}, 'o': {'wert': p * b, 'einheit': w[4]}, 'c': f'{p * a}/{a}*{b}',
            'w': f'1. {satz(w, a, p * a)}. 2. Geteilt durch {a}: {satz(w, 1, p)}. 3. Mal {b}: {zt(p)} · {b} = {zt(p * b)} {w[4]}.',
            'h': 'Drei Zeilen: was du weißt, dann auf 1 schließen (teilen), dann auf das Gesuchte (malnehmen).'}


def g_geschickt(s):
    w = R.choice(WAREN); p = R.choice(w[5])
    t = {1: R.choice([2, 3]), 2: R.choice([3, 4, 5]), 3: R.choice([5, 6, 10, 25])}[s]
    x, y = R.sample([2, 3, 4, 5, 7] if s < 3 else [2, 3, 4, 6, 7, 9], 2)
    a, b = t * x, t * y
    if b % a == 0 or a % b == 0: return g_geschickt(s)
    if s == 3 and R.random() < .5:
        ri = f'{t} {w[1]}'
        aw, i = mische(R, ri, [f'{t + 1 if (a % (t + 1) or b % (t + 1)) else t + 2} {w[1]}', f'{a + b} {w[1]}'])
        return {'y': 'auswahl', 'f': {'text': f'Du kennst den Wert für {a} {w[1]} und suchst den Wert für {b} {w[1]}. Welcher Zwischenschritt ist geschickt?'}, 'a': aw, 'o': {'index': i},
                'w': f'{t} steckt in {a} ({a} : {t} = {x}) und in {b} ({b} : {t} = {y}). Also erst durch {x} teilen, dann mal {y}.', 'h': 'Suche eine Zahl, durch die beide Mengen teilbar sind.'}
    return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {satz(w, a, p * a)}. {satz(w, b, 0, True)}?'}, 'o': {'wert': p * b, 'einheit': w[4]}, 'c': f'{p * a}/{x}*{y}',
            'w': f'Zwischenschritt {t}: {zt(p * a)} : {x} = {zt(p * t)} {w[4]}. Dann mal {y}: {zt(p * b)} {w[4]}.', 'h': f'Welche Menge steckt in {a} und in {b}?'}


def g_pruefen(s):
    p = R.choice([2, 3, 4, 5, 6, 7, 8, 12, 15])
    ns = sorted(R.sample(range(2, 13), 3))
    if s == 1:
        return {'y': 'zahl', 'f': {'text': f'Eine proportionale Tabelle: {ns[0]} → {p * ns[0]}, {ns[1]} → {p * ns[1]}, {ns[2]} → {p * ns[2]}. Welcher Wert gehört zu 1?'}, 'o': {'wert': p}, 'c': f'{p * ns[0]}/{ns[0]}',
                'w': f'Wert geteilt durch Menge: {p * ns[0]} : {ns[0]} = {p}. Das stimmt auch für die anderen Paare.', 'h': 'Teile einen Wert durch seine Menge.'}
    if s == 2:
        j = R.randrange(3); d = R.choice([-2, -1, 1, 2, 3])
        werte = [p * n for n in ns]; werte[j] += d
        a = [f'{ns[k]} → {werte[k]}' for k in range(3)]
        return {'y': 'auswahl', 'f': {'text': 'Zwei Paare gehören zu einer proportionalen Zuordnung, eines passt nicht. Welches?'}, 'a': a, 'o': {'index': j},
                'w': f'Bei den beiden anderen ist Wert : Menge = {p}. Bei {a[j]} müsste der Wert {p * ns[j]} sein.', 'h': 'Rechne bei jedem Paar Wert geteilt durch Menge.'}
    q = p + R.choice([1, 2])
    t1 = ', '.join(f'{n} → {p * n}' for n in ns)
    t2 = ', '.join(f'{n} → {p * n + q}' for n in ns)
    t3 = ', '.join(f'{n} → {n * n}' for n in ns)
    aw, i = mische(R, t1, [t2, t3])
    return {'y': 'auswahl', 'f': {'text': 'Welche Tabelle gehört zu einer proportionalen Zuordnung?'}, 'a': aw, 'o': {'index': i},
            'w': f'Nur bei {t1} ist Wert : Menge immer gleich ({p}). Bei den anderen ändert sich der Quotient.', 'h': 'Proportional heißt: Wert geteilt durch Menge ist bei allen Paaren gleich.'}


def g_sach(s):
    if s == 1:
        pers, k = R.choice([2, 4]), R.choice([2, 3, 4]); g = R.choice([150, 200, 250, 300]) * pers // 2
        ding = R.choice(['Nudeln', 'Reis', 'Mehl', 'Kartoffeln'])
        return {'y': 'zahl', 'f': {'text': f'Ein Rezept für {pers} Personen braucht {g} g {ding}. Wie viel Gramm braucht man für {pers * k} Personen?'}, 'o': {'wert': g * k, 'einheit': 'g'}, 'c': f'{g}*{k}',
                'w': f'{pers * k} Personen sind {k}-mal so viele. {g} g · {k} = {zt(g * k)} g.', 'h': 'Wie viel mal so viele Personen sind es?'}
    if s == 2:
        if R.random() < .35:
            n, m, t = R.randint(2, 4), R.randint(5, 9), R.choice([6, 8, 10, 45, 90])
            was, ein = R.choice([(f'{n} Eier kochen {t} Minuten. Wie viele Minuten kochen {m} Eier im selben Topf?', 'min'), (f'{n} Hemden trocknen auf der Leine in {t} Minuten. Wie viele Minuten brauchen {m} Hemden?', 'min'),
                                 (f'Ein Lied dauert {t} Minuten, wenn {n} Kinder es singen. Wie viele Minuten dauert es, wenn {m} Kinder singen?', 'min')])
            return {'y': 'zahl', 'f': {'text': was}, 'o': {'wert': t, 'einheit': ein}, 'c': str(t),
                    'w': f'Falle: Die Zeit hängt nicht von der Anzahl ab. Es bleibt bei {t} Minuten.', 'h': 'Prüfe zuerst: Wird die Zeit wirklich länger, wenn es mehr sind?'}
        a, b = R.choice([(4, 6), (6, 9), (4, 10), (6, 4), (8, 12), (10, 4), (3, 5), (5, 8)]); g = R.choice([20, 25, 30, 40, 45]) * a
        ding = R.choice(['Mehl', 'Zucker', 'Butter', 'Quark'])
        return {'y': 'zahl', 'f': {'text': f'Ein Rezept für {a} Muffins braucht {g} g {ding}. Wie viel Gramm braucht man für {b} Muffins?'}, 'o': {'wert': g // a * b, 'einheit': 'g'}, 'c': f'{g}/{a}*{b}',
                'w': f'1 Muffin: {g} g : {a} = {g // a} g. {b} Muffins: {g // a} g · {b} = {zt(g // a * b)} g.', 'h': 'Dreisatz: erst auf 1 Muffin, dann auf die gesuchte Anzahl.'}
    art = R.choice(['benzin', 'lohn', 'vergleich'])
    if art == 'benzin':
        v, s2 = R.choice([5, 6, 7, 8]), R.choice([250, 350, 450, 650, 750])
        return {'y': 'zahl', 'f': {'text': f'Ein Auto verbraucht auf 100 km {v} Liter Benzin. Wie viele Liter braucht es für {s2} km? (Das Ergebnis ist eine Kommazahl.)'}, 'o': {'wert': v * s2 / 100, 'einheit': 'Liter'}, 'c': f'{v}*{s2}/100',
                'w': f'50 km: {zt(v / 2)} Liter. {s2} km sind {s2 // 50}-mal 50 km: {zt(v / 2)} · {s2 // 50} = {zt(v * s2 / 100)} Liter.', 'h': 'Gehe über 50 km als Zwischenschritt.'}
    if art == 'lohn':
        h1, lohn, h2 = R.choice([3, 4, 6]), R.choice([9, 11, 12, 13]), R.choice([5, 7, 9, 11])
        if h1 == h2: return g_sach(s)
        return {'y': 'zahl', 'f': {'text': f'Mia trägt Zeitungen aus. Für {h1} Stunden bekommt sie {h1 * lohn} €. Wie viel bekommt sie für {h2} Stunden, wenn jede Stunde gleich bezahlt wird?'}, 'o': {'wert': lohn * h2, 'einheit': '€'}, 'c': f'{h1 * lohn}/{h1}*{h2}',
                'w': f'1 Stunde: {h1 * lohn} € : {h1} = {lohn} €. {h2} Stunden: {lohn} € · {h2} = {lohn * h2} €.', 'h': 'Dreisatz über 1 Stunde.'}
    n1, n2 = R.choice([(3, 5), (4, 6), (5, 8), (6, 10)]); p1 = R.choice([40, 50, 60]); p2 = p1 + R.choice([-5, 5, 10])
    bill = 'die kleine Packung' if p1 < p2 else 'die große Packung'
    aw, i = mische(R, 'D' + bill[1:], ['Die kleine Packung' if bill != 'die kleine Packung' else 'Die große Packung', 'Beide sind gleich günstig'])
    return {'y': 'auswahl', 'f': {'text': f'Kleine Packung: {n1} Riegel für {zt(n1 * p1)} ct. Große Packung: {n2} Riegel für {zt(n2 * p2)} ct. Bei welcher Packung ist ein Riegel billiger?'}, 'a': aw, 'o': {'index': i},
            'w': f'Klein: {n1 * p1} : {n1} = {p1} ct pro Riegel. Groß: {n2 * p2} : {n2} = {p2} ct pro Riegel. Billiger ist {bill}.', 'h': 'Rechne für jede Packung den Preis für 1 Riegel aus.'}


GEN = {'erkennen': g_erkennen, 'vervielfachen': g_vervielfachen, 'einheit': g_einheit, 'dreisatz': g_dreisatz, 'geschickt': g_geschickt, 'pruefen': g_pruefen, 'sach': g_sach}
DATEI = {
    'thema_schluessel': 'groessen.proportional', 'thema_id': 26, 'block_id': 54, 'klasse': {'gym_by': 5, 'rs_by': 5, 'ib_myp': 2},
    'autor': 'Claude (Generator groessen_proportional.py)',
    'offen': ['Produktgleichheit (indirekte Proportionalität) steht im „umfang“, gehört aber zum Thema groessen.indirekt (Kl. 8) und ist hier weggelassen.',
              'Darstellung im Koordinatensystem (Ursprungsgerade) fehlt, weil die App noch keine Graphen zeichnen kann.'],
    'inhalt': {
        'ziel': 'Proportionale Zuordnungen erkennen und mit dem Dreisatz in Sachaufgaben rechnen.',
        'merke': ['Proportional: doppelte Menge → doppelter Wert.', 'Auf beiden Seiten dasselbe: mal oder geteilt, nie plus oder minus.',
                  'Dreisatz: wissen → auf 1 schließen → auf das Gesuchte schließen.', 'Erst prüfen, ob es überhaupt proportional ist.'],
        'abschnitte': [{'titel': 'Proportional – was ist das?', 'lernziele': ['erkennen', 'vervielfachen', 'pruefen']},
                       {'titel': 'Der Dreisatz', 'lernziele': ['einheit', 'dreisatz', 'geschickt']},
                       {'titel': 'Anwenden', 'lernziele': ['sach']}],
        'etappen': ETAPPEN,
        'teilfaehigkeiten': [{'k': 'begriff', 'text': 'Proportionale Zuordnungen erkennen', 'lernziele': ['erkennen', 'pruefen']},
                             {'k': 'tabelle', 'text': 'Werte durch Vervielfachen und Teilen bestimmen', 'lernziele': ['vervielfachen']},
                             {'k': 'dreisatz', 'text': 'Schlussrechnung und Dreisatz', 'lernziele': ['einheit', 'dreisatz', 'geschickt']},
                             {'k': 'anwenden', 'text': 'Sachaufgaben', 'lernziele': ['sach']}],
        'bewertung': {'lernziele_pflicht': [e['lernziel'] for e in ETAPPEN], 'lernziele_vertiefung': [], 'testaufgaben_je_lernziel': 1, 'hilfen_im_test': False},
        'quellen': {'erklaerungen': 'Eigene Fassung (Claude).', 'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern, Gymnasium Mathematik 5.'},
    },
    'aufgaben': baue(R, ETAPPEN, GEN, TEIL, je_stufe=5),
}

if __name__ == '__main__':
    schreibe(DATEI, 'groessen.proportional.json')
