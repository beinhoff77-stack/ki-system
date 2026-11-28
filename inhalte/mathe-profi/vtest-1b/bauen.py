"""Mathe-Profi, Runde „Verstehen in Tests“ Teil 1b (vtest-1b, Kürzel VT1B): neue Test-, Korrektur- und Nachtest-Aufgaben (Pools test, korrektur, sicherung).

Aufruf: python3 -I inhalte/mathe-profi/vtest-1b/bauen.py     (muss mit „OK“ enden)
Lädt th_<Einheit>.py (je Einheit eine Datei), prüft alle Regeln aus auftrag.md, schreibt je Einheit <Einheit>.json und README.md (aus readme_vorlage.md).
Mit der Umgebungsvariable VT_TEIL=1 werden unvollständige Zwischenstände geprüft (Anzahlen je Lernziel nur nach oben begrenzt); die Abgabe läuft ohne.
Nur Inhalte. Nichts wird eingespielt.
"""
import glob
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from fractions import Fraction as F

sys.dont_write_bytecode = True
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import kern                      # noqa: E402
import pruefhilfen as P          # noqa: E402
from kern import A, ip, WURZEL, G2, G3, FORMEN   # noqa: E402

TEIL = bool(os.environ.get("VT_TEIL"))
KUERZEL = "VT1B"
# Einheit -> gewählte Lernziele (Reihenfolge der Etappen) – siehe auswahl.md
AUSWAHL = {
    "bruch.prozent": ["prozentsatz", "rabatt_aufschlag", "verstehen"],
    "gleichungen.bruch": ["definitionsmenge", "ueber_kreuz", "scheinloesung", "verhaeltnis"],
    "terme.potenzgesetze": ["negativer_exponent", "fehler_finden"],
    "zahlen.potenzen_zehner": ["gross_wissenschaftlich", "negativer_exponent", "vorsilben_klein", "vergleichen_pruefen"],
    "messen.flaechen_vielecke": ["dreieck", "rueckwaerts", "zusammengesetzt", "verstehen"],
}
POOLFOLGE = {"test": 0, "korrektur": 1, "sicherung": 2}
SOLL_ANZAHL = {"test": 1, "korrektur": 3, "sicherung": 3}
FORMNAME = {"anwenden": "Anwenden", "umkehren": "Umkehren", "verfahren_waehlen": "Verfahren wählen", "fehler_detektiv": "Fehler-Detektiv", "bruecke": "Brücke",
            "zwei_wege": "Zwei Wege vergleichen", "viele_antworten": "Viele richtige Antworten (bedingung)", None: "Anwenden"}
geladen = []
for schl in AUSWAHL:
    pfad = os.path.join(HIER, "th_" + schl.replace(".", "_") + ".py")
    if os.path.exists(pfad):
        exec(compile(open(pfad, encoding="utf-8").read(), pfad, "exec"), {"__name__": "th", **{k: getattr(kern, k) for k in dir(kern) if not k.startswith("_")}, "F": F})
        geladen.append(schl)
assert geladen, "keine Themen-Dateien"

# ═════════ Bestand laden ═════════
ALLE_THEMEN = {}
for _p in sorted(glob.glob(os.path.join(WURZEL, "inhalte", "themen", "*.json"))):
    _d = json.load(open(_p, encoding="utf-8"))
    ALLE_THEMEN[_d["thema_schluessel"]] = _d
KARTE = {}
for schl in AUSWAHL:
    d = ALLE_THEMEN[schl]
    alle_lz = json.load(open(os.path.join(WURZEL, "inhalte", "plan", "rollend-einheiten.json"), encoding="utf-8"))["einheiten"][schl]["lz"]
    for lz in AUSWAHL[schl]:
        assert lz in alle_lz, (schl, lz, "gewähltes Lernziel gibt es in der Einheit nicht")
    assert len(AUSWAHL[schl]) == (len(alle_lz) + 1) // 2, (schl, "⌈n/2⌉ Lernziele, n = alle Lernziele der Einheit")
    for a in d["aufgaben"]:
        KARTE.setdefault((schl, a["l"]), a["t"])
GESAMT_TEXT = {a["f"].get("text", "") for d in ALLE_THEMEN.values() for a in d["aufgaben"]}
GESAMT_BAU = {P.bau_ohne_zahl(t) for t in GESAMT_TEXT}
ANDERE_TEXTE, ANDERE_BAU, DP_ANDERE = set(), set(), []
for _p in sorted(glob.glob(os.path.join(WURZEL, "inhalte", "mathe-profi", "rollend-*", "*.json")) + glob.glob(os.path.join(WURZEL, "inhalte", "mathe-profi", "vtest-*", "*.json"))):
    if os.path.basename(os.path.dirname(_p)) == "vtest-1b":
        continue
    _d = json.load(open(_p, encoding="utf-8"))
    for _e in _d.get("aufgaben", []):
        if isinstance(_e, dict) and "aufgabe" in _e and _e["aufgabe"].get("f", {}).get("text"):
            _t = _e["aufgabe"]["f"]["text"]
            ANDERE_TEXTE.add(_t)
            ANDERE_BAU.add(P.bau_ohne_zahl(_t))
            DP_ANDERE.append((os.path.basename(os.path.dirname(_p)) + ":" + str(_e.get("kennung", "")), P.dp_merk(_e["aufgabe"])))
DP_BESTAND = {dat: [(f"{dat}:{i}", P.dp_merk(a)) for i, a in enumerate(d["aufgaben"]) if a["f"].get("text") and a.get("o")] for dat, d in ALLE_THEMEN.items()}
DP_ALLE_BESTAND = [x for lst in DP_BESTAND.values() for x in lst]

# ═════════ Prüfen ═════════
reihe = {schl: i for i, schl in enumerate(AUSWAHL)}
A.sort(key=lambda a: (reihe[a["thema"]], AUSWAHL[a["thema"]].index(a["lk"]), POOLFOLGE[a["pool"]], a["nr"]))
aus = defaultdict(list)
alle_texte, alle_bau = set(), set()
dp_treffer = []
n_rechnung = n_fb = n_fb_rechnung = n_fb_ohne = 0
sollwerte = {}
VERBOTEN_WORTE = re.compile(r"Tipp|Hinweis:|Lückenweg|Hilfe:", re.I)
zaehler = 0
for a in A:
    schl, lk = a["thema"], a["lk"]
    assert schl in geladen and lk in AUSWAHL[schl], (schl, lk, "Lernziel nicht in der Auswahl")
    zaehler += 1
    kenn = f"{KUERZEL}-{zaehler:03d}"
    q = a["aufgabe"]
    assert (schl, lk) in KARTE, (kenn, lk)
    assert a["g"] not in ("direkt", "erkennen"), (kenn, "Typ direkt/erkennen nicht erlaubt")
    assert a["form"] != "lueckenweg", kenn
    assert a["s"] in (2, 3), (kenn, "Stufe 2 oder 3")
    assert a["pool"] != "korrektur" or a["s"] == 2, (kenn, "Korrektur nur Stufe 2")
    q.update({"l": lk, "t": KARTE[(schl, lk)], "p": a["pool"], "s": a["s"], "g": a["g"]})
    q = dict(l=q.pop("l"), t=q.pop("t"), p=q.pop("p"), s=q.pop("s"), g=q.pop("g"), **q)
    a["aufgabe"] = q
    assert "h" not in q and "toleranz" not in q["o"], (kenn, "keine Tipps, keine Toleranz")
    assert len(q["w"]) >= 40, (kenn, "Lösungsweg zu kurz")
    text = q["f"]["text"]
    for t in P.texte_von({"f": q["f"], "h": "", "w": q["w"], "a": q.get("a", [])}):
        assert not P.ZWEIDEUTIG.search(t), (kenn, "Bruch nicht eindeutig", t)
        assert not P.name_treffer(t), (kenn, "Name")
        assert not VERBOTEN_WORTE.search(t), (kenn, "verbotenes Wort", t)
    assert text not in alle_texte, (kenn, "Fragetext doppelt")
    assert text not in GESAMT_TEXT and text not in ANDERE_TEXTE, (kenn, "Fragetext schon im Bestand")
    b = P.bau_ohne_zahl(text)
    assert b not in alle_bau and b not in GESAMT_BAU and b not in ANDERE_BAU, (kenn, "Fragetext nur mit anderen Zahlen schon vorhanden", b)
    alle_texte.add(text)
    alle_bau.add(b)
    dm = P.dp_merk(q)
    for dquelle, db_ in DP_ALLE_BESTAND + DP_ANDERE:
        grund = P.dp_vergleich(dm, db_)
        if grund:
            dp_treffer.append((kenn, grund, dquelle, db_["t"][:110]))
    eintrag = dict(kennung=kenn, thema=schl, lernkarte=lk, pool=a["pool"], typ=a["g"], form=a["form"], stufe=a["s"], zaehlt="ja", lehrplan=a["lp"],
                   abgrenzung=kern.ABG.get((schl, lk), ""), idee=a["idee"], antwortform=q["y"], loesung_rechnung=q.get("c"), fehlbilder=[])
    if a["pool"] == "test":
        eintrag["ersetzt_test"] = True

    def fb_eintrag(ort, antwort, beschr, rech=None):
        global n_fb
        assert beschr and len(beschr) > 12, (kenn, "Beschreibung des Fehlbilds")
        n_fb += 1
        d_ = dict(**ort, antwort=antwort)
        if rech is not None:
            d_["rechnung"] = rech
        eintrag["fehlbilder"].append(dict(**d_, fehlbild=None, regel_des_fehlbilds=None, beschreibung=beschr))

    if q["y"] == "zahl":
        soll = ip.rechne(q["c"])
        assert soll == ip.zahlwert(q["o"]["wert"]), (kenn, soll, q["o"]["wert"])
        zw = a["zweit"][0]
        zwv = ip.rechne(zw) if isinstance(zw, str) else F(str(zw))
        assert F(zwv) == soll, (kenn, "zweite Rechnung", zwv, soll)
        n_rechnung += 1
        if abs(soll) >= 10:
            assert abs(soll) not in P.zahlen_im(text), (kenn, "Ergebnis steht schon im Text")
        assert a["fb"], (kenn, "mindestens ein Fehlbild")
        werte = set()
        for (w, beschr, rech) in a["fb"]:
            assert w != q["o"]["wert"] and w not in werte, (kenn, w)
            werte.add(w)
            P.fb_zahlen_pruefen(kenn, w, beschr, rech, q)
            assert isinstance(rech, str), (kenn, w, "Fehlbild braucht eine Rechnung (Text)")
            P.fb_pruefen(kenn, "Zahl", w, rech)
            n_fb_rechnung += 1
            fb_eintrag({}, w, beschr, rech)
    elif q["y"] == "luecken":
        assert not P.KOMMA_LUECKE.search(text + " " + q["f"]["schablone"]), (kenn, "Lücke hinter dem Komma")
        assert q["f"]["schablone"].count("□") == len(q["o"]["werte"]) and all(isinstance(w, int) for w in q["o"]["werte"]), kenn
        soll = [ip.rechne(c) for c in q["c"]]
        zw = [ip.rechne(z) if isinstance(z, str) else F(z) for z in a["zweit"]]
        assert soll == [F(w) for w in q["o"]["werte"]] == zw, (kenn, soll, a["zweit"])
        n_rechnung += len(soll)
        assert a["fb"], (kenn, "mindestens ein Fehlbild")
        for i, liste in sorted(a["fb"].items()):
            werte = set()
            for (w, beschr, rech) in liste:
                assert w != q["o"]["werte"][i] and w not in werte, (kenn, i, w)
                werte.add(w)
                P.fb_zahlen_pruefen(kenn, w, beschr, rech, q)
                P.fb_pruefen(kenn, f"Lücke {i + 1}", w, rech)
                n_fb_rechnung += 1
                fb_eintrag({"luecke": i + 1}, w, beschr, rech)
    else:
        assert q["y"] == "auswahl", kenn
        assert len(q["a"]) == 4 and len(set(q["a"])) == 4, (kenn, "genau 4 verschiedene Antworten")
        assert a["zweit"]() is True, (kenn, "Probe der Auswahl")
        assert set(a["fb"]) == set(range(4)) - {q["o"]["index"]}, kenn
        n_rechnung += 1
        for i, (_, beschr) in sorted(a["fb"].items()):
            P.fb_zahlen_pruefen(kenn, q["a"][i], beschr, None, q)
            fb_eintrag({"index": i}, q["a"][i], beschr)
            n_fb_ohne += 1
    if a["form"] == "fehler_detektiv" or a["g"] == "fehler":
        if q["y"] == "luecken":
            assert "Zeile" in q["f"]["schablone"] and len(re.findall(r"Zeile \d+:", text)) >= 3 and q["o"]["werte"][0] in range(1, 10), (kenn, "Fehler-Detektiv: luecken Zeile □, richtig □ mit mindestens 3 Zeilen")
        else:
            assert q["y"] == "auswahl" and len(re.findall(r"Zeile \d+:", text)) >= 4 and all(re.search(r"Zeile \d", o_) and re.search(r"\b(weil|denn|da)\b", o_) for o_ in q["a"]), (kenn, "Fehler-Detektiv: auswahl mit mindestens 4 Zeilen, jede Möglichkeit nennt Zeile und Begründung")
    sk = (schl, lk, str(q["o"]["wert"]) if q["y"] == "zahl" else (q["a"][q["o"]["index"]] if q["y"] == "auswahl" else str(q["o"]["werte"])))
    assert sk not in sollwerte or q["y"] == "auswahl", (kenn, "gleicher Sollwert in derselben Etappe wie", sollwerte.get(sk))
    sollwerte[sk] = kenn
    eintrag["aufgabe"] = q
    aus[schl].append(eintrag)

for _f in P.FB_ZAHL_FEHLER:
    print("FEHLBILD-ZAHL:", *_f)
assert not P.FB_ZAHL_FEHLER, "Fehlbild-Beschreibung nennt Zahlen, die weder in der Aufgabe noch in der Rechnung vorkommen"

# ═════════ Anzahlen und Mischung je Lernziel ═════════
verteil = []
for schl in geladen:
    for lk in AUSWAHL[schl]:
        xs = [e for e in aus[schl] if e["lernkarte"] == lk]
        c = Counter(e["pool"] for e in xs)
        ide = Counter(("umkehr" if e["idee"] == "rueckwaerts" else e["idee"]) for e in xs)
        assert max(ide.values()) <= 2, (schl, lk, "höchstens zwei Aufgaben je Idee", dict(ide))
        if not TEIL:
            assert len(ide) >= 5, (schl, lk, "mindestens 5 verschiedene Ideen unter den 7", dict(ide))
        if TEIL:
            assert all(c[p] <= SOLL_ANZAHL[p] for p in SOLL_ANZAHL), (schl, lk, dict(c))
            continue
        assert all(c[p] == SOLL_ANZAHL[p] for p in SOLL_ANZAHL) and len(xs) == 7, (schl, lk, "1 test + 3 korrektur + 3 sicherung", dict(c))
        t = [e for e in xs if e["pool"] == "test"][0]
        assert t["stufe"] in (2, 3), (schl, lk)
        assert all(e["stufe"] == 2 for e in xs if e["pool"] == "korrektur"), (schl, lk, "Korrektur Stufe 2")
        assert {e["stufe"] for e in xs if e["pool"] == "sicherung"} == {2, 3}, (schl, lk, "Sicherung gemischt 2 und 3")
        assert len({e["typ"] for e in xs}) >= 5, (schl, lk, "mindestens 5 verschiedene Typen unter den 7", Counter(e["typ"] for e in xs))
        assert len({(e["typ"], e["form"], e["antwortform"]) for e in xs}) == 7, (schl, lk, "7 verschiedene Bauarten (Typ, Form, Antwortform)")
        assert len({e["form"] for e in xs if e["form"]}) >= 3, (schl, lk, "mindestens 3 verschiedene Formen", Counter(e["form"] for e in xs))
        zs = Counter(e["antwortform"] for e in xs)
        assert zs["auswahl"] <= 5, (schl, lk, "nicht fast nur Auswahl", dict(zs))
if not TEIL:
    assert len(A) == 119, len(A)
lagen = defaultdict(list)
for a in A:
    if a["aufgabe"]["y"] == "auswahl":
        lagen[len(a["aufgabe"]["a"])].append(a["aufgabe"]["o"]["index"])
for k, v in lagen.items():
    if len(v) >= 8:
        assert max(Counter(v).values()) <= len(v) // 2 + 1, ("Lage der richtigen Antwort einseitig", Counter(v))

# ═════════ tools/inhalt_pruefen.py über Bestand + neue Aufgaben ═════════
def lauf(pfad):
    r = subprocess.run([sys.executable, "-I", os.path.join(WURZEL, "tools", "inhalt_pruefen.py"), pfad], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


print("Einheit                             neu  inhalt_pruefen (Bestand → Bestand + neu)")
with tempfile.TemporaryDirectory() as tmp:
    for schl in geladen:
        liste = [e["aufgabe"] for e in aus[schl]]
        quelle = os.path.join(WURZEL, "inhalte", "themen", f"{schl}.json")
        d = json.load(open(quelle, encoding="utf-8"))
        assert all(q["l"] in {e["lernziel"] for e in d["inhalt"]["etappen"]} and q["t"] in {t["k"] for t in d["inhalt"]["teilfaehigkeiten"]} for q in liste), schl
        code0, _ = lauf(quelle)
        d["aufgaben"] = d["aufgaben"] + liste
        ziel = os.path.join(tmp, f"{schl}.json")
        json.dump(d, open(ziel, "w", encoding="utf-8"), ensure_ascii=False)
        code1, aus1 = lauf(ziel)
        print(f"{schl:35} {len(liste):3}  Code {code0} → {code1}")
        if code1 != 0:
            print(aus1[-2500:])
        assert code0 == 0 and code1 == 0, schl

for _t in dp_treffer:
    print("DOPPELUNG", *_t)
assert not dp_treffer, "Doppelungen mit dem Bestand oder früheren Runden (siehe oben)"

# ═════════ Negativproben: die Prüfungen müssen kaputte Aufgaben ablehnen ═════════
def lehnt_ab(f, *args):
    try:
        f(*args)
    except (AssertionError, ZeroDivisionError, ValueError, SyntaxError, KeyError, TypeError):
        return True
    return False


n_neg = Counter()
hs = lambda w: __import__("hashlib").sha256(w.lower().encode()).hexdigest()[:12]
assert P.name_treffer("Heute spielt Zzprobewort mit Kim.", summen={hs("zzprobewort")}) and not P.name_treffer("Heute spielt Alex mit Kim.", summen={hs("zzprobewort")})
n_neg["Namensprüfung"] += 2
assert P.bau_ohne_zahl("Kim kauft 5 Äpfel für 3,20 €.") == P.bau_ohne_zahl("Kim kauft 7 Äpfel für 4,10 €.") != P.bau_ohne_zahl("Kim kauft 5 Birnen für 3,20 €.")
n_neg["Bauplan (nur andere Zahlen = gleich)"] += 2
assert F(42) in P.zahlen_im("Es sind 42 Stück.") and F(1350) in P.zahlen_im("Das sind 1 350 cm².") and F(41) not in P.zahlen_im("Es sind 42 Stück.")
n_neg["Ergebnis steht im Text"] += 3
assert lehnt_ab(P.fb_pruefen, "N", "Zahl", 25, "6 * 4") and lehnt_ab(P.fb_pruefen, "N", "Zahl", 24, None) and P.fb_pruefen("N", "Zahl", 24, "6 * 4") is True
n_neg["Fehlbild-Rechnung stimmt nicht"] += 3
for a in A:
    q = a["aufgabe"]
    if q["y"] != "zahl":
        continue
    assert ip.rechne(q["c"]) == ip.zahlwert(q["o"]["wert"]) and ip.rechne(q["c"]) != ip.zahlwert(q["o"]["wert"]) + 1
    n_neg["Sollwert um 1 verschoben fällt auf"] += 1
    for (fw, fb_text, rech) in a["fb"]:
        assert lehnt_ab(P.fb_pruefen, "N", "Zahl", float(fw) + 1, rech), (a["thema"], a["lk"], fw)
        assert fw != q["o"]["wert"]
        n_neg["Fehlbild-Wert um 1 verschoben fällt auf"] += 1
bekannt = [(d_, a_) for d_, dd in ALLE_THEMEN.items() for a_ in dd["aufgaben"][::37] if a_["y"] == "zahl" and len(a_["f"].get("text", "")) > 60 and len(P.dp_zahlen(a_["f"]["text"])) >= 2][::9]
for d_, a_ in bekannt[:40]:
    m = P.dp_merk(dict(f={"text": a_["f"]["text"].replace("Kim", "Alex") + " Rechne genau."}, o=a_["o"]))
    assert any(P.dp_vergleich(m, b) for _, b in DP_BESTAND[d_]), ("leicht geänderte Bestandsaufgabe nicht erkannt", d_, a_["f"]["text"][:80])
    n_neg["Doppelung mit dem Bestand wird erkannt"] += 1
print("\nSelbstprüfung mit Negativproben:")
for k, v in n_neg.items():
    print(f"  {v:4}  {k}")

# ═════════ Schreiben und Zählen ═════════
print()
print("Einheit                        Lernziele  Aufgaben  Stufe 2/3  Typen  Formen")
gesamt = defaultdict(Counter)
for schl in geladen:
    liste = aus[schl]
    json.dump({"stand": "2026-11-28", "runde": "vtest-1b", "kuerzel": KUERZEL, "titel": schl, "klasse": ALLE_THEMEN[schl]["klasse"], "themen": [schl],
               "hinweis": "Verstehens-Aufgaben für Tests (Pools test, korrektur, sicherung), je Lernziel 1 + 2 + 3. Nicht eingespielt. Je Eintrag: thema, lernkarte, pool, typ (Aufgabentyp g), "
                          "form, stufe, zaehlt, lehrplan, ersetzt_test (nur test), Fehlbilder und unter „aufgabe“ die Aufgabe im Format von inhalte/README.md (ohne Tipp h, ohne Toleranz).",
               "aufgaben": liste}, open(os.path.join(HIER, f"{schl}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for e in liste:
        gesamt["pool"][e["pool"]] += 1
        gesamt["stufe"][e["stufe"]] += 1
        gesamt["typ"][e["typ"]] += 1
        gesamt["form"][e["form"] or "(ohne Form)"] += 1
        gesamt["antwort"][e["antwortform"]] += 1
    s = Counter(e["stufe"] for e in liste)
    print(f"{schl:30} {len(AUSWAHL[schl]):9} {len(liste):9}  {s[2]:3}/{s[3]:<3}   {len({e['typ'] for e in liste}):3}   {len({e['form'] for e in liste})}")
print()
print("Summe Aufgaben", len(A), "| Pools", dict(gesamt["pool"]), "| Stufen", dict(sorted(gesamt["stufe"].items())), "| Antwortformen", dict(gesamt["antwort"]))
print("Typen", dict(gesamt["typ"]))
print("Formen", dict(gesamt["form"]))
print(f"{n_rechnung} Lösungen zweifach nachgerechnet; {n_fb} Fehlbilder ({n_fb_rechnung} als Rechnung nachgerechnet, {n_fb_ohne} bei Auswahl über die Probe)")

# README aus der Vorlage
vorlage = os.path.join(HIER, "readme_vorlage.md")
if os.path.exists(vorlage) and not TEIL:
    z = ["| Einheit | Lernziel | test | korrektur | sicherung | Stufe 2 / 3 | Antwortformen (Zahl / Auswahl / Lücken) | Typen | Formen |", "|---|---|---|---|---|---|---|---|---|"]
    for schl in geladen:
        for lk in AUSWAHL[schl]:
            xs = [e for e in aus[schl] if e["lernkarte"] == lk]
            pc, sc, ac = Counter(e["pool"] for e in xs), Counter(e["stufe"] for e in xs), Counter(e["antwortform"] for e in xs)
            z.append(f"| `{schl}` | `{lk}` | {pc['test']} | {pc['korrektur']} | {pc['sicherung']} | {sc[2]} / {sc[3]} | {ac['zahl']} / {ac['auswahl']} / {ac['luecken']} | "
                     + ", ".join(f"{k} {v}" for k, v in sorted(Counter(e['typ'] for e in xs).items())) + " | " + ", ".join(f"{k or 'ohne'} {v}" for k, v in sorted(Counter(e['form'] for e in xs).items(), key=lambda t: str(t[0]))) + " |")
    z.append(f"| Summe | {sum(len(v) for v in AUSWAHL.values())} Lernziele | {gesamt['pool']['test']} | {gesamt['pool']['korrektur']} | {gesamt['pool']['sicherung']} | {gesamt['stufe'][2]} / {gesamt['stufe'][3]} | "
             f"{gesamt['antwort']['zahl']} / {gesamt['antwort']['auswahl']} / {gesamt['antwort']['luecken']} | | |")
    gl = lambda c, namen: "\n".join(f"| {k} | {v} | {round(100 * v / len(A))} % |" for k, v in sorted(c.items(), key=lambda t: -t[1]))
    txt = open(vorlage, encoding="utf-8").read()
    txt = txt.replace("{{ZAHLEN}}", "\n".join(z)).replace("{{TYPEN}}", gl(gesamt["typ"], None)).replace("{{FORMEN}}", gl(gesamt["form"], None))
    txt = txt.replace("{{KENNUNGEN}}", "\n".join(f"| `{s}` | {aus[s][0]['kennung']} bis {aus[s][-1]['kennung']} | {len(aus[s])} |" for s in geladen))
    txt = txt.replace("{{FEHLBILDER}}", f"{n_fb}").replace("{{FB_RECHNUNG}}", f"{n_fb_rechnung}")
    open(os.path.join(HIER, "README.md"), "w", encoding="utf-8").write(txt)

# ═════════ vorrat_pruefen.py (Fehlbild-Rechnung in der Beschreibung) über Kopien mit typ = Formname ═════════
VPSKRIPT = r"""
import importlib.util, sys, glob, os
spec = importlib.util.spec_from_file_location("vp", sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.DATEIEN = sorted(glob.glob(os.path.join(sys.argv[2], "*.json")))
sys.argv = ["vp"]
sys.exit(m.main())
"""
with tempfile.TemporaryDirectory() as tmp:
    for schl in geladen:
        d = json.load(open(os.path.join(HIER, schl + ".json"), encoding="utf-8"))
        for e in d["aufgaben"]:
            e["typ"] = FORMNAME[e["form"]]
        json.dump(d, open(os.path.join(tmp, schl + ".json"), "w", encoding="utf-8"), ensure_ascii=False)
    r = subprocess.run([sys.executable, "-I", "-c", VPSKRIPT, os.path.join(WURZEL, "tools", "vorrat_pruefen.py"), tmp], capture_output=True, text=True, cwd=WURZEL)
print("tools/vorrat_pruefen.py über vtest-1b:")
print(r.stdout[-2000:] + r.stderr[-800:])
assert re.search(r"Aufgaben geprüft, 0 Meldungen", r.stdout), "tools/vorrat_pruefen.py meldet etwas"
print("OK")
