#!/usr/bin/env python3
"""Prüft inhalte/regeln/regeln.json und inhalte/regeln/zuordnung.json.

Aufruf (vom Repo-Wurzelordner):  python3 -I tools/regeln_pruefen.py
Prüft: Zahl der Regeln und Arbeitsweisen, Pflichtfelder, Textlängen, alle Rechnungen und Beispiele
(Gewand-Zeilen, Grenze, Probe, Klassen-Beispiele soweit lesbar), Gegenseitigkeit von baut_auf / grundlage_fuer,
und dass jedes Thema und jede Lernkarte der Zuordnung im Bestand (inhalte/themen/*.json) vorkommt.
Exit-Code 0 = alles in Ordnung. Keine Datenbank, keine Lerndaten.

Schreibweise in den Rechnungen: {a|b} = Bruch, ⟦…⟧ = gelb markiert, __…__ = unterstrichen,
{x} in "vorlage" = Platz für die eingesetzte Zahl.
"""
import json
import os
import re
import sys
from fractions import Fraction

sys.dont_write_bytecode = True
WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGELN = os.path.join(WURZEL, "inhalte", "regeln", "regeln.json")
ZUORD = os.path.join(WURZEL, "inhalte", "regeln", "zuordnung.json")
THEMEN = os.path.join(WURZEL, "inhalte", "themen")

SUP = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9"}
CANDS = [Fraction(k, 12) for k in range(-120, 121)]


def N(s):
    return Fraction(s.replace(",", "."))


def nach_python(s):
    """Wandelt eine Rechnung der Karten in Python um (Fraction-Rechnung)."""
    s = s.replace("⟦", "").replace("⟧", "").replace("__", "")
    s = re.sub(r"(\d+(?:,\d+)?) % von (\{[^}]*\}|[0-9,]+|x)", r"(\1/100)*(\2)", s)
    s = re.sub(r"\{([^{}|]*)\|([^{}|]*)\}", r"((\1)/(\2))", s)
    s = s.replace("−", "-").replace("·", "*").replace(":", "/")
    s = re.sub("[⁰¹²³⁴⁵⁶⁷⁸⁹]+", lambda m: "**(" + "".join(SUP[c] for c in m.group()) + ")", s)
    s = re.sub(r"(\d)(x)", r"\1*\2", s)
    s = re.sub(r"\)\s*(\(|x|\d)", r")*\1", s)
    s = re.sub(r"x\s*\(", "x*(", s)
    s = re.sub(r"(?<![A-Za-z_\d.\"])\d+(?:,\d+)?", lambda m: 'N("%s")' % m.group(), s)
    return s


def wert(s, x=None):
    return eval(nach_python(s), {"N": N, "x": x, "__builtins__": {}})


def hat_x(s):
    return re.search(r"(?<![A-Za-zäöü])x(?![A-Za-zäöü])", s) is not None


def kette(teil, x=None):
    """Prüft 'a = b = c' oder 'a ≠ b' (Zahlen). Gibt True/False."""
    teile = re.split(r"(=|≠)", teil)
    werte = [wert(t.strip(), x) for t in teile[0::2]]
    ops = teile[1::2]
    return all((werte[i] == werte[i + 1]) == (ops[i] == "=") for i in range(len(ops)))


def loesungen(teil):
    """Alle Kandidaten x, für die die Kette stimmt."""
    return {c for c in CANDS if kette_sicher(teil, c)}


def kette_sicher(teil, x):
    try:
        return kette(teil, x)
    except ZeroDivisionError:
        return False


def zeile_ok(z):
    """Eine Zeile der Gewand-Karte. Formen: 'a = b' | 'G → G2' | 'G → T1 oder T2' (Gleichungen)."""
    if "→" in z:
        links, rechts = [t.strip() for t in z.split("→")]
        teile = [t.strip() for t in rechts.split(" oder ")]
        if hat_x(z):
            return loesungen(links) == set().union(*[loesungen(t) for t in teile])
        return kette(links) and any(kette(t) for t in teile) and (len(teile) > 1 or kette(teile[0]))
    if hat_x(z):
        return all(kette_sicher(z, c) for c in [Fraction(2), Fraction(3), Fraction(4), Fraction(1, 2), Fraction(5, 3)])
    return kette(z)


def fmt(q):
    if q.denominator == 1:
        return str(q.numerator)
    d = q.denominator
    for p in (2, 5):
        while d % p == 0:
            d //= p
    if d == 1:
        s = ("%.6f" % float(q)).rstrip("0").rstrip(".")
        return s.replace(".", ",")
    return "%d/%d" % (q.numerator, q.denominator)


def saetze(t):
    return [s for s in re.split(r"(?<=[.!?“])\s+(?=[A-ZÄÖÜ„(])", t.strip()) if s]


def pruefen():
    fehler, hinweise = [], []

    def f(m):
        fehler.append(m)

    r = json.load(open(REGELN, encoding="utf-8"))
    z = json.load(open(ZUORD, encoding="utf-8"))
    regeln = r.get("regeln", [])
    aw = r.get("arbeitsweisen", [])
    if len(regeln) != 15:
        f("Regeln: %d statt 15" % len(regeln))
    if len(aw) != 5:
        f("Arbeitsweisen: %d statt 5" % len(aw))
    if [x.get("nr") for x in regeln] != list(range(1, 16)):
        f("Nummern der Regeln nicht 1..15")
    kennungen = [x.get("kennung") for x in regeln]
    if len(set(kennungen)) != len(kennungen) or any(not re.fullmatch(r"[a-z]+", k or "") for k in kennungen):
        f("Kennungen: doppelt oder nicht nur Kleinbuchstaben ohne Umlaute")
    planeten = {p["id"]: p for p in r.get("planeten", [])}
    zu_planet = {}
    for p in planeten.values():
        for n in p.get("regeln", []):
            zu_planet[n] = p["id"]
    if sorted(zu_planet) != list(range(1, 16)):
        f("Planeten ordnen nicht genau die Regeln 1..15 zu")

    pflicht = ["nr", "kennung", "name", "name_fachlich", "planet", "satz", "weg_b_satz", "bild", "gewand", "grenze", "probe",
               "merksatz", "erklaerung_lehrer", "gilt_nicht", "klassen", "lehrplan", "baut_auf", "grundlage_fuer", "fehlbilder"]
    grenzen = {"satz": 90, "satz2": 90, "weg_b_satz": 60, "merksatz": 190, "gilt_nicht": 330}
    anz = {"gewand": 0, "grenze": 0, "probe": 0, "klassen": 0, "klassen_gerechnet": 0}
    for g in regeln:
        n = g.get("nr")
        for k in pflicht:
            if k not in g or (g[k] in (None, "", []) and k not in ("baut_auf", "grundlage_fuer")):
                f("Regel %s: Feld %s fehlt oder leer" % (n, k))
        if zu_planet.get(n) != g.get("planet"):
            f("Regel %s: Planet passt nicht zu den Planeten-Daten" % n)
        for k, m in grenzen.items():
            if len(g.get(k, "")) > m:
                f("Regel %s: %s zu lang (%d > %d)" % (n, k, len(g[k]), m))
        if not re.fullmatch(r"Hier hat .* (geklemmt|gefehlt)\.", g.get("weg_b_satz", "")):
            f("Regel %s: weg_b_satz hat nicht die Form 'Hier hat … geklemmt.'" % n)
        ez = g.get("erklaerung_lehrer", "")
        if not 2 <= len(saetze(ez)) <= 3:
            f("Regel %s: erklaerung_lehrer hat %d Sätze (2 bis 3 verlangt)" % (n, len(saetze(ez))))
        b = g.get("bild", {})
        for k in ("art", "motiv", "beschreibung", "unter"):
            if not b.get(k):
                f("Regel %s: bild.%s fehlt" % (n, k))
        if len(b.get("unter", "")) > 170:
            f("Regel %s: bild.unter zu lang" % n)
        # Gewand
        gw = g.get("gewand", [])
        if [x.get("art") for x in gw] != ["Zahlen", "mit x", "mit Brüchen"]:
            f("Regel %s: Gewand muss Zahlen / mit x / mit Brüchen heißen" % n)
        for x in gw:
            anz["gewand"] += 1
            try:
                if not zeile_ok(x["rechnung"]):
                    f("Regel %s: Gewand-Zeile '%s' stimmt nicht" % (n, x["rechnung"]))
            except Exception as e:  # noqa
                f("Regel %s: Gewand-Zeile nicht lesbar (%s): %s" % (n, e, x.get("rechnung")))
        # Grenze
        gr = g.get("grenze", {})
        for k in ("satz", "text", "rechnung"):
            if not gr.get(k):
                f("Regel %s: grenze.%s fehlt" % (n, k))
        if len(gr.get("text", "")) > 230:
            f("Regel %s: grenze.text zu lang" % n)
        zl = gr.get("rechnung", [])
        try:
            for line in zl:
                for teil in line.split(" und "):
                    if not kette(teil):
                        f("Regel %s: Grenze-Zeile '%s' stimmt nicht" % (n, line))
            if len(zl) == 2 and "≠" in zl[0] and "≠" in zl[1] and "und" not in zl[1]:
                a1, a2 = [wert(t) for t in zl[0].split("≠")]
                b1, b2 = [wert(t) for t in zl[1].split("≠")]
                if (a1, a2) != (b1, b2):
                    f("Regel %s: Grenze: Zeile 2 gibt nicht die Werte von Zeile 1" % n)
            anz["grenze"] += 1
        except Exception as e:  # noqa
            f("Regel %s: Grenze nicht lesbar (%s)" % (n, e))
        # Probe
        pb = g.get("probe", {})
        try:
            erg = pb["ergebnisse"]
            gleich = 0
            for xs in ("2", "3", "4"):
                lw = wert(pb["vorlage"][0].replace("{x}", xs))
                rw = wert(pb["vorlage"][1].replace("{x}", xs))
                if [fmt(lw), fmt(rw)] != erg[xs]:
                    f("Regel %s: Probe x=%s: gerechnet %s / %s, gespeichert %s" % (n, xs, fmt(lw), fmt(rw), erg[xs]))
                gleich += lw == rw
            soll = "stimmt" if gleich == 3 else ("stimmt_nicht" if gleich == 0 else "teils")
            if pb.get("gesamt") != soll:
                f("Regel %s: Probe gesamt ist %s, gerechnet %s" % (n, pb.get("gesamt"), soll))
            if pb.get("vorgewaehlt") != 3:
                f("Regel %s: Probe: 3 muss vorgewählt sein" % n)
            anz["probe"] += 1
        except Exception as e:  # noqa
            f("Regel %s: Probe nicht lesbar (%s)" % (n, e))
        # Klassen
        kl = g.get("klassen", [])
        if not kl:
            f("Regel %s: keine Klassen-Beispiele" % n)
        for k in kl:
            anz["klassen"] += 1
            try:
                if "=" in k["text"] or "≠" in k["text"]:
                    teile = [t for t in re.split(r", also |, aber ", k["text"])]
                    ok = all(kette(t) for t in teile if re.search(r"[=≠]", t) and not hat_x(t))
                    if not ok:
                        f("Regel %s Klasse %s: Beispiel '%s' stimmt nicht" % (n, k["klasse"], k["text"]))
                    anz["klassen_gerechnet"] += 1
            except Exception:
                hinweise.append("Regel %s Klasse %s: Beispiel nicht maschinell lesbar: %s" % (n, k.get("klasse"), k.get("text")))
        # Lehrplan
        lp = g.get("lehrplan")
        if lp != "nicht geprüft":
            if not isinstance(lp, dict) or not lp.get("quelle"):
                f("Regel %s: lehrplan muss 'nicht geprüft' sein oder eine Quelle nennen" % n)
            else:
                for q in lp["quelle"]:
                    if not os.path.exists(os.path.join(WURZEL, q)):
                        f("Regel %s: Lehrplan-Quelle fehlt im Repo: %s" % (n, q))
        for fb in g.get("fehlbilder", []):
            if not fb.get("kennung") or not fb.get("beschreibung") or len(saetze(fb["beschreibung"])) > 2:
                f("Regel %s: Fehlbild unvollständig oder länger als ein Satz-Paar" % n)
    # Gegenseitigkeit
    by = {g["nr"]: g for g in regeln}
    for g in regeln:
        for m in g.get("baut_auf", []):
            if m not in by or g["nr"] not in by[m].get("grundlage_fuer", []):
                f("Regel %s baut auf %s, aber %s nennt %s nicht als grundlage_fuer" % (g["nr"], m, m, g["nr"]))
        for m in g.get("grundlage_fuer", []):
            if m not in by or g["nr"] not in by[m].get("baut_auf", []):
                f("Regel %s ist Grundlage für %s, aber %s nennt %s nicht in baut_auf" % (g["nr"], m, m, g["nr"]))
        if g["nr"] in g.get("baut_auf", []) + g.get("grundlage_fuer", []):
            f("Regel %s verweist auf sich selbst" % g["nr"])
    # Kreisfreiheit
    zustand = {}

    def tief(n):
        if zustand.get(n) == 1:
            f("Kreis in baut_auf bei Regel %s" % n)
            return
        if zustand.get(n) == 2:
            return
        zustand[n] = 1
        for m in by[n].get("baut_auf", []):
            tief(m)
        zustand[n] = 2
    for n in by:
        tief(n)
    # Arbeitsweisen
    for a in aw:
        for k in ("nr", "kennung", "name", "satz"):
            if not a.get(k):
                f("Arbeitsweise %s: Feld %s fehlt" % (a.get("nr"), k))
        if len(a.get("satz", "")) > 90:
            f("Arbeitsweise %s: Satz zu lang" % a.get("nr"))
    # Zuordnung
    zr = z.get("regeln", [])
    if [x.get("nr") for x in zr] != list(range(1, 16)):
        f("Zuordnung: Regeln nicht 1..15")
    buckets = {"ja": 0, "teilweise": 0, "nein": 0}
    cache = {}

    def thema(t):
        if t not in cache:
            p = os.path.join(THEMEN, t + ".json")
            cache[t] = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None
        return cache[t]
    for x in zr:
        n = x.get("nr")
        if x.get("kennung") != by.get(n, {}).get("kennung"):
            f("Zuordnung %s: Kennung passt nicht zu regeln.json" % n)
        if x.get("sicher") not in buckets:
            f("Zuordnung %s: sicher muss ja/teilweise/nein sein" % n)
        else:
            buckets[x["sicher"]] += 1
        if not x.get("begruendung"):
            f("Zuordnung %s: Begründung fehlt" % n)
        leer = not any(t.get("lernkarten") for t in x.get("themen", []))
        if leer and not x.get("offen"):
            f("Zuordnung %s: ohne Lernkarte, aber nicht als offen markiert" % n)
        if leer and x.get("sicher") == "ja":
            f("Zuordnung %s: ohne Lernkarte kann 'sicher' nicht ja sein" % n)
        for liste, name in ((x.get("themen", []), "themen"), (x.get("vielleicht", []), "vielleicht")):
            for t in liste:
                d = thema(t["thema"])
                if d is None:
                    f("Zuordnung %s: Thema %s gibt es nicht" % (n, t["thema"]))
                    continue
                lz = [e["lernziel"] for e in d["inhalt"]["etappen"]]
                for k in t.get("lernkarten", []):
                    if k not in lz:
                        f("Zuordnung %s: Lernkarte %s.%s gibt es nicht" % (n, t["thema"], k))
        if len(x.get("beispielaufgaben", [])) > 3:
            f("Zuordnung %s: mehr als drei Beispielaufgaben" % n)
        for b in x.get("beispielaufgaben", []):
            d = thema(b["thema"])
            try:
                a = d["aufgaben"][b["index"]]
                if a["l"] != b["lernziel"]:
                    f("Zuordnung %s: Aufgabe %s#%s gehört zu %s, nicht %s" % (n, b["thema"], b["index"], a["l"], b["lernziel"]))
            except Exception:
                f("Zuordnung %s: Aufgabe %s#%s gibt es nicht" % (n, b.get("thema"), b.get("index")))
    return fehler, hinweise, anz, buckets


if __name__ == "__main__":
    fehler, hinweise, anz, buckets = pruefen()
    print("Regeln und Arbeitsweisen gezählt; Rechnungen geprüft: Gewand-Zeilen %(gewand)d, Grenzen %(grenze)d, Proben %(probe)d, "
          "Klassen-Beispiele %(klassen)d (davon maschinell gerechnet %(klassen_gerechnet)d)" % anz)
    print("Zuordnung sicher: ja %(ja)d, teilweise %(teilweise)d, nein %(nein)d" % buckets)
    for h in hinweise:
        print("Hinweis:", h)
    for m in fehler:
        print("FEHLER:", m)
    print("OK" if not fehler else "%d Fehler" % len(fehler))
    sys.exit(1 if fehler else 0)
