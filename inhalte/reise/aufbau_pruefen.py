"""Baut aufbau-vorschlag.json aus aufbau_daten.py und prüft den Vorschlag.
Aufruf (Repo-Wurzel):  python3 -I inhalte/reise/aufbau_pruefen.py
Ortsprüfung und Koordinaten brauchen: pip install geonamescache
Grundlagen: db_stand.json (DB, nur lesend), inhalte/themenliste.json + Themendateien (neue LK-D-Etappen),
inhalte/pruefung/lehrplan/lk_teilung_2211.json (Teilung), laender_geo.json (Natural Earth).
"""
import json, sys, unicodedata, pathlib, collections, math
HIER = pathlib.Path(__file__).resolve().parent
INHALTE = HIER.parent
REPO = INHALTE.parent
sys.path.insert(0, str(HIER))
from aufbau_daten import (KONTINENTE, BEGONNENE_ORTE, EXPEDITIONEN, REGIONEN, NACHBARSCHAFT, RESERVE,
                          RESERVE_STAEDTE, HAUPTSTADT_DE, HAUPTSTADT_SUCHE, HAUPTSTADT_HINWEIS, VORGEMERKT)

themen = {t["thema_id"]: t for t in json.load(open(INHALTE / "themenliste.json"))}
dbj = json.load(open(HIER / "db_stand.json"))
db = {int(k): v for k, v in dbj["thema_einheit_etappen"].items()}
db_lz = {int(k): v for k, v in dbj["thema_lernziele"].items()}
teilung = {t["thema"]: t for t in json.load(open(INHALTE / "pruefung/lehrplan/lk_teilung_2211.json"))["teilungsliste"]}
geo = json.load(open(HIER / "laender_geo.json"))
# Etappen laut Themendatei (enthält die neuen LK-D-Etappen, die noch nicht in der DB sind)
def datei_etappen(tid):
    d = json.load(open(REPO / themen[tid]["datei"]))
    return [e["lernziel"] for e in (d.get("etappen") or d["inhalt"]["etappen"])]
NEU_LKD = {"vektor_koordinaten", "vektor_drehen", "streckung_vektor", "vierecke_konstruieren", "drachen_raute", "wahre_groesse"}

def kl_key(t):
    k, r = t["klasse"], t["reihenfolge"]
    if k.get("gym_by"):
        return (0, k["gym_by"], r.get("gym_by") or 99, t["thema_id"])
    if k.get("rs_by"):
        return (1, k["rs_by"], r.get("rs_by") or 99, t["thema_id"])
    return (2, k.get("ib_myp") or 9, r.get("ib_myp") or 99, t["thema_id"])

def name(s): return s if isinstance(s, str) else s[0]
def such(s): return s if isinstance(s, str) else s[1]
def schluessel(k):
    if isinstance(k, int): return k, None
    a, b = k.split("-"); return int(a), int(b)

fehler, hinweise = [], []

# ---------- GeoNames ----------
try:
    import geonamescache
    gc = geonamescache.GeonamesCache(min_city_population=500)
    cities = gc.get_cities().values()
    countries = gc.get_countries()
    def norm(x): return "".join(c for c in unicodedata.normalize("NFKD", x.casefold()) if not unicodedata.combining(c)).replace("'", "").replace("’", "").replace("ʻ", "").replace("`", "").replace("‘", "")
    idx = collections.defaultdict(list)
    for c in cities:
        for n in {c["name"], *c.get("alternatenames", [])}:
            idx[norm(n)].append(c)
    def finde(stadt, iso, region):
        t = [c for c in idx.get(norm(such(stadt)), []) if c["countrycode"] == iso]
        if region: t = [c for c in t if c["admin1code"] in REGIONEN[region]["admin1"]]
        return max(t, key=lambda c: c["population"]) if t else None
except ImportError:
    geonamescache = None
    hinweise.append("geonamescache fehlt – Ortsprüfung und Koordinaten übersprungen")
    def finde(*a): return None

geo_ok, geo_offen = 0, []
def stadt_obj(s, iso, region, **extra):
    c = finde(s, iso, region)
    global geo_ok
    o = {"stadt": name(s)}
    o.update(extra)
    if c:
        geo_ok += 1
        o.update({"breite": round(c["latitude"], 5), "laenge": round(c["longitude"], 5), "geonames_id": c["geonameid"], "geonames_name": c["name"]})
    elif geonamescache:
        geo_offen.append(f"{name(s)} ({iso}{'/' + region if region else ''})")
    return o

def mitte(iso, region, staedte):
    if region:
        lt = geo["landesteile"].get(region)
        if lt: return {"breite": lt["mitte"][0], "laenge": lt["mitte"][1], "quelle": f"Natural Earth admin_1 ({lt['art']})"}
        pts = [s for s in staedte if "breite" in s]
        if pts:
            return {"breite": round(sum(p["breite"] for p in pts) / len(pts), 4), "laenge": round(sum(p["laenge"] for p in pts) / len(pts), 4),
                    "quelle": "Mittel der Städte (Natural Earth 1:50 m hat keinen Punkt für diesen Landesteil)"}
        return None
    l = geo["laender"][iso]
    return {"breite": l["mitte"][0], "laenge": l["mitte"][1], "quelle": "Natural Earth admin_0 Beschriftungspunkt"}

hauptstadt_cache, hs_abweichung = {}, []
def hauptstadt(iso):
    if iso in hauptstadt_cache: return hauptstadt_cache[iso]
    de = HAUPTSTADT_DE.get(iso)
    o = {"name": de}
    if not de: fehler.append(f"Hauptstadt (deutsch) fehlt für {iso}")
    if geonamescache:
        en = HAUPTSTADT_SUCHE.get(iso) or countries[iso]["capital"]
        c = finde(en, iso, None)
        if c:
            o.update({"breite": round(c["latitude"], 5), "laenge": round(c["longitude"], 5), "geonames_id": c["geonameid"], "geonames_name": c["name"]})
            namen = {norm(n) for n in {c["name"], *c.get("alternatenames", [])}}
            if de and norm(de) not in namen:
                hs_abweichung.append(f"{iso}: „{de}“ nicht unter den GeoNames-Namen von {c['name']}")
        else:
            fehler.append(f"Hauptstadt {iso} ({en}) nicht in GeoNames gefunden")
    if iso in HAUPTSTADT_HINWEIS: o["hinweis"] = HAUPTSTADT_HINWEIS[iso]
    hauptstadt_cache[iso] = o
    return o

def landesteil_hauptort(region):
    r = REGIONEN[region]; de, en = r["hauptort"]
    return de, en, r.get("hauptort_art", "Hauptstadt des Landesteils")

# ---------- bauen ----------
out = {"stand": "2026-11-22", "art": "Vorschlag – nicht umgesetzt (Reise-Aufbau 2)", "kontinente": [], "reserve": [], "expeditionen": [],
       "quellen": {"staedte": "GeoNames über geonamescache (CC BY 4.0)", "mitte": "Natural Earth 1:50 m (gemeinfrei)",
                   "stationen": "COMNAP Antarctic Facilities 2024 (frei für Bildung/nicht kommerziell)"}}
teile_gesehen = collections.defaultdict(list)
for k in KONTINENTE:
    fl = []
    for key in sorted(k["fluege"], key=lambda x: (kl_key(themen[schluessel(x)[0]]), schluessel(x)[1] or 0)):
        land, iso, region, st = k["fluege"][key]
        tid, teil = schluessel(key)
        t = themen[tid]
        alle = datei_etappen(tid)
        if teil:
            if tid not in teilung or teil > len(teilung[tid]["teile"]):
                fehler.append(f"Flug {key}: Teil {teil} steht nicht (mehr) in lk_teilung_2211.json"); continue
            tl = teilung[tid]["teile"][teil - 1]
            lz = [e["lernziel"] for e in tl["etappen"]]
            et_titel = {e["lernziel"]: e["titel"] for e in tl["etappen"]}
            teile_gesehen[tid].append((teil, lz))
            kopf = {"flug_id": key, "thema_id": tid, "teil": teil, "von": tl["von"], "thema": tl["titel"], "untertitel": tl["untertitel"],
                    "einheit_id": db[tid][0] if teil == 1 else None,
                    "einheit_hinweis": "bisherige Einheit" if teil == 1 else "neue Einheit kommt mit TL-S (bau-lehrer)",
                    "klasse": {"gym_by": tl["klasse"]["gym"], "rs_by_I": tl["klasse"]["rs_I"], "rs_by_II_III": tl["klasse"]["rs_II_III"], "ib_myp": tl["klasse"]["ib_standard"]}}
            if teil > 1: kopf["nachbarschaft"] = NACHBARSCHAFT.get(key) or fehler.append(f"Nachbarschaft fehlt für {key}")
        else:
            if tid in teilung:
                fehler.append(f"Thema {tid} ist laut lk_teilung_2211.json geteilt, im Vorschlag noch ein Flug")
            lz = alle
            et_titel = {}
            kopf = {"flug_id": str(tid), "thema_id": tid, "teil": None, "thema": t["titel"], "einheit_id": db[tid][0], "klasse": t["klasse"]}
            if len(st) != len(lz):
                fehler.append(f"Thema {tid} {land}: {len(st)} Städte, {len(lz)} Etappen (Themendatei)")
        if len(st) != len(lz):
            fehler.append(f"Flug {key} {land}: {len(st)} Städte, {len(lz)} Etappen")
        staedte = []
        for i, (s, l) in enumerate(zip(st, lz)):
            extra = {"etappe": i + 1, "lernziel": l}
            if l in et_titel: extra["etappe_titel"] = et_titel[l]
            if l in NEU_LKD:
                extra["neu_lkd"] = True
                if not teil: extra["kuer"] = True   # Vertiefung laut LK-D (bewertung.lernziele_vertiefung)
            if l not in db_lz[tid]: extra["noch_nicht_in_db"] = True
            staedte.append(stadt_obj(s, iso, region, **extra))
        f = dict(kopf, heute_ort=t["ort"], land=land, iso=iso, region=region, etappen=len(lz), kurzflug=len(lz) < 3)
        f["mitte"] = mitte(iso, region, staedte)
        if region:
            de, en, art = landesteil_hauptort(region)
            ho = stadt_obj((de, en), iso, region)
            f["hauptort_landesteil"] = dict(ho, art=art)
        f["hauptstadt"] = hauptstadt(iso)
        f["staedte"] = staedte
        fl.append(f)
    out["kontinente"].append({"kontinent_id": k["kontinent_id"], "themengebiet": k["themengebiet"], "reise": k["reise"], "fluege": fl})

for kid, liste in RESERVE.items():
    kont = next(k for k in KONTINENTE if k["kontinent_id"] == kid)
    rl = []
    for land, iso, region, st in liste:
        staedte = [stadt_obj(s, iso, region) for s in st]
        geo_ok -= sum(1 for s in staedte if "breite" in s)
        r = {"land": land, "iso": iso, "region": region, "staedte": staedte, "mitte": mitte(iso, region, staedte), "hauptstadt": hauptstadt(iso)}
        if region:
            de, en, art = landesteil_hauptort(region)
            r["hauptort_landesteil"] = dict(stadt_obj((de, en), iso, region), art=art)
        rl.append(r)
    out["reserve"].append({"kontinent_id": kid, "reise": kont["reise"], "laender": rl})
out["reserve_staedte_je_land"] = {}
for land, st in RESERVE_STAEDTE.items():
    f = next(f for k in out["kontinente"] for f in k["fluege"] if f["land"] == land)
    out["reserve_staedte_je_land"][land] = [stadt_obj(s, f["iso"], f["region"]) for s in st]
    geo_ok -= sum(1 for s in out["reserve_staedte_je_land"][land] if "breite" in s)
for s, (st, betr, br, la) in EXPEDITIONEN.items():
    out["expeditionen"].append({"expedition": s, "station": st, "betreiber": betr, "breite": br, "laenge": la})

# ---------- prüfen ----------
alle_fluege = [f for k in out["kontinente"] for f in k["fluege"]]
geteilt = set(teilung)
soll_fluege = len(db) + sum(len(teilung[t]["teile"]) - 1 for t in geteilt)
if len(alle_fluege) != soll_fluege: fehler.append(f"Flüge: {len(alle_fluege)} statt {soll_fluege}")
if {f["thema_id"] for f in alle_fluege} != set(db): fehler.append("Flüge passen nicht zu den freigegebenen Einheiten")
for tid in geteilt:
    if not teile_gesehen[tid]:
        fehler.append(f"Thema {tid} ist laut lk_teilung_2211.json geteilt ({len(teilung[tid]['teile'])} Teile), im Vorschlag aber nicht"
                      + (f" – vorgemerkt: {VORGEMERKT[tid]}" if tid in VORGEMERKT else " – kein Nachbarland vorgemerkt"))
        continue
    teile = sorted(teile_gesehen[tid])
    if [t for t, _ in teile] != list(range(1, len(teilung[tid]["teile"]) + 1)): fehler.append(f"Thema {tid}: Teile unvollständig")
    alle_lz = [l for _, lz in teile for l in lz]
    if len(alle_lz) != len(set(alle_lz)): fehler.append(f"Thema {tid}: Etappe in zwei Teilen")
    if sorted(alle_lz) != sorted(datei_etappen(tid)): fehler.append(f"Thema {tid}: Teile ≠ Etappen der Themendatei")
soll_staedte = sum(len(datei_etappen(t)) for t in db)
summe = sum(len(f["staedte"]) for f in alle_fluege)
if summe != soll_staedte: fehler.append(f"Städte gesamt {summe} statt {soll_staedte}")
landkey = collections.Counter((f["land"]) for f in alle_fluege)
for l, n in landkey.items():
    if n > 1: fehler.append(f"Land doppelt: {l} ({n}×)")
gebiet = collections.Counter((f["iso"], f["region"]) for f in alle_fluege)
for g, n in gebiet.items():
    if n > 1: fehler.append(f"Gebiet (ISO/Landesteil) doppelt: {g}")
staedte = collections.Counter(s["stadt"] for f in alle_fluege for s in f["staedte"])
for s, n in staedte.items():
    if n > 1: fehler.append(f"Stadt doppelt: {s} ({n}×)")
gid = collections.Counter(s.get("geonames_id") for f in alle_fluege for s in f["staedte"] if s.get("geonames_id"))
for g, n in gid.items():
    if n > 1: fehler.append(f"GeoNames-Ort doppelt belegt: {g}")
# Reserve: nichts doppelt mit der Belegung
res_laender = [r for k in out["reserve"] for r in k["laender"]]
for r in res_laender:
    if r["land"] in landkey or (r["iso"], r["region"]) in gebiet: fehler.append(f"Reserve-Land schon belegt: {r['land']}")
    for s in r["staedte"]:
        if s["stadt"] in staedte: fehler.append(f"Reserve-Stadt schon belegt: {s['stadt']}")
for k in out["reserve"]:
    if len(k["laender"]) < 3: hinweise.append(f"Reserve {k['reise']}: nur {len(k['laender'])} Länder")
    for r in k["laender"]:
        if not 6 <= len(r["staedte"]) <= 8: hinweise.append(f"Reserve {r['land']}: {len(r['staedte'])} Städte (Ziel 6–8)")
for land, st in out["reserve_staedte_je_land"].items():
    for s in st:
        if s["stadt"] in staedte: fehler.append(f"Reserve-Stadt {s['stadt']} ({land}) ist belegt")
for f in alle_fluege:
    if f["etappen"] > 14: hinweise.append(f"Flug {f['flug_id']} hat {f['etappen']} Etappen")
    if f["kurzflug"]: hinweise.append(f"Kurzflug {f['flug_id']} {f['land']}: {f['etappen']} Städte (erlaubt, Teilung 16:20 Punkt 3)")
    if not f["mitte"]: fehler.append(f"Mittelpunkt fehlt: {f['land']}")
for bid, (stadt, tid, grund) in BEGONNENE_ORTE.items():
    f = next(f for f in alle_fluege if f["thema_id"] == tid and f["teil"] in (None, 1))
    if stadt not in [s["stadt"] for s in f["staedte"]]:
        fehler.append(f"Begonnener Ort {stadt}: fehlt im Flug {tid} ({f['land']})")
if len({s for s, *_ in EXPEDITIONEN.values()}) != len(EXPEDITIONEN): fehler.append("Station doppelt")
for s, (st, b, br, la) in EXPEDITIONEN.items():
    if not (-90 <= br <= -60 and -180 <= la <= 180): fehler.append(f"Station {st}: Koordinaten nicht in der Antarktis")
# Nachbarteil: Entfernung erster Teil → neuer Teil (nächste Städte)
def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a["breite"], a["laenge"], b["breite"], b["laenge"]))
    return 6371 * 2 * math.asin(math.sqrt(math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2))
nachbar = []
for f in alle_fluege:
    if f["teil"] and f["teil"] > 1:
        f1 = next(g for g in alle_fluege if g["thema_id"] == f["thema_id"] and g["teil"] == 1)
        fv = next(g for g in alle_fluege if g["thema_id"] == f["thema_id"] and g["teil"] == f["teil"] - 1)
        try:
            d1 = min(km(a, b) for a in f1["staedte"] for b in f["staedte"])
            dv = min(km(a, b) for a in fv["staedte"] for b in f["staedte"])
            nachbar.append(f"{f['flug_id']}: {f1['land']} → {f['land']} (nächste Städte {d1:.0f} km; zum vorigen Teil {dv:.0f} km)")
        except KeyError:
            pass
lange = []
for f in alle_fluege:
    pts = [s for s in f["staedte"] if "breite" in s]
    for a, b in zip(pts, pts[1:]):
        d = km(a, b)
        if d > 700: lange.append(f"{a['stadt']} → {b['stadt']}: {d:.0f} km Luftlinie")
alle_staedte_geo = sum(len(f["staedte"]) for f in alle_fluege)
pruef = {"fluege": len(alle_fluege), "davon_neue_teile": len(alle_fluege) - len(db), "laender": len(landkey), "staedte": summe,
         "staedte_einmalig": len(staedte), "staedte_mit_koordinaten": sum(1 for f in alle_fluege for s in f["staedte"] if "breite" in s),
         "neue_etappen_noch_nicht_in_db": sum(1 for f in alle_fluege for s in f["staedte"] if s.get("noch_nicht_in_db")),
         "reserve_laender": {k["reise"]: len(k["laender"]) for k in out["reserve"]},
         "expeditionen": len(EXPEDITIONEN), "geonames_nicht_gefunden": geo_offen,
         "hauptstadt_name_nicht_in_geonames": hs_abweichung, "nachbarteile": nachbar,
         "lange_teilstrecken_ueber_700km": lange, "fehler": fehler, "hinweise": hinweise}
out["selbstpruefung"] = pruef
# ---------- Markdown-Tabellen (zwischen den AUTO-Markern in aufbau-vorschlag.md) ----------
def kl_text(f):
    k = f["klasse"]
    if f["teil"]:
        t = [f"Gym {k['gym_by']}" if k.get("gym_by") else None, f"RS {k['rs_by_I']}" if k.get("rs_by_I") else None]
    else:
        t = [f"Gym {k['gym_by']}" if k.get("gym_by") else None, f"RS {k['rs_by']}" if k.get("rs_by") else None,
             f"IB {k['ib_myp']}" if k.get("ib_myp") and not k.get("gym_by") and not k.get("rs_by") else None]
    return " · ".join(x for x in t if x)
def st_text(s):
    z = s["stadt"]
    if s.get("kuer"): z += " ★Kür"
    elif s.get("neu_lkd"): z += " (neu)"
    return z
md = []
for k in out["kontinente"]:
    n = sum(f["etappen"] for f in k["fluege"])
    md += [f"### {k['themengebiet']} → {k['reise']}  ({len(k['fluege'])} Flüge, {n} Etappen)", "",
           "| # | Flug | Kl. | heute | Land (ISO) · Hauptstadt | Etappen = Städte (Reihenfolge) |", "|---|---|---|---|---|---|"]
    for i, f in enumerate(k["fluege"], 1):
        titel = f["thema"] + (f" · {f['untertitel']}" if f.get("untertitel") else "")
        if f["teil"] and f["teil"] > 1: titel = "↪ " + titel
        hs = f["hauptort_landesteil"]["stadt"] + " (Landesteil)" if f.get("hauptort_landesteil") else f["hauptstadt"]["name"]
        md.append(f"| {i} | {titel} | {kl_text(f)} | {f['heute_ort']} | **{f['land']}** ({f['iso']}) · {hs} | {f['etappen']}: " + " → ".join(st_text(s) for s in f["staedte"]) + " |")
    md.append("")
md += ["### Reserve-Länder je Kontinent (frei für neue Themen und weitere Teilungen)", "", "| Kontinent | Land (ISO) · Hauptstadt | Städte |", "|---|---|---|"]
for k in out["reserve"]:
    for r in k["laender"]:
        hs = r["hauptort_landesteil"]["stadt"] + " (Landesteil)" if r.get("hauptort_landesteil") else r["hauptstadt"]["name"]
        md.append(f"| {k['reise'].split(' (')[0]} | {r['land']} ({r['iso']}) · {hs} | {len(r['staedte'])}: " + " → ".join(s["stadt"] for s in r["staedte"]) + " |")
md += ["", "Reserve-Städte, die durch die Teilung frei wurden: " + "; ".join(f"{l}: " + ", ".join(s["stadt"] for s in st) for l, st in out["reserve_staedte_je_land"].items()) + ".", ""]
md += ["### Antarktis → Expeditionen (je Expedition eine Forschungsstation, Koordinaten COMNAP 2024)", "", "| Expedition | Station | Betreiber | Breite | Länge |", "|---|---|---|---|---|"]
for e in out["expeditionen"]:
    md.append(f"| {e['expedition']} | {e['station']} | {e['betreiber']} | {e['breite']:.4f} | {e['laenge']:.4f} |")
mdp = HIER / "aufbau-vorschlag.md"
text = mdp.read_text()
a, b = "<!-- AUTO:START (aufbau_pruefen.py) -->", "<!-- AUTO:ENDE -->"
if a in text and b in text:
    mdp.write_text(text[:text.index(a) + len(a)] + "\n\n" + "\n".join(md) + "\n" + text[text.index(b):])
else:
    hinweise.append("AUTO-Marker in aufbau-vorschlag.md fehlen – Tabellen nicht geschrieben")

json.dump(out, open(HIER / "aufbau-vorschlag.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(pruef, ensure_ascii=False, indent=1))
sys.exit(1 if fehler or geo_offen else 0)
