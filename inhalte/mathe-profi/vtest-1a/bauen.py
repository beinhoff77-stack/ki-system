"""Runde VT1A (Verstehen in Tests, Klasse 5): baut und prüft die neuen Test-, Korrektur- und Sicherungs-Aufgaben.

Aufruf: python3 -I inhalte/mathe-profi/vtest-1a/bauen.py     (muss mit „OK“ enden)
Lädt th_<Einheit>.py, prüft alle Regeln des Auftrags (vtest-auftrag-schreiber), schreibt <Einheit>.json und regeln-zuordnung.md.
Nur Inhalte; nichts wird eingespielt.
"""
import difflib
import glob
import hashlib
import json
import math
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from fractions import Fraction as F

sys.dont_write_bytecode = True
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import kern                      # noqa: E402
from kern import A, ip, WURZEL, POOLS   # noqa: E402

KUERZEL = "VT1A"
EINHEITEN = ["zahlen.potenzen_basis", "zahlen.rechengesetze"]
# gewählte Lernziele (Reihenfolge der Etappen); die Begründung steht in auswahl.md
GEWAEHLT = {
    "zahlen.potenzen_basis": ["schreibweise", "quadrat", "zehner", "sach"],
    "zahlen.rechengesetze": ["klammern", "termaufbau", "vorteil", "verteilen", "umkehraufgabe_mal", "ueberschlag", "sach"],
}
ABGRENZUNG = {
    "zahlen.potenzen_basis": {
        "schreibweise": "Die Übungen lassen Potenzen schreiben und lesen; hier muss das Kind aus Basis, Wert oder Hochzahl rückwärts schließen oder die Schreibweise begründen und an Fehlvorstellungen prüfen.",
        "quadrat": "Die Übungen rechnen Quadratzahlen aus; hier werden Quadrate gedeutet (Fläche, Quadratzahlen vergleichen, Gegenstück zu Verdoppeln) und Fehlvorstellungen wie „mal 2“ begründet entschieden.",
        "zehner": "Die Übungen lesen Zehnerpotenzen ab; hier geht es um die Bedeutung der Hochzahl als Zahl der Nullen und den Weg von großen Zahlen zurück zur Potenz.",
        "sach": "Die Übungen setzen eine Potenz in einer Sachaufgabe direkt ein; hier muss das Kind die Situation selbst als Potenz erkennen, rückwärts rechnen oder Rechenwege vergleichen.",
    },
    "zahlen.rechengesetze": {
        "klammern": "Die Übungen rechnen Terme mit Klammern aus; hier muss das Kind Klammern selbst setzen, Terme mit gleichen Zahlen vergleichen oder die Reihenfolge begründen.",
        "termaufbau": "Die Übungen ordnen Termen eine Art zu; hier muss das Kind Terme zu Geschichten, Rechnungen zu Texten und Texte zu Termen finden und die Struktur begründen.",
        "vorteil": "Die Übungen rechnen geschickt mit vorgegebenen Zahlen; hier muss das Kind das Tauschen und Zusammenfassen begründen, Fehler finden und fehlende Zahlen bestimmen.",
        "verteilen": "Die Übungen rechnen Aufgaben mit dem Verteilungsgesetz aus; hier wird das Gesetz an Flächen gedeutet, rückwärts angewendet und Fehler beim Ausklammern werden begründet.",
        "umkehraufgabe_mal": "Die Übungen lösen einfache Platzhalteraufgaben; hier muss das Kind mehrschrittige Umkehrungen finden, Gleichungen deuten und die Lösbarkeit begründen.",
        "ueberschlag": "Die Übungen runden und rechnen den Überschlag selbst; hier wird der Überschlag zur Kontrolle genutzt, bewertet und in seiner Genauigkeit untersucht.",
        "sach": "Die Übungen rechnen Sachaufgaben vorwärts; hier muss das Kind rückwärts rechnen, Gleichungen aufstellen und Rechenwege begründen.",
    },
}
VERBOTEN_LZ = {"negativ", "mal_ganz", "geteilt_ganz"}      # Rechnen mit negativen Zahlen: nicht Klasse 5
NAMEN_SUMMEN = {"8535e86c8118", "6a61eb7383e8", "ac818c81a10c", "96ae70b8d33e", "a26ac014d8b9", "4dd68e2ab3a3", "97bbc80c5a10", "68168224c472", "f7f376a1fcd0"}   # sha256-Anfänge; keine Namen im Klartext

RBL = json.load(open(os.path.join(WURZEL, "inhalte", "plan", "regelbezug-lernkarten.json"), encoding="utf-8"))
KENN = json.load(open(os.path.join(HIER, "..", "regeln-uebersicht", "kennungen.json"), encoding="utf-8"))["kennungen"]
REGELN = {e["kennung"]: e for e in KENN}

# ═════════ Themen-Dateien laden ═════════
for schl in EINHEITEN:
    pfad = os.path.join(HIER, "th_" + schl.replace(".", "_") + ".py")
    exec(compile(open(pfad, encoding="utf-8").read(), pfad, "exec"), {"__name__": "th", "neu": kern.neu, "Z": kern.Z, "W": kern.W})

# ═════════ Bestand ═════════
BESTAND = {}
for p in sorted(glob.glob(os.path.join(WURZEL, "inhalte", "themen", "*.json"))):
    d = json.load(open(p, encoding="utf-8"))
    BESTAND[d["thema_schluessel"]] = d
PFLICHT = {s: BESTAND[s]["inhalt"]["bewertung"]["lernziele_pflicht"] for s in EINHEITEN}

ZAHL = re.compile(r"[−-]?\d+(?:[  ]\d{3})*(?:[,.]\d+)?")
HOCH = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
HOCHLAUF = re.compile(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+")
maske = lambda t: re.sub(r"\s+", " ", ZAHL.sub("#", HOCHLAUF.sub("#", t))).strip()


def zahlen_im(t):
    t = HOCHLAUF.sub(lambda m: " " + m.group(0).translate(HOCH) + " ", t)
    r = set()
    for m in ZAHL.findall(t):
        r.add(F(re.sub(r"[  ]", "", m).replace("−", "").replace("-", "").replace(",", ".")))
    return r


def name_treffer(t):
    return {hashlib.sha256(w.lower().encode()).hexdigest()[:12] for w in re.findall(r"\w+", t)} & NAMEN_SUMMEN


def auswerten(zw):
    """zweite, unabhängige Rechnung: Funktion oder Zahl oder Python-Ausdruck"""
    if callable(zw):
        return F(str(zw()))
    if isinstance(zw, str):
        return F(str(eval(zw, {"__builtins__": {}}, {})))
    return F(str(zw))


# ═════════ Reihenfolge und Kennungen ═════════
reihe = {s: i for i, s in enumerate(EINHEITEN)}
A.sort(key=lambda a: (reihe[a["thema"]], GEWAEHLT[a["thema"]].index(a["lz"]), POOLS.index(a["pool"]), a["nr"]))

# ═════════ Anzahlen je Lernziel ═════════
for s in EINHEITEN:
    n_pflicht = len(PFLICHT[s])
    soll = -(-n_pflicht // 2)
    assert len(GEWAEHLT[s]) == soll, (s, "Hälfte der Pflicht-Lernziele (aufgerundet)", n_pflicht, soll)
    assert all(l in PFLICHT[s] for l in GEWAEHLT[s]) and not (set(GEWAEHLT[s]) & VERBOTEN_LZ), s
    for lz in GEWAEHLT[s]:
        xs = [a for a in A if a["thema"] == s and a["lz"] == lz]
        assert Counter(a["pool"] for a in xs) == {"test": 1, "korrektur": 3, "sicherung": 3}, (s, lz, Counter(a["pool"] for a in xs))
        assert {a["s"] for a in xs if a["pool"] == "korrektur"} == {2}, (s, lz, "Korrektur: Stufe 2")
        assert {a["s"] for a in xs if a["pool"] == "test"} <= {2, 3}, (s, lz)
        assert {a["s"] for a in xs if a["pool"] == "sicherung"} == {2, 3}, (s, lz, "Sicherung gemischt 2 und 3")
        ideen = Counter(a["idee"] for a in xs)
        assert len(ideen) >= 5 and max(ideen.values()) <= 2, (s, lz, "mindestens 5 verschiedene Ideen, keine öfter als 2-mal", dict(ideen))
assert len(A) == 77, len(A)
assert all(a["thema"] in EINHEITEN and a["lz"] in GEWAEHLT[a["thema"]] for a in A)

# ═════════ Bestand für die Doppelungsprüfung ═════════
BESTAND_TEXTE = {a["f"].get("text", "") for d in BESTAND.values() for a in d["aufgaben"]}
BESTAND_MASKEN = {maske(t) for t in BESTAND_TEXTE}
for p in glob.glob(os.path.join(WURZEL, "inhalte", "mathe-profi", "rollend-*", "*.json")):
    for e in json.load(open(p, encoding="utf-8")).get("aufgaben", []):
        if isinstance(e, dict) and "aufgabe" in e:
            t = e["aufgabe"]["f"].get("text", "")
            BESTAND_TEXTE.add(t)
            BESTAND_MASKEN.add(maske(t))
EIGENE = [a for s in EINHEITEN for a in BESTAND[s]["aufgaben"] if a["f"].get("text")]


def sollwert_von(q):
    if q["y"] == "zahl":
        return F(str(q["o"]["wert"]))
    return None


def aehnlich(q, b):
    """Grund der Ähnlichkeit zwischen Aufgabe q (neu) und Bestandsaufgabe b, sonst None"""
    t1, t2 = q["f"]["text"], b["f"].get("text", "")
    m1, m2 = maske(t1), maske(t2)
    sm = difflib.SequenceMatcher(None, m1, m2)
    if abs(len(m1) - len(m2)) < 40 and sm.real_quick_ratio() >= .7 and sm.quick_ratio() >= .7 and sm.ratio() >= .85:
        return "fast gleicher Wortlaut (ohne Zahlen)"
    n1, n2 = zahlen_im(t1), zahlen_im(t2)
    s1, s2 = sollwert_von(q), (F(str(b["o"]["wert"])) if b.get("y") == "zahl" and "wert" in b.get("o", {}) else None)
    if s1 is not None and s1 == s2 and len(n1) >= 2 and len(n1 & n2) / max(1, len(n1 | n2)) >= .75:
        return "gleiche Zahlen und gleicher Sollwert"
    return None


# ═════════ Prüfen und Bauen ═════════
aus = defaultdict(list)
alle_texte, alle_masken = set(), set()
n_fb = n_fb_rechnung = n_fb_bool = n_fb_hand = n_opt_geprueft = n_opt_hand = 0
treffer = []
FEHLER = []
REGEL_AUSSER_LISTE = set()
for zaehler, a in enumerate(A, 1):
    try:
        kenn = f"{KUERZEL}-{zaehler:03d}"
        q = dict(a["aufgabe"])
        alt = [b for b in BESTAND[a["thema"]]["aufgaben"] if b.get("p") == "test" and b.get("l") == a["lz"]]
        assert len(alt) == 1, (kenn, "alte Test-Aufgabe")
        q = dict(l=a["lz"], t=alt[0]["t"], p=a["pool"], s=a["s"], g=a["typ"], **q)
        assert a["s"] in (2, 3) and ip.STUFE_VON[a["typ"]] == a["s"], kenn
        assert a["typ"] not in ("direkt", "erkennen") and a["form"] != "lueckenweg", kenn
        assert q["y"] in ("zahl", "auswahl"), (kenn, "Antworttyp: nur Zahl oder Auswahl (kein Lückenweg)")
        assert "h" not in q and "tipp" not in q and "toleranz" not in q.get("o", {}), (kenn, "im Test keine Tipps, keine Toleranz")
        assert len(q["w"]) >= 60 and q["w"].count(".") >= 2, (kenn, "Lösungsweg vollständig")
        assert a["lehrplan"].startswith("M5 "), kenn
        assert a["regel"] is None or a["regel"] in REGELN, (kenn, a["regel"], "Regel nicht im Katalog")
        if a["regel"] and a["thema"] not in REGELN[a["regel"]]["themen"]:
            REGEL_AUSSER_LISTE.add((a["thema"], a["lz"], a["regel"]))
        text = q["f"]["text"]
        for t in [text, q["w"]] + list(q.get("a", [])):
            assert not name_treffer(t), (kenn, "Name")
            assert "?" not in t or t.count("?") <= 2, kenn
        assert text not in alle_texte and text not in BESTAND_TEXTE, (kenn, "Fragetext schon vorhanden")
        assert maske(text) not in alle_masken and maske(text) not in BESTAND_MASKEN, (kenn, "Fragetext nur mit anderen Zahlen schon vorhanden", text)
        alle_texte.add(text)
        alle_masken.add(maske(text))
        for b in EIGENE:
            g = aehnlich(q, b)
            if g:
                treffer.append((kenn, g, b["f"]["text"][:100]))
        if "grafik" in q["f"]:
            gf = q["f"]["grafik"]
            assert gf["typ"] == "tabelle" and all(len(z) == len(gf["kopf"]) and all(isinstance(x, str) for x in z) for z in gf["zeilen"]), kenn
        eintrag = dict(kennung=kenn, thema=a["thema"], lernkarte=a["lz"], pool=a["pool"], stufe=a["s"], typ=a["typ"], form=a["form"], antwortform=q["y"], zaehlt="ja",
                       lehrplan=a["lehrplan"], idee=a["idee"], abgrenzung=ABGRENZUNG[a["thema"]][a["lz"]], regel=a["regel"], regel_name=REGELN[a["regel"]]["name"] if a["regel"] else None, fehlbilder=[])
        if a["pool"] == "test":
            eintrag["ersetzt_test"] = True

        if q["y"] == "zahl":
            soll = ip.rechne(q["c"])
            assert soll == ip.zahlwert(q["o"]["wert"]) and soll.denominator == 1 and soll > 0, (kenn, "Rechnung 1", soll, q["o"]["wert"])
            eintrag["loesung_rechnung"] = q["c"]
            if re.search(r"\brunde|gerundet", text, re.I):
                eintrag["runden"] = 0
            assert auswerten(a["zweit"][0]) == soll, (kenn, "zweite Rechnung", auswerten(a["zweit"][0]), soll)
            if soll >= 10:
                assert soll not in zahlen_im(text), (kenn, "Ergebnis steht schon im Text")
            assert a["fb"] and len(a["fb"]) >= 2, (kenn, "mindestens zwei Fehlbilder")
            werte = set()
            for w, beschr, rech in a["fb"]:
                assert w != q["o"]["wert"] and w not in werte, (kenn, w)
                werte.add(w)
                assert len(beschr) > 12, (kenn, w, "Beschreibung")
                assert isinstance(rech, str), (kenn, w, "Fehlbild braucht eine Rechnung")
                if True:
                    assert ip.rechne(rech) == ip.zahlwert(w), (kenn, "Fehlbild: Rechnung", rech, "ergibt", ip.rechne(rech), "nicht", w)
                    n_fb_rechnung += 1
                    # Zahlen der Beschreibung müssen aus der Aufgabe oder aus der Rechnung stammen
                    erlaubt = zahlen_im(text) | zahlen_im(rech) | {F(w), F(0), F(1), F(2)}
                    import ast
                    for kn in ast.walk(ast.parse(rech, mode="eval")):
                        if isinstance(kn, (ast.BinOp, ast.UnaryOp)):
                            try:
                                erlaubt.add(ip.rechne(ast.unparse(kn)))
                            except Exception:
                                pass
                    fremd = {x for x in zahlen_im(beschr) if x not in erlaubt}
                    assert not fremd, (kenn, w, "Zahl in der Beschreibung ohne Rechnung", sorted(fremd), beschr)
                n_fb += 1
                eintrag["fehlbilder"].append(dict(antwort=w, rechnung=rech, fehlbild=None, regel_des_fehlbilds=None, beschreibung=beschr))
        else:
            opts = q["a"]
            assert len(opts) >= 4 and len(set(opts)) == len(opts), (kenn, "mindestens 4 verschiedene Optionen")
            assert a["zweit"] is True, (kenn, "Probe der richtigen Antwort")
            assert set(a["fb"]) == set(range(len(opts))) - {q["o"]["index"]}, kenn
            for i, (beschr, pruef) in sorted(a["fb"].items()):
                assert len(beschr) > 12, (kenn, i)
                assert pruef is True or pruef is None, (kenn, i, "Prüfung der falschen Option ergibt nicht True", beschr)
                if pruef:
                    n_opt_geprueft += 1
                else:
                    n_opt_hand += 1
                n_fb += 1
                eintrag["fehlbilder"].append(dict(index=i, antwort=opts[i], fehlbild=None, regel_des_fehlbilds=None, beschreibung=beschr))
            assert a["form"] != "fehler_detektiv" and a["typ"] != "fehler", kenn
            if any(o.startswith(("Fehler:", "Kein Fehler:")) for o in opts):
                # vollständige Aussagen „Fehler ist … Richtig wäre …“ (oder: kein Fehler), keine Zeilenwahl
                assert all(o.startswith(("Fehler:", "Kein Fehler:")) for o in opts), (kenn, "Fehler-Aufgabe: vollständige Aussagen")
                ro = opts[q["o"]["index"]]
                assert ro.startswith("Kein Fehler:") or "Richtig wäre" in ro, (kenn, "richtige Option: Kein Fehler oder Fehler mit Richtig wäre")
        q["_kennung"] = kenn
        eintrag["aufgabe"] = q
        del q["_kennung"]
        aus[a["thema"]].append(eintrag)
    except AssertionError as e:
        import traceback
        FEHLER.append(e.args or (kenn, traceback.format_exc().splitlines()[-3].strip()))

assert not FEHLER, FEHLER
assert not treffer, ("Ähnlichkeit zu Bestandsaufgaben der Einheiten", treffer)

# ═════════ Ähnlichkeit innerhalb eines Lernziels ═════════
for s in EINHEITEN:
    for lz in GEWAEHLT[s]:
        xs = [e for e in aus[s] if e["lernkarte"] == lz]
        for i in range(len(xs)):
            for j in range(i + 1, len(xs)):
                r = difflib.SequenceMatcher(None, maske(xs[i]["aufgabe"]["f"]["text"]), maske(xs[j]["aufgabe"]["f"]["text"])).ratio()
                assert r < .7, (xs[i]["kennung"], xs[j]["kennung"], "zu ähnlich innerhalb des Lernziels", round(r, 2))
        sa = Counter(str(e["aufgabe"]["o"]["wert"] if e["antwortform"] == "zahl" else e["aufgabe"]["a"][e["aufgabe"]["o"]["index"]]) for e in xs)
        if max(sa.values()) > 1:
            print("Hinweis: gleiche Sollantwort im Lernziel", s, lz, {k: v for k, v in sa.items() if v > 1})

MUSTER = {p: [0, 0] for p in ("Kein Fehler", "Nur ", "Keiner", "Beide")}
# ═════════ Lage der richtigen Antwort, Länge, Anfangswörter, Statistik ═════════
AUSW = [e for l in aus.values() for e in l if e["antwortform"] == "auswahl"]
lagen = defaultdict(list)
for e in AUSW:
    lagen[len(e["aufgabe"]["a"])].append(e["aufgabe"]["o"]["index"])
for k, v in lagen.items():
    c = Counter(v)
    assert max(c.values()) - min(c.get(i, 0) for i in range(k)) <= 2, ("Lage der richtigen Antwort nicht gleichmäßig", k, dict(c))
laenger = [e["kennung"] for e in AUSW if len(e["aufgabe"]["a"][e["aufgabe"]["o"]["index"]]) > max(len(o) for i, o in enumerate(e["aufgabe"]["a"]) if i != e["aufgabe"]["o"]["index"])]
if os.environ.get("VT_TAB"):
    for e in AUSW:
        a_ = e["aufgabe"]["a"]; r_ = e["aufgabe"]["o"]["index"]
        print(e["kennung"], e["pool"][:4], "r=%d" % r_, [len(o) for o in a_], "LANGEST" if e["kennung"] in laenger else "")
        if os.environ.get("VT_TAB") == "2" and e["kennung"] in laenger:
            for i_, o_ in enumerate(a_): print("   ", "*" if i_ == r_ else " ", o_)
assert len(laenger) <= .35 * len(AUSW), ("richtige Option zu oft die längste", len(laenger), len(AUSW))
kurz = [e["kennung"] for e in AUSW if len(e["aufgabe"]["a"][e["aufgabe"]["o"]["index"]]) < min(len(o) for i, o in enumerate(e["aufgabe"]["a"]) if i != e["aufgabe"]["o"]["index"])]
assert len(kurz) <= .35 * len(AUSW), ("richtige Option zu oft die kürzeste", len(kurz), len(AUSW))
def _w(o):
    return o.split(":")[0] if o.split(" ")[0] in ("Kein", "Nur", "Beide", "Keiner", "Fehler:") or o.startswith("Fehler:") else "-"
for e in AUSW:
    a_ = e["aufgabe"]["a"]; ri = e["aufgabe"]["o"]["index"]
    for pre in ("Kein Fehler", "Nur ", "Keiner", "Beide"):
        n_alle = sum(1 for o in a_ if o.startswith(pre)); n_ri = int(a_[ri].startswith(pre))
        if n_alle:
            MUSTER[pre][0] += n_alle; MUSTER[pre][1] += n_ri
for pre, (n_alle, n_ri) in MUSTER.items():
    assert n_alle == 0 or n_ri / n_alle >= .2, ("Option mit Anfangswort „%s“ fast nie richtig (Ausschlussmuster)" % pre, n_ri, n_alle)
nz = [e for l in aus.values() for e in l if e["antwortform"] == "zahl"]
tp = [e for l in aus.values() for e in l if e["pool"] == "test"]
print("Statistik: Auswahl %d, Zahl %d, Lücken %d (gesamt %d); Test-Pool: Auswahl %d von %d" % (len(AUSW), len(nz), sum(1 for l in aus.values() for e in l if e["antwortform"] == "luecken"), len(AUSW) + len(nz), sum(1 for e in tp if e["antwortform"] == "auswahl"), len(tp)))
print("Länge: richtige Option die längste in %d von %d (%.0f %%), die kürzeste in %d" % (len(laenger), len(AUSW), 100 * len(laenger) / len(AUSW), len(kurz)))
print("Lage der richtigen Antwort:", {k: dict(sorted(Counter(v).items())) for k, v in lagen.items()})
print("Anfangswörter (alle, davon richtig):", {k: tuple(v) for k, v in MUSTER.items()})

# ═════════ Schreiben ═════════
KURZ = {"zahlen.potenzen_basis": "Klasse 5, Potenzen als Schreibweise", "zahlen.rechengesetze": "Klasse 5, Grundrechenarten und Rechengesetze"}
for s in EINHEITEN:
    json.dump({"stand": "2026-11-28", "runde": "vtest-1a", "kuerzel": KUERZEL, "flug": "vt1a-" + s, "titel": s, "fuer": "Klasse 5", "klasse": 5, "themen": [s], "themen_datei_im_bestand": s,
               "hinweis": "Verstehens-Aufgaben für Tests (Pools test, korrektur, sicherung), Auftrag „Verstehen in Tests“. Nicht eingespielt. Je Eintrag: thema, lernkarte, pool, stufe, typ (Aufgabentyp g), form (optional), "
                          "zaehlt, lehrplan, ersetzt_test (nur Pool test), Fehlbilder und unter „aufgabe“ die Aufgabe im Format von inhalte/README.md (ohne Tipp).",
               "aufgaben": aus[s]}, open(os.path.join(HIER, f"{s}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

ZEILEN = []
for s in EINHEITEN:
    for e, a in zip(aus[s], [x for x in A if x["thema"] == s]):
        ZEILEN.append((e["kennung"], e["thema"], e["lernkarte"], e["regel"], a["zweifel"] or "", a["ohne"] or ""))
with open(os.path.join(HIER, "regeln-zuordnung.md"), "w", encoding="utf-8") as f:
    f.write("# Runde VT1A: Regel-Kennung je Aufgabe\n\nMaßstab: die Regel, die das Kind zum Lösen am stärksten braucht (tragender Lösungsschritt). Kennungen aus `inhalte/mathe-profi/regeln-uebersicht/kennungen.json`; `bauen.py` prüft, dass die Kennung im Katalog steht; `tools/vtest_pruefen.py` vergleicht mit der Regel der Lernkarte (`inhalte/plan/regelbezug-lernkarten.json`). Alle Aufgaben tragen die Regel ihrer Lernkarte (auch dort, wo die Aufgabe daneben noch andere Regeln braucht). Die Fehlbild-Kennungen des Katalogs (`fb.*`) sind nicht vergeben (die Fehlbilder stehen als Beschreibung mit Rechnung in den JSON-Dateien).\n\n")
    f.write(f"**{sum(1 for z in ZEILEN if z[3])} Aufgaben mit Regel, {sum(1 for z in ZEILEN if not z[3])} ohne.**\n\n## Verteilung\n\n| Regel | Name | Aufgaben |\n|---|---|---|\n")
    for r_, n_ in sorted(Counter(z[3] for z in ZEILEN).items(), key=lambda x: (x[0] is None, -x[1], str(x[0]))):
        f.write(f"| {'`' + r_ + '`' if r_ else '– (ohne Regel)'} | {REGELN[r_]['name'] if r_ else ''} | {n_} |\n")
    f.write("\n## Hinweis zur Themenliste des Katalogs\n\nDiese Regeln der Lernkarten stehen im Katalog nicht mit der Einheit in der Themenliste: " + "; ".join(f"`{r_}` ({t_}.{l_})" for t_, l_, r_ in sorted(REGEL_AUSSER_LISTE)) + ". Sie wurden trotzdem vergeben, weil die Lernkarte sie so führt (Vorgabe der Prüfung); die Themenliste des Katalogs könnte um `zahlen.rechengesetze` ergänzt werden.\n")
    f.write("\n## Aufgaben ohne Regel (mit Begründung)\n\n| Aufgabe | Einheit.Lernziel | Begründung |\n|---|---|---|\n")
    for z in ZEILEN:
        if not z[3]:
            f.write(f"| {z[0]} | {z[1]}.{z[2]} | {z[5]} |\n")
    f.write("\n## Zweifelsfälle\n\n| Aufgabe | Einheit.Lernziel | gewählt | Bemerkung |\n|---|---|---|---|\n")
    for z in ZEILEN:
        if z[4]:
            f.write(f"| {z[0]} | {z[1]}.{z[2]} | {'`' + z[3] + '`' if z[3] else '–'} | {z[4]} |\n")
    f.write("\n## Alle Aufgaben\n\n| Aufgabe | Einheit.Lernziel | Regel |\n|---|---|---|\n")
    for z in ZEILEN:
        f.write(f"| {z[0]} | {z[1]}.{z[2]} | {'`' + z[3] + '`' if z[3] else '–'} |\n")

# ═════════ Zählen ═════════
alle = [e for s in EINHEITEN for e in aus[s]]
print("Einheit · Lernziele · Aufgaben:")
for s in EINHEITEN:
    print(f"  {s}: {len(GEWAEHLT[s])} von {len(PFLICHT[s])} Lernzielen, {len(aus[s])} Aufgaben")
print("Pool:", dict(Counter(e["pool"] for e in alle)))
print("Stufe:", dict(sorted(Counter(e["stufe"] for e in alle).items())), "| je Pool:", {p: dict(sorted(Counter(e["stufe"] for e in alle if e["pool"] == p).items())) for p in POOLS})
print("Typ:", dict(Counter(e["typ"] for e in alle).most_common()))
print("Form:", dict(Counter(e["form"] or "ohne" for e in alle).most_common()))
print("Antwortform:", dict(Counter(e["antwortform"] for e in alle)))
print(f"{n_fb} Fehlbilder/falsche Optionen: {n_fb_rechnung} Zahl-Fehlbilder als Rechnung nachgerechnet, {n_fb_bool} Zahl-Fehlbilder mit geprüfter Aussage, {n_opt_geprueft} falsche Optionen mit geprüfter Aussage, {n_opt_hand} nur von Hand")
print("Lage der richtigen Antwort:", {k: dict(sorted(Counter(v).items())) for k, v in lagen.items()})

# ═════════ tools/vorrat_pruefen.py über die eigenen Dateien ═════════
VPSKRIPT = r"""
import importlib.util, sys, glob, os
spec = importlib.util.spec_from_file_location("vp", sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.DATEIEN = sorted(glob.glob(os.path.join(sys.argv[2], "*.json")))
sys.argv = ["vp"]
sys.exit(m.main())
"""
r = subprocess.run([sys.executable, "-I", "-c", VPSKRIPT, os.path.join(WURZEL, "tools", "vorrat_pruefen.py"), HIER], capture_output=True, text=True, cwd=WURZEL)
print("tools/vorrat_pruefen.py über vtest-1a:")
print(r.stdout[-2500:] + r.stderr[-800:])
assert re.search(r"77 Aufgaben geprüft, 0 Meldungen", r.stdout), "tools/vorrat_pruefen.py meldet etwas"
r2 = subprocess.run([sys.executable, "-I", os.path.join(WURZEL, "tools", "vtest_pruefen.py"), "--runde", "1a"], capture_output=True, text=True, cwd=WURZEL)
print(r2.stdout[-6000:] + r2.stderr[-800:])
assert r2.returncode == 0 and "FEHLER" not in r2.stdout.replace("0 FEHLER", ""), "tools/vtest_pruefen.py meldet FEHLER"
print("OK")
