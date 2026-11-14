#!/usr/bin/env python3
"""Grundrechenarten und Rechengesetze (Gymnasium Kl. 5): Vorrangregeln, Klammern, Rechenvorteile (Vertauschen,
Verbinden, Verteilen), Multiplikation/Division ganzer Zahlen, Überschlag, schriftliches Rechnen, Termaufbau."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl5 import baue, kl, mische, schreibe, zt  # noqa: E402

R = random.Random(18)

ETAPPEN = [
    {'lernziel': 'punkt_strich', 'titel': 'Punkt vor Strich',
     'regel': '⟦Punktrechnung⟧ (mal und geteilt) kommt vor ⟦Strichrechnung⟧ (plus und minus). Gleichrangiges wird von links nach rechts gerechnet.',
     'schritte': ['3 + 4 · 5: zuerst der Punkt, 4 · 5 = 20.', 'Dann der Strich: 3 + 20 = ⟦23⟧.'],
     'fehler': 'Einfach von links nach rechts: 3 + 4 = 7, 7 · 5 = 35 ist falsch. Erst ⟦4 · 5⟧, dann plus 3.'},
    {'lernziel': 'klammern', 'titel': 'Klammern zuerst',
     'regel': 'Was in ⟦Klammern⟧ steht, wird zuerst ausgerechnet. Bei Klammern in Klammern beginnst du ⟦innen⟧. Danach gilt Punkt vor Strich.',
     'schritte': ['(3 + 4) · 5: zuerst die Klammer, 3 + 4 = 7.', 'Dann 7 · 5 = ⟦35⟧.'],
     'probe': 'Ohne Klammer wäre es 3 + 4 · 5 = 23. Die Klammer ändert das Ergebnis.',
     'fehler': 'Die Klammer übersehen und Punkt vor Strich rechnen. Die Klammer hat ⟦immer Vorrang⟧.'},
    {'lernziel': 'vorteil', 'titel': 'Geschickt: tauschen und verbinden',
     'regel': 'Bei ⟦plus⟧ und bei ⟦mal⟧ darfst du die Reihenfolge ändern und Zahlen beliebig zusammenfassen. Suche Paare, die glatte Zahlen ergeben: 25 · 4 = 100, 37 + 63 = 100.',
     'schritte': ['25 · 7 · 4: tausche zu 25 · 4 · 7.', '25 · 4 = 100, dann 100 · 7 = ⟦700⟧.'],
     'fehler': 'Auch bei Minus oder Geteilt tauschen: 10 − 3 ist nicht 3 − 10. Tauschen geht nur bei ⟦plus und mal⟧.'},
    {'lernziel': 'verteilen', 'titel': 'Geschickt: verteilen',
     'regel': 'Eine Zahl mal eine Klammer: mit ⟦jedem⟧ Teil der Klammer malnehmen. 7 · (100 − 2) = 7 · 100 − 7 · 2. Rückwärts: gemeinsamen Faktor ⟦ausklammern⟧, 6 · 13 + 6 · 7 = 6 · (13 + 7).',
     'schritte': ['7 · 98 = 7 · (100 − 2)', '7 · 100 − 7 · 2 = 700 − 14 = ⟦686⟧'],
     'fehler': 'Nur den ersten Teil malnehmen: 7 · (100 − 2) = 700 − 2 ist falsch. Auch die 2 wird ⟦mal 7⟧ genommen.'},
    {'lernziel': 'mal_ganz', 'titel': 'Ganze Zahlen multiplizieren',
     'regel': 'Rechne mit den Beträgen. ⟦Gleiche⟧ Vorzeichen ergeben plus, ⟦verschiedene⟧ Vorzeichen ergeben minus.',
     'schritte': ['(−6) · 4: Beträge 6 · 4 = 24.', 'Verschiedene Vorzeichen, also ⟦−24⟧.'],
     'probe': '(−6) + (−6) + (−6) + (−6) = −24 ✓',
     'fehler': '(−6) · (−4) = −24 ist falsch: Minus mal Minus ergibt ⟦Plus⟧, also 24.'},
    {'lernziel': 'geteilt_ganz', 'titel': 'Ganze Zahlen dividieren',
     'regel': 'Beim Dividieren gelten dieselben Vorzeichenregeln wie beim Multiplizieren: ⟦gleich → plus⟧, ⟦verschieden → minus⟧.',
     'schritte': ['(−48) : 6: Beträge 48 : 6 = 8.', 'Verschiedene Vorzeichen, also ⟦−8⟧.'],
     'probe': '(−8) · 6 = −48 ✓',
     'fehler': '(−48) : (−6) = −8 ist falsch: Minus geteilt durch Minus ergibt ⟦Plus⟧, also 8.'},
    {'lernziel': 'ueberschlag', 'titel': 'Überschlagen',
     'regel': 'Beim Überschlag rundest du jede Zahl so, dass du ⟦im Kopf⟧ rechnen kannst. So prüfst du, ob ein Ergebnis stimmen kann.',
     'schritte': ['487 · 21: runde zu 500 · 20.', '500 · 20 = ⟦10 000⟧. Das genaue Ergebnis 10 227 liegt in der Nähe.'],
     'fehler': 'Ein Ergebnis wie 1 022 hinschreiben, ohne zu prüfen: Der Überschlag 10 000 zeigt, dass eine ⟦Stelle fehlt⟧.'},
    {'lernziel': 'schriftlich', 'titel': 'Schriftlich mal und geteilt',
     'regel': 'Schriftlich multiplizieren: mit jeder Ziffer des zweiten Faktors einzeln malnehmen, ⟦stellengerecht⟧ untereinander schreiben, addieren. Schriftlich dividieren: teilen, malnehmen, abziehen, nächste Ziffer herunterholen.',
     'schritte': ['347 · 26: 347 · 20 = 6 940 und 347 · 6 = 2 082.', '6 940 + 2 082 = ⟦9 022⟧. Überschlag: 350 · 25 ≈ 8 750 ✓'],
     'fehler': 'Das Teilprodukt mit der Zehnerziffer nicht um eine Stelle versetzen. 347 · 2 Zehner sind ⟦6 940⟧, nicht 694.'},
    {'lernziel': 'termaufbau', 'titel': 'Terme lesen und aufstellen',
     'regel': 'Die Rechenart, die du ⟦zuletzt⟧ ausführst, gibt dem Term den Namen: Summe (+), Differenz (−), Produkt (·), Quotient (:).',
     'schritte': ['3 + 4 · 5: zuletzt wird addiert.', 'Der Term ist eine ⟦Summe⟧ aus 3 und dem Produkt von 4 und 5.'],
     'fehler': '3 + 4 · 5 „Produkt“ nennen, weil ein Malpunkt vorkommt. Entscheidend ist die ⟦letzte⟧ Rechnung, hier das Plus.'},
]
TEIL = {'punkt_strich': 'vorrang', 'klammern': 'vorrang', 'vorteil': 'gesetze', 'verteilen': 'gesetze', 'mal_ganz': 'ganz', 'geteilt_ganz': 'ganz',
        'ueberschlag': 'verfahren', 'schriftlich': 'verfahren', 'termaufbau': 'terme'}


def g_punkt_strich(s):
    a, b, c, d = (R.randint(2, 12) for _ in range(4))
    if s == 1:
        op = R.choice('+-')
        if op == '-': a = b * c + a
        vorn = R.random() < .5
        text = f'{a} {"+" if op == "+" else "−"} {b} · {c}' if vorn else (f'{b} · {c} {"+" if op == "+" else "−"} {a}' if op == '+' or b * c > a else None)
        if text is None: return g_punkt_strich(s)
        e = a + b * c if op == '+' else (a - b * c if vorn else b * c - a)
        return {'y': 'zahl', 'f': {'text': f'Berechne {text}.'}, 'o': {'wert': e}, 'c': text.replace('·', '*').replace('−', '-'),
                'w': f'Punkt vor Strich: zuerst {b} · {c} = {b * c}. Dann {text.replace(f"{b} · {c}", str(b * c))} = {e}.', 'h': 'Suche zuerst die Mal- oder Geteilt-Rechnung.'}
    if s == 2:
        q = R.randint(2, 9)
        form = R.choice(['mm', 'dm', 'md'])
        if form == 'mm': text, e, zw = f'{a} · {b} + {c} · {d}', a * b + c * d, f'{a * b} + {c * d}'
        elif form == 'dm': text, e, zw = f'{a * q} : {q} + {c} · {d}', a + c * d, f'{a} + {c * d}'
        else:
            if a * b <= c: return g_punkt_strich(s)
            text, e, zw = f'{a} · {b} − {c * q} : {q}', a * b - c, f'{a * b} − {c}'
        return {'y': 'zahl', 'f': {'text': f'Berechne {text}.'}, 'o': {'wert': e}, 'c': text.replace('·', '*').replace('−', '-').replace(':', '/'),
                'w': f'Zuerst beide Punktrechnungen: {zw}. Dann der Strich: {e}.', 'h': 'Es gibt zwei Punktrechnungen. Rechne beide zuerst aus.'}
    q = R.randint(2, 9)
    form = R.choice(['a', 'b', 'c'])
    if form == 'a': text, e, zw = f'{a * q + b * c + d} − {b} · {c} − {a * q} : {q}', a * q + d - a, f'{a * q + b * c + d} − {b * c} − {a}'
    elif form == 'b': text, e, zw = f'{a} + {b} · {c} · {d} − {q}', a + b * c * d - q, f'{a} + {b * c * d} − {q}'
    else: text, e, zw = f'{a * b * q} : {q} : {b} + {c} · {d}', a + c * d, f'{a} + {c * d}'
    return {'y': 'zahl', 'f': {'text': f'Berechne {text}.'}, 'o': {'wert': e}, 'c': text.replace('·', '*').replace('−', '-').replace(':', '/'),
            'w': f'Zuerst alle Punktrechnungen, jeweils von links nach rechts: {zw}. Dann von links nach rechts: {e}.', 'h': 'Erst alle Punktrechnungen. Dann die Strichrechnungen von links nach rechts.'}


def g_klammern(s):
    a, b, c, d = (R.randint(2, 12) for _ in range(4))
    py = lambda t: t.replace('·', '*').replace('−', '-').replace(':', '/').replace('[', '(').replace(']', ')')
    if s == 1:
        form = R.choice(['p', 'm'])
        if form == 'p': text, e, zw = f'({a} + {b}) · {c}', (a + b) * c, f'{a + b} · {c}'
        else: text, e, zw = f'{c} · ({a + b} − {b})', c * a, f'{c} · {a}'
        return {'y': 'zahl', 'f': {'text': f'Berechne {text}.'}, 'o': {'wert': e}, 'c': py(text), 'w': f'Zuerst die Klammer: {zw}. Ergebnis {e}.', 'h': 'Rechne zuerst aus, was in der Klammer steht.'}
    if s == 2:
        form = R.choice(['a', 'b', 'c'])
        if form == 'a': text, e, zw = f'({a} + {b}) · ({c + d} − {d})', (a + b) * c, f'{a + b} · {c}'
        elif form == 'b': text, e, zw = f'{a * b + c} − ({a} · {b} − {d if d < a * b else 1})', c + (d if d < a * b else 1), f'{a * b + c} − {a * b - (d if d < a * b else 1)}'
        else: text, e, zw = f'({a * c} + {b * c}) : {c} + {d}', a + b + d, f'{a * c + b * c} : {c} + {d} = {a + b} + {d}'
        return {'y': 'zahl', 'f': {'text': f'Berechne {text}.'}, 'o': {'wert': e}, 'c': py(text), 'w': f'Zuerst die Klammern: {zw}. Ergebnis {e}.', 'h': 'Erst jede Klammer ausrechnen, dann Punkt vor Strich.'}
    if R.random() < .5:
        text = f'{a} · [{b * c + d} − ({b} · {c} − {min(d, b * c - 1)})]'
        inn = b * c - min(d, b * c - 1); e = a * (b * c + d - inn)
        return {'y': 'zahl', 'f': {'text': f'Berechne {text}.'}, 'o': {'wert': e}, 'c': py(text),
                'w': f'Von innen nach außen: runde Klammer {b} · {c} − {min(d, b * c - 1)} = {inn}. Eckige Klammer {b * c + d} − {inn} = {b * c + d - inn}. Dann {a} · {b * c + d - inn} = {e}.',
                'h': 'Beginne mit der innersten Klammer.'}
    r1, r2 = (a + b) * c, a + b * c
    aw, i = mische(R, f'({a} + {b}) · {c}', [f'{a} + {b} · {c}', f'{a} + ({b} · {c})'])
    return {'y': 'auswahl', 'f': {'text': f'Bei welchem Term kommt {r1} heraus?'}, 'a': aw, 'o': {'index': i},
            'w': f'({a} + {b}) · {c} = {a + b} · {c} = {r1}. Die beiden anderen Terme ergeben {r2}, weil dort zuerst {b} · {c} gerechnet wird.',
            'h': 'Rechne jeden Term aus. Achte darauf, was die Klammer ändert.'}


def g_vorteil(s):
    if s == 1:
        if R.random() < .5:
            x = R.randint(11, 89); y = 100 - x; z = R.randint(11, 99)
            zs = [x, z, y]
            return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {zs[0]} + {zs[1]} + {zs[2]}'}, 'o': {'wert': sum(zs)}, 'c': '+'.join(map(str, zs)),
                    'w': f'Tausche so, dass 100 entsteht: {x} + {y} = 100. Dann 100 + {z} = {100 + z}.', 'h': 'Welche zwei Zahlen ergeben zusammen 100?'}
        p, q = R.choice([(25, 4), (5, 20), (2, 50), (5, 2), (4, 5)]); z = R.randint(3, 19)
        return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {p} · {z} · {q}'}, 'o': {'wert': p * q * z}, 'c': f'{p}*{z}*{q}',
                'w': f'Tausche: {p} · {q} = {p * q}. Dann {p * q} · {z} = {zt(p * q * z)}.', 'h': 'Welche zwei Faktoren ergeben eine glatte Zahl?'}
    if s == 2:
        if R.random() < .5:
            x = R.randint(101, 899); y = 1000 - x; u = R.randint(11, 89); v = 100 - u
            zs = [x, u, y, v]
            return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {zs[0]} + {zs[1]} + {zs[2]} + {zs[3]}'}, 'o': {'wert': 1100}, 'c': '+'.join(map(str, zs)),
                    'w': f'Passende Paare: {x} + {y} = 1 000 und {u} + {v} = 100. Zusammen 1 100.', 'h': 'Suche Paare, die 100 oder 1 000 ergeben.'}
        p, q = R.choice([(125, 8), (25, 4), (50, 20), (250, 4), (5, 200)]); z = R.randint(7, 39)
        return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {p} · {z} · {q}'}, 'o': {'wert': p * q * z}, 'c': f'{p}*{z}*{q}',
                'w': f'Tausche: {p} · {q} = {zt(p * q)}. Dann {zt(p * q)} · {z} = {zt(p * q * z)}.', 'h': 'Welche zwei Faktoren ergeben 100 oder 1 000?'}
    if R.random() < .5:
        x, y = R.randint(20, 90), R.randint(2, 15)
        aw, i = mische(R, f'{x} − {y} = {y} − {x}', [f'{x} + {y} = {y} + {x}', f'{x} · {y} = {y} · {x}', f'({x} + {y}) + 5 = {x} + ({y} + 5)'])
        return {'y': 'auswahl', 'f': {'text': 'Welche Gleichung ist falsch?'}, 'a': aw, 'o': {'index': i},
                'w': f'Tauschen darf man nur bei Plus und Mal. {x} − {y} = {x - y}, aber {y} − {x} = {zt(y - x)}.', 'h': 'Bei welcher Rechenart darf man nicht tauschen?'}
    p, q = R.choice([(25, 4), (125, 8), (5, 20)]); k, m = R.randint(2, 9), R.randint(2, 9)
    return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {p * k} · {q * m}'}, 'o': {'wert': p * k * q * m}, 'c': f'{p * k}*{q * m}',
            'w': f'Zerlege: {p * k} = {p} · {k} und {q * m} = {q} · {m}. Dann {p} · {q} = {zt(p * q)} und {k} · {m} = {k * m}. Ergebnis {zt(p * q)} · {k * m} = {zt(p * q * k * m)}.',
            'h': f'Zerlege die Faktoren so, dass {p} · {q} entsteht.'}


def g_verteilen(s):
    k = R.randint(3, 9)
    if s == 1:
        d = R.choice([1, 2, 3]); base = R.choice([100, 50, 20, 30, 40]); plus = R.random() < .4
        n = base + d if plus else base - d
        return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {k} · {n}'}, 'o': {'wert': k * n}, 'c': f'{k}*{n}',
                'w': f'{k} · {n} = {k} · ({base} {"+" if plus else "−"} {d}) = {k * base} {"+" if plus else "−"} {k * d} = {k * n}.', 'h': f'Zerlege {n} in eine glatte Zahl plus oder minus einen kleinen Rest.'}
    if s == 2:
        if R.random() < .5:
            x = R.randint(11, 89); y = R.choice([100, 50, 20]) - x
            if y < 2: return g_verteilen(s)
            return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {k} · {x} + {k} · {y}'}, 'o': {'wert': k * (x + y)}, 'c': f'{k}*{x}+{k}*{y}',
                    'w': f'Gemeinsamer Faktor {k}: {k} · ({x} + {y}) = {k} · {x + y} = {k * (x + y)}.', 'h': 'Welcher Faktor kommt in beiden Produkten vor? Klammere ihn aus.'}
        d = R.randint(1, 4); base = R.choice([200, 300, 500, 1000]); n = base - d; k2 = R.randint(6, 12)
        return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {k2} · {n}'}, 'o': {'wert': k2 * n}, 'c': f'{k2}*{n}',
                'w': f'{k2} · {n} = {k2} · ({zt(base)} − {d}) = {zt(k2 * base)} − {k2 * d} = {zt(k2 * n)}.', 'h': f'{n} ist fast {base}.'}
    if R.random() < .5:
        x, y = R.randint(2, 9), R.randint(10, 60)
        aw, i = mische(R, f'{k} · {y} + {k} · {x}', [f'{k} · {y} + {x}', f'{k} + {y} · {k} + {x}', f'{k} · {y} · {x}'])
        return {'y': 'auswahl', 'f': {'text': f'Welcher Term ist gleich {k} · ({y} + {x})?'}, 'a': aw, 'o': {'index': i},
                'w': f'Jeder Teil der Klammer wird mal {k} genommen: {k} · {y} + {k} · {x} = {k * y} + {k * x} = {k * (x + y)}.', 'h': 'Der Faktor vor der Klammer gehört zu jedem Teil der Klammer.'}
    x = R.randint(101, 199); y = x - 100; k2 = R.randint(12, 48)
    return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {k2} · {x} − {k2} · {y}'}, 'o': {'wert': k2 * 100}, 'c': f'{k2}*{x}-{k2}*{y}',
            'w': f'Gemeinsamer Faktor {k2}: {k2} · ({x} − {y}) = {k2} · 100 = {zt(k2 * 100)}.', 'h': 'Klammere den gemeinsamen Faktor aus.'}


def _vz(a, b): return 'Gleiche Vorzeichen, also plus' if (a < 0) == (b < 0) else 'Verschiedene Vorzeichen, also minus'


def g_mal_ganz(s):
    g = {1: 10, 2: 15, 3: 30}[s]
    a, b = R.choice([-1, 1]) * R.randint(2, g), R.choice([-1, 1]) * R.randint(2, g)
    if a > 0 and b > 0: return g_mal_ganz(s)
    if s == 3 and R.random() < .5:
        c = -R.randint(2, 6); a, b = R.choice([-1, 1]) * R.randint(2, 9), R.choice([-1, 1]) * R.randint(2, 9)
        neg = sum(x < 0 for x in (a, b, c))
        return {'y': 'zahl', 'f': {'text': f'Berechne {kl(a)} · {kl(b)} · {kl(c)}.'}, 'o': {'wert': a * b * c}, 'c': f'({a})*({b})*({c})',
                'w': f'Beträge: {abs(a)} · {abs(b)} · {abs(c)} = {abs(a * b * c)}. {neg} negative {"Faktor" if neg == 1 else "Faktoren"}: {"gerade Anzahl, also plus" if neg % 2 == 0 else "ungerade Anzahl, also minus"}. Ergebnis {zt(a * b * c)}.',
                'h': 'Zähle die negativen Faktoren: gerade Anzahl ergibt plus, ungerade minus.'}
    return {'y': 'zahl', 'f': {'text': f'Berechne {kl(a)} · {kl(b)}.'}, 'o': {'wert': a * b}, 'c': f'({a})*({b})',
            'w': f'Beträge: {abs(a)} · {abs(b)} = {abs(a * b)}. {_vz(a, b)}: {zt(a * b)}.', 'h': 'Erst die Beträge multiplizieren, dann das Vorzeichen bestimmen.'}


def g_geteilt_ganz(s):
    g = {1: 10, 2: 12, 3: 25}[s]
    q, b = R.choice([-1, 1]) * R.randint(2, g), R.choice([-1, 1]) * R.randint(2, g if s < 3 else 12)
    a = q * b
    if a > 0 and b > 0: return g_geteilt_ganz(s)
    if s == 3 and R.random() < .4:
        c = R.choice([-1, 1]) * R.randint(2, 6)
        return {'y': 'zahl', 'f': {'text': f'Berechne {kl(a * c)} : {kl(b)} : {kl(c)}.'}, 'o': {'wert': q}, 'c': f'({a * c})/({b})/({c})',
                'w': f'Von links nach rechts: {kl(a * c)} : {kl(b)} = {zt(q * c)}. Dann {kl(q * c)} : {kl(c)} = {zt(q)}.', 'h': 'Rechne von links nach rechts und bestimme bei jedem Schritt das Vorzeichen.'}
    return {'y': 'zahl', 'f': {'text': f'Berechne {kl(a)} : {kl(b)}.'}, 'o': {'wert': q}, 'c': f'({a})/({b})',
            'w': f'Beträge: {abs(a)} : {abs(b)} = {abs(q)}. {_vz(a, b)}: {zt(q)}.', 'h': 'Erst die Beträge dividieren, dann das Vorzeichen bestimmen.'}


def _rund1(n):
    st = 10 ** (len(str(n)) - 1)
    return int((n + st / 2) // st * st)


def g_ueberschlag(s):
    if s == 1:
        a, b = R.randint(110, 980), R.randint(110, 980)
        if abs(a % 100 - 50) < 8 or abs(b % 100 - 50) < 8: return g_ueberschlag(s)
        ra, rb = _rund1(a), _rund1(b)
        return {'y': 'zahl', 'f': {'text': f'Überschlage {a} + {b}. Runde dazu beide Zahlen auf Hunderter und addiere.'}, 'o': {'wert': ra + rb}, 'c': f'{ra}+{rb}',
                'w': f'{a} ≈ {zt(ra)} und {b} ≈ {zt(rb)}. Überschlag: {zt(ra)} + {zt(rb)} = {zt(ra + rb)}. (Genau: {zt(a + b)})', 'h': 'Runde jede Zahl auf Hunderter: Schau auf die Zehnerziffer.'}
    if s == 2:
        a, b = R.randint(110, 980), R.randint(12, 88)
        if abs(a % 100 - 50) < 8 or abs(b % 10 - 5) < 1: return g_ueberschlag(s)
        ra, rb = _rund1(a), _rund1(b)
        return {'y': 'zahl', 'f': {'text': f'Überschlage {a} · {b}. Runde dazu den ersten Faktor auf Hunderter, den zweiten auf Zehner und multipliziere.'}, 'o': {'wert': ra * rb}, 'c': f'{ra}*{rb}',
                'w': f'{a} ≈ {ra} und {b} ≈ {rb}. Überschlag: {zt(ra)} · {rb} = {zt(ra * rb)}. (Genau: {zt(a * b)})', 'h': 'Runde beide Faktoren, dann rechne im Kopf: erst die Ziffern, dann die Nullen anhängen.'}
    a, b = R.randint(210, 980), R.randint(21, 88)
    if abs(a % 100 - 50) < 10 or abs(b % 10 - 5) < 2: return g_ueberschlag(s)
    genau = a * b
    f1 = genau // 10 + R.randint(1, 9); f2 = genau * 10 + R.randint(1, 9) * 10; f3 = _rund1(a) * _rund1(b) * 2 + a
    aw, i = mische(R, zt(genau), [zt(f1), zt(f2), zt(f3)])
    return {'y': 'auswahl', 'f': {'text': f'Nur ein Ergebnis kann stimmen. Entscheide mit einem Überschlag: {a} · {b} = ?'}, 'a': aw, 'o': {'index': i},
            'w': f'Überschlag: {_rund1(a)} · {_rund1(b)} = {zt(_rund1(a) * _rund1(b))}. Nur {zt(genau)} liegt in dieser Größenordnung.', 'h': 'Runde beide Faktoren und rechne im Kopf. Welches Ergebnis liegt in der Nähe?'}


def g_schriftlich(s):
    if s == 1:
        a, b = R.randint(123, 987), R.randint(3, 9)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Rechne schriftlich: {a} · {b}'}, 'o': {'wert': a * b}, 'c': f'{a}*{b}',
                    'w': f'Stellenweise: {a // 100 * 100} · {b} = {a // 100 * 100 * b}, {a // 10 % 10 * 10} · {b} = {a // 10 % 10 * 10 * b}, {a % 10} · {b} = {a % 10 * b}. Summe: {zt(a * b)}.',
                    'h': 'Multipliziere Einer, Zehner und Hunderter einzeln mit dem Faktor und denke an die Überträge.'}
        return {'y': 'zahl', 'f': {'text': f'Rechne schriftlich: {zt(a * b)} : {b}'}, 'o': {'wert': a}, 'c': f'{a * b}/{b}',
                'w': f'Probe durch Malnehmen: {a} · {b} = {zt(a * b)}. Also {zt(a * b)} : {b} = {a}.', 'h': 'Teile von links Ziffer für Ziffer. Prüfe am Ende mit der Umkehrrechnung.'}
    if s == 2:
        a, b = R.randint(123, 987), R.randint(12, 98)
        if b % 10 == 0: return g_schriftlich(s)
        if R.random() < .55:
            return {'y': 'zahl', 'f': {'text': f'Rechne schriftlich: {a} · {b}'}, 'o': {'wert': a * b}, 'c': f'{a}*{b}',
                    'w': f'Teilprodukte: {a} · {b // 10 * 10} = {zt(a * (b // 10 * 10))} und {a} · {b % 10} = {zt(a * (b % 10))}. Summe: {zt(a * b)}. Überschlag: {_rund1(a)} · {_rund1(b)} = {zt(_rund1(a) * _rund1(b))}.',
                    'h': 'Zwei Teilprodukte: erst mit den Zehnern (eine Stelle versetzt), dann mit den Einern. Dann addieren.'}
        d = R.randint(11, 25); q = R.randint(23, 98)
        return {'y': 'zahl', 'f': {'text': f'Rechne schriftlich: {zt(q * d)} : {d}'}, 'o': {'wert': q}, 'c': f'{q * d}/{d}',
                'w': f'Probe durch Malnehmen: {q} · {d} = {zt(q * d)}. Also {zt(q * d)} : {d} = {q}.', 'h': f'Schreibe dir zuerst die {d}er-Reihe bis {d} · 9 auf.'}
    if R.random() < .5:
        a, b = R.randint(1234, 9876), R.randint(123, 987)
        if b % 10 == 0 or b // 10 % 10 == 0: return g_schriftlich(s)
        return {'y': 'zahl', 'f': {'text': f'Rechne schriftlich: {zt(a)} · {b}'}, 'o': {'wert': a * b}, 'c': f'{a}*{b}',
                'w': f'Teilprodukte: {zt(a)} · {b // 100 * 100} = {zt(a * (b // 100 * 100))}, {zt(a)} · {b // 10 % 10 * 10} = {zt(a * (b // 10 % 10 * 10))}, {zt(a)} · {b % 10} = {zt(a * (b % 10))}. Summe: {zt(a * b)}.',
                'h': 'Drei Teilprodukte stellengerecht untereinander, dann addieren. Mache vorher einen Überschlag.'}
    d = R.randint(26, 97); q = R.randint(123, 987)
    return {'y': 'zahl', 'f': {'text': f'Rechne schriftlich: {zt(q * d)} : {d}'}, 'o': {'wert': q}, 'c': f'{q * d}/{d}',
            'w': f'Probe durch Malnehmen: {q} · {d} = {zt(q * d)}. Also {zt(q * d)} : {d} = {q}.', 'h': f'Überschlage zuerst: Wie oft passt {_rund1(d)} ungefähr hinein?'}


NAME = {'+': 'Summe', '-': 'Differenz', '*': 'Produkt', ':': 'Quotient'}


def g_termaufbau(s):
    a, b, c = R.randint(2, 12), R.randint(2, 12), R.randint(2, 12)
    if s == 1:
        op = R.choice('+-*:')
        x, y = (a * b, b) if op == ':' else ((a + b, b) if op == '-' else (a, b))
        text = f'{x} {dict(zip("+-*:", "+−·:"))[op]} {y}'
        aw, i = mische(R, NAME[op], [n for n in NAME.values() if n != NAME[op]])
        return {'y': 'auswahl', 'f': {'text': f'Wie heißt der Term {text}?'}, 'a': aw, 'o': {'index': i},
                'w': f'Plus: Summe. Minus: Differenz. Mal: Produkt. Geteilt: Quotient. {text} ist {"eine" if op != ":" and op != "*" else "ein"} {NAME[op]}.', 'h': 'Welche Rechenart steht da?'}
    if s == 2:
        form = R.choice(['sp', 'ps', 'dp', 'pd'])
        if form == 'sp': text, n, erkl = f'{a} + {b} · {c}', 'Summe', f'zuerst {b} · {c}, zuletzt das Plus'
        elif form == 'ps': text, n, erkl = f'({a} + {b}) · {c}', 'Produkt', 'zuerst die Klammer, zuletzt das Mal'
        elif form == 'dp': text, n, erkl = f'{a * b + c} − {a} · {b}', 'Differenz', f'zuerst {a} · {b}, zuletzt das Minus'
        else: text, n, erkl = f'({a + b} − {b}) · {c}', 'Produkt', 'zuerst die Klammer, zuletzt das Mal'
        aw, i = mische(R, n, [x for x in NAME.values() if x != n])
        return {'y': 'auswahl', 'f': {'text': f'Welche Art von Term ist {text}?'}, 'a': aw, 'o': {'index': i},
                'w': f'Reihenfolge: {erkl}. Die letzte Rechnung gibt den Namen: {n}.', 'h': 'Welche Rechnung führst du als letzte aus?'}
    form = R.choice(['a', 'b', 'c', 'd'])
    if form == 'a': satz, r, f = f'Addiere {a} zum Produkt aus {b} und {c}.', f'{b} · {c} + {a}', [f'({a} + {b}) · {c}', f'{a} · {b} + {c}']
    elif form == 'b': satz, r, f = f'Multipliziere die Summe aus {a} und {b} mit {c}.', f'({a} + {b}) · {c}', [f'{a} + {b} · {c}', f'{a} · {b} + {c}']
    elif form == 'c': satz, r, f = f'Subtrahiere das Produkt aus {a} und {b} von {a * b + c}.', f'{a * b + c} − {a} · {b}', [f'{a} · {b} − {a * b + c}', f'({a * b + c} − {a}) · {b}']
    else: satz, r, f = f'Dividiere die Differenz aus {a * c + b * c} und {b * c} durch {c}.', f'({a * c + b * c} − {b * c}) : {c}', [f'{a * c + b * c} − {b * c} : {c}', f'{c} : ({a * c + b * c} − {b * c})']
    aw, i = mische(R, r, f)
    return {'y': 'auswahl', 'f': {'text': f'Welcher Term passt? „{satz}“'}, 'a': aw, 'o': {'index': i},
            'w': f'Der Satz beschreibt die letzte Rechnung zuerst. Was zuerst gerechnet werden muss, steht als Produkt oder in einer Klammer: {r}.',
            'h': 'Überlege, was zuerst ausgerechnet werden muss. Das braucht Vorrang (Punktrechnung oder Klammer).'}


GEN = {'punkt_strich': g_punkt_strich, 'klammern': g_klammern, 'vorteil': g_vorteil, 'verteilen': g_verteilen, 'mal_ganz': g_mal_ganz,
       'geteilt_ganz': g_geteilt_ganz, 'ueberschlag': g_ueberschlag, 'schriftlich': g_schriftlich, 'termaufbau': g_termaufbau}
DATEI = {
    'thema_schluessel': 'zahlen.rechengesetze', 'thema_id': 18, 'block_id': 49, 'klasse': {'gym_by': 5, 'rs_by': 5, 'ib_myp': 1},
    'autor': 'Claude (Generator zahlen_rechengesetze.py)',
    'inhalt': {
        'ziel': 'Terme in der richtigen Reihenfolge berechnen, Rechengesetze für Rechenvorteile nutzen, ganze Zahlen multiplizieren und dividieren, überschlagen und schriftlich rechnen.',
        'merke': ['Klammer vor Punkt vor Strich.', 'Tauschen und verbinden: nur bei plus und mal.', 'Verteilen: Der Faktor gehört zu jedem Teil der Klammer.',
                  'Mal und geteilt: gleiche Vorzeichen plus, verschiedene minus.', 'Erst überschlagen, dann genau rechnen.'],
        'abschnitte': [{'titel': 'Reihenfolge beim Rechnen', 'lernziele': ['punkt_strich', 'klammern', 'termaufbau']},
                       {'titel': 'Geschickt rechnen', 'lernziele': ['vorteil', 'verteilen']},
                       {'titel': 'Mal und geteilt mit ganzen Zahlen', 'lernziele': ['mal_ganz', 'geteilt_ganz']},
                       {'titel': 'Große Rechnungen', 'lernziele': ['ueberschlag', 'schriftlich']}],
        'etappen': ETAPPEN,
        'teilfaehigkeiten': [{'k': 'vorrang', 'text': 'Vorrangregeln und Klammern', 'lernziele': ['punkt_strich', 'klammern']},
                             {'k': 'gesetze', 'text': 'Rechengesetze für Rechenvorteile', 'lernziele': ['vorteil', 'verteilen']},
                             {'k': 'ganz', 'text': 'Multiplikation und Division ganzer Zahlen', 'lernziele': ['mal_ganz', 'geteilt_ganz']},
                             {'k': 'verfahren', 'text': 'Überschlag und schriftliche Verfahren', 'lernziele': ['ueberschlag', 'schriftlich']},
                             {'k': 'terme', 'text': 'Termstrukturen erkennen', 'lernziele': ['termaufbau']}],
        'bewertung': {'lernziele_pflicht': [e['lernziel'] for e in ETAPPEN], 'lernziele_vertiefung': [], 'testaufgaben_je_lernziel': 1, 'hilfen_im_test': False},
        'quellen': {'erklaerungen': 'Eigene Fassung (Claude).', 'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern, Gymnasium Mathematik 5.'},
    },
    'aufgaben': baue(R, ETAPPEN, GEN, TEIL, je_stufe=5),
}

if __name__ == '__main__':
    schreibe(DATEI, 'zahlen.rechengesetze.json')
