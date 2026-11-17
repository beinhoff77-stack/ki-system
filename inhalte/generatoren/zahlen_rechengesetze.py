#!/usr/bin/env python3
"""Grundrechenarten und Rechengesetze (Gymnasium Kl. 5): Vorrangregeln, Klammern, Rechenvorteile (Vertauschen,
Verbinden, Verteilen), Multiplikation/Division ganzer Zahlen, Überschlag, schriftliches Rechnen, Termaufbau."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl5 import baue, kl, mische, mische_rund, schreibe, zt
from _bausatz import rechne  # noqa: E402

R = random.Random(18)

# Erklärungen: Fassung der Prüfung (inhalte/pruefung/erklaerungen/zahlen.rechengesetze.json) übernommen,
# termaufbau hinter klammern gesetzt, neue Karte differenz_summe hinter vorteil.
ETAPPEN = [
    {
        "lernziel": "punkt_strich",
        "titel": "Punkt vor Strich",
        "regel": "⟦Punktrechnung⟧ (mal und geteilt) kommt vor ⟦Strichrechnung⟧ (plus und minus). Gleichrangiges wird von links nach rechts gerechnet.",
        "schritte": [
            "Du kaufst eine Tüte Popcorn für 3 € und 4 Kinokarten zu je 5 €: 3 + 4 · 5.",
            "Zuerst der Punkt: 4 Karten kosten 4 · 5 = 20 €.",
            "Dann der Strich: 3 + 20 = ⟦23⟧ €."
        ],
        "fehler": "Einfach von links nach rechts: 3 + 4 = 7, 7 · 5 = 35 ist falsch. Das wären 7 Kinokarten – du hast aber nur 4 gekauft. Erst ⟦4 · 5⟧, dann plus 3."
    },
    {
        "lernziel": "klammern",
        "titel": "Klammern zuerst",
        "regel": "Was in ⟦Klammern⟧ steht, wird zuerst ausgerechnet. Bei Klammern in Klammern beginnst du ⟦innen⟧. Danach gilt Punkt vor Strich.",
        "schritte": [
            "(3 + 4) · 5: zuerst die Klammer, 3 + 4 = 7. Dann 7 · 5 = ⟦35⟧.",
            "Klammer in Klammer: 2 · (10 − (3 + 4)). Innen zuerst: 3 + 4 = 7.",
            "Dann die äußere Klammer: 10 − 7 = 3. Zum Schluss 2 · 3 = ⟦6⟧."
        ],
        "probe": "Ohne Klammer wäre 3 + 4 · 5 = 23. Die Klammer ändert das Ergebnis.",
        "fehler": "Die Klammer übersehen und Punkt vor Strich rechnen: (3 + 4) · 5 = 3 + 20 = 23 ist falsch. Die Klammer sagt: Erst ⟦3 + 4⟧ ausrechnen, dann mal 5. Richtig ist 35."
    },
    {
        "lernziel": "termaufbau",
        "titel": "Terme lesen und aufstellen",
        "regel": "Die Rechenart, die du ⟦zuletzt⟧ ausführst, gibt dem Term den Namen: Summe (+), Differenz (−), Produkt (·), Quotient (:).",
        "schritte": [
            "3 + 4 · 5: zuletzt wird addiert.",
            "Der Term ist eine ⟦Summe⟧ aus 3 und dem Produkt von 4 und 5."
        ],
        "fehler": "3 + 4 · 5 „Produkt“ nennen, weil ein Malpunkt vorkommt. Entscheidend ist die ⟦letzte⟧ Rechnung, hier das Plus."
    },
    {
        "lernziel": "vorteil",
        "titel": "Geschickt: tauschen und verbinden",
        "regel": "Bei ⟦plus⟧ und bei ⟦mal⟧ darfst du die Reihenfolge ändern und Zahlen beliebig zusammenfassen. Suche Paare, die glatte Zahlen ergeben: 25 · 4 = 100, 37 + 63 = 100.",
        "schritte": [
            "25 · 7 · 4: tausche zu 25 · 4 · 7.",
            "25 · 4 = 100, dann 100 · 7 = ⟦700⟧."
        ],
        "fehler": "Auch bei Minus oder Geteilt tauschen: 10 − 3 ist nicht 3 − 10. Tauschen geht nur bei ⟦plus und mal⟧."
    },
    {
        "lernziel": "differenz_summe",
        "titel": "Das Minus wandert mit",
        "regel": "Jede Differenz ist eine Summe: 47 − 18 = 47 + (−18). Das Rechenzeichen ⟦gehört zur Zahl dahinter⟧. Wenn du Zahlen tauschst, nimmst du ihr Zeichen ⟦mit⟧.",
        "schritte": [
            "Du hast 47 € und gibst 18 € aus. Dann bekommst du 13 € geschenkt: 47 − 18 + 13.",
            "Tausche die +13 nach vorn, das Minus bleibt bei der 18: 47 + 13 − 18.",
            "47 + 13 = 60, und 60 − 18 = ⟦42⟧ €."
        ],
        "probe": "Von links nach rechts: 47 − 18 = 29, 29 + 13 = 42 ✓",
        "fehler": "47 − 18 + 13 = 47 − 31 = 16 ist falsch. Du hast die 13 mit unter das Minus gezogen. Die 13 bekommst du aber ⟦dazu⟧, du gibst sie nicht aus."
    },
    {
        "lernziel": "verteilen",
        "titel": "Geschickt: verteilen",
        "regel": "Eine Zahl mal eine Klammer: mit ⟦jedem⟧ Teil der Klammer malnehmen. 7 · (100 − 2) = 7 · 100 − 7 · 2. Rückwärts: gemeinsamen Faktor ⟦ausklammern⟧, 6 · 13 + 6 · 7 = 6 · (13 + 7) = 6 · 20.",
        "schritte": [
            "Ein Verein kauft 7 Sporttaschen zu je 98 €: 7 · 98 = 7 · (100 − 2).",
            "Stell dir vor, jede Tasche kostet 100 €: 7 · 100 = 700 €. Aber jede Tasche ist 2 € billiger, das sind 7 · 2 = 14 € zu viel.",
            "700 − 14 = ⟦686⟧ €."
        ],
        "fehler": "Nur den ersten Teil malnehmen: 7 · (100 − 2) = 700 − 2 ist falsch. Jede der ⟦7⟧ Taschen ist 2 € billiger, also ziehst du 7 · 2 = 14 ab, nicht nur 2."
    },
    {
        "lernziel": "mal_ganz",
        "titel": "Ganze Zahlen multiplizieren",
        "regel": "Rechne mit den Beträgen. Dann das Vorzeichen: ⟦gleiche⟧ Vorzeichen ergeben plus, ⟦verschiedene⟧ Vorzeichen ergeben minus.",
        "schritte": [
            "Von deinem Konto werden 4-mal je 6 € abgebucht: 4 · (−6) = (−6) + (−6) + (−6) + (−6) = ⟦−24⟧.",
            "Warum ist Minus mal Minus plus? Schau auf die Reihe: (−6) · 2 = −12, (−6) · 1 = −6, (−6) · 0 = 0.",
            "Bei jedem Schritt wird das Ergebnis um 6 größer. Also geht es so weiter: (−6) · (−1) = ⟦6⟧, (−6) · (−2) = ⟦12⟧."
        ],
        "probe": "(−6) + (−6) + (−6) + (−6) = −24 ✓",
        "fehler": "(−6) · (−4) = −24 ist falsch: Zwei gleiche Vorzeichen ergeben ⟦Plus⟧, also 24. Aber Achtung: Die Regel gilt nur für mal und geteilt. Beim Addieren ist (−6) + (−4) = −10."
    },
    {
        "lernziel": "geteilt_ganz",
        "titel": "Ganze Zahlen dividieren",
        "regel": "Beim Dividieren gelten dieselben Vorzeichenregeln wie beim Multiplizieren: ⟦gleich → plus⟧, ⟦verschieden → minus⟧.",
        "schritte": [
            "(−48) : 6: Beträge 48 : 6 = 8.",
            "Verschiedene Vorzeichen, also ⟦−8⟧."
        ],
        "probe": "(−8) · 6 = −48 ✓",
        "fehler": "(−48) : (−6) = −8 ist falsch: Minus geteilt durch Minus ergibt ⟦Plus⟧, also 8."
    },
    {
        "lernziel": "ueberschlag",
        "titel": "Überschlagen",
        "regel": "Beim Überschlag rundest du jede Zahl so, dass du ⟦im Kopf⟧ rechnen kannst. So prüfst du, ob ein Ergebnis stimmen kann.",
        "schritte": [
            "487 · 21: runde zu 500 · 20.",
            "500 · 20 = ⟦10 000⟧. Das genaue Ergebnis 10 227 liegt in der Nähe."
        ],
        "fehler": "Ein Ergebnis wie 1 022 hinschreiben, ohne zu prüfen: Der Überschlag 10 000 zeigt, dass eine ⟦Stelle fehlt⟧."
    },
    {
        "lernziel": "schriftlich",
        "titel": "Schriftlich mal und geteilt",
        "regel": "Schriftlich multiplizieren: mit jeder Ziffer des zweiten Faktors einzeln malnehmen, ⟦stellengerecht⟧ untereinander schreiben, addieren. Schriftlich dividieren: teilen, malnehmen, abziehen, nächste Ziffer herunterholen.",
        "schritte": [
            "Mal: 347 · 26. Rechne 347 · 20 = 6 940 und 347 · 6 = 2 082. Zusammen ⟦9 022⟧. Überschlag: 350 · 25 = 8 750, passt ✓",
            "Geteilt: 1 476 : 6. Die 1 allein geht nicht, also 14 : 6 = 2, denn 2 · 6 = 12. Rest 14 − 12 = 2.",
            "Die 7 herunterholen: 27 : 6 = 4, denn 4 · 6 = 24. Rest 3.",
            "Die 6 herunterholen: 36 : 6 = 6, Rest 0. Ergebnis: ⟦246⟧."
        ],
        "fehler": "Beim Malnehmen das Teilprodukt mit der Zehnerziffer nicht um eine Stelle versetzen: 347 · 2 Zehner sind ⟦6 940⟧, nicht 694. Beim Teilen eine Null im Ergebnis vergessen: 1 236 : 6 ist 206, nicht 26 – wenn die heruntergeholte Ziffer nicht reicht, schreibst du ⟦0⟧ ins Ergebnis.",
        "probe": "246 · 6 = 1 476 ✓"
    }
]
TEIL = {'differenz_summe': 'gesetze', 'punkt_strich': 'vorrang', 'klammern': 'vorrang', 'vorteil': 'gesetze', 'verteilen': 'gesetze', 'mal_ganz': 'ganz', 'geteilt_ganz': 'ganz',
        'ueberschlag': 'verfahren', 'schriftlich': 'verfahren', 'termaufbau': 'terme'}


def _ps_rechnen(s):
    a, b, c, d = (R.randint(2, 12) for _ in range(4))
    if s == 1:
        op = R.choice('+-')
        if op == '-': a = b * c + a
        vorn = R.random() < .5
        text = f'{a} {"+" if op == "+" else "−"} {b} · {c}' if vorn else (f'{b} · {c} {"+" if op == "+" else "−"} {a}' if op == '+' or b * c > a else None)
        if text is None: return _ps_rechnen(s)
        e = a + b * c if op == '+' else (a - b * c if vorn else b * c - a)
        return {'y': 'zahl', 'f': {'text': f'Berechne {text}.'}, 'o': {'wert': e}, 'c': text.replace('·', '*').replace('−', '-'),
                'w': f'Punkt vor Strich: zuerst {b} · {c} = {b * c}. Dann {text.replace(f"{b} · {c}", str(b * c))} = {e}.', 'h': 'Suche zuerst die Mal- oder Geteilt-Rechnung.'}
    if s == 2:
        q = R.randint(2, 9)
        form = R.choice(['mm', 'dm', 'md'])
        if form == 'mm': text, e, zw = f'{a} · {b} + {c} · {d}', a * b + c * d, f'{a * b} + {c * d}'
        elif form == 'dm': text, e, zw = f'{a * q} : {q} + {c} · {d}', a + c * d, f'{a} + {c * d}'
        else:
            if a * b <= c: return _ps_rechnen(s)
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








def _vz(a, b): return 'Gleiche Vorzeichen, also plus' if (a < 0) == (b < 0) else 'Verschiedene Vorzeichen, also minus'






def _rund1(n):
    st = 10 ** (len(str(n)) - 1)
    return int((n + st / 2) // st * st)


def _ue_alt(s):
    if s == 1:
        a, b = R.randint(110, 980), R.randint(110, 980)
        if abs(a % 100 - 50) < 8 or abs(b % 100 - 50) < 8: return _ue_alt(s)
        ra, rb = _rund1(a), _rund1(b)
        return {'y': 'zahl', 'f': {'text': f'Überschlage {a} + {b}. Runde dazu beide Zahlen auf Hunderter und addiere.'}, 'o': {'wert': ra + rb}, 'c': f'{ra}+{rb}',
                'w': f'{a} ≈ {zt(ra)} und {b} ≈ {zt(rb)}. Überschlag: {zt(ra)} + {zt(rb)} = {zt(ra + rb)}. (Genau: {zt(a + b)})', 'h': 'Runde jede Zahl auf Hunderter: Schau auf die Zehnerziffer.'}
    if s == 2:
        a, b = R.randint(110, 980), R.randint(12, 88)
        if abs(a % 100 - 50) < 8 or abs(b % 10 - 5) < 1: return _ue_alt(s)
        ra, rb = _rund1(a), _rund1(b)
        return {'y': 'zahl', 'f': {'text': f'Überschlage {a} · {b}. Runde dazu den ersten Faktor auf Hunderter, den zweiten auf Zehner und multipliziere.'}, 'o': {'wert': ra * rb}, 'c': f'{ra}*{rb}',
                'w': f'{a} ≈ {ra} und {b} ≈ {rb}. Überschlag: {zt(ra)} · {rb} = {zt(ra * rb)}. (Genau: {zt(a * b)})', 'h': 'Runde beide Faktoren, dann rechne im Kopf: erst die Ziffern, dann die Nullen anhängen.'}
    a, b = R.randint(210, 980), R.randint(21, 88)
    if abs(a % 100 - 50) < 10 or abs(b % 10 - 5) < 2: return _ue_alt(s)
    genau = a * b
    f1 = genau // 10 + R.randint(1, 9); f2 = genau * 10 + R.randint(1, 9) * 10; f3 = _rund1(a) * _rund1(b) * 2 + a
    aw, i = mische(R, zt(genau), [zt(f1), zt(f2), zt(f3)])
    return {'y': 'auswahl', 'f': {'text': f'Nur ein Ergebnis kann stimmen. Entscheide mit einem Überschlag: {a} · {b} = ?'}, 'a': aw, 'o': {'index': i},
            'w': f'Überschlag: {_rund1(a)} · {_rund1(b)} = {zt(_rund1(a) * _rund1(b))}. Nur {zt(genau)} liegt in dieser Größenordnung.', 'h': 'Runde beide Faktoren und rechne im Kopf. Welches Ergebnis liegt in der Nähe?'}




NAME = {'+': 'Summe', '-': 'Differenz', '*': 'Produkt', ':': 'Quotient'}




# ---------- Prüfung eingearbeitet (inhalte/pruefung/aufgaben/zahlen.rechengesetze.json) ----------
def _py(t): return t.replace('·', '*').replace('−', '-').replace(':', '/').replace('[', '(').replace(']', ')')


def _rund(r, f): return mische_rund(R, r, f)


def _ps_fehler():
    if R.random() < .5:
        a, b, c = R.randint(5, 20), R.randint(2, 9), R.randint(2, 9)
        falsch, richtig = (a + b) * c, a + b * c
        text = f'Jemand rechnet {a} + {b} · {c} = {falsch}. Was ist falsch?'
        r = f'Zuerst {b} · {c} = {b * c}, dann {a} + {b * c} = {richtig}.'
        f = [f'{b} · {c} ist falsch ausgerechnet.', f'Nichts, {falsch} stimmt.']
    else:
        c, q = R.randint(2, 9), R.randint(2, 9)
        b = c * q; a = b + c * R.randint(2, 9)
        falsch, richtig = (a - b) // c, a - q
        text = f'Jemand rechnet {a} − {b} : {c} = {falsch}. Was ist falsch?'
        r = f'Zuerst {b} : {c} = {q}, dann {a} − {q} = {richtig}.'
        f = [f'{b} : {c} ist falsch ausgerechnet.', f'Nichts, {falsch} stimmt.']
    aw, i = _rund(r, f)
    return {'y': 'auswahl', 'f': {'text': text}, 'a': aw, 'o': {'index': i},
            'w': f'Das Kind hat einfach von links nach rechts gerechnet. Punkt vor Strich: {r}',
            'h': 'Welche Rechnung muss zuerst kommen?'}


def g_punkt_strich(s):
    if s == 3 and R.random() < .4: return _ps_fehler()
    return _ps_rechnen(s)


def _kl_welcher():
    a, b, c = R.randint(2, 12), R.randint(2, 12), R.randint(2, 12)
    r1, r2, r3 = (a + b) * c, a + b * c, a * b + c
    if len({r1, r2, r3}) < 3: return _kl_welcher()
    aw, i = _rund(f'({a} + {b}) · {c}', [f'{a} + {b} · {c}', f'{a} · {b} + {c}'])
    return {'y': 'auswahl', 'f': {'text': f'Bei welchem Term kommt {r1} heraus?'}, 'a': aw, 'o': {'index': i},
            'w': f'({a} + {b}) · {c} = {a + b} · {c} = {r1}. {a} + {b} · {c} = {r2} (Punkt vor Strich) und {a} · {b} + {c} = {r3}.',
            'h': 'Rechne jeden Term aus. Achte darauf, was die Klammer ändert.'}


def _kl_setzen():
    form = R.choice(['plus', 'minus', 'geteilt'])
    if form == 'plus':
        a, b, c = R.randint(2, 12), R.randint(2, 12), R.randint(2, 9)
        ziel, r, f1 = (a + b) * c, f'({a} + {b}) · {c}', f'{a} + ({b} · {c})'
        term = f'{a} + {b} · {c}'
    elif form == 'minus':
        a, c = R.randint(3, 9), R.randint(2, 9); b = c + R.randint(2, 9)
        ziel, r, f1 = a * (b - c), f'{a} · ({b} − {c})', f'({a} · {b}) − {c}'
        term = f'{a} · {b} − {c}'
    else:
        y, z = R.randint(2, 9), R.randint(2, 9); k = R.randint(2, 6); x = (y + z) * k * y
        ziel, r, f1 = x // (y + z), f'{x} : ({y} + {z})', f'({x} : {y}) + {z}'
        term = f'{x} : {y} + {z}'
    aw, i = _rund(r, [f1, 'Keine Klammer nötig'])
    return {'y': 'auswahl', 'f': {'text': f'Wo musst du Klammern setzen, damit {term} = {ziel} stimmt?'}, 'a': aw, 'o': {'index': i},
            'w': f'{r} = {ziel}. Ohne Klammer (oder mit Klammer um die Punktrechnung) kommt {rechne(_py(term))} heraus.',
            'h': 'Probiere aus: Was muss zuerst gerechnet werden, damit das Ergebnis passt?'}


def g_klammern(s):
    a, b, c, d = (R.randint(2, 12) for _ in range(4))
    if s == 1:
        form = R.choice(['p', 'm'])
        if form == 'p': text, e, zw = f'({a} + {b}) · {c}', (a + b) * c, f'{a + b} · {c}'
        else: text, e, zw = f'{c} · ({a + b} − {b})', c * a, f'{c} · {a}'
        return {'y': 'zahl', 'f': {'text': f'Berechne {text}.'}, 'o': {'wert': e}, 'c': _py(text), 'w': f'Zuerst die Klammer: {zw}. Ergebnis {e}.', 'h': 'Rechne zuerst aus, was in der Klammer steht.'}
    if s == 2:
        form = R.choice(['a', 'b', 'c'])
        if form == 'a': text, e, zw = f'({a} + {b}) · ({c + d} − {d})', (a + b) * c, f'{a + b} · {c}'
        elif form == 'b':
            dd = d if d < a * b else 1
            text, e, zw = f'{a * b + c} − ({a} · {b} − {dd})', c + dd, f'{a * b + c} − {a * b - dd}'
        else: text, e, zw = f'({a * c} + {b * c}) : {c} + {d}', a + b + d, f'{a * c + b * c} : {c} + {d} = {a + b} + {d}'
        return {'y': 'zahl', 'f': {'text': f'Berechne {text}.'}, 'o': {'wert': e}, 'c': _py(text), 'w': f'Zuerst die Klammern: {zw}. Ergebnis {e}.', 'h': 'Erst jede Klammer ausrechnen, dann Punkt vor Strich.'}
    art = R.choice(['innen', 'welcher', 'setzen'])
    if art == 'welcher': return _kl_welcher()
    if art == 'setzen': return _kl_setzen()
    m = min(d, b * c - 1)
    text = f'{a} · [{b * c + d} − ({b} · {c} − {m})]'
    inn = b * c - m; e = a * (b * c + d - inn)
    return {'y': 'zahl', 'f': {'text': f'Berechne {text}.'}, 'o': {'wert': e}, 'c': _py(text),
            'w': f'Von innen nach außen: runde Klammer {b} · {c} − {m} = {inn}. Eckige Klammer {b * c + d} − {inn} = {b * c + d - inn}. Dann {a} · {b * c + d - inn} = {e}.',
            'h': 'Beginne mit der innersten Klammer.'}


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
        p, q = R.choice([(125, 8), (25, 4), (50, 2), (250, 4), (5, 200)]); z = R.randint(7, 39)
        return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {p} · {z} · {q}'}, 'o': {'wert': p * q * z}, 'c': f'{p}*{z}*{q}',
                'w': f'Tausche: {p} · {q} = {zt(p * q)}. Dann {zt(p * q)} · {z} = {zt(p * q * z)}.', 'h': 'Welche zwei Faktoren ergeben 100 oder 1 000?'}
    art = R.choice(['falsch', 'warum', 'vier'])
    if art == 'falsch':
        x, y = R.randint(20, 90), R.randint(2, 15)
        aw, i = _rund(f'{x} − {y} = {y} − {x}', [f'{x} + {y} = {y} + {x}', f'{x} · {y} = {y} · {x}', f'({x} + {y}) + 5 = {x} + ({y} + 5)'])
        return {'y': 'auswahl', 'f': {'text': 'Welche Gleichung ist falsch?'}, 'a': aw, 'o': {'index': i},
                'w': f'Tauschen darf man nur bei Plus und Mal. {x} − {y} = {x - y}, aber {y} − {x} = {zt(y - x)}.', 'h': 'Bei welcher Rechenart darf man nicht tauschen?'}
    if art == 'warum':
        if R.random() < .5:
            x, y = R.randint(20, 90), R.randint(2, 15)
            text = f'Warum darf man {x} − {y} nicht zu {y} − {x} tauschen?'
            r = f'Weil {x - y} und {zt(y - x)} verschieden sind. Tauschen geht nur bei Plus und Mal.'
            f = ['Man darf es, das Ergebnis bleibt gleich.', f'Weil {y} kleiner ist als {x}.']
            w = f'{x} − {y} = {x - y}, aber {y} − {x} = {zt(y - x)}. Das Vertauschungsgesetz gilt nur für Plus und Mal.'
        else:
            y = R.randint(3, 9); x = y * R.randint(4, 12)
            text = f'Gilt {x} : {y} = {y} : {x}?'
            r = f'Nein: {x} : {y} = {x // y}, aber {y} : {x} ist kleiner als 1. Bei Geteilt darf man nicht tauschen.'
            f = ['Ja, bei Geteilt darf man tauschen wie bei Mal.', f'Ja, weil beide Male {x} und {y} vorkommen.']
            w = f'{x} : {y} = {x // y}. Teilt man {y} durch {x}, ist das weniger als 1. Das Vertauschungsgesetz gilt nur für Plus und Mal.'
        aw, i = _rund(r, f)
        return {'y': 'auswahl', 'f': {'text': text}, 'a': aw, 'o': {'index': i}, 'w': w, 'h': 'Rechne beide Seiten aus und vergleiche.'}
    p, q = R.choice([(25, 4), (125, 8), (50, 2), (20, 5)]); z1, z2 = R.randint(3, 9), R.randint(3, 13)
    zs = [p, z1, z2, q] if R.random() < .5 else [z1, p, z2, q]
    return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {" · ".join(map(str, zs))}'}, 'o': {'wert': p * q * z1 * z2}, 'c': '*'.join(map(str, zs)),
            'w': f'Tausche und verbinde: ({p} · {q}) · ({z1} · {z2}) = {zt(p * q)} · {z1 * z2} = {zt(p * q * z1 * z2)}.',
            'h': 'Welche zwei Faktoren ergeben zusammen eine glatte Zahl? Rechne die anderen beiden zusammen.'}


def _rundzahl(lo, hi):
    """Zwei Zahlen, deren Summe eine glatte Zehnerzahl ist."""
    a = R.randint(lo, hi)
    if a % 10 == 0: return _rundzahl(lo, hi)
    c = (10 - a % 10) + 10 * R.randint(0, 5)
    return a, c


def g_differenz_summe(s):
    if s == 1:
        a, c = _rundzahl(21, 89)
        b = R.randint(11, a - 1)
        if b in (a, c) or b % 10 == 0: return g_differenz_summe(s)
        return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {a} − {b} + {c}'}, 'o': {'wert': a - b + c}, 'c': f'{a}-{b}+{c}',
                'w': f'Das Plus gehört zur {c}, das Minus zur {b}. Tausche: {a} + {c} − {b} = {a + c} − {b} = {a - b + c}.',
                'h': 'Welche zwei Zahlen ergeben zusammen eine glatte Zahl? Das Rechenzeichen wandert mit.'}
    if s == 2:
        if R.random() < .5:
            c = R.randint(11, 49); a = 100 + c + 100 * R.randint(0, 2); b = R.randint(11, 89)
            if b == c: return g_differenz_summe(s)
            return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {a} − {b} − {c}'}, 'o': {'wert': a - b - c}, 'c': f'{a}-{b}-{c}',
                    'w': f'Tausche die beiden Minus-Zahlen: {a} − {c} − {b} = {a - c} − {b} = {a - b - c}.',
                    'h': 'Welche Minus-Zahl passt gut zur ersten Zahl?'}
        a, c = _rundzahl(31, 89); b = R.randint(11, 29)
        if b == c: return g_differenz_summe(s)
        r = f'{a} + {c} − {b}'
        f = [f'{a} − {c} + {b}', f'{a} − ({b} + {c})']
        if len({a - b + c, a - c + b, a - b - c}) < 3: return g_differenz_summe(s)
        aw, i = _rund(r, f)
        return {'y': 'auswahl', 'f': {'text': f'Welcher Term hat denselben Wert wie {a} − {b} + {c}?'}, 'a': aw, 'o': {'index': i},
                'w': f'Jede Zahl nimmt ihr Rechenzeichen mit: −{b} und +{c}. Also {a} + {c} − {b} = {a - b + c}. {a} − {c} + {b} = {zt(a - c + b)} und {a} − ({b} + {c}) = {zt(a - b - c)}.',
                'h': 'Welches Rechenzeichen gehört zu welcher Zahl?'}
    if R.random() < .5:
        a, c = _rundzahl(31, 89); b = R.randint(11, 29)
        if b == c or a - b - c < 0 or b + c == a: return g_differenz_summe(s)
        text = f'Jemand rechnet {a} − {b} + {c} = {a} − {b + c} = {a - b - c}. Was ist falsch?'
        r = f'Die {c} wird dazugezählt, nicht abgezogen. Richtig: {a} + {c} − {b} = {a - b + c}.'
        f = ['Nichts, das Ergebnis stimmt.', f'Man muss zuerst {a} − {b} rechnen, dann {a - b} − {c} = {a - b - c}.']
        aw, i = _rund(r, f)
        return {'y': 'auswahl', 'f': {'text': text}, 'a': aw, 'o': {'index': i},
                'w': f'Das Minus gehört nur zur {b}. Die {c} hat ein Plus. Richtig ist {a - b + c}.',
                'h': 'Welches Rechenzeichen steht vor der letzten Zahl?'}
    a, c = _rundzahl(21, 79); b, d = _rundzahl(11, 49)
    if len({a, b, c, d}) < 4 or a + c <= b + d: return g_differenz_summe(s)
    e = a - b + c - d
    return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {a} − {b} + {c} − {d}'}, 'o': {'wert': e}, 'c': f'{a}-{b}+{c}-{d}',
            'w': f'Plus-Zahlen zusammen: {a} + {c} = {a + c}. Minus-Zahlen zusammen: {b} + {d} = {b + d}. {a + c} − {b + d} = {e}.',
            'h': 'Sammle die Plus-Zahlen und die Minus-Zahlen. Jedes Zeichen wandert mit seiner Zahl.'}


def _ausklammern(gross):
    k = R.choice([x for x in (range(12, 49) if gross else range(3, 10)) if x not in (10, 20, 30, 40)])
    art = R.choice(['plus', 'plus', 'minus'])
    if art == 'plus':
        ziel = R.choice([100] if gross else [100, 50, 20]); x = R.randint(3 if ziel == 20 else 11, ziel - (3 if ziel == 20 else 11)); y = ziel - x
        rechts = gross and R.random() < .4
        text = f'{x} · {k} + {y} · {k}' if rechts else f'{k} · {x} + {k} · {y}'
        return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {text}'}, 'o': {'wert': k * ziel}, 'c': _py(text),
                'w': f'Gemeinsamer Faktor {k}: {k} · ({x} + {y}) = {k} · {ziel} = {zt(k * ziel)}.', 'h': 'Welcher Faktor kommt in beiden Produkten vor? Klammere ihn aus.'}
    diff = R.choice([10, 100]); y = R.randint(3, 99); x = y + diff
    text = f'{k} · {x} − {k} · {y}'
    return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {text}'}, 'o': {'wert': k * diff}, 'c': _py(text),
            'w': f'Gemeinsamer Faktor {k}: {k} · ({x} − {y}) = {k} · {diff} = {zt(k * diff)}.', 'h': 'Klammere den gemeinsamen Faktor aus.'}


def g_verteilen(s):
    k = R.randint(3, 9)
    if s == 1:
        d = R.choice([1, 2, 3]); base = R.choice([100, 50, 20, 30, 40]); plus = R.random() < .4
        n = base + d if plus else base - d
        return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {k} · {n}'}, 'o': {'wert': k * n}, 'c': f'{k}*{n}',
                'w': f'{k} · {n} = {k} · ({base} {"+" if plus else "−"} {d}) = {k * base} {"+" if plus else "−"} {k * d} = {k * n}.', 'h': f'Zerlege {n} in eine glatte Zahl plus oder minus einen kleinen Rest.'}
    if s == 2:
        if R.random() < .5: return _ausklammern(False)
        d = R.randint(1, 4); base = R.choice([200, 300, 500, 1000]); n = base - d; k2 = R.choice([6, 7, 8, 9, 11, 12])
        return {'y': 'zahl', 'f': {'text': f'Rechne geschickt: {k2} · {n}'}, 'o': {'wert': k2 * n}, 'c': f'{k2}*{n}',
                'w': f'{k2} · {n} = {k2} · ({zt(base)} − {d}) = {zt(k2 * base)} − {k2 * d} = {zt(k2 * n)}.', 'h': f'{n} ist fast {zt(base)}.'}
    if R.random() < .67: return _ausklammern(True)
    x, y = R.randint(2, 9), R.randint(10, 60)
    aw, i = _rund(f'{k} · {y} + {k} · {x}', [f'{k} · {y} + {x}', f'{k} + {y} · {k} + {x}', f'{k} · {y} · {x}'])
    return {'y': 'auswahl', 'f': {'text': f'Welcher Term ist gleich {k} · ({y} + {x})?'}, 'a': aw, 'o': {'index': i},
            'w': f'Jeder Teil der Klammer wird mal {k} genommen: {k} · {y} + {k} · {x} = {k * y} + {k * x} = {k * (x + y)}.', 'h': 'Der Faktor vor der Klammer gehört zu jedem Teil der Klammer.'}


def _mal_vorzeichen():
    zs = [R.choice([-1, 1]) * R.randint(1, 9) for _ in range(4)]
    neg = sum(z < 0 for z in zs)
    if neg < 2: return _mal_vorzeichen()
    e = 1
    for z in zs: e *= z
    r = 'positiv' if e > 0 else 'negativ'
    aw, i = _rund(r, ['negativ' if e > 0 else 'positiv', 'genau 0'])
    return {'y': 'auswahl', 'f': {'text': f'Ist {" · ".join(kl(z) for z in zs)} positiv oder negativ? Entscheide, ohne auszurechnen.'}, 'a': aw, 'o': {'index': i},
            'w': f'Es gibt {neg} negative Faktoren. {"Gerade Anzahl, also positiv" if neg % 2 == 0 else "Ungerade Anzahl, also negativ"} (Ergebnis {zt(e)}).',
            'h': 'Zähle die negativen Faktoren.'}


def _mal_umkehr():
    a, x = R.choice([-1, 1]) * R.randint(2, 9), R.choice([-1, 1]) * R.randint(2, 12)
    if a > 0 and x > 0: return _mal_umkehr()
    c = a * x
    text = f'{kl(a)} · □ = {zt(c)}' if R.random() < .5 else f'□ · {kl(a)} = {zt(c)}'
    return {'y': 'zahl', 'f': {'text': f'{text}. Welche Zahl gehört in das Kästchen?'}, 'o': {'wert': x}, 'c': f'({c})/({a})',
            'w': f'Umkehraufgabe: {zt(c)} : {kl(a)} = {zt(x)}. Probe: {kl(a)} · {kl(x)} = {zt(c)} ✓',
            'h': 'Rechne rückwärts mit Geteilt. Achte auf das Vorzeichen.'}


def g_mal_ganz(s):
    if s == 2 and R.random() < .25: return _mal_vorzeichen()
    if s == 3:
        art = R.choice(['drei', 'umkehr', 'vorzeichen'])
        if art == 'umkehr': return _mal_umkehr()
        if art == 'vorzeichen': return _mal_vorzeichen()
        c = -R.randint(2, 6); a, b = R.choice([-1, 1]) * R.randint(2, 9), R.choice([-1, 1]) * R.randint(2, 9)
        neg = sum(x < 0 for x in (a, b, c))
        return {'y': 'zahl', 'f': {'text': f'Berechne {kl(a)} · {kl(b)} · {kl(c)}.'}, 'o': {'wert': a * b * c}, 'c': f'({a})*({b})*({c})',
                'w': f'Beträge: {abs(a)} · {abs(b)} · {abs(c)} = {abs(a * b * c)}. {"1 negativer Faktor" if neg == 1 else f"{neg} negative Faktoren"}: {"gerade Anzahl, also plus" if neg % 2 == 0 else "ungerade Anzahl, also minus"}. Ergebnis {zt(a * b * c)}.',
                'h': 'Zähle die negativen Faktoren: gerade Anzahl ergibt plus, ungerade minus.'}
    g = {1: 10, 2: 15}[s]
    a, b = R.choice([-1, 1]) * R.randint(2, g), R.choice([-1, 1]) * R.randint(2, g)
    if a > 0 and b > 0: return g_mal_ganz(s)
    return {'y': 'zahl', 'f': {'text': f'Berechne {kl(a)} · {kl(b)}.'}, 'o': {'wert': a * b}, 'c': f'({a})*({b})',
            'w': f'Beträge: {abs(a)} · {abs(b)} = {abs(a * b)}. {_vz(a, b)}: {zt(a * b)}.', 'h': 'Erst die Beträge multiplizieren, dann das Vorzeichen bestimmen.'}


def _null():
    n = R.choice([-1, 1]) * R.randint(2, 20)
    if R.random() < .5:
        text, r, f = f'Was ergibt 0 : {kl(n)}?', '0', [zt(n), 'geht nicht']
        w = f'0 geteilt durch eine Zahl ist immer 0. Probe: 0 · {kl(n)} = 0 ✓'
    else:
        text, r, f = f'Was ergibt {kl(n)} : 0?', 'geht nicht, durch 0 darf man nicht teilen', ['0', zt(n)]
        w = f'Es gibt keine Zahl, die mal 0 wieder {zt(n)} ergibt. Durch 0 darf man nicht teilen.'
    aw, i = _rund(r, f)
    return {'y': 'auswahl', 'f': {'text': text}, 'a': aw, 'o': {'index': i}, 'w': w, 'h': 'Mach die Probe mit der Umkehraufgabe (Malnehmen).'}


def g_geteilt_ganz(s):
    if s == 2 and R.random() < .2: return _null()
    if s == 3:
        if R.random() < .5:
            q, b = R.choice([-1, 1]) * R.randint(2, 12), R.choice([-1, 1]) * R.randint(2, 9)
            c = R.choice([-1, 1]) * R.randint(2, 6); a = q * b
            if q > 0 and b > 0 and c > 0: return g_geteilt_ganz(s)
            return {'y': 'zahl', 'f': {'text': f'Berechne {kl(a * c)} : {kl(b)} : {kl(c)}.'}, 'o': {'wert': q}, 'c': f'({a * c})/({b})/({c})',
                    'w': f'Von links nach rechts: {kl(a * c)} : {kl(b)} = {zt(q * c)}. Dann {kl(q * c)} : {kl(c)} = {zt(q)}.', 'h': 'Rechne von links nach rechts und bestimme bei jedem Schritt das Vorzeichen.'}
        a, b, c = R.choice([-1, 1]) * R.randint(2, 9), R.choice([-1, 1]) * R.randint(2, 12), R.choice([-1, 1]) * R.randint(2, 9)
        if (a * b) % c or a * b // c == 0 or (a > 0 and b > 0 and c > 0) or abs(c) in (abs(a), abs(b)): return g_geteilt_ganz(s)
        e = a * b // c
        return {'y': 'zahl', 'f': {'text': f'Berechne {kl(a)} · {kl(b)} : {kl(c)}.'}, 'o': {'wert': e}, 'c': f'({a})*({b})/({c})',
                'w': f'Von links nach rechts: {kl(a)} · {kl(b)} = {zt(a * b)}. Dann {kl(a * b)} : {kl(c)} = {zt(e)}.', 'h': 'Mal und Geteilt sind gleichrangig: von links nach rechts.'}
    g = {1: 10, 2: 12}[s]
    q, b = R.choice([-1, 1]) * R.randint(2, g), R.choice([-1, 1]) * R.randint(2, g)
    a = q * b
    if a > 0 and b > 0: return g_geteilt_ganz(s)
    return {'y': 'zahl', 'f': {'text': f'Berechne {kl(a)} : {kl(b)}.'}, 'o': {'wert': q}, 'c': f'({a})/({b})',
            'w': f'Beträge: {abs(a)} : {abs(b)} = {abs(q)}. {_vz(a, b)}: {zt(q)}.', 'h': 'Erst die Beträge dividieren, dann das Vorzeichen bestimmen.'}


def _ue_sach():
    if R.random() < .5:
        n, p = R.randint(21, 34), R.randint(152, 244)
        if n == 25: return _ue_sach()
        rn, rp = _rund1(n), _rund1(p)
        return {'y': 'zahl', 'f': {'text': f'{n} Kinder fahren ins Schullandheim, jedes zahlt {p} €. Überschlage die Gesamtkosten: Runde {n} auf Zehner und {p} auf Hunderter.'},
                'o': {'wert': rn * rp, 'einheit': '€'}, 'c': f'{rn}*{rp}',
                'w': f'{n} ≈ {rn} und {p} ≈ {rp}. Überschlag: {rn} · {rp} = {zt(rn * rp)} €. (Genau: {zt(n * p)} €)',
                'h': 'Runde zuerst beide Zahlen. Dann rechne im Kopf.'}
    k, f = R.randint(12, 48), R.randint(12, 48)
    if k % 10 in (0, 5) or f % 10 in (0, 5): return _ue_sach()
    rk, rf = _rund1(k), _rund1(f)
    return {'y': 'zahl', 'f': {'text': f'Im Lager stehen {k} Kisten mit je {f} Flaschen. Überschlage die Zahl der Flaschen: Runde beide Zahlen auf Zehner.'},
            'o': {'wert': rk * rf}, 'c': f'{rk}*{rf}',
            'w': f'{k} ≈ {rk} und {f} ≈ {rf}. Überschlag: {rk} · {rf} = {zt(rk * rf)}. (Genau: {zt(k * f)})',
            'h': 'Runde zuerst beide Zahlen auf Zehner. Dann rechne im Kopf.'}


def g_ueberschlag(s):
    if s == 2 and R.random() < .3: return _ue_sach()
    if s == 3 and R.random() < .4: return _ue_sach()
    return _ue_alt(s)


def div_weg(n, d):
    """Lösungsweg der schriftlichen Division, Schritt für Schritt."""
    ziff = str(n); i, teil = 0, 0
    while teil < d and i < len(ziff): teil = teil * 10 + int(ziff[i]); i += 1
    sch = []
    q = teil // d; r = teil - q * d
    sch.append(f'{zt(teil)} : {d} = {q}' + (f' Rest {r}' if r else ''))
    erg = str(q)
    while i < len(ziff):
        teil = r * 10 + int(ziff[i]); i += 1
        q = teil // d; r = teil - q * d; erg += str(q)
        if q == 0: sch.append(f'{ziff[i - 1]} herunterholen: {teil} : {d} geht nicht, also 0 ins Ergebnis' + (f', Rest {r}' if r else ''))
        else: sch.append(f'{ziff[i - 1]} herunterholen: {teil} : {d} = {q}' + (f' Rest {r}' if r else ''))
    return '. '.join(sch) + f'. Ergebnis {zt(int(erg))}. Probe: {zt(int(erg))} · {d} = {zt(n)}.'


def _mal_weg(a, b):
    teile = [(a * (int(z) * 10 ** (len(str(b)) - 1 - j)), int(z) * 10 ** (len(str(b)) - 1 - j)) for j, z in enumerate(str(b))]
    return 'Teilprodukte: ' + '; '.join(f'{a} · {zt(t)} = {zt(p)}' for p, t in teile) + f'. Summe: {zt(a * b)}. Überschlag: {zt(_rund1(a))} · {_rund1(b)} = {zt(_rund1(a) * _rund1(b))}.'


def _null_im_ergebnis():
    d = R.randint(3, 9)
    q = R.choice([R.randint(1, 9) * 100 + R.randint(1, 9), R.randint(1, 9) * 1000 + R.randint(1, 9), R.randint(1, 9) * 1000 + R.randint(1, 9) * 10 + R.randint(1, 9)])
    return q, d


def g_schriftlich(s):
    if s == 1:
        a, b = R.randint(123, 987), R.randint(3, 9)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'Rechne schriftlich: {a} · {b}'}, 'o': {'wert': a * b}, 'c': f'{a}*{b}',
                    'w': f'Stellenweise: {a // 100 * 100} · {b} = {zt(a // 100 * 100 * b)}, {a // 10 % 10 * 10} · {b} = {zt(a // 10 % 10 * 10 * b)}, {a % 10} · {b} = {a % 10 * b}. Summe: {zt(a * b)}.',
                    'h': 'Multipliziere Einer, Zehner und Hunderter einzeln mit dem Faktor und denke an die Überträge.'}
        return {'y': 'zahl', 'f': {'text': f'Rechne schriftlich: {zt(a * b)} : {b}'}, 'o': {'wert': a}, 'c': f'{a * b}/{b}',
                'w': div_weg(a * b, b), 'h': 'Teile von links Ziffer für Ziffer. Prüfe am Ende mit der Umkehrrechnung.'}
    if s == 2:
        if R.random() < .55:
            a, b = R.randint(123, 987), R.randint(12, 98)
            if b % 10 == 0: return g_schriftlich(s)
            return {'y': 'zahl', 'f': {'text': f'Rechne schriftlich: {a} · {b}'}, 'o': {'wert': a * b}, 'c': f'{a}*{b}', 'w': _mal_weg(a, b),
                    'h': 'Zwei Teilprodukte: erst mit den Zehnern (eine Stelle versetzt), dann mit den Einern. Dann addieren.'}
        d = R.randint(11, 25); q = R.randint(23, 98)
        if d in (20,): return g_schriftlich(s)
        return {'y': 'zahl', 'f': {'text': f'Rechne schriftlich: {zt(q * d)} : {d}'}, 'o': {'wert': q}, 'c': f'{q * d}/{d}',
                'w': div_weg(q * d, d), 'h': f'Schreibe dir zuerst die {d}er-Reihe bis {d} · 9 auf.'}
    art = R.choice(['null', 'null', 'fehler', 'uebertrag'])
    if art == 'uebertrag':
        a, b = R.randint(567, 989), R.randint(46, 99)
        if b % 10 < 6 or a % 10 < 5 or a // 10 % 10 < 5: return g_schriftlich(s)
        return {'y': 'zahl', 'f': {'text': f'Rechne schriftlich: {a} · {b}'}, 'o': {'wert': a * b}, 'c': f'{a}*{b}', 'w': _mal_weg(a, b),
                'h': 'Achte auf die Überträge und versetze das Zehner-Teilprodukt um eine Stelle. Mache vorher einen Überschlag.'}
    q, d = _null_im_ergebnis()
    if art == 'null':
        return {'y': 'zahl', 'f': {'text': f'Rechne schriftlich: {zt(q * d)} : {d}'}, 'o': {'wert': q}, 'c': f'{q * d}/{d}',
                'w': div_weg(q * d, d), 'h': 'Wenn die heruntergeholte Zahl nicht reicht, schreibe eine 0 ins Ergebnis.'}
    ohne = int(str(q).replace('0', ''))
    hinten = int(str(ohne) + '0' * str(q).count('0'))
    if hinten == q: return g_schriftlich(s)
    aw, i = _rund(f'Die 0 im Ergebnis fehlt. Richtig ist {zt(q)}.', ['Das Kind hat richtig gerechnet.', f'Die 0 gehört ans Ende: {zt(hinten)}.'])
    return {'y': 'auswahl', 'f': {'text': f'Jemand rechnet {zt(q * d)} : {d} = {zt(ohne)}. Was ist passiert?'}, 'a': aw, 'o': {'index': i},
            'w': div_weg(q * d, d) + f' Überschlag zeigt es auch: {zt(ohne)} · {d} ist viel zu klein.',
            'h': 'Mach die Probe: Ergebnis mal Teiler.'}


def g_termaufbau(s):
    a, b, c = R.randint(2, 12), R.randint(2, 12), R.randint(2, 12)
    if s == 1:
        op = R.choice('+-*:')
        x, y = (a * b, b) if op == ':' else ((a + b, b) if op == '-' else (a, b))
        text = f'{x} {dict(zip("+-*:", "+−·:"))[op]} {y}'
        aw, i = _rund(NAME[op], [n for n in NAME.values() if n != NAME[op]])
        return {'y': 'auswahl', 'f': {'text': f'Wie heißt der Term {text}?'}, 'a': aw, 'o': {'index': i},
                'w': f'Plus: Summe. Minus: Differenz. Mal: Produkt. Geteilt: Quotient. {text} ist {"eine" if op != ":" and op != "*" else "ein"} {NAME[op]}.', 'h': 'Welche Rechenart steht da?'}
    if s == 2:
        form = R.choice(['sp', 'ps', 'dp', 'pd'])
        if form == 'sp': text, n, erkl = f'{a} + {b} · {c}', 'Summe', f'zuerst {b} · {c}, zuletzt das Plus'
        elif form == 'ps': text, n, erkl = f'({a} + {b}) · {c}', 'Produkt', 'zuerst die Klammer, zuletzt das Mal'
        elif form == 'dp': text, n, erkl = f'{a * b + c} − {a} · {b}', 'Differenz', f'zuerst {a} · {b}, zuletzt das Minus'
        else: text, n, erkl = f'({a + b} − {b}) · {c}', 'Produkt', 'zuerst die Klammer, zuletzt das Mal'
        aw, i = _rund(n, [x for x in NAME.values() if x != n])
        return {'y': 'auswahl', 'f': {'text': f'Welche Art von Term ist {text}?'}, 'a': aw, 'o': {'index': i},
                'w': f'Reihenfolge: {erkl}. Die letzte Rechnung gibt den Namen: {n}.', 'h': 'Welche Rechnung führst du als letzte aus?'}
    if R.random() < .45:
        form = R.choice(['dm', 'qs', 'sm'])
        if form == 'dm':
            x = a + b + c
            term, r, f = f'({x} − {b}) · {c}', f'Multipliziere die Differenz aus {x} und {b} mit {c}.', [f'Subtrahiere das Produkt aus {b} und {c} von {x}.', f'Multipliziere {x} mit der Differenz aus {b} und {c}.']
        elif form == 'qs':
            x = (b + c) * a
            term, r, f = f'{x} : ({b} + {c})', f'Dividiere {x} durch die Summe aus {b} und {c}.', [f'Addiere {c} zum Quotienten aus {x} und {b}.', f'Dividiere die Summe aus {x} und {b} durch {c}.']
        else:
            term, r, f = f'({a} + {b}) · {c}', f'Multipliziere die Summe aus {a} und {b} mit {c}.', [f'Addiere {a} zum Produkt aus {b} und {c}.', f'Multipliziere {a} mit der Summe aus {b} und {c}.']
        if len({a, b, c}) < 3: return g_termaufbau(s)
        aw, i = _rund(r, f)
        return {'y': 'auswahl', 'f': {'text': f'Welcher Satz passt zum Term {term}?'}, 'a': aw, 'o': {'index': i},
                'w': f'Die letzte Rechnung gibt den Anfang des Satzes. Die Klammer wird zuerst gerechnet und heißt im Satz Summe oder Differenz: {r}',
                'h': 'Welche Rechnung kommt zuletzt? Damit beginnt der Satz.'}
    form = R.choice(['a', 'b', 'c', 'd'])
    if form == 'c' and a == b: return g_termaufbau(s)
    if form == 'a': satz, r, f = f'Addiere {a} zum Produkt aus {b} und {c}.', f'{b} · {c} + {a}', [f'({a} + {b}) · {c}', f'{a} · {b} + {c}']
    elif form == 'b': satz, r, f = f'Multipliziere die Summe aus {a} und {b} mit {c}.', f'({a} + {b}) · {c}', [f'{a} + {b} · {c}', f'{a} · {b} + {c}']
    elif form == 'c': satz, r, f = f'Subtrahiere das Produkt aus {a} und {b} von {a * b + c}.', f'{a * b + c} − {a} · {b}', [f'{a} · {b} − {a * b + c}', f'({a * b + c} − {a}) · {b}']
    else: satz, r, f = f'Dividiere die Differenz aus {a * c + b * c} und {b * c} durch {c}.', f'({a * c + b * c} − {b * c}) : {c}', [f'{a * c + b * c} − {b * c} : {c}', f'{c} : ({a * c + b * c} − {b * c})']
    if len({r, *f}) < 3: return g_termaufbau(s)
    aw, i = _rund(r, f)
    return {'y': 'auswahl', 'f': {'text': f'Welcher Term passt? „{satz}“'}, 'a': aw, 'o': {'index': i},
            'w': f'Der Satz beschreibt die letzte Rechnung zuerst. Was zuerst gerechnet werden muss, steht als Produkt oder in einer Klammer: {r}.',
            'h': 'Überlege, was zuerst ausgerechnet werden muss. Das braucht Vorrang (Punktrechnung oder Klammer).'}


GEN = {'differenz_summe': g_differenz_summe, 'punkt_strich': g_punkt_strich, 'klammern': g_klammern, 'vorteil': g_vorteil, 'verteilen': g_verteilen, 'mal_ganz': g_mal_ganz,
       'geteilt_ganz': g_geteilt_ganz, 'ueberschlag': g_ueberschlag, 'schriftlich': g_schriftlich, 'termaufbau': g_termaufbau}
DATEI = {
    'thema_schluessel': 'zahlen.rechengesetze', 'thema_id': 18, 'block_id': 49, 'klasse': {'gym_by': 5, 'rs_by': 5, 'ib_myp': 1},
    'autor': 'Claude (Generator zahlen_rechengesetze.py)',
    'inhalt': {
        'ziel': 'Terme in der richtigen Reihenfolge berechnen, Rechengesetze für Rechenvorteile nutzen, ganze Zahlen multiplizieren und dividieren, überschlagen und schriftlich rechnen.',
        'merke': ['Klammer vor Punkt vor Strich.', 'Tauschen und verbinden: nur bei plus und mal.', 'Verteilen: Der Faktor gehört zu jedem Teil der Klammer.',
                  'Mal und geteilt: gleiche Vorzeichen plus, verschiedene minus.', 'Erst überschlagen, dann genau rechnen.'],
        'abschnitte': [{'titel': 'Reihenfolge beim Rechnen', 'lernziele': ['punkt_strich', 'klammern', 'termaufbau']},
                       {'titel': 'Geschickt rechnen', 'lernziele': ['vorteil', 'differenz_summe', 'verteilen']},
                       {'titel': 'Mal und geteilt mit ganzen Zahlen', 'lernziele': ['mal_ganz', 'geteilt_ganz']},
                       {'titel': 'Große Rechnungen', 'lernziele': ['ueberschlag', 'schriftlich']}],
        'etappen': ETAPPEN,
        'teilfaehigkeiten': [{'k': 'vorrang', 'text': 'Vorrangregeln und Klammern', 'lernziele': ['punkt_strich', 'klammern']},
                             {'k': 'gesetze', 'text': 'Rechengesetze für Rechenvorteile', 'lernziele': ['vorteil', 'differenz_summe', 'verteilen']},
                             {'k': 'ganz', 'text': 'Multiplikation und Division ganzer Zahlen', 'lernziele': ['mal_ganz', 'geteilt_ganz']},
                             {'k': 'verfahren', 'text': 'Überschlag und schriftliche Verfahren', 'lernziele': ['ueberschlag', 'schriftlich']},
                             {'k': 'terme', 'text': 'Termstrukturen erkennen', 'lernziele': ['termaufbau']}],
        'bewertung': {'lernziele_pflicht': [e['lernziel'] for e in ETAPPEN], 'lernziele_vertiefung': [], 'testaufgaben_je_lernziel': 1, 'hilfen_im_test': False},
        'quellen': {'erklaerungen': 'Eigene Fassung (Claude).', 'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern, Gymnasium Mathematik 5.'},
    },
    'aufgaben': baue(R, ETAPPEN, GEN, TEIL, je_stufe=5),
}

# Umbau U5 (Achte Runde, Vorgabe 16.11.): Lernkarten nach dem neuen Muster – einstieg, woerter (≤ 3), Kartenbild,
# Bildergeschichte (schritte mit bild), „Pass auf!“ (fehler + fehler_bild), MERKE (regel). Situationen: Kino, Einkauf, Konto, Verein.
# Rechentabellen (Typ tabelle) füllen sich Schritt für Schritt; Rechenbaum (Typ baum) für den Aufbau eines Terms.
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl5.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl5 import umbau  # noqa: E402

KOPF = ['Was', 'Rechnung', 'Euro']
BAUM = lambda plus, mal: {'typ': 'baum', 'aeste': [{'text': plus, 'aeste': [{'text': '3'}, {'text': mal, 'aeste': [{'text': '4'}, {'text': '5'}]}]}]}

KARTEN = {
 'punkt_strich': {
  'einstieg': 'Du kaufst 4 Kinokarten zu je 5 € und ein Popcorn für 3 €. Erst rechnest du die Karten aus, dann kommt das Popcorn dazu. Diese Reihenfolge heißt ⟦Punkt vor Strich⟧.',
  'woerter': [['·', 'das Malzeichen: 4 · 5 heißt „4 mal 5“'], ['Punktrechnung', 'mal (·) und geteilt (:)'], ['Strichrechnung', 'plus (+) und minus (−)']],
  'bild': {'typ': 'tabelle', 'kopf': KOPF, 'zeilen': [['Karten', '4 · 5', '?'], ['Popcorn', '3', '3'], ['zusammen', '3 + 4 · 5', '?']]},
  'schritte': [{'text': 'Die Rechnung für den Kinobesuch heißt 3 + 4 · 5.'},
               {'text': 'Punktrechnung zuerst: 4 · 5 = 20. Die Karten kosten 20 €.',
                'bild': {'zeilen': [['Karten', '4 · 5', '20'], ['Popcorn', '3', '3'], ['zusammen', '3 + 4 · 5', '?']]}},
               {'text': 'Dann die Strichrechnung: 3 + 20 = ⟦23⟧.',
                'bild': {'zeilen': [['Karten', '4 · 5', '20'], ['Popcorn', '3', '3'], ['zusammen', '3 + 20', '23']]}}],
  'fehler': 'Stur von links rechnen: 3 + 4 = 7, dann 7 · 5 = 35. Das wären 7 Kinokarten – gekauft hast du nur 4.',
  'fehler_bild': {'zeilen': [['falsch', '7 · 5', '35'], ['richtig', '3 + 20', '23']]},
  'regel': '⟦Punktrechnung⟧ kommt vor Strichrechnung. Sonst rechnest du von links nach rechts.'},
 'klammern': {
  'einstieg': 'Für jede Person kostet die Karte 3 € und das Menü 4 €. Ihr seid 5 Personen. Erst den Preis pro Person, dann mal 5: Das zeigen ⟦Klammern⟧.',
  'woerter': [['Klammern ( )', 'Was in der Klammer steht, rechnest du zuerst'], ['(3 + 4) · 5', 'gelesen „3 plus 4, das Ganze mal 5“']],
  'bild': {'typ': 'tabelle', 'kopf': KOPF, 'zeilen': [['1 Person', '3 + 4', '?'], ['5 Personen', '(3 + 4) · 5', '?']]},
  'schritte': [{'text': 'Rechne (3 + 4) · 5. Klammer zuerst: 3 + 4 = 7.', 'bild': {'zeilen': [['1 Person', '3 + 4', '7'], ['5 Personen', '(3 + 4) · 5', '?']]}},
               {'text': 'Eine Person zahlt 7 €. Für 5 Personen: 7 · 5 = ⟦35⟧.', 'bild': {'zeilen': [['1 Person', '3 + 4', '7'], ['5 Personen', '7 · 5', '35']]}}],
  'fehler': 'Die Klammer übersehen: 3 + 4 · 5 = 23. Das wären eine Karte und 5 Menüs statt 5-mal Karte und Menü.',
  'fehler_bild': {'zeilen': [['ohne Klammer', '3 + 4 · 5', '23'], ['mit Klammer', '(3 + 4) · 5', '35']]},
  'regel': 'Klammern rechnest du ⟦zuerst⟧. Stecken Klammern ineinander, fängst du innen an. Danach gilt Punkt vor Strich.'},
 'termaufbau': {
  'einstieg': 'Beschreibst du die Kino-Rechnung, sagst du: Zu den Karten kommt das Popcorn dazu. Am Ende wird also addiert. Nach seiner letzten Rechnung bekommt jeder ⟦Term⟧ einen Namen.',
  'woerter': [['Term', 'eine Rechnung aus Zahlen und Rechenzeichen, zum Beispiel 3 + 4 · 5'], ['Summe', 'ein Term, bei dem zuletzt plus gerechnet wird'],
              ['Produkt', 'ein Term, bei dem zuletzt mal gerechnet wird']],
  'bild': BAUM('+', '·'),
  'schritte': [{'text': 'Bei 3 + 4 · 5 rechnest du zuerst 4 · 5 = 20.', 'bild': BAUM('+', '· zuerst')},
               {'text': 'Zuletzt kommt 3 + 20. Die letzte Rechnung ist ein Plus.', 'bild': BAUM('+ zuletzt', '· zuerst')},
               {'text': 'Darum ist der Term eine ⟦Summe⟧: aus 3 und dem Produkt 4 · 5.'}],
  'fehler': 'Den Term „Produkt“ nennen, weil ein Malpunkt vorkommt, ist falsch. Am Ende kommt das Popcorn dazu: Die letzte Rechnung ist plus.',
  'regel': 'Der Name richtet sich nach der ⟦letzten Rechnung⟧. Plus: Summe, minus: Differenz, mal: Produkt, geteilt: Quotient.'},
 'vorteil': {
  'einstieg': 'An der Kasse ist egal, in welcher Reihenfolge deine Sachen aufs Band kommen. Der Preis bleibt gleich. Bei plus und mal darfst du deshalb ⟦tauschen⟧.',
  'woerter': [['tauschen', 'die Reihenfolge ändern; erlaubt bei plus und mal (Fachwort: Kommutativgesetz)'],
              ['zusammenfassen', 'zwei Zahlen zuerst miteinander rechnen (Fachwort: Assoziativgesetz)'], ['glatte Zahl', 'eine Zahl wie 10, 100 oder 1 000']],
  'bild': {'typ': 'tabelle', 'kopf': ['Weg', 'Rechnung', 'Ergebnis'], 'zeilen': [['von links', '25 · 7 · 4', 'mühsam'], ['getauscht', '25 · 4 · 7', '?']]},
  'schritte': [{'text': 'Rechne 25 · 7 · 4. Von links wäre 25 · 7 mühsam.'},
               {'text': 'Tausche die 4 nach vorn. Dann 25 · 4 zusammenfassen.'},
               {'text': '25 · 4 = 100 ist eine glatte Zahl.', 'bild': {'zeilen': [['von links', '25 · 7 · 4', 'mühsam'], ['getauscht', '100 · 7', '?']]}},
               {'text': '100 · 7 = ⟦700⟧.', 'bild': {'zeilen': [['von links', '25 · 7 · 4', 'mühsam'], ['getauscht', '100 · 7', '700']]}}],
  'fehler': 'Bei minus tauschen ist falsch. 10 − 3 = 7, aber 3 − 10 = −7. Tauschen geht nur bei plus und mal.',
  'fehler_bild': {'kopf': ['Rechnung', 'Ergebnis'], 'zeilen': [['10 − 3', '7'], ['3 − 10', '−7']]},
  'regel': 'Bei plus und mal darfst du ⟦tauschen⟧ und zusammenfassen. Suche Paare mit glatten Ergebnissen: 25 · 4 = 100.'},
 'differenz_summe': {
  'einstieg': 'Du hast 47 €, kaufst ein Buch für 18 € und bekommst 13 € geschenkt. Lieber rechnest du zuerst 47 + 13 = 60. Das geht, wenn jedes ⟦Rechenzeichen⟧ mitwandert.',
  'woerter': [['Rechenzeichen', '+, −, · oder : zwischen zwei Zahlen'], ['mitwandert', 'Beim Tauschen nimmt jede Zahl das Zeichen vor ihr mit']],
  'bild': {'typ': 'tabelle', 'kopf': ['Reihenfolge', 'Rechnung', 'Euro'], 'zeilen': [['wie es kam', '47 − 18 + 13', '?']]},
  'schritte': [{'text': 'Das Minus gehört zur 18, das Plus zur 13.'},
               {'text': 'Hol + 13 mit seinem Zeichen nach vorn: 47 + 13 − 18.',
                'bild': {'zeilen': [['wie es kam', '47 − 18 + 13', '?'], ['getauscht', '47 + 13 − 18', '?']]}},
               {'text': '47 + 13 = 60, dann 60 − 18 = ⟦42⟧.', 'bild': {'zeilen': [['wie es kam', '47 − 18 + 13', '42'], ['getauscht', '60 − 18', '42']]}}],
  'fehler': '47 − 18 + 13 = 47 − 31 = 16 ist falsch. Die 13 € bekommst du dazu, du gibst sie nicht aus.',
  'fehler_bild': {'zeilen': [['falsch', '47 − 31', '16'], ['richtig', '60 − 18', '42']]},
  'regel': 'Jedes Rechenzeichen gehört zur ⟦Zahl dahinter⟧. Beim Tauschen nimmt die Zahl ihr Zeichen mit.'},
 'verteilen': {
  'einstieg': 'Ein Verein kauft 7 Taschen zu je 98 €. Rechne so, als kostete jede 100 €. Danach ziehst du für jede Tasche 2 € ab: Das ist das ⟦Verteilungsgesetz⟧.',
  'woerter': [['Verteilungsgesetz', 'Zahl mal Klammer: mit jedem Teil der Klammer malnehmen (Fachwort: Distributivgesetz)']],
  'bild': {'typ': 'tabelle', 'kopf': ['Teil', 'Rechnung', 'Euro'], 'zeilen': [['wie 100 €', '7 · 100', '?'], ['zu viel', '7 · 2', '?'], ['Preis', '7 · 98', '?']]},
  'schritte': [{'text': 'Schreibe 98 als 100 − 2. Die Rechnung heißt 7 · (100 − 2).'},
               {'text': 'So, als kostete jede Tasche 100 €: 7 · 100 = 700.',
                'bild': {'zeilen': [['wie 100 €', '7 · 100', '700'], ['zu viel', '7 · 2', '?'], ['Preis', '7 · 98', '?']]}},
               {'text': 'Das ist für jede Tasche 2 € zu viel: 7 · 2 = 14.',
                'bild': {'zeilen': [['wie 100 €', '7 · 100', '700'], ['zu viel', '7 · 2', '14'], ['Preis', '7 · 98', '?']]}},
               {'text': '700 − 14 = ⟦686⟧. Die Taschen kosten 686 €.',
                'bild': {'zeilen': [['wie 100 €', '7 · 100', '700'], ['zu viel', '7 · 2', '14'], ['Preis', '700 − 14', '686']]}}],
  'fehler': '7 · (100 − 2) = 700 − 2 ist falsch. Jede der 7 Taschen ist 2 € billiger, also ziehst du 14 € ab.',
  'fehler_bild': {'zeilen': [['wie 100 €', '7 · 100', '700'], ['falsch', 'nur 2', '698'], ['richtig', '7 · 2', '14']]},
  'regel': 'Zahl mal Klammer: mit ⟦jedem Teil⟧ malnehmen. 7 · (100 − 2) = 7 · 100 − 7 · 2. Rückwärts heißt das ausklammern.'},
 'mal_ganz': {
  'einstieg': 'Für ein Handy-Abo werden jeden Monat 6 € abgebucht. Nach 4 Monaten fehlen 24 €. Malnehmen mit negativen Zahlen heißt auch ⟦multiplizieren⟧.',
  'woerter': [['multiplizieren', 'malnehmen'], ['abgebucht', 'vom Konto weggenommen'], ['Vorzeichenregel', 'gleiche Vorzeichen ergeben plus, verschiedene ergeben minus']],
  'bild': {'typ': 'zahlenstrahl', 'start': -30, 'ende': 0, 'abschnitte': 15, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': '4 · (−6) heißt: viermal 6 € abgebucht.',
                'bild': {'boegen': [{'von': 0, 'bis': -6}, {'von': -6, 'bis': -12}, {'von': -12, 'bis': -18}, {'von': -18, 'bis': -24}]}},
               {'text': 'Du landest bei ⟦−24⟧.', 'bild': {'punkte': [{'wert': -24}]}},
               {'text': 'Und Minus mal Minus? (−6) · 1 = −6 und (−6) · 0 = 0.',
                'bild': {'start': -12, 'ende': 12, 'abschnitte': 12, 'boegen': [{'von': -6, 'bis': 0, 'name': '+6'}], 'punkte': [{'wert': -6}, {'wert': 0}]}},
               {'text': 'Jeder Schritt bringt 6 mehr. Also ist (−6) · (−1) = ⟦6⟧.',
                'bild': {'boegen': [{'von': -6, 'bis': 0, 'name': '+6'}, {'von': 0, 'bis': 6, 'name': '+6'}], 'punkte': [{'wert': -6}, {'wert': 0}, {'wert': 6}]}},
               {'text': 'Das ist die Vorzeichenregel: gleiche Vorzeichen ergeben plus.'}],
  'fehler': '(−6) · (−4) = −24 ist falsch: Gleiche Vorzeichen ergeben plus, also 24. Beim Addieren gilt das nicht: (−6) + (−4) = −10.',
  'regel': 'Erst die Zahlen ohne Vorzeichen malnehmen. ⟦Gleiche Vorzeichen⟧ ergeben plus, verschiedene ergeben minus.'},
 'geteilt_ganz': {
  'einstieg': 'Du hast 48 € Schulden und zahlst sie in 6 gleichen Raten ab. Jede Rate ist 8 €. Teilen heißt ⟦dividieren⟧, und es gelten dieselben Vorzeichenregeln.',
  'woerter': [['dividieren', 'teilen'], ['Rate', 'ein gleich großer Teil, in dem man Schulden abzahlt']],
  'bild': {'typ': 'zahlenstrahl', 'start': -48, 'ende': 0, 'abschnitte': 6, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': '(−48) : 6 heißt: −48 in 6 gleiche Teile teilen.',
                'bild': {'boegen': [{'von': 0, 'bis': -8}, {'von': -8, 'bis': -16}, {'von': -16, 'bis': -24}, {'von': -24, 'bis': -32}, {'von': -32, 'bis': -40}, {'von': -40, 'bis': -48}]}},
               {'text': 'Ohne Vorzeichen: 48 : 6 = 8. Jeder Teil ist 8 lang.', 'bild': {'punkte': [{'wert': -8, 'name': '1 Rate'}]}},
               {'text': 'Verschiedene Vorzeichen ergeben minus: ⟦(−48) : 6 = −8⟧.'}],
  'fehler': '(−48) : (−6) = −8 ist falsch: Minus durch Minus ergibt plus, also 8. Probe: 8 · (−6) = −48.',
  'regel': 'Teilen geht wie Malnehmen: ⟦gleiche Vorzeichen⟧ ergeben plus, verschiedene minus. Prüfe mit der Malrechnung rückwärts.'},
 'ueberschlag': {
  'einstieg': 'Das Kino hat 487 Plätze und war an 21 Abenden voll. Wie viele Besucher waren das ungefähr? Mit gerundeten Zahlen im Kopf rechnen heißt ⟦überschlagen⟧.',
  'woerter': [['runden', 'eine Zahl durch eine nahe glatte Zahl ersetzen: 487 wird zu 500'], ['≈', '„ungefähr gleich“'],
              ['überschlagen', 'schnell und ungefähr mit gerundeten Zahlen rechnen']],
  'bild': {'typ': 'zahlenstrahl', 'start': 400, 'ende': 600, 'abschnitte': 4, 'beschriftet': 'alle'},
  'schritte': [{'text': '487 liegt näher an 500 als an 400. Also ist 487 ≈ 500.',
                'bild': {'punkte': [{'wert': 487, 'name': 'Plätze'}], 'boegen': [{'von': 487, 'bis': 500, 'name': 'runden'}]}},
               {'text': '21 Abende runden wir auf 20.',
                'bild': {'start': 0, 'ende': 40, 'abschnitte': 4, 'punkte': [{'wert': 21, 'name': 'Abende'}], 'boegen': [{'von': 21, 'bis': 20, 'name': 'runden'}]}},
               {'text': 'Im Kopf: 500 · 20 = ⟦10 000⟧ Besucher.'},
               {'text': 'Genau sind es 487 · 21 = 10 227. Das passt.'}],
  'fehler': '1 022 hinschreiben, ohne zu prüfen. Der Überschlag sagt etwa 10 000. Bei 1 022 fehlt eine Stelle.',
  'regel': 'Erst ⟦runden⟧, dann im Kopf rechnen. Liegt das genaue Ergebnis weit weg, hast du dich verrechnet.'},
 'schriftlich': {
  'einstieg': 'Ein Verein kauft 26 Fahrräder zu je 347 €. Das ist zu viel für den Kopf. Mit dem Stift zerlegst du die Rechnung in kleine Teile: ⟦schriftlich rechnen⟧.',
  'woerter': [['Teilprodukt', 'das Ergebnis eines kleinen Malschritts, zum Beispiel 347 · 6'], ['stellengerecht', 'Einer unter Einer, Zehner unter Zehner']],
  'bild': {'typ': 'tabelle', 'kopf': ['', 'T', 'H', 'Z', 'E'], 'zeilen': [['347 · 20', '', '', '', ''], ['347 · 6', '', '', '', ''], ['zusammen', '', '', '', '']]},
  'schritte': [{'text': 'Rechne 347 · 26. Zerlege 26 in 20 und 6.'},
               {'text': 'Die Teilprodukte: 347 · 20 = 6 940 und 347 · 6 = 2 082.',
                'bild': {'zeilen': [['347 · 20', '6', '9', '4', '0'], ['347 · 6', '2', '0', '8', '2'], ['zusammen', '', '', '', '']]}},
               {'text': 'Stellengerecht untereinander und addieren: ⟦9 022⟧.',
                'bild': {'zeilen': [['347 · 20', '6', '9', '4', '0'], ['347 · 6', '2', '0', '8', '2'], ['zusammen', '9', '0', '2', '2']]}},
               {'text': 'Überschlag: 350 · 25 = 8 750. Das passt.'}],
  'fehler': 'Beim Teilen eine Null vergessen: 1 236 : 6 ist 206, nicht 26. Reicht die heruntergeholte Zahl nicht, schreibst du 0.',
  'regel': 'Schriftlich mal: mit ⟦jeder Ziffer⟧ malnehmen, stellengerecht addieren. Schriftlich geteilt: teilen, malnehmen, abziehen, nächste Ziffer herunterholen.'},
}
umbau(DATEI, KARTEN)


# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl5) ----------
# Neue Übungen nach Prüfungsvorbild (Jahrgangsstufentest 6 Bayern, Bayerischer Mathematik-Test, Känguru 5/6); eigene Zahlen und Einkleidung.
from itertools import permutations  # noqa: E402
from _schwer_kl5 import A, L, Z, de, einzig, ergaenze, rw, wahl  # noqa: E402


def _schwer():
    N = {}
    groesst = ['2 · 3 + 4 · 5', '2 + 3 · 4 + 5', '2 · 3 · 4 + 5', '2 + 3 + 4 · 5']
    zeichen = {'+': 12 + 4 + 8, '−': 12 - 4 + 8, '·': 12 * 4 + 8, ':': 12 // 4 + 8}
    N['punkt_strich'] = [
        Z(2, 'Berechne 7 · 8 − 36 : 4 + 2.', '7 * 8 - 36 / 4 + 2', 'Punkt zuerst: 7 · 8 = 56 und 36 : 4 = 9. Dann 56 − 9 + 2 = 49.', 'Erst alle Mal- und Geteilt-Rechnungen, dann von links nach rechts.'),
        Z(2, 'Berechne 150 − 6 · 15 : 3.', '150 - 6 * 15 / 3', 'Punktrechnung von links: 6 · 15 = 90, 90 : 3 = 30. Dann 150 − 30 = 120.', 'Mal und geteilt hintereinander: von links nach rechts.'),
        L(3, 'Ergänze die Lücke: 60 − □ · 7 = 4', '60 − □ · 7 = 4', 'Trage die fehlende Zahl ein.', ['(60 - 4) // 7'],
          '□ · 7 muss 60 − 4 = 56 sein. 56 : 7 = 8. Probe: 60 − 8 · 7 = 60 − 56 = 4.', 'Was muss von 60 abgezogen werden, damit 4 übrig bleibt?'),
        wahl(3, 'Welche Rechnung hat das größte Ergebnis?', groesst, lambda o: rw(o) == max(rw(x) for x in groesst),
             'Ergebnisse: 6 + 20 = 26, 2 + 12 + 5 = 19, 24 + 5 = 29, 5 + 20 = 25. Am größten ist 2 · 3 · 4 + 5.', 'Rechne jede Zeile mit Punkt vor Strich aus.'),
        wahl(3, 'Welches Rechenzeichen gehört in die Lücke? 12 □ 4 + 8 = 11', list(zeichen), lambda o: zeichen[o] == 11,
             'Mit „:“: 12 : 4 = 3, 3 + 8 = 11. Die anderen ergeben 24, 16 und 56.', 'Probiere alle vier Zeichen aus. Denk an Punkt vor Strich.'),
        A(3, 'Jemand rechnet 5 + 3 · 4 = 32. Was ist falsch?', 'Punkt vor Strich: 3 · 4 = 12, dann 5 + 12 = 17.',
          ['Nichts, 32 stimmt.', '3 · 4 ist falsch ausgerechnet. Richtig ist 27.', 'Man muss von rechts rechnen: 4 · 3 + 5 = 17, also stimmt 32.'],
          'Gerechnet wurde (5 + 3) · 4 = 32. Ohne Klammer gilt aber Punkt vor Strich: 5 + 12 = 17.', 'Was wurde hier zuerst gerechnet? Was hätte zuerst gerechnet werden müssen?'),
    ]
    setzen = ['48 : (4 + 4) · 2', '48 : (4 + 4 · 2)', '(48 : 4 + 4) · 2', '48 : 4 + (4 · 2)']
    werte = set()
    for a, b, c in permutations([2, 3, 4]):
        werte |= {(a + b) * c, a + b * c, a * b + c, a * (b + c)}
    N['klammern'] = [
        Z(2, 'Berechne (45 − 17) : (2 + 5).', '(45 - 17) / (2 + 5)', 'Beide Klammern zuerst: 28 und 7. Dann 28 : 7 = 4.', 'Rechne zuerst jede Klammer für sich aus.'),
        Z(2, 'Berechne 3 · (40 − 8 · 4).', '3 * (40 - 8 * 4)', 'In der Klammer Punkt vor Strich: 8 · 4 = 32, 40 − 32 = 8. Dann 3 · 8 = 24.', 'Auch in der Klammer gilt Punkt vor Strich.'),
        wahl(3, 'Wo müssen die Klammern stehen, damit das Ergebnis 12 ist?', setzen, lambda o: rw(o) == 12,
             '48 : (4 + 4) · 2 = 48 : 8 · 2 = 6 · 2 = 12. Die anderen ergeben 4, 32 und 20.', 'Rechne jede Möglichkeit aus. Die Klammer immer zuerst.'),
        Z(3, 'Berechne: Dividiere die Summe aus 96 und 48 durch die Differenz von 20 und 8.', '(96 + 48) / (20 - 8)',
          'Summe: 96 + 48 = 144. Differenz: 20 − 8 = 12. 144 : 12 = 12.', 'Schreibe zuerst den Term mit Klammern auf: (… + …) : (… − …).'),
        L(3, 'Ergänze die Lücke: 4 · (□ − 9) = 28', '4 · (□ − 9) = 28', 'Trage die fehlende Zahl ein.', ['28 // 4 + 9'],
          'Die Klammer muss 28 : 4 = 7 ergeben. □ − 9 = 7, also □ = 16. Probe: 4 · (16 − 9) = 28.', 'Was muss in der Klammer herauskommen, damit 4 · Klammer = 28 ist?'),
        Z(3, 'Verwende die Zahlen 2, 3 und 4 je genau einmal, dazu einmal „+“ und einmal „·“. Klammern sind erlaubt. Wie groß ist das größte mögliche Ergebnis?',
          str(max(werte)), f'Am meisten bringt es, die Summe der beiden kleineren Zahlen mit der größten malzunehmen: (2 + 3) · 4 = {max(werte)}.',
          'Probiere systematisch: Was passiert, wenn die Summe in eine Klammer kommt?'),
    ]
    ausflug = ['(24 · 7 − 120) : 4', '24 · 7 − 120 : 4', '24 · (7 − 120) : 4', '(24 · 7 − 120) · 4']
    produkt = ['(4 + 5) · 7', '4 + 5 · 7', '4 · (5 + 7)', '4 · 5 + 7']
    N['termaufbau'] = [
        Z(2, 'Berechne das Produkt aus 12 und der Summe von 5 und 3.', '12 * (5 + 3)', 'Term: 12 · (5 + 3) = 12 · 8 = 96.', 'Die Summe kommt in Klammern, weil sie ein Faktor ist.'),
        wahl(2, 'Welche Art von Term ist (60 − 12) : (3 + 5)?', ['Quotient', 'Differenz', 'Summe', 'Produkt'], lambda o: o == 'Quotient',
             'Zuletzt wird 48 durch 8 geteilt. Die letzte Rechnung ist geteilt, also ein Quotient.', 'Welche Rechnung kommt ganz zum Schluss?'),
        wahl(3, '24 Kinder zahlen je 7 € für einen Ausflug. Der Bus kostet 120 €. Der Rest wird gleich auf 4 Gruppen verteilt. Welcher Term gibt den Betrag für eine Gruppe an?',
             ausflug, lambda o: o == '(24 · 7 − 120) : 4',
             'Eingenommen: 24 · 7. Rest nach dem Bus: 24 · 7 − 120. Dieser ganze Rest wird durch 4 geteilt, also braucht er eine Klammer: (24 · 7 − 120) : 4 = 12 €.',
             'Was wird zuerst ausgerechnet? Was wird am Schluss durch 4 geteilt?'),
        Z(3, 'Berechne: Subtrahiere vom Produkt aus 15 und 8 den Quotienten aus 72 und 9.', '15 * 8 - 72 / 9',
          'Term: 15 · 8 − 72 : 9 = 120 − 8 = 112.', 'Achtung bei „subtrahiere A von B“: Es heißt B − A.'),
        Z(3, 'Ein Term ist eine Differenz. Der erste Teil ist das Produkt aus 9 und einer unbekannten Zahl, der zweite Teil ist 13. Der Term hat den Wert 50. Wie heißt die unbekannte Zahl?',
          '(50 + 13) // 9', 'Term: 9 · □ − 13 = 50. Rückwärts: 9 · □ = 63, □ = 7.', 'Schreibe den Term mit □ auf und rechne rückwärts.'),
        wahl(3, 'Welcher Term ist ein Produkt, dessen erster Faktor eine Summe ist?', produkt, lambda o: o == '(4 + 5) · 7',
             'Bei (4 + 5) · 7 wird zuletzt malgenommen (Produkt), und der erste Faktor ist die Summe 4 + 5.', 'Bestimme bei jedem Term die letzte Rechnung.'),
    ]
    N['vorteil'] = [
        Z(2, 'Rechne geschickt: 4 · 13 · 25', '4 * 13 * 25', '4 · 25 = 100, dann 100 · 13 = 1 300.', 'Welche zwei Zahlen ergeben zusammen eine glatte Zahl?'),
        Z(2, 'Rechne geschickt: 198 + 467 + 2', '198 + 467 + 2', '198 + 2 = 200, dann 200 + 467 = 667.', 'Tausche so, dass zuerst eine glatte Zahl entsteht.'),
        Z(3, 'Rechne geschickt: 8 · 23 · 125', '8 * 23 * 125', '8 · 125 = 1 000, dann 1 000 · 23 = 23 000.', 'Kennst du ein Paar, das 1 000 ergibt?'),
        A(3, 'Jemand rechnet 80 : 8 : 2 = 80 : 4 = 20. Was ist falsch?', 'Beim Teilen darf man nicht so zusammenfassen. Richtig: 80 : 8 : 2 = 10 : 2 = 5.',
          ['Nichts, 20 stimmt.', '8 : 2 ist nicht 4. Richtig ist 80 : 6.', 'Man muss von rechts rechnen: 8 : 2 = 4, also stimmt 20.'],
          'Tauschen und Verbinden gelten nur bei plus und mal. Von links: 80 : 8 = 10, dann 10 : 2 = 5.', 'Rechne einfach von links nach rechts und vergleiche.'),
        Z(3, 'Rechne geschickt: 1 + 2 + 3 + … + 19 + 20', ' + '.join(str(i) for i in range(1, 21)),
          'Paare bilden: 1 + 20, 2 + 19, … , 10 + 11. Das sind 10 Paare mit je 21: 10 · 21 = 210.', 'Addiere die erste und die letzte Zahl, dann die zweite und die vorletzte …'),
        Z(3, 'Rechne geschickt: 25 · 25 · 4 · 4', '25 * 25 * 4 * 4', '(25 · 4) · (25 · 4) = 100 · 100 = 10 000.', 'Bilde zwei Paare.'),
    ]
    nicht = ['80 + 15 − 25 − 10', '80 − 10 + 15 − 25', '80 − (25 + 10) + 15', '80 − (25 + 15) − 10']
    N['differenz_summe'] = [
        Z(2, 'Rechne geschickt: 93 − 47 + 7', '93 - 47 + 7', 'Tauschen: 93 + 7 − 47 = 100 − 47 = 53.', 'Hol die + 7 mit ihrem Zeichen nach vorn.'),
        Z(2, 'Rechne geschickt: 250 − 38 − 62', '250 - 38 - 62', 'Beide Zahlen werden abgezogen: 38 + 62 = 100. 250 − 100 = 150.', 'Was wird insgesamt abgezogen?'),
        A(3, 'Jemand rechnet 64 − 19 + 36 − 11 = 64 + 36 − 19 + 11 = 92. Was ist falsch?', 'Die 11 hat ihr Minus verloren. Richtig ist 70.',
          ['Nichts, 92 stimmt.', 'Die 36 hätte ein Minus bekommen müssen. Richtig ist −2.', 'Die 19 hat ihr Minus verloren. Richtig ist 130.'],
          'Jede Zahl nimmt ihr Zeichen mit: 64 + 36 − 19 − 11 = 100 − 30 = 70.', 'Prüfe bei jeder Zahl, ob das Zeichen davor mitgewandert ist.'),
        Z(3, 'Welche Zahl musst du zu 128 − 45 addieren, damit 100 herauskommt?', '100 - (128 - 45)', '128 − 45 = 83. Bis 100 fehlen 17.', 'Rechne zuerst 128 − 45 aus.'),
        Z(3, 'Rechne geschickt: 100 − 99 + 98 − 97 + … + 4 − 3 + 2 − 1', ' + '.join(f'({i} - {i - 1})' for i in range(100, 0, -2)),
          'Paare bilden: (100 − 99) + (98 − 97) + … + (2 − 1). Das sind 50 Paare mit je 1: Ergebnis 50.', 'Fasse immer eine Plus- und die folgende Minus-Zahl zusammen.'),
        wahl(3, 'Welcher Term hat NICHT denselben Wert wie 80 − 25 + 15 − 10?', nicht, lambda o: rw(o) != rw('80 − 25 + 15 − 10'),
             '80 − 25 + 15 − 10 = 60. In 80 − (25 + 15) − 10 wird die 15 abgezogen statt addiert: 30.', 'Achte darauf, welches Zeichen jede Zahl am Ende hat.'),
    ]
    N['verteilen'] = [
        Z(2, 'Rechne geschickt: 9 · 102', '9 * 102', '9 · (100 + 2) = 900 + 18 = 918.', 'Zerlege 102 in 100 + 2.'),
        Z(2, 'Rechne geschickt: 14 · 7 + 14 · 3', '14 * 7 + 14 * 3', 'Ausklammern: 14 · (7 + 3) = 14 · 10 = 140.', 'Welcher Faktor kommt in beiden Produkten vor?'),
        Z(3, 'Ein Kino verkauft am Samstag 37 und am Sonntag 63 Karten zu je 9 €. Wie viel Geld nimmt es an beiden Tagen zusammen ein?', '37 * 9 + 63 * 9',
          '37 · 9 + 63 · 9 = (37 + 63) · 9 = 100 · 9 = 900 €.', 'Zähle zuerst alle Karten zusammen.', einheit='€'),
        Z(3, 'Rechne geschickt: 17 · 99 + 17', '17 * 99 + 17', '17 ist 17 · 1. Also 17 · (99 + 1) = 17 · 100 = 1 700.', 'Schreibe die einzelne 17 als 17 · 1.'),
        Z(3, 'Rechne geschickt: 36 · 25', '36 * 25', '36 · 25 = (40 − 4) · 25 = 1 000 − 100 = 900.', 'Schreibe 36 als 40 − 4.'),
        A(3, 'Jemand rechnet 6 · (20 + 4) = 6 · 20 + 4 = 124. Was ist falsch?', 'Auch die 4 muss mit 6 malgenommen werden. Richtig ist 144.',
          ['Nichts, 124 stimmt.', 'Man darf nicht verteilen. Richtig ist 6 · 20 = 120.', 'Richtig ist 6 + 20 + 4 = 30.'],
          '6 · (20 + 4) = 6 · 20 + 6 · 4 = 120 + 24 = 144.', 'Jeder Teil in der Klammer wird malgenommen.'),
    ]
    trip = [s for a in range(-3, 4) for b in range(a + 1, 4) for c in range(b + 1, 4) if a * b * c == -6 for s in [a + b + c]]
    N['mal_ganz'] = [
        Z(2, 'Berechne (−12) · (−5).', '(-12) * (-5)', '12 · 5 = 60. Gleiche Vorzeichen: plus. Ergebnis 60.', 'Erst ohne Vorzeichen rechnen, dann das Vorzeichen bestimmen.'),
        Z(2, 'Berechne (−4) · 25 · (−3).', '(-4) * 25 * (-3)', '(−4) · 25 = −100, dann (−100) · (−3) = 300.', 'Zwei Minuszeichen: Das Ergebnis ist positiv.'),
        Z(3, 'Berechne geschickt: (−25) · 7 · (−4) · (−1)', '(-25) * 7 * (-4) * (-1)',
          '(−25) · (−4) = 100. 100 · 7 = 700. 700 · (−1) = −700. Drei Minuszeichen: negativ.', 'Zähle die Minuszeichen. Suche ein Paar mit glattem Ergebnis.'),
        L(3, 'Ergänze die Lücke: (−6) · □ = 54', '(−6) · □ = 54', 'Trage die fehlende Zahl ein (mit Minus, falls negativ).', ['54 // (-6)'],
          '6 · 9 = 54. Damit das Ergebnis positiv wird, braucht −6 einen negativen Partner: □ = −9.', 'Das Ergebnis ist positiv, −6 ist negativ. Welches Vorzeichen braucht □?'),
        Z(3, 'Drei verschiedene ganze Zahlen von −3 bis 3 haben das Produkt −6. Wie groß kann ihre Summe höchstens sein?', str(max(trip)),
          'Möglich sind −1, 2, 3 (Summe 4), 1, −2, 3 (Summe 2), 1, 2, −3 (Summe 0) und −1, −2, −3 (Summe −6). Höchstens 4.',
          'Zerlege 6 in drei Faktoren und verteile die Minuszeichen.'),
        Z(3, 'Berechne (−1) · (−1) · (−1) · … mit genau 15 Faktoren (−1).', '(-1) ** 15',
          'Je zwei Faktoren (−1) ergeben 1. 14 Faktoren ergeben 1, der 15. macht daraus −1.', 'Ist die Zahl der Minuszeichen gerade oder ungerade?'),
    ]
    N['geteilt_ganz'] = [
        Z(2, 'Berechne (−144) : 12.', '(-144) / 12', '144 : 12 = 12. Verschiedene Vorzeichen: −12.', 'Erst ohne Vorzeichen teilen.'),
        Z(2, 'Berechne 0 : (−7).', '0 / (-7)', '0 geteilt durch eine Zahl (nicht 0) ist 0: 0 · (−7) = 0.', 'Prüfe rückwärts mit der Malrechnung.'),
        L(3, 'Ergänze die Lücke: □ : (−8) = 9', '□ : (−8) = 9', 'Trage die fehlende Zahl ein (mit Minus, falls negativ).', ['9 * (-8)'],
          'Rückwärts: □ = 9 · (−8) = −72. Probe: (−72) : (−8) = 9.', 'Rechne rückwärts mit Malnehmen.'),
        Z(3, 'Berechne (−56) : 7 − 18 : (−3).', '(-56) / 7 - 18 / (-3)', 'Punkt zuerst: (−56) : 7 = −8 und 18 : (−3) = −6. Dann −8 − (−6) = −2.',
          'Erst beide Divisionen, dann das Minus dazwischen.'),
        Z(3, 'Eine Zahl wird durch −4 geteilt. Dann wird 5 addiert. Das Ergebnis ist −3. Wie heißt die Zahl?', '(-3 - 5) * (-4)',
          'Rückwärts: −3 − 5 = −8. Dann −8 · (−4) = 32. Probe: 32 : (−4) + 5 = −8 + 5 = −3.', 'Gehe die Schritte rückwärts und kehre jede Rechnung um.'),
        Z(3, 'Die Temperatur fiel in 6 Stunden gleichmäßig von 4 °C auf −14 °C. Um wie viel Grad fiel sie pro Stunde?', '(4 - (-14)) / 6',
          'Insgesamt: 4 − (−14) = 18 Grad. 18 : 6 = 3 Grad pro Stunde.', 'Wie viele Grad sind es von 4 bis −14?'),
    ]
    rund = ['344 999', '345 000', '355 000', '335 500']
    stadion = {'3-mal': 3, '30-mal': 30, '300-mal': 300, '3 000-mal': 3000}
    kleinste = min(n for n in range(0, 1000) if (n + 50) // 100 * 100 == 800)
    N['ueberschlag'] = [
        Z(2, 'Überschlage 4 812 : 6. Runde dazu 4 812 auf eine Zahl, die sich gut durch 6 teilen lässt.', '4800 / 6', '4 812 ≈ 4 800, und 4 800 : 6 = 800.', 'Welche glatte Zahl in der Nähe ist durch 6 teilbar?'),
        Z(2, 'Überschlage 61 · 39. Runde dazu beide Zahlen auf Zehner.', '60 * 40', '61 ≈ 60, 39 ≈ 40. 60 · 40 = 2 400.', 'Erst runden, dann im Kopf malnehmen.'),
        wahl(3, 'Welche Zahl ergibt auf Zehntausender gerundet 350 000?', rund, lambda o: (int(rw(o)) + 5000) // 10000 * 10000 == 350000,
             '345 000: Die Tausenderstelle ist 5, also aufrunden auf 350 000. 344 999 wird zu 340 000, 355 000 zu 360 000, 335 500 zu 340 000.',
             'Schau auf die Tausenderstelle: ab 5 aufrunden.'),
        wahl(3, 'Ein Stadion hat 18 900 Plätze. Wie oft passt eine Schule mit 612 Kindern ungefähr hinein?', list(stadion),
             lambda o: stadion[o] == min(stadion.values(), key=lambda v: abs(v - 18900 / 612)),
             '18 900 ≈ 18 000 und 612 ≈ 600. 18 000 : 600 = 30. Also etwa 30-mal.', 'Runde beide Zahlen und teile dann.'),
        Z(3, 'Eine natürliche Zahl ergibt auf Hunderter gerundet 800. Wie heißt die kleinste Zahl, für die das gilt?', str(kleinste),
          '749 wird zu 700 abgerundet, 750 wird zu 800 aufgerundet. Die kleinste Zahl ist 750.', 'Ab welcher Zehnerstelle rundet man auf?'),
        wahl(3, 'Nur ein Ergebnis kann stimmen. Entscheide mit einem Überschlag: 3 912 : 8 = ?', ['489', '48', '4 890', '4 809'], lambda o: rw(o) == rw('3 912 : 8'),
             'Überschlag: 4 000 : 8 = 500. Nur 489 liegt in der Nähe.', 'Runde 3 912 auf Tausender und teile durch 8.'),
    ]
    zif = einzig([d for d in range(10) if (300 + 10 * d + 7) * 4 == 1468])
    N['schriftlich'] = [
        Z(2, 'Rechne schriftlich: 6 048 : 12', '6048 / 12', '60 : 12 = 5, Rest 0. 4 : 12 = 0 (die 0 aufschreiben!). 48 : 12 = 4. Ergebnis 504.', 'Wenn eine Stelle nicht reicht, schreibst du eine 0 ins Ergebnis.'),
        Z(2, 'Rechne schriftlich: 305 · 48', '305 * 48', '305 · 40 = 12 200, 305 · 8 = 2 440. Zusammen 14 640.', 'Zerlege 48 in 40 und 8.'),
        L(3, 'Ergänze die fehlende Ziffer: 3□7 · 4 = 1 468', '3□7 · 4 = 1 468', 'Trage die fehlende Ziffer ein.', [str(zif)],
          f'1 468 : 4 = 367. Die fehlende Ziffer ist {zif}.', 'Rechne rückwärts: 1 468 : 4.'),
        Z(3, 'Eine Klasse hat 250 € für Bastelmaterial. Ein Paket kostet 18 €. Wie viele Pakete kann sie höchstens kaufen?', '250 // 18',
          '250 : 18 = 13 Rest 16. Für ein 14. Paket reichen die 16 € nicht. Also 13 Pakete.', 'Teile schriftlich. Was bedeutet der Rest?'),
        Z(3, 'Bei einer Division ist der Teiler 24, das Ergebnis 37 und der Rest 5. Welche Zahl wurde geteilt?', '24 * 37 + 5',
          'Probe der Division rückwärts: 24 · 37 = 888, dazu der Rest 5: 893.', 'Rückwärts: Ergebnis mal Teiler, dann den Rest dazu.'),
        A(3, 'Jemand rechnet schriftlich 4 236 : 6 = 76. Was ist falsch?', 'Die 0 im Ergebnis fehlt. Richtig ist 706.',
          ['Nichts, 76 stimmt.', 'Richtig ist 7 060.', 'Der Rest wurde vergessen. Richtig ist 76 Rest 0.'],
          '42 : 6 = 7, dann 3 : 6 = 0 (0 aufschreiben), dann 36 : 6 = 6. Ergebnis 706. Überschlag: 4 200 : 6 = 700.', 'Mach einen Überschlag: 4 200 : 6.'),
    ]
    return N


ergaenze(DATEI, _schwer(), 1018)

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('zahlen.rechengesetze', 13_5_2)
# a) gleich leicht wie Stufe 1
for _t in ['Berechne (−3) · 2.', 'Berechne 4 · (−2).', 'Berechne (−3) · 9.']:
    BF.stufe('mal_ganz', _t, 1)
# a) nur größere Zahlen bzw. längere Rechnung ohne neuen Gedanken
BF.stufe('schriftlich', 'Rechne schriftlich: 865 · 47', 2)
BF.stufe('punkt_strich', 'Berechne 81 : 3 : 3 + 5 · 12.', 2)

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----

# ---- LÜCKEN (Achtzehnte Runde, Teil B, Zweig luecken-kl5): vier neue Lernkarten, siehe _luecken_kl5.py ----
# Lehrplan M5 3.1 (schriftlich dividieren auch mit mehrstelligen Teilern über zehn; Produkte/Quotienten ganzer Zahlen auch im Kopf;
# Gleichungen a · x = b, x : a = b, a : x = b durch Probieren oder Umkehraufgabe) und M5 3.2 (Vorwärts- und Rückwärtsarbeiten,
# Sachaufgaben mit allen Grundrechenarten). Die Karte „schriftlich“ bleibt unverändert; schriftlich_geteilt steht direkt dahinter.
# Alle bisherigen Karten und Aufgaben bleiben unverändert; neue Aufgaben hängen hinten an (Zufallsstarts 18_5_4 … 18_5_7).
from _luecken_kl5 import mische as m18, neue_karte  # noqa: E402


# --- Lernkarte kopfrechnen ---
def g_kopf(R, s):
    if s == 1:
        art = R.choice(['zerlegen', 'zerlegen', 'vorteil'])
        if art == 'zerlegen':
            a, b = R.randint(3, 9), R.choice([x for x in range(12, 50) if x % 10])
            z, e = b // 10 * 10, b % 10
            return {'y': 'zahl', 'f': {'text': f'Rechne im Kopf: {a} · {b}'}, 'o': {'wert': a * b}, 'c': f'{a} * {b}',
                    'w': f'Zerlegen: {b} = {z} + {e}. {a} · {z} = {a * z} und {a} · {e} = {a * e}. Zusammen {a * z} + {a * e} = {zt(a * b)}.',
                    'h': f'Zerlege {b} in Zehner und Einer.'}
        k, (p, q) = R.choice([x for x in range(3, 20) if x % 10]), R.choice([(25, 4), (4, 25), (2, 50), (50, 2), (5, 20)])
        return {'y': 'zahl', 'f': {'text': f'Rechne im Kopf: {p} · {k} · {q}'}, 'o': {'wert': p * k * q}, 'c': f'{p} * {k} * {q}',
                'w': f'Vertauschen: {p} · {q} = {p * q}. Dann {p * q} · {k} = {zt(p * q * k)}.', 'h': f'Welche zwei Zahlen ergeben zusammen eine glatte Zahl?'}
    if s == 2:
        art = R.choice(['fast', 'fast', 'negativ', 'geteilt', 'weg'])
        if art == 'fast':
            a = R.randint(3, 9); b = R.choice([99, 98, 49, 199, 101, 102, 51])
            r = b - (b % 50 if b % 50 < 25 else b % 50 - 50)
            d = b - r
            return {'y': 'zahl', 'f': {'text': f'Rechne im Kopf: {a} · {b}'}, 'o': {'wert': a * b}, 'c': f'{a} * {b}',
                    'w': f'{b} = {r} {"+" if d > 0 else "−"} {abs(d)}. {a} · {r} = {zt(a * r)}, {a} · {abs(d)} = {a * abs(d)}. {zt(a * r)} {"+" if d > 0 else "−"} {a * abs(d)} = {zt(a * b)}.',
                    'h': f'{b} liegt nahe bei {r}. Rechne erst mit {r}, dann korrigiere.'}
        if art == 'negativ':
            a, b = R.choice([-1, 1]) * R.randint(3, 9), R.choice([-1, 1]) * R.choice([x for x in range(12, 40) if x % 10])
            if a > 0 and b > 0: a = -a
            return {'y': 'zahl', 'f': {'text': f'Rechne im Kopf: {kl(a)} · {kl(b)}'}, 'o': {'wert': a * b}, 'c': f'({a}) * ({b})',
                    'w': f'Erst ohne Vorzeichen zerlegen: {abs(a)} · {abs(b)} = {abs(a) * (abs(b) // 10 * 10)} + {abs(a) * (abs(b) % 10)} = {abs(a * b)}. '
                         f'{"Verschiedene" if (a < 0) != (b < 0) else "Gleiche"} Vorzeichen: {zt(a * b)}.',
                    'h': 'Rechne zuerst ohne Vorzeichen. Überlege dann das Vorzeichen.'}
        if art == 'geteilt':
            a, q = R.randint(3, 9), R.randint(11, 99)
            n = a * q * 10
            neg = R.random() < .5
            return {'y': 'zahl', 'f': {'text': f'Rechne im Kopf: {kl(-n if neg else n)} : {a}'}, 'o': {'wert': -q * 10 if neg else q * 10}, 'c': f'({-n if neg else n}) / {a}',
                    'w': f'Ohne die Null: {a * q} : {a} = {q}. Die Null kommt wieder dazu: {q * 10}.' + (' Minus durch plus ergibt minus.' if neg else ''),
                    'h': 'Lass die Null am Ende weg, teile, und hänge sie wieder an.'}
        a, b = R.randint(3, 9), R.choice([x for x in range(21, 99) if x % 10 not in (0, 1, 9)])
        z, e = b // 10 * 10, b % 10
        r = f'{a} · {z} + {a} · {e}'
        opts, i = m18(R, r, [f'{a} · {z} + {e}', f'{a} · {z} · {e}', f'{a} + {z} · {e}'])
        return {'y': 'auswahl', 'f': {'text': f'Welcher Rechenweg passt zu {a} · {b}?'}, 'a': opts, 'o': {'index': i},
                'w': f'{b} = {z} + {e}. Jeder Teil wird mal {a} genommen: {r} = {a * z} + {a * e} = {a * b}. Bei „{a} · {z} + {e}“ fehlt das „mal {a}“ bei den Einern.',
                'h': 'Beide Teile der zerlegten Zahl müssen mal genommen werden.'}
    art = R.choice(['ausklammern', 'vier', 'neun', 'fehler'])
    if art == 'ausklammern':
        a = R.randint(3, 19); b = R.randint(11, 89); c = 100 - b
        return {'y': 'zahl', 'f': {'text': f'Rechne im Kopf: {a} · {b} + {a} · {c}'}, 'o': {'wert': a * 100}, 'c': f'{a} * {b} + {a} * {c}',
                'w': f'Ausklammern: {a} · ({b} + {c}) = {a} · 100 = {zt(a * 100)}.', 'h': f'Beide Produkte haben den Faktor {a}. Was ergibt {b} + {c}?'}
    if art == 'vier':
        k = R.randint(3, 19) * 4; neg = R.random() < .6
        return {'y': 'zahl', 'f': {'text': f'Rechne im Kopf: {"(−25)" if neg else "25"} · {k}'}, 'o': {'wert': -25 * k if neg else 25 * k}, 'c': f'{-25 if neg else 25} * {k}',
                'w': f'{k} = 4 · {k // 4}. 25 · 4 = 100, also 100 · {k // 4} = {zt(25 * k)}.' + (' Mit dem Minus: ' + zt(-25 * k) + '.' if neg else ''),
                'h': 'Zerlege die zweite Zahl so, dass ein Faktor 4 entsteht.'}
    if art == 'neun':
        a = R.randint(3, 9); b = R.choice([999, 990, 1001, 1010])
        return {'y': 'zahl', 'f': {'text': f'Rechne im Kopf: {a} · {zt(b)}'}, 'o': {'wert': a * b}, 'c': f'{a} * {b}',
                'w': f'{zt(b)} = 1 000 {"−" if b < 1000 else "+"} {abs(b - 1000)}. {a} · 1 000 = {zt(a * 1000)}, {a} · {abs(b - 1000)} = {a * abs(b - 1000)}. Ergebnis {zt(a * b)}.',
                'h': f'{zt(b)} liegt nahe bei 1 000.'}
    a, b = R.randint(3, 9), R.choice([x for x in range(21, 99) if x % 10 not in (0, 1)])
    z, e = b // 10 * 10, b % 10
    f = a * z + e
    opts, i = m18(R, f'Die {e} Einer wurden nicht mal {a} genommen. Richtig ist {a * b}.',
                  ['Nichts, das stimmt.', f'Es hätte {a} · {z} − {e} heißen müssen: {a * z - e}.', f'Die Zehner sind falsch. Richtig ist {zt(a * z * 10 + a * e)}.'])
    return {'y': 'auswahl', 'f': {'text': f'Jemand rechnet im Kopf {a} · {b} = {a} · {z} + {e} = {f}. Was ist falsch?'}, 'a': opts, 'o': {'index': i},
            'w': f'Richtig: {a} · {b} = {a} · {z} + {a} · {e} = {a * z} + {a * e} = {a * b}. Jeder Teil der Zerlegung muss mal {a} genommen werden.',
            'h': 'Rechne selbst mit Zerlegen nach. Wurden beide Teile mal genommen?'}


KARTE_KOPF = {
    'lernziel': 'kopfrechnen', 'titel': 'Geschickt im Kopf rechnen',
    'einstieg': 'Sechs Kinder fahren in den Freizeitpark, jede Karte kostet 47 €. An der Kasse hast du keinen Stift. Mit einem Trick rechnest du ⟦im Kopf⟧.',
    'woerter': [['im Kopf', 'ohne Stift und Taschenrechner, nur mit Denken'], ['zerlegen', 'eine Zahl in leichte Teile aufteilen: 47 = 40 + 7']],
    'bild': {'typ': 'tabelle', 'kopf': ['Teil', 'Rechnung', 'Euro'], 'zeilen': [['40 €', '6 · 40', '?'], ['7 €', '6 · 7', '?'], ['zusammen', '6 · 47', '?']]},
    'schritte': [
        {'text': '47 zerlegen: 47 = 40 + 7.'},
        {'text': 'Sechs Karten zu 40 €: 6 · 40 = 240.', 'bild': {'zeilen': [['40 €', '6 · 40', '240'], ['7 €', '6 · 7', '?'], ['zusammen', '6 · 47', '?']]}},
        {'text': 'Dazu sechsmal 7 €: 6 · 7 = 42.', 'bild': {'zeilen': [['40 €', '6 · 40', '240'], ['7 €', '6 · 7', '42'], ['zusammen', '6 · 47', '?']]}},
        {'text': 'Zusammen: 240 + 42 = ⟦282 €⟧.', 'bild': {'zeilen': [['40 €', '6 · 40', '240'], ['7 €', '6 · 7', '42'], ['zusammen', '240 + 42', '282']]}}],
    'fehler': '6 · 47 = 240 + 7 ist falsch. Jede der sechs Karten kostet 7 € mehr, nicht nur eine.',
    'fehler_bild': {'zeilen': [['falsch', '240 + 7', '247'], ['richtig', '240 + 42', '282'], ['Abstand', '5 · 7', '35']]},
    'regel': 'Zerlege eine Zahl in ⟦leichte Teile⟧ und rechne jeden Teil. Auch praktisch: 25 · 4 = 100 und 98 = 100 − 2.',
}
FEST_KOPF = [
    # Prüfungsvorbild: Klammer-Term im Kopf (Jahrgangsstufentest 6 Realschule Bayern 2025, Nr. 1a „4 · (75 − 15)“)
    Z(3, 'Rechne im Kopf auf zwei Wegen und vergleiche: 8 · (125 − 25)', '8 * (125 - 25)',
      'Weg 1: Klammer zuerst, 125 − 25 = 100, 8 · 100 = 800. Weg 2: verteilen, 8 · 125 − 8 · 25 = 1 000 − 200 = 800. Beide Wege ergeben 800.',
      'Rechne zuerst die Klammer aus – oder verteile die 8 auf beide Zahlen.'),
    # Prüfungsvorbild: Rechenvorteil durch Vertauschen (ISB, Illustrierende Aufgaben LehrplanPLUS M6 1.3, Aufgabe 1 „im Kopf rechnen“)
    Z(3, 'Rechne im Kopf geschickt: (−37) · 4 · (−25)', '(-37) * 4 * (-25)',
      'Vertauschen: 4 · (−25) = −100. Dann (−37) · (−100) = 3 700. Minus mal minus ergibt plus.',
      'Welche zwei Faktoren ergeben zusammen 100 oder −100?'),
    # Knobelaufgabe: einen Kopfrechentrick prüfen und übertragen
    wahl(3, 'Ein Trick: 15 · 15 = 10 · 20 + 25 = 225. Welche Rechnung liefert nach demselben Trick 35 · 35?',
         ['30 · 40 + 25', '30 · 30 + 25', '35 · 30 + 25', '40 · 40 − 25'], lambda o: rw(o) == 35 * 35 and o.startswith('30 · 40'),
         'Beim Trick nimmt man die Zehnerzahl einmal kleiner (10) und einmal größer (20) und hängt 25 an. Bei 35: 30 · 40 + 25 = 1 200 + 25 = 1 225 = 35 · 35.',
         'Schau, wie aus 15 die Zahlen 10 und 20 werden.'),
]


# --- Lernkarte umkehraufgabe_mal ---
def _glm(form, a, x):
    """Gleichung zu Form und Lösung x; gibt (text, b, c-Ausdruck für x)."""
    if form == 'ax': b = a * x; return f'{kl(a)} · x = {zt(b)}', b, f'({b}) / ({a})'
    if form == 'xa': b = x * a; return f'x · {kl(a)} = {zt(b)}', b, f'({b}) / ({a})'
    if form == 'x:a': b = x // a; return f'x : {kl(a)} = {zt(b)}', b, f'({b}) * ({a})'
    b = a // x; return f'{kl(a)} : x = {zt(b)}', b, f'({a}) / ({b})'


def _umkm_weg(form, a, b, x):
    if form in ('ax', 'xa'):
        return f'Umkehraufgabe von „mal {kl(a)}“ ist „geteilt durch {kl(a)}“: x = {kl(b)} : {kl(a)} = {zt(x)}. Probe: {kl(a)} · {kl(x)} = {zt(b)} ✓'
    if form == 'x:a':
        return f'Umkehraufgabe von „geteilt durch {kl(a)}“ ist „mal {kl(a)}“: x = {kl(b)} · {kl(a)} = {zt(x)}. Probe: {kl(x)} : {kl(a)} = {zt(b)} ✓'
    return f'{zt(a)} wird durch x geteilt und es kommt {zt(b)} heraus. Also ist x = {kl(a)} : {kl(b)} = {zt(x)}. Probe: {kl(a)} : {kl(x)} = {zt(b)} ✓'


H_UMKM = {'ax': 'Kehre mal mit geteilt um. Denk an die Vorzeichenregel.', 'xa': 'Kehre mal mit geteilt um. Denk an die Vorzeichenregel.',
          'x:a': 'Kehre geteilt mit mal um. Denk an die Vorzeichenregel.', 'a:x': 'Frage: Durch welche Zahl muss ich teilen? Rechne die erste Zahl geteilt durch das Ergebnis.'}


def g_umkm(R, s):
    if s == 2 and R.random() < .2:
        form = R.choice(['ax', 'x:a'])
        a, x = R.choice([-1, 1]) * R.randint(3, 12), R.choice([-1, 1]) * R.randint(2, 12)
        if a > 0 and x > 0: x = -x
        if form == 'x:a': a = abs(a) if R.random() < .5 else a
        text, b, c = _glm(form, a, x * a if form == 'x:a' else x)
        if form == 'x:a': x = x * a
        r = f'x = {kl(b)} : {kl(a)}' if form == 'ax' else f'x = {kl(b)} · {kl(a)}'
        f = [f'x = {kl(b)} · {kl(a)}' if form == 'ax' else f'x = {kl(b)} : {kl(a)}', f'x = {kl(b)} − {kl(a)}', f'x = {kl(a)} : {kl(b)}' if form == 'ax' else f'x = {kl(b)} + {kl(a)}']
        if len(set([r] + f)) < 4: return g_umkm(R, s)
        opts, i = m18(R, r, f)
        return {'y': 'auswahl', 'f': {'text': f'Welche Umkehraufgabe löst die Gleichung {text}?'}, 'a': opts, 'o': {'index': i},
                'w': _umkm_weg(form, a, b, x), 'h': 'Mal kehrt man mit geteilt um, geteilt mit mal.'}
    if s == 3 and R.random() < .5:
        art = R.choice(['sach_rate', 'sach_temp', 'probieren', 'zwei'])
        if art == 'sach_rate':
            n, r = R.randint(3, 12), R.randint(2, 15) * 5
            return {'y': 'zahl', 'f': {'text': f'Ein Konto steht nach {n} gleichen Abbuchungen bei {zt(-n * r)} €. Vorher war es bei 0 €. Löse {n} · x = {zt(-n * r)}: Wie groß war jede Abbuchung als Zahl?'},
                    'o': {'wert': -r, 'einheit': '€'}, 'c': f'({-n * r}) / {n}', 'w': _umkm_weg('ax', n, -n * r, -r) + f' Jede Abbuchung war {r} €.',
                    'h': 'Kehre mal mit geteilt um. Eine Abbuchung ist eine negative Zahl.'}
        if art == 'sach_temp':
            n, d = R.randint(3, 8), R.randint(2, 6)
            return {'y': 'zahl', 'f': {'text': f'In einer Kältekammer ändert sich die Temperatur jede Stunde gleich stark. Nach {n} Stunden hat sie sich um {zt(-n * d)} Grad geändert. Löse {n} · x = {zt(-n * d)}: Um wie viel Grad ändert sie sich pro Stunde?'},
                    'o': {'wert': -d, 'einheit': '°C'}, 'c': f'({-n * d}) / {n}', 'w': _umkm_weg('ax', n, -n * d, -d) + f' Es wird jede Stunde {d} Grad kälter.',
                    'h': 'Kehre mal mit geteilt um. Kälter heißt: negative Änderung.'}
        if art == 'probieren':
            a, x = R.choice([-1, 1]) * R.randint(24, 96), R.choice([-1, 1]) * R.randint(2, 12)
            if a % x or a > 0 and x > 0: return g_umkm(R, s)
            b = a // x
            kand = sorted({x, -x, b, a * b if abs(a * b) < 1000 else x + 1} - {0})
            if x not in kand or len(kand) < 3: return g_umkm(R, s)
            opts, i = m18(R, zt(x), [zt(k) for k in kand if k != x][:3])
            return {'y': 'auswahl', 'f': {'text': f'Welche Zahl ist eine Lösung von {zt(a)} : x = {zt(b)}? Probiere die Zahlen aus.'}, 'a': opts, 'o': {'index': i},
                    'w': f'Einsetzen: {kl(a)} : {kl(x)} = {zt(a // x)} ✓. ' + _umkm_weg('a:x', a, b, x), 'h': 'Setze jede Zahl für x ein und rechne nach.'}
        a, x, d = R.randint(2, 6), R.choice([-1, 1]) * R.randint(2, 12), R.randint(3, 20)
        b = a * x + d
        return {'y': 'zahl', 'f': {'text': f'Löse die Gleichung {a} · x + {d} = {zt(b)}. Wie groß ist x?'}, 'o': {'wert': x}, 'c': f'(({b}) - {d}) / {a}',
                'w': f'Rückwärts, den letzten Schritt zuerst: {zt(b)} − {d} = {zt(b - d)}. Dann {kl(b - d)} : {a} = {zt(x)}. Probe: {a} · {kl(x)} + {d} = {zt(b)} ✓',
                'h': f'Kehre zuerst das „+ {d}“ um, danach das „mal {a}“.'}
    g = {1: 9, 2: 14, 3: 20}[s]
    form = R.choice(['ax', 'x:a'] if s == 1 else ['ax', 'xa', 'x:a', 'a:x'] + (['a:x'] if s == 3 else []))
    for _ in range(300):
        a, x = R.choice([-1, 1]) * R.randint(2, g), R.choice([-1, 1]) * R.randint(2, g)
        if a > 0 and x > 0: continue
        if form == 'x:a':
            x = x * a; text, b, c = _glm(form, a, x)
        elif form == 'a:x':
            a = a * x; text, b, c = _glm(form, a, x)
        else:
            text, b, c = _glm(form, a, x)
        break
    return {'y': 'zahl', 'f': {'text': f'Löse die Gleichung {text}. Wie groß ist x?'}, 'o': {'wert': x}, 'c': c,
            'w': _umkm_weg(form, a, b, x), 'h': H_UMKM[form]}


KARTE_UMKM = {
    'lernziel': 'umkehraufgabe_mal', 'titel': 'Mal- und Geteilt-Gleichungen lösen',
    'einstieg': 'Ein Taucher sinkt jede Minute gleich viel und ist nach 6 Minuten bei −48 m. Wie viele Meter sind es pro Minute? Mit x für diese Zahl heißt die ⟦Gleichung⟧ 6 · x = −48.',
    'woerter': [['Gleichung', 'zwei Seiten mit Gleichheitszeichen, eine Zahl ist noch unbekannt'], ['x', 'steht für die gesuchte Zahl, wie ein leeres Kästchen'],
                ['Umkehraufgabe', 'die Rechnung rückwärts: aus mal wird geteilt, aus geteilt wird mal']],
    'bild': {'typ': 'zahlenstrahl', 'start': -48, 'ende': 0, 'abschnitte': 6, 'beschriftet': 'alle'},
    'schritte': [
        {'text': 'Die Gleichung heißt 6 · x = −48. Gesucht ist x.', 'bild': {'punkte': [{'wert': -48, 'name': 'nach 6 min'}]}},
        {'text': 'Umkehraufgabe: Aus „mal 6“ wird „geteilt durch 6“.',
         'bild': {'boegen': [{'von': 0, 'bis': -8}, {'von': -8, 'bis': -16}, {'von': -16, 'bis': -24}, {'von': -24, 'bis': -32}, {'von': -32, 'bis': -40}, {'von': -40, 'bis': -48}]}},
        {'text': 'x = (−48) : 6 = ⟦−8⟧. Er sinkt 8 m pro Minute.', 'bild': {'punkte': [{'wert': -8, 'name': '1 min'}, {'wert': -48, 'name': 'nach 6 min'}]}},
        {'text': 'Probe: 6 · (−8) = −48. Die Gleichung stimmt.'}],
    'fehler': 'x = (−48) · 6 ist falsch. Dann wäre der Taucher bei −288 m. Mal kehrst du mit geteilt um.',
    'regel': 'Mal kehrst du mit ⟦geteilt⟧ um, geteilt mit mal. Bei 12 : x = −3 fragst du: 12 geteilt durch was?',
}
FEST_UMKM = [
    # Prüfungsvorbild: Lücke in einer Division ergänzen (Jahrgangsstufentest 6 Realschule Bayern 2024, Nr. 7 „__ : __ = −70“)
    L(3, 'Ergänze die Lücke so, dass die Rechnung stimmt: □ : (−6) = −70', '□ : (−6) = −70', 'Trage die fehlende Zahl ein (mit Minus, falls negativ).',
      ['(-70) * (-6)'], 'Umkehraufgabe: □ = (−70) · (−6) = 420. Probe: 420 : (−6) = −70 ✓', 'Kehre „geteilt durch (−6)“ mit „mal (−6)“ um.'),
    # Prüfungsvorbild: Lücke in einem Klammer-Term (Jahrgangsstufentest 6 Realschule Bayern 2019, Nr. 7 „3 · (__ − 15) = 18“)
    L(3, 'Ergänze die Lücke so, dass die Rechnung stimmt: 4 · (□ − 12) = −20', '4 · (□ − 12) = −20', 'Trage die fehlende Zahl ein (mit Minus, falls negativ).',
      ['(-20) / 4 + 12'], 'Rückwärts: Zuerst „mal 4“ umkehren: (−20) : 4 = −5. Dann „− 12“ umkehren: −5 + 12 = 7. Probe: 4 · (7 − 12) = 4 · (−5) = −20 ✓',
      'Was muss in der Klammer herauskommen? Kehre zuerst das „mal 4“ um.'),
    # Knobelaufgabe: systematisches Probieren mit negativen Zahlen
    Z(3, 'Ich denke mir eine ganze Zahl. Multipliziere ich sie mit −3, erhalte ich dasselbe wie beim Addieren von 8. Welche Zahl ist es?', str(einzig([x for x in range(-50, 51) if x * (-3) == x + 8])),
      'Probieren: x = −2 ergibt (−2) · (−3) = 6 und (−2) + 8 = 6 ✓. Für positive Zahlen ist „mal −3“ negativ, „plus 8“ aber positiv – die Zahl muss negativ sein.',
      'Probiere kleine negative Zahlen aus: −1, −2, −3 …'),
]


# --- Lernkarte schriftlich_geteilt ---
def _dividend(R, d, ziffern, mit_null):
    for _ in range(500):
        q = R.randint(10 ** (ziffern - 1), 10 ** ziffern - 1)
        z = str(q)
        if mit_null != ('0' in z[1:]): continue
        if not mit_null and '0' in z: continue
        return q, q * d
    raise SystemExit('kein Quotient')


def _div_weg(n, d):
    """Kurzer Lösungsweg der schriftlichen Division (Teilschritte)."""
    s, rest, teile, start = str(n), 0, [], True
    for ch in s:
        rest = rest * 10 + int(ch)
        if start and rest < d: continue
        start = False
        q = rest // d
        teile.append(f'{zt(rest)} : {d} = {q}' + (f', Rest {zt(rest - q * d)}' if rest - q * d else ''))
        rest -= q * d
    return '; '.join(teile)


BUSSE = {'n': 0}  # Bus-Aufgabe höchstens zweimal


def g_sdiv(R, s):
    if s == 1:
        d = R.choice([x for x in range(12, 40) if x % 10])
        q, n = _dividend(R, d, 2 if d > 19 else R.choice([2, 3]), False)
        return {'y': 'zahl', 'f': {'text': f'Teile schriftlich: {zt(n)} : {d}'}, 'o': {'wert': q}, 'c': f'{n} / {d}',
                'w': f'{_div_weg(n, d)}. Ergebnis {zt(q)}. Probe: {zt(q)} · {d} = {zt(n)}.', 'h': f'Schreibe dir zuerst die Vielfachen von {d} auf: {d}, {2 * d}, {3 * d} …'}
    if s == 2:
        art = R.choice(['null', 'null', 'rest', 'ueberschlag'])
        if art == 'null':
            d = R.choice([x for x in range(11, 49) if x % 10])
            q, n = _dividend(R, d, 3, True)
            return {'y': 'zahl', 'f': {'text': f'Teile schriftlich: {zt(n)} : {d}'}, 'o': {'wert': q}, 'c': f'{n} / {d}',
                    'w': f'{_div_weg(n, d)}. Ergebnis {zt(q)}. Die 0 im Ergebnis nicht vergessen. Probe: {zt(q)} · {d} = {zt(n)}.',
                    'h': 'Reicht eine heruntergeholte Zahl nicht für den Teiler, schreibst du eine 0 ins Ergebnis.'}
        if art == 'rest':
            d = R.choice([x for x in range(12, 40) if x % 10]); n = R.randint(300, 2000)
            if n % d == 0: return g_sdiv(R, s)
            return {'y': 'zahl', 'f': {'text': f'Teile schriftlich {zt(n)} : {d}. Wie groß ist der Rest?'}, 'o': {'wert': n % d}, 'c': f'{n} % {d}',
                    'w': f'{zt(n)} : {d} = {n // d} Rest {n % d}. Probe: {n // d} · {d} + {n % d} = {zt(n)}.', 'h': 'Teile wie immer. Was am Ende übrig bleibt, ist der Rest.'}
        d = R.choice([x for x in range(12, 49) if x % 10])
        q, n = _dividend(R, d, 3, R.random() < .5)
        opts, i = m18(R, zt(q), [zt(q * 10), zt(q // 10) if q // 10 else zt(q * 100), zt(q * 100)] if q // 10 else [zt(q * 10), zt(q * 100)])
        e = 10 ** (len(str(n)) - 2)
        nr, dr = (n + e // 2) // e * e, (d + 5) // 10 * 10
        return {'y': 'auswahl', 'f': {'text': f'Welches Ergebnis passt zu {zt(n)} : {d}? Entscheide mit einem Überschlag.'}, 'a': opts, 'o': {'index': i},
                'w': f'Überschlag: {zt(nr)} : {dr} ≈ {zt(nr // dr)}. Das Ergebnis ist also dreistellig. Genau: {zt(n)} : {d} = {zt(q)}.',
                'h': 'Runde beide Zahlen und rechne im Kopf. Wie viele Stellen hat das Ergebnis?'}
    art = R.choice(['drei', 'busse', 'fehler', 'gross'])
    if art == 'busse':
        BUSSE['n'] += 1
        if BUSSE['n'] > 2: art = R.choice(['drei', 'fehler', 'gross'])
    if art == 'drei':
        d = R.choice([125, 250, 112, 115, 135, 225, 150])
        q, n = _dividend(R, d, 3, R.random() < .3)
        return {'y': 'zahl', 'f': {'text': f'Teile schriftlich: {zt(n)} : {d}'}, 'o': {'wert': q}, 'c': f'{n} / {d}',
                'w': f'{_div_weg(n, d)}. Ergebnis {zt(q)}. Probe: {zt(q)} · {d} = {zt(n)}.',
                'h': f'Der Teiler hat drei Stellen. Nimm so viele Ziffern, dass die Zahl größer als {d} ist.'}
    if art == 'busse':
        p = R.choice([48, 52, 56, 45, 60]); n = R.randint(380, 1400)
        if n % p == 0: return g_sdiv(R, s)
        k = n // p + 1
        return {'y': 'zahl', 'f': {'text': f'{zt(n)} Kinder fahren zu einem Sportfest. Ein Bus hat {p} Plätze. Wie viele Busse braucht man mindestens?'},
                'o': {'wert': k}, 'c': f'{n} // {p} + 1',
                'w': f'{zt(n)} : {p} = {n // p} Rest {n % p}. {n // p} Busse sind voll, für die übrigen {n % p} Kinder braucht man noch einen Bus: {k}.',
                'h': 'Teile schriftlich. Was machst du mit den Kindern, die übrig bleiben?'}
    if art == 'fehler':
        d = R.choice([x for x in range(12, 40) if x % 10])
        q, n = _dividend(R, d, 3, True)
        if q % 10 == 0: return g_sdiv(R, s)
        f = int(str(q).replace('0', ''))
        opts, i = m18(R, f'Die 0 im Ergebnis fehlt. Richtig ist {zt(q)}.',
                      ['Nichts, das stimmt.', f'Am Ende fehlt eine 0. Richtig ist {zt(f * 10)}.', f'Es bleibt ein Rest. Richtig ist {zt(f)} Rest 1.'])
        return {'y': 'auswahl', 'f': {'text': f'Jemand rechnet schriftlich {zt(n)} : {d} = {zt(f)}. Was ist falsch?'}, 'a': opts, 'o': {'index': i},
                'w': f'{_div_weg(n, d)}. Richtig ist {zt(q)}. Probe: {zt(q)} · {d} = {zt(n)}. Der Überschlag zeigt: Das Ergebnis muss dreistellig sein.',
                'h': 'Mach die Probe: Ergebnis mal Teiler. Kommt die große Zahl heraus?'}
    d = R.choice([x for x in range(13, 49) if x % 10])
    q, n = _dividend(R, d, 4, R.random() < .5)
    return {'y': 'zahl', 'f': {'text': f'Teile schriftlich: {zt(n)} : {d}'}, 'o': {'wert': q}, 'c': f'{n} / {d}',
            'w': f'{_div_weg(n, d)}. Ergebnis {zt(q)}. Probe: {zt(q)} · {d} = {zt(n)}.', 'h': f'Schreibe dir die Vielfachen von {d} auf. Achte auf Nullen im Ergebnis.'}


SDIV_LEER = [['74 : 24', '', '', ''], ['28 : 24', '', '', ''], ['48 : 24', '', '', '']]
KARTE_SDIV = {
    'lernziel': 'schriftlich_geteilt', 'titel': 'Schriftlich teilen: Teiler über 10',
    'einstieg': 'Ein Konzert bringt 7 488 € ein. Das Geld wird gerecht an 24 Musikerinnen und Musiker verteilt. Bei einem zweistelligen ⟦Teiler⟧ hilft das Einmaleins allein nicht.',
    'woerter': [['Teiler', 'die Zahl, durch die du teilst: bei 7 488 : 24 ist es 24'], ['herunterholen', 'die nächste Ziffer der großen Zahl neben den Rest schreiben']],
    'bild': {'typ': 'tabelle', 'kopf': ['Teil', 'Ziffer', 'mal 24', 'Rest'], 'zeilen': SDIV_LEER},
    'schritte': [
        {'text': '7 : 24 geht nicht. Nimm die ersten zwei Ziffern: 74.'},
        {'text': '74 : 24 = 3, denn 3 · 24 = 72. Es bleibt Rest 2.',
         'bild': {'zeilen': [['74 : 24', '3', '72', '2'], SDIV_LEER[1], SDIV_LEER[2]]}},
        {'text': 'Die 8 herunterholen: 28 : 24 = 1, Rest 4.', 'bild': {'zeilen': [['74 : 24', '3', '72', '2'], ['28 : 24', '1', '24', '4'], SDIV_LEER[2]]}},
        {'text': 'Die letzte 8 herunterholen: 48 : 24 = 2. Das ergibt ⟦312⟧ €.',
         'bild': {'zeilen': [['74 : 24', '3', '72', '2'], ['28 : 24', '1', '24', '4'], ['48 : 24', '2', '48', '0']]}},
        {'text': 'Überschlag: 7 500 : 25 = 300. Das passt.'}],
    'fehler': 'Die 1 vergessen ergibt 32 € pro Person. Der Überschlag sagt etwa 300 €. Jede heruntergeholte Ziffer bringt eine Ziffer im Ergebnis.',
    'fehler_bild': {'zeilen': [['74 : 24', '3', '72', '2'], ['28 : 24', 'fehlt', '', ''], ['48 : 24', '2', '48', '0']]},
    'regel': 'Teilen, malnehmen, abziehen, ⟦herunterholen⟧ – bis keine Ziffer übrig ist. Tipp: Schreib dir die Vielfachen des Teilers auf.',
}
assert 7488 // 24 == 312 and 7488 % 24 == 0
FEST_SDIV = [
    # Prüfungsvorbild: schriftliche Division mit zweistelligem Teiler (Jahrgangsstufentest 6 Realschule Bayern 2016 Nr. 2, 2021 Nr. 1a, 2025 Nr. 1b)
    Z(3, 'Teile schriftlich: 23 715 : 15', '23715 / 15', '23 : 15 = 1, Rest 8; 87 : 15 = 5, Rest 12; 121 : 15 = 8, Rest 1; 15 : 15 = 1. Ergebnis 1 581. Probe: 1 581 · 15 = 23 715.',
      'Schreibe dir die Vielfachen von 15 auf: 15, 30, 45, 60 …'),
    # Prüfungsvorbild: erst teilen, dann vervielfachen (Jahrgangsstufentest 6 Realschule Bayern 2020, Nr. 13 „25 Güterwagen – 30 Güterwagen“)
    Z(3, '18 gleich schwere Kisten wiegen zusammen 846 kg. Wie viel wiegen 25 solche Kisten?', '846 / 18 * 25',
      'Eine Kiste: 846 : 18 = 47 kg. 25 Kisten: 47 · 25 = 1 175 kg.', 'Rechne zuerst aus, wie schwer eine Kiste ist.', einheit='kg'),
    # Knobelaufgabe: mit Division und Rest rückwärts denken
    Z(3, 'Welche ist die größte vierstellige Zahl, die sich ohne Rest durch 37 teilen lässt?', '37 * (9999 // 37)',
      '9 999 : 37 = 270 Rest 9. Zieht man den Rest ab, geht es auf: 9 999 − 9 = 9 990 = 37 · 270.', 'Teile die größte vierstellige Zahl durch 37. Was machst du mit dem Rest?'),
]


# --- Lernkarte sach ---
def g_sach(R, s):
    if s == 1:
        art = R.choice(['kasse', 'temp', 'eintritt'])
        if art == 'kasse':
            k, n, p, a = R.randint(2, 9) * 10, R.randint(18, 30), R.choice([4, 5, 6, 8]), R.randint(8, 25) * 10
            e = k + n * p - a
            if e < 0: return g_sach(R, s)
            return {'y': 'zahl', 'f': {'text': f'In der Klassenkasse sind {k} €. {n} Kinder zahlen je {p} € ein. Dann kostet der Ausflug {a} €. Wie viel Euro bleiben in der Kasse?'},
                    'o': {'wert': e, 'einheit': '€'}, 'c': f'{k} + {n} * {p} - {a}',
                    'w': f'Vorwärts: Einzahlung {n} · {p} = {n * p} €. {k} + {n * p} = {k + n * p} €. Nach dem Ausflug: {k + n * p} − {a} = {e} €.',
                    'h': 'Rechne der Reihe nach: erst einzahlen, dann bezahlen.'}
        if art == 'temp':
            t, h, d = -R.randint(5, 20), R.randint(3, 6), R.randint(2, 5)
            return {'y': 'zahl', 'f': {'text': f'Morgens zeigt das Thermometer {zt(t)} °C. Dann wird es {h} Stunden lang jede Stunde {d} Grad wärmer. Wie warm ist es danach?'},
                    'o': {'wert': t + h * d, 'einheit': '°C'}, 'c': f'({t}) + {h} * {d}',
                    'w': f'Wärmer um {h} · {d} = {h * d} Grad. {kl(t)} + {h * d} = {zt(t + h * d)} °C.', 'h': 'Rechne zuerst aus, um wie viel Grad es insgesamt wärmer wird.'}
        n, p, m = R.randint(80, 250), R.choice([6, 7, 8, 9]), R.randint(2, 6) * 100
        return {'y': 'zahl', 'f': {'text': f'Ein Schulkino verkauft {n} Karten zu je {p} €. Die Filmmiete kostet {m} €. Wie viel Euro Gewinn bleiben?'},
                'o': {'wert': n * p - m, 'einheit': '€'}, 'c': f'{n} * {p} - {m}',
                'w': f'Einnahmen: {n} · {p} = {zt(n * p)} €. Gewinn: {zt(n * p)} − {m} = {zt(n * p - m)} €.', 'h': 'Erst die Einnahmen ausrechnen, dann die Miete abziehen.'}
    if s == 2:
        art = R.choice(['kasse_r', 'raetsel', 'term', 'aufzug'])
        if art == 'kasse_r':
            a, g, q = R.randint(8, 30) * 10, R.choice([3, 4, 5, 6]), R.randint(15, 60)
            return {'y': 'zahl', 'f': {'text': f'Aus der Klassenkasse gehen {a} € an den Bus. Den Rest teilen {g} Gruppen gleich auf, jede bekommt {q} €. Wie viel Euro waren in der Kasse?'},
                    'o': {'wert': q * g + a, 'einheit': '€'}, 'c': f'{q} * {g} + {a}',
                    'w': f'Rückwärts, den letzten Schritt zuerst: {q} · {g} = {q * g} €. Dazu der Bus: {q * g} + {a} = {q * g + a} €. Probe: {q * g + a} − {a} = {q * g}, {q * g} : {g} = {q}.',
                    'h': 'Arbeite rückwärts: Kehre zuerst das Teilen um, dann das Bezahlen.'}
        if art == 'raetsel':
            a, b, x = R.randint(2, 9), R.randint(3, 30), R.randint(2, 20)
            c = a * x + b
            return {'y': 'zahl', 'f': {'text': f'Ich denke mir eine Zahl. Ich multipliziere sie mit {a} und addiere {b}. Ich erhalte {c}. Welche Zahl habe ich mir gedacht?'},
                    'o': {'wert': x}, 'c': f'({c} - {b}) / {a}',
                    'w': f'Rückwärts: {c} − {b} = {c - b}, dann {c - b} : {a} = {x}. Probe: {x} · {a} + {b} = {c} ✓', 'h': 'Kehre die Schritte in umgekehrter Reihenfolge um.'}
        if art == 'term':
            n, p, a = R.randint(20, 40), R.randint(3, 9), R.randint(20, 90)
            r = f'{n} · {p} − {a}'
            f = [f'{n} · ({p} − {a})', f'({n} + {p}) − {a}', f'{n} · {p} + {a}']
            opts, i = m18(R, r, f)
            return {'y': 'auswahl', 'f': {'text': f'Ein Fest: {n} Gäste zahlen je {p} € Eintritt. Davon gehen {a} € für Getränke ab. Welcher Term berechnet, was übrig bleibt?'},
                    'a': opts, 'o': {'index': i}, 'w': f'Einnahmen: {n} · {p}. Davon gehen {a} € ab: {r} = {n * p - a} €.',
                    'h': 'Was wird zuerst ausgerechnet, was danach abgezogen?'}
        e, k, u, o = R.randint(-3, 8), R.randint(2, 4), R.randint(2, 5), R.randint(3, 9)
        st = e - o + k * u
        return {'y': 'zahl', 'f': {'text': f'Ein Aufzug fährt {k}-mal je {u} Stockwerke nach unten und danach {o} Stockwerke nach oben. Er hält in Stockwerk {zt(e)}. In welchem Stockwerk ist er losgefahren?'},
                'o': {'wert': st}, 'c': f'({e}) - {o} + {k} * {u}',
                'w': f'Rückwärts: Die {o} nach oben werden zu „{o} nach unten“: {zt(e)} − {o} = {zt(e - o)}. Die {k} · {u} = {k * u} nach unten werden zu „nach oben“: {zt(e - o)} + {k * u} = {zt(st)}.',
                'h': 'Arbeite rückwärts: nach oben wird nach unten und umgekehrt.'}
    art = R.choice(['raetsel_neg', 'kuehl', 'konto'])
    if art == 'raetsel_neg':
        a, b, x = -R.randint(2, 6), R.randint(5, 30), R.choice([-1, 1]) * R.randint(2, 15)
        c = a * x + b
        return {'y': 'zahl', 'f': {'text': f'Ich denke mir eine Zahl. Ich multipliziere sie mit {kl(a)} und addiere {b}. Ich erhalte {zt(c)}. Welche Zahl habe ich mir gedacht?'},
                'o': {'wert': x}, 'c': f'(({c}) - {b}) / ({a})',
                'w': f'Rückwärts: {zt(c)} − {b} = {zt(c - b)}, dann {kl(c - b)} : {kl(a)} = {zt(x)}. Probe: {kl(x)} · {kl(a)} + {b} = {zt(c)} ✓',
                'h': 'Kehre die Schritte in umgekehrter Reihenfolge um. Achte auf die Vorzeichen.'}
    if art == 'kuehl':
        h, d, w, e = R.randint(3, 6), R.randint(3, 6), R.randint(2, 8), -R.randint(12, 24)
        st = e - w + h * d
        return {'y': 'zahl', 'f': {'text': f'Ein Kühlraum wird {h} Stunden lang jede Stunde {d} Grad kälter. Danach wird er {w} Grad wärmer und hat jetzt {zt(e)} °C. Wie kalt war er am Anfang?'},
                'o': {'wert': st, 'einheit': '°C'}, 'c': f'({e}) - {w} + {h} * {d}',
                'w': f'Rückwärts: {zt(e)} − {w} = {zt(e - w)} °C. Dann die {h} · {d} = {h * d} Grad Abkühlung umkehren: {zt(e - w)} + {h * d} = {zt(st)} °C. Probe: {zt(st)} − {h * d} + {w} = {zt(e)} ✓',
                'h': 'Arbeite rückwärts: aus wärmer wird kälter, aus kälter wird wärmer.'}
    r, n, ein, e = R.randint(2, 6) * 5, R.randint(3, 8), R.randint(4, 12) * 10, -R.randint(2, 12) * 5
    st = e - ein + n * r
    return {'y': 'zahl', 'f': {'text': f'Von einem Konto werden {n}-mal je {r} € abgebucht. Dann werden {ein} € eingezahlt. Jetzt steht es bei {zt(e)} €. Wie war der Kontostand am Anfang?'},
            'o': {'wert': st, 'einheit': '€'}, 'c': f'({e}) - {ein} + {n} * {r}',
            'w': f'Rückwärts: {zt(e)} − {ein} = {zt(e - ein)} €. Die Abbuchungen {n} · {r} = {n * r} € kommen wieder dazu: {zt(e - ein)} + {n * r} = {zt(st)} €.',
            'h': 'Kehre zuerst das Einzahlen um, dann die Abbuchungen.'}


SACH_KOPF = ['', 'vorwärts', 'rückwärts']
KARTE_SACH = {
    'lernziel': 'sach', 'titel': 'Sachaufgaben: vorwärts und rückwärts',
    'einstieg': 'Aus der Klassenkasse gehen 180 € an den Bus. Den Rest teilen 4 Gruppen, jede bekommt 35 €. Den Anfangsbetrag findest du durch ⟦Rückwärtsarbeiten⟧.',
    'woerter': [['Rückwärtsarbeiten', 'vom Ende aus jeden Schritt umkehren, bis du beim Anfang bist'], ['Probe', 'nachrechnen, ob das Ergebnis zur Geschichte passt']],
    'bild': {'typ': 'tabelle', 'kopf': SACH_KOPF, 'zeilen': [['Kasse', '?', '?'], ['Bus', '− 180 €', ''], ['Gruppen', ': 4', ''], ['je Gruppe', '35 €', '35 €']]},
    'schritte': [
        {'text': 'Vorwärts: Kasse minus 180 €, dann geteilt durch 4. Das ergibt 35 €.'},
        {'text': 'Rückwärts beginnst du am Ende: 35 € · 4 = 140 €.',
         'bild': {'zeilen': [['Kasse', '?', '?'], ['Bus', '− 180 €', ''], ['Gruppen', ': 4', '· 4 = 140 €'], ['je Gruppe', '35 €', '35 €']]}},
        {'text': 'Dann kommen die 180 € für den Bus wieder dazu.',
         'bild': {'zeilen': [['Kasse', '?', '?'], ['Bus', '− 180 €', '+ 180 €'], ['Gruppen', ': 4', '· 4 = 140 €'], ['je Gruppe', '35 €', '35 €']]}},
        {'text': '140 + 180 = 320. In der Kasse waren ⟦320 €⟧.',
         'bild': {'zeilen': [['Kasse', '?', '320 €'], ['Bus', '− 180 €', '+ 180 €'], ['Gruppen', ': 4', '· 4 = 140 €'], ['je Gruppe', '35 €', '35 €']]}},
        {'text': 'Probe: 320 − 180 = 140 und 140 : 4 = 35. Passt.'}],
    'fehler': 'Falsche Reihenfolge: 35 + 180 = 215, dann 215 · 4 = 860 €. Kehre zuerst den letzten Schritt um, hier das Teilen.',
    'fehler_bild': {'zeilen': [['Kasse', '?', '860 €'], ['Bus', '− 180 €', 'zuerst + 180'], ['Gruppen', ': 4', 'dann · 4'], ['je Gruppe', '35 €', 'falsch']]},
    'regel': 'Beim ⟦Rückwärtsarbeiten⟧ beginnst du am Ende. Kehre jeden Schritt um, den letzten zuerst. Mach zum Schluss die Probe.',
}
assert (320 - 180) // 4 == 35
FEST_SACH = [
    # Prüfungsvorbild: Rückwärtsarbeiten mit „die Hälfte und dann noch …“ (Jahrgangsstufentest 8 Realschule Bayern 2005, in SMART Gymnasium Jgst. 6)
    Z(3, 'Ein Kind verschenkt die Hälfte seiner Sticker und danach noch 6 Sticker. Jetzt hat es noch 15 Sticker. Wie viele hatte es am Anfang?', '(15 + 6) * 2',
      'Rückwärts: Vor dem Verschenken der 6 waren es 15 + 6 = 21. Das war die Hälfte, also am Anfang 21 · 2 = 42. Probe: 42 : 2 = 21, 21 − 6 = 15 ✓',
      'Fang am Ende an. Kehre zuerst „noch 6 verschenkt“ um, dann „die Hälfte“.'),
    # Prüfungsvorbild: Term zu einem Text (Jahrgangsstufentest 6 Realschule Bayern 2016: „Multipliziere die Differenz … mit der Summe …“)
    wahl(3, 'Multipliziere die Differenz von 90 und 15 mit der Summe aus 4 und 8. Welcher Term passt?',
         ['(90 − 15) · (4 + 8)', '90 − 15 · 4 + 8', '(90 − 15) · 4 + 8', '90 − 15 · (4 + 8)'], lambda o: o == '(90 − 15) · (4 + 8)',
         'Differenz von 90 und 15: (90 − 15). Summe aus 4 und 8: (4 + 8). Beide werden multipliziert, also braucht jede ihre Klammer: (90 − 15) · (4 + 8) = 75 · 12 = 900.',
         'Differenz und Summe müssen zuerst ausgerechnet werden. Was braucht man dafür?'),
    # Prüfungsvorbild: fehlende Information erkennen (Jahrgangsstufentest 6 Realschule Bayern 2019, Nr. 14)
    wahl(3, 'Eine Klasse fährt mit dem Bus ins Museum. Der Bus kostet 420 €, jedes Kind zahlt 15 €. Welche Angabe fehlt, um zu berechnen, wie viel Geld übrig bleibt?',
         ['wie viele Kinder mitfahren', 'wie lange die Fahrt dauert', 'wie viele Sitzplätze der Bus hat', 'wann das Museum öffnet'], lambda o: o == 'wie viele Kinder mitfahren',
         'Übrig bleibt: Anzahl der Kinder · 15 € − 420 €. Ohne die Anzahl der Kinder kann man nicht rechnen. Die anderen Angaben braucht man für die Rechnung nicht.',
         'Schreibe die Rechnung auf. Welche Zahl fehlt darin?'),
    # Knobelaufgabe: Rückwärtsarbeiten mit negativen Zahlen
    Z(3, 'Ich denke mir eine Zahl, multipliziere sie mit (−2), addiere 15 und teile durch 3. Ich erhalte −1. Welche Zahl habe ich mir gedacht?', '((-1) * 3 - 15) / (-2)',
      'Rückwärts: (−1) · 3 = −3. Dann −3 − 15 = −18. Dann (−18) : (−2) = 9. Probe: 9 · (−2) = −18, −18 + 15 = −3, (−3) : 3 = −1 ✓',
      'Fang hinten an: Kehre zuerst „durch 3“ um, dann „plus 15“, dann „mal (−2)“.'),
]

neue_karte(DATEI, KARTE_KOPF, 'verteilen', 'Geschickt rechnen', 'gesetze', g_kopf, 18_5_4, FEST_KOPF)
neue_karte(DATEI, KARTE_UMKM, 'geteilt_ganz', 'Mal und geteilt mit ganzen Zahlen', ('gleichungen', 'Gleichungen mit mal und geteilt durch Umkehraufgaben lösen'), g_umkm, 18_5_5, FEST_UMKM)
neue_karte(DATEI, KARTE_SDIV, 'schriftlich', 'Große Rechnungen', 'verfahren', g_sdiv, 18_5_6, FEST_SDIV)
neue_karte(DATEI, KARTE_SACH, 'schriftlich_geteilt', ('Anwenden', 'Große Rechnungen'), ('anwenden', 'Sachaufgaben mit allen Grundrechenarten, Vorwärts- und Rückwärtsarbeiten'), g_sach, 18_5_7, FEST_SACH)
# ---- LÜCKEN ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl5, siehe _durchsicht_kl5.py) ----
from _durchsicht_kl5 import Durchsicht, durchsicht_anwenden  # noqa: E402

DS = Durchsicht('zahlen.rechengesetze', 19_5_6)
# a) Stufe 3 ohne neuen Gedanken (längere Rechnung, mehr Faktoren, gleiche Vorlage wie Stufe 2) → Stufe 2
for _lz, _t in [('punkt_strich', 'Berechne 8 + 4 · 8 · 8 − 4.'),
        ('punkt_strich', 'Berechne 588 : 7 : 7 + 4 · 7.'),
        ('klammern', 'Bei welchem Term kommt 88 heraus?'),
        ('vorteil', 'Rechne geschickt: 125 · 6 · 9 · 8'),
        ('vorteil', 'Rechne geschickt: 20 · 3 · 9 · 5'),
        ('vorteil', 'Rechne geschickt: 4 · 50 · 3 · 2'),
        ('vorteil', 'Rechne geschickt: 25 · 25 · 4 · 4'),
        ('vorteil', 'Rechne geschickt: 8 · 23 · 125'),
        ('differenz_summe', 'Rechne geschickt: 43 − 26 + 37 − 34'),
        ('differenz_summe', 'Rechne geschickt: 51 − 34 + 9 − 16'),
        ('differenz_summe', 'Rechne geschickt: 42 − 33 + 18 − 17'),
        ('verteilen', 'Rechne geschickt: 15 · 29 + 85 · 29'),
        ('verteilen', 'Rechne geschickt: 53 · 38 + 47 · 38'),
        ('verteilen', 'Welcher Term ist gleich 3 · (10 + 3)?'),
        ('verteilen', 'Rechne geschickt: 18 · 11 + 18 · 89'),
        ('verteilen', 'Rechne geschickt: 26 · 67 − 26 · 57'),
        ('mal_ganz', 'Ist (−1) · (−6) · (−1) · (−8) positiv oder negativ? Entscheide, ohne auszurechnen.'),
        ('mal_ganz', 'Berechne 2 · 6 · (−5).'),
        ('mal_ganz', 'Ist (−2) · (−8) · (−1) · 2 positiv oder negativ? Entscheide, ohne auszurechnen.'),
        ('mal_ganz', 'Berechne 9 · 6 · (−3).'),
        ('mal_ganz', 'Ist 6 · (−9) · 6 · (−9) positiv oder negativ? Entscheide, ohne auszurechnen.'),
        ('geteilt_ganz', 'Berechne 3 · (−3) : 9.'),
        ('geteilt_ganz', 'Berechne (−72) : (−3) : (−2).'),
        ('geteilt_ganz', 'Berechne 12 : 2 : (−2).'),
        ('geteilt_ganz', 'Berechne 24 : 3 : (−2).'),
        ('geteilt_ganz', 'Berechne (−240) : (−8) : (−6).'),
        ('ueberschlag', 'Im Lager stehen 42 Kisten mit je 34 Flaschen. Überschlage die Zahl der Flaschen: Runde beide Zahlen auf Zehner.'),
        ('ueberschlag', 'Nur ein Ergebnis kann stimmen. Entscheide mit einem Überschlag: 818 · 73 = ?'),
        ('ueberschlag', 'Nur ein Ergebnis kann stimmen. Entscheide mit einem Überschlag: 940 · 59 = ?')]:
    DS.stufe(_lz, _t, 2, enthaelt=lambda x: x['s'] == 3)
# e) Prüfung der Achtzehnten Runde: Das Bild zu Schritt 2 zeigte schon die 6 Sprünge bis −8 und verriet die Lösung → Sprünge erst in Schritt 3
_B6 = [{'von': 0, 'bis': -8}, {'von': -8, 'bis': -16}, {'von': -16, 'bis': -24}, {'von': -24, 'bis': -32}, {'von': -32, 'bis': -40}, {'von': -40, 'bis': -48}]
DS.karte('umkehraufgabe_mal', 'Schritt 2 zeigte schon die sechs Sprünge bis −8 (Lösung verraten); jetzt erscheinen die Sprünge erst in Schritt 3 zusammen mit dem Ergebnis.',
         schritte=[{'text': 'Die Gleichung heißt 6 · x = −48. Gesucht ist x.', 'bild': {'punkte': [{'wert': -48, 'name': 'nach 6 min'}]}},
                   {'text': 'Umkehraufgabe: Aus „mal 6“ wird „geteilt durch 6“.'},
                   {'text': 'x = (−48) : 6 = ⟦−8⟧. Er sinkt 8 m pro Minute.',
                    'bild': {'boegen': _B6, 'punkte': [{'wert': -8, 'name': '1 min'}, {'wert': -48, 'name': 'nach 6 min'}]}},
                   {'text': 'Probe: 6 · (−8) = −48. Die Gleichung stimmt.'}])
# c) Prüfung der Achtzehnten Runde: drei Aufgaben „Fest, Eintritt, Getränke“ direkt hintereinander auf Stufe 2 → zwei davon durch andere Sachaufgaben ersetzt
DS.ersetze('sach', 'Ein Fest: 39 Gäste zahlen je 9 € Eintritt. Davon gehen 44 € für Getränke ab. Welcher Term berechnet, was übrig bleibt?', DS.Z(
    'Ein Verein kauft 12 Bälle zu je 18 €. Weil er so viele nimmt, bekommt er 25 € Rabatt auf den ganzen Einkauf. Wie viel Euro zahlt er?', 191, '12 * 18 - 25',
    'Vorwärts: 12 · 18 = 216 €. Davon gehen 25 € Rabatt ab: 216 − 25 = 191 €.', 'Rechne zuerst den Preis ohne Rabatt aus.', einheit='€'))
DS.ersetze('sach', 'Ein Fest: 30 Gäste zahlen je 9 € Eintritt. Davon gehen 83 € für Getränke ab. Welcher Term berechnet, was übrig bleibt?', DS.Z(
    'Beim Kuchenverkauf werden zuerst 45 € für die Zutaten abgezogen. Den Rest teilen 3 Klassen gleich auf, jede bekommt 52 €. Wie viel Euro wurden eingenommen?', 201, '52 * 3 + 45',
    'Rückwärts, den letzten Schritt zuerst: 52 · 3 = 156 €. Dazu die Zutaten: 156 + 45 = 201 €. Probe: 201 − 45 = 156, 156 : 3 = 52.',
    'Arbeite rückwärts: Kehre zuerst das Teilen um, dann das Abziehen.', einheit='€'))
durchsicht_anwenden(DATEI, DS)
# ---- DURCHSICHT ENDE ----
# ---- STUFEN (Zwanzigste Runde, Zweig stufen-kl5, siehe _stufen_kl5.py und _st5_zahlen_rechengesetze.py) ----
from _stufen_kl5 import stufen_anwenden  # noqa: E402
stufen_anwenden(DATEI, 'zahlen.rechengesetze')
# ---- STUFEN ENDE ----

if __name__ == '__main__':
    schreibe(DATEI, 'zahlen.rechengesetze.json')
