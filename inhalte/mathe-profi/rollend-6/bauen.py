"""Mathe-Profi, Auftrag „Vorrat neue Formen“ (Helfer Aufgaben), Runde rollend-6, Kürzel K6, Zielgruppe Klasse 6.

Aufruf: python3 -I inhalte/mathe-profi/rollend-6/bauen.py     (muss mit „OK“ enden)
Lädt th_<Thema>.py (je Thema eine Datei mit den Aufgaben), prüft alles (Teil A der „Lehren aus der Gegenprüfung“),
schreibt je Thema <Thema>.json. Nur Inhalte. Nichts wird eingespielt.
"""
import json
import math
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
# Bewusst gesetzte Ausnahmen: Katalogtext trifft zu, das Thema steht aber (noch) nicht in der Themenliste der Kennung.
REGEL_AUSNAHME = {("bruch.rechnen", "rr.potenz"), ("messen.volumen", "id.flaeche_raum.aus_dem_quader"),
                  ("messen.koerper_berechnung", "id.flaeche_raum.aus_dem_quader")}
FEHLBILD = {f["kennung"]: e["kennung"] for e in KENN for f in e["fehlbilder"]}

THEMEN = {
    "bruch.brueche": ("bruch.brueche", ["bruchteil_von", "anteil_bestimmen", "ganzes_bestimmen", "erweitern", "ggt", "kuerzen", "verhaeltnis_kuerzen", "gleichwertig",
                                        "gemischte_zahlen", "kgv", "vergleichen", "zahlenstrahl", "zahlbereiche", "verstehen"]),
    "bruch.dezimal": ("bruch.dezimal", ["stellenwerte", "vergleichen_ordnen", "runden", "bruch_zu_dezimal", "dezimal_zu_bruch", "merkwerte", "periodisch", "verstehen"]),
    "bruch.rechnen": ("bruch.rechnen", ["brueche_plus_minus", "dezimal_plus_minus", "vorzeichen", "brueche_mal", "brueche_geteilt", "dezimal_mal", "dezimal_geteilt",
                                        "potenzen", "rechenvorteile", "gemischt", "fehler_finden", "sach"]),
    "bruch.prozent": ("bruch.prozent", ["prozent_bedeutung", "prozentwert", "prozentsatz", "grundwert", "rabatt_aufschlag", "verstehen"]),
    "terme.aufstellen": ("terme.aufstellen", ["struktur", "termwert", "uebersetzen", "sachsituation", "muster", "deuten"]),
    "messen.flaechen_vielecke": ("messen.flaechen_vielecke", ["parallelogramm", "dreieck", "trapez", "rueckwaerts", "zusammengesetzt", "oberflaeche", "verstehen", "drachen_raute"]),
    "messen.volumen": ("messen.volumen", ["einheitswuerfel", "quader", "einheiten", "liter", "rueckwaerts", "zusammengesetzt", "verstehen"]),
    "messen.koerper_berechnung": ("messen.koerper_berechnung", ["quader", "oberflaeche", "sachaufgaben", "zusammengesetzt", "verstehen"]),
}
KUERZEL = "K6"
GEPRUEFT = ("umkehren", "zwei_wege", "bruecke", "anwenden")
ZAEHLT_JA_AUS = ("umkehren", "zwei_wege", "bruecke", "verfahren_waehlen", "anwenden")

geladen = []
for schl in THEMEN:
    pfad = os.path.join(HIER, "th_" + schl.replace(".", "_") + ".py")
    if os.path.exists(pfad):
        exec(compile(open(pfad, encoding="utf-8").read(), pfad, "exec"), {"__name__": "th", **{k: getattr(kern, k) for k in dir(kern) if not k.startswith("_")}})
        geladen.append(schl)
assert geladen, "keine Themen-Dateien"

ZAHL = re.compile(r"[−-]?\d+(?:[  ]\d{3})*(?:[,.]\d+)?")
bau_ohne_zahl = lambda t: re.sub(r"\s+", " ", ZAHL.sub("#", t)).strip()
KOMMA_LUECKE = re.compile(r"\d\s*,\s*[①②③④⑤□]")
KOMMA_NEBEN = re.compile(r"[①②③④⑤□],|,[①②③④⑤□]")
ZWEIDEUTIG = re.compile(r"\d/\d+[a-zA-Z]|/\([^()]*\(|\)\)/")

# Zahlwörter (wie tools/vorrat_pruefen.py): Lückenwert darf auch als Wort nicht im Text stehen
ZAHLWORTE = {0: ['null', 'kein', 'keine', 'keinen', 'keiner', 'keinem', 'nie', 'nichts', 'niemals'],
             1: ['eins', 'einmal', 'einzige', 'einziger', 'einziges', 'einzigen'],
             2: ['zwei', 'zweimal', 'doppelt', 'doppelte', 'doppelten', 'doppeltes', 'verdoppelt', 'halbe', 'halbiert', 'hälfte'],
             3: ['drei', 'dreimal', 'dreifache', 'dreifachen'], 4: ['vier', 'viermal'], 5: ['fünf', 'fünfmal'],
             6: ['sechs'], 7: ['sieben'], 8: ['acht'], 9: ['neun'], 10: ['zehn'], 11: ['elf'], 12: ['zwölf'],
             13: ['dreizehn'], 14: ['vierzehn'], 15: ['fünfzehn'], 16: ['sechzehn'], 17: ['siebzehn'],
             18: ['achtzehn'], 19: ['neunzehn'], 20: ['zwanzig']}
EIN = re.compile(r'\bein(?:e|en)?\s+(?:Paar|Punkt|Schnittpunkt|gemeinsamen?)\w*', re.I)


def wortfund(wert, s):
    w = abs(wert)
    if w.denominator != 1 or w.numerator > 20:
        return []
    t = [x for x in ZAHLWORTE.get(int(w), []) if re.search(r'(?<![\wäöüß])' + x + r'(?![\wäöüß])', s, re.I)]
    if int(w) == 1 and EIN.search(s):
        t.append(EIN.search(s).group(0))
    return t


HOCH = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
HOCHLAUF = re.compile(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+")


def zahlen_im(text):
    text = HOCHLAUF.sub(lambda m: " " + m.group(0).translate(HOCH) + " ", text)
    r = set()
    for m in ZAHL.findall(text):
        s = re.sub(r"[  ]", "", m).replace("−", "").replace("-", "").replace(",", ".")
        r.add(F(s))
    return r


def texte_von(q):
    return [q["f"]["text"], q["h"], q["w"]] + list(q.get("a", [])) + [q["f"].get("hinweis", "")]


# Antwort als Zahl lesen (nur um gleiche Werte bei Auswahl zu erkennen und Rechnungen zu prüfen)
ANT = re.compile(r"^\s*(?:(\d+)\s+)?([−-]?\d+(?:[  ]\d{3})*(?:,\d+)?)(?:/(\d+))?\s*(%|€|ct|Cent|cm²|cm³|dm²|dm³|m²|m³|mm²|mm³|cm|dm|mm|km|kg|g|ml|l|m|h|min|s|°|Stücke|Stück)?\s*$")


def ant_wert(s):
    m = ANT.match(s)
    if not m:
        return None
    ganz, z, n, unit = m.groups()
    z = F(re.sub(r"[  ]", "", z).replace("−", "-").replace(",", "."))
    if n:
        z = z / int(n)
    if ganz:
        z = z + int(ganz)
    return (z, unit)


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

PLATZ = re.compile(r"\{(\d+)\}")


def setze_ein(ausdruck, frueher):
    def ers(m):
        n = int(m.group(1))
        assert 1 <= n <= len(frueher), (ausdruck, "Verweis auf eine spätere oder fehlende Lücke", n)
        return f"({frueher[n - 1]})"
    return PLATZ.sub(ers, ausdruck)


def wert_von_c(ausdruck, frueher):
    t = setze_ein(str(ausdruck), frueher)
    v = ip.rechne(t)
    return (int(v) if v.denominator == 1 else v), t


def verweise(ausdruck):
    return {int(n) for n in PLATZ.findall(str(ausdruck))}


def hang_ab(vorlage, soll, i, n):
    ist = soll[i]
    for neu_wert in (0, soll[n - 1] + 1, soll[n - 1] + 2, -soll[n - 1] - 1):
        andere = list(soll[:i])
        andere[n - 1] = neu_wert
        try:
            if wert_von_c(vorlage, andere)[0] != ist:
                return True
        except ZeroDivisionError:
            return True
    return False


def fb_pruefen(kenn, ort, wert, rechnung, frueher=()):
    """Das Fehlbild nennt eine Rechnung: sie muss den falschen Wert wirklich ergeben. Rückgabe: fertige Rechnung (Text) oder None (keine Rechnung)."""
    assert rechnung is not None, (kenn, ort, wert, "Fehlbild ohne Rechnung (4. Eintrag: Ausdruck, Funktion oder False)")
    if rechnung is False:
        return None
    if callable(rechnung):
        assert rechnung() is True, (kenn, ort, wert, "Fehlbild stimmt nicht")
        return "(Prüffunktion)"
    v, t = wert_von_c(rechnung, list(frueher))
    ok = F(v) == ip.zahlwert(wert)   # exakt: keine gerundeten Fehlwerte (Vorprüfung)
    assert ok, (kenn, ort, "Fehlbild: Rechnung", t, "ergibt", float(v), "nicht", wert)
    return t


# ═════════ Prüfen ═════════
reihe = {schl: i for i, schl in enumerate(THEMEN)}
A.sort(key=lambda a: (reihe[a["thema"]], THEMEN[a["thema"]][1].index(a["lk"]), a["rang"]))
aus = defaultdict(list)
n_rechnung = n_fb = n_fb_rechnung = n_fb_ohne = n_abhaengig = 0
alle_texte, alle_bau = set(), defaultdict(set)
ohne_c_liste = []
zaehler = 0
for a in A:
    assert a["thema"] in geladen and a["lk"] in THEMEN[a["thema"]][1], (a["thema"], a["lk"])
    datei = THEMEN[a["thema"]][0]
    q = a["aufgabe"]
    gleich_ok = bool(q.pop("_gleich_ok", False))
    zaehler += 1
    kenn = f"{KUERZEL}-V{zaehler:03d}"
    # Regel-Kennung nur, wenn der Katalogtext (genau) die Aufgabe wirklich trifft; sonst leer (None).
    assert a["regel"] is None or a["regel"] in REGELN, (kenn, "Regel-Kennung nicht im Katalog", a["regel"])
    assert a["regel"] is None or datei in REGELN[a["regel"]]["themen"] or (datei, a["regel"]) in REGEL_AUSNAHME, (kenn, "Regel passt nicht zum Thema", datei, a["regel"])
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
        assert not re.search("[¼½¾⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞]", t), (kenn, "Unicode-Bruchzeichen")
    assert text not in alle_texte and text not in BESTAND_TEXT[datei], (kenn, "Fragetext schon vorhanden")
    b = bau_ohne_zahl(text)
    assert b not in alle_bau[datei] and b not in BESTAND_BAU[datei], (kenn, "Fragetext nur mit anderen Zahlen schon vorhanden", b)
    alle_texte.add(text)
    alle_bau[datei].add(b)
    eintrag = dict(kennung=kenn, thema=a["thema"], lernkarte=a["lk"], stufe=a["s"], typ=FORM[a["form"]][0], form=a["form"], antwortform=q["y"],
                   regel=a["regel"], regel_name=REGELN[a["regel"]]["name"] if a["regel"] else None, zaehlt=a["zaehlt"], fehlbilder=[])

    def fb_eintrag(ort, antwort, fbk, beschr, c):
        global n_fb
        assert fbk is None or fbk in FEHLBILD, (kenn, fbk)
        assert beschr and len(beschr) > 5, (kenn, "Beschreibung des Fehlbilds")
        n_fb += 1
        eintrag["fehlbilder"].append(dict(**ort, antwort=antwort, fehlbild=fbk, regel_des_fehlbilds=FEHLBILD.get(fbk), beschreibung=beschr, c=c))

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
        for t in a["fb"]:
            assert len(t) == 4, (kenn, t[:1], "Fehlbild braucht 4 Einträge (Wert, Kennung, Beschreibung, Rechnung)")
            w, fbk, beschr, rech = t
            assert w != q["o"]["wert"] and w not in werte, (kenn, w)
            werte.add(w)
            ct = fb_pruefen(kenn, "Zahl", w, rech)
            if ct:
                n_fb_rechnung += 1
            else:
                n_fb_ohne += 1
                ohne_c_liste.append((kenn, "Zahl", w))
            fb_eintrag({}, w, fbk, beschr, ct)
    elif q["y"] == "luecken":
        assert not KOMMA_LUECKE.search(text + " " + q["f"]["schablone"]), (kenn, "Lücke hinter dem Komma")
        assert not KOMMA_NEBEN.search(text + " " + q["f"]["schablone"]), (kenn, "Komma direkt neben einer Lücke")
        vorlagen = [str(c) for c in q["c"]]
        soll, c_fertig = [], []
        for v in vorlagen:
            wert_i, t = wert_von_c(v, soll)
            soll.append(wert_i)
            c_fertig.append(t)
        zw = [z2(z) if isinstance(z, str) else F(z) for z in a["zweit"]]
        assert soll == q["o"]["werte"] == zw, (kenn, soll, a["zweit"])
        assert not any(PLATZ.search(str(z)) for z in a["zweit"]), (kenn, "Zweitrechnung muss unabhängig sein")
        q["c"] = c_fertig
        assert all(isinstance(w, int) for w in q["o"]["werte"]) and q["f"]["schablone"].count("□") == len(soll), kenn
        if a["form"] == "lueckenweg":
            im_text = text + " " + q["f"]["schablone"] + " " + q["f"].get("hinweis", "") + " " + q["h"]
            zi = zahlen_im(im_text)
            for v in soll:
                assert abs(v) not in zi, (kenn, v, "Lückenwert steht schon in Text, Schablone, Hinweis oder Tipp")
                wf = wortfund(F(v), im_text)
                assert not wf, (kenn, v, "Lückenwert als Zahlwort im Text", wf)
            assert len(soll) >= 2 and q["y"] == "luecken", (kenn, "Lückenweg: mindestens zwei Lücken")
            refs = [verweise(v) for v in vorlagen]
            assert refs[-1], (kenn, "die letzte Lücke muss von einer früheren abhängen ({n} in c)")
            assert sum(1 for r in refs[1:] if r) >= 1, kenn
            for i, r in enumerate(refs):
                for n in r:
                    assert n <= i, (kenn, "Verweis nach vorn")
                    assert hang_ab(vorlagen[i], soll, i, n), (kenn, i + 1, n, "Lücke hängt in Wahrheit nicht vom früheren Wert ab")
            assert sum(1 for r in refs[1:] if r) >= 1 and sum(1 for r in refs if r) >= 1, kenn
            # Vorprüfung: Lückenweg mit nur zwei Lücken hat genau eine abhängige; ab drei Lücken müssen mindestens zwei von früheren abhängen
            assert len(soll) == 2 or sum(1 for r in refs if r) >= 2, (kenn, "ab drei Lücken mindestens zwei abhängige Lücken")
            n_abhaengig += 1
            assert gleich_ok or len(set(soll)) == len(soll), (kenn, "Lückenwerte sollen verschieden sein")
            assert a["fb"], (kenn, "Lückenweg braucht Fehlbilder")
        n_rechnung += len(soll)
        for i, liste in sorted(a["fb"].items()):
            werte = set()
            for t in liste:
                assert len(t) == 4, (kenn, i + 1, t[:1], "Fehlbild braucht 4 Einträge (Wert, Kennung, Beschreibung, Rechnung)")
                w, fbk, beschr, rech = t
                assert w != soll[i] and w not in werte, (kenn, i, w)
                assert isinstance(w, int), (kenn, i, w, "Fehlwert einer Lücke muss eine ganze Zahl sein (Eingabe: ganze Zahl)")
                werte.add(w)
                ct = fb_pruefen(kenn, f"Lücke {i + 1}", w, rech, soll[:i])
                if ct:
                    n_fb_rechnung += 1
                else:
                    n_fb_ohne += 1
                    ohne_c_liste.append((kenn, f"Lücke {i + 1}", w))
                fb_eintrag({"luecke": i + 1}, w, fbk, beschr, ct)
    else:
        assert a["zweit"]() is True and len(set(q["a"])) == len(q["a"]) >= 3, kenn
        assert set(a["fb"]) == set(range(len(q["a"]))) - {q["o"]["index"]}, kenn
        werte_a = [ant_wert(x) for x in q["a"]]
        if all(v is not None for v in werte_a):
            assert len(set(werte_a)) == len(werte_a), (kenn, "zwei Antworten mit gleichem Wert", q["a"])
        n_rechnung += 1
        for i, (fbk, beschr, rech) in sorted(a["fb"].items()):
            ct = None
            if rech is not None:
                v = ant_wert(q["a"][i])
                assert v is not None, (kenn, q["a"][i], "Antwort nicht als Zahl lesbar, aber Rechnung angegeben")
                r = ip.rechne(rech)
                v = v[0]
                assert r == v, (kenn, q["a"][i], "Rechnung", rech, "ergibt", float(r))
                ct = rech
                n_fb_rechnung += 1
            else:
                n_fb_ohne += 1
                ohne_c_liste.append((kenn, "Auswahl", q["a"][i]))
            fb_eintrag({"index": i}, q["a"][i], fbk, beschr, ct)
    eintrag["aufgabe"] = q
    aus[a["thema"]].append(eintrag)

STUFEN = {}
# ═════════ Mischung je Lernkarte und je Thema ═════════
for schl in geladen:
    for lk in THEMEN[schl][1]:
        xs = [e for e in aus[schl] if e["lernkarte"] == lk]
        formen = Counter(e["form"] for e in xs)
        if not xs and "--voll" not in sys.argv:
            continue
        assert len(xs) == 3, (schl, lk, "genau drei Aufgaben", len(xs))
        assert formen["lueckenweg"] <= 1, (schl, lk, "höchstens ein Lückenweg")
        assert formen["fehler_detektiv"] <= 1, (schl, lk, "höchstens ein Fehler-Detektiv")
        assert any(e["zaehlt"] == "ja" and e["form"] in ZAEHLT_JA_AUS for e in xs), (schl, lk, "mindestens eine zählende Aufgabe aus umkehren/zwei_wege/bruecke/verfahren_waehlen/anwenden")
        stu = [e["stufe"] for e in xs if e["zaehlt"] == "ja"]
        assert 2 in stu and 3 in stu, (schl, lk, "mindestens eine zählende Aufgabe auf Stufe 2 und eine auf Stufe 3", stu)
        STUFEN[(schl, lk)] = tuple(sorted(e["stufe"] for e in xs))
AUSNAHME = {}
for schl in geladen:
    c = Counter(e["form"] for e in aus[schl])
    for f in GEPRUEFT:
        assert c[f] >= 2 or "--voll" not in sys.argv or (schl, f) in AUSNAHME, (schl, f, "weniger als zweimal", c[f])

lagen = defaultdict(list)
for a in A:
    if a["aufgabe"]["y"] == "auswahl" and a["form"] != "fehler_detektiv":
        lagen[len(a["aufgabe"]["a"])].append(a["aufgabe"]["o"]["index"])
if len(geladen) == len(THEMEN):
    assert set(lagen[4]) == {0, 1, 2, 3} and set(lagen[3]) <= {0, 1, 2}, lagen


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
    json.dump({"stand": "2026-11-27", "runde": "rollend-6", "kuerzel": KUERZEL, "flug": "k6-" + schl, "titel": schl, "fuer": "Klasse 6", "klasse": 6,
               "themen": [schl], "themen_datei_im_bestand": datei,
               "hinweis": "Aufgaben auf Vorrat in neuer Form (Feld form: " + ", ".join(FORM) + "), Auftrag Vorrat neue Formen. Nicht eingespielt. Je Eintrag: thema, lernkarte, "
                          "typ (Name wie in tools/rollend_sql.py), form, zaehlt (ja/nein), Regel-Kennung, Fehlbilder (mit Rechnung c, wo es eine gibt) und unter „aufgabe“ die Aufgabe im Format von inhalte/README.md.",
               "aufgaben": liste}, open(os.path.join(HIER, f"{schl}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{schl:30} {len(lks):10} {len(liste):9}  " + "/".join(str(c[f]) for f in KURZ) + f"   {z['ja']}/{z['nein']}")
print()
print("Summe Lernkarten", sum(len(THEMEN[s][1]) for s in geladen), "Aufgaben", len(A), "| Formen", dict(gesamt_f), "| zaehlt", dict(gesamt_z))
print(f"{n_fb_rechnung} Fehlbilder mit Rechnung nachgerechnet, {n_fb_ohne} ohne Rechnung (c = null); {n_abhaengig} Lückenwege mit nachgewiesener Abhängigkeit der Lücken")
print(f"{n_rechnung} Lösungen zweifach nachgerechnet; {n_fb} Fehlbilder")
fd = [(e["kennung"], e["aufgabe"]["o"]["index"] + 1, len(e["aufgabe"]["a"])) for l in aus.values() for e in l if e["form"] == "fehler_detektiv"]
verteilung = Counter(z for _, z, _ in fd)
print("Fehler-Detektiv: Fehlerzeile je Zeile", dict(sorted(verteilung.items())), "von", len(fd))
if fd and "--voll" in sys.argv:
    assert max(verteilung.values()) <= len(fd) // 3 + 1, "Fehlerzeile zu einseitig verteilt"
if "--ohne-c" in sys.argv:
    for x in ohne_c_liste:
        print("  ohne c:", x)
print("Stufen je Lernkarte:", dict(Counter(STUFEN.values())))
print("Themen geladen:", ", ".join(geladen))
print("OK")
