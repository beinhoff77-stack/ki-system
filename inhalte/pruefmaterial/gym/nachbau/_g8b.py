# Generatoren Geometrie und Messen (Kl. 8 und Grundwissen 5–7; teils auch Kl. 5)
from _kern import *


def flaeche(pts):
    s = F(0)
    for i in range(len(pts)):
        x1, y1 = pts[i]; x2, y2 = pts[(i + 1) % len(pts)]
        s += F(x1) * y2 - F(x2) * y1
    return abs(s) / 2


def pk(p):
    return f"({fz(p[0])} | {fz(p[1])})"


PI3 = "π ≈ 3"


# ============================================================ Abbildungen
@reg(("abbildungen.kongruenz", "mittelsenkrechte"))
def _(c):
    A = (c.ri(-4, 0), c.ri(-3, 2)); B = (A[0] + 2 * c.ri(1, 4), A[1] + 2 * c.ri(-2, 3))
    M = (F(A[0] + B[0], 2), F(A[1] + B[1], 2))
    d = (B[0] - A[0], B[1] - A[1]); Q = (M[0] - d[1], M[1] + d[0])
    chk((Q[0] - A[0]) ** 2 + (Q[1] - A[1]) ** 2 == (Q[0] - B[0]) ** 2 + (Q[1] - B[1]) ** 2, "Q gleich weit von A und B")
    if c.niv == "I":
        return T(f"Zeichne die Strecke [AB] mit A{pk(A)} und B{pk(B)} und konstruiere ihre Mittelsenkrechte mit Zirkel und Lineal.",
                 f"Mittelsenkrechte durch M{pk(M)}, senkrecht zu [AB]", ["zwei Kreise gleichen Radius um A und B (Radius > halbe Streckenlänge)", "Schnittpunkte verbinden", f"Kontrolle: M{pk(M)} liegt darauf"])
    return T(f"A{pk(A)} und B{pk(B)} sind zwei Bäume. Ein Brunnen soll von beiden gleich weit entfernt sein. Konstruiere alle möglichen Orte und gib einen Gitterpunkt an, der passt.",
             f"Mittelsenkrechte von [AB], z. B. Q{pk(Q)}", ["gesuchte Punkte: Mittelsenkrechte", f"Mittelpunkt M{pk(M)}", f"Q{pk(Q)}: Abstand zu A und B gleich (Probe)"])


@reg(("abbildungen.kongruenz", "punktspiegelung"))
def _(c):
    Z = (c.ri(-2, 2), c.ri(-2, 2)); A = (c.ri(-5, -1), c.ri(1, 5)); B = (c.ri(0, 4), c.ri(-4, 0))
    A2 = (2 * Z[0] - A[0], 2 * Z[1] - A[1]); B2 = (2 * Z[0] - B[0], 2 * Z[1] - B[1])
    chk(A2[0] + A[0] == 2 * Z[0], "Z ist Mittelpunkt von [AA']")
    return T(f"Spiegle die Strecke [AB] mit A{pk(A)}, B{pk(B)} am Punkt Z{pk(Z)}. Gib die Koordinaten der Bildpunkte an.",
             f"A'{pk(A2)}, B'{pk(B2)}", ["Z ist Mittelpunkt von [AA'] und [BB']", f"A' = 2Z − A = {pk(A2)}", f"B' = {pk(B2)}"])


@reg(("abbildungen.kongruenz", "symmetrie"), ("abbildungen.kongruenz", "achsenspiegelung"))
def _(c):
    if c.z["etappe"] == "achsenspiegelung":
        A = (c.ri(1, 5), c.ri(1, 6)); B = (c.ri(1, 6), c.ri(-3, 0)); C = (c.ri(5, 8), c.ri(2, 5))
        bild = [(-p[0], p[1]) for p in (A, B, C)]
        if c.has("ablesen", "koordinaten", "schräg") or c.niv != "I":
            return T(f"Spiegle das Dreieck ABC mit A{pk(A)}, B{pk(B)}, C{pk(C)} an der y-Achse und gib die Koordinaten der Bildpunkte an.",
                     ", ".join(f"{n}'{pk(p)}" for n, p in zip("ABC", bild)), ["x-Koordinate wechselt das Vorzeichen, y bleibt", "Bildpunkte eintragen und verbinden"])
        fig = c.ch(("ein Herz", "ein Haus mit Satteldach", "einen Pfeil", "ein Blatt"))
        return T(f"Zeichne {fig} achsensymmetrisch: Zeichne zuerst die linke Hälfte auf Karopapier und ergänze sie an einer senkrechten Achse.",
                 "symmetrische Figur", ["jeder Punkt hat auf der anderen Seite den gleichen Abstand zur Achse", "Verbindungslinie Punkt–Bildpunkt senkrecht zur Achse"])
    fig = c.ch([("Raute (kein Quadrat)", 2), ("Rechteck (kein Quadrat)", 2), ("Quadrat", 4), ("gleichseitiges Dreieck", 3), ("regelmäßiges Sechseck", 6),
                ("gleichschenkliges Trapez", 1), ("Drachenviereck (keine Raute)", 1), ("Parallelogramm (schief, keine Raute)", 0)])
    if c.niv == "III":
        k = c.ri(2, 4)
        return T(f"Ein Quadrat aus 4 × 4 Kästchen hat {k} gefärbte Kästchen in der linken Hälfte. Färbe weitere Kästchen so, dass die Figur achsensymmetrisch zur senkrechten Mittellinie ist und genau {2*k}/16 der Fläche gefärbt sind.",
                 f"{k} gespiegelte Kästchen dazu", ["Spiegelbild jedes gefärbten Kästchens färben", f"{2*k} von 16 Kästchen"])
    return T(f"Wie viele Symmetrieachsen hat diese Figur: {fig[0]}? Zeichne sie in eine Skizze ein.", str(fig[1]), [f"{fig[1]} Achse(n)" + ("; punktsymmetrisch, aber keine Achse" if fig[1] == 0 else "")])


# ============================================================ Konstruktion / Kongruenz
@reg(("geometrie.konstruktion", "kongruenzsatz"), ("geometrie.konstruktion", "vierecke"))
def _(c):
    a_, b_, w = c.ri(4, 7), c.ri(5, 9), c.ri(30, 50)
    if c.z["etappe"] == "vierecke":
        s_ = c.ri(3, 6)
        return T(f"Zeige mit einem Gegenbeispiel: Zwei Vierecke mit vier gleich langen Seiten ({s_} cm) müssen nicht kongruent sein.",
                 "z. B. Quadrat und Raute mit Seite " + str(s_) + " cm", ["Quadrat: Winkel 90°", "Raute mit 60°-Winkel: gleiche Seiten, andere Winkel → nicht deckungsgleich"])
    if c.has("bewert", "ankreuz"):
        return T("Welche Angaben legen ein Dreieck eindeutig fest? (A) drei Seiten  (B) drei Winkel  (C) zwei Seiten und der eingeschlossene Winkel  (D) zwei Seiten und ein Gegenwinkel der kürzeren Seite",
                 "A und C", ["A: SSS", "B: nur Form, nicht Größe", "C: SWS", "D: SsW nur mit Gegenwinkel der längeren Seite"])
    return T(f"Zeichne zwei nicht kongruente Dreiecke, die beide eine Seite von {b_} cm, eine Seite von {a_} cm und einen Winkel von {w}° gegenüber der {a_}-cm-Seite haben. Erkläre, warum das möglich ist.",
             "zwei Dreiecke (SsW-Fall mit Gegenwinkel der kürzeren Seite)", [f"Winkel {w}° an der {b_}-cm-Seite antragen", f"Kreis mit r = {a_} cm schneidet den freien Schenkel zweimal", "Gegenwinkel liegt an der kürzeren Seite → nicht eindeutig"])


@reg(("geometrie.konstruktion", "gleichschenklig"), ("geometrie.konstruktion", "planfigur"), ("geometrie.konstruktion", "vierecke_konstruieren"))
def _(c):
    et = c.z["etappe"]; s_ = c.ri(4, 7)
    if et == "gleichschenklig":
        return T("Zwei Kreise um M mit gleichem Radius werden von einer Geraden in A und B geschnitten (A, B auf demselben Kreis). Begründe, dass das Dreieck ABM gleichschenklig ist.",
                 "MA = MB = r", ["A und B liegen auf dem Kreis um M", "beide Strecken sind Radien"])
    if et == "vierecke_konstruieren":
        w = c.ch((50, 60, 70, 120))
        return T(f"Konstruiere eine Raute mit Seitenlänge {s_} cm und einem Innenwinkel von {w}° (nur Zirkel und Lineal; {w}° darfst du mit dem Geodreieck antragen, falls nicht konstruierbar).",
                 f"Raute, Winkel {w}° und {180-w}°", [f"Seite {s_} cm, Winkel {w}° antragen", f"Kreisbögen mit r = {s_} cm", "vierten Eckpunkt als Schnitt, verbinden"])
    return T(f"Beschreibe in Worten die Konstruktion eines gleichseitigen Dreiecks mit Seitenlänge {s_} cm nur mit Zirkel und Lineal.", "Konstruktionsbeschreibung",
             [f"Strecke [AB] = {s_} cm zeichnen", f"Kreise um A und B mit r = {s_} cm", "Schnittpunkt C, verbinden"])


# ============================================================ Kreis / Thales
@reg(("geometrie.kreis", "thales"), ("geometrie.kreis", "umkehrung"), ("geometrie.kreis", "beweis"), ("geometrie.kreis", "tangente"),
     ("geometrie.kreis", "umkreis_inkreis"))
def _(c):
    et = c.z["etappe"]; al = c.ri(20, 70)
    if et == "thales":
        be = 90 - al
        chk(al + be + 90 == 180, "Winkelsumme")
        return T(f"[AB] ist ein Durchmesser eines Kreises, C liegt auf dem Kreis, ∢BAC = {al}°. Berechne ∢ACB und ∢ABC und begründe.",
                 f"∢ACB = 90°, ∢ABC = {be}°", ["Satz des Thales: Winkel am Halbkreis 90°", f"Winkelsumme: 180° − 90° − {al}° = {be}°"])
    if et == "umkehrung":
        if c.niv == "III":
            return T("In einem Viereck ABCD sind die Winkel bei B und D rechte Winkel. Beweise, dass A, B, C, D auf einem Kreis liegen.",
                     "Kreis über [AC]", ["B sieht [AC] unter 90° → B auf Thaleskreis über [AC]", "D ebenso", "alle vier auf dem Kreis mit Durchmesser [AC]"])
        d_ = c.ri(5, 9); h_ = c.ri(2, 3)
        return T(f"Konstruiere alle Punkte C, für die das Dreieck ABC mit [AB] = {d_} cm bei C rechtwinklig ist und C den Abstand {h_} cm von AB hat.",
                 "bis zu 4 Punkte", ["Thaleskreis über [AB] (r = " + fd(F(d_, 2)) + " cm)", f"Parallelen zu AB im Abstand {h_} cm", "Schnittpunkte" + (" (4 Stück)" if F(d_, 2) > h_ else "")])
    if et == "beweis":
        return T("Beweise: Liegt C auf dem Kreis mit Durchmesser [AB], so ist ∢ACB = 90°. Nutze den Mittelpunkt M.",
                 "Beweis über zwei gleichschenklige Dreiecke", ["MA = MB = MC → Dreiecke AMC, BMC gleichschenklig", "Basiswinkel α und β", "Winkelsumme: 2α + 2β = 180° → α + β = 90°"])
    if et == "tangente":
        return T(f"Eine Tangente berührt einen Kreis mit Mittelpunkt M im Punkt B; A liegt auf der Tangente, ∢BAM = {al}°. Berechne ∢AMB und begründe.",
                 f"{90-al}°", ["Berührradius ⊥ Tangente: ∢MBA = 90°", f"Winkelsumme: 180° − 90° − {al}° = {90-al}°"])
    if c.has("ohne umkreis", "viereck"):
        return T("Zeichne ein Viereck, das keinen Umkreis hat, und begründe.", "z. B. Raute mit 60°-Winkel",
                 ["Umkreis nur, wenn die Mittelsenkrechten aller Seiten sich in einem Punkt schneiden", "bei der Raute (kein Quadrat) nicht der Fall"])
    pts = [(0, 0), (2 * c.ri(2, 4), 0), (0, 2 * c.ri(2, 4))]
    M = (F(pts[1][0], 2), F(pts[2][1], 2))
    chk(M[0] ** 2 + M[1] ** 2 == (M[0] - pts[1][0]) ** 2 + M[1] ** 2, "gleich weit von allen Ecken")
    return T(f"Drei Orte liegen bei A{pk(pts[0])}, B{pk(pts[1])}, C{pk(pts[2])} (1 LE = 1 km). Ein Funkmast soll von allen gleich weit entfernt sein. Konstruiere seinen Standort und gib die Koordinaten an.",
             f"M{pk(M)}", ["Mittelsenkrechten zweier Seiten", "Schnittpunkt = Umkreismittelpunkt", f"rechtwinkliges Dreieck: M ist Mitte von [BC] = {pk(M)}"])


@reg(("geometrie.ortslinien", "verknuepfen"))
def _(c):
    d_, r_ = c.ri(2, 4), c.ri(3, 6)
    return T(f"Gegeben sind eine Gerade g und ein Punkt P im Abstand {d_+1} cm von g. Konstruiere alle Punkte, die von g den Abstand {d_} cm und von P den Abstand {r_} cm haben.",
             "Schnittpunkte von Parallelenpaar und Kreis", [f"zwei Parallelen zu g im Abstand {d_} cm", f"Kreis um P mit r = {r_} cm", "Schnittpunkte markieren"])


# ============================================================ Winkelsätze
@reg(("geometrie.winkelsaetze", "stufen_wechsel"), ("geometrie.winkelsaetze", "figuren"), ("geometrie.winkelsaetze", "beweisen"),
     ("geometrie.winkelsaetze", "innenwinkelsumme"), ("geometrie.winkelsaetze", "parallel_pruefen"), ("geometrie.winkelsaetze", "vieleck"),
     ("geometrie.winkelsaetze", "scheitel_neben"))
def _(c):
    et = c.z["etappe"]; al = c.ri(25, 75)
    if et in ("stufen_wechsel", "scheitel_neben"):
        chk(4 * al + 4 * (180 - al) == 720, "zwei Vollwinkel")
        return T(f"Zwei parallele Geraden g und h werden von einer Geraden s geschnitten. Ein Winkel an g beträgt {al}°. Gib alle anderen sieben Winkel an und begründe mit Fachbegriffen.",
                 f"je vier Winkel {al}° und {180-al}°", [f"Scheitelwinkel: {al}°", f"Nebenwinkel: {180-al}°", "Stufen-/Wechselwinkel an h gleich groß"])
    if et == "parallel_pruefen":
        b_ = al + c.ch((0, 0, 1, 2))
        return T(f"Eine Gerade s schneidet g unter {al}° und h unter {b_}° (Stufenwinkel). Sind g und h parallel? Begründe.",
                 "ja" if b_ == al else "nein", ["Stufenwinkel gleich ↔ parallel", f"{al}° {'=' if b_==al else '≠'} {b_}°"])
    if et == "innenwinkelsumme":
        w1, w2 = c.ri(95, 120), c.ri(60, 100)
        return T(f"Gibt es ein Dreieck mit den Winkeln {w1}° und {w2}°? Begründe.", "nein" if w1 + w2 >= 180 else "ja",
                 [f"{w1}° + {w2}° = {w1+w2}°", "Winkelsumme 180° " + ("überschritten" if w1 + w2 >= 180 else f"→ dritter Winkel {180-w1-w2}°")])
    if et == "vieleck":
        nn = c.ri(5, 12)
        su = (nn - 2) * 180
        chk(su == 180 * nn - 360, "Zerlegung in Dreiecke vom Mittelpunkt")
        if c.has("eckenzahl") or c.niv == "II" and c.ch((0, 1)):
            return T(f"Die Innenwinkel eines Vielecks ergeben zusammen {su}°. Wie viele Ecken hat es?", str(nn), ["(n − 2)·180° = " + str(su) + "°", f"n − 2 = {nn-2} → n = {nn}"])
        w = F(su, nn)
        return T(f"Berechne die Größe eines Innenwinkels eines regelmäßigen {nn}-Ecks.", f"{fz(w, dez=True) if endlich(w) else gerundet(w,1)}°",
                 [f"Winkelsumme (n − 2)·180° = {su}°", f"geteilt durch {nn}"])
    if et == "beweisen":
        return T("In einem gleichschenkligen Dreieck ABC (AC = BC) wird die Seite [AC] über C hinaus verlängert. Zeige: Der Außenwinkel bei C ist doppelt so groß wie ein Basiswinkel.",
                 "Außenwinkel = 2α", ["Basiswinkel α = β", "Außenwinkel = Summe der nicht anliegenden Innenwinkel = α + β", "= 2α"])
    g_ = c.ri(30, 80)
    chk(g_ + 2 * F(180 - g_, 2) == 180, "Winkelsumme")
    return T(f"In einem gleichschenkligen Dreieck beträgt der Winkel an der Spitze {g_}°. Berechne die Basiswinkel und nenne die verwendeten Sätze.",
             f"je {fz(F(180-g_,2), dez=True)}°", ["Basiswinkel gleich groß", f"(180° − {g_}°) : 2 = {fz(F(180-g_,2), dez=True)}°"])


# ============================================================ Grundbegriffe (auch Kl. 5)
@reg(("geometrie.grundbegriffe", "vierecke"))
def _(c):
    if c.k5:
        v = c.ch(("Quadrat", "Rechteck", "Parallelogramm", "Raute", "Drachenviereck"))
        if c.has("eigenschaft", "beschreib", "bedingung", "ankreuz"):
            eig = {"Quadrat": "4 gleich lange Seiten, 4 rechte Winkel", "Rechteck": "gegenüberliegende Seiten gleich lang und parallel, 4 rechte Winkel",
                   "Parallelogramm": "gegenüberliegende Seiten parallel und gleich lang", "Raute": "4 gleich lange Seiten, gegenüberliegende Seiten parallel",
                   "Drachenviereck": "zwei Paare benachbarter gleich langer Seiten, Diagonalen senkrecht"}[v]
            return T(f"Nenne drei Eigenschaften dieser Figur: {v}.", eig, ["Seiten", "Winkel/Parallelität", "Diagonalen"])
        A = (1, 1); s_ = c.ri(2, 5)
        return T(f"Die Punkte A(1|1), B({1+s_}|1) und C({1+s_}|{1+s_}) sind Ecken eines Quadrats. Zeichne es in ein Koordinatensystem und gib den fehlenden Eckpunkt D an.",
                 f"D(1|{1+s_})", ["gleiche Seitenlänge " + str(s_), "D liegt senkrecht über A"])
    A = (c.ri(-3, 1), c.ri(-3, 0)); B = (A[0] + c.ri(3, 6), A[1] + c.ri(-1, 1)); C = (B[0] + c.ri(1, 3), B[1] + c.ri(2, 4))
    D = (A[0] + C[0] - B[0], A[1] + C[1] - B[1])
    chk(D[0] - A[0] == C[0] - B[0], "AD parallel BC")
    return T(f"A{pk(A)}, B{pk(B)} und C{pk(C)} sind Eckpunkte des Parallelogramms ABCD. Gib die Koordinaten von D an.", f"D{pk(D)}",
             ["Verschiebung von B nach C auf A anwenden", f"D = A + (C − B) = {pk(D)}"])


@reg(("geometrie.grundbegriffe", "koordinaten"))
def _(c):
    if c.k5:
        pts = [(c.ri(0, 9), c.ri(0, 9)) for _ in range(4 if c.niv == "I" else 3)]
        if c.has("fehler"):
            p0 = pts[0]
            return T(f"Ida soll P({p0[0]}|{p0[1]}) eintragen und markiert den Punkt ({p0[1]}|{p0[0]}). Beschreibe ihren Fehler.", "x- und y-Koordinate vertauscht",
                     ["zuerst nach rechts (x), dann nach oben (y)"])
        return T(f"Zeichne ein Koordinatensystem (1 LE = 1 cm) und trage die Punkte {', '.join(f'{chr(65+i)}({px}|{py})' for i, (px, py) in enumerate(pts))} ein. Verbinde sie der Reihe nach.",
                 "Punkte im Koordinatensystem", ["x-Wert nach rechts, y-Wert nach oben", "der Reihe nach verbinden"])
    a_, b_ = c.ri(1, 3), c.ri(5, 8); h_ = c.ri(2, 5); d_ = c.ri(1, 2)
    D = (a_ + d_, h_); C = (b_ - d_, h_)
    return T(f"A({a_}|0), B({b_}|0) und D({D[0]}|{h_}) sind Ecken eines gleichschenkligen Trapezes ABCD mit AB ∥ CD. Gib C an.", f"C{pk(C)}",
             [f"Symmetrieachse x = {fz(F(a_+b_,2))}", f"C ist Spiegelbild von D: x = {a_+b_} − {D[0]} = {C[0]}"])


@reg(("geometrie.grundbegriffe", "lagebeziehungen"))
def _(c):
    if not c.k5:
        return T("Ergänze den Satz: „Der Abstand eines Punktes P von einer Geraden g ist die Länge …“", "der kürzesten Verbindungsstrecke, also des Lots von P auf g",
                 ["Lot fällen", "Länge der Lotstrecke"])
    v = c.ri(0, 3)
    P_ = (c.ri(1, 7), c.ri(4, 8))
    if c.has("parallele", "senkrechte") or v == 0:
        art = "Parallele" if c.has("parallel") else ("Senkrechte" if c.has("senkrecht") else c.ch(("Parallele", "Senkrechte")))
        return T(f"Zeichne eine Gerade g durch A(0|1) und B(8|3) und den Punkt P{pk(P_)}. Zeichne die {art} zu g durch P.",
                 f"{art} durch P", ["Geodreieck an g anlegen", "parallel bzw. senkrecht verschieben bis P", "Linie zeichnen"])
    if c.has("abstand", "messen", "nächs") or v == 1:
        return T(f"Zeichne die Gerade g durch A(0|0) und B(9|0) und den Punkt P({c.ri(1,8)}|{c.ri(2,6)}). Miss den Abstand von P zu g.", "Abstand = y-Wert von P (in cm)",
                 ["Lot von P auf g", "Länge messen"])
    return T("Zeichne vier Geraden a, b, c, d so, dass a ∥ b, c ⊥ a und d weder zu a noch zu c parallel ist. Notiere alle Lagebeziehungen mit Zeichen.",
             "a ∥ b, c ⊥ a, c ⊥ b", ["Parallele mit Geodreieck", "Senkrechte", "Zeichen ∥ und ⊥"])


# ============================================================ Flächen (auch Kl. 5)
@reg(("messen.flaechen", "einheiten"))
def _(c):
    if c.k5 or c.has("umrechnen", "nächst", "gemischt"):
        aufg = []
        for _ in range(3):
            e = c.ch((("m²", "dm²", 100), ("dm²", "cm²", 100), ("ha", "a", 100), ("a", "m²", 100), ("km²", "ha", 100), ("cm²", "mm²", 100)))
            w = c.ri(2, 90)
            if c.has("größer"):
                aufg.append((f"{fz(w*100)} {e[1]}", f"{w} {e[0]}"))
            else:
                aufg.append((f"{w} {e[0]}", f"{fz(w*100)} {e[1]}"))
        chk(len(aufg) == 3, "Umrechnungszahl 100")
        return T("Rechne in die angegebene Nachbareinheit um: " + "; ".join(f"{q} = ___" for q, _ in aufg), "; ".join(f"{q} = {z}" for q, z in aufg),
                 ["Umrechnungszahl bei Flächen 100"])
    l_, f_ = c.ri(2, 9), c.ri(3, 9)
    return T(f"Ein Mitschüler sagt: „1 m² sind 10 dm².“ Begründe mit einer Skizze, dass das falsch ist, und gib den richtigen Wert an.", "1 m² = 100 dm²",
             ["Quadrat mit 1 m = 10 dm Seite", "10 · 10 Quadrate mit 1 dm² Fläche"])


@reg(("messen.flaechen", "sachaufgaben"))
def _(c):
    a_, b_ = c.ri(8, 30), c.ri(5, 20)
    if c.has("zaun", "umfang", "lauf"):
        chk(ev(f"2 · ({a_} + {b_})") == 2 * (a_ + b_), "Umfang")
        return T(f"Ein rechteckiger Park ist {a_} m lang und {b_} m breit. Wie lang ist ein Weg einmal ganz außen herum, und wie groß ist die Fläche des Parks?",
                 f"{2*(a_+b_)} m; {a_*b_} m²", [f"u = 2·({a_} + {b_}) = {2*(a_+b_)} m", f"A = {a_}·{b_} = {a_*b_} m²"])
    d_ = c.ri(2, 4); rw = c.ri(8, 12); L_ = a_ // 3 + 4
    eimer = -(-L_ * d_ // rw)
    chk(eimer * rw >= L_ * d_ > (eimer - 1) * rw, "kleinste ausreichende Anzahl")
    return T(f"Eine Wand ist {L_} m lang und {d_} m hoch; ein Eimer Farbe reicht für {rw} m². Wie viele Eimer braucht man mindestens?",
             f"{eimer} Eimer", [f"A = {L_}·{d_} = {L_*d_} m²", f"{L_*d_} : {rw} ≈ {gerundet(F(L_*d_,rw),1)} → aufrunden auf {eimer}"])


@reg(("messen.flaechen", "zerlegen"))
def _(c):
    a_, b_, q_ = c.ri(8, 16), c.ri(6, 12), c.ri(2, 4)
    A_ = a_ * b_ - q_ * q_
    chk(flaeche([(0, 0), (a_, 0), (a_, b_ - q_), (a_ - q_, b_ - q_), (a_ - q_, b_), (0, b_)]) == A_, "Fläche über Koordinaten (Gaußsche Formel)")
    if not c.k5 and c.niv == "III":
        return T(f"Aus einer rechteckigen Platte ({a_} cm × {b_} cm) sollen zwei gleich große quadratische Löcher geschnitten werden, sodass die Restfläche genau die Hälfte ist. Wie lang ist die Seite eines Lochs?",
                 f"√({a_*b_}/4) ≈ {gerundet(F(round((a_*b_/4)**0.5*10),10),1)} cm",
                 [f"Lochfläche zusammen {fz(F(a_*b_,2))} cm²", f"ein Loch {fz(F(a_*b_,4))} cm²", "Seite = Wurzel daraus"])
    u_ = 2 * (a_ + b_)
    return T(f"Aus einem Rechteck ({a_} cm × {b_} cm) wird an einer Ecke ein Quadrat mit {q_} cm Seitenlänge herausgeschnitten. Berechne Flächeninhalt und Umfang der Restfigur.",
             f"A = {A_} cm²; u = {u_} cm", [f"{a_}·{b_} − {q_}·{q_} = {A_}", "Umfang bleibt gleich (zwei Kanten werden nur verschoben)", f"u = {u_} cm"])


@reg(("messen.flaechen_vielecke", "dreieck"), ("messen.flaechen_vielecke", "parallelogramm"), ("messen.flaechen_vielecke", "drachen_raute"),
     ("messen.flaechen_vielecke", "trapez"), ("messen.flaechen_vielecke", "zusammengesetzt"), ("messen.flaechen_vielecke", "rueckwaerts"),
     ("messen.flaechen_vielecke", "verstehen"))
def _(c):
    et = c.z["etappe"]
    if et == "dreieck":
        A = (c.ri(0, 2), c.ri(0, 2)); B = (A[0] + c.ri(4, 8), A[1]); C = (c.ri(A[0], B[0]), A[1] + c.ri(3, 6))
        fl = flaeche([A, B, C])
        chk(fl == F((B[0] - A[0]) * (C[1] - A[1]), 2), "Formel = Gaußsche Fläche")
        return T(f"Berechne den Flächeninhalt des Dreiecks A{pk(A)}, B{pk(B)}, C{pk(C)} (1 LE = 1 cm). Zeichne die verwendete Höhe ein.", f"{fz(fl, dez=True)} cm²",
                 [f"g = [AB] = {B[0]-A[0]} cm", f"h = {C[1]-A[1]} cm", f"A = ½·{B[0]-A[0]}·{C[1]-A[1]}"])
    if et == "parallelogramm":
        g_, h_ = c.ri(3, 9), c.ri(2, 7); s_ = c.ri(1, 3)
        pts = [(0, 0), (g_, 0), (g_ + s_, h_), (s_, h_)]
        chk(flaeche(pts) == g_ * h_, "Koordinatenfläche")
        return T(f"Berechne den Flächeninhalt des Parallelogramms mit den Ecken {', '.join(pk(p) for p in pts)}.", f"{g_*h_} FE", [f"g = {g_}, h = {h_}", f"A = {g_*h_}"])
    if et == "drachen_raute":
        e_, f_ = c.ri(4, 12), c.ri(3, 10)
        if c.has("term"):
            return T("Ein Drachenviereck hat die Diagonalen e = 2r und f = 3r. Gib einen Term für den Flächeninhalt an.", "A = 3r²", ["A = ½·e·f = ½·2r·3r = 3r²"])
        chk(flaeche([(0, F(f_, 2)), (F(e_, 2), 0), (0, F(-f_, 2)), (F(-e_, 2), 0)]) == F(e_ * f_, 2), "Fläche über Koordinaten")
        return T(f"Eine Raute hat die Diagonalen {e_} cm und {f_} cm. Berechne ihren Flächeninhalt und begründe die Formel kurz.", f"{fz(F(e_*f_,2), dez=True)} cm²",
                 ["Raute = halbes Rechteck aus den Diagonalen", f"A = ½·{e_}·{f_}"])
    if et == "trapez":
        return T("Leite die Flächenformel für das Trapez her, indem du es mit einer Diagonale in zwei Dreiecke zerlegst.", "A = ½(a + c)·h",
                 ["Dreieck 1: ½·a·h", "Dreieck 2: ½·c·h", "Summe ½(a + c)·h"])
    if et == "zusammengesetzt":
        pts = [(0, 0), (c.ri(5, 8), c.ri(-1, 1)), (c.ri(6, 9), c.ri(4, 6)), (c.ri(0, 2), c.ri(3, 5))]
        fl = flaeche(pts)
        return T(f"Berechne den Flächeninhalt des Vierecks mit den Eckpunkten {', '.join(pk(p) for p in pts)} (1 LE = 1 cm).", f"{fz(fl, dez=True)} cm²",
                 ["umschließendes Rechteck oder Zerlegung in zwei Dreiecke", "Teilflächen addieren bzw. abziehen", f"A = {fz(fl, dez=True)}"])
    if et == "rueckwaerts":
        a_ = c.ri(6, 12); h_ = 2 * c.ri(2, 5)
        return T(f"Ein Rechteck ({a_} cm × {h_} cm) wird durch eine Strecke von einer Ecke zu einem Punkt P auf der gegenüberliegenden langen Seite so geteilt, dass ein Dreieck mit einem Viertel der Rechteckfläche entsteht. Wie weit ist P von der Ecke entfernt?",
                 f"{fz(F(a_,2), dez=True)} cm", [f"Rechteckfläche {a_*h_} cm²", f"Dreieck {fz(F(a_*h_,4))} = ½·x·{h_}", f"x = {fz(F(a_,2), dez=True)}"])
    g_, h_ = c.ri(4, 8), c.ri(3, 6)
    return T(f"Ein Dreieck ABC hat die Grundseite [AB] = {g_} cm und die Höhe {h_} cm. Wo liegen alle Punkte C', für die das Dreieck ABC' denselben Flächeninhalt hat? Begründe.",
             f"auf den Parallelen zu AB im Abstand {h_} cm", ["gleiche Grundseite und gleiche Höhe → gleiche Fläche", "Parallele zu AB durch C (und auf der anderen Seite)"])


# ============================================================ Körper, Volumen
@reg(("messen.koerper_darstellung", "prisma"), ("messen.koerper_darstellung", "schraegbild"))
def _(c):
    if c.z["etappe"] == "prisma":
        nn = c.ri(3, 9)
        return T(f"Wie viele Ecken, Kanten und Flächen hat ein Prisma mit {nn}-eckiger Grundfläche?", f"{2*nn} Ecken, {3*nn} Kanten, {nn+2} Flächen",
                 [f"zwei {nn}-Ecke → {2*nn} Ecken", f"{nn} + {nn} + {nn} Kanten", f"{nn} Seitenflächen + 2"])
    return T("Im Schrägbild eines Quaders ABCDEFGH (ABCD unten, E über A). Welche Kante steht senkrecht auf der Grundfläche und wie wird sie im Schrägbild gezeichnet?",
             "z. B. [AE]; senkrecht nach oben, in wahrer Länge", ["senkrechte Kanten: AE, BF, CG, DH", "im Schrägbild senkrecht und unverkürzt"])


@reg(("messen.volumen", "zusammengesetzt"), ("messen.volumen", "liter"), ("messen.volumen", "rueckwaerts"), ("messen.volumen", "verstehen"),
     ("messen.volumen", "einheiten"))
def _(c):
    et = c.z["etappe"]
    a_, b_, h_ = c.ri(3, 9), c.ri(2, 8), c.ri(2, 6)
    if et == "zusammengesetzt":
        a2 = c.ri(1, a_ - 1) if a_ > 2 else 1
        V = a_ * b_ * h_ - a2 * b_ * (h_ // 2 or 1)
        chk(V == (a_ - a2) * b_ * h_ + a2 * b_ * (h_ - (h_ // 2 or 1)), "andere Zerlegung ergibt dasselbe")
        return T(f"Ein L-förmiger Körper entsteht aus einem Quader ({a_} cm × {b_} cm × {h_} cm), aus dem oben ein Quader ({a2} cm × {b_} cm × {h_//2 or 1} cm) herausgeschnitten ist. Berechne das Volumen.",
                 f"{V} cm³", [f"großer Quader {a_*b_*h_} cm³", f"minus {a2*b_*(h_//2 or 1)} cm³", f"V = {V} cm³"])
    if et == "liter":
        if c.k5:
            L_ = c.ri(2, 12); g_ = c.ch((200, 250, 500))
            chk(L_ * 1000 // g_ * g_ <= L_ * 1000, "Anzahl Gläser")
            return T(f"Wie viele Gläser zu je {g_} ml kann man mit {L_} Litern Saft füllen?", fz(F(L_ * 1000, g_), dez=True) + (" (ganze Gläser: " + str(L_ * 1000 // g_) + ")" if (L_ * 1000) % g_ else ""),
                     [f"{L_} l = {L_*1000} ml", f"{L_*1000} : {g_}"])
        s_ = c.ri(2, 9) * 10
        chk(F(s_ ** 3, 1000) == ev(f"{s_} · {s_} · {s_} : 1000"), "Liter nachgerechnet")
        return T(f"Ein würfelförmiger Behälter hat die Kantenlänge {s_} cm. Wie viele Liter passen hinein?", f"{fz(F(s_**3,1000), dez=True)} l",
                 [f"V = {s_}³ = {s_**3} cm³", "1 l = 1000 cm³"])
    if et == "rueckwaerts":
        if c.k5:
            k_ = c.ri(2, 9)
            chk(round((k_ ** 3) ** (1 / 3)) == k_, "Kubikwurzel")
            return T(f"Ein Würfel hat das Volumen {k_**3} cm³. Wie lang ist eine Kante?", f"{k_} cm", [f"{k_}·{k_}·{k_} = {k_**3}"])
        L_ = a_ * b_ * h_ // 1
        chk(F(a_ * b_ * h_ * 1000) / (a_ * 10 * b_ * 10) == h_ * 10, "Höhe = Volumen : Grundfläche")
        return T(f"Ein Aquarium hat eine Grundfläche von {a_*10} cm × {b_*10} cm und soll {fz(F(a_*b_*h_*1000,1000), dez=True)} Liter fassen. Wie hoch steht das Wasser?",
                 f"{h_*10} cm", [f"V = {a_*b_*h_*1000} cm³", f"h = V : ({a_*10}·{b_*10}) = {h_*10} cm"])
    if et == "einheiten":
        v_ = c.ri(2, 9)
        return T(f"Welche Angaben sind gleich groß? (A) {v_} dm³  (B) {v_} l  (C) {v_*100} cm³  (D) {v_*1000} cm³  (E) {v_*1000} ml", "A, B, D, E",
                 ["1 dm³ = 1 l = 1000 cm³ = 1000 ml", f"{v_*100} cm³ passt nicht"])
    if c.k5:
        return T("Schätze das Volumen eines Würfels mit 1 m Kantenlänge in Litern und begründe.", "1000 l", ["1 m = 10 dm", "10·10·10 dm³ = 1000 l"])
    k_ = c.ch((2, 5, 10))
    return T(f"Ein Modell ist im Maßstab 1 : {k_} gebaut und hat ein Volumen von {a_*b_*h_} cm³. Welches Volumen hat das Original?", f"{a_*b_*h_*k_**3} cm³",
             [f"alle Längen ×{k_}", f"Volumen × {k_}³ = ×{k_**3}"])


@reg(("messen.prisma_zylinder", "zylinder_volumen"), ("messen.prisma_zylinder", "prisma_volumen"), ("messen.prisma_zylinder", "zylinder_oberflaeche"),
     ("messen.prisma_zylinder", "prisma_oberflaeche"))
def _(c):
    et = c.z["etappe"]; r_, h_ = c.ri(2, 9), c.ri(5, 20)
    if et == "zylinder_volumen":
        V3 = 3 * r_ * r_ * h_
        if c.has("schätz", "grob", "abschätz") or c.niv != "I":
            chk(V3 == ev(f"3 · {r_} · {r_} · {h_}"), "nachgerechnet")
            return T(f"Eine Regentonne ist ungefähr zylinderförmig mit Durchmesser {2*r_} dm und Höhe {h_} dm. Schätze das Volumen in Litern ({PI3}).", f"etwa {V3} l",
                     [f"r = {r_} dm", f"V ≈ 3·{r_}²·{h_} = {V3} dm³", "1 dm³ = 1 l"])
        return T(f"Berechne das Volumen eines Zylinders mit r = {r_} cm und h = {h_} cm (π auf zwei Dezimalen).", f"≈ {gerundet(F(314,100)*r_*r_*h_,1)} cm³",
                 [f"V = π·r²·h = π·{r_*r_}·{h_}"])
    if et == "zylinder_oberflaeche":
        return T("Erkläre, warum die Mantelfläche eines Zylinders mit M = 2π·r·h berechnet wird.", "abgewickelter Mantel ist ein Rechteck",
                 ["Mantel aufschneiden und abwickeln", "Rechteck mit Länge 2πr (Umfang) und Breite h"])
    if et == "prisma_oberflaeche":
        a_, b_ = c.ri(3, 8), c.ri(3, 8)
        return T(f"In einem Quader mit den Kanten {a_} cm, {b_} cm und {h_} cm wird die Schnittfläche durch zwei gegenüberliegende senkrechte Kanten betrachtet, die {a_} cm voneinander entfernt sind. Berechne ihren Flächeninhalt.",
                 f"{a_*h_} cm²", [f"Rechteck {a_} cm × {h_} cm"])
    g_, hd = c.ri(3, 8), c.ri(2, 6)
    V = F(g_ * hd, 2) * h_
    chk(V == ev(f"{g_} · {hd} : 2 · {h_}"), "nachgerechnet")
    return T(f"Ein Prisma hat als Grundfläche ein rechtwinkliges Dreieck mit den Katheten {g_} cm und {hd} cm; seine Höhe ist {h_} cm. Berechne das Volumen.",
             f"{fz(V, dez=True)} cm³", [f"G = ½·{g_}·{hd} = {fz(F(g_*hd,2), dez=True)} cm²", f"V = G·h"])


@reg(("messen.kreisberechnung", "flaeche"), ("messen.kreisberechnung", "umfang"), ("messen.kreisberechnung", "verstehen"),
     ("messen.kreisberechnung", "zusammengesetzt"))
def _(c):
    et = c.z["etappe"]; r_ = c.ri(2, 9)
    if et == "umfang":
        if c.has("formel", "radius"):
            return T("Stelle die Formel u = 2πr nach r um.", "r = u/(2π)", ["durch 2π teilen"])
        v = c.ri(2, 6)
        return T(f"Ein Karussell hat einen Radius von {r_} m und dreht sich {v}-mal pro Minute. Welche Strecke legt ein Platz am Rand pro Minute zurück ({PI3})?",
                 f"≈ {6*r_*v} m", [f"u ≈ 2·3·{r_} = {6*r_} m", f"× {v}"])
    if et == "flaeche":
        return T(f"Ein Scheibenwischer von {r_*10} cm Länge überstreicht einen Halbkreis. Schätze die überstrichene Fläche ({PI3}).", f"≈ {fz(F(3*(r_*10)**2,2))} cm²",
                 [f"Kreis: 3·{r_*10}² = {3*(r_*10)**2}", "halbieren"])
    if et == "verstehen":
        return T(f"Eine Ziege ist an einem {r_} m langen Seil angebunden. Wie ändert sich die Weidefläche, wenn das Seil doppelt so lang ist?", "vierfach",
                 ["A = πr²", "(2r)² = 4r²"])
    a_ = 2 * r_
    chk(4 * a_ * a_ - 6 * r_ * r_ == ev(f"{2*a_} · {2*a_} − 2 · 3 · {r_} · {r_}"), "nachgerechnet")
    return T(f"Aus einem Quadrat mit {2*a_} cm Seitenlänge werden zwei Kreise mit Radius {r_} cm ausgeschnitten. Gib einen Term für die Restfläche an und berechne sie näherungsweise ({PI3}).",
             f"{4*a_*a_} − 2π·{r_*r_} ≈ {4*a_*a_ - 6*r_*r_} cm²", [f"Quadrat {4*a_*a_} cm²", f"zwei Kreise 2π·{r_*r_}", "subtrahieren"])


# ============================================================ Lücken (Körper)
@reg(("L", "Netz eines Quaders zeichnen (Kl. 5)"))
def _(c):
    a_, b_, h_ = c.ri(2, 5), c.ri(2, 4), c.ri(1, 3)
    O = 2 * (a_ * b_ + a_ * h_ + b_ * h_)
    return T(f"Zeichne ein Netz eines Quaders mit den Kantenlängen {a_} cm, {b_} cm und {h_} cm. Beschrifte die Kantenlängen.", f"Netz aus 6 Rechtecken, zusammen {O} cm²",
             [f"je zwei Rechtecke {a_}×{b_}, {a_}×{h_}, {b_}×{h_}", "Rechtecke so anordnen, dass sie sich falten lassen", "gleich lange Kanten passen aneinander"])


@reg(("L", "Würfelnetz – Lage von Markierungen bestimmen"))
def _(c):
    return T("Ein Würfelnetz hat die Form eines Kreuzes: In der senkrechten Spalte stehen von oben nach unten die Flächen 1, 2, 3, 4; links und rechts neben Fläche 2 liegen die Flächen 5 und 6. "
             "Welche Fläche liegt nach dem Falten jeweils gegenüber von 1, 2 und 5?", "1–3, 2–4, 5–6",
             ["in einer Reihe von drei Flächen liegen die äußeren gegenüber", "1 und 3, 2 und 4", "5 und 6 links und rechts von 2"])


@reg(("L", "Eulerscher Polyedersatz"))
def _(c):
    nn = c.ri(4, 9)
    if c.niv == "III":
        return T("Zeige allgemein, dass für jedes Prisma mit n-eckiger Grundfläche gilt: Ecken + Flächen − Kanten = 2.", "2n + (n + 2) − 3n = 2",
                 ["Ecken 2n", "Flächen n + 2", "Kanten 3n"])
    e, f, k = 2 * nn, nn + 2, 3 * nn
    chk(e + f - k == 2, "Euler")
    return T(f"Prüfe die Formel e + f − k = 2 für ein Prisma mit {nn}-eckiger Grundfläche.", f"{e} + {f} − {k} = 2", [f"e = {e}", f"f = {f}", f"k = {k}"])


# ============================================================ außerhalb (Kl. 9)
@reg(("X", "Satz des Pythagoras (LehrplanPLUS Kl. 9, Test noch G8)"), ("X", "Satz des Pythagoras (Kl. 9)"))
def _(c):
    k = c.ri(1, 3); a_, b_, cc = (3 * k, 4 * k, 5 * k) if c.ch((0, 1)) else (5 * k, 12 * k, 13 * k)
    chk(a_ ** 2 + b_ ** 2 == cc ** 2, "Pythagoras")
    return T(f"Eine Leiter ist {cc} dm lang; ihr Fuß steht {a_} dm von der Wand entfernt. Stelle eine Gleichung mit dem Satz des Pythagoras auf und berechne die Höhe, die sie an der Wand erreicht.",
             f"{b_} dm", [f"{a_}² + h² = {cc}²", f"h² = {cc*cc - a_*a_}", f"h = {b_}"])


@reg(("X", "Gleichung x² = a (Wurzel, LehrplanPLUS Kl. 9)"))
def _(c):
    k = c.ri(2, 9)
    return T(f"Ein Quadrat hat den Flächeninhalt 4x² = {4*k*k} cm². Bestimme x und die Seitenlänge.", f"x = {k}; Seite {2*k} cm", [f"x² = {k*k}", f"x = {k} (positiv)"])
