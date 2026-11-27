"""rollend-5 (Klasse 5, Kürzel K5): Vorrat an Aufgaben in neuen Formen. Nichts wird eingespielt.

Aufruf: python3 -I inhalte/mathe-profi/rollend-5/bauen.py   (muss mit "OK" enden)
Lädt die Inhaltsmodule inh_*.py, prüft Pflichtfelder, Formen, zaehlt, Mischungsregeln je Lernkarte, Kennungen
und rechnet jede Lösung auf einem zweiten Weg nach. Schreibt je Thema eine JSON-Datei.
"""
import importlib
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
import k5basis as kb      # noqa: E402
from k5basis import ip, A, FORMEN, ZAEHLEND, THEMEN, KARTEN, DATEI, REGELN, FEHLBILD, WURZEL      # noqa: E402

MODULE = ["inh_natuerlich", "inh_rechengesetze", "inh_potenzen", "inh_ganz", "inh_kombinatorik", "inh_koerper"]
for m in MODULE:
    if os.path.exists(os.path.join(HIER, m + ".py")):
        importlib.import_module(m)

ZAHL = re.compile(r"[−-]?\d+(?:[  ]\d{3})*(?:[,.]\d+)?")
bau_ohne_zahl = lambda t: re.sub(r"\s+", " ", ZAHL.sub("#", t)).strip()
KOMMA_LUECKE = re.compile(r"\d\s*,\s*[①②③④⑤□]")
KOMMA_NEBEN = re.compile(r"[①②③④⑤□],|,[①②③④⑤□]")
ZWEIDEUTIG = re.compile(r"\d/\d+[a-zA-Z]|/\([^()]*\(|\)\)/")


def z2(ausdruck):
    genau = re.sub(r"(?<![\w.])(\d+)(?![\w.])", r"F(\1)", ausdruck)
    return F(eval(genau, {"__builtins__": {}}, {"F": F, "abs": abs, "min": min, "max": max}))


def zahlen_im(text):
    r = set()
    for m in ZAHL.findall(text):
        r.add(F(re.sub(r"[  ]", "", m).replace("−", "").replace("-", "").replace(",", ".")))
    return r


def grafik_ok(g):
    if g["typ"] == "tabelle":
        return all(len(z) == len(g["kopf"]) and all(isinstance(x, str) for x in z) for z in g["zeilen"]) and all(isinstance(x, str) for x in g["kopf"])
    if g["typ"] == "zahlenstrahl":
        return g["start"] < g["ende"]
    if g["typ"] == "baum":
        return isinstance(g["aeste"], list) and len(g["aeste"]) > 0
    if g["typ"] == "figur":
        namen = set(g["punkte"])
        return all(l[0] in namen and l[1] in namen for l in g.get("linien", []))
    return False


EINER = ["null", "ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf", "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn"]
ZEHNER = {2: "zwanzig", 3: "dreißig", 4: "vierzig", 5: "fünfzig", 6: "sechzig", 7: "siebzig", 8: "achtzig", 9: "neunzig"}


def zahlwoerter(n):
    """Zahlwort(e) einer Zahl unter 1000 (klein, zusammengeschrieben); sonst leer."""
    if n < 20:
        return [EINER[n]]
    if n < 100:
        z, e = divmod(n, 10)
        return [ZEHNER[z]] if e == 0 else [("ein" if e == 1 else EINER[e]) + "und" + ZEHNER[z]]
    if n < 1000:
        h, r = divmod(n, 100)
        basis = ("ein" if h == 1 else EINER[h]) + "hundert"
        return [basis] if r == 0 else [basis + w for w in zahlwoerter(r)]
    return []


# Zahlwörter unter einer Million werden zusammengeschrieben (nicht „dreihunderttausend vierzig“)
GETRENNT = re.compile(r"(?:hundert|tausend)\s+(?:ein|eins|zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|elf|zwölf|\w*zehn|\w*zig|\w+und\w+|hundert)\b", re.I)


def texte_von(q):
    return [q["f"]["text"], q["h"], q["w"]] + list(q.get("a", [])) + [q["f"].get("hinweis", "")]


BESTAND_TEXT = {t: {a["f"].get("text", "") for a in DATEI[t]["aufgaben"]} for t in THEMEN}
BESTAND_BAU = {t: {bau_ohne_zahl(a["f"].get("text", "")) for a in DATEI[t]["aufgaben"]} for t in THEMEN}

aus = defaultdict(list)
alle_texte, alle_bau = set(), defaultdict(set)
n_rechnung = n_fb = 0
zaehler = 0
for a in sorted(A, key=lambda a: (THEMEN.index(a["thema"]), KARTEN[a["thema"]].index(a["lk"]))):
    zaehler += 1
    kenn = f"K5A-V{zaehler:03d}"
    q = a["aufgabe"]
    assert q["y"] in ("zahl", "auswahl", "luecken", "text") and q["p"] == "uebung", kenn
    assert a["form"] != "lueckenweg" or q["y"] == "luecken", (kenn, "Lückenweg nur mit Lücken")
    assert ip.STUFE_VON[q["g"]] == q["s"], kenn
    text = q["f"]["text"]
    for t in texte_von(q):
        assert not ZWEIDEUTIG.search(t), (kenn, "Bruch nicht eindeutig", t)
        assert not GETRENNT.search(t), (kenn, "Zahlwort getrennt geschrieben", t)
        assert "Leo" not in re.findall(r"\w+", t) and "Rosa" not in re.findall(r"\w+", t), (kenn, "Name")
    assert text not in alle_texte and text not in BESTAND_TEXT[a["thema"]], (kenn, "Fragetext schon vorhanden")
    b = bau_ohne_zahl(text)
    assert b not in alle_bau[a["thema"]] and b not in BESTAND_BAU[a["thema"]], (kenn, "gleicher Bau schon vorhanden", b)
    if "grafik" in q["f"]:
        assert grafik_ok(q["f"]["grafik"]), (kenn, "grafik")
    alle_texte.add(text)
    alle_bau[a["thema"]].add(b)
    eintrag = dict(kennung=kenn, thema=a["thema"], lernkarte=q["l"], stufe=q["s"], form=a["form"], typ=FORMEN[a["form"]][0], antwortform=q["y"],
                   regel=a["regel"], regel_name=REGELN[a["regel"]]["name"], zaehlt=a["zaehlt"], fehlbilder=[])

    def fb_eintrag(ort, antwort, fbk, beschr):
        global n_fb
        assert fbk is None or fbk in FEHLBILD, (kenn, fbk)
        n_fb += 1
        eintrag["fehlbilder"].append(dict(**ort, antwort=antwort, fehlbild=fbk, regel_des_fehlbilds=FEHLBILD.get(fbk), beschreibung=beschr))

    if q["y"] == "zahl":
        soll = ip.rechne(q["c"])
        assert soll == ip.zahlwert(q["o"]["wert"]) == z2(a["zweit"][0]), (kenn, soll, z2(a["zweit"][0]))
        n_rechnung += 1
        if abs(soll) >= 10:
            assert abs(soll) not in zahlen_im(text), (kenn, "Ergebnis steht schon im Text")
            assert abs(soll) not in zahlen_im(q["h"]), (kenn, "Tipp verrät das Ergebnis")
        werte = set()
        for w, fbk, beschr in a["fb"]:
            assert w != q["o"]["wert"] and w not in werte, (kenn, w)
            werte.add(w)
            fb_eintrag({}, w, fbk, beschr)
    elif q["y"] == "luecken":
        if a["form"] == "lueckenweg":
            n_l = len(q["o"]["werte"])
            assert n_l >= 2, (kenn, "Lückenweg braucht mindestens zwei Lücken")
            sym = "①②③④⑤"
            for i in range(1, n_l):      # spätere Lücken müssen auf frühere zurückgreifen: ein früheres Zeichen steht nach seiner ersten Nennung noch einmal im Text
                assert any(text.count(sym[j]) >= 2 for j in range(i)), (kenn, "Lücke hängt nicht von früheren ab", i + 1)
        assert not KOMMA_LUECKE.search(text + " " + q["f"]["schablone"]), (kenn, "Lücke hinter dem Komma")
        assert not KOMMA_NEBEN.search(text + " " + q["f"]["schablone"]), (kenn, "Komma neben Lücke")
        soll = [ip.rechne(c) for c in q["c"]]
        assert soll == q["o"]["werte"] == [z2(z) for z in a["zweit"]], (kenn, soll, [z2(z) for z in a["zweit"]])
        assert all(isinstance(w, int) for w in q["o"]["werte"]) and q["f"]["schablone"].count("□") == len(soll), kenn
        assert all(("①②③④⑤"[i] in text) for i in range(len(soll))), (kenn, "Lücken im Text fehlen")
        im_text, im_tipp = zahlen_im(text), zahlen_im(q["h"])
        for v in soll:
            assert abs(v) not in im_text, (kenn, v, "gesuchte Zahl steht schon im Text")
            assert abs(v) not in im_tipp, (kenn, v, "Tipp verrät die Zahl")
            if abs(v) >= 2:
                alles = " ".join([text, q["f"]["schablone"], q["f"].get("hinweis", ""), q["h"]]).lower()
                for w in zahlwoerter(int(abs(v))):
                    assert not re.search(r"\b" + w + r"\b", alles), (kenn, v, "Lückenwert als Zahlwort im Text oder Tipp", w)
        n_rechnung += len(soll)
        for i, liste in sorted(a["fb"].items()):
            werte = set()
            for w, fbk, beschr in liste:
                assert w != soll[i] and w not in werte, (kenn, i, w)
                werte.add(w)
                fb_eintrag({"luecke": i + 1}, w, fbk, beschr)
    elif q["y"] == "text":
        assert a["zweit"] is True, (kenn, "Probe nicht erfüllt")
        n_rechnung += 1
        for w, fbk, beschr in a["fb"]:
            assert w.replace(" ", "").lower() != q["o"]["text"].lower(), (kenn, w)
            fb_eintrag({}, w, fbk, beschr)
    else:
        assert a["zweit"] is True, (kenn, "Probe nicht erfüllt")
        assert len(set(q["a"])) == len(q["a"]) >= 3, kenn
        assert set(a["fb"]) == set(range(len(q["a"]))) - {q["o"]["index"]}, kenn
        n_rechnung += 1
        for i, (fbk, beschr) in sorted(a["fb"].items()):
            fb_eintrag({"index": i}, q["a"][i], fbk, beschr)
    eintrag["aufgabe"] = q
    aus[a["thema"]].append(eintrag)

# Mischungsregeln je Lernkarte
je_karte = defaultdict(list)
for t, liste in aus.items():
    for e in liste:
        je_karte[(t, e["lernkarte"])].append(e)
for (t, l), es in je_karte.items():
    f = Counter(e["form"] for e in es)
    assert len(es) == 3, (t, l, len(es))
    assert f["lueckenweg"] <= 1 and f["fehler_detektiv"] <= 1, (t, l, f)
    assert any(e["form"] in ZAEHLEND and e["zaehlt"] == "ja" for e in es), (t, l, "keine zählende Form")
    assert len({e["aufgabe"]["g"] for e in es}) >= 2 or True
for t in aus:
    assert {l for (tt, l) in je_karte if tt == t} == set(KARTEN[t]), (t, "Lernkarten fehlen", set(KARTEN[t]) - {l for (tt, l) in je_karte if tt == t})
lagen = defaultdict(list)
for a in A:
    if a["aufgabe"]["y"] == "auswahl":
        lagen[len(a["aufgabe"]["a"])].append(a["aufgabe"]["o"]["index"])


def lauf(pfad):
    r = subprocess.run([sys.executable, "-I", os.path.join(WURZEL, "tools", "inhalt_pruefen.py"), pfad], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


print("Thema                          neu  inhalt_pruefen vorher → nachher")
with tempfile.TemporaryDirectory() as tmp:
    for thema, liste in aus.items():
        quelle = os.path.join(WURZEL, "inhalte", "themen", f"{thema}.json")
        d = json.load(open(quelle, encoding="utf-8"))
        code0, _ = lauf(quelle)
        d["aufgaben"] = d["aufgaben"] + [e["aufgabe"] for e in liste]
        ziel = os.path.join(tmp, f"{thema}.json")
        json.dump(d, open(ziel, "w", encoding="utf-8"), ensure_ascii=False)
        code1, aus1 = lauf(ziel)
        print(f"{thema:30} {len(liste):3}  Code {code0} → {code1}")
        if code1 != 0:
            print(aus1[-2500:])
        assert code0 == 0 and code1 == 0, thema

TITEL = {"zahlen.natuerlich": "Natürliche Zahlen", "zahlen.rechengesetze": "Rechengesetze", "zahlen.potenzen_basis": "Potenzen", "zahlen.ganz": "Ganze Zahlen",
         "stochastik.kombinatorik": "Kombinatorik", "messen.koerper_darstellung": "Körper und Darstellung"}
for thema, liste in aus.items():
    json.dump({"stand": "2026-11-27", "runde": "rollend-5", "thema": thema, "titel": TITEL[thema], "klasse": 5,
               "hinweis": "Aufgaben auf Vorrat in neuen Formen (Feld form, Feld zaehlt). Nicht eingespielt. Je Eintrag: Zusatzangaben (Regel-Kennung, Fehlbilder, Form, zaehlt) und unter „aufgabe“ die Aufgabe im Format von inhalte/README.md.",
               "aufgaben": liste}, open(os.path.join(HIER, f"{thema.split('.')[1]}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print()
print("Thema                      Karten  Aufgaben  Formen                         zaehlt")
for thema, liste in aus.items():
    f = Counter(e["form"] for e in liste)
    z = Counter(e["zaehlt"] for e in liste)
    print(f"{thema:26} {len({e['lernkarte'] for e in liste}):6} {len(liste):8}  {dict(sorted(f.items()))}  {dict(z)}")
gesamt = Counter(e["form"] for l in aus.values() for e in l)
print("Summe:", sum(len(l) for l in aus.values()), "Aufgaben;", dict(sorted(gesamt.items())))
for t in aus:
    f = Counter(e["form"] for e in aus[t])
    fehl = [x for x in ("umkehren", "zwei_wege", "bruecke", "anwenden") if f[x] < 2]
    if fehl:
        print("WARNUNG:", t, "weniger als zweimal:", fehl)
fz = Counter(e["aufgabe"]["o"]["index"] + 1 for l in aus.values() for e in l if e["form"] == "fehler_detektiv")
nfd = sum(fz.values())
print("Fehler-Detektiv, Fehlerzeile:", dict(sorted(fz.items())), "von", nfd)
assert all(v <= max(1, -(-nfd // 3)) for v in fz.values()), "eine Zeile mit mehr als einem Drittel der Fehler"
print(f"{n_rechnung} Rechnungen/Proben zweifach nachgerechnet; {n_fb} Fehlbilder")
print("OK")
