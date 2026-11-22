"""Baut aufbau-vorschlag.json / .md aus aufbau_daten.py und prüft den Vorschlag.
Aufruf (Repo-Wurzel):  python3 -I inhalte/reise/aufbau_pruefen.py
Ortsprüfung braucht: pip install geonamescache
"""
import json, sys, unicodedata, pathlib, collections
HIER = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
from aufbau_daten import KONTINENTE, BEGONNENE_ORTE, EXPEDITIONEN

themen = {t["thema_id"]: t for t in json.load(open(HIER.parent / "themenliste.json"))}
db = {int(k): v for k, v in json.load(open(HIER / "db_stand.json"))["thema_einheit_etappen"].items()}

def kl_key(t):
    k, r = t["klasse"], t["reihenfolge"]
    if k.get("gym_by"):
        return (0, k["gym_by"], r.get("gym_by") or 99, t["thema_id"])
    if k.get("rs_by"):
        return (1, k["rs_by"], r.get("rs_by") or 99, t["thema_id"])
    return (2, k.get("ib_myp") or 9, r.get("ib_myp") or 99, t["thema_id"])

def name(s): return s if isinstance(s, str) else s[0]
def such(s): return s if isinstance(s, str) else s[1]

# ---------- bauen ----------
out = {"stand": "2026-11-22", "art": "Vorschlag – nicht umgesetzt", "kontinente": [], "expeditionen": []}
for k in KONTINENTE:
    fl = []
    for tid in sorted(k["fluege"], key=lambda i: kl_key(themen[i])):
        land, iso, region, st = k["fluege"][tid]
        t = themen[tid]
        fl.append({"thema_id": tid, "einheit_id": db[tid][0], "thema": t["titel"],
                   "klasse": t["klasse"], "heute_ort": t["ort"], "land": land, "iso": iso,
                   "region": region, "etappen": db[tid][1],
                   "staedte": [{"etappe": i + 1, "stadt": name(s)} for i, s in enumerate(st)]})
    out["kontinente"].append({"kontinent_id": k["kontinent_id"], "themengebiet": k["themengebiet"],
                              "reise": k["reise"], "fluege": fl})
for s, (st, betr) in EXPEDITIONEN.items():
    out["expeditionen"].append({"expedition": s, "station": st, "betreiber": betr})

# ---------- prüfen ----------
fehler, hinweise = [], []
alle_fluege = [f for k in out["kontinente"] for f in k["fluege"]]
if len(alle_fluege) != 87: fehler.append(f"Flüge: {len(alle_fluege)} statt 87")
if set(f["thema_id"] for f in alle_fluege) != set(db): fehler.append("Flüge passen nicht zu den freigegebenen Einheiten")
summe = sum(len(f["staedte"]) for f in alle_fluege)
if summe != 606: fehler.append(f"Städte gesamt {summe} statt 606")
laender = collections.Counter((f["land"]) for f in alle_fluege)
for l, n in laender.items():
    if n > 1: fehler.append(f"Land doppelt: {l} ({n}×)")
staedte = collections.Counter(s["stadt"] for f in alle_fluege for s in f["staedte"])
for s, n in staedte.items():
    if n > 1: fehler.append(f"Stadt doppelt: {s} ({n}×)")
for f in alle_fluege:
    if len(f["staedte"]) != f["etappen"]:
        fehler.append(f"Thema {f['thema_id']} {f['land']}: {len(f['staedte'])} Städte, {f['etappen']} Etappen")
    if not 3 <= f["etappen"] <= 12:
        hinweise.append(f"Thema {f['thema_id']} ({f['thema']}) hat {f['etappen']} Etappen – außerhalb 3–12; Land mit genug Städten gewählt ({f['land']})")
# begonnene Orte: heutige Stadt bleibt im Flug, der das Land behält
for bid, (stadt, tid, grund) in BEGONNENE_ORTE.items():
    f = next(f for f in alle_fluege if f["thema_id"] == tid)
    if stadt not in [s["stadt"] for s in f["staedte"]]:
        fehler.append(f"Begonnener Ort {stadt}: fehlt im Flug {tid} ({f['land']})")
if len(set(s for s, _ in EXPEDITIONEN.values())) != len(EXPEDITIONEN): fehler.append("Station doppelt")

# Stadt liegt im Land (GeoNames, Orte ab 500 Einwohnern)
geo_ok, geo_offen, koord, lange = 0, [], {}, []
try:
    import geonamescache
    cities = geonamescache.GeonamesCache(min_city_population=500).get_cities().values()
    def norm(x): return "".join(c for c in unicodedata.normalize("NFKD", x.casefold()) if not unicodedata.combining(c)).replace("'", "").replace("’", "").replace("ʻ", "").replace("`", "").replace("‘", "")
    idx = collections.defaultdict(list)
    for c in cities:
        for n in {c["name"], *c.get("alternatenames", [])}:
            idx[norm(n)].append(c)
    NZ = {"NORD": {"E7", "E8", "F1", "F2", "F3", "F6", "F9", "G1", "G2"}, "SUED": {"E9", "F4", "F5", "F7", "F8", "G3", "G4"}}
    roh = {k: v for kk in KONTINENTE for k, v in kk["fluege"].items()}
    for f in alle_fluege:
        for s in roh[f["thema_id"]][3]:
            treffer = [c for c in idx.get(norm(such(s)), []) if c["countrycode"] == f["iso"]]
            if f["region"] in NZ: treffer = [c for c in treffer if c["admin1code"] in NZ[f["region"]]]
            elif f["region"]: treffer = [c for c in treffer if c["admin1code"] == f["region"]]
            if treffer:
                geo_ok += 1
                best = max(treffer, key=lambda c: c["population"])
                koord.setdefault(f["thema_id"], []).append((name(s), best["latitude"], best["longitude"]))
            else: geo_offen.append(f"{name(s)} ({f['land']})")
except ImportError:
    hinweise.append("geonamescache fehlt – Ortsprüfung übersprungen")

import math
def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[1], a[2], b[1], b[2]))
    return 6371 * 2 * math.asin(math.sqrt(math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2))
for tid, pts in koord.items():
    for a, b in zip(pts, pts[1:]):
        d = km(a, b)
        if d > 700: lange.append(f"{a[0]} → {b[0]}: {d:.0f} km Luftlinie")
pruef = {"fluege": len(alle_fluege), "laender": len(laender), "staedte": summe,
         "staedte_einmalig": len(staedte), "expeditionen": len(EXPEDITIONEN),
         "geonames_bestaetigt": geo_ok, "geonames_nicht_gefunden": geo_offen, "lange_teilstrecken_ueber_700km": lange,
         "fehler": fehler, "hinweise": hinweise}
out["selbstpruefung"] = pruef
json.dump(out, open(HIER / "aufbau-vorschlag.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(pruef, ensure_ascii=False, indent=1))
sys.exit(1 if fehler else 0)
