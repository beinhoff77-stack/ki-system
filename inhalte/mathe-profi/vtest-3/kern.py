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


_ZAEHL = 0


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
        # Platz der richtigen Option gleichmäßig verteilen (die App mischt nach Stand der Vorprüfung nicht):
        # fortlaufender Zähler über alle Auswahl-Aufgaben, Platz = (3 · Zähler + 1) mod 4; aufeinanderfolgende Aufgaben haben nie denselben Platz
        global _ZAEHL
        ziel = (3 * _ZAEHL + 1) % 4
        _ZAEHL += 1
        rest = [i for i in range(len(opts)) if i != idx]
        reihe = rest[:ziel] + [idx] + rest[ziel:]
        neu = {alt: pos for pos, alt in enumerate(reihe)}
        opts = [opts[i] for i in reihe]
        fb = {neu[i]: v for i, v in fb.items()}
        idx = ziel
        e["aufgabe"]["a"] = list(opts)
        e["aufgabe"]["o"] = {"index": idx}
        e["fehlbilder"] = []
        for i, v in sorted(fb.items()):
            d = {"index": i, "antwort": opts[i], "beschreibung": v if isinstance(v, str) else v[0], "fehlbild": None, "regel_des_fehlbilds": None}
            if not isinstance(v, str):
                d["rechnung"] = v[1]
            e["fehlbilder"].append(d)
        return e


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
    return out
