"""Mathe-Profi: Fachwörter Summe · Differenz · Produkt · Quotient – Wort in Term übersetzen.

Aufruf: python3 -I inhalte/mathe-profi/fachwoerter/bauen.py
Thema `zahlen.rechengesetze`, Lernkarte `termaufbau` (Flug z1, Klasse 5).
Anlass: In dieser Lernkarte verlangen von 42 Aufgaben nur 3 die Übersetzung Wort → Term, alle drei als Auswahl.
Geprüft: jede Rechnung zweifach, Lücken mit eindeutiger Lösung, keine Lücke hinter einem Komma,
inhalt_pruefen an einer Kopie der Themen-Datei (vorher = nachher), kein Text wörtlich im Bestand.
Nur Inhalte. Nichts wird eingespielt.
"""
import json
import os
import re
import subprocess
import sys
import tempfile
from fractions import Fraction as F

sys.dont_write_bytecode = True
HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
sys.path.insert(0, os.path.join(WURZEL, "tools"))
import inhalt_pruefen as ip      # noqa: E402

THEMA, LK, TF = "zahlen.rechengesetze", "termaufbau", "terme"
KENN = json.load(open(os.path.join(HIER, "..", "regeln-uebersicht", "kennungen.json"), encoding="utf-8"))["kennungen"]
REGELN = {e["kennung"]: e for e in KENN}
FEHLBILD = {f["kennung"]: e["kennung"] for e in KENN for f in e["fehlbilder"]}
TYP = {4: "Lückenweg", 12: "Fehler-Detektiv (einfache Form)", 13: "Verfahren wählen (einfache Form)", 17: "Umkehren", "B": "Brücke", "A": "Anwenden"}
TERM, REIH, PM, VZ = "id.algebra.term", "rr.reihenfolge", "rr.plusminus", "rr.vorzeichen"
A = []


def z2(ausdruck):
    return F(eval(re.sub(r"(?<![\w.])(\d+)(?![\w.])", r"F(\1)", ausdruck), {"__builtins__": {}}, {"F": F, "abs": abs}))


def neu(typ, s, g, regel, zaehlt, aufgabe, zweit, fb, probe=None):
    A.append(dict(typ=typ, regel=regel, zaehlt=zaehlt, aufgabe={"l": LK, "t": TF, "p": "uebung", "s": s, "g": g, **aufgabe}, zweit=zweit, fb=fb, probe=probe))


def luecken(text, schablone, werte, c, h, w, hinweis="Je Lücke eine ganze Zahl (mit Minus, falls negativ)."):
    return {"y": "luecken", "f": {"text": text, "schablone": schablone, "hinweis": hinweis}, "o": {"werte": werte}, "c": c, "h": h, "w": w}


def zahl(text, wert, c, h, w):
    return {"y": "zahl", "f": {"text": text}, "o": {"wert": wert}, "c": c, "h": h, "w": w}


def wahl(text, antworten, index, h, w):
    return {"y": "auswahl", "f": {"text": text}, "a": antworten, "o": {"index": index}, "h": h, "w": w}


# ───────────── Stufe 1: die vier Wörter und die Reihenfolge ─────────────
neu(4, 1, "direkt", TERM, "ja",
    luecken("Schreibe als Term: die Differenz aus 42 und 17. Achte auf die Reihenfolge.", "□ − □", [42, 17], ["42", "17"],
            "Differenz heißt minus. Welche Zahl steht zuerst?", "Die Differenz aus 42 und 17 ist 42 − 17. Die zuerst genannte Zahl steht vorn. Bei 17 − 42 wären die Zahlen vertauscht, und es käme −25 statt 25 heraus."),
    ["42", "17"], {0: [(17, None, "die beiden Zahlen vertauscht")], 1: [(42, None, "die beiden Zahlen vertauscht")]})
neu(4, 1, "direkt", TERM, "ja",
    luecken("Schreibe als Term: der Quotient aus 72 und 9.", "□ : □", [72, 9], ["72", "9"],
            "Quotient heißt geteilt. Welche Zahl wird geteilt?", "Der Quotient aus 72 und 9 ist 72 : 9. Die zuerst genannte Zahl wird geteilt, sie heißt Dividend. Bei 9 : 72 wären die beiden Zahlen vertauscht, und es käme kein ganzzahliges Ergebnis heraus. (Der Wert ist 8.)"),
    ["72", "9"], {0: [(9, None, "die beiden Zahlen vertauscht")], 1: [(72, None, "die beiden Zahlen vertauscht")]})
neu(13, 1, "erkennen", TERM, "ja",
    wahl("Welcher Ausdruck ist die Differenz aus 5 und 12?", ["12 − 5", "5 − 12", "5 + 12", "12 : 5"], 1,
         "Bei „aus … und …“ steht die zuerst genannte Zahl vorn.", "Die Differenz aus 5 und 12 ist 5 − 12 = −7. Bei 12 − 5 wären die Zahlen vertauscht."),
    lambda: 5 - 12 == -7 and 12 - 5 == 7, {0: (None, "die Zahlen vertauscht – das wäre die Differenz aus 12 und 5"), 2: (None, "Summe statt Differenz"), 3: (None, "Quotient statt Differenz")})
neu("B", 1, "direkt", PM, "ja",
    zahl("Berechne die Summe aus −7 und 19.", 12, "-7 + 19",
         "Summe heißt plus – auch wenn eine der beiden Zahlen negativ ist.", "Die Summe aus −7 und 19 ist −7 + 19 = 12. Von −7 aus 19 nach rechts: über die Null hinaus bis 12."),
    ["19-7"], [(-26, "fb.plusminus.zeichen_des_ergebnisses", "−7 − 19 gerechnet: Differenz statt Summe"), (26, None, "7 + 19 gerechnet: das Minus übersehen")])

# ───────────── Stufe 2: zusammengesetzte Terme und die „von“-Falle ─────────────
neu(4, 2, "mehrschritt", REIH, "ja",
    luecken("Multipliziere die Differenz aus 3 und 11 mit der Summe aus −6 und 2. Setze die vier Zahlen ein und rechne aus.",
            "(□ − □) · (□ + □) = □", [3, 11, -6, 2, 32], ["3", "11", "-6", "2", "(3 - 11) * (-6 + 2)"],
            "Erst jede Klammer für sich, dann malnehmen.", "(3 − 11) · (−6 + 2) = (−8) · (−4) = 32. Zwei Minus ergeben beim Malnehmen ein Plus."),
    ["3", "11", "0-6", "2", "(0-8)*(0-4)"], {4: [(-32, "fb.vorzeichen.falsches_zeichen", "Minus mal Minus als Minus gerechnet"), (12, None, "(−8) + (−4) gerechnet: addiert statt malgenommen")]})
neu("B", 2, "mehrschritt", REIH, "ja",
    zahl("Berechne: Subtrahiere das Produkt aus 4 und 6 von 50.", 26, "50 - 4 * 6",
         "„Von 50 subtrahieren“ heißt: 50 steht vorn.", "Produkt aus 4 und 6: 24. Von 50 abgezogen: 50 − 24 = 26."),
    ["50-24"], [(-26, None, "24 − 50 gerechnet: „von“ überlesen und die Reihenfolge vertauscht"), (74, None, "dazugezählt statt abgezogen"), (184, "fb.reihenfolge.links_nach_rechts", "(50 − 4) · 6 gerechnet")])
neu(12, 2, "mehrschritt", REIH, "ja",
    wahl("Jemand schreibt für „Subtrahiere die Summe aus 3 und 4 von 20“ den Term 3 + 4 − 20. Was stimmt?",
         ["Der Term ist richtig.", "Richtig wäre 20 − 3 + 4.", "Richtig wäre 20 − (3 + 4) = 13.", "Richtig wäre 20 : (3 + 4)."], 2,
         "Von welcher Zahl wird etwas abgezogen? Und was wird abgezogen?", "Abgezogen wird die ganze Summe, und zwar von 20: 20 − (3 + 4) = 20 − 7 = 13. Der Term 3 + 4 − 20 ergibt −13."),
    lambda: 20 - (3 + 4) == 13 and 3 + 4 - 20 == -13 and 20 - 3 + 4 == 21,
    {0: (None, "„von 20“ überlesen: so wird von der Summe abgezogen"), 1: (None, "die Klammer fehlt – so wird nur die 3 abgezogen"), 3: (None, "geteilt statt abgezogen")})
neu(17, 2, "umkehr", TERM, "ja",
    wahl("Welcher Satz beschreibt den Term (20 + 4) : 6?",
         ["Teile die Summe aus 20 und 4 durch 6.", "Addiere 20 zum Quotienten aus 4 und 6.", "Teile 20 durch die Summe aus 4 und 6.", "Bilde die Summe aus 20 und dem Quotienten aus 4 und 6."], 0,
         "Was steht in der Klammer, und was passiert mit der ganzen Klammer?", "Zuerst wird die Summe 20 + 4 gebildet, dann durch 6 geteilt: 24 : 6 = 4."),
    lambda: F(20 + 4, 6) == 4, {1: (None, "das wäre 20 + 4 : 6"), 2: (None, "das wäre 20 : (4 + 6)"), 3: (None, "das wäre ebenfalls 20 + 4 : 6")})
neu(4, 2, "darstellung", TERM, "ja",
    luecken("Schreibe als Term: das Dreifache der Summe aus −5 und 9.", "□ · (□ + □)", [3, -5, 9], ["3", "-5", "9"],
            "„Das Dreifache von etwas“ heißt: mal 3. Die Klammer hält die Summe zusammen.", "Das Dreifache der Summe aus −5 und 9 ist 3 · (−5 + 9) = 3 · 4 = 12. Ohne Klammer käme 3 · (−5) + 9 = −6 heraus."),
    ["3", "0-5", "9"], {})
neu("B", 2, "mehrschritt", REIH, "ja",
    zahl("Berechne den Quotienten aus der Summe von 72 und 18 und der Differenz aus 15 und 6.", 10, "(72 + 18) / (15 - 6)",
         "Rechne zuerst die beiden Klammern aus.", "Summe: 72 + 18 = 90. Differenz: 15 − 6 = 9. Quotient: 90 : 9 = 10."),
    ["90/9"], [(81, "fb.reihenfolge.links_nach_rechts", "72 + 18 : 15 − 6 ohne Klammern gerechnet"), (9, None, "die Differenz als Ergebnis genannt")])

# ───────────── Stufe 3: rückwärts und begründen ─────────────
neu(17, 3, "rueckwaerts", REIH, "ja",
    zahl("Von welcher Zahl muss man das Produkt aus 6 und 7 abziehen, damit 8 herauskommt?", 50, "8 + 6 * 7",
         "Rechne rückwärts: Was wird abgezogen, und was bleibt übrig?", "Das Produkt ist 42. Gesucht ist die Zahl, von der 42 abgezogen 8 ergibt: 8 + 42 = 50. Probe: 50 − 42 = 8."),
    ["42+8"], [(34, "fb.gegenrechnung.gleiche_rechnung", "42 − 8 gerechnet statt 42 + 8"), (42, None, "nur das Produkt genannt")])
neu(12, 3, "begruenden", TERM, "ja",
    wahl("Jemand sagt: „Die Differenz aus 5 und 9 ist dasselbe wie die Differenz aus 9 und 5.“ Stimmt das?",
         ["Ja, beim Minus darf man tauschen.", "Nein: 5 − 9 = −4, aber 9 − 5 = 4.", "Ja, denn beide Male steht 4 da.", "Das lässt sich nicht entscheiden."], 1,
         "Rechne beide Differenzen aus und vergleiche.", "5 − 9 = −4 und 9 − 5 = 4. Die Zahlen sind verschieden. Tauschen darf man nur bei Plus und Mal."),
    lambda: 5 - 9 == -4 and 9 - 5 == 4, {0: ("fb.tauschen.minus_getauscht", "beim Minus getauscht"), 2: (None, "nur die Ziffern verglichen, nicht die Vorzeichen"), 3: (None, "beide Werte lassen sich ausrechnen")})
neu(17, 3, "rueckwaerts", REIH, "ja",
    luecken("Setze die Zahlen 3, 5 und 8 so in den Term ein, dass der Wert 25 herauskommt. Jede Zahl genau einmal.",
            "□ · (□ − □)", [5, 8, 3], ["5", "8", "3"],
            "Probiere: Welche Zahl steht vorn, welche beiden gehören in die Klammer?", "5 · (8 − 3) = 5 · 5 = 25. Die anderen Anordnungen ergeben 8 · (5 − 3) = 16 und 3 · (8 − 5) = 9."),
    ["5", "8", "3"], {}, probe=lambda: 5 * (8 - 3) == 25 and 8 * (5 - 3) == 16 and 3 * (8 - 5) == 9)

# ───────────── Prüfen ─────────────
KOMMA_LUECKE = re.compile(r"\d\s*,\s*[①②③④⑤□]")
aus = []
n_rechnung = n_fb = 0
for i, a in enumerate(sorted(A, key=lambda a: a["aufgabe"]["s"]), 1):
    q, kenn = a["aufgabe"], f"FW-{i:02d}"
    assert a["regel"] in REGELN, (kenn, a["regel"])
    assert ip.STUFE_VON[q["g"]] == q["s"], (kenn, q["g"], q["s"])
    assert a["typ"] in TYP and a["zaehlt"] in ("ja", "folge", "nein"), kenn
    if a["probe"]:
        assert a["probe"]() is True, kenn
    eintrag = dict(kennung=kenn, thema=THEMA, lernkarte=LK, stufe=q["s"], typ=TYP[a["typ"]], antwortform=q["y"],
                   regel=a["regel"], regel_name=REGELN[a["regel"]]["name"], zaehlt=a["zaehlt"], fehlbilder=[])

    def fb_eintrag(ort, antwort, fbk, text):
        global n_fb
        assert fbk is None or fbk in FEHLBILD, (kenn, fbk)
        n_fb += 1
        eintrag["fehlbilder"].append(dict(**ort, antwort=antwort, fehlbild=fbk, regel_des_fehlbilds=FEHLBILD.get(fbk), beschreibung=text))

    if q["y"] == "zahl":
        soll = ip.rechne(q["c"])
        assert soll == ip.zahlwert(q["o"]["wert"]) == z2(a["zweit"][0]), (kenn, soll)
        n_rechnung += 1
        for w, fbk, text in a["fb"]:
            assert w != q["o"]["wert"], (kenn, w)
            fb_eintrag({}, w, fbk, text)
    elif q["y"] == "luecken":
        assert not KOMMA_LUECKE.search(q["f"]["text"] + " " + q["f"]["schablone"]), (kenn, "Lücke hinter dem Komma")
        soll = [ip.rechne(c) for c in q["c"]]
        assert soll == q["o"]["werte"] == [z2(z) for z in a["zweit"]], (kenn, soll, [z2(z) for z in a["zweit"]])
        assert all(isinstance(w, int) for w in q["o"]["werte"]) and q["f"]["schablone"].count("□") == len(soll), kenn
        assert not re.search(r"[a-z]", q["f"]["schablone"]), (kenn, "Schablone mit Kleinbuchstabe wäre eine Term-Vorlage")
        n_rechnung += len(soll)
        for i2, liste in sorted(a["fb"].items()):
            for w, fbk, text in liste:
                assert w != soll[i2], (kenn, i2, w)
                fb_eintrag({"luecke": i2 + 1}, w, fbk, text)
    else:
        assert a["zweit"]() is True and len(set(q["a"])) == len(q["a"]) >= 3, kenn
        assert set(a["fb"]) == set(range(len(q["a"]))) - {q["o"]["index"]}, kenn
        for i2, (fbk, text) in sorted(a["fb"].items()):
            fb_eintrag({"index": i2}, q["a"][i2], fbk, text)
    eintrag["aufgabe"] = q
    aus.append(eintrag)

lagen = {}
for e in aus:
    if e["antwortform"] == "auswahl":
        lagen.setdefault(len(e["aufgabe"]["a"]), set()).add(e["aufgabe"]["o"]["index"])
assert len(lagen[4]) >= 3, lagen        # richtige Antwort auf wechselnden Plätzen
texte = [e["aufgabe"]["f"]["text"] for e in aus]
assert len(set(texte)) == len(texte)


def lauf(pfad):
    r = subprocess.run([sys.executable, "-I", os.path.join(WURZEL, "tools", "inhalt_pruefen.py"), pfad], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


quelle = os.path.join(WURZEL, "inhalte", "themen", f"{THEMA}.json")
d = json.load(open(quelle, encoding="utf-8"))
liste = [e["aufgabe"] for e in aus]
assert all(q["l"] in {x["lernziel"] for x in d["inhalt"]["etappen"]} and q["t"] in {x["k"] for x in d["inhalt"]["teilfaehigkeiten"]} for q in liste)
assert not {x["f"].get("text") for x in d["aufgaben"]} & {q["f"]["text"] for q in liste}, "Text schon im Bestand"
code0, _ = lauf(quelle)
with tempfile.TemporaryDirectory() as tmp:
    d["aufgaben"] = d["aufgaben"] + liste
    ziel = os.path.join(tmp, f"{THEMA}.json")
    json.dump(d, open(ziel, "w", encoding="utf-8"), ensure_ascii=False)
    code1, aus1 = lauf(ziel)
    if code1 != 0:
        for z in aus1.split("\n"):
            if any(k in z for k in ("✗", "FEHLER", "Fehler:", "termaufbau")):
                print("  >", z[:260])
assert code0 == 0 and code1 == 0, (code0, code1)

json.dump({"stand": "2026-11-27", "thema": THEMA, "lernkarte": LK, "klasse": 5, "fuer": "beide Kinder",
           "hinweis": "Übersetzung Wort → Term (Summe, Differenz, Produkt, Quotient). Nicht eingespielt. "
                      "Aufbau je Eintrag wie in rollend-1 bis rollend-3.", "aufgaben": aus},
          open(os.path.join(HIER, "termaufbau.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(aus)} Aufgaben für {THEMA} / {LK}: Stufen {[sum(1 for e in aus if e['stufe'] == s) for s in (1, 2, 3)]}, "
      f"Antwortformen {sorted({e['antwortform'] for e in aus})}; inhalt_pruefen Code {code0} → {code1}")
print(f"{n_rechnung} Rechnungen zweifach nachgerechnet; {n_fb} Fehlbilder, davon {sum(1 for e in aus for x in e['fehlbilder'] if x['fehlbild'])} mit Kennung")
print("OK")
