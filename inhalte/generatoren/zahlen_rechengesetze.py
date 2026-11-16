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


if __name__ == '__main__':
    schreibe(DATEI, 'zahlen.rechengesetze.json')
