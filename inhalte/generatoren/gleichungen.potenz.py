#!/usr/bin/env python3
"""Thema gleichungen.potenz – Potenzgleichungen xⁿ = c (Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(905)
HZ = HOCHZ
L2 = 'x₁ = □; x₂ = □'
H2 = 'kleinere Lösung zuerst'
GR = {2: 15, 3: 6, 4: 5, 5: 3, 6: 3, 7: 2, 8: 2}


def xn(n, v='x'):
    return f'{v}{str(n).translate(HZ)}'


def wz(n, a):
    return f'√{a}' if n == 2 else f'{str(n).translate(HZ)}√{a}'


ETAPPEN = [
    {'lernziel': 'gerade', 'titel': 'xⁿ = c mit geradem Exponenten',
     'regel': 'n gerade: Für ⟦c > 0⟧ gibt es zwei Lösungen ⟦x = ±ⁿ√c⟧, für c = 0 nur x = 0, für ⟦c < 0 keine⟧ (gerade Potenzen sind nie negativ).',
     'schritte': ['x⁴ = 16: Welche Zahlen hoch 4 ergeben 16? 2⁴ = 16 und (−2)⁴ = 16.', 'Also ⟦x₁ = −2, x₂ = 2⟧.'],
     'probe': '(−2)⁴ = (−2)(−2)(−2)(−2) = 16 ✓',
     'fehler': 'x⁴ = 16 ⇒ x = 2 ist unvollständig: Bei geradem Exponenten ist auch ⟦−2⟧ eine Lösung.'},
    {'lernziel': 'ungerade', 'titel': 'xⁿ = c mit ungeradem Exponenten',
     'regel': 'n ungerade: Es gibt ⟦genau eine Lösung⟧. Für c ≥ 0 ist x = ⁿ√c, für ⟦c < 0⟧ ist x = ⟦−ⁿ√|c|⟧ (negativ).',
     'schritte': ['x³ = −125: Ungerader Exponent, c negativ.', 'x = −³√125 = ⟦−5⟧, denn (−5)³ = −125.'],
     'probe': '(−5) · (−5) · (−5) = 25 · (−5) = −125 ✓',
     'fehler': '„x³ = −125 hat keine Lösung“ ist falsch: Bei ⟦ungeradem⟧ Exponenten ergibt eine negative Zahl hoch n etwas Negatives. x = −5.'},
    {'lernziel': 'anzahl', 'titel': 'Lösungsanzahl begründen',
     'regel': 'Entscheidend sind ⟦n gerade oder ungerade⟧ und das ⟦Vorzeichen von c⟧. Am Graphen: Wie oft schneidet die Gerade y = c den Graphen von y = xⁿ?',
     'schritte': ['x⁶ = −1: n = 6 ist gerade, x⁶ ist nie negativ.', 'Die Gerade y = −1 schneidet den Graphen von y = x⁶ nicht: ⟦keine Lösung⟧.'],
     'probe': 'x⁶ = (x³)² ≥ 0 für jedes x ✓',
     'fehler': '„x⁵ = 32 hat zwei Lösungen 2 und −2“ ist falsch: (−2)⁵ = ⟦−32⟧. Bei ungeradem Exponenten gibt es nur eine Lösung.'},
    {'lernziel': 'umformen', 'titel': 'Erst umformen, dann Wurzel ziehen',
     'regel': 'Bringe die Gleichung auf die Form ⟦(…)ⁿ = c⟧. Steht eine Klammer hoch n, löst du zuerst nach der ⟦Klammer⟧ auf.',
     'schritte': ['2x³ + 7 = 61 | − 7, : 2 ergibt x³ = 27.', 'x = ³√27 = ⟦3⟧.'],
     'probe': '2 · 27 + 7 = 61 ✓',
     'fehler': '2x³ = 54 ⇒ x³ = 54 − 2 ist falsch: Die 2 ist ein ⟦Faktor⟧, also wird ⟦geteilt⟧: x³ = 27.'},
    {'lernziel': 'naeherung', 'titel': 'Lösungen mit dem Taschenrechner',
     'regel': 'Ist c keine „glatte“ Potenz, bestimmst du ⁿ√c mit dem ⟦Taschenrechner⟧ und ⟦rundest⟧ sinnvoll. Vorzeichen-Regeln gelten wie sonst.',
     'schritte': ['x³ = 40: genau eine Lösung x = ³√40.', 'Taschenrechner: ³√40 ≈ 3,42 (auf zwei Nachkommastellen ⟦x ≈ 3,42⟧).'],
     'probe': '3,42³ ≈ 40,0 ✓',
     'fehler': 'x³ = 40 ⇒ x = 40 : 3 ≈ 13,33 ist falsch: Die Probe zeigt 13,33³ ≈ 2 370. Man muss die ⟦dritte Wurzel⟧ ziehen.'},
    {'lernziel': 'sachaufgabe', 'titel': 'Sachaufgaben mit Potenzgleichungen',
     'regel': 'Stelle eine Gleichung der Form ⟦xⁿ = c⟧ auf (Würfel: a³ = V, Wachstum: q² = Faktor) und prüfe, welche Lösung ⟦im Sachzusammenhang⟧ passt.',
     'schritte': ['Ein Würfel hat das Volumen 216 cm³: a³ = 216.', 'a = ³√216 = ⟦6⟧, die Kante ist 6 cm lang.'],
     'probe': '6 cm · 6 cm · 6 cm = 216 cm³ ✓',
     'fehler': 'Bei a² = 49 für eine Seitenlänge a = −7 cm anzugeben ist falsch: Längen sind ⟦positiv⟧, nur a = 7 cm passt.'},
]


def g_gerade(s):
    n = 2 if s == 1 else R.choice([4, 6]) if s == 2 else R.choice([2, 4, 6, 8])
    r = R.randint(1 if s == 1 else 2, GR[n])
    c = r ** n
    if s == 3 and R.random() < 0.4:
        if R.random() < 0.5:
            return auswahl(f'Welche Lösungsmenge hat {xn(n)} = −{dz(c)}?', 'L = { }', [f'L = {{−{r}}}', f'L = {{−{r}; {r}}}', f'L = {{{r}}}'],
                           f'n = {n} ist gerade, {xn(n)} ist nie negativ. Keine Lösung.', 'Kann eine gerade Potenz negativ sein?')
        return auswahl(f'Welche Lösungsmenge hat {xn(n)} = 0?', 'L = {0}', ['L = { }', 'L = {−1; 1}', 'L = {0; 1}'],
                       f'Nur 0 hoch {n} ergibt 0.', 'Welche Zahl hoch n ergibt 0?')
    if s == 2 and R.random() < 0.3:
        n, r = 2, R.randint(11, 25)
        c = r * r
    form = R.choice([f'Löse {xn(n)} = {dz(c)}.', f'Löse {xn(n)} − {dz(c)} = 0.', f'Bestimme alle Lösungen von {dz(c)} = {xn(n)}.'])
    return luecken(form, L2, H2, [-r, r], f'n = {n} gerade, c > 0: x = ±{wz(n, dz(c))} = ±{r}.',
                   'Gerader Exponent: Denke an beide Vorzeichen.', c=[f'-({c} / {r} ** {n - 1})', f'{c} / {r} ** {n - 1}'])


def g_ungerade(s):
    n = 3 if s == 1 else R.choice([3, 5]) if s == 2 else R.choice([3, 5, 7])
    r = R.randint(1, 10 if n == 3 and s > 1 else GR[n])
    neg = s > 1 and R.random() < 0.6 or s == 1 and R.random() < 0.3
    c = -(r ** n) if neg else r ** n
    x = -r if neg else r
    if s > 1 and R.random() < 0.3:
        z = Fr(R.randint(1, 4), 10) * (-1 if neg else 1)
        c = z ** n
        return zahl(f'Löse {xn(n)} = {dz(c)}.', f'n = {n} ungerade: genau eine Lösung x = {dz(z)}, denn {kl(z)}{str(n).translate(HZ)} = {dz(c)}.',
                    'Ungerader Exponent: Vorzeichen bleibt erhalten. Achte auf die Nachkommastellen.', z, f'{float(c)} / ({float(z)}) ** {n - 1}')
    return zahl(f'Löse {xn(n)} = {dz(c)}.',
                f'n = {n} ungerade: genau eine Lösung x = {"−" if neg else ""}{wz(n, dz(abs(c)))} = {dz(x)}.',
                'Ungerader Exponent: Das Vorzeichen von c bleibt erhalten.', x, f'({c}) / ({x}) ** {n - 1}')


def g_anzahl(s):
    n = R.randint(2, 9)
    r = R.randint(1, 4 if n < 6 else 2)
    c = R.choice([r ** n, -(r ** n), 0]) if s > 1 else R.choice([r ** n, -(r ** n)])
    if n % 2 == 0:
        k = 2 if c > 0 else 1 if c == 0 else 0
    else:
        k = 1
    txt = {0: 'keine Lösung', 1: 'genau eine Lösung', 2: 'zwei Lösungen'}
    grund = (f'n = {n} ist {"gerade" if n % 2 == 0 else "ungerade"}' +
             (f' und c {"> 0" if c > 0 else "= 0" if c == 0 else "< 0"}' if n % 2 == 0 else '') + f': {txt[k]}.')
    if s < 3:
        return auswahl(f'Wie viele Lösungen hat {xn(n)} = {dz(c)}?', txt[k], list(txt.values()), grund,
                       'Ist der Exponent gerade oder ungerade? Welches Vorzeichen hat c?')
    typ = R.random()
    if typ < 0.35:
        n = R.choice([3, 5, 7])
        r = R.randint(2, GR[n])
        return auswahl(f'Jemand sagt: „{xn(n)} = {dz(r ** n)} hat die Lösungen {r} und −{r}.“ Was stimmt?',
                       f'Falsch: (−{r}){str(n).translate(HZ)} = −{dz(r ** n)}, nur x = {r} ist Lösung.',
                       ['Richtig, wie bei x² gibt es zwei Lösungen.', f'Falsch: Es gibt keine Lösung.', f'Falsch: Nur x = −{r} ist Lösung.'],
                       f'Bei ungeradem Exponenten wird eine negative Zahl hoch {n} negativ. Probe: (−{r}){str(n).translate(HZ)} = −{dz(r ** n)} ≠ {dz(r ** n)}.',
                       'Mache die Probe mit der negativen Zahl.')
    if typ < 0.7:
        n = R.choice([3, 5, 7])
        r = R.randint(2, GR[n])
        return auswahl(f'Jemand sagt: „{xn(n)} = −{dz(r ** n)} hat keine Lösung, weil man aus negativen Zahlen keine Wurzel ziehen kann.“ Was stimmt?',
                       f'Falsch: x = −{r} ist Lösung, denn (−{r}){str(n).translate(HZ)} = −{dz(r ** n)}.',
                       ['Richtig, negative Radikanden sind verboten.', f'Falsch: x = {r} ist Lösung.', f'Falsch: Es gibt zwei Lösungen ±{r}.'],
                       f'Bei ungeradem Exponenten gibt es immer genau eine Lösung. Hier x = −{wz(n, dz(r ** n))} = −{r}.',
                       'Prüfe, ob eine negative Zahl die Gleichung erfüllt.')
    n = R.choice([4, 6, 8])
    d = R.randint(1, 20)
    return auswahl(f'Für welche Werte von c hat {xn(n)} = c genau zwei Lösungen?', 'für alle c > 0',
                   ['für alle c', 'für alle c ≥ 0', 'für alle c < 0'],
                   f'n = {n} gerade: Für c > 0 schneidet y = c den Graphen zweimal (z. B. c = {d}), für c = 0 einmal, für c < 0 nie.',
                   'Denke an den Graphen von y = x' + str(n).translate(HZ) + ' und waagrechte Geraden.')


def g_umformen(s):
    if s == 1:
        n = R.choice([2, 3])
        a, r = R.randint(2, 6), R.randint(2, GR[n] if n == 3 else 10)
        if n == 2:
            return luecken(f'Löse {a}x² = {dz(a * r * r)}.', L2, H2, [-r, r], f'x² = {dz(a * r * r)} : {a} = {r * r}, x = ±{r}.',
                           'Teile zuerst durch den Faktor vor x².', c=[f'-({a * r * r} / {a}) / {r}', f'({a * r * r} / {a}) / {r}'])
        return zahl(f'Löse {a}x³ = {dz(a * r ** 3)}.', f'x³ = {dz(a * r ** 3)} : {a} = {r ** 3}, x = {r}.',
                    'Teile zuerst durch den Faktor vor x³.', r, f'({a * r ** 3} / {a}) / {r} ** 2')
    if s == 2:
        n = R.choice([3, 4, 5])
        r = R.randint(1, GR[n])
        a, b = R.randint(2, 5), nz9()
        neg = n % 2 == 1 and R.random() < 0.5
        x = -r if neg else r
        rechts = a * x ** n + b
        t = f'Löse {a}{xn(n)} {plus(b)} = {dz(rechts)}.'
        w = f'{a}{xn(n)} = {dz(rechts - b)} ⇒ {xn(n)} = {dz(x ** n)}'
        if n % 2 == 0:
            return luecken(t, L2, H2, [-r, r], w + f' ⇒ x = ±{r}.', 'Erst die Zahl, dann den Faktor auf die andere Seite bringen.',
                           c=[f'-(({rechts} - ({b})) / {a}) / {r} ** {n - 1}', f'(({rechts} - ({b})) / {a}) / {r} ** {n - 1}'])
        return zahl(t, w + f' ⇒ x = {dz(x)}.', 'Erst die Zahl, dann den Faktor auf die andere Seite bringen.', x,
                    f'(({rechts} - ({b})) / {a}) / ({x}) ** {n - 1}')
    n = R.choice([2, 3, 4])
    p, r = nz9(), R.randint(1, 4 if n > 2 else 9)
    if n == 3:
        neg = R.random() < 0.5
        k = -r if neg else r
        return zahl(f'Löse {minus_klammer(p)}³ = {dz(k ** 3)}.', f'{minus_klammer(p)[1:-1]} = {wz(3, dz(k ** 3)) if k > 0 else "−" + wz(3, dz(-k ** 3))} = {dz(k)}, also x = {dz(p + k)}.',
                    'Löse zuerst nach der Klammer auf, dann nach x.', p + k, f'{p} + ({k ** 3}) / ({k}) ** 2')
    return luecken(f'Löse {minus_klammer(p)}{str(n).translate(HZ)} = {dz(r ** n)}.', L2, H2, [p - r, p + r],
                   f'{minus_klammer(p)[1:-1]} = ±{r}, also x₁ = {dz(p - r)}, x₂ = {dz(p + r)}.',
                   'Gerader Exponent: Die Klammer ist ±' + wz(n, '…') + '.', c=[f'{p} - {r ** n} / {r} ** {n - 1}', f'{p} + {r ** n} / {r} ** {n - 1}'])


def nz9():
    return R.choice([i for i in range(-9, 10) if i != 0])


def g_naeherung(s):
    n = R.choice([3, 3, 4, 5]) if s < 3 else R.choice([3, 4, 5, 6])
    c = R.randint(2, 300)
    if round(c ** (1 / n)) ** n == c: return None
    wahr = c ** (1 / n)
    v = gerundet(wahr, 2)
    if v is None: return None
    if s == 1:
        n = 3
        wahr = c ** (1 / 3)
        v = gerundet(wahr, 2)
        if v is None or round(wahr) ** 3 == c: return None
        return zahl(f'Löse x³ = {c}. Runde auf zwei Nachkommastellen.', f'x = ³√{c} ≈ {dz(v)}.', 'Nutze die Wurzeltaste des Taschenrechners.',
                    v, f'round({K(wahr)}, 2)')
    if s == 2 or n % 2:
        neg = n % 2 == 1 and R.random() < 0.5
        cc = -c if neg else c
        x = -v if neg else v
        if n % 2 == 0:
            return zahl(f'Löse {xn(n)} = {c}. Gib die positive Lösung auf zwei Nachkommastellen an.', f'x = ±{wz(n, c)} ≈ ±{dz(v)}; positiv: {dz(v)}.',
                        'Gerader Exponent: zwei Lösungen ±ⁿ√c.', v, f'round({K(wahr)}, 2)')
        return zahl(f'Löse {xn(n)} = {dz(cc)}. Runde auf zwei Nachkommastellen.',
                    f'Ungerader Exponent: x = {"−" if neg else ""}{wz(n, c)} ≈ {dz(x)}.', 'Vorzeichen von c beachten.', x,
                    f'round({"-" if neg else ""}{K(wahr)}, 2)')
    a = R.randint(2, 5)
    return zahl(f'Löse {a}{xn(n)} = {a * c}. Gib die negative Lösung auf zwei Nachkommastellen an.',
                f'{xn(n)} = {c}, x = ±{wz(n, c)} ≈ ±{dz(v)}; negativ: −{dz(v)}.', 'Erst durch den Faktor teilen.', -v,
                f'round(-{K(wahr)}, 2)')


def g_sachaufgabe(s):
    typ = R.random()
    if s == 1:
        a = R.randint(2, 12)
        dinge = ['Ein würfelförmiger Karton', 'Ein Würfel aus Beton', 'Ein würfelförmiges Aquarium', 'Ein Holzwürfel']
        return zahl(f'{R.choice(dinge)} hat {dz(a ** 3)} dm³ Volumen. Wie lang ist eine Kante?', f'a³ = {dz(a ** 3)} ⇒ a = ³√{dz(a ** 3)} = {a} dm.',
                    'Stelle die Volumenformel des Würfels auf.', a, f'{a ** 3} / {a} ** 2', einheit='dm')
    if s == 2:
        if typ < 0.5:
            p = R.choice([2, 3, 4, 5, 6, 8, 10])
            q = 1 + Fr(p, 100)
            K0 = R.choice([1000, 2000, 4000, 5000, 10000, 20000])
            K2 = K0 * q * q
            return zahl(f'Ein Guthaben wächst in 2 Jahren bei gleichem Zinssatz (mit Zinseszins) von {dz(K0)} € auf {dz(K2)} €. Wie hoch ist der Zinssatz in Prozent?',
                        f'{dz(K0)} · q² = {dz(K2)} ⇒ q² = {dz(q * q)} ⇒ q = {dz(q)} (positiv). Zinssatz {p} %.',
                        'Wachstumsfaktor q pro Jahr: Anfangswert · q · q = Endwert.', p, f'(({float(q * q)}) / {float(q)} - 1) * 100')
        a = R.randint(3, 12)
        return zahl(f'Eine quadratische Terrasse ist mit {dz(a * a)} gleich großen quadratischen Platten (Seite 1 m) belegt. Wie lang ist eine Seite der Terrasse?',
                    f'a² = {dz(a * a)} ⇒ a = {a} m (nur die positive Lösung ist eine Länge).', 'Stelle a² = … auf.', a, f'{a * a} / {a}', einheit='m')
    if typ < 0.5:
        l, b, h = R.choice([(2, 4, 8), (4, 4, 4 * 2 * 2), (3, 9, 8), (2, 9, 12), (4, 6, 9), (5, 5, 5), (2, 2, 16), (6, 9, 4), (8, 8, 1), (3, 6, 12)])
        a = round((l * b * h) ** (1 / 3))
        if a ** 3 != l * b * h: return None
        return zahl(f'Ein Quader ({l} cm × {b} cm × {h} cm) wird eingeschmolzen und zu einem Würfel mit gleichem Volumen gegossen. Wie lang ist eine Würfelkante?',
                    f'V = {l} · {b} · {h} = {l * b * h} cm³. a³ = {l * b * h} ⇒ a = {a} cm.', 'Das Volumen bleibt gleich.', a,
                    f'({l} * {b} * {h}) / {a} ** 2', einheit='cm')
    x = R.randint(2, 8)
    k = R.choice([2, 3, 4])
    V = k * x ** 3
    return zahl(f'Eine Kiste hat eine quadratische Grundfläche. Sie ist {k}-mal so hoch wie breit und hat {dz(V)} cm³ Volumen. Wie breit ist sie?',
                f'V = x · x · {k}x = {k}x³ = {dz(V)} ⇒ x³ = {dz(x ** 3)} ⇒ x = {x} cm.', 'Breite x, Höhe ' + str(k) + 'x. Stelle das Volumen auf.',
                x, f'({V} / {k}) / {x} ** 2', einheit='cm')


GEN = {'gerade': g_gerade, 'ungerade': g_ungerade, 'anzahl': g_anzahl, 'umformen': g_umformen, 'naeherung': g_naeherung,
       'sachaufgabe': g_sachaufgabe}

if __name__ == '__main__':
    bauen('gleichungen.potenz',
          'Gleichungen der Form xⁿ = c lösen und die Anzahl der Lösungen begründen.',
          ['n gerade, c > 0: zwei Lösungen ±ⁿ√c; c = 0: x = 0; c < 0: keine Lösung.', 'n ungerade: genau eine Lösung (bei c < 0 negativ).',
           'Erst auf die Form (…)ⁿ = c bringen, dann Wurzel ziehen.'],
          [('Grundform xⁿ = c', ['gerade', 'ungerade', 'anzahl']), ('Umformen und Runden', ['umformen', 'naeherung']),
           ('Anwenden', ['sachaufgabe'])],
          ETAPPEN, GEN,
          meiden={'gerade': ['x⁴ = 16.'], 'ungerade': ['x³ = −125.'], 'anzahl': ['x⁶ = −1?'], 'umformen': ['= 61.'],
                  'naeherung': ['x³ = 40.'], 'sachaufgabe': ['216 dm³']},
          offen=['Lernkarte „anzahl“ braucht Zeichnung: Graphen von y = xⁿ (n gerade/ungerade) mit waagrechter Geraden y = c, um die Lösungsanzahl zu begründen (Lehrplan: „mit Skizzen begründen“). Bisher nur in Worten.',
                 'Rechenausdruck c bei gerundeten Lösungen (Lernkarte „naeherung“): Das Prüfskript kann keine Wurzeln ziehen; der Wurzelwert steht als 12-stellige Konstante im Ausdruck.'])
