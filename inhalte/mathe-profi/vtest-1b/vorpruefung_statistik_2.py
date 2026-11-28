"""Auswahl-Statistik und Fehler-Detektiv-Verteilung für vtest-1b (zweite Vorprüfung). Aufruf: python3 -I vorpruefung_statistik_2.py"""
import json, os, re
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__))
alle = []
for d in ["bruch.prozent", "gleichungen.bruch", "terme.potenzgesetze", "zahlen.potenzen_zehner", "messen.flaechen_vielecke"]:
    alle += json.load(open(os.path.join(H, d + ".json"), encoding="utf-8"))["aufgaben"]
au = [a for a in alle if a["antwortform"] == "auswahl"]
print("Auswahl:", len(au), "Tests mit Auswahl:", sum(1 for a in au if a["pool"] == "test"))
print("Platz richtig:", sorted(Counter(a["aufgabe"]["o"]["index"] for a in au).items()))
folge = [a["aufgabe"]["o"]["index"] for a in au]
print("Platzfolge:", "".join(map(str, folge)))
laenge = 0; laengste = []
rl = []; fl = []
for a in au:
    o = a["aufgabe"]["a"]; i = a["aufgabe"]["o"]["index"]
    L = [len(x) for x in o]
    if L[i] == max(L) and L.count(max(L)) == 1: laengste.append(a["kennung"])
    rl.append(L[i]); fl += [L[j] for j in range(4) if j != i]
    if L[i] > 1.3 * (sum(L[j] for j in range(4) if j != i) / 3): print("  >1,3 x Schnitt der falschen:", a["kennung"], L)
print("richtige = einzig längste:", len(laengste), "von", len(au), laengste)
print("Mittel Länge richtig/falsch: %.1f / %.1f" % (sum(rl) / len(rl), sum(fl) / len(fl)))
pat = {"denn/weil": r"\b(denn|weil)\b", "=": "=", "Absolut": r"\b(immer|nie|nur|genau|jede[rs]?|alle|keine?|niemals|stets|nichts|beide)\b", "höchstens/mindestens": r"höchstens|mindestens", "Verneinung": r"\b(nicht|kein\w*|nie)\b", "Sammel": r"\b(Beide|Keine|Alle)\b|keiner", "Komma-Nebensatz": r", (der|die|das|dass|wenn|obwohl)\b"}
for n, p in pat.items():
    r = f = 0
    for a in au:
        o = a["aufgabe"]["a"]; i = a["aufgabe"]["o"]["index"]
        for j, t in enumerate(o):
            if re.search(p, t, re.I if n != "Sammel" else 0):
                if j == i: r += 1
                else: f += 1
    print(f"{n}: richtig {r}/{len(au)}, falsch {f}/{3*len(au)}")
d = Counter(); 
for a in alle:
    if a.get("form") == "fehler_detektiv" and a["antwortform"] == "luecken":
        d[a["aufgabe"]["o"]["werte"][0]] += 1
print("Fehler-Detektiv Lücken: Fehlerzeile", dict(d))
for a in alle:
    if a.get("form") == "fehler_detektiv" and a["antwortform"] == "auswahl":
        print("FD-Auswahl", a["kennung"], a["aufgabe"]["o"])
print("Tests:", [(a["kennung"], a["antwortform"]) for a in alle if a["pool"] == "test"])
print("Antwortform insgesamt:", Counter(a["antwortform"] for a in alle))
print("Zahl-Antworten <=10 ganze (Zählaufgaben):", sum(1 for a in alle if a["antwortform"] == "zahl" and isinstance(a["aufgabe"]["o"]["wert"], int) and 0 <= a["aufgabe"]["o"]["wert"] <= 10 and a["aufgabe"]["o"].get("einheit") in ("Zahlen","Gleichungen","Längen","Kinder")))
