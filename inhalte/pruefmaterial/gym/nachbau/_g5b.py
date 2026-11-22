# Generatoren Klasse 5: Geometrie, Flächen, Körper
from _kern import *


@reg(("messen.flaechen", "rechteck"))
def _(c):
    a_, b_ = c.ri(3, 25), c.ri(2, 18)
    if c.has("tabelle"):
        zeilen = []
        loes = []
        for i in range(3):
            l_, br = c.ri(3, 20), c.ri(2, 15)
            gegeben = c.ch(("lb", "lu", "lA"))
            u_, A_ = 2 * (l_ + br), l_ * br
            if gegeben == "lb":
                zeilen.append((f"{l_} cm", f"{br} cm", "", ""))
            elif gegeben == "lu":
                zeilen.append((f"{l_} cm", "", f"{u_} cm", ""))
            else:
                zeilen.append((f"{l_} cm", "", "", f"{A_} cm²"))
            chk(ev(f"2 · ({l_} + {br})") == u_ and ev(f"{l_} · {br}") == A_, "Umfang und Fläche nachgerechnet")
            loes.append(f"b = {br} cm, u = {u_} cm, A = {A_} cm²")
        return T("Ergänze die Tabelle für Rechtecke:\n" + tabelle(["Länge", "Breite", "Umfang", "Flächeninhalt"], zeilen), " | ".join(loes),
                 ["u = 2·(l + b), A = l·b", "fehlende Breite aus u: b = u : 2 − l bzw. aus A: b = A : l"])
    if c.has("aus umfang", "seite und fläche", "breite aus", "seite aus"):
        u_ = 2 * (a_ + b_)
        chk(ev(f"{u_} : 2 − {a_}") == b_, "Breite aus Umfang")
        return T(f"Ein Rechteck ist {a_} m lang und hat einen Umfang von {u_} m. Berechne die Breite und den Flächeninhalt.", f"b = {b_} m; A = {a_*b_} m²",
                 [f"{u_} : 2 = {a_+b_}", f"b = {a_+b_} − {a_} = {b_}", f"A = {a_*b_} m²"])
    if c.has("zeichnen", "zeichne"):
        A_ = a_ * b_ if a_ * b_ <= 48 else 24
        chk(all(t * (A_ // t) == A_ for t in teiler(A_)[1:3]), "Teilerpaare")
        return T(f"Zeichne zwei verschiedene Rechtecke mit dem Flächeninhalt {A_} cm². Gib jeweils den Umfang an.", "z. B. " + "; ".join(f"{t}×{A_//t} cm (u = {2*(t+A_//t)} cm)" for t in teiler(A_)[1:3]),
                 ["Teilerpaare des Flächeninhalts", "Umfang berechnen"])
    chk(ev(f"2 · ({a_} + {b_})") == 2 * (a_ + b_) and ev(f"{a_} · {b_}") == a_ * b_, "nachgerechnet")
    return T(f"Ein Rechteck ist {a_} cm lang und {b_} cm breit. Berechne Umfang und Flächeninhalt.", f"u = {2*(a_+b_)} cm; A = {a_*b_} cm²",
             [f"u = 2·({a_} + {b_})", f"A = {a_}·{b_}"])


@reg(("messen.flaechen", "verstehen"))
def _(c):
    a_, b_ = c.ri(3, 12), c.ri(2, 9)
    if c.has("quadrat", "maßzahl"):
        chk([s_ for s_ in range(1, 50) if 4 * s_ == s_ * s_] == [4], "alle Seitenlängen durchprobiert")
        return T("Bei welchem Quadrat haben Umfang (in cm) und Flächeninhalt (in cm²) dieselbe Maßzahl? Begründe.", "Seitenlänge 4 cm", ["u = 4·s, A = s·s", "4·s = s·s → s = 4"])
    if c.has("verdoppel"):
        chk(2 * (2 * a_ + 2 * b_) == 2 * (2 * (a_ + b_)) and (2 * a_) * (2 * b_) == 4 * a_ * b_, "Verdopplung nachgerechnet")
        return T(f"Ein Rechteck ist {a_} cm lang und {b_} cm breit. Wie ändern sich Umfang und Flächeninhalt, wenn man beide Seiten verdoppelt?",
                 "Umfang doppelt, Fläche vierfach", [f"u: {2*(a_+b_)} → {4*(a_+b_)} cm", f"A: {a_*b_} → {4*a_*b_} cm²"])
    if c.has("gleicher fläche", "flächengleich", "gleich groß"):
        chk(a_ * 2 * b_ == 2 * a_ * b_, "gleiche Fläche")
        return T(f"Zeichne ein Rechteck mit derselben Fläche wie ein Rechteck mit {a_*2} cm × {b_} cm, aber mit anderen Seitenlängen. Haben beide denselben Umfang?",
                 f"z. B. {a_} cm × {2*b_} cm; Umfang {2*(a_+2*b_)} cm statt {2*(2*a_+b_)} cm", ["eine Seite halbieren, die andere verdoppeln", "Umfänge vergleichen"])
    if c.has("teil", "größte", "vergleich"):
        chk(ev(f"2 · ({a_} + {b_})") == 2 * (a_ + b_), "Umfang")
        return T(f"Ein Rechteck ({a_*2} cm × {b_} cm) wird in zwei gleich große Rechtecke geteilt, indem man die lange Seite halbiert. Wie groß ist der Umfang eines Teilrechtecks?",
                 f"{2*(a_+b_)} cm", [f"Teilrechteck {a_} cm × {b_} cm", f"u = 2·({a_} + {b_})"])
    chk(ev(f"{a_} + {b_} + {a_} + {b_}") == ev(f"2 · ({a_} + {b_})") != ev(f"{a_} · {b_}") or a_ * b_ == 2 * (a_ + b_), "Rechenwege verglichen")
    return T(f"Ein Faden umspannt ein Rechteck mit {a_} cm × {b_} cm. Welche Rechnungen liefern die Fadenlänge? (A) {a_} + {b_} + {a_} + {b_}  (B) 2 · {a_} + 2 · {b_}  (C) {a_} · {b_}  (D) 2 · ({a_} + {b_})",
             "A, B, D", ["Umfang = Summe aller Seiten", "C ist der Flächeninhalt"])


@reg(("messen.flaechen", "einheitsquadrate"), ("messen.flaechen", "kommaschreibweise"))
def _(c):
    if c.z["etappe"] == "kommaschreibweise":
        v = c.ri(2, 9) * 100 + c.ri(1, 99)
        chk(F(v, 100) * 10000 == v * 100, "Umrechnung")
        return T(f"Ergänze die Kette gleich großer Flächen: {v} dm² = ___ m² = ___ cm²", f"{fd(F(v,100))} m² = {v*100} cm²", ["1 m² = 100 dm²", "1 dm² = 100 cm²"])
    if c.has("schätz"):
        voll, halb = c.ri(15, 40), c.ri(6, 16)
        chk(voll + halb // 2 == voll + int(F(halb, 2)), "Schätzwert")
        return T(f"Ein Blatt liegt auf Karopapier (1 Kästchen = 1 cm²). Es bedeckt {voll} Kästchen ganz und {halb} Kästchen ungefähr zur Hälfte. Schätze den Flächeninhalt.",
                 f"etwa {voll + halb//2} cm²", ["ganze Kästchen zählen", "halbe paarweise zusammenfassen"])
    a_, b_ = c.ri(3, 8), c.ri(2, 6); q_ = c.ri(1, 2)
    chk(ev(f"{a_} · {b_} + {q_} · {q_}") == a_ * b_ + q_ * q_, "nachgerechnet")
    return T(f"Eine Figur besteht aus einem Rechteck aus {a_}·{b_} Einheitsquadraten, an dessen Seite ein Quadrat aus {q_}·{q_} Einheitsquadraten angesetzt ist. Wie groß ist ihr Flächeninhalt (1 Einheitsquadrat = 1 cm²)?",
             f"{a_*b_+q_*q_} cm²", [f"{a_*b_} + {q_*q_}"])


@reg(("geometrie.grundbegriffe", "winkelarten"))
def _(c):
    w = [c.ri(5, 355) for _ in range(4)]
    art = lambda v: "spitz" if v < 90 else "recht" if v == 90 else "stumpf" if v < 180 else "gestreckt" if v == 180 else "überstumpf"
    if c.has("zeichn"):
        z = c.ri(20, 170) if not c.has("stumpf") else c.ri(95, 175)
        return T(f"Zeichne einen Winkel von {z}° und benenne seine Art.", f"{art(z)}er Winkel", ["Scheitel und ersten Schenkel zeichnen", f"mit Geodreieck {z}° antragen"])
    if c.has("mess"):
        A = (0, 0); z = c.ri(25, 160)
        return T(f"Zeichne die Halbgeraden vom Scheitel S aus durch die Punkte P(6|0) und Q, wobei Q so liegt, dass ∢PSQ = {z}° ist; miss dann den Winkel nach. Wie heißt diese Winkelart?",
                 f"{z}°, {art(z)}", ["Geodreieck am Scheitel anlegen", "Skala von 0 aus ablesen"])
    if c.has("markier", "stumpf"):
        return T("Welche der Winkel 35°, 90°, 112°, 180°, 275° sind stumpf, welche überstumpf?", "stumpf: 112°; überstumpf: 275°", ["stumpf: zwischen 90° und 180°", "überstumpf: zwischen 180° und 360°"])
    chk(all((v < 90) + (v < 180) + (v < 360) >= 1 for v in w), "Bereiche")
    return T("Bestimme die Winkelart: " + ", ".join(f"{v}°" for v in w), ", ".join(f"{v}°: {art(v)}" for v in w), ["Vergleich mit 90°, 180°, 360°"])


@reg(("geometrie.grundbegriffe", "strecken"), ("geometrie.grundbegriffe", "verstehen"))
def _(c):
    if c.z["etappe"] == "verstehen":
        return T("Behauptung: „Zwei Geraden, die beide senkrecht zu einer dritten Geraden sind, schneiden sich.“ Widerlege mit einer Skizze.", "falsch – sie sind parallel",
                 ["zwei Senkrechte zu g zeichnen", "sie verlaufen parallel"])
    A = (c.ri(0, 3), c.ri(0, 3)); B = (A[0] + c.ri(3, 7), A[1] + c.ri(0, 4))
    if c.has("strecke, gerade", "strahl", "linienarten"):
        return T("Zeichne durch A(1|1) und B(6|3) eine Strecke [AB], einen Strahl [AB und eine Gerade AB in drei Farben. Erkläre die Unterschiede.",
                 "Strecke: begrenzt; Strahl: ein Anfangspunkt; Gerade: unbegrenzt", ["zwei, ein bzw. kein Endpunkt"])
    d2 = (B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2
    chk(abs(math.hypot(B[0] - A[0], B[1] - A[1]) ** 2 - d2) < 1e-9, "Länge über Koordinaten")
    return T(f"Zeichne die Strecke [AB] mit A({A[0]}|{A[1]}) und B({B[0]}|{B[1]}) (1 LE = 1 cm) und miss ihre Länge auf mm genau.",
             f"≈ {gerundet(F(round(d2**0.5*10),10),1)} cm", ["Punkte eintragen und verbinden", "mit dem Lineal messen"])


@reg(("messen.koerper_berechnung", "verstehen"), ("messen.koerper_berechnung", "quader"))
def _(c):
    et = c.z["etappe"]
    if et == "verstehen":
        if c.has("würfel ein quader", "jeder würfel"):
            return T("Ist jeder Würfel ein Quader? Begründe.", "ja", ["Würfel hat alle Quadereigenschaften (Rechtecksflächen, rechte Winkel)", "zusätzlich alle Kanten gleich lang"])
        if c.has("quader ein würfel", "jeder quader"):
            return T("Ist jeder Quader ein Würfel? Begründe.", "nein", ["Quader kann verschieden lange Kanten haben, z. B. 2 × 3 × 5 cm"])
        if c.has("kegel", "pyramide", "unterschied"):
            return T("Nenne einen Unterschied zwischen Kegel und Pyramide.", "Kegel: kreisförmige Grundfläche, gekrümmte Mantelfläche; Pyramide: Vieleck als Grundfläche, Dreiecke als Seiten", ["Grundfläche vergleichen"])
        k = c.ch([("Quader", 8, 12, 6), ("quadratische Pyramide", 5, 8, 5), ("dreiseitiges Prisma", 6, 9, 5), ("Würfel", 8, 12, 6)])
        return T(f"Wie viele Ecken, Kanten und Flächen hat ein {k[0]}?", f"{k[1]} Ecken, {k[2]} Kanten, {k[3]} Flächen", ["am Modell oder Schrägbild zählen"])
    a_, b_, h_ = c.ri(2, 9), c.ri(2, 9), c.ri(2, 9)
    if c.has("benenn"):
        return T("Benenne die Körper: (1) sechs gleiche Quadrate als Seitenflächen; (2) zwei Kreise und eine gekrümmte Fläche; (3) eine Spitze und ein Viereck als Grundfläche.",
                 "Würfel; Zylinder; (vierseitige) Pyramide", ["Flächen zählen und benennen"])
    if c.has("karton", "passend"):
        V_ = a_ * b_ * h_
        return T(f"Ein Spiel ist {a_} cm × {b_} cm × {h_} cm groß. Welcher Karton passt: (A) {a_+1}×{b_+1}×{h_-1} cm, (B) {a_+1}×{b_}×{h_+1} cm, (C) {a_-1}×{b_+2}×{h_+2} cm?", "B",
                 ["jede Kante muss mindestens so lang sein", "A zu niedrig, C zu schmal"])
    chk(ev(f"4 · ({a_} + {b_} + {h_})") == 4 * (a_ + b_ + h_), "Kantenlänge")
    return T(f"Ein Quadernetz hat eine Grundfläche von {a_} cm × {b_} cm; die gesamte Kantenlänge des Quaders beträgt {4*(a_+b_+h_)} cm. Wie hoch ist der Quader?", f"{h_} cm",
             [f"4·({a_} + {b_} + h) = {4*(a_+b_+h_)}", f"h = {h_}"])


@reg(("messen.koerper_berechnung", "zusammengesetzt"), ("messen.koerper_berechnung", "oberflaeche"), ("messen.koerper_berechnung", "sachaufgaben"))
def _(c):
    et = c.z["etappe"]
    if et == "oberflaeche":
        a_, b_, h_ = c.ri(2, 9), c.ri(2, 9), c.ri(2, 9)
        if c.has("würfel"):
            chk(ev(f"6 · {a_} · {a_}") == 6 * a_ * a_, "nachgerechnet")
            return T(f"Berechne die Oberfläche eines Würfels mit {a_} cm Kantenlänge.", f"{6*a_*a_} cm²", [f"6·{a_}·{a_}"])
        if c.has("heraus", "änderung"):
            return T("Aus einer Ecke eines großen Würfels wird ein kleiner Würfel herausgeschnitten. Ändert sich die Oberfläche? Begründe.", "bleibt gleich",
                     ["drei Quadrate fallen weg", "drei gleich große Quadrate kommen innen dazu"])
        O = 2 * (a_ * b_ + a_ * h_ + b_ * h_)
        chk(O == sum(1 for i in range(a_) for j in range(b_) for k in range(h_) for nb in ((i - 1, j, k), (i + 1, j, k), (i, j - 1, k), (i, j + 1, k), (i, j, k - 1), (i, j, k + 1))
                     if not (0 <= nb[0] < a_ and 0 <= nb[1] < b_ and 0 <= nb[2] < h_)), "Oberfläche durch Zählen der Außenflächen von Einheitswürfeln")
        return T(f"Ein Quader ist {a_} cm lang, {b_*10} mm breit und {h_} cm hoch. Berechne seine Oberfläche und sein Volumen.", f"O = {O} cm²; V = {a_*b_*h_} cm³",
                 [f"{b_*10} mm = {b_} cm", f"O = 2·({a_*b_} + {a_*h_} + {b_*h_})", f"V = {a_}·{b_}·{h_}"])
    if et == "sachaufgaben":
        a_, b_, h_ = c.ri(10, 40), c.ri(10, 30), c.ri(5, 20); sch = c.ri(10, 30)
        if c.has("turm", "höhe"):
            hs = sorted(c.r.sample(range(2, 12), 3))
            chk(hs[2] + hs[1] + hs[2] == max(hs[0], hs[1], hs[2]) + max(hs[1], hs[0]) + max(hs[2], hs[0]), "längste Kanten gewählt")
            return T(f"Drei Quader haben die Kanten {hs[0]}×{hs[1]}×{hs[2]} cm, {hs[1]}×{hs[1]}×{hs[0]} cm und {hs[2]}×{hs[0]}×{hs[0]} cm. Wie hoch kann ein Turm aus allen drei höchstens werden?",
                     f"{hs[2]*2 + hs[1]} cm", ["jeden Quader auf seine längste Kante stellen", f"{hs[2]} + {hs[1]} + {hs[2]}"])
        chk(ev(f"2 · ({a_} + {h_}) + 2 · ({b_} + {h_}) + {sch}") == 2 * (a_ + h_) + 2 * (b_ + h_) + sch, "Schnurlänge")
        return T(f"Ein Päckchen ({a_} cm × {b_} cm × {h_} cm) wird kreuzweise einmal längs und einmal quer verschnürt; für die Schleife braucht man {sch} cm extra. Wie lang muss die Schnur sein?",
                 f"{2*(a_+h_)+2*(b_+h_)+sch} cm", [f"längs: 2·({a_} + {h_})", f"quer: 2·({b_} + {h_})", f"+ {sch} cm"])
    n_ = c.ri(3, 5)
    if c.has("gefärbt", "eine seite", "einer"):
        chk(sum(1 for i in range(n_) for j in range(n_) for k in range(n_) if [i in (0, n_ - 1), j in (0, n_ - 1), k in (0, n_ - 1)].count(True) == 1) == 6 * (n_ - 2) ** 2,
            "alle kleinen Würfel durchgezählt")
        return T(f"Ein großer Würfel aus {n_}·{n_}·{n_} kleinen Würfeln wird außen rot angemalt. Wie viele kleine Würfel haben genau eine rote Seite?", str(6 * (n_ - 2) ** 2),
                 [f"je Seitenfläche die inneren {(n_-2)**2}", f"6·{(n_-2)**2}"])
    a_, b_ = c.ri(2, 4), c.ri(2, 4)
    da = c.ri(2, 6)
    chk(2 * a_ * b_ - da + da == ev(f"{a_} · {b_} · 2"), "Würfel gezählt")
    return T(f"Ein Bauwerk aus Würfeln ist {a_} Würfel lang, {b_} breit und 2 hoch, aber in der oberen Schicht fehlen {da} Würfel. Wie viele Würfel sind verbaut, und wie viele fehlen zum vollständigen Quader?",
             f"{2*a_*b_-da}; fehlen {da}", [f"vollständig: {2*a_*b_}", f"minus {da}"])


@reg(("messen.volumen", "einheitswuerfel"), ("messen.volumen", "quader"))
def _(c):
    if c.z["etappe"] == "quader":
        V_ = c.ch((24, 36, 48, 60, 72))
        tr = [(a_, b_, V_ // (a_ * b_)) for a_ in range(1, 7) for b_ in range(a_, 7) if V_ % (a_ * b_) == 0 and V_ // (a_ * b_) >= b_][:3]
        chk(all(a_ * b_ * cc == V_ for a_, b_, cc in tr) and len(tr) == 3, "Volumen nachgerechnet")
        return T(f"Gib drei verschiedene Quader mit ganzzahligen Kantenlängen (in cm) an, die jeweils {V_} cm³ Volumen haben.", "; ".join(f"{a_}×{b_}×{cc}" for a_, b_, cc in tr),
                 ["V = a·b·c", "Zerlegungen von " + str(V_)])
    k = c.ch((4, 6, 8))
    chk(ev(f"{k} · {k} · {k}") == k ** 3, "nachgerechnet")
    return T(f"Ein Würfel mit {k} cm Kantenlänge wird mit Würfeln von 1 cm³ gefüllt. Wie viele passen hinein? Wie viele sind es, wenn er nur bis zur halben Höhe gefüllt wird?",
             f"{k**3}; {fz(F(k**3,2), dez=True)}", [f"{k}·{k}·{k}", "halbe Höhe: Hälfte"])


@reg(("geometrie.winkel", "kreuzung"), ("geometrie.winkel", "drehungen"), ("geometrie.winkel", "ergaenzen"))
def _(c):
    et = c.z["etappe"]; al = c.ri(25, 85)
    if et == "kreuzung":
        chk(al + (180 - al) + al + (180 - al) == 360, "Vollwinkel")
        return T(f"Zwei Geraden schneiden sich; einer der vier Winkel ist {al}° groß. Bestimme die anderen drei Winkel ohne Messen.", f"{180-al}°, {al}°, {180-al}°",
                 [f"Nebenwinkel: 180° − {al}°", "gegenüberliegende Winkel gleich groß"])
    if et == "ergaenzen":
        chk((al + 5) + (85 - al) + 90 == 180, "Winkelsumme im Dreieck")
        return T(f"Eine Leiter steht schräg an einer senkrechten Wand und bildet mit dem Boden einen Winkel von {al+5}°. Wie groß ist der Winkel zwischen Leiter und Wand? Ist die Leiter sicher, wenn der Bodenwinkel zwischen 65° und 75° liegen soll?",
                 f"{85-al}°; {'ja' if 65 <= al+5 <= 75 else 'nein'}", [f"Winkel zusammen 90°: 90° − {al+5}°", "mit dem sicheren Bereich vergleichen"])
    if c.has("weg", "skizze"):
        return T("Zeichne eine Wegskizze (1 cm ≙ 100 m): 300 m nach Osten, dann um 90° nach links drehen und 200 m gehen, dann um 45° nach rechts drehen und 100 m gehen.",
                 "Wegskizze", ["Strecken im Maßstab: 3 cm, 2 cm, 1 cm", "Drehwinkel mit Geodreieck"])
    return T("Welche der Figuren Quadrat, gleichseitiges Dreieck, Rechteck (kein Quadrat) sehen nach einer Drehung um 90° um ihren Mittelpunkt wieder gleich aus?", "nur das Quadrat",
             ["Quadrat: Drehsymmetrie 90°", "Dreieck: 120°", "Rechteck: 180°"])


@reg(("geometrie.ortslinien", "parallelen"), ("geometrie.ortslinien", "kreislinie"))
def _(c):
    d_ = c.ri(2, 5)
    if c.z["etappe"] == "kreislinie":
        return T(f"Zeichne einen Punkt M und mehrere Geraden, die alle den Abstand {d_} cm von M haben. Welche Figur entsteht, wenn man sehr viele solche Geraden zeichnet?", f"Kreis mit Radius {d_} cm",
                 ["jede Gerade berührt den Kreis um M", "Tangenten umhüllen den Kreis"])
    return T(f"Zeichne eine Gerade g durch A(1|1) und B(9|3). Zeichne die beiden Parallelen zu g im Abstand {d_} cm.", f"zwei Parallelen, je {d_} cm entfernt",
             [f"Geodreieck: Senkrechte, {d_} cm abtragen", "Parallele durch den Punkt, auf beiden Seiten"])


@reg(("L", "Schrägbild eines Quaders zeichnen (Kl. 5)"))
def _(c):
    a_, b_, h_ = c.ri(3, 6), c.ri(2, 4), c.ri(2, 4)
    chk(F(b_, 2) * 2 == b_, "Verkürzung")
    return T(f"Zeichne ein Schrägbild eines Quaders mit {a_} cm Länge, {b_} cm Tiefe und {h_} cm Höhe (Tiefe unter 45° und halb so lang). Beschrifte die Ecken mit A bis H.",
             f"Tiefenkanten {fd(F(b_,2))} cm lang", ["Vorderfläche in wahrer Größe", f"nach hinten unter 45° mit {fd(F(b_,2))} cm", "verdeckte Kanten gestrichelt"])


@reg(("L", "Kreissektor mit vorgegebenem Mittelpunktswinkel zeichnen"))
def _(c):
    r_, w = c.ri(2, 5), c.ch((45, 60, 90, 120, 135))
    chk(F(w, 360) * 360 == w, "Anteil")
    return T(f"Zeichne einen Kreis mit r = {r_} cm und darin einen Kreisausschnitt mit Mittelpunktswinkel {w}°. Welcher Teil des Kreises ist das?", fz(F(w, 360)),
             ["zwei Radien mit Winkel " + str(w) + "°", f"{w}/360 = {fz(F(w,360))}"])


@reg(("L", "Ansichten von Körpern (in der App erst Kl. 8)"))
def _(c):
    h = [c.ri(1, 3) for _ in range(3)]
    return T(f"Drei Würfeltürme stehen nebeneinander in einer Reihe: {h[0]}, {h[1]} und {h[2]} Würfel hoch. Zeichne die Ansicht von vorne und von oben.",
             "vorne: Säulen der Höhen " + ", ".join(map(str, h)) + "; oben: 3 Quadrate in einer Reihe", ["von vorne: Höhen sichtbar", "von oben: nur die Grundfläche"])
