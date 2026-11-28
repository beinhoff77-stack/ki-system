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

# ---------- feste Prüfungen des Bauskripts (Vorprüfungs-Lehren) ----------
fehler = []
alle = []
for thema in out:
    alle += out[thema]
# 1. Denkfiguren je Lernziel: mindestens 5 verschiedene Kategorien, keine mehr als zweimal
je_lz = {}
for a in alle:
    je_lz.setdefault((a["thema"], a["lernkarte"]), []).append(a["idee"].split("|")[0])
for lz, kat in je_lz.items():
    z = {k: kat.count(k) for k in set(kat)}
    if len(z) < 5: fehler.append(f"{lz}: nur {len(z)} Denkfiguren")
    if max(z.values()) > 2: fehler.append(f"{lz}: Denkfigur mehr als zweimal: {z}")
# 2. Auswahl: vier Optionen, richtige Option nicht (zu oft) die längste, Position gleichmäßig, nie zweimal hintereinander gleich
aus = [a for a in alle if a["aufgabe"]["y"] == "auswahl"]
laengste = 0
plaetze = [0, 0, 0, 0]
for a in aus:
    opts = a["aufgabe"]["a"]
    i = a["aufgabe"]["o"]["index"]
    if len(opts) != 4: fehler.append(f"{a['kennung']}: nicht vier Optionen")
    if len(opts[i]) == max(len(t) for t in opts): laengste += 1
    plaetze[i] += 1
if laengste > 0.35 * len(aus): fehler.append(f"richtige Option ist in {laengste} von {len(aus)} Fällen die längste (mehr als 35 %)")
if max(plaetze) - min(plaetze) > 2 and max(plaetze) > 0.32 * len(aus): fehler.append(f"Positionen ungleich verteilt: {plaetze}")
for lz, kat in je_lz.items():
    folge = [a["aufgabe"]["o"]["index"] for a in alle if (a["thema"], a["lernkarte"]) == lz and a["aufgabe"]["y"] == "auswahl"]
    if any(x == y for x, y in zip(folge, folge[1:])): fehler.append(f"{lz}: richtige Position zweimal hintereinander {folge}")
print(f"Auswahl: {len(aus)} Aufgaben, richtige Option längste in {laengste} ({100 * laengste / len(aus):.0f} %), Plätze {plaetze}")
# 2b. Jede Lücke hat mindestens ein eigenes Fehlbild (Urteil 1222)
for a in alle:
    if a["aufgabe"]["y"] == "luecken":
        n = len(a["aufgabe"]["o"]["werte"])
        have = {f["luecke"] for f in a.get("fehlbilder", [])}
        for i in range(1, n + 1):
            if i not in have: fehler.append(f"{a['kennung']}: Lücke {i} hat kein Fehlbild")
# 3. Auswahl-Bauweise (Vorprüfung 2): alle Optionen einer Aufgabe gleich gebaut, keine Sammel-/Absolut-/Gleichheitszeichen-Verzerrung, keine Zahlenfolge der Plätze
import re  # noqa: E402
def _dw(t): return bool(re.search(r"\b(denn|weil)\b", t))
rr = [0, 0]; ww = [0, 0]; eq = [0, 0]; sam = [0, 0]; ab = [0, 0]; he = [0, 0]; ne = [0, 0]
for a in aus:
    opts = a["aufgabe"]["a"]; i = a["aufgabe"]["o"]["index"]
    if len({_dw(t) for t in opts}) > 1: fehler.append(f"{a['kennung']}: Optionen ungleich gebaut (denn/weil nur bei einem Teil)")
    for k, t in enumerate(opts):
        r = 0 if k == i else 1
        (rr if r == 0 else ww)[0] += 1
        eq[r] += "=" in t
        sam[r] += bool(re.match(r"(Beide|Kein|Keine|Alle)\b", t))
        ab[r] += bool(re.search(r"\b(immer|nie|niemals|alle|stets)\b", t, re.I))
        he[r] += bool(re.search(r"\b(höchstens|mindestens|wenigstens)\b", t, re.I))   # Abschwächung (Vorprüfung 3, B6)
        ne[r] += bool(re.search(r"\b(nicht|kein|keine|keiner|keinen|nie|niemals)\b", t, re.I))            # Verneinung (Vorprüfung 3, B6)
nr, nw = rr[0], ww[0]
if abs(eq[0] / nr - eq[1] / nw) > 0.10: fehler.append(f"„=“ in {eq[0]}/{nr} richtigen, {eq[1]}/{nw} falschen Optionen (Unterschied über 10 Prozentpunkte)")
if abs(sam[0] / nr - sam[1] / nw) > 0.10: fehler.append(f"Sammel-Optionen verzerrt: richtig {sam[0]}/{nr}, falsch {sam[1]}/{nw}")
if abs(ab[0] / nr - ab[1] / nw) > 0.10: fehler.append(f"Absolutwörter verzerrt: richtig {ab[0]}/{nr}, falsch {ab[1]}/{nw}")
if abs(he[0] / nr - he[1] / nw) > 0.05: fehler.append(f"„höchstens/mindestens“ verzerrt: richtig {he[0]}/{nr}, falsch {he[1]}/{nw} (Unterschied über 5 Prozentpunkte)")
if abs(ne[0] / nr - ne[1] / nw) > 0.10: fehler.append(f"Verneinung verzerrt: richtig {ne[0]}/{nr}, falsch {ne[1]}/{nw} (Unterschied über 10 Prozentpunkte)")
folge_alle = [a["aufgabe"]["o"]["index"] for a in aus]
for j in range(len(folge_alle) - 4):
    d = [(folge_alle[j + k + 1] - folge_alle[j + k]) % 4 for k in range(4)]
    if len(set(d)) == 1 and d[0] != 0: fehler.append(f"Plätze folgen über 5 Aufgaben einer Zahlenfolge ab Position {j}")
print(f"Auswahl-Bauweise: „=“ richtig {eq[0]}/{nr}, falsch {eq[1]}/{nw}; Sammel richtig {sam[0]}/{nr}, falsch {sam[1]}/{nw}; Absolutwörter richtig {ab[0]}/{nr}, falsch {ab[1]}/{nw}; Abschwächung richtig {he[0]}/{nr}, falsch {he[1]}/{nw}; Verneinung richtig {ne[0]}/{nr}, falsch {ne[1]}/{nw}")
if fehler:
    print("FESTE PRÜFUNG FEHLGESCHLAGEN:")
    for f in fehler: print("  ", f)
    sys.exit(1)
