#!/usr/bin/env python3
"""Ganze Zahlen (Gymnasium Kl. 5): negative Zahlen deuten, Zahlengerade, ordnen, Betrag, addieren, subtrahieren.
Multiplikation/Division ganzer Zahlen gehört zum Thema zahlen.rechengesetze."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl5 import baue, kl, mische, schreibe, zt  # noqa: E402

R = random.Random(16)

ETAPPEN = [
    {'lernziel': 'deuten', 'titel': 'Was bedeutet eine negative Zahl?',
     'regel': 'Negative Zahlen liegen ⟦unter null⟧. Sie haben ein Minus davor: −5 °C heißt 5 Grad unter null, −20 € heißt 20 € Schulden.',
     'schritte': ['Das Thermometer zeigt 3 Grad unter null.', 'Unter null heißt negativ: Man schreibt ⟦−3 °C⟧.'],
     'fehler': 'Das Minus weglassen: 3 °C und −3 °C sind verschieden. Bei 3 °C taut Schnee, bei −3 °C friert es.'},
    {'lernziel': 'zahlengerade', 'titel': 'Zahlen auf der Zahlengeraden',
     'regel': 'Links von der 0 stehen die ⟦negativen⟧ Zahlen, rechts die positiven. Nach links wird es immer kleiner: … −3, −2, −1, 0, 1, 2 …',
     'schritte': ['Die Zahlengerade geht von −10 bis 10 in 10 Abschnitten: Ein Abschnitt ist (10 − (−10)) : 10 = 2 wert.', 'Vom Anfang −10 aus zählst du weiter: −8, −6, ⟦−4⟧ ist der 3. Strich nach dem Anfang.'],
     'bild': {'typ': 'zahlenstrahl', 'start': -10, 'ende': 10, 'abschnitte': 10, 'beschriftet': 'anfang_ende'},
     'fehler': 'Von der 0 aus in die falsche Richtung zählen: −4 liegt ⟦links⟧ von der 0, nicht rechts.'},
    {'lernziel': 'ordnen', 'titel': 'Welche Zahl ist kleiner?',
     'regel': 'Die Zahl, die auf der Zahlengeraden ⟦weiter links⟧ steht, ist kleiner. Jede negative Zahl ist kleiner als jede positive.',
     'schritte': ['Vergleiche −8 und −3: −8 liegt weiter links als −3.', 'Also ist ⟦−8 < −3⟧.'],
     'probe': 'Bei −8 °C ist es kälter als bei −3 °C ✓',
     'fehler': '−8 > −3, „weil 8 größer ist als 3“: Bei negativen Zahlen ist es umgekehrt. Mehr Minus heißt ⟦kleiner⟧.'},
    {'lernziel': 'betrag', 'titel': 'Betrag und Gegenzahl',
     'regel': 'Der ⟦Betrag⟧ einer Zahl ist ihr Abstand zur 0, also nie negativ: |−7| = 7 und |7| = 7. Die ⟦Gegenzahl⟧ hat denselben Betrag, aber das andere Vorzeichen.',
     'schritte': ['−7 ist 7 Schritte von der 0 entfernt, also |−7| = ⟦7⟧.', 'Die Gegenzahl von −7 liegt gleich weit auf der anderen Seite: ⟦7⟧.'],
     'fehler': '|−7| = −7 ist falsch: Ein Abstand ist ⟦nie negativ⟧.'},
    {'lernziel': 'addieren', 'titel': 'Ganze Zahlen addieren',
     'regel': 'Gleiche Vorzeichen: Beträge ⟦addieren⟧, das Vorzeichen bleibt. Verschiedene Vorzeichen: Beträge ⟦subtrahieren⟧, das Ergebnis bekommt das Vorzeichen der Zahl mit dem größeren Betrag.',
     'schritte': ['(−7) + 4: verschiedene Vorzeichen, also 7 − 4 = 3.', 'Der größere Betrag (7) gehört zur negativen Zahl, also ⟦−3⟧.'],
     'probe': 'Auf der Zahlengeraden: von −7 vier Schritte nach rechts → −3 ✓',
     'fehler': '(−7) + 4 = −11 ist falsch: Bei verschiedenen Vorzeichen wird nicht addiert, sondern ⟦subtrahiert⟧.'},
    {'lernziel': 'subtrahieren', 'titel': 'Ganze Zahlen subtrahieren',
     'regel': 'Subtrahieren heißt: die ⟦Gegenzahl addieren⟧. Also a − b = a + (−b) und a − (−b) = a + b.',
     'schritte': ['3 − 8 = 3 + (−8): verschiedene Vorzeichen, 8 − 3 = 5, also ⟦−5⟧.', '5 − (−3) = 5 + 3 = ⟦8⟧.'],
     'probe': '−5 + 8 = 3 ✓ und 8 + (−3) = 5 ✓',
     'fehler': '5 − (−3) = 2 ist falsch: Minus und Minus direkt hintereinander ergeben ⟦Plus⟧, also 5 + 3.'},
    {'lernziel': 'ketten', 'titel': 'Mehrere Zahlen hintereinander',
     'regel': 'Schreibe zuerst alles ⟦ohne Klammern⟧: + (−4) wird − 4, − (−4) wird + 4. Dann sammle alle Plus-Zahlen und alle Minus-Zahlen und verrechne sie.',
     'schritte': ['12 − (−5) + (−9) − 4 wird zu 12 + 5 − 9 − 4.', 'Plus: 12 + 5 = 17. Minus: 9 + 4 = 13.', '17 − 13 = ⟦4⟧.'],
     'fehler': 'Nur die erste Klammer auflösen und die zweite vergessen. Löse ⟦jede⟧ Klammer auf, bevor du rechnest.'},
    {'lernziel': 'sach', 'titel': 'Negative Zahlen im Alltag rechnen',
     'regel': 'Übersetze die Geschichte in eine Rechnung: Startwert, dann jede Änderung. ⟦Wärmer, einzahlen, steigen⟧ ist Plus. ⟦Kälter, abheben, sinken⟧ ist Minus.',
     'schritte': ['Morgens sind es −4 °C. Bis mittags wird es 7 Grad wärmer.', 'Rechnung: −4 + 7 = ⟦3⟧. Mittags sind es 3 °C.'],
     'probe': 'Von −4 bis 0 sind es 4 Grad, dann noch 3 weiter ✓',
     'fehler': 'Den Startwert ohne Minus einsetzen: 4 + 7 = 11 wäre der Start bei +4 °C, nicht bei ⟦−4 °C⟧.'},
]
TEIL = {'deuten': 'verstehen', 'zahlengerade': 'verstehen', 'ordnen': 'ordnen', 'betrag': 'ordnen',
        'addieren': 'addieren', 'subtrahieren': 'subtrahieren', 'ketten': 'verbinden', 'sach': 'verbinden'}


# ---------- Generatoren ----------
def g_deuten(s):
    n = R.randint(2, 30) if s < 3 else R.randint(2, 15)
    if s == 1:
        text, einheit = R.choice([
            (f'Das Thermometer zeigt {n} Grad unter null. Schreibe die Temperatur als Zahl.', '°C'),
            (f'Auf einem Konto sind {n * 10} € Schulden. Schreibe den Kontostand als Zahl.', '€'),
            (f'Ein Taucher ist {n} m unter der Wasseroberfläche. Schreibe seine Höhe als Zahl.', 'm'),
            (f'Das Parkhaus hat Stockwerke unter der Erde. Ein Auto steht {min(n, 5)} Stockwerke unter dem Erdgeschoss (Stockwerk 0). Welche Stockwerk-Zahl ist das?', None)])
        w = n * 10 if 'Konto' in text else (min(n, 5) if 'Parkhaus' in text else n)
        o = {'wert': -w, **({'einheit': einheit} if einheit else {})}
        return {'y': 'zahl', 'f': {'text': text}, 'o': o, 'c': f'-({w})',
                'w': f'„Unter null“, „Schulden“ und „unter“ bedeuten negativ. Also steht ein Minus davor: {zt(-w)}.',
                'h': 'Liegt der Wert über oder unter null? Unter null bekommt ein Minus.'}
    if s == 2:
        art = R.choice(['temp', 'konto', 'meer'])
        if art == 'temp':
            text = f'Was bedeutet die Temperatur {zt(-n)} °C?'
            r, f = f'{n} Grad unter null', [f'{n} Grad über null', f'Es wird {n} Grad wärmer']
        elif art == 'konto':
            text = f'Was bedeutet der Kontostand {zt(-n * 10)} €?'
            r, f = f'{n * 10} € Schulden', [f'{n * 10} € Guthaben', 'Das Konto ist genau leer']
        else:
            text = f'Ein Ort liegt auf der Höhe {zt(-n * 10)} m. Was bedeutet das?'
            r, f = f'{n * 10} m unter dem Meeresspiegel', [f'{n * 10} m über dem Meeresspiegel', 'Genau auf Höhe des Meeres']
        a, i = mische(R, r, f)
        return {'y': 'auswahl', 'f': {'text': text}, 'a': a, 'o': {'index': i},
                'w': f'Das Minus zeigt: Der Wert liegt unter null. Richtig ist: {r}.',
                'h': 'Das Minuszeichen heißt „unter null“.'}
    a, b = -n, R.randint(1, 15)
    text = R.choice([f'Morgens sind es {zt(a)} °C, mittags {zt(b)} °C. Um wie viel Grad ist es wärmer geworden?',
                     f'Ein Aufzug fährt von Stockwerk {zt(a)} bis Stockwerk {zt(b)}. Wie viele Stockwerke fährt er nach oben?'])
    return {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': b - a}, 'c': f'({b}) - ({a})',
            'w': f'Von {zt(a)} bis 0 sind es {n}. Von 0 bis {b} sind es {b}. Zusammen {n} + {b} = {b - a}.',
            'h': 'Gehe in zwei Teilen: erst bis zur 0, dann von der 0 weiter.'}


def g_zahlengerade(s):
    n = R.choice([8, 10])
    step = {1: [1], 2: [2, 5, 10], 3: [20, 25, 50, 100]}[s]
    step = R.choice(step)
    start = -step * R.randint(2, n - 2) if s < 3 else -step * R.randint(n // 2, n - 1)
    ende = start + n * step
    idx = R.randint(1, n - 1)
    z = start + idx * step
    if s >= 2 and z >= 0 and R.random() < .7: return g_zahlengerade(s)   # meist negative Zielzahl
    return {'y': 'markierung', 'f': {'text': f'Tippe die Markierung an, an der die Zahl {zt(z)} liegt.',
                                     'grafik': {'typ': 'zahlenstrahl', 'start': start, 'ende': ende, 'abschnitte': n, 'beschriftet': 'anfang_ende'}},
            'o': {'index': idx}, 'zahl': z, 'c': f'({start}) + {idx} * {step}',
            'w': f'Ein Abschnitt ist ({zt(ende)} − {kl(start)}) : {n} = {step} wert. Vom Anfang {zt(start)} aus {idx} {"Schritt" if idx == 1 else "Schritte"} nach rechts: {zt(z)}.',
            'h': 'Rechne zuerst aus, wie viel ein Abschnitt wert ist. Zähle dann vom Anfang aus.'}


def g_ordnen(s):
    if s == 1:
        zs = R.sample(range(-12, 13), 3)
        if all(z >= 0 for z in zs) or 0 in zs: return g_ordnen(s)
        kleinste = R.random() < .5
        r = min(zs) if kleinste else max(zs)
        a = [zt(z) for z in zs]
        return {'y': 'auswahl', 'f': {'text': f'Welche Zahl ist am {"kleinsten" if kleinste else "größten"}?'}, 'a': a, 'o': {'index': zs.index(r)},
                'w': f'Auf der Zahlengeraden von links nach rechts: {" < ".join(zt(z) for z in sorted(zs))}. Am {"weitesten links" if kleinste else "weitesten rechts"} steht {zt(r)}.',
                'h': 'Stell dir die Zahlengerade vor: Wer steht am weitesten links?'}
    if s == 2:
        zs = R.sample(range(-60, -1), 3)
        kleinste = R.random() < .5
        r = min(zs) if kleinste else max(zs)
        a = [zt(z) for z in zs]
        return {'y': 'auswahl', 'f': {'text': f'Alle drei Zahlen sind negativ. Welche ist am {"kleinsten" if kleinste else "größten"}?'}, 'a': a, 'o': {'index': zs.index(r)},
                'w': f'Bei negativen Zahlen gilt: größerer Betrag = weiter links = kleiner. Reihenfolge: {" < ".join(zt(z) for z in sorted(zs))}. Gesucht ist {zt(r)}.',
                'h': 'Bei negativen Zahlen ist die mit dem größeren Betrag die kleinere.'}
    if R.random() < .5:
        zs = R.sample(range(-20, 21), 4)
        if sum(z < 0 for z in zs) < 2: return g_ordnen(s)
        ri = sorted(zs)
        f1 = sorted(zs, key=abs)
        f2 = sorted([z for z in zs if z >= 0]) + sorted([z for z in zs if z < 0], reverse=True)
        f2 = sorted([z for z in zs if z < 0], reverse=True) + sorted([z for z in zs if z >= 0])
        if f1 == ri or f2 == ri or f1 == f2: return g_ordnen(s)
        fmt = lambda l: ' < '.join(zt(z) for z in l)
        a, i = mische(R, fmt(ri), [fmt(f1), fmt(f2)])
        return {'y': 'auswahl', 'f': {'text': 'Welche Kette ist richtig von klein nach groß geordnet?'}, 'a': a, 'o': {'index': i},
                'w': f'Zuerst die negativen Zahlen, die mit dem größten Betrag ganz links, dann die positiven: {fmt(ri)}.',
                'h': 'Ordne erst die negativen Zahlen (größter Betrag zuerst), dann die positiven.'}
    x, y = R.sample(range(2, 40), 2)
    lo, hi = -max(x, y), -min(x, y)
    a, i = mische(R, f'{zt(lo)} < {zt(hi)}', [f'{zt(lo)} > {zt(hi)}', f'{zt(lo)} = {zt(-lo)}'])
    return {'y': 'auswahl', 'f': {'text': 'Welche Aussage stimmt?'}, 'a': a, 'o': {'index': i},
            'w': f'{zt(lo)} liegt links von {zt(hi)}, also {zt(lo)} < {zt(hi)}. Eine Zahl und ihre Gegenzahl sind nicht gleich.',
            'h': 'Welche der beiden Zahlen steht weiter links auf der Zahlengeraden?'}


def g_betrag(s):
    n = R.randint(2, 60)
    if s == 1:
        if R.random() < .5:
            z = R.choice([-n, n])
            return {'y': 'zahl', 'f': {'text': f'Wie groß ist der Betrag von {zt(z)}?'}, 'o': {'wert': n}, 'c': f'abs({z})',
                    'w': f'{zt(z)} ist {n} Schritte von der 0 entfernt. Der Betrag ist {n}.', 'h': 'Der Betrag ist der Abstand zur 0.'}
        z = R.choice([-n, n])
        return {'y': 'zahl', 'f': {'text': f'Wie heißt die Gegenzahl von {zt(z)}?'}, 'o': {'wert': -z}, 'c': f'-({z})',
                'w': f'Die Gegenzahl liegt gleich weit von der 0 entfernt auf der anderen Seite: {zt(-z)}.', 'h': 'Gleicher Abstand zur 0, anderes Vorzeichen.'}
    if s == 2:
        a, b = R.choice([-1, 1]) * R.randint(2, 30), -R.randint(2, 30)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Berechne |{zt(a)}| + |{zt(b)}|.'}, 'o': {'wert': abs(a) + abs(b)}, 'c': f'abs({a}) + abs({b})',
                    'w': f'|{zt(a)}| = {abs(a)} und |{zt(b)}| = {abs(b)}. Zusammen {abs(a)} + {abs(b)} = {abs(a) + abs(b)}.', 'h': 'Bestimme zuerst jeden Betrag einzeln.'}
        z = -n
        aw, i = mische(R, str(n), [zt(z), '0'])
        return {'y': 'auswahl', 'f': {'text': f'Wie weit ist {zt(z)} von der 0 entfernt?'}, 'a': aw, 'o': {'index': i},
                'w': f'Der Abstand zur 0 ist der Betrag: |{zt(z)}| = {n}. Ein Abstand ist nie negativ.', 'h': 'Ein Abstand ist nie negativ.'}
    if R.random() < .5:
        a, i = mische(R, f'{n} und {zt(-n)}', [f'nur {n}', f'nur {zt(-n)}'])
        return {'y': 'auswahl', 'f': {'text': f'Welche Zahlen haben den Betrag {n}?'}, 'a': a, 'o': {'index': i},
                'w': f'Zwei Zahlen sind {n} Schritte von der 0 entfernt: {n} rechts und {zt(-n)} links.', 'h': 'Schau auf beide Seiten der 0.'}
    a, b = -R.randint(20, 60), -R.randint(2, 19)
    return {'y': 'zahl', 'f': {'text': f'Berechne |{zt(a)}| − |{zt(b)}|.'}, 'o': {'wert': abs(a) - abs(b)}, 'c': f'abs({a}) - abs({b})',
            'w': f'|{zt(a)}| = {abs(a)} und |{zt(b)}| = {abs(b)}. {abs(a)} − {abs(b)} = {abs(a) - abs(b)}.', 'h': 'Bestimme zuerst jeden Betrag einzeln.'}


def _add_weg(a, b):
    if (a < 0) == (b < 0):
        return f'Gleiche Vorzeichen: Beträge addieren, {abs(a)} + {abs(b)} = {abs(a) + abs(b)}. Das Vorzeichen bleibt: {zt(a + b)}.'
    gr, k = max(abs(a), abs(b)), min(abs(a), abs(b))
    if a + b == 0: return f'Verschiedene Vorzeichen und gleiche Beträge: Die Zahlen heben sich auf, Ergebnis 0.'
    return f'Verschiedene Vorzeichen: Beträge subtrahieren, {gr} − {k} = {gr - k}. Der größere Betrag ({gr}) gehört zur {"negativen" if a + b < 0 else "positiven"} Zahl, also {zt(a + b)}.'


def g_addieren(s):
    g = {1: 12, 2: 60, 3: 400}[s]
    a, b = R.randint(-g, g), R.randint(-g, g)
    if (a >= 0 and b >= 0) or 0 in (a, b): return g_addieren(s)
    return {'y': 'zahl', 'f': {'text': f'Berechne {kl(a)} + {kl(b)}.'}, 'o': {'wert': a + b}, 'c': f'({a}) + ({b})', 'w': _add_weg(a, b),
            'h': 'Vergleiche die Vorzeichen. Gleich: Beträge addieren. Verschieden: Beträge subtrahieren.'}


def g_subtrahieren(s):
    g = {1: 12, 2: 60, 3: 400}[s]
    form = R.choice(['pp', 'pn', 'np', 'nn'])
    x, y = R.randint(1, g), R.randint(1, g)
    if form == 'pp':
        if x >= y: x, y = y, x + 1
        a, b = x, y
    elif form == 'pn': a, b = x, -y
    elif form == 'np': a, b = -x, y
    else: a, b = -x, -y
    return {'y': 'zahl', 'f': {'text': f'Berechne {kl(a)} − {kl(b)}.'}, 'o': {'wert': a - b}, 'c': f'({a}) - ({b})',
            'w': f'Gegenzahl addieren: {kl(a)} − {kl(b)} = {kl(a)} + {kl(-b)}. ' + _add_weg(a, -b),
            'h': 'Schreibe die Subtraktion als Addition der Gegenzahl. Dann gelten die Regeln fürs Addieren.'}


def g_ketten(s):
    n = {1: 3, 2: 4, 3: 4}[s]
    g = {1: 12, 2: 25, 3: 40}[s]
    zs = [R.choice([-1, 1]) * R.randint(1, g) for _ in range(n)]
    if all(z > 0 for z in zs[1:]) : return g_ketten(s)
    if s < 3:
        text = zt(zs[0]) + ''.join(f' {"+" if z > 0 else "−"} {abs(z)}' for z in zs[1:])
        ops = None
    else:
        ops = [R.choice('+-') for _ in zs[1:]]
        if not any(o == '-' and z < 0 for o, z in zip(ops, zs[1:])): return g_ketten(s)
        text = zt(zs[0]) + ''.join(f' {"+" if o == "+" else "−"} {kl(z)}' for o, z in zip(ops, zs[1:]))
    werte = [zs[0]] + [z if (ops is None or o == '+') else -z for o, z in zip(ops or ['+'] * (n - 1), zs[1:])]
    plus, minus = [w for w in werte if w > 0], [-w for w in werte if w < 0]
    ohne = zt(werte[0]) + ''.join(f' {"+" if w > 0 else "−"} {abs(w)}' for w in werte[1:])
    weg = (f'Ohne Klammern: {ohne}. ' if ops else '') + f'Plus-Zahlen: {" + ".join(map(str, plus)) or "keine"} = {sum(plus)}. Minus-Zahlen: {" + ".join(map(str, minus)) or "keine"} = {sum(minus)}. {sum(plus)} − {sum(minus)} = {zt(sum(werte))}.'
    return {'y': 'zahl', 'f': {'text': f'Berechne {text}.'}, 'o': {'wert': sum(werte)}, 'c': ' + '.join(f'({w})' for w in werte), 'w': weg,
            'h': 'Löse zuerst alle Klammern auf. Sammle dann die Plus-Zahlen und die Minus-Zahlen getrennt.'}


def g_sach(s):
    if s == 1:
        a, d = -R.randint(1, 15), R.randint(2, 20)
        auf = R.random() < .6
        text = R.choice([(f'Es sind {zt(a)} °C. Es wird {d} Grad {"wärmer" if auf else "kälter"}. Wie viel Grad sind es dann?', '°C'),
                         (f'Ein Taucher ist auf {zt(a)} m. Er {"steigt" if auf else "sinkt"} {d} m. Auf welcher Höhe ist er jetzt?', 'm')])
        if not auf and 'Taucher' not in text[0] and a - d < -40: return g_sach(s)
        e = a + d if auf else a - d
        return {'y': 'zahl', 'f': {'text': text[0]}, 'o': {'wert': e, 'einheit': text[1]}, 'c': f'({a}) {"+" if auf else "-"} {d}',
                'w': f'Start {zt(a)}, Änderung {"+" if auf else "−"} {d}: {zt(a)} {"+" if auf else "−"} {d} = {zt(e)}.',
                'h': 'Startwert aufschreiben. Wärmer oder steigen ist Plus, kälter oder sinken ist Minus.'}
    if s == 2:
        a, x, y = -R.randint(1, 9) * 10, R.randint(1, 12) * 5, R.randint(1, 12) * 5
        if x == y: return g_sach(s)
        text = f'Der Kontostand ist {zt(a)} €. Dann werden {x} € eingezahlt und {y} € abgehoben. Wie ist der Kontostand jetzt?'
        return {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': a + x - y, 'einheit': '€'}, 'c': f'({a}) + {x} - {y}',
                'w': f'Einzahlen ist Plus, abheben ist Minus: {zt(a)} + {x} − {y} = {zt(a + x - y)}.',
                'h': 'Einzahlen ist Plus, abheben ist Minus. Rechne Schritt für Schritt.'}
    if R.random() < .5:
        a, b = -R.randint(2, 20), -R.randint(21, 60)
        text = f'Ein U-Boot taucht von {zt(a)} m auf {zt(b)} m. Um wie viele Meter ist es tiefer gegangen?'
        return {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': a - b, 'einheit': 'm'}, 'c': f'({a}) - ({b})',
                'w': f'Unterschied der beiden Höhen: {zt(a)} − {kl(b)} = {zt(a)} + {-b} = {a - b}.',
                'h': 'Gesucht ist der Abstand der beiden Zahlen auf der Zahlengeraden.'}
    a, d1, d2, d3 = -R.randint(1, 10), R.randint(3, 12), R.randint(2, 9), R.randint(5, 15)
    text = f'Um 6 Uhr sind es {zt(a)} °C. Bis mittags wird es {d1} Grad wärmer, bis abends {d2} Grad kälter und in der Nacht noch einmal {d3} Grad kälter. Wie kalt ist es in der Nacht?'
    e = a + d1 - d2 - d3
    return {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': e, 'einheit': '°C'}, 'c': f'({a}) + {d1} - {d2} - {d3}',
            'w': f'{zt(a)} + {d1} − {d2} − {d3}: Plus {d1}, Minus {abs(a)} + {d2} + {d3} = {abs(a) + d2 + d3}. {d1} − {abs(a) + d2 + d3} = {zt(e)}.',
            'h': 'Schreibe eine Rechnung mit allen Änderungen hintereinander.'}


GEN = {'deuten': g_deuten, 'zahlengerade': g_zahlengerade, 'ordnen': g_ordnen, 'betrag': g_betrag,
       'addieren': g_addieren, 'subtrahieren': g_subtrahieren, 'ketten': g_ketten, 'sach': g_sach}
PFLICHT = [e['lernziel'] for e in ETAPPEN]

DATEI = {
    'thema_schluessel': 'zahlen.ganz', 'thema_id': 16, 'block_id': 49, 'klasse': {'gym_by': 5, 'rs_by': 5, 'ib_myp': 2},
    'autor': 'Claude (Generator zahlen_ganz.py)',
    'inhalt': {
        'ziel': 'Negative Zahlen deuten, auf der Zahlengeraden finden und ordnen; Betrag und Gegenzahl bestimmen; ganze Zahlen addieren und subtrahieren.',
        'merke': ['Negative Zahlen stehen links von der 0. Weiter links heißt kleiner.', 'Betrag = Abstand zur 0, nie negativ.',
                  'Gleiche Vorzeichen: Beträge addieren. Verschiedene: Beträge subtrahieren.', 'Subtrahieren = Gegenzahl addieren.'],
        'abschnitte': [{'titel': 'Negative Zahlen verstehen', 'lernziele': ['deuten', 'zahlengerade', 'ordnen', 'betrag']},
                       {'titel': 'Addieren und Subtrahieren', 'lernziele': ['addieren', 'subtrahieren']},
                       {'titel': 'Alles zusammen', 'lernziele': ['ketten', 'sach']}],
        'etappen': ETAPPEN,
        'teilfaehigkeiten': [
            {'k': 'verstehen', 'text': 'Negative Zahlen deuten und an der Zahlengeraden darstellen', 'lernziele': ['deuten', 'zahlengerade']},
            {'k': 'ordnen', 'text': 'Ganze Zahlen ordnen, Betrag und Gegenzahl', 'lernziele': ['ordnen', 'betrag']},
            {'k': 'addieren', 'text': 'Ganze Zahlen addieren', 'lernziele': ['addieren']},
            {'k': 'subtrahieren', 'text': 'Ganze Zahlen subtrahieren', 'lernziele': ['subtrahieren']},
            {'k': 'verbinden', 'text': 'Mehrgliedrige Rechnungen und Sachaufgaben', 'lernziele': ['ketten', 'sach']}],
        'bewertung': {'lernziele_pflicht': PFLICHT, 'lernziele_vertiefung': [], 'testaufgaben_je_lernziel': 1, 'hilfen_im_test': False},
        'quellen': {'erklaerungen': 'Eigene Fassung (Claude).', 'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern, Gymnasium Mathematik 5.'},
    },
    'aufgaben': baue(R, ETAPPEN, GEN, TEIL),
}

if __name__ == '__main__':
    schreibe(DATEI, 'zahlen.ganz.json')
