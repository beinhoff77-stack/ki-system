#!/usr/bin/env python3
"""Direkte Proportionalität und Dreisatz (Gymnasium Kl. 5): proportionale Zuordnungen erkennen, Tabellen ergänzen,
auf die Einheit schließen, Dreisatz, geschickte Zwischenschritte, Sachaufgaben mit Fallen.
Indirekte Proportionalität (Produktgleichheit) gehört zum Thema groessen.indirekt (Kl. 8)."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl5 import baue, mische, mische_rund, schreibe, zt  # noqa: E402

R = random.Random(26)

# (Ding Einzahl, Mehrzahl, Einheit vorn, Größe hinten, Einheit hinten, Preis je Stück wählbar)
WAREN = [('Heft', 'Hefte', '', 'kosten', '€', [2, 3, 4]), ('kg Äpfel', 'kg Äpfel', '', 'kosten', '€', [2, 3, 4]), ('Brötchen', 'Brötchen', '', 'kosten', 'ct', [30, 40, 45, 60]),
         ('Liter Farbe', 'Liter Farbe', '', 'reichen für', 'm²', [6, 8, 12]), ('Stunde', 'Stunden', '', 'fährt ein Radfahrer', 'km', [12, 15, 18]),
         ('Packung', 'Packungen', '', 'enthalten', 'Kekse', [12, 16, 24]), ('Minute', 'Minuten', '', 'laufen aus dem Hahn', 'Liter', [6, 8, 9]),
         ('Schritt', 'Schritte', '', 'sind', 'cm', [60, 65, 70, 75]), ('Karte', 'Eintrittskarten', '', 'kosten', '€', [7, 9, 12, 14])]


def satz(w, n, wert, frage=False):
    ding = w[0] if n == 1 else w[1]
    if w[3] == 'fährt ein Radfahrer': return f'In {n} {ding if n > 1 else "Stunde"} fährt ein Radfahrer {"wie viele" if frage else zt(wert)} km'
    if w[3] == 'laufen aus dem Hahn': return f'In {n} {ding} {"laufen" if frage or wert != 1 else "läuft"} {"wie viele" if frage else zt(wert)} Liter aus dem Hahn'
    if w[4] == 'ct' and not frage and wert >= 1000: return f'{n} {ding} {"kostet" if n == 1 else "kosten"} {wert // 100},{wert % 100:02d} €'
    verb = {'kosten': 'kostet' if n == 1 else 'kosten', 'reichen für': 'reicht für' if n == 1 else 'reichen für', 'enthalten': 'enthält' if n == 1 else 'enthalten', 'sind': 'ist' if n == 1 else 'sind'}[w[3]]
    return f'{n} {ding} {verb} {"wie viel" if frage and w[4] in ("€", "ct") else ("wie viele" if frage else zt(wert))} {w[4]}'


# Erklärungen: Fassung der Prüfung (inhalte/pruefung/erklaerungen/groessen.proportional.json) übernommen,
# Karte pruefen hinter vervielfachen gesetzt (erst erkennen und prüfen, dann rechnen).
ETAPPEN = [
    {
        "lernziel": "erkennen",
        "titel": "Was heißt proportional?",
        "regel": "Eine Zuordnung ist ⟦proportional⟧, wenn gilt: doppelte Menge → doppelter Preis, dreifache Menge → dreifacher Preis, halbe Menge → halber Preis. Dazu gehört auch: ⟦nichts kaufen kostet 0 €⟧.",
        "schritte": [
            "1 Brötchen kostet 40 ct. 2 Brötchen kosten 80 ct, 3 Brötchen 120 ct.",
            "Doppelt so viele Brötchen kosten doppelt so viel, dreimal so viele dreimal so viel.",
            "Die Zuordnung Anzahl → Preis ist ⟦proportional⟧."
        ],
        "fehler": "„Je mehr Kilometer, desto teurer – also proportional.“ Falsch beim Taxi: 4 € Grundgebühr plus 2 € pro km. 1 km kostet 6 €, 2 km kosten 8 €, nicht 12 €. Wegen des festen Grundbetrags ist es ⟦nicht proportional⟧. „Je mehr, desto mehr“ reicht nicht – es muss ⟦genau das Doppelte⟧ sein.",
        "bild": {
            "typ": "tabelle",
            "kopf": [
                "Anzahl Brötchen",
                "0",
                "1",
                "2",
                "3"
            ],
            "zeilen": [
                [
                    "Preis",
                    "0 ct",
                    "40 ct",
                    "80 ct",
                    "120 ct"
                ]
            ]
        }
    },
    {
        "lernziel": "vervielfachen",
        "titel": "Verdoppeln, verdreifachen, halbieren",
        "regel": "Bei proportionalen Zuordnungen machst du auf ⟦beiden Seiten dasselbe⟧: Menge mal 3 → Wert mal 3. Menge geteilt durch 2 → Wert geteilt durch 2.",
        "schritte": [
            "3 kg Äpfel kosten 6 €. Gesucht: 9 kg.",
            "9 kg sind 3-mal so viel wie 3 kg.",
            "Also auch der Preis mal 3: 6 € · 3 = ⟦18 €⟧."
        ],
        "fehler": "Auf beiden Seiten dieselbe Zahl ⟦addieren⟧: Von 3 kg auf 9 kg sind es +6 kg, aber der Preis steigt nicht um 6 €. Gerechnet wird mit ⟦mal und geteilt⟧."
    },
    {
        "lernziel": "pruefen",
        "titel": "Ist die Tabelle proportional?",
        "regel": "In einer proportionalen Tabelle ist ⟦Preis geteilt durch Menge⟧ immer gleich. Diese Zahl ist der Preis für 1 Stück (1 kg, 1 Liter …).",
        "schritte": [
            "Rechne für jedes Paar Preis : Menge: 6 : 2 = 3, 15 : 5 = 3, 24 : 8 = 3.",
            "Immer 3 € pro kg: Die Tabelle ist ⟦proportional⟧."
        ],
        "fehler": "Nur die ersten beiden Paare prüfen. Bei 2 kg → 6 €, 4 kg → 12 €, 10 kg → 25 € stimmen die ersten beiden (je 3 € pro kg), aber 25 : 10 = 2,5. Beim Großeinkauf gibt es Rabatt: ⟦nicht proportional⟧. Prüfe ⟦alle⟧ Paare.",
        "bild": {
            "typ": "tabelle",
            "kopf": [
                "Menge",
                "2 kg",
                "5 kg",
                "8 kg"
            ],
            "zeilen": [
                [
                    "Preis",
                    "6 €",
                    "15 €",
                    "24 €"
                ],
                [
                    "Preis : Menge",
                    "3",
                    "3",
                    "3"
                ]
            ]
        }
    },
    {
        "lernziel": "einheit",
        "titel": "Auf die Einheit schließen",
        "regel": "Teile durch die Anzahl, dann weißt du den Wert für ⟦1 Stück⟧ (für 1 kg, 1 Stunde …). Das nennt man: auf die Einheit schließen.",
        "schritte": [
            "5 Hefte kosten 10 €.",
            "Beide Seiten geteilt durch 5: 1 Heft kostet 10 € : 5 = ⟦2 €⟧."
        ],
        "probe": "5 · 2 € = 10 € ✓",
        "fehler": "Falsch herum teilen: 5 : 10 statt 10 : 5. Geteilt wird der ⟦Wert⟧ durch die ⟦Anzahl⟧."
    },
    {
        "lernziel": "dreisatz",
        "titel": "Der Dreisatz",
        "regel": "Der Dreisatz hat ⟦drei Zeilen⟧: 1. Was du weißt. 2. Auf 1 Stück schließen: ⟦beide Seiten teilen⟧. 3. Auf das Gesuchte schließen: ⟦beide Seiten malnehmen⟧. Was du links tust, tust du auch rechts.",
        "schritte": [
            "Zeile 1: 4 kg Äpfel kosten 12 €.",
            "Zeile 2: Links : 4, also auch rechts : 4. 1 kg kostet 12 € : 4 = 3 €.",
            "Zeile 3: Links · 7, also auch rechts · 7. 7 kg kosten 3 € · 7 = ⟦21 €⟧."
        ],
        "probe": "Überschlag: 7 kg sind knapp das Doppelte von 4 kg. 21 € sind knapp das Doppelte von 12 € ✓",
        "fehler": "In Zeile 3 mit der alten Menge malnehmen: 3 € · 4 = 12 €. Das ist wieder der Preis für 4 kg! Gesucht sind 7 kg, also musst du mit ⟦7⟧ malnehmen: 3 € · 7 = 21 €.",
        "bild": {
            "typ": "tabelle",
            "kopf": [
                "",
                "Menge",
                "Preis"
            ],
            "zeilen": [
                [
                    "Zeile 1",
                    "4 kg",
                    "12 €"
                ],
                [
                    "Zeile 2 (: 4)",
                    "1 kg",
                    "3 €"
                ],
                [
                    "Zeile 3 (· 7)",
                    "7 kg",
                    "21 €"
                ]
            ]
        }
    },
    {
        "lernziel": "geschickt",
        "titel": "Geschickte Zwischenschritte",
        "regel": "Du musst nicht immer auf 1 gehen. Suche eine Zwischenmenge, die ⟦in beide Zahlen passt⟧: von 6 auf 9 geht es bequem über 3. Noch ein Trick: Bei proportionalen Zuordnungen darfst du ⟦Zeilen addieren⟧.",
        "schritte": [
            "6 Karten kosten 42 €. Gesucht: 9 Karten.",
            "3 Karten sind die Hälfte von 6 Karten: 42 € : 2 = 21 €.",
            "9 Karten sind 3 Karten mal 3: 21 € · 3 = ⟦63 €⟧.",
            "Oder mit dem Additions-Trick: 9 Karten = 6 Karten + 3 Karten, also 42 € + 21 € = ⟦63 €⟧."
        ],
        "probe": "Über 1 Karte: 42 € : 6 = 7 €, und 7 € · 9 = 63 € ✓",
        "fehler": "Eine Zwischenmenge nehmen, die nicht in beide Zahlen passt, z. B. 4: Von 6 Karten auf 4 Karten musst du durch 1,5 teilen – das ist schwerer als vorher. Die Zwischenmenge muss in ⟦beide⟧ Zahlen ohne Rest passen: 3 passt in 6 und in 9."
    },
    {
        "lernziel": "sach",
        "titel": "Sachaufgaben mit Dreisatz",
        "regel": "Prüfe zuerst: Ist die Zuordnung überhaupt ⟦proportional⟧? Erst dann rechnest du mit dem Dreisatz. Manche Aufgaben sind Fallen.",
        "schritte": [
            "Für 4 Personen braucht man 600 g Nudeln. Wie viel für 6 Personen?",
            "Doppelt so viele Personen essen doppelt so viel: proportional.",
            "2 Personen: 300 g. 6 Personen: 300 g · 3 = ⟦900 g⟧."
        ],
        "fehler": "„1 Ei kocht 8 Minuten, also kochen 3 Eier 24 Minuten“: falsch. Die Kochzeit hängt ⟦nicht⟧ von der Anzahl der Eier ab."
    }
]
TEIL = {'erkennen': 'begriff', 'pruefen': 'begriff', 'vervielfachen': 'tabelle', 'einheit': 'dreisatz', 'dreisatz': 'dreisatz', 'geschickt': 'dreisatz', 'sach': 'anwenden'}

PROP = ['Anzahl gleicher Brötchen → Preis', 'Benzinmenge → Preis an der Tankstelle', 'Anzahl gleicher Fliesen → bedeckte Fläche', 'Zeit bei gleichem Tempo → gefahrene Strecke',
        'Anzahl gleicher Flaschen → Gewicht der Flaschen', 'Seitenlänge eines Quadrats → Umfang', 'Anzahl gleicher Schritte → zurückgelegter Weg', 'Menge Wasser aus einem Hahn → Zeit, die der Hahn läuft']
NICHT = ['Alter eines Kindes → Körpergröße', 'Anzahl der Eier im Topf → Kochzeit', 'Seitenlänge eines Quadrats → Flächeninhalt', 'Anzahl der Geschwister → Taschengeld',
         'Tageszeit → Temperatur', 'Anzahl der Kerzen → Brenndauer der Kerzen', 'Anzahl der Musiker → Dauer des Liedes', 'Alter eines Autos → Wert des Autos',
         'Parkdauer → Parkgebühr, wenn die erste Stunde frei ist', 'Anzahl der Handtücher auf der Leine → Trockenzeit']
















# ---------- Prüfung eingearbeitet (inhalte/pruefung/aufgaben/groessen.proportional.json) ----------
def _rund(r, f): return mische_rund(R, r, f)


def euro(ct): return f'{ct // 100},{ct % 100:02d} €'


def ok(w, p, mengen, gesucht=None):
    """Realistisch: Radfahrer höchstens 6 Stunden; gesuchte Cent-Beträge unter 1 000 ct (sonst in Euro, siehe satz)."""
    if w[3] == 'fährt ein Radfahrer' and max(mengen) > 6: return False
    if w[4] == 'ct' and gesucht is not None and gesucht >= 1000: return False
    return True


TEIL_WORT = {2: 'die Hälfte', 3: 'ein Drittel', 4: 'ein Viertel', 5: 'ein Fünftel', 6: 'ein Sechstel'}

PROP_JA = [('Eine Packung enthält {p} Kekse.', 'Anzahl Packungen → Anzahl Kekse', [12, 16, 24], 'Kekse', 'Packungen'),
           ('Ein Heft kostet {p} €. Es gibt keinen Mengenrabatt.', 'Anzahl Hefte → Preis', [2, 3, 4], '€', 'Hefte'),
           ('Ein Schritt ist {p} cm lang.', 'Anzahl Schritte → Weg', [60, 65, 70, 75], 'cm', 'Schritte'),
           ('Eine Kiste wiegt {p} kg.', 'Anzahl gleicher Kisten → Gewicht', [5, 8, 12], 'kg', 'Kisten')]
PROP_NEIN = [('Eine Taxifahrt kostet {g} € Grundgebühr und {p} € je km.', 'Kilometer → Preis', 'km'),
             ('Ein Kletterpark kostet {g} € Eintritt und {p} € je Stunde.', 'Stunden → Preis', 'Stunden'),
             ('Ein Fahrradverleih kostet {g} € Grundgebühr und {p} € je Stunde.', 'Stunden → Preis', 'Stunden')]
GROESSE = {4: 103, 5: 110, 6: 116, 7: 122}


def g_erkennen(s):
    if s == 1:
        if R.random() < .5:
            a, i = _rund(R.choice(PROP), R.sample(NICHT, 2))
            return {'y': 'auswahl', 'f': {'text': 'Welche Zuordnung ist proportional?'}, 'a': a, 'o': {'index': i},
                    'w': f'Nur bei „{a[i]}“ gehört zum Doppelten immer genau das Doppelte.', 'h': 'Prüfe: Gehört zur doppelten Menge genau der doppelte Wert?'}
        a, i = _rund(R.choice(NICHT), R.sample(PROP, 2))
        return {'y': 'auswahl', 'f': {'text': 'Welche Zuordnung ist nicht proportional?'}, 'a': a, 'o': {'index': i},
                'w': f'Bei „{a[i]}“ gehört zum Doppelten nicht das Doppelte. Die beiden anderen sind proportional.', 'h': 'Prüfe: Gehört zur doppelten Menge genau der doppelte Wert?'}
    if s == 2:
        art = R.choice(['quadrat', 'alter', 'ja', 'ja'])
        if art == 'quadrat':
            x = R.randint(2, 6)
            text = f'Ein Quadrat mit {x} cm Seitenlänge hat {x * x} cm² Fläche, eines mit {2 * x} cm Seitenlänge hat {4 * x * x} cm². Ist Seitenlänge → Flächeninhalt proportional?'
            r, f = 'Nein, doppelte Seite gibt vierfache Fläche.', ['Ja, je länger die Seite, desto größer die Fläche.', 'Ja, beide Zahlen werden größer.']
            w = f'Zum Doppelten der Seite ({x} → {2 * x} cm) gehört das Vierfache der Fläche ({x * x} → {4 * x * x} cm²), nicht das Doppelte. „Je mehr, desto mehr“ reicht nicht.'
        elif art == 'alter':
            a = R.choice(list(GROESSE))
            text = f'Mit {a} Jahren ist ein Kind {GROESSE[a]} cm groß. Ist es mit {2 * a} Jahren {2 * GROESSE[a]} cm groß?'
            r, f = 'Nein, Alter und Größe sind nicht proportional.', ['Ja, doppeltes Alter heißt doppelte Größe.', 'Ja, weil Kinder mit dem Alter wachsen.']
            w = f'{2 * GROESSE[a]} cm wären über {zt(2 * GROESSE[a] // 100)} m – so groß ist kein Kind mit {2 * a} Jahren. Das Kind wächst zwar, aber nicht auf das Doppelte.'
        else:
            n, kg = R.randint(2, 6), R.choice([1, 2, 3])
            text = f'{n} gleiche Flaschen Saft wiegen zusammen {n * kg} kg, {2 * n} solche Flaschen wiegen {2 * n * kg} kg. Ist Anzahl → Gewicht proportional?'
            r, f = 'Ja, zum Doppelten gehört genau das Doppelte.', ['Nein, das Gewicht wird ja größer.', 'Nein, man braucht dafür eine Grundgebühr.']
            w = f'{2 * n} Flaschen sind doppelt so viele wie {n}, und {2 * n * kg} kg ist genau das Doppelte von {n * kg} kg. Jede Flasche wiegt gleich viel: proportional.'
        aw, i = _rund(r, f)
        return {'y': 'auswahl', 'f': {'text': text}, 'a': aw, 'o': {'index': i}, 'w': w, 'h': 'Prüfe mit den Zahlen: Gehört zum Doppelten genau das Doppelte?'}
    art = R.choice(['zahlen', 'entscheiden', 'entscheiden', 'quadrat'])
    if art == 'zahlen':
        satz_, was, ein = R.choice(PROP_NEIN); g, p, n = R.randint(2, 5), R.randint(1, 3), R.randint(1, 3)
        if g == p: return g_erkennen(s)
        t = satz_.format(g=g, p=p)
        r = 'Nein, denn für das Doppelte zahlt man nicht das Doppelte.'
        jede = 'jeder Kilometer' if ein == 'km' else 'jede Stunde'
        e1 = ein if n > 1 or ein == 'km' else 'Stunde'
        aw, i = _rund(r, ['Ja, denn der Preis wird größer.', f'Ja, denn {jede} kostet gleich viel.'])
        return {'y': 'auswahl', 'f': {'text': f'{t} {n} {e1}: {g + p * n} €, {2 * n} {ein}: {g + 2 * p * n} €. Ist {was} proportional?'}, 'a': aw, 'o': {'index': i},
                'w': f'Proportional wäre: {2 * n} {ein} kosten 2 · {g + p * n} € = {2 * (g + p * n)} €. Es sind aber {g + 2 * p * n} €. Die feste Gebühr von {g} € zahlt man nur einmal.',
                'h': 'Vergleiche: Kostet das Doppelte auch doppelt so viel?'}
    if art == 'quadrat':
        x = R.randint(2, 9)
        a, i = _rund('Der Umfang verdoppelt sich, der Flächeninhalt vervierfacht sich', ['Umfang und Flächeninhalt verdoppeln sich', 'Umfang und Flächeninhalt vervierfachen sich'])
        return {'y': 'auswahl', 'f': {'text': f'Ein Quadrat hat die Seitenlänge {x} cm. Die Seitenlänge wird verdoppelt. Was stimmt?'}, 'a': a, 'o': {'index': i},
                'w': f'Umfang: 4 · {x} = {4 * x} cm, danach 4 · {2 * x} = {8 * x} cm (doppelt). Fläche: {x * x} cm², danach {4 * x * x} cm² (vierfach). Nur der Umfang ist proportional zur Seitenlänge.',
                'h': 'Rechne Umfang und Flächeninhalt vorher und nachher aus.'}
    n = R.randint(3, 8)
    if R.random() < .34:
        satz_, was, ein = R.choice(PROP_NEIN); g, p = R.randint(2, 5), R.randint(1, 3)
        t = satz_.format(g=g, p=p)
        r, f = f'Nein; {n} {ein}: {g + p * n} €', [f'Ja; {n} {ein}: {p * n} €', f'Ja; {n} {ein}: {(g + p) * n} €']
        w = f'Die Grundgebühr zahlt man nur einmal: {g} € + {n} · {p} € = {g + p * n} €. Für 0 {ein} zahlt man schon {g} € – also nicht proportional.'
        frage = f'{t} Ist {was} proportional, und was kostet es für {n} {ein}?'
    else:
        satz_, was, werte, ein, mz = R.choice(PROP_JA); p = R.choice(werte)
        t = satz_.format(p=p)
        r, f = f'Ja; {n} {mz}: {zt(p * n)} {ein}', [f'Ja; {n} {mz}: {zt(p + n)} {ein}', 'Nein, das kann man nicht wissen']
        w = f'Jedes Stück bringt gleich viel, und 0 Stück ergeben 0: proportional. {n} · {zt(p)} = {zt(p * n)} {ein}.'
        frage = f'{t} Ist „{was}“ proportional, und was gilt für {n} {mz}?'
    aw, i = _rund(r, f)
    return {'y': 'auswahl', 'f': {'text': frage}, 'a': aw, 'o': {'index': i}, 'w': w,
            'h': 'Frag dich: Was kostet nichts? Gibt es einen festen Betrag, der immer dazukommt?'}


def _tabelle_luecken(s):
    w = R.choice(WAREN); p = R.choice(w[5])
    n = R.randint(2, 5); k = R.choice([2, 3, 4, 5])
    if s == 3:
        k2 = R.choice([2, 3, 4]); m1, m2, m3 = n, n * k, n * k2
        if m2 == m3 or not ok(w, p, [m1, m2, m3], p * max(m2, m3)): return _tabelle_luecken(s)
        mengen, gesucht = [m2, 1, m3], [p * m2, p, p * m3]
    else:
        m1, mengen = n, [n * k, 1]
        if not ok(w, p, [m1, n * k], p * n * k): return _tabelle_luecken(s)
        gesucht = [p * n * k, p]
    e = w[0] if w[0].startswith('kg') or w[0] in ('Stunde', 'Minute') else ''
    nm = lambda m: f'{m} {w[0] if m == 1 else w[1]}'
    return {'y': 'luecken', 'f': {'text': f'Die Zuordnung ist proportional. Ergänze die Tabelle.',
                                  'grafik': {'typ': 'tabelle', 'kopf': ['Menge', nm(m1)] + [nm(m) for m in mengen], 'zeilen': [[w[4], zt(p * m1)] + ['?'] * len(mengen)]},
                                  'schablone': '; '.join(f'{nm(m)}: □ {w[4]}' for m in mengen), 'hinweis': 'Trage die fehlenden Werte als Zahlen ein.'},
            'o': {'werte': gesucht}, 'c': [f'{p * m1}/{m1}*{m}' for m in mengen],
            'w': f'Erst auf 1 schließen: {zt(p * m1)} : {m1} = {zt(p)} {w[4]}. Dann ' + ', '.join(f'{m} · {zt(p)} = {zt(p * m)}' for m in mengen if m != 1) + f' {w[4]}.',
            'h': 'Was du links tust, tust du auch rechts. Am einfachsten über 1 Stück.'}


def _umkehr(s):
    w = R.choice(WAREN); p = R.choice(w[5]); n = R.randint(2, 4); k = R.choice([2, 3, 4, 5])
    if not ok(w, p, [n, n * k]) or w[4] == 'ct' and p * n * k >= 1000: return _umkehr(s)
    frage = {'kosten': f'Wie viele {w[1]} bekommst du für {zt(p * n * k)} {w[4]}?', 'reichen für': f'Wie viele {w[1]} braucht man für {zt(p * n * k)} {w[4]}?',
             'fährt ein Radfahrer': f'Wie viele Stunden braucht er für {zt(p * n * k)} km?', 'enthalten': f'Wie viele Packungen braucht man für {zt(p * n * k)} Kekse?',
             'laufen aus dem Hahn': f'Wie viele Minuten dauert es, bis {zt(p * n * k)} Liter gelaufen sind?', 'sind': f'Wie viele Schritte sind {zt(p * n * k)} cm?'}[w[3]]
    return {'y': 'zahl', 'f': {'text': f'{satz(w, n, p * n)}. {frage}'}, 'o': {'wert': n * k}, 'c': f'{p * n * k}/{p * n}*{n}',
            'w': f'{zt(p * n * k)} ist das {k}-Fache von {zt(p * n)} ({zt(p * n * k)} : {zt(p * n)} = {k}). Also auch die Menge mal {k}: {n} · {k} = {n * k}.',
            'h': 'Wie oft passt der bekannte Wert in den neuen Wert? Nimm die Menge genauso oft.'}


def g_vervielfachen(s):
    w = R.choice(WAREN); p = R.choice(w[5])
    if s == 1:
        n, k = R.randint(2, 5), R.choice([2, 3, 10])
        if not ok(w, p, [n, n * k], p * n * k): return g_vervielfachen(s)
        return {'y': 'zahl', 'f': {'text': f'{satz(w, n, p * n)}. {satz(w, n * k, 0, True)}?'}, 'o': {'wert': p * n * k, 'einheit': w[4]}, 'c': f'{p * n}*{k}',
                'w': f'{n * k} ist das {k}-Fache von {n}. Also: {zt(p * n)} · {k} = {zt(p * n * k)} {w[4]}.', 'h': 'Mit welcher Zahl musst du die Menge malnehmen? Nimm den Wert mit derselben Zahl mal.'}
    if s == 2:
        art = R.choice(['teilen', 'umkehr', 'tabelle'])
        if art == 'umkehr': return _umkehr(s)
        if art == 'tabelle': return _tabelle_luecken(s)
        k = R.choice([2, 3, 4, 5]); n = R.randint(2, 6)
        if not ok(w, p, [n, n * k], p * n): return g_vervielfachen(s)
        return {'y': 'zahl', 'f': {'text': f'{satz(w, n * k, p * n * k)}. {satz(w, n, 0, True)}?'}, 'o': {'wert': p * n, 'einheit': w[4]}, 'c': f'{p * n * k}/{k}',
                'w': f'{n} ist {TEIL_WORT[k]} von {n * k}, denn {n * k} : {k} = {n}. Also auch der Wert geteilt durch {k}: {zt(p * n * k)} : {k} = {zt(p * n)} {w[4]}.',
                'h': 'Durch welche Zahl musst du die Menge teilen? Teile den Wert durch dieselbe Zahl.'}
    if R.random() < .5: return _tabelle_luecken(s)
    n = R.choice([2, 3, 4, 5]); k1, k2 = R.sample([2, 3, 4, 5, 6], 2)
    if not ok(w, p, [n * k1, n * k2], p * n * k2): return g_vervielfachen(s)
    return {'y': 'zahl', 'f': {'text': f'{satz(w, n * k1, p * n * k1)}. {satz(w, n * k2, 0, True)}?'}, 'o': {'wert': p * n * k2, 'einheit': w[4]}, 'c': f'{p * n * k1}/{k1}*{k2}',
            'w': f'Erst durch {k1}: {n} {w[1] if n > 1 else w[0]} → {zt(p * n)} {w[4]}. Dann mal {k2}: {zt(p * n * k2)} {w[4]}.', 'h': 'Gehe über eine kleinere Menge, die in beiden Mengen steckt.'}


def _einheit_um():
    if R.random() < .5:
        ct, n = R.choice([30, 40, 45, 50, 60, 80, 35, 55]), R.randint(2, 8)
        ges = ct * n
        return {'y': 'zahl', 'f': {'text': f'{n} Brötchen kosten zusammen {euro(ges)}. Wie viel Cent kostet 1 Brötchen?'}, 'o': {'wert': ct, 'einheit': 'ct'}, 'c': f'{ges}/{n}',
                'w': f'Erst in Cent umrechnen: {euro(ges)} = {ges} ct. Dann {ges} ct : {n} = {ct} ct.', 'h': 'Rechne zuerst Euro in Cent um.'}
    g, n = R.choice([(250, 4), (500, 2), (500, 4), (200, 5), (125, 8), (250, 8), (400, 5), (200, 10)])
    kg = g * n // 1000
    if g * n % 1000: return _einheit_um()
    return {'y': 'zahl', 'f': {'text': f'{n} gleiche Pakete wiegen zusammen {kg} kg. Wie viel Gramm wiegt 1 Paket?'}, 'o': {'wert': g, 'einheit': 'g'}, 'c': f'{kg}*1000/{n}',
            'w': f'Erst in Gramm umrechnen: {kg} kg = {zt(kg * 1000)} g. Dann {zt(kg * 1000)} g : {n} = {g} g.', 'h': 'Rechne zuerst kg in g um.'}


def _einheit_fehler():
    n, p = R.randint(3, 9), R.randint(2, 9)
    ges = n * p
    if R.random() < .5:
        text = f'Jemand rechnet: {n} Hefte kosten {ges} €, also kostet 1 Heft {n} : {ges} €. Was ist falsch?'
        r = f'Menge und Wert sind vertauscht. Richtig: {ges} : {n} = {p} €.'
        f = [f'Es muss {ges} − {n} = {ges - n} € heißen.', 'Nichts, so rechnet man.']
    else:
        text = f'Jemand rechnet: {n} kg kosten {ges} €, also kostet 1 kg {ges} − {n} = {ges - n} €. Was ist falsch?'
        r = f'Es wurde subtrahiert statt geteilt. Richtig: {ges} : {n} = {p} €.'
        f = [f'Es muss {n} : {ges} heißen.', 'Nichts, das stimmt.']
    aw, i = _rund(r, f)
    return {'y': 'auswahl', 'f': {'text': text}, 'a': aw, 'o': {'index': i},
            'w': f'Auf die Einheit schließen heißt: Wert geteilt durch Anzahl. {ges} : {n} = {p} €. Probe: {n} · {p} € = {ges} € ✓',
            'h': 'Mach die Probe: Anzahl mal Preis für 1 Stück muss den Gesamtpreis ergeben.'}


def g_einheit(s):
    if s == 3:
        art = R.choice(['um', 'um', 'fehler', 'gross'])
        if art == 'um': return _einheit_um()
        if art == 'fehler': return _einheit_fehler()
    w = R.choice(WAREN); p = R.choice(w[5])
    n = {1: R.randint(2, 6), 2: R.randint(7, 12), 3: R.choice([15, 20, 25, 30, 40, 50])}[s]
    if not ok(w, p, [n]): return g_einheit(s)
    return {'y': 'zahl', 'f': {'text': f'{satz(w, n, p * n)}. {satz(w, 1, 0, True)}?'}, 'o': {'wert': p, 'einheit': w[4]}, 'c': f'{p * n}/{n}',
            'w': f'Beide Seiten geteilt durch {n}: {euro(p * n) + " = " + str(p * n) + " ct" if w[4] == "ct" and p * n >= 1000 else zt(p * n) + " " + w[4]} : {n} = {zt(p)} {w[4]}.',
            'h': 'Teile den Wert durch die Anzahl.'}


def g_dreisatz(s):
    w = R.choice(WAREN); p = R.choice(w[5])
    if s == 3 and R.random() < .5:
        a, b = R.randint(3, 8), R.randint(4, 12)
        if a == b or b % a == 0 or a % b == 0 or not ok(w, p, [a, b]) or w[4] == 'ct' and p * b >= 1000: return g_dreisatz(s)
        frage = {'kosten': f'Wie viele {w[1]} bekommst du für {zt(p * b)} {w[4]}?', 'reichen für': f'Wie viele {w[1]} braucht man für {zt(p * b)} {w[4]}?',
                 'fährt ein Radfahrer': f'Wie viele Stunden braucht er für {zt(p * b)} km?', 'enthalten': f'Wie viele Packungen braucht man für {zt(p * b)} Kekse?',
                 'laufen aus dem Hahn': f'Wie viele Minuten braucht der Hahn für {zt(p * b)} Liter?', 'sind': f'Wie viele Schritte sind {zt(p * b)} cm?'}[w[3]]
        return {'y': 'zahl', 'f': {'text': f'{satz(w, a, p * a)}. {frage}'}, 'o': {'wert': b}, 'c': f'{p * b}/({p * a}/{a})',
                'w': f'1. {satz(w, a, p * a)}. 2. Auf 1 schließen: {satz(w, 1, p)}. 3. {zt(p * b)} : {zt(p)} = {b}.',
                'h': 'Schließe zuerst auf 1 Stück. Dann: Wie oft passt der Wert für 1 Stück in den gesuchten Wert?'}
    a, b = {1: (R.randint(2, 5), R.randint(6, 9)), 2: (R.randint(3, 9), R.randint(4, 12)), 3: (R.choice([12, 15, 20, 25]), R.choice([7, 9, 11, 13, 30, 35]))}[s]
    if a == b or b % a == 0 or not ok(w, p, [a, b], p * b): return g_dreisatz(s)
    return {'y': 'zahl', 'f': {'text': f'{satz(w, a, p * a)}. {satz(w, b, 0, True)}?'}, 'o': {'wert': p * b, 'einheit': w[4]}, 'c': f'{p * a}/{a}*{b}',
            'w': f'1. {satz(w, a, p * a)}. 2. Geteilt durch {a}: {satz(w, 1, p)}. 3. Mal {b}: {zt(p)} · {b} = {zt(p * b)} {w[4]}.',
            'h': 'Drei Zeilen: was du weißt, dann auf 1 schließen (teilen), dann auf das Gesuchte (malnehmen).'}


def g_geschickt(s):
    w = R.choice(WAREN); p = R.choice(w[5])
    t = {1: R.choice([2, 3]), 2: R.choice([3, 4, 5]), 3: R.choice([5, 6, 10, 25])}[s]
    x, y = R.sample([2, 3, 4, 5, 7] if s < 3 else [2, 3, 4, 6, 7, 9], 2)
    a, b = t * x, t * y
    if b % a == 0 or a % b == 0 or not ok(w, p, [a, b], p * b): return g_geschickt(s)
    if (s == 3 and R.random() < .5) or (s == 2 and R.random() < .3):
        ri = f'{t} {w[1]}'
        z2 = next(z for z in range(t + 1, t + 20) if a % z or b % z)
        aw, i = _rund(ri, [f'{z2} {w[1]}', f'{a + b} {w[1]}'])
        return {'y': 'auswahl', 'f': {'text': f'Du kennst den Wert für {a} {w[1]} und suchst den Wert für {b} {w[1]}. Welcher Zwischenschritt ist geschickt?'}, 'a': aw, 'o': {'index': i},
                'w': f'{t} steckt in {a} ({a} : {t} = {x}) und in {b} ({b} : {t} = {y}). Also erst durch {x} teilen, dann mal {y}.', 'h': 'Suche eine Zahl, durch die beide Mengen teilbar sind.'}
    return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {satz(w, a, p * a)}. {satz(w, b, 0, True)}?'}, 'o': {'wert': p * b, 'einheit': w[4]}, 'c': f'{p * a}/{x}*{y}',
            'w': f'Zwischenschritt {t}: {zt(p * a) if w[4] != "ct" or p * a < 1000 else str(p * a)} : {x} = {zt(p * t)} {w[4]}. Dann mal {y}: {zt(p * b)} {w[4]}.', 'h': f'Welche Menge steckt in {a} und in {b}?'}


def g_pruefen(s):
    p = R.choice([2, 3, 4, 5, 6, 7, 8, 12, 15])
    ns = sorted(R.sample(range(2, 13), 3))
    if s == 1:
        return {'y': 'zahl', 'f': {'text': f'Eine proportionale Tabelle: {ns[0]} → {p * ns[0]}, {ns[1]} → {p * ns[1]}, {ns[2]} → {p * ns[2]}. Welcher Wert gehört zu 1?'}, 'o': {'wert': p}, 'c': f'{p * ns[0]}/{ns[0]}',
                'w': f'Wert geteilt durch Menge: {p * ns[0]} : {ns[0]} = {p}. Das stimmt auch für die anderen Paare.', 'h': 'Teile einen Wert durch seine Menge.'}
    if s == 2:
        if R.random() < .5:
            j = R.randrange(3); d = R.choice([-2, -1, 1, 2, 3])
            werte = [p * n for n in ns]; werte[j] += d
            a = [f'{ns[k]} → {werte[k]}' for k in range(3)]
            return {'y': 'auswahl', 'f': {'text': 'Zwei Paare gehören zu einer proportionalen Zuordnung, eines passt nicht. Welches?'}, 'a': a, 'o': {'index': j},
                    'w': f'Bei den beiden anderen ist Wert : Menge = {p}. Bei {a[j]} müsste der Wert {p * ns[j]} sein.', 'h': 'Rechne bei jedem Paar Wert geteilt durch Menge.'}
        q = p + R.choice([1, 2])
        t1 = ', '.join(f'{n} → {p * n}' for n in ns)
        t2 = ', '.join(f'{n} → {p * n + q}' for n in ns)
        t3 = ', '.join(f'{n} → {n * n}' for n in ns)
        aw, i = _rund(t1, [t2, t3])
        return {'y': 'auswahl', 'f': {'text': 'Welche Tabelle gehört zu einer proportionalen Zuordnung?'}, 'a': aw, 'o': {'index': i},
                'w': f'Nur bei {t1} ist Wert : Menge immer gleich ({p}). Bei den anderen ändert sich der Quotient.', 'h': 'Proportional heißt: Wert geteilt durch Menge ist bei allen Paaren gleich.'}
    if R.random() < .55:
        z, nn = R.choice([2, 4]), R.choice([3, 5, 7])          # Wert für z Stück ist ganz, für 1 Stück nicht
        if nn % z == 0: return g_pruefen(s)
        m = sorted(R.sample([z * k for k in range(1, 9)], 3))
        wert = lambda x: x // z * nn
        if any(x % z for x in m) or len({x // z for x in m}) < 3 or m[0] == z: return g_pruefen(s)
        return {'y': 'zahl', 'f': {'text': 'Die Tabelle gehört zu einer proportionalen Zuordnung. Welcher Wert fehlt?',
                                   'grafik': {'typ': 'tabelle', 'kopf': ['Menge'] + [str(x) for x in m], 'zeilen': [['Wert', str(wert(m[0])), str(wert(m[1])), '?']]}},
                'o': {'wert': wert(m[2])}, 'c': f'{wert(m[0])}/{m[0] // z}*{m[2] // z}',
                'w': f'Für 1 gäbe es keine ganze Zahl. Nimm {z}: {m[0]} ist {m[0] // z}-mal {z}, also gehört zu {z} der Wert {wert(m[0])} : {m[0] // z} = {nn}. {m[2]} ist {m[2] // z}-mal {z}: {nn} · {m[2] // z} = {wert(m[2])}.',
                'h': 'Suche eine kleine Menge, für die der Wert eine ganze Zahl ist.'}
    if R.random() < .5:
        st, d = R.randint(2, 9), R.randint(3, 8)
        if st == d: return g_pruefen(s)
        tab = ', '.join(f'{k} → {st + (k - 1) * d}' for k in (1, 2, 3))
        r = f'Nein, {st} · 2 wäre {2 * st}, nicht {st + d}.'
        f = [f'Ja, der Wert wird immer um {d} größer.', 'Ja, je mehr, desto mehr.']
        w = f'Proportional hieße: Zum Doppelten (2) gehört das Doppelte von {st}, also {2 * st}. In der Tabelle steht {st + d}. Gleich große Schritte allein reichen nicht.'
    else:
        tab = ', '.join(f'{k} → {k * p}' for k in (2, 3, 4))
        r = f'Ja, Wert : Menge ist immer {p}.'
        f = [f'Nein, der Wert wird immer um {p} größer, das ist nicht proportional.', 'Nein, zu 1 fehlt der Wert.']
        w = f'{2 * p} : 2 = {3 * p} : 3 = {4 * p} : 4 = {p}. Alle Quotienten sind gleich: proportional.'
    aw, i = _rund(r, f)
    return {'y': 'auswahl', 'f': {'text': f'Tabelle: {tab}. Ist die Zuordnung proportional?'}, 'a': aw, 'o': {'index': i}, 'w': w,
            'h': 'Rechne für jedes Paar Wert geteilt durch Menge.'}


FALLEN = [('{n} Eier kochen {t} Minuten. Wie viele Minuten kochen {m} Eier im selben Topf?', [6, 7, 8, 9, 10]),
          ('{n} Hemden trocknen auf der Leine in {t} Minuten. Wie viele Minuten brauchen {m} Hemden auf derselben Leine?', [60, 75, 90, 120]),
          ('Ein Lied dauert {t} Minuten, wenn {n} Kinder es singen. Wie viele Minuten dauert es, wenn {m} Kinder singen?', [3, 4, 5])]
MUFFIN = {'Mehl': (15, 25), 'Zucker': (10, 20), 'Butter': (10, 15), 'Quark': (20, 40)}
SCHAETZ = [('Für {a} Pfannkuchen braucht man {g} g Mehl. Ungefähr wie viel Mehl brauchst du für {b} Pfannkuchen?', 'g', 'Für 1 Pfannkuchen', 'Für {b} Pfannkuchen'),
           ('Ein Hahn füllt in {a} Minuten einen Eimer mit {g} Litern. Ungefähr wie viele Liter laufen in {b} Minuten?', 'Liter', 'In 1 Minute', 'In {b} Minuten')]
PACK = {'n': 0}


def _falle():
    vorlage, zeiten = R.choice(FALLEN); n, m, t = R.randint(2, 4), R.randint(5, 9), R.choice(zeiten)
    return {'y': 'zahl', 'f': {'text': vorlage.format(n=n, m=m, t=t)}, 'o': {'wert': t, 'einheit': 'min'}, 'c': str(t),
            'w': f'Falle: Die Zeit hängt nicht von der Anzahl ab. Es bleibt bei {t} Minuten.', 'h': 'Prüfe zuerst: Wird die Zeit wirklich länger, wenn es mehr sind?'}


def _schaetzen():
    vorlage, ein, eins, viele = R.choice(SCHAETZ)
    a = R.choice([2, 3, 4]); je = R.choice([25, 30, 40, 50]) if ein == 'g' else R.choice([8, 10, 12]); g = a * je
    b = R.choice([15, 20, 25, 30]) if ein == 'g' else R.choice([12, 15, 20])
    genau = je * b
    rund = lambda x: (x + 50) // 100 * 100 if x >= 200 else (x + 5) // 10 * 10
    r = f'etwa {zt(rund(genau))} {ein}'
    f = [f'etwa {zt(rund(g + b))} {ein}' if rund(g + b) != rund(genau) else f'etwa {zt(rund(genau) * 10)} {ein}', f'etwa {zt(rund(genau) * 10)} {ein}' if rund(g + b) != rund(genau) else f'etwa {zt(g)} {ein}']
    if len({r, *f}) < 3: return _schaetzen()
    aw, i = _rund(r, f)
    return {'y': 'auswahl', 'f': {'text': vorlage.format(a=a, g=g, b=b)}, 'a': aw, 'o': {'index': i},
            'w': f'{eins} sind es {g} : {a} = {je} {ein}. {viele.format(b=b)}: {je} · {b} = {zt(genau)} {ein}, also {r}. Nur dazuzählen ({g} + {b}) ist falsch.',
            'h': 'Überschlage: Wie viel ist es für 1? Wie oft so viel brauchst du?'}


def g_sach(s):
    if R.random() < (.25 if s != 2 else .3): return _falle()
    if s == 1:
        pers, k = R.choice([2, 4]), R.choice([2, 3, 4]); je = R.choice([75, 100, 125, 150]); g = je * pers
        ding = R.choice(['Nudeln', 'Reis', 'Mehl', 'Kartoffeln'])
        if (pers, g, k) == (2, 300, 3): return g_sach(s)          # entspricht dem vorgerechneten Beispiel
        return {'y': 'zahl', 'f': {'text': f'Ein Rezept für {pers} Personen braucht {g} g {ding}. Wie viel Gramm braucht man für {pers * k} Personen?'}, 'o': {'wert': g * k, 'einheit': 'g'}, 'c': f'{g}*{k}',
                'w': f'{pers * k} Personen sind {k}-mal so viele. {g} g · {k} = {zt(g * k)} g.', 'h': 'Wie viel mal so viele Personen sind es?'}
    if s == 2:
        if R.random() < .3: return _schaetzen()
        a, b = R.choice([(4, 6), (6, 9), (4, 10), (6, 4), (8, 12), (10, 4), (3, 5), (5, 8)])
        ding = R.choice(list(MUFFIN)); je = R.randint(*MUFFIN[ding]); g = je * a
        return {'y': 'zahl', 'f': {'text': f'Ein Rezept für {a} Muffins braucht {g} g {ding}. Wie viel Gramm braucht man für {b} Muffins?'}, 'o': {'wert': je * b, 'einheit': 'g'}, 'c': f'{g}/{a}*{b}',
                'w': f'1 Muffin: {g} g : {a} = {je} g. {b} Muffins: {je} g · {b} = {zt(je * b)} g.', 'h': 'Dreisatz: erst auf 1 Muffin, dann auf die gesuchte Anzahl.'}
    art = R.choice(['benzin', 'lohn', 'vergleich', 'vergleich'])
    if art == 'benzin':
        v, s2 = R.choice([5, 6, 7, 8]), R.choice([250, 350, 450, 650, 750])
        komma = (v * s2) % 100 != 0
        return {'y': 'zahl', 'f': {'text': f'Ein Auto verbraucht auf 100 km {v} Liter Benzin. Wie viele Liter braucht es für {s2} km?' + (' (Das Ergebnis ist eine Kommazahl.)' if komma else '')},
                'o': {'wert': v * s2 / 100, 'einheit': 'Liter'}, 'c': f'{v}*{s2}/100',
                'w': f'50 km: {zt(v / 2)} Liter. {s2} km sind {s2 // 50}-mal 50 km: {zt(v / 2)} · {s2 // 50} = {zt(v * s2 / 100)} Liter.', 'h': 'Gehe über 50 km als Zwischenschritt.'}
    if art == 'lohn':
        h1, lohn, h2 = R.choice([3, 4, 6]), R.choice([9, 11, 12, 13]), R.choice([5, 7, 9, 11])
        if h1 == h2: return g_sach(s)
        return {'y': 'zahl', 'f': {'text': f'Mia trägt Zeitungen aus. Für {h1} Stunden bekommt sie {h1 * lohn} €. Wie viel bekommt sie für {h2} Stunden, wenn jede Stunde gleich bezahlt wird?'}, 'o': {'wert': lohn * h2, 'einheit': '€'}, 'c': f'{h1 * lohn}/{h1}*{h2}',
                'w': f'1 Stunde: {h1 * lohn} € : {h1} = {lohn} €. {h2} Stunden: {lohn} € · {h2} = {lohn * h2} €.', 'h': 'Dreisatz über 1 Stunde.'}
    n1, n2 = R.choice([(3, 5), (4, 6), (5, 8), (6, 10)]); p1 = R.choice([40, 50, 60])
    fall = ['gross', 'klein', 'gross', 'klein', 'gleich'][PACK['n'] % 5]; PACK['n'] += 1     # 40 % / 40 % / 20 %
    p2 = {'gross': p1 - R.choice([5, 10]), 'klein': p1 + R.choice([5, 10]), 'gleich': p1}[fall]
    r = {'gross': 'Die große Packung', 'klein': 'Die kleine Packung', 'gleich': 'Beide sind gleich günstig'}[fall]
    aw, i = _rund(r, [x for x in ['Die kleine Packung', 'Die große Packung', 'Beide sind gleich günstig'] if x != r])
    return {'y': 'auswahl', 'f': {'text': f'Kleine Packung: {n1} Riegel für {euro(n1 * p1)}. Große Packung: {n2} Riegel für {euro(n2 * p2)}. Bei welcher Packung ist ein Riegel billiger?'}, 'a': aw, 'o': {'index': i},
            'w': f'Klein: {n1 * p1} ct : {n1} = {p1} ct pro Riegel. Groß: {n2 * p2} ct : {n2} = {p2} ct pro Riegel. ' + ('Beide kosten gleich viel pro Riegel.' if fall == 'gleich' else f'Billiger ist {r[0].lower() + r[1:]}.'),
            'h': 'Rechne für jede Packung den Preis für 1 Riegel aus.'}


GEN = {'erkennen': g_erkennen, 'vervielfachen': g_vervielfachen, 'einheit': g_einheit, 'dreisatz': g_dreisatz, 'geschickt': g_geschickt, 'pruefen': g_pruefen, 'sach': g_sach}
DATEI = {
    'thema_schluessel': 'groessen.proportional', 'thema_id': 26, 'block_id': 54, 'klasse': {'gym_by': 5, 'rs_by': 5, 'ib_myp': 2},
    'autor': 'Claude (Generator groessen_proportional.py)',
    'offen': ['Produktgleichheit (indirekte Proportionalität) steht im „umfang“, gehört aber zum Thema groessen.indirekt (Kl. 8) und ist hier weggelassen.',
              'Darstellung als Graph (Ursprungsgerade) bewusst weggelassen: Die App kann sie inzwischen zeichnen, lehrplan_gym Kl. 5 verlangt aber nur Schlussrechnung und Dreisatz; ein Graph wäre Stoff einer höheren Jahrgangsstufe. Dargestellt wird mit Tabellen (Lernkarten erkennen, pruefen, dreisatz und Aufgaben).'],
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

# Umbau U5 (Achte Runde, Vorgabe 16.11.): Lernkarten nach dem neuen Muster – einstieg, woerter (≤ 3), Kartenbild,
# Bildergeschichte (schritte mit bild), „Pass auf!“ (fehler + fehler_bild), MERKE (regel).
# Situation: Einkaufen (Bäcker, Markt, Laden, Eintrittskarten, Rezept). Die Tabellen füllen sich Schritt für Schritt.
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl5.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl5 import umbau  # noqa: E402

BROETCHEN = lambda *p: {'zeilen': [['Preis', *p]]}
OBST = lambda *p: {'zeilen': [['Preis', '6 €', '15 €', '24 €'], ['Preis : Menge', *p]]}

KARTEN = {
 'erkennen': {
  'einstieg': 'Beim Bäcker kostet ein Brötchen 40 ct. Doppelt so viele kosten doppelt so viel, keins kostet nichts. So eine Zuordnung heißt ⟦proportional⟧.',
  'woerter': [['Zuordnung', 'zu jeder Menge gehört ein Wert, zum Beispiel zu jeder Anzahl ein Preis'],
              ['proportional', 'doppelte Menge → doppelter Wert, halbe Menge → halber Wert']],
  'bild': {'typ': 'tabelle', 'kopf': ['Anzahl Brötchen', '0', '1', '2', '3'], 'zeilen': [['Preis', '?', '40 ct', '?', '?']]},
  'schritte': [{'text': '2 Brötchen kosten doppelt so viel: 80 ct.', 'bild': BROETCHEN('?', '40 ct', '80 ct', '?')},
               {'text': '3 Brötchen kosten dreimal so viel: 120 ct.', 'bild': BROETCHEN('?', '40 ct', '80 ct', '120 ct')},
               {'text': '0 Brötchen kosten 0 ct.', 'bild': BROETCHEN('0 ct', '40 ct', '80 ct', '120 ct')},
               {'text': 'Doppelt, dreifach und null passen: Die Zuordnung ist ⟦proportional⟧.'}],
  'fehler': 'Das Taxi ist nicht proportional: Schon das Einsteigen kostet 4 €. 2 km kosten 8 €, nicht das Doppelte von 6 €.',
  'fehler_bild': {'kopf': ['Strecke', '0 km', '1 km', '2 km'], 'zeilen': [['Taxi', '4 €', '6 €', '8 €']]},
  'regel': 'Proportional heißt: doppelte Menge, ⟦doppelter Wert⟧. Und zu 0 gehört 0.'},
 'vervielfachen': {
  'einstieg': 'Auf dem Markt kosten 3 kg Äpfel 6 €. Du brauchst 9 kg für Apfelmus. 9 kg sind dreimal so viel, also kosten sie ⟦dreimal so viel⟧.',
  'woerter': [['vervielfachen', 'mit einer Zahl malnehmen'], ['verdreifacht', 'mal 3 genommen']],
  'bild': {'typ': 'tabelle', 'kopf': ['Menge', '3 kg', '9 kg'], 'zeilen': [['Preis', '6 €', '?']]},
  'schritte': [{'text': 'Von 3 kg auf 9 kg: 9 : 3 = 3. Die Menge wird verdreifacht.', 'bild': {'kopf': ['Menge', '3 kg', '9 kg (· 3)']}},
               {'text': 'Den Preis vervielfachen wir genauso: 6 € · 3 = ⟦18 €⟧.', 'bild': {'zeilen': [['Preis', '6 €', '18 € (· 3)']]}}],
  'fehler': 'Plus statt mal: 9 kg sind 6 kg mehr als 3 kg. Der Preis wird aber nicht 6 € + 6 € = 12 €.',
  'fehler_bild': {'zeilen': [['Preis', '6 €', 'nicht 12 €']]},
  'regel': 'Auf beiden Seiten ⟦dasselbe⟧ tun: Menge mal 3, Preis mal 3. Gerechnet wird mit mal und geteilt.'},
 'pruefen': {
  'einstieg': 'Der Obsthändler hat eine Preisliste für 2 kg, 5 kg und 8 kg. Gibt es irgendwo Rabatt? Du rechnest für jede Spalte den ⟦Preis für 1 kg⟧ aus.',
  'woerter': [['Rabatt', 'ein Preisnachlass: Man zahlt weniger'], ['Preis : Menge', 'der Preis geteilt durch die Menge, also der Preis für 1 kg']],
  'bild': {'typ': 'tabelle', 'kopf': ['Menge', '2 kg', '5 kg', '8 kg'], 'zeilen': [['Preis', '6 €', '15 €', '24 €'], ['Preis : Menge', '?', '?', '?']]},
  'schritte': [{'text': 'Erste Spalte, Preis : Menge: 6 € : 2 = 3 €.', 'bild': OBST('3 €', '?', '?')},
               {'text': '15 € : 5 = 3 € und 24 € : 8 = 3 €.', 'bild': OBST('3 €', '3 €', '3 €')},
               {'text': 'Überall 3 € für 1 kg: Die Tabelle ist ⟦proportional⟧.'}],
  'fehler': 'Nur zwei Spalten prüfen reicht nicht. Ein Rabatt kann in der letzten Spalte stecken: 20 € : 8 = 2,50 €.',
  'fehler_bild': {'zeilen': [['Preis', '6 €', '15 €', '20 €'], ['Preis : Menge', '3 €', '3 €', '2,50 €']]},
  'regel': 'Rechne für jede Spalte ⟦Preis : Menge⟧. Kommt überall dieselbe Zahl heraus, ist die Tabelle proportional.'},
 'einheit': {
  'einstieg': 'Im Laden kosten 5 Hefte zusammen 10 €. Du willst wissen, was ein einziges Heft kostet. Das heißt ⟦auf die Einheit schließen⟧.',
  'woerter': [['auf die Einheit schließen', 'ausrechnen, was 1 Stück kostet']],
  'bild': {'typ': 'tabelle', 'kopf': ['Hefte', '5', '1'], 'zeilen': [['Preis', '10 €', '?']]},
  'schritte': [{'text': 'Von 5 Heften auf 1 Heft teilst du durch 5.', 'bild': {'kopf': ['Hefte', '5', '1 (: 5)']}},
               {'text': 'Beim Preis genauso: 10 € : 5 = ⟦2 €⟧.', 'bild': {'zeilen': [['Preis', '10 €', '2 € (: 5)']]}}],
  'fehler': 'Falsch herum teilen: 5 : 10 = 0,50. Wenn fünf Hefte 10 € kosten, kostet eins nicht nur 50 ct.',
  'fehler_bild': {'zeilen': [['Preis', '10 €', 'nicht 0,50 €']]},
  'regel': '⟦Wert durch Anzahl⟧ teilen ergibt den Preis für 1 Stück.'},
 'dreisatz': {
  'einstieg': '4 kg Äpfel kosten 12 €, gesucht ist der Preis für 7 kg. Du gehst den Umweg über 1 kg, in drei Zeilen: den ⟦Dreisatz⟧.',
  'woerter': [['Dreisatz', 'Rechenweg in drei Zeilen: bekannt → 1 Stück → gesucht']],
  'bild': {'typ': 'tabelle', 'kopf': ['Zeile', 'Menge', 'Preis'], 'zeilen': [['1: bekannt', '4 kg', '12 €']]},
  'schritte': [{'text': 'Zeile 1: 4 kg kosten 12 €.'},
               {'text': 'Zeile 2: beide Seiten durch 4. 1 kg kostet 3 €.', 'bild': {'zeilen': [['1: bekannt', '4 kg', '12 €'], ['2: durch 4', '1 kg', '3 €']]}},
               {'text': 'Zeile 3: beide Seiten mal 7. 7 kg kosten ⟦21 €⟧.',
                'bild': {'zeilen': [['1: bekannt', '4 kg', '12 €'], ['2: durch 4', '1 kg', '3 €'], ['3: mal 7', '7 kg', '21 €']]}}],
  'fehler': 'In Zeile 3 mit der alten Menge malnehmen: 3 € · 4 = 12 €. Das ist wieder der Preis für 4 kg, nicht für 7 kg.',
  'fehler_bild': {'zeilen': [['1: bekannt', '4 kg', '12 €'], ['2: durch 4', '1 kg', '3 €'], ['3: mal 4?', '4 kg', '12 €']]},
  'regel': 'Erst auf ⟦1 Stück⟧ schließen, dann auf das Gesuchte. Was du links tust, tust du auch rechts.'},
 'geschickt': {
  'einstieg': '6 Eintrittskarten kosten 42 €, ihr braucht aber 9. Über 3 Karten geht es schneller als über 1 Karte. So eine passende ⟦Zwischenmenge⟧ spart Rechenarbeit.',
  'woerter': [['Zwischenmenge', 'eine Menge auf dem Weg zum Ziel, mit der man bequem rechnet']],
  'bild': {'typ': 'tabelle', 'kopf': ['Schritt', 'Karten', 'Preis'], 'zeilen': [['bekannt', '6', '42 €']]},
  'schritte': [{'text': '3 passt in 6 und in 9 ohne Rest. Darum geht es über 3 Karten.'},
               {'text': '3 Karten sind die Hälfte: 42 € : 2 = 21 €.', 'bild': {'zeilen': [['bekannt', '6', '42 €'], ['durch 2', '3', '21 €']]}},
               {'text': '9 Karten sind dreimal 3 Karten: 21 € · 3 = ⟦63 €⟧.',
                'bild': {'zeilen': [['bekannt', '6', '42 €'], ['durch 2', '3', '21 €'], ['mal 3', '9', '63 €']]}}],
  'fehler': 'Eine Zwischenmenge wählen, die nicht in beide passt, zum Beispiel 4. Von 6 auf 4 müsstest du durch 1,5 teilen.',
  'regel': 'Suche eine ⟦Zwischenmenge⟧, die in beide Zahlen passt. Von 6 nach 9 geht es über 3.'},
 'sach': {
  'einstieg': 'Im Rezept stehen 600 g Nudeln für 4 Personen, heute kommen 6. Mehr Personen essen mehr, im gleichen Verhältnis. Aber nicht alles ist ⟦proportional⟧.',
  'woerter': [['im gleichen Verhältnis', 'doppelt so viele Personen brauchen doppelt so viel']],
  'bild': {'typ': 'tabelle', 'kopf': ['Schritt', 'Personen', 'Nudeln'], 'zeilen': [['bekannt', '4', '600 g']]},
  'schritte': [{'text': 'Prüfe zuerst: Doppelt so viele Personen essen doppelt so viel. Proportional!'},
               {'text': 'Über 2 Personen: 600 g : 2 = 300 g.', 'bild': {'zeilen': [['bekannt', '4', '600 g'], ['durch 2', '2', '300 g']]}},
               {'text': '6 Personen sind dreimal 2: 300 g · 3 = ⟦900 g⟧.',
                'bild': {'zeilen': [['bekannt', '4', '600 g'], ['durch 2', '2', '300 g'], ['mal 3', '6', '900 g']]}}],
  'fehler': '„1 Ei kocht 8 Minuten, also kochen 3 Eier 24 Minuten“ ist falsch. Die Kochzeit hängt nicht von der Zahl der Eier ab.',
  'fehler_bild': {'kopf': ['Eier', '1', '3'], 'zeilen': [['Kochzeit', '8 min', '8 min']]},
  'regel': 'Prüfe zuerst, ob die Zuordnung ⟦proportional⟧ ist. Nur dann rechnest du mit dem Dreisatz.'},
}
umbau(DATEI, KARTEN)


# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl5) ----------
# Neue Übungen nach Prüfungsvorbild (Jahrgangsstufentest 6 Bayern: Güterwagen, Gondeln, Gewitter-Faustregel, Einlass-Zeit,
# Bücher/Gewicht; Klassenarbeiten: Aussagen beurteilen; Knobelaufgabe Katzen und Mäuse); eigene Zahlen und Einkleidung.
from fractions import Fraction  # noqa: E402
from _schwer_kl5 import A, L, Z, de, einzig, ergaenze, wahl  # noqa: E402


def _schwer():
    N = {}
    N['erkennen'] = [
        wahl(2, 'Welche Zuordnung ist proportional?', ['Anzahl gleicher Busfahrkarten → Preis', 'Alter eines Kindes → Schuhgröße',
                                                       'Fahrstrecke mit dem Taxi (mit Grundgebühr) → Preis', 'Zahl der Spieler → Dauer eines Fußballspiels'],
             lambda o: o.startswith('Anzahl gleicher'), 'Doppelt so viele gleiche Karten kosten doppelt so viel, und 0 Karten kosten 0 €.',
             'Prüfe: Doppelte Menge – doppelter Wert? Und gehört zu 0 die 0?'),
        wahl(2, 'Für 2 Stunden Parken zahlt man 3 €, für 4 Stunden 6 €, für 6 Stunden 8 €. Ist Parkdauer → Preis proportional?',
             ['Nein, für 6 Stunden müssten es 9 € sein.', 'Ja, je länger, desto teurer.', 'Ja, 2 → 3 und 4 → 6 passen.'], lambda o: o.startswith('Nein'),
             '3 € : 2 = 1,50 € je Stunde. Für 6 Stunden wären es 6 · 1,50 € = 9 €, nicht 8 €.', 'Prüfe jede Spalte, nicht nur die ersten beiden.'),
        wahl(3, 'Faustregel beim Gewitter: In 3 Sekunden legt der Donner etwa 1 km zurück. Wie weit ist das Gewitter entfernt, wenn der Donner 12 Sekunden nach dem Blitz kommt?',
             ['etwa 4 km', 'etwa 36 km', 'etwa 9 km', 'Das kann man nicht sagen.'], lambda o: o == f'etwa {12 // 3} km',
             'Die Zuordnung ist proportional: 12 s sind 4-mal 3 s, also 4 · 1 km = 4 km.', 'Wie oft passen 3 Sekunden in 12 Sekunden?'),
        A(3, 'Jemand sagt: „Je älter ein Baum, desto höher ist er. Also ist Alter → Höhe proportional.“ Stimmt das?',
          'Nein: „Je mehr, desto mehr“ reicht nicht. Ein doppelt so alter Baum ist nicht doppelt so hoch.',
          ['Ja, weil beide Größen zusammen wachsen.', 'Ja, aber nur bei jungen Bäumen.', 'Nein, weil ein Baum gar nicht wächst.'],
          'Proportional heißt: doppeltes Alter, doppelte Höhe. Bäume wachsen aber irgendwann kaum noch.', 'Was müsste bei doppeltem Alter passieren?'),
        Z(3, 'Eine Tabelle: 0 → 0, 2 → 5, 4 → 10, 6 → 16. Ein Wert ist falsch. Welcher Wert müsste bei 6 stehen, damit die Zuordnung proportional ist?', '6 * 5 / 2',
          'Zu 2 gehört 5, also zu 1 der Wert 2,5. Zu 6 gehört 6 · 2,5 = 15, nicht 16.', 'Schließe zuerst auf den Wert für 1.'),
        wahl(3, 'Eine Kerze ist 20 cm lang und brennt jede Stunde 2 cm ab. Ist „Brenndauer → Restlänge der Kerze“ proportional?',
             ['Nein, die Restlänge wird kleiner, wenn die Zeit größer wird.', 'Ja, jede Stunde fehlen 2 cm.', 'Ja, nach 5 Stunden sind es 10 cm.'],
             lambda o: o.startswith('Nein'), 'Nach 1 h sind es 18 cm, nach 2 h 16 cm. Doppelte Zeit gibt nicht doppelte Restlänge. Proportional wäre „Brenndauer → abgebrannte Länge“.',
             'Rechne die Restlänge nach 1 und nach 2 Stunden aus.'),
    ]
    N['vervielfachen'] = [
        Z(2, '6 Kugeln Eis kosten 7,20 €. Was kosten 2 Kugeln?', '7.2 / 3', '2 Kugeln sind ein Drittel von 6 Kugeln: 7,20 € : 3 = 2,40 €.', 'Von 6 auf 2: durch 3.', einheit='€'),
        Z(2, 'Für 5 Kuchen braucht man 15 Eier. Für wie viele Kuchen reichen 45 Eier?', '5 * 45 // 15', '45 Eier sind 3-mal 15 Eier. Also 3 · 5 = 15 Kuchen.', 'Wie oft passen 15 Eier in 45 Eier?'),
        Z(3, '20 gleiche Waggons sind zusammen 260 m lang. Wie lang sind 35 solche Waggons?', '260 * 35 / 20',
          'Über 5 Waggons: 260 m : 4 = 65 m. 35 Waggons sind 7-mal 5 Waggons: 7 · 65 m = 455 m.', 'Suche eine Zwischenzahl, die in 20 und in 35 passt.', einheit='m'),
        Z(3, 'Ein Riesenrad hat 30 gleiche Gondeln. 5 Gondeln bieten zusammen 40 Plätze. Wie viele Personen passen in alle Gondeln?', '40 * 30 // 5',
          '30 Gondeln sind 6-mal 5 Gondeln: 6 · 40 = 240 Plätze.', 'Wie oft passen 5 Gondeln in 30 Gondeln?'),
        Z(3, '3 Katzen fangen in 3 Minuten 3 Mäuse. Wie viele Mäuse fangen 6 Katzen in 6 Minuten, wenn alle gleich schnell sind?', '3 * 2 * 2',
          'Doppelt so viele Katzen: 6 Mäuse in 3 Minuten. Doppelt so lange Zeit: 12 Mäuse in 6 Minuten.', 'Verdopple zuerst die Katzen, dann die Zeit.'),
        A(3, 'Jemand rechnet: 4 Hefte kosten 6 €, also kosten 8 Hefte 6 € + 4 € = 10 €. Was ist falsch?', 'Doppelt so viele Hefte kosten doppelt so viel: 12 €.',
          ['Nichts, 10 € stimmt.', 'Richtig ist 6 € + 8 € = 14 €.', 'Richtig ist 6 € · 8 = 48 €.'],
          'Von 4 auf 8 Hefte wird verdoppelt. Also wird auch der Preis verdoppelt: 6 € · 2 = 12 €.', 'Was passiert mit der Menge? Mach dasselbe mit dem Preis.'),
    ]
    tab = {'4,50 €': (3, Fraction(9, 2)), '7,50 €': (5, Fraction(15, 2)), '12,50 €': (8, Fraction(25, 2))}
    def passt_nicht(o):
        n, p = tab[o]
        andere = [q / m for k, (m, q) in tab.items() if k != o]
        return andere[0] == andere[1] and p / n != andere[0]
    prop = ['2 → 3, 4 → 6, 7 → 10,5', '2 → 3, 4 → 5, 7 → 8', '2 → 3, 4 → 6, 7 → 12', '2 → 4, 4 → 6, 7 → 9']
    def ist_prop(o):
        paare = [(Fraction(a.replace(',', '.')), Fraction(b.replace(',', '.'))) for a, b in (x.split(' → ') for x in o.split(', '))]
        return len({b / a for a, b in paare}) == 1
    N['pruefen'] = [
        wahl(2, 'Ist die Tabelle proportional? 2 → 7, 4 → 14, 10 → 35', ['Ja, Wert : Menge ist immer 3,5.', 'Nein, 35 ist kein Vielfaches von 14.', 'Nein, die Abstände sind verschieden.'],
             lambda o: o.startswith('Ja'), '7 : 2 = 3,5; 14 : 4 = 3,5; 35 : 10 = 3,5. Immer gleich, also proportional.', 'Rechne in jeder Spalte Wert : Menge.'),
        Z(2, 'Eine proportionale Tabelle: 4 → 10. Welcher Wert gehört zu 6?', '10 / 4 * 6', 'Zu 2 gehört 5. Zu 6 gehört 3 · 5 = 15.', 'Gehe über 2.'),
        Z(3, 'An einer Kasse werden in 30 Minuten 240 Besucher eingelassen. Wie viele Minuten dauert es bei gleichem Tempo für 680 Besucher?', '680 / (240 / 30)',
          'In 1 Minute: 240 : 30 = 8 Besucher. Für 680 Besucher: 680 : 8 = 85 Minuten.', 'Wie viele Besucher kommen in einer Minute hinein?', einheit='min'),
        wahl(3, 'Die Tabelle soll proportional sein. Welcher Preis passt nicht?', list(tab), passt_nicht,
             '3 Stück: 4,50 €, also 1,50 € je Stück. 5 Stück: 7,50 € passt. 8 Stück müssten 12,00 € kosten, nicht 12,50 €.',
             'Rechne für jede Spalte den Preis für 1 Stück aus.',
             grafik={'typ': 'tabelle', 'kopf': ['Anzahl', '3', '5', '8'], 'zeilen': [['Preis', '4,50 €', '7,50 €', '12,50 €']]}),
        Z(3, 'In einer proportionalen Tabelle gehört zu 4 der Wert 18. Zu welcher Menge gehört der Wert 45?', '45 / (18 / 4)',
          'Zu 4 gehört 18, also zu 2 der Wert 9. 45 ist 5-mal 9, also gehört 45 zu 5 · 2 = 10.', 'Gehe über einen Zwischenschritt: Zu 2 gehört …'),
        wahl(3, 'Welche Tabelle ist proportional?', prop, ist_prop,
             'Bei 2 → 3, 4 → 6, 7 → 10,5 ist Wert : Menge immer 1,5. Bei den anderen ändert sich der Quotient.', 'Teile in jeder Spalte Wert durch Menge.'),
    ]
    obst = einzig([b for b in range(1, 200) for a in range(1, 200) if 3 * a + 2 * b == 190 and 3 * a + 4 * b == 290])
    N['einheit'] = [
        Z(2, '12 Brezen kosten 8,40 €. Was kostet 1 Breze?', '8.4 / 12', '8,40 € : 12 = 0,70 €.', 'Teile den Preis durch die Anzahl. Rechne in Cent: 840 ct : 12.', einheit='€'),
        Z(2, '5 gleich lange Bretter sind zusammen 4 m lang. Wie viele cm ist 1 Brett lang?', '400 / 5', '4 m = 400 cm. 400 cm : 5 = 80 cm.', 'Rechne zuerst in cm um.', einheit='cm'),
        Z(3, '10 gleich große Käfer liegen hintereinander und sind zusammen 6 cm lang. Ein Hirschkäfer ist 4,8 cm lang. Wie oft so lang wie ein kleiner Käfer ist er?',
          '4.8 / (6 / 10)', 'Ein kleiner Käfer: 6 cm : 10 = 0,6 cm. 4,8 cm : 0,6 cm = 8. Der Hirschkäfer ist 8-mal so lang.', 'Wie lang ist ein kleiner Käfer?'),
        Z(3, 'Packung A: 250 g für 2,00 €. Packung B: 400 g für 3,00 €. Wie viel Cent kosten 100 g bei der günstigeren Packung?', 'min(200 * 100 / 250, 300 * 100 / 400)',
          'A: 100 g kosten 200 ct : 2,5 = 80 ct. B: 100 g kosten 300 ct : 4 = 75 ct. B ist günstiger: 75 ct.', 'Rechne für beide Packungen den Preis für 100 g aus.', einheit='ct'),
        Z(3, '3 Äpfel und 2 Birnen kosten 1,90 €. 3 Äpfel und 4 Birnen kosten 2,90 €. Wie viel Cent kostet 1 Birne?', str(obst),
          'Der Unterschied sind 2 Birnen. Sie kosten 2,90 € − 1,90 € = 1,00 €. 1 Birne kostet 50 ct.', 'Vergleiche die beiden Einkäufe: Was ist beim zweiten mehr?', einheit='ct'),
        Z(3, 'Ein Stück kostet 35 ct. Wie viele Stück bekommst du höchstens für 5 €?', '500 // 35',
          '5 € = 500 ct. 14 Stück kosten 490 ct, 15 Stück 525 ct – zu viel. Also 14 Stück.', 'Rechne in Cent und teile. Was bedeutet der Rest?'),
    ]
    N['dreisatz'] = [
        Z(2, '7 Kinokarten kosten 63 €. Was kosten 5 Karten?', '63 / 7 * 5', '1 Karte: 63 € : 7 = 9 €. 5 Karten: 5 · 9 € = 45 €.', 'Erst auf 1 Karte schließen.', einheit='€'),
        Z(2, 'In 6 Minuten tropfen 90 ml aus einem Hahn. Wie viele ml sind es in 15 Minuten?', '90 / 6 * 15', '1 Minute: 90 ml : 6 = 15 ml. 15 Minuten: 15 · 15 ml = 225 ml.', 'Erst auf 1 Minute schließen.', einheit='ml'),
        Z(3, 'Der Schall legt in 5 Sekunden etwa 1 700 m zurück. Der Donner kommt 13 Sekunden nach dem Blitz. Wie viele Meter ist das Gewitter entfernt?', '1700 / 5 * 13',
          '1 Sekunde: 1 700 m : 5 = 340 m. 13 Sekunden: 13 · 340 m = 4 420 m.', 'Wie weit kommt der Schall in 1 Sekunde?', einheit='m'),
        Z(3, '6 gleiche Ordner wiegen zusammen 4,2 kg. Wie viel kg wiegen 25 Ordner?', '4.2 / 6 * 25', '1 Ordner: 4,2 kg : 6 = 0,7 kg. 25 Ordner: 25 · 0,7 kg = 17,5 kg.',
          'Rechne in g, wenn dir das leichter fällt: 4 200 g : 6.', einheit='kg'),
        Z(3, 'Mit 8 Litern Farbe streicht man 56 m². Ein Zaun hat 91 m². Die Farbe gibt es nur in 2-Liter-Dosen. Wie viele Dosen muss man kaufen?', '-(-(91 / (56 / 8)) // 2)',
          '1 Liter reicht für 56 : 8 = 7 m². Für 91 m² braucht man 91 : 7 = 13 Liter. 6 Dosen sind nur 12 Liter, also 7 Dosen.', 'Rechne zuerst die Liter aus. Reichen 6 Dosen?'),
        A(3, 'Jemand rechnet: 5 kg kosten 15 €. Also kostet 1 kg 5 € und 8 kg kosten 40 €. Was ist falsch?', 'Beim Schluss auf 1 kg wurde falsch geteilt: 15 € : 5 = 3 €. 8 kg kosten 24 €.',
          ['Nichts, 40 € stimmt.', 'Man muss 15 € · 8 = 120 € rechnen.', 'Richtig ist 15 € + 3 € = 18 €.'],
          '1 kg kostet 15 € : 5 = 3 €, nicht 5 €. 8 kg: 8 · 3 € = 24 €.', 'Prüfe den zweiten Schritt: Was ist 15 : 5?'),
    ]
    zw = {'15': 15, '5': 5, '1': 1, '30': 30}
    N['geschickt'] = [
        Z(2, 'Rechne geschickt: 12 Eier kosten 3,60 €. Was kosten 18 Eier?', '3.6 / 2 * 3', 'Über 6 Eier: 3,60 € : 2 = 1,80 €. 18 Eier: 3 · 1,80 € = 5,40 €.', 'Welche Zahl passt in 12 und in 18?', einheit='€'),
        Z(2, 'Rechne geschickt: 25 m Stoff kosten 75 €. Was kosten 15 m?', '75 / 5 * 3', 'Über 5 m: 75 € : 5 = 15 €. 15 m: 3 · 15 € = 45 €.', 'Gehe über 5 m.', einheit='€'),
        Z(3, '16 gleiche Platten wiegen zusammen 40 kg. Wie schwer sind 24 Platten?', '40 / 2 * 3', 'Über 8 Platten: 40 kg : 2 = 20 kg. 24 Platten: 3 · 20 kg = 60 kg.', 'Welche Zahl passt in 16 und in 24?', einheit='kg'),
        wahl(3, 'Du kennst den Preis für 45 Stück und suchst den Preis für 75 Stück. Welcher Zwischenschritt passt ohne Rest in beide Zahlen und ist am größten?', list(zw),
             lambda o: zw[o] == max(v for v in zw.values() if 45 % v == 0 and 75 % v == 0),
             '15 passt in 45 (3-mal) und in 75 (5-mal). 30 passt nicht ohne Rest; 5 und 1 gehen auch, sind aber kleiner.', 'Prüfe für jede Zahl, ob sie ohne Rest in 45 und in 75 passt.'),
        Z(3, 'Ein Drucker druckt 18 Seiten in 45 Sekunden. Wie viele Seiten schafft er in 2 Minuten?', '18 / 45 * 120',
          '2 min = 120 s. Über 15 s: 18 : 3 = 6 Seiten. 120 s sind 8-mal 15 s: 8 · 6 = 48 Seiten.', 'Rechne 2 Minuten in Sekunden um. Welche Zeit passt in 45 s und in 120 s?'),
        Z(3, 'Rechne geschickt: 0,5 kg Kirschen kosten 3,40 €. Was kosten 1,5 kg?', '3.4 * 3', '1,5 kg sind 3-mal 0,5 kg: 3 · 3,40 € = 10,20 €.', 'Wie oft passen 0,5 kg in 1,5 kg?', einheit='€'),
    ]
    N['sach'] = [
        Z(2, 'Ein Rezept für 6 Personen braucht 300 ml Sahne. Wie viel ml braucht man für 4 Personen?', '300 / 6 * 4', '1 Person: 50 ml. 4 Personen: 200 ml.', 'Gehe über 2 Personen oder über 1 Person.', einheit='ml'),
        Z(2, 'Ein Auto braucht für 100 km 6 Liter Benzin. Wie viele Liter braucht es für 250 km?', '6 * 250 / 100', '250 km sind 2,5-mal 100 km: 2,5 · 6 l = 15 l. Oder über 50 km: 3 l · 5 = 15 l.',
          'Wie viel braucht es für 50 km?', einheit='l'),
        L(3, 'Ein Liter Apfelsaft kostet 1,20 €. Für das Klassenfest gibt es 15 €. Wie viele ganze Liter kann man kaufen, und wie viel Geld bleibt übrig?',
          '□ Liter, Rest □ ct', 'Trage die Liter und den Rest in Cent ein.', ['1500 // 120', '1500 % 120'],
          '15 € = 1 500 ct. 1 500 : 120 = 12 Rest 60. Also 12 Liter, es bleiben 60 ct.', 'Rechne in Cent: 1 500 ct : 120 ct.'),
        wahl(3, 'Ein Kind läuft 100 m in 16 Sekunden. Wie lange braucht es für 1 000 m?', ['Das kann man so nicht ausrechnen: Auf langen Strecken wird man langsamer.', '160 Sekunden', '16 Sekunden', '1 600 Sekunden'],
             lambda o: o.startswith('Das kann man'), 'Laufzeit und Strecke sind nicht proportional: Niemand hält das Sprinttempo 1 000 m lang durch.',
             'Prüfe zuerst, ob die Zuordnung proportional ist.'),
        Z(3, 'Eine Kerze brennt in 3 Stunden 4 cm ab. Sie ist 18 cm lang. Wie viele Stunden brennt sie insgesamt?', '18 / 4 * 3',
          '1 cm brennt in 3 h : 4 = 0,75 h ab. 18 cm: 18 · 0,75 h = 13,5 h. Oder: 18 cm sind 4,5-mal 4 cm, also 4,5 · 3 h.', 'Wie oft passen 4 cm in 18 cm?', einheit='h'),
        Z(3, 'Ein Wasserhahn tropft. In 10 Minuten sammeln sich 60 ml. Wie viele Liter tropfen an einem ganzen Tag?', '60 / 10 * 60 * 24 / 1000',
          '1 Minute: 6 ml. 1 Stunde: 360 ml. 1 Tag: 24 · 360 ml = 8 640 ml = 8,64 l.', 'Rechne zuerst pro Stunde, dann pro Tag. Zum Schluss in Liter umrechnen.', einheit='l'),
    ]
    return N


ergaenze(DATEI, _schwer(), 1026)

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('groessen.proportional', 13_5_5)
# a) Lied-Falle stand auf Stufe 1, Eier-Falle zweimal auf Stufe 3 (gleicher Gedanke wie Stufe 2) → einheitlich Stufe 2
BF.stufe('sach', 'Ein Lied dauert 4 Minuten, wenn 4 Kinder es singen. Wie viele Minuten dauert es, wenn 9 Kinder singen?', 2)
BF.stufe('sach', '2 Eier kochen 10 Minuten. Wie viele Minuten kochen 8 Eier im selben Topf?', 2)
BF.stufe('sach', '3 Eier kochen 9 Minuten. Wie viele Minuten kochen 5 Eier im selben Topf?', 2)
# c) „etwa 200 Liter“ wirkt falsch, weil 240 l leicht genau zu rechnen ist → genaue Antwort
BF.ersetze('sach', 'Ein Hahn füllt in 4 Minuten einen Eimer mit 48 Litern. Ungefähr wie viele Liter laufen in 20 Minuten?', BF.A(
    'Aus einem Hahn laufen in 4 Minuten 48 Liter Wasser, jede Minute gleich viel. Wie viele Liter laufen in 20 Minuten?', '240 Liter',
    ['68 Liter', '960 Liter', '2 400 Liter'],
    'In 1 Minute sind es 48 : 4 = 12 Liter. In 20 Minuten: 12 · 20 = 240 Liter. Nur dazuzählen (48 + 20 = 68) ist falsch.',
    'Wie viel ist es in 1 Minute? Wie oft so viel brauchst du?'))
BF.ersetze('sach', 'Ein Hahn füllt in 2 Minuten einen Eimer mit 24 Litern. Ungefähr wie viele Liter laufen in 20 Minuten?', BF.A(
    'Aus einem Hahn laufen in 2 Minuten 24 Liter Wasser, jede Minute gleich viel. Wie viele Liter laufen in 20 Minuten?', '240 Liter',
    ['44 Liter', '480 Liter', '2 400 Liter'],
    'In 1 Minute sind es 24 : 2 = 12 Liter. In 20 Minuten: 12 · 20 = 240 Liter. Nur dazuzählen (24 + 20 = 44) ist falsch.',
    'Wie viel ist es in 1 Minute? Wie oft so viel brauchst du?'))
# a) Standard-Dreisatz → Stufe 2
BF.stufe('dreisatz', '20 Hefte kosten 80 €. 11 Hefte kosten wie viel €?', 2)

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----

if __name__ == '__main__':
    schreibe(DATEI, 'groessen.proportional.json')
