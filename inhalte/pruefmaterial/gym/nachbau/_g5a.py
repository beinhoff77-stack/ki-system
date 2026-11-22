# Generatoren Klasse 5: Zahlen, Rechnen, Gleichungen, Teilbarkeit, Potenzen
from _kern import *

EINER = ["null", "ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf",
         "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn"]
ZEHNER = ["", "", "zwanzig", "dreißig", "vierzig", "fünfzig", "sechzig", "siebzig", "achtzig", "neunzig"]


def _bis999(n):
    s = ""
    if n >= 100:
        s += EINER[n // 100] + "hundert"; n %= 100
    if n == 0:
        return s
    if n < 20:
        return s + EINER[n]
    e, z = n % 10, n // 10
    return s + ((EINER[e] + "und") if e else "") + ZEHNER[z]


def zahlwort(n):
    if n == 0:
        return "null"
    teile = []
    for wert, sg, pl in ((10**9, "eine Milliarde", "Milliarden"), (10**6, "eine Million", "Millionen")):
        if n >= wert:
            k = n // wert
            teile.append(sg if k == 1 else _bis999(k) + " " + pl)
            n %= wert
    if n >= 1000:
        teile.append(_bis999(n // 1000) + "tausend"); n %= 1000
    if n:
        r = _bis999(n)
        if n % 100 == 1 and n % 100 != 11:
            r += "s"
        teile.append(r)
    return " ".join(teile)


def zahl_aus_wort(w):
    """unabhängige Rückübersetzung eines Zahlworts (für die Prüfung)"""
    W = {z: i for i, z in enumerate(EINER)}
    W.update({"eins": 1, "eine": 1})
    Z = {z: i * 10 for i, z in enumerate(ZEHNER) if z}
    def klein(t):
        v = 0
        if "hundert" in t:
            h, t = t.split("hundert", 1); v += W[h] * 100
        if not t:
            return v
        if "und" in t:
            e, z = t.split("und", 1); return v + W[e] + Z[z]
        if t in Z:
            return v + Z[t]
        return v + W[t]
    tot = 0
    teile = w.split()
    i = 0
    while i < len(teile):
        t = teile[i]
        if i + 1 < len(teile) and teile[i + 1] in ("Milliarde", "Milliarden", "Million", "Millionen"):
            f = 10**9 if teile[i + 1].startswith("Milliard") else 10**6
            tot += (1 if t == "eine" else klein(t)) * f; i += 2; continue
        if "tausend" in t:
            a_, t = t.split("tausend", 1); tot += (klein(a_) if a_ else 1) * 1000
        if t:
            tot += klein(t)
        i += 1
    return tot


def gross(c, stellen):
    return c.ri(10 ** (stellen - 1), 10 ** stellen - 1)


# ============================================================ zahlen.natuerlich
@reg(("zahlen.natuerlich", "stellenwert"))
def _(c):
    if c.has("differenz", "maximal"):
        k = c.r.sample(range(1, 10), 6)
        gr = int("".join(map(str, sorted(k[:3], reverse=True)))); kl_ = int("".join(map(str, sorted(k[3:]))))
        best = max(int("".join(map(str, sorted(p, reverse=True)))) - int("".join(map(str, sorted(q))))
                   for p in itertools.combinations(k, 3) for q in [tuple(z for z in k if z not in p)])
        chk(best == max(int("".join(map(str, p))) - int("".join(map(str, q))) for p in itertools.permutations(k, 3)
                        for q in itertools.permutations([z for z in k if z not in p], 3)), "alle Anordnungen durchprobiert")
        return T(f"Lege mit den Ziffernkarten {', '.join(map(str, k))} zwei dreistellige Zahlen (jede Karte genau einmal), deren Differenz möglichst groß ist.", f"Differenz {best}",
                 ["große Zahl: die drei größten Ziffern absteigend", "kleine Zahl: die drei kleinsten aufsteigend", f"Differenz {best}"])
    if c.has("kleinste", "größte", "karten", "bilden", "nahe"):
        k = c.r.sample(range(0, 10), c.ri(5, 7))
        gr = "".join(map(str, sorted(k, reverse=True)))
        kl_ = sorted(k);
        if kl_[0] == 0:
            kl_[0], kl_[1] = kl_[1], kl_[0]
        kl_ = "".join(map(str, kl_))
        alle = [int("".join(map(str, p))) for p in itertools.permutations(k) if p[0] != 0]
        chk(int(gr) == max(alle) and int(kl_) == min(alle), "alle Anordnungen durchprobiert")
        return T(f"Bilde aus den Ziffern {', '.join(map(str, k))} (jede genau einmal) die größte und die kleinste mögliche Zahl.", f"{fz(int(gr))}; {fz(int(kl_))}",
                 ["größte: Ziffern absteigend", "kleinste: aufsteigend, 0 nicht vorne"])
    z_ = gross(c, c.ri(6, 9))
    s_ = str(z_)
    pos = c.ri(0, len(s_) - 2)
    namen = ["Einer", "Zehner", "Hunderter", "Tausender", "Zehntausender", "Hunderttausender", "Millionen", "Zehnmillionen", "Hundertmillionen"]
    stelle = len(s_) - 1 - pos
    chk(z_ // 10**stelle % 10 == int(s_[pos]), "Ziffer an der Stelle")
    return T(f"Welchen Stellenwert hat die Ziffer {s_[pos]} (die {pos+1}. Ziffer von links) in der Zahl {fz(z_)}? Gib ihren Wert an.",
             f"{namen[stelle]}; Wert {fz(int(s_[pos]) * 10**stelle)}", ["Stellen von rechts zählen", f"{s_[pos]} · {fz(10**stelle)}"])


@reg(("zahlen.natuerlich", "zahlwort_zu_ziffern"), ("zahlen.natuerlich", "ziffern_zu_zahlwort"))
def _(c):
    z_ = [c.ri(10**5, 10**9) for _ in range(2)]
    z_ = [int(str(v)[:3] + "0" * (len(str(v)) - 6) + str(v)[-3:]) if len(str(v)) > 6 else v for v in z_]
    if c.z["etappe"] == "ziffern_zu_zahlwort":
        chk(zahl_aus_wort(zahlwort(z_[0])) == z_[0], "Zahlwort zurückübersetzt")
        return T(f"Schreibe als Zahlwort: {fz(z_[0])}", zahlwort(z_[0]), ["in Dreiergruppen von rechts gliedern", "Gruppen benennen"])
    chk(all(zahl_aus_wort(zahlwort(v)) == v for v in z_), "Zahlwort zurückübersetzt")
    return T(f"Schreibe mit Ziffern: „{zahlwort(z_[0])}“ und „{zahlwort(z_[1])}“", f"{fz(z_[0])}; {fz(z_[1])}", ["Stellenwerttafel nutzen", "fehlende Stellen mit 0 füllen"])


@reg(("zahlen.natuerlich", "runden_regel"), ("zahlen.natuerlich", "runden_uebertrag"), ("zahlen.natuerlich", "runden_sinnvoll"))
def _(c):
    et = c.z["etappe"]
    z_ = gross(c, c.ri(5, 8))
    if et == "runden_uebertrag":
        z0 = gross(c, 6)
        s0 = str(z0)
        pos = len(s0) - 3          # Hunderterziffer verdecken
        ziel = runde(z0, 1000)
        ok = [d for d in range(10) if runde(int(s0[:pos] + str(d) + s0[pos+1:]), 1000) == ziel]
        chk(ok, "mindestens eine Ziffer passt")
        verdeckt = s0[:pos] + "▢" + s0[pos+1:]
        return T(f"In der Zahl {verdeckt} ist die Hunderterziffer verdeckt. Auf Tausender gerundet ergibt sich {fz(ziel)}. Welche Ziffern sind möglich?",
                 ", ".join(map(str, ok)), ["Hunderterziffer entscheidet über Auf- oder Abrunden", f"Rundung {fz(ziel)} → " + ("aufgerundet: 5–9" if ok[0] >= 5 else "abgerundet: 0–4")])
    if et == "runden_sinnvoll":
        e_ = [(c.ch(("Augsburg", "Würzburg", "Regensburg", "Ingolstadt")), gross(c, 6)) for _ in range(3)]
        chk(all(abs(runde(v, 1000) - v) <= 500 and runde(v, 1000) % 1000 == 0 for _, v in e_), "Rundung")
        r0 = runde(e_[0][1], 1000)
        return T("a) Runde die Einwohnerzahlen auf Tausender: " + "; ".join(f"Stadt {i+1}: {fz(v)}" for i, (_, v) in enumerate(e_)) +
                 "\nb) Welche Einwohnerzahlen sind für Stadt 1 möglich, wenn nur die gerundete Zahl bekannt ist? Gib die kleinste und die größte an."
                 "\nc) Begründe, warum Zeitungen meist gerundete Zahlen angeben.",
                 "a) " + "; ".join(fz(runde(v, 1000)) for _, v in e_) + f"; b) {fz(r0-500)} bis {fz(r0+499)}",
                 ["Hunderterziffer entscheidet", f"Grenzen: {fz(r0-500)} und {fz(r0+499)}", "genaue Zahl ändert sich ständig, gerundet leichter zu merken"])
    if c.has("größter", "kleinste", "rückwärts", "wert mit", "zahl, die", "anzahl"):
        r_ = c.ri(12, 98) * 1000
        chk(runde(r_ - 500, 1000) == r_ and runde(r_ + 499, 1000) == r_ and runde(r_ - 501, 1000) != r_ and runde(r_ + 500, 1000) != r_, "Grenzen geprüft")
        return T(f"Eine Zahl wurde auf Tausender gerundet; das Ergebnis ist {fz(r_)}. Gib die kleinste und die größte natürliche Zahl an, die so gerundet worden sein kann.",
                 f"{fz(r_-500)} und {fz(r_+499)}", ["ab Hunderterziffer 5 wird aufgerundet", f"kleinste {fz(r_-500)}, größte {fz(r_+499)}"])
    if c.has("korrekt", "prüf"):
        r1 = runde(z_, 1000); r2 = runde(z_, 100) + 100
        return T(f"Welche Rundung ist richtig? {fz(z_)} ≈ {fz(r1)} (Tausender) oder {fz(z_)} ≈ {fz(r2)} (Hunderter)? Begründe.", f"{fz(r1)} (Tausender)",
                 ["Ziffer rechts neben der Rundungsstelle prüfen", f"Hunderter richtig wäre {fz(runde(z_,100))}"])
    st = [(10, "Zehner"), (100, "Hunderter"), (1000, "Tausender"), (10000, "Zehntausender")]
    chk(all(int(F(z_, v) + F(1, 2)) * v == runde(z_, v) for v, _ in st), "Rundung unabhängig nachgerechnet")
    return T(f"Runde {fz(z_)} auf " + ", ".join(n for _, n in st) + ".", "; ".join(fz(runde(z_, v)) for v, _ in st),
             ["Ziffer rechts neben der Rundungsstelle: 0–4 abrunden, 5–9 aufrunden"])


@reg(("zahlen.natuerlich", "vergleichen"))
def _(c):
    if c.has("vorgänger", "nachfolger", "nachbar"):
        z_ = gross(c, 7)
        chk((z_ - 1) + 1 == z_, "Nachbarzahlen")
        return T(f"Gib Vorgänger und Nachfolger von {fz(z_)} und von {fz(z_ - z_ % 1000)} an.", f"{fz(z_-1)}, {fz(z_+1)}; {fz(z_ - z_%1000 - 1)}, {fz(z_ - z_%1000 + 1)}",
                 ["±1", "Übertrag beachten"])
    w = sorted(c.r.sample(range(10**6, 10**7), 4))
    w = [w[0], w[0] + c.ri(1, 9) * 10, w[2], int(str(w[0])[::-1][:7]) if len(str(w[0])[::-1]) == 7 else w[3]]
    w = list(dict.fromkeys(w))
    c.r.shuffle(w)
    chk(sorted(w) == sorted(w, key=lambda v: (len(str(v)), str(v))), "Vergleich über Stellenzahl und Ziffern")
    return T("Ordne der Größe nach mit „<“: " + "; ".join(fz(v) for v in w), " < ".join(fz(v) for v in sorted(w)),
             ["Stellenzahl vergleichen", "von links stellenweise vergleichen"])


@reg(("zahlen.natuerlich", "strahl_ablesen"), ("zahlen.natuerlich", "strahl_eintragen"))
def _(c):
    s0 = c.ri(1, 9) * 10 ** c.ri(2, 5); sch = c.ch((s0 // 10, s0 // 5, s0 // 2)) or 1
    start = c.ri(1, 9) * s0
    marks = sorted(c.r.sample(range(1, 11), 3))
    if c.z["etappe"] == "strahl_eintragen":
        zielen = [start + m * sch for m in marks]
        chk(all((v - start) % sch == 0 for v in zielen), "Lage auf Teilstrichen")
        return T(f"Zeichne einen Zahlenstrahl, der bei {fz(start)} beginnt; 1 cm entspricht {fz(sch)}. Trage die Zahlen {', '.join(fz(v) for v in zielen)} ein.",
                 "; ".join(f"{fz(v)} bei {m} cm" for v, m in zip(zielen, marks)), ["Abstand vom Start durch Schrittweite teilen"])
    chk(all(start + m * sch - start == m * sch for m in marks), "Teilstriche")
    return T(f"Ein Zahlenstrahl beginnt bei {fz(start)}; zwischen zwei Teilstrichen liegen {fz(sch)}. Welche Zahlen gehören zu den Teilstrichen Nr. {', '.join(map(str, marks))}?",
             "; ".join(fz(start + m * sch) for m in marks), [f"Start + Nummer · {fz(sch)}"])


@reg(("zahlen.natuerlich", "roemisch_schreiben"), ("zahlen.natuerlich", "roemisch_system"))
def _(c):
    z_ = [c.ri(14, 3999) for _ in range(3)]
    if c.z["etappe"] == "roemisch_system":
        a_, b_ = c.ri(12, 400), c.ri(12, 400)
        chk(aus_roemisch(roemisch(a_ + b_)) == aus_roemisch(roemisch(a_)) + aus_roemisch(roemisch(b_)), "römisch zurückgerechnet")
        return T(f"Rechne {roemisch(a_)} + {roemisch(b_)} und gib das Ergebnis römisch an. Erkläre einen Unterschied zwischen römischem System und Zehnersystem.",
                 roemisch(a_ + b_), [f"{a_} + {b_} = {a_+b_}", "römisch: kein Stellenwertsystem, keine Null"])
    if c.has("in dezimal", "römisch in", "vorgänger"):
        for v in z_:
            chk(aus_roemisch(roemisch(v)) == v, "Rückumwandlung")
        return T("Schreibe im Zehnersystem: " + "; ".join(roemisch(v) for v in z_), "; ".join(str(v) for v in z_), ["Werte addieren, kleineres Zeichen vor größerem wird abgezogen"])
    chk(all(aus_roemisch(roemisch(v)) == v for v in z_), "Rückumwandlung")
    return T("Schreibe als römische Zahl: " + "; ".join(str(v) for v in z_), "; ".join(roemisch(v) for v in z_), ["in Tausender, Hunderter, Zehner, Einer zerlegen"])


@reg(("zahlen.natuerlich", "dualsystem"))
def _(c):
    b_ = c.ch((2, 3, 4, 5, 7)) if not c.has("dual", "zweier") else 2
    z_ = [c.ri(5, 120) for _ in range(3)]
    if c.has("ziffern", "wissen"):
        return T(f"Welche Ziffern gibt es im {b_}er-System? Welche Stellenwerte haben die ersten vier Stellen?", f"0 bis {b_-1}; 1, {b_}, {b_*b_}, {b_**3}",
                 ["Ziffern kleiner als die Basis", "Potenzen der Basis"])
    if c.has("ins zehner", "aus anderen", "dezimal", "→ dezimal") or c.ch((0, 1)):
        for v in z_:
            chk(int(basis(v, b_), b_) == v, "Rückumwandlung")
        return T(f"Rechne aus dem {b_}er-System ins Zehnersystem um: " + "; ".join(f"({basis(v, b_)})_{b_}" for v in z_), "; ".join(str(v) for v in z_),
                 ["Stellenwerte " + ", ".join(str(b_**i) for i in range(4)), "Ziffer · Stellenwert addieren"])
    chk(all(int(basis(v, b_), b_) == v for v in z_), "Rückumwandlung")
    return T(f"Schreibe im {b_}er-System: " + "; ".join(str(v) for v in z_), "; ".join(f"({basis(v, b_)})_{b_}" for v in z_),
             [f"fortgesetzt durch {b_} teilen, Reste von unten lesen"])


# ============================================================ zahlen.rechengesetze
@reg(("zahlen.rechengesetze", "punkt_strich"), ("zahlen.rechengesetze", "klammern"))
def _(c):
    a_, b_, cc, d_ = c.ri(12, 90), c.ri(2, 9), c.ri(3, 12), c.ri(2, 9)
    if c.has("klammern setzen", "setzen"):
        w = (a_ + b_) * cc
        chk(ev(f"({a_} + {b_}) · {cc}") == w and ev(f"{a_} + {b_} · {cc}") != w, "Klammer nötig")
        return T(f"Setze Klammern so, dass die Rechnung stimmt: {a_} + {b_} · {cc} = {w}", f"({a_} + {b_}) · {cc} = {w}", [f"ohne Klammer: {a_+b_*cc}", "Klammer um die Summe"])
    if c.z["etappe"] == "klammern":
        w = (a_ - b_ * d_) * 2 + cc ** 2 if c.niv != "I" else (a_ + cc) * b_
        if c.niv != "I":
            if a_ - b_ * d_ < 0:
                a_ = b_ * d_ + c.ri(1, 30); w = (a_ - b_ * d_) * 2 + cc ** 2
            chk(ev(f"({a_} − {b_} · {d_}) · 2 + {cc}²") == w, "Ausdruck ausgewertet")
            return T(f"Berechne: ({a_} − {b_} · {d_}) · 2 + {cc}²", str(w), [f"Klammer: {a_} − {b_*d_} = {a_-b_*d_}", f"Potenz: {cc*cc}", f"{(a_-b_*d_)*2} + {cc*cc} = {w}"])
        chk(ev(f"({a_} + {cc}) · {b_}") == w, "Ausdruck ausgewertet")
        return T(f"Berechne: ({a_} + {cc}) · {b_}", str(w), [f"Klammer zuerst: {a_+cc}", f"· {b_} = {w}"])
    q = b_ * d_
    w = a_ + q // d_ * cc - b_
    chk(ev(f"{a_} + {q} : {d_} · {cc} − {b_}") == a_ + b_ * cc - b_, "Ausdruck ausgewertet")
    return T(f"Berechne: {a_} + {q} : {d_} · {cc} − {b_}", str(a_ + b_ * cc - b_), [f"Punkt vor Strich: {q} : {d_} · {cc} = {b_*cc}", f"{a_} + {b_*cc} − {b_} = {a_+b_*cc-b_}"])


@reg(("zahlen.rechengesetze", "schriftlich_geteilt"), ("zahlen.rechengesetze", "schriftlich"), ("zahlen.rechengesetze", "geteilt_ganz"),
     ("zahlen.rechengesetze", "umkehraufgabe_mal"))
def _(c):
    et = c.z["etappe"]
    if et == "schriftlich_geteilt":
        d_ = c.ri(3, 9) if c.niv == "I" and not c.has("zweistell") else c.ri(12, 48)
        q_ = c.ri(105, 2999)
        rest = c.ri(1, d_ - 1) if c.has("rest") else 0
        chk(divmod(q_ * d_ + rest, d_) == (q_, rest), "Division mit Rest")
        return T(f"Berechne schriftlich: {fz(q_*d_+rest)} : {d_}", f"{fz(q_)}" + (f" Rest {rest}" if rest else ""), ["Stelle für Stelle teilen, Rest weiterführen", f"Probe: {q_}·{d_}" + (f" + {rest}" if rest else "")])
    if et == "geteilt_ganz":
        if c.has("verdoppelt"):
            return T("Was passiert mit dem Ergebnis einer Division, wenn man den Divisor verdoppelt und den Dividenden gleich lässt? Begründe an einem Beispiel.", "es halbiert sich",
                     ["z. B. 48 : 6 = 8, 48 : 12 = 4"])
        a_, b_ = c.ri(2, 12), c.ri(2, 12)
        chk(ev(f"(−{a_*b_}) : {b_}") == -a_ and ev(f"{a_*b_} : (−{a_})") == -b_, "Quotienten")
        return T(f"Berechne: ({-a_*b_}) : {b_} und {a_*b_} : ({-a_})", f"{-a_}; {-b_}", ["Vorzeichen verschieden → negativ"])
    if et == "umkehraufgabe_mal":
        a_, b_ = c.ri(12, 99), c.ri(3, 9)
        s = str(a_ * b_)
        chk(int(s) % a_ == 0 and int(s) // a_ == b_, "Umkehraufgabe")
        return T(f"In der Rechnung {a_} · ▢ = {s} ist eine Ziffer verdeckt. Bestimme sie mit der Umkehraufgabe.", str(b_), [f"{s} : {a_} = {b_}"])
    a_, b_ = c.ri(123, 987), c.ri(13, 89)
    if c.has("lücke", "fehlende ziffer"):
        p_ = a_ * b_
        chk(p_ // b_ == a_ and p_ % b_ == 0, "Umkehraufgabe")
        return T(f"Ergänze die fehlenden Ziffern: {str(a_)[0]}▢{str(a_)[2]} · {b_} = {fz(p_)}", str(a_)[1], [f"{fz(p_)} : {b_} = {a_}"])
    chk(ev(f"{a_} · {b_}") == a_ * b_ and a_ * (b_ // 10 * 10) + a_ * (b_ % 10) == a_ * b_, "Teilprodukte")
    return T(f"Berechne schriftlich: {a_} · {b_}", fz(a_ * b_), [f"{a_}·{b_//10*10} = {a_*(b_//10*10)}", f"{a_}·{b_%10} = {a_*(b_%10)}", "addieren"])


@reg(("zahlen.rechengesetze", "termaufbau"))
def _(c):
    v = c.ri(0, 3)
    a_, b_, cc = c.ri(12, 60), c.ri(3, 9), c.ri(2, 8)
    if c.has("termart", "benennen", "fachbegriff", "beschreib", "erklär"):
        chk(ev(f"({a_} + {b_}) · {cc}") == (a_ + b_) * cc, "Ausdruck ausgewertet")
        return T(f"Berechne den Term ({a_} + {b_}) · {cc} und gib die Art des Terms (Summe, Differenz, Produkt, Quotient) an. Benenne die Teile.", f"{(a_+b_)*cc}; Produkt",
                 ["zuletzt wird multipliziert → Produkt", f"Faktoren ({a_} + {b_}) und {cc}"])
    if c.has("text zum term", "zuordnen", "ankreuz", "wort"):
        chk(ev(f"({a_} + {b_}) · ({cc*3} − {cc})") == (a_ + b_) * 2 * cc, "Ausdruck ausgewertet")
        return T(f"Schreibe als Term und berechne: „Multipliziere die Summe aus {a_} und {b_} mit der Differenz aus {cc*3} und {cc}.“", f"({a_} + {b_}) · ({cc*3} − {cc}) = {(a_+b_)*2*cc}",
                 ["Summe und Differenz in Klammern", "dann multiplizieren"])
    if c.has("restbetrag", "geld", "kosten") or v == 0:
        g_ = c.ri(20, 50); p1, p2 = c.ri(3, 9), c.ri(2, 8)
        chk(ev(f"{g_} − {cc}·{p1} − {p2*3}") == g_ - cc * p1 - p2 * 3, "Ausdruck ausgewertet")
        return T(f"Ben hat {g_} €. Er kauft {cc} Hefte zu je {p1} € und ein Buch für {p2*3} €. Schreibe einen Term für den Restbetrag und berechne ihn.", f"{g_} − {cc}·{p1} − {p2*3} = {g_-cc*p1-p2*3} €",
                 ["Ausgaben abziehen", f"{g_} − {cc*p1} − {p2*3}"]) if g_ - cc * p1 - p2 * 3 > 0 else T(
            f"Ben hat {g_+40} €. Er kauft {cc} Hefte zu je {p1} € und ein Buch für {p2*3} €. Schreibe einen Term für den Restbetrag und berechne ihn.", f"{g_+40} − {cc}·{p1} − {p2*3} = {g_+40-cc*p1-p2*3} €",
            ["Ausgaben abziehen"])
    chk(ev(f"{a_*cc} : {cc} + 2 · {b_}") == a_ + 2 * b_, "Ausdruck ausgewertet")
    return T(f"Stelle einen Term auf: „Dividiere {a_*cc} durch {cc} und addiere zum Ergebnis das Doppelte von {b_}.“ Berechne.", f"{a_*cc} : {cc} + 2 · {b_} = {a_+2*b_}",
             ["Quotient", "plus Produkt"])


@reg(("zahlen.rechengesetze", "mal_ganz"))
def _(c):
    a_, b_ = c.nz(-12, 12), c.nz(-12, 12)
    if c.has("produkt gegeben", "zwei ganze", "offen"):
        p_ = -c.ri(2, 9) * c.ri(2, 9)
        return T(f"Gib zwei ganze Zahlen an, deren Produkt {p_} ist (mindestens zwei Möglichkeiten).", "z. B. " + ", ".join(f"{t}·({p_//t})" for t in teiler(-p_)[:2]),
                 ["ein Faktor negativ, einer positiv"])
    if c.has("vorzeichen"):
        return T("Welches Vorzeichen hat das Produkt (−3)·(−5)·(−2)·4? Begründe ohne zu rechnen.", "negativ", ["drei negative Faktoren → ungerade Anzahl → negativ"])
    chk(ev(f"({a_})·({b_})") == a_ * b_, "Produkt")
    return T(f"Berechne: ({a_}) · ({b_}) und ({a_}) · ({b_}) · (−1)", f"{a_*b_}; {-a_*b_}", ["Vorzeichenregel", "Beträge multiplizieren"])


@reg(("zahlen.rechengesetze", "vorteil"))
def _(c):
    if c.has("summe", "ordnen"):
        w = [c.ri(11, 89) for _ in range(2)]
        e = [100 - w[0], 100 - w[1]]
        z = [w[0], w[1], e[0], e[1]]
        c.r.shuffle(z)
        chk(sum(z) == 200, "zwei Hunderter")
        return T("Rechne geschickt: " + " + ".join(map(str, z)), str(sum(z)), ["Summanden zu Hundertern zusammenfassen", f"= {sum(z)}"])
    if c.has("wertgleich", "ankreuz"):
        a_ = c.ri(12, 49)
        return T(f"Welche Ausdrücke haben denselben Wert wie 4 · {a_} · 25? (A) 100 · {a_}  (B) 4 + {a_} + 25  (C) {a_} · 25 · 4  (D) 29 · {a_}", "A und C",
                 ["Kommutativ-/Assoziativgesetz: Reihenfolge der Faktoren egal", "4·25 = 100"])
    a_ = c.ri(12, 99)
    p, q = c.ch(((4, 25), (2, 50), (5, 20), (8, 125)))
    chk(ev(f"{p} · {a_} · {q}") == p * q * a_, "Produkt")
    return T(f"Rechne geschickt: {p} · {a_} · {q}", str(p * q * a_), [f"{p}·{q} = {p*q}", f"{p*q}·{a_}"])


@reg(("zahlen.rechengesetze", "kopfrechnen"), ("zahlen.rechengesetze", "ueberschlag"))
def _(c):
    if c.z["etappe"] == "ueberschlag":
        w = [c.ri(110, 980) for _ in range(4)]
        ub = sum(runde(v, 100) for v in w)
        chk(abs(ub - sum(w)) <= 200, "Überschlag nahe am genauen Wert")
        return T(f"Eine Rundreise hat die Etappen {', '.join(f'{v} km' for v in w)}. Überschlage die Gesamtstrecke und rechne dann genau.", f"Überschlag {ub} km; genau {sum(w)} km",
                 ["auf Hunderter runden", f"{' + '.join(str(runde(v,100)) for v in w)} = {ub}", f"genau {sum(w)}"])
    if c.has("quadrat", "füllen"):
        a_, b_, cc = c.ri(2, 9), c.ri(2, 9), c.ri(2, 9)
        return T(f"Fülle das Rechenquadrat: Zeile 1: {a_} · ▢ = {a_*b_}; Zeile 2: ▢ · {cc} = {b_*cc}; Spalte: {a_} · ▢ = {a_*cc*2}. Bestimme die fehlenden Zahlen.",
                 f"{b_}; {b_}; {cc*2}", [f"{a_*b_} : {a_} = {b_}", f"{b_*cc} : {cc} = {b_}", f"{a_*cc*2} : {a_} = {cc*2}"])
    if c.has("einmaleins", "falsch"):
        k = c.ri(6, 9)
        zeilen = [(i, k * i + (1 if i == 7 else 0)) for i in range(5, 9)]
        return T("Welche Zeile ist falsch? " + "; ".join(f"{i}·{k} = {v}" for i, v in zeilen), f"7·{k} = {7*k+1} (richtig {7*k})", ["jede Zeile nachrechnen"])
    a_ = c.ri(2, 9)
    return T(f"Ein Kind rechnet 25 · {a_*4} als {a_*4} : 4 · 100. Erkläre, warum das funktioniert, und berechne.", str(25 * a_ * 4), ["25 = 100 : 4", f"{a_*4} : 4 = {a_}, · 100"])


# ============================================================ zahlen.ganz
@reg(("zahlen.ganz", "schriftlich_plus_minus"), ("zahlen.ganz", "addieren"), ("zahlen.ganz", "subtrahieren"), ("zahlen.ganz", "ketten"))
def _(c):
    et = c.z["etappe"]
    if et == "schriftlich_plus_minus":
        a_, b_, cc = gross(c, c.ri(4, 6)), gross(c, c.ri(4, 6)), gross(c, 4)
        if c.has("fehlende", "operation"):
            return T(f"Setze + oder − ein, damit die Rechnung stimmt: {fz(a_+b_)} ▢ {fz(b_)} = {fz(a_)}", "−", ["Umkehraufgabe"])
        chk(ev(f"{a_} + {b_} − {cc}") == a_ + b_ - cc, "Ausdruck ausgewertet")
        return T(f"Berechne schriftlich: {fz(a_)} + {fz(b_)} − {fz(cc)}", fz(a_ + b_ - cc), [f"{fz(a_)} + {fz(b_)} = {fz(a_+b_)}", f"− {fz(cc)}"])
    if et == "ketten":
        a_, b_, cc = c.nz(-15, 15), c.nz(-15, 15), c.nz(-9, 9)
        chk(ev(f"{a_} − ({b_}) + ({cc}) − ({a_ + cc})") == -b_, "Ausdruck ausgewertet")
        return T(f"Berechne: {a_} − {kl(b_)} + {kl(cc)} − {kl(a_ + cc)}", fz(a_ - b_ + cc - (a_ + cc)), ["Minus einer negativen Zahl = Plus", "schrittweise rechnen"])
    a_, b_ = c.nz(-40, 40), c.nz(-40, 40)
    if et == "subtrahieren":
        b_ = -c.ri(2, 40); a_ = c.nz(-40, 40)
        chk(ev(f"{a_} − ({b_})") == a_ - b_, "Ausdruck ausgewertet")
        return T(f"Berechne: {a_} − {kl(b_)} und {-b_} − {abs(a_)+7}", f"{a_-b_}; {-b_-abs(a_)-7}", ["Subtrahieren = Addieren der Gegenzahl"])
    if c.has("mauer"):
        u = [c.nz(-9, 9) for _ in range(3)]
        m = [u[0] + u[1], u[1] + u[2]]
        chk(m[0] + m[1] == u[0] + 2 * u[1] + u[2], "oberer Stein")
        return T(f"Zahlenmauer: Unten stehen {u[0]}, {u[1]}, {u[2]}; jeder Stein ist die Summe der beiden darunter. Berechne die mittlere Reihe und den obersten Stein.", f"{m[0]}, {m[1]}; {m[0]+m[1]}",
                 ["Nachbarn addieren"])
    chk(ev(f"({a_}) + ({b_})") == a_ + b_, "Ausdruck ausgewertet")
    return T(f"Berechne: ({a_}) + ({b_})", str(a_ + b_), ["Vorzeichen vergleichen", "Beträge addieren bzw. subtrahieren"])


@reg(("zahlen.ganz", "umkehraufgabe"))
def _(c):
    a_, x_ = c.nz(-30, 30), c.nz(-20, 20)
    k = c.ri(2, 9)
    aufg = [(f"▢ + {kl(a_)} = {a_ + x_}", x_), (f"{a_} − ▢ = {a_ - x_}", x_), (f"{k} · ▢ = {k * x_}", x_), (f"▢ : {k} = {x_}", k * x_)]
    chk(x_ + a_ == a_ + x_ and a_ - x_ == a_ - x_ and (k * x_) // k == x_, "Einsetzprobe")
    return T("Bestimme die fehlende Zahl: " + ";  ".join(t for t, _ in aufg), "; ".join(str(v) for _, v in aufg), ["Umkehraufgabe nutzen"])


@reg(("zahlen.ganz", "sach"), ("zahlen.ganz", "ordnen"), ("zahlen.ganz", "verstehen"), ("zahlen.ganz", "betrag"))
def _(c):
    et = c.z["etappe"]
    if et == "sach":
        t0, d1, d2 = c.ri(-12, -2), c.ri(3, 9), c.ri(2, 15)
        chk(ev(f"({t0}) + {d1+d2} − {2*d1}") == t0 + d1 + d2 - 2 * d1, "Ausdruck ausgewertet")
        return T(f"Morgens zeigt das Thermometer {t0} °C. Bis mittags steigt die Temperatur um {d1+d2} Grad, bis abends fällt sie um {d1*2} Grad. Wie warm ist es abends?",
                 f"{t0+d1+d2-2*d1} °C", [f"{t0} + {d1+d2} = {t0+d1+d2}", f"− {2*d1} = {t0+d1+d2-2*d1}"])
    if et == "ordnen":
        w = sorted({c.nz(-30, 30) for _ in range(6)})
        c.r.shuffle(w)
        chk(sorted(w) == sorted(w, key=lambda v: (v >= 0, abs(v) if v >= 0 else -abs(v))), "Vorzeichen und Betrag")
        return T("Ordne der Größe nach, beginne mit der kleinsten Zahl: " + "; ".join(map(str, w)), " < ".join(map(str, sorted(w))), ["negative Zahlen: größerer Betrag = kleiner"])
    if et == "betrag":
        k = c.ri(3, 6)
        return T(f"Gib alle ganzen Zahlen an, deren Betrag höchstens {k} ist und die kleiner als 2 sind.", "; ".join(str(v) for v in range(-k, 2)), [f"Betrag ≤ {k}: −{k} bis {k}", "davon < 2"])
    return T("Wahr oder falsch? (1) Die Gegenzahl von −7 ist 7. (2) Jede natürliche Zahl ist eine ganze Zahl. (3) −3 ist größer als −1.", "(1) wahr (2) wahr (3) falsch",
             ["Gegenzahl: gleicher Betrag, anderes Vorzeichen", "ℕ ⊂ ℤ", "−3 liegt links von −1"])


# ============================================================ Teilbarkeit
@reg(("zahlen.teilbarkeit", "quersumme"), ("zahlen.teilbarkeit", "neunerregel"), ("zahlen.teilbarkeit", "endziffer"), ("zahlen.teilbarkeit", "vielfache"))
def _(c):
    et = c.z["etappe"]
    if et in ("quersumme", "neunerregel"):
        t_ = 9 if et == "neunerregel" else 3
        if c.has("begründ", "alle karten"):
            k = c.r.sample(range(1, 10), 3)
            while sum(k) % 3:
                k = c.r.sample(range(1, 10), 3)
            return T(f"Aus den Karten {', '.join(map(str, k))} werden dreistellige Zahlen gelegt. Begründe ohne zu rechnen, dass alle durch 3 teilbar sind.", "Quersumme immer " + str(sum(k)),
                     [f"jede Zahl hat die Quersumme {sum(k)}", f"{sum(k)} ist durch 3 teilbar"])
        z_ = gross(c, 4) // 10
        s = str(z_)
        ok = [d for d in range(10) if (sum(map(int, s)) + d) % t_ == 0]
        chk(all(int(s + str(d)) % t_ == 0 for d in ok) and all(int(s + str(d)) % t_ for d in range(10) if d not in ok), "alle Ziffern durchprobiert")
        return T(f"Welche Ziffer kann man für ▢ in {s}▢ einsetzen, damit die Zahl durch {t_} teilbar ist? Gib alle an.", ", ".join(map(str, ok)),
                 [f"Quersumme ohne ▢: {sum(map(int, s))}", f"muss mit ▢ durch {t_} teilbar sein"])
    if et == "endziffer":
        if c.has("regel"):
            return T("Schreibe die Teilbarkeitsregeln für 2, 4, 5 und 10 auf.", "Endziffer gerade; letzte zwei Ziffern durch 4; Endziffer 0 oder 5; Endziffer 0",
                     ["Endstellenregeln"])
        z_ = gross(c, 4)
        chk((z_ // 10 * 10) % 2 == 0 and (z_ // 10 * 10) % 5 == 0, "Teilbarkeit geprüft")
        return T(f"Ersetze die letzte Ziffer von {z_} so, dass die Zahl durch 2 und durch 5 teilbar ist. Welche Teilbarkeitsregel nutzt du?", f"{z_//10}0", ["durch 2 und 5 → durch 10 → Endziffer 0"])
    a_, b_ = c.ch(((3, 4), (4, 6), (6, 8), (5, 6), (4, 10)))
    k = kgv(a_, b_)
    lo = c.ri(40, 90)
    erg = [v for v in range(lo, lo + 2 * k + 1) if v % k == 0]
    if c.has("termin", "pfosten", "gemeinsam", "periode") or c.niv == "III":
        chk(min(t for t in range(1, 1000) if t % a_ == 0 and t % b_ == 0) == k, "kleinstes gemeinsames Vielfaches gesucht")
        return T(f"Ein Bus fährt alle {a_} Minuten, ein anderer alle {b_} Minuten. Um 8:00 Uhr fahren beide gleichzeitig ab. Wann fahren sie das nächste Mal gleichzeitig?",
                 f"nach {k} min, um 8:{k:02d} Uhr" if k < 60 else f"nach {k} min", [f"gemeinsame Vielfache von {a_} und {b_}", f"kleinstes: {k}"])
    chk(erg == [v for v in range(lo, lo + 2 * k + 1) if v % a_ == 0 and v % b_ == 0], "alle Zahlen geprüft")
    return T(f"Gib alle Zahlen zwischen {lo} und {lo+2*k} an, die durch {a_} und durch {b_} teilbar sind.", ", ".join(map(str, erg)), [f"durch beide teilbar ↔ Vielfache von {k}"])


@reg(("L", "ggT zweier Zahlen bestimmen (in der App erst Kl. 6)"))
def _(c):
    g = c.ri(3, 12); a_, b_ = g * c.ri(2, 7), g * c.ri(2, 7)
    while ggt(a_, b_) != g or a_ == b_:
        a_, b_ = g * c.ri(2, 7), g * c.ri(2, 7)
    chk(max(t for t in range(1, a_ + 1) if a_ % t == 0 and b_ % t == 0) == g, "Teiler durchprobiert")
    return T(f"Bestimme den größten gemeinsamen Teiler von {a_} und {b_}.", str(g), [f"Teiler von {a_}: {', '.join(map(str, teiler(a_)))}", f"Teiler von {b_}: {', '.join(map(str, teiler(b_)))}"])


@reg(("L", "Teilbarkeitsregeln begründen (Quersummenregel)"))
def _(c):
    z_ = c.ri(100, 999); h, zz, e = z_ // 100, z_ // 10 % 10, z_ % 10
    return T(f"Begründe am Beispiel {z_}, warum man die Teilbarkeit durch 3 an der Quersumme erkennt.", f"{z_} = {h}·99 + {zz}·9 + ({h}+{zz}+{e})",
             [f"{z_} = {h}·100 + {zz}·10 + {e}", "100 = 99 + 1, 10 = 9 + 1", "99 und 9 sind durch 3 teilbar → nur die Quersumme entscheidet"])


# ============================================================ Potenzen
@reg(("zahlen.potenzen_basis", "sach"), ("zahlen.potenzen_basis", "schreibweise"), ("zahlen.potenzen_basis", "zehner"), ("zahlen.potenzen_basis", "vertauschen"))
def _(c):
    et = c.z["etappe"]
    if et == "sach":
        f_, n_ = c.ch((2, 3, 4)), c.ri(4, 8)
        st = c.ri(1, 5)
        chk(st * f_ ** n_ == st * eval("*".join([str(f_)] * n_)), "Potenz ausmultipliziert")
        return T(f"Eine Nachricht wird von {st} Person{'en' if st>1 else ''} an jeweils {f_} neue Personen weitergeleitet; jede neue Person leitet sie wieder an {f_} weiter. Wie viele Personen erhalten sie in der {n_}. Runde?",
                 fz(st * f_ ** n_), [f"Runde 1: {st*f_}", f"jede Runde ·{f_}", f"{st}·{f_}{hoch(n_)} = {fz(st*f_**n_)}"])
    if et == "zehner":
        z_ = [c.ri(2, 9) * 10 ** c.ri(4, 9) for _ in range(3)]
        return T("Schreibe mit Zehnerpotenz: " + "; ".join(fz(v) for v in z_), "; ".join(f"{str(v)[0]}·10{hoch(len(str(v))-1)}" for v in z_), ["Nullen zählen"])
    if et == "vertauschen":
        a_, b_ = c.ch(((2, 3), (2, 5), (3, 4)))
        return T(f"Stimmt die Behauptung „{a_}{hoch(b_)} = {b_}{hoch(a_)}“? Begründe.", "falsch" if a_ ** b_ != b_ ** a_ else "wahr", [f"{a_}{hoch(b_)} = {a_**b_}", f"{b_}{hoch(a_)} = {b_**a_}"])
    b_, e_ = c.ri(2, 5), c.ri(3, 6)
    if c.has("größte", "vergleich"):
        w = [(f"2{hoch(10)}", 2 ** 10), (f"10{hoch(3)}", 1000), (f"3{hoch(6)}", 729), (f"5{hoch(4)}", 625)]
        return T("Welche Zahl ist am größten? " + ", ".join(s for s, _ in w), "2¹⁰ = 1024", ["alle ausrechnen: 1024, 1000, 729, 625"])
    chk(b_ ** e_ == eval("*".join([str(b_)] * e_)), "Potenz ausmultipliziert")
    return T(f"Schreibe als Potenz mit möglichst kleiner Basis: {b_**e_}", f"{b_}{hoch(e_)}", [f"{b_**e_} = " + "·".join([str(b_)] * e_)])


# ============================================================ Gleichungen
@reg(("gleichungen.einfach", "zwei_schritte"), ("gleichungen.einfach", "waage"))
def _(c):
    x_, k, a_ = c.ri(2, 40), c.ri(2, 9), c.ri(3, 60)
    if c.z["etappe"] == "waage":
        g_ = c.ri(2, 9)
        chk(k * x_ + a_ == k * x_ + a_ and (k * x_ + a_ - a_) % k == 0, "Einsetzprobe")
        return T(f"Auf einer Waage liegen links {k} gleich schwere Päckchen und ein {a_}-g-Gewicht, rechts {k*x_+a_} g. Wie schwer ist ein Päckchen?", f"{x_} g",
                 [f"{k}x + {a_} = {k*x_+a_}", f"beide Seiten −{a_}: {k}x = {k*x_}", f"x = {x_}"])
    if c.has("fehlend", "zeichen", "klammer"):
        chk(ev(f"({x_} + {a_}) · {k}") == (x_ + a_) * k, "Einsetzprobe")
        return T(f"Ergänze die fehlende Zahl: ({x_} + ▢) · {k} = {(x_+a_)*k}", str(a_), [f"{(x_+a_)*k} : {k} = {x_+a_}", f"− {x_} = {a_}"])
    chk(ev(f"{k} · {x_} + {a_}") == k * x_ + a_, "Einsetzprobe")
    return T(f"Löse die Gleichung (Grundmenge ℕ): {k} · x + {a_} = {k*x_+a_}", f"x = {x_}", [f"− {a_}: {k}x = {k*x_}", f": {k}: x = {x_}", f"Probe: {k}·{x_} + {a_} = {k*x_+a_}"])


@reg(("gleichungen.einfach", "aufstellen"))
def _(c):
    x_, k, a_ = c.ri(4, 40), c.ri(2, 6), c.ri(5, 50)
    if c.has("frage", "erfind"):
        chk(ev(f"{k} · {x_} + {a_}") == k * x_ + a_, "Einsetzprobe")
        return T(f"Erfinde eine passende Frage zu: „Ein Kino hat {k} Säle mit gleich vielen Plätzen und zusätzlich {a_} Klappsitze, insgesamt {k*x_+a_} Plätze.“ Löse die zugehörige Gleichung.",
                 f"Wie viele Plätze hat ein Saal? {x_}", [f"{k}·x + {a_} = {k*x_+a_}", f"x = {x_}"])
    if c.niv == "III":
        r_, a2 = c.ri(3, 12), c.ri(2, 8)
        rad = 2 * r_ + 4 * a2
        chk([m for m in range(0, r_ + a2 + 1) if 2 * (r_ + a2 - m) + 4 * m == rad] == [a2], "alle Aufteilungen durchprobiert")
        return T(f"Auf einem Parkplatz stehen {r_+a2} Fahrzeuge: Motorräder (2 Räder) und Autos (4 Räder). Zusammen haben sie {rad} Räder. Wie viele Autos sind es?", str(a2),
                 ["probieren oder: alle wären Motorräder", f"{2*(r_+a2)} Räder, fehlen {rad-2*(r_+a2)}", f"jedes Auto 2 mehr → {a2} Autos"])
    chk(ev(f"{k} · {x_} + {a_}") == k * x_ + a_, "Einsetzprobe")
    return T(f"Ich denke mir eine Zahl, multipliziere sie mit {k} und addiere {a_}. Ich erhalte {k*x_+a_}. Stelle eine Gleichung auf und bestimme die Zahl.", f"{k}·x + {a_} = {k*x_+a_}; x = {x_}",
             ["Gleichung aufstellen", f"x = {x_}"])


@reg(("L", "Ungleichungen über N über die zugehörige Gleichung lösen"), ("L", "Lösungsmenge in einer vorgegebenen Grundmenge bestimmen (Bedingungen prüfen)"))
def _(c):
    k, a_ = c.ri(2, 9), c.ri(3, 40)
    g = c.ri(20, 90)
    grenze = (g - a_) // k
    L_ = [v for v in range(1, grenze + 1) if k * v + a_ < g]
    chk(L_, "Lösungsmenge nicht leer")
    if c.has("gerade"):
        L_ = [v for v in L_ if v % 2 == 0]
    chk(all(k * v + a_ < g for v in L_), "alle Lösungen erfüllen die Ungleichung")
    return T(f"Bestimme alle {'geraden ' if c.has('gerade') else ''}natürlichen Zahlen x (x ≥ 1) mit {k} · x + {a_} < {g}. Löse zuerst die zugehörige Gleichung {k}·x + {a_} = {g}.",
             "{" + "; ".join(map(str, L_)) + "}", [f"Gleichung: x = {fz(F(g-a_,k), dez=True) if endlich(F(g-a_,k)) else fz(F(g-a_,k))}", "kleinere Zahlen erfüllen die Ungleichung", "Lösungen auflisten"])


@reg(("L", "Zahlenfolgen – Bildungsregel erkennen und fortsetzen"))
def _(c):
    v = c.ri(0, 2)
    if v == 0:
        s, d = c.ri(2, 30), c.ri(3, 15)
        f = [s + i * d for i in range(6)]
    elif v == 1:
        s, q = c.ri(1, 5), c.ch((2, 3))
        f = [s * q ** i for i in range(6)]
    else:
        s = c.ri(1, 10)
        f = [s]
        for i in range(1, 6):
            f.append(f[-1] + i)
    zeig = f[:4]
    chk(len(f) == 6, "Folge berechnet")
    return T(f"Setze die Zahlenfolge um zwei Zahlen fort und beschreibe die Regel: {', '.join(map(str, zeig))}, …", f"{f[4]}, {f[5]}",
             ["Unterschiede bzw. Quotienten benachbarter Zahlen prüfen", ["immer +" + str(f[1] - f[0]), "immer ·" + str(f[1] // f[0] if f[0] else 0), "Unterschied wächst um 1"][v]])


@reg(("L", "Wie ändert sich der Termwert, wenn man alle Zahlen gleich verändert?"))
def _(c):
    a_, b_, k = c.ri(200, 900), c.ri(20, 190), c.ri(3, 20)
    if c.has("summe"):
        return T(f"In der Summe {a_} + {b_} wird der erste Summand um {k} größer und der zweite um {k} kleiner. Wie ändert sich die Summe? Begründe ohne zu rechnen.", "gar nicht",
                 [f"+{k} und −{k} heben sich auf"])
    return T(f"In der Differenz {a_} − {b_} werden beide Zahlen um {k} vergrößert. Wie ändert sich das Ergebnis? Begründe ohne zu rechnen.", "gar nicht",
             ["Abstand der Zahlen bleibt gleich", f"({a_}+{k}) − ({b_}+{k}) = {a_} − {b_}"])


@reg(("L", "Sachaufgabe – fehlende Angabe erkennen"))
def _(c):
    k = c.ri(3, 9)
    return T(f"„Eine Klasse fährt mit dem Bus in den Zoo. Der Eintritt kostet {k} € pro Kind. Wie viel muss die Klasse insgesamt zahlen?“ Welche Angabe fehlt, um die Frage zu beantworten?",
             "die Anzahl der Kinder (ggf. Buskosten)", ["Gesamtpreis = Anzahl · Einzelpreis", "Anzahl ist nicht angegeben"])


@reg(("L", "Rechengeschichte zu einer Größenrechnung erfinden"))
def _(c):
    L_, k = c.ri(2, 9) * 6, c.ri(2, 6)
    return T(f"Erfinde eine kurze Sachaufgabe zur Rechnung {L_} m : {k} und löse sie.", f"z. B. Seil in {k} gleich lange Stücke: je {fz(F(L_,k), dez=True)} m", ["Verteilen oder Aufteilen", f"{L_} : {k}"])


@reg(("L", "Summe fortlaufender Zahlen geschickt berechnen (Gauß-Idee)"))
def _(c):
    n_ = c.ch((40, 50, 60, 80, 100, 200))
    chk(sum(range(1, n_ + 1)) == n_ * (n_ + 1) // 2, "Summe direkt addiert")
    return T(f"Berechne geschickt: 1 + 2 + 3 + … + {n_}", str(n_ * (n_ + 1) // 2), [f"Paare bilden: 1 + {n_}, 2 + {n_-1}, … je {n_+1}", f"{n_//2} Paare", f"{n_//2}·{n_+1}"])


@reg(("X", "Wahrscheinlichkeit/Chancen (Gym Kl. 8)"), ("X", "Wahrscheinlichkeit/Zufall (Gym Kl. 8)"))
def _(c):
    if "Zufall" in c.z["vorschlag"]:
        return T("Kann man vorhersagen, welche Zahl beim nächsten Wurf eines fairen Würfels fällt? Begründe.", "nein", ["Zufallsexperiment, jede Zahl gleich wahrscheinlich"])
    r1, g1, r2, g2 = c.ri(1, 4), c.ri(4, 10), c.ri(2, 6), c.ri(8, 16)
    besser = "A" if F(r1, g1) > F(r2, g2) else "B"
    return T(f"Glücksrad A hat {g1} gleich große Felder, davon {r1} Gewinnfelder; Glücksrad B hat {g2} Felder, davon {r2} Gewinnfelder. Bei welchem Rad ist die Gewinnchance größer?",
             besser if F(r1, g1) != F(r2, g2) else "gleich", [f"A: {r1} von {g1}", f"B: {r2} von {g2}", "Anteile vergleichen"])
