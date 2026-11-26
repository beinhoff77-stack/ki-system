"""Mathe-Profi, Auftrag 14 Teil B: die 78 Aufgaben aus Schritt 1 von den alten 15 Etikett-Nummern auf die stabilen Kennungen umhängen.

Aufruf: python3 -I inhalte/mathe-profi/schritt1/umhaengen.py
Liest etiketten.json und regeln-uebersicht/kennungen.json, schreibt kennungen-zuordnung.json.
etiketten.json bleibt unverändert (alter Stand zum Vergleich). Wo nichts passt, steht null und ein Grund – nichts wird passend gemacht.
"""
import collections
import json
import os

HIER = os.path.dirname(os.path.abspath(__file__))
K = json.load(open(os.path.join(HIER, "..", "regeln-uebersicht", "kennungen.json"), encoding="utf-8"))
VON_ETIKETT = {e["etikett_alt"]: e["kennung"] for e in K["kennungen"] if e["etikett_alt"]}
NAME = {e["kennung"]: e["name"] for e in K["kennungen"]}
assert len(VON_ETIKETT) == 14 and 9 not in VON_ETIKETT
GRUND9 = "Etikett 9 „Einsetzen und Probe“ ist eine Arbeitsweise, keine Regel; Arbeitsweisen haben keine Kennung."
# Aufgaben, die mit den alten 15 Nummern nur als „Probe“ zu fassen waren, inhaltlich aber zu einer tragenden Idee gehören
ANDERS = {"BG-10": ("id.algebra.erlaubte_zahlen", "Alt Etikett 9. Die Aufgabe fragt nach dem Prüfen der Definitionsmenge (x = 2 macht den Nenner null) – das ist die Idee „Erlaubte Zahlen“, die es bei den 15 Nummern nicht gab.")}
assert all(k in NAME for k, _ in ANDERS.values())
alt = json.load(open(os.path.join(HIER, "etiketten.json"), encoding="utf-8"))["aufgaben"]
aus, ohne, fb_ohne = [], [], 0
zahl = collections.Counter()
for a in alt:
    nr = a["regel"]["nr"]
    k = VON_ETIKETT.get(nr) or ANDERS.get(a["kennung"], (None, None))[0]
    e = dict(kennung_aufgabe=a["kennung"], thema=a["thema"], regel_alt=nr, regel=k, regel_name=NAME.get(k))
    if a["kennung"] in ANDERS:
        e["bemerkung"] = ANDERS[a["kennung"]][1]
    if k is None:
        e["grund"] = GRUND9
        ohne.append(a["kennung"])
    zahl[k or "ohne"] += 1
    e["fehlbilder"] = []
    for f in a["fehlbilder"]:
        fk = VON_ETIKETT.get(f["regel"]["nr"])
        fb_ohne += fk is None
        ort = {x: f[x] for x in ("luecke", "index") if x in f}
        e["fehlbilder"].append(dict(**ort, antwort=f["antwort"], beschreibung=f["fehlbild"], regel_alt=f["regel"]["nr"], regel=fk, fehlbild=None))
    aus.append(e)
assert len(aus) == 78
json.dump({"stand": "2026-11-26",
           "hinweis": "Zuordnung der 78 Aufgaben aus Schritt 1 zu den Kennungen aus regeln-uebersicht/kennungen.json. Reihenfolge wie etiketten.json. "
                      "„regel“ ist die Kennung; null heißt: passt zu keiner Kennung (Grund steht dabei). "
                      "Bei den Fehlbildern ist nur die Regel umgehängt; „fehlbild“ (Fehlbild-Kennung) bleibt null, bis die Beschreibungen einzeln gegen die Fehlbild-Liste gelesen sind.",
           "ohne_kennung": ohne, "aufgaben": aus}, open(os.path.join(HIER, "kennungen-zuordnung.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"78 Aufgaben umgehängt: {dict(sorted(zahl.items()))}")
print(f"ohne Kennung: {ohne}; Fehlbilder: {sum(len(e['fehlbilder']) for e in aus)}, davon ohne Regel-Kennung: {fb_ohne}")
print("OK")
