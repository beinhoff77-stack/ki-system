"""Kern für den Nachbau von Prüfungsaufgaben (Auftrag PM 2, Teil B).

Jede Aufgabenfamilie liefert ein Objekt `Kern` (Aufgabenstamm, Ziel, Antwort, Lösungsweg, Ablenker, Prüfungen).
`formen()` macht daraus die verlangte Aufgabenform (rechnen, Lücke, ankreuzen, begründen, Fehler finden …).
Alle Zahlen und Kontexte werden zufällig (aber reproduzierbar) erzeugt – nichts stammt aus einer Originalaufgabe.
"""
import re
from fractions import Fraction as Fr

import sympy as sp

X, A, B, Y = sp.symbols('x a b y')

NAMEN = ['Mila', 'Jonas', 'Ella', 'Timo', 'Nora', 'Emil', 'Lea', 'Paul', 'Ida', 'Ben', 'Lina', 'Finn', 'Maja', 'Noah', 'Zoe', 'Elias',
         'Amira', 'Luca', 'Hanna', 'Milan', 'Selin', 'David', 'Romy', 'Kerem', 'Frieda', 'Aaron']


class Pruefe(Exception):
    pass


def z(w, dez=None):
    """Zahl schön darstellen: Bruch, ganze Zahl oder Dezimalzahl mit Komma; Minus als −."""
    if isinstance(w, sp.Basic):
        w = Fr(int(sp.fraction(sp.nsimplify(w))[0]), int(sp.fraction(sp.nsimplify(w))[1]))
    if isinstance(w, float):
        w = Fr(w).limit_denominator(10 ** 6)
    if isinstance(w, int):
        w = Fr(w)
    neg = w < 0
    w = abs(w)
    if w.denominator == 1:
        s = f'{w.numerator:,}'.replace(',', ' ') if w.numerator >= 10000 else str(w.numerator)
    elif dez is not False and (dez or (_endlich(w) and 10000 % w.denominator == 0)):
        s = _dezimal(w, dez)
    else:
        s = f'{w.numerator}/{w.denominator}'
    return ('−' if neg else '') + s


def _endlich(w):
    d = w.denominator
    for p in (2, 5):
        while d % p == 0:
            d //= p
    return d == 1


def _dezimal(w, stellen=None):
    if stellen in (None, True):
        stellen = 0
        while (w * 10 ** stellen).denominator != 1 and stellen < 8:
            stellen += 1
    s = f'{float(w):.{stellen}f}'.replace('.', ',')
    return s


def zk(w, dez=None):
    """Zahl, negative in Klammern (für Terme)."""
    s = z(w, dez)
    return f'({s})' if s.startswith('−') else s


def euro(w):
    w = Fr(w)
    return z(w, 2) + ' €' if w.denominator != 1 else z(w) + ' €'


def term(expr):
    """sympy-Ausdruck lesbar: 3x² − 2x + 1."""
    s = sp.sstr(sp.expand(expr) if not isinstance(expr, str) else expr, order='lex')
    return term_str(s)


def term_str(s):
    s = s.replace('**', '^')
    s = re.sub(r'\^(\d)', lambda m: '⁰¹²³⁴⁵⁶⁷⁸⁹'[int(m.group(1))], s)
    s = re.sub(r'(\d)\*([a-z(])', r'\1\2', s)
    s = s.replace('*', '·').replace('-', '−').replace('/', ' : ' if False else '/')
    s = re.sub(r'(?<![\w)])1([a-z])', r'\1', s)
    return s


HOCH = str.maketrans('0123456789-()', '⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁽⁾')


def hoch(basis, exp):
    """Potenz mit hochgestelltem Exponenten, z. B. 10⁻³."""
    e = str(exp).replace('−', '-')
    return f'{basis}{e.translate(HOCH)}'


def pt(xy):
    return f'({z(xy[0])} | {z(xy[1])})'


def vek(v):
    return f'({z(v[0])}; {z(v[1])})'


class Kern:
    """Fachlicher Kern einer Aufgabe."""

    def __init__(self, stamm, ziel, antwort, weg, falsch=None, pruef=None, luecke=None, aussage=None, abb=None,
                 hilfe=None, antwort_kurz=None):
        self.stamm = stamm.strip()
        self.ziel = ziel.strip()
        self.antwort = antwort           # Text der richtigen Lösung (kurz)
        self.antwort_kurz = antwort_kurz or antwort  # für Ankreuzen/Behauptungen
        self.weg = [w for w in weg if w]
        self.falsch = falsch or []       # Liste (Wert-Text, typischer Fehler)
        self.pruef = pruef or []         # Liste (Beschreibung, bool)
        self.luecke = luecke             # eigener Lückentext (optional)
        self.aussage = aussage           # (Behauptung, wahr?, Begründung) für begründen (optional)
        self.abb = abb                   # Abbildungsbeschreibung (optional)
        self.hilfe = hilfe

    def ok(self):
        return all(b for _, b in self.pruef)


def check(beschr, bedingung):
    return (beschr, bool(bedingung))


def wissen(beschr):
    """Wissens-/Definitionsfrage oder Konstruktion: keine Rechnung zum Nachprüfen."""
    return ('WISSEN: ' + beschr, True)


ZAHL = re.compile(r'−?\d+(?:,\d+)?(?:/\d+)?')


def ablenker(text, rng, letzte=False):
    """Zusätzliche falsche Antworten: erste (bzw. letzte) Zahl im Text verändern (Vorzeichen, ±1, ·2, :2)."""
    treffer = list(ZAHL.finditer(text))
    if not treffer or (len(treffer) > 2 and not letzte):
        return []
    m = treffer[-1] if letzte else treffer[0]
    s = m.group(0)
    try:
        w = Fr(s.replace('−', '-').replace(',', '.'))
    except ValueError:
        return []
    out = []
    for v in (-w, w + 1, w - 1, w * 2, w / 2, w + 10):
        if v != w:
            out.append(text[:m.start()] + z(v) + text[m.end():])
    rng.shuffle(out)
    return out


def _satz(s):
    s = s.strip()
    return s if s.endswith(('.', '?', '!')) else s + '.'


def formen(k, typ, rng):
    """Aufgabenform herstellen. Liefert (aufgabentext, loesungstext, form)."""
    typ = (typ or 'rechnen').lower()
    abb = f'\n\n*Abbildung (Beschreibung):* {k.abb}' if k.abb else ''
    name = rng.choice(NAMEN)
    stamm = (k.stamm + ('\n\n' if k.stamm.rstrip().endswith('|') else ' ')) if k.stamm else ''
    schon_begruendung = any(w in k.ziel for w in ('Begründe', 'begründe', 'Prüfe', 'Beurteile', 'Ist die', 'Sind g', 'Liegt der'))
    weg = k.weg
    if typ.startswith('ankreuzen') or typ.startswith('zuordnen'):
        opts = [k.antwort_kurz] + [f for f, _ in k.falsch if f != k.antwort_kurz]
        opts = list(dict.fromkeys(opts))
        for neu in ablenker(k.antwort_kurz, rng) + ablenker(k.antwort_kurz, rng, letzte=True):
            if len(opts) >= 4:
                break
            if neu not in opts:
                opts.append(neu)
        opts = opts[:4]
        if len(opts) < 2 or (len(opts) < 3 and k.antwort_kurz not in ('Ja', 'Nein', 'richtig', 'falsch')):
            return formen(k, 'rechnen', rng)
        rng.shuffle(opts)
        buchst = 'ABCD'
        richtig = buchst[opts.index(k.antwort_kurz)]
        text = f'{stamm}{k.ziel} Kreuze die richtige Antwort an.{abb}\n\n' + '\n'.join(f'- ☐ {buchst[i]}) {o}' for i, o in enumerate(opts))
        loes = f'Richtig ist **{richtig}) {k.antwort_kurz}**.'
        return text, loes, weg, 'ankreuzen'
    if typ.startswith('begründen') or typ.startswith('beschreiben (fachsprache)'):
        if schon_begruendung and not k.aussage:
            return f'{stamm}{k.ziel}{abb}', k.antwort, weg, 'begründen'
        if k.aussage:
            beh, wahr, grund = k.aussage
            text = f'{stamm}{beh}{abb}'
            loes = ('Die Aussage stimmt. ' if wahr else 'Die Aussage stimmt nicht. ') + grund
            return text, loes, weg, 'begründen'
        if k.falsch and rng.random() < 0.55:
            wert, grund = k.falsch[0]
            text = f'{stamm}{_satz(k.ziel)} {name} gibt als Ergebnis {wert} an. Hat {name} recht? Begründe.{abb}'
            loes = f'{name} hat nicht recht ({grund}). Richtig: {k.antwort}.'
        else:
            text = f'{stamm}{_satz(k.ziel)} {name} gibt als Ergebnis {k.antwort_kurz} an. Hat {name} recht? Begründe.{abb}'
            loes = f'{name} hat recht: {k.antwort}.'
        return text, loes, weg, 'begründen'
    if typ.startswith('fehler'):
        if k.falsch and not schon_begruendung:
            wert, grund = k.falsch[0]
            text = (f'{stamm}{_satz(k.ziel)} {name} erhält: {wert}. Finde den Fehler, beschreibe ihn und gib das '
                    f'richtige Ergebnis an.{abb}')
            loes = f'Fehler: {grund}. Richtig: {k.antwort}.'
            return text, loes, weg, 'Fehler finden'
        return formen(k, 'begründen', rng)
    if typ.startswith('lücke') and k.luecke:
        return f'{stamm}{k.luecke}{abb}', k.antwort, weg, 'Lücke'
    form = {'sachaufgabe': 'Sachaufgabe', 'zeichnen': 'zeichnen', 'konstruieren': 'konstruieren', 'ablesen': 'ablesen',
            'lücke': 'Lücke', 'beschreiben': 'beschreiben'}.get(typ.split()[0].split('/')[0], 'rechnen')
    return f'{stamm}{k.ziel}{abb}', k.antwort, weg, form


def punkte_weg(weg, p):
    """Punkte auf Lösungsschritte verteilen (ganze und halbe Punkte)."""
    if p is None:
        return [None] * len(weg)
    p2 = int(round(p * 2))
    n = max(1, len(weg))
    if n == 1:
        return [Fr(p2, 2)]
    n_eff = min(n, max(1, p2))
    basis, rest = divmod(p2, n_eff)
    teile = [basis + (1 if i >= n_eff - rest else 0) for i in range(n_eff)]
    # nur die letzten n_eff Schritte bekommen Punkte (Ansatz bekommt sonst 0)
    out = [Fr(0)] * (n - n_eff) + [Fr(t, 2) for t in teile]
    return out
