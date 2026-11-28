"""Prüfhilfen für vtest-1b (aus rollend-15/bauen.py übernommen und gekürzt): Zahlen im Text, Namensprüfung über Prüfsummen, Doppelungsprüfung gegen den Bestand,
Fehlbild-Rechnungen und Fehlbild-Zahlen. Keine Aufgaben hier."""
import ast as _ast
import difflib
import hashlib
import math
import os
import re
import sys
from fractions import Fraction as F

sys.dont_write_bytecode = True
import kern                      # noqa: E402
from kern import ip, WURZEL      # noqa: E402

ZAHL = re.compile(r"[−-]?\d+(?:[  ]\d{3})*(?:[,.]\d+)?")
bau_ohne_zahl = lambda t: re.sub(r"\s+", " ", ZAHL.sub("#", t)).strip()
KOMMA_LUECKE = re.compile(r"\d\s*,\s*[①②③④⑤□]")
KOMMA_NEBEN = re.compile(r"[①②③④⑤□],|,[①②③④⑤□]")
ZWEIDEUTIG = re.compile(r"\d/\d+[a-zA-Z]|/\([^()]*\(|\)\)/")


HOCH = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
HOCHLAUF = re.compile(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+")


def name_treffer(t, summen=frozenset({"8535e86c8118", "6a61eb7383e8", "ac818c81a10c"})):
    """Verbotene Vornamen nur über Prüfsummen (sha256, erste 12 Zeichen, kleingeschrieben) – wie in den früheren Runden, keine Namen im Klartext."""
    return {__import__("hashlib").sha256(w.lower().encode()).hexdigest()[:12] for w in re.findall(r"\w+", t)} & set(summen)


def zahlen_im(text):
    text = HOCHLAUF.sub(lambda m: " " + m.group(0).translate(HOCH) + " ", text)   # Hochzahlen zählen als Zahlen im Text
    r = set()
    for m in ZAHL.findall(text):
        s = re.sub(r"[  ]", "", m).replace("−", "").replace("-", "").replace(",", ".")
        r.add(F(s))
    return r


def texte_von(q):
    return [q["f"]["text"], q.get("h", ""), q["w"]] + list(q.get("a", [])) + [q["f"].get("hinweis", ""), q["f"].get("schablone", "")]



# ═════════ Doppelungsprüfung über Zahlen, Sollwert und Wortlaut ═════════
# Der Vergleich über den maskierten Fragetext (Bauplan) erkennt nur Aufgaben mit gleichem Wortlaut. Hier wird jede neue Aufgabe zusätzlich
# gegen ALLE Aufgaben derselben Einheit im Bestand (inhalte/themen/<datei>.json, das sind auch die Generator-Ausgaben) und gegen alle
# Aufgaben der früheren Runden (rollend-1 bis rollend-13) über Zahlenmenge, Sollwert und Wortlaut verglichen.
DP_STOP = set("wieviel viele welche welcher wird werden sind ist hat haben eine einen einem eines dann auch nicht noch sich oder aber nach beim vom zum zur dass dieser wenn immer jede jeder jedes".split())
DP_EINHEITHOCH = re.compile(r"(?<=[A-Za-zµ])[⁰¹²³⁴⁵⁶⁷⁸⁹]+")    # Hochzahl an einer Einheit (m², cm³) ist keine Zahl der Aufgabe
DP_ZEHNER = re.compile(r"10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]")
DP_PI_REST = F(14, 100)                                            # 3,14 ist vorgegeben und zählt nicht als gemeinsame Nachkommastellen


def dp_zahlen(t):
    t = HOCHLAUF.sub(lambda m: " " + m.group(0).translate(HOCH) + " ", DP_EINHEITHOCH.sub("", t))
    return {F(re.sub(r"[  ]", "", m).replace("−", "").replace("-", "").replace(",", ".")) for m in ZAHL.findall(t)}


def dp_merk(q):
    t = q["f"].get("text", "")
    o = q["o"]
    return dict(t=t, N=dp_zahlen(t), S=F(str(o["wert"])) if "wert" in o else None, M=bau_ohne_zahl(t),
                W={w for w in re.findall(r"[a-zäöüß]{4,}", t.lower())} - DP_STOP)


def dp_dez(S):
    """Nachkommaanteile der Dezimalzahlen (ohne den Rest von 3,14)"""
    return {n - (n.numerator // n.denominator) for n in S if n.denominator != 1} - {DP_PI_REST}


def dp_fein(x):
    return (x * 1000).denominator == 1 and (x * 100).denominator != 1


def dp_vergleich(a, b):
    """a: Aufgabe der Runde, b: Aufgabe aus dem Bestand (beide als dp_merk). Liefert den Grund der Ähnlichkeit oder None."""
    jac = lambda X, Y: len(X & Y) / max(1, len(X | Y))
    if not (a["N"] & b["N"]) and len(a["W"] & b["W"]) < 3 and a["M"] != b["M"] and not (dp_dez(a["N"]) & dp_dez(b["N"])):
        return None     # Vorfilter: keine gemeinsame Zahl, kaum gemeinsame Wörter
    sm = difflib.SequenceMatcher(None, a["M"], b["M"])
    ratio = sm.ratio() if (abs(len(a["M"]) - len(b["M"])) < 40 and sm.real_quick_ratio() >= .7 and sm.quick_ratio() >= .7) else 0
    ws, jn = jac(a["W"], b["W"]), jac(a["N"], b["N"])
    gleich = a["S"] is not None and a["S"] == b["S"]
    da, db = dp_dez(a["N"]), dp_dez(b["N"])
    if gleich and jn >= .99 and (len(a["N"]) >= 2 or (a["N"] and max(a["N"]) >= 50)):
        return "gleiche Zahlenmenge und gleicher Sollwert (ohne Maskierung der Zahlen verglichen)"
    if gleich and len(a["N"]) >= 2 and jn >= .75 and ws >= .2:
        return "gleiche Zahlen und gleicher Sollwert"
    if gleich and jn >= .99 and len(a["N"]) >= 3 and ws >= .15:
        return "dieselbe Zahlenmenge und gleicher Sollwert"
    if gleich and jn >= .5 and len(a["N"]) >= 4 and DP_ZEHNER.search(a["t"]) and DP_ZEHNER.search(b["t"]):
        return "Zehnerpotenzen mit fast denselben Zahlen und gleichem Sollwert"
    if ratio >= .9:
        return "fast gleicher Wortlaut"
    if jn >= .99 and len(a["N"]) >= 2 and ws >= .5:
        return "gleiche Zahlen im gleichen Sachverhalt"
    if jn >= .99 and ratio >= .8 and ws >= .25:
        return "gleiche Zahlen, fast gleicher Wortlaut"
    if gleich and (a["S"].denominator != 1 or a["S"] >= 10) and ws >= .3 and len(a["W"] & b["W"]) >= 4:
        return "gleicher Sollwert bei ähnlichem Sachverhalt"
    if da & db and ratio >= .7 and ws >= .4:
        return "gleicher Aufbau mit denselben Nachkommastellen"
    if len(da & db) >= 2 and any(dp_fein(x) for x in da & db):
        return "dieselben Nachkommastellen in mehreren Zahlen"
    return None



# ═════════ Hilfen für Lücken und Fehlbilder ═════════
GGT = re.compile(r"ggT\(\s*(\(?-?\d+\)?)\s*,\s*(\(?-?\d+\)?)\s*\)")
PLATZ = re.compile(r"\{(\d+)\}")


def setze_ein(ausdruck, frueher):
    """{n} durch den Wert der n-ten Lücke (ab 1) ersetzen, ggT(a, b) ausrechnen. Gibt den fertigen Ausdruck zurück."""
    def ers(m):
        n = int(m.group(1))
        assert 1 <= n <= len(frueher), (ausdruck, "Verweis auf eine spätere oder fehlende Lücke", n)
        return f"({frueher[n - 1]})"
    t = PLATZ.sub(ers, ausdruck)
    return GGT.sub(lambda m: str(math.gcd(int(m.group(1).strip("()")), int(m.group(2).strip("()")))), t)


MATHENAMEN = re.compile(r"\b(sqrt|sin|cos|tan|asin|acos|atan|pi|floor)\b")


def _wurzeln(t, quot=False):
    """wurzel(Ausdruck) -> ganze Zahl (nur bei vollständigen Quadraten), damit der Anker für tools/inhalt_pruefen.py lesbar bleibt."""
    while "wurzel(" in t:
        i = t.rindex("wurzel(")
        tiefe, j = 0, i + 6
        while True:
            tiefe += (t[j] == "(") - (t[j] == ")")
            if tiefe == 0:
                break
            j += 1
        inner = ip.rechne(t[i + 7:j])
        rn, rd_ = math.isqrt(inner.numerator), math.isqrt(inner.denominator)
        assert rn * rn == inner.numerator and rd_ * rd_ == inner.denominator, (t, "keine exakte Wurzel")
        r = F(rn, rd_)
        r = str(int(r)) if r.denominator == 1 else str(float(r))
        t = t[:i] + (f"(({t[i + 7:j]}) / {r})" if quot else str(r)) + t[j + 1:]
    return t


def wert_von_c(ausdruck, frueher):
    t = _wurzeln(setze_ein(str(ausdruck), frueher))
    if MATHENAMEN.search(t):                       # nur für Fehlbild-Rechnungen: Gleitkomma, Winkel in Grad
        v = float(kern.rechne_mathe(t))
        return v, t
    v = ip.rechne(t)
    return (int(v) if v.denominator == 1 else v), t



def fb_pruefen(kenn, ort, wert, rechnung, frueher=()):
    """Das Fehlbild nennt eine Rechnung: sie muss den falschen Wert wirklich ergeben. Rückgabe: True = nachgerechnet, False = keine Rechnung."""
    assert rechnung is not None, (kenn, ort, wert, "Fehlbild ohne Rechnung (4. Eintrag: Ausdruck, Funktion oder False)")
    if rechnung is False:
        return False
    if callable(rechnung):
        assert rechnung() is True, (kenn, ort, wert, "Fehlbild stimmt nicht")
        return True
    v, t = wert_von_c(rechnung, list(frueher))
    nd = max(2, len(str(wert).split(".")[1]) if "." in str(wert) else 0)
    ok = (not isinstance(v, float) and F(v) == ip.zahlwert(wert)) or round(float(v), nd) == float(wert)
    assert ok, (kenn, ort, "Fehlbild: Rechnung", t, "ergibt", float(v), "nicht", wert)
    return True


import ast as _ast

FB_ZAHL_FEHLER = []
FB_ZAHL_OK = {}      # (Kennung, Wert): Zahl in der Fehlbild-Beschreibung, die weder in der Aufgabe noch in der Rechnung steht – von Hand nachgerechnet (hier: keine)
WURZEL_BEHAUPTUNG = re.compile(r"√\(?(\d+(?:,\d+)?)\)?\s*≈\s*(\d+(?:,\d+)?)")
SMALL = {F(0), F(1), F(2)}


def _teilwerte(ausdruck):
    """Alle Zwischenwerte eines Ausdrucks (jeder Teilausdruck, Gleitkomma mit Mathe-Funktionen, Winkel in Grad)."""
    r = set()
    try:
        baum = _ast.parse(str(ausdruck), mode="eval")
    except SyntaxError:
        return r
    for kn in _ast.walk(baum):
        if isinstance(kn, (_ast.BinOp, _ast.UnaryOp, _ast.Call, _ast.Constant)):
            try:
                v = eval(compile(_ast.Expression(kn), "<fb>", "eval"), {"__builtins__": {}}, dict(kern.MATHE))
            except Exception:
                continue
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                r.add(F(str(round(v, 9))) if isinstance(v, float) else F(v))
    return r


def _mit_rundung(werte):
    r = set()
    for v in werte:
        r.add(abs(v))
        for k in range(0, 4):
            r.add(abs(F(str(round(float(v), k)))))
    return r


def fb_zahlen_pruefen(kenn, wert, beschr, rechnung, q, soll_vor=()):
    """Jede Zahl in der Fehlbild-Beschreibung muss aus der Aufgabe oder aus der Rechnung des Fehlbilds stammen (Text ↔ Zahl)."""
    for m in WURZEL_BEHAUPTUNG.finditer(beschr):      # „√N ≈ x“ in der Beschreibung muss stimmen (auf die genannten Stellen)
        rad, beh = (float(g.replace(",", ".")) for g in m.groups())
        st = len(m.group(2).split(",")[1]) if "," in m.group(2) else 0
        assert round(math.sqrt(rad), st) == beh, (kenn, wert, "Wurzelbehauptung in der Beschreibung stimmt nicht", m.group(0))
    gemeint = zahlen_im(beschr)
    if not gemeint:
        return
    erlaubt = set(SMALL)
    for t in texte_von(q):
        erlaubt |= zahlen_im(t)
    if isinstance(rechnung, str):
        r = rechnung
        for n, v in enumerate(soll_vor, 1):
            r = r.replace("{%d}" % n, "(%s)" % v)
        erlaubt |= _teilwerte(r)
    if isinstance(wert, (int, float)):
        erlaubt.add(F(str(wert)))
    erlaubt = _mit_rundung(erlaubt)
    fremd = {x for x in gemeint if abs(x) not in erlaubt}
    if fremd and not FB_ZAHL_OK.get((kenn, wert)):
        FB_ZAHL_FEHLER.append((kenn, wert, sorted(float(x) for x in fremd), beschr))


