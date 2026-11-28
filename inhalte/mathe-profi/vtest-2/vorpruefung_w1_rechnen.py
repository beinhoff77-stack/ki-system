#!/usr/bin/env python3
"""Vorprüfung Welle 1, Runde 2 (Urteil 1222): unabhängige Nachrechnung.

Einheiten: zahlen.natuerlich (VT2-085..133) und terme.umformen (VT2-029..049).
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
L = {}   # kennung -> Sollwert (zahl), Liste (luecken) oder Index (auswahl)
N = {}   # kennung -> Notiz (Sonderfälle)

# --- stellenwert
# 085: Ziffer d (1..9) und 0 an ZT/T tauschen; Zuwachs 27 000
kand = []
for d in range(1, 10):
    for vorne in (0, d):                  # Ziffer an ZT vorher
        hinten = d if vorne == 0 else 0
        zuwachs = (hinten - vorne) * 10000 + (vorne - hinten) * 1000
        if zuwachs == 27000:
            kand.append(d)
L["VT2-085"] = kand[0]
N["VT2-085"] = "eindeutig d=%s; vorher 0 an ZT -> nur möglich, wenn vor ZT noch eine Ziffer steht (sonst führende 0); Probe der Lösung schreibt '03 000'" % kand
L["VT2-086"] = 1                          # 5000:5 = 1000 -> Option 1
assert 5000 // 5 == 1000
L["VT2-087"] = 7777 - 7007
z = "360482"
L["VT2-088"] = [2, int(z[1]) * 10 ** (len(z) - 2)]
L["VT2-089"] = 3
L["VT2-090"] = len({p for p in permutations("046") if p[0] != "0"})
L["VT2-091"] = [n for n in range(1, 10000) if 10 * n - n == 4050][0]

# --- ziffern_zu_zahlwort
z = str(204 * 10 ** 6 + 7 * 10 ** 3 + 5)
L["VT2-092"] = [len(z), int(z[-4])]
L["VT2-093"] = str(30 * 10 ** 6 + 3020).count("0")
L["VT2-094"] = 2                          # Zeile 3 falsch
L["VT2-095"] = 0
L["VT2-096"] = 1 if 2000300 > 200300 else None
L["VT2-097"] = [3, (10010100 // 1000) % 1000]
L["VT2-098"] = ["60 000 600", "6 600", "6 600 000", "6 000 600"].index(
    "{:,}".format(6 * 10 ** 6 + 600).replace(",", " "))

# --- strahl_eintragen
je_cm = F(2000 - 1200, 4)
L["VT2-099"] = [int((3400 - 1200) / je_cm), int(1200 + 9 * je_cm)]
marken = [0, 250, 500, 800, 1000]
schritt = F(marken[-1] - marken[0], len(marken) - 1)
falsch = [i for i, m in enumerate(marken) if m != marken[0] + i * schritt]
L["VT2-100"] = falsch[0] - 1              # Optionen ohne die 0
L["VT2-101"] = 700 + (12 - 5) * 50
L["VT2-102"] = [3, int(F(7500, 1000) * 2)]
a = set(range(200, 1200, 200)); b = set(range(150, 1200, 150))
L["VT2-103"] = len(a & b)
je_cm = F(120, 6)
L["VT2-104"] = sum(1 for n in range(0, 121) if abs(n - 60) / je_cm < 1)
L["VT2-105"] = 0

# --- runden_regel
L["VT2-106"] = sum(1 for n in range(1, 101) if rund(n, 10) == rund(n, 100))
L["VT2-107"] = [sum(1 for n in range(0, 10000) if rund(n, 100) == 3700),
                sum(1 for n in range(0, 10000) if rund(n, 1000) == 4000)]
L["VT2-108"] = max(abs(rund(n, 100) - n) for n in range(0, 100000))
L["VT2-109"] = [2, rund(4949, 100)]
faelle = {(rund(n, 10000) > n, rund(n, 10000) < n, rund(n, 10000) == n) for n in range(1, 200000)}
L["VT2-110"] = 1 if len(faelle) == 3 else None
mono = all(rund(a, 100) <= rund(a + 1, 100) for a in range(0, 100000))
gleich_moeglich = rund(4760, 100) == rund(4770, 100)
L["VT2-111"] = 3 if (mono and gleich_moeglich) else None
zahlen = [n for n in range(0, 10000) if rund(n, 100) == 2000]
L["VT2-112"] = 2 if (min(zahlen), max(zahlen)) == (1950, 2049) else None

# --- runden_sinnvoll
L["VT2-113"] = [50 * 30 - 48 * 29, 48 * 30 - 48 * 29]
L["VT2-114"] = [1000 // 36, -(-1000 // 36)]
N["VT2-114"] = "Text nennt 27,8 (Dezimalzahl) – in M5 noch nicht eingeführt (Dezimalbrüche M6)"
L["VT2-115"] = 2 if (rund(22817, 1000) == 23000 and rund(22817, 10000) == 20000) else None
L["VT2-116"] = [min(n for n in range(0, 10000) if rund(n, 100) == 4300) * 15,
                max(n for n in range(0, 10000) if rund(n, 100) == 4300) * 15]
L["VT2-117"] = 3 if 237 < 249 else None
laengen = [m for m in range(1, 100) if rund(m, 10) == 30]
L["VT2-118"] = [min(m // 3 for m in laengen), max(m // 3 for m in laengen)]
w = [1480, 1460, 1440, 1450]
assert sum(w) == 5830 and sum(rund(x, 1000) for x in w) == 4000
L["VT2-119"] = 1

# --- roemisch_schreiben
nils = "M" + "CD" + "XL" + "VIIII"
assert roem(1449) == "MCDXLIX"
L["VT2-120"] = [4, len(nils), len(roem(1449))]
opts = ["VC", "CDXC", "MCMXC", "XLIV"]
ungueltig = [i for i, s in enumerate(opts) if not roem_regelgerecht(s)]
L["VT2-121"] = ungueltig[0] if len(ungueltig) == 1 else ungueltig
L["VT2-122"] = [len(roem(1999, ADD)), len(roem(1999))]
# Eindeutigkeit 122: rein additive Schreibweisen von 1999 sind nicht eindeutig
alt = "M" + "C" * 9 + "L" + "X" * 4 + "V" + "I" * 4    # ebenfalls nur addiert, = 1999
assert sum(WERT[c] for c in alt) == 1999
N["VT2-122"] = "rein additiv auch z. B. %s (%d Zeichen) möglich – 'mit möglichst wenigen Zeichen' fehlt" % (alt, len(alt))
L["VT2-123"] = [1000, 900, 40, 4]
L["VT2-124"] = sum(1 for n in range(1, 51) if any(p in roem(n) for p in ("IV", "IX", "XL")))
L["VT2-125"] = 1 if (roem_regelgerecht("MCMXCIX") and not roem_regelgerecht("MIM")) else None
L["VT2-126"] = min(n for n in range(1, 4000) if len(roem(n)) == 6)

# --- dualsystem
L["VT2-127"] = sum(1 for n in range(16, 32) if n > 20)
L["VT2-128"] = sum(1 for n in (24, 32, 48, 64, 96, 128) if bin(n).count("1") == 1)
L["VT2-129"] = 3 if int("0111", 2) == int("111", 2) else None
L["VT2-130"] = [2, int("1011", 2)]
L["VT2-131"] = int("1101", 2) - int("0101", 2)
L["VT2-132"] = len({format(n, "b") for n in range(0, 32)})
L["VT2-133"] = len(format(127, "b")) if set(format(127, "b")) == {"1"} else None

# --- terme.umformen: zusammenfassen
U_R = lambda x: 2 * ((3 * x + 2) + (x + 6))
a_kand = [a for a in range(-50, 51) if gleichwertig(U_R, lambda x, a=a: 4 * (2 * x + a))]
L["VT2-029"] = a_kand[0]
N["VT2-029"] = "für x = -1 ist die Seite 3x + 2 = -1 cm (negativ) – 'für jede Zahl x' im Sachkontext; x > 0 o. ä. vorgeben"
glieder = [("x", 1), ("x", 2), ("x", 1), ("", 0), ("x", 2), ("", 0)]   # 2x,3x²,-x,4,5x²,7
L["VT2-030"] = sum(1 for i in range(6) for j in range(i + 1, 6) if glieder[i] == glieder[j])
L["VT2-031"] = 7 * 2 ** 3 - (3 * 2 + 4 * 2 ** 2)
assert 7 * 0 ** 3 == 3 * 0 + 4 * 0 and 7 * 1 == 3 + 4
L["VT2-032"] = 2
assert gleichwertig(lambda x: 6 * x - 4 * 7 + 2 * x + 5 * 7, lambda x: 8 * x + 7)  # y = 7 Probe
lsg = [(p, q) for p in range(-10, 11) for q in range(-10, 11)
       if gleichwertig(lambda x: 5 * x * x - 3 * x - p * x * x + q * x, lambda x: 3 * x * x - 2 * x)]
L["VT2-033"] = list(lsg[0])
L["VT2-034"] = (lambda x: 5 * x - 7 + 3 - 4 * x - x + 10)(1000)
T = lambda x, y: 6 * x + 4 * y - 2 * x - 3 * y
L["VT2-035"] = T(11, 5) - T(10, 5)

# --- minusklammer
lsg = [(a, b) for a in range(-20, 21) for b in range(-20, 21)
       if gleichwertig(lambda x: (a * x + 5) - (3 * x - b), lambda x: 2 * x + 9)]
L["VT2-036"] = list(lsg[0])
werte = {(lambda x: 9 - (x - 4) - (6 - x))(F(x)) for x in range(-5, 6)}
L["VT2-037"] = int(werte.pop()) if len(werte) == 1 else None
L["VT2-038"] = [k for k in range(-20, 21) if 7 * 1 - (k * 1 - 3) == 4][0]
assert 10 - (2 + 3) != 10 - 2 + 3
L["VT2-039"] = 0
A = lambda x: 12 - (x - 5)
L["VT2-040"] = sum(1 for g in (lambda x: 12 - x - 5, lambda x: 12 - x + 5, lambda x: 17 - x, lambda x: -x + 17)
                   if gleichwertig(A, g))
assert gleichwertig(lambda a: 4 * a - (3 - 2 * a) + (a - 1), lambda a: 7 * a - 4)
L["VT2-041"] = [2, 7, -4]
L["VT2-042"] = [x for x in range(-50, 51) if 20 * x - (5 * x - 3 + 2 * x - 8 + x) == 35][0]

# --- aequivalenz
Ts = {"A": lambda x: 2 * (x + 3), "B": lambda x: 2 * x + 6, "C": lambda x: 3 * (x + 2) - x,
      "D": lambda x: 5 * x - 2 * (x + 1), "E": lambda x: 3 * x - 2, "F": lambda x: 3 * x + 2}
ks = list(Ts)
L["VT2-043"] = sum(1 for i in range(6) for j in range(i + 1, 6) if gleichwertig(Ts[ks[i]], Ts[ks[j]]))
echt = lambda n: 4 * n - (n - 1)          # n Quadrate, n-1 gemeinsame Hölzer
terme = [lambda n: 4 + 3 * (n - 1), lambda n: 3 * n + 1, lambda n: 4 * n - n - 1]
L["VT2-044"] = [sum(1 for t in terme if all(t(n) == echt(n) for n in range(1, 30))), echt(10)]
G = lambda x: 3 * (x + 2) - (x - 4)
kette = [lambda x: 3 * x + 6 - x - 4, lambda x: 2 * x + 2, lambda x: 3 * x + 6 - x + 4,
         lambda x: 2 * x + 10, lambda x: 3 * x + 6 - (x - 4)]
L["VT2-045"] = sum(1 for t in kette if gleichwertig(G, t))
R = lambda x: F(2 * x + 6, 2) - x
L["VT2-046"] = [int(R(5)), int(R(100))]
ab = [(a, b) for a in range(-20, 21) for b in range(-20, 21) if [a * x + b for x in (0, 1, 2)] == [4, 7, 10]]
L["VT2-047"] = ab[0][0] * 10 + ab[0][1]
treffer = [x for x in range(1, 11) if x * x + 6 == 5 * x]
L["VT2-048"] = [len(treffer), 5 * max(treffer)]
L["VT2-049"] = [a for a in range(-20, 21) if gleichwertig(lambda x: 3 * (x - 2) + a * x, lambda x: 7 * x - 6)][0]


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
