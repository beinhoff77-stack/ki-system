"""Baut die JSON-Dateien der Runde vtest-3 aus den e_*.py. Aufruf: python3 -I inhalte/mathe-profi/vtest-3/bauen.py"""
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
import kern  # noqa: E402
import ideen  # noqa: E402

DATEIEN = ["e_volumen", "e_darstellen", "e_kennwerte", "e_grundbegriffe", "e_winkel"]
KOPF = {"stand": kern.STAND, "runde": "vtest-3", "kuerzel": "VT3", "klasse": None,
        "hinweis": "Verstehen in Tests, Stufe 1, Runde 3. Nicht eingespielt."}
KLASSE = {"messen.volumen": 6, "daten.darstellen": 6, "daten.kennwerte": 6, "funktionen.grundbegriffe": 8, "geometrie.winkel": 5}

baus = []
for d in DATEIEN:
    p = HIER / f"{d}.py"
    if not p.exists():
        continue
    spec = importlib.util.spec_from_file_location(d, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    baus.append(m.B)
out = kern.zusammen(baus)
n = 0
for thema, liste in out.items():
    for a in liste:
        a["idee"] = ideen.IDEE[a["kennung"]]
    kopf = dict(KOPF, titel=thema, klasse=KLASSE[thema], themen=[thema])
    (HIER / f"{thema}.json").write_text(json.dumps({**kopf, "aufgaben": liste}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    n += len(liste)
    print(thema, len(liste))
print("zusammen", n)
