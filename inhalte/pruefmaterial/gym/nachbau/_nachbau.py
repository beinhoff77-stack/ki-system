#!/usr/bin/env python3
# Baut die nachgebauten Schulaufgaben aus katalog.json.
# Aufruf: python3 _nachbau.py [8|5|alle]
# Jede Aufgabe: eigener Text, Zufallszahlen (fester Seed je Aufgabe), Lösung im Generator berechnet und gegengeprüft (chk).
import json, os, re, sys, zlib
from fractions import Fraction as F

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import _kern as K
for mod in ("_g8a", "_g8b", "_g8c", "_g5a", "_g5b"):
    if os.path.exists(os.path.join(HIER, mod + ".py")):
        __import__(mod)

KAT = json.load(open(os.path.join(HIER, "..", "katalog.json")))
ABRUF = "2026-11-22"


def schluessel(z):
    if z["status"] == "zugeordnet":
        return (z["thema_schluessel"], z["etappe"])
    if z["status"] == "luecke":
        return ("L", z["vorschlag"])
    return ("X", z["vorschlag"])


BESCHREIBEND = ("zeichn", "konstru", "begründ", "erklär", "beschreib", "skizz", "beweis", "spiegel", "markier", "erfind", "frage", "regel",
                "ankreuz", "wissen", "definier", "benenn", "notation", "zuordnen", "puzzle", "netz", "falten", "drehen", "ansicht", "wahr")


def pruefart(t, z):
    if K.PRUEF:
        return "gegengerechnet"
    if any(w in (z.get("typ") or "").lower() for w in BESCHREIBEND) or z["kompetenz"] in ("K1", "K4", "K6") or not re.search(r"\d", t.loesung):
        return "Musterlösung (Zeichnung/Begründung/Wissen)"
    return "vom Skript berechnet, ohne zweite Rechnung"


def punkte_verteilen(arbeit, zeilen):
    bek = [z["punkte"] for z in zeilen if z["punkte"] is not None]
    unb = [z for z in zeilen if z["punkte"] is None]
    pk = {}
    auszug = "Auszug" in arbeit["titel"]
    if unb:
        ges = arbeit.get("punkte_gesamt")
        if ges and not auszug and ges > sum(bek):
            rest = F(ges) - sum(F(b) for b in bek)
            gew = [{"I": 2, "II": 3, "III": 4}[z["niveau"]] for z in unb]
            roh = [rest * g / sum(gew) for g in gew]
            ganz = [max(1, int(r)) for r in roh]
            diff = int(rest) - sum(ganz)
            i = 0
            while diff != 0 and i < 1000:
                j = i % len(ganz)
                if diff > 0:
                    ganz[j] += 1; diff -= 1
                elif ganz[j] > 1:
                    ganz[j] -= 1; diff += 1
                i += 1
            for z, p in zip(unb, ganz):
                pk[id(z)] = p
        else:
            for z in unb:
                pk[id(z)] = {"I": 1, "II": 2, "III": 2}[z["niveau"]] if arbeit.get("punkte_gesamt") else {"I": 2, "II": 3, "III": 4}[z["niveau"]]
    return [z["punkte"] if z["punkte"] is not None else pk[id(z)] for z in zeilen]


def schritte_punkte(weg, p):
    """Lösungsschritte zu Gruppen mit Punkten zusammenfassen."""
    p = F(p).limit_denominator(2)
    weg = [w for w in weg if w]
    if not weg:
        weg = ["Ergebnis"]
    if p < 1:
        return [(" · ".join(weg), p)]
    ganz = int(p); halb = p - ganz
    if ganz >= len(weg):
        basis, rest = divmod(ganz, len(weg))
        out = [[w, basis + (1 if i >= len(weg) - rest else 0)] for i, w in enumerate(weg)]
    else:
        # Schritte auf 'ganz' Gruppen verteilen
        gr = [[] for _ in range(ganz)]
        for i, w in enumerate(weg):
            gr[min(i * ganz // len(weg), ganz - 1)].append(w)
        out = [[" · ".join(g), 1] for g in gr]
    if halb:
        out[-1][1] = out[-1][1] + halb
    return [(w, F(q)) for w, q in out]


MINUS_RE = re.compile(r'(^|[\s(\[{|;=/·,:])-(?=\d)')


def minus(t):
    if t is None:
        return t
    return MINUS_RE.sub(lambda m: m.group(1) + "−", t)


def fp(p):
    return K.fz(F(p).limit_denominator(2), dez=True)


def baue(klasse):
    fehlt, fehler, ergebnis = {}, [], []
    os.makedirs(HIER, exist_ok=True)
    for arb in KAT["arbeiten"]:
        if arb["klasse"] != klasse:
            continue
        zeilen = [z for z in KAT["aufgaben"] if z["arbeit_id"] == arb["arbeit_id"]]
        pkte = punkte_verteilen(arb, zeilen)
        aufg = []
        texte = set()
        for z, pk in zip(zeilen, pkte):
            key = schluessel(z)
            gen = K.REG.get(key)
            if gen is None:
                fehlt.setdefault(key, []).append(f"{arb['arbeit_id']}/{z['aufgabe']}: {z['kurzbeschreibung']}")
                continue
            t = None
            for versuch in range(40):
                seed = zlib.crc32(f"{arb['arbeit_id']}|{z['aufgabe']}|{versuch}".encode())
                K.PRUEF.clear()
                try:
                    t = gen(K.Ctx(seed, z))
                    if t.text in texte and versuch < 39:
                        t = None
                        continue
                    texte.add(t.text)
                    break
                except (K.Pruefung, ZeroDivisionError, ValueError, AssertionError, IndexError):
                    t = None
            if t is None:
                fehler.append(f"{arb['arbeit_id']}/{z['aufgabe']} {key}")
                continue
            aufg.append(dict(nr=z["aufgabe"], punkte=pk, niveau=z["niveau"], kompetenz=z["kompetenz"], typ=z["typ"],
                             thema=z["thema_schluessel"], etappe=z["etappe"], etappe_titel=z.get("etappe_titel"), teil=z.get("teil"),
                             lernbereich=z.get("lernbereich"), status=z["status"], vorschlag=z.get("vorschlag"),
                             text=minus(t.text), abbildung=t.abb, loesung=minus(t.loesung),
                             weg=[dict(schritt=minus(w), punkte=float(q)) for w, q in schritte_punkte(t.weg, pk)],
                             gegenpruefung=list(K.PRUEF), pruefart=pruefart(t, z)))
        if not aufg:
            continue
        summe = sum(F(a["punkte"]).limit_denominator(2) for a in aufg)
        auszug = "Auszug" in arb["titel"]
        zeit = arb.get("zeit_min")
        zeit_hinweis = ""
        if auszug and zeit:
            zeit = max(10, round(zeit * float(summe) / (arb.get("punkte_gesamt") or 21) / 5) * 5)
            zeit_hinweis = " (anteilig zum Auszug)"
        elif not zeit:
            zeit = 45; zeit_hinweis = " (Annahme: übliche Dauer)"
        eintrag = dict(arbeit_id=arb["arbeit_id"], klasse=klasse, vorbild=arb["titel"], vorbild_quelle=arb["quelle"], kategorie=arb.get("kategorie"),
                       zeit_min=zeit, punkte=float(summe), hilfsmittel=arb.get("hilfsmittel"), themen=arb.get("themen_gemeinsam"), aufgaben=aufg)
        ergebnis.append(eintrag)
        schreibe_md(eintrag, zeit_hinweis)
    return ergebnis, fehlt, fehler


def schreibe_md(e, zeit_hinweis):
    L = []
    L.append(f"# Nachbau {e['arbeit_id']} – Mathematik Klasse {e['klasse']}")
    L.append("")
    L.append(f"*Eigene Aufgaben nach dem Muster von „{e['vorbild']}“ (gleicher Typ, gleiche Kompetenz und gleiches Niveau, eigene Texte und Zahlen). Vorbild: {e['vorbild_quelle']}*")
    L.append("")
    L.append(f"**Zeit:** {e['zeit_min']} min{zeit_hinweis} · **Punkte:** {fp(e['punkte'])} · **Hilfsmittel:** {e['hilfsmittel'] or 'keine Angabe'}")
    L.append("")
    L.append("Name: ______________________  Datum: ____________")
    L.append("")
    L.append("## Aufgaben")
    for a in e["aufgaben"]:
        L.append("")
        L.append(f"**Aufgabe {a['nr']}** ({fp(a['punkte'])} P)")
        L.append("")
        L.append(a["text"].replace("\n", "  \n"))
        if a.get("abbildung"):
            L.append("")
            L.append(a["abbildung"])
    L.append("")
    L.append(f"*Gesamt: {fp(e['punkte'])} Punkte*")
    L.append("")
    L.append('<div style="page-break-after: always;"></div>')
    L.append("")
    L.append(f"## Lösungsblatt {e['arbeit_id']}")
    for a in e["aufgaben"]:
        L.append("")
        L.append(f"**{a['nr']}** ({fp(a['punkte'])} P) – Ergebnis: {a['loesung']}")
        for w in a["weg"]:
            L.append(f"- {w['schritt']} ({fp(w['punkte'])} P)")
        L.append(f"- *Lösungskontrolle: {a['pruefart']}*")
        if a["status"] == "zugeordnet":
            teil = f", {a['teil']}" if a.get("teil") else ""
            L.append(f"- *Zuordnung: {a['thema']} › {a['etappe']} ({a['etappe_titel'] or ''}{teil}); Niveau {a['niveau']}, {a['kompetenz']}*")
        elif a["status"] == "luecke":
            L.append(f"- *Zuordnung: Lücke – Vorschlag „{a['vorschlag']}“ ({a['thema'] or ''}); Niveau {a['niveau']}, {a['kompetenz']}*")
        else:
            L.append(f"- *Zuordnung: außerhalb – {a['vorschlag']}; Niveau {a['niveau']}, {a['kompetenz']}*")
    g = float(e["punkte"])
    stufen = [(1, 0.85), (2, 0.70), (3, 0.55), (4, 0.40), (5, 0.20)]
    L.append("")
    L.append("**Notenschlüssel (Vorschlag, Annahme – Lehrkräfte legen ihn selbst fest):** " +
             " · ".join(f"{nt}: ab {fp(F(round(g*q*2),2))} P" for nt, q in stufen) + " · 6: darunter")
    L.append("")
    with open(os.path.join(HIER, f"{e['arbeit_id']}.md"), "w") as f:
        f.write("\n".join(L))


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "alle"
    klassen = [8, 5] if arg == "alle" else [int(arg)]
    alle = []
    pfad = os.path.join(HIER, "nachbau.json")
    alt = json.load(open(pfad))["arbeiten"] if os.path.exists(pfad) else []
    gesamt_fehlt, gesamt_fehler = {}, []
    for k in klassen:
        erg, fehlt, fehler = baue(k)
        alle += erg
        gesamt_fehlt.update(fehlt); gesamt_fehler += fehler
        n = sum(len(e["aufgaben"]) for e in erg)
        print(f"Klasse {k}: {len(erg)} Arbeiten, {n} Aufgaben, {sum(len(v) for v in fehlt.values())} ohne Generator, {len(fehler)} Prüffehler")
    behalten = [e for e in alt if e["klasse"] not in klassen]
    alle = sorted(behalten + alle, key=lambda e: (-e["klasse"], e["arbeit_id"]))
    json.dump(dict(stand=ABRUF, hinweis="Nachbau: eigene Aufgaben nach Typ/Kompetenz/Niveau der katalogisierten Prüfungsaufgaben; keine Originaltexte. "
                   "Lösungen im Generator berechnet und per Einsetz-/Gegenrechnung geprüft (Feld gegenpruefung).",
                   arbeiten=alle), open(pfad, "w"), ensure_ascii=False, indent=1)
    for k, v in sorted(gesamt_fehlt.items(), key=lambda t: -len(t[1])):
        print("FEHLT", k, len(v), v[0])
    for f in gesamt_fehler:
        print("FEHLER", f)
