"""Mathe-Profi: Eingangsdiagnose auf Papier (frühere Klassen), zwei Blätter, 30 Minuten.

Aufruf: python3 -I inhalte/mathe-profi/diagnose-1/bauen.py
Schreibt k8-diagnose.html (für Kind 2, Stoff Klasse 5 bis 7) und k5-diagnose.html (für Kind 1, Grundlagen für die kommenden Flüge).
Jede Lösung wird im Programm berechnet und auf einem zweiten Weg nachgerechnet; jede Fehlantwort wird aus einem Fehlermodell
berechnet und muss von der richtigen Lösung und von der anderen Fehlantwort verschieden sein.
Geprüft wird außerdem: Kennungen stehen in kennungen.json, Themen gibt es in inhalte/themen/, Flug und Thema passen zu plan.py,
die Flüge der Kind-2-Blätter stehen NICHT in der Route von Kind 2 (route.md).
Nur Inhalte. Keine Namen, keine Lerndaten, keine Ergebnisse.
"""
import ast
import json
import math
import os
import re
from fractions import Fraction as F

HIER = os.path.dirname(os.path.abspath(__file__))
MP = os.path.dirname(HIER)                      # inhalte/mathe-profi
THEMEN = os.path.join(os.path.dirname(MP), "themen")
M = "−"
NB = " "


# ───────────────────────────── Hilfen ─────────────────────────────
def z(n):
    """ganze Zahl, echtes Minus, Tausender mit festem Leerzeichen ab vier Stellen"""
    s = f"{abs(n):,}".replace(",", NB)
    return (M + s) if n < 0 else s


def dez(x):
    """Dezimalzahl mit Komma (x muss endlich darstellbar sein)"""
    x = F(x)
    for k in range(0, 9):
        if (x * 10 ** k).denominator == 1:
            s = str(abs(int(x * 10 ** k))).rjust(k + 1, "0")
            if k:
                s = s[:-k] + "," + s[-k:]
            return (M + s) if x < 0 else s
    raise ValueError(x)


def k(n):
    return f"({z(n)})" if n < 0 else z(n)


def fr(a, b):
    return f'<span class="fr"><span>{a}</span><span>{b}</span></span>'


def frac(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else fr(x.numerator, x.denominator)


# ───────────────────────────── Prüfung gegen das Repo ─────────────────────────────
KEN = {e["kennung"]: e for e in json.load(open(os.path.join(MP, "regeln-uebersicht", "kennungen.json"), encoding="utf-8"))["kennungen"]}


def flug_tabelle():
    src = open(os.path.join(MP, "lehrplan-kinder", "plan.py"), encoding="utf-8").read()
    for node in ast.parse(src).body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "FLUG":
            return ast.literal_eval(node.value)
    raise SystemExit("FLUG in plan.py nicht gefunden")


FLUG = flug_tabelle()


def route_fluege():
    t = open(os.path.join(MP, "lehrplan-kinder", "route.md"), encoding="utf-8").read()
    i1, i2 = t.index("## Kind 1"), t.index("## Kind 2")
    pick = lambda s: set(re.findall(r"\| \*\*([a-z0-9-]+)\*\* ", s))
    k1 = pick(t[i1:i2])
    k2 = pick(t[i2:t.index("### Abschnitt 5", i2)])      # Abschnitt 5 (Vorgriff Klasse 9) ist nicht eingestellt
    return k1, k2


ROUTE1, ROUTE2 = route_fluege()


def pruefe_zuordnung(A, kind):
    for a in A:
        if a["kennung"]:
            assert a["kennung"] in KEN, a["kennung"]
        fl, th = a["flug"]
        assert fl in FLUG and th in FLUG[fl][2], (fl, th)
        assert os.path.exists(os.path.join(THEMEN, th + ".json")), th
        if kind == 8:
            assert fl not in ROUTE2, f"{fl} steht in der Route von Kind 2 – dann ist es keine Lücke aus früheren Klassen"
        else:
            assert fl in ROUTE1, f"{fl} steht nicht in der Route von Kind 1"


# ───────────────────────────── Zeichnungen (SVG) ─────────────────────────────
def svg_l_figur():
    s = 20
    pts = [(0, 0), (10, 0), (10, 5), (6, 5), (6, 8), (0, 8)]      # cm, y nach oben
    px = [(12 + x * s, 12 + (8 - y) * s) for x, y in pts]
    umfang = sum(abs(pts[i][0] - pts[i - 1][0]) + abs(pts[i][1] - pts[i - 1][1]) for i in range(6))
    poly = " ".join(f"{x},{y}" for x, y in px)
    svg = (f'<svg width="270" height="190" viewBox="0 0 270 190" xmlns="http://www.w3.org/2000/svg" style="font:11px sans-serif">'
           f'<polygon points="{poly}" fill="#eee" stroke="#000" stroke-width="1.6"/>'
           f'<text x="{12 + 5 * s}" y="{12 + 8 * s + 15}" text-anchor="middle">10 cm</text>'
           f'<text x="8" y="{12 + 4 * s}" text-anchor="end" transform="rotate(-90 8 {12 + 4 * s})" dy="-2" dx="0">8 cm</text>'
           f'<text x="{12 + 8 * s}" y="{12 + 5 * s - 4}" text-anchor="middle" dy="-3">4 cm</text>'
           f'<text x="{12 + 6 * s + 6}" y="{12 + 3.5 * s}" text-anchor="start" dy="3">3 cm</text>'
           f'<text x="266" y="{12 + 8 * s + 15}" text-anchor="end">(Skizze, nicht maßstäblich)</text></svg>')
    return svg, umfang


def svg_winkel(alpha=65):
    cx, cy, r, R = 125, 85, 34, 100
    ca, sa = math.cos(math.radians(alpha)), math.sin(math.radians(alpha))
    ex, ey = cx + R * ca, cy - R * sa
    fx, fy = cx - R * ca, cy + R * sa
    ax, ay = cx + r * ca, cy - r * sa
    la = math.radians(alpha / 2)
    lb = math.radians((alpha + 180) / 2)
    return (f'<svg width="260" height="170" viewBox="0 0 260 170" xmlns="http://www.w3.org/2000/svg" style="font:13px sans-serif">'
            f'<line x1="10" y1="{cy}" x2="245" y2="{cy}" stroke="#000" stroke-width="1.6"/>'
            f'<line x1="{fx:.1f}" y1="{fy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="#000" stroke-width="1.6"/>'
            f'<path d="M {cx + r} {cy} A {r} {r} 0 0 0 {ax:.1f} {ay:.1f}" fill="none" stroke="#000" stroke-width="1.2"/>'
            f'<text x="{cx + 52 * math.cos(la):.1f}" y="{cy - 52 * math.sin(la) + 4:.1f}" text-anchor="middle">{alpha}°</text>'
            f'<text x="{cx + 40 * math.cos(lb):.1f}" y="{cy - 40 * math.sin(lb) + 5:.1f}" text-anchor="middle" font-weight="bold">?</text></svg>')


def svg_zahlenstrahl(wert, anfang=2000, ende=3000, schritt=100):
    n = (ende - anfang) // schritt
    assert (wert - anfang) % (schritt // 2) == 0 and (wert - anfang) % schritt != 0     # genau zwischen zwei Strichen
    x0, w = 20, 420
    xs = lambda v: x0 + w * (v - anfang) / (ende - anfang)
    t = "".join(f'<line x1="{xs(anfang + i * schritt):.1f}" y1="{38 if i in (0, n) else 42}" x2="{xs(anfang + i * schritt):.1f}" y2="{58 if i in (0, n) else 52}" stroke="#000" stroke-width="1.4"/>' for i in range(n + 1))
    px = xs(wert)
    return (f'<svg width="470" height="92" viewBox="0 0 470 92" xmlns="http://www.w3.org/2000/svg" style="font:13px sans-serif">'
            f'<line x1="{x0}" y1="47" x2="{x0 + w}" y2="47" stroke="#000" stroke-width="1.6"/>{t}'
            f'<polygon points="{px - 8:.1f},6 {px + 8:.1f},6 {px:.1f},34" fill="#000"/>'
            f'<text x="{x0}" y="78" text-anchor="middle">{z(anfang)}</text><text x="{x0 + w}" y="78" text-anchor="middle">{z(ende)}</text></svg>')


def svg_anteil(teile, gefaerbt):
    b = 38
    r = "".join(f'<rect x="{6 + i * b}" y="6" width="{b}" height="40" fill="{"#aaa" if i < gefaerbt else "#fff"}" stroke="#000" stroke-width="1.4"/>' for i in range(teile))
    return f'<svg width="{12 + teile * b}" height="52" viewBox="0 0 {12 + teile * b} 52" xmlns="http://www.w3.org/2000/svg">{r}</svg>'


# ───────────────────────────── Aufgaben Kind 2 (Klasse 8, Stoff Klasse 5–7) ─────────────────────────────
def kind2():
    A = []

    def auf(nr, gruppe, kennung, flug, text, antwort, hoehe, richtig, weg, fehl, luecke):
        assert len(fehl) == 2 and all(f[0] != richtig for f in fehl) and fehl[0][0] != fehl[1][0], nr
        A.append(dict(nr=nr, gruppe=gruppe, kennung=kennung, flug=flug, text=text, antwort=antwort, h=hoehe, richtig=richtig, weg=weg, fehl=fehl, luecke=luecke))

    # 1 plus/minus mit negativer Zahl
    a, b, c = 6, 13, -4
    e = a - b - c
    pos = a
    pos -= b
    pos += -c                       # zweiter Weg: Zahlengerade, minus eine negative Zahl = nach rechts
    assert e == pos == -3
    fa, fb = a - b - abs(c), -e
    auf(1, "Zahlen und Rechenregeln", "rr.plusminus", ("z1", "zahlen.ganz"), f"Rechne aus: &nbsp; {a} {M} {b} {M} ({M}{abs(c)})", "= ______", 2.3, z(e),
        f"{a} {M} {b} = {z(a - b)}; minus ({M}{abs(c)}) heißt plus {abs(c)}: {z(a - b)} + {abs(c)} = {z(e)}",
        [(z(fa), f"{M} ({M}{abs(c)}) wie {M} {abs(c)} gerechnet: Doppelminus übersehen."), (z(fb), "Der Betrag stimmt, das Vorzeichen des Ergebnisses ist falsch.")],
        "Minus vor einer negativen Zahl dreht um (Doppelminus); Rechnen über die Null.")

    # 2 Vorzeichen bei Mal und Geteilt
    a1, b1, a2, b2 = -7, -6, -54, 9
    e1, e2 = a1 * b1, a2 // b2
    assert e1 == abs(a1) * abs(b1) and e2 * b2 == a2 and e2 == -6 and e1 == 42
    auf(2, "Zahlen und Rechenregeln", "rr.vorzeichen", ("z1", "zahlen.rechengesetze"),
        f"Rechne aus:<br>a) &nbsp; ({M}7) · ({M}6) &nbsp;&nbsp;&nbsp;&nbsp; b) &nbsp; ({M}54) : 9", "a) ______ &nbsp;&nbsp; b) ______", 2.2, f"a) {e1}; b) {z(e2)}",
        f"a) gleiche Vorzeichen: Plus, 7 · 6 = {e1}. b) verschiedene Vorzeichen: Minus, 54 : 9 = 6, also {z(e2)}. Probe b): {z(e2)} · 9 = {z(a2)}.",
        [(f"a) {z(-e1)}", f"Minus mal Minus als Minus gerechnet (a falsch, b richtig)."), (f"b) {abs(e2)}", "Minus vergessen beim Teilen (b falsch, a richtig).")],
        "Vorzeichenregel bei Mal und Geteilt.")

    # 3 Reihenfolge
    a, b, c, d = 2, 3, 4, 2
    e = a + b * c ** d
    assert e == eval("2+3*4**2") == a + (b * (c ** d)) == 50
    fa, fb = (a + b) * c ** d, a + (b * c) ** d
    assert len({e, fa, fb}) == 3
    auf(3, "Zahlen und Rechenregeln", "rr.reihenfolge", ("z1", "zahlen.rechengesetze"), f"Rechne aus. Schreib Zwischenschritte auf.<br>{a} + {b} · {c}²", "= ______", 2.6, z(e),
        f"Erst hoch: {c}² = {c ** d}. Dann Punkt: {b} · {c ** d} = {b * c ** d}. Dann Strich: {a} + {b * c ** d} = {e}.",
        [(z(fa), f"Strich zuerst: ({a} + {b}) · {c}² – von links nach rechts gerechnet."), (z(fb), f"Mal vor Hoch: ({b} · {c})² – das Quadrat gilt nur für die {c}.")],
        "Reihenfolge: Hoch vor Punkt vor Strich.")

    # 4 Stellenwert mit Komma
    e = F(7, 100) * 1000
    assert e == 70 and dez(e) == "70"
    ziffern = "7"
    assert F(ziffern + "0") == e                  # zweiter Weg: Ziffer 7 rückt zwei Stellen nach links über das Komma, Platz bleibt Null
    fa, fb = "0,07000", "7"
    assert F(fb.replace(",", ".")) != e and F(fa.replace(",", ".")) != e
    auf(4, "Zahlen und Rechenregeln", "rr.stellenwert", ("z4", "bruch.dezimal"), "Rechne aus (ohne Rechenweg):<br>0,07 · 1 000", "= ______", 1.8, "70",
        "Mal 1 000: jede Ziffer rückt drei Stellen nach links. 0,07 → 0,7 → 7 → 70.",
        [(fa, "Beim Malnehmen wurden einfach Nullen angehängt (Komma bleibt stehen)."), (fb, "Die Ziffern sind um eine Stelle zu wenig gerückt.")],
        "Stellenwert: Mal 10, 100, 1 000 mit Komma (Ziffern rücken).")

    # 5 Größen: Länge
    e = F("2.35") * 100
    assert e == 235 and F(235, 100) == F("2.35")
    fa, fb = "23,5", "0,0235"
    auf(5, "Größen", "id.verhaeltnisse.groesse", ("g1", "groessen.einheiten"), "Rechne um:<br>2,35 m = ______ cm", "", 1.8, "235",
        "1 m = 100 cm, kleinere Einheit, größere Zahl: 2,35 · 100 = 235.",
        [(fa, "Mal 10 statt mal 100 (Umrechnungszahl falsch)."), (fb, "Geteilt statt mal: falsche Richtung (kleinere Einheit braucht die größere Zahl).")],
        "Einheiten umrechnen: Richtung und Umrechnungszahl.")

    # 6 Größen: Fläche
    e = 4 * (100 * 100)
    assert e == 40000 and F(4) * 100 * 100 == e
    fa, fb = 4 * 100, 4 * 1000
    auf(6, "Größen", "id.verhaeltnisse.groesse", ("r1", "messen.flaechen"), "Rechne um:<br>4 m² = ______ cm²", "", 1.8, z(e),
        "1 m² ist ein Quadrat mit 100 cm mal 100 cm = 10 000 cm². Also 4 · 10 000 = 40 000.",
        [(z(fa), "Umrechnungszahl 100 wie bei der Länge (bei Flächen 100 · 100)."), (z(fb), "Umrechnungszahl 1 000 (Rechnung wie bei Litern/Kubik oder geraten).")],
        "Flächeneinheiten: die Umrechnungszahl ist das Quadrat der Längen-Zahl.")

    # 7 Kürzen
    a, b = 36, 48
    g = math.gcd(a, b)
    x, y = a, b
    for p in (2, 2, 3):                            # zweiter Weg: Primfaktor für Primfaktor
        assert x % p == 0 and y % p == 0
        x, y = x // p, y // p
    assert (x, y) == (a // g, b // g) == (3, 4) and math.gcd(x, y) == 1
    fa, fb = (18, 24), (24, 36)
    assert F(*fa) == F(a, b) and math.gcd(*fa) > 1 and F(*fb) != F(a, b) and fb == (a - 12, b - 12)
    auf(7, "Brüche und Prozent", "rr.kuerzen", ("z3", "bruch.brueche"), f"Kürze so weit wie möglich:<br>{fr(a, b)} = ______", "", 2.0, f"{x}/{y}",
        f"Beide durch 12 (größter gemeinsamer Teiler) oder Schritt für Schritt: :2 → 18/24, :3 → 6/8, :2 → 3/4.",
        [(f"18/24", "Nur einmal gekürzt, Kürzen nicht zu Ende geführt (Wert bleibt richtig)."), (f"24/36", "12 abgezogen statt geteilt – der Bruch hat dadurch einen anderen Wert.")],
        "Kürzen = oben und unten durch dieselbe Zahl teilen (nicht abziehen), bis es nicht mehr geht.")

    # 8 Brüche addieren
    p, q = F(2, 3), F(1, 4)
    e = p + q
    nenner = 12
    assert e == F(2 * 4 + 1 * 3, nenner) == F(11, 12) and nenner % 3 == 0 and nenner % 4 == 0
    fa, fb = (3, 7), (3, 12)
    assert F(*fa) != e and F(*fb) != e
    auf(8, "Brüche und Prozent", "rr.bruchrechnen", ("z5", "bruch.rechnen"), f"Rechne aus und schreibe das Ergebnis als Bruch:<br>{fr(2, 3)} + {fr(1, 4)} = ______", "", 2.4, "11/12",
        "Gemeinsamer Nenner 12: 8/12 + 3/12 = 11/12.",
        [("3/7", "Zähler plus Zähler, Nenner plus Nenner."), ("3/12 (auch 1/4)", "Gemeinsamer Nenner gefunden, aber die Zähler nicht mit erweitert.")],
        "Brüche addieren: erst gleiche Nenner (erweitern), dann nur die Zähler addieren.")

    # 9 Prozent
    e = F(15, 100) * 80
    assert e == 12 and F(80, 100) * 15 == e                      # 1 % sind 0,80 €
    fa, fb = 15 * 80, 80 - 15
    auf(9, "Brüche und Prozent", "id.verhaeltnisse.prozent", ("g3", "bruch.prozent"), "Wie viel sind 15 % von 80 €?<br>Antwort: ______ €", "", 2.2, "12",
        "1 % von 80 € sind 0,80 €. 15 · 0,80 € = 12 €. (Oder 15/100 · 80.)",
        [(z(fa), "Prozentzahl mit dem Grundwert malgenommen, durch 100 vergessen."), (z(fb), "Die Prozentzahl als Betrag abgezogen (15 € statt 15 %).")],
        "Prozent heißt „von hundert“: erst 1 %, dann mal die Prozentzahl.")

    # 10 L-Figur
    svg, umfang = svg_l_figur()
    e = 10 * 8 - 4 * 3
    assert e == 6 * 8 + 4 * (8 - 3) == 68                       # zweiter Weg: in zwei Rechtecke zerlegt
    fa, fb = 10 * 8, umfang
    assert umfang == 36
    auf(10, "Fläche und Winkel", "id.flaeche_raum.aus_dem_rechteck", ("r1", "messen.flaechen"), f"Wie groß ist der Flächeninhalt der Figur?<br>{svg}<br>Antwort: ______ cm²", "", 5.3, "68",
        "Ergänzen zum Rechteck: 10 · 8 = 80, minus die fehlende Ecke 4 · 3 = 12 → 68. Oder zerlegen: 6 · 8 + 4 · 5 = 48 + 20 = 68.",
        [(z(fa), "Ganzes Rechteck gerechnet, die fehlende Ecke nicht abgezogen."), (z(fb), "Umfang statt Fläche gerechnet (Randstrecken addiert).")],
        "Flächen aus Rechtecken: ergänzen oder zerlegen; Umfang und Fläche unterscheiden.")

    # 11 Dreieck
    g, h = 14, 9
    e = F(g * h, 2)
    assert e == 63 and F(g * h) / 2 == e and 2 * e == g * h        # Dreieck = halbes Parallelogramm
    fa, fb = g * h, g + h
    auf(11, "Fläche und Winkel", "id.flaeche_raum.aus_dem_rechteck", ("r7", "messen.flaechen_vielecke"),
        f"Ein Dreieck hat die Grundseite {g} cm. Die Höhe auf diese Seite ist {h} cm.<br>Wie groß ist die Fläche?<br>Antwort: ______ cm²", "", 2.4, "63",
        f"Das Dreieck ist ein halbes Rechteck: {g} · {h} : 2 = {g * h} : 2 = 63.",
        [(z(fa), "Das Halbieren vergessen (Fläche des ganzen Rechtecks)."), (z(fb), "Die beiden Maße addiert.")],
        "Dreiecksfläche = Grundseite mal Höhe geteilt durch 2.")

    # 12 Nebenwinkel
    al = 65
    e = 180 - al
    assert e == 115 and (360 - 2 * al) // 2 == e and al + e == 180
    fa, fb = 90 - al, al
    auf(12, "Fläche und Winkel", "id.geometrie.winkel", ("ge3", "geometrie.winkel"),
        f"Zwei Geraden schneiden sich. Ein Winkel ist {al}°. Wie groß ist der Winkel „?“ direkt daneben (die beiden zusammen bilden eine gerade Linie)?<br>{svg_winkel(al)}<br>Antwort: ______ °", "", 5.0, "115",
        "Eine gerade Linie ist ein gestreckter Winkel: 180°. 180° − 65° = 115°. (Zweiter Weg: 360° − 2 · 65° = 230°, die Hälfte ist 115°.)",
        [(z(fa), "Mit 90° statt 180° gerechnet (Ergänzung zum rechten Winkel)."), (z(fb), "Scheitelwinkel und Nebenwinkel verwechselt (gleicher Winkel angegeben).")],
        "Winkel an Geraden: Nebenwinkel ergänzen sich zu 180°.")

    # 13 Gegenrechnung
    mal, minus, erg = 4, 7, 29
    e = (erg + minus) // mal
    assert e * mal - minus == erg and [x for x in range(0, 200) if x * mal - minus == erg] == [e] and e == 9
    fa, fb = erg + minus, F(erg - minus, mal)
    assert fb == F(11, 2)
    auf(13, "Gleichung und Daten", "rr.gegenrechnung", ("a1", "gleichungen.einfach"),
        f"Ich denke mir eine Zahl. Ich rechne mal {mal} und ziehe dann {minus} ab. Ich bekomme {erg}.<br>Welche Zahl habe ich mir gedacht?<br>Antwort: ______", "", 2.6, "9",
        f"Rückwärts, die letzte Rechnung zuerst: {erg} + {minus} = {erg + minus}, dann : {mal} = {e}. Probe: {e} · {mal} − {minus} = {erg}.",
        [(z(fa), "Nur die letzte Rechnung zurückgerechnet, das Malnehmen vergessen."), (dez(fb), f"In der falschen Reihenfolge zurückgerechnet (Minus {minus} wie Plus behandelt).")],
        "Rückwärts rechnen: Die letzte Rechnung zuerst umkehren.")

    # 14 Mittelwert
    werte = [9, 3, 17, 5, 6]
    e = F(sum(werte), len(werte))
    assert e == 8 and sum(w - e for w in werte) == 0 and sorted(werte)[2] == 6 and e != 6
    fa, fb = sum(werte), sorted(werte)[2]
    auf(14, "Gleichung und Daten", "id.daten.kennzahl", ("d3", "daten.kennwerte"),
        f"An fünf Tagen wurden {', '.join(map(str, werte))} Eis verkauft.<br>Wie viele waren es im Durchschnitt (Mittelwert) pro Tag?<br>Antwort: ______", "", 2.4, "8",
        f"Alles zusammen: {' + '.join(map(str, werte))} = {sum(werte)}. Geteilt durch die Anzahl der Tage: {sum(werte)} : 5 = 8.",
        [(z(fa), "Nur zusammengezählt, nicht durch die Anzahl geteilt."), (z(fb), "Die mittlere Zahl der geordneten Reihe genommen (Median statt Mittelwert).")],
        "Mittelwert = Summe geteilt durch Anzahl.")
    pruefe_zuordnung(A, 8)
    return A


# ───────────────────────────── Aufgaben Kind 1 (Klasse 5, Grundlagen) ─────────────────────────────
def kind1():
    A = []

    def auf(nr, gruppe, kennung, flug, text, antwort, hoehe, richtig, weg, fehl, luecke):
        assert len(fehl) == 2 and all(f[0] != richtig for f in fehl) and fehl[0][0] != fehl[1][0], nr
        A.append(dict(nr=nr, gruppe=gruppe, kennung=kennung, flug=flug, text=text, antwort=antwort, h=hoehe, richtig=richtig, weg=weg, fehl=fehl, luecke=luecke))

    # 1 Stellenwerttafel / Platzhalter-Null
    T, Z, E = 5, 3, 8
    e = T * 1000 + Z * 10 + E
    assert e == int("".join(map(str, (T, 0, Z, E)))) == 5038
    fa, fb = int(f"{T}{Z}{E}"), int(f"{T}{Z}0{E}")
    auf(1, "Stellenwert und Zahlen", "id.zahlen.buendeln", ("z1", "zahlen.natuerlich"),
        "Schreibe als Zahl:<br>5 Tausender, 3 Zehner und 8 Einer (Hunderter hat die Zahl keine).", "Die Zahl ist: ____________", 2.2, z(e),
        "Tausender 5, Hunderter 0, Zehner 3, Einer 8 – die Null hält den Platz frei: 5 038.",
        [(z(fa), "Die Null als Platzhalter fehlt (Ziffern einfach hintereinander)."), (z(fb), "Die Null an die falsche Stelle gesetzt (Stellen verrutscht).")],
        "Stellenwert: Jede Stelle hat einen Wert, die Null hält den Platz frei.")

    # 2 Mal 1000
    e = 36 * 1000
    assert e == int("36" + "000") == 36000
    fa, fb = 3600, 360000
    auf(2, "Stellenwert und Zahlen", "rr.stellenwert", ("z1", "zahlen.natuerlich"), "Rechne ohne Rechenweg:<br>36 · 1 000", "= ____________", 1.8, z(e),
        "Mal 1 000: jede Ziffer rückt drei Stellen nach links, drei Nullen: 36 000.",
        [(z(fa), "Nur zwei Nullen (zu wenig gezählt)."), (z(fb), "Vier Nullen (zu viel gezählt).")],
        "Stellenwert: Mal 10, 100, 1 000 – Nullen richtig zählen.")

    # 3 Zahlenstrahl
    e = 2650
    auf(3, "Stellenwert und Zahlen", "id.zahlen.zahlengerade", ("z1", "zahlen.natuerlich"),
        f"Der Pfeil zeigt auf eine Zahl. Zwischen den beschrifteten Strichen sind 10 gleiche Abschnitte.<br>{svg_zahlenstrahl(e)}<br>Die Zahl am Pfeil ist: ____________", "", 4.0, z(e),
        "Von 2 000 bis 3 000 sind es 10 Abschnitte, jeder ist 100 breit. Der Pfeil steht genau in der Mitte zwischen 2 600 und 2 700: 2 650.",
        [(z(2600), "Nur bis zum letzten Strich gezählt, die halbe Strecke nicht beachtet."), (z(2700), "Zum nächsten Strich aufgerundet, die Mitte nicht erkannt.")],
        "Zahlenstrahl: Abschnitte lesen, Zwischenwerte finden.")

    # 4 schriftlich addieren
    a, b = 4758, 2684
    e = a + b

    def spalten_plus(a, b, mit_uebertrag=True):
        ra, rb, c, out = str(a)[::-1], str(b)[::-1], 0, []
        for i in range(max(len(ra), len(rb))):
            s = int(ra[i] if i < len(ra) else 0) + int(rb[i] if i < len(rb) else 0) + (c if mit_uebertrag else 0)
            out.append(s % 10)
            c = s // 10
        if c and mit_uebertrag:
            out.append(c)
        return int("".join(map(str, out[::-1])))

    assert spalten_plus(a, b) == e == 7442
    fa, fb = spalten_plus(a, b, False), e - 10
    assert (fa, fb) == (6332, 7432)
    auf(4, "Schriftlich und Einmaleins", "id.zahlen.buendeln", ("z1", "zahlen.natuerlich"), f"Rechne schriftlich:<br>{z(a)} + {z(b)}", "= ____________", 3.6, z(e),
        "Spaltenweise von rechts, Übertrag mitnehmen: 8+4=12 (2, Übertrag 1), 5+8+1=14 (4, Übertrag 1), 7+6+1=14 (4, Übertrag 1), 4+2+1=7 → 7 442.",
        [(z(fa), "Kein Übertrag mitgenommen (zehn Einer werden nicht zu einem Zehner gebündelt)."), (z(fb), "Der Übertrag von den Einern zu den Zehnern wurde vergessen.")],
        "Bündeln: Zehn Einer sind ein Zehner (Übertrag beim Addieren).")

    # 5 schriftlich subtrahieren
    a, b = 5002, 1874
    e = a - b
    assert e + b == a and e == 3128

    def spalten_minus_ohne_entbuendeln(a, b):
        ra, rb, out = str(a)[::-1], str(b)[::-1], []
        for i in range(len(ra)):
            x, y = int(ra[i]), int(rb[i] if i < len(rb) else 0)
            out.append(x + 10 - y if x < y else x - y)       # borgt 10, aber die nächste Stelle wird nicht kleiner gemacht
        return int("".join(map(str, out[::-1])))

    def kleinere_von_groesserer(a, b):
        ra, rb = str(a), str(b).rjust(len(str(a)), "0")
        return int("".join(str(abs(int(x) - int(y))) for x, y in zip(ra, rb)))

    fa, fb = kleinere_von_groesserer(a, b), spalten_minus_ohne_entbuendeln(a, b)
    assert (fa, fb) == (4872, 4238)
    auf(5, "Schriftlich und Einmaleins", "id.zahlen.buendeln", ("z1", "zahlen.natuerlich"), f"Rechne schriftlich und mach die Probe:<br>{z(a)} {M} {z(b)}", "= ____________", 3.6, z(e),
        "Entbündeln über die Nullen: 5 002 = 4 Tausender, 9 Hunderter, 9 Zehner, 12 Einer. Dann 12−4=8, 9−7=2, 9−8=1, 4−1=3 → 3 128. Probe: 3 128 + 1 874 = 5 002.",
        [(z(fa), "In jeder Spalte die kleinere Ziffer von der größeren abgezogen (nicht entbündelt)."), (z(fb), "Zehn dazugeborgt, aber die Stelle links nicht um 1 verkleinert.")],
        "Bündeln und Entbündeln: eine Stelle leihen, die nächste wird um 1 kleiner (auch über Nullen).")

    # 6 schriftlich malnehmen
    a, b = 46, 7
    e = a * b
    assert e == 40 * 7 + 6 * 7 == 280 + 42 == 322
    fa, fb = 28 * 10 + 2, int(str(4 * 7) + str(6 * 7))
    assert (fa, fb) == (282, 2842)
    auf(6, "Schriftlich und Einmaleins", "rr.ausmultiplizieren", ("z1", "zahlen.rechengesetze"), f"Rechne schriftlich oder mit Zerlegen:<br>{a} · {b}", "= ____________", 3.0, z(e),
        "Zerlegen: 46 · 7 = 40 · 7 + 6 · 7 = 280 + 42 = 322. (Schriftlich: 6·7=42, 2 hinschreiben, 4 merken; 4·7=28, plus 4 = 32.)",
        [(z(fa), "Der Übertrag 4 beim Malnehmen wurde vergessen (282)."), (z(fb), "Die Teilergebnisse 28 und 42 einfach nebeneinandergeschrieben.")],
        "Verteilen: Die Zahl vor dem Malnehmen in Zehner und Einer zerlegen, jeden Teil mal nehmen.")

    # 7 Einmaleins und Umkehrung
    a_ = [x for x in range(0, 100) if 7 * x == 56]
    b_ = [x for x in range(0, 200) if x // 9 == 8 and x % 9 == 0]
    assert a_ == [8] and b_ == [72]
    fa, fb = 8 + 9, 56 - 7
    assert fa != 72 and fb != 8
    auf(7, "Schriftlich und Einmaleins", "rr.gegenrechnung", ("z1", "zahlen.natuerlich"), "Welche Zahl gehört in die Lücke?<br>a) &nbsp; 7 · □ = 56 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; b) &nbsp; □ : 9 = 8", "a) ____________ &nbsp;&nbsp; b) ____________", 2.0, "a) 8; b) 72",
        "a) 56 : 7 = 8 (Einmaleins rückwärts). b) Umkehren: 8 · 9 = 72. Probe: 72 : 9 = 8.",
        [("b) 17", "Plus statt Mal: 8 + 9 gerechnet (die Umkehraufgabe wurde nicht erkannt)."), ("a) 49", "Minus statt Geteilt: 56 − 7 gerechnet.")],
        "Umkehren: Mal und Geteilt gehören zusammen (Einmaleins vorwärts und rückwärts).")

    # 8 Teilen mit Rest
    q, r = divmod(85, 6)
    assert (q, r) == (14, 1) and 6 * q + r == 85 and [(x, y) for x in range(0, 40) for y in range(0, 6) if 6 * x + y == 85] == [(14, 1)]
    fa, fb = (q - 1, r + 6), (q, 0)
    assert 6 * fa[0] + fa[1] == 85 and fa[1] >= 6 and 6 * fb[0] + fb[1] != 85
    auf(8, "Schriftlich und Einmaleins", "id.zahlen.bausteine", ("z2", "zahlen.teilbarkeit"), "Teile mit Rest:<br>85 : 6 = ______ Rest ______", "", 2.0, "14 Rest 1",
        "6 · 14 = 84, übrig bleibt 1. Probe: 6 · 14 + 1 = 85. Der Rest muss kleiner als 6 sein.",
        [("13 Rest 7", "Der Rest ist größer als der Teiler: noch einmal teilbar, also zu klein geteilt."), ("14 (ohne Rest)", "Der Rest wurde vergessen oder weggelassen.")],
        "Teilen mit Rest: Der Rest ist immer kleiner als der Teiler (Vielfache kennen).")

    # 9 Größen
    e = 2 * 1000 + 50
    assert e == 2050
    fa, fb = int("2" + "50"), 2 * 1000 + 500
    auf(9, "Größen und Geometrie", "id.verhaeltnisse.groesse", ("g1", "groessen.einheiten"), "Rechne um:<br>2 kg 50 g = ______ g", "", 1.8, z(e),
        "1 kg = 1 000 g. 2 kg = 2 000 g, dazu 50 g: 2 050 g.",
        [(z(fa), "Die Zahlen einfach hintereinandergeschrieben (250)."), (z(fb), "50 g wie 500 g behandelt.")],
        "Einheiten umrechnen: 1 kg = 1 000 g; mehrere Einheiten zusammensetzen.")

    # 10 Fläche Rechteck
    l, br = 9, 4
    e = l * br
    assert e == 36 and sum(l for _ in range(br)) == e
    fa, fb = 2 * (l + br), l + br
    auf(10, "Größen und Geometrie", "id.flaeche_raum.auslegen", ("r1", "messen.flaechen"), f"Ein Rechteck ist {l} cm lang und {br} cm breit.<br>Wie groß ist seine Fläche?<br>Antwort: ______ cm²", "", 2.2, z(e),
        f"Auslegen und zählen: {br} Reihen mit je {l} Quadraten: {br} · {l} = {e}.",
        [(z(fa), "Umfang statt Fläche gerechnet."), (z(fb), "Länge und Breite addiert.")],
        "Fläche = Quadrate auslegen und zählen (Reihen mal Quadrate je Reihe); nicht mit dem Umfang verwechseln.")

    # 11 Winkelarten
    def art(w):
        return "spitz" if w < 90 else "recht" if w == 90 else "stumpf"

    ws = [35, 90, 130]
    e = [art(w) for w in ws]
    assert e == ["spitz", "recht", "stumpf"]
    fa = ["stumpf", "recht", "spitz"]
    fb = ["spitz", "spitz", "stumpf"]
    auf(11, "Größen und Geometrie", "id.geometrie.winkel", ("ge3", "geometrie.winkel"),
        "Schreibe zu jedem Winkel: spitz, recht oder stumpf.<br>35° ______ &nbsp;&nbsp; 90° ______ &nbsp;&nbsp; 130° ______", "", 1.8, ", ".join(e),
        "Kleiner als 90°: spitz. Genau 90°: recht. Größer als 90° (und kleiner als 180°): stumpf.",
        [(", ".join(fa), "„spitz“ und „stumpf“ vertauscht."), (", ".join(fb), "90° nicht als rechter Winkel erkannt (als „spitz“ eingeordnet).")],
        "Winkelarten: spitz (< 90°), recht (= 90°), stumpf (> 90°).")

    # 12 Anteil aus dem Bild
    teile, gef = 8, 3
    e = F(teile - gef, teile)
    assert e == F(5, 8)
    fa, fb = (gef, teile), (teile - gef, gef)
    auf(12, "Brüche", "id.daten.anteil", ("z3", "bruch.brueche"),
        f"Das Rechteck ist in gleich große Teile geteilt. Ein Teil davon ist grau.<br>{svg_anteil(teile, gef)}<br>Welcher Bruchteil ist <u>nicht</u> grau? &nbsp; Bruch: ______ ", "", 3.4, "5/8",
        "8 gleiche Teile, 3 sind grau, also 5 nicht grau: 5 von 8 = 5/8.",
        [("3/8", "Den grauen Teil angegeben (die Frage war nach dem nicht grauen)."), ("5/3", "Teil durch Teil statt Teil durch Ganzes (unten stand nicht die Gesamtzahl).")],
        "Bruch als Anteil: Zähler = betrachtete Teile, Nenner = alle gleichen Teile.")

    # 13 Bruchteil von einer Größe
    e = F(3, 4) * 20
    assert e == 15 and 20 // 4 * 3 == 15
    fa, fb = 20 // 4, 20 * 3
    auf(13, "Brüche", "id.verhaeltnisse.wert_fuer_eins", ("z3", "bruch.brueche"), f"Wie viel sind {fr(3, 4)} von 20 €?<br>Antwort: ______ €", "", 2.2, "15",
        "Erst auf ein Viertel: 20 € : 4 = 5 €. Dann drei Viertel: 3 · 5 € = 15 €.",
        [(z(fa), "Nur ein Viertel berechnet, das Malnehmen mit dem Zähler vergessen."), (z(fb), "Nur mit dem Zähler malgenommen (20 · 3), das Teilen durch den Nenner fehlt.")],
        "Bruchteil von einer Zahl: durch den Nenner teilen, mal den Zähler.")

    # 14 Sachaufgabe zwei Schritte
    n, preis, stift, schein = 3, 3, 4, 20
    kosten = n * preis + stift
    e = schein - kosten
    assert (e, kosten) == (7, 13) and schein - n * preis - stift == e
    fa, fb = schein - n * preis, kosten
    auf(14, "Sachaufgabe", None, ("z1", "zahlen.rechengesetze"),
        f"Tobi kauft {n} Hefte. Jedes Heft kostet {preis} €. Dazu kauft er einen Stift für {stift} €. Er bezahlt mit einem {schein}-€-Schein.<br>Wie viel Geld bekommt er zurück? Schreibe deine Rechnung auf.<br>Antwort: ______ €", "", 3.6, z(e),
        f"Erst die Kosten: {n} · {preis} + {stift} = {n * preis} + {stift} = {kosten}. Dann das Rückgeld: {schein} − {kosten} = {e}.",
        [(z(fa), "Den Stift vergessen (nur ein Teil der Kosten abgezogen)."), (z(fb), "Beim Gesamtpreis aufgehört, das Rückgeld nicht mehr gerechnet.")],
        "Zwei Schritte planen: erst alle Kosten, dann das Rückgeld (Arbeitsweise „Ansatz“, kein Regel-Etikett).")
    pruefe_zuordnung(A, 5)
    return A


# ───────────────────────────── Ausgabe ─────────────────────────────
CSS = """@page{size:A4;margin:16mm 15mm}
body{font:12pt/1.4 Georgia,'Times New Roman',serif;color:#000;margin:0}
h1{font-size:15pt;margin:0 0 2mm} h2{font-size:12.5pt;margin:5mm 0 2mm;border-bottom:1px solid #000}
.seite{page-break-after:always} .seite:last-child{page-break-after:auto}
.kopf{display:flex;justify-content:space-between;font-size:10.5pt;border:1px solid #000;padding:2mm 3mm;margin-bottom:3mm}
.regeln{font-size:10.5pt;margin:0 0 3mm}
.auf{display:flex;gap:3mm;page-break-inside:avoid;border-top:1px dotted #777;padding-top:1.5mm}
.auf .nr{width:9mm;font-weight:bold} .auf .tx{flex:1} .auf .tx svg{vertical-align:middle;margin:1mm 0}
.fr{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;margin:0 .15em;font-size:.95em}
.fr span:first-child{border-bottom:1px solid #000;padding:0 .25em} .fr span:last-child{padding:0 .25em}
.antw{margin-top:2mm}
table{border-collapse:collapse;width:100%;font-size:9pt;line-height:1.3} td,th{border:1px solid #000;padding:1.1mm 1.5mm;vertical-align:top;text-align:left}
th{background:#eee} .klein{font-size:9.5pt} .bogen td{height:6.6mm}
ul{margin:1mm 0 2mm 5mm;padding-left:4mm} code{font-size:.92em}
.kast{display:inline-block;width:4mm;height:4mm;border:1px solid #000;vertical-align:middle}"""

KOPF = {
    8: dict(titel="Eingangsdiagnose Klasse 8 – Stoff aus früheren Klassen", kurz="K8-Diagnose",
            regeln=("<b>30 Minuten.</b> Ohne Taschenrechner, ohne Formelsammlung, ohne Hilfe. Das sind kurze Aufgaben aus früheren Schuljahren. "
                    "Sie zeigen, was von früher noch da ist – nicht, wie gut du bist. Rechne auf dem Blatt; der Rechenweg muss nicht schön sein. "
                    "Fang vorne an. <b>Weißt du bei einer Aufgabe nicht, wie du anfangen sollst, lass sie leer und mach mit der nächsten weiter.</b> "
                    "Nach 30 Minuten sagt der Erwachsene „Strich“. Dann nimm einen anderen Stift und arbeite in Ruhe weiter, bis du fertig bist.")),
    5: dict(titel="Eingangsdiagnose Klasse 5 – Grundlagen", kurz="K5-Diagnose",
            regeln=("<b>30 Minuten.</b> Ohne Taschenrechner und ohne Hilfe. Das sind kurze Aufgaben zu Dingen, die du schon gelernt hast. "
                    "Sie zeigen, was schon gut sitzt und was wir noch üben – nicht, wie gut du bist. Rechne auf dem Blatt. "
                    "Fang vorne an. <b>Weißt du bei einer Aufgabe nicht, wie du anfangen sollst, lass sie leer und mach mit der nächsten weiter.</b> "
                    "Nach 30 Minuten sagt der Erwachsene „Strich“. Dann nimm einen anderen Stift und arbeite in Ruhe weiter, bis du fertig bist.")),
}
SEITE1 = {8: 8, 5: 6}          # Aufgaben auf Seite 1, Rest auf Seite 2


def kennung_name(a):
    if not a["kennung"]:
        return "ohne Kennung (Arbeitsweise „Ansatz“)"
    return f'<code>{a["kennung"]}</code> {KEN[a["kennung"]]["name"]}'


def flug_text(a):
    fl, th = a["flug"]
    return f'<b>{fl}</b> {FLUG[fl][0]} · <code>{th}</code>'


def seite_kind(kl, A):
    ko = KOPF[kl]
    n1 = SEITE1[kl]
    hoehe1 = sum(a["h"] for a in A[:n1])
    hoehe2 = sum(a["h"] for a in A[n1:])
    assert hoehe1 <= 19.2 and hoehe2 <= 24.0, (kl, hoehe1, hoehe2)      # in cm, Rest der Seite nach Kopf/Regeln
    zeile = lambda a: (f'<div class="auf" style="min-height:{a["h"] + 0.3:.1f}cm"><div class="nr">{a["nr"]}</div><div class="tx">{a["text"]}'
                       + (f'<div class="antw">{a["antwort"]}</div>' if a["antwort"] else "") + '</div></div>')
    kopf = f'<div class="kopf"><span>Mathematik · {ko["kurz"]}</span><span>Datum: __________</span><span>Minuten gebraucht: ____</span></div>'
    p1 = f'<div class="seite"><h1>{ko["titel"]}</h1>{kopf}<p class="regeln">{ko["regeln"]}</p>' + "".join(zeile(a) for a in A[:n1]) + "</div>"
    p2 = '<div class="seite"><p class="klein" style="margin:0 0 2mm">Seite 2 · Rechne auf dem Blatt. Leer lassen ist erlaubt.</p>' + "".join(zeile(a) for a in A[n1:]) + \
         '<p class="klein" style="margin-top:4mm">Fertig? Schreib oben rechts auf, wie viele Minuten du gebraucht hast.</p></div>'
    return p1 + p2


def seite_loesung(kl, A):
    zeilen = "".join(
        f'<tr><td><b>{a["nr"]}</b></td><td>{kennung_name(a)}</td><td><b>{a["richtig"]}</b><br><span class="klein">{a["weg"]}</span></td>'
        f'<td><b>A: {a["fehl"][0][0]}</b><br>{a["fehl"][0][1]}</td><td><b>B: {a["fehl"][1][0]}</b><br>{a["fehl"][1][1]}</td></tr>' for a in A)
    return f"""<div class="seite"><h1>Lösungen – {KOPF[kl]['kurz']}</h1>
<p class="klein"><b>Nur für Erwachsene.</b> Jede Aufgabe prüft genau eine tragende Idee (Kennung aus <code>regeln-uebersicht/kennungen.json</code>). Eine Aufgabe zählt 1 Punkt, wenn die Antwort stimmt
(bei zwei Teilen: beide). Der Rechenweg wird nicht bewertet. Die Spalten A und B zeigen die zwei häufigsten falschen Antworten; die Deutung dahinter ist eine <b>Vermutung</b>, kein Urteil. Die Fehlantworten sind aus Fehlermodellen berechnet, nicht aus Beobachtung.</p>
<table><tr><th>Nr.</th><th style="width:16%">Idee</th><th style="width:34%">Richtige Lösung · Weg</th><th style="width:21%">Fehlantwort A · Deutung</th><th style="width:21%">Fehlantwort B · Deutung</th></tr>{zeilen}</table></div>"""


def seite_bogen(kl, A):
    gruppen = []
    for a in A:
        if a["gruppe"] not in gruppen:
            gruppen.append(a["gruppe"])
    zeilen = "".join(
        f'<tr><td><b>{a["nr"]}</b></td><td>{a["gruppe"]}</td><td class="klein">{(a["kennung"] or "–").replace("rr.", "").replace("id.", "")}</td>'
        f'<td></td><td></td><td style="text-align:center"><span class="kast"></span></td><td style="text-align:center">A &nbsp; B &nbsp; andere</td><td></td></tr>' for a in A)
    gz = "".join(f'<tr><td colspan="3">{g}: Aufgaben {", ".join(str(a["nr"]) for a in A if a["gruppe"] == g)}</td><td></td><td></td><td></td><td colspan="2"></td></tr>' for g in gruppen)
    n = len(A)
    return f"""<div class="seite"><h1>Erfassungsbogen – {KOPF[kl]['kurz']}</h1>
<p class="klein">Datum: __________ &nbsp; Ausgefüllt von: __________ &nbsp; Gebrauchte Zeit gesamt: ____ Min.<br>
<b>So füllst du aus:</b> Nach 30 Minuten hat das Kind bei „Strich“ den Stift gewechselt. <b>Spalte „bis Strich“:</b> ✓, wenn die Antwort mit dem ersten Stift dasteht und stimmt. <b>Spalte „mit Zugabe“:</b> ✓, wenn sie am Ende stimmt (auch wenn sie erst nach dem Strich dazukam).
<b>Kästchen „nicht angefangen“:</b> am Ende nichts hingeschrieben, „weiß nicht“ geschrieben oder nur die Aufgabe abgeschrieben – das ist ein anderes Signal als „falsch“. Bei falscher Antwort: A oder B einkreisen, wenn sie zu einer Fehlantwort aus der Lösungsseite passt, sonst „andere“ und in „Notiz“ kurz aufschreiben.
Dieser Bogen kommt <b>nicht</b> ins Repo; Ergebnisse gehen nur an den Nutzer.</p>
<table class="bogen"><tr><th>Nr.</th><th>Gruppe</th><th>Idee</th><th>✓ bis Strich</th><th>✓ mit Zugabe</th><th>nicht angefangen</th><th>Fehlantwort</th><th style="width:20%">Notiz</th></tr>{zeilen}
<tr><td colspan="3"><b>Stand nach 30 Minuten</b> (Zahl der ✓ „bis Strich“)</td><td><b>____ / {n}</b></td><td></td><td></td><td colspan="2"></td></tr>
<tr><td colspan="3"><b>Stand mit Zugabe</b> (Zahl der ✓ „mit Zugabe“)</td><td></td><td><b>____ / {n}</b></td><td></td><td colspan="2"></td></tr>
<tr><td colspan="3"><b>nicht angefangen</b> (Zahl der Kästchen)</td><td></td><td></td><td><b>____ / {n}</b></td><td colspan="2"></td></tr>
<tr><th colspan="3">Zählung je Gruppe (richtig mit Zugabe / nicht angefangen)</th><th>richtig</th><th>falsch</th><th>leer</th><th colspan="2"></th></tr>{gz}</table></div>"""


def seite_auswertung(kl, A):
    zeilen = "".join(
        f'<tr><td><b>{a["nr"]}</b></td><td>{KEN[a["kennung"]]["name"] + "<br><span class=klein>" + KEN[a["kennung"]]["merksatz"] + "</span>" if a["kennung"] else "Zwei Schritte planen<br><span class=klein>ohne Kennung (Arbeitsweise „Ansatz“)</span>"}</td>'
        f'<td>Vermutung: {a["luecke"]}</td><td>{flug_text(a)}</td></tr>' for a in A)
    wo = {8: "Alle Flüge in der rechten Spalte stehen <b>nicht</b> in der Route von Kind 2 (Stand <code>lehrplan-kinder/route.md</code>). Wer sie braucht, muss sie zusätzlich einstellen.",
          5: "Alle Flüge in der rechten Spalte stehen in der Route von Kind 1; die Diagnose zeigt, welche davon vor allem gebraucht werden und womit man früher anfängt."}[kl]
    return f"""<div class="seite"><h1>Auswertungshilfe für den Vater – {KOPF[kl]['kurz']}</h1>
<p class="klein"><b>In einfachen Worten.</b> Das Blatt sagt nicht „gut“ oder „schlecht“. Es sucht <i>Stellen, an denen früher etwas nicht fest geworden ist</i>. Jede Aufgabe gehört zu genau einer Idee.
Eine einzelne falsche Aufgabe ist ein <b>Hinweis, kein Beweis</b> (Flüchtigkeit ist möglich): Lass das Kind die Aufgabe danach <b>laut</b> noch einmal rechnen und frag: „Wie bist du darauf gekommen?“ Erst wenn es wieder nicht geht, gilt die Lücke als wahrscheinlich.</p>
<ul class="klein">
<li><b>richtig bis Strich:</b> sitzt, auch im Tempo. Nichts tun.</li>
<li><b>richtig erst mit Zugabe:</b> kann es, aber langsam. Kein Lernstoff fehlt; später mit der Zeit üben (kurze Wiederholungen).</li>
<li><b>falsch, und die Antwort passt zu A oder B:</b> das Kind hat sich eine falsche Regel gemerkt. Die Spalte „wenn falsch“ unten nennt die vermutete Lücke. Erst erklären, dann den Flug in der App machen.</li>
<li><b>falsch, passt zu keiner Antwort:</b> Gespräch nötig; Rechenweg ansehen. Nicht sofort auf eine Lücke schließen.</li>
<li><b>nicht angefangen:</b> ein anderes Signal. Vermutung: Das Kind weiß nicht, wie es anfangen soll, oder meidet die Art von Aufgabe. Frag nach, was es sich dabei gedacht hat. Mehrere leere Aufgaben in derselben Gruppe (Bogen unten) sind ein deutlicheres Zeichen als eine.</li>
<li><b>Viel „mit Zugabe“ und wenig „bis Strich“:</b> zuerst das Tempo ansehen, nicht den Stoff.</li>
</ul>
<p class="klein">{wo}</p>
<table><tr><th>Aufgabe</th><th style="width:26%">Idee</th><th>wenn falsch, dann fehlt vermutlich …</th><th style="width:27%">passender Flug in der App (Flug · Thema)</th></tr>{zeilen}</table>
<p class="klein"><b>Fakten und Annahmen.</b> Fakt: Idee, Kennung und Flug stammen aus <code>kennungen.json</code>, <code>plan.py</code> und <code>inhalte/themen/</code>. Annahme (nicht gemessen): Die Zuordnung „falsche Antwort → fehlende Idee“ ist eine Vermutung; kein Schwellenwert ist getestet. Kein Normwert, kein Notenmaßstab.</p></div>"""


def html(kl, A):
    pruefe_zuordnung(A, 8 if kl == 8 else 5)
    teile = seite_kind(kl, A) + seite_loesung(kl, A) + seite_bogen(kl, A) + seite_auswertung(kl, A)
    return f'<!doctype html><html lang="de"><meta charset="utf-8"><title>Eingangsdiagnose · {KOPF[kl]["kurz"]}</title><style>{CSS}</style><body>{teile}</body></html>'


if __name__ == "__main__":
    for kl, bau in ((8, kind2), (5, kind1)):
        A = bau()
        assert 12 <= len(A) <= 15
        assert [a["nr"] for a in A] == list(range(1, len(A) + 1))
        with open(os.path.join(HIER, f"k{kl}-diagnose.html"), "w", encoding="utf-8") as f:
            f.write(html(kl, A))
        ids = sorted({a["kennung"] for a in A if a["kennung"]})
        print(f"K{kl}: {len(A)} Aufgaben; Ideen: {', '.join(i for i in ids)}")
    print("OK")
