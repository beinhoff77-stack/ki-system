#!/usr/bin/env python3
"""Prüft den Aufgabenvorrat (rollend-1 bis rollend-4, fachwoerter) auf Fehler, die sich maschinell finden lassen.

Aufruf: python3 -I tools/vorrat_pruefen.py [--kennung K ...]   (ohne Argumente: alles)

Meldungen (jede ist ein HINWEIS zum Nachsehen von Hand, kein Beweis):
  (i)   Lückenwert steht im Aufgabentext, in der Schablone, im Tipp oder im Eingabehinweis
        als Ziffer oder als Zahlwort (null bis zwanzig, kein, nie, einmal, doppelt ...).
  (ii)  Lückenweg ohne Abhängigkeit: keine spätere Lücke hängt an einer früheren, oder die letzte
        Lücke ist eine unabhängige Nebenfrage. Erkennbar nur über die Rechenanker (c) und die
        Satzstellung der Lückensymbole im Text.
  (iii) Fehlbild-Beschreibung nennt eine Rechnung (a + b, a − b, a · b, a : b), die nicht die
        gespeicherte Fehlantwort ergibt (nur bei Zahl- und Lücken-Antworten).
  (iv)  Fehler-Detektiv: Rechnung in einer Zeile vor der Fehlerzeile stimmt nicht, oder die
        Fehlerzeile enthält Rechnungen, die alle stimmen (dann muss der Fehler ein Denkfehler sein).
Grenzen: Wörter ("halbiert", "verdoppelt") und Rechnungen mit Variablen werden nicht ausgewertet;
Zahlwörter in zusammengesetzten Wörtern (Dreieck, Viereck) werden bewusst nicht gezählt.
"""
import ast, glob, json, operator, os, re, sys
from fractions import Fraction

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATEIEN = sorted(glob.glob(os.path.join(WURZEL, 'inhalte/mathe-profi/rollend-[1-4]/*.json')) +
                 glob.glob(os.path.join(WURZEL, 'inhalte/mathe-profi/fachwoerter/*.json')))
SYM = '①②③④⑤⑥⑦⑧'

ZAHLWORT = {0: ['null', 'kein', 'keine', 'keinen', 'keiner', 'keinem', 'nie', 'nichts', 'niemals'],
            1: ['eins', 'einmal', 'einzige', 'einziger', 'einziges', 'einzigen'],
            2: ['zwei', 'zweimal', 'doppelt', 'doppelte', 'doppelten', 'doppeltes', 'verdoppelt'],
            3: ['drei', 'dreimal', 'dreifache', 'dreifachen'], 4: ['vier', 'viermal'], 5: ['fünf', 'fünfmal'],
            6: ['sechs'], 7: ['sieben'], 8: ['acht'], 9: ['neun'], 10: ['zehn'], 11: ['elf'], 12: ['zwölf'],
            13: ['dreizehn'], 14: ['vierzehn'], 15: ['fünfzehn'], 16: ['sechzehn'], 17: ['siebzehn'],
            18: ['achtzehn'], 19: ['neunzehn'], 20: ['zwanzig']}
EIN = re.compile(r'\bein(?:e|en)?\s+(?:Paar|Punkt|Schnittpunkt|gemeinsamen?)\w*', re.I)
ZAHL = re.compile(r'\d+(?:[.,]\d+)?')


def alle():
    for d in DATEIEN:
        for a in json.load(open(d, encoding='utf-8'))['aufgaben']:
            yield os.path.relpath(d, WURZEL), a


def ohne_tausender(s):
    return re.sub(r'(?<=\d)[   ](?=\d{3}(?!\d))', '', s)


def zahlen_in(s):
    out = set()
    for m in ZAHL.findall(ohne_tausender(s)):
        try:
            out.add(Fraction(m.replace(',', '.')))
        except ValueError:
            pass
    return out


def wortfund(wert, s):
    """Zahlwörter zu einem ganzzahligen Wert (Betrag) im Text; Wortgrenzen, ohne Zusammensetzungen."""
    w = abs(wert)
    if w.denominator != 1 or w.numerator > 20:
        return []
    treffer = [x for x in ZAHLWORT.get(int(w), []) if re.search(r'(?<![\wäöüß])' + x + r'(?![\wäöüß])', s, re.I)]
    if int(w) == 1 and EIN.search(s):
        treffer.append(EIN.search(s).group(0))
    return treffer


# ---------- sichere Auswertung einfacher Rechnungen ----------
OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv,
       ast.FloorDiv: lambda a, b: Fraction(a // b), ast.Mod: operator.mod}


def rechne(ausdruck):
    def ev(n):
        if isinstance(n, ast.Expression): return ev(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)): return Fraction(str(n.value))
        if isinstance(n, ast.BinOp): return OPS[type(n.op)](ev(n.left), ev(n.right))
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub): return -ev(n.operand)
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.UAdd): return ev(n.operand)
        if isinstance(n, ast.Call) and getattr(n.func, 'id', '') == 'abs': return abs(ev(n.args[0]))
        raise ValueError
    return ev(ast.parse(ausdruck, mode='eval'))


def text_zu_ausdruck(s):
    s = ohne_tausender(s).replace('−', '-').replace('·', '*').replace('×', '*').replace(':', '/').replace(',', '.')
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def versuche(s):
    try:
        return rechne(text_zu_ausdruck(s))
    except Exception:
        return None


ZEICHEN = r'[\d\s.,+\-−·×:*/()  ]'
EINHEIT = r'(?:\s*(?:°|cm²|dm²|m²|mm²|cm|dm|mm|km|kg|g|m|€|Cent|%))?'
RECHNUNG = re.compile(r'(?<![\w.])(?:[−\-]?\(?[−\-]?\d[\d.,]*\)?)(?:\s*[+\-−·×:*/]\s*[−\-]?\(?[−\-]?\d[\d.,]*\)?)+')


def rechnungen_in(s):
    """Alle Rechnungen a op b (op b ...) in einem Text, ohne Gleichheitszeichen."""
    s = ohne_tausender(s)
    s = re.sub(r'(?<=\d)\s*(?:°|cm²|dm²|m²|mm²|km|kg|cm|dm|mm|Cent|ct|€)', '', s)
    out = []
    for m in RECHNUNG.finditer(s):
        t = m.group(0).rstrip(' ,.')
        # Ziffernreihen wie 3,5 als Dezimalzahl nicht als Aufzählung lesen
        v = versuche(t)
        if v is not None:
            out.append((t.strip(), v))
    return out


# ---------- (i) ----------
def pruefe_i(f, a, melde):
    if not a['typ'].startswith('Lückenweg') or a['antwortform'] != 'luecken':
        return
    q = a['aufgabe']
    texte = {'Text': q['f'].get('text', ''), 'Schablone': q['f'].get('schablone', ''),
             'Tipp': q.get('h', ''), 'Eingabehinweis': q['f'].get('hinweis', '')}
    for i, wert in enumerate(q['o']['werte'], 1):
        wert = Fraction(wert)
        for name, s in texte.items():
            if name == 'Schablone':
                continue
            nur_zahl = abs(wert) in zahlen_in(s)
            wort = wortfund(wert, s)
            if nur_zahl or wort:
                melde('i', a, f'Lücke {SYM[i-1]} = {wert}: steht im {name} ' + ('als Ziffer ' if nur_zahl else '') + (('als Wort ' + ', '.join(wort)) if wort else ''))


# ---------- (ii) ----------
def norm(c):
    return re.sub(r'\s+', '', c)


def pruefe_ii(f, a, melde):
    if not a['typ'].startswith('Lückenweg') or a['antwortform'] != 'luecken':
        return
    q = a['aufgabe']; c = [norm(x) for x in q['c']]; n = len(c)
    text = q['f']['text']
    # Satzweise: steht in demselben Satz wie Lücke i ein früheres Symbol?
    saetze = re.split(r'(?<=[.!?])\s+', text)
    ANSCHLUSS = re.compile(r'(?:Dann|Also|Daher|Deshalb|Damit|Somit|Folglich|Weil|Deswegen|Das|Er|Sie)\b')
    def sym_abh(i):
        # Erstes Auftreten von SYM[i]. Abhängig, wenn
        #  (A) im selben Satz davor ein früheres Symbol steht und SYM[i] das Ergebnis einer Gleichung ist
        #      („② − ① = ③“; gilt nicht für Aufzählungen wie „y = ①x + ②“), oder
        #  (B) der Satz mit einem Anschlusswort beginnt („Dann hat g ④ Punkte“) und im Satz davor ein früheres
        #      Symbol steht. Spätere Wiederholungen der Lücke zählen nicht.
        for k, s in enumerate(saetze):
            if SYM[i] in s:
                pre = s.split(SYM[i])[0]
                if re.search(r'=\s*$', pre) and any(SYM[j] in pre for j in range(i)):
                    return True
                if k and ANSCHLUSS.match(s) and any(SYM[j] in saetze[k - 1] for j in range(i)):
                    return True
                return False
        return False
    def c_abh(i):
        for j in range(i):
            if len(c[j]) >= 3 and c[j] in c[i]:
                return True
            # früherer Wert als Zahl im späteren Anker (z. B. 24 in 24-8)? zu unscharf, nur mit Klammerform
        return False
    abh = [False] + [c_abh(i) or sym_abh(i) for i in range(1, n)]
    if n >= 2 and not any(abh):
        melde('ii', a, f'keine Lücke hängt an einer früheren (Anker: {q["c"]})')
    elif n >= 2 and not abh[-1]:
        melde('ii', a, f'letzte Lücke {SYM[n-1]} hängt an keiner früheren (Nebenfrage?)')


# ---------- (iii) ----------
def pruefe_iii(f, a, melde):
    q = a['aufgabe']
    if q['y'] not in ('zahl', 'luecken'):
        return
    for fb in a['fehlbilder']:
        beschr = fb.get('beschreibung') or ''
        ant = fb['antwort']
        if isinstance(ant, str):
            continue
        r = rechnungen_in(beschr)
        if not r:
            continue
        werte = [v for _, v in r]
        # auch Beträge zulassen? nein: Vorzeichen zählt
        if Fraction(str(ant)) not in werte:
            melde('iii', a, f'Fehlbild {fb.get("luecke", "")} Antwort {ant}: „{beschr}“ ergibt ' + ', '.join(f'{t} = {v}' for t, v in r))


# ---------- (iv) ----------
ZEILE = re.compile(r'Zeile (\d+):\s*(.*?)(?=\s*Zeile \d+:|\s*In welcher Zeile|$)', re.S)


EINHEITEN = r'°|cm²|dm²|m²|mm²|km|kg|cm|dm|mm|Cent|ct|€|g(?![\wäöü])|m(?![\wäöü])'


def gleichungsketten(s):
    """Liefert (Kette, stimmt) für jede Kette a = b = c aus reinen Zahlenausdrücken in s.
    Ketten mit verschiedenen Einheiten (1 kg = 1 000 g) werden übersprungen, Prozent wird als /100 gelesen."""
    s = ohne_tausender(s)
    s = re.sub(r'(\d[\d.,]*)\s*%', r'(\1/100)', s)
    s = re.sub(r'(?<=\d)\s*(' + EINHEITEN + r')', lambda m: '~' + m.group(1) + '~', s)
    out = []
    for m in re.finditer(r'(?:~[^~]+~|[\d\s.,+\-−·×:*/()=°²€])+', s):
        lauf = m.group(0)
        if m.start() > 0 and s[m.start() - 1].isalpha() and lauf.lstrip().startswith('('):
            continue
        for seg in re.split(r'(?<=\d)[.,]\s+|\s+[.,]\s*', lauf):
            seg = seg.strip(' .,:')
            if '=' not in seg:
                continue
            teile = [p.strip() for p in seg.split('=')]
            if len(teile) < 2 or any(not p for p in teile):
                continue
            einh = {e for p in teile for e in re.findall(r'~([^~]+)~', p)}
            if len(einh) > 1:
                continue
            vals = [versuche(re.sub(r'~[^~]+~', '', p)) for p in teile]
            if any(v is None for v in vals):
                continue
            out.append((re.sub(r'~', '', seg), len(set(vals)) == 1))
    return out


def pruefe_iv(f, a, melde):
    if not a['typ'].startswith('Fehler') or a['antwortform'] != 'auswahl':
        return
    q = a['aufgabe']
    if not q['a'][0].startswith('In Zeile'):
        return
    err = q['o']['index'] + 1
    zeilen = {int(i): t for i, t in ZEILE.findall(q['f']['text'])}
    for i, t in zeilen.items():
        ketten = gleichungsketten(t)
        if i < err:
            for k, ok in ketten:
                if not ok:
                    melde('iv', a, f'Zeile {i} (vor der Fehlerzeile {err}) enthält eine falsche Rechnung: {k}')
        elif i == err and ketten and all(ok for _, ok in ketten):
            melde('iv', a, f'Fehlerzeile {err}: alle Rechnungen stimmen ({"; ".join(k for k, _ in ketten)}); Fehler muss ein Denkfehler sein')


def main():
    nur = set()
    args = sys.argv[1:]
    if '--kennung' in args:
        nur = set(args[args.index('--kennung') + 1:])
    funde = []
    def melde(art, a, text):
        funde.append((art, a['kennung'], text))
    n = 0
    for f, a in alle():
        if nur and a['kennung'] not in nur:
            continue
        n += 1
        for p in (pruefe_i, pruefe_ii, pruefe_iii, pruefe_iv):
            p(f, a, melde)
    for art in ('i', 'ii', 'iii', 'iv'):
        sel = [x for x in funde if x[0] == art]
        print(f'== ({art}) {len(sel)} Meldungen')
        for _, k, t in sel:
            print(f'  {k}: {t}')
    print(f'{n} Aufgaben geprüft, {len(funde)} Meldungen')
    return 1 if funde else 0


if __name__ == '__main__':
    sys.exit(main())
