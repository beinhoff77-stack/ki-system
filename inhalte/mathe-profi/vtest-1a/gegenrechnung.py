"""Gegenrechnung Runde VT1A (Verstehen in Tests, Klasse 5), Stand nach Vorprüfung W1 (55 Aufgaben).

Rechnet alle 55 Sollantworten NEU und UNABHÄNGIG von `bauen.py`, `kern.py` und den Quelltexten `th_*.py`:
- Zahlaufgaben: Sollwert aus den Angaben des Fragetextes mit Zählschleifen, Probieren oder Nachbauen der beschriebenen (auch falschen) Regel;
  der gespeicherte Wert muss GENAU gleich sein (keine Toleranz).
- Auswahlaufgaben: Wo die Optionen Terme, Zahlen oder Gleichungen sind, wird JEDE Option aus ihrem Text ausgewertet und geprüft, dass genau
  die gespeicherte richtige Option die Bedingung der Frage erfüllt. Sonst: erwarteter Anfang der richtigen Option und eine eigene Probe.
Aufruf: python3 -I inhalte/mathe-profi/vtest-1a/gegenrechnung.py   (Ausgabe endet mit „0 Abweichungen“)
"""
import glob
import json
import os
import re
from fractions import Fraction as F

HIER = os.path.dirname(os.path.abspath(__file__))
Q = {}
for _p in sorted(glob.glob(os.path.join(HIER, "*.json"))):
    for _q in json.load(open(_p, encoding="utf-8"))["aufgaben"]:
        Q[_q["kennung"][5:]] = _q["aufgabe"]
assert len(Q) == 55, len(Q)
abw = []
gesehen = set()
HOCH = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")


def term(t):
    """Wert eines Terms aus dem Optionstext (·, :, −, Hochzahlen, Tausenderleerzeichen), exakt als Bruch."""
    t = t.replace("·", "*").replace(":", "/").replace("−", "-").replace(" ", "").strip()
    t = re.sub(r"(?<=\d) (?=\d{3}(?!\d))", "", t)
    t = re.sub(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+", lambda m: "**" + m.group(0).translate(HOCH), t)
    t = re.sub(r"(\d+)", r"F(\1)", t)
    return eval(t, {"__builtins__": {}, "F": F})


def zahl(k, soll):
    a = Q[k]
    gesehen.add(k)
    assert a["y"] == "zahl", k
    if "toleranz" in a["o"]:
        abw.append((k, "Toleranz vorhanden"))
    if F(str(a["o"]["wert"])) != F(soll):
        abw.append((k, "Zahl", a["o"]["wert"], soll))


def wahl(k, anfang, probe=True):
    a = Q[k]
    gesehen.add(k)
    assert a["y"] == "auswahl", k
    if not a["a"][a["o"]["index"]].startswith(anfang):
        abw.append((k, "Antwort", a["a"][a["o"]["index"]][:60], anfang))
    if probe is not True:
        abw.append((k, "Probe", probe))
    if len(set(a["a"])) != len(a["a"]) or len(a["a"]) < 4:
        abw.append((k, "Möglichkeiten"))


def wahl_genau(k, bedingung):
    """Genau eine Option erfüllt die Bedingung, und es ist die gespeicherte."""
    a = Q[k]
    gesehen.add(k)
    treffer = [i for i, o in enumerate(a["a"]) if bedingung(o)]
    if treffer != [a["o"]["index"]]:
        abw.append((k, "Optionen", treffer, a["o"]["index"]))


def erste(f, bis=100000, ab=0):
    return next(n for n in range(ab, bis) if f(n))


# ═════════ zahlen.potenzen_basis ═════════
# schreibweise
wahl_genau("001", lambda o: term(o) != 2 ** 20)
zahl("002", next(n for n in range(1, 200) if 2 ** n == sum(2 ** 30 for _ in range(4))))
def wert_003(o):
    z = [int(x) for x in re.findall(r"\d+", o)]
    return z[1] ** 12 if o.startswith("Die Basis") else 3 ** z[1]


wahl_genau("003", lambda o: wert_003(o) == 3 * 3 ** 12)
gleich_oder_kleiner = [(a, b) for a in range(2, 30) for b in range(2, 30) if a ** b <= a * b]
wahl("004", "Fast immer: Bei 2²", gleich_oder_kleiner == [(2, 2)])
wahl("005", "In 4 Kisten stehen je 4 Schachteln, in jeder Schachtel liegen 4", 4 * 4 * 4 == 4 ** 3)
# quadrat
zahl("006", next(n * n for n in range(1, 200) if (n + 2) * (n + 2) - n * n == 44))
zahl("007", 50 * sum(1 for _ in range(3) for _ in range(3)))
wahl("008", "Zwei Rechtecke mit 30 cm", 37 * 37 - 30 * 30 - 7 * 7 == 2 * 30 * 7)
quadrate = {n * n for n in range(1, 200)}
wahl_genau("009", lambda o: term(o) not in quadrate)
anzahlen = [(n + 1) ** 2 - n ** 2 - 1 for n in range(1, 500)]
wahl("010", "Die Anzahl ist immer gerade", all(x % 2 == 0 for x in anzahlen) and len(set(anzahlen)) > 1)
# zehner
zahl("011", erste(lambda x: x * 10 ** 8 > 7 * 10 ** 11, 10 ** 6, 1))
zahl("012", len([n for n in range(0, 40) if 5 * 10 ** 3 < 10 ** n < 5 * 10 ** 7]))
vorher = 7 * 10 ** 9 + 5 * 10 ** 6 + 3 * 10 ** 2
nachher = 7 * 10 ** 10 + 5 * 10 ** 7 + 3 * 10 ** 3
wahl("013", "Sie wird 10-mal so groß", nachher == 10 * vorher)
wahl("014", "10⁶ ist um 1 000 größer", 10 ** 6 - (9 * 10 ** 5 + 9 * 10 ** 4 + 9 * 10 ** 3) == 1000)
nullen = lambda z: len(str(z)) - len(str(z).rstrip("0"))
wahl("015", "Manchmal", nullen(50 * 10 ** 3) == 4 != 3 and nullen(3 * 10 ** 2) == 2)
# sach
zweier = lambda z: next(k for k in range(60) if z % 2 ** (k + 1))      # Zahl der Faktoren 2
zahl("016", zweier(6 ** 6) - zweier(2 * 3 ** 6))
zahl("017", len({96 // 2 ** n for n in range(1, 10) if 96 % 2 ** n == 0}))
wahl("018", "Ein Stapel hat am Anfang 3 Blätter. Er wird 5-mal hintereinander verdoppelt", 3 * 2 ** 5 == 96 and 5 * 2 ** 3 != 96)
a_, b_ = 5, 10
for _ in range(20):
    a_, b_ = 3 * a_, 3 * b_
zahl("019", F(b_, a_))
A_, B_, vorn = 100, 1, []
for _ in range(80):
    A_, B_ = A_ + 100, B_ * 2
    vorn.append(B_ > A_)
erst = vorn.index(True)
wahl("020", "B überholt A irgendwann und bleibt danach immer vorn", all(vorn[erst:]) and not any(vorn[:erst]))

# ═════════ zahlen.rechengesetze ═════════
# klammern
unterschiede = {(z - 4800 + 650) - (z - (4800 + 650)) for z in range(10001, 30000, 97)}
assert len(unterschiede) == 1
zahl("021", unterschiede.pop())
ohne_klammern = lambda t: term(t.replace("(", "").replace(")", ""))   # Regel des Kindes: Klammern weglassen
assert [ohne_klammern(t) for t in ("3 · (4 + 5)", "(8 − 2) · 3", "2 · (10 − 4)")] == [17, 2, 16]
zahl("022", ohne_klammern("(6 + 4) · (5 − 3)") - term("(6 + 4) · (5 − 3)"))
wahl_genau("023", lambda o: term(o) == 50 - 3 * (9 - 2))
ketten_gleich = {"Plus": all((a + b) + c == a + (b + c) for a in range(1, 20) for b in range(1, 20) for c in range(1, 20)),
                 "Minus": all((a - b) - c == a - (b - c) for a in range(1, 20) for b in range(1, 20) for c in range(1, 20)),
                 "Mal": all((a * b) * c == a * (b * c) for a in range(1, 9) for b in range(1, 9) for c in range(1, 9)),
                 "Geteilt": all(F(F(a, b), c) == F(a, F(b, c)) for a in range(1, 9) for b in range(1, 9) for c in range(1, 9))}
wahl("024", "Bei einer Kette nur mit Plus ändert", ketten_gleich == {"Plus": True, "Minus": False, "Mal": True, "Geteilt": False})
zuwachs = {((z + 5) + 7) * 3 - (z + 7) * 3 for z in range(0, 500)}
assert len(zuwachs) == 1
zahl("025", zuwachs.pop())
# termaufbau
alt_, neu_ = F(136 * 89 + 64 * 112 - 20, 4), F(136 * 89 + 64 * 112 - 36, 4)
wahl("026", "Er wird um 4 kleiner", alt_ - neu_ == 4 and neu_.denominator == 1)
passend = [n for n, w in (("①", 30 - 6 - 4), ("②", 30 - (6 + 4)), ("③", 30 - 6 + 4), ("④", 30 - (6 - 4))) if w == 30 - 6 - 4]
wahl("027", "Genau ① und ②", passend == ["①", "②"])


def letzter_schritt(t):
    """Rechenart des letzten Schritts eines Terms ohne Klammern um das Ganze: das am weitesten rechts stehende Zeichen
    mit niedrigster Bindung außerhalb von Klammern (Strich vor Punkt beim Suchen, gleichrangig von rechts)."""
    tiefe, kand = 0, []
    for i, z in enumerate(t):
        tiefe += z == "("
        tiefe -= z == ")"
        if tiefe == 0 and z in "+−·:":
            kand.append((0 if z in "+−" else 1, i, z))
    return max(kand, key=lambda k: (-k[0], k[1]))[2]


ersetzt = {}
for o in Q["028"]["a"]:
    alt_z, neu_z = re.findall(r"Das (.) durch (.)", o)[0]
    ersetzt[o] = letzter_schritt("(6 + 4) · 5 − 2".replace(alt_z, neu_z, 1))
wahl_genau("028", lambda o: ersetzt[o] == "·")
namen = {"+": "Summe", "−": "Differenz", "·": "Produkt", ":": "Quotient"}
beispiele = {"4 + 6 · 2": "Produkt", "12 : 3 − 1": "Differenz", "20 − (5 + 3)": "Summe"}
rechts = lambda t: namen[[z for z in t if z in namen][-1]]
links = lambda t: namen[[z for z in t if z in namen][0]]
zuletzt = lambda t: namen[letzter_schritt(t)]
wahl("029", "Es benennt den Term nach dem Rechenzeichen, das ganz rechts",
     all(rechts(t) == n for t, n in beispiele.items()) and not all(links(t) == n for t, n in beispiele.items()) and not all(zuletzt(t) == n for t, n in beispiele.items()))
wahl("030", "Mit Klammer ist es eine Differenz, ohne Klammer eine Summe", namen[letzter_schritt("20 − (5 + 3)")] == "Differenz" and namen[letzter_schritt("20 − 5 + 3")] == "Summe")
# vorteil
paare = [(a, 200 // a) for a in range(6, 201) if 200 % a == 0 and a < 200 // a and 200 // a > 5 and a % 10 and (200 // a) % 10]
assert len(paare) == 1 and 4600 // 23 == 200
zahl("031", paare[0][1])
wahl("032", "Sie sind gleich groß", 36 * 4375 * 5 == 18 * 4375 * 10)
zahl("033", (748362 - 199997) - (748362 - 200000 - 3))
wahl("034", "Die Zahlen nehmen ihre Rechenzeichen mit", 763 - 289 + 237 == 763 + 237 - 289 != 763 - 237 + 289)
zahl("035", F(4368 * 75, 1456 * 25))
# verteilen
def fehlt_036(o):
    teile = [term(t) for t in re.findall(r"\d+ · \d+", o)]
    return 300 * 40 + 68 * 7 + sum(teile) == 368 * 47


wahl_genau("036", fehlt_036)
zahl("037", 2347 * 89 - 2347 * 86)
wahl("038", "Erst werden alle vier Eis bezahlt, danach alle vier Getränke", 4 * 2 + 4 * 3 == 4 * (2 + 3))
verteilt_produkt = lambda a, b, c: a * b * a * c                     # Regel des Kindes: a · (b · c) = a · b · a · c
assert (verteilt_produkt(2, 3, 5), verteilt_produkt(3, 2, 4)) == (60, 72)
stimmt = [a for a in range(1, 100) if verteilt_produkt(a, 2, 7) == a * 2 * 7]
assert len(stimmt) == 1
zahl("039", stimmt[0])
wahl("040", "Er wird dreimal so groß", all(3 * h * b1 + 3 * h * b2 == 3 * (h * b1 + h * b2) for h in range(1, 9) for b1 in range(1, 9) for b2 in range(1, 9)))
# umkehraufgabe_mal
zahl("041", sum(1 for a in range(1, 13) if any(a * x == 36 for x in range(1, 37))))
def gilt_042(o, x, q):
    l, rr = o.replace("□", str(q)).replace("x", str(x)).split("=")
    return term(l) == term(rr)


wahl_genau("042", lambda o: all(gilt_042(o, x, 8 * x) for x in range(1, 30)))
wahl("043", "48 Murmeln werden gleichmäßig verteilt", 48 // 8 == 6 and 48 % 8 == 0)
loes = {a: 360 // a for a in range(1, 361) if 360 % a == 0}
wahl("044", "Sie wird zu einem Drittel", all(loes[a] == 3 * loes[3 * a] for a in loes if 3 * a in loes))


mal_immer = all(b % a == 0 for a in range(1, 20) for b in range(1, 20))
geteilt_immer = all((a * b) % a == 0 and (a * b) // a == b for a in range(1, 20) for b in range(1, 20))
wahl("045", "Nur die Mal-Gleichung kann ohne Lösung sein", not mal_immer and geteilt_immer)
# ueberschlag
fragen = {"Reichen 500 € für 26 Karten zu je 19 €?": (26, 19, 500), "Reichen 100 € für 4 Spiele zu je 19 €?": (4, 19, 100),
          "Passen 6 Kisten zu je 38 kg auf einen Wagen für 300 kg?": (6, 38, 300), "Reichen 400 Plätze für 9 Klassen mit je 27 Kindern?": (9, 27, 400)}
auf = lambda z: z if z < 10 else -(-z // 10) * 10                       # zweistellige Zahlen auf Zehner aufrunden, einstellige genau lassen
sicher = {f: auf(a) * auf(b) <= g for f, (a, b, g) in fragen.items()}     # aufgerundeter Überschlag unter der Grenze = sicher
wahl_genau("049", lambda o: not sicher[o])
abschneiden = lambda z: z // 1000 * 1000
runden = lambda z: (z + 500) // 1000 * 1000
assert (abschneiden(6812) + abschneiden(3487),) == (9000,)
zahl("047", max(runden(a) + runden(b) - abschneiden(a) - abschneiden(b) for a in range(1000, 10000) for b in (1000, 1499, 1500, 9999)))
wahl("048", "B ist genauer als A", abs(4800 + 3500 - 8299) < abs(5000 + 3000 - 8299) and 4812 + 3487 == 8299)
assert len(str(3000 * 3000)) == 7 and len(str(3400 * 3400)) == len(str(3500 * 3500)) == 8
zahl("046", len(str(3412 * 3438)))
wahl("050", "Größer", F(7236, 9) > 700 and F(7000, 10) < F(7236, 10) < F(7236, 9))
# sach
zahl("051", erste(lambda g: 4 + 4 * g > 12 + 2 * g, 100))
busse = 0
rest = 189
while rest > 0:
    busse += 1
    rest -= 52
wahl("052", "Wie viele Busse werden gebraucht", busse == 4 and 189 // 52 == 3 and 189 % 52 == 33)
zahl("053", sum(1 for h in range(1, 21) for t in range(1, 21) if 3 * h + 2 * t == 20))
wahl("054", "Mias Ergebnis ist immer um 6 größer", {(x + 6) * 2 - (2 * x + 6) for x in range(1, 2000)} == {6})
wahl("055", "4 · x + 12 − 4 = 108", erste(lambda x: 4 * x + 12 - 4 == 108, 1000, 1) == 25)

fehlt = sorted(set(Q) - gesehen)
if fehlt:
    abw.append(("nicht geprüft", fehlt))
for x in abw:
    print("ABWEICHUNG", x)
print(f"{len(gesehen)} Sollantworten neu gerechnet, {len(abw)} Abweichungen")
