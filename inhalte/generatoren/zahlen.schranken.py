#!/usr/bin/env python3
"""Thema zahlen.schranken – Schranken und Genauigkeit (ohne Lehrplan-Zuordnung, Niveau Klasse 9/10)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403
from _rsib2 import PLAN2, art3  # noqa: E402

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
    art = R.choice({1: ['luecke', 'unten', 'oben'], 2: ['unten', 'oben', 'luecke', 'welcher'], 3: ['welcher', 'rueck', 'nicht', 'rueck']}[s])  # Durchsicht 19
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
    art = R.choice({1: ['unten', 'oben'], 2: ['spanne', 'welcher', 'genauigkeit', 'unten'], 3: ['moeglich', 'genauigkeit', 'moeglich']}[s])  # Durchsicht 19
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
    ein = {Fr(1): 'cm', Fr(1, 10): 'm', Fr(10): 'm'}[sch]  # Durchsicht 19: kg passte nicht zu „Seiten“ und „Strecken“
    a, b = sorted([sch * R.randint(20, 90), sch * R.randint(5, 60)], reverse=True)
    if a == b: return None
    la, ha = grenzen(a, sch)
    lb, hb = grenzen(b, sch)
    wort = {Fr(1): 'auf ganze cm', Fr(1, 10): 'auf 0,1 m', Fr(10): 'auf 10 m'}[sch]
    art = R.choice({1: ['max_sum', 'min_sum'], 2: ['max_diff', 'min_diff', 'umfang', 'drei'], 3: ['max_diff', 'min_diff', 'umfang', 'drei']}[s])  # Durchsicht 19
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
    art = R.choice({1: ['flaeche_max', 'flaeche_min'], 2: ['tempo_max', 'tempo_min', 'quader'], 3: ['tempo_max', 'tempo_min', 'menge', 'quader']}[s])  # Durchsicht 19
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
                f'Ungünstigster Fall: wenig Saft ({dz(lg)} ml), große Gläser ({dz(hgl)} ml). {dz(lg)} : {dz(hgl)} ≈ {dz(round(float(n), 2))} → sicher {sicher} {"volles Glas" if sicher == 1 else "volle Gläser"}.',
                'Rechne mit der kleinsten Saftmenge und dem größten Glas.', sicher, f'{lg} // {hgl}')


def g_entscheiden(s):
    art = R.choice({1: ['aufzug', 'passt'], 2: ['fehler', 'brett'], 3: ['fehler', 'genauigkeit_ergebnis', 'aufzug', 'brett']}[s])  # Durchsicht 19
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
    brett = n * lang + R.choice([0, 2, 3, 4, 5, 6])
    ok = (brett - Fr(1, 2)) >= n * (lang + Fr(1, 2))
    return ja_nein(f'Aus einem {brett} cm langen Brett sollen {n} Stücke von je {lang} cm gesägt werden (alle Maße auf ganze cm gerundet, Sägeschnitte vernachlässigt). Reicht das Brett sicher?', ok,
                   f'Ungünstigster Fall: Brett {dz(brett - Fr(1, 2))} cm, Stücke {n} · {dz(lang + Fr(1, 2))} = {dz(n * (lang + Fr(1, 2)))} cm. ' + ('Reicht sicher.' if ok else 'Reicht nicht sicher.'),
                   'Kürzestes Brett gegen längste Stücke.')


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-2) ----------
# Prüfungsvorbilder: Cambridge IGCSE / IB MYP „upper and lower bounds“ (ganzzahlige Anzahlen, fehlende Seite aus dem Umfang,
# Seite aus Fläche, prozentualer Fehler, „angemessene Genauigkeit“, Geschwindigkeit/Zeit). Eigene Zahlen.
def _filter(g, s, teil, nicht=False):
    for _ in range(150):
        t = g(s)
        if t and ((teil in t['f']['text']) != nicht): return t
    return None


def grenzen3(art):
    if art == 'anzahl':
        sch = R.choice([10, 100, 1000])
        x = sch * R.randint(12, 95)
        g = R.choice(['Besucher', 'Zuschauer', 'Teilnehmer'])
        w = {10: 'Zehner', 100: 'Hunderter', 1000: 'Tausender'}[sch]
        hoch = R.random() < 0.6
        r = x + sch // 2 - 1 if hoch else x - sch // 2
        return zahl(f'Die Zahl der {g} wurde auf {w} gerundet: {dz(x)}. Wie viele {g} waren es {"höchstens" if hoch else "mindestens"}?',
                    (f'Fehlerbereich {dz(x - sch // 2)} ≤ n < {dz(x + sch // 2)}. Anzahlen sind ganze Zahlen, also höchstens {dz(r)}.' if hoch
                     else f'Fehlerbereich {dz(x - sch // 2)} ≤ n < {dz(x + sch // 2)}. Mindestens {dz(r)}.'),
                    'Personen zählt man ganz. Die obere Schranke selbst gehört nicht dazu.', r, f'{r}')
    if art == 'werte':
        st = R.choice([(Fr(1, 10), Fr(1, 100), 'eine Nachkommastelle', 'eine Zahl mit (höchstens) zwei Nachkommastellen'), (Fr(10), Fr(1), 'Zehner', 'eine ganze Zahl'),
                       (Fr(100), Fr(10), 'Hunderter', 'ein Vielfaches von 10'), (Fr(1), Fr(1, 10), 'Ganze', 'eine Zahl mit (höchstens) einer Nachkommastelle')])
        grob, fein, wg, wf_ = st
        x = grob * R.randint(11, 99)
        lo, hi = grenzen(x, grob)
        n = int((hi - lo) / fein)
        return zahl(f'Eine Zahl x ist auf {wg} gerundet: {dz(x)}. Man weiß außerdem: x ist {wf_}. Wie viele Werte kann x haben?',
                    f'Fehlerbereich {dz(lo)} ≤ x < {dz(hi)}. Möglich: {dz(lo)}, {dz(lo + fein)}, …, {dz(hi - fein)}. Das sind {n} Werte.',
                    'Zähle von der unteren Schranke bis knapp unter die obere Schranke.', n, f'{n}')
    # doppelt: erst auf Zehner, dann auf Hunderter
    v = 10 * R.randint(12, 98)
    lo, hi = v - 5, v + 5
    h_lo, h_hi = round_half_up(lo, 100), round_half_up(hi - Fr(1, 100), 100)
    if h_lo == h_hi:
        r = f'Ja, x auf Hunderter gerundet ist sicher {dz(h_lo)}.'
        fs = [f'Nein, es kann auch {dz(h_lo + 100)} sein.', f'Nein, es kann auch {dz(h_lo - 100)} sein.', 'Das lässt sich nie sagen.']
        beg = f'Alle x mit {dz(lo)} ≤ x < {dz(hi)} werden auf {dz(h_lo)} gerundet.'
    else:
        r = f'Nein: Es kann {dz(h_lo)} oder {dz(h_hi)} sein.'
        fs = [f'Ja, x auf Hunderter gerundet ist sicher {dz(h_lo)}.', f'Ja, x auf Hunderter gerundet ist sicher {dz(h_hi)}.', 'Das lässt sich nie sagen.']
        beg = f'{dz(lo)} ≤ x < {dz(hi)}: Werte unter {dz(v)} ergeben {dz(h_lo)}, Werte ab {dz(v)} ergeben {dz(h_hi)}.'
    return auswahl(f'x ist auf Zehner gerundet: {dz(v)}. Weiß man damit, was x auf Hunderter gerundet ist?', r, fs, beg,
                   'Bestimme den Fehlerbereich und runde beide Enden auf Hunderter.')


def round_half_up(x, sch):
    return sch * ((Fr(x) / sch + Fr(1, 2)) // 1)


def messen3(art):
    g, ein, sch, wort, (a, b) = R.choice(MESS[:4] + MESS[5:])
    x = wert_mit(sch, a, b)
    if art == 'prozent':
        p = gerundet(float(sch / 2 / x * 100), 1)
        if p is None or p < 0.1: return None
        return zahl(f'{g}: {dz(x)} {ein}, {wort}. Wie viel Prozent des Messwerts beträgt der größte mögliche Fehler? (auf eine Nachkommastelle)',
                    f'Größter Fehler: {dz(sch / 2)} {ein}. {dz(sch / 2)} : {dz(x)} · 100 % ≈ {dz(p)} %.', 'Größter Fehler = halbe Messgenauigkeit. Dann durch den Messwert teilen.',
                    p, f'round({float(sch)} / 2 / {float(x)} * 100, 1)', einheit='%', tol=0.1)
    # genauer: welche Messung ist relativ genauer?
    (g1, e1, s1, w1, b1), (g2, e2, s2, w2, b2) = R.sample(MESS[:4] + MESS[5:], 2)
    x1, x2 = wert_mit(s1, *b1), wert_mit(s2, *b2)
    r1, r2 = s1 / 2 / x1, s2 / 2 / x2
    if abs(r1 - r2) < Fr(1, 2000): return None
    r = f'{g1}' if r1 < r2 else f'{g2}'
    return auswahl(f'Messung A: {g1} {dz(x1)} {e1}, {w1}. Messung B: {g2} {dz(x2)} {e2}, {w2}. Bei welcher Messung ist der größte Fehler im Verhältnis zum Messwert kleiner?',
                   'Messung A' if r1 < r2 else 'Messung B', ['Messung B' if r1 < r2 else 'Messung A', 'Beide gleich'],
                   f'A: {dz(s1 / 2)} : {dz(x1)} ≈ {dz(round(float(r1) * 100, 2))} %. B: {dz(s2 / 2)} : {dz(x2)} ≈ {dz(round(float(r2) * 100, 2))} %. Kleiner ist es bei {r}.',
                   'Vergleiche den größten Fehler geteilt durch den Messwert, nicht die Fehler allein.')


def summe3(art):
    if art == 'rest':
        L, n, st = R.randint(15, 40), R.randint(2, 5), Fr(R.randint(25, 60), 10)
        if n * st >= L - 2: return None
        mi = L - Fr(1, 2) - n * (st + Fr(1, 20))
        return zahl(f'Ein Seil ist {L} m lang (auf ganze m gerundet). Davon werden {n} Stücke zu je {dz(st)} m abgeschnitten (auf 0,1 m gerundet). Wie lang ist der Rest mindestens?',
                    f'Kürzestes Seil: {dz(L - Fr(1, 2))} m. Längste Stücke: {n} · {dz(st + Fr(1, 20))} m = {dz(n * (st + Fr(1, 20)))} m. Rest ≥ {dz(mi)} m.',
                    'Für den kleinsten Rest: wenig Seil, große Stücke.', mi, f'{L} - 0.5 - {n} * {float(st + Fr(1, 20))}', einheit='m')
    if art == 'fehlend':
        s1, s2 = R.randint(6, 15), R.randint(6, 15)
        u = s1 + s2 + R.randint(max(abs(s1 - s2) + 2, 4), s1 + s2 - 2)
        hoch = R.random() < 0.5
        v = (u + Fr(1, 2)) - (s1 - Fr(1, 2)) - (s2 - Fr(1, 2)) if hoch else (u - Fr(1, 2)) - (s1 + Fr(1, 2)) - (s2 + Fr(1, 2))
        return zahl(f'Ein Dreieck hat den Umfang {u} cm. Zwei Seiten sind {s1} cm und {s2} cm lang (alles auf ganze cm gerundet). Wie lang ist die dritte Seite {"höchstens" if hoch else "mindestens"}?',
                    (f'Großer Umfang, kurze Seiten: {dz(u + Fr(1, 2))} − {dz(s1 - Fr(1, 2))} − {dz(s2 - Fr(1, 2))} = {dz(v)} cm.' if hoch
                     else f'Kleiner Umfang, lange Seiten: {dz(u - Fr(1, 2))} − {dz(s1 + Fr(1, 2))} − {dz(s2 + Fr(1, 2))} = {dz(v)} cm.'),
                    'Dritte Seite = Umfang − Seite 1 − Seite 2. Was macht die Differenz am größten (kleinsten)?', v,
                    f'{u} + 0.5 - {s1 - 0.5} - {s2 - 0.5}' if hoch else f'{u} - 0.5 - {s1 + 0.5} - {s2 + 0.5}', einheit='cm')
    # breite: Breite des Fehlerbereichs einer Summe
    (s1, w1, e1), (s2, w2, e2) = R.choice([((Fr(1), 'auf ganze cm', 'cm'), (Fr(1), 'auf ganze cm', 'cm')), ((Fr(1), 'auf ganze cm', 'cm'), (Fr(1, 10), 'auf mm', 'cm')),
                                            ((Fr(10), 'auf 10 m', 'm'), (Fr(1), 'auf ganze m', 'm')), ((Fr(1, 10), 'auf 0,1 kg', 'kg'), (Fr(1, 10), 'auf 0,1 kg', 'kg'))])
    a, b = wert_mit(s1, 20, 90), wert_mit(s2, 5, 40)
    br = s1 + s2
    return zahl(f'a = {dz(a)} {e1} ({w1} gerundet) und b = {dz(b)} {e2} ({w2} gerundet). Wie breit ist der Fehlerbereich von a + b (obere minus untere Schranke)?',
                f'Breite bei a: {dz(s1)}, bei b: {dz(s2)}. Bei der Summe addieren sich die Breiten: {dz(br)} {e1}.',
                'Rechne beide Schranken von a + b aus oder überlege, wie sich die Breiten verhalten.', br, f'{float(s1)} + {float(s2)}', einheit=e1)


def produkt3(art):
    if art == 'seite':
        A, l = R.randint(30, 90), R.randint(5, 12)
        hoch = R.random() < 0.5
        v = (A + Fr(1, 2)) / (l - Fr(1, 2)) if hoch else (A - Fr(1, 2)) / (l + Fr(1, 2))
        g = gerundet(float(v), 2)
        if g is None: return None
        return zahl(f'Ein Rechteck hat die Fläche {A} cm² (auf ganze cm² gerundet) und die Länge {l} cm (auf ganze cm gerundet). Wie breit ist es {"höchstens" if hoch else "mindestens"}? (auf zwei Nachkommastellen)',
                    (f'Breite = Fläche : Länge. Größte Fläche durch kleinste Länge: {dz(A + Fr(1, 2))} : {dz(l - Fr(1, 2))} ≈ {dz(g)} cm.' if hoch
                     else f'Breite = Fläche : Länge. Kleinste Fläche durch größte Länge: {dz(A - Fr(1, 2))} : {dz(l + Fr(1, 2))} ≈ {dz(g)} cm.'),
                    'Breite = Fläche : Länge. Beim Teilen: Für das Maximum durch die kleinste Zahl teilen.', g,
                    f'round({A + 0.5} / {l - 0.5}, 2)' if hoch else f'round({A - 0.5} / {l + 0.5}, 2)', einheit='cm', tol=0.01)
    # unterschied: Zwei Rechtecke, größter Flächenunterschied
    a1, b1, a2, b2 = R.randint(8, 15), R.randint(6, 12), R.randint(4, 9), R.randint(3, 8)
    if a1 * b1 <= a2 * b2 + 10: return None
    v = (a1 + Fr(1, 2)) * (b1 + Fr(1, 2)) - (a2 - Fr(1, 2)) * (b2 - Fr(1, 2))
    return zahl(f'Beet A ist {a1} m × {b1} m groß, Beet B {a2} m × {b2} m (alle Maße auf ganze m gerundet). Um wie viel m² kann A höchstens größer sein als B?',
                f'A möglichst groß: {dz(a1 + Fr(1, 2))} · {dz(b1 + Fr(1, 2))} = {dz((a1 + Fr(1, 2)) * (b1 + Fr(1, 2)))}. B möglichst klein: {dz(a2 - Fr(1, 2))} · {dz(b2 - Fr(1, 2))} = {dz((a2 - Fr(1, 2)) * (b2 - Fr(1, 2)))}. Unterschied: {dz(v)} m².',
                'Erst überlegen: Welche Fläche soll groß, welche klein sein? Dann die passenden Schranken wählen.', v,
                f'{a1 + 0.5} * {b1 + 0.5} - {a2 - 0.5} * {b2 - 0.5}', einheit='m²')


def entscheiden3(art):
    if art == 'zeit':
        d, v = 10 * R.randint(8, 30), 5 * R.randint(12, 24)
        tmax = Fr(d + 5) / Fr(v - Fr(5, 2))
        tmin = Fr(d - 5) / Fr(v + Fr(5, 2))
        t = Fr(round(float(tmax + tmin) * 2) + R.choice([-1, 0, 0, 1]), 4)
        if t <= 0: return None
        if tmin < t < tmax: z = 'Das lässt sich nicht sicher sagen.'
        elif tmax <= t: z = 'Ja, sicher.'
        else: z = 'Nein, sicher nicht.'

        return auswahl(f'Ein Zug fährt {d} km (auf 10 km gerundet) mit {v} km/h (auf 5 km/h gerundet). Schafft er die Strecke in {dz(t)} {"Stunde" if t == 1 else "Stunden"}?', z,
                       [x for x in ['Ja, sicher.', 'Nein, sicher nicht.', 'Das lässt sich nicht sicher sagen.'] if x != z],
                       f'Zeit = Strecke : Geschwindigkeit. Höchstens {dz(d + 5)} : {dz(v - Fr(5, 2))} ≈ {dz(round(float(tmax), 2))} h, mindestens {dz(d - 5)} : {dz(v + Fr(5, 2))} ≈ {dz(round(float(tmin), 2))} h.',
                       'Berechne die kürzeste und die längste mögliche Fahrzeit.')
    # angemessen: Ergebnis sinnvoll runden
    for _ in range(80):
        a, b = Fr(R.randint(21, 99), 10), Fr(R.randint(21, 99), 10)
        lo, hi = (a - Fr(1, 20)) * (b - Fr(1, 20)), (a + Fr(1, 20)) * (b + Fr(1, 20))
        for st, txt in [(Fr(1, 10), 'eine Nachkommastelle'), (Fr(1), 'Ganze'), (Fr(10), 'Zehner')]:
            if round_half_up(lo, st) == round_half_up(hi - Fr(1, 10 ** 6), st): break
        else:
            continue
        if st != Fr(1, 10): break
    else:
        return None
    r = dz(round_half_up(lo, st))
    fs = [dz(a * b), dz(round_half_up(a * b, Fr(1, 10))), dz(round_half_up(lo, st) + st)]
    if len({r, *fs}) < 4: return None
    return auswahl(f'Ein Rechteck ist {dz(a)} cm × {dz(b)} cm groß (auf 0,1 cm gerundet). Welche Angabe der Fläche ist sicher richtig, ohne mehr Genauigkeit vorzutäuschen?', f'{r} cm²',
                   [f'{x} cm²' for x in fs],
                   f'Untere Schranke {dz(lo)}, obere {dz(hi)}. Beide ergeben auf {txt} gerundet {r}. Genauer geht es nicht sicher.',
                   'Berechne beide Schranken. Auf welche Stelle gerundet stimmen sie überein?')


def g2_grenzen(s):
    if s == 1: return g_grenzen(1)
    if s == 2: return g_grenzen(2) if (AKT['nr'] % 3 if AKT['pool'] == 'uebung' else R.random() < 0.6) else _filter(g_grenzen, 3, 'Auf welchen Wert')
    art = art3('nicht', 'anzahl', 'doppelt', ['nicht', 'anzahl', 'doppelt', 'werte', 'anzahl'])
    if art == 'nicht': return _filter(g_grenzen, 3, 'NICHT')
    return grenzen3(art)


def g2_messen(s):
    if s < 3: return g_messen(s)
    art = art3('moeglich', 'prozent', 'genauer', ['moeglich', 'prozent', 'genauer', 'genauigkeit', 'prozent'])
    if art == 'moeglich': return _filter(g_messen, 3, 'Kann der wahre Wert')
    if art == 'genauigkeit': return _filter(g_messen, 3, 'Wie genau')
    return messen3(art)


def g2_summe(s):
    if s < 3: return g_summe(s)
    art = art3('rest', 'fehlend', 'breite', ['rest', 'fehlend', 'breite', 'fehlend', 'rest'])
    return summe3(art)


def g2_produkt(s):
    if s < 3: return g_produkt(s)
    art = art3('menge', 'seite', 'unterschied', ['menge', 'seite', 'unterschied', 'seite', 'unterschied'])
    if art == 'menge': return _filter(g_produkt, 3, 'Gläser')
    return produkt3(art)


def g2_entscheiden(s):
    if s < 3: return g_entscheiden(s)
    art = art3('genauigkeit_ergebnis', 'zeit', 'angemessen', ['genauigkeit_ergebnis', 'zeit', 'angemessen', 'zeit', 'genauigkeit_ergebnis'])
    if art == 'genauigkeit_ergebnis': return _filter(g_entscheiden, 3, 'sicher sagen')
    return entscheiden3(art)


GEN = {'grenzen': g2_grenzen, 'messen': g2_messen, 'summe': g2_summe, 'produkt': g2_produkt, 'entscheiden': g2_entscheiden}

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
            {'text': 'Bei Anzahlen wie Personen ist die größte Zahl ⟦eins weniger⟧ als die obere Schranke.'},
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
            {'text': 'Fehler im Verhältnis: 0,05 : 4,3 ≈ ⟦1,2 %⟧ des Messwerts.'},
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
            {'text': 'Ein Ergebnis rundet man nur so weit, wie ⟦beide Schranken⟧ gleich gerundet werden.'},
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
             'Feld klasse: {"zusatz": 10} statt {} (Prüfskript verlangt einen Eintrag) – siehe FRAGE im Postfach.'], plan=PLAN2)
umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)
