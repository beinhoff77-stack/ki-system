"""Aufgabenfamilien: Zahlen, Bruch- und Dezimalrechnen, Potenzen, Zehnerpotenzen, Prozent, Zinsen, Proportionalität, Einheiten."""
from fractions import Fraction as Fr
import math

import sympy as sp

from _nachbau_kern import Kern, check, wissen, z, zk, euro, NAMEN, hoch


def wert(s):
    """Dargestellten Term unabhängig auswerten (Prüfung)."""
    t = s.replace('−', '-').replace('·', '*').replace(':', '/').replace('[', '(').replace(']', ')')
    t = t.replace('²', '**2').replace('³', '**3').replace('⁴', '**4').replace('⁵', '**5')
    import re
    t = re.sub(r'(\d),(\d)', r'\1.\2', t)
    return sp.nsimplify(sp.sympify(t, rational=True))


def nett(v, maxnenner=40, maxbetrag=200):
    v = sp.nsimplify(v)
    if not v.is_Rational:
        return False
    return abs(v.q) <= maxnenner and abs(v) <= maxbetrag


def zufall_zahl(rng, art, groesse=12):
    if art == 'ganz':
        n = 0
        while n == 0:
            n = rng.randint(-groesse, groesse)
        return Fr(n)
    if art == 'bruch':
        nen = rng.choice([2, 3, 4, 5, 6, 8, 9, 10, 12])
        zae = rng.choice([x for x in range(-11, 12) if x and math.gcd(x, nen) == 1])
        return Fr(zae, nen)
    if art == 'dez':
        return Fr(rng.choice([x for x in range(-95, 96) if x and x % 10]), rng.choice([10, 100]) if groesse > 5 else 10)
    raise ValueError(art)


VORLAGEN_GEMISCHT = [
    ('{a} − {b} · ({c} − {d})', '({a} − {b}) · ({c} − {d})', 'Punkt vor Strich missachtet'),
    ('({a} + {b}) : {c} − {d}', '{a} + {b} : {c} − {d}', 'Klammer nicht zuerst berechnet'),
    ('{a} · {b} + {c} : {d}', '{a} · ({b} + {c}) : {d}', 'Punkt vor Strich missachtet'),
    ('[{a} − ({b} + {c})] · {d}', '[{a} − {b} + {c}] · {d}', 'Minusklammer falsch aufgelöst'),
    ('{a} − ({b} − {c}) · {d}', '{a} − {b} − {c} · {d}', 'Minusklammer falsch aufgelöst'),
]


def f_qterm(rng, niv, info, et):
    arten = {'I': ['ganz', 'bruch', 'dez'], 'II': ['bruch', 'dez', 'ganz'], 'III': ['bruch', 'dez']}[niv]
    for _ in range(400):
        if et == 'brueche_plus_minus':
            a, b, c = (zufall_zahl(rng, 'bruch') for _ in range(3))
            s = f'{zk(a, False)} + {zk(b, False)}' if niv == 'I' else f'{zk(a, False)} − {zk(b, False)} + {zk(c, False)}'
            fs, fg = None, None
        elif et in ('brueche_mal', 'brueche_geteilt'):
            a, b = zufall_zahl(rng, 'bruch'), zufall_zahl(rng, 'bruch')
            op = '·' if et == 'brueche_mal' else ':'
            s = f'{zk(a, False)} {op} {zk(b, False)}'
            if niv != 'I':
                s += f' {op if rng.random() < .5 else "·"} {zk(zufall_zahl(rng, "bruch"), False)}'
            fs = s.replace(':', '·') if op == ':' else None
            fg = 'mit dem Divisor statt mit seinem Kehrwert multipliziert' if fs else None
        elif et in ('dezimal_mal', 'dezimal_geteilt'):
            a = zufall_zahl(rng, 'dez')
            b = Fr(rng.choice([2, 4, 5, 8, 12, 15, 25, 6]), rng.choice([10, 100]))
            if et == 'dezimal_geteilt':
                a = b * rng.randint(3, 40) * (1 if rng.random() < .5 else -1)
                s = f'{zk(a)} : {zk(b)}'
            else:
                s = f'{zk(a)} · {zk(b)}'
            fs, fg = None, None
        elif et in ('vorzeichen', 'addieren', 'ketten'):
            n = 3 if niv == 'I' else 5
            teile = [zufall_zahl(rng, 'ganz' if niv == 'I' else rng.choice(['ganz', 'dez']), 30) for _ in range(n)]
            s = zk(teile[0])
            for t in teile[1:]:
                s += f' {rng.choice(["+", "−"])} {zk(t)}'
            fs, fg = None, None
        elif et == 'potenzen':
            a, b, c = rng.randint(2, 5), rng.randint(2, 4), rng.randint(2, 6)
            s = f'(−{a})² − {b}³ : {zk(Fr(-c))}' if niv != 'I' else f'(−{a})² + {b}²'
            fs, fg = (f'−{a}² − {b}³ : {zk(Fr(-c))}' if niv != 'I' else f'−{a}² + {b}²'), 'Vorzeichen bei (−a)² falsch'
        elif et == 'rechenvorteile':
            g = zufall_zahl(rng, 'dez')
            p = Fr(rng.randint(11, 89), 100)
            s = f'{z(p)} · {zk(g)} + {z(1 - p)} · {zk(g)}'
            fs, fg = None, None
        else:  # gemischt, fehler_finden, sonst
            vor, fvor, fg = rng.choice(VORLAGEN_GEMISCHT)
            vals = {k: zufall_zahl(rng, rng.choice(arten)) for k in 'abcd'}
            if vals['d'] == 0 or vals['c'] == 0:
                continue
            fmt = {k: zk(v) for k, v in vals.items()}
            s, fs = vor.format(**fmt), fvor.format(**fmt)
        try:
            v = wert(s)
        except ZeroDivisionError:
            continue
        if not nett(v, 60 if niv == 'III' else 30):
            continue
        fw = None
        if fs:
            try:
                fw = wert(fs)
            except ZeroDivisionError:
                fw = None
            if fw is None or not getattr(fw, 'is_Rational', False) or fw == v:
                fs = None
        break
    vf = Fr(int(v.p), int(v.q))
    falsch = []
    if fs:
        falsch.append((z(Fr(int(fw.p), int(fw.q))), fg))
    falsch.append((z(-vf) if vf != 0 else '1', 'Vorzeichenfehler'))
    falsch.append((z(vf + rng.choice([1, -1, Fr(1, 2)])), 'Rechenfehler in einem Zwischenschritt'))
    weg = ['Rechenreihenfolge beachten: Klammern, dann Potenzen, Punkt vor Strich.',
           'Vorzeichenregeln anwenden und Zwischenergebnisse kürzen.', f'Ergebnis: {s} = {z(vf)}']
    if et == 'rechenvorteile':
        weg = [f'Distributivgesetz: gemeinsamen Faktor {zk(g)} ausklammern.', f'({z(p)} + {z(1 - p)}) · {zk(g)} = 1 · {zk(g)} = {z(g)}']
    ziel = 'Berechne geschickt.' if et == 'rechenvorteile' else 'Berechne.'
    if info.get('typ') == 'Sachaufgabe' or et == 'sach':
        return f_ganz_sach(rng, niv, info, et)
    return Kern('', f'{ziel} {s} = ?', z(vf), weg, falsch,
                [check('Wert unabhängig ausgewertet', wert(s) == v)], luecke=f'Ergänze das Ergebnis: {s} = ___')


KONTEXTE_GANZ = [
    ('Temperatur', 'Am Morgen zeigt das Thermometer an einer Bergstation {a} °C. Bis zum Mittag steigt die Temperatur um {b} °C, '
     'am Abend fällt sie gegenüber dem Mittag um {c} °C.', 'Gib die Abendtemperatur an.', '°C'),
    ('Konto', 'Auf {n}s Konto stehen {a} €. Es werden {b} € für ein Fahrrad abgebucht, danach gehen {c} € Taschengeld ein.',
     'Berechne den neuen Kontostand.', '€'),
    ('Tauchen', 'Eine Taucherin befindet sich {a} m unter der Wasseroberfläche (Höhe −{a} m). Sie taucht {b} m tiefer und steigt dann {c} m auf.',
     'In welcher Höhe (bezogen auf die Wasseroberfläche) befindet sie sich jetzt?', 'm'),
    ('Aufzug', 'Ein Aufzug startet im Untergeschoss −{a}. Er fährt {b} Etagen nach oben und dann {c} Etagen nach unten.',
     'In welcher Etage hält er?', ''),
]


def f_ganz_sach(rng, niv, info, et):
    name, ctx, frage, einh = rng.choice(KONTEXTE_GANZ)
    a, b, c = rng.randint(2, 30), rng.randint(5, 60), rng.randint(5, 60)
    n = rng.choice(NAMEN)
    if name == 'Temperatur':
        a = -a
        e = a + b - c
        s = ctx.format(a=z(a), b=b, c=c)
        weg = [f'Mittag: {z(a)} + {b} = {z(a + b)}', f'Abend: {z(a + b)} − {c} = {z(e)}']
    elif name == 'Konto':
        a = rng.randint(20, 300)
        b = a + rng.randint(10, 200)
        e = a - b + c
        s = ctx.format(n=n, a=a, b=b, c=c)
        weg = [f'{a} − {b} = {z(a - b)}', f'{z(a - b)} + {c} = {z(e)}']
    elif name == 'Tauchen':
        c = rng.randint(2, a + b - 1)
        e = -a - b + c
        s = ctx.format(a=a, b=b, c=c)
        weg = [f'−{a} − {b} = {z(-a - b)}', f'{z(-a - b)} + {c} = {z(e)}']
    else:
        a, b, c = rng.randint(1, 3), rng.randint(3, 9), rng.randint(1, 9)
        e = -a + b - c
        s = ctx.format(a=a, b=b, c=c)
        weg = [f'−{a} + {b} = {z(-a + b)}', f'{z(-a + b)} − {c} = {z(e)}']
    if niv != 'I':
        frage += ' Schreibe zuerst einen Rechenterm auf.'
    ant = f'{z(e)} {einh}'.strip()
    return Kern(s, frage, ant, weg, [(f'{z(-e)} {einh}'.strip(), 'Vorzeichen verwechselt'), (f'{z(e + 2 * c)} {einh}'.strip(), 'Richtung der Änderung verwechselt')],
                [check('Ergebnis aus den Einzelschritten', _aus_weg(weg) == e)])


def _aus_weg(weg):
    """letzte Zahl des letzten Schritts unabhängig neu berechnen: linke Seite auswerten."""
    links = weg[-1].split('=')[0]
    erster = weg[0].split('=')[0]
    return wert(erster.replace('Mittag:', '').strip()) if False else wert(links.replace('Abend:', '').strip().replace('€', ''))


def f_ordnen(rng, niv, info, et):
    for _ in range(200):
        n = 5 if niv == 'I' else 6
        zahlen = set()
        while len(zahlen) < n:
            art = rng.choice(['ganz', 'dez', 'bruch']) if et != 'ordnen' else 'ganz'
            zahlen.add(zufall_zahl(rng, art, 12))
        zahlen = list(zahlen)
        if len({float(x) for x in zahlen}) == n:
            break
    rng.shuffle(zahlen)
    darst = [z(x, False if x.denominator in (3, 6, 9, 12) else None) for x in zahlen]
    sortiert = sorted(zahlen)
    if et == 'zahlengerade':
        ziel = 'Zeichne eine Zahlengerade mit passender Einteilung und markiere diese Zahlen: ' + '; '.join(darst) + '.'
        ant = 'Reihenfolge von links nach rechts: ' + ' < '.join(z(x) for x in sortiert)
        weg = ['Kleinste und größte Zahl bestimmen, Einheit so wählen, dass alle Zahlen Platz haben.', ant]
    elif et == 'betrag':
        x = zahlen[0]
        aus = rng.choice([('Der Betrag einer negativen Zahl ist immer größer als die Zahl selbst.', True,
                           'der Betrag ist positiv, die Zahl negativ, z. B. |−3| = 3 > −3.'),
                          ('Zwei verschiedene Zahlen können denselben Betrag haben.', True, 'z. B. |−4| = |4| = 4.'),
                          ('Der Betrag einer Zahl ist immer größer als die Zahl.', False, 'für positive Zahlen gilt |a| = a, z. B. |5| = 5.')])
        return Kern('', f'Berechne |{z(x)}| und |{z(-x)}|.', f'|{z(x)}| = |{z(-x)}| = {z(abs(x))}',
                    [f'Der Betrag ist der Abstand von 0: {z(abs(x))}.'], [(z(x if x < 0 else -x), 'Betrag mit Gegenzahl verwechselt')],
                    [check('Betrag', abs(x) >= 0)], aussage=('Prüfe die Aussage und begründe: „' + aus[0] + '“', aus[1], aus[2]))
    else:
        ziel = 'Ordne der Größe nach. Beginne mit der kleinsten Zahl: ' + '; '.join(darst) + '.'
        ant = ' < '.join(z(x, False if x.denominator in (3, 6, 9, 12) else None) for x in sortiert)
        weg = ['Alle Zahlen in Dezimalschreibweise vergleichen (Brüche umwandeln).', 'Negative Zahlen: je größer der Betrag, desto kleiner die Zahl.', ant]
    falsch = [(' < '.join(z(x) for x in sorted(zahlen, key=abs)), 'nach dem Betrag statt nach dem Wert geordnet'),
              (' < '.join(z(x) for x in sorted(zahlen, key=lambda v: (v < 0, abs(v) if v < 0 else v))), 'negative Zahlen falsch eingeordnet'),
              (' < '.join(z(x) for x in sorted(zahlen, key=lambda v: (v.denominator != 1, v))), 'Brüche und Dezimalzahlen nicht umgerechnet')]
    if et == 'zahlengerade':
        falsch = [('Reihenfolge von links nach rechts: ' + f, g) for f, g in falsch]
    return Kern('', ziel, ant, weg, falsch, [check('sortiert', all(sortiert[i] < sortiert[i + 1] for i in range(n - 1)))])


def f_umkehr(rng, niv, info, et):
    a, b = zufall_zahl(rng, 'ganz', 40), zufall_zahl(rng, 'ganz', 40)
    if niv != 'I':
        a, b = zufall_zahl(rng, 'dez'), zufall_zahl(rng, 'dez')
    op = rng.choice(['+', '−'])
    x = b - a if op == '+' else a - b
    s = f'{zk(a)} {op} ___ = {z(b)}'
    pr = (a + x == b) if op == '+' else (a - x == b)
    return Kern('', f'Ergänze die fehlende Zahl: {s}', z(x), [f'Umkehraufgabe: {"" if op == "+" else z(a) + " − "}{z(b)}{" − " + zk(a) if op == "+" else ""} = {z(x)}', f'Probe: {zk(a)} {op} {zk(x)} = {z(b)}'],
                [(z(-x), 'Umkehroperation mit falschem Vorzeichen')], [check('Probe', pr)])


def f_dezimal(rng, niv, info, et):
    if et == 'runden':
        w = Fr(rng.randint(10000, 999999), 10000)
        st = rng.choice([1, 2])
        r = Fr(round(w * 10 ** st), 10 ** st)
        # korrektes kaufmännisches Runden
        r = Fr(math.floor(w * 10 ** st + Fr(1, 2)), 10 ** st)
        return Kern('', f'Runde {z(w)} auf {"eine Stelle" if st == 1 else "zwei Stellen"} nach dem Komma.', z(r, st),
                    [f'Die {st + 1}. Nachkommastelle entscheidet: 0–4 abrunden, 5–9 aufrunden.', f'{z(w)} ≈ {z(r, st)}'],
                    [(z(Fr(math.floor(w * 10 ** st), 10 ** st), st), 'immer abgerundet'), (z(Fr(math.ceil(w * 10 ** st), 10 ** st), st), 'immer aufgerundet')],
                    [check('Rundung', abs(r - w) <= Fr(1, 2 * 10 ** st))])
    nen = rng.choice([4, 5, 8, 20, 25, 3, 6, 9])
    zae = rng.choice([k for k in range(1, nen * 2) if math.gcd(k, nen) == 1])
    w = Fr(zae, nen)
    if w.denominator in (3, 6, 9):
        d = f'{float(w):.4f}'.replace('.', ',') + '… (periodisch)'
    else:
        d = z(w, True)
    return Kern('', f'Schreibe {zae}/{nen} als Dezimalbruch.', d, [f'{zae} : {nen} = {d}'], [(z(Fr(nen, zae) if zae else 0, True), 'Zähler und Nenner vertauscht')],
                [check('Division', abs(float(w) - zae / nen) < 1e-12)])


# ---------- Potenzen ----------
def f_potenz(rng, niv, info, et, thema):
    a = rng.randint(2, 6)
    n = rng.randint(2, 4)
    m = rng.randint(2, 6)
    var = rng.choice(['a', 'b', 'x', 'y', 'k'])
    if et == 'potenz_begriff' or et == 'fehler_finden':
        varianten = [(f'(−{a})^{n}', Fr(-a) ** n, f'−{a}^{n}', -Fr(a) ** n, 'das Minus gehört bei −a^n nicht zur Basis'),
                     (f'−{a}^{n}', -Fr(a) ** n, f'(−{a})^{n}', Fr(-a) ** n, 'Basis und Vorzeichen verwechselt'),
                     (f'({a}/{a + 1})^{n}', Fr(a, a + 1) ** n, None, Fr(a ** n, a + 1), 'nur den Zähler potenziert')]
        txt, v, ft, fv, grund = rng.choice(varianten)
        sup = lambda s: s.replace('^2', '²').replace('^3', '³').replace('^4', '⁴')
        if et == 'fehler_finden' or info.get('typ') == 'beschreiben':
            pass
        erkl = {0: f'Basis ist −{a}: (−{a}) wird {n}-mal mit sich selbst multipliziert.', 1: f'Basis ist {a}: Das Minus steht vor der Potenz und gehört nicht zur Basis, also −({a}·…·{a}) mit {n} Faktoren.',
                2: f'Zähler und Nenner werden beide {n}-mal mit sich selbst multipliziert.'}[[v_[0] for v_ in varianten].index(txt)]
        return Kern('', f'Berechne den Potenzwert {sup(txt)}.', z(v), [erkl, f'= {z(v)}'],
                    [(z(fv), grund), (z(a * n), 'Basis mit Exponent multipliziert')], [check('Potenzwert', v == (Fr(-a) ** n if txt.startswith('(−') else (-Fr(a) ** n if txt.startswith('−') else Fr(a, a + 1) ** n)))],
                    luecke=f'Ergänze: {sup(txt)} = ___')
    if et == 'negativer_exponent':
        b = rng.choice([2, 3, 5, 10])
        k = rng.randint(1, 3)
        v = Fr(1, b ** k)
        return Kern('', f'Schreibe {hoch(b, -k)} als Bruch und als Dezimalzahl, falls möglich.', f'{hoch(b, -k)} = 1/{b ** k}' + (f' = {z(v, True)}' if b != 3 else ''),
                    [f'a⁻ⁿ = 1/aⁿ', f'{hoch(b, -k)} = 1/{hoch(b, k)} = 1/{b ** k}'], [(z(-b * k), 'negativen Exponenten als Faktor gelesen'), (z(Fr(-1, b ** k)), 'Exponent als Vorzeichen gedeutet')],
                    [check('Kehrwert', v * b ** k == 1)])
    if et == 'gleicher_exponent':
        p, q = rng.choice([(2, 5), (4, 25), (5, 20), (25, 4), (8, 125)])
        k = rng.randint(3, 6)
        v = (p * q) ** k
        return Kern('', f'Berechne geschickt: {p}^{k} · {q}^{k}'.replace(f'^{k}', '⁰¹²³⁴⁵⁶⁷⁸⁹'[k]), f'({p} · {q})^{k} = {p * q}^{k} = {z(v)}',
                    [f'Gleicher Exponent: a^n · b^n = (a · b)^n', f'= {p * q}^{k} = {z(v)}'], [(z((p * q) ** (2 * k)), 'Exponenten addiert'), (z(p + q), 'falsch')],
                    [check('Potenzgesetz', p ** k * q ** k == v)])
    # Rechenregeln mit Variablen
    e1, e2 = rng.randint(2, 7), rng.randint(2, 6)
    c1, c2 = rng.randint(2, 6), rng.randint(2, 6)
    v_ = sp.Symbol(var)
    e3 = 0
    if et == 'mal_gleiche_basis':
        ausdr = c1 * v_ ** e1 * c2 * v_ ** e2
        s = f'{c1}{var}^{e1} · {c2}{var}^{e2}'
        f_ = f'{c1 * c2}{var}^{e1 * e2}'
        gr = 'Exponenten multipliziert statt addiert'
    elif et == 'geteilt_gleiche_basis':
        e1 = e2 + rng.randint(1, 5)
        c1 = c2 * rng.randint(2, 6)
        ausdr = c1 * v_ ** e1 / (c2 * v_ ** e2)
        s = f'{c1}{var}^{e1} : ({c2}{var}^{e2})'
        f_ = f'{sp.Rational(c1, c2)}{var}^{sp.Rational(e1, e2) if e1 % e2 == 0 else e1 + e2}'
        gr = 'Exponenten dividiert bzw. addiert statt subtrahiert'
    elif et == 'potenz_von_potenz':
        ausdr = (c1 * v_ ** e1) ** e2 if e2 <= 3 else (v_ ** e1) ** e2
        e2 = min(e2, 3)
        ausdr = (c1 * v_ ** e1) ** e2
        s = f'({c1}{var}^{e1})^{e2}'
        f_ = f'{c1 * e2}{var}^{e1 + e2}'
        gr = 'Exponenten addiert und Faktor mit Exponent multipliziert'
    else:  # anwenden
        e3 = rng.randint(1, 4)
        ausdr = (v_ ** e1 * v_ ** e2) / v_ ** e3 * c1
        s = f'{c1} · {var}^{e1} · {var}^{e2} : {var}^{e3}'
        f_ = f'{c1}{var}^{e1 * e2 - e3}'
        gr = 'Exponenten multipliziert statt addiert'
    ausdr = sp.simplify(ausdr)
    sup = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')

    def schoen(t):
        import re
        return re.sub(r'\^(\d+)', lambda m: m.group(1).translate(sup), t).replace('**', '^')

    ant = schoen(str(ausdr).replace('**', '^').replace('*', ''))
    erwartet = {'mal_gleiche_basis': c1 * c2 * v_ ** (e1 + e2), 'geteilt_gleiche_basis': sp.Rational(c1, c2) * v_ ** (e1 - e2),
                'potenz_von_potenz': c1 ** e2 * v_ ** (e1 * e2)}.get(et, c1 * v_ ** (e1 + e2 - e3))
    gepr = sp.simplify(ausdr - erwartet) == 0
    return Kern('', f'Vereinfache so weit wie möglich: {schoen(s)}', ant,
                ['Potenzen mit gleicher Basis: multiplizieren → Exponenten addieren; dividieren → Exponenten subtrahieren; potenzieren → Exponenten multiplizieren.',
                 'Zahlfaktoren getrennt verrechnen.', f'Ergebnis: {ant}'],
                [(schoen(f_), gr), (schoen(f'{c1 + c2}{var}^{e1 + e2}'), 'Faktoren addiert statt multipliziert')],
                [check('mit sympy vereinfacht', gepr)], luecke=f'Vereinfache: {schoen(s)} = ___')


def f_zehner(rng, niv, info, et):
    if et in ('gross_wissenschaftlich', 'zehnerpotenz'):
        m = Fr(rng.randint(11, 99), 10)
        k = rng.randint(5, 12)
        w = m * 10 ** k
        kont = rng.choice(['Die Entfernung zweier Himmelskörper beträgt', 'Ein Land hat ungefähr', 'Ein Rechenzentrum speichert', 'Der Jahresumsatz einer Firma beträgt'])
        einh = {'Die Entfernung zweier Himmelskörper beträgt': 'km', 'Ein Land hat ungefähr': 'Einwohner', 'Ein Rechenzentrum speichert': 'Byte', 'Der Jahresumsatz einer Firma beträgt': '€'}[kont]
        return Kern(f'{kont} {z(w)} {einh}.', 'Schreibe die Zahl in wissenschaftlicher Schreibweise (mit Zehnerpotenz).', f'{z(m)} · {hoch(10, k)}',
                    [f'Komma so verschieben, dass eine Ziffer vor dem Komma steht: {z(m)}.', f'Das Komma wurde um {k} Stellen verschoben → · {hoch(10, k)}.'],
                    [(f'{z(m)} · {hoch(10, k + 1)}', 'Stellen falsch gezählt'), (f'{z(m * 10)} · {hoch(10, k - 1)}', 'nicht normiert')],
                    [check('Wert', m * 10 ** k == w)])
    if et in ('klein_wissenschaftlich', 'negativer_exponent'):
        m = Fr(rng.randint(11, 99), 10)
        k = rng.randint(3, 9)
        w = m / 10 ** k
        return Kern(f'Ein Bakterium ist etwa {z(w, True)} m lang.' if rng.random() < .5 else f'Eine Staubschicht ist {z(w, True)} m dick.',
                    'Schreibe die Länge mit einer Zehnerpotenz.', f'{z(m)} · {hoch(10, -k)} m',
                    [f'Komma um {k} Stellen nach rechts verschieben → Exponent −{k}.'], [(f'{z(m)} · {hoch(10, k)} m', 'Vorzeichen des Exponenten vergessen'), (f'{z(m)} · {hoch(10, -k - 1)} m', 'Stellen falsch gezählt')],
                    [check('Wert', m * Fr(1, 10 ** k) == w)])
    if et in ('vorsilben_gross', 'vorsilben_klein'):
        tab = [('k', 3), ('M', 6), ('G', 9), ('T', 12)] if et == 'vorsilben_gross' else [('m', -3), ('µ', -6), ('n', -9)]
        v, e = rng.choice(tab)
        einh = rng.choice(['m', 'g', 'W', 'Byte' if et == 'vorsilben_gross' else 's'])
        zahl = Fr(rng.randint(12, 950), 10)
        return Kern('', f'Schreibe {z(zahl)} {v}{einh} in der Grundeinheit {einh} mit Zehnerpotenz.', f'{z(zahl)} · {hoch(10, e)} {einh}',
                    [f'{v} bedeutet {hoch(10, e)}.'], [(f'{z(zahl)} · {hoch(10, -e)} {einh}', 'Vorsilbe falsch gedeutet')], [wissen('Vorsilbe')])
    # vergleichen_pruefen
    m1, m2 = Fr(rng.randint(11, 99), 10), Fr(rng.randint(11, 99), 10)
    k1 = rng.randint(3, 8)
    k2 = k1 + rng.choice([-1, 1])
    w1, w2 = m1 * Fr(10) ** k1, m2 * Fr(10) ** k2
    zei = '<' if w1 < w2 else ('>' if w1 > w2 else '=')
    return Kern('', f'Setze <, > oder = ein: {z(m1)} · {hoch(10, k1)} ___ {z(m2)} · {hoch(10, k2)}', zei,
                ['Zuerst die Exponenten vergleichen, bei gleichem Exponenten die Vorfaktoren.', f'{z(w1)} {zei} {z(w2)}'],
                [('>' if zei == '<' else '<', 'nur die Vorfaktoren verglichen')], [check('Vergleich', (w1 < w2) == (zei == '<'))])


# ---------- Prozent ----------
P_KONTEXTE = [('Ein Fahrrad kostet', '€', (180, 900)), ('Eine Schule hat', 'Schülerinnen und Schüler', (300, 1200)),
              ('Ein Sportverein hat', 'Mitglieder', (120, 800)), ('Eine Wanderung ist', 'km lang', (8, 40)),
              ('Ein Handyvertrag kostet im Jahr', '€', (120, 480)), ('Ein Bäcker backt am Tag', 'Brezen', (200, 900))]


def f_prozent(rng, niv, info, et):
    ktx, einh, (lo, hi) = rng.choice(P_KONTEXTE)
    p = rng.choice([5, 10, 12, 15, 20, 25, 30, 35, 40, 60, 75, 8, 4]) if niv != 'III' else rng.choice([2.5, 7.5, 12.5, 17.5, 3, 6, 15, 35])
    p = Fr(p).limit_denominator(10)
    for _ in range(100):
        g = rng.randint(lo, hi)
        if niv == 'I':
            g = (g // 10) * 10 or 10
        w = g * p / 100
        if w.denominator in (1, 2, 4, 5, 10, 20, 100) and w > 0:
            break
    euro_ = einh == '€'
    W = (lambda v: euro(v)) if euro_ else (lambda v: f'{z(v)} {einh.split()[0]}')
    if et == 'prozent_bedeutung':
        b = rng.choice([Fr(3, 4), Fr(2, 5), Fr(7, 20), Fr(1, 8), Fr(13, 25), Fr(3, 2), Fr(9, 10)])
        return Kern('', f'Schreibe {b.numerator}/{b.denominator} als Dezimalbruch und in Prozent.', f'{z(b, True)} = {z(b * 100)} %',
                    [f'{b.numerator} : {b.denominator} = {z(b, True)}', f'· 100 → {z(b * 100)} %'], [(f'{z(b * 10)} %', 'mit 10 statt 100 multipliziert')],
                    [check('Umrechnung', b * 100 == Fr(z(b * 100).replace(',', '.')) if ',' not in z(b * 100) else True)])
    if et in ('prozentwert',):
        return Kern(f'{ktx} {W(g) if euro_ else str(g) + " " + einh}.'.replace(' €.', ' €.'), f'Berechne {z(p)} % davon.', W(w),
                    [f'Prozentwert = Grundwert · p/100', f'{g} · {z(p)}/100 = {z(w)}'], [(W(g * p / 10), 'durch 10 statt durch 100 geteilt'), (W(g - w), 'Restwert statt Prozentwert')],
                    [check('W = G·p', w * 100 == g * p)])
    if et in ('prozentsatz',):
        saetze = {'Eine Schule hat': f'Von {g} Schülerinnen und Schülern einer Schule kommen {z(w)} mit dem Bus.',
                  'Ein Sportverein hat': f'Von {g} Mitgliedern eines Sportvereins sind {z(w)} jünger als 18 Jahre.',
                  'Eine Wanderung ist': f'Von einer {g} km langen Wanderung sind {z(w)} km geschafft.',
                  'Ein Bäcker backt am Tag': f'Von {g} gebackenen Brezen sind bis Mittag {z(w)} verkauft.'}
        return Kern(saetze.get(ktx, f'Ein Preis wird um {euro(w)} gesenkt. Der alte Preis war {euro(g)}.'), 'Wie viel Prozent sind das?', f'{z(p)} %',
                    [f'p = W : G · 100', f'{z(w)} : {g} · 100 = {z(p)}'], [(f'{z(Fr(g, 1) / w * 100 if w else 0)} %', 'Grundwert und Prozentwert vertauscht'), (f'{z(100 - p)} %', 'Restanteil berechnet')],
                    [check('p = W/G', p == w * 100 / g)])
    if et in ('zurueck', 'grundwert'):
        art = rng.choice(['vermindert', 'vermehrt', 'einfach']) if niv != 'I' else 'einfach'
        if art == 'einfach':
            return Kern(f'{z(p)} % einer Strecke sind {z(w)} km.' if not euro_ else f'{z(p)} % des Kaufpreises sind {euro(w)} Anzahlung.',
                        'Berechne den Grundwert.', (f'{g} km' if not euro_ else euro(g)), [f'G = W : p · 100', f'{z(w)} : {z(p)} · 100 = {g}'],
                        [(z(w * p / 100), 'Prozentwert vom Prozentwert berechnet'), (z(w + w * p / 100), 'Prozentsatz addiert')], [check('G·p/100 = W', g * p / 100 == w)])
        f = 1 + p / 100 if art == 'vermehrt' else 1 - p / 100
        neu = g * f
        tx = (f'Nach einer Preiserhöhung um {z(p)} % kostet ein Artikel {euro(neu)}.' if art == 'vermehrt'
              else f'Im Ausverkauf kostet eine Jacke nach {z(p)} % Rabatt noch {euro(neu)}.')
        return Kern(tx, 'Wie viel hat der Artikel vorher gekostet?', euro(g), [f'Neuer Preis = {z(f * 100)} % des alten Preises.', f'Alter Preis = {euro(neu)} : {z(f, True)} = {euro(g)}'],
                    [(euro(neu * (1 - p / 100) if art == 'vermehrt' else neu * (1 + p / 100)), f'{z(p)} % vom neuen Preis {"abgezogen" if art == "vermehrt" else "aufgeschlagen"}'),
                     (euro(neu - w), 'Prozentwert vom alten Preis falsch zugeordnet')], [check('Rückrechnung', g * f == neu)])
    if et in ('vermehrt', 'vermindert', 'faktor'):
        f = 1 + p / 100 if et == 'vermehrt' else 1 - p / 100
        neu = g * f
        return Kern(f'{ktx} {W(g)}.', f'Der Wert {"steigt" if et == "vermehrt" else "sinkt"} um {z(p)} %. Berechne den neuen Wert mit dem Wachstumsfaktor.', W(neu),
                    [f'Faktor {z(f, True)}', f'{g} · {z(f, True)} = {z(neu)}'], [(W(g * p / 100), 'nur die Änderung berechnet'), (W(g * (2 - f)), 'falsche Richtung')],
                    [check('Faktor', neu == g + (g * p / 100 if et == 'vermehrt' else -g * p / 100))])
    if et in ('mehrfach', 'argumente'):
        p1 = rng.choice([10, 20, 25, 30, 40, 50])
        p2 = p1 if et == 'argumente' or rng.random() < .5 else rng.choice([10, 20, 25])
        f = Fr(100 + p1, 100) * Fr(100 - p2, 100)
        gesamt = (f - 1) * 100
        behauptung = f'Ein Preis wird zuerst um {p1} % erhöht und danach um {p2} % gesenkt. {rng.choice(NAMEN)} sagt: „Dann ist der Preis insgesamt um {p1 - p2} % gestiegen.“'
        wahr = gesamt == p1 - p2
        grund = f'Gesamtfaktor {z(Fr(100 + p1, 100), True)} · {z(Fr(100 - p2, 100), True)} = {z(f, True)}, also Änderung {z(gesamt)} %; die zweite Änderung bezieht sich auf einen anderen Grundwert.'
        return Kern('', f'Ein Preis wird zuerst um {p1} % erhöht und danach um {p2} % gesenkt. Um wie viel Prozent hat er sich insgesamt verändert?',
                    f'{"+" if gesamt > 0 else ""}{z(gesamt)} %', [f'Faktoren multiplizieren: {z(Fr(100 + p1, 100), True)} · {z(Fr(100 - p2, 100), True)} = {z(f, True)}', f'Änderung: {z(gesamt)} %'],
                    [(f'{p1 - p2} %', 'Prozentsätze einfach addiert/subtrahiert')], [check('Gesamtfaktor', f * 100 - 100 == gesamt)],
                    aussage=(behauptung + ' Hat sie/er recht? Begründe.', wahr, grund))
    return f_prozent(rng, niv, info, 'prozentwert')


def f_zins(rng, niv, info, et):
    k = rng.choice([800, 1200, 1500, 2400, 3600, 4000, 5000, 7200, 12000])
    p = rng.choice([Fr(3, 2), 2, Fr(5, 2), 3, Fr(7, 2), 4, Fr(9, 2), 5, 6])
    jz = k * Fr(p) / 100
    n = rng.choice(NAMEN)
    if et == 'jahreszinsen':
        return Kern(f'{n} legt {euro(k)} für ein Jahr zu einem Zinssatz von {z(p)} % an.', 'Berechne die Jahreszinsen.', euro(jz),
                    ['Z = K · p/100', f'{k} · {z(p)}/100 = {z(jz)}'], [(euro(k * Fr(p) / 10), 'durch 10 statt 100 geteilt'), (euro(k + jz), 'Endkapital statt Zinsen')],
                    [check('Z·100 = K·p', jz * 100 == k * Fr(p))])
    if et == 'zinssatz':
        return Kern(f'Für einen Kredit über {euro(k)} zahlt eine Familie in einem Jahr {euro(jz)} Zinsen.', 'Berechne den Zinssatz.', f'{z(p)} %',
                    ['p = Z : K · 100', f'{z(jz)} : {k} · 100 = {z(p)}'], [(f'{z(Fr(k) / jz)} %', 'Kapital durch Zinsen geteilt')], [check('p', Fr(p) == jz * 100 / k)])
    if et == 'kapital':
        return Kern(f'Bei einem Zinssatz von {z(p)} % bringt ein Guthaben in einem Jahr {euro(jz)} Zinsen.', 'Wie groß ist das Guthaben?', euro(k),
                    ['K = Z : p · 100', f'{z(jz)} : {z(p)} · 100 = {k}'], [(euro(jz * Fr(p) / 100), 'mit p/100 multipliziert statt geteilt')], [check('K', k == jz / Fr(p) * 100)])
    mon = rng.choice([3, 4, 5, 7, 8, 9]) if et != 'zeitanteil' else None
    if et == 'monatszinsen' or mon:
        mon = mon or 5
        zm = jz * Fr(mon, 12)
        return Kern(f'{euro(k)} werden {mon} Monate lang zu {z(p)} % verzinst.', 'Berechne die Zinsen.', euro(zm),
                    [f'Jahreszinsen: {z(jz)} €', f'· {mon}/12 = {z(zm, 2)} €'], [(euro(jz), 'Jahreszinsen statt Monatszinsen'), (euro(jz * mon), 'mit Monaten multipliziert ohne :12')],
                    [check('Zm', zm * 12 == jz * mon)])
    tage = rng.choice([36, 45, 60, 72, 90, 120, 150, 200, 240, 300])
    zt = jz * Fr(tage, 360)
    return Kern(f'{euro(k)} werden {tage} Tage lang zu {z(p)} % angelegt (1 Jahr = 360 Tage).', 'Berechne die Zinsen.', euro(zt),
                [f'Jahreszinsen: {z(jz)} €', f'· {tage}/360 = {z(zt, 2)} €'], [(euro(jz * Fr(tage, 365)), '365 statt 360 Tage'), (euro(jz), 'Zeitanteil vergessen')],
                [check('Zt', zt * 360 == jz * tage)])


# ---------- Proportionalität ----------
PROP = [('Für {a} kg Äpfel zahlt man {b} €.', 'Wie viel kosten {c} kg?', 'kg', '€'),
        ('Ein Drucker druckt in {a} Minuten {b} Seiten.', 'Wie viele Seiten druckt er in {c} Minuten?', 'min', 'Seiten'),
        ('Ein Auto verbraucht auf {a} km {b} Liter Benzin.', 'Wie viel verbraucht es auf {c} km?', 'km', 'l'),
        ('{a} Hefte kosten {b} €.', 'Was kosten {c} Hefte?', 'Hefte', '€')]
INDIREKT = [('{a} Helfer brauchen für das Aufbauen einer Bühne {b} Stunden.', 'Wie lange brauchen {c} Helfer (gleiches Arbeitstempo)?', 'Helfer', 'h'),
            ('Ein Futtervorrat reicht für {a} Ziegen {b} Tage.', 'Wie lange reicht er für {c} Ziegen?', 'Ziegen', 'Tage'),
            ('Bei {a} Teilnehmenden zahlt jeder {b} € für den Bus.', 'Wie viel zahlt jeder bei {c} Teilnehmenden?', 'Personen', '€'),
            ('Mit {a} Pumpen ist ein Becken in {b} Stunden leer.', 'Wie lange dauert es mit {c} Pumpen?', 'Pumpen', 'h')]


def f_prop(rng, niv, info, et, indirekt):
    kt, fr, e1, e2 = rng.choice(INDIREKT if indirekt else PROP)
    teilbar = e2 in ('€', 'l', 'h')
    for _ in range(400):
        a = rng.randint(2, 12)
        b = rng.randint(3, 40) * (rng.choice([1, 1, Fr(1, 2)]) if not indirekt and teilbar else 1)
        c = rng.randint(2, 15)
        if c == a:
            continue
        e = Fr(b) * Fr(a) / c if indirekt else Fr(b) / a * c
        if (e.denominator == 1) or (teilbar and e.denominator in (2, 4, 5, 10, 20, 25, 100)):
            break
    stamm = kt.format(a=a, b=z(b), c=c)
    if et in ('pruefen', 'erkennen', 'unterscheiden', 'produkt', 'vervielfachen', 'graph'):
        if indirekt:
            k = rng.choice([12, 24, 36, 48, 60, 72, 120])
            xs = sorted(rng.sample([d for d in range(1, 25) if k % d == 0 and d * d != k or (k % d == 0 and d < 13)], 4))
        else:
            xs = sorted(rng.sample(range(1, 13), 4))
            k = rng.randint(2, 9)
        ys = [Fr(k, x) if indirekt else Fr(k) * x for x in xs]
        stoer = rng.random() < .4 and et in ('pruefen', 'unterscheiden', 'erkennen')
        if stoer:
            ys[2] = ys[2] + 1
        tab = '| x | ' + ' | '.join(str(x) for x in xs) + ' |\n|---|' + '---|' * 4 + '\n| y | ' + ' | '.join(z(y) for y in ys) + ' |'
        if et in ('vervielfachen', 'produkt'):
            luecke_i = rng.randint(1, 3)
            ys_t = [z(y) if i != luecke_i else '___' for i, y in enumerate(ys)]
            tab = '| x | ' + ' | '.join(str(x) for x in xs) + ' |\n|---|' + '---|' * 4 + '\n| y | ' + ' | '.join(ys_t) + ' |'
            art = 'umgekehrt proportional' if indirekt else 'proportional'
            return Kern(f'Die Zuordnung x ↦ y ist {art}.\n\n{tab}\n', 'Ergänze die fehlende Zahl und gib die Rechnung an.', z(ys[luecke_i]),
                        [('Produkt x · y ist konstant: ' if indirekt else 'Quotient y : x ist konstant: ') + z(k), f'y = {z(ys[luecke_i])}'],
                        [(z(Fr(k) * xs[luecke_i] if indirekt else Fr(k, xs[luecke_i])), 'proportional und umgekehrt proportional verwechselt')],
                        [check('Konstante', all((x * y == k) if indirekt else (y / x == k) for x, y in zip(xs, ys)))])
        if et == 'graph':
            x0 = rng.choice([v for v in range(1, 31) if k % v == 0 and v not in xs] or [1]) if indirekt else rng.choice([v for v in range(2, 15) if v not in xs])
            y0 = Fr(k, x0) if indirekt else k * x0
            return Kern(f'Zu der Tabelle gehört ein Graph.\n\n{tab}\n', f'Wie heißt die Form des Graphen? Bestimme den y-Wert für x = {x0}.',
                        f'{"Hyperbel(ast)" if indirekt else "Ursprungshalbgerade"}; y = {z(y0)}',
                        [('x · y = ' if indirekt else 'y : x = ') + z(k), f'y = {z(y0)}'], [('Gerade durch den Ursprung' if indirekt else 'Hyperbel', 'Graphformen verwechselt')],
                        [check('Wert', (x0 * y0 == k) if indirekt else (y0 == k * x0))])
        if stoer:
            ant = 'weder proportional noch umgekehrt proportional'
            grund = f'bei x = {xs[2]} passt der y-Wert nicht ({"Produkt" if indirekt else "Quotient"} ändert sich)'
        else:
            ant = 'umgekehrt proportional' if indirekt else 'proportional'
            grund = ('alle Produkte x · y = ' if indirekt else 'alle Quotienten y : x = ') + z(k)
        return Kern(f'\n\n{tab}\n', 'Ist die Zuordnung proportional, umgekehrt proportional oder keins von beiden? Begründe.', f'{ant} ({grund})',
                    ['Quotienten y : x und Produkte x · y berechnen.', grund], [(o, 'Zuordnungsarten verwechselt') for o in ('proportional', 'umgekehrt proportional', 'weder proportional noch umgekehrt proportional') if o != ant],
                    [wissen('Konstanz')], antwort_kurz=ant)
    if et == 'aenderung':
        v1, t1 = rng.randint(3, 9) * 10, rng.randint(2, 5)
        return Kern(f'Ein Zug fährt gleichmäßig {v1 * t1} km in {t1} Stunden.', 'Wie weit kommt er in 1,5 Stunden? Wie verändert sich der Graph (Strecke über Zeit), wenn er halb so schnell fährt?',
                    f'{z(Fr(v1 * 3, 2))} km; die Halbgerade wird halb so steil', [f'{v1 * t1} : {t1} = {v1} km pro Stunde', f'{v1} · 1,5 = {z(Fr(v1 * 3, 2))}'],
                    [(f'{z(v1 * t1 * Fr(3, 2))} km', 'mit der Gesamtstrecke statt mit der Geschwindigkeit gerechnet')], [check('Weg', Fr(v1) * Fr(3, 2) * t1 == Fr(v1 * t1 * 3, 2))])
    frage = fr.format(c=c)
    ant = f'{z(e)} {e2}'
    weg = [f'Auf die Einheit schließen: 1 {e1} → {z(Fr(b) * a) if indirekt else z(Fr(b) / a)} {e2}', f'{c} {e1} → {z(e)} {e2}']
    falsch = [(f'{z(Fr(b) / a * c if indirekt else Fr(b) * a / c)} {e2}', 'proportional und umgekehrt proportional verwechselt'), (f'{z(Fr(b) + c - a)} {e2}', 'Differenz statt Verhältnis gerechnet')]
    return Kern(stamm, frage, ant, weg, falsch, [check('Verhältnis', (e * c == Fr(b) * a) if indirekt else (e / c == Fr(b) / a))])


# ---------- Einheiten ----------
def f_einheiten(rng, niv, info, et):
    if et == 'zeit':
        h = Fr(rng.choice([15, 25, 35, 45, 55, 65, 75, 85, 105, 125]), 10)
        mi = h * 60
        return Kern('', f'Wandle {z(h)} h in Stunden und Minuten um.', f'{int(h)} h {int(mi - int(h) * 60)} min',
                    [f'{z(h - int(h))} h = {z((h - int(h)) * 60)} min'], [(f'{int(h)} h {int(round((h - int(h)) * 100))} min', 'Nachkommastellen als Minuten gelesen')],
                    [check('Minuten', mi == int(h) * 60 + (mi - int(h) * 60))])
    if et == 'massstab':
        m = rng.choice([25000, 50000, 100000, 200000])
        cm = Fr(rng.randint(15, 95), 10)
        km = cm * m / 100000
        return Kern(f'Auf einer Wanderkarte im Maßstab 1 : {z(m)} sind zwei Orte {z(cm)} cm voneinander entfernt.', 'Wie groß ist die Entfernung in Wirklichkeit (in km)?',
                    f'{z(km)} km', [f'{z(cm)} cm · {z(m)} = {z(cm * m)} cm', f'= {z(km)} km'], [(f'{z(km * 10)} km', 'beim Umrechnen eine Stelle verschoben')],
                    [check('Maßstab', km * 100000 == cm * m)])
    if et == 'kommaschreibweise':
        g = rng.randint(1205, 98765)
        return Kern('', f'Schreibe {g} g in kg (Kommaschreibweise).', f'{z(Fr(g, 1000))} kg', ['1 kg = 1000 g'], [(f'{z(Fr(g, 100))} kg', 'Umrechnungszahl 100 statt 1000')],
                    [wissen('kg')])
    tab = [('die Höhe einer Zimmertür', '2 m', ['20 cm', '20 m', '0,2 km']), ('die Masse eines Apfels', '150 g', ['15 g', '1,5 kg', '15 kg']),
           ('die Fläche eines Handballfelds', '800 m²', ['80 m²', '8 000 m²', '8 ha'])]
    was, r, f = rng.choice(tab)
    return Kern('', f'Schätze {was}.', r, ['Mit bekannten Vergleichsgrößen schätzen.'], [(x, 'unrealistische Größenordnung') for x in f], [wissen('Auswahl')])


def f_stellenwert(rng, niv, info, et):
    ziff = rng.sample(range(10), 6)
    if ziff[0] == 0:
        ziff[0], ziff[1] = ziff[1], ziff[0]
    gross = int(''.join(map(str, sorted(ziff, reverse=True))))
    kl = sorted(ziff)
    if kl[0] == 0:
        kl[0], kl[1] = kl[1], kl[0]
    klein = int(''.join(map(str, kl)))
    return Kern(f'Aus den Ziffern {", ".join(map(str, ziff))} (jede genau einmal) werden sechsstellige Zahlen gebildet.', 'Gib die größte und die kleinste mögliche Zahl an und berechne ihre Differenz.',
                f'{z(gross)}; {z(klein)}; Differenz {z(gross - klein)}', ['Größte Zahl: Ziffern absteigend; kleinste: aufsteigend, aber 0 nicht vorne.', f'{z(gross)} − {z(klein)} = {z(gross - klein)}'],
                [(z(gross - int(''.join(map(str, sorted(ziff))))), '0 an erster Stelle zugelassen')], [check('Ziffern', sorted(str(gross)) == sorted(str(klein)))])


def f_brueche(rng, niv, info, et):
    nen = rng.choice([4, 5, 6, 8, 10, 12, 15, 20])
    zae = rng.choice([k for k in range(1, nen) if math.gcd(k, nen) == 1])
    b = Fr(zae, nen)
    ganz = nen * rng.randint(3, 20)
    if et in ('anteil_bestimmen', 'bruchteil_von'):
        return Kern(f'Von {ganz} Losen einer Tombola sind {z(b, False)} Gewinne.', 'Wie viele Gewinnlose sind das?', z(ganz * b),
                    [f'{ganz} : {nen} · {zae} = {z(ganz * b)}'], [(z(ganz * nen // zae if zae else 0), 'durch den Bruch geteilt statt multipliziert')], [check('Anteil', ganz * b * nen == ganz * zae)])
    if et == 'ganzes_bestimmen':
        teil = ganz * b
        return Kern(f'{z(b, False)} der Klasse fahren mit dem Bus; das sind {z(teil)} Kinder.', 'Wie viele Kinder hat die Klasse?', z(Fr(ganz)),
                    [f'{z(teil)} : {zae} · {nen} = {ganz}'], [(z(teil * b), 'Anteil vom Anteil berechnet')], [check('Ganzes', teil / b == ganz)])
    if et == 'vergleichen':
        c = Fr(rng.choice([k for k in range(1, nen + 3) if math.gcd(k, nen + 1) == 1]), nen + 1)
        zei = '<' if b < c else ('>' if b > c else '=')
        return Kern('', f'Vergleiche {z(b, False)} und {z(c, False)} (setze <, > oder =).', zei, ['Auf den Hauptnenner bringen und Zähler vergleichen.'],
                    [('>' if zei == '<' else '<', 'nur die Nenner verglichen'), ('=', 'gleiche Zähler für gleich gehalten')], [check('Vergleich', (b < c) == (zei == '<'))])
    k = rng.randint(2, 6)
    if et == 'kuerzen':
        return Kern('', f'Kürze vollständig: {zae * k}/{nen * k}', f'{zae}/{nen}', [f'Durch {k} kürzen.'], [(f'{zae * k // math.gcd(zae * k, 2) if (zae * k) % 2 == 0 else zae}/{nen * k // 2 if (nen * k) % 2 == 0 else nen}', 'nicht vollständig gekürzt')],
                    [check('gleichwertig', Fr(zae * k, nen * k) == b)])
    return Kern('', f'Erweitere {zae}/{nen} auf den Nenner {nen * k}.', f'{zae * k}/{nen * k}', [f'Zähler und Nenner mit {k} multiplizieren.'], [(f'{zae}/{nen * k}', 'nur den Nenner erweitert')],
                [check('gleichwertig', Fr(zae * k, nen * k) == b)])
