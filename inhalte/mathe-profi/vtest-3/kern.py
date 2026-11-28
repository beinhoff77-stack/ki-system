"""Hilfen für die Runde vtest-3 (Kürzel VT3): baut die Einträge im Format von tools/vtest_pruefen.py.
Nur Inhalte. Nichts wird eingespielt."""
import json
from pathlib import Path

HIER = Path(__file__).resolve().parent
WURZEL = HIER.parent.parent.parent
RBL = json.loads((WURZEL / "inhalte/plan/regelbezug-lernkarten.json").read_text(encoding="utf-8"))["themen"]
STAND = "2026-11-28"
POOLREIHE = {"test": 0, "korrektur": 1, "sicherung": 2}

BAUART = {
    "fehler_detektiv": "Fehler-Detektiv (Zeile finden und richtigstellen)",
    "umkehren": "Umkehren (vom Ergebnis zur Ausgangsgröße)",
    "verfahren_waehlen": "Verfahren wählen",
    "zwei_wege": "zwei Wege vergleichen",
    "bruecke": "Brücke zwischen zwei Darstellungen",
    "anwenden": "Transfer auf eine neue Situation",
}
TYPNAME = {
    "begruenden": "Begründung wählen",
    "parameter": "Was-wäre-wenn",
    "umkehr": "Umkehren",
    "rueckwaerts": "rückwärts denken",
    "transfer": "Transfer",
    "darstellung": "Darstellung wechseln",
    "fehler": "Fehler finden",
    "verknuepfen": "Verknüpfen",
}


class Bau:
    """Sammelt die Aufgaben einer Einheit."""

    def __init__(self, thema, lehrplan, unterschied):
        self.thema = thema
        self.lehrplan = lehrplan
        self.unterschied = unterschied      # lernkarte -> Satz: was die Übungen tun
        self.liste = []

    def _regel(self, lz):
        lk = ((RBL.get(self.thema) or {}).get("lernkarten") or {}).get(lz) or {}
        return lk.get("regel")

    def _basis(self, lz, pool, stufe, typ, form, y, text, w, abgr, runden=None):
        assert pool in POOLREIHE and stufe in (2, 3), (lz, pool, stufe)
        art = BAUART.get(form) or TYPNAME.get(typ) or typ
        e = {
            "kennung": None,
            "thema": self.thema,
            "lernkarte": lz,
            "pool": pool,
            "typ": typ,
            "form": form,
            "stufe": stufe,
            "zaehlt": "ja",
            "lehrplan": self.lehrplan,
            "abgrenzung": (abgr or self.unterschied[lz]) + f" Diese Aufgabe: {art}.",
            "aufgabe": {"l": lz, "t": lz, "p": pool, "s": stufe, "y": y, "f": {"text": text}, "w": w},
        }
        if pool == "test":
            e["ersetzt_test"] = True
        rg = self._regel(lz)
        if rg:
            e["regel"] = rg
        if runden is not None:
            e["runden"] = runden
        self.liste.append(e)
        return e

    # ---- Antworttypen ----
    def zahl(self, lz, pool, stufe, typ, form, text, wert, rech, fb, w, einheit=None, runden=None, abgr=None):
        e = self._basis(lz, pool, stufe, typ, form, "zahl", text, w, abgr, runden)
        e["aufgabe"]["o"] = {"wert": wert} | ({"einheit": einheit} if einheit else {})
        e["loesung_rechnung"] = rech
        e["fehlbilder"] = []
        for f in fb:
            a, r, b = f[:3]
            d = {"antwort": a, "rechnung": r, "beschreibung": b, "fehlbild": None, "regel_des_fehlbilds": None}
            if len(f) > 3:
                d["runden"] = f[3]
            e["fehlbilder"].append(d)
        return e

    def luecken(self, lz, pool, stufe, typ, form, text, schablone, werte, rechs, fb, w, abgr=None):
        e = self._basis(lz, pool, stufe, typ, form, "luecken", text, w, abgr)
        e["aufgabe"]["f"]["schablone"] = schablone
        e["aufgabe"]["f"]["hinweis"] = "Je Feld eine ganze Zahl."
        e["aufgabe"]["o"] = {"werte": werte}
        e["loesung_rechnung"] = rechs
        e["fehlbilder"] = [{"luecke": l, "antwort": a, "rechnung": r, "beschreibung": b, "fehlbild": None, "regel_des_fehlbilds": None}
                           for (l, a, r, b) in fb]
        return e

    def auswahl(self, lz, pool, stufe, typ, form, text, opts, idx, fb, w, abgr=None):
        """fb: {index: Beschreibung} oder {index: (Beschreibung, Rechnung)} für alle falschen Möglichkeiten."""
        e = self._basis(lz, pool, stufe, typ, form, "auswahl", text, w, abgr)
        # Die Reihenfolge der Optionen wird erst in zusammen() festgelegt (Platz der richtigen Option, siehe plaetze()).
        e["aufgabe"]["a"] = list(opts)
        e["aufgabe"]["o"] = {"index": idx}
        e["fehlbilder"] = []
        for i, v in sorted(fb.items()):
            d = {"index": i, "antwort": opts[i], "beschreibung": v if isinstance(v, str) else v[0], "fehlbild": None, "regel_des_fehlbilds": None}
            if not isinstance(v, str):
                d["rechnung"] = v[1]
            e["fehlbilder"].append(d)
        return e


def plaetze(out, seed=20261128):
    """Legt für alle Auswahl-Aufgaben den Platz der richtigen Option fest: unregelmäßig (festes Seed, Rückverfolgung),
    jeder Platz etwa ein Viertel, nie zweimal derselbe Platz hintereinander (auch über Lernziele hinweg),
    keine Folge von drei Aufgaben mit gleichem Schritt (mod 4). Ordnet Optionen und Fehlbilder entsprechend um."""
    import random
    es = [e for liste in out.values() for e in liste if e["aufgabe"]["y"] == "auswahl"]
    n = len(es)
    rng = random.Random(seed)
    grenze = -(-n // 4)
    folge = []
    zaehl = [0, 0, 0, 0]

    def geht(p):
        if folge and folge[-1] == p: return False
        if zaehl[p] >= grenze: return False
        if len(folge) >= 2:
            d1 = (folge[-1] - folge[-2]) % 4
            d2 = (p - folge[-1]) % 4
            if d1 == d2: return False
        return True

    def los(i):
        if i == n: return min(zaehl) >= n // 4
        if n - i < sum(max(0, n // 4 - z) for z in zaehl): return False
        cand = [0, 1, 2, 3]
        rng.shuffle(cand)
        for p in cand:
            if geht(p):
                folge.append(p); zaehl[p] += 1
                if los(i + 1): return True
                folge.pop(); zaehl[p] -= 1
        return False

    assert los(0), "keine Platzfolge gefunden"
    for e, ziel in zip(es, folge):
        a = e["aufgabe"]
        idx = a["o"]["index"]
        opts = a["a"]
        rest = [i for i in range(len(opts)) if i != idx]
        reihe = rest[:ziel] + [idx] + rest[ziel:]
        neu = {alt: pos for pos, alt in enumerate(reihe)}
        a["a"] = [opts[i] for i in reihe]
        a["o"] = {"index": ziel}
        for f in e["fehlbilder"]:
            f["index"] = neu[f["index"]]
        e["fehlbilder"].sort(key=lambda f: f["index"])


def zusammen(baus, kuerzel="VT3"):
    """Kennungen fortlaufend vergeben, Lernziele in Reihenfolge der Bauten."""
    n = 0
    out = {}
    for b in baus:
        # innerhalb jedes Lernziels: Pool-Reihenfolge test, korrektur, sicherung (Reihenfolge des Hinzufügens bleibt sonst erhalten)
        lzs = []
        for e in b.liste:
            if e["lernkarte"] not in lzs:
                lzs.append(e["lernkarte"])
        feste = []
        for lz in lzs:
            xs = [e for e in b.liste if e["lernkarte"] == lz]
            xs.sort(key=lambda e: POOLREIHE[e["pool"]])
            feste += xs
        for e in feste:
            n += 1
            e["kennung"] = f"{kuerzel}-{n:03d}"
        out[b.thema] = feste
    plaetze(out)
    return out
