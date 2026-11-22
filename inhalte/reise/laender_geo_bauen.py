"""Baut laender_geo.json: Mittelpunkt (Beschriftungspunkt) und deutscher Name je Land/Landesteil aus Natural Earth.
Nur einmal nötig, wenn Länder dazukommen. Natural Earth ist gemeinfrei.
Aufruf (Repo-Wurzel):
  python3 -I inhalte/reise/laender_geo_bauen.py <ne_50m_admin_0_countries.geojson> <ne_50m_admin_1_states_provinces.geojson>
Quelle: https://github.com/nvkelso/natural-earth-vector (geojson/), Natural Earth 1:50 m, Version im Repo-Stand Nov. 2026.
"""
import json, sys, pathlib
HIER = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
from aufbau_daten import KONTINENTE, RESERVE, REGIONEN

adm0 = json.load(open(sys.argv[1]))["features"]
adm1 = json.load(open(sys.argv[2]))["features"]

def iso_von(p):
    for k in ("ISO_A2", "ISO_A2_EH"):
        if p.get(k) and p[k] != "-99":
            return p[k]
    return None

laender = {}
for f in adm0:
    p = f["properties"]
    iso = iso_von(p)
    if iso and iso not in laender:
        laender[iso] = {"name_de_ne": p.get("NAME_DE"), "mitte": [round(p["LABEL_Y"], 4), round(p["LABEL_X"], 4)]}
a1 = {f["properties"]["iso_3166_2"]: f["properties"] for f in adm1}

gebraucht = {iso for k in KONTINENTE for (_, iso, _, _) in k["fluege"].values()}
gebraucht |= {iso for r in RESERVE.values() for (_, iso, _, _) in r}
out = {"quelle": "Natural Earth 1:50 m (gemeinfrei): admin_0 LABEL_Y/LABEL_X, admin_1 latitude/longitude", "laender": {}, "landesteile": {}, "fehlt": []}
for iso in sorted(gebraucht):
    if iso in laender:
        out["laender"][iso] = laender[iso]
    else:
        out["fehlt"].append(iso)
for reg, r in REGIONEN.items():
    pts = [a1[c] for c in r["ne"] if c in a1]
    if r["ne"] and len(pts) == len(r["ne"]):
        out["landesteile"][reg] = {"mitte": [round(sum(p["latitude"] for p in pts) / len(pts), 4),
                                             round(sum(p["longitude"] for p in pts) / len(pts), 4)],
                                   "art": "Natural-Earth-Punkt" if len(pts) == 1 else f"Mittel aus {len(pts)} Bundesstaaten"}
    elif r["ne"]:
        out["fehlt"].append(reg)
json.dump(out, open(HIER / "laender_geo.json", "w"), ensure_ascii=False, indent=1)
print("Länder:", len(out["laender"]), "Landesteile:", len(out["landesteile"]), "fehlt:", out["fehlt"])
