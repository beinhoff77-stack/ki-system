"""Mathe-Profi, Auftrag 21 „Vorrat neue Formen, Klasse 7": rollend-8.

Aufruf: python3 -I inhalte/mathe-profi/rollend-8/bauen.py
Baut je Lernkarte der zehn Themen GENAU DREI Aufgaben in neuer Form, schreibt eine JSON-Datei je Thema
und endet mit „OK", wenn alle Prüfungen durchlaufen. Der Inhalt steht von Hand in teile/<kurz>.py;
dieses Programm rechnet jede Lösung nach und prüft Pflichtfelder, Formen, zaehlt und die Mischung je Lernkarte.
Nur Inhalte. Nichts wird eingespielt.
"""
import importlib
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from fractions import Fraction as F

sys.dont_write_bytecode = True
HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
sys.path.insert(0, os.path.join(WURZEL, "tools"))
sys.path.insert(0, HIER)
import inhalt_pruefen as ip      # noqa: E402

KENN = json.load(open(os.path.join(HIER, "..", "regeln-uebersicht", "kennungen.json"), encoding="utf-8"))["kennungen"]
REGELN = {e["kennung"]: e for e in KENN}

# Kürzel -> (Typ-Name wie in tools/rollend_sql.py, Standard-g, zaehlt)
TYP = {
    "LW": ("Lückenweg", "direkt", "nein"),
    "FD": ("Fehler-Detektiv (einfache Form)", "fehler", "ja"),
    "VW": ("Verfahren wählen (einfache Form)", "erkennen", "ja"),
    "ZW": ("Zwei Wege vergleichen", "mehrschritt", "ja"),
    "UM": ("Umkehren", "umkehr", "ja"),
    "BR": ("Brücke", "darstellung", "ja"),
    "AN": ("Anwenden", "einkleidung", "ja"),
}
ZAEHLENDE_FORMEN = {"UM", "ZW", "BR", "VW", "AN"}       # Auftrag: mindestens eine je Lernkarte
MINDESTENS_ZWEIMAL = ("UM", "ZW", "BR", "AN")           # Auftrag: je Thema mindestens zweimal, wo es fachlich passt

# Reihenfolge wie im Auftrag; (Modul, Thema-Schlüssel, Datei, Themen-Datei des Bestands, Lernkarten)
THEMEN = [
    ("zinsen", "finanzen.zinsen", "finanzen.zinsen", "finanzen.zinsen",
     ["begriffe", "rollen", "jahreszinsen", "jahreszinsen_komma", "zinssatz", "kapital", "monatszinsen", "zeitanteil"]),
    ("zehner", "zahlen.potenzen_zehner", "zahlen.potenzen_zehner", "zahlen.potenzen_zehner",
     ["zehnerpotenz", "gross_wissenschaftlich", "vorsilben_gross", "negativer_exponent", "klein_wissenschaftlich",
      "vorsilben_klein", "vergleichen_pruefen"]),
    ("kreis", "geometrie.kreis", "geometrie.kreis", "geometrie.kreis",
     ["thales", "umkehrung", "beweis", "lage", "tangente", "umkreis_inkreis"]),
    ("kennwerte", "daten.kennwerte", "daten.kennwerte", "daten.kennwerte",
     ["mittelwert", "mittel_tabelle", "mittel_rueckwaerts"]),
    ("boxplot", "daten.boxplot", "daten.boxplot", "daten.boxplot",
     ["median", "kennwerte", "mittel_median", "quartile", "boxplot", "vergleichen"]),
    ("stichproben", "daten.stichproben", "daten.stichproben", "daten.stichproben",
     ["begriffe", "hochrechnen", "repraesentativ", "fehlerquellen", "aussagen"]),
    ("potenzgesetze", "terme.potenzgesetze", "terme.potenzgesetze", "terme.potenzgesetze",
     ["potenz_begriff", "negativer_exponent", "fehler_finden"]),
    ("determinanten", "abbildungen.determinanten2", "abbildungen.determinanten2", "abbildungen.determinanten2",
     ["det_berechnen", "parallelogramm", "dreieck", "umlaufsinn", "viereck", "vieleck"]),
    ("schraegbilder", "raum.schraegbilder", "raum.schraegbilder", "raum.schraegbilder",
     ["pyramide", "lage", "wahre_groesse", "raumwinkel"]),
    ("schraegbilder2", "raum.schraegbilder_teil2", "raum.schraegbilder_teil2", "raum.schraegbilder",
     ["koordinaten", "rotation", "axialschnitt", "koerper_symmetrie"]),
]

SUP = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁻": "-"}
# Zahlwörter und Umschreibungen, an denen man einen Lückenwert erraten könnte (Wortanfang genügt)
ZAHLWORT = {
    0: r"null|kein\w*|nie|nichts", 1: r"eins|einmal|einzig\w*", 2: r"zwei\w*|doppelt\w*|paar", 3: r"drei\w*|dritt\w*",
    4: r"vier\w*", 5: r"fünf\w*", 6: r"sechs\w*", 7: r"sieben\w*", 8: r"acht\w*", 9: r"neun\w*", 10: r"zehn\w*",
    11: r"elf\w*", 12: r"zwölf\w*", 20: r"zwanzig\w*", 100: r"hundert\w*", 1000: r"tausend\w*", 1000000: r"million\w*",
}
# Wörter, die zufällig wie ein Zahlwort beginnen, aber nichts verraten
HARMLOS = re.compile(r"\b(dreieck\w*|viereck\w*|vieleck\w*|zehnerpotenz\w*|viertel\w*|dritte[nrs]?|nachdrei\w*)\b", re.I)
ZAHL = re.compile(r"[−-]?\d+(?:[  ]\d{3})*(?:[,.]\d+)?")
ohne_zahlen = lambda t: re.sub(r"\s+", " ", ZAHL.sub("#", t)).strip()
KOMMA_LUECKE = re.compile(r"\d\s*,\s*[①②③④⑤□]")
fehler = []
FEHLERZEILEN = []


def pruefe_fehlbild(k, fb, antwort, richtig, env):
    """Fehlbild einer Zahl- oder Lückenaufgabe: die beschriebene Rechnung muss genau die gespeicherte Fehlantwort ergeben."""
    if "rechnung" not in fb:
        fehler.append(f"{k}: Fehlbild „{fb.get('beschreibung', '')[:40]}“ hat keine Rechnung zum Nachrechnen")
        return
    try:
        v = rechne(fb["rechnung"], env)
    except Exception as ex:      # noqa: BLE001
        fehler.append(f"{k}: Fehlbild-Rechnung {fb['rechnung']!r} nicht auswertbar ({ex})")
        return
    if not gleich(v, antwort):
        fehler.append(f"{k}: Fehlbild „{fb['beschreibung'][:50]}“: Rechnung {fb['rechnung']} ergibt {float(v):g}, gespeichert ist {antwort}")
    if gleich(antwort, richtig):
        fehler.append(f"{k}: Fehlbild-Antwort {antwort} ist gleich der richtigen Antwort")


def rechne(ausdruck, env=None):
    """Rechnet einen Ausdruck mit Brüchen aus (ganze Zahlen werden zu Fraction, damit : exakt bleibt).
    env: Namen wie L1, L2 (schon berechnete Lücken) für die Prüfung der Abhängigkeit."""
    genau = re.sub(r"(?<![\w.])(\d+)(?![\w.])", r"F(\1)", ausdruck)
    namen = {"F": F, "abs": abs, "min": min, "max": max, "round": round}
    namen.update(env or {})
    return F(eval(genau, {"__builtins__": {}}, namen))


def norm(t):
    """Text für die Suche nach Lückenwerten: Hochzahlen als ^n, Tausenderleerzeichen entfernt."""
    t = re.sub(r"[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+", lambda m: "^" + "".join(SUP[c] for c in m.group()), t)
    return re.sub(r"(?<=\d)[ \u00a0\u202f\u2009](?=\d{3}(?!\d))", "", t)


def steht_als_ziffer(w, t):
    return re.search(rf"(?<![\d,.]){re.escape(str(w))}(?!\d|[,.]\d)", norm(t)) is not None


def steht_als_zahlwort(w, t):
    if w not in ZAHLWORT:
        return None
    rest = HARMLOS.sub(" ", t)
    m = re.search(rf"\b({ZAHLWORT[w]})\b", rest, re.I)
    return m.group(0) if m else None


def gleich(a, b):
    a, b = float(a), float(b)
    return abs(a - b) <= 1e-9 + 1e-3 * max(abs(a), abs(b))


def als_zahl(x):
    """Fraction -> int, wenn ganz, sonst float (so steht es auch im Bestand)."""
    f = F(x) if not isinstance(x, F) else x
    return int(f) if f.denominator == 1 else float(f)


def bestand(datei):
    d = json.load(open(os.path.join(WURZEL, "inhalte", "themen", datei + ".json"), encoding="utf-8"))
    texte = {a["f"].get("text", "") for a in d["aufgaben"]}
    bauform = {ohne_zahlen(a["f"].get("text", "")) for a in d["aufgaben"]}
    karte = {}
    for a in d["aufgaben"]:
        karte.setdefault(a["l"], a["t"])
    sach = defaultdict(bool)
    for a in d["aufgaben"]:
        if a.get("g") in ("einkleidung", "transfer", "pruefung"):
            sach[a["l"]] = True
    return d, texte, bauform, karte, sach


def eintrag_bauen(e, thema, karte_zu_t, kuerzel):
    """Macht aus einem Eintrag von Hand den vollständigen Datensatz wie in rollend-4."""
    k, typ = e["k"], e["typ"]
    name, g_standard, zaehlt = TYP[typ]
    s = e["s"]
    y = e["y"]
    g = e.get("g", g_standard)
    if typ == "AN" and "g" not in e:
        g = "einkleidung" if s == 2 else "transfer"
    f = {"text": e["text"]}
    if y == "luecken":
        f["schablone"] = e["schablone"]
        f["hinweis"] = e.get("f_hinweis", "Je Lücke eine ganze Zahl (mit Minus, falls negativ).")
    elif e.get("f_hinweis"):
        f["hinweis"] = e["f_hinweis"]
    if e.get("schablone") and y == "text":
        f["schablone"] = e["schablone"]
        f["hinweis"] = e.get("f_hinweis", "")
    a = {"l": e["karte"], "t": karte_zu_t.get(e["karte"], e["karte"]), "p": "uebung", "s": s, "g": g, "y": y, "f": f}

    if y == "luecken":
        env, werte = {}, []
        for i, c in enumerate(e["c"], 1):
            v = rechne(c, env)
            env[f"L{i}"] = v
            werte.append(als_zahl(v))
        if werte != list(e["erwartet"]):
            fehler.append(f"{k}: Lücken nachgerechnet {werte}, von Hand erwartet {list(e['erwartet'])}")
        a["o"] = {"werte": werte}
        # Im Datensatz steht c ohne Namen: frühere Lücken werden als Klammerausdruck eingesetzt (tools/inhalt_pruefen.py kennt nur Rechnungen)
        c_aus = []
        for c in e["c"]:
            c_aus.append(re.sub(r"\bL(\d+)\b", lambda m: "(" + c_aus[int(m.group(1)) - 1] + ")", c))
        if [als_zahl(rechne(c)) for c in c_aus] != werte:
            fehler.append(f"{k}: eingesetzte c-Ausdrücke ergeben andere Werte")
        a["c"] = c_aus
        if f["schablone"].count("□") != len(werte):
            fehler.append(f"{k}: {f['schablone'].count('□')} Kästchen, aber {len(werte)} Werte")
        if re.search(r"[a-zäöüß]", f["schablone"]):
            fehler.append(f"{k}: Kleinbuchstabe in der Schablone wäre eine Term-Vorlage (dann kein Zahlenfeld)")
        if KOMMA_LUECKE.search(e["text"]) or KOMMA_LUECKE.search(f["schablone"]):
            fehler.append(f"{k}: Komma direkt neben einer Lücke")
        # --- Selbstprüfung nach den Maßstäben der Gegenprüfung (Lückenwege) ---
        if len(werte) < 2:
            fehler.append(f"{k}: Lückenweg braucht mindestens zwei Lücken")
        if any(not isinstance(w, int) for w in werte):
            fehler.append(f"{k}: Lückenwerte müssen ganze Zahlen sein: {werte}")
        sichtbar = {"Text": e["text"], "Schablone": f["schablone"], "Tipp": e["h"], "Eingabehinweis": f.get("hinweis", "")}
        for w in werte:
            for ort, t in sichtbar.items():
                if steht_als_ziffer(w, t):
                    fehler.append(f"{k}: Lückenwert {w} steht als Zahl im {ort}")
                zw = steht_als_zahlwort(w, t)
                if zw:
                    fehler.append(f"{k}: Lückenwert {w} steht als Zahlwort „{zw}“ im {ort}")
        # Abhängigkeit: spätere Lücke muss sich ändern, wenn man eine frühere Lücke verändert
        abhaengig = []
        for j in range(1, len(e["c"])):
            bez = sorted({int(n) for n in re.findall(r"\bL(\d+)\b", e["c"][j]) if int(n) <= j})
            if not bez:
                continue
            geaendert = False
            for i in bez:
                for delta in (420, -420):          # 420 ist durch 2, 3, 4, 5, 6, 7, 10, 12 teilbar
                    env2 = {n: v for n, v in env.items()}
                    env2[f"L{i}"] = env[f"L{i}"] + delta
                    if rechne(e["c"][j], env2) != env[f"L{j+1}"]:
                        geaendert = True
            if geaendert:
                abhaengig.append(j + 1)
            else:
                fehler.append(f"{k}: Lücke {j+1} ändert sich nicht, wenn man eine frühere Lücke ändert")
        if not abhaengig:
            fehler.append(f"{k}: keine spätere Lücke hängt von einer früheren ab")
        if len(e["c"]) not in abhaengig:
            fehler.append(f"{k}: die letzte Lücke hängt von keiner früheren ab (wäre eine Nebenfrage)")
        ent = e.get("entscheidend")
        if ent not in range(1, len(werte) + 1):
            fehler.append(f"{k}: Feld entscheidend (Nummer der Lücke an der entscheidenden Stelle) fehlt oder ist falsch")
        elif not any(fb.get("luecke") == ent for fb in e["fehlbilder"]):
            fehler.append(f"{k}: zur entscheidenden Lücke {ent} gibt es kein Fehlbild")
        for fb in e["fehlbilder"]:
            n = fb.get("luecke")
            if n not in range(1, len(werte) + 1):
                fehler.append(f"{k}: Fehlbild mit unbekannter Lücke {n}")
                continue
            pruefe_fehlbild(k, fb, fb.get("antwort"), werte[n - 1], env)
    elif y == "zahl":
        wert = als_zahl(rechne(e["c"]))
        if wert != e["erwartet"]:
            fehler.append(f"{k}: nachgerechnet {wert}, von Hand erwartet {e['erwartet']}")
        a["o"] = {"wert": wert}
        for fb in e["fehlbilder"]:
            pruefe_fehlbild(k, fb, fb.get("antwort"), wert, {})
        if steht_als_ziffer(wert, e["h"]) and wert not in (1, 2, 3, 4, 5, 10):
            fehler.append(f"{k}: Ergebnis {wert} steht im Tipp")
        if e.get("einheit"):
            a["o"]["einheit"] = e["einheit"]
        a["c"] = e["c"]
    elif y == "auswahl":
        a["a"] = list(e["a"])
        a["o"] = {"index": e["richtig"]}
        if not 0 <= e["richtig"] < len(e["a"]):
            fehler.append(f"{k}: richtige Nummer {e['richtig']} gibt es nicht")
        if len(set(e["a"])) != len(e["a"]):
            fehler.append(f"{k}: zwei gleiche Antworten")
        if len(e["a"]) < 3:
            fehler.append(f"{k}: weniger als drei Antworten")
        if "a_rechnung" in e:
            if len(e["a_rechnung"]) != len(e["a"]):
                fehler.append(f"{k}: a_rechnung hat nicht so viele Einträge wie Antworten")
            else:
                vals = [float(rechne(x)) for x in e["a_rechnung"]]
                for i, v in enumerate(vals):
                    for j in range(i + 1, len(vals)):
                        if gleich(v, vals[j]):
                            fehler.append(f"{k}: Antworten {i} und {j} sind rechnerisch gleich ({v})")
                if not gleich(vals[e["richtig"]], e["a_wert"]):
                    fehler.append(f"{k}: richtige Antwort rechnet {vals[e['richtig']]}, erwartet {e['a_wert']}")
        falsch = {fb["index"] for fb in e["fehlbilder"] if "index" in fb}
        if falsch != set(range(len(e["a"]))) - {e["richtig"]}:
            fehler.append(f"{k}: zu jeder falschen Antwort gehört ein Fehlbild (fehlt: "
                          f"{sorted(set(range(len(e['a']))) - {e['richtig']} - falsch)})")
        for fb in e["fehlbilder"]:
            if "index" in fb and fb.get("antwort") != e["a"][fb["index"]]:
                fehler.append(f"{k}: Fehlbild {fb['index']} nennt einen anderen Text als die Antwort")
    elif y == "text":
        a["o"] = {"text": e["erwartet"]}
    else:
        fehler.append(f"{k}: Antwortform {y} ist hier nicht vorgesehen")
    if typ == "FD":
        if "erste Fehler" not in e["text"]:
            fehler.append(f"{k}: Fehler-Detektiv muss nach dem ERSTEN Fehler fragen")
        zeilen = len(re.findall(r"Zeile \d:", e["text"]))
        if y != "auswahl" or len(e["a"]) != zeilen or e["a"] != [f"In Zeile {i}" for i in range(1, zeilen + 1)]:
            fehler.append(f"{k}: Antworten müssen genau den {zeilen} Zeilen entsprechen")
        FEHLERZEILEN.append((k, e["richtig"] + 1))
    a["h"] = e["h"]
    a["w"] = e["w"]
    if len(e["w"]) < 15:
        fehler.append(f"{k}: Lösungsweg w zu kurz")
    if not e["h"]:
        fehler.append(f"{k}: Hinweis h fehlt")
    regel = REGELN.get(e["regel"])
    if regel is None:
        fehler.append(f"{k}: Regel {e['regel']} gibt es im Regel-Universum nicht")
    return {
        "kennung": k, "thema": thema, "lernkarte": e["karte"], "stufe": s, "typ": name, "antwortform": y,
        "regel": e["regel"], "regel_name": regel["name"] if regel else "?", "zaehlt": zaehlt,
        "fehlbilder": [{"luecke": fb.get("luecke"), "index": fb.get("index"), "antwort": fb.get("antwort"), "rechnung": fb.get("rechnung"),
                        "fehlbild": fb.get("fehlbild"), "regel_des_fehlbilds": fb.get("regel_des_fehlbilds"),
                        "beschreibung": fb["beschreibung"]} for fb in e["fehlbilder"]],
        "aufgabe": a,
    }


def thema_bauen(modul, thema, datei, bestand_datei, karten):
    teil = importlib.import_module("teile." + modul)
    d, texte, bauform, karte_zu_t, sach = bestand(bestand_datei)
    eintraege = []
    for e in teil.AUFGABEN:
        e = dict(e)
        e.setdefault("karte", e.get("karte"))
        eintraege.append(eintrag_bauen(e, thema, karte_zu_t, thema))
    # Mischung und Vollständigkeit je Lernkarte
    nach_karte = defaultdict(list)
    for e, roh in zip(eintraege, teil.AUFGABEN):
        nach_karte[e["lernkarte"]].append((e, roh["typ"]))
    for lk in karten:
        if lk not in karte_zu_t:
            fehler.append(f"{thema}/{lk}: Lernkarte gibt es im Bestand nicht")
        gruppe = nach_karte.get(lk, [])
        if len(gruppe) != 3:
            fehler.append(f"{thema}/{lk}: {len(gruppe)} Aufgaben statt genau drei")
        kuerzel = [t for _, t in gruppe]
        if kuerzel.count("LW") > 1:
            fehler.append(f"{thema}/{lk}: mehr als ein Lückenweg")
        if kuerzel.count("FD") > 1:
            fehler.append(f"{thema}/{lk}: mehr als ein Fehler-Detektiv")
        if not set(kuerzel) & ZAEHLENDE_FORMEN:
            fehler.append(f"{thema}/{lk}: keine zählende Aufgabe der Formen Umkehren/Zwei Wege/Brücke/Verfahren wählen/Anwenden")
        for e, t in gruppe:
            if t == "LW" and (e["stufe"] != 1 or e["zaehlt"] != "nein"):
                fehler.append(f"{e['kennung']}: Lückenweg muss Stufe 1 und zaehlt = nein sein")
            if t == "FD" and e["stufe"] != 3:
                fehler.append(f"{e['kennung']}: Fehler-Detektiv muss Stufe 3 sein")
    for ueber in set(nach_karte) - set(karten):
        fehler.append(f"{thema}: Lernkarte {ueber} steht nicht im Auftrag")
    # je Thema mindestens zweimal, wo es fachlich passt (Ausnahmen nennt das Teil-Modul)
    zaehl = Counter(e["typ"] for e in teil.AUFGABEN)
    for t in MINDESTENS_ZWEIMAL:
        if zaehl[t] < 2 and t not in getattr(teil, "PASST_NICHT", ()):
            fehler.append(f"{thema}: Form {TYP[t][0]} nur {zaehl[t]}-mal (mindestens zweimal, sonst in PASST_NICHT begründen)")
    # keine Dopplung zum Bestand
    for e in eintraege:
        t = e["aufgabe"]["f"]["text"]
        if t in texte:
            fehler.append(f"{e['kennung']}: Aufgabentext steht wörtlich im Bestand")
        if ohne_zahlen(t) in bauform:
            fehler.append(f"{e['kennung']}: Aufgabentext gleicht einer Bestandsaufgabe (nur andere Zahlen)")
    datei_inhalt = {
        "stand": teil.STAND,
        "flug": thema,
        "titel": teil.TITEL,
        "fuer": "Klasse 7",
        "klasse": 7,
        "themen": [bestand_datei],
        "hinweis": "Vorrat an Aufgaben in neuer Form (Auftrag 21). Nicht eingespielt. Kennungen mit K7.",
        "aufgaben": eintraege,
    }
    pfad = os.path.join(HIER, datei + ".json")
    with open(pfad, "w", encoding="utf-8") as f:
        json.dump(datei_inhalt, f, ensure_ascii=False, indent=1)
        f.write("\n")
    return eintraege, d


def inhalt_pruefen_lassen(eintraege, bestand_datei):
    """Hängt die neuen Aufgaben an eine Kopie der Themen-Datei und lässt tools/inhalt_pruefen.py laufen."""
    quelle = os.path.join(WURZEL, "inhalte", "themen", bestand_datei + ".json")
    d = json.load(open(quelle, encoding="utf-8"))
    d["aufgaben"] = d["aufgaben"] + [e["aufgabe"] for e in eintraege]
    with tempfile.TemporaryDirectory() as ordner:
        ziel = os.path.join(ordner, bestand_datei + ".json")
        json.dump(d, open(ziel, "w", encoding="utf-8"), ensure_ascii=False)
        lauf = subprocess.run([sys.executable, "-I", os.path.join(WURZEL, "tools", "inhalt_pruefen.py"), ziel],
                              capture_output=True, text=True)
    return lauf.returncode, (lauf.stdout + lauf.stderr)


def main():
    nur = sys.argv[1:] or [t[0] for t in THEMEN]
    alle, kennungen = [], Counter()
    print(f"{'Thema':34s} {'Karten':>6s} {'Aufg.':>5s}  Formen")
    for modul, thema, datei, bestand_datei, karten in THEMEN:
        if modul not in nur:
            continue
        eintraege, _ = thema_bauen(modul, thema, datei, bestand_datei, karten)
        alle += eintraege
        teil = importlib.import_module("teile." + modul)
        z = Counter(e["typ"] for e in teil.AUFGABEN)
        for e in eintraege:
            kennungen[e["kennung"]] += 1
        print(f"{thema:34s} {len({e['lernkarte'] for e in eintraege}):6d} {len(eintraege):5d}  "
              + " ".join(f"{k}:{v}" for k, v in sorted(z.items())))
        code, text = inhalt_pruefen_lassen(eintraege, bestand_datei)
        if code != 0:
            fehler.append(f"{thema}: inhalt_pruefen.py Code {code}\n{text[:2000]}")
        else:
            print(f"{'':34s} inhalt_pruefen.py: Code 0")
    for k, n in kennungen.items():
        if n > 1:
            fehler.append(f"Kennung {k} kommt {n}-mal vor")
    print(f"\nGesamt: {len(alle)} Aufgaben, {len({(e['thema'], e['lernkarte']) for e in alle})} Lernkarten")
    print("Formen:", dict(Counter(e["typ"] for e in alle)))
    print("zaehlt:", dict(Counter(e["zaehlt"] for e in alle)))
    print("Stufen:", dict(sorted(Counter(e["stufe"] for e in alle).items())))
    print("Antwortformen:", dict(Counter(e["antwortform"] for e in alle)))
    if not sys.argv[1:]:
        print("Fehlerzeilen der Fehler-Detektive:", dict(sorted(Counter(z for _, z in FEHLERZEILEN).items())))
    if fehler:
        print("\nFEHLER:")
        for f in fehler:
            print(" -", f)
        sys.exit(1)
    print("\nOK")


if __name__ == "__main__":
    main()
