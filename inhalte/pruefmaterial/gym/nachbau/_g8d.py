# Generatoren für die dritte Runde (Realschul-Grundwissentests Jgst. 9, ältere bayerische Schulaufgaben)
from _kern import *


def pk(p):
    return f"({fz(p[0])} | {fz(p[1])})"


def lin(m, t):
    return (F(m) * x + F(t)).fmt()


@reg(("X", "quadratische Terme/Gleichungen, Extremwerte (RS Kl. 8, Gym Kl. 9/10)"))
def _(c):
    a_ = c.ch((1, -1, 2, -2)); h_ = c.nz(-5, 5); k = c.nz(-9, 9)
    art = "Minimum" if a_ > 0 else "Maximum"
    t = f"{'' if a_ == 1 else ('−' if a_ == -1 else str(a_))}(x {'−' if h_ > 0 else '+'} {abs(h_)})² {'+' if k > 0 else '−'} {abs(k)}"
    chk(all((a_ * (xx - h_) ** 2 + k >= k) == (a_ > 0) or xx == h_ for xx in range(-10, 11)), "Extremwert durch Einsetzen geprüft")
    return T(f"Gib für den Term T(x) = {t} die Art des Extremwerts, seinen Wert und die zugehörige Belegung von x an.",
             f"{art} {k} für x = {h_}", ["Quadrat ist nie negativ", f"bei x = {h_} ist die Klammer 0", f"{'Faktor positiv → Minimum' if a_>0 else 'Faktor negativ → Maximum'}: T = {k}"])


@reg(("X", "Determinante/Vektorrechnung (nur Realschule)"))
def _(c):
    A = (c.ri(-3, 0), c.ri(-3, 0)); B = (A[0] + c.ri(3, 7), A[1] + c.ri(-1, 2)); C = (A[0] + c.ri(0, 3), A[1] + c.ri(3, 6))
    u = (B[0] - A[0], B[1] - A[1]); v = (C[0] - A[0], C[1] - A[1])
    fl = F(abs(u[0] * v[1] - u[1] * v[0]), 2)
    chk(fl == abs(F(A[0]) * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])) / 2, "Gaußsche Flächenformel")
    return T(f"Berechne den Flächeninhalt des Dreiecks A{pk(A)}, B{pk(B)}, C{pk(C)} mithilfe der Vektoren AB und AC (Determinante).",
             f"{fz(fl, dez=True)} FE", [f"AB = ({u[0]} | {u[1]}), AC = ({v[0]} | {v[1]})", f"A = ½·|{u[0]}·{kl(v[1])} − {kl(u[1])}·{kl(v[0])}|"])


@reg(("X", "Rotationskörper (nur Realschule)"))
def _(c):
    f = c.ch((("ein Rechteck um eine seiner Seiten", "Zylinder"), ("ein rechtwinkliges Dreieck um eine Kathete", "Kegel"), ("ein Halbkreis um seinen Durchmesser", "Kugel")))
    return T(f"Welcher Körper entsteht, wenn {f[0]} rotiert? Benenne Grundfläche bzw. Mantel.", f[1], ["Rotation gedanklich ausführen", f"es entsteht ein {f[1]}"])


@reg(("X", "Betragsgleichungen/-ungleichungen (alter G9-Lehrplan)"))
def _(c):
    k = c.ri(2, 9); m = c.nz(-5, 5)
    L = [m - k, m + k]
    chk(all(abs(v - m) == k for v in L), "Einsetzprobe")
    return T(f"Bestimme die Lösungsmenge: |x {'−' if m>0 else '+'} {abs(m)}| = {k}", f"L = {{{L[0]}; {L[1]}}}",
             ["Abstand von x zu " + str(m) + " ist " + str(k), f"x = {m} − {k} oder x = {m} + {k}"])


@reg(("X", "Strecke in wahrer Größe (alter G9-Lehrplan)"))
def _(c):
    a_ = c.ri(3, 6)
    return T(f"In einem Würfel mit Kantenlänge {a_} cm wird die Flächendiagonale betrachtet. Konstruiere sie in wahrer Größe aus einem Quadrat.",
             "Diagonale eines Quadrats mit " + str(a_) + " cm Seite", ["Quadrat in wahrer Größe zeichnen", "Diagonale einzeichnen"])


@reg(("X", "Vektoraddition, Windkorrektur (alter G9-Lehrplan)"))
def _(c):
    v, w = c.ri(3, 8), c.ri(1, 3)
    return T(f"Ein Boot fährt mit {v} km/h nach Norden, die Strömung treibt es mit {w} km/h nach Osten. Zeichne die Vektoren maßstäblich und miss Richtung und Geschwindigkeit über Grund.",
             "Vektorsumme zeichnerisch", ["Pfeile aneinandersetzen", "Länge und Winkel des Summenpfeils messen"])


@reg(("abbildungen.kongruenz", "vierecke_ordnen"), ("abbildungen.kongruenz", "eigenschaften"))
def _(c):
    f = c.ch((("Die Diagonalen halbieren sich gegenseitig und stehen senkrecht aufeinander.", "Raute"),
              ("Alle Winkel sind rechte Winkel, die Diagonalen sind gleich lang.", "Rechteck"),
              ("Eine Diagonale ist Symmetrieachse, die Diagonalen stehen senkrecht.", "Drachenviereck"),
              ("Ein Paar paralleler Seiten, die Schenkel sind gleich lang.", "gleichschenkliges Trapez")))
    if c.z["etappe"] == "eigenschaften" or c.has("falsch", "aussage"):
        return T("Welche Aussage ist falsch? (A) Jedes Quadrat ist eine Raute. (B) Jedes Rechteck ist ein Parallelogramm. (C) Jede Raute ist ein Rechteck. (D) Jedes Parallelogramm ist punktsymmetrisch.",
                 "C", ["Raute hat nicht zwingend rechte Winkel"])
    return T(f"Nenne das speziellste Viereck mit dieser Eigenschaft: „{f[0]}“", f[1], ["Eigenschaften im Haus der Vierecke prüfen"])


@reg(("abbildungen.kongruenz", "drehung"))
def _(c):
    Z = (c.ri(-2, 2), c.ri(-2, 2)); P = (Z[0] + c.nz(-4, 4), Z[1] + c.nz(-4, 4)); w = c.ch((90, 180, -90))
    d = (P[0] - Z[0], P[1] - Z[1])
    r = {90: (-d[1], d[0]), 180: (-d[0], -d[1]), -90: (d[1], -d[0])}[w]
    P2 = (Z[0] + r[0], Z[1] + r[1])
    chk(d[0] ** 2 + d[1] ** 2 == r[0] ** 2 + r[1] ** 2, "Abstand zum Drehzentrum bleibt gleich")
    richt = "gegen den Uhrzeigersinn" if w > 0 else "im Uhrzeigersinn"
    return T(f"Drehe den Punkt P{pk(P)} um Z{pk(Z)} um {abs(w)}° {richt}. Gib die Koordinaten des Bildpunkts an.", f"P'{pk(P2)}",
             [f"Pfeil ZP = ({d[0]} | {d[1]})", f"gedreht: ({r[0]} | {r[1]})", f"P' = Z + gedrehter Pfeil"])


@reg(("abbildungen.kongruenz", "verschiebung"), ("abbildungen.kongruenz", "vektor_koordinaten"))
def _(c):
    P = (c.nz(-6, 6), c.nz(-6, 6)); v = (c.nz(-5, 5), c.nz(-5, 5)); Q = (P[0] + v[0], P[1] + v[1])
    chk(Q[0] - P[0] == v[0] and Q[1] - P[1] == v[1], "Pfeil nachgerechnet")
    if c.z["etappe"] == "vektor_koordinaten":
        return T(f"Gib die Koordinaten des Vektors an, der P{pk(P)} auf Q{pk(Q)} verschiebt.", f"({v[0]} | {v[1]})", ["x: Q − P", "y: Q − P"])
    return T(f"Der Punkt Q entsteht aus P{pk(P)} durch Verschiebung um den Vektor ({v[0]} | {v[1]}). Berechne Q.", f"Q{pk(Q)}", ["Koordinaten addieren"])


@reg(("geometrie.konstruktion", "konstruierbar"), ("geometrie.konstruktion", "satz_kehrsatz"))
def _(c):
    if c.z["etappe"] == "satz_kehrsatz":
        return T("Bilde den Kehrsatz zu: „Wenn ein Viereck ein Quadrat ist, dann sind seine Diagonalen gleich lang.“ Ist der Kehrsatz wahr?", "Kehrsatz falsch (z. B. Rechteck)",
                 ["Voraussetzung und Behauptung tauschen", "Gegenbeispiel: Rechteck"])
    a_, b_ = c.ri(2, 6), c.ri(7, 12)
    cc = a_ + b_ + c.ri(0, 3)
    return T(f"Kann man ein Dreieck mit den Seitenlängen {a_} cm, {b_} cm und {cc} cm zeichnen? Begründe.", "nein",
             [f"{a_} + {b_} = {a_+b_} ist nicht größer als {cc}", "Dreiecksungleichung verletzt"])


@reg(("funktionen.linear", "aufstellen"))
def _(c):
    m_ = F(c.nz(-4, 4), c.ch((1, 2))); px, py = c.nz(-4, 4), c.nz(-4, 4)
    ms = -1 / m_; t2 = py - ms * px
    chk(m_ * ms == -1 and ms * px + t2 == py, "senkrecht und durch P")
    return T(f"Gib die Gleichung der Geraden an, die senkrecht zu y = {lin(m_, 1)} verläuft und durch P({px} | {py}) geht.", f"y = {lin(ms, t2)}",
             [f"m₁·m₂ = −1 → m = {fz(ms)}", f"t aus P: {py} = {fz(ms)}·{kl(px)} + t → t = {fz(t2)}"])


@reg(("stochastik.grundbegriffe", "rel_haeufigkeit"))
def _(c):
    n_ = c.ch((20, 25, 40, 50)); k = c.ri(2, n_ - 2)
    if c.has("quote", "vergleich", "trefferquote"):
        a1, n1, n2 = c.ri(3, 9), c.ri(12, 20), c.ri(12, 20)
        a2 = a1 * n2 // n1
        return T(f"Spieler A trifft {a1}-mal bei {n1} Würfen, Spieler B {a2}-mal bei {n2} Würfen. Wer hat die bessere Trefferquote? Begründe.",
                 "A" if F(a1, n1) > F(a2, n2) else ("B" if F(a2, n2) > F(a1, n1) else "gleich"), [f"A: {fz(F(a1,n1))}", f"B: {fz(F(a2,n2))}", "relative Häufigkeiten vergleichen"])
    chk(F(k, n_) * 100 == F(k * 100, n_), "Prozent")
    return T(f"Ein Würfel wird {n_}-mal geworfen; {k}-mal fällt eine Sechs. Gib die relative Häufigkeit der Sechs als Bruch und in Prozent an.", f"{fz(F(k,n_))} = {fd(F(k*100,n_))} %",
             [f"{k}/{n_}", "· 100 %"])


@reg(("gleichungen.ungleichungen", "umformen"))
def _(c):
    a_, b_ = c.ri(2, 6), c.nz(-9, 9); s = c.nz(-5, 5); r_ = a_ * s + b_
    chk(a_ * (s - 1) + b_ < r_, "Testwert")
    return T(f"Bestimme die Lösungsmenge über ℚ: {a_}x {'+' if b_>0 else '−'} {abs(b_)} < {r_}", f"x < {s}", [f"{a_}x < {r_-b_}", f"x < {s}"])


@reg(("groessen.indirekt", "sach"))
def _(c):
    v_, t_ = c.ri(4, 12) * 100, c.ri(20, 60)
    tag = F(v_, t_)
    neu = c.ri(10, 40)
    chk(F(v_, neu) * neu == v_, "Produkt konstant")
    return T(f"Ein Heizölvorrat von {v_} Litern reicht {t_} Tage, wenn täglich gleich viel verbraucht wird. Wie lange reicht er bei {neu} Litern pro Tag?",
             f"{fd(F(v_,neu)) if endlich(F(v_,neu)) else '≈ ' + gerundet(F(v_,neu),1)} Tage", [f"Vorrat konstant: {v_} l", f"{v_} : {neu}"])


@reg(("groessen.proportional", "pruefen"), ("groessen.proportional", "erkennen"))
def _(c):
    k = c.ri(2, 9); xs = [1, 2, 3, 4, 5]; ys = [k * v for v in xs]; i = c.ri(1, 4); ys[i] += c.ch((-1, 1, 2))
    if c.z["etappe"] == "erkennen":
        return T("Welche Zuordnung hat als Graph eine Ursprungsgerade, welche eine Hyperbel? (A) Anzahl Hefte → Preis  (B) Geschwindigkeit → Fahrzeit für 100 km  (C) Alter → Körpergröße",
                 "A Ursprungsgerade, B Hyperbel, C keine von beiden", ["A direkt proportional", "B indirekt proportional", "C weder noch"])
    chk([v for j, v in enumerate(ys) if v != k * xs[j]] == [ys[i]], "genau ein Ausreißer")
    return T(f"Prüfe, ob die Tabelle eine direkte Proportionalität beschreibt: x: {', '.join(map(str, xs))}; y: {', '.join(map(str, ys))}. Korrigiere den falschen Wert.",
             f"y({xs[i]}) muss {k*xs[i]} sein", [f"Quotient y : x meist {k}", f"bei x = {xs[i]} abweichend"])


@reg(("gleichungen.linear", "probe"))
def _(c):
    a_, b_, s = c.ri(2, 7), c.nz(-9, 9), c.nz(-6, 6); r_ = a_ * s + b_; falsch = s + c.ch((-1, 1))
    chk(a_ * falsch + b_ != r_, "falscher Wert erfüllt die Gleichung nicht")
    return T(f"Ist x = {falsch} eine Lösung der Gleichung {a_}x {'+' if b_>0 else '−'} {abs(b_)} = {r_}? Prüfe mit einer Probe.", "nein",
             [f"links: {a_}·{kl(falsch)} {'+' if b_>0 else '−'} {abs(b_)} = {a_*falsch+b_}", f"≠ {r_}"])


@reg(("terme.bruchterme", "erweitern"))
def _(c):
    p, k = c.ri(1, 6), c.ri(2, 5)
    return T(f"Erweitere 3/(x + {p}) so, dass der Nenner {k}x² + {k*p}x lautet.", f"{3*k}x/({k}x² + {k*p}x)", [f"Nenner mal {k}x", f"Zähler mal {k}x"])


@reg(("gleichungen.lgs2", "grafisch"))
def _(c):
    sx, sy = c.nz(-4, 4), c.nz(-4, 4); m1, m2 = c.nz(-2, 2), c.nz(-2, 2)
    while m1 == m2:
        m2 = c.nz(-2, 2)
    t1, t2 = sy - m1 * sx, sy - m2 * sx
    chk(m1 * sx + t1 == m2 * sx + t2, "Schnittpunkt liegt auf beiden Geraden")
    return T(f"Löse das Gleichungssystem zeichnerisch und rechnerisch: I y = {lin(m1, t1)}; II y = {lin(m2, t2)}.", f"({sx} | {sy})",
             ["beide Geraden zeichnen, Schnittpunkt ablesen", "gleichsetzen und lösen"])
