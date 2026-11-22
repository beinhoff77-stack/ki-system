# Kern für den Aufgaben-Nachbau: Zahlformat, Polynome, Registrierung, Prüfungen.
# Alle Aufgaben sind eigene Texte mit Zufallszahlen; Lösungen werden hier berechnet und gegengeprüft.
from fractions import Fraction as F
import math, random, itertools

REG = {}          # (thema, etappe) -> Generator; ("L", vorschlag) / ("X", grund)
PRUEF = []        # Protokoll der Gegenprüfungen der aktuellen Aufgabe


def reg(*schluessel):
    def deko(fn):
        for s in schluessel:
            REG[s] = fn
        return fn
    return deko


class Pruefung(Exception):
    pass


def chk(bed, was):
    if not bed:
        raise Pruefung(was)
    PRUEF.append(was)


def ev(ausdruck):
    """Rechenausdruck in Schreibweise der Aufgabe (·, :, −, ², ³, Klammern) unabhängig auswerten."""
    import re as _re
    t = ausdruck.replace("·", "*").replace(":", "/").replace("−", "-").replace("²", "**2").replace("³", "**3").replace(" ", "")
    t = _re.sub(r"(\d+),(\d+)", r"\1.\2", t)
    t = _re.sub(r"(\d+(?:\.\d+)?)", r"F('\1')", t)
    return eval(t, {"F": F})


# ------------------------------------------------------------------ Zahlformat
MINUS = "−"


def _int(n):
    s = f"{abs(n):,}".replace(",", " ") if abs(n) >= 10000 else str(abs(n))
    return (MINUS if n < 0 else "") + s


def fz(v, dez=None):
    """Zahl deutsch formatieren. Fraction -> Bruch, außer dez=True (Dezimal, wenn endlich)."""
    if isinstance(v, float):
        v = F(v).limit_denominator(10**6)
    if isinstance(v, int):
        return _int(v)
    v = F(v)
    if v.denominator == 1:
        return _int(v.numerator)
    if dez is None:
        dez = False
    if dez and endlich(v):
        return dezimal(v)
    return (MINUS if v < 0 else "") + f"{abs(v.numerator)}/{v.denominator}"


def endlich(v):
    d = F(v).denominator
    for p in (2, 5):
        while d % p == 0:
            d //= p
    return d == 1


def dezimal(v, stellen=None):
    v = F(v)
    if stellen is None:
        stellen = 0
        while (v * 10**stellen).denominator != 1 and stellen < 8:
            stellen += 1
    q = round(v * 10**stellen)
    s = _int(abs(q) // 10**stellen if stellen else abs(q))
    if stellen:
        s += "," + str(abs(q) % 10**stellen).rjust(stellen, "0")
    return (MINUS if q < 0 else "") + s


def fd(v):
    return fz(v, dez=True)


def gerundet(v, stellen):
    """Gerundete Dezimaldarstellung (für Näherungen)."""
    q = F(round(F(v) * 10**stellen), 10**stellen)
    return dezimal(q, stellen)


def eur(v):
    """Geldbetrag mit zwei Dezimalen."""
    return dezimal(F(v), 2)


def plusminus(v):
    """'+ 3' bzw. '− 3' für Terme wie x + a."""
    v = F(v)
    return f"{'+' if v >= 0 else MINUS} {fz(abs(v))}"


def kl(v, dez=False):
    """Zahl, negative in Klammern (für Rechenausdrücke)."""
    s = fz(v, dez=dez)
    return f"({s})" if F(v) < 0 else s


# ------------------------------------------------------------------ Polynome (mehrere Variablen)
class P:
    """Polynom mit rationalen Koeffizienten. Monom = Tupel ((var, exp), ...) sortiert."""
    ORD = "xyzabnmrstkhuvwp"

    def __init__(self, d=None):
        self.d = {}
        for k, v in (d or {}).items():
            v = F(v)
            if v:
                self.d[k] = self.d.get(k, 0) + v
        self.d = {k: v for k, v in self.d.items() if v}

    @staticmethod
    def var(n):
        return P({((n, 1),): 1})

    @staticmethod
    def c(z):
        return P({(): z})

    def _co(self, o):
        return o if isinstance(o, P) else P.c(o)

    def __add__(self, o):
        o = self._co(o); r = dict(self.d)
        for k, v in o.d.items():
            r[k] = r.get(k, 0) + v
        return P(r)
    __radd__ = __add__

    def __neg__(self):
        return P({k: -v for k, v in self.d.items()})

    def __sub__(self, o):
        return self + (-self._co(o))

    def __rsub__(self, o):
        return self._co(o) - self

    def __mul__(self, o):
        o = self._co(o); r = {}
        for k1, v1 in self.d.items():
            for k2, v2 in o.d.items():
                e = dict(k1)
                for n, x in k2:
                    e[n] = e.get(n, 0) + x
                k = tuple(sorted(((n, x) for n, x in e.items() if x), key=lambda t: P.ORD.index(t[0])))
                r[k] = r.get(k, 0) + v1 * v2
        return P(r)
    __rmul__ = __mul__

    def __pow__(self, n):
        r = P.c(1)
        for _ in range(n):
            r = r * self
        return r

    def __eq__(self, o):
        return self.d == self._co(o).d

    def ev(self, **w):
        s = F(0)
        for k, v in self.d.items():
            t = F(v)
            for n, x in k:
                t *= F(w[n]) ** x
            s += t
        return s

    def grad(self, k):
        return sum(x for _, x in k)

    def __str__(self):
        return self.fmt()

    def fmt(self, dez=False):
        if not self.d:
            return "0"
        keys = sorted(self.d, key=lambda k: (-self.grad(k), [P.ORD.index(n) for n, _ in k], [-x for _, x in k]))
        out = []
        for i, k in enumerate(keys):
            v = self.d[k]
            mon = "".join(n + (hoch(x) if x != 1 else "") for n, x in k)
            av = abs(v)
            if mon and av == 1:
                zs = ""
            else:
                zs = fz(av, dez=dez)
                if mon and "/" in zs:
                    zs = zs + "·"
            term = zs + mon
            if i == 0:
                out.append((MINUS if v < 0 else "") + term)
            else:
                out.append((" − " if v < 0 else " + ") + term)
        return "".join(out)


HOCH = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def hoch(n):
    return str(n).translate(HOCH)


x, y, a, b, n = (P.var(t) for t in "xyabn")


# ------------------------------------------------------------------ Lösen
def loese_linear(lhs, rhs, v="x"):
    """lhs = rhs, beide P (linear in v). Gibt Fraction oder 'alle'/'keine'."""
    d = lhs - rhs
    a1 = d.d.get(((v, 1),), F(0)); a0 = d.d.get((), F(0))
    chk(all(k in ((), ((v, 1),)) for k in d.d), "linear")
    if a1 == 0:
        return "alle" if a0 == 0 else "keine"
    return -a0 / a1


def ggt(*z):
    g = 0
    for t in z:
        g = math.gcd(g, int(t))
    return g


def kgv(*z):
    r = 1
    for t in z:
        r = r * int(t) // math.gcd(r, int(t))
    return r


def teiler(n):
    return [t for t in range(1, n + 1) if n % t == 0]


def prim(n):
    return n > 1 and all(n % t for t in range(2, int(n**0.5) + 1))


def pfz(n):
    r, t = [], 2
    while n > 1:
        while n % t == 0:
            r.append(t); n //= t
        t += 1
    return r


def roemisch(n):
    w = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
         (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    s = ""
    for z, r in w:
        while n >= z:
            s += r; n -= z
    return s


def aus_roemisch(s):
    w = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    t = 0
    for i, ch in enumerate(s):
        if i + 1 < len(s) and w[ch] < w[s[i + 1]]:
            t -= w[ch]
        else:
            t += w[ch]
    return t


def basis(n, b):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = "0123456789ABCDEF"[n % b] + s; n //= b
    return s


def runde(n, stelle):
    return (n + stelle // 2) // stelle * stelle


def balken(daten, einheit="", breite=30):
    """Waagrechtes Balkendiagramm als Textblock (druckbar)."""
    m = max(v for _, v in daten) or 1
    lw = max(len(k) for k, _ in daten)
    zeilen = []
    for k, v in daten:
        lang = round(float(v) / float(m) * breite)
        zeilen.append(f"{k.ljust(lw)} | {'█' * lang} {fz(v, dez=True)}{einheit}")
    return "```\n" + "\n".join(zeilen) + "\n```"


def tabelle(kopf, zeilen):
    s = "| " + " | ".join(kopf) + " |\n|" + "---|" * len(kopf) + "\n"
    for z in zeilen:
        s += "| " + " | ".join(str(t) for t in z) + " |\n"
    return s


# ------------------------------------------------------------------ Kontext je Aufgabe
VORNAMEN = ["Mia", "Ben", "Jonas", "Lena", "Emil", "Ida", "Paul", "Nora", "Tom", "Ella", "Finn", "Lisa", "Noah", "Jana"]


class Ctx:
    def __init__(self, seed, zeile):
        self.r = random.Random(seed)
        self.z = zeile
        self.niv = zeile["niveau"]
        self.kurz = (zeile.get("kurzbeschreibung") or "").lower()
        self.typ = (zeile.get("typ") or "").lower()
        self.pkt = zeile.get("punkte")
        self.kl = zeile.get("klasse")
        self.k5 = self.kl == 5

    def has(self, *w):
        t = self.kurz + " " + self.typ
        return any(s in t for s in w)

    def name(self, k=1):
        ns = self.r.sample(VORNAMEN, k)
        return ns[0] if k == 1 else ns

    def ri(self, a, b, ohne=()):
        self.zaehler = getattr(self, "zaehler", 0) + 1
        if self.zaehler > 20000:
            raise Pruefung("Endlosschleife")
        while True:
            v = self.r.randint(a, b)
            if v not in ohne:
                return v

    def ch(self, seq):
        self.zaehler = getattr(self, "zaehler", 0) + 1
        if self.zaehler > 20000:
            raise Pruefung("Endlosschleife")
        return self.r.choice(list(seq))

    def nz(self, a, b):
        """ganze Zahl ungleich 0 in [a, b]"""
        return self.ri(a, b, ohne=(0,))

    def schwer(self):
        return {"I": 0, "II": 1, "III": 2}[self.niv]


class T:
    def __init__(self, text, loesung, weg, abb=None):
        self.text, self.loesung, self.weg, self.abb = text, loesung, list(weg), abb
