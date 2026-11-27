"""Mathe-Profi, Auftrag „Stufe 3“ (Helfer Aufgaben), Runde rollend-11, Kürzel S3.

Aufruf: python3 -I inhalte/mathe-profi/rollend-11/bauen.py [Thema ...]    (muss mit „OK“ enden)
Für jede Lernkarte aus rollend-5 (Klasse 5) und rollend-7 (Klasse 8) ohne zählende Aufgabe auf Stufe 3: GENAU EINE neue Aufgabe
(Fehler-Detektiv, Umkehren, Zwei Wege, Brücke oder Anwenden als Transfer), zaehlt = ja, Stufe 3. Schreibt je Thema <Thema>.json.
Die Aufgaben stehen in th_*.py (Bausteine in kern.py). Nur Inhalte, nichts wird eingespielt.
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
import kern                                   # noqa: E402
from kern import A, FORM, ip, WURZEL          # noqa: E402

KENN = json.load(open(os.path.join(HIER, "..", "regeln-uebersicht", "kennungen.json"), encoding="utf-8"))["kennungen"]
REGELN = {e["kennung"]: e for e in KENN}
FEHLBILD = {f["kennung"]: e["kennung"] for e in KENN for f in e["fehlbilder"]}
PLAN = json.load(open(os.path.join(WURZEL, "inhalte", "plan", "rollend-einheiten.json"), encoding="utf-8"))
KUERZEL = "S3"

# (Thema, Klasse, Themen-Datei im Bestand) in der Reihenfolge der Kennungen
THEMEN = [
    ("zahlen.natuerlich", 5, "zahlen.natuerlich"), ("zahlen.rechengesetze", 5, "zahlen.rechengesetze"), ("zahlen.potenzen_basis", 5, "zahlen.potenzen_basis"),
    ("zahlen.ganz", 5, "zahlen.ganz"), ("stochastik.kombinatorik", 5, "stochastik.kombinatorik"), ("messen.koerper_darstellung", 5, "messen.koerper_darstellung"),
    ("terme.umformen", 8, "terme.umformen"), ("terme.umformen_teil2", 8, "terme.umformen"), ("gleichungen.linear", 8, "gleichungen.linear"),
    ("terme.bruchterme", 8, "terme.bruchterme"), ("gleichungen.bruch", 8, "gleichungen.bruch"), ("terme.quadratische_extreme", 8, "terme.quadratische_extreme"),
    ("terme.potenzgesetze_natuerlich", 8, "terme.potenzgesetze_natuerlich"), ("terme.potenzgesetze_ganzzahlig", 8, "terme.potenzgesetze_ganzzahlig"),
    ("stochastik.grundbegriffe", 8, "stochastik.grundbegriffe"), ("messen.prisma_zylinder", 8, "messen.prisma_zylinder"), ("groessen.indirekt", 8, "groessen.indirekt"),
]
KLASSE = {t: k for t, k, _ in THEMEN}
DATEI = {t: d for t, _, d in THEMEN}
REIHE = {t: i for i, (t, _, _) in enumerate(THEMEN)}

# ═════════ Lernkarten ohne Stufe 3 aus rollend-5 und rollend-7 (live gezählt) ═════════
VORHER = defaultdict(lambda: defaultdict(list))     # (Thema, Lernkarte) -> Stufe -> [Formen]
T_VON = {}                                          # (Thema, Lernkarte) -> t der vorhandenen Aufgaben
VORHANDEN_TEXT = set()
for runde in ("rollend-5", "rollend-7"):
    for p in sorted(glob.glob(os.path.join(HIER, "..", runde, "*.json"))):
        for e in json.load(open(p, encoding="utf-8"))["aufgaben"]:
            VORHER[(e["thema"], e["lernkarte"])][e["aufgabe"]["s"]].append(e["form"])
            T_VON.setdefault((e["thema"], e["lernkarte"]), e["aufgabe"]["t"])
            VORHANDEN_TEXT.add(e["aufgabe"]["f"]["text"])
OHNE3 = {k for k, v in VORHER.items() if 3 not in v}
assert sum(1 for k in OHNE3 if KLASSE[k[0]] == 5) == 29 and sum(1 for k in OHNE3 if KLASSE[k[0]] == 8) == 31, "erwartet: 29 in rollend-5, 31 in rollend-7"

geladen = []
nur = sys.argv[1:]
for t, _, _ in THEMEN:
    pfad = os.path.join(HIER, "th_" + t.replace(".", "_") + ".py")
    if os.path.exists(pfad) and (not nur or t in nur):
        exec(compile(open(pfad, encoding="utf-8").read(), pfad, "exec"), {"__name__": "th", **{k: getattr(kern, k) for k in dir(kern) if not k.startswith("_")}})
        geladen.append(t)
assert geladen, "keine Themen-Dateien"

ZAHL = re.compile(r"[−-]?\d+(?:[  ]\d{3})*(?:[,.]\d+)?")
bau_ohne_zahl = lambda t: re.sub(r"\s+", " ", ZAHL.sub("#", t)).strip()
HOCH = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
ZWEIDEUTIG = re.compile(r"\d/\d+[a-zA-Z]|/\([^()]*\(|\)\)/")
ZAHLWORT_ERG = {}


def zahlen_im(text):
    text = re.sub(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+", lambda m: " " + m.group(0).translate(HOCH) + " ", text)
    r = set()
    for m in ZAHL.findall(text):
        s = re.sub(r"[  ]", "", m).replace("−", "").replace("-", "").replace(",", ".")
        r.add(F(s))
    return r


def gleich(a, b):
    return abs(float(a) - float(b)) <= 1e-9


def grafik_ok(g):
    return g["typ"] == "tabelle" and all(len(z) == len(g["kopf"]) and all(isinstance(x, str) for x in z) for z in g["zeilen"]) and all(isinstance(x, str) for x in g["kopf"])


def zahl_aus(x):
    f = F(x)
    return int(f) if f.denominator == 1 else float(f)


# ═════════ Bestand laden ═════════
BESTAND = {}
for t in geladen:
    if DATEI[t] not in BESTAND:
        BESTAND[DATEI[t]] = json.load(open(os.path.join(WURZEL, "inhalte", "themen", DATEI[t] + ".json"), encoding="utf-8"))
KARTE_T = defaultdict(Counter)
for dat, d in BESTAND.items():
    for a in d["aufgaben"]:
        KARTE_T[(dat, a["l"])][a["t"]] += 1
B_TEXT = {dat: {a["f"].get("text", "") for a in d["aufgaben"]} for dat, d in BESTAND.items()}
B_BAU = {dat: {bau_ohne_zahl(a["f"].get("text", "")) for a in d["aufgaben"]} for dat, d in BESTAND.items()}

# ═════════ Prüfen ═════════
A.sort(key=lambda a: REIHE[a["thema"]])      # stabil: Reihenfolge innerhalb eines Themas wie geschrieben
aus = defaultdict(list)
n_fb = n_fb_rechnung = n_fb_ohne = n_rechnung = n_zeilen = 0
alle_texte, alle_bau = set(), defaultdict(set)
FEHLERZEILEN = []
LAGEN = []
for nr, a in enumerate(A, 1):
    thema, lk, form = a["thema"], a["lk"], a["form"]
    kenn = f"{KUERZEL}-V{nr:03d}"
    datei = DATEI[thema]
    assert (thema, lk) in OHNE3, (kenn, thema, lk, "diese Lernkarte hat schon Stufe 3 oder gibt es nicht")
    assert form not in {f for fs in VORHER[(thema, lk)].values() for f in fs}, (kenn, "Form kommt in dieser Lernkarte schon vor", form)
    assert form != "lueckenweg" and a["regel"] in REGELN, (kenn, a["regel"])
    assert ip.STUFE_VON[a["g"]] == 3, kenn
    t = T_VON[(thema, lk)]
    assert t in PLAN["einheiten"][thema]["tf"] and lk in PLAN["einheiten"][thema]["lz"], (kenn, "t oder l nicht in der Einheit")
    assert KARTE_T[(datei, lk)].most_common(1)[0][0] == t, (kenn, "t weicht vom Bestand ab", t, KARTE_T[(datei, lk)])
    h, w = a["h"], a["w"]
    assert h.strip() and len(w) >= 15, kenn
    y = a["y"]
    fb_liste = []            # (Ort, antwort, fehlbildkennung, beschreibung, rechnung)

    if y == "zahl":
        text = a["text"]
        soll = ip.rechne(a["c"])
        assert soll == ip.zahlwert(a["wert"]), (kenn, "c ergibt", soll, "gespeichert", a["wert"])
        zw = a["zweit"]
        zwv = ip.rechne(zw) if isinstance(zw, str) else F(zw)
        assert zwv == soll, (kenn, "zweite Rechnung", zwv, soll)
        n_rechnung += 1
        if abs(soll) >= 10:
            assert abs(soll) not in zahlen_im(text), (kenn, "Ergebnis steht schon im Text")
            assert abs(soll) not in zahlen_im(h), (kenn, "Tipp verrät das Ergebnis")
        assert a["fb"], (kenn, "mindestens ein Fehlbild")
        werte = set()
        for ant, rech, beschr in a["fb"]:
            assert ant != a["wert"] and ant not in werte, (kenn, ant, "gleich der richtigen Antwort oder doppelt")
            werte.add(ant)
            assert beschr and len(beschr) > 5, (kenn, "Beschreibung")
            if rech is not None:
                v = ip.rechne(rech)
                assert v == ip.zahlwert(ant), (kenn, "Fehlbild: Rechnung", rech, "ergibt", float(v), "nicht", ant)
                n_fb_rechnung += 1
            else:
                n_fb_ohne += 1
            fb_liste.append(({}, ant, beschr, rech))
        aufg = {"y": "zahl", "f": {"text": text}, "o": {"wert": a["wert"]}, "c": a["c"]}
        if a["einheit"]:
            aufg["o"]["einheit"] = a["einheit"]
        antwortform = "zahl"
    elif y == "auswahl":
        text = a["text"]
        ant = a["a"]
        assert 3 <= len(ant) <= 4 and len(set(ant)) == len(ant), (kenn, "Antworten")
        assert len(a["wahr"]) == len(ant) and sum(1 for x in a["wahr"] if x is True) == 1 and all(isinstance(x, bool) for x in a["wahr"]), (kenn, "genau eine Antwort muss stimmen", a["wahr"])
        assert a["wahr"][a["richtig"]] is True, (kenn, "richtige Stelle", a["wahr"])
        assert set(a["fb"]) == set(range(len(ant))) - {a["richtig"]}, (kenn, "zu jeder falschen Antwort ein Fehlbild")
        if a["werte"] is not None:
            assert len(a["werte"]) == len(ant) and len({F(str(v)) for v in a["werte"]}) == len(ant), (kenn, "zwei Antworten mit gleichem Wert")
        for i, (beschr, rech) in sorted(a["fb"].items()):
            assert beschr and len(beschr) > 5, (kenn, "Beschreibung")
            if callable(rech):
                assert rech() is True, (kenn, "Fehlbild", i, "die beschriebene Rechnung ergibt nicht diese Antwort")
                n_fb_rechnung += 1
            elif rech is not None:
                assert a["werte"] is not None, (kenn, "Rechnung ohne werte")
                assert ip.rechne(rech) == ip.zahlwert(a["werte"][i]), (kenn, "Fehlbild", i, rech, "ergibt", float(ip.rechne(rech)), "nicht", a["werte"][i])
                n_fb_rechnung += 1
            else:
                n_fb_ohne += 1
            fb_liste.append(({"index": i}, ant[i], beschr, rech))
        n_rechnung += 1
        LAGEN.append((len(ant), a["richtig"]))
        aufg = {"y": "auswahl", "f": {"text": text}, "a": ant, "o": {"index": a["richtig"]}}
        antwortform = "auswahl"
    elif y == "fd":
        z = a["zeilen"]
        assert 3 <= len(z) <= 4 and all(isinstance(x[1], bool) for x in z), (kenn, "Zeilen")
        falsch = [i for i, (_, ok) in enumerate(z) if not ok]
        assert len(falsch) == 1, (kenn, "genau eine Zeile darf nicht stimmen", falsch)
        text = a["einleitung"] + " " + " ".join(f"Zeile {i + 1}: {tx}" for i, (tx, _) in enumerate(z)) + " In welcher Zeile passiert der erste Fehler?"
        ant = [f"In Zeile {i + 1}" for i in range(len(z))]
        FEHLERZEILEN.append((kenn, falsch[0] + 1, KLASSE[thema]))
        n_zeilen += len(z)
        n_rechnung += 1
        for i in range(len(z)):
            if i != falsch[0]:
                fb_liste.append(({"index": i}, ant[i], "diese Zeile ist richtig; der erste Fehler steckt in Zeile %d" % (falsch[0] + 1) if i < falsch[0] else
                                 "diese Zeile folgt aus der falschen Zeile %d richtig; der erste Fehler steckt weiter oben" % (falsch[0] + 1), None))
        n_fb_ohne += len(z) - 1
        aufg = {"y": "auswahl", "f": {"text": text}, "a": ant, "o": {"index": falsch[0]}}
        antwortform = "auswahl"
        a["fb_zeile"] = a["fb_text"]
    else:
        raise AssertionError(kenn)

    assert not ZWEIDEUTIG.search(text), (kenn, "Bruch nicht eindeutig")
    for tx in [text, h, w] + list(a.get("a", [])):
        assert not {"Leo", "Rosa", "Leopold"} & set(re.findall(r"\w+", tx)), (kenn, "Name")
    assert text not in alle_texte and text not in B_TEXT[datei] and text not in VORHANDEN_TEXT, (kenn, "Fragetext schon vorhanden")
    b = bau_ohne_zahl(text)
    assert b not in alle_bau[datei] and b not in B_BAU[datei], (kenn, "Fragetext nur mit anderen Zahlen schon vorhanden")
    if a.get("grafik"):
        assert grafik_ok(a["grafik"]), (kenn, "grafik")
        aufg["f"]["grafik"] = a["grafik"]
    alle_texte.add(text)
    alle_bau[datei].add(b)
    aufg = dict(l=lk, t=t, p="uebung", s=3, g=a["g"], **aufg, h=h, w=w)
    eintrag = dict(kennung=kenn, thema=thema, lernkarte=lk, stufe=3, typ=FORM[form][0], form=form, antwortform=antwortform,
                   regel=a["regel"], regel_name=REGELN[a["regel"]]["name"], zaehlt="ja", fehlbilder=[])
    for ort, antw, beschr, rech in fb_liste:
        eintrag["fehlbilder"].append(dict(**ort, antwort=antw, fehlbild=None, regel_des_fehlbilds=None, beschreibung=beschr, rechnung=rech))
    if y == "fd":
        eintrag["fehlerzeile"] = falsch[0] + 1
        eintrag["fehler"] = a["fb_text"]
        eintrag["zeilen"] = [dict(zeile=i + 1, text=tx, stimmt=ok) for i, (tx, ok) in enumerate(a["zeilen"])]
    eintrag["aufgabe"] = aufg
    aus[thema].append(eintrag)

# ═════════ Vollständigkeit und Mischung ═════════
for t in geladen:
    soll = {lk for (th, lk) in OHNE3 if th == t}
    ist = [e["lernkarte"] for e in aus[t]]
    assert sorted(ist) == sorted(soll) and len(set(ist)) == len(ist), (t, "genau eine Aufgabe je Lernkarte ohne Stufe 3; fehlt/zu viel:", sorted(soll - set(ist)), sorted(set(x for x in ist if ist.count(x) > 1)))
alle = [e for t in geladen for e in aus[t]]
formen = Counter(e["form"] for e in alle)
for kl in (5, 8):
    xs = [e for e in alle if KLASSE[e["thema"]] == kl]
    fk = Counter(e["form"] for e in xs)
    if len(geladen) == len(THEMEN):
        assert fk["fehler_detektiv"] * 3 <= len(xs), (kl, "höchstens ein Drittel Fehler-Detektive", fk)
    zl = Counter(z for _, z, k in FEHLERZEILEN if k == kl)
    if len(geladen) == len(THEMEN) and zl:
        assert max(zl.values()) * 3 <= sum(zl.values()) + 2, (kl, "Fehlerzeile zu einseitig", zl)
if len(geladen) == len(THEMEN):
    lg = Counter(LAGEN)
    for n in (3, 4):
        pos = Counter(p for k, p in LAGEN if k == n)
        assert not pos or max(pos.values()) * 2 <= sum(pos.values()) + 1, (n, "Position der richtigen Antwort einseitig", pos)


def lauf(pfad):
    r = subprocess.run([sys.executable, "-I", os.path.join(WURZEL, "tools", "inhalt_pruefen.py"), pfad], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


print("Datei im Bestand                    neu  inhalt_pruefen vorher → nachher")
with tempfile.TemporaryDirectory() as tmp:
    for datei in dict.fromkeys(DATEI[t] for t in geladen):
        liste = [e["aufgabe"] for t in geladen if DATEI[t] == datei for e in aus[t]]
        quelle = os.path.join(WURZEL, "inhalte", "themen", f"{datei}.json")
        d = json.load(open(quelle, encoding="utf-8"))
        code0, _ = lauf(quelle)
        d["aufgaben"] = d["aufgaben"] + liste
        ziel = os.path.join(tmp, f"{datei}.json")
        json.dump(d, open(ziel, "w", encoding="utf-8"), ensure_ascii=False)
        code1, aus1 = lauf(ziel)
        print(f"{datei:35} {len(liste):3}  Code {code0} → {code1}")
        if code1 != 0:
            print(aus1[-2500:])
        assert code0 == 0 and code1 == 0, datei

# ═════════ Schreiben und Zählen ═════════
KURZ = {"fehler_detektiv": "fd", "umkehren": "um", "zwei_wege": "zw", "bruecke": "br", "anwenden": "an"}
print()
print("Thema                          Lernkarten  Aufgaben  fd/um/zw/br/an")
for t in geladen:
    liste = aus[t]
    c = Counter(e["form"] for e in liste)
    json.dump({"stand": "2026-11-27", "runde": "rollend-11", "kuerzel": KUERZEL, "thema": t, "titel": t, "fuer": f"Klasse {KLASSE[t]}", "klasse": KLASSE[t],
               "themen_datei_im_bestand": DATEI[t],
               "hinweis": "Je Lernkarte ohne Aufgabe auf Stufe 3 in rollend-5/rollend-7 genau eine zählende Aufgabe der Stufe 3 in neuer Form. Nicht eingespielt. "
                          "Je Eintrag: thema (Einheit), lernkarte, typ, form, zaehlt, Regel-Kennung, Fehlbilder (mit rechnung) und unter „aufgabe“ die Aufgabe im Format von inhalte/README.md.",
               "aufgaben": liste}, open(os.path.join(HIER, f"{t}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{t:30} {len(liste):10} {len(liste):9}  " + "/".join(str(c[f]) for f in KURZ))
print()
print("Summe Lernkarten", len(alle), "Aufgaben", len(alle), "| Formen", dict(formen))
for kl in (5, 8):
    print(f"Klasse {kl}:", len([e for e in alle if KLASSE[e['thema']] == kl]), "Aufgaben", dict(Counter(e['form'] for e in alle if KLASSE[e['thema']] == kl)))
print(f"{n_fb_rechnung} Fehlbilder mit Rechnung nachgerechnet, {n_fb_ohne} ohne Rechnung (Worte, Zeilen oder Auswahltext); {n_rechnung} Lösungen nachgerechnet; {n_zeilen} Detektiv-Zeilen einzeln geprüft")
print("Fehler-Detektiv: Fehlerzeile je Zeile", dict(sorted(Counter(z for _, z, _ in FEHLERZEILEN).items())), "von", len(FEHLERZEILEN))
print("Lage der richtigen Auswahlantwort (Anzahl Antworten, Platz):", dict(sorted(Counter(LAGEN).items())))
print("Themen geladen:", ", ".join(geladen))
print("OK")
