#!/usr/bin/env python3
"""Thema gleichungen.ungleichungen – Lineare Ungleichungen (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, M, Z, baue, ca, cz, eur, kl, lin, zt  # noqa: E402

META = {'thema_schluessel': 'gleichungen.ungleichungen', 'thema_id': 3, 'block_id': 61, 'klasse': {'gym_by': 8, 'rs_by': 7}}

UMKEHR = {'<': '>', '>': '<', '≤': '≥', '≥': '≤'}
ZEICHEN = ['<', '>', '≤', '≥']

ETAPPEN = [
    {'lernziel': 'umformen', 'titel': 'Ungleichungen umformen',
     'regel': 'Eine Ungleichung löst du wie eine Gleichung: Auf beiden Seiten ⟦dasselbe addieren, subtrahieren⟧ oder mit einer ⟦positiven⟧ Zahl multiplizieren bzw. durch sie dividieren. Das Zeichen bleibt dabei gleich.',
     'schritte': ['3x + 5 < 17   | − 5', '3x < 12   | : 3', '⟦x < 4⟧: Alle Zahlen kleiner als 4 sind Lösungen.'],
     'probe': 'x = 0: 3 · 0 + 5 = 5 < 17 ✓  x = 4: 17 < 17 ✗ – 4 gehört nicht dazu.',
     'fehler': 'Aus 3x + 5 < 17 wird nicht 3x < 22: Die 5 wird ⟦subtrahiert⟧, nicht addiert. Richtig ist 3x < 12.',
     'bild': {'typ': 'zahlenstrahl', 'start': -2, 'ende': 8, 'abschnitte': 10, 'beschriftet': 'anfang_ende'},
     '_verbot': ['3x + 5 < 17']},
    {'lernziel': 'umdrehen', 'titel': 'Mal negative Zahl: Zeichen umdrehen',
     'regel': 'Multiplizierst oder dividierst du beide Seiten mit einer ⟦negativen⟧ Zahl, musst du das Ungleichheitszeichen ⟦umdrehen⟧: aus < wird >, aus ≤ wird ≥.',
     'schritte': ['−2x + 1 ≤ 9   | − 1', '−2x ≤ 8   | : (−2), Zeichen umdrehen', '⟦x ≥ −4⟧'],
     'probe': 'x = 0: −2 · 0 + 1 = 1 ≤ 9 ✓ – und 0 ≥ −4 passt.',
     'fehler': '−2x ≤ 8 ergibt nicht x ≤ −4. Prüfe mit x = −5: −2 · (−5) = 10 ≤ 8 ist falsch. Beim Teilen durch (−2) wird das Zeichen ⟦umgedreht⟧: x ≥ −4.',
     '_verbot': ['−2x + 1 ≤ 9']},
    {'lernziel': 'klammern', 'titel': 'Klammern und x auf beiden Seiten',
     'regel': 'Erst ⟦Klammern auflösen⟧ und zusammenfassen, dann alle x-Glieder auf ⟦eine Seite⟧ bringen. Hat x am Ende einen negativen Faktor, Zeichen beim Teilen umdrehen.',
     'schritte': ['2(x + 3) > 5x − 9', '2x + 6 > 5x − 9   | − 5x − 6', '−3x > −15   | : (−3), Zeichen umdrehen', '⟦x < 5⟧'],
     'probe': 'x = 0: 2 · 3 = 6 > −9 ✓',
     'fehler': '2(x + 3) ist nicht 2x + 3: Die 2 wird mit ⟦jedem⟧ Summanden in der Klammer multipliziert, also 2x + 6.',
     '_verbot': ['2(x + 3) > 5x − 9']},
    {'lernziel': 'intervall', 'titel': 'Lösungsmenge als Intervall angeben',
     'regel': 'Die Lösungsmenge schreibst du als Intervall. Eckige Klammer ⟦nach innen⟧: Grenze gehört dazu (≤, ≥). Klammer ⟦nach außen⟧: Grenze gehört nicht dazu (<, >). Bei ∞ steht immer eine Klammer nach außen.',
     'schritte': ['x ≤ 3 → L = ⟦]−∞; 3]⟧', 'x > −2 → L = ⟦]−2; ∞[⟧'],
     'fehler': 'x < 3 ist nicht ]−∞; 3]: Die 3 erfüllt x < 3 nicht, also muss die Klammer ⟦nach außen⟧ zeigen: ]−∞; 3[.'},
    {'lernziel': 'pruefen', 'titel': 'Lösungen prüfen und Fehler finden',
     'regel': 'Ob eine Zahl eine Lösung ist, prüfst du durch ⟦Einsetzen⟧. Bei einer Rechnung prüfst du jeden Schritt, besonders das ⟦Umdrehen des Zeichens⟧.',
     'schritte': ['Ist 6 eine Lösung von 2x − 3 > 7?', '2 · 6 − 3 = 9 und 9 > 7 ist wahr, also ⟦ja⟧.'],
     'fehler': 'Nur eine Zahl zu testen reicht nicht, um eine ganze Lösungsmenge zu bestätigen. Teste auch eine Zahl ⟦nahe der Grenze⟧ auf der anderen Seite.',
     '_verbot': ['2x − 3 > 7']},
    {'lernziel': 'sachaufgabe', 'titel': 'Sachaufgaben mit Ungleichungen',
     'regel': 'Wörter wie ⟦höchstens⟧ (≤), ⟦mindestens⟧ (≥), ⟦mehr als⟧ (>) oder ⟦weniger als⟧ (<) führen zu einer Ungleichung. Bei Stückzahlen ist nur eine ⟦ganze Zahl⟧ als Antwort sinnvoll.',
     'schritte': ['Eintritt 4 €, jede Fahrt 2,50 €, höchstens 20 € ausgeben.', '4 + 2,5x ≤ 20  →  2,5x ≤ 16  →  x ≤ 6,4', 'Man kann ⟦höchstens 6⟧ Fahrten machen.'],
     'fehler': 'Aus x ≤ 6,4 folgt nicht „7 Fahrten“ durch Aufrunden: 7 Fahrten kosten 4 + 17,50 = 21,50 €, das ist zu viel. Bei „höchstens“ wird ⟦abgerundet⟧.'},
]


def loese(p, q, z, r, s):
    """p·x + q  z  r·x + s  ->  (Zeichen, Grenze)."""
    k = p - r
    g = Fr(s - q, k)
    return (z if k > 0 else UMKEHR[z]), g


def falsch_loesungen(z, g):
    return [f'x {UMKEHR[z]} {zt(g)}', f'x {z} {zt(-g)}' if g != 0 else f'x {z} 1', f'x {UMKEHR[z]} {zt(-g)}' if g != 0 else f'x {UMKEHR[z]} 1',
            f'x {z.replace("≤", "<").replace("≥", ">") if z in "≤≥" else {"<": "≤", ">": "≥"}[z]} {zt(g)}']


def text_ug(p, q, z, r, s):
    return f'{lin(p, q)} {z} {lin(r, s)}'


def g_umformen(R, st):
    z = R.choice(ZEICHEN)
    if st == 1:
        a, g = R.randint(2, 9), R.randint(-6, 9)
        if R.random() < .5:
            b = R.randint(1, 15) * R.choice([-1, 1])
            lhs, c = f'x {"+" if b > 0 else "−"} {abs(b)}', g + b
            weg = f'{"−" if b > 0 else "+"} {abs(b)} auf beiden Seiten: x {z} {zt(g)}'
        else:
            lhs, c = f'{a}x', a * g
            weg = f': {a} auf beiden Seiten: x {z} {zt(g)}'
        if R.random() < .35 and -10 <= g <= 10:
            return M(f'Löse {lhs} {z} {zt(c)}. Markiere die Grenze der Lösungsmenge am Zahlenstrahl.', -10, 10, 20, g + 10,
                     f'{weg}. Die Grenze ist {zt(g)}.', 'Rechne zuerst die Grenze aus, dann suche sie auf dem Zahlenstrahl.')
        return A(R, f'Löse die Ungleichung {lhs} {z} {zt(c)}.', f'x {z} {zt(g)}', falsch_loesungen(z, g), weg + '.',
                 'Forme wie bei einer Gleichung um. Das Zeichen bleibt gleich.')
    if st == 2:
        a, g, b = R.randint(2, 9), R.randint(-8, 10), R.randint(1, 20) * R.choice([-1, 1])
        c = a * g + b
        txt = f'{lin(a, b)} {z} {zt(c)}'
        weg = f'{lin(a, b)} {z} {zt(c)} | {"−" if b > 0 else "+"} {abs(b)} → {a}x {z} {zt(a * g)} | : {a} → x {z} {zt(g)}'
        if R.random() < .5:
            return Z(f'Löse {txt}. Die Lösung hat die Form x {z} □. Gib die Zahl an.', g, f'({c} - ({b})) / {a}', weg + '.',
                     'Erst den Summanden ohne x wegbringen, dann durch die Zahl vor x teilen.')
        return A(R, f'Löse die Ungleichung {txt}.', f'x {z} {zt(g)}', falsch_loesungen(z, g) + [f'x {z} {zt(Fr(c + b, a))}'], weg + '.',
                 'Erst den Summanden ohne x wegbringen, dann durch die Zahl vor x teilen.')
    # Stufe 3: x auf beiden Seiten, Koeffizient bleibt positiv; Grenze darf Dezimalzahl sein
    while True:
        r = R.randint(1, 6); p = r + R.randint(1, 5)
        g = Fr(R.randint(-20, 30), R.choice([1, 2, 4, 5])) if R.random() < .4 else Fr(R.randint(-9, 9))
        q = R.randint(-15, 15)
        s = (p - r) * g + q
        if s.denominator == 1 and q != 0: break
    txt = text_ug(p, q, z, r, s)
    weg = f'| − {lin(r, 0)} → {lin(p - r, q)} {z} {zt(s)} | {"−" if q > 0 else "+"} {abs(q)} → {lin(p - r, 0)} {z} {zt(s - q)} | : {p - r} → x {z} {zt(g)}'
    if g.denominator in (1, 2, 4, 5) and R.random() < .5:
        return Z(f'Löse {txt}. Die Lösung hat die Form x {z} □. Gib die Zahl an.', g, f'({cz(s)} - ({q})) / ({p} - {r})', weg + '.',
                 'Bringe alle x-Glieder auf die linke Seite, alle Zahlen auf die rechte.')
    return A(R, f'Löse die Ungleichung {txt}.', f'x {z} {zt(g)}', falsch_loesungen(z, g) + [f'x {z} {zt(Fr(s + q, p - r))}'], weg + '.',
             'Bringe alle x-Glieder auf die linke Seite, alle Zahlen auf die rechte.')


def g_umdrehen(R, st):
    z = R.choice(ZEICHEN)
    while True:
        if st == 1:
            a, g = -R.randint(2, 9), Fr(R.randint(-9, 9)); q = 0; p, r = a, 0
        elif st == 2:
            a, g, q = -R.randint(2, 9), Fr(R.randint(-9, 9)), R.randint(-15, 15); p, r = a, 0
        else:
            p = R.randint(1, 6); r = p + R.randint(1, 5); g = Fr(R.randint(-9, 12)); q = R.randint(-15, 15)
        s = (p - r) * g + q
        if g != 0 and (st == 1 or q != 0): break
    z2, g2 = loese(p, q, z, r, s)
    assert g2 == g and z2 == UMKEHR[z]
    txt = text_ug(p, q, z, r, s)
    k = p - r
    if st == 3:
        weg = f'| − {r}x → {lin(k, q)} {z} {zt(s)} | {"−" if q > 0 else "+"} {abs(q)} → {lin(k, 0)} {z} {zt(s - q)} | : {kl(k)}, Zeichen umdrehen → x {z2} {zt(g)}'
        h = 'Alle x nach links bringen. Ist der Faktor vor x negativ, beim Teilen das Zeichen umdrehen.'
    elif q:
        weg = f'| {"−" if q > 0 else "+"} {abs(q)} → {lin(k, 0)} {z} {zt(s - q)} | : {kl(k)}, Zeichen umdrehen → x {z2} {zt(g)}'
        h = 'Teilst du durch eine negative Zahl, drehst du das Zeichen um.'
    else:
        weg = f': {kl(k)} auf beiden Seiten, Zeichen umdrehen → x {z2} {zt(g)}'
        h = 'Teilst du durch eine negative Zahl, drehst du das Zeichen um.'
    richtig = f'x {z2} {zt(g)}'
    falsch = [f'x {z} {zt(g)}', f'x {z2} {zt(-g)}', f'x {z} {zt(-g)}']
    if st >= 2 and R.random() < .4:
        return Z(f'Löse {txt}. Die Lösung hat die Form x {z2} □. Gib die Zahl an.', g, f'({cz(s)} - ({q})) / ({p} - ({r}))', weg + '.', h)
    return A(R, f'Löse die Ungleichung {txt}.', richtig, falsch, weg + '.', h)


def g_klammern(R, st):
    z = R.choice(ZEICHEN)
    while True:
        a, b = R.choice([2, 3, 4, 5, -2, -3]), R.randint(-6, 6)
        if st == 1:
            g = Fr(R.randint(-8, 8)); r, s0 = 0, None
            p, q = a, a * b
            s = p * g + q
            txt = f'{a if a > 0 else "−" + str(-a)}(x {"+" if b >= 0 else "−"} {abs(b)}) {z} {zt(s)}'
        elif st == 2:
            g = Fr(R.randint(-8, 8)); r = R.randint(-4, 6)
            p, q = a, a * b
            if p == r: continue
            d = R.randint(-10, 10)
            s = (p - r) * g + q   # rechte Seite r·x + s
            txt = f'{a if a > 0 else "−" + str(-a)}(x {"+" if b >= 0 else "−"} {abs(b)}) {z} {lin(r, s)}'
        else:
            c, d = R.randint(2, 5), R.randint(-5, 5)
            g = Fr(R.randint(-8, 8)); r = R.randint(-3, 3)
            p, q = a - c, a * b + c * d          # a(x+b) − c(x−d) = (a−c)x + ab + cd
            if p == r: continue
            s = (p - r) * g + q
            txt = (f'{a if a > 0 else "−" + str(-a)}(x {"+" if b >= 0 else "−"} {abs(b)}) − {c}(x {"−" if d >= 0 else "+"} {abs(d)}) {z} {lin(r, s)}')
        if b != 0 and s.denominator == 1: break
    z2, g2 = loese(p, q, z, r, s)
    assert g2 == g
    k = p - r
    weg = (f'Klammern auflösen: {lin(p, q)} {z} {lin(r, s)}. ' + ((f'− {lin(r, 0)}: ' if r > 0 else f'+ {lin(-r, 0)}: ') + f'{lin(k, q)} {z} {zt(s)}. ' if r else '') +
           f'{"−" if q > 0 else "+"} {abs(q)}: {lin(k, 0)} {z} {zt(s - q)}. : {kl(k)}' +
           (', Zeichen umdrehen' if k < 0 else '') + f' → x {z2} {zt(g)}.')
    h = 'Löse zuerst die Klammern auf. Achte am Ende auf das Vorzeichen vor x.'
    if st >= 2 and R.random() < .4:
        return Z(f'Löse {txt}. Die Lösung hat die Form x {z2} □. Gib die Zahl an.', g, f'({cz(s)} - ({q})) / (({p}) - ({r}))', weg, h)
    return A(R, f'Löse die Ungleichung {txt}.', f'x {z2} {zt(g)}', [f'x {UMKEHR[z2]} {zt(g)}', f'x {z2} {zt(-g)}' if g else f'x {z2} 1',
             f'x {z2} {zt(Fr(s + q, k))}', f'x {UMKEHR[z2]} {zt(-g)}' if g else f'x {UMKEHR[z2]} 1'], weg, h)


def intervall(z, g):
    G = zt(g)
    return {'<': f']−∞; {G}[', '≤': f']−∞; {G}]', '>': f']{G}; ∞[', '≥': f'[{G}; ∞['}[z]


def g_intervall(R, st):
    if st == 1:
        z, g = R.choice(ZEICHEN), Fr(R.randint(-9, 9))
        r = intervall(z, g)
        andere = [intervall(x, g) for x in ZEICHEN if x != z]
        return A(R, f'Schreibe die Lösungsmenge von x {z} {zt(g)} als Intervall.', f'L = {r}', [f'L = {x}' for x in andere],
                 f'{"Die Grenze gehört dazu" if z in "≤≥" else "Die Grenze gehört nicht dazu"}, und x ist {"kleiner" if z in "<≤" else "größer"} als {zt(g)}: L = {r}.',
                 'Zeigt das Zeichen nach links (<, ≤), reicht das Intervall bis −∞. Gehört die Grenze dazu?')
    if st == 2:
        z = R.choice(ZEICHEN)
        while True:
            a, g, b = R.choice([2, 3, 4, 5, -2, -3, -4]), Fr(R.randint(-8, 8)), R.randint(-12, 12)
            if b: break
        c = a * g + b
        z2, _ = loese(a, b, z, 0, c)
        r = intervall(z2, g)
        return A(R, f'Löse {lin(a, b)} {z} {zt(c)} und gib die Lösungsmenge als Intervall an.', f'L = {r}',
                 [f'L = {intervall(x, g)}' for x in ZEICHEN if x != z2] + [f'L = {intervall(z2, -g)}'],
                 f'{lin(a, b)} {z} {zt(c)} → {lin(a, 0)} {z} {zt(c - b)} → x {z2} {zt(g)}' + (' (Zeichen umgedreht, da durch eine negative Zahl geteilt)' if a < 0 else '') + f'. L = {r}.',
                 'Erst lösen, dann das Intervall aufschreiben. Achte auf negative Faktoren vor x.')
    # Doppelungleichung
    while True:
        a, b = R.choice([2, 3, 4, 5]), R.randint(-9, 9)
        u, o = sorted(R.sample(range(-8, 9), 2))
        if b: break
    z1, z2 = R.choice(['<', '≤']), R.choice(['<', '≤'])
    lo, hi = a * u + b, a * o + b
    r = ('[' if z1 == '≤' else ']') + f'{zt(u)}; {zt(o)}' + (']' if z2 == '≤' else '[')
    falsch = [('[' if z1 == '<' else ']') + f'{zt(u)}; {zt(o)}' + (']' if z2 == '<' else '['),
              ('[' if z1 == '≤' else ']') + f'{zt(lo)}; {zt(hi)}' + (']' if z2 == '≤' else '['),
              ('[' if z1 == '≤' else ']') + f'{zt(Fr(lo + b, a))}; {zt(Fr(hi + b, a))}' + (']' if z2 == '≤' else '[')]
    return A(R, f'Löse {zt(lo)} {z1} {lin(a, b)} {z2} {zt(hi)} und gib die Lösungsmenge als Intervall an.', f'L = {r}', [f'L = {x}' for x in falsch],
             f'Auf allen drei Teilen {"−" if b > 0 else "+"} {abs(b)}: {zt(lo - b)} {z1} {a}x {z2} {zt(hi - b)}. Durch {a}: {zt(u)} {z1} x {z2} {zt(o)}. L = {r}.',
             'Rechne auf allen drei Teilen gleichzeitig. Dann gibt es eine linke und eine rechte Grenze.')


def g_pruefen(R, st):
    z = R.choice(ZEICHEN)
    if st == 1:
        while True:
            a, b, g = R.randint(2, 6), R.randint(-10, 10), R.randint(-6, 6)
            if b: break
        c = a * g + b
        txt = f'{lin(a, b)} {z} {zt(c)}'
        ok = {'<': lambda x: x < g, '≤': lambda x: x <= g, '>': lambda x: x > g, '≥': lambda x: x >= g}[z]
        kand = [g - 3, g - 1, g, g + 1, g + 3]
        rich = [x for x in kand if ok(x)]; fal = [x for x in kand if not ok(x)]
        if len(rich) >= len(fal) and len(fal) >= 1:
            # Frage nach der Zahl, die KEINE Lösung ist
            x0 = R.choice(fal)
            return A(R, f'Welche Zahl ist KEINE Lösung von {txt}?', zt(x0), [zt(x) for x in R.sample(rich, min(3, len(rich)))],
                     f'Einsetzen: {a} · {kl(x0)} {"+" if b > 0 else "−"} {abs(b)} = {zt(a * x0 + b)}, und {zt(a * x0 + b)} {z} {zt(c)} ist falsch. Lösung ist x {z} {zt(g)}.',
                     'Setze jede Zahl ein oder löse die Ungleichung zuerst.')
        x0 = R.choice(rich)
        return A(R, f'Welche Zahl ist eine Lösung von {txt}?', zt(x0), [zt(x) for x in R.sample(fal, min(3, len(fal)))],
                 f'Einsetzen: {a} · {kl(x0)} {"+" if b > 0 else "−"} {abs(b)} = {zt(a * x0 + b)}, und {zt(a * x0 + b)} {z} {zt(c)} ist wahr. Lösung ist x {z} {zt(g)}.',
                 'Setze jede Zahl ein oder löse die Ungleichung zuerst.')
    if st == 2:
        # größte/kleinste ganze Zahl, die die Ungleichung erfüllt
        while True:
            a, b = R.choice([2, 3, 4, 5, -2, -3, -4]), R.randint(-12, 12)
            c = R.randint(-20, 20)
            if b and (c - b) % a != 0: break
        g = Fr(c - b, a)
        z2 = z if a > 0 else UMKEHR[z]
        # Grenze ist nicht ganzzahlig: abrunden bzw. aufrunden
        if z2 in '<≤':
            frage, wert = 'größte', g.numerator // g.denominator
        else:
            frage, wert = 'kleinste', -((-g.numerator) // g.denominator)
        p, qn = g.numerator, g.denominator
        c_ausdr = f'{p} // {qn}' if frage == 'größte' else f'-((-{p}) // {qn})'
        return Z(f'Gib die {frage} ganze Zahl an, die {lin(a, b)} {z} {zt(c)} erfüllt.', wert, c_ausdr,
                 f'Lösen: x {z2} {zt(g)}' + (' (Zeichen umgedreht)' if a < 0 else '') + f'. Die {frage} ganze Zahl ist {zt(wert)}.',
                 'Löse zuerst die Ungleichung. Liegt die Grenze zwischen zwei ganzen Zahlen, überlege, welche noch passt.')
    # Stufe 3: Fehler in einer Rechnung finden
    while True:
        a, g, b = -R.randint(2, 6), R.randint(-6, 6), R.randint(1, 12) * R.choice([-1, 1])
        if g: break
    c = a * g + b
    art = R.choice(['umdrehen', 'subtraktion', 'richtig', 'teilen'])
    s1 = c - b
    if art == 'subtraktion': s1 = c + b
    gg = Fr(s1, a)
    zf = z if art == 'umdrehen' else UMKEHR[z]
    if art == 'teilen': gg = -gg
    text = (f'Jemand löst {lin(a, b)} {z} {zt(c)} so: {"−" if b > 0 else "+"} {abs(b)} ergibt {lin(a, 0)} {z} {zt(s1)}; '
            f'durch {kl(a)} ergibt x {zf} {zt(gg)}. Was stimmt?')
    opts = {'umdrehen': 'Beim Teilen durch die negative Zahl wurde das Zeichen nicht umgedreht.',
            'subtraktion': f'Im ersten Schritt wurde falsch gerechnet: richtig ist {lin(a, 0)} {z} {zt(c - b)}.',
            'teilen': 'Beim Teilen wurde das Vorzeichen des Ergebnisses falsch bestimmt.',
            'richtig': 'Die Rechnung ist richtig.'}
    richtig = opts[art]
    loes = f'Richtig: {lin(a, 0)} {z} {zt(c - b)}, durch {kl(a)} mit Umdrehen: x {UMKEHR[z]} {zt(g)}.'
    return A(R, text, richtig, [v for k, v in opts.items() if k != art], loes,
             'Rechne jeden Schritt selbst nach und vergleiche.')


def g_sachaufgabe(R, st):
    art = R.choice({1: ['aufzug', 'tarif', 'regal'], 2: ['tarif', 'taxi', 'sparen', 'aufzug'], 3: ['kino', 'sparen', 'vergleich']}[st])
    if art == 'aufzug':
        L, p, k = R.choice([450, 500, 630, 800, 1000]), R.randint(65, 95), R.choice([12, 15, 18, 20, 25, 30, 35])
        n = (L - p) // k
        return Z(f'Ein Aufzug darf höchstens {L} kg tragen. Eine Person ({p} kg) will Kisten zu je {k} kg mitnehmen. Wie viele Kisten darf sie höchstens einladen?',
                 n, f'({L} - {p}) // {k}', f'{p} + {k}x ≤ {L} → {k}x ≤ {L - p} → x ≤ {ca(Fr(L - p, k))}. Höchstens {n} Kisten.',
                 'Stelle eine Ungleichung mit „≤“ auf. Nur ganze Kisten sind möglich.')
    if art == 'regal':
        L, k = R.choice([40, 50, 60, 75, 80]), R.choice([3, 4, 6, 7, 8, 9])
        if L % k == 0: L += 1
        n = L // k
        return Z(f'Ein Regalbrett trägt höchstens {L} kg. Ein Karton wiegt {k} kg. Wie viele Kartons passen höchstens darauf?',
                 n, f'{L} // {k}', f'{k}x ≤ {L} → x ≤ {ca(Fr(L, k))}. Höchstens {n} Kartons.', 'Teile und runde ab.')
    if art == 'tarif':
        g, p, B = R.choice([5, 8, 10, 12]), R.choice([Fr(3, 2), Fr(2), Fr(5, 2), Fr(3), Fr(7, 2)]), R.choice([20, 25, 30, 35, 40])
        n = int((B - g) / p)
        return Z(f'Ein Handytarif kostet im Monat {eur(g)} € Grundgebühr und {eur(p)} € je zusätzliches Datenpaket. Man will höchstens {B} € zahlen. Wie viele Datenpakete kann man höchstens kaufen?',
                 n, f'({B} - {g}) * {p.denominator} // {p.numerator}', f'{eur(g)} + {eur(p)}x ≤ {B} → {eur(p)}x ≤ {B - g} → x ≤ {ca(Fr(B - g) / p)}. Höchstens {n} Pakete.',
                 'Grundgebühr + Preis · Anzahl ≤ Höchstbetrag.')
    if art == 'taxi':
        g, p, B = R.choice([Fr(7, 2), Fr(4), Fr(9, 2)]), R.choice([Fr(2), Fr(11, 5), Fr(12, 5), Fr(5, 2)]), R.choice([20, 25, 30, 40, 50])
        n = int((B - g) / p)
        return Z(f'Eine Taxifahrt kostet {eur(g)} € Grundpreis und {eur(p)} € je angefangenen Kilometer. Wie viele Kilometer kann man mit {B} € höchstens fahren?',
                 n, f'(({B}) - {cz(g)}) * {p.denominator} // {p.numerator}' if g.denominator == 1 else f'({B} * {g.denominator} - {g.numerator}) * {p.denominator} // ({p.numerator} * {g.denominator})',
                 f'{eur(g)} + {eur(p)}x ≤ {B} → {eur(p)}x ≤ {eur(B - g)} → x ≤ {ca((B - g) / p)}. Höchstens {n} km.',
                 'Stelle die Ungleichung auf und runde passend.')
    if art == 'sparen':
        s, w, Zl = R.randint(10, 60), R.choice([4, 5, 6, 7, 8, 12, 15]), R.choice([150, 200, 250, 300, 400])
        n = (Zl - s) // w + 1
        return Z(f'Auf einem Sparbuch sind {s} €. Jede Woche kommen {w} € dazu. Nach wie vielen Wochen sind zum ersten Mal mehr als {Zl} € darauf?',
                 n, f'({Zl} - {s}) // {w} + 1', f'{s} + {w}x > {Zl} → x > {ca(Fr(Zl - s, w))}. Kleinste ganze Zahl: {n} Wochen.',
                 '„Mehr als“ bedeutet >. Gesucht ist die kleinste passende ganze Zahl.')
    if art == 'kino':
        e, r = R.choice([Fr(9), Fr(19, 2), Fr(10), Fr(21, 2), Fr(12)]), R.choice([Fr(4), Fr(9, 2), Fr(5), Fr(6)])
        j = R.choice([45, 50, 60, 70, 80, 90])
        n = int(j / (e - r)) + 1
        return Z(f'Ein Kinobesuch kostet {eur(e)} €. Mit einer Jahreskarte für {j} € zahlt man pro Besuch nur {eur(r)} €. Ab wie vielen Besuchen ist man mit der Jahreskarte billiger?',
                 n, f'{j} * {(e - r).denominator} // {(e - r).numerator} + 1', f'{j} + {eur(r)}x < {eur(e)}x → {eur(e - r)}x > {j} → x > {ca(j / (e - r))}. Ab {n} Besuchen.',
                 'Kosten mit Karte < Kosten ohne Karte. Gesucht ist die kleinste ganze Zahl.')
    # vergleich zweier Tarife
    g1, p1 = R.choice([0, 2, 3]), R.choice([Fr(3, 2), Fr(2), Fr(5, 2)])
    g2, p2 = g1 + R.choice([6, 8, 10, 12]), p1 - R.choice([Fr(1, 2), Fr(1)])
    n = int((g2 - g1) / (p1 - p2)) + 1
    return Z(f'Fitness-Studio A: {g1} € Grundbetrag, {eur(p1)} € je Besuch. Studio B: {g2} € Grundbetrag, {eur(p2)} € je Besuch. Ab wie vielen Besuchen im Monat ist B billiger?',
             n, f'({g2} - {g1}) * {(p1 - p2).denominator} // {(p1 - p2).numerator} + 1',
             f'{g2} + {eur(p2)}x < {g1} + {eur(p1)}x → {eur(p1 - p2)}x > {g2 - g1} → x > {ca((g2 - g1) / (p1 - p2))}. Ab {n} Besuchen.',
             'Stelle „Kosten B < Kosten A“ auf und löse nach x.')


GEN = {'umformen': g_umformen, 'umdrehen': g_umdrehen, 'klammern': g_klammern, 'intervall': g_intervall, 'pruefen': g_pruefen, 'sachaufgabe': g_sachaufgabe}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Ungleichungen lösen', ['umformen', 'umdrehen', 'klammern']), ('Lösungsmenge', ['intervall', 'pruefen']), ('Anwenden', ['sachaufgabe'])],
         'Lineare Ungleichungen lösen, beim Multiplizieren oder Dividieren mit einer negativen Zahl das Zeichen umdrehen und die Lösungsmenge als Intervall angeben.',
         ['Wie bei Gleichungen umformen – aber: Mal oder geteilt durch eine negative Zahl dreht das Zeichen um.',
          '< und > : Grenze gehört nicht dazu, Klammer nach außen. ≤ und ≥ : Grenze gehört dazu, Klammer nach innen.',
          'Höchstens = ≤, mindestens = ≥.'],
         offen=['Lehrplan nennt auch das graphische Lösen von Ungleichungen (Geraden im Koordinatensystem). Dafür braucht die App eine Zeichnung von Funktionsgraphen; nicht gebaut.',
                'Lernkarte „umformen“: Lösungsmenge als markierter Bereich auf dem Zahlenstrahl (offener/geschlossener Kreis, Schraffur) kann die App nicht zeichnen; es wird nur die Grenze markiert.'])
