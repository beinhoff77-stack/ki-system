#!/usr/bin/env python3
"""Thema zahlen.schranken – Schranken und Genauigkeit (ohne Lehrplan-Zuordnung, Niveau Klasse 9/10)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403

start(7010)

GENAU = [  # (Schrittweite, Wortlaut)
    (Fr(10), 'auf Zehner gerundet'), (Fr(100), 'auf Hunderter gerundet'), (Fr(1), 'auf Ganze gerundet'),
    (Fr(1, 10), 'auf eine Nachkommastelle gerundet'), (Fr(5), 'auf 5 genau gerundet'), (Fr(1, 100), 'auf zwei Nachkommastellen gerundet'),
]
MESS = [  # (Größe, Einheit, Schritt, Wortlaut, Bereich)
    ('Länge eines Tisches', 'cm', Fr(1), 'auf ganze cm gemessen', (120, 200)),
    ('Masse eines Pakets', 'kg', Fr(1, 10), 'auf 0,1 kg genau gewogen', (2, 20)),
    ('Laufzeit über 100 m', 's', Fr(1, 10), 'auf Zehntelsekunden gestoppt', (11, 18)),
    ('Breite eines Zimmers', 'm', Fr(1, 10), 'auf 10 cm genau gemessen', (3, 6)),
    ('Besucherzahl', 'Personen', Fr(100), 'auf Hunderter gerundet', (2000, 9000)),
    ('Strecke', 'km', Fr(1), 'auf ganze km gerundet', (20, 300)),
]


def wert_mit(schritt, lo, hi):
    k0, k1 = int(lo / schritt), int(hi / schritt)
    return schritt * R.randint(k0, k1)


def grenzen(x, schritt):
    return x - schritt / 2, x + schritt / 2


def e(einheit):
    return f' {einheit}' if einheit else ''


ETAPPEN = [
    {'lernziel': 'grenzen', 'titel': 'Untere und obere Schranke',
     'regel': 'Ein gerundeter Wert verrät nur einen ⟦Bereich⟧ für den wahren Wert x. Die ⟦untere Schranke⟧ (lower bound) liegt eine ⟦halbe Rundungseinheit darunter⟧, die ⟦obere Schranke⟧ (upper bound) eine halbe darüber. Man schreibt den ⟦Fehlerbereich⟧ (error interval) als ⟦untere ≤ x < obere⟧.',
     'schritte': ['Eine Länge ist auf ganze cm gerundet: 27 cm. Rundungseinheit 1 cm, die Hälfte 0,5 cm.', 'Untere Schranke 26,5 cm, obere Schranke 27,5 cm.', 'Fehlerbereich: ⟦26,5 cm ≤ x < 27,5 cm⟧.'],
     'probe': '26,5 wird auf 27 aufgerundet, 27,5 aber schon auf 28 ✓',
     'bild': {'typ': 'koordinaten', 'x': [26, 28], 'y': [0, 2], 'schritt_x': 0.5, 'schritt_y': 1, 'name_x': 'cm', 'name_y': ' ',
              'punkte': [{'x': 26.5, 'y': 1, 'name': '26,5'}, {'x': 27, 'y': 1, 'name': '27'}, {'x': 27.5, 'y': 1, 'name': '27,5', 'offen': True}],
              'strecken': [[26.5, 1, 27.5, 1]]},
     'fehler': 'Bei „auf Zehner gerundet: 70“ den Bereich 69 bis 71 anzugeben ist falsch: Die Rundungseinheit ist 10, die Hälfte also ⟦5⟧. Richtig: 65 ≤ x < 75.'},
    {'lernziel': 'messen', 'titel': 'Genauigkeit von Messungen',
     'regel': 'Jede Messung ist nur ⟦so genau wie das Messgerät⟧. „Auf 0,1 kg genau“ heißt: Rundungseinheit 0,1 kg, also ⟦± 0,05 kg⟧. Der wahre Wert liegt im Fehlerbereich; die obere Schranke selbst gehört ⟦nicht mehr dazu⟧.',
     'schritte': ['Ein Paket wiegt auf 0,1 kg genau 4,3 kg.', 'Halbe Einheit: 0,05 kg. Bereich: ⟦4,25 kg ≤ m < 4,35 kg⟧.'],
     'probe': '4,25 und 4,349 werden beide zu 4,3 gerundet ✓',
     'fehler': 'Bei „auf 0,1 kg genau 4,3 kg“ den Bereich 4,2 kg bis 4,4 kg anzugeben ist falsch: Das wäre ± 0,1 kg. Man geht nur ⟦eine halbe Einheit⟧ (0,05 kg) nach unten und oben.'},
    {'lernziel': 'summe', 'titel': 'Schranken bei Summen und Differenzen',
     'regel': '⟦Größte Summe⟧: obere + obere Schranke. ⟦Kleinste Summe⟧: untere + untere. Bei der ⟦Differenz⟧ a − b: größte = ⟦obere(a) − untere(b)⟧, kleinste = untere(a) − obere(b).',
     'schritte': ['a = 12 cm, b = 5 cm, beide auf ganze cm gerundet.', 'Größte Differenz: 12,5 cm − 4,5 cm = ⟦8 cm⟧.', 'Kleinste Differenz: 11,5 cm − 5,5 cm = 6 cm.'],
     'probe': 'Für eine große Differenz: a möglichst groß, b möglichst klein ✓',
     'fehler': 'Die größte Differenz als obere − obere (12,5 − 5,5 = 7) zu berechnen ist falsch: Man ⟦zieht möglichst wenig ab⟧, also die ⟦untere⟧ Schranke von b: 12,5 − 4,5 = 8.'},
    {'lernziel': 'produkt', 'titel': 'Schranken bei Produkten und Quotienten',
     'regel': 'Bei positiven Größen gilt: ⟦größtes Produkt⟧ = obere · obere, kleinstes = untere · untere. Beim ⟦Quotienten⟧ a : b: größter = ⟦obere(a) : untere(b)⟧, kleinster = untere(a) : obere(b).',
     'schritte': ['Ein Rechteck: 8 cm und 5 cm, auf ganze cm gerundet.', 'Größte Fläche: 8,5 cm · 5,5 cm = ⟦46,75 cm²⟧.', 'Kleinste Fläche: 7,5 cm · 4,5 cm = 33,75 cm².'],
     'probe': '33,75 ≤ A < 46,75; der gerundete Wert 8 · 5 = 40 liegt dazwischen ✓',
     'fehler': 'Die größte Geschwindigkeit als obere Strecke : obere Zeit zu berechnen ist falsch: Durch eine ⟦kleinere⟧ Zahl geteilt ergibt mehr – also ⟦obere Strecke : untere Zeit⟧.'},
    {'lernziel': 'entscheiden', 'titel': 'Mit Schranken entscheiden',
     'regel': 'Bei Sicherheitsfragen rechnet man mit dem ⟦ungünstigsten Fall⟧ (worst case): Passt es ⟦auch mit den Schranken⟧ sicher, ist die Antwort „ja, sicher“. Ein Ergebnis gibt man nur so genau an, wie es ⟦beide Schranken hergeben⟧.',
     'schritte': ['Ein Aufzug darf 630 kg tragen. 8 Personen wiegen je 78 kg (auf ganze kg gerundet).', 'Ungünstigster Fall: 8 · 78,5 kg = ⟦628 kg⟧.', '628 kg < 630 kg: ⟦sicher erlaubt⟧.'],
     'probe': 'Mit gerundeten Werten wären es 624 kg – die Reserve wäre kleiner als gedacht ✓',
     'fehler': 'Nur mit den gerundeten Werten zu rechnen (8 · 78 = 624 kg) und daraus „sicher“ zu folgern ist riskant: Der ⟦wahre⟧ Wert kann bis zu 628 kg betragen. Für die Sicherheit zählt die ⟦obere Schranke⟧.'},
]


def g_grenzen(s):
    sch, wort = R.choice(GENAU[:3] if s == 1 else GENAU)
    x = sch * R.randint(3, 99) if sch >= 1 else sch * R.randint(11, 999)
    lo, hi = grenzen(x, sch)
    art = R.choice({1: ['luecke', 'unten', 'oben'], 2: ['unten', 'oben', 'luecke', 'welcher'], 3: ['welcher', 'rueck', 'nicht', 'oben']}[s])
    vor = f'Eine Zahl x ist {wort}: {dz(x)}.'
    if art == 'luecke':
        if lo.denominator != 1 or hi.denominator != 1: return None
        return luecken(vor + ' Gib den Fehlerbereich an.', '□ ≤ x < □', 'untere und obere Schranke', [int(lo), int(hi)],
                       f'Halbe Rundungseinheit: {dz(sch / 2)}. {dz(x)} − {dz(sch / 2)} = {dz(lo)}, {dz(x)} + {dz(sch / 2)} = {dz(hi)}.',
                       'Rundungseinheit halbieren, dann abziehen und addieren.', c=[f'{float(x)} - {float(sch)} / 2', f'{float(x)} + {float(sch)} / 2'])
    if art == 'unten':
        return zahl(vor + ' Wie groß ist die untere Schranke?', f'Halbe Rundungseinheit {dz(sch / 2)}: {dz(x)} − {dz(sch / 2)} = {dz(lo)}.', 'Ziehe eine halbe Rundungseinheit ab.', lo, f'{float(x)} - {float(sch)} / 2')
    if art == 'oben':
        return zahl(vor + ' Wie groß ist die obere Schranke?', f'Halbe Rundungseinheit {dz(sch / 2)}: {dz(x)} + {dz(sch / 2)} = {dz(hi)}.', 'Addiere eine halbe Rundungseinheit.', hi, f'{float(x)} + {float(sch)} / 2')
    if art == 'welcher':
        r = f'{dz(lo)} ≤ x < {dz(hi)}'
        return auswahl(vor + ' Welcher Fehlerbereich ist richtig?', r,
                       [f'{dz(x - sch)} ≤ x < {dz(x + sch)}', f'{dz(lo)} < x ≤ {dz(hi)}', f'{dz(x)} ≤ x < {dz(x + sch)}'],
                       f'Eine halbe Einheit ({dz(sch / 2)}) nach unten und oben; die untere Schranke gehört dazu, die obere nicht (sie würde aufgerundet).',
                       'Wie groß ist die halbe Rundungseinheit? Welche Grenze wird noch auf den Wert gerundet?')
    if art == 'nicht':
        kand = [lo, x + sch / 4, hi - sch / 10 if sch >= Fr(1, 10) else x, hi]
        r = dz(hi)
        falsch = [dz(k) for k in kand if k != hi]
        return auswahl(vor + ' Welcher Wert kann x NICHT sein?', r, falsch,
                       f'Fehlerbereich {dz(lo)} ≤ x < {dz(hi)}. {dz(hi)} würde schon auf {dz(x + sch)} gerundet.', 'Prüfe, worauf jeder Wert gerundet würde.')
    return zahl(f'Der Fehlerbereich einer gerundeten Zahl ist {dz(lo)} ≤ x < {dz(hi)}. Auf welchen Wert wurde gerundet?', f'Mitte des Bereichs: ({dz(lo)} + {dz(hi)}) : 2 = {dz(x)}.',
                'Der gerundete Wert liegt genau in der Mitte.', x, f'({float(lo)} + {float(hi)}) / 2')


def g_messen(s):
    g, ein, sch, wort, (a, b) = R.choice(MESS)
    x = wert_mit(sch, a, b)
    lo, hi = grenzen(x, sch)
    art = R.choice({1: ['unten', 'oben'], 2: ['unten', 'oben', 'spanne', 'welcher'], 3: ['moeglich', 'spanne', 'genauigkeit']}[s])
    vor = f'{g}: {dz(x)} {ein}, {wort}.'
    if art == 'unten':
        return zahl(vor + ' Wie groß ist die untere Schranke?', f'Halbe Einheit {dz(sch / 2)} {ein}: {dz(x)} − {dz(sch / 2)} = {dz(lo)} {ein}.', 'Welche Einheit hat die Genauigkeit? Davon die Hälfte abziehen.',
                    lo, f'{float(x)} - {float(sch)} / 2', einheit=ein)
    if art == 'oben':
        return zahl(vor + ' Wie groß ist die obere Schranke?', f'Halbe Einheit {dz(sch / 2)} {ein}: {dz(x)} + {dz(sch / 2)} = {dz(hi)} {ein}.', 'Die Hälfte der Genauigkeit addieren.',
                    hi, f'{float(x)} + {float(sch)} / 2', einheit=ein)
    if art == 'spanne':
        return zahl(vor + ' Wie groß ist der Abstand zwischen oberer und unterer Schranke?', f'{dz(hi)} − {dz(lo)} = {dz(sch)} {ein} – genau eine Rundungseinheit.',
                    'Berechne beide Schranken oder überlege, wie breit der Bereich ist.', sch, f'{float(hi)} - {float(lo)}', einheit=ein)
    if art == 'welcher':
        r = f'{dz(lo)} {ein} ≤ x < {dz(hi)} {ein}'
        return auswahl(vor + ' Welcher Fehlerbereich passt?', r,
                       [f'{dz(x - sch)} {ein} ≤ x < {dz(x + sch)} {ein}', f'{dz(x)} {ein} ≤ x < {dz(x + sch)} {ein}', f'{dz(lo)} {ein} < x ≤ {dz(hi)} {ein}'],
                       f'± halbe Einheit ({dz(sch / 2)} {ein}); obere Schranke ausgeschlossen.', 'Halbe Messgenauigkeit nach unten und oben.')
    if art == 'moeglich':
        v = R.choice([lo, hi, lo - sch / 10, x + sch / 5])
        ok = lo <= v < hi
        return ja_nein(vor + f' Kann der wahre Wert {dz(v)} {ein} sein?', ok, f'Fehlerbereich: {dz(lo)} {ein} ≤ x < {dz(hi)} {ein}. {dz(v)} liegt {"darin" if ok else "nicht darin"}.',
                       'Bestimme den Fehlerbereich; Achtung bei den Grenzen.')
    x2 = wert_mit(sch, a, b)
    r = wort
    return auswahl(f'Der wahre Wert einer Messung ({g}) liegt zwischen {dz(x2 - sch / 2)} {ein} und {dz(x2 + sch / 2)} {ein}. Wie genau wurde gemessen?', r,
                   [w for _, _, _, w, _ in MESS if w != wort][:3],
                   f'Die Breite des Bereichs ({dz(sch)} {ein}) ist die Messgenauigkeit: {wort}.', 'Wie breit ist der Bereich?')


def g_summe(s):
    sch = R.choice([Fr(1), Fr(1, 10), Fr(10)])
    ein = {Fr(1): 'cm', Fr(1, 10): 'kg', Fr(10): 'm'}[sch]
    a, b = sorted([sch * R.randint(20, 90), sch * R.randint(5, 60)], reverse=True)
    if a == b: return None
    la, ha = grenzen(a, sch)
    lb, hb = grenzen(b, sch)
    wort = {Fr(1): 'auf ganze cm', Fr(1, 10): 'auf 0,1 kg', Fr(10): 'auf 10 m'}[sch]
    art = R.choice({1: ['max_sum', 'min_sum'], 2: ['max_sum', 'max_diff', 'min_diff', 'min_sum'], 3: ['max_diff', 'min_diff', 'umfang', 'drei']}[s])
    vor = f'a = {dz(a)} {ein} und b = {dz(b)} {ein}, beide {wort} gerundet.'
    if art == 'max_sum':
        return zahl(vor + ' Wie groß kann a + b höchstens sein (obere Schranke)?', f'{dz(ha)} + {dz(hb)} = {dz(ha + hb)} {ein}.', 'Obere + obere Schranke.', ha + hb, f'{float(ha)} + {float(hb)}', einheit=ein)
    if art == 'min_sum':
        return zahl(vor + ' Wie groß ist a + b mindestens (untere Schranke)?', f'{dz(la)} + {dz(lb)} = {dz(la + lb)} {ein}.', 'Untere + untere Schranke.', la + lb, f'{float(la)} + {float(lb)}', einheit=ein)
    if art == 'max_diff':
        return zahl(vor + ' Wie groß ist die obere Schranke von a − b?', f'Größte Differenz: obere(a) − untere(b) = {dz(ha)} − {dz(lb)} = {dz(ha - lb)} {ein}.',
                    'a möglichst groß, b möglichst klein.', ha - lb, f'{float(ha)} - {float(lb)}', einheit=ein)
    if art == 'min_diff':
        return zahl(vor + ' Wie groß ist die untere Schranke von a − b?', f'Kleinste Differenz: untere(a) − obere(b) = {dz(la)} − {dz(hb)} = {dz(la - hb)} {ein}.',
                    'a möglichst klein, b möglichst groß.', la - hb, f'{float(la)} - {float(hb)}', einheit=ein)
    if art == 'umfang':
        return zahl(f'Ein Rechteck hat die Seiten {dz(a)} {ein} und {dz(b)} {ein} ({wort} gerundet). Wie groß ist die obere Schranke des Umfangs?',
                    f'u = 2 · ({dz(ha)} + {dz(hb)}) = {dz(2 * (ha + hb))} {ein}.', 'Umfang = 2 · (a + b) – mit beiden oberen Schranken.', 2 * (ha + hb),
                    f'2 * ({float(ha)} + {float(hb)})', einheit=ein)
    c = sch * R.randint(5, 40)
    lc, hc = grenzen(c, sch)
    return zahl(f'Drei Strecken: {dz(a)} {ein}, {dz(b)} {ein} und {dz(c)} {ein}, alle {wort} gerundet. Wie groß ist die untere Schranke der Gesamtlänge?',
                f'{dz(la)} + {dz(lb)} + {dz(lc)} = {dz(la + lb + lc)} {ein}.', 'Alle unteren Schranken addieren.', la + lb + lc, f'{float(la)} + {float(lb)} + {float(lc)}', einheit=ein)


def g_produkt(s):
    art = R.choice({1: ['flaeche_max', 'flaeche_min'], 2: ['flaeche_max', 'tempo_max', 'flaeche_min', 'tempo_min'], 3: ['tempo_max', 'tempo_min', 'menge', 'quader']}[s])
    if art in ('flaeche_max', 'flaeche_min', 'quader'):
        a, b = R.randint(3, 20), R.randint(2, 15)
        la, ha, lb, hb = a - Fr(1, 2), a + Fr(1, 2), b - Fr(1, 2), b + Fr(1, 2)
        if art == 'quader':
            c = R.randint(2, 10)
            lc, hc = c - Fr(1, 2), c + Fr(1, 2)
            return zahl(f'Ein Quader ist {a} cm × {b} cm × {c} cm groß (auf ganze cm gerundet). Wie groß ist die obere Schranke des Volumens (in cm³)?',
                        f'V = {dz(ha)} · {dz(hb)} · {dz(hc)} = {dz(ha * hb * hc)} cm³.', 'Alle drei oberen Schranken multiplizieren.', ha * hb * hc,
                        f'{float(ha)} * {float(hb)} * {float(hc)}', einheit='cm³')
        if art == 'flaeche_max':
            return zahl(f'Ein Rechteck ist {a} cm lang und {b} cm breit (auf ganze cm gerundet). Wie groß ist die obere Schranke der Fläche?', f'A = {dz(ha)} · {dz(hb)} = {dz(ha * hb)} cm².',
                        'Obere · obere Schranke.', ha * hb, f'{float(ha)} * {float(hb)}', einheit='cm²')
        return zahl(f'Ein Rechteck ist {a} cm lang und {b} cm breit (auf ganze cm gerundet). Wie groß ist die untere Schranke der Fläche?', f'A = {dz(la)} · {dz(lb)} = {dz(la * lb)} cm².',
                    'Untere · untere Schranke.', la * lb, f'{float(la)} * {float(lb)}', einheit='cm²')
    if art in ('tempo_max', 'tempo_min'):
        for _ in range(100):
            d = R.choice([100, 200, 400, 120, 150, 300])
            t = R.choice([10, 12, 15, 16, 20, 25, 40, 50, 60, 80])
            lt, ht = t - Fr(1, 2), t + Fr(1, 2)
            ld, hd = d - Fr(1, 2), d + Fr(1, 2)
            v = hd / lt if art == 'tempo_max' else ld / ht
            g = gerundet(float(v), 2)
            if g is not None: break
        else:
            return None
        w_ = (f'Größte Geschwindigkeit: obere Strecke : untere Zeit = {dz(hd)} : {dz(lt)} ≈ {dz(g)} m/s.' if art == 'tempo_max' else
              f'Kleinste Geschwindigkeit: untere Strecke : obere Zeit = {dz(ld)} : {dz(ht)} ≈ {dz(g)} m/s.')
        return zahl(f'Ein Läufer legt {d} m in {t} s zurück (beides auf ganze Einheiten gerundet). Berechne die {"obere" if art == "tempo_max" else "untere"} Schranke seiner Geschwindigkeit in m/s (auf zwei Nachkommastellen).',
                    w_, 'Bei einem Quotienten: Für das Maximum durch die kleinste Zahl teilen.', g,
                    f'round({float(hd)} / {float(lt)}, 2)' if art == 'tempo_max' else f'round({float(ld)} / {float(ht)}, 2)', einheit='m/s', tol=0.01)
    gesamt = R.choice([500, 1000, 1500, 2000])
    glas = R.choice([200, 250])
    lg, hgl = gesamt - 5, glas + 5
    n = Fr(lg, hgl)
    sicher = int(n)
    return zahl(f'In einem Behälter sind {dz(gesamt)} ml Saft (auf 10 ml gerundet). Ein Glas fasst {glas} ml (auf 10 ml gerundet). Wie viele Gläser kann man auf jeden Fall vollständig füllen?',
                f'Ungünstigster Fall: wenig Saft ({dz(lg)} ml), große Gläser ({dz(hgl)} ml). {dz(lg)} : {dz(hgl)} ≈ {dz(round(float(n), 2))} → sicher {sicher} volle Gläser.',
                'Rechne mit der kleinsten Saftmenge und dem größten Glas.', sicher, f'{lg} // {hgl}')


def g_entscheiden(s):
    art = R.choice({1: ['aufzug', 'passt'], 2: ['aufzug', 'passt', 'fehler'], 3: ['fehler', 'genauigkeit_ergebnis', 'aufzug', 'brett']}[s])
    if art == 'aufzug':
        n = R.randint(6, 10)
        m = R.randint(70, 85)
        grenze_ = R.choice([n * m + R.choice([2, 3, 4, 6, 8]), n * m + n // 2 + 10, n * m + n // 2 - 1])
        worst = n * (m + Fr(1, 2))
        ok = worst <= grenze_
        return ja_nein(f'Ein Aufzug darf höchstens {grenze_} kg tragen. {n} Personen wiegen je {m} kg (auf ganze kg gerundet). Ist die Fahrt sicher erlaubt?', ok,
                       f'Ungünstigster Fall: {n} · {dz(m + Fr(1, 2))} kg = {dz(worst)} kg {"≤" if ok else ">"} {grenze_} kg: {"sicher erlaubt" if ok else "nicht sicher erlaubt"}.',
                       'Rechne mit der oberen Schranke des Gewichts.')
    if art == 'passt':
        b = R.randint(60, 120)
        luecke_ = b + R.choice([0, 2])
        return ja_nein(f'Ein Schrank ist {b} cm breit, die Lücke in der Küche {luecke_} cm (beide auf ganze cm gerundet). Passt der Schrank sicher hinein?', luecke_ - Fr(1, 2) >= b + Fr(1, 2),
                       f'Ungünstigster Fall: Schrank {dz(b + Fr(1, 2))} cm, Lücke {dz(luecke_ - Fr(1, 2))} cm. ' + ('Passt sicher.' if luecke_ - Fr(1, 2) >= b + Fr(1, 2) else 'Nicht sicher – es kann knapp nicht passen.'),
                       'Größtmöglicher Schrank gegen kleinstmögliche Lücke.')
    if art == 'fehler':
        a, b = R.randint(20, 60), R.randint(5, 19)
        r = f'Falsch: richtig ist {dz(a + Fr(1, 2))} − {dz(b - Fr(1, 2))} = {dz(a - b + 1)}.'
        return auswahl(f'a = {a} cm, b = {b} cm (auf ganze cm gerundet). Jana berechnet die obere Schranke von a − b als {dz(a + Fr(1, 2))} − {dz(b + Fr(1, 2))} = {a - b}. Stimmt das?', r,
                       ['Richtig.', f'Falsch: richtig ist {a} − {b} = {a - b}.', f'Falsch: richtig ist {dz(a - Fr(1, 2))} − {dz(b - Fr(1, 2))} = {a - b}.'],
                       'Für die größte Differenz zieht man möglichst wenig ab: die untere Schranke von b.', 'Welche Schranke von b macht a − b am größten?')
    if art == 'genauigkeit_ergebnis':
        a, b = R.randint(5, 15), R.randint(5, 15)
        lo, hi = (a - Fr(1, 2)) * (b - Fr(1, 2)), (a + Fr(1, 2)) * (b + Fr(1, 2))
        r = f'Zwischen {dz(lo)} cm² und {dz(hi)} cm² – „{a * b} cm²“ täuscht eine Genauigkeit vor, die es nicht gibt.'
        return auswahl(f'Ein Rechteck misst {a} cm × {b} cm (auf ganze cm gerundet). Was lässt sich über die Fläche sicher sagen?', r,
                       [f'Sie ist genau {a * b} cm².', f'Sie liegt zwischen {a * b - 1} cm² und {a * b + 1} cm².', f'Sie liegt zwischen {dz(lo)} cm² und {dz(lo + 1)} cm².'],
                       f'Untere Schranke {dz(a - Fr(1, 2))} · {dz(b - Fr(1, 2))} = {dz(lo)}, obere {dz(a + Fr(1, 2))} · {dz(b + Fr(1, 2))} = {dz(hi)}.',
                       'Berechne untere und obere Schranke der Fläche.')
    n = R.randint(4, 8)
    lang = R.randint(25, 45)
    brett = n * lang + R.choice([0, 1, 2, 3])
    ok = (brett - Fr(1, 2)) >= n * (lang + Fr(1, 2))
    return ja_nein(f'Aus einem {brett} cm langen Brett sollen {n} Stücke von je {lang} cm gesägt werden (alle Maße auf ganze cm gerundet, Sägeschnitte vernachlässigt). Reicht das Brett sicher?', ok,
                   f'Ungünstigster Fall: Brett {dz(brett - Fr(1, 2))} cm, Stücke {n} · {dz(lang + Fr(1, 2))} = {dz(n * (lang + Fr(1, 2)))} cm. ' + ('Reicht sicher.' if ok else 'Reicht nicht sicher.'),
                   'Kürzestes Brett gegen längste Stücke.')


GEN = {'grenzen': g_grenzen, 'messen': g_messen, 'summe': g_summe, 'produkt': g_produkt, 'entscheiden': g_entscheiden}

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import tab  # noqa: E402


def _zs(a, b, n, **kw):
    return {'typ': 'zahlenstrahl', 'start': a, 'ende': b, 'abschnitte': n, 'beschriftet': kw.pop('beschriftet', 'alle'), **kw}


def _pk(*w):
    return [{'wert': x, 'name': n} for x, n in w]


def _sk(a, b):
    return tab(['', 'untere', 'obere'], ['a = 12 cm', *a], ['b = 5 cm', *b])


def _re(l, b, tl, tb):
    return {'typ': 'figur', 'punkte': {'_A': [0, 0], '_B': [l, 0], '_C': [l, b], '_D': [0, b]}, 'flaeche': ['_A', '_B', '_C', '_D'],
            'linien': [['_A', '_B', tl], ['_B', '_C', tb], ['_C', '_D'], ['_D', '_A']]}


UMBAU = {
    'grenzen': {
        'einstieg': 'Auf einem Zettel steht: Das Brett ist 27 cm lang, auf ganze cm gerundet. Wirklich kann es 26,8 cm oder 27,4 cm sein. '
                    'Der wahre Wert liegt in einem ⟦Fehlerbereich⟧.',
        'woerter': [['untere Schranke', 'der kleinste Wert, der noch auf 27 gerundet wird'],
                    ['obere Schranke', 'ab hier wird schon auf 28 gerundet; der Wert gehört nicht mehr dazu'],
                    ['Fehlerbereich', 'untere ≤ x < obere']],
        'bild': _zs(26, 28, 4, punkte=_pk((27, '27'))),
        'schritte': [
            {'text': 'Rundungseinheit 1 cm, die Hälfte ist 0,5 cm.'},
            {'text': 'Untere Schranke: 27 − 0,5 = 26,5 cm.', 'bild': {'punkte': _pk((27, '27'), (26.5, 'untere'))}},
            {'text': 'Obere Schranke: 27 + 0,5 = 27,5 cm.', 'bild': {'punkte': _pk((27, '27'), (26.5, 'untere'), (27.5, 'obere'))}},
            {'text': 'Fehlerbereich: ⟦26,5 cm ≤ x < 27,5 cm⟧.', 'bild': {'bereich': {'von': 26.5, 'bis': 27.5}}},
        ],
        'fehler': 'Bei „auf Zehner gerundet: 70“ ist 69 bis 71 falsch. Die halbe Rundungseinheit ist ⟦5⟧: 65 ≤ x < 75.',
        'fehler_bild': _zs(60, 80, 4, punkte=_pk((70, '70')), bereich={'von': 65, 'bis': 75}),
        'regel': 'Eine ⟦halbe Rundungseinheit⟧ nach unten und nach oben. Fehlerbereich: untere ≤ x < obere.',
    },
    'messen': {
        'einstieg': 'Eine Paketwaage zeigt 4,3 kg, sie misst auf 0,1 kg genau. Das Paket kann also etwas leichter oder schwerer sein. '
                    'Jede Messung ist nur so ⟦genau wie das Messgerät⟧.',
        'woerter': [['auf 0,1 kg genau', 'die Waage rundet auf Zehntel-Kilogramm']],
        'bild': _zs(4.2, 4.4, 4, punkte=_pk((4.3, '4,3'))),
        'schritte': [
            {'text': 'Rundungseinheit 0,1 kg, die Hälfte ist 0,05 kg.'},
            {'text': 'Untere Schranke 4,25 kg, obere Schranke 4,35 kg.', 'bild': {'punkte': _pk((4.3, '4,3'), (4.25, 'untere'), (4.35, 'obere'))}},
            {'text': 'Bereich: ⟦4,25 kg ≤ m < 4,35 kg⟧.', 'bild': {'bereich': {'von': 4.25, 'bis': 4.35}}},
        ],
        'fehler': '4,2 kg bis 4,4 kg ist falsch, das wären ± 0,1 kg. Nur ⟦eine halbe Einheit⟧, 0,05 kg, nach unten und oben.',
        'fehler_bild': {'punkte': _pk((4.3, '4,3')), 'bereich': {'von': 4.2, 'bis': 4.4}},
        'regel': '„Auf 0,1 genau“ heißt ⟦± 0,05⟧. Die obere Schranke selbst gehört nicht mehr dazu.',
    },
    'summe': {
        'einstieg': 'Ein Brett ist 12 cm lang, du sägst 5 cm ab. Beide Maße sind auf ganze cm gerundet. Wie lang ist der Rest höchstens? '
                    'Gesucht ist die ⟦größte Differenz⟧.',
        'woerter': [['Differenz', 'das Ergebnis einer Minus-Rechnung']],
        'bild': _sk(['11,5', '12,5'], ['4,5', '5,5']),
        'schritte': [
            {'text': 'Größte Differenz: a möglichst groß, b möglichst klein.'},
            {'text': '12,5 cm − 4,5 cm = ⟦8 cm⟧.', 'bild': _sk(['11,5', '12,5 ✓'], ['4,5 ✓', '5,5'])},
            {'text': 'Kleinste Differenz: 11,5 cm − 5,5 cm = 6 cm.', 'bild': _sk(['11,5 ✓', '12,5'], ['4,5', '5,5 ✓'])},
            {'text': 'Bei Summen gilt: obere + obere und untere + untere.'},
        ],
        'fehler': 'Obere − obere, also 12,5 − 5,5 = 7, ist falsch. Man ⟦zieht möglichst wenig ab⟧, also die untere Schranke von b.',
        'fehler_bild': _sk(['11,5', '12,5 ✓'], ['4,5', '5,5 ✗']),
        'regel': 'Größte Summe: obere + obere. ⟦Größte Differenz: obere − untere⟧.',
    },
    'produkt': {
        'einstieg': 'Eine Fliese ist 8 cm lang und 5 cm breit, beides auf ganze cm gerundet. Wie groß ist sie höchstens? '
                    'Man rechnet mit den ⟦Schranken⟧.',
        'woerter': [['Quotient', 'das Ergebnis einer Geteilt-Rechnung']],
        'bild': _re(8, 5, '8 cm', '5 cm'),
        'schritte': [
            {'text': 'Größte Fläche: obere mal obere, 8,5 cm · 5,5 cm.', 'bild': _re(8.5, 5.5, '8,5 cm', '5,5 cm')},
            {'text': 'Das sind ⟦46,75 cm²⟧.'},
            {'text': 'Kleinste Fläche: 7,5 cm · 4,5 cm = 33,75 cm².', 'bild': _re(7.5, 4.5, '7,5 cm', '4,5 cm')},
            {'text': 'Beim Quotienten a : b ist der größte Wert obere(a) : untere(b).'},
        ],
        'fehler': 'Größte Geschwindigkeit als obere Strecke : obere Zeit ist falsch. Durch ⟦weniger⟧ teilen ergibt mehr: obere Strecke : untere Zeit.',
        'regel': 'Größtes Produkt: ⟦obere · obere⟧. Größter Quotient: obere : untere.',
    },
    'entscheiden': {
        'einstieg': 'Ein Aufzug darf 630 kg tragen. 8 Personen wiegen je 78 kg, auf ganze kg gerundet. Dürfen alle mitfahren? '
                    'Bei Sicherheit rechnet man mit dem ⟦ungünstigsten Fall⟧.',
        'woerter': [['ungünstigster Fall', 'alle Werte so gewählt, dass es am knappsten wird']],
        'bild': _zs(620, 632, 12, beschriftet='anfang_ende', punkte=_pk((630, 'Grenze'))),
        'schritte': [
            {'text': 'Jede Person wiegt höchstens 78,5 kg.'},
            {'text': 'Ungünstigster Fall: 8 · 78,5 kg = ⟦628 kg⟧.', 'bild': {'punkte': _pk((630, 'Grenze'), (628, 'höchstens'))}},
            {'text': '628 kg < 630 kg: ⟦sicher erlaubt⟧.', 'bild': {'bereich': {'von': 620, 'bis': 628}}},
        ],
        'fehler': 'Nur 8 · 78 = 624 kg rechnen ist riskant. Der wahre Wert kann bis 628 kg sein. Für Sicherheit zählt die ⟦obere Schranke⟧.',
        'fehler_bild': {'punkte': _pk((630, 'Grenze'), (624, 'gerundet'), (628, 'höchstens')), 'bereich': None},
        'regel': 'Bei Sicherheitsfragen mit dem ⟦ungünstigsten Fall⟧ rechnen. Passt es auch dann, ist es sicher.',
    },
}
UMBAU_OFFEN = ['Umbau (Paket UR): Die Lernkarten zeigen Fehlerbereiche jetzt auf dem Zahlenstrahl mit markiertem Bereich. '
               'Die Aufgaben-Grafiken bleiben unverändert (Strecke im Koordinatensystem).']
UMBAU_WEG = ['Lernkarte „grenzen“: Fehlerbereich als Strecke']
# ---------- Ende UMBAU ----------


d = bauen('zahlen.schranken',
      'Untere und obere Schranken gerundeter Werte bestimmen, Fehlerbereiche angeben und mit Schranken bei Summen, Differenzen, Produkten und Quotienten rechnen.',
      ['Untere Schranke (lower bound) = Wert − halbe Rundungseinheit; obere Schranke (upper bound) = Wert + halbe Einheit.',
       'Fehlerbereich (error interval): untere ≤ x < obere.',
       'Größte Summe: obere + obere. Größte Differenz: obere − untere.',
       'Größtes Produkt: obere · obere. Größter Quotient: obere : untere.',
       'Für Sicherheit mit dem ungünstigsten Fall rechnen.'],
      [('Schranken bestimmen', ['grenzen', 'messen']), ('Mit Schranken rechnen', ['summe', 'produkt']), ('Entscheiden', ['entscheiden'])],
      ETAPPEN, GEN,
      offen=['Ohne Lehrplan-Zuordnung (IB-typischer Stoff „upper and lower bounds“); Niveau Klasse 9/10 angenommen. Nur positive Größen; bei Quotienten Ergebnis auf zwei Nachkommastellen mit Toleranz 0,01.',
             'Lernkarte „grenzen“: Fehlerbereich als Strecke im Koordinatensystem (untere Schranke voller, obere hohler Punkt) – ein Zahlenstrahl mit markiertem Bereich wäre schöner (App-Wunsch).',
             'Feld klasse: {"zusatz": 10} statt {} (Prüfskript verlangt einen Eintrag) – siehe FRAGE im Postfach.'])
umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
