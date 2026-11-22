# Generatoren Kl. 8 (und Grundwissen Kl. 7 in BMT8): Terme, Gleichungen, Funktionen
from _kern import *


def lin(m, t, v="x"):
    return (F(m) * P.var(v) + F(t)).fmt()


def gl(l, r):
    return f"{l} = {r}"


# ============================================================ terme.umformen
@reg(("terme.umformen", "zusammenfassen"), ("terme.umformen", "produkte"))
def _(c):
    k = c.r.sample(range(2, 10), 4); s = [c.ch((1, -1)) for _ in range(4)]
    if c.has("produkt") or c.z["etappe"] == "produkte":
        a1, b1 = c.nz(-6, 6), c.ri(2, 5)
        a2, b2 = c.nz(-4, 4), c.ri(2, 6)
        t1 = P.c(a1) * x * (P.c(b1) * y); t2 = P.c(a2) * x * x * (P.c(b2) * x)
        txt = f"Vereinfache die Produkte.\na) {kl(a1)}x · {b1}y   b) {kl(a2)}x² · {b2}x"
        chk(t1.ev(x=2, y=3) == a1 * 2 * b1 * 3, "Einsetzprobe a"); chk(t2.ev(x=2) == a2 * 4 * b2 * 2, "Einsetzprobe b")
        return T(txt, f"a) {t1}   b) {t2}", [f"Zahlen multiplizieren: {a1}·{b1} = {a1*b1}, Variablen dazu: {t1}",
                                                     f"{a2}·{b2} = {a2*b2}, x²·x = x³: {t2}"])
    e = P.c(k[0] * s[0]) * x + P.c(k[1] * s[1]) * y + P.c(k[2] * s[2]) * x + P.c(k[3] * s[3]) * y
    if c.niv != "I":
        e2 = e + P.c(c.nz(-5, 5)) * x * x + P.c(c.nz(-9, 9)) * x * x
        e = e2
    teile = []
    # Term ungeordnet darstellen
    mons = []
    for kk, vv in [(("x", 1), k[0] * s[0]), (("y", 1), k[1] * s[1]), (("x", 1), k[2] * s[2]), (("y", 1), k[3] * s[3])]:
        mons.append(P.c(vv) * P.var(kk[0]))
    if c.niv != "I":
        rest = e - sum(mons, P.c(0))
        for kk, vv in rest.d.items():
            mons.insert(1, P({kk: vv}))
    roh = ""
    for i, m in enumerate(mons):
        s_ = m.fmt()
        roh += s_ if i == 0 else (" − " + s_[1:] if s_.startswith(MINUS) else " + " + s_)
    erg = sum(mons, P.c(0))
    chk(erg.ev(x=3, y=-2) == sum(m.ev(x=3, y=-2) for m in mons), "Einsetzprobe x=3, y=−2")
    return T(f"Vereinfache den Term so weit wie möglich: {roh}", str(erg),
             ["gleichartige Glieder sortieren (x², x, y)", f"zusammenfassen: {erg}"])


@reg(("terme.umformen", "ausmultiplizieren"), ("terme.umformen", "minusklammer"))
def _(c):
    a1, b1, k = c.nz(-6, 6), c.nz(-9, 9), c.nz(2, 6)
    a2, b2 = c.nz(-5, 5), c.nz(-8, 8)
    e1 = P.c(k) * (P.c(a1) * x + b1)
    e2 = -(P.c(a2) * x + b2)
    if c.z["etappe"] == "minusklammer" or c.has("minus", "klammern"):
        m = c.ri(2, 5)
        inner = c.ri(1, 6)
        q = 0
        u = c.nz(-7, 7)
        t = P.c(u) * x - (P.c(a2) * x + b2) + P.c(m) * (x - inner)
        txt = f"{lin(u, 0)} − ({lin(a2, b2)}) + {m}(x − {inner})"
        if c.niv != "I":
            q = c.nz(-3, 3)
            t = t - P.c(q) * x * (x + 1)
            txt += f" − {kl(q)}x(x + 1)"
        chk(t.ev(x=5) == u * 5 - (a2 * 5 + b2) + m * (5 - inner) - (q * 5 * 6 if c.niv != "I" else 0), "Einsetzprobe x = 5")
        return T(f"Löse die Klammern auf und fasse zusammen: {txt}", str(t),
                 ["Minusklammer: alle Vorzeichen in der Klammer umkehren", "Faktor vor der Klammer mit jedem Summanden multiplizieren",
                  f"zusammenfassen: {t}"])
    s = e1 + e2
    txt = f"{k}({lin(a1, b1)}) − ({lin(a2, b2)})"
    chk(s.ev(x=7) == k * (a1 * 7 + b1) - (a2 * 7 + b2), "Einsetzprobe x = 7")
    return T(f"Vereinfache: {txt}", str(s), [f"ausmultiplizieren: {e1} − ({lin(a2, b2)})", f"Minusklammer auflösen, zusammenfassen: {s}"])


@reg(("terme.umformen", "summe_mal_summe"))
def _(c):
    p, q, r, s = c.nz(-7, 7), c.nz(-7, 7), c.ri(2, 4), c.nz(-6, 6)
    e = (x + p) * (P.c(r) * x + s)
    txt = f"({lin(1, p)})({lin(r, s)})"
    if c.niv != "I":
        e = e - (x - 1) * (x + 1); txt += " − (x − 1)(x + 1)"
    chk(e.ev(x=-3) == (-3 + p) * (r * -3 + s) - ((8) if c.niv != "I" else 0), "Einsetzprobe x = −3")
    return T(f"Multipliziere aus und fasse zusammen: {txt}", str(e), ["jedes Glied der ersten Klammer mal jedes Glied der zweiten", f"zusammenfassen: {e}"])


@reg(("terme.umformen", "binomisch"))
def _(c):
    p, k = c.ri(2, 9), c.ri(2, 5)
    if c.has("faktor") or c.niv == "III":
        e = (P.c(k) * x - p) ** 2
        chk(e == P.c(k * k) * x * x - P.c(2 * k * p) * x + p * p, "binomisch rückwärts")
        return T(f"Schreibe als Quadrat einer Differenz: {e}", f"({lin(k, -p)})²",
                 [f"{k*k}x² = ({k}x)², {p*p} = {p}²", f"Mittelglied prüfen: 2·{k}x·{p} = {2*k*p}x", f"also ({lin(k, -p)})²"])
    if c.niv == "I":
        e = (x + p) ** 2
        return T(f"Berechne mit einer binomischen Formel: (x + {p})²", str(e), [f"(a + b)² = a² + 2ab + b² mit a = x, b = {p}", str(e)])
    q = c.ri(2, 7)
    e = (P.c(k) * x + q) ** 2 - (P.c(k) * x - q) * (P.c(k) * x + q)
    chk(e.ev(x=2) == (2 * k + q) ** 2 - (2 * k - q) * (2 * k + q), "Einsetzprobe x = 2")
    return T(f"Vereinfache mit den binomischen Formeln: ({lin(k, q)})² − ({lin(k, -q)})({lin(k, q)})", str(e),
             [f"1. binomische Formel: {(P.c(k)*x+q)**2}", f"3. binomische Formel: {(P.c(k)*x-q)*(P.c(k)*x+q)}", f"Differenz (Klammer!): {e}"])


@reg(("terme.umformen", "ausklammern"))
def _(c):
    g = c.ri(2, 9); u, v = c.nz(-7, 7), c.nz(-9, 9)
    while ggt(u, v) != 1:
        v = c.nz(-9, 9)
    if c.has("dezimal"):
        g = F(c.ri(2, 9), 10)
        e = P.c(g * u) * x + P.c(g * v)
        return T(f"Klammere den Faktor {fd(g)} aus: {e.fmt(dez=True)}", f"{fd(g)}·({lin(u, v)})",
                 [f"{fd(g*u)} : {fd(g)} = {u},  {fd(g*v)} : {fd(g)} = {v}"])
    e = P.c(g * u) * x * y + P.c(g * v) * y
    chk(P.c(g) * y * (P.c(u) * x + v) == e, "Ausmultiplizieren ergibt den Ausgangsterm")
    return T(f"Klammere den größten gemeinsamen Faktor aus: {e}", f"{g}y({lin(u, v)})",
             [f"gemeinsamer Zahlfaktor {g}, gemeinsame Variable y", f"Probe durch Ausmultiplizieren: {e}"])


@reg(("terme.umformen", "aequivalenz"))
def _(c):
    p, q = c.ri(2, 6), c.ri(1, 5)
    t1 = (x + p) * (x - q); t2 = x * x + (p - q) * x - p * q
    if c.niv == "III":
        w = c.ri(1, 5)
        # zwei nicht äquivalente Terme mit gleichem Wert bei x = w
        A = P.c(2) * x + p; B = x + (p + w)
        chk(A.ev(x=w) == B.ev(x=w) and A != B, "gleicher Wert nur an einer Stelle")
        return T(f"Gib zwei Terme mit der Variablen x an, die für x = {w} denselben Wert haben, aber nicht äquivalent sind. Begründe.",
                 f"z. B. {A} und {B}", [f"Wert bei x = {w}: beide {A.ev(x=w)}", f"bei x = 0: {A.ev(x=0)} ≠ {B.ev(x=0)} → nicht äquivalent"])
    chk(t1 == t2, "Ausmultiplizieren")
    return T(f"Zeige, dass die Terme (x + {p})(x − {q}) und {t2} äquivalent sind.", "äquivalent",
             [f"(x + {p})(x − {q}) = x² − {q}x + {p}x − {p*q}", f"= {t1}, also gleich dem zweiten Term"])


# ============================================================ terme.aufstellen
@reg(("terme.aufstellen", "termwert"))
def _(c):
    if c.niv == "III":
        a1, b1 = c.ri(2, 9), c.ri(2, 9)
        w = a1 * b1 + 6
        # Zahl im Term a1·b1 + 6 ersetzen, damit der Wert sich verdoppelt
        neu = 2 * w - 6
        chk(neu / b1 == F(neu, b1), "Rechnung")
        nb = F(2 * w - a1 * b1)
        return T(f"Im Term {a1} · {b1} + 6 soll die Zahl 6 so ersetzt werden, dass sich der Termwert verdoppelt. Welche Zahl musst du einsetzen?",
                 fz(nb), [f"Termwert jetzt {w}, Ziel {2*w}", f"{a1*b1} + z = {2*w} → z = {nb}"])
    w = c.nz(-4, 5); u, v = c.nz(-5, 5), c.nz(-8, 8)
    e = P.c(u) * x * x + P.c(v) * x
    val = e.ev(x=w)
    return T(f"Berechne den Wert des Terms {e} für x = {w}.", fz(val), [f"{kl(u)}·{kl(w)}² + {kl(v)}·{kl(w)}", f"= {fz(u*w*w)} + {kl(v*w)} = {fz(val)}"])


@reg(("terme.aufstellen", "uebersetzen"))
def _(c):
    k, m = c.ri(2, 6), c.ri(2, 9)
    e = P.c(k) * (x + m) - x
    return T(f"Addiere zu einer Zahl x die Zahl {m}, multipliziere die Summe mit {k} und subtrahiere danach die Zahl x. Schreibe als Term und vereinfache.",
             f"{k}(x + {m}) − x = {e}", [f"Term: {k}(x + {m}) − x", f"vereinfacht: {e}"])


@reg(("terme.aufstellen", "sachsituation"))
def _(c):
    a_, b_ = c.ri(2, 6), c.ri(1, 4)
    # L-förmige Figur: Rechteck (x+a_) × x ohne Quadrat b_×b_
    fl = (x + a_) * x - b_ * b_
    um = 2 * (x + a_) + 2 * x
    if c.has("umfang"):
        return T(f"Ein Rechteck ist x cm breit und {a_} cm länger als breit. An einer Ecke wird ein Quadrat mit {b_} cm Seitenlänge ausgeschnitten.\n"
                 f"Gib einen Term für den Umfang der Restfigur an und vereinfache.", f"u = {um} (cm)",
                 ["Das Ausschneiden an der Ecke ändert den Umfang nicht (zwei Kanten verschoben)", f"u = 2(x + {a_}) + 2x = {um}"])
    chk(fl.ev(x=10) == (10 + a_) * 10 - b_ * b_, "Einsetzprobe x = 10")
    return T(f"Ein Rechteck ist x cm breit und {a_} cm länger als breit. An einer Ecke wird ein Quadrat mit {b_} cm Seitenlänge ausgeschnitten.\n"
             f"Gib einen Term für den Flächeninhalt der Restfigur an und vereinfache.", f"A = {fl} (cm²)",
             [f"Rechteck: (x + {a_})·x", f"minus Quadrat {b_*b_} cm²", f"A = {fl}"])


@reg(("terme.aufstellen", "deuten"))
def _(c):
    gp, pr = c.ri(3, 12), c.ri(2, 9)
    e = f"{gp} + {pr}·n"
    return T(f"Ein Fahrradverleih berechnet den Preis in Euro mit dem Term {e}; n ist die Anzahl der Tage.\n"
             f"Erkläre, was die Zahlen {gp} und {pr} im Sachzusammenhang bedeuten, und berechne den Preis für {c.ri(3,7)} Tage.",
             f"{gp} € Grundgebühr, {pr} € je Tag", [f"{gp}: fester Betrag, unabhängig von der Dauer", f"{pr}·n: {pr} € pro Tag", "Preis: Einsetzen von n"])


@reg(("terme.aufstellen", "muster"))
def _(c):
    k, s = c.ri(3, 6), c.ri(1, 4)
    # Figur n besteht aus k*n + s Hölzern
    werte = [(nn, k * nn + s) for nn in range(1, 4)]
    N = c.ri(20, 60)
    if c.has("begründ", "formel"):
        return T(f"Für ein Geländer aus n Feldern braucht man {k}n + {s} Stäbe (Figur 1: {werte[0][1]}, Figur 2: {werte[1][1]}, …). Begründe die Formel an der Figur.",
                 f"je Feld {k} Stäbe, dazu {s} am Anfang", [f"jedes neue Feld bringt {k} Stäbe", f"{s} Stäbe gehören zum Abschluss/Start", f"also {k}n + {s}"])
    if c.has("passend", "teilbar", "ohne rest", "anzahl"):
        lo = c.ri(90, 110)
        ok = [m for m in range(lo, lo + 15) if (m - s) % k == 0 and m > s]
        return T(f"Ein Geländer braucht {k}n + {s} Stäbe (n Felder). Welche Stabzahlen zwischen {lo} und {lo+14} gehen genau auf? Begründe.",
                 ", ".join(map(str, ok)), [f"Stabzahl − {s} muss durch {k} teilbar sein", "Zahlen prüfen"])
    return T(f"Eine Folge von Figuren wird aus Hölzern gelegt. Figur 1 hat {werte[0][1]}, Figur 2 hat {werte[1][1]}, Figur 3 hat {werte[2][1]} Hölzer; "
             f"jede neue Figur bekommt gleich viele Hölzer dazu.\nGib einen Term für die Anzahl der Hölzer in Figur n an und berechne die Anzahl für Figur {N}.",
             f"{k}n + {s}; Figur {N}: {k*N+s}", [f"Zuwachs je Figur: {k}", f"Startwert: {werte[0][1]} − {k} = {s}", f"{k}·{N} + {s} = {k*N+s}"])


@reg(("L", "Mit Termen beweisen (gerade/ungerade, Teilbarkeit)"))
def _(c):
    m = c.ch((2, 3, 4))
    if m == 2:
        return T("Beweise: Die Summe aus einer ungeraden Zahl und der nächstgrößeren ungeraden Zahl ist immer durch 4 teilbar.",
                 "(2n + 1) + (2n + 3) = 4n + 4 = 4(n + 1)", ["ungerade Zahl: 2n + 1, nächste: 2n + 3", "Summe 4n + 4 = 4(n + 1) → Vielfaches von 4"])
    k = c.ri(3, 5)
    return T(f"Beweise: Die Summe von {k} aufeinanderfolgenden natürlichen Zahlen ist durch {k if k % 2 else k//2} teilbar.",
             "Term und Faktor", [f"Zahlen n, n+1, …, n+{k-1}", f"Summe {k}n + {k*(k-1)//2}",
                                 f"= {k}(n + {(k-1)//2})" if k % 2 else f"= {k//2}(2n + {k-1})"])


@reg(("L", "Rechengeschichte zu einem Term erfinden"))
def _(c):
    a_, b_ = c.ri(3, 9), c.ri(12, 40)
    return T(f"Erfinde eine kurze Sachaufgabe, die zum Term {b_} − {a_}·x passt, und erkläre die Bedeutung von x.",
             "z. B. Guthaben/Restbetrag", [f"z. B.: {b_} € Guthaben, jeder Kinobesuch kostet {a_} €, x = Anzahl der Besuche", "Term gibt den Rest an"])


@reg(("L", "Tabellenkalkulation – Formel aufstellen/ergänzen"), ("L", "Tabellenkalkulation – Formeln lesen und Fehler finden"))
def _(c):
    w = [c.ri(2, 30) for _ in range(4)]
    if c.has("fehler"):
        return T(f"In den Zellen B2 bis B5 stehen die Werte {', '.join(map(str, w))}. In B6 soll der Mittelwert stehen; eingetragen ist =B2+B3+B4+B5/4.\n"
                 "Erkläre den Fehler und gib eine richtige Formel an.", "=(B2+B3+B4+B5)/4",
                 ["Punkt vor Strich: nur B5 wird durch 4 geteilt", f"richtig: =(B2+B3+B4+B5)/4 → {fz(F(sum(w),4), dez=True)}"])
    p = c.ri(2, 9)
    return T(f"In einer Tabellenkalkulation steht in A2 eine Stückzahl, in B2 der Stückpreis {p} €. In C2 soll der Gesamtpreis mit 10 % Rabatt stehen.\n"
             f"Gib eine passende Formel an und berechne den Wert für A2 = {w[0]}.", f"=A2*B2*0,9 → {fd(F(w[0]*p*9,10))} €",
             [f"Gesamt ohne Rabatt: {w[0]}·{p} = {w[0]*p}", f"mal 0,9: {fd(F(w[0]*p*9,10))}"])


# ============================================================ terme.bruchterme
@reg(("terme.bruchterme", "definitionsmenge"))
def _(c):
    p, q = c.nz(-6, 6), c.nz(-6, 6)
    while q == p:
        q = c.nz(-6, 6)
    return T(f"Gib alle Zahlen an, die man für x in den Term (x + 2) / ((x {'−' if p>0 else '+'} {abs(p)})(x {'−' if q>0 else '+'} {abs(q)})) nicht einsetzen darf, und begründe.",
             f"x = {p} und x = {q}", ["Nenner darf nicht 0 sein", f"Produkt 0, wenn x − ({p}) = 0 oder x − ({q}) = 0", f"D = ℚ \\ {{{p}; {q}}}"])


@reg(("terme.bruchterme", "kuerzen"))
def _(c):
    p, k = c.ri(1, 7), c.ri(2, 6)
    zt = P.c(k) * x * x - P.c(k * p * p); nt = P.c(k) * x + P.c(k * p)
    erg = x - p
    for w in (10, -3, F(1, 2)):
        if w != -p:
            chk(zt.ev(x=w) / nt.ev(x=w) == erg.ev(x=w), f"Einsetzprobe x = {w}")
    return T(f"Gib die Definitionsmenge an und kürze so weit wie möglich: ({zt}) / ({nt})", f"D = ℚ \\ {{{-p}}};  {erg}",
             [f"Zähler: {k}(x² − {p*p}) = {k}(x − {p})(x + {p})", f"Nenner: {k}(x + {p})", f"kürzen: x − {p} (für x ≠ {-p})"])


@reg(("terme.bruchterme", "addieren"))
def _(c):
    p = c.ri(1, 6)
    # 1/(x-p) - 1/(x+p) = 2p/(x²-p²)
    for w in (p + 1, -p - 2, 0 if p else 1):
        chk(F(1, w - p) - F(1, w + p) == F(2 * p, w * w - p * p), f"Einsetzprobe x = {w}")
    return T(f"Fasse zu einem Bruchterm zusammen: 1/(x − {p}) − 1/(x + {p})", f"{2*p} / (x² − {p*p})",
             [f"Hauptnenner (x − {p})(x + {p}) = x² − {p*p}", f"Zähler: (x + {p}) − (x − {p}) = {2*p}", f"Ergebnis {2*p}/(x² − {p*p}), x ≠ ±{p}"])


@reg(("terme.bruchterme", "multiplizieren"))
def _(c):
    p, k = c.ri(1, 6), c.ri(2, 5)
    # (x²-p²)/(kx) : (x+p)/(k²) = k(x-p)/x
    for w in (p + 2, 7):
        lhs = F(w * w - p * p, k * w) / F(w + p, k * k)
        chk(lhs == F(k * (w - p), w), f"Einsetzprobe x = {w}")
    return T(f"Vereinfache: (x² − {p*p}) / ({k}x)  :  (x + {p}) / {k*k}", f"{k}(x − {p}) / x",
             ["mit dem Kehrwert multiplizieren", f"x² − {p*p} = (x − {p})(x + {p})", f"kürzen → {k}(x − {p})/x (x ≠ 0, x ≠ {-p})"])


@reg(("terme.bruchterme", "termwert"))
def _(c):
    w = c.ri(2, 9); p = c.ri(1, 5)
    v = F(w * w - 1, w + p)
    return T(f"Berechne den Wert des Terms (x² − 1)/(x + {p}) für x = {w}. Gib das Ergebnis als gekürzten Bruch an.", fz(v),
             [f"Zähler {w*w-1}, Nenner {w+p}", f"= {fz(v)}"])


@reg(("terme.bruchterme", "fehler_finden"))
def _(c):
    nn = c.ri(2, 5)
    # Muster: 1/k - 1/(k+1) = 1/(k(k+1))
    bsp = "; ".join(f"1/{k} − 1/{k+1} = 1/{k*(k+1)}" for k in range(nn, nn + 3))
    for k in range(1, 20):
        chk(F(1, k) - F(1, k + 1) == F(1, k * (k + 1)), "Muster für k = 1…19")
    return T(f"Setze das Muster fort und schreibe es allgemein als Gleichung mit n: {bsp}; … Weise die Gleichung durch Umformen nach.",
             "1/n − 1/(n + 1) = 1/(n(n + 1))", ["Hauptnenner n(n + 1)", "Zähler (n + 1) − n = 1"])


# ============================================================ Potenzen
@reg(("terme.potenzgesetze_ganzzahlig", "gleiche_basis_ganz"), ("terme.potenzgesetze_ganzzahlig", "exponent_und_potenz"),
     ("terme.potenzgesetze_ganzzahlig", "terme_vereinfachen"), ("terme.potenzgesetze_natuerlich", "mal_gleiche_basis"))
def _(c):
    et = c.z["etappe"]
    if et == "mal_gleiche_basis":
        p, q, k = c.ri(2, 6), c.ri(2, 5), c.ri(2, 5)
        return T(f"Vereinfache: {k}a{hoch(p)} · {k+1}a{hoch(q)} · a", f"{k*(k+1)}a{hoch(p+q+1)}",
                 [f"Zahlen: {k}·{k+1} = {k*(k+1)}", f"Exponenten addieren: {p} + {q} + 1 = {p+q+1}"])
    if et == "gleiche_basis_ganz":
        b_, e_ = c.ri(2, 5), -c.ri(1, 3)
        v = F(1, b_ ** (-e_))
        return T(f"Schreibe ohne negativen Exponenten und berechne: {b_}{hoch(e_)}", fz(v), [f"{b_}{hoch(e_)} = 1/{b_}{hoch(-e_)} = {fz(v)}"])
    if et == "exponent_und_potenz":
        p, q = c.ri(2, 4), -c.ri(1, 3)
        return T(f"Vereinfache und schreibe ohne negativen Exponenten: (x{hoch(p)}){hoch(q)} · x{hoch(-q*p+1)}", "x",
                 [f"(x^{p})^{q} = x{hoch(p*q)}", f"x{hoch(p*q)} · x{hoch(-q*p+1)} = x¹"])
    p, q, r = c.ri(2, 6), c.ri(2, 6), c.ri(1, 4)
    k = c.ri(2, 9)
    e = p + q - r - (q + 1)
    erg = f"{k}" + (f"a{hoch(e)}" if e not in (0, 1) else ("a" if e == 1 else ""))
    neg = f"a{hoch(-e)}" if e < 0 else ""
    los = f"{k}/{('a' + hoch(-e)) if -e != 1 else 'a'}" if e < 0 else erg
    return T(f"Vereinfache und gib das Ergebnis ohne negative Exponenten an: ({k*2}a{hoch(p)} · a{hoch(q)}) / (2a{hoch(r)} · a{hoch(q+1)})",
             los, [f"Zahlen: {k*2} : 2 = {k}", f"Exponent: {p} + {q} − {r} − {q+1} = {e}", f"Ergebnis {los}"])


# ============================================================ gleichungen.linear
def lin_gleichung(c, klammern=False):
    s = F(c.nz(-9, 9)) if c.niv == "I" else F(c.nz(-12, 12), c.ch((1, 1, 2, 4)))
    a1, a2 = c.nz(-9, 9), c.nz(-9, 9)
    while a1 == a2:
        a2 = c.nz(-9, 9)
    if klammern:
        k = c.ri(2, 5); p = c.nz(-6, 6); m = c.ri(2, 4); q = c.nz(-5, 5)
        lhs = P.c(k) * (x + p) - P.c(m) * (x - q)
        rl = lhs.ev(x=s)
        r1 = c.nz(-4, 4)
        while r1 == k - m:
            r1 = c.nz(-4, 4)
        r0 = rl - r1 * s
        rhs = P.c(r1) * x + r0
        txt = f"{k}(x {'+' if p>0 else '−'} {abs(p)}) − {m}(x {'−' if q>0 else '+'} {abs(q)}) = {rhs.fmt(dez=True)}"
    else:
        b1 = c.nz(-20, 20)
        lhs = P.c(a1) * x + b1
        b2 = lhs.ev(x=s) - a2 * s
        rhs = P.c(a2) * x + b2
        txt = gl(lhs.fmt(dez=True), rhs.fmt(dez=True))
    erg = loese_linear(lhs, rhs)
    chk(erg == s and lhs.ev(x=s) == rhs.ev(x=s), f"Probe: beide Seiten {fz(lhs.ev(x=s), dez=True)}")
    return txt, lhs, rhs, s


@reg(("gleichungen.linear", "beide_seiten"), ("gleichungen.linear", "klammern"))
def _(c):
    txt, lhs, rhs, s = lin_gleichung(c, klammern=c.z["etappe"] == "klammern")
    d = lhs - rhs
    return T(f"Löse die Gleichung (Grundmenge ℚ): {txt}", f"x = {fz(s, dez=True)}",
             [f"Klammern auflösen/ordnen: {lhs.fmt(dez=True)} = {rhs.fmt(dez=True)}", f"x-Glieder auf eine Seite: {d.fmt(dez=True)} = 0",
              f"x = {fz(s, dez=True)}", "Probe: Einsetzen ergibt auf beiden Seiten denselben Wert"])


@reg(("gleichungen.linear", "sach"))
def _(c):
    a_ = c.ri(3, 9); d_ = c.ri(2, 6); u = 2 * (2 * a_ + d_) * 1
    # Rechteck: Länge = Breite + d_, Umfang u -> Breite
    u = c.ri(30, 80) * 2
    while (u // 2 - d_) % 2:
        d_ = c.ri(2, 9)
    b0 = F(u // 2 - d_, 2)
    chk(2 * (b0 + b0 + d_) == u, "Umfang nachgerechnet")
    return T(f"Ein rechteckiges Beet ist {d_} m länger als breit. Sein Umfang beträgt {u} m. Stelle eine Gleichung auf und berechne Länge und Breite.",
             f"Breite {fz(b0, dez=True)} m, Länge {fz(b0+d_, dez=True)} m", [f"2(x + x + {d_}) = {u}", f"4x + {2*d_} = {u}", f"x = {fz(b0, dez=True)}"])


@reg(("gleichungen.linear", "sonderfaelle"))
def _(c):
    k, p = c.ri(2, 6), c.nz(-6, 6)
    if c.has("allgemeingültig", "lücke"):
        return T(f"Ergänze die Lücke so, dass die Gleichung für alle x erfüllt ist: {k}(x + {p}) = {k}x + ▢", fz(k * p),
                 [f"{k}(x + {p}) = {k}x + {k*p}", f"▢ = {k*p}"])
    q = c.nz(-9, 9)
    return T(f"Für welchen Wert des Parameters a hat die Gleichung a·x + {q} = {k}x − {abs(q)+1} keine Lösung? Begründe.", f"a = {k}",
             [f"für a = {k} fällt x weg: {q} = {-(abs(q)+1)} ist falsch", "für alle anderen a genau eine Lösung"])


@reg(("L", "Zahl in einer Gleichung so wählen, dass eine vorgegebene Lösung entsteht"))
def _(c):
    a1, b1, s = c.ri(2, 7), c.nz(-9, 9), c.nz(-5, 5)
    rhs = a1 * s + b1
    # Ersetze b1 durch z so, dass x = s2
    s2 = c.nz(-6, 6)
    while s2 == s:
        s2 = c.nz(-6, 6)
    z = rhs - a1 * s2
    chk(a1 * s2 + z == rhs, "Probe")
    return T(f"In der Gleichung {a1}x + {kl(b1)} = {rhs} soll die Zahl {b1} so durch eine andere Zahl ersetzt werden, dass x = {s2} die Lösung ist. Welche Zahl?",
             fz(z), [f"x = {s2} einsetzen: {a1}·{kl(s2)} + z = {rhs}", f"z = {rhs} − {kl(a1*s2)} = {z}"])


@reg(("L", "Ein Produkt ist null (Satz vom Nullprodukt)"))
def _(c):
    p, q = c.nz(-7, 7), c.nz(-7, 7)
    k = c.ri(2, 5)
    return T(f"Bestimme die Lösungsmenge: (x {'−' if p>0 else '+'} {abs(p)}) · ({k}x {'+' if q>0 else '−'} {abs(q)}) = 0",
             f"L = {{{p}; {fz(F(-q,k))}}}", ["Ein Produkt ist 0, wenn ein Faktor 0 ist", f"x = {p} oder {k}x = {-q} → x = {fz(F(-q,k))}"])


# ============================================================ gleichungen.bruch
@reg(("gleichungen.bruch", "ein_bruch"), ("gleichungen.bruch", "definitionsmenge"))
def _(c):
    s = c.nz(-6, 8); p = c.nz(-5, 5)
    while s + p == 0:
        p = c.nz(-5, 5)
    k = c.nz(-6, 6)
    rhs = F(k, s + p)
    num = k
    if c.z["etappe"] == "definitionsmenge":
        return T(f"Begründe, warum x = {-p} nicht zur Definitionsmenge der Gleichung {num}/(x {'+' if p>0 else '−'} {abs(p)}) = 2 gehört.", f"Nenner wird 0",
                 [f"x = {-p} eingesetzt: Nenner {-p} + {kl(p)} = 0", "Division durch 0 nicht definiert"])
    chk(F(num, s + p) == rhs, "Probe")
    return T(f"Gib die Definitionsmenge an und löse: {num}/(x {'+' if p>0 else '−'} {abs(p)}) = {fz(rhs)}", f"D = ℚ \\ {{{-p}}}; x = {s}",
             [f"Nenner ≠ 0 → x ≠ {-p}", f"mit (x {'+' if p>0 else '−'} {abs(p)}) multiplizieren: {num} = {fz(rhs)}·(x + {kl(p)})", f"x = {s}, liegt in D"])


@reg(("gleichungen.bruch", "hauptnenner"))
def _(c):
    s = c.nz(-6, 9)
    if c.niv == "III":
        p = c.ri(1, 6)
        while abs(s) == p:
            s = c.nz(-6, 9)
        cc = 2 * s
        chk(F(1, s - p) + F(1, s + p) == F(cc, s * s - p * p), "Probe")
        return T(f"Bestimme die Definitionsmenge und löse: 1/(x − {p}) + 1/(x + {p}) = {cc}/(x² − {p*p})",
                 f"D = ℚ \\ {{−{p}; {p}}}; x = {s}", [f"x² − {p*p} = (x − {p})(x + {p}) ist Hauptnenner", f"(x + {p}) + (x − {p}) = {cc}",
                                                    f"2x = {cc} → x = {s} ∈ D"])
    p, q = c.nz(-5, 5), c.nz(-5, 5)
    while p == q or s + p == 0 or s + q == 0:
        p, q = c.nz(-5, 5), c.nz(-5, 5)
    k = c.ch((1, -1, 2))
    A, B = k * (s + q), k * (s + p)
    # Gleichung A/(x+q) = B/(x+p)  -> A(x+p) = B(x+q)
    chk(F(A, s + q) == F(B, s + p), "Probe: beide Seiten gleich")
    chk(A != B, "eindeutige Lösung")
    return T(f"Bestimme die Definitionsmenge und löse: {A}/(x {'+' if q>0 else '−'} {abs(q)}) = {B}/(x {'+' if p>0 else '−'} {abs(p)})",
             f"D = ℚ \\ {{{-q}; {-p}}}; x = {s}", [f"Hauptnenner (x + {kl(q)})(x + {kl(p)})", f"{A}(x + {kl(p)}) = {B}(x + {kl(q)})",
                                                f"{A-B}x = {B*q - A*p} → x = {s}", "x liegt in D"])


@reg(("gleichungen.bruch", "scheinloesung"))
def _(c):
    p = c.ri(1, 6)
    return T(f"Löse: x/(x − {p}) = {p}/(x − {p})  und gib die Lösungsmenge an.", "L = { }",
             [f"D = ℚ \\ {{{p}}}", f"mal (x − {p}): x = {p}", f"{p} ∉ D → keine Lösung"])


@reg(("gleichungen.bruch", "verhaeltnis"))
def _(c):
    a_, b_ = c.ri(2, 9), c.ri(2, 9)
    return T(f"Zwei Strecken stehen im Verhältnis {a_} : {b_}. Die längere ist x cm, die kürzere {min(a_,b_)*3} cm lang. Stelle eine passende Verhältnisgleichung auf und löse.",
             f"x = {fz(F(max(a_,b_)*min(a_,b_)*3, min(a_,b_)))}", [f"x : {min(a_,b_)*3} = {max(a_,b_)} : {min(a_,b_)}", f"x = {max(a_,b_)}·3 = {max(a_,b_)*3}"])


@reg(("gleichungen.bruch", "graphisch"))
def _(c):
    r1, r2 = -c.ri(1, 4), c.ri(1, 5)
    t = -(r1 + r2); k = -r1 * r2
    for r in (r1, r2):
        chk(F(k, r) == r + t, f"Schnitt bei x = {r}")
    return T(f"Die Graphen von f(x) = {k}/x und g(x) = {lin(1, t)} schneiden sich. Erkläre, was die x-Werte der Schnittpunkte für die Gleichung {k}/x = {lin(1,t)} bedeuten, "
             f"und prüfe rechnerisch, dass x = {r1} und x = {r2} Lösungen sind.", f"L = {{{r1}; {r2}}}",
             ["Schnittstellen = Stellen mit f(x) = g(x) = Lösungen der Gleichung", f"x = {r1}: {fz(F(k,r1))} = {r1 + t}", f"x = {r2}: {fz(F(k,r2))} = {r2 + t}"])


@reg(("L", "Bruchgleichung aus einem Text über Zähler und Nenner aufstellen"))
def _(c):
    z_, n_ = c.ri(2, 7), c.ri(8, 15)
    while ggt(z_, n_) != 1:
        n_ += 1
    # Zähler und Nenner um gleiche Zahl x vergrößern → Wert a/b
    xs = c.ri(2, 9)
    w = F(z_ + xs, n_ + xs)
    chk(F(z_ + xs, n_ + xs) == w, "Probe")
    return T(f"Zähler und Nenner des Bruchs {z_}/{n_} werden um dieselbe Zahl x vergrößert. Der neue Bruch hat den Wert {fz(w)}. Stelle eine Gleichung auf und bestimme x.",
             f"({z_} + x)/({n_} + x) = {fz(w)}; x = {xs}", [f"({z_} + x)·{w.denominator} = {w.numerator}·({n_} + x)", f"x = {xs}"])


# ============================================================ gleichungen.formeln
@reg(("gleichungen.formeln", "ein_schritt"), ("gleichungen.formeln", "geometrie"))
def _(c):
    v = c.ch(("dreieck", "rechteck", "trapez", "kreis"))
    if c.has("dreieck") or v == "dreieck":
        g_, A_ = c.ri(4, 12), c.ri(10, 60)
        h_ = F(2 * A_, g_)
        return T(f"Stelle die Formel A = ½·g·h nach h um und berechne h für A = {A_} cm² und g = {g_} cm.", f"h = 2A/g = {fd(h_) if endlich(h_) else fz(h_)} cm",
                 ["beide Seiten mal 2, dann durch g", f"h = 2·{A_}/{g_}"])
    if c.has("umfang") or v == "rechteck":
        u_, a0 = c.ri(20, 60), c.ri(3, 9)
        return T(f"Stelle die Umfangsformel u = 2a + 2b eines Rechtecks nach b um und berechne b für u = {u_} cm, a = {a0} cm.", f"b = (u − 2a)/2 = {fd(F(u_-2*a0,2))} cm",
                 ["−2a, dann :2", f"b = ({u_} − {2*a0})/2"])
    a0, c0, A_ = c.ri(4, 10), c.ri(2, 6), c.ri(20, 80)
    h_ = F(2 * A_, a0 + c0)
    return T(f"Stelle die Trapezformel A = ½(a + c)·h nach h um und berechne h für A = {A_} cm², a = {a0} cm, c = {c0} cm.",
             f"h = 2A/(a + c) = {fz(h_, dez=True)} cm", [f"h = 2·{A_}/({a0}+{c0})"])


@reg(("gleichungen.formeln", "zwei_schritte"), ("gleichungen.formeln", "einsetzen"))
def _(c):
    # Temperatur: F = 1,8·C + 32
    if c.has("umrechnung", "steigung") or c.ch((0, 1)):
        Fw = c.ri(50, 104)
        C = F(Fw - 32) / F(9, 5)
        return T(f"Die Formel f = 1,8·c + 32 rechnet Grad Celsius c in Grad Fahrenheit f um. Stelle nach c um und berechne c für f = {Fw}.",
                 f"c = (f − 32)/1,8 ≈ {gerundet(C, 1)} °C", ["−32", ":1,8", f"({Fw} − 32)/1,8"])
    v0, s0 = c.ri(30, 90), c.ri(10, 60)
    t_ = F(s0 * 60, v0)
    return T(f"Für eine Fahrt gilt s = v·t (s in km, v in km/h, t in h). Stelle nach t um und berechne die Fahrzeit in Minuten für s = {s0} km und v = {v0} km/h.",
             f"t = s/v = {fz(F(s0,v0))} h = {fd(t_) if endlich(t_) else gerundet(t_,1)} min", ["durch v teilen", f"{s0}/{v0} h · 60"])


@reg(("gleichungen.formeln", "pruefen"))
def _(c):
    return T("Für einen Zylinder gilt V = π·r²·h. Kreuze alle richtigen Umformungen an: (A) h = V/(π·r²)  (B) r² = V·π·h  (C) π = V/(r²·h)  (D) r = V/(π·h)",
             "A und C", ["A: durch πr² geteilt – richtig", "B: falsch (müsste geteilt werden)", "C: richtig", "D: falsch, es fehlt die Wurzel"])


# ============================================================ gleichungen.lgs2
def lgs(c):
    sx, sy = c.nz(-6, 7), c.nz(-6, 7)
    while True:
        a1, b1, a2, b2 = c.nz(-5, 5), c.nz(-5, 5), c.nz(-5, 5), c.nz(-5, 5)
        if a1 * b2 - a2 * b1 != 0:
            break
    c1, c2 = a1 * sx + b1 * sy, a2 * sx + b2 * sy
    chk(a1 * sx + b1 * sy == c1 and a2 * sx + b2 * sy == c2, "Probe in beiden Gleichungen")
    return (a1, b1, c1, a2, b2, c2, sx, sy)


def lgs_txt(a1, b1, c1):
    return f"{(P.c(a1)*x + P.c(b1)*y)} = {c1}"


@reg(("gleichungen.lgs2", "verfahren"), ("gleichungen.lgs2", "addition"))
def _(c):
    a1, b1, c1, a2, b2, c2, sx, sy = lgs(c)
    v = "Additionsverfahren" if c.z["etappe"] == "addition" else "einem Verfahren deiner Wahl"
    return T(f"Löse das Gleichungssystem mit {v}:\n  I  {lgs_txt(a1,b1,c1)}\n  II {lgs_txt(a2,b2,c2)}", f"L = {{({sx} | {sy})}}",
             [f"eine Variable eliminieren (z. B. I·{a2} − II·{a1})", f"y = {sy}", f"einsetzen: x = {sx}", "Probe in beiden Gleichungen"])


@reg(("gleichungen.lgs2", "loesbarkeit"))
def _(c):
    a1, b1 = c.nz(-5, 5), c.nz(-5, 5); c1 = c.ri(1, 9); k = c.ri(2, 3)
    return T(f"Gegeben ist die Gleichung {lgs_txt(a1,b1,c1)}. Gib eine zweite Gleichung an, sodass das Gleichungssystem keine Lösung hat. Begründe.",
             f"z. B. {lgs_txt(k*a1, k*b1, k*c1+1)}", [f"linke Seite das {k}-Fache, rechte Seite nicht → Widerspruch", "Geraden parallel, kein Schnittpunkt"])


@reg(("gleichungen.lgs2", "sachaufgabe"))
def _(c):
    p1, p2 = c.ri(2, 6), c.ri(7, 12); n1, n2 = c.ri(5, 20), c.ri(5, 20)
    ges, summe = n1 + n2, n1 * p1 + n2 * p2
    chk(n1 * p1 + n2 * p2 == summe and n1 + n2 == ges, "Probe")
    return T(f"Ein Kiosk verkauft kleine Becher zu {p1} € und große zu {p2} €. An einem Tag wurden {ges} Becher für insgesamt {summe} € verkauft.\n"
             "Stelle ein Gleichungssystem auf und bestimme die Anzahl jeder Sorte.", f"{n1} kleine, {n2} große",
             [f"I x + y = {ges}", f"II {p1}x + {p2}y = {summe}", f"y = {n2}, x = {n1}"])


# ============================================================ gleichungen.ungleichungen
@reg(("gleichungen.ungleichungen", "klammern"), ("gleichungen.ungleichungen", "pruefen"), ("gleichungen.ungleichungen", "umdrehen"),
     ("gleichungen.ungleichungen", "grafisch"), ("gleichungen.ungleichungen", "sachaufgabe"))
def _(c):
    et = c.z["etappe"]
    if et == "umdrehen":
        return T("Nenne zwei Umformungen, die bei Gleichungen und Ungleichungen gleich funktionieren, und die Besonderheit bei Ungleichungen.",
                 "Addieren/Subtrahieren, Multiplizieren mit positiver Zahl; bei negativer Zahl Zeichen umdrehen",
                 ["gleiche Zahl addieren/subtrahieren", "mit positiver Zahl multiplizieren/dividieren", "mal negative Zahl: < wird >"])
    if et == "pruefen":
        k = c.ri(2, 6)
        return T(f"Gilt die Ungleichung x² + {k} > {2}x für alle rationalen Zahlen x? Begründe.", "ja",
                 [f"x² − 2x + {k} = (x − 1)² + {k-1}", f"(x − 1)² ≥ 0, also Summe ≥ {k-1} > 0"])
    if et == "sachaufgabe":
        g_, p_, b_ = c.ri(5, 15), c.ri(2, 6), c.ri(40, 90)
        n_ = (b_ - g_) // p_
        return T(f"Ein Ausflug kostet {g_} € Grundbetrag und {p_} € je Fahrt. Wie viele Fahrten sind höchstens möglich, wenn höchstens {b_} € ausgegeben werden dürfen? Beschreibe dein Vorgehen.",
                 f"höchstens {n_} Fahrten", [f"{g_} + {p_}·n ≤ {b_}", f"n ≤ {fz(F(b_-g_,p_), dez=True)}", f"größte natürliche Zahl: {n_}"])
    if et == "grafisch":
        m_, t_ = c.nz(-3, 3), c.nz(-6, 6)
        ns = F(-t_, m_)
        rel = "x ≥" if m_ > 0 else "x ≤"
        return T(f"Für welche x ist f(x) = {lin(m_, t_)} nicht negativ? Begründe mithilfe des Graphen.", f"{rel} {fz(ns)}",
                 [f"Nullstelle x = {fz(ns)}", "Steigung " + ("positiv" if m_ > 0 else "negativ"), f"Graph über der x-Achse für {rel} {fz(ns)}"])
    k = c.ri(2, 5); p = c.nz(-6, 6); m = c.nz(-6, 6)
    while k == m:
        m = c.nz(-6, 6)
    q = c.nz(-9, 9)
    lhs = P.c(k) * (x + p); rhs = P.c(m) * x + q
    gr = loese_linear(lhs, rhs)
    rel = "<" if k - m > 0 else ">"
    chk((lhs - rhs).ev(x=gr - 1) * (1 if rel == "<" else -1) < 0, "Testwert erfüllt")
    return T(f"Löse die Ungleichung: {k}(x {'+' if p>0 else '−'} {abs(p)}) < {rhs}", f"x {rel} {fz(gr)}",
             [f"{lhs} < {rhs}", f"{k-m}x < {q - k*p}", ("durch " + str(k - m) + (" (negativ: Zeichen umdrehen)" if k - m < 0 else "")), f"x {rel} {fz(gr)}"])


@reg(("L", "Lösungsmenge eines Ungleichungssystems grafisch darstellen"))
def _(c):
    m1, t1 = c.ri(1, 3), c.nz(-3, 3)
    return T(f"Stelle die Lösungsmenge des Systems y ≤ {lin(m1, t1)} und y ≥ 0 und x ≤ 4 im Koordinatensystem dar.",
             "Dreieck/Viereck unter der Geraden, über der x-Achse, links von x = 4",
             [f"Gerade y = {lin(m1, t1)} zeichnen, Bereich darunter", "Bereich oberhalb der x-Achse", "links von x = 4; Schnittfläche markieren"])


# ============================================================ funktionen.linear
@reg(("funktionen.linear", "zwei_punkte"), ("funktionen.linear", "einsetzen"))
def _(c):
    m_ = F(c.nz(-4, 4), c.ch((1, 2)))
    t_ = c.nz(-6, 6)
    x1, x2 = c.ri(-4, 0), c.ri(1, 6)
    if (m_ * x1).denominator != 1:
        x1 -= 1
    if (m_ * x2).denominator != 1:
        x2 += 1
    y1, y2 = m_ * x1 + t_, m_ * x2 + t_
    if c.z["etappe"] == "einsetzen":
        A_ = c.ri(4, 12)
        # Gerade y = m x + 4 schneidet Achsen: Dreieck Fläche ½·4·|4/m| = A → m = ±8/A
        mm = F(8, A_)
        chk(F(1, 2) * 4 * (4 / mm) == A_, "Fläche nachgerechnet")
        return T(f"Die Gerade y = −m·x + 4 (m > 0) bildet mit den Koordinatenachsen ein Dreieck. Bestimme m so, dass das Dreieck den Flächeninhalt {A_} hat.",
                 f"m = {fz(mm)}", ["Nullstelle x = 4/m", "A = ½·4·(4/m) = 8/m", f"8/m = {A_} → m = {fz(mm)}"])
    chk((y2 - y1) / (x2 - x1) == m_ and y1 - m_ * x1 == t_, "Steigung und Achsenabschnitt aus beiden Punkten")
    return T(f"Bestimme die Gleichung der Geraden durch A({x1} | {fz(y1)}) und B({x2} | {fz(y2)}).", f"y = {lin(m_, t_)}",
             [f"m = ({fz(y2)} − {kl(y1)}) / ({x2} − {kl(x1)}) = {fz(m_)}", f"t aus A: {fz(y1)} = {fz(m_)}·{kl(x1)} + t → t = {t_}"])


@reg(("funktionen.linear", "graph_ablesen"), ("funktionen.linear", "ablesen"))
def _(c):
    m_ = F(c.nz(-3, 3), c.ch((1, 2, 3))); t_ = c.nz(-4, 4)
    pts = [(xx, m_ * xx + t_) for xx in range(-3, 6) if (m_ * xx + t_).denominator == 1][:3]
    if c.z["etappe"] == "ablesen" or c.has("ablesen"):
        return T(f"Eine Gerade geht durch die Gitterpunkte {', '.join(f'({px} | {fz(py)})' for px, py in pts)}. Lies Steigung und y-Achsenabschnitt ab und gib die Gleichung an.",
                 f"m = {fz(m_)}, t = {t_}; y = {lin(m_, t_)}", ["Steigungsdreieck zwischen zwei Gitterpunkten", f"Schnitt mit y-Achse bei {t_}"])
    return T(f"Zeichne den Graphen von y = {lin(m_, t_)} in ein Koordinatensystem (1 LE = 1 cm).", f"Gerade durch {', '.join(f'({px}|{fz(py)})' for px, py in pts[:2])}",
             [f"y-Achsenabschnitt {t_} markieren", f"Steigungsdreieck: {m_.denominator} nach rechts, {abs(m_.numerator)} nach {'oben' if m_>0 else 'unten'}", "Gerade zeichnen"])


@reg(("funktionen.linear", "lage"))
def _(c):
    m_, t_ = c.nz(-4, 4), c.nz(-5, 5); px, py = c.nz(-4, 4), c.nz(-5, 5)
    t2 = py - m_ * px
    chk(m_ * px + t2 == py, "Punkt liegt auf der Parallelen")
    return T(f"Gib die Gleichung der Parallelen zu g: y = {lin(m_, t_)} durch P({px} | {py}) an und bestimme ihre Achsenschnittpunkte.",
             f"y = {lin(m_, t2)}; S_y(0 | {t2}), N({fz(F(-t2,m_))} | 0)", ["gleiche Steigung", f"t aus P: {py} = {m_}·{kl(px)} + t → t = {t2}", f"Nullstelle x = {fz(F(-t2,m_))}"])


@reg(("funktionen.linear", "proportional"))
def _(c):
    k = c.ri(2, 9)
    return T(f"Entscheide für f(x) = {k}x und g(x) = {k}x + {c.ri(1,5)}, welche Funktion eine direkte Proportionalität beschreibt, und begründe am Term und am Graphen.",
             "f", ["f: Form y = m·x, Graph durch den Ursprung", "g: zusätzlicher y-Achsenabschnitt, nicht durch den Ursprung"])


@reg(("funktionen.linear", "schnittpunkte"))
def _(c):
    sx, sy = c.nz(-4, 5), c.nz(-4, 5)
    m1, m2 = c.nz(-3, 3), c.nz(-3, 3)
    while m1 == m2:
        m2 = c.nz(-3, 3)
    t1, t2 = sy - m1 * sx, sy - m2 * sx
    chk(m1 * sx + t1 == m2 * sx + t2, "beide Geraden durch S")
    return T(f"Berechne den Schnittpunkt der Geraden g: y = {lin(m1, t1)} und h: y = {lin(m2, t2)}.", f"S({sx} | {sy})",
             ["gleichsetzen", f"{m1-m2}x = {t2-t1} → x = {sx}", f"y = {sy}"])


@reg(("funktionen.linear", "deuten"), ("funktionen.linear", "wirkung"))
def _(c):
    v0, ab = c.ri(200, 500), c.ri(5, 25)
    tt = F(v0, ab)
    if c.z["etappe"] == "wirkung":
        return T(f"Ein Tank enthält {v0} Liter; pro Minute fließen {ab} Liter ab: V(t) = {v0} − {ab}t. Wie ändert sich der Term, wenn nur halb so viel pro Minute abfließt? Nach welcher Zeit ist der Tank dann leer?",
                 f"V(t) = {v0} − {fd(F(ab,2))}t; {fz(2*tt, dez=True)} min", ["Steigung halbiert", f"0 = {v0} − {fd(F(ab,2))}t → t = {fz(2*tt, dez=True)}"])
    return T(f"Ein Wassertank enthält zu Beginn {v0} Liter; pro Minute fließen {ab} Liter ab.\n"
             f"a) Gib einen Funktionsterm für das Volumen V(t) an (t in min).\nb) Erkläre die Bedeutung von Steigung und y-Achsenabschnitt.\nc) Nach welcher Zeit ist der Tank leer?",
             f"V(t) = {v0} − {ab}t; leer nach {fz(tt, dez=True) if endlich(tt) else gerundet(tt,1)} min",
             [f"V(t) = {v0} − {ab}t", f"Steigung −{ab}: Abnahme pro Minute; {v0}: Anfangsvolumen", f"0 = {v0} − {ab}t → t = {fz(tt, dez=True) if endlich(tt) else gerundet(tt,1)}"])


@reg(("L", "Gerade an einer Achse spiegeln und Gleichung angeben"))
def _(c):
    m_, t_ = c.nz(-4, 4), c.nz(-5, 5)
    return T(f"Die Gerade g: y = {lin(m_, t_)} wird an der x-Achse gespiegelt. Gib die Gleichung der Bildgeraden an.", f"y = {lin(-m_, -t_)}",
             ["Spiegelung an der x-Achse: y-Werte wechseln das Vorzeichen", f"y = −({lin(m_, t_)})"])


# ============================================================ funktionen.grundbegriffe
@reg(("funktionen.grundbegriffe", "eindeutig"))
def _(c):
    return T("Entscheide, ob die Zuordnung „Schüler einer Klasse → Geburtsmonat“ eine Funktion ist, und ob die umgekehrte Zuordnung „Monat → Schüler“ eine Funktion ist. Begründe.",
             "erste ja, zweite nein", ["jedem Schüler genau ein Monat → Funktion", "zu einem Monat können mehrere oder kein Schüler gehören → keine Funktion"])


@reg(("funktionen.grundbegriffe", "funktionswert"), ("funktionen.grundbegriffe", "stelle"))
def _(c):
    m_, t_ = c.ri(2, 9), c.ri(10, 60)
    if c.z["etappe"] == "stelle":
        y0 = c.ri(80, 200)
        s_ = F(y0 - t_, m_)
        return T(f"In ein Becken mit {t_} Litern laufen pro Minute {m_} Liter: f(t) = {m_}t + {t_}. Nach welcher Zeit sind {y0} Liter im Becken?",
                 f"t = {fz(s_, dez=True) if endlich(s_) else gerundet(s_,1)} min", [f"{m_}t + {t_} = {y0}", f"t = {fz(s_)}"])
    w = c.ri(3, 12)
    return T(f"Berechne den Funktionswert von f(x) = {m_}x + {t_} an der Stelle x = {w}.", fz(m_ * w + t_), [f"{m_}·{w} + {t_} = {m_*w+t_}"])


@reg(("funktionen.grundbegriffe", "wertetabelle"))
def _(c):
    m_, t_ = c.nz(-3, 3), c.nz(-4, 4)
    xs = [-2, -1, 0, 1, 2, 3]
    return T(f"Ergänze die Wertetabelle von f(x) = {lin(m_, t_)} für x = −2; −1; 0; 1; 2; 3 und zeichne den Graphen.",
             "; ".join(f"f({xx}) = {m_*xx+t_}" for xx in xs), ["Werte einsetzen", "Punkte eintragen und verbinden"])


@reg(("funktionen.grundbegriffe", "nullstellen"))
def _(c):
    m_, ns = c.nz(-4, 4), c.nz(-5, 5)
    t_ = -m_ * ns
    return T(f"Berechne die Nullstelle und den Schnittpunkt mit der y-Achse von f(x) = {lin(m_, t_)}.", f"x = {ns}; S_y(0 | {t_})",
             [f"{lin(m_, t_)} = 0 → x = {ns}", f"f(0) = {t_}"])


@reg(("funktionen.grundbegriffe", "punkt_graph"))
def _(c):
    m_, t_ = c.nz(-3, 3), c.nz(-5, 5); px = c.nz(-4, 4); py = m_ * px + t_ + c.ch((-2, -1, 1, 2))
    lage = "oberhalb" if py > m_ * px + t_ else "unterhalb"
    return T(f"Liegt der Punkt P({px} | {py}) oberhalb, unterhalb oder auf dem Graphen von f(x) = {lin(m_, t_)}? Begründe rechnerisch.", lage,
             [f"f({px}) = {m_*px+t_}", f"{py} {'>' if lage=='oberhalb' else '<'} {m_*px+t_} → {lage}"])


@reg(("funktionen.grundbegriffe", "graph_lesen"))
def _(c):
    pts = [(0, c.ri(0, 2)), (2, c.ri(5, 7)), (4, c.ri(1, 2)), (6, c.ri(5, 7)), (8, c.ri(0, 2))]
    yy = c.ri(3, 4)
    st = []
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        if (y1 - yy) * (y2 - yy) < 0:
            st.append(x1 + F(yy - y1, y2 - y1) * (x2 - x1))
    for sx in st:
        chk(min(p[1] for p in pts) <= yy, "Schnitt im Bereich")
    return T(f"Ein Graph verbindet die Punkte {' – '.join(f'({px}|{py})' for px, py in pts)} geradlinig. An wie vielen Stellen hat die Funktion den Wert {yy}? Gib die Stellen an.",
             f"{len(st)} Stellen: " + "; ".join(f"x = {fd(sx) if endlich(sx) else '≈ ' + gerundet(sx,1)}" for sx in st),
             ["waagrechte Linie y = " + str(yy) + " einzeichnen", "auf jedem steigenden/fallenden Teilstück schneiden", "x-Werte durch Verhältnis bestimmen"])


@reg(("funktionen.grundbegriffe", "mengen"))
def _(c):
    p = c.ri(1, 6)
    return T(f"Gib jeweils die maximale Definitionsmenge an: f(x) = {c.ri(2,9)}x − 1;  g(x) = 1/(x − {p});  h(x) = 3/x²", f"D_f = ℚ; D_g = ℚ \\ {{{p}}}; D_h = ℚ \\ {{0}}",
             ["f: keine Einschränkung", f"g: Nenner ≠ 0 → x ≠ {p}", "h: x ≠ 0"])


# ============================================================ funktionen.gebrochen
@reg(("funktionen.gebrochen", "definitionsmenge"), ("funktionen.gebrochen", "achsenpunkte"), ("funktionen.gebrochen", "asymptoten"),
     ("funktionen.gebrochen", "parameter"), ("funktionen.gebrochen", "beurteilen"))
def _(c):
    k, p, q = c.nz(-6, 6), c.nz(-4, 4), c.nz(-3, 3)
    et = c.z["etappe"]
    txt_f = f"f(x) = {k}/(x {'−' if p>0 else '+'} {abs(p)}) {'+' if q>0 else '−'} {abs(q)}"
    ns = p - F(k, q)
    if et == "definitionsmenge":
        if c.has("angeben", "lücke"):
            return T(f"Gib einen Bruchterm an, der genau für x = {p} und x = {p+2} nicht definiert ist.", f"z. B. 1/((x − {p})(x − {p+2}))",
                     ["Nenner muss genau an diesen Stellen 0 werden"])
        return T(f"Gib die maximale Definitionsmenge von {txt_f} an.", f"D = ℚ \\ {{{p}}}", [f"Nenner x − ({p}) = 0 für x = {p}"])
    if et == "achsenpunkte":
        chk(F(k) / (ns - p) + q == 0, "f(Nullstelle) = 0")
        return T(f"Berechne die Nullstelle von {txt_f}.", f"x = {fz(ns)}", [f"{k}/(x − {kl(p)}) = {-q}", f"x − {kl(p)} = {fz(F(-k,q))}", f"x = {fz(ns)}"])
    if et == "asymptoten":
        if c.niv == "III":
            return T(f"Gib einen Funktionsterm an, dessen Graph die senkrechte Asymptote x = {p} und die waagrechte Asymptote y = {q} hat.",
                     f"z. B. f(x) = 1/(x {plusminus(-p)}) {plusminus(q)}", ["Nenner null bei x = " + str(p), "Summand " + str(q) + " verschiebt nach oben/unten"])
        return T(f"Gib alle Asymptoten des Graphen von {txt_f} an.", f"x = {p}; y = {q}", ["senkrecht: Nennernullstelle", "waagrecht: für große |x| geht der Bruch gegen 0"])
    if et == "parameter":
        return T(f"Beschreibe, wie der Graph von {txt_f} aus dem Graphen von y = 1/x entsteht, und skizziere ihn.",
                 f"Streckung um {abs(k)}{', Spiegelung an der x-Achse' if k<0 else ''}, {abs(p)} nach {'rechts' if p>0 else 'links'}, {abs(q)} nach {'oben' if q>0 else 'unten'}",
                 [f"Faktor {k}", f"x − {kl(p)}: Verschiebung in x-Richtung", f"{kl(q)}: Verschiebung in y-Richtung"])
    # beurteilen
    m_ = c.ri(1, 3)
    return T(f"Entscheide, ob der Graph von {txt_f} durch den Punkt P({p+1} | {k+q}) verläuft, und begründe.", "ja",
             [f"f({p+1}) = {k}/1 + {kl(q)} = {k+q}"])


# ============================================================ groessen.indirekt
@reg(("groessen.indirekt", "dreisatz"), ("groessen.indirekt", "produkt"), ("groessen.indirekt", "erkennen"), ("groessen.indirekt", "graph"),
     ("groessen.indirekt", "unterscheiden"))
def _(c):
    et = c.z["etappe"]
    n1 = c.ri(3, 8); n2 = c.ri(2, 12, ohne=(n1,)); t1 = n2 * c.ri(2, 5)
    t2 = F(n1 * t1, n2)
    if et == "erkennen":
        return T("Eine feste Strecke wird mit unterschiedlicher Geschwindigkeit gefahren. Welcher Zusammenhang besteht zwischen Geschwindigkeit und Fahrzeit? Begründe.",
                 "indirekt proportional", ["doppelte Geschwindigkeit → halbe Zeit", "Produkt v·t = Strecke bleibt gleich"])
    if et == "unterscheiden":
        w = [(1, 36), (2, 18), (3, 12), (4, 9)]
        return T(f"Prüfe, ob die Wertetabelle x: 1; 2; 3; 4 und y: 36; 18; 12; 9 eine direkte oder indirekte Proportionalität beschreibt.", "indirekt",
                 ["Produkte x·y: alle 36", "Quotienten nicht gleich → nicht direkt"])
    if et == "graph":
        return T("Ein Mitschüler behauptet: „Der Graph einer indirekten Proportionalität ist eine fallende Gerade.“ Nimm Stellung.", "falsch",
                 ["Graph ist eine Hyperbel (y = k/x)", "z. B. k = 12: (1|12), (2|6), (3|4) liegen nicht auf einer Geraden"])
    if et == "produkt":
        k = n1 * t1
        return T(f"Ein Rechteck hat den Flächeninhalt {k} cm². Ergänze die Tabelle der möglichen Seitenlängen a = 1, 2, 3, 4, 6 cm und gib die Formel b(a) an.",
                 f"b = {k}/a: " + ", ".join(f"{fz(F(k,aa), dez=True)}" for aa in (1, 2, 3, 4, 6)), [f"a·b = {k} konstant", f"b = {k}/a"])
    chk(n2 * t2 == n1 * t1, "Produkt konstant")
    return T(f"{n1} Helfer brauchen für das Aufstellen der Stühle {t1} Minuten. Wie lange brauchen {n2} Helfer bei gleichem Arbeitstempo?",
             f"{fz(t2, dez=True)} min", [f"1 Helfer: {n1*t1} min", f"{n2} Helfer: {n1*t1}/{n2} = {fz(t2, dez=True)} min"])
