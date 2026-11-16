#!/usr/bin/env python3
"""Ganze Zahlen (Gymnasium Kl. 5): negative Zahlen deuten, Zahlengerade, ordnen, Betrag, addieren, subtrahieren.
Multiplikation/Division ganzer Zahlen gehört zum Thema zahlen.rechengesetze."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl5 import baue, kl, mische_rund, schreibe, zt  # noqa: E402

R = random.Random(16)

# Erklärungen: Fassung der Prüfung (inhalte/pruefung/erklaerungen/zahlen.ganz.json) übernommen.
ETAPPEN = [
    {
        "lernziel": "deuten",
        "titel": "Was bedeutet eine negative Zahl?",
        "regel": "Negative Zahlen liegen ⟦unter null⟧. Sie haben ein Minus davor: −5 °C heißt 5 Grad unter null, −20 € heißt 20 € Schulden.",
        "schritte": [
            "Das Thermometer zeigt 3 Grad unter null.",
            "Unter null heißt negativ: Man schreibt ⟦−3 °C⟧."
        ],
        "fehler": "Das Minus weglassen: 3 °C und −3 °C sind verschieden. Bei 3 °C taut Schnee, bei −3 °C friert es."
    },
    {
        "lernziel": "zahlengerade",
        "titel": "Zahlen auf der Zahlengeraden",
        "regel": "Links von der 0 stehen die ⟦negativen⟧ Zahlen, rechts die positiven. Nach links wird es immer kleiner: … −3, −2, −1, 0, 1, 2 …",
        "schritte": [
            "Die Zahlengerade geht von −10 bis 10. Dazwischen sind 10 gleich lange Abschnitte.",
            "Von −10 bis 10 sind es 20 Schritte. 20 : 10 = 2, also ist ⟦ein Abschnitt 2 wert⟧.",
            "Vom Anfang −10 aus zählst du in Zweierschritten: −8, −6, ⟦−4⟧. Die −4 ist der 3. Strich nach dem Anfang."
        ],
        "bild": {
            "typ": "zahlenstrahl",
            "start": -10,
            "ende": 10,
            "abschnitte": 10,
            "beschriftet": "anfang_ende",
            "pfeil": 3
        },
        "fehler": "Jeden Strich als 1 zählen: Dann wäre der 3. Strich nach −10 die −7. Hier ist aber jeder Abschnitt ⟦2⟧ wert. Rechne immer zuerst aus, wie viel ein Abschnitt wert ist."
    },
    {
        "lernziel": "ordnen",
        "titel": "Welche Zahl ist kleiner?",
        "regel": "Die Zahl, die auf der Zahlengeraden ⟦weiter links⟧ steht, ist kleiner. Jede negative Zahl ist kleiner als jede positive.",
        "schritte": [
            "Vergleiche −8 und −3: −8 liegt weiter links als −3.",
            "Also ist ⟦−8 < −3⟧."
        ],
        "probe": "Bei −8 °C ist es kälter als bei −3 °C ✓",
        "fehler": "−8 > −3, „weil 8 größer ist als 3“: Bei negativen Zahlen ist es umgekehrt. Mehr Minus heißt ⟦kleiner⟧."
    },
    {
        "lernziel": "betrag",
        "titel": "Betrag und Gegenzahl",
        "regel": "Der ⟦Betrag⟧ einer Zahl ist ihr Abstand zur 0. Ein Abstand ist nie negativ: |−7| = 7 und |7| = 7. Die ⟦Gegenzahl⟧ liegt gleich weit von der 0 weg, aber auf der anderen Seite: Die Gegenzahl von −7 ist 7.",
        "schritte": [
            "Ein Taucher ist 7 m unter dem Meeresspiegel: −7 m.",
            "Wie weit ist er von der Wasseroberfläche weg? 7 m. Also |−7| = ⟦7⟧.",
            "Ein Vogel 7 m über dem Wasser ist gleich weit weg, nur auf der anderen Seite: Die Gegenzahl von −7 ist ⟦7⟧."
        ],
        "fehler": "|−7| = −7 ist falsch. Der Betrag fragt nur „wie weit weg?“ – und ein Abstand ist ⟦nie negativ⟧.",
        "bild": {
            "typ": "zahlenstrahl",
            "start": -10,
            "ende": 10,
            "abschnitte": 20,
            "beschriftet": "anfang_ende",
            "pfeil": 3
        }
    },
    {
        "lernziel": "addieren",
        "titel": "Ganze Zahlen addieren",
        "regel": "Stell dir die Zahlengerade vor. ⟦+ eine positive Zahl⟧: Du gehst nach rechts. ⟦+ eine negative Zahl⟧: Du gehst nach links. Abkürzung: Gleiche Vorzeichen – Beträge addieren. Verschiedene Vorzeichen – Beträge subtrahieren; das Ergebnis hat das Vorzeichen der Zahl, die weiter von der 0 weg ist.",
        "schritte": [
            "Du hast 7 € Schulden, also −7 €. Dann bekommst du 4 € geschenkt: (−7) + 4.",
            "Auf der Zahlengeraden: Start bei −7, dann 4 Schritte nach rechts: −6, −5, −4, ⟦−3⟧.",
            "Du hast noch 3 € Schulden. Mit der Abkürzung: 7 − 4 = 3. Die −7 ist weiter von der 0 weg, also ⟦−3⟧."
        ],
        "probe": "Kontostand: Von 7 € Schulden zahlst du 4 € zurück, es bleiben 3 € Schulden ✓",
        "fehler": "(−7) + 4 = −11 ist falsch. Wer 4 € dazubekommt, hat danach ⟦weniger⟧ Schulden, nicht mehr. Bei verschiedenen Vorzeichen werden die Beträge ⟦subtrahiert⟧: 7 − 4 = 3, also −3.",
        "bild": {
            "typ": "zahlenstrahl",
            "start": -10,
            "ende": 10,
            "abschnitte": 20,
            "beschriftet": "anfang_ende",
            "pfeil": 7
        }
    },
    {
        "lernziel": "subtrahieren",
        "titel": "Ganze Zahlen subtrahieren",
        "regel": "Subtrahieren heißt: ⟦die Gegenzahl addieren⟧. Also 3 − 8 = 3 + (−8) und 5 − (−3) = 5 + 3. Warum? Wenn dir jemand ⟦Schulden wegnimmt⟧, wirst du reicher.",
        "schritte": [
            "3 − 8: Du hast 3 € und gibst 8 € aus. Das ist 3 + (−8). Von 3 gehst du 8 Schritte nach links: ⟦−5⟧.",
            "5 − (−3): Du hast 5 €. Jemand streicht dir 3 € Schulden. Danach hast du 3 € mehr: 5 + 3 = ⟦8⟧."
        ],
        "probe": "Umkehraufgabe: (−5) + 8 = 3 ✓ und 8 + (−3) = 5 ✓",
        "fehler": "5 − (−3) = 2 ist falsch. Hier werden nicht 3 € weggenommen, sondern ⟦3 € Schulden⟧. Weniger Schulden heißt mehr Geld: 5 − (−3) = 5 + 3 = 8. Vorsicht auch bei (−3) − 5: Das ist (−3) + (−5) = −8, nicht +8 – hier wird ja keine negative Zahl abgezogen."
    },
    {
        "lernziel": "ketten",
        "titel": "Mehrere Zahlen hintereinander",
        "regel": "Schreibe zuerst alles ⟦ohne Klammern⟧: + (−4) wird − 4, − (−4) wird + 4. Dann sammle alle Plus-Zahlen und alle Minus-Zahlen und verrechne sie.",
        "schritte": [
            "12 − (−5) + (−9) − 4 wird zu 12 + 5 − 9 − 4.",
            "Plus: 12 + 5 = 17. Minus: 9 + 4 = 13.",
            "17 − 13 = ⟦4⟧."
        ],
        "fehler": "Nur die erste Klammer auflösen und die zweite vergessen. Löse ⟦jede⟧ Klammer auf, bevor du rechnest."
    },
    {
        "lernziel": "sach",
        "titel": "Negative Zahlen im Alltag rechnen",
        "regel": "Übersetze die Geschichte in eine Rechnung: Startwert, dann jede Änderung. ⟦Wärmer, einzahlen, steigen⟧ ist Plus. ⟦Kälter, abheben, sinken⟧ ist Minus.",
        "schritte": [
            "Morgens sind es −4 °C. Bis mittags wird es 7 Grad wärmer.",
            "Rechnung: −4 + 7 = ⟦3⟧. Mittags sind es 3 °C."
        ],
        "probe": "Von −4 bis 0 sind es 4 Grad, dann noch 3 weiter ✓",
        "fehler": "Den Startwert ohne Minus einsetzen: 4 + 7 = 11 wäre der Start bei +4 °C, nicht bei ⟦−4 °C⟧."
    }
]
TEIL = {'deuten': 'verstehen', 'zahlengerade': 'verstehen', 'ordnen': 'ordnen', 'betrag': 'ordnen',
        'addieren': 'addieren', 'subtrahieren': 'subtrahieren', 'ketten': 'verbinden', 'sach': 'verbinden'}


# ---------- Generatoren ----------
# Prüfung eingearbeitet (inhalte/pruefung/aufgaben/zahlen.ganz.json): neue Aufgabentypen je Karte,
# Stufe 3 mit anderem Gedanken statt nur größeren Zahlen, Ablenker aus typischen Fehlern, richtige Antwort reihum verteilt.
KONTO = {'n': 0}          # Kontoaufgabe „einzahlen/abheben“ höchstens 8-mal


def _rund(r, f):
    return mische_rund(R, r, f)


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
        art = R.choice(['temp', 'konto', 'meer', 'taucher_hoch', 'konto_null'])
        if art == 'taucher_hoch':
            a = R.randint(3, 40)
            return {'y': 'zahl', 'f': {'text': f'Ein Taucher ist auf {zt(-a)} m. Wie viele Meter muss er nach oben, bis er an der Wasseroberfläche (0 m) ist?'},
                    'o': {'wert': a, 'einheit': 'm'}, 'c': f'0 - ({-a})',
                    'w': f'{zt(-a)} m heißt {a} m unter der Wasseroberfläche. Bis 0 m sind es also {a} m nach oben.',
                    'h': 'Wie weit ist der Taucher von der 0 entfernt?'}
        if art == 'konto_null':
            a = R.randint(1, 19) * 5
            return {'y': 'zahl', 'f': {'text': f'Ein Konto steht auf {zt(-a)} €. Wie viel Geld musst du einzahlen, damit genau 0 € darauf sind?'},
                    'o': {'wert': a, 'einheit': '€'}, 'c': f'0 - ({-a})',
                    'w': f'{zt(-a)} € heißt {a} € Schulden. Erst wenn du {a} € einzahlst, ist das Konto bei 0 €.',
                    'h': 'Wie viele Schulden sind auf dem Konto?'}
        if art == 'temp':
            n = max(n, 4)
            y = R.randint(1, n - 1)
            text = f'Was bedeutet die Temperatur {zt(-n)} °C?'
            r, f = f'{n} Grad unter null', [f'{n} Grad über null', f'wärmer als {zt(-y)} °C']
            w = f'Das Minus zeigt: unter null. {zt(-n)} °C ist sogar kälter als {zt(-y)} °C, weil {zt(-n)} weiter links liegt. Richtig ist: {r}.'
        elif art == 'konto':
            text = f'Was bedeutet der Kontostand {zt(-n * 10)} €?'
            r, f = f'{n * 10} € Schulden', [f'{n * 10} € Guthaben', 'Das Konto ist genau leer']
            w = f'Das Minus zeigt: Der Wert liegt unter null. Richtig ist: {r}.'
        else:
            text = f'Ein Ort liegt auf der Höhe {zt(-n * 10)} m. Was bedeutet das?'
            r, f = f'{n * 10} m unter dem Meeresspiegel', [f'{n * 10} m über dem Meeresspiegel', 'Genau auf Höhe des Meeres']
            w = f'Das Minus zeigt: Der Wert liegt unter null. Richtig ist: {r}.'
        a, i = _rund(r, f)
        return {'y': 'auswahl', 'f': {'text': text}, 'a': a, 'o': {'index': i}, 'w': w,
                'h': 'Das Minuszeichen heißt „unter null“.'}
    art = R.choice(['abstand', 'abstand', 'waermer', 'schulden'])
    if art == 'waermer':
        x = R.randint(3, 20); y = R.randint(1, x - 1)
        if R.random() < .5:
            text = f'Bei {zt(-y)} °C ist es wärmer als bei {zt(-x)} °C. Stimmt das?'
            r, f = f'Ja, {zt(-y)} liegt rechts von {zt(-x)}.', [f'Nein, denn {x} ist größer als {y}.', 'Nein, beide sind gleich kalt.']
        else:
            text = f'Bei {zt(-x)} °C ist es wärmer als bei {zt(-y)} °C. Stimmt das?'
            r, f = f'Nein, {zt(-x)} liegt links von {zt(-y)}. Dort ist es kälter.', [f'Ja, denn {x} ist größer als {y}.', 'Ja, beide sind gleich warm.']
        a, i = _rund(r, f)
        return {'y': 'auswahl', 'f': {'text': text}, 'a': a, 'o': {'index': i},
                'w': f'Auf dem Thermometer liegt {zt(-x)} °C tiefer als {zt(-y)} °C. Bei {zt(-y)} °C ist es also wärmer. Die Beträge {x} und {y} allein sagen nichts über warm und kalt.',
                'h': 'Stell dir ein Thermometer vor: Welche Temperatur steht weiter oben?'}
    if art == 'schulden':
        x = R.randint(3, 19) * 5; y = R.randint(1, x // 5 - 1) * 5
        text = f'Wer hat mehr Schulden: Konto A mit {zt(-x)} € oder Konto B mit {zt(-y)} €?'
        r, f = f'Konto A ({zt(-x)} €)', [f'Konto B, weil {zt(-y)} größer ist als {zt(-x)}', 'Beide haben gleich viele Schulden']
        a, i = _rund(r, f)
        return {'y': 'auswahl', 'f': {'text': text}, 'a': a, 'o': {'index': i},
                'w': f'{zt(-x)} € heißt {x} € Schulden, {zt(-y)} € heißt {y} € Schulden. {x} € Schulden sind mehr. Die Zahl {zt(-x)} ist dabei die kleinere.',
                'h': 'Schulden: Wie viele Euro fehlen auf jedem Konto?'}
    a, b = -n, R.randint(1, 15)
    text = R.choice([f'Morgens sind es {zt(a)} °C, mittags {zt(b)} °C. Um wie viel Grad ist es wärmer geworden?',
                     f'Ein Aufzug fährt von Stockwerk {zt(a)} bis Stockwerk {zt(b)}. Wie viele Stockwerke fährt er nach oben?'])
    return {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': b - a}, 'c': f'({b}) - ({a})',
            'w': f'Von {zt(a)} bis 0 sind es {n}. Von 0 bis {b} sind es {b}. Zusammen {n} + {b} = {b - a}.',
            'h': 'Gehe in zwei Teilen: erst bis zur 0, dann von der 0 weiter.'}


def _markierung(step):
    n = R.choice([8, 10])
    k = R.randint(2, n - 2)
    start = -step * k
    ende = start + n * step
    # mindestens ein Drittel der Ziele positiv (Prüfung)
    idx = R.randint(k + 1, n - 1) if R.random() < .4 else R.randint(1, k - 1)
    z = start + idx * step
    return {'y': 'markierung', 'f': {'text': f'Tippe die Markierung an, an der die Zahl {zt(z)} liegt.',
                                     'grafik': {'typ': 'zahlenstrahl', 'start': start, 'ende': ende, 'abschnitte': n, 'beschriftet': 'anfang_ende'}},
            'o': {'index': idx}, 'zahl': z, 'c': f'({start}) + {idx} * {step}',
            'w': f'Ein Abschnitt ist ({zt(ende)} − {kl(start)}) : {n} = {step} wert. Vom Anfang {zt(start)} aus {idx} {"Schritt" if idx == 1 else "Schritte"} nach rechts: {zt(z)}.',
            'h': 'Rechne zuerst aus, wie viel ein Abschnitt wert ist. Zähle dann vom Anfang aus.'}


def g_zahlengerade(s):
    if s == 1: return _markierung(1)
    if s == 2:
        if R.random() < .7: return _markierung(R.choice([2, 5, 10]))
        a, d = R.randint(-15, 15), R.randint(3, 15)
        links = R.random() < .5
        e = a - d if links else a + d
        if a >= 0 and e >= 0: return g_zahlengerade(s)
        return {'y': 'zahl', 'f': {'text': f'Du startest auf der Zahlengeraden bei {zt(a)} und gehst {d} Schritte nach {"links" if links else "rechts"}. Wo landest du?'},
                'o': {'wert': e}, 'c': f'({a}) {"-" if links else "+"} {d}',
                'w': f'Nach {"links" if links else "rechts"} heißt {"minus" if links else "plus"}: {kl(a)} {"−" if links else "+"} {d} = {zt(e)}.',
                'h': 'Nach rechts wird es größer, nach links kleiner.'}
    art = R.choice(['mitte', 'abschnitt', 'gross'])
    if art == 'gross': return _markierung(R.choice([20, 25, 50, 100]))
    if art == 'mitte':
        a = -R.randint(2, 40); b = a + 2 * R.randint(2, 20)
        m = (a + b) // 2
        return {'y': 'zahl', 'f': {'text': f'Welche Zahl liegt genau in der Mitte zwischen {zt(a)} und {zt(b)}?'},
                'o': {'wert': m}, 'c': f'(({a}) + ({b})) / 2',
                'w': f'Von {zt(a)} bis {zt(b)} sind es {b - a} Schritte. Die Hälfte sind {(b - a) // 2} Schritte. {kl(a)} + {(b - a) // 2} = {zt(m)}.',
                'h': 'Wie viele Schritte sind es von der einen Zahl zur anderen? Gehe die Hälfte davon.'}
    step, n = R.choice([2, 4, 5, 10, 20, 25, 50]), R.choice([4, 5, 8, 10])
    start = -step * R.randint(1, n - 1)
    ende = start + n * step
    return {'y': 'zahl', 'f': {'text': 'Wie viel ist ein Abschnitt dieser Zahlengeraden wert?',
                               'grafik': {'typ': 'zahlenstrahl', 'start': start, 'ende': ende, 'abschnitte': n, 'beschriftet': 'anfang_ende'}},
            'o': {'wert': step}, 'c': f'(({ende}) - ({start})) / {n}',
            'w': f'Von {zt(start)} bis {zt(ende)} sind es {ende - start} Schritte. Es gibt {n} Abschnitte: {ende - start} : {n} = {step}.',
            'h': 'Wie weit ist es vom Anfang bis zum Ende? Zähle die Abschnitte.'}


def g_ordnen(s):
    if s == 1:
        if R.random() < .4:
            a = R.randint(-20, -1)
            return {'y': 'zahl', 'f': {'text': f'Nenne die ganze Zahl, die zwischen {zt(a)} und {zt(a + 2)} liegt.'},
                    'o': {'wert': a + 1}, 'c': f'({a}) + 1',
                    'w': f'Auf der Zahlengeraden: {zt(a)}, {zt(a + 1)}, {zt(a + 2)}. Dazwischen liegt {zt(a + 1)}.',
                    'h': 'Gehe von der linken Zahl einen Schritt nach rechts.'}
        big = R.randint(8, 20)
        zs = [-big, R.randint(1, big - 1), R.choice([-1, 1]) * R.randint(1, big - 1)]
        if len(set(zs)) < 3: return g_ordnen(s)
        R.shuffle(zs)
        kleinste = R.random() < .5
        r = min(zs) if kleinste else max(zs)
        a = [zt(z) for z in zs]
        return {'y': 'auswahl', 'f': {'text': f'Welche Zahl ist am {"kleinsten" if kleinste else "größten"}?'}, 'a': a, 'o': {'index': zs.index(r)},
                'w': f'Auf der Zahlengeraden von links nach rechts: {" < ".join(zt(z) for z in sorted(zs))}. Am {"weitesten links" if kleinste else "weitesten rechts"} steht {zt(r)}.',
                'h': f'Stell dir die Zahlengerade vor: Wer steht am weitesten {"links" if kleinste else "rechts"}?'}
    if s == 2:
        zs = R.sample(range(-60, -1), 3)
        kleinste = R.random() < .5
        r = min(zs) if kleinste else max(zs)
        a = [zt(z) for z in zs]
        return {'y': 'auswahl', 'f': {'text': f'Alle drei Zahlen sind negativ. Welche ist am {"kleinsten" if kleinste else "größten"}?'}, 'a': a, 'o': {'index': zs.index(r)},
                'w': f'Bei negativen Zahlen gilt: größerer Betrag = weiter links = kleiner. Reihenfolge: {" < ".join(zt(z) for z in sorted(zs))}. Gesucht ist {zt(r)}.',
                'h': 'Bei negativen Zahlen ist die mit dem größeren Betrag die kleinere.'}
    art = R.choice(['kette', 'aussage', 'fehler'])
    if art == 'kette':
        zs = R.sample(range(-20, 21), 4)
        if sum(z < 0 for z in zs) < 2: return g_ordnen(s)
        ri = sorted(zs)
        f1 = sorted(zs, key=abs)
        f2 = sorted([z for z in zs if z < 0], reverse=True) + sorted([z for z in zs if z >= 0])
        if f1 == ri or f2 == ri or f1 == f2: return g_ordnen(s)
        fmt = lambda l: ' < '.join(zt(z) for z in l)
        a, i = _rund(fmt(ri), [fmt(f1), fmt(f2)])
        return {'y': 'auswahl', 'f': {'text': 'Welche Kette ist richtig von klein nach groß geordnet?'}, 'a': a, 'o': {'index': i},
                'w': f'Zuerst die negativen Zahlen, die mit dem größten Betrag ganz links, dann die positiven: {fmt(ri)}.',
                'h': 'Ordne erst die negativen Zahlen (größter Betrag zuerst), dann die positiven.'}
    x, y = R.sample(range(2, 40), 2)
    lo, hi = -max(x, y), -min(x, y)
    if art == 'aussage':
        a, i = _rund(f'{zt(lo)} < {zt(hi)}', [f'{zt(lo)} > {zt(hi)}', f'{zt(lo)} = {zt(-lo)}'])
        return {'y': 'auswahl', 'f': {'text': 'Welche Aussage stimmt?'}, 'a': a, 'o': {'index': i},
                'w': f'{zt(lo)} liegt links von {zt(hi)}, also {zt(lo)} < {zt(hi)}. Eine Zahl und ihre Gegenzahl sind nicht gleich.',
                'h': 'Welche der beiden Zahlen steht weiter links auf der Zahlengeraden?'}
    if R.random() < .5:
        p = R.randint(1, 15)
        text = f'Jemand ordnet: {zt(hi)} < {zt(lo)} < {p}. Was ist falsch?'
        r, f = f'{zt(lo)} ist kleiner als {zt(hi)}. Richtig: {zt(lo)} < {zt(hi)} < {p}', [f'{p} muss ganz links stehen.', 'Nichts, die Kette stimmt.']
    else:
        text = f'Jemand schreibt: {zt(lo)} > {zt(hi)}, weil {-lo} > {-hi}. Stimmt das?'
        r, f = f'Nein: {zt(lo)} liegt links von {zt(hi)}, also {zt(lo)} < {zt(hi)}.', [f'Ja, weil {-lo} größer ist als {-hi}.', f'Nein: {zt(lo)} und {zt(hi)} sind gleich groß.']
    a, i = _rund(r, f)
    return {'y': 'auswahl', 'f': {'text': text}, 'a': a, 'o': {'index': i},
            'w': f'{zt(lo)} hat den größeren Betrag und liegt deshalb weiter links: {zt(lo)} < {zt(hi)}. Wer nur die Beträge vergleicht, ordnet negative Zahlen falsch herum.',
            'h': 'Bei negativen Zahlen: Größerer Betrag heißt weiter links.'}


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
        art = R.choice(['summe', 'weit', 'gegen'])
        if art == 'summe':
            a, b = R.choice([-1, 1]) * R.randint(2, 30), -R.randint(2, 30)
            return {'y': 'zahl', 'f': {'text': f'Berechne |{zt(a)}| + |{zt(b)}|.'}, 'o': {'wert': abs(a) + abs(b)}, 'c': f'abs({a}) + abs({b})',
                    'w': f'|{zt(a)}| = {abs(a)} und |{zt(b)}| = {abs(b)}. Zusammen {abs(a)} + {abs(b)} = {abs(a) + abs(b)}.', 'h': 'Bestimme zuerst jeden Betrag einzeln.'}
        if art == 'weit':
            aw, i = _rund(str(n), [zt(-n), str(2 * n)])
            return {'y': 'auswahl', 'f': {'text': f'Wie weit ist {zt(-n)} von der 0 entfernt?'}, 'a': aw, 'o': {'index': i},
                    'w': f'Der Abstand zur 0 ist der Betrag: |{zt(-n)}| = {n}. Ein Abstand ist nie negativ. {2 * n} wäre der Weg von {zt(-n)} bis {n}.', 'h': 'Ein Abstand ist nie negativ.'}
        if R.random() < .12:
            aw, i = _rund('0', ['1', 'Es gibt keine.'])
            return {'y': 'auswahl', 'f': {'text': 'Was ist die Gegenzahl von 0?'}, 'a': aw, 'o': {'index': i},
                    'w': 'Die 0 hat den Abstand 0 zur 0. Auf der anderen Seite liegt wieder die 0. Die Gegenzahl von 0 ist 0.',
                    'h': 'Wie weit ist die 0 von der 0 weg?'}
        z = R.choice([-n, n])
        aw, i = _rund(zt(-z), [zt(z), '0'])
        return {'y': 'auswahl', 'f': {'text': f'Was ist die Gegenzahl von {zt(z)}?'}, 'a': aw, 'o': {'index': i},
                'w': f'Gegenzahl: gleicher Abstand zur 0, anderes Vorzeichen. Die Gegenzahl von {zt(z)} ist {zt(-z)}.',
                'h': 'Die Gegenzahl hat das andere Vorzeichen.'}
    art = R.choice(['zwei', 'diff', 'beides'])
    if art == 'zwei':
        a, i = _rund(f'{n} und {zt(-n)}', [f'nur {n}', f'nur {zt(-n)}'])
        return {'y': 'auswahl', 'f': {'text': f'Welche Zahlen haben den Betrag {n}?'}, 'a': a, 'o': {'index': i},
                'w': f'Zwei Zahlen sind {n} Schritte von der 0 entfernt: {n} rechts und {zt(-n)} links.', 'h': 'Schau auf beide Seiten der 0.'}
    if art == 'beides':
        z = R.choice([-n, n])
        r = f'Betrag {n}, Gegenzahl {zt(-z)}'
        f = [f'Betrag {zt(-n)}, Gegenzahl {zt(-z)}', f'Betrag {n}, Gegenzahl {zt(z)}']
        a, i = _rund(r, f)
        return {'y': 'auswahl', 'f': {'text': f'Welche Aussage über die Zahl {zt(z)} stimmt?'}, 'a': a, 'o': {'index': i},
                'w': f'Der Betrag ist der Abstand zur 0: {n} (nie negativ). Die Gegenzahl hat das andere Vorzeichen: {zt(-z)}.',
                'h': 'Betrag: wie weit weg von der 0? Gegenzahl: anderes Vorzeichen.'}
    a, b = -R.randint(20, 60), -R.randint(2, 19)
    return {'y': 'zahl', 'f': {'text': f'Berechne |{zt(a)}| − |{zt(b)}|.'}, 'o': {'wert': abs(a) - abs(b)}, 'c': f'abs({a}) - abs({b})',
            'w': f'|{zt(a)}| = {abs(a)} und |{zt(b)}| = {abs(b)}. {abs(a)} − {abs(b)} = {abs(a) - abs(b)}.', 'h': 'Bestimme zuerst jeden Betrag einzeln.'}


def _add_weg(a, b):
    if (a < 0) == (b < 0):
        return f'Gleiche Vorzeichen: Beträge addieren, {abs(a)} + {abs(b)} = {abs(a) + abs(b)}. Das Vorzeichen bleibt: {zt(a + b)}.'
    gr, k = max(abs(a), abs(b)), min(abs(a), abs(b))
    if a + b == 0: return 'Verschiedene Vorzeichen und gleiche Beträge: Die Zahlen heben sich auf, Ergebnis 0.'
    return f'Verschiedene Vorzeichen: Beträge subtrahieren, {gr} − {k} = {gr - k}. Der größere Betrag ({gr}) gehört zur {"negativen" if a + b < 0 else "positiven"} Zahl, also {zt(a + b)}.'


def _add_rechnen(g):
    a, b = R.randint(-g, g), R.randint(-g, g)
    if (a >= 0 and b >= 0) or 0 in (a, b): return _add_rechnen(g)
    return {'y': 'zahl', 'f': {'text': f'Berechne {kl(a)} + {kl(b)}.'}, 'o': {'wert': a + b}, 'c': f'({a}) + ({b})', 'w': _add_weg(a, b),
            'h': 'Vergleiche die Vorzeichen. Gleich: Beträge addieren. Verschieden: Beträge subtrahieren.'}


def _add_vorzeichen(g):
    x, y = R.sample(range(2, g), 2)
    a, b = (-x, y) if R.random() < .5 else (y, -x)
    e = a + b
    r = 'negativ' if e < 0 else 'positiv'
    aw, i = _rund(r, ['positiv' if e < 0 else 'negativ', 'genau 0'])
    gr = a if abs(a) > abs(b) else b
    return {'y': 'auswahl', 'f': {'text': f'Ist {kl(a)} + {kl(b)} positiv oder negativ? Entscheide, ohne auszurechnen.'}, 'a': aw, 'o': {'index': i},
            'w': f'Die Vorzeichen sind verschieden. Die Zahl mit dem größeren Betrag ist {zt(gr)}. Ihr Vorzeichen bekommt das Ergebnis: {r} (es ist {zt(e)}).',
            'h': 'Welche der beiden Zahlen ist weiter von der 0 weg?'}


def _add_ergaenzen(g):
    a = R.choice([-1, 1]) * R.randint(2, g)
    e = R.randint(-g, g)
    x = e - a
    if x == 0 or e == 0 or (a > 0 and e > 0): return _add_ergaenzen(g)
    text = R.choice([f'Welche Zahl musst du zu {zt(a)} addieren, um {zt(e)} zu erhalten?',
                     f'{kl(a)} + □ = {zt(e)}. Welche Zahl gehört in das Kästchen?'])
    return {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': x}, 'c': f'({e}) - ({a})',
            'w': f'Von {zt(a)} nach {zt(e)} auf der Zahlengeraden: {abs(x)} Schritte nach {"rechts" if x > 0 else "links"}, also {zt(x)}. Probe: {kl(a)} + {kl(x)} = {zt(e)} ✓',
            'h': 'Wie weit und in welche Richtung musst du auf der Zahlengeraden gehen?'}


def g_addieren(s):
    if s == 1: return _add_rechnen(12)
    if s == 2: return _add_rechnen(60) if R.random() < .75 else _add_vorzeichen(60)
    return R.choice([lambda: _add_rechnen(400), lambda: _add_ergaenzen(60), lambda: _add_vorzeichen(400)])()


def _sub_rechnen(g):
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


def _sub_abstand(g):
    a, b = sorted(R.sample(range(-g, g + 1), 2))
    if a >= 0: return _sub_abstand(g)
    return {'y': 'zahl', 'f': {'text': f'Wie groß ist der Abstand zwischen {zt(a)} und {zt(b)} auf der Zahlengeraden?'},
            'o': {'wert': b - a}, 'c': f'({b}) - ({a})',
            'w': f'Abstand = größere Zahl − kleinere Zahl: {zt(b)} − {kl(a)} = {zt(b)} + {-a} = {b - a}.',
            'h': 'Rechne: größere Zahl minus kleinere Zahl.'}


def _sub_fehler():
    if R.random() < .5:
        a, b = R.choice([-1, 1]) * R.randint(2, 20), R.randint(2, 15)
        richtig, falsch = a + b, a - b
        text = f'Ein Kind rechnet {kl(a)} − ({zt(-b)}) = {zt(falsch)}. Was stimmt?'
        r = f'Falsch: − ({zt(-b)}) heißt + {b}. Richtig ist {zt(richtig)}.'
        f = ['Das Kind hat richtig gerechnet.', f'Falsch: Richtig ist {zt(-falsch)}.']
        w = f'({zt(-b)}) abziehen ist wie {b} € Schulden streichen – dadurch wird es mehr: {kl(a)} − ({zt(-b)}) = {kl(a)} + {b} = {zt(richtig)}.'
    else:
        a, b = R.randint(2, 20), R.randint(2, 20)
        if a == b: return _sub_fehler()
        richtig = -a - b
        text = f'Ein Kind rechnet ({zt(-a)}) − {b} = {a + b}, weil „Minus und Minus Plus ergibt“. Was stimmt?'
        r = f'Falsch: Hier wird keine negative Zahl abgezogen. ({zt(-a)}) − {b} = ({zt(-a)}) + ({zt(-b)}) = {zt(richtig)}.'
        f = ['Das Kind hat richtig gerechnet.', f'Falsch: Richtig ist {zt(b - a)}.']
        w = f'Von {zt(-a)} gehst du {b} Schritte nach links: ({zt(-a)}) − {b} = {zt(richtig)}. „Minus mal Minus“ gilt nur, wenn eine negative Zahl abgezogen wird.'
    aw, i = _rund(r, f)
    return {'y': 'auswahl', 'f': {'text': text}, 'a': aw, 'o': {'index': i}, 'w': w,
            'h': 'Wird hier eine negative Zahl abgezogen oder eine positive?'}


def g_subtrahieren(s):
    if s == 1: return _sub_rechnen(12)
    if s == 2: return _sub_rechnen(60) if R.random() < .75 else _sub_abstand(30)
    return R.choice([lambda: _sub_rechnen(400), _sub_fehler, lambda: _sub_abstand(80)])()


def _liste(sing, pl, werte):
    if not werte: return f'{pl}: keine.'
    if len(werte) == 1: return f'{sing}: {werte[0]}.'
    return f'{pl}: {" + ".join(map(str, werte))} = {sum(werte)}.'


def _sammeln(werte):
    plus, minus = [w for w in werte if w > 0], [-w for w in werte if w < 0]
    P, M = sum(plus), sum(minus)
    schluss = f'Ergebnis: {zt(-M)}.' if not plus else (f'Ergebnis: {P}.' if not minus else f'{P} − {M} = {zt(P - M)}.')
    return f'{_liste("Plus-Zahl", "Plus-Zahlen", plus)} {_liste("Minus-Zahl", "Minus-Zahlen", minus)} {schluss}'


def _geschickt():
    p = R.randint(11, 60)
    if R.random() < .5:
        a, y = R.randint(10, 60), R.randint(5, 50)
        if len({a, p, y}) < 3: return _geschickt()
        werte, text = [a, -p, p, -y], f'{a} − {p} + {p} − {y}'
    else:
        q, r = R.randint(10, 60), R.randint(3, 30)
        if len({p, q, r}) < 3: return _geschickt()
        werte, text = [-p, q, p, -r], f'({zt(-p)}) + {q} + {p} − {r}'
    rest = [w for w in werte if abs(w) != p]
    e = sum(werte)
    return {'y': 'zahl', 'f': {'text': f'Berechne geschickt: {text}.'}, 'o': {'wert': e}, 'c': ' + '.join(f'({w})' for w in werte),
            'w': f'{zt(-p)} und +{p} sind Gegenzahlen und heben sich auf. Übrig bleibt {zt(rest[0])} {"+" if rest[1] > 0 else "−"} {abs(rest[1])} = {zt(e)}.',
            'h': 'Suche zwei Zahlen, die zusammen 0 ergeben.'}


def g_ketten(s):
    if s == 3 and R.random() < .4: return _geschickt()
    if s == 2 and R.random() < .25: return _geschickt()
    n = {1: 3, 2: 4, 3: 4}[s]
    g = {1: 12, 2: 25, 3: 40}[s]
    zs = [R.choice([-1, 1]) * R.randint(1, g) for _ in range(n)]
    if all(z > 0 for z in zs[1:]) or len(set(map(abs, zs))) < n: return g_ketten(s)
    if s < 3:
        text = zt(zs[0]) + ''.join(f' {"+" if z > 0 else "−"} {abs(z)}' for z in zs[1:])
        ops = None
    else:
        ops = [R.choice('+-') for _ in zs[1:]]
        if not any(o == '-' and z < 0 for o, z in zip(ops, zs[1:])): return g_ketten(s)
        text = zt(zs[0]) + ''.join(f' {"+" if o == "+" else "−"} {kl(z)}' for o, z in zip(ops, zs[1:]))
    werte = [zs[0]] + [z if (ops is None or o == '+') else -z for o, z in zip(ops or ['+'] * (n - 1), zs[1:])]
    ohne = zt(werte[0]) + ''.join(f' {"+" if w > 0 else "−"} {abs(w)}' for w in werte[1:])
    weg = (f'Ohne Klammern: {ohne}. ' if ops else '') + _sammeln(werte)
    tipp = ('Löse zuerst alle Klammern auf. Sammle dann die Plus-Zahlen und die Minus-Zahlen getrennt.' if ops
            else 'Sammle die Plus-Zahlen und die Minus-Zahlen getrennt.')
    return {'y': 'zahl', 'f': {'text': f'Berechne {text}.'}, 'o': {'wert': sum(werte)}, 'c': ' + '.join(f'({w})' for w in werte), 'w': weg, 'h': tipp}


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
        arten = ['rueck_temp', 'rueck_konto'] + (['konto', 'konto'] if KONTO['n'] < 8 else [])
        art = R.choice(arten)
        if art == 'konto':
            a, x, y = -R.randint(1, 9) * 10, R.randint(1, 12) * 5, R.randint(1, 12) * 5
            if x == y: return g_sach(s)
            KONTO['n'] += 1
            text = f'Der Kontostand ist {zt(a)} €. Dann werden {x} € eingezahlt und {y} € abgehoben. Wie ist der Kontostand jetzt?'
            return {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': a + x - y, 'einheit': '€'}, 'c': f'({a}) + {x} - {y}',
                    'w': f'Einzahlen ist Plus, abheben ist Minus: {zt(a)} + {x} = {zt(a + x)}; {zt(a + x)} − {y} = {zt(a + x - y)}.',
                    'h': 'Einzahlen ist Plus, abheben ist Minus. Rechne Schritt für Schritt.'}
        if art == 'rueck_temp':
            d, e = R.randint(3, 15), R.randint(-12, 6)
            if e == 0: return g_sach(s)
            sturz = R.random() < .6
            v = e + d if sturz else e - d
            if e > 0 and v > 0: return g_sach(s)
            text = (f'Nach einem Temperatursturz um {d} Grad sind es {zt(e)} °C. Wie warm war es vorher?' if sturz
                    else f'Die Temperatur ist um {d} Grad gestiegen. Jetzt sind es {zt(e)} °C. Wie warm war es vorher?')
            return {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': v, 'einheit': '°C'}, 'c': f'({e}) {"+" if sturz else "-"} {d}',
                    'w': f'Rückwärts rechnen: Die Änderung umkehren. {"Es wurde kälter, also vorher wärmer" if sturz else "Es wurde wärmer, also vorher kälter"}: {zt(e)} {"+" if sturz else "−"} {d} = {zt(v)}.',
                    'h': 'Rechne rückwärts: Mache die Änderung rückgängig.'}
        x, y = R.randint(4, 24) * 5, R.randint(1, 12) * 5
        ab = R.random() < .6
        v = -y + x if ab else -y - x
        text = (f'Nach einer Abhebung von {x} € steht das Konto auf {zt(-y)} €. Wie hoch war der Kontostand vorher?' if ab
                else f'Nach einer Einzahlung von {x} € steht das Konto immer noch auf {zt(-y)} €. Wie hoch war der Kontostand vorher?')
        if v == 0: return g_sach(s)
        return {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': v, 'einheit': '€'}, 'c': f'({-y}) {"+" if ab else "-"} {x}',
                'w': f'Rückwärts rechnen: Die {"Abhebung" if ab else "Einzahlung"} rückgängig machen. {zt(-y)} {"+" if ab else "−"} {x} = {zt(v)}.',
                'h': 'Rechne rückwärts: Mache die Änderung rückgängig.'}
    if R.random() < .5:
        a, b = -R.randint(2, 20), -R.randint(21, 60)
        text = f'Ein U-Boot taucht von {zt(a)} m auf {zt(b)} m. Um wie viele Meter ist es tiefer gegangen?'
        return {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': a - b, 'einheit': 'm'}, 'c': f'({a}) - ({b})',
                'w': f'Unterschied der beiden Höhen: {zt(a)} − {kl(b)} = {zt(a)} + {-b} = {a - b}.',
                'h': 'Gesucht ist der Abstand der beiden Zahlen auf der Zahlengeraden.'}
    a, d1, d2, d3 = -R.randint(1, 10), R.randint(3, 12), R.randint(2, 9), R.randint(5, 15)
    if len({-a, d1, d2, d3}) < 4: return g_sach(s)
    t1, t2 = a + d1, a + d1 - d2
    e = t2 - d3
    text = f'Um 6 Uhr sind es {zt(a)} °C. Bis mittags wird es {d1} Grad wärmer, bis abends {d2} Grad kälter und in der Nacht noch einmal {d3} Grad kälter. Wie kalt ist es in der Nacht?'
    return {'y': 'zahl', 'f': {'text': text}, 'o': {'wert': e, 'einheit': '°C'}, 'c': f'({a}) + {d1} - {d2} - {d3}',
            'w': f'Schritt für Schritt: {zt(a)} + {d1} = {zt(t1)}; {zt(t1)} − {d2} = {zt(t2)}; {zt(t2)} − {d3} = {zt(e)}.',
            'h': 'Rechne Schritt für Schritt: erst mittags, dann abends, dann nachts.'}


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

# Umbau U5 (Achte Runde, Vorgabe 16.11.): Lernkarten nach dem neuen Muster – einstieg, woerter (≤ 3), Kartenbild,
# Bildergeschichte (schritte mit bild), „Pass auf!“ (fehler + fehler_bild), MERKE (regel). Situationen: Thermometer, Taschengeld.
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl5.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl5 import umbau  # noqa: E402

THERMO = {'typ': 'thermometer', 'start': -10, 'ende': 10, 'schritt': 5, 'bereich_unter_null': True, 'einheit': '°C'}
GERADE = {'typ': 'zahlenstrahl', 'start': -10, 'ende': 10, 'abschnitte': 20, 'beschriftet': 'anfang_ende'}

KARTEN = {
 'deuten': {
  'einstieg': 'Im Winter zeigt das Thermometer morgens 3 Grad unter null. Dann friert die Pfütze zu. Für Werte unter null schreibt man ein Minus vor die Zahl: ⟦negative Zahlen⟧.',
  'woerter': [['negative Zahl', 'eine Zahl unter null, mit Minus davor, zum Beispiel −3'], ['−3 °C', 'gelesen „minus drei Grad“: 3 Grad unter null']],
  'bild': THERMO,
  'schritte': [{'text': 'Das Thermometer zeigt 3 Grad unter null.', 'bild': {'stand': -3}},
               {'text': 'Unter null heißt: Vor die Zahl kommt ein Minus.'},
               {'text': 'Man schreibt ⟦−3 °C⟧ und sagt „minus drei Grad“.'}],
  'fehler': 'Das Minus vergessen: 3 °C ist etwas ganz anderes. Bei 3 °C taut der Schnee, bei −3 °C friert die Pfütze.',
  'fehler_bild': {'stand': 3},
  'regel': 'Unter null schreibst du ein ⟦Minus⟧ vor die Zahl. 3 Grad unter null sind −3 °C, 5 € Schulden sind −5 €.'},
 'zahlengerade': {
  'einstieg': 'Ein Thermometer kannst du dir auch quer gelegt denken. Dann stehen die Zahlen unter null links und die über null rechts. So eine Linie heißt ⟦Zahlengerade⟧.',
  'woerter': [['Zahlengerade', 'eine Linie mit allen Zahlen der Reihe nach – wie ein liegendes Thermometer'], ['Abschnitt', 'das Stück zwischen zwei Strichen; alle sind gleich lang']],
  'bild': {'typ': 'zahlenstrahl', 'start': -10, 'ende': 10, 'abschnitte': 10, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': 'Gesucht ist der Strich für −4. Die Linie hat 10 Abschnitte.'},
               {'text': 'Von −10 bis 10 sind es 20, verteilt auf 10 Abschnitte: ⟦2⟧ je Abschnitt.', 'bild': {'bereich': {'von': -10, 'bis': -8}}},
               {'text': 'Von −10 aus in Zweierschritten: −8, −6, ⟦−4⟧.',
                'bild': {'bereich': [], 'boegen': [{'von': -10, 'bis': -8}, {'von': -8, 'bis': -6}, {'von': -6, 'bis': -4}], 'punkte': [{'wert': -4}]}}],
  'fehler': 'Jeden Strich als 1 zählen ergibt −7 statt −4. Wie am Thermometer: Erst schauen, wie viel ein Strich wert ist.',
  'fehler_bild': {'boegen': [], 'punkte': [{'wert': -7, 'name': 'falsch'}]},
  'regel': 'Erst ausrechnen, wie viel ⟦ein Abschnitt⟧ wert ist. Dann vom Anfang aus in diesen Schritten zählen.'},
 'ordnen': {
  'einstieg': 'Morgens sind es −8 °C, abends −3 °C. Morgens ist es kälter, das Thermometer steht tiefer. Auf der Zahlengeraden heißt tiefer: weiter links, also ⟦kleiner⟧.',
  'woerter': [['<', '„ist kleiner als“: Die Spitze zeigt zur kleineren Zahl'], ['Zahlengerade', 'eine Linie mit allen Zahlen der Reihe nach – wie ein liegendes Thermometer']],
  'bild': GERADE,
  'schritte': [{'text': 'Trage −8 und −3 auf der Zahlengeraden ein.', 'bild': {'punkte': [{'wert': -8, 'name': 'morgens'}, {'wert': -3, 'name': 'abends'}]}},
               {'text': '−8 liegt weiter links als −3.'},
               {'text': 'Weiter links heißt kleiner: ⟦−8 < −3⟧.'}],
  'fehler': '„−8 ist größer, weil 8 mehr ist als 3“ ist falsch. −8 °C ist kälter als −3 °C. Mehr Minus heißt kleiner.',
  'fehler_bild': dict(THERMO, stand=-8),
  'regel': 'Weiter links auf der Zahlengeraden ist ⟦kleiner⟧. Jede negative Zahl ist kleiner als 0.'},
 'betrag': {
  'einstieg': 'Ein Taucher ist 7 m unter Wasser, ein Vogel fliegt 7 m darüber. Beide sind gleich weit von der Wasseroberfläche weg. Diese Entfernung von der 0 heißt ⟦Betrag⟧.',
  'woerter': [['Betrag', 'wie weit eine Zahl von der 0 weg ist – immer ohne Minus'], ['|−7|', 'gelesen „Betrag von minus sieben“'],
              ['Gegenzahl', 'gleich weit von der 0 weg, aber auf der anderen Seite: zu −7 gehört 7']],
  'bild': GERADE,
  'schritte': [{'text': 'Der Taucher ist bei −7 m, der Vogel bei 7 m.', 'bild': {'punkte': [{'wert': -7, 'name': 'Taucher'}, {'wert': 7, 'name': 'Vogel'}]}},
               {'text': 'Von −7 bis 0 sind es 7 Schritte. Also ist ⟦|−7| = 7⟧.', 'bild': {'boegen': [{'von': -7, 'bis': 0, 'name': '7'}]}},
               {'text': 'Der Vogel ist auf der anderen Seite: 7 ist die ⟦Gegenzahl⟧ von −7.',
                'bild': {'boegen': [{'von': -7, 'bis': 0, 'name': '7'}, {'von': 0, 'bis': 7, 'name': '7'}]}}],
  'fehler': '|−7| = −7 ist falsch. Der Betrag fragt nur: Wie weit weg? Ein Abstand ist nie kleiner als null.',
  'fehler_bild': {'boegen': [{'von': -7, 'bis': 0, 'name': '7, nicht −7'}]},
  'regel': 'Beim ⟦Betrag⟧ lässt du das Minus weg: |−7| = 7. Die Gegenzahl liegt gegenüber: Zu −7 gehört 7.'},
 'addieren': {
  'einstieg': 'Du hast 7 € Schulden und bekommst 4 € geschenkt. Die zahlst du sofort zurück. Etwas dazuzählen heißt ⟦addieren⟧, auch bei negativen Zahlen.',
  'woerter': [['addieren', 'plus rechnen, etwas dazuzählen'], ['Schulden', 'Geld, das du jemandem zurückgeben musst'],
              ['(−7) + 4', 'gelesen „minus sieben plus vier“; die Klammer hält das Minus bei der 7']],
  'bild': GERADE,
  'schritte': [{'text': 'Rechne (−7) + 4. Die 7 € Schulden sind −7, dort startest du.', 'bild': {'punkte': [{'wert': -7, 'name': 'Start'}]}},
               {'text': 'Plus 4 heißt: 4 Schritte nach rechts.', 'bild': {'boegen': [{'von': -7, 'bis': -3, 'name': '+4'}]}},
               {'text': 'Du landest bei ⟦−3⟧. Es bleiben 3 € Schulden.', 'bild': {'punkte': [{'wert': -7, 'name': 'Start'}, {'wert': -3, 'name': 'Ziel'}]}},
               {'text': 'Abkürzung: 7 − 4 = 3. Die −7 ist weiter weg von 0, also ⟦−3⟧.'}],
  'fehler': '(−7) + 4 = −11 ist falsch. Wer 4 € bekommt, hat danach weniger Schulden, nicht mehr.',
  'fehler_bild': {'punkte': [{'wert': -7, 'name': 'Start'}], 'boegen': [{'von': -7, 'bis': -3, 'name': '+4 heißt nach rechts'}]},
  'regel': 'Plus heißt auf der Zahlengeraden ⟦nach rechts⟧. Plus eine negative Zahl heißt nach links: (−3) + (−5) = −8.'},
 'subtrahieren': {
  'einstieg': 'Du hast 3 € und kaufst etwas für 8 €. Danach fehlen dir 5 €. Abziehen heißt ⟦subtrahieren⟧ – auch negative Zahlen kann man abziehen.',
  'woerter': [['subtrahieren', 'minus rechnen, abziehen'], ['5 − (−3)', 'gelesen „fünf minus minus drei“: Die −3 wird abgezogen'],
              ['erlassen', 'Schulden streichen: Du musst sie nicht mehr zurückzahlen']],
  'bild': GERADE,
  'schritte': [{'text': '3 − 8: Starte bei 3 und gehe 8 Schritte nach links.', 'bild': {'punkte': [{'wert': 3, 'name': 'Start'}], 'boegen': [{'von': 3, 'bis': -5, 'name': '−8'}]}},
               {'text': 'Du landest bei ⟦−5⟧. Dir fehlen 5 €.', 'bild': {'punkte': [{'wert': 3, 'name': 'Start'}, {'wert': -5, 'name': 'Ziel'}]}},
               {'text': '5 − (−3): Werden dir 3 € Schulden erlassen, hast du 3 € mehr.',
                'bild': {'punkte': [{'wert': 5, 'name': 'Start'}], 'boegen': [{'von': 5, 'bis': 8, 'name': '+3'}]}},
               {'text': 'Minus minus 3 wird plus 3: 5 + 3 = ⟦8⟧.', 'bild': {'punkte': [{'wert': 5, 'name': 'Start'}, {'wert': 8, 'name': 'Ziel'}]}}],
  'fehler': '5 − (−3) = 2 ist falsch. Abgezogen werden 3 € Schulden, nicht 3 €. Weniger Schulden heißt mehr Geld.',
  'fehler_bild': {'punkte': [{'wert': 5, 'name': 'Start'}], 'boegen': [{'von': 5, 'bis': 2, 'name': 'falsche Richtung'}]},
  'regel': 'Minus eine Zahl heißt: plus die ⟦Gegenzahl⟧. 3 − 8 = 3 + (−8) und 5 − (−3) = 5 + 3.'},
 'ketten': {
  'einstieg': 'Deine Woche: 12 € bekommen, 5 € Schulden erlassen, 9 € und 4 € ausgegeben. Wie viel ist übrig? Viele Plus- und Minus-Schritte hintereinander heißen ⟦Rechenkette⟧.',
  'woerter': [['Rechenkette', 'mehrere Plus- und Minusrechnungen hintereinander'], ['Klammer auflösen', '„+ (−9)“ als „− 9“ schreiben und „− (−5)“ als „+ 5“']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 20, 'abschnitte': 20, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': 'Rechne 12 − (−5) + (−9) − 4. Zuerst jede Klammer auflösen.'},
               {'text': 'Aus − (−5) wird + 5, aus + (−9) wird − 9.'},
               {'text': 'Plus-Zahlen: 12 + 5 = 17. Minus-Zahlen: 9 + 4 = 13.', 'bild': {'boegen': [{'von': 0, 'bis': 17, 'name': '+17'}]}},
               {'text': '17 − 13 = ⟦4⟧. Es sind 4 € übrig.',
                'bild': {'boegen': [{'von': 0, 'bis': 17, 'name': '+17'}, {'von': 17, 'bis': 4, 'name': '−13'}], 'punkte': [{'wert': 4, 'name': 'übrig'}]}}],
  'fehler': 'Eine Klammer vergessen: 12 + 5 + 9 − 4 = 22 ist falsch. Die 9 € hast du ausgegeben, nicht bekommen.',
  'regel': 'Erst ⟦jede Klammer auflösen⟧, dann rechnen. Plus-Zahlen und Minus-Zahlen getrennt sammeln und voneinander abziehen.'},
 'sach': {
  'einstieg': 'Die Wetter-App sagt: morgens −4 °C, bis mittags 7 Grad wärmer. Wie warm ist es mittags? Rechenaufgaben als kleine Geschichte heißen ⟦Sachaufgaben⟧.',
  'woerter': [['Sachaufgabe', 'eine Rechenaufgabe, die als kleine Geschichte erzählt wird'], ['Startwert', 'die Zahl, mit der die Geschichte beginnt']],
  'bild': THERMO,
  'schritte': [{'text': 'Der Startwert ist −4 °C.', 'bild': {'stand': -4}},
               {'text': '7 Grad wärmer heißt plus 7: −4 + 7.'},
               {'text': 'Das Thermometer steigt um 7 Grad auf ⟦3 °C⟧.', 'bild': {'stand': 3}}],
  'fehler': 'Den Startwert ohne Minus nehmen: 4 + 7 = 11 ist falsch. Morgens waren es 4 Grad unter null, nicht darüber.',
  'fehler_bild': {'stand': 4, 'name': 'falsch: 4 °C'},
  'regel': 'Erst den ⟦Startwert⟧ hinschreiben, dann jede Änderung. Wärmer, einzahlen, steigen ist plus. Kälter, abheben, sinken ist minus.'},
}
umbau(DATEI, KARTEN)


if __name__ == '__main__':
    schreibe(DATEI, 'zahlen.ganz.json')
