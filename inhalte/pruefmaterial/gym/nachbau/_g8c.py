# Generatoren Zahlen, Brüche, Prozent, Daten, Stochastik, Größen (Kl. 8 und Grundwissen; teils auch Kl. 5)
from _kern import *
from itertools import product, permutations, combinations


# ============================================================ Stochastik
@reg(("stochastik.grundbegriffe", "laplace"))
def _(c):
    v = c.ri(0, 2)
    if c.has("würfel", "pasch", "augensumme") or v == 0:
        z = c.ri(4, 10)
        g = sum(1 for a_, b_ in product(range(1, 7), repeat=2) if a_ + b_ == z)
        return T(f"Zwei faire Würfel werden geworfen. Berechne die Wahrscheinlichkeit, dass die Augensumme {z} beträgt.", fz(F(g, 36)),
                 ["36 gleich wahrscheinliche Ergebnisse (Paare)", f"günstig: {g} Paare", f"P = {g}/36 = {fz(F(g,36))}"])
    if v == 1:
        r_, b_, g_ = c.ri(2, 8), c.ri(2, 8), c.ri(1, 6)
        ges = r_ + b_ + g_
        return T(f"In einer Urne liegen {r_} rote, {b_} blaue und {g_} grüne Kugeln. Eine Kugel wird zufällig gezogen. Berechne P(„nicht blau“).", fz(F(r_ + g_, ges)),
                 [f"{ges} Kugeln", f"nicht blau: {r_+g_}", f"P = {fz(F(r_+g_, ges))}"])
    sek = c.ri(6, 12); rot = c.ri(1, sek - 2)
    return T(f"Ein Glücksrad hat {sek} gleich große Felder, davon {rot} rot. Mit welcher Wahrscheinlichkeit bleibt es auf Rot stehen? Begründe, warum es ein Laplace-Experiment ist.",
             fz(F(rot, sek)), ["gleich große Felder → gleich wahrscheinlich", f"P = {rot}/{sek} = {fz(F(rot,sek))}"])


@reg(("stochastik.grundbegriffe", "laplace_pruefen"))
def _(c):
    return T("Ein Würfel wird zweimal geworfen und die Augensumme notiert. Begründe, warum das Notieren der Augensumme (2 bis 12) kein Laplace-Experiment ist.",
             "Augensummen nicht gleich wahrscheinlich", ["Summe 2 nur bei (1|1): 1/36", "Summe 7 bei 6 Paaren: 6/36", "Ergebnisse unterschiedlich wahrscheinlich"])


@reg(("stochastik.grundbegriffe", "begriffe"))
def _(c):
    nmax = c.ch((20, 30, 40, 50))
    t_ = c.ch((3, 4, 6))
    A = {n for n in range(1, nmax + 1) if n % t_ == 0}
    k = c.ch([z for z in range(10) if any(n % 10 == z for n in A)])
    B = {n for n in range(1, nmax + 1) if n % 10 in (k, )}
    S = sorted(A & B)
    chk(S, "Schnitt nicht leer")
    if c.has("vereinigung", "schraffier"):
        return T(f"Aus Karten mit den Zahlen 1 bis {nmax} wird eine gezogen. A: „durch {t_} teilbar“, B: „Endziffer {k}“. Gib A ∪ B an und wie viele Ergebnisse es enthält.",
                 f"{len(A|B)} Ergebnisse: {{{'; '.join(map(str, sorted(A|B)))}}}", ["alle Zahlen, die mindestens eine Bedingung erfüllen", "Doppelte nur einmal"])
    if c.has("rechnung", "beschreib"):
        w = c.ri(4, 8)
        return T(f"Ein Glücksrad mit {w} gleich großen Feldern (1 bis {w}) wird zweimal gedreht. Zu welchem Ereignis passt die Rechnung 1 − ({w-1}/{w})²? Beschreibe es in Worten.",
                 f"„mindestens einmal die {w}“ (o. Ä.)", [f"({w-1}/{w})²: zweimal nicht die {w}", "1 minus Gegenereignis"])
    return T(f"Aus Karten mit den Zahlen 1 bis {nmax} wird eine gezogen. A: „Zahl ist durch {t_} teilbar“, B: „Endziffer {k}“. Gib A ∩ B an und beschreibe das Gegenereignis von B in Worten.",
             f"A ∩ B = {{{'; '.join(map(str, S))}}}; B̄: „Endziffer ist nicht {k}“", ["Schnitt: beide Bedingungen", "Gegenereignis: alle übrigen Ergebnisse"])


@reg(("stochastik.grundbegriffe", "gegenereignis"))
def _(c):
    p = F(c.ri(1, 4), c.ch((5, 6, 8, 10)))
    if c.niv == "III":
        q = 1 - p
        chk(1 - q * q == 2 * p - p * p, "Gegenereignis")
        return T(f"Ein Glücksrad zeigt mit der Wahrscheinlichkeit {fz(p)} „Gewinn“. Es wird zweimal gedreht. Berechne die Wahrscheinlichkeit für mindestens einen Gewinn über das Gegenereignis.",
                 fz(1 - q * q), [f"Gegenereignis: zweimal kein Gewinn, ({fz(q)})² = {fz(q*q)}", f"1 − {fz(q*q)} = {fz(1-q*q)}"])
    return T(f"Die Wahrscheinlichkeit, dass ein zufällig gewählter Schüler mit dem Rad kommt, beträgt {fz(p)}. Wie groß ist die Wahrscheinlichkeit, dass er nicht mit dem Rad kommt?",
             fz(1 - p), [f"P(Ā) = 1 − P(A) = {fz(1-p)}"])


@reg(("L", "Vierfeldertafel ergänzen"))
def _(c):
    a_, b_, c_, d_ = (c.ri(5, 40) for _ in range(4))
    return T(f"Ergänze die Vierfeldertafel (Brille ja/nein, Mädchen/Jungen): Mädchen mit Brille {a_}, Mädchen gesamt {a_+b_}, Jungen mit Brille {c_}, alle zusammen {a_+b_+c_+d_}.",
             f"Mädchen ohne {b_}; Jungen ohne {d_}; Jungen gesamt {c_+d_}; mit Brille {a_+c_}; ohne {b_+d_}", ["Zeilen- und Spaltensummen nutzen"])


@reg(("stochastik.kombinatorik", "zaehlprinzip"), ("stochastik.kombinatorik", "reihenfolgen"), ("stochastik.kombinatorik", "systematisch"),
     ("stochastik.kombinatorik", "bedingungen"), ("stochastik.kombinatorik", "grenzen"))
def _(c):
    et = c.z["etappe"]
    if et == "grenzen":
        t_ = c.ri(5, 12)
        return T(f"Bei einem Turnier spielt jede von {t_} Mannschaften genau einmal gegen jede andere. Wie viele Spiele gibt es?", str(t_ * (t_ - 1) // 2),
                 [f"jede spielt {t_-1}-mal", f"{t_}·{t_-1} zählt jedes Spiel doppelt", f"{t_*(t_-1)//2}"])
    if et == "reihenfolgen":
        k = c.ri(3, 4)
        return T(f"Auf wie viele Arten können sich {k} Kinder nebeneinander für ein Foto aufstellen? Schreibe die Rechnung auf.", str(math.factorial(k)),
                 [" · ".join(str(i) for i in range(k, 0, -1)), str(math.factorial(k))])
    if et == "systematisch":
        mz = sorted(c.r.sample([1, 2, 5, 10, 20], 3))
        summen = sorted({a_ + b_ for a_, b_ in combinations(mz, 2)} | set(mz))
        return T(f"In einer Tüte sind drei Münzen zu {', '.join(f'{m} ct' for m in mz)}. Man darf eine oder zwei Münzen ziehen. Welche Beträge sind möglich? Liste systematisch auf.",
                 ", ".join(f"{s} ct" for s in summen), ["eine Münze: drei Beträge", "zwei Münzen: drei Paare", "Liste ohne Doppelte"])
    if et == "bedingungen":
        zif = c.r.sample(range(1, 10), 4)
        ger = [z for z in zif if z % 2 == 0]
        anz = sum(1 for p in permutations(zif, 3) if p[2] % 2 == 0)
        chk(anz == len(ger) * 3 * 2, "Zählprinzip")
        if c.k5 and not ger:
            zif[0] = 2; ger = [2]; anz = 6
        return T(f"Aus den Ziffernkarten {', '.join(map(str, zif))} werden dreistellige Zahlen ohne Wiederholung gelegt. Wie viele davon sind gerade?", str(anz),
                 [f"Einerstelle gerade: {len(ger)} Möglichkeiten", "dann 3 und 2 für die anderen Stellen", f"{len(ger)}·3·2 = {anz}"])
    a_, b_, cc = c.ri(2, 5), c.ri(2, 4), c.ri(2, 5)
    if c.niv == "III" and not c.k5:
        return T("Wie viele dreistellige Zahlen kann man mit einem Würfel durch dreimaliges Werfen bilden, bei denen mindestens zwei Ziffern gleich sind?", "96",
                 ["alle: 6³ = 216", "alle verschieden: 6·5·4 = 120", "216 − 120 = 96"])
    if c.niv == "III":
        ges = a_ * b_ * cc
        return T(f"Ein Restaurant bietet {ges} verschiedene Menüs aus Vorspeise, Hauptgericht und Nachtisch an. Es gibt {a_} Vorspeisen und {cc} Nachtische. Wie viele Hauptgerichte gibt es?",
                 str(b_), [f"{a_}·x·{cc} = {ges}", f"x = {b_}"])
    return T(f"Zu einem Outfit gehören ein T-Shirt ({a_} Stück), eine Hose ({b_}) und Schuhe ({cc} Paar). Wie viele verschiedene Kombinationen gibt es?", str(a_ * b_ * cc),
             [f"Zählprinzip: {a_}·{b_}·{cc} = {a_*b_*cc}"])


@reg(("L", "Auswahl ohne Reihenfolge (Kombinationen)"))
def _(c):
    n_, k = c.ri(6, 9), 3
    erg = math.comb(n_, k)
    chk(erg == n_ * (n_ - 1) * (n_ - 2) // 6, "Formel")
    return T(f"Aus {n_} Schülern werden 3 für den Aufbaudienst ausgewählt. Wie viele verschiedene Gruppen sind möglich?", str(erg),
             [f"mit Reihenfolge {n_}·{n_-1}·{n_-2} = {n_*(n_-1)*(n_-2)}", "jede Gruppe wird 3·2·1 = 6-mal gezählt", f"{erg}"])


@reg(("X", "mehrstufige Zufallsexperimente (Pfadregel, Kl. 9/10)"))
def _(c):
    p = F(c.ri(1, 4), c.ch((5, 10)))
    return T(f"Ein Glücksrad zeigt Rot mit der Wahrscheinlichkeit {fz(p)}. Es wird dreimal gedreht. Berechne mit einem Baumdiagramm P(„dreimal Rot“) und P(„genau einmal Rot“).",
             f"{fz(p**3)}; {fz(3*p*(1-p)**2)}", [f"Pfadregel: ({fz(p)})³", f"genau einmal: 3 Pfade je {fz(p*(1-p)**2)}"])


@reg(("X", "Ziehen mit/ohne Zurücklegen (Kl. 9/10)"))
def _(c):
    r_, b_ = c.ri(2, 5), c.ri(2, 5)
    return T(f"In einer Schachtel liegen {r_} rote und {b_} blaue Stifte; zwei werden nacheinander gezogen. Entscheide und begründe, ob das „mit“ oder „ohne Zurücklegen“ ist, und berechne P(zwei rote).",
             f"ohne Zurücklegen; {fz(F(r_*(r_-1), (r_+b_)*(r_+b_-1)))}", ["gezogener Stift fehlt beim zweiten Zug", f"{r_}/{r_+b_} · {r_-1}/{r_+b_-1}"])


# ============================================================ Größen
@reg(("groessen.einheiten", "massstab"))
def _(c):
    m = c.ch((1000, 2000, 5000, 10000, 25000, 50000, 100000))
    cm = c.ri(2, 15)
    real = cm * m
    if c.has("karte", "kartenlänge", "plan") and c.has("real", "in kartenlänge"):
        km = c.ri(2, 9)
        lg = F(km * 100000, m)
        return T(f"Zwei Orte sind in Wirklichkeit {km} km voneinander entfernt. Wie lang ist die Strecke auf einer Karte im Maßstab 1 : {fz(m)}?", f"{fz(lg, dez=True)} cm",
                 [f"{km} km = {km*100000} cm", f": {fz(m)}"])
    if c.niv == "III" and not c.k5:
        A_ = c.ri(2, 9) * 10000
        s_ = (A_ ** 0.5)
        return T(f"Auf einer Karte im Maßstab 1 : {fz(m)} soll ein quadratisches Grundstück mit {fz(A_)} m² eingezeichnet werden. Wie lang ist eine Seite auf der Karte (Näherung)?",
                 f"≈ {gerundet(F(round(s_*100/m*100),100),2)} cm", [f"Seite ≈ {gerundet(F(round(s_*10),10),1)} m", "in cm umrechnen und durch den Maßstab teilen"])
    if c.has("wählen", "passend"):
        return T(f"Ein Zimmer ist {c.ri(3,6)} m lang. Es soll auf ein DIN-A4-Blatt (ca. 28 cm) gezeichnet werden. Welcher Maßstab passt: 1 : 10, 1 : 50 oder 1 : 1000? Begründe.", "1 : 50",
                 ["1 : 10 → zu groß (über 30 cm)", "1 : 50 → etwa 6–12 cm", "1 : 1000 → wenige mm"])
    return T(f"Auf einer Karte im Maßstab 1 : {fz(m)} ist ein Weg {cm} cm lang. Wie lang ist er in Wirklichkeit? Gib das Ergebnis in einer sinnvollen Einheit an.",
             f"{fd(F(real,100))} m" if real < 100000 else f"{fd(F(real,100000))} km", [f"{cm}·{fz(m)} = {fz(real)} cm", "umrechnen"])


@reg(("groessen.einheiten", "schaetzen"))
def _(c):
    obj = c.ch([("einen Stapel von 1000 Blatt Papier (0,1 mm je Blatt)", F(1, 10), 1000, "mm", "10 cm"),
                ("eine Reihe aus 1 Million Ein-Cent-Münzen (Durchmesser 1,6 cm) nebeneinander", F(16, 10), 1000000, "cm", "16 km"),
                ("einen Turm aus 500 Schulbüchern (je 2 cm dick)", F(2), 500, "cm", "10 m")])
    if c.k5 and c.has("bild", "höhe", "vergleich"):
        h_ = c.ri(3, 6)
        return T(f"Auf einem Foto steht ein Mann (ca. 1,80 m) vor einem Haus; das Haus ist etwa {h_}-mal so hoch wie der Mann. Schätze die Höhe des Hauses.", f"etwa {fd(F(18*h_,10))} m",
                 ["Vergleichsgröße 1,80 m", f"× {h_}"])
    return T(f"Schätze die Länge bzw. Höhe von {obj[0]}. Schreibe deinen Rechenweg auf.", obj[4], [f"{fz(obj[2])} · {fd(obj[1])} {obj[3]}", f"in passende Einheit: {obj[4]}"])


@reg(("groessen.einheiten", "masse"), ("groessen.einheiten", "laenge"), ("groessen.einheiten", "zeit"), ("groessen.einheiten", "rechnen"),
     ("groessen.einheiten", "kommaschreibweise"), ("groessen.einheiten", "verstehen"))
def _(c):
    et = c.z["etappe"]
    if et == "masse":
        t_ = c.ri(2, 9); kg = c.ri(50, 950)
        if c.k5 and c.has("ordnen"):
            w = [(f"{t_*1000+kg} kg", t_ * 1000 + kg), (f"{t_} t", t_ * 1000), (f"{kg*1000} g", kg), (f"{fd(F(t_*1000+kg+100,1000))} t", t_ * 1000 + kg + 100)]
            c.r.shuffle(w)
            return T("Ordne der Größe nach (kleinste zuerst): " + "; ".join(s for s, _ in w), " < ".join(s for s, _ in sorted(w, key=lambda t: t[1])),
                     ["alles in kg umrechnen", "vergleichen"])
        return T(f"Ein Lkw wiegt leer {t_} t und beladen {fd(F(t_*1000+kg,1000))} t. Wie viel Kilogramm wiegt die Ladung?", f"{kg} kg",
                 [f"{fd(F(t_*1000+kg,1000))} t = {t_*1000+kg} kg", f"− {t_*1000} kg"])
    if et == "laenge":
        if c.has("fehler"):
            w = c.ri(2, 9)
            return T(f"Ben rechnet: {w} m = {w*10} cm. Beschreibe den Fehler und gib das richtige Ergebnis an.", f"{w*100} cm", ["1 m = 100 cm, nicht 10"])
        u = [(c.ri(2, 9), "km", "m", 1000), (c.ri(12, 90), "dm", "cm", 10), (c.ri(2, 30), "m", "mm", 1000), (c.ri(300, 900), "cm", "m", F(1, 100))]
        return T("Rechne um: " + "; ".join(f"{v} {e1} = ___ {e2}" for v, e1, e2, _ in u), "; ".join(f"{fd(v*f)} {e2}" for v, e1, e2, f in u), ["Umrechnungszahlen 10, 100, 1000"])
    if et == "zeit":
        h_, m_ = c.ri(1, 4), c.ri(5, 55)
        if c.k5 and c.has("spanne", "ankunft", "dauer", "abfahrt"):
            s1, d1 = c.ri(7, 16), c.ri(35, 170)
            an = s1 * 60 + c.ri(0, 59)
            ende = an + d1
            return T(f"Ein Zug fährt um {an//60}:{an%60:02d} Uhr ab und ist {d1} min unterwegs. Wann kommt er an?", f"{ende//60}:{ende%60:02d} Uhr",
                     [f"{d1} min = {d1//60} h {d1%60} min", "zur Abfahrtszeit addieren"])
        return T(f"Rechne in Minuten um: {h_} h {m_} min; {fd(F(c.ri(1,7)*2+1,4))} h.", f"{h_*60+m_} min; …", [f"{h_}·60 + {m_}", "Viertelstunde = 15 min"])
    if et == "kommaschreibweise":
        m_, cm = c.ri(1, 9), c.ri(1, 99)
        return T(f"Schreibe mit Komma in Metern: {m_} m {cm} cm; {c.ri(2,9)} dm {c.ri(1,9)} cm.", f"{fd(F(m_*100+cm,100))} m; …", ["1 cm = 0,01 m", "1 dm = 0,1 m"])
    if et == "verstehen":
        return T("Welche Angaben sind unrealistisch? Ein Schulbus ist 12 m lang; eine Katze wiegt 40 kg; ein Glas fasst 0,2 l; ein Schüler läuft 100 m in 3 s.",
                 "Katze 40 kg; 100 m in 3 s", ["Katze etwa 4 kg", "100 m dauern etwa 13–20 s"])
    if c.k5 and c.has("rückgeld", "geld", "euro", "cent"):
        p1, p2 = c.ri(120, 890), c.ri(120, 890); bz = 20 if p1 + p2 < 2000 else 50
        rg = bz * 100 - p1 - p2
        return T(f"Ida kauft ein Heft für {fd(F(p1,100))} € und einen Stift für {fd(F(p2,100))} €. Sie zahlt mit einem {bz}-€-Schein. Wie viel Rückgeld bekommt sie?",
                 f"{fd(F(rg,100))} €", [f"zusammen {fd(F(p1+p2,100))} €", f"{bz} € − {fd(F(p1+p2,100))} €"])
    s_ = c.ri(50, 100)
    t_ = c.ri(8, 16)
    return T(f"Ein Läufer schafft {s_*2} m in {t_*2} Sekunden. Rechne seine mittlere Geschwindigkeit in m/s und in km/h um.", f"{fd(F(s_,t_)) if endlich(F(s_,t_)) else gerundet(F(s_,t_),1)} m/s ≈ {gerundet(F(s_*36,t_*10),1)} km/h",
             [f"{s_*2} : {t_*2}", "× 3,6 für km/h"])


@reg(("groessen.proportional", "dreisatz"), ("groessen.proportional", "sach"), ("groessen.proportional", "einheit"))
def _(c):
    n1, n2 = c.ri(2, 6), c.ri(7, 15)
    p1 = c.ri(2, 9) * n1
    p2 = F(p1, n1) * n2
    if c.z["etappe"] == "einheit":
        a1, a2 = c.ri(2, 6), c.ri(7, 12)
        q1, q2 = c.ri(3, 9) * a1, c.ri(3, 9) * a2
        besser = "erste" if F(q1, a1) < F(q2, a2) else "zweite"
        return T(f"Angebot 1: {a1} Hefte für {fd(F(q1,10))} €. Angebot 2: {a2} Hefte für {fd(F(q2,10))} €. Welches Angebot ist günstiger?", f"das {besser}",
                 [f"Preis je Heft: {fd(F(q1,10*a1))} € bzw. {fd(F(q2,10*a2))} €" if endlich(F(q1, 10 * a1)) and endlich(F(q2, 10 * a2)) else "Preis je Heft vergleichen", "kleinerer Stückpreis"])
    if c.z["etappe"] == "sach":
        v_ = c.ri(4, 12) * 10; s_ = c.ri(30, 240)
        t_ = F(s_ * 60, v_)
        return T(f"Ein Bus fährt im Mittel {v_} km/h. Wie lange braucht er für {s_} km? Gib das Ergebnis in Stunden und Minuten an.",
                 f"{int(t_)//60} h {int(t_)%60} min" if t_.denominator == 1 else f"≈ {gerundet(t_,0)} min", [f"{s_} : {v_} h", "× 60 für Minuten"])
    ktx = c.ch((("Pfannkuchen", "g Mehl", "g"), ("Gläser Limonade", "ml Sirup", "ml"), ("Meter Zaun", "Latten", ""), ("Brötchen", "g Teig", "g")))
    return T(f"Für {n1} {ktx[0]} braucht man {p1} {ktx[1]}. Wie viel braucht man für {n2} {ktx[0]}?", f"{fd(p2)} {ktx[1]}",
             [f"für 1: {fd(F(p1,n1))}", f"für {n2}: {fd(p2)}"])


# ============================================================ Brüche, Dezimal, Prozent
@reg(("bruch.rechnen", "gemischt"), ("bruch.rechnen", "brueche_plus_minus"), ("bruch.rechnen", "dezimal_mal"), ("bruch.rechnen", "potenzen"),
     ("bruch.rechnen", "brueche_mal"), ("bruch.rechnen", "dezimal_plus_minus"))
def _(c):
    et = c.z["etappe"]
    a_ = F(c.ri(1, 7), c.ch((2, 3, 4, 5, 6, 8))); b_ = F(c.ri(1, 7), c.ch((2, 3, 4, 6, 9)))
    if et == "brueche_plus_minus":
        if c.has("mittel"):
            m = (a_ + b_) / 2
            return T(f"Berechne die Zahl genau in der Mitte zwischen {fz(a_)} und {fz(b_)}.", fz(m), ["Summe halbieren", f"({fz(a_)} + {fz(b_)}) : 2 = {fz(m)}"])
        if a_ < b_:
            a_, b_ = b_, a_
        return T(f"Berechne und kürze: {fz(a_)} − {fz(b_)}", fz(a_ - b_), [f"Hauptnenner {kgv(a_.denominator, b_.denominator)}", f"= {fz(a_-b_)}"])
    if et == "brueche_mal":
        k = c.ri(2, 9)
        return T(f"Berechne: {fz(a_)} · {k}", fz(a_ * k), [f"Zähler mal {k}", f"= {fz(a_*k)}"])
    if et == "dezimal_plus_minus":
        d1, d2 = F(c.ri(11, 99), 10), F(c.ri(101, 999), 100)
        return T(f"Berechne: {fd(d1)} + {fd(d2)} − {fd(F(1,2))}", fd(d1 + d2 - F(1, 2)), ["Komma unter Komma", f"= {fd(d1+d2-F(1,2))}"])
    if et == "dezimal_mal":
        p_, q_ = c.ri(12, 99), c.ri(12, 99)
        return T(f"Es gilt {p_} · {q_} = {p_*q_}. Berechne ohne Nebenrechnung {fd(F(p_,10))} · {fd(F(q_,100))} und {fd(F(p_*q_,1000))} : {fd(F(q_,10))}.",
                 f"{fd(F(p_*q_,1000))}; {fd(F(p_,100))}", ["Kommastellen zählen: 1 + 2 = 3", f"{fd(F(p_*q_,1000))} : {fd(F(q_,10))} = {fd(F(p_,100))}"])
    if et == "potenzen":
        b0 = c.nz(-5, 5); e0 = c.ch((2, 3))
        w = F(-1, 2) ** 3 if c.niv != "I" else None
        if c.has(" n ", "mit n") or c.niv == "III":
            return T("Berechne (−½)ⁿ für n = 1, 2, 3, 4 und beschreibe, wie die Werte auf der Zahlengeraden liegen.", "−1/2; 1/4; −1/8; 1/16",
                     ["Vorzeichen wechselt", "Betrag halbiert sich", "springen abwechselnd um 0 und nähern sich 0"])
        return T(f"Berechne: −{abs(b0)}{hoch(e0)} + ({b0}){hoch(e0)}", fz(-abs(b0) ** e0 + b0 ** e0), [f"−{abs(b0)}{hoch(e0)} = {-abs(b0)**e0}", f"({b0}){hoch(e0)} = {b0**e0}"])
    d_ = F(c.ri(1, 9), 10)
    w = a_ * c.ri(2, 6) - d_
    t = f"{fz(a_)} · {kl(c.ri(2,6))}"
    k = c.ri(2, 6)
    w = a_ * k - d_
    return T(f"Berechne: {fz(a_)} · {k} − {fd(d_)}  (Ergebnis als Bruch)", fz(w), [f"{fz(a_)}·{k} = {fz(a_*k)}", f"{fd(d_)} = {fz(d_)}", f"= {fz(w)}"])


@reg(("bruch.rechnen", "sach"))
def _(c):
    g_ = c.ri(4, 12) * 12
    a_ = F(c.ri(1, 3), 4); b_ = F(c.ri(1, 2), 3)
    if c.niv == "III":
        rest = g_ * (1 - a_) * (1 - b_)
        return T(f"Jana verschenkt {fz(a_)} ihrer Sticker, dann {fz(b_)} des Rests. Danach hat sie noch {fz(rest)}. Wie viele hatte sie zu Beginn?", str(g_),
                 [f"Rest = x·{fz(1-a_)}·{fz(1-b_)}", f"x = {fz(rest)} : {fz((1-a_)*(1-b_))} = {g_}"])
    return T(f"In einer Schule mit {g_} Schülern fährt {fz(a_)} mit dem Bus, davon wiederum {fz(b_)} mehr als 10 km. Wie viele sind das?", fz(g_ * a_ * b_),
             [f"{fz(a_)} von {fz(b_)} = {fz(a_*b_)}", f"{fz(a_*b_)}·{g_}"])


@reg(("bruch.brueche", "anteil_bestimmen"), ("bruch.brueche", "ganzes_bestimmen"), ("bruch.brueche", "kuerzen"), ("bruch.brueche", "zahlbereiche"),
     ("bruch.brueche", "bruchteil_von"), ("bruch.brueche", "verstehen"))
def _(c):
    et = c.z["etappe"]
    z_, n_ = c.ri(1, 7), c.ch((4, 6, 8, 10, 12))
    if z_ >= n_:
        z_ = n_ - 1
    if et == "kuerzen":
        k = c.ri(2, 9)
        return T(f"Kürze vollständig: {z_*k}/{n_*k}", fz(F(z_, n_)), [f"ggT = {ggt(z_*k, n_*k)}", fz(F(z_, n_))])
    if et == "ganzes_bestimmen":
        k = c.ri(3, 12)
        return T(f"{fz(F(z_,n_))} aller Teilnehmer, das sind {z_*k}, kamen mit dem Rad. Wie viele Teilnehmer gab es insgesamt?", str(n_ * k),
                 [f"1/{n_} entspricht {k}", f"Ganzes: {n_}·{k} = {n_*k}"])
    if et == "zahlbereiche":
        return T("Stimmt die Aussage „Das Quadrat einer negativen Zahl ist immer kleiner als die Zahl selbst“? Begründe.", "falsch",
                 ["Quadrat einer negativen Zahl ist positiv", "also größer als die Zahl"])
    if et == "bruchteil_von":
        g_ = n_ * c.ri(2, 9)
        return T(f"Von {g_} Kindern einer Klassenstufe spielen {fz(F(z_,n_))} ein Instrument. Wie viele Kinder sind das?", str(g_ * z_ // n_),
                 [f"1/{n_} von {g_} = {g_//n_}", f"·{z_}"])
    if et == "verstehen":
        return T("Ein Kreis wird in vier ungleich große Stücke geteilt; eines wird gefärbt. Ein Kind sagt: „Das ist ein Viertel.“ Begründe, warum das nicht stimmt.",
                 "Teile müssen gleich groß sein", ["Bruch 1/4: Ganzes in 4 gleich große Teile"])
    if c.k5:
        return T(f"Ein Rechteck ist in {n_} gleich große Kästchen geteilt; {z_} davon sind gefärbt. Welcher Bruchteil ist gefärbt? Kürze, falls möglich.", fz(F(z_, n_)),
                 [f"{z_}/{n_}", f"gekürzt {fz(F(z_,n_))}"])
    a1, a2 = c.ri(2, 9), c.ri(2, 9)
    g1, g2 = a1 + c.ri(5, 15), a2 + c.ri(5, 15)
    mehr = "Gruppe 1" if F(a1, g1) > F(a2, g2) else "Gruppe 2"
    return T(f"In Gruppe 1 sind {a1} von {g1} Kindern Linkshänder, in Gruppe 2 {a2} von {g2}. In welcher Gruppe ist der Anteil größer?", mehr,
             [f"{fz(F(a1,g1))} ≈ {gerundet(F(a1*100,g1),0)} %", f"{fz(F(a2,g2))} ≈ {gerundet(F(a2*100,g2),0)} %"])


@reg(("bruch.dezimal", "merkwerte"), ("bruch.dezimal", "verstehen"), ("bruch.dezimal", "vergleichen_ordnen"))
def _(c):
    et = c.z["etappe"]
    if et == "merkwerte":
        w = c.r.sample([F(1, 2), F(1, 4), F(3, 4), F(1, 5), F(1, 8), F(3, 10), F(2, 5)], 4)
        return T("Ordne zu, was gleich ist: " + ", ".join(fz(v) for v in w) + " | " + ", ".join(f"{fd(v*100)} %" for v in c.r.sample(w, 4)) + " | " +
                 ", ".join(fd(v) for v in c.r.sample(w, 4)), "; ".join(f"{fz(v)} = {fd(v)} = {fd(v*100)} %" for v in w), ["Bruch in Dezimalzahl umwandeln"])
    if et == "verstehen":
        return T("Stimmt: „Jeder Bruch lässt sich als abbrechende Dezimalzahl schreiben“? Begründe mit einem Gegenbeispiel.", "falsch, z. B. 1/3 = 0,333…",
                 ["Nenner mit Primfaktor 3 (oder 7, …) → periodisch"])
    w = set()
    while len(w) < 4:
        dn = c.ch((2, 4, 5, 10)); w.add(F(c.nz(-2 * dn + 1, 2 * dn - 1), dn))
    w = sorted(w)
    return T("Trage auf einer Zahlengeraden von −2 bis 2 ein und ordne: " + "; ".join(fd(v) if endlich(v) else fz(v) for v in c.r.sample(w, len(w))), " < ".join(fd(v) for v in w),
             ["in Dezimalzahlen umwandeln", "der Größe nach ordnen"])


@reg(("bruch.prozent", "prozentsatz"), ("bruch.prozent", "grundwert"), ("bruch.prozent", "prozentwert"), ("bruch.prozent", "verstehen"))
def _(c):
    et = c.z["etappe"]
    G = c.ri(2, 20) * 20; ps = c.ch((5, 10, 15, 20, 25, 30, 40, 60, 75))
    W = F(G * ps, 100)
    if et == "grundwert":
        return T(f"{ps} % der Plätze in einem Bus sind besetzt, das sind {fz(W)} Plätze. Wie viele Plätze hat der Bus?", str(G), [f"{ps} % ≙ {fz(W)}", f"100 % ≙ {fz(W)}·100/{ps} = {G}"])
    if et == "prozentwert":
        p2 = c.ch((10, 20, 50))
        return T(f"{ps} % der Schüler einer Schule ({G} Schüler) fahren Rad, davon tragen {p2} % einen Helm. Wie viele Schüler tragen einen Helm? Wie viel Prozent aller Schüler sind das?",
                 f"{fz(W*p2/100)}; {fd(F(ps*p2,100))} %", [f"{fz(W)} Radfahrer", f"{p2} % davon: {fz(W*p2/100)}", f"{ps} % von {p2} % = {fd(F(ps*p2,100))} %"])
    if et == "verstehen":
        return T("Klasse A: 30 % der 20 Schüler haben ein Haustier. Klasse B: 25 % der 32 Schüler. In welcher Klasse haben mehr Schüler ein Haustier? Was zeigt das?",
                 "B (8 > 6)", ["A: 6, B: 8", "höherer Prozentsatz bedeutet nicht mehr Personen, wenn der Grundwert verschieden ist"])
    return T(f"Von {G} befragten Jugendlichen nutzen {fz(W)} täglich ein Tablet. Wie viel Prozent sind das?", f"{ps} %", [f"{fz(W)}/{G} = {fd(F(ps,100))}", f"= {ps} %"])


@reg(("bruch.prozent_grundwert", "prozentsatz"), ("bruch.prozent_grundwert", "zurueck"), ("bruch.prozent_grundwert", "mehrfach"),
     ("bruch.prozent_grundwert", "vermindert"), ("bruch.prozent_grundwert", "argumente"))
def _(c):
    et = c.z["etappe"]
    ps = c.ch((10, 15, 20, 25, 30, 40)); G = c.ri(4, 30) * 20
    if et == "zurueck":
        neu = G * (100 - ps) // 100
        chk(neu * 100 == G * (100 - ps), "glatt")
        return T(f"Ein Fahrrad kostet nach einer Preissenkung um {ps} % noch {neu} €. Wie viel kostete es vorher?", f"{G} €",
                 [f"{neu} € ≙ {100-ps} %", f"100 % ≙ {neu}·100/{100-ps} = {G} €"])
    if et == "mehrfach":
        p1, p2 = c.ch((10, 20, 25)), c.ch((10, 20))
        fak = F(100 + p1, 100) * F(100 - p2, 100)
        return T(f"Ein Preis steigt zuerst um {p1} % und sinkt dann um {p2} %. Um wie viel Prozent hat er sich insgesamt verändert?",
                 f"{'+' if fak>1 else MINUS}{fd(abs(fak-1)*100)} %", [f"Faktor {fd(F(100+p1,100))}·{fd(F(100-p2,100))} = {fd(fak)}", "mit 1 vergleichen"])
    if et == "vermindert":
        z_ = c.ri(2, 9) * 10 ** c.ri(6, 8)
        return T(f"Ein Filter entfernt 99 % von {fz(z_)} Schmutzteilchen. Wie viele bleiben übrig?", fz(z_ // 100), ["1 % bleibt", f"{fz(z_)} : 100"])
    if et == "argumente":
        return T(f"Ein Preis P wird um {ps} % erhöht. Welche Terme geben den neuen Preis an? (A) P + {ps}  (B) P·{fd(F(100+ps,100))}  (C) P + {fd(F(ps,100))}·P  (D) P·{fd(F(ps,100))}",
                 "B und C", [f"Erhöhung um {ps} % → Faktor {fd(F(100+ps,100))}", "C ist ausgeklammert dasselbe"])
    a1 = G; a2 = G * (100 + ps) // 100
    if (G * (100 + ps)) % 100:
        a2 = G + G * ps // 100
    p = F(a2 - a1, a1) * 100
    return T(f"Die Zahl der Vereinsmitglieder stieg von {a1} auf {a2}. Um wie viel Prozent ist sie gestiegen?", f"{fd(p) if endlich(p) else gerundet(p,1)} %",
             [f"Zunahme {a2-a1}", f"{a2-a1}/{a1} = {fd(p/100) if endlich(p) else gerundet(p/100,3)}"])


# ============================================================ Daten
THEMEN = [("Lieblingssport", ["Fußball", "Schwimmen", "Tanzen", "Handball", "Turnen", "Tennis", "Reiten", "Basketball"]),
          ("Schulweg", ["Bus", "Fahrrad", "zu Fuß", "Auto", "Tram", "Roller"]),
          ("Lieblingsfach", ["Mathe", "Deutsch", "Sport", "Kunst", "Musik", "Bio", "Englisch"]),
          ("Haustier", ["Hund", "Katze", "Hase", "Fische", "Vogel", "keins"]),
          ("Lieblingsobst", ["Apfel", "Banane", "Mango", "Erdbeere", "Kiwi", "Traube"])]


def daten(c, n=5, lo=3, hi=30):
    th, kat = c.ch(THEMEN)
    c.thema_umfrage = th
    kat = c.r.sample(kat, min(n, len(kat)))
    return [(k, c.ri(lo, hi)) for k in kat]


@reg(("daten.darstellen", "saeulendiagramm"), ("daten.darstellen", "tabelle_auswerten"), ("daten.darstellen", "absolute_haeufigkeit"),
     ("daten.darstellen", "relative_haeufigkeit"), ("daten.darstellen", "kreisdiagramm"), ("daten.darstellen", "irrefuehrend"))
def _(c):
    et = c.z["etappe"]
    d = daten(c, 4 if c.k5 else 5, 2, 20 if c.k5 else 40)
    ges = sum(v for _, v in d)
    abb = balken(d)
    if et == "kreisdiagramm":
        d = [(k, v) for k, v in d]
        ges = sum(v for _, v in d)
        k0, v0 = d[0]
        w = F(v0 * 360, ges)
        return T(f"Bei einer Umfrage zum Thema „{c.thema_umfrage}“ antworteten {ges} Schüler ({', '.join(f'{k}: {v}' for k, v in d)}). Berechne den Mittelpunktswinkel für „{k0}“ im Kreisdiagramm.",
                 f"{fd(w) if endlich(w) else gerundet(w,1)}°", [f"Anteil {v0}/{ges}", f"· 360°"])
    if et == "irrefuehrend":
        return T("Ein Säulendiagramm zeigt die Verkaufszahlen 980 und 1020; die y-Achse beginnt bei 960. Die zweite Säule wirkt dreimal so hoch. Erkläre die Täuschung.",
                 "abgeschnittene Achse", ["Säulenhöhen ab 960: 20 und 60", "tatsächlicher Unterschied nur etwa 4 %"])
    if et == "relative_haeufigkeit":
        k0, v0 = d[1]
        return T(f"Die Tabelle zeigt das Ergebnis einer Umfrage zum Thema „{c.thema_umfrage}“: {', '.join(f'{k} {v}' for k, v in d)}. Welcher Anteil der Befragten nannte {k0}? Gib als Bruch und in Prozent an.",
                 f"{fz(F(v0,ges))} ≈ {gerundet(F(v0*100,ges),1)} %", [f"Gesamt {ges}", f"{v0}/{ges}"])
    if et == "absolute_haeufigkeit":
        k0, v0 = d[2]
        return T(f"In einer Strichliste wurden {ges} Stimmen gezählt: {', '.join(f'{k} {v}' for k, v in d if k != k0)}, {k0} ?. Wie viele Stimmen bekam {k0}?", str(v0),
                 [f"bekannte Summe {ges - v0}", f"{ges} − {ges-v0} = {v0}"])
    if et == "saeulendiagramm" and c.has("ergänz", "säule halb", "einzeichnen"):
        k0, v0 = d[0]
        return T(f"Zeichne ein Säulendiagramm zu den Werten {', '.join(f'{k}: {v}' for k, v in d)} (1 Kästchen = 2 Stimmen).", "Säulen mit halber Kästchenzahl", ["Achsen beschriften", "Höhen = Wert : 2"])
    mx = max(d, key=lambda t: t[1]); mn = min(d, key=lambda t: t[1])
    k1, v1 = d[0]; k2, v2 = d[1]
    grenze = ges + c.ch((-6, -2, 3, 7))
    falsch_max = c.ch([k for k, _ in d if k != mx[0]])
    erste = (f"{mx[0]} wurde am häufigsten genannt.", True) if c.ch((0, 1)) else (f"{falsch_max} wurde am häufigsten genannt.", False)
    aus = [erste, (f"{k1} wurde öfter genannt als {k2}.", v1 > v2),
           (f"Insgesamt wurden mehr als {grenze} Stimmen abgegeben.", ges > grenze), (f"{mn[0]} hat weniger als ein Zehntel aller Stimmen.", mn[1] * 10 < ges)]
    return T(f"Das Diagramm zeigt das Ergebnis einer Umfrage zum Thema „{c.thema_umfrage}“. Entscheide, ob die Aussagen wahr oder falsch sind.\n" +
             "\n".join(f"({i+1}) {s}" for i, (s, _) in enumerate(aus)), "; ".join(f"({i+1}) {'wahr' if w else 'falsch'}" for i, (_, w) in enumerate(aus)),
             ["Werte ablesen", f"Summe {ges}", "Aussagen einzeln prüfen"], abb=abb)


@reg(("L", "Mehrfachnennungen in Umfragen erkennen"))
def _(c):
    a_, b_ = c.ri(45, 70), c.ri(40, 65)
    return T(f"Bei einer Umfrage nennen {a_} % der Befragten „Musik hören“ und {b_} % „Sport“ als Hobby. Wie ist es möglich, dass die Summe über 100 % liegt? Folgt daraus, dass mehr als die Hälfte beides nennt?",
             "Mehrfachnennungen; nicht zwingend", [f"Summe {a_+b_} % > 100 % → Mehrfachantworten erlaubt", f"mindestens {a_+b_-100} % nennen beides, nicht unbedingt mehr als 50 %"])


@reg(("daten.kennwerte", "mittelwert"), ("daten.kennwerte", "mittel_tabelle"), ("daten.kennwerte", "mittel_rueckwaerts"))
def _(c):
    et = c.z["etappe"]
    w = [c.ri(1, 6) for _ in range(c.ri(5, 8))]
    m = F(sum(w), len(w))
    if et == "mittel_tabelle":
        an = [c.ri(1, 8) for _ in range(6)]
        s = sum((i + 1) * a_ for i, a_ in enumerate(an)); n_ = sum(an)
        return T("Notenverteilung einer Klassenarbeit: " + ", ".join(f"Note {i+1}: {a_}×" for i, a_ in enumerate(an)) + ". Berechne den Notendurchschnitt (auf zwei Dezimalen).",
                 gerundet(F(s, n_), 2), [f"Summe der Noten {s}", f"Anzahl {n_}", f"{s}/{n_}"])
    if et == "mittel_rueckwaerts":
        z_ = c.ri(3, 5); n_ = 4
        return T(f"Vier Würfelwürfe sollen den Mittelwert {z_} haben; die ersten drei zeigen {z_-1}, {z_+1} und {z_-2}. Was muss der vierte zeigen?", str(4 * z_ - (3 * z_ - 2)),
                 [f"Summe muss {4*z_} sein", f"{4*z_} − {3*z_-2} = {z_+2}"])
    if c.has("änderung") or c.niv == "II":
        neu = c.ri(1, 6)
        m2 = F(sum(w) + neu, len(w) + 1)
        return T(f"Die Werte {', '.join(map(str, w))} haben den Mittelwert {fd(m) if endlich(m) else gerundet(m,2)}. Ein weiterer Wert {neu} kommt hinzu. Wie ändert sich der Mittelwert?",
                 f"{fd(m2) if endlich(m2) else '≈ ' + gerundet(m2,2)}", [f"neue Summe {sum(w)+neu}", f"durch {len(w)+1}"])
    return T(f"Berechne den Mittelwert von {', '.join(map(str, w))}.", fd(m) if endlich(m) else gerundet(m, 2), [f"Summe {sum(w)}", f": {len(w)}"])


@reg(("daten.boxplot", "median"), ("daten.boxplot", "boxplot"))
def _(c):
    w = sorted(c.ri(10, 60) for _ in range(c.ch((7, 8, 9))))
    n_ = len(w)
    med = F(w[n_ // 2]) if n_ % 2 else F(w[n_ // 2 - 1] + w[n_ // 2], 2)
    c.r.shuffle(w)
    if c.z["etappe"] == "boxplot":
        return T(f"Ein Boxplot hat die Werte Minimum 12, unteres Quartil 18, Median {c.ri(20,30)}, oberes Quartil 34, Maximum 50. Lies den Median ab und erkläre, welcher Anteil der Werte darunter liegt.",
                 "Median aus dem Boxplot; etwa die Hälfte", ["Strich in der Box = Median", "50 % der Werte liegen darunter"])
    return T(f"Bestimme den Median der Werte {', '.join(map(str, w))} und erkläre dein Vorgehen.", fd(med), ["Werte ordnen", "mittlerer Wert" + (" (Mittel der beiden mittleren)" if n_ % 2 == 0 else "")])


# ============================================================ Zahlen
@reg(("zahlen.teilbarkeit", "teiler"), ("zahlen.teilbarkeit", "primzahl"), ("zahlen.teilbarkeit", "primfaktoren"))
def _(c):
    et = c.z["etappe"]
    if et == "primzahl":
        if c.has("widerleg", "behauptung"):
            return T("Behauptung: „Jede ungerade Zahl ist eine Primzahl.“ Widerlege mit einem Gegenbeispiel.", "z. B. 9 = 3·3", ["eine ungerade Zahl mit Teilern finden"])
        pz = [p for p in range(c.ri(10, 60), 100) if prim(p)][:3]
        return T(f"Gib die drei kleinsten Primzahlen an, die größer als {pz[0]-1} sind.", ", ".join(map(str, pz)), ["nur durch 1 und sich selbst teilbar", "Teiler 2, 3, 5, 7 prüfen"])
    if et == "primfaktoren":
        z_ = c.ch((36, 48, 60, 72, 84, 90, 120))
        return T(f"Zerlege {z_} in Primfaktoren und begründe damit, dass 4·{z_//4} = 6·{z_//6} ist.", " · ".join(map(str, pfz(z_))),
                 ["fortlaufend durch kleinste Primzahl teilen", "beide Produkte haben dieselbe Primfaktorzerlegung"])
    if c.k5:
        z_ = c.ch((36, 48, 60, 72, 84, 90, 96, 100, 120))
        return T(f"Gib alle Teiler von {z_} an.", ", ".join(map(str, teiler(z_))), ["Teilerpaare suchen", "bis die Paare sich treffen"])
    k = c.ri(3, 5)
    return T(f"Ist die Summe von {k} aufeinanderfolgenden natürlichen Zahlen immer durch {k} teilbar? Begründe mit einem Term.",
             "ja" if k % 2 else "nein", [f"Summe = {k}n + {k*(k-1)//2}", "durch " + str(k) + (" teilbar" if k % 2 else " nicht immer teilbar (Gegenbeispiel 1 + 2 + … )")])


@reg(("zahlen.potenzen_basis", "negativ"), ("zahlen.potenzen_basis", "quadrat"), ("zahlen.potenzen_basis", "berechnen"))
def _(c):
    et = c.z["etappe"]
    if et == "quadrat":
        if c.k5:
            z_ = [c.ri(11, 25) for _ in range(3)]
            return T(f"Berechne die Quadratzahlen: {', '.join(f'{v}²' for v in z_)}", ", ".join(str(v * v) for v in z_), ["v·v"])
        k = c.ri(11, 30)
        return T(f"Welche positive Zahl ergibt quadriert {k*k}?", str(k), [f"{k}·{k} = {k*k}"])
    if et == "negativ":
        b0 = c.ri(-6, -2); e0 = c.ch((3, 4)); k = c.ri(2, 5)
        w = b0 ** e0 - k ** 2
        return T(f"Berechne: ({b0}){hoch(e0)} − {k}² und −{k}² + ({b0})²", f"{fz(w)}; {fz(-k*k + b0*b0)}",
                 [f"({b0}){hoch(e0)} = {b0**e0}", f"{k}² = {k*k}; −{k}² = {-k*k}", f"({b0})² = {b0*b0}"])
    b0, e0 = c.ri(2, 5), c.ri(2, 4)
    return T(f"Berechne: {b0}{hoch(e0)} + {e0}{hoch(b0)}", str(b0 ** e0 + e0 ** b0), [f"{b0**e0} + {e0**b0}"])


@reg(("zahlen.potenzen_zehner", "gross_wissenschaftlich"), ("zahlen.potenzen_zehner", "vorsilben_klein"), ("zahlen.potenzen_zehner", "zehnerpotenz"))
def _(c):
    et = c.z["etappe"]
    if et == "vorsilben_klein":
        v = c.ri(2, 900)
        return T(f"Rechne {v} Milligramm in Gramm um und schreibe mit Zehnerpotenz.", f"{fd(F(v,1000))} g = {v}·10⁻³ g", ["milli = 10⁻³"])
    if et == "zehnerpotenz":
        a_, b_ = c.ri(2, 5), c.ri(6, 9)
        return T(f"Um welchen Faktor ist 3·10{hoch(b_)} größer als 3·10{hoch(a_)}?", f"10{hoch(b_-a_)}", [f"Exponenten subtrahieren: {b_} − {a_}"])
    z_ = c.ri(12, 98); e_ = c.ri(6, 9)
    wort = {6: "Millionen", 9: "Milliarden"}.get(e_, "")
    return T(f"Schreibe {z_}·10{hoch(e_)} als ausgeschriebene Zahl und in wissenschaftlicher Schreibweise (eine Ziffer vor dem Komma).",
             f"{fz(z_*10**e_)}; {fd(F(z_,10))}·10{hoch(e_+1)}", ["Nullen anhängen", "Komma um eine Stelle verschieben"])


@reg(("zahlen.rechengesetze", "verteilen"))
def _(c):
    a_, b_ = c.ri(11, 49), c.ri(2, 9)
    if c.k5 and c.niv == "I":
        return T(f"Rechne geschickt mit dem Distributivgesetz: {b_}·{a_}", str(a_ * b_), [f"{b_}·{a_//10*10} + {b_}·{a_%10}", str(a_ * b_)])
    k = c.ri(2, 9)
    return T(f"Berechne geschickt und erkläre: {k}·{a_} + {k}·{100-a_}", str(k * 100), ["gleichen Faktor ausklammern", f"{k}·({a_} + {100-a_}) = {k}·100"])


@reg(("zahlen.ganz", "zahlengerade"))
def _(c):
    m = c.nz(-6, 6)
    if c.k5 and c.niv == "I":
        return T(f"Zeichne eine Zahlengerade von −10 bis 10 und markiere {m} und {-m}.", "Markierungen", ["gleicher Abstand zur 0, verschiedene Seiten"])
    d_ = c.ri(abs(m) + 1, abs(m) + 8)
    return T(f"Gib zwei Zahlen mit verschiedenen Vorzeichen an, deren Mitte auf der Zahlengeraden {m} ist und die {2*d_} voneinander entfernt sind.", f"{m-d_} und {m+d_}",
             [f"je {d_} links und rechts von {m}"])


@reg(("zahlen.intervalle", "schreiben"), ("zahlen.intervalle", "lesen"))
def _(c):
    a_, b_ = c.ri(10, 40), c.ri(50, 90)
    if c.z["etappe"] == "lesen":
        p = c.ri(1, 6)
        return T(f"Welche Menge ist die maximale Definitionsmenge von f(x) = 1/(x − {p})? (A) ]{p}; ∞[  (B) ℚ \\ {{{p}}}  (C) [{p}; ∞[", "B", [f"nur x = {p} ausgeschlossen"])
    return T(f"Ein Winkel α ist größer als {a_}° und höchstens {b_}°. Schreibe den Bereich als Intervall.", f"]{a_}°; {b_}°]", ["offene Klammer: Grenze gehört nicht dazu"])


@reg(("zahlen.rechengesetze", "sach"))
def _(c):
    p_, n1, n2 = c.ri(2, 9), c.ri(20, 80), c.ri(10, 40)
    if c.k5:
        st, lh, pa = c.ri(2, 5), c.ri(15, 30), c.ri(20, 60)
        return T(f"Ein Handwerker berechnet {lh} € pro Stunde und eine Anfahrtspauschale von {pa} €. Er arbeitet {st} Stunden. Wie viel kostet das?", f"{lh*st+pa} €",
                 [f"{lh}·{st} = {lh*st}", f"+ {pa}"])
    q1, q2 = F(c.ri(6, 25) * 10, 100), F(c.ri(6, 25) * 10, 100)
    return T(f"Am Schulfest werden {n1} Becher Saft zu {eur(q1)} € und {n2} Becher Tee zu {eur(q2)} € verkauft. Wie hoch sind die Einnahmen?",
             f"{eur(n1*q1 + n2*q2)} €", [f"{n1}·{eur(q1)} € = {eur(n1*q1)} €", f"{n2}·{eur(q2)} € = {eur(n2*q2)} €", "addieren"])


# ============================================================ außerhalb: Wurzeln (Kl. 9)
@reg(("X", "teilweise Wurzelziehen (LehrplanPLUS Kl. 9)"), ("X", "Wurzelgesetze (LehrplanPLUS Kl. 9)"), ("X", "binomische Formel mit Wurzeln (Kl. 9)"),
     ("X", "reelle/irrationale Zahlen (Kl. 9)"), ("X", "irrationale Zahlen (Kl. 9)"), ("X", "quadratische Gleichung (LehrplanPLUS Kl. 9, Test noch G8)"))
def _(c):
    v = c.z["vorschlag"]
    if "teilweise" in v:
        z = [(q, r) for q, r in ((c.ri(2, 6), c.ch((2, 3, 5, 7))) for _ in range(3))]
        return T("Ziehe teilweise die Wurzel: " + "; ".join(f"√{q*q*r}" for q, r in z), "; ".join(f"{q}√{r}" for q, r in z), ["größten Quadratfaktor suchen"])
    if "Wurzelgesetze" in v:
        a_ = c.ri(2, 7)
        return T(f"Vereinfache: √{a_} · √{a_*4};  √{a_*9} : √{a_}", f"{2*a_}; 3", [f"√{a_*a_*4} = {2*a_}", f"√9 = 3"])
    if "binomische" in v:
        a_ = c.ri(2, 7)
        return T(f"Berechne: (√{a_} + 1)²", f"{a_+1} + 2√{a_}", [f"{a_} + 2√{a_} + 1"])
    if "quadratische" in v:
        k = c.ri(2, 9)
        return T(f"Löse über ℚ⁺: x² − {k*k} = 0", f"x = {k}", [f"x² = {k*k}", "positive Lösung"])
    if "reelle" in v:
        k = c.ri(2, 9)
        return T(f"Wahr oder falsch? Begründe. (1) √{k*k} ist rational. (2) Jede Wurzel ist irrational. (3) Zwischen 1 und 2 liegt eine irrationale Zahl. (4) √{k*k+1} ist eine natürliche Zahl.",
                 "(1) wahr (2) falsch (3) wahr (4) falsch", [f"√{k*k} = {k}", "Gegenbeispiel √4 = 2", "z. B. √2 ≈ 1,41", f"{k}² < {k*k+1} < {k+1}²"])
    return T("Gib zwei irrationale Zahlen an, deren Produkt rational ist.", "z. B. √2 und √8 (Produkt 4)", ["√2·√8 = √16 = 4"])
