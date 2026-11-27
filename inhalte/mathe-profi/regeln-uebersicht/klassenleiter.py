"""Mathe-Profi, Auftrag 15: Klassenleitern (Teil A, B) und Prüfung der Klassen an der Lehrplan-Kopie (Teil D).

Aufruf: python3 -I inhalte/mathe-profi/regeln-uebersicht/klassenleiter.py
Liest leiter_daten.py, kennungen.json, inhalte/themenliste.json und lehrplan-kopie-zuordnung.txt.
Rechnet jedes Beispiel nach, prüft die Klasse jedes Beispiels gegen die Themenliste und schreibt
klassenleiter.md (zum Lesen), klassenleiter.json (für den Designer: Text und Zeichenpositionen der wirkenden Stelle)
und lehrplan-pruefung.md.
"""
import collections
import json
import os
import sys

sys.dont_write_bytecode = True
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import leiter_daten as LD      # noqa: E402

WURZEL = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
LISTE = {t["thema_schluessel"]: t for t in json.load(open(os.path.join(WURZEL, "inhalte", "themenliste.json"), encoding="utf-8"))}
KENN = {e["kennung"]: e for e in json.load(open(os.path.join(HIER, "kennungen.json"), encoding="utf-8"))["kennungen"]}
assert set(LD.LEITER_R) | set(LD.LEITER_I) == set(KENN) and set(LD.ETIKETT.values()) == set(LD.LEITER_R)
assert all(KENN[k]["etikett_alt"] == nr for nr, k in LD.ETIKETT.items())
# Lehrplan-Kopie: LP[thema][(schulart, gruppe)][jahr] = Menge der Rollen
LP = collections.defaultdict(lambda: collections.defaultdict(dict))
for zeile in open(os.path.join(HIER, "lehrplan-kopie-zuordnung.txt"), encoding="utf-8"):
    if zeile.startswith("#") or not zeile.strip():
        continue
    th, schulart, gruppe, jahr, rollen, _ = zeile.strip().split("|")
    LP[th][(schulart, gruppe)][int(jahr)] = set(rollen.split(","))
KL = range(5, 11)


def marken(text):
    """liefert (Klartext, [[start, ende], …]) – Positionen im Klartext, Ende ausschließlich"""
    klar, pos, offen = [], [], None
    for ch in text:
        if ch == "⟦":
            assert offen is None
            offen = len(klar)
        elif ch == "⟧":
            assert offen is not None and len(klar) > offen
            pos.append([offen, len(klar)])
            offen = None
        else:
            klar.append(ch)
    assert offen is None
    return "".join(klar), pos


n_bsp = n_kein = 0
LAENGEN = []
# einzige Ausnahmen von „Stelle höchstens 12 Zeichen“: die Primfaktoren der 60 (13 Zeichen, gehört zur Zeichnung)
LANGE_STELLE = {("id.zahlen.bausteine", 5)}
daten, texte = [], set()
for kennung in list(LD.LEITER_R) + list(LD.LEITER_I):
    gleich, zeilen = (LD.LEITER_R.get(kennung) or LD.LEITER_I[kennung])
    assert sorted({z[0] for z in zeilen}) == list(KL) and [z[0] for z in zeilen] == sorted(z[0] for z in zeilen), kennung
    stufen = []
    for z in zeilen:
        if z[1] is None:
            assert z[2].startswith("kommt nicht vor"), kennung
            assert [x[0] for x in zeilen].count(z[0]) == 1, (kennung, z[0])
            n_kein += 1
            stufen.append(dict(klasse=z[0], kommt_vor=False, grund=z[2]))
            continue
        kl, art, thema, text, probe = z
        assert probe() is True, (kennung, kl, text)
        assert art in LD.ARTNAME and LISTE[thema]["klasse"].get("gym_by") == kl, (kennung, kl, thema)
        klar, pos = marken(text)
        assert pos and (kennung, klar) not in texte, (kennung, kl)
        texte.add((kennung, klar))
        n_bsp += 1
        lang = max(b - a for a, b in pos)
        assert lang <= 12 or (kennung, kl) in LANGE_STELLE, (kennung, kl, lang, klar)      # Auftrag 17: markierte Stelle höchstens 12 Zeichen
        LAENGEN.append((len(klar), lang, kennung, kl, klar))
        stufen.append(dict(klasse=kl, kommt_vor=True, art=LD.ARTNAME[art], thema=thema, text=klar, wirkende_stelle=[klar[a:b] for a, b in pos], wirkende_stelle_positionen=pos))
    klassen_da = sorted({s["klasse"] for s in stufen if s["kommt_vor"]})
    daten.append(dict(kennung=kennung, art=KENN[kennung]["art"], ort=KENN[kennung]["ort"], name=KENN[kennung]["name"], merksatz=KENN[kennung]["merksatz"],
                      in_jeder_zeile_markiert=gleich, klassen_mit_beispiel=klassen_da, laeuft_ueber_mehrere_klassen=len(klassen_da) > 1, stufen=stufen))

json.dump({"stand": "2026-11-27",
           "hinweis": "Klassenleitern für das Regel-Universum, Gymnasium Bayern, Klasse 5 bis 10. Je Kennung und Klasse genau eine Aussage: ein Beispiel oder „kommt nicht vor“ mit Grund. "
                      "„wirkende_stelle_positionen“: Zeichenpositionen im Feld „text“ (Anfang einschließlich, Ende ausschließlich) – genau diese Zeichen werden markiert. "
                      "Art: Vorwissen (kommt vor, wird noch nicht als Regel gelehrt), Einführung, Anwendung.",
           "leitern": daten}, open(os.path.join(HIER, "klassenleiter.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ── klassenleiter.md ──
def uebersicht(kennungen):
    t = ["| | " + " | ".join(f"Kl. {k}" for k in KL) + " |", "|---|" + "---|" * 6]
    for k in kennungen:
        d = next(x for x in daten if x["kennung"] == k)
        zellen = []
        for kl in KL:
            arten = [s.get("art") for s in d["stufen"] if s["klasse"] == kl and s["kommt_vor"]]
            zellen.append("–" if not arten else ("E" if "Einführung" in arten else "A" if "Anwendung" in arten else "V"))
        t.append(f"| {d['name']} | " + " | ".join(zellen) + " |")
    return "\n".join(t)


teile = []
for i, k in enumerate(LD.LEITER_R, 1):
    d = next(x for x in daten if x["kennung"] == k)
    teile += [f"### Rechenregel {i}: {d['name']} (`{k}`)", "", f"> **{d['merksatz']}**", "", f"**In jeder Zeile markiert:** {LD.LEITER_R[k][0]}", "", LD.leiter_tabelle(LD.LEITER_R[k][1]), ""]
ideen = []
planet = None
nur_eine = []
for k in LD.LEITER_I:
    d = next(x for x in daten if x["kennung"] == k)
    if d["ort"] != planet:
        planet = d["ort"]
        ideen += [f"### Planet „{planet}“", ""]
    kl = d["klassen_mit_beispiel"]
    lauf = f"läuft über die Klassen {', '.join(str(x) for x in kl)}" if len(kl) > 1 else f"kommt nur in Klasse {kl[0]} vor"
    if len(kl) <= 2:
        nur_eine.append((d["name"], planet, kl))
    ideen += [f"#### {d['name']} (`{k}`) – {lauf}", "", f"> **{d['merksatz']}**", "", f"**In jeder Zeile markiert:** {LD.LEITER_I[k][0]}", "", LD.leiter_tabelle(LD.LEITER_I[k][1]), ""]
n_r = sum(1 for d in daten if d["art"] == "rechenregel" for s in d["stufen"] if s["kommt_vor"])
n_r_kein = sum(1 for d in daten if d["art"] == "rechenregel" for s in d["stufen"] if not s["kommt_vor"])
open(os.path.join(HIER, "klassenleiter.md"), "w", encoding="utf-8").write(f"""# Regel-Universum · Klassenleitern: dieselbe Regel, dieselbe Idee – von Klasse 5 bis 10

Mathe-Profi, 27.11.2026 (Auftrag 15, Teil A und B). Erzeugt von `klassenleiter.py` aus `leiter_daten.py`; {n_bsp} Beispiele, jedes nachgerechnet, jede Klasse gegen die Themenliste geprüft (Lauf „OK“).
Für den Designer liegt dasselbe als `klassenleiter.json` vor – mit den genauen Zeichenpositionen der wirkenden Stelle.

## Wie die Leitern gebaut sind

- **Je Regel und Klasse genau eine Aussage:** ein Rechenbeispiel mit dem Thema der App – oder ausdrücklich „kommt nicht vor“ mit Grund. Kein Feld ist leer, nichts ist erfunden.
- **Gleich gebaut:** In jeder Zeile einer Leiter steht dieselbe Stelle an derselben Position und es geschieht dieselbe Handlung. Nur die Zahlen werden zu Brüchen, Buchstaben, Wurzeln.
- **Wirkende Stelle:** die Zeichen in ⟦ ⟧. Genau diese markiert der Designer; untereinandergesetzt stehen sie senkrecht übereinander.
- **Art:** Vorwissen (kommt vor, wird noch nicht als Regel gelehrt), Einführung, Anwendung. Geprüft gegen die Lehrplan-Kopie der App: `lehrplan-pruefung.md`.
- **Klassen:** Gymnasium Bayern. Realschule und IB: siehe `lehrplan-pruefung.md`.
- „kommt nicht vor … wird als bekannt benutzt“ heißt: Die Regel wird in dieser Klasse gebraucht, aber kein Thema der App übt sie eigens. „Beginnt später“ heißt: Der Stoff ist noch nicht dran.

## Teil A – die 14 Rechenregeln

{n_r} Beispiele, {n_r_kein} Mal „kommt nicht vor“ (von {14 * 6} Feldern).

{uebersicht(LD.LEITER_R)}

{chr(10).join(teile)}
## Teil B – die 28 tragenden Ideen

{uebersicht(LD.LEITER_I)}

**Ideen, die nur in einer oder zwei Klassen vorkommen** (keine Leiter, sondern ein Ort): {'; '.join(f"{n} ({p}): Klasse {' und '.join(str(x) for x in kl)}" for n, p, kl in nur_eine)}.

{chr(10).join(ideen)}
## Nicht geprüft

- Die Beispiele sind fachlich nachgerechnet; ob ein Kind an ihnen „es ist dasselbe“ wirklich sieht, ist nicht erprobt.
- „Kommt nicht vor“ ist an den Themen der App entschieden, nicht am Unterricht einer Schule.
- Klassen der Realschule und des IB sind in den Leitern nicht eigens ausgeführt.
""")

# ── Teil D: Lehrplan-Prüfung ──
G = ("gym_by", "allgemein")
GRUPPEN = [("rs_by", "allgemein"), ("rs_by", "rs_I"), ("rs_by", "rs_II_III"), ("ib_myp", "myp_beide"), ("ib_myp", "myp_standard"), ("ib_myp", "myp_extended")]


def neu_in(thema, schulart):
    """früheste Jahre mit Rolle „neu“ je Gruppe einer Schulart: {gruppe: jahr}"""
    aus = {}
    for (s, g), jahre in LP.get(thema, {}).items():
        if s == schulart:
            j = [x for x, r in jahre.items() if "neu" in r]
            if j:
                aus[g] = min(j)
    return aus


def erstes(thema, schulart):
    j = [x for (s, g), jahre in LP.get(thema, {}).items() if s == schulart for x in jahre]
    return min(j) if j else None


abw, ok = [], 0
for d in daten:
    for s in d["stufen"]:
        if not s["kommt_vor"]:
            continue
        rollen = LP.get(s["thema"], {}).get(G, {}).get(s["klasse"])
        wo = f"{d['name']}, Klasse {s['klasse']}, `{s['thema']}`"
        if s["thema"] not in LP:
            abw.append((wo, s["art"], "Thema fehlt in der Lehrplan-Kopie ganz", "nicht prüfbar"))
        elif rollen is None:
            da = sorted(LP[s["thema"]].get(G, {}))
            abw.append((wo, s["art"], f"Lehrplan-Kopie nennt das Thema am Gymnasium nicht in Klasse {s['klasse']}" + (f", sondern in {', '.join(map(str, da))}" if da else " (gar nicht am Gymnasium)"), "Abweichung"))
        elif s["art"] == "Einführung" and "neu" not in rollen:
            abw.append((wo, s["art"], "Lehrplan-Kopie nennt das Thema in dieser Klasse, aber nicht als „neu“", "Abweichung"))
        else:
            ok += 1
themen = sorted({s["thema"] for d in daten for s in d["stufen"] if s["kommt_vor"]})
klassen_abw = []
for th in themen:
    for schulart, name in (("gym_by", "Gymnasium"), ("rs_by", "Realschule"), ("ib_myp", "IB")):
        soll = LISTE[th]["klasse"].get(schulart)
        n = neu_in(th, schulart)
        fr = erstes(th, schulart)
        if soll is None and fr is None:
            continue
        if soll is None:
            klassen_abw.append((th, name, "–", f"Lehrplan-Kopie: ab Jahr {fr}"))
        elif fr is None:
            klassen_abw.append((th, name, str(soll), "in der Lehrplan-Kopie kein Eintrag"))
        elif not n:
            if fr != soll:
                klassen_abw.append((th, name, str(soll), f"Lehrplan-Kopie: erster Eintrag Jahr {fr}, nirgends als „neu“"))
        elif min(n.values()) != soll:
            klassen_abw.append((th, name, str(soll), "Lehrplan-Kopie: „neu“ in " + ", ".join(f"{g.replace('rs_', 'Gruppe ').replace('myp_', '').replace('allgemein', 'allen')} Jahr {j}" for g, j in sorted(n.items()))))
zeilen_e = []
for d in daten:
    e = [s for s in d["stufen"] if s["kommt_vor"] and s["art"] == "Einführung"]
    if not e:
        zeilen_e.append(f"| {d['name']} | – | – | – | – | – | keine Einführung in 5 bis 10 gesetzt |")
        continue
    s = e[0]
    r, i = neu_in(s["thema"], "rs_by"), neu_in(s["thema"], "ib_myp")
    fmt = lambda x: str(x) if x is not None else "–"
    rs1 = r.get("rs_I", r.get("allgemein"))
    rs2 = r.get("rs_II_III", r.get("allgemein"))
    ib = min(i.values()) if i else None
    bem = []
    if rs1 is None and rs2 is None:
        bem.append("Realschule: nicht als „neu“ genannt" if erstes(s["thema"], "rs_by") else "Realschule: Thema fehlt")
    elif rs1 != rs2:
        bem.append("Gruppen I und II/III verschieden")
    if (rs1 or rs2) and min(x for x in (rs1, rs2) if x) != s["klasse"]:
        bem.append("Realschule in anderer Klasse als Gymnasium")
    if ib is None:
        bem.append("IB: nicht als „neu“ genannt" if erstes(s["thema"], "ib_myp") else "IB: Thema fehlt")
    zeilen_e.append(f"| {d['name']} | {s['klasse']} | `{s['thema']}` | {fmt(rs1)} | {fmt(rs2)} | {fmt(ib)} | {'; '.join(bem)} |")
n_abw = sum(1 for a in abw if a[3] == "Abweichung")
open(os.path.join(HIER, "lehrplan-pruefung.md"), "w", encoding="utf-8").write(f"""# Regel-Universum · Klassen am Lehrplan geprüft (Auftrag 15, Teil D)

Mathe-Profi, 27.11.2026. Erzeugt von `klassenleiter.py`.

## Womit geprüft wurde – und womit nicht

- **Im Repo liegen keine Lehrplan-Dateien.** Es gibt nur `inhalte/themenliste.json`: je Thema eine Klasse je Schulart und einige Stichworte aus dem Lehrplan. [G]
- Geprüft habe ich deshalb gegen die **Lehrplan-Kopie in der Datenbank der App** (nur gelesen; 434 Zeilen, abgelegt als `lehrplan-kopie-zuordnung.txt`). Sie sagt je Thema, Schulart, Gruppe und Jahr, ob der Lehrplan das Thema nennt und mit welcher Rolle: „neu“, „weitergeführt“ oder ohne Angabe. [G]
- **Nicht geprüft: LehrplanPLUS an der Quelle.** Ob die Kopie den Lehrplan richtig und vollständig wiedergibt, weiß ich nicht.
- **Die Prüfung reicht nur bis zum Thema, nicht bis zur Regel.** Der Lehrplan ordnet Themen Klassen zu, keine Rechenregeln. Ob etwa „Minus vor der Klammer“ in Klasse 5 Vorwissen oder schon Stoff ist, steht in der Kopie nicht; das bleibt meine Einschätzung.

## 1. Gymnasium: jedes Beispiel der Klassenleitern

Regel der Prüfung: Das Thema muss in der Lehrplan-Kopie in dieser Klasse stehen. Ist das Beispiel als „Einführung“ gesetzt, muss die Kopie das Thema dort als „neu“ führen.

**{ok} von {ok + len(abw)} Beispielen bestehen. {n_abw} Abweichungen:**

| Beispiel | von mir gesetzt | Befund | |
|---|---|---|---|
{chr(10).join(f"| {a} | {b} | {c} | {e} |" for a, b, c, e in abw) or "| – | – | – | – |"}

## 2. Themenliste gegen Lehrplan-Kopie: Klasse je Thema

Für die {len(themen)} Themen, die in den Klassenleitern vorkommen: Stimmt die Klasse der Themenliste mit dem frühesten „neu“ der Lehrplan-Kopie überein? Abweichungen:

| Thema | Schulart | Themenliste | Lehrplan-Kopie |
|---|---|---|---|
{chr(10).join(f"| `{a}` | {b} | {c} | {d} |" for a, b, c, d in klassen_abw) or "| – | – | – | – |"}

Zu lesen mit Vorsicht: Beim IB zählt die Kopie Jahre (MYP 1 bis 5), nicht Klassen, und das IB schreibt keine verbindliche Jahresfolge vor. „Nirgends als neu“ kann auch heißen, dass die Rolle in der Kopie nicht gepflegt ist.

## 3. Einführung je Regel und Idee: Gymnasium, Realschule, IB

Erste als „Einführung“ gesetzte Stufe der Klassenleiter; dazu, in welchem Jahr die Lehrplan-Kopie dasselbe Thema an Realschule (Gruppe I, Gruppe II/III) und IB als „neu“ führt.

| Regel oder Idee | Gym. | Thema | RS I | RS II/III | IB (Jahr) | Bemerkung |
|---|---|---|---|---|---|---|
{chr(10).join(zeilen_e)}

## Was sich so nicht prüfen lässt

1. **Vorwissen / Einführung / Anwendung auf der Ebene der Regel.** Prüfbar ist nur, ob das *Thema* in der Klasse steht und neu ist.
2. **„Kommt nicht vor“.** Die Kopie kann zeigen, dass ein Thema fehlt – nicht, dass eine Regel in einer Klasse nirgends gebraucht wird.
3. **Realschule Gruppe II/III:** Die Kopie enthält dort an vielen Stellen nur Überschriften; ein fehlendes „neu“ ist kein Beleg.
4. **IB:** Jahre statt Klassen, keine verbindliche Folge.
5. **Die Kopie selbst** gegen LehrplanPLUS.
""")
print(f"Leitern: {len(daten)} ({n_bsp} Beispiele, {n_kein} Mal „kommt nicht vor“); Rechenregeln {n_r} Beispiele / {n_r_kein} ohne")
print(f"Länge der Sprossen: über 34 Zeichen {sum(1 for l in LAENGEN if l[0] > 34)}, über 44 Zeichen {sum(1 for l in LAENGEN if l[0] > 44)} von {len(LAENGEN)}; längste Stelle {max(l[1] for l in LAENGEN)} Zeichen")
for l in sorted(LAENGEN, reverse=True)[:14]:
    print("   ", l[0], l[2], l[3], l[4])
print(f"Lehrplan-Kopie: {ok} bestanden, {len(abw)} Befunde; Klassen-Abweichungen Themenliste: {len(klassen_abw)}")
print("OK")
