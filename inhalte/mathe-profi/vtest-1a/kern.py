"""Kern der Runde VT1A (Verstehen in Tests, Klasse 5): Hilfsfunktionen zum Schreiben der Aufgaben.
Die Dateien th_*.py rufen neu(...) auf; bauen.py prüft alles und schreibt die JSON-Dateien."""
import itertools
import os
import sys

sys.dont_write_bytecode = True
HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
sys.path.insert(0, os.path.join(WURZEL, "tools"))
import inhalt_pruefen as ip      # noqa: E402

A = []
def _lagenfolge(n_runden=10, k=4, saat=0):
    """Gleichmäßig verteilte, unregelmäßige Lage der richtigen Antwort (festes Saatkorn, damit die Runde reproduzierbar bleibt)."""
    import random
    r = random.Random(saat)
    while True:
        f = [i for _ in range(n_runden) for i in range(k)]
        r.shuffle(f)
        if any(f[i] == f[i + 1] == f[i + 2] or (f[i + 1] - f[i] == f[i + 2] - f[i + 1] and abs(f[i + 1] - f[i]) == 1) for i in range(len(f) - 2)):
            continue
        if any(sum(1 for i in range(len(f) - p) if f[i] == f[i + p]) / (len(f) - p) > .4 for p in (2, 3, 4, 5, 6, 8)):
            continue
        return f


LAGEN_SAAT = 3
POSITION = {4: iter(_lagenfolge(saat=LAGEN_SAAT)), 5: itertools.cycle([3, 1, 4, 0, 2, 0, 4, 2, 1, 3])}
POOLS = ("test", "korrektur", "sicherung")
TYPEN_ERLAUBT = ("mehrschritt", "einkleidung", "umkehr", "darstellung", "rueckwaerts", "verknuepfen", "begruenden", "fehler", "transfer", "parameter", "pruefung")
FORMEN = ("anwenden", "umkehren", "verfahren_waehlen", "fehler_detektiv", "bruecke", "zwei_wege", "viele_antworten")


def Z(text, wert, c, zweit, w, fb, einheit=None, grafik=None):
    """Zahl. c: Rechenausdruck (für ip.rechne), zweit: zweite, unabhängige Rechnung (Ausdruck oder Zahl).
    fb: [(falscher Wert, Beschreibung, Rechnung)]; Rechnung = Ausdruck, dessen Wert der falsche Wert ist, oder True (von Hand gerechnet, Beschreibung nennt die Rechnung)."""
    o = {"wert": wert}
    if einheit:
        o["einheit"] = einheit
    d = {"y": "zahl", "f": {"text": text}, "o": o, "c": c, "w": w}
    if grafik:
        d["f"]["grafik"] = grafik
    return d, [zweit], fb


def W(text, richtig, falsch, w, probe, grafik=None):
    """Auswahl mit mindestens 4 Optionen. falsch: [(Antwort, Beschreibung, Prüfung)]; Prüfung = bool (im Quelltext gerechnet), der zeigt, dass die Antwort falsch ist
    und aus dem beschriebenen Fehler entsteht (oder None: nur von Hand gelesen). probe: bool, dass die richtige Antwort stimmt."""
    n = len(falsch) + 1
    assert n in (4, 5), text
    p = next(POSITION[n])
    antworten = [f[0] for f in falsch]
    antworten.insert(p, richtig)
    fb = {}
    for i, f in enumerate(falsch):
        fb[i if i < p else i + 1] = (f[1], f[2])
    d = {"y": "auswahl", "f": {"text": text}, "a": antworten, "o": {"index": p}, "w": w}
    if grafik:
        d["f"]["grafik"] = grafik
    return d, probe, fb


def neu(thema, lz, pool, typ, bau, form=None, regel=None, ohne=None, zweifel=None, lehrplan="M5 3", idee=None):
    assert idee, (thema, lz, pool, "idee fehlt")
    assert pool in POOLS and typ in TYPEN_ERLAUBT and (form is None or form in FORMEN), (thema, lz, pool, typ, form)
    assert (regel is None) == bool(ohne), (thema, lz, "Regel oder Begründung ohne Regel angeben, nicht beides")
    aufgabe, zweit, fb = bau
    A.append(dict(thema=thema, lz=lz, pool=pool, typ=typ, form=form, regel=regel, ohne=ohne, zweifel=zweifel, lehrplan=lehrplan, idee=idee,
                  s=ip.STUFE_VON[typ], aufgabe=aufgabe, zweit=zweit, fb=fb, nr=len(A)))
