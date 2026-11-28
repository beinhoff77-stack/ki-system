#!/usr/bin/env python3
"""Vorprüfung Welle 1, Runde 2 (Urteil 1222): unabhängige Nachrechnung.

Einheiten: zahlen.natuerlich und terme.umformen.
Zweite Fassung (Stand 9a986063) und dritte Fassung (Stand 7cc61b65): VT2-085..119 und VT2-029..043, 5 je Lernziel.
Jede Lösung wird hier aus der Aufgabenstellung neu gerechnet (exakt, Fraction,
wo möglich durch vollständiges Durchprobieren). Nicht aus gegenrechnung.py
übernommen. Danach: Vergleich mit der Sollantwort in der JSON, Prüfung der
Fehlbilder (Rechnung = Antwort, Antwort != Lösung, je Lücke mindestens eins)
und Bauart-Merkmale der Auswahl-Aufgaben.

Aufruf (aus dem Repo-Wurzelordner):
  python3 -I inhalte/mathe-profi/vtest-2/vorpruefung_w1_rechnen.py
"""
import json
import os
import re
from fractions import Fraction as F
from itertools import permutations

HIER = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------- Hilfen
def rund(n, stufe):
    """kaufmännisch runden (natürliche Zahlen) auf Vielfache von stufe"""
    q, r = divmod(n, stufe)
    return (q + (1 if 2 * r >= stufe else 0)) * stufe


ROEM = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
        (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
ADD = [(1000, "M"), (500, "D"), (100, "C"), (50, "L"), (10, "X"), (5, "V"), (1, "I")]
WERT = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
ERLAUBT_VOR = {"I": "VX", "X": "LC", "C": "DM"}


def roem(n, tab=ROEM):
    s = ""
    for w, z in tab:
        while n >= w:
            s += z
            n -= w
    return s


def roem_regelgerecht(s):
    """Regeln der Aufgaben 121/125: höchstens dreimal hintereinander;
    kleineres links von größerem nur I vor V/X, X vor L/C, C vor D/M;
    zusätzlich: Ergebnis muss mit der Standardschreibweise übereinstimmen."""
    if re.search(r"(.)\1\1\1", s):
        return False
    for a, b in zip(s, s[1:]):
        if WERT[a] < WERT[b] and b not in ERLAUBT_VOR.get(a, ""):
            return False
    wert, i = 0, 0
    while i < len(s):
        if i + 1 < len(s) and WERT[s[i]] < WERT[s[i + 1]]:
            wert += WERT[s[i + 1]] - WERT[s[i]]
            i += 2
        else:
            wert += WERT[s[i]]
            i += 1
    return roem(wert) == s


def ausdruck(t):
    """Ausdruck der JSON (·, :, −, ², ³, Komma) exakt auswerten"""
    t = str(t).replace("·", "*").replace(":", "/").replace("−", "-")
    t = t.replace("²", "**2").replace("³", "**3").replace("×", "*")
    t = re.sub(r"(\d),(\d)", r"\1.\2", t)
    t = re.sub(r"(?<![\w.])(\d+(?:\.\d+)?)", r"F('\1')", t)
    return eval(t, {"F": F, "abs": abs})


def gleichwertig(f, g, punkte=range(-4, 8)):
    return all(f(F(x)) == g(F(x)) for x in punkte)


# ---------------------------------------------------------------- Eigene Lösungen
# Stand 9a986063: 50 Aufgaben (VT2-085 … 119, VT2-029 … 043), 5 je Lernziel.
L = {}   # kennung -> Sollwert (zahl), Liste (luecken) oder Index (auswahl)
N = {}   # kennung -> Notiz (Sonderfälle)


def ziffern(n):
    return [int(c) for c in str(n)]


def tausch(n, i, j):
    """Ziffern an Stellenwert 10^i und 10^j tauschen"""
    s = list(str(n).rjust(max(i, j) + 1, "0"))[::-1]
    s[i], s[j] = s[j], s[i]
    return int("".join(s[::-1]))


# --- stellenwert
best = None
for n in range(100000, 1000000):
    s = str(n)
    if s.count("4") != 2:
        continue
    p = [k for k, c in enumerate(s) if c == "4"]
    if 10 ** (p[1] - p[0]) != 1000:
        continue
    rest = [c for c in s if c != "4"]
    if len(set(rest)) == 4:
        best = n
L["VT2-085"] = best
# 086: alle Zahlen (5- und 6-stellig), bei denen der Tausch ZT<->T genau +36 000 bringt
diffs, paare = set(), set()
for n in range(10000, 1000000):
    if tausch(n, 4, 3) - n == 36000:
        d = ziffern(n)[::-1]
        diffs.add(d[3] - d[4]); paare.add((d[4], d[3]))
assert diffs == {4} and len(paare) == 6         # 0/4 … 5/9: Option 3 („nur 0 und 4“) falsch
L["VT2-086"] = 1
L["VT2-087"] = [2, 60000]
assert 7090 != 79 and 7090 != 790 and 7090 != 709
L["VT2-088"] = 3
werte = [t * 1000 + h * 100 + z * 10 + e for t in range(10) for h in range(10) for z in range(10)
         for e in range(10) if t + h + z + e == 12]
L["VT2-089"] = [min(werte), max(werte)]

# --- ziffern_zu_zahlwort
L["VT2-090"] = sum(1 for n in range(10 ** 6 + 1, 2 * 10 ** 6) if (n // 1000) % 1000 == 0)
assert {len(str(n)) for n in range(10 ** 7, 11 * 10 ** 6)} == {8}
L["VT2-091"] = 2
L["VT2-092"] = 0


def tim_liest(n):
    s = str(n)
    g = [int(s[i:i + 3]) for i in range(0, len(s), 3)]       # Gruppen von links
    return sum(x * 1000 ** (len(g) - 1 - k) for k, x in enumerate(g))


L["VT2-093"] = sum(1 for n in range(1000, 1000000) if tim_liest(n) == n)


def hundert_anzahl(n):
    k = 0
    while n:
        if (n % 1000) // 100:
            k += 1
        n //= 1000
    return k


assert max(hundert_anzahl(n) for n in range(10 ** 8, 10 ** 8 + 200000)) == 3
kleinste = next(n for n in range(10 ** 8, 10 ** 9) if hundert_anzahl(n) == 3)
assert all(hundert_anzahl(n) <= 2 for n in range(1, 10 ** 6, 7))       # Stichprobe < 10^8
L["VT2-094"] = [3, kleinste]

# --- strahl_eintragen
je_cm = F(2000 - 1200, 4)
L["VT2-095"] = [int((3400 - 1200) / je_cm), int(1200 + 9 * je_cm)]
striche = {300 + 200 * k for k in range(2000)}
L["VT2-096"] = 1 if not any(2 * s in striche for s in list(striche)[:1000]) else None
L["VT2-097"] = 2 if F(600, 50) / F(600, 200) == 4 else None
L["VT2-098"] = len(set(range(200, 1200, 200)) & set(range(150, 1200, 150)))
L["VT2-099"] = 0 if len({10 - 0, 100 - 10, 1000 - 100}) > 1 else None

# --- runden_regel
L["VT2-100"] = sum(1 for n in range(1, 101) if rund(n, 10) == rund(n, 100))
L["VT2-101"] = max(abs(rund(n, 100) - n) for n in range(0, 100000))
L["VT2-102"] = [2, rund(4949, 100)]
faelle = {(rund(n, 10000) > n, rund(n, 10000) < n) for n in range(1, 200000)}
L["VT2-103"] = 1 if len(faelle) == 3 else None
L["VT2-104"] = 3 if all(rund(a, 100) <= rund(a + 1, 100) for a in range(100000)) else None

# --- runden_sinnvoll
laengen = [m for m in range(1, 100) if rund(m, 10) == 30]
L["VT2-105"] = [min(m // 3 for m in laengen), max(m // 3 for m in laengen)]
assert divmod(1000, 36) == (27, 28)
L["VT2-106"] = [1000 // 36, -(-1000 // 36)]
L["VT2-107"] = 2 if (rund(22817, 1000), rund(22817, 10000)) == (23000, 20000) else None
L["VT2-108"] = [50 * 30 - 48 * 29, 48 * 30 - 48 * 29]
w = [3460, 3420, 3440, 3470]
assert sum(w) == 13790 and sum(rund(x, 1000) for x in w) == 12000 and rund(sum(w), 1000) != sum(w)
L["VT2-109"] = 0

# --- roemisch_schreiben
ADD_C = [(100, "C"), (50, "L"), (10, "X"), (5, "V"), (1, "I")]
ersparnis = {n: len(roem(n, ADD_C)) - len(roem(n)) for n in range(1, 91)}
mx = max(ersparnis.values())
top = [n for n, e in ersparnis.items() if e == mx]
N["VT2-110"] = "größte Ersparnis %d nur bei %s" % (mx, top)
L["VT2-110"] = [top[0], mx] if len(top) == 1 else top
opts = ["MCMXC", "CDXC", "XLIV", "VC"]
L["VT2-111"] = [i for i, s in enumerate(opts) if not roem_regelgerecht(s)][0]
assert len("XII") > len("X") and 12 > 10 and len("VIII") > len("L") and 8 < 50
L["VT2-112"] = 1
L["VT2-113"] = max(n for n in range(1, 6000) if not re.search(r"(.)\1\1\1", roem(n)))
L["VT2-114"] = min(n for n in range(1, 4000) if len(roem(n)) == 6)

# --- dualsystem
mia = lambda n: sum(int(c) * 2 ** k for k, c in enumerate(format(n, "b")))   # Stellenwerte von links
L["VT2-115"] = sum(1 for n in range(1, 32) if mia(n) == n)
L["VT2-116"] = 0 if int("0111", 2) == int("111", 2) else None
d117 = {int(format(n, "b"), 2) - int("0" + format(n, "b")[1:-1] + "1", 2)
        for n in range(64, 128) if format(n, "b").endswith("0")}
L["VT2-117"] = d117.pop() if len(d117) == 1 else d117
endet00 = [n for n in range(4, 4096) if format(n, "b").endswith("00")]
assert all(n % 4 == 0 for n in endet00)
assert any(bin(n).count("1") > 1 for n in endet00) and any(n % 100 != 0 for n in endet00)
L["VT2-118"] = 1
L["VT2-119"] = [min(len(str(n)) for n in range(512, 1024)), max(len(str(n)) for n in range(512, 1024))]

# --- terme.umformen: zusammenfassen
U_R = lambda x: 2 * ((3 * x + 2) + (x + 6))
a_kand = [a for a in range(-50, 51) if gleichwertig(U_R, lambda x, a=a: 4 * (2 * x + a), range(1, 12))]
assert all(s > 0 for x in (F(1, 1000), 1, 5) for s in (3 * x + 2, x + 6, 2 * x + a_kand[0]))
L["VT2-029"] = a_kand[0]
L["VT2-030"] = 2
gleich = [x for x in range(-100, 101) if 3 * x + 2 == 5 * x]
L["VT2-031"] = 0 if gleich == [1] else None
L["VT2-032"] = (lambda x: 5 * x - 7 + 3 - 4 * x - x + 10)(987654)
T33 = lambda a, b: 7 * a - 2 * b + 3 - 4 * a + 5 * b - a
d33 = {T33(a, b) - T33(a + 1, b - 1) for a in range(-5, 6) for b in range(-5, 6)}
L["VT2-033"] = d33.pop() if len(d33) == 1 else d33

# --- minusklammer
kand = [a for a in range(1, 100)
        if all((40 - (3 * x - a)) - (40 - 3 * x - a) == 18 for x in range(-5, 6))]
L["VT2-034"] = kand[0] if len(kand) == 1 else kand
assert gleichwertig(lambda a: 4 * a - (3 - 2 * a) + (a - 1), lambda a: 7 * a - 4)
L["VT2-035"] = [2, 7, -4]
rest = lambda x: 50 - (x - 3)              # Lisa zahlt x - 3
assert all(rest(x) == 50 - (x - 3) and rest(x) != 50 - x - 3 for x in range(3, 50))
L["VT2-036"] = 1


def T37(n, x):
    t = x - 1
    for _ in range(n - 1):
        t = x - t
    return t


L["VT2-037"] = [T37(10, 50), T37(11, 50)]
assert gleichwertig(lambda x: -(x - 7), lambda x: 7 - x)
L["VT2-038"] = 2

# --- aequivalenz
ok39 = all((a1 == a2 and b1 == b2) for a1 in range(-6, 7) for b1 in range(-6, 7)
           for a2 in range(-6, 7) for b2 in range(-6, 7) if b1 == b2 and a1 + b1 == a2 + b2)
assert 1 == 1 * 1 and 3 * 1 - 2 == 1 and 4 == 3 * 2 - 2          # Beispiel im Lösungsweg
L["VT2-039"] = 0 if ok39 else None
echt = lambda n: 4 * n - (n - 1)
terme = [lambda n: 4 + 3 * (n - 1), lambda n: 3 * n + 1, lambda n: 4 * n - n - 1]
L["VT2-040"] = [sum(1 for t in terme if all(t(n) == echt(n) for n in range(1, 30))), echt(10)]
L["VT2-041"] = [k for k in range(-50, 51) if all(F(2 * x + k, 2) - x == 10 for x in range(-5, 6))][0]
L["VT2-042"] = sum(1 for x in range(-100, 101) if 3 * (x + 4) - x == 2 * x + 9)
Ts = {"A": lambda x: 2 * (x + 3), "B": lambda x: 2 * x + 6, "C": lambda x: 3 * (x + 2) - x,
      "D": lambda x: 5 * x - 2 * (x + 1), "E": lambda x: 3 * x - 2, "F": lambda x: 3 * x + 2}
ks = list(Ts)
L["VT2-043"] = sum(1 for i in range(6) for j in range(i + 1, 6) if gleichwertig(Ts[ks[i]], Ts[ks[j]]))


# ---------------------------------------------------------------- Dritte Fassung (Stand 7cc61b65)
# Neue bzw. geänderte Aufgaben; überschreibt die Werte der zweiten Fassung.
# 095: gleicher Unterschied auf beiden Strahlen, umgekehrter Maßstab
unterschied = 6 * 50
L["VT2-095"] = int(F(unterschied, 4))
# 097: Lena zählt Striche ab dem Strich bei 0 → landet bei (n:10 − 1)·10
assert all(n - (n // 10 - 1) * 10 == 10 for n in range(10, 10000, 10))
L["VT2-097"] = 2
L["VT2-098"] = len(set(range(200, 12000, 200)) & set(range(150, 12000, 150)))
# 108: nur Faktoren, die keine Zehnerzahl sind
nz = [n for n in range(11, 200) if n % 10]
auf = lambda n: (n // 10 + 1) * 10
ab = lambda n: (n // 10) * 10
assert all(auf(a) * auf(b) > a * b for a in nz for b in nz)                      # Lea immer zu groß
tom = {(auf(a) * ab(b) > a * b, auf(a) * ab(b) < a * b) for a in nz for b in nz}
assert (True, False) in tom and (False, True) in tom                              # Tom beide Richtungen
assert auf(18) * ab(11) > 18 * 11 and ab(12) * auf(19) < 12 * 19                   # Beispiele im Text
L["VT2-108"] = 0
assert sum(rund(x, 1000) for x in [3460, 3420, 3440, 3470]) == 12000
L["VT2-109"] = 3
spar = {n: len(roem(n, ADD_C)) - len(roem(n)) for n in range(10, 100)}
L["VT2-110"] = sorted(n for n, e in spar.items() if e == 5)
N["VT2-110"] = "Ersparnis genau 5 nur bei %s; 99 spart %d" % (L["VT2-110"], spar[99])
assert len(roem(18)) == 5 and len(roem(19)) == 3 and len(roem(8)) > len(roem(9))
kuerzer = [n for n in range(2, 100) if len(roem(n)) < len(roem(n - 1))]
N["VT2-112"] = "kürzer als der Vorgänger bei %s" % kuerzer[:12]
L["VT2-112"] = 0
L["VT2-113"] = max(n for n in range(1, 6000) if roem_regelgerecht(roem(n)))
# 115: Zahl und „Gegenzahl“ (alle Ziffern getauscht), 5 Stellen, Unterschied 7
paare = {tuple(sorted((n, 31 - n), reverse=True)) for n in range(32) if abs(n - (31 - n)) == 7}
L["VT2-115"] = list(paare.pop()) if len(paare) == 1 else paare
L["VT2-116"] = 1
# 117: mehr Einsen → nichts Sicheres (Gegenbeispiele beider Richtungen)
assert int("111", 2) < int("1000", 2) and int("11", 2) > int("10", 2)
L["VT2-117"] = 3
L["VT2-118"] = sum(1 for n in range(32) if not n & 4)
# terme
glieder = set()
for art in ("x2", "x", "z"):
    for a in range(-10, 11):
        if a == 0:
            continue
        k = {"x2": 3, "x": 5, "z": -2}
        k[art] += a
        glieder.add(sum(1 for v in k.values() if v != 0))
L["VT2-031"] = [min(glieder), max(glieder)]
werte38 = {20 - (a - b) for a in range(1, 6) for b in range(1, 6) if a != b}
L["VT2-038"] = [len(werte38), max(werte38)]
N["VT2-038"] = "nur 20 Paare: vollständiges Ausrechnen in 2–3 Minuten möglich"
L["VT2-039"] = 1
L["VT2-040"] = 2
def faelle42(a, b):
    g = [x for x in range(-200, 201) if a * x + 9 == 2 * x + b]
    return "jede" if len(g) == 401 else ("keine" if not g else ("eine" if len(g) == 1 else "?"))
assert {faelle42(2, b) for b in range(-20, 21) if b != 9} == {"keine"}
assert faelle42(2, 9) == "jede" and {faelle42(a, 9) for a in range(-9, 10) if a != 2} == {"eine"}
assert "eine" in {faelle42(3, 4)}
L["VT2-042"] = 0
L["VT2-036"] = 0
L["VT2-111"] = ["MCMXC", "VC", "CDXC", "XLIV"].index([s for s in ["MCMXC", "VC", "CDXC", "XLIV"] if not roem_regelgerecht(s)][0])


# ---------------------------------------------------------------- Vergleich mit JSON
def soll(a):
    o = a["aufgabe"]["o"]
    if "werte" in o:
        return list(o["werte"])
    if "wert" in o:
        return o["wert"]
    return o["index"]


MARKER = {
    "=": r"=", "<": r"<", ">": r">",
    "kleiner/größer": r"\b(kleiner|größer|mehr|weniger)\b",
    "denn/weil/da": r"\b(denn|weil|da)\b",
    "Nebensatz (dass/wenn/ob/obwohl)": r"\b(dass|wenn|ob|obwohl|sodass)\b",
    "Absolutwort (immer/nie/stets/jede/alle/nur/kein)": r"\b(immer|nie|niemals|stets|jede[rs]?|alle|nur|kein[e]?)\b",
    "höchstens/mindestens": r"\b(höchstens|mindestens)\b",
    "Verneinung (nicht)": r"\bnicht\b",
    "Sammeloption (beide/weder/alle drei)": r"\b(beide|weder|alle drei)\b",
    "Zahl im Text": r"\d",
    "nicht entscheidbar": r"(nicht entscheiden|nicht sagen|nichts sagen|weiß man nicht|weiß man erst|nichts Sicheres|hängt vom Rest ab|kann man nicht)",
    "Sammel (jeder/beide/keiner/weder)": r"\b(beide|weder|keiner|jeder der|alle drei)\b",
    "Doppelpunkt/Semikolon": r"[:;]",
}


def bauart(a):
    opts = a["aufgabe"]["a"]
    k = a["aufgabe"]["o"]["index"]
    laengen = [len(o) for o in opts]
    rang = sorted(range(len(opts)), key=lambda i: -laengen[i]).index(k) + 1
    nur_richtig, nur_falsch = [], []
    for name, rx in MARKER.items():
        hat = [bool(re.search(rx, o, re.I)) for o in opts]
        if hat[k] and sum(hat) == 1:
            nur_richtig.append(name)
        if not hat[k] and sum(hat) == len(opts) - 1:
            nur_falsch.append(name)
    # Urteil-Einzelgänger: erstes Wort / Satzanfang bis Komma bei Urteilsoptionen
    kopf = [re.split(r"[,;:]| denn | weil ", o)[0].strip().lower() for o in opts]
    urteil = [re.match(r"^(nur \w+|beide|weder|[\w ]{0,30}?(recht|unrecht|irrt|größer|kleiner|gleich))", h) for h in kopf]
    return laengen, rang, nur_richtig, nur_falsch


def main():
    fehler = 0
    zeilen = []
    for datei in ("zahlen.natuerlich.json", "terme.umformen.json"):
        d = json.load(open(os.path.join(HIER, datei), encoding="utf-8"))
        for a in d["aufgaben"]:
            k = a["kennung"]
            s = soll(a)
            mein = L.get(k)
            ok = mein == s
            if not ok:
                fehler += 1
            # Fehlbilder
            fb_befund = []
            y = a["aufgabe"]["y"]
            luecken_mit_fb = set()
            for fb in a["fehlbilder"]:
                if y in ("zahl", "luecken") and fb.get("rechnung") is not None:
                    try:
                        w = ausdruck(fb["rechnung"])
                        if w != F(fb["antwort"]):
                            fb_befund.append("Rechnung %s ergibt %s, nicht %s" % (fb["rechnung"], w, fb["antwort"]))
                    except Exception as e:
                        fb_befund.append("Rechnung %r nicht auswertbar (%s)" % (fb["rechnung"], e))
                if y == "zahl" and fb["antwort"] == s:
                    fb_befund.append("Fehlbild = Lösung")
                if y == "luecken":
                    luecken_mit_fb.add(fb["luecke"])
                    if fb["antwort"] == s[fb["luecke"] - 1]:
                        fb_befund.append("Fehlbild = Lösung in Lücke %s" % fb["luecke"])
            if y == "luecken":
                fehlt = [i for i in range(1, len(s) + 1) if i not in luecken_mit_fb]
                if fehlt:
                    fb_befund.append("Lücke ohne eigenes Fehlbild: %s" % fehlt)
            if y == "auswahl":
                idx = {fb["index"] for fb in a["fehlbilder"]}
                soll_idx = set(range(len(a["aufgabe"]["a"]))) - {s}
                if idx != soll_idx:
                    fb_befund.append("Fehlbild-Indizes %s statt %s" % (sorted(idx), sorted(soll_idx)))
                laengen, rang, nr, nf = bauart(a)
                fb_befund.append("Länge %s, richtige Option Längenrang %d/%d; nur in richtiger: %s; nur in allen falschen: %s"
                                 % (laengen, rang, len(laengen), nr or "-", nf or "-"))
            # Lösungsrechnung der JSON gegen Soll
            lr = a.get("loesung_rechnung")
            if lr is not None:
                lr_l = lr if isinstance(lr, list) else [lr]
                try:
                    w = [ausdruck(t) for t in lr_l]
                    s_l = s if isinstance(s, list) else [s]
                    if [F(x) for x in s_l] != w:
                        fb_befund.append("loesung_rechnung %s ergibt %s" % (lr, w))
                except Exception as e:
                    fb_befund.append("loesung_rechnung nicht auswertbar (%s)" % e)
            zeilen.append("%s %-9s soll=%s mein=%s %s%s%s" % (
                k, a["pool"], s, mein, "OK" if ok else "ABWEICHUNG",
                ("\n    " + "\n    ".join(fb_befund)) if fb_befund else "",
                ("\n    Notiz: " + N[k]) if k in N else ""))
    print("\n".join(zeilen))
    print("\nAbweichungen Lösung: %d" % fehler)
    return fehler


if __name__ == "__main__":
    raise SystemExit(1 if main() else 0)
