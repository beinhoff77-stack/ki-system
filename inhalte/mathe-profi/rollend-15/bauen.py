"""Mathe-Profi, Auftrag „Vorrat neue Formen“ (Helfer Aufgaben), Runde rollend-15 (Klassen 7 und 9, dünn besetzte Einheiten auffüllen), Kürzel R15.

Aufruf: python3 -I inhalte/mathe-profi/rollend-15/bauen.py     (muss mit „OK“ enden)
Lädt th_<Thema>.py (je Thema eine Datei mit den Aufgaben), prüft alles, schreibt je Thema <Thema>.json sowie regeln.py und regeln-zuordnung.md.
Nur Inhalte. Nichts wird eingespielt.
"""
import difflib
import glob
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
import importlib.util as _iu     # noqa: E402
_sp = _iu.spec_from_file_location("vorrat_pruefen", os.path.join(os.path.abspath(os.path.join(HIER, "..", "..", "..")), "tools", "vorrat_pruefen.py"))
VP = _iu.module_from_spec(_sp)
_sp.loader.exec_module(VP)
from kern import A, FORM, ip, WURZEL, z2   # noqa: E402

KENN = json.load(open(os.path.join(HIER, "..", "regeln-uebersicht", "kennungen.json"), encoding="utf-8"))["kennungen"]
REGELN = {e["kennung"]: e for e in KENN}
FEHLBILD = {f["kennung"]: e["kennung"] for e in KENN for f in e["fehlbilder"]}

# Datei-Schlüssel (so heißt auch die Einheit) -> (Themen-Datei im Bestand, Lernkarten der Einheit in der Reihenfolge von rollend-einheiten.json)
_EINH = json.load(open(os.path.join(HIER, "..", "..", "plan", "rollend-einheiten.json"), encoding="utf-8"))["einheiten"]
AUSWAHL7 = ["bruch.prozent_grundwert", "terme.potenzgesetze_natuerlich", "terme.umformen", "abbildungen.kongruenz", "geometrie.winkelsaetze", "geometrie.konstruktion", "gleichungen.linear"]
AUSWAHL9 = ["zahlen.wurzeln_basis", "zahlen.reell", "gleichungen.quadratisch", "funktionen.quadratisch", "trigo.pythagoras", "trigo.rechtwinklig", "stochastik.verknuepft"]
THEMEN = {s: (s, list(_EINH[s]["lz"])) for s in AUSWAHL7 + AUSWAHL9}
KUERZEL = "R15"
KLASSE = {s: (7 if s in AUSWAHL7 else 9) for s in THEMEN}
REGEL_AUSNAHME = set()      # (Themen-Datei, Regel-Kennung): von Hand gelesene Ausnahmen der Themenliste des Katalogs (siehe regeln-zuordnung.md)
FEHLBILD_GELESEN = set()      # (Kennung der Aufgabe, Fehlbild-Kennung): keine Ausnahmen in dieser Runde
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


HOCH = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
HOCHLAUF = re.compile(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+")


def name_treffer(t, summen=frozenset({"8535e86c8118", "6a61eb7383e8", "ac818c81a10c"})):
    """Verbotene Vornamen nur über Prüfsummen (sha256, erste 12 Zeichen, kleingeschrieben) – wie in den früheren Runden, keine Namen im Klartext."""
    return {__import__("hashlib").sha256(w.lower().encode()).hexdigest()[:12] for w in re.findall(r"\w+", t)} & set(summen)


def zahlen_im(text):
    text = HOCHLAUF.sub(lambda m: " " + m.group(0).translate(HOCH) + " ", text)   # Hochzahlen zählen als Zahlen im Text
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
        return len(g["x"]) == len(g["y"]) == 2 and set(g) <= {"typ", "x", "y", "graphen", "kreise", "punkte", "schritt_x", "schritt_y", "name_x", "name_y", "strecken", "senkrecht", "waagrecht", "pfeile", "flaechen"}
    if g["typ"] == "figur":
        return set(g) <= {"typ", "punkte", "flaeche", "linien", "rechter_winkel", "winkel", "kreise"} and isinstance(g["punkte"], dict)
    if g["typ"] in ("saeulen", "kreisdiagramm"):
        return all(set(w) == {"name", "wert"} and len(w["name"]) <= 8 for w in g["werte"]) and (g["typ"] == "saeulen" or sum(w["wert"] for w in g["werte"]) == 100)
    return False


# ═════════ Bestand laden ═════════
ALLE_THEMEN = {}
for _p in sorted(glob.glob(os.path.join(WURZEL, "inhalte", "themen", "*.json"))):
    _d = json.load(open(_p, encoding="utf-8"))
    ALLE_THEMEN[_d["thema_schluessel"]] = _d
BESTAND = {datei: ALLE_THEMEN[datei] for datei, _ in THEMEN.values()}
KARTE = {}
for datei, d in BESTAND.items():
    for a in d["aufgaben"]:
        KARTE.setdefault((datei, a["l"]), a["t"])
GESAMT_TEXT = {a["f"].get("text", "") for d in ALLE_THEMEN.values() for a in d["aufgaben"]}
GESAMT_BAU = {bau_ohne_zahl(t) for t in GESAMT_TEXT}

ANDERE_TEXTE, ANDERE_BAU = set(), set()
for _p in glob.glob(os.path.join(WURZEL, "inhalte", "mathe-profi", "rollend-*", "*.json")):
    if "rollend-15" in _p:
        continue
    _d = json.load(open(_p, encoding="utf-8"))
    for _e in _d.get("aufgaben", []):
        if isinstance(_e, dict) and "aufgabe" in _e:
            _t = _e["aufgabe"]["f"].get("text", "")
            ANDERE_TEXTE.add(_t)
            ANDERE_BAU.add(bau_ohne_zahl(_t))


# ═════════ Doppelungsprüfung über Zahlen, Sollwert und Wortlaut ═════════
# Der Vergleich über den maskierten Fragetext (Bauplan) erkennt nur Aufgaben mit gleichem Wortlaut. Hier wird jede neue Aufgabe zusätzlich
# gegen ALLE Aufgaben derselben Einheit im Bestand (inhalte/themen/<datei>.json, das sind auch die Generator-Ausgaben) und gegen alle
# Aufgaben der früheren Runden (rollend-1 bis rollend-13) über Zahlenmenge, Sollwert und Wortlaut verglichen.
DP_STOP = set("wieviel viele welche welcher wird werden sind ist hat haben eine einen einem eines dann auch nicht noch sich oder aber nach beim vom zum zur dass dieser wenn immer jede jeder jedes".split())
DP_EINHEITHOCH = re.compile(r"(?<=[A-Za-zµ])[⁰¹²³⁴⁵⁶⁷⁸⁹]+")    # Hochzahl an einer Einheit (m², cm³) ist keine Zahl der Aufgabe
DP_ZEHNER = re.compile(r"10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]")
DP_PI_REST = F(14, 100)                                            # 3,14 ist vorgegeben und zählt nicht als gemeinsame Nachkommastellen


def dp_zahlen(t):
    t = HOCHLAUF.sub(lambda m: " " + m.group(0).translate(HOCH) + " ", DP_EINHEITHOCH.sub("", t))
    return {F(re.sub(r"[  ]", "", m).replace("−", "").replace("-", "").replace(",", ".")) for m in ZAHL.findall(t)}


def dp_merk(q):
    t = q["f"].get("text", "")
    o = q["o"]
    return dict(t=t, N=dp_zahlen(t), S=F(str(o["wert"])) if "wert" in o else None, M=bau_ohne_zahl(t),
                W={w for w in re.findall(r"[a-zäöüß]{4,}", t.lower())} - DP_STOP)


def dp_dez(S):
    """Nachkommaanteile der Dezimalzahlen (ohne den Rest von 3,14)"""
    return {n - (n.numerator // n.denominator) for n in S if n.denominator != 1} - {DP_PI_REST}


def dp_fein(x):
    return (x * 1000).denominator == 1 and (x * 100).denominator != 1


def dp_vergleich(a, b):
    """a: Aufgabe der Runde, b: Aufgabe aus dem Bestand (beide als dp_merk). Liefert den Grund der Ähnlichkeit oder None."""
    jac = lambda X, Y: len(X & Y) / max(1, len(X | Y))
    if not (a["N"] & b["N"]) and len(a["W"] & b["W"]) < 3 and a["M"] != b["M"] and not (dp_dez(a["N"]) & dp_dez(b["N"])):
        return None     # Vorfilter: keine gemeinsame Zahl, kaum gemeinsame Wörter
    sm = difflib.SequenceMatcher(None, a["M"], b["M"])
    ratio = sm.ratio() if (abs(len(a["M"]) - len(b["M"])) < 40 and sm.real_quick_ratio() >= .7 and sm.quick_ratio() >= .7) else 0
    ws, jn = jac(a["W"], b["W"]), jac(a["N"], b["N"])
    gleich = a["S"] is not None and a["S"] == b["S"]
    da, db = dp_dez(a["N"]), dp_dez(b["N"])
    if gleich and jn >= .99 and (len(a["N"]) >= 2 or (a["N"] and max(a["N"]) >= 50)):
        return "gleiche Zahlenmenge und gleicher Sollwert (ohne Maskierung der Zahlen verglichen)"
    if gleich and len(a["N"]) >= 2 and jn >= .75 and ws >= .2:
        return "gleiche Zahlen und gleicher Sollwert"
    if gleich and jn >= .99 and len(a["N"]) >= 3 and ws >= .15:
        return "dieselbe Zahlenmenge und gleicher Sollwert"
    if gleich and jn >= .5 and len(a["N"]) >= 4 and DP_ZEHNER.search(a["t"]) and DP_ZEHNER.search(b["t"]):
        return "Zehnerpotenzen mit fast denselben Zahlen und gleichem Sollwert"
    if ratio >= .9:
        return "fast gleicher Wortlaut"
    if jn >= .99 and len(a["N"]) >= 2 and ws >= .5:
        return "gleiche Zahlen im gleichen Sachverhalt"
    if jn >= .99 and ratio >= .8 and ws >= .25:
        return "gleiche Zahlen, fast gleicher Wortlaut"
    if gleich and (a["S"].denominator != 1 or a["S"] >= 10) and ws >= .3 and len(a["W"] & b["W"]) >= 4:
        return "gleicher Sollwert bei ähnlichem Sachverhalt"
    if da & db and ratio >= .7 and ws >= .4:
        return "gleicher Aufbau mit denselben Nachkommastellen"
    if len(da & db) >= 2 and any(dp_fein(x) for x in da & db):
        return "dieselben Nachkommastellen in mehreren Zahlen"
    return None


alle_sollwerte = {}
dp_treffer = []
# Doppelungsprüfung gegen den GESAMTEN Bestand (alle Themen-Dateien), nicht nur gegen die eigene Einheit
DP_BESTAND = {dat: [(f"{dat}:{i}", dp_merk(a)) for i, a in enumerate(d["aufgaben"]) if a["f"].get("text")] for dat, d in ALLE_THEMEN.items()}
DP_ALLE_BESTAND = [x for lst in DP_BESTAND.values() for x in lst]
DP_ANDERE = []
for _p in sorted(glob.glob(os.path.join(WURZEL, "inhalte", "mathe-profi", "rollend-*", "*.json"))):
    if "rollend-15" in _p:
        continue
    for _e in json.load(open(_p, encoding="utf-8")).get("aufgaben", []):
        if isinstance(_e, dict) and "aufgabe" in _e and _e["aufgabe"]["f"].get("text"):
            DP_ANDERE.append((os.path.basename(os.path.dirname(_p)) + ":" + str(_e.get("kennung", "")), dp_merk(_e["aufgabe"])))


# ═════════ Hilfen für Lücken und Fehlbilder ═════════
GGT = re.compile(r"ggT\(\s*(\(?-?\d+\)?)\s*,\s*(\(?-?\d+\)?)\s*\)")
PLATZ = re.compile(r"\{(\d+)\}")


def setze_ein(ausdruck, frueher):
    """{n} durch den Wert der n-ten Lücke (ab 1) ersetzen, ggT(a, b) ausrechnen. Gibt den fertigen Ausdruck zurück."""
    def ers(m):
        n = int(m.group(1))
        assert 1 <= n <= len(frueher), (ausdruck, "Verweis auf eine spätere oder fehlende Lücke", n)
        return f"({frueher[n - 1]})"
    t = PLATZ.sub(ers, ausdruck)
    return GGT.sub(lambda m: str(math.gcd(int(m.group(1).strip("()")), int(m.group(2).strip("()")))), t)


MATHENAMEN = re.compile(r"\b(sqrt|sin|cos|tan|asin|acos|atan|pi)\b")


def _wurzeln(t, quot=False):
    """wurzel(Ausdruck) -> ganze Zahl (nur bei vollständigen Quadraten), damit der Anker für tools/inhalt_pruefen.py lesbar bleibt."""
    while "wurzel(" in t:
        i = t.rindex("wurzel(")
        tiefe, j = 0, i + 6
        while True:
            tiefe += (t[j] == "(") - (t[j] == ")")
            if tiefe == 0:
                break
            j += 1
        inner = ip.rechne(t[i + 7:j])
        rn, rd_ = math.isqrt(inner.numerator), math.isqrt(inner.denominator)
        assert rn * rn == inner.numerator and rd_ * rd_ == inner.denominator, (t, "keine exakte Wurzel")
        r = F(rn, rd_)
        r = str(int(r)) if r.denominator == 1 else str(float(r))
        t = t[:i] + (f"(({t[i + 7:j]}) / {r})" if quot else str(r)) + t[j + 1:]
    return t


def wert_von_c(ausdruck, frueher):
    t = _wurzeln(setze_ein(str(ausdruck), frueher))
    if MATHENAMEN.search(t):                       # nur für Fehlbild-Rechnungen: Gleitkomma, Winkel in Grad
        v = float(kern.rechne_mathe(t))
        return v, t
    v = ip.rechne(t)
    return (int(v) if v.denominator == 1 else v), t


def verweise(ausdruck):
    return {int(n) for n in PLATZ.findall(str(ausdruck))}


def hang_ab(vorlage, soll, i, n):
    """Ändert sich der Wert der Lücke i (ab 0), wenn der frühere Wert n (ab 1) ein anderer wäre? (Abhängigkeit wirklich nötig)"""
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
    """Das Fehlbild nennt eine Rechnung: sie muss den falschen Wert wirklich ergeben. Rückgabe: True = nachgerechnet, False = keine Rechnung."""
    assert rechnung is not None, (kenn, ort, wert, "Fehlbild ohne Rechnung (4. Eintrag: Ausdruck, Funktion oder False)")
    if rechnung is False:
        return False
    if callable(rechnung):
        assert rechnung() is True, (kenn, ort, wert, "Fehlbild stimmt nicht")
        return True
    v, t = wert_von_c(rechnung, list(frueher))
    nd = max(2, len(str(wert).split(".")[1]) if "." in str(wert) else 0)
    ok = (not isinstance(v, float) and F(v) == ip.zahlwert(wert)) or round(float(v), nd) == float(wert)
    assert ok, (kenn, ort, "Fehlbild: Rechnung", t, "ergibt", float(v), "nicht", wert)
    return True


# ═════════ Prüfen ═════════
reihe = {schl: i for i, schl in enumerate(THEMEN)}
A.sort(key=lambda a: (reihe[a["thema"]], THEMEN[a["thema"]][1].index(a["lk"]), a["rang"]))   # rang: Kennungen bleiben stabil, auch wenn g nach der Tätigkeit gesetzt wird
aus = defaultdict(list)
n_rechnung = n_fb = n_grafik = n_fb_rechnung = n_fb_ohne = n_abhaengig = 0
alle_texte, alle_bau = set(), defaultdict(set)
zaehler = 0
GEZ_SET = set()
for a in A:
    assert a["thema"] in geladen and a["lk"] in THEMEN[a["thema"]][1], (a["thema"], a["lk"])
    datei = THEMEN[a["thema"]][0]
    q = a["aufgabe"]
    gleich_ok = bool(q.pop("_gleich_ok", False))
    zaehler += 1
    kenn = f"{KUERZEL}-V{zaehler:03d}"
    assert a["regel"] is None or a["regel"] in REGELN, (kenn, a["regel"])
    # Katalog (kennungen.json): die tragende Idee muss zum Thema passen (Ausnahmen von Hand gelesen); Kennung leer, wenn der Katalog nichts Passendes hat
    assert a["regel"] is None or datei in REGELN[a["regel"]]["themen"] or (datei, a["regel"]) in REGEL_AUSNAHME, (kenn, a["regel"], "Thema steht nicht in der Themenliste der Idee")
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
        assert not name_treffer(t), (kenn, "Name")
    assert text not in alle_texte and text not in GESAMT_TEXT and text not in ANDERE_TEXTE, (kenn, "Fragetext schon vorhanden")
    b = bau_ohne_zahl(text)
    assert b not in alle_bau[datei] and b not in GESAMT_BAU and b not in ANDERE_BAU, (kenn, "Fragetext nur mit anderen Zahlen schon vorhanden", b)
    if "grafik" in q["f"]:
        assert grafik_ok(q["f"]["grafik"]), (kenn, "grafik")
        n_grafik += 1
    dm = dp_merk(q)
    for dquelle, db_ in DP_ALLE_BESTAND + DP_ANDERE:
        grund = dp_vergleich(dm, db_)
        if grund:
            dp_treffer.append((kenn, grund, dquelle, db_["t"][:110]))
    sk = (datei, a["lk"], str(q["o"]["wert"]) if q["y"] == "zahl" else (q["a"][q["o"]["index"]] if q["y"] == "auswahl" else str(q["o"]["werte"])))
    assert sk not in alle_sollwerte, (kenn, "gleicher Sollwert in derselben Etappe wie", alle_sollwerte.get(sk))
    alle_sollwerte[sk] = kenn
    alle_texte.add(text)
    alle_bau[datei].add(b)
    eintrag = dict(kennung=kenn, thema=a["thema"], lernkarte=a["lk"], stufe=a["s"], typ=FORM[a["form"]][0], form=a["form"], antwortform=q["y"],
                   regel=a["regel"], regel_name=REGELN[a["regel"]]["name"] if a["regel"] else None, zaehlt=a["zaehlt"], fehlbilder=[])

    def fb_eintrag(ort, antwort, fbk, beschr):
        global n_fb
        assert fbk is None or fbk in FEHLBILD, (kenn, fbk, "Fehlbild-Kennung nicht im Katalog")
        assert fbk is None or datei in REGELN[FEHLBILD[fbk]]["themen"] or (kenn, fbk) in FEHLBILD_GELESEN, (kenn, fbk, "Fehlbild-Kennung: Thema nicht in der Themenliste, Katalogtext von Hand lesen und in FEHLBILD_GELESEN eintragen")
        assert beschr and len(beschr) > 5, (kenn, "Beschreibung des Fehlbilds")
        n_fb += 1
        eintrag["fehlbilder"].append(dict(**ort, antwort=antwort, fehlbild=fbk, regel_des_fehlbilds=FEHLBILD.get(fbk), beschreibung=beschr))

    if q["y"] == "zahl":
        q["c"] = _wurzeln(q["c"])
        soll = ip.rechne(q["c"])
        assert soll == ip.zahlwert(q["o"]["wert"]), (kenn, soll, q["o"]["wert"])
        zw = a["zweit"][0]
        if not isinstance(zw, str):
            GEZ_SET.add(kenn)
        zwv = z2(zw) if isinstance(zw, str) else F(str(zw))
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
            if fb_pruefen(kenn, "Zahl", w, rech):
                n_fb_rechnung += 1
            else:
                n_fb_ohne += 1
            fb_eintrag({}, w, fbk, beschr)
    elif q["y"] == "luecken":
        assert not KOMMA_LUECKE.search(text + " " + q["f"]["schablone"]), (kenn, "Lücke hinter dem Komma")
        assert not KOMMA_NEBEN.search(text + " " + q["f"]["schablone"]), (kenn, "Komma direkt neben einer Lücke")
        vorlagen = [str(c) for c in q["c"]]
        soll, c_fertig = [], []
        for v in vorlagen:
            wert_i, t = wert_von_c(v, soll)
            soll.append(wert_i)
            c_fertig.append(_wurzeln(PLATZ.sub(lambda m: f"({c_fertig[int(m.group(1)) - 1]})", v), quot=True))
        zw = [z2(z) if isinstance(z, str) else F(z) for z in a["zweit"]]
        assert soll == q["o"]["werte"] == zw, (kenn, soll, a["zweit"])
        assert not any(PLATZ.search(str(z)) for z in a["zweit"]), (kenn, "Zweitrechnung muss unabhängig sein")
        q["c"] = c_fertig
        assert all(isinstance(w, int) for w in q["o"]["werte"]) and q["f"]["schablone"].count("□") == len(soll), kenn
        im_text = zahlen_im(text + " " + q["f"]["schablone"] + " " + q["f"].get("hinweis", ""))
        im_tipp = zahlen_im(q["h"])
        for v in soll:
            alles_text = text + " " + q["f"]["schablone"] + " " + q["f"].get("hinweis", "") + " " + q["h"]
            assert not VP.wortfund(F(v), alles_text), (kenn, v, "Lückenwert als Zahlwort in Text oder Tipp", VP.wortfund(F(v), alles_text))
            assert abs(v) not in im_text, (kenn, v, "Lückenwert steht schon in Text, Schablone oder Hinweis")
            assert abs(v) not in im_tipp, (kenn, v, "Tipp verrät den Lückenwert")
        if len(soll) >= 2:
            refs = [verweise(v) for v in vorlagen]
            assert refs[-1], (kenn, "die letzte Lücke muss von einer früheren abhängen ({n} in c)")
            assert sum(1 for r in refs[1:] if r) >= 1, kenn
            for i, r in enumerate(refs):
                for n in r:
                    assert n <= i, (kenn, "Verweis nach vorn")
                    assert hang_ab(vorlagen[i], soll, i, n), (kenn, i + 1, n, "Lücke hängt in Wahrheit nicht vom früheren Wert ab")
            n_abhaengig += 1
        if a["form"] == "lueckenweg":
            assert len(soll) >= 2 and q["y"] == "luecken", (kenn, "Lückenweg: mindestens zwei Lücken")
            assert gleich_ok or len(set(soll)) == len(soll), (kenn, "Lückenwerte sollen verschieden sein")
        n_rechnung += len(soll)
        for i, liste in sorted(a["fb"].items()):
            werte = set()
            for t in liste:
                assert len(t) == 4, (kenn, i + 1, t[:1], "Fehlbild braucht 4 Einträge (Wert, Kennung, Beschreibung, Rechnung)")
                w, fbk, beschr, rech = t
                assert w != soll[i] and w not in werte, (kenn, i, w)
                werte.add(w)
                if fb_pruefen(kenn, f"Lücke {i + 1}", w, rech, soll[:i]):
                    n_fb_rechnung += 1
                else:
                    n_fb_ohne += 1
                fb_eintrag({"luecke": i + 1}, w, fbk, beschr)
    else:
        assert a["zweit"]() is True and len(set(q["a"])) == len(q["a"]) >= 3, kenn
        assert set(a["fb"]) == set(range(len(q["a"]))) - {q["o"]["index"]}, kenn
        n_rechnung += 1
        for i, (fbk, beschr) in sorted(a["fb"].items()):
            fb_eintrag({"index": i}, q["a"][i], fbk, beschr)
    eintrag["aufgabe"] = q
    aus[a["thema"]].append(eintrag)

# ═════════ Mischung je Einheit und Etappe ═════════
FORMEN_OK = ("umkehren", "zwei_wege", "bruecke", "anwenden", "fehler_detektiv", "verfahren_waehlen", "lueckenweg")
mix = []
for schl in geladen:
    xs_u = aus[schl]
    assert 12 <= len(xs_u) <= 18, (schl, "12 bis 18 Aufgaben je Einheit", len(xs_u))
    assert len({e["aufgabe"]["f"]["text"] for e in xs_u}) == len(xs_u), schl
    for lk in THEMEN[schl][1]:
        xs = [e for e in xs_u if e["lernkarte"] == lk]
        formen = Counter(e["form"] for e in xs)
        assert len(xs) >= 1, (schl, lk, "jede Etappe braucht mindestens eine Aufgabe")
        assert all(e["form"] in FORMEN_OK for e in xs), (schl, lk)
        assert any(e["zaehlt"] == "ja" and e["stufe"] >= 2 for e in xs), (schl, lk, "mindestens eine zählende Aufgabe auf Stufe 2 oder 3 je Etappe")
        assert formen["fehler_detektiv"] <= 1 and formen["lueckenweg"] <= 1, (schl, lk, "höchstens ein Fehler-Detektiv und ein Lückenweg je Etappe")
        assert max(formen.values()) <= 2, (schl, lk, "höchstens zwei Aufgaben derselben Form je Etappe", dict(formen))
        mix.append((schl, lk, formen))
    assert max(len([e for e in xs_u if e["lernkarte"] == lk]) for lk in THEMEN[schl][1]) - min(len([e for e in xs_u if e["lernkarte"] == lk]) for lk in THEMEN[schl][1]) <= 1 or len(THEMEN[schl][1]) >= 9, (schl, "gleichmäßig über die Etappen")
    assert sum(1 for e in xs_u if e["stufe"] == 3) >= max(2, len(THEMEN[schl][1]) // 2), (schl, "zu wenige Aufgaben auf Stufe 3")
    assert sum(1 for e in xs_u if e["form"] == "anwenden") >= 2, (schl, "mindestens zwei Sachaufgaben (anwenden) je Einheit")
lagen = defaultdict(list)
for a in A:
    if a["aufgabe"]["y"] == "auswahl" and a["form"] != "fehler_detektiv":
        lagen[len(a["aufgabe"]["a"])].append(a["aufgabe"]["o"]["index"])
assert set(lagen[3]) <= {0, 1, 2} and set(lagen[4]) <= {0, 1, 2, 3}, lagen
assert all(max(Counter(v).values()) <= len(v) // 2 + 1 for v in lagen.values() if len(v) >= 6), ("Lage der richtigen Antwort einseitig", {k: Counter(v) for k, v in lagen.items()})


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

# ═════════ Unabhängige Zählung: Aufgaben, deren Lösung auf Abzählen oder Suchen beruht, werden im Programm durch ein Modell (Ausprobieren, Aufzählen) nachgezählt ═════════
# Die Themen-Dateien übergeben dafür als zweite Rechnung (zweit) nicht einen Ausdruck, sondern das Ergebnis einer Zählschleife (Zahl, kein Text). bauen.py vergleicht es mit dem Sollwert.
GEZAEHLT = sorted(GEZ_SET)
print(len(GEZAEHLT), "Aufgaben mit unabhängiger Zählung (Zählschleife im Programm) bestätigt:", " ".join(k[4:] for k in sorted(GEZAEHLT)))
ZAEHL_PROBEN = 0

for _t in dp_treffer:
    print("DOPPELUNG", *_t)
assert not dp_treffer, "Doppelungen mit dem Bestand (siehe oben)"

# ═════════ Selbstprüfung mit Negativproben: die Prüfungen müssen kaputte Aufgaben wirklich ablehnen ═════════
def lehnt_ab(f, *args):
    try:
        f(*args)
    except (AssertionError, ZeroDivisionError, ValueError, SyntaxError, KeyError, TypeError):
        return True
    return False


n_neg = Counter()
hs = lambda w: __import__("hashlib").sha256(w.lower().encode()).hexdigest()[:12]
# 1. Namensprüfung über Prüfsumme: eine künstliche Prüfsumme (Fantasiewort) wird gefunden, neutrale Namen nicht
assert name_treffer("Heute spielt Zzprobewort mit Kim.", summen={hs("zzprobewort")}) == {hs("zzprobewort")}
assert not name_treffer("Heute spielt Alex mit Kim und Sam.", summen={hs("zzprobewort")})
n_neg["Namensprüfung (Prüfsumme findet, neutrale Namen nicht)"] += 2
# 2. Bauplan: gleiche Aufgabe mit anderen Zahlen wird als gleich erkannt, ein anderer Sachverhalt nicht
assert bau_ohne_zahl("Kim kauft 5 Äpfel für 3,20 €.") == bau_ohne_zahl("Kim kauft 7 Äpfel für 4,10 €.")
assert bau_ohne_zahl("Kim kauft 5 Äpfel für 3,20 €.") != bau_ohne_zahl("Kim kauft 5 Birnen für 3,20 €.")
n_neg["Bauplan (nur andere Zahlen = gleich)"] += 2
# 3. Ergebnis im Text: wird erkannt, auch mit Tausenderleerzeichen und Komma
assert F(42) in zahlen_im("Es sind 42 Stück.") and F(1350) in zahlen_im("Das sind 1 350 cm².") and F(5.5) in zahlen_im("Es sind 5,5 m.") and F(41) not in zahlen_im("Es sind 42 Stück.")
n_neg["Ergebnis steht im Text"] += 4
# 4. Eine Fehlbild-Rechnung, die den genannten Wert nicht ergibt, wird abgelehnt; eine richtige nicht
assert lehnt_ab(fb_pruefen, "N", "Zahl", 25, "6 * 4") and lehnt_ab(fb_pruefen, "N", "Zahl", 24.5, "6 * 4") and lehnt_ab(fb_pruefen, "N", "Zahl", 24, None)
assert fb_pruefen("N", "Zahl", 24, "6 * 4") is True
n_neg["Fehlbild-Rechnung stimmt nicht"] += 3
# 5. Zweitrechnung und Hauptrechnung: eine zweite Rechnung mit anderem Ergebnis wird erkannt
assert z2("6 * 7") == F(42) and z2("6 * 8") != F(42)
n_neg["Zweitrechnung"] += 1
# 6. Unzulässige Rechenausdrücke (len, range, Namen) werden vom Rechner abgelehnt
assert lehnt_ab(ip.rechne, "len([1, 2])") and lehnt_ab(ip.rechne, "__import__('os')") and lehnt_ab(ip.rechne, "1 / 0")
n_neg["Rechner lehnt unzulässige Ausdrücke ab"] += 3
# 7. Mutationen an allen echten Aufgaben mit Zahlantwort: falscher Sollwert, ein Fehlbild mit dem richtigen Wert, ein Fehlbild mit falscher Rechnung
for a in A:
    q = a["aufgabe"]
    if q["y"] != "zahl":
        continue
    soll = ip.rechne(q["c"])
    w = q["o"]["wert"]
    def sollwert_stimmt(wert):
        assert soll == ip.zahlwert(wert)
    assert not lehnt_ab(sollwert_stimmt, w) and lehnt_ab(sollwert_stimmt, float(w) + 1), (a["thema"], a["lk"])   # richtiger Sollwert besteht, um 1 verschoben fällt durch
    n_neg["Sollwert um 1 verschoben fällt auf"] += 1
    for (fw, fk, fb_text, rech) in a["fb"]:
        assert lehnt_ab(fb_pruefen, "N", "Zahl", float(fw) + 1, rech), (a["thema"], a["lk"], fw)      # Fehlwert um 1 verschoben: Rechnung passt nicht mehr
        assert fw != w                                                                                 # kein Fehlbild entspricht dem richtigen Wert
        n_neg["Fehlbild-Wert um 1 verschoben fällt auf"] += 1
        n_neg["Fehlbild ist nicht die richtige Antwort"] += 1
# 8. Doppelungsprüfung über Zahlen, Sollwert und Wortlaut: bekannte Aufgaben aus dem Bestand (jede 600. Bestandsaufgabe mit Zahlantwort) und aus früheren Runden, leicht umformuliert
#    (anderer Name, ein Wort ergänzt), müssen erkannt werden; Aufgaben mit anderem Sachverhalt und anderen Zahlen dürfen nicht anschlagen
n_neg["unabhängige Zählung"] += ZAEHL_PROBEN
proben = 0
bekannt = [(d_, a_) for d_, dd in ALLE_THEMEN.items() for a_ in dd["aufgaben"][::37] if a_["y"] == "zahl" and len(a_["f"].get("text", "")) > 60 and len(dp_zahlen(a_["f"]["text"])) >= 2][::9]
for d_, a_ in bekannt[:60]:
    m = dp_merk(dict(f={"text": a_["f"]["text"].replace("Kim", "Alex") + " Rechne genau."}, o=a_["o"]))
    assert any(dp_vergleich(m, b) for _, b in DP_BESTAND[d_]), ("leicht geänderte Bestandsaufgabe nicht erkannt", d_, a_["f"]["text"][:80])
    n_neg["Doppelung mit dem Bestand wird erkannt (leicht geänderter Text)"] += 1
for k_, b_ in DP_ANDERE[::40][:40]:
    m = dict(b_)
    m["t"] = m["t"] + " Bitte genau rechnen."
    assert dp_vergleich(m, b_), ("gleiche Aufgabe früherer Runde nicht erkannt", k_)
    n_neg["Doppelung mit früherer Runde wird erkannt"] += 1
for text, wert in [("Auf einem Flug von Dubai nach München dauert der Start 18 Minuten. Der Pilot meldet 2 Stunden und 40 Minuten bis zur Landung. Wie viele Minuten sind das zusammen?", 178),
                   ("Eine Kletterwand ist 7,5 m hoch. Ein Seil ist 3 m länger als die Wand. Wie lang ist das Seil?", 10.5)]:
    m = dp_merk({"f": {"text": text}, "o": {"wert": wert}})
    assert not any(dp_vergleich(m, b) for _, b in DP_ALLE_BESTAND + DP_ANDERE), ("falscher Alarm", text)
    n_neg["andere Aufgabe schlägt nicht an"] += 1
print()
print("Selbstprüfung mit Negativproben (jede Probe muss die Prüfung zum Anschlagen bringen):")
for k, v in n_neg.items():
    print(f"  {v:4}  {k}")
print(f"  gesamt {sum(n_neg.values())} Proben, alle bestanden")

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
    json.dump({"stand": "2026-11-28", "runde": "rollend-15", "kuerzel": KUERZEL, "flug": "r15-" + schl, "titel": schl, "fuer": f"Klasse {KLASSE[schl]}", "klasse": KLASSE[schl],
               "themen": [schl], "themen_datei_im_bestand": datei,
               "hinweis": "Aufgaben auf Vorrat in neuer Form (Feld form: " + ", ".join(FORM) + "), Auftrag Vorrat neue Formen. Nicht eingespielt. Je Eintrag: thema (Einheit), lernkarte, "
                          "typ (Name wie in tools/rollend_sql.py), form, zaehlt (ja/nein), Regel-Kennung, Fehlbilder und unter „aufgabe“ die Aufgabe im Format von inhalte/README.md.",
               "aufgaben": liste}, open(os.path.join(HIER, f"{schl}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{schl:30} {len(lks):10} {len(liste):9}  " + "/".join(str(c[f]) for f in FORM and KURZ) + f"   {z['ja']}/{z['nein']}")
print()
print("Summe Lernkarten", sum(len(THEMEN[s][1]) for s in geladen), "Aufgaben", len(A), "| Formen", dict(gesamt_f), "| zaehlt", dict(gesamt_z))
print(f"{n_fb_rechnung} Fehlbilder mit Rechnung nachgerechnet, {n_fb_ohne} ohne Rechnung (Wert oder Auswahl); {n_abhaengig} Lückenaufgaben mit nachgewiesener Abhängigkeit der Lücken")
print(f"{n_rechnung} Lösungen zweifach nachgerechnet; {n_fb} Fehlbilder, davon {sum(1 for fl in aus.values() for e in fl for x in e['fehlbilder'] if x['fehlbild'])} mit Kennung; {n_grafik} Aufgaben mit Zeichnung")
fd = [(e["kennung"], e["aufgabe"]["o"]["index"] + 1, len(e["aufgabe"]["a"])) for l in aus.values() for e in l if e["form"] == "fehler_detektiv"]
verteilung = Counter(z for _, z, _ in fd)
assert all("In welcher Zeile passiert der erste Fehler?" in e["aufgabe"]["f"]["text"] or "Welche Zeile ist falsch?" in e["aufgabe"]["f"]["text"] for l in aus.values() for e in l if e["form"] == "fehler_detektiv")
print("Fehler-Detektiv: Fehlerzeile je Zeile", dict(sorted(verteilung.items())), "von", len(fd))
if fd:
    assert max(verteilung.values()) <= len(fd) // 3 + 1, "Fehlerzeile zu einseitig verteilt"
print("Regel-Kennung:", sum(1 for l in aus.values() for e in l if e["regel"]), "Aufgaben mit,", sum(1 for l in aus.values() for e in l if not e["regel"]), "ohne Regel (regeln.py)")

# ═════════ regeln.py und regeln-zuordnung.md (Regel-Kennung je Aufgabe) ═════════
_zeilen = []
for a in A:
    pass
_info = {id(a["aufgabe"]): a for a in A}
ZEILEN = []
for schl in geladen:
    for e in aus[schl]:
        a = next(x for x in A if x["aufgabe"] is e["aufgabe"])
        ZEILEN.append((e["kennung"], e["thema"], e["lernkarte"], e["regel"], a["zweifel"] or "", a["ohne"] or ""))
with open(os.path.join(HIER, "regeln.py"), "w", encoding="utf-8") as f_:
    f_.write('"""Runde 15: Regel-Kennung je Aufgabe (erzeugt von bauen.py aus den Angaben regel / ohne / zweifel in th_*.py; nicht von Hand ändern).\n'
             'ZUORDNUNG: (Kennung, Thema, Lernkarte, Regel oder None, Zweifel, Begründung bei keiner Regel). Tabelle: regeln-zuordnung.md."""\nZUORDNUNG = [\n')
    for z in ZEILEN:
        f_.write("    " + repr(z) + ",\n")
    f_.write("]\n")
verteilung_r = Counter(z[3] for z in ZEILEN)
with open(os.path.join(HIER, "regeln-zuordnung.md"), "w", encoding="utf-8") as f_:
    f_.write("# Runde 15: Regel-Kennung je Aufgabe (Selbstkontrolle der Zuordnung)\n\n")
    f_.write("Maßstab: die Regel, die das Kind zum Lösen braucht (tragender Lösungsschritt), nicht das Thema. Jede Kennung wurde gegen `inhalte/mathe-profi/regeln-uebersicht/kennungen.json` gelesen; "
             "`bauen.py` prüft, dass sie im Katalog steht und das Thema in der Themenliste der Regel steht (Ausnahmen unten). Quelle der Daten: die Angaben `regel` / `ohne` / `zweifel` in `th_*.py`; "
             "`regeln.py` und diese Tabelle werden von `bauen.py` erzeugt.\n\n")
    f_.write(f"**{sum(1 for z in ZEILEN if z[3])} Aufgaben mit Regel, {sum(1 for z in ZEILEN if not z[3])} ohne.**\n\n## Verteilung\n\n| Regel | Name | Aufgaben |\n|---|---|---|\n")
    for r_, n_ in sorted(verteilung_r.items(), key=lambda x: (x[0] is None, -x[1], str(x[0]))):
        f_.write(f"| {'`' + r_ + '`' if r_ else '– (ohne Regel)'} | {REGELN[r_]['name'] if r_ else ''} | {n_} |\n")
    f_.write("\n## Ausnahmen von der Themenliste des Katalogs (von Hand gelesen)\n\n")
    for dd, rr in sorted(REGEL_AUSNAHME):
        f_.write(f"- `{dd}` mit `{rr}`: " + ", ".join(z[0][4:] for z in ZEILEN if z[3] == rr and THEMEN[z[1]][0] == dd) + "\n")
    f_.write("\n## Aufgaben ohne Regel (mit Begründung)\n\n| Aufgabe | Einheit.Lernkarte | Begründung |\n|---|---|---|\n")
    for z in ZEILEN:
        if not z[3]:
            f_.write(f"| {z[0]} | {z[1]}.{z[2]} | {z[5]} |\n")
    f_.write("\n## Zweifelsfälle\n\n| Aufgabe | Einheit.Lernkarte | gewählt | Bemerkung |\n|---|---|---|---|\n")
    for z in ZEILEN:
        if z[4]:
            f_.write(f"| {z[0]} | {z[1]}.{z[2]} | `{z[3]}` | {z[4]} |\n" if z[3] else f"| {z[0]} | {z[1]}.{z[2]} | – | {z[4]} |\n")
    f_.write("\n## Alle Aufgaben\n\n| Aufgabe | Einheit.Lernkarte | Regel |\n|---|---|---|\n")
    for z in ZEILEN:
        f_.write(f"| {z[0]} | {z[1]}.{z[2]} | {'`' + z[3] + '`' if z[3] else '–'} |\n")

print("Themen geladen:", ", ".join(geladen))
print("Stufen:", dict(sorted(Counter(e["stufe"] for l in aus.values() for e in l).items())))

# ═════════ zusätzlich tools/vorrat_pruefen.py über die eigenen Dateien ═════════
VPSKRIPT = r"""
import importlib.util, sys, glob, os
spec = importlib.util.spec_from_file_location("vp", sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.DATEIEN = sorted(glob.glob(os.path.join(sys.argv[2], "*.json")))
sys.argv = ["vp"]
sys.exit(m.main())
"""
r = subprocess.run([sys.executable, "-I", "-c", VPSKRIPT, os.path.join(WURZEL, "tools", "vorrat_pruefen.py"), HIER], capture_output=True, text=True, cwd=WURZEL)
print("tools/vorrat_pruefen.py über rollend-15:")
print(r.stdout[-3000:] + r.stderr[-1000:])
print("OK")
