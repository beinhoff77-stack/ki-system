"""Mathe-Profi, Auftrag „Vorrat neue Formen“ (Helfer Aufgaben), Runde rollend-7, Kürzel K8, Zielgruppe Klasse 8.

Aufruf: python3 -I inhalte/mathe-profi/rollend-7/bauen.py     (muss mit „OK“ enden)
Lädt th_<Thema>.py (je Thema eine Datei mit den Aufgaben), prüft alles, schreibt je Thema <Thema>.json.
Nur Inhalte. Nichts wird eingespielt.
"""
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
from kern import A, FORM, ip, WURZEL, z2   # noqa: E402

KENN = json.load(open(os.path.join(HIER, "..", "regeln-uebersicht", "kennungen.json"), encoding="utf-8"))["kennungen"]
REGELN = {e["kennung"]: e for e in KENN}
FEHLBILD = {f["kennung"]: e["kennung"] for e in KENN for f in e["fehlbilder"]}

# Datei-Schlüssel (so heißt auch die Einheit) -> (Themen-Datei im Bestand, Lernkarten in der Reihenfolge des Auftrags)
THEMEN = {
    "terme.umformen": ("terme.umformen", ["zusammenfassen", "produkte", "minusklammer", "ausmultiplizieren", "aequivalenz"]),
    "terme.umformen_teil2": ("terme.umformen", ["summe_mal_summe", "ausklammern", "binomisch", "gleichungen_binomisch"]),
    "gleichungen.linear": ("gleichungen.linear", ["waage", "beide_seiten", "klammern", "probe", "sonderfaelle", "sach"]),
    "terme.bruchterme": ("terme.bruchterme", ["definitionsmenge", "termwert", "kuerzen", "erweitern", "addieren", "multiplizieren", "fehler_finden"]),
    "gleichungen.bruch": ("gleichungen.bruch", ["definitionsmenge", "ein_bruch", "ueber_kreuz", "hauptnenner", "scheinloesung", "verhaeltnis", "graphisch"]),
    "terme.quadratische_extreme": ("terme.quadratische_extreme", ["ergaenzen", "scheitelform", "extremwert", "mit_faktor", "optimierung"]),
    "terme.potenzgesetze_natuerlich": ("terme.potenzgesetze_natuerlich", ["mal_gleiche_basis", "gleicher_exponent", "potenz_von_potenz", "geteilt_gleiche_basis", "anwenden"]),
    "terme.potenzgesetze_ganzzahlig": ("terme.potenzgesetze_ganzzahlig", ["warum_gilt", "gleiche_basis_ganz", "exponent_und_potenz", "terme_vereinfachen", "fehler_ganz"]),
    "stochastik.grundbegriffe": ("stochastik.grundbegriffe", ["begriffe", "rel_haeufigkeit", "darstellen"]),
    "messen.prisma_zylinder": ("messen.prisma_zylinder", ["prisma_volumen", "prisma_oberflaeche", "prisma_umstellen", "zylinder_volumen", "zylinder_oberflaeche", "sach", "verstehen"]),
    "groessen.indirekt": ("groessen.indirekt", ["erkennen", "vervielfachen", "produkt", "dreisatz", "graph", "unterscheiden", "sach"]),
}
KUERZEL = "K8"
GEPRUEFT = ("umkehren", "zwei_wege", "bruecke", "anwenden")
ZAEHLT_JA_AUS = ("umkehren", "zwei_wege", "bruecke", "verfahren_waehlen", "anwenden")

geladen = []
for schl in THEMEN:
    pfad = os.path.join(HIER, "th_" + schl.replace(".", "_") + ".py")
    if os.path.exists(pfad):
        # die Themen-Dateien rufen kern.neu auf; der Schlüssel steckt in jedem Aufruf
        exec(compile(open(pfad, encoding="utf-8").read(), pfad, "exec"), {"__name__": "th", **{k: getattr(kern, k) for k in dir(kern) if not k.startswith("_")}})
        geladen.append(schl)
assert geladen, "keine Themen-Dateien"

ZAHL = re.compile(r"[−-]?\d+(?:[  ]\d{3})*(?:[,.]\d+)?")
bau_ohne_zahl = lambda t: re.sub(r"\s+", " ", ZAHL.sub("#", t)).strip()
KOMMA_LUECKE = re.compile(r"\d\s*,\s*[①②③④⑤□]")
KOMMA_NEBEN = re.compile(r"[①②③④⑤□],|,[①②③④⑤□]")
ZWEIDEUTIG = re.compile(r"\d/\d+[a-zA-Z]|/\([^()]*\(|\)\)/")


def zahlen_im(text):
    r = set()
    for m in ZAHL.findall(text):
        s = re.sub(r"[  ]", "", m).replace("−", "").replace("-", "").replace(",", ".")
        r.add(F(s))
    return r


def texte_von(q):
    return [q["f"]["text"], q["h"], q["w"]] + list(q.get("a", [])) + [q["f"].get("hinweis", "")]


def grafik_ok(g):
    if g["typ"] == "tabelle":
        return all(len(z) == len(g["kopf"]) and all(isinstance(x, str) for x in z) for z in g["zeilen"]) and all(isinstance(x, str) for x in g["kopf"])
    if g["typ"] == "koordinaten":
        return len(g["x"]) == len(g["y"]) == 2 and set(g) <= {"typ", "x", "y", "graphen", "kreise", "punkte", "schritt_x", "schritt_y", "name_x", "name_y"}
    if g["typ"] in ("saeulen", "kreisdiagramm"):
        return all(set(w) == {"name", "wert"} and len(w["name"]) <= 8 for w in g["werte"]) and (g["typ"] == "saeulen" or sum(w["wert"] for w in g["werte"]) == 100)
    return False


# ═════════ Bestand laden ═════════
BESTAND = {}
KARTE = {}
for schl, (datei, lk) in THEMEN.items():
    if datei not in BESTAND:
        BESTAND[datei] = json.load(open(os.path.join(WURZEL, "inhalte", "themen", datei + ".json"), encoding="utf-8"))
for datei, d in BESTAND.items():
    for a in d["aufgaben"]:
        KARTE.setdefault((datei, a["l"]), a["t"])
BESTAND_TEXT = {dat: {a["f"].get("text", "") for a in d["aufgaben"]} for dat, d in BESTAND.items()}
BESTAND_BAU = {dat: {bau_ohne_zahl(a["f"].get("text", "")) for a in d["aufgaben"]} for dat, d in BESTAND.items()}

# ═════════ Prüfen ═════════
reihe = {schl: i for i, schl in enumerate(THEMEN)}
A.sort(key=lambda a: (reihe[a["thema"]], THEMEN[a["thema"]][1].index(a["lk"]), a["s"]))
aus = defaultdict(list)
n_rechnung = n_fb = n_grafik = 0
alle_texte, alle_bau = set(), defaultdict(set)
zaehler = 0
for a in A:
    assert a["thema"] in geladen and a["lk"] in THEMEN[a["thema"]][1], (a["thema"], a["lk"])
    datei = THEMEN[a["thema"]][0]
    q = a["aufgabe"]
    zaehler += 1
    kenn = f"{KUERZEL}-V{zaehler:03d}"
    assert a["regel"] in REGELN, (kenn, a["regel"])
    assert ip.STUFE_VON[a["g"]] == a["s"], kenn
    assert (datei, a["lk"]) in KARTE, (kenn, a["lk"])
    q.update({"l": a["lk"], "t": KARTE[(datei, a["lk"])], "p": "uebung", "s": a["s"], "g": a["g"]})
    q = dict(l=q.pop("l"), t=q.pop("t"), p=q.pop("p"), s=q.pop("s"), g=q.pop("g"), **q)
    a["aufgabe"] = q
    assert q["y"] in ("zahl", "auswahl", "luecken"), kenn
    assert a["form"] != "lueckenweg" or q["y"] == "luecken", (kenn, "Lückenweg nur mit Lücken")
    assert a["form"] != "lueckenweg" or a["s"] == 1, (kenn, "Lückenweg gehört auf Stufe 1")
    assert a["form"] != "fehler_detektiv" or a["s"] == 3, (kenn, "Fehler-Detektiv gehört auf Stufe 3")
    assert a["zaehlt"] == ("nein" if a["form"] == "lueckenweg" else "ja"), kenn
    assert q["h"].strip() and len(q["w"]) >= 15, kenn
    text = q["f"]["text"]
    for t in texte_von(q):
        assert not ZWEIDEUTIG.search(t), (kenn, "Bruch nicht eindeutig", t)
        assert not {"Leo", "Rosa", "Leopold"} & set(re.findall(r"\w+", t)), (kenn, "Name")
    assert text not in alle_texte and text not in BESTAND_TEXT[datei], (kenn, "Fragetext schon vorhanden")
    b = bau_ohne_zahl(text)
    assert b not in alle_bau[datei] and b not in BESTAND_BAU[datei], (kenn, "Fragetext nur mit anderen Zahlen schon vorhanden", b)
    if "grafik" in q["f"]:
        assert grafik_ok(q["f"]["grafik"]), (kenn, "grafik")
        n_grafik += 1
    alle_texte.add(text)
    alle_bau[datei].add(b)
    eintrag = dict(kennung=kenn, thema=a["thema"], lernkarte=a["lk"], stufe=a["s"], typ=FORM[a["form"]][0], form=a["form"], antwortform=q["y"],
                   regel=a["regel"], regel_name=REGELN[a["regel"]]["name"], zaehlt=a["zaehlt"], fehlbilder=[])

    def fb_eintrag(ort, antwort, fbk, beschr):
        global n_fb
        assert fbk is None or fbk in FEHLBILD, (kenn, fbk)
        assert beschr and len(beschr) > 5, (kenn, "Beschreibung des Fehlbilds")
        n_fb += 1
        eintrag["fehlbilder"].append(dict(**ort, antwort=antwort, fehlbild=fbk, regel_des_fehlbilds=FEHLBILD.get(fbk), beschreibung=beschr))

    if q["y"] == "zahl":
        soll = ip.rechne(q["c"])
        assert soll == ip.zahlwert(q["o"]["wert"]), (kenn, soll, q["o"]["wert"])
        zw = a["zweit"][0]
        zwv = z2(zw) if isinstance(zw, str) else zw
        tol = q["o"].get("toleranz")
        if tol is None:
            assert F(zwv) == soll, (kenn, "zweite Rechnung", zwv, soll)
        else:
            assert abs(float(zwv) - float(q["o"]["wert"])) <= tol, (kenn, "zweite Rechnung mit Toleranz", zwv)
        n_rechnung += 1
        if abs(soll) >= 10 and tol is None:
            assert abs(soll) not in zahlen_im(text), (kenn, "Ergebnis steht schon im Text")
            assert abs(soll) not in zahlen_im(q["h"]), (kenn, "Tipp verrät das Ergebnis")
        assert a["fb"], (kenn, "mindestens ein Fehlbild")
        werte = set()
        for w, fbk, beschr in a["fb"]:
            assert w != q["o"]["wert"] and w not in werte, (kenn, w)
            werte.add(w)
            fb_eintrag({}, w, fbk, beschr)
    elif q["y"] == "luecken":
        assert not KOMMA_LUECKE.search(text + " " + q["f"]["schablone"]), (kenn, "Lücke hinter dem Komma")
        assert not KOMMA_NEBEN.search(text + " " + q["f"]["schablone"]), (kenn, "Komma direkt neben einer Lücke")
        soll = [ip.rechne(c) for c in q["c"]]
        assert soll == q["o"]["werte"] == [z2(z) if isinstance(z, str) else F(z) for z in a["zweit"]], (kenn, soll, a["zweit"])
        assert all(isinstance(w, int) for w in q["o"]["werte"]) and q["f"]["schablone"].count("□") == len(soll), kenn
        im_text = zahlen_im(text + " " + q["f"]["schablone"] + " " + q["f"].get("hinweis", ""))
        im_tipp = zahlen_im(q["h"])
        for v in soll:
            assert abs(v) not in im_text, (kenn, v, "Lückenwert steht schon in Text, Schablone oder Hinweis")
            assert abs(v) not in im_tipp, (kenn, v, "Tipp verrät den Lückenwert")
        if a["form"] == "lueckenweg":
            assert len(soll) >= 2 and q["y"] == "luecken", (kenn, "Lückenweg: mindestens zwei Lücken")
            assert len(set(soll)) == len(soll), (kenn, "Lückenwerte sollen verschieden sein")
        n_rechnung += len(soll)
        for i, liste in sorted(a["fb"].items()):
            werte = set()
            for w, fbk, beschr in liste:
                assert w != soll[i] and w not in werte, (kenn, i, w)
                werte.add(w)
                fb_eintrag({"luecke": i + 1}, w, fbk, beschr)
    else:
        assert a["zweit"]() is True and len(set(q["a"])) == len(q["a"]) >= 3, kenn
        assert set(a["fb"]) == set(range(len(q["a"]))) - {q["o"]["index"]}, kenn
        n_rechnung += 1
        for i, (fbk, beschr) in sorted(a["fb"].items()):
            fb_eintrag({"index": i}, q["a"][i], fbk, beschr)
    eintrag["aufgabe"] = q
    aus[a["thema"]].append(eintrag)

# ═════════ Mischung je Lernkarte und je Thema ═════════
mix = []
for schl in geladen:
    for lk in THEMEN[schl][1]:
        xs = [e for e in aus[schl] if e["lernkarte"] == lk]
        formen = Counter(e["form"] for e in xs)
        assert len(xs) == 3, (schl, lk, "genau drei Aufgaben", len(xs))
        assert formen["lueckenweg"] <= 1, (schl, lk, "höchstens ein Lückenweg")
        assert formen["fehler_detektiv"] <= 1, (schl, lk, "höchstens ein Fehler-Detektiv")
        assert any(e["zaehlt"] == "ja" and e["form"] in ZAEHLT_JA_AUS for e in xs), (schl, lk, "mindestens eine Aufgabe mit zaehlt ja aus umkehren/zwei_wege/bruecke/verfahren_waehlen/anwenden")
        mix.append((schl, lk, formen))
AUSNAHME = {}     # (Thema, Form): Begründung, wenn die Form fachlich nicht zweimal passt
for schl in geladen:
    c = Counter(e["form"] for e in aus[schl])
    for f in GEPRUEFT:
        assert c[f] >= 2 or (schl, f) in AUSNAHME, (schl, f, "weniger als zweimal", c[f])

lagen = defaultdict(list)
for a in A:
    if a["aufgabe"]["y"] == "auswahl" and a["form"] != "fehler_detektiv":
        lagen[len(a["aufgabe"]["a"])].append(a["aufgabe"]["o"]["index"])
if len(geladen) == len(THEMEN):
    assert set(lagen[4]) == {0, 1, 2, 3} and set(lagen[3]) == {0, 1, 2}, lagen


def lauf(pfad):
    r = subprocess.run([sys.executable, "-I", os.path.join(WURZEL, "tools", "inhalt_pruefen.py"), pfad], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


print("Thema (Datei)                       neu  inhalt_pruefen vorher → nachher")
with tempfile.TemporaryDirectory() as tmp:
    for datei in dict.fromkeys(THEMEN[s][0] for s in geladen):
        liste = [e["aufgabe"] for s in geladen if THEMEN[s][0] == datei for e in aus[s]]
        quelle = os.path.join(WURZEL, "inhalte", "themen", f"{datei}.json")
        d = json.load(open(quelle, encoding="utf-8"))
        assert all(q["l"] in {e["lernziel"] for e in d["inhalt"]["etappen"]} and q["t"] in {t["k"] for t in d["inhalt"]["teilfaehigkeiten"]} for q in liste), datei
        code0, aus0 = lauf(quelle)
        d["aufgaben"] = d["aufgaben"] + liste
        ziel = os.path.join(tmp, f"{datei}.json")
        json.dump(d, open(ziel, "w", encoding="utf-8"), ensure_ascii=False)
        code1, aus1 = lauf(ziel)
        print(f"{datei:35} {len(liste):3}  Code {code0} → {code1}")
        if code1 != 0:
            print(aus1[-2500:])
        assert code0 == 0 and code1 == 0, datei

# ═════════ Schreiben und Zählen ═════════
gesamt_f, gesamt_z = Counter(), Counter()
print()
print("Thema                          Lernkarten  Aufgaben  Formen (lw/fd/vw/zw/um/br/an)  zaehlt ja/nein")
KURZ = {"lueckenweg": "lw", "fehler_detektiv": "fd", "verfahren_waehlen": "vw", "zwei_wege": "zw", "umkehren": "um", "bruecke": "br", "anwenden": "an"}
for schl in geladen:
    datei, lks = THEMEN[schl]
    liste = aus[schl]
    c = Counter(e["form"] for e in liste)
    z = Counter(e["zaehlt"] for e in liste)
    gesamt_f.update(c)
    gesamt_z.update(z)
    json.dump({"stand": "2026-11-27", "runde": "rollend-7", "kuerzel": KUERZEL, "flug": "k8-" + schl, "titel": schl, "fuer": "Klasse 8", "klasse": 8,
               "themen": [schl], "themen_datei_im_bestand": datei,
               "hinweis": "Aufgaben auf Vorrat in neuer Form (Feld form: " + ", ".join(FORM) + "), Auftrag Vorrat neue Formen. Nicht eingespielt. Je Eintrag: thema (Einheit), lernkarte, "
                          "typ (Name wie in tools/rollend_sql.py), form, zaehlt (ja/nein), Regel-Kennung, Fehlbilder und unter „aufgabe“ die Aufgabe im Format von inhalte/README.md.",
               "aufgaben": liste}, open(os.path.join(HIER, f"{schl}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{schl:30} {len(lks):10} {len(liste):9}  " + "/".join(str(c[f]) for f in FORM and KURZ) + f"   {z['ja']}/{z['nein']}")
print()
print("Summe Lernkarten", sum(len(THEMEN[s][1]) for s in geladen), "Aufgaben", len(A), "| Formen", dict(gesamt_f), "| zaehlt", dict(gesamt_z))
print(f"{n_rechnung} Lösungen zweifach nachgerechnet; {n_fb} Fehlbilder, davon {sum(1 for fl in aus.values() for e in fl for x in e['fehlbilder'] if x['fehlbild'])} mit Kennung; {n_grafik} Aufgaben mit Zeichnung")
fd = [(e["kennung"], e["aufgabe"]["o"]["index"] + 1, len(e["aufgabe"]["a"])) for l in aus.values() for e in l if e["form"] == "fehler_detektiv"]
verteilung = Counter(z for _, z, _ in fd)
assert all("In welcher Zeile passiert der erste Fehler?" in e["aufgabe"]["f"]["text"] or "Welche Zeile ist falsch?" in e["aufgabe"]["f"]["text"] for l in aus.values() for e in l if e["form"] == "fehler_detektiv")
print("Fehler-Detektiv: Fehlerzeile je Zeile", dict(sorted(verteilung.items())), "von", len(fd))
if fd:
    assert max(verteilung.values()) <= len(fd) // 3 + 1, "Fehlerzeile zu einseitig verteilt"
print("Themen geladen:", ", ".join(geladen))
print("OK")
