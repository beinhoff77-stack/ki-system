T = "terme.potenzgesetze_natuerlich"
R = "rr.potenz"
# ───────── mal_gleiche_basis ─────────
neu(T, "mal_gleiche_basis", "anwenden", Z(
    "Aus einer Zelle entstehen durch 4 Teilungen 2⁴ Zellen. Jede dieser Zellen teilt sich danach noch 5-mal weiter. Wie viele Zellen sind es nach den insgesamt 9 Teilungen?",
    512, "2 ** 4 * 2 ** 5", "2 ** 9", "Bei jeder Teilung verdoppelt sich die Zahl der Zellen. Wie oft wird insgesamt mit 2 malgenommen?",
    "Erst gibt es 2⁴ = 16 Zellen. Jede teilt sich 5-mal weiter: 2⁵ = 32 Zellen aus einer. Insgesamt 2⁴ · 2⁵ = 2⁹ = 512 Zellen. Gleiche Basis beim Malnehmen: die Hochzahlen addieren.",
    [B("2 ** 20", "die Hochzahlen malgenommen statt addiert", "fb.potenz.hochzahlen_malgenommen"), B("2 * 9", "die Basis mit der Hochzahl malgenommen", "fb.potenz.basis_mal_hochzahl"), B("4 ** 9", "die Basen malgenommen statt beibehalten")], einheit="Zellen"), g="einkleidung", regel=R)
neu(T, "mal_gleiche_basis", "fehler_detektiv", FD(
    "Kim soll 3⁴ · 3² vereinfachen und schreibt auf:",
    [("Bei beiden Faktoren ist die Basis 3, also gleich.", True, True),
     ("Bei gleicher Basis werden die Hochzahlen malgenommen.", False, True),
     ("Also ist 3⁴ · 3² = 3⁸.", 4 * 2 == 8, 4 * 2 == 8)],
    "Was geschieht mit den Hochzahlen, wenn zwei Potenzen mit gleicher Basis malgenommen werden? Schreibe 3⁴ · 3² einmal als Faktoren aus.",
    "3⁴ · 3² = (3 · 3 · 3 · 3) · (3 · 3) hat 6 Faktoren 3, also 3⁶. Die Hochzahlen werden addiert, nicht malgenommen. Der Fehler steckt in Zeile 2. Zeile 3 rechnet mit der falschen Regel richtig weiter."), g="fehler", regel=R)
neu(T, "mal_gleiche_basis", "lueckenweg", L(
    "Du vereinfachst das Produkt 3³ · 3² · 3². Die Basis 3 bleibt stehen, die Hochzahlen werden verrechnet. Das Ergebnis ist die Potenz 3^①. Der Wert dieser Potenz ist ②.",
    "① = □; ② = □", [7, 2187], ["3 + 2 + 2", "3 ** {1}"], ["7", "2187"],
    "Gleiche Basis beim Malnehmen: Was passiert mit den Hochzahlen? Rechne danach die Potenz aus.",
    "Die Hochzahlen werden addiert: 3 + 2 + 2 = 7. Also ist das Produkt 3⁷. Ausgerechnet: 3⁷ = 2 187.",
    {0: [(12, "fb.potenz.hochzahlen_malgenommen", "die Hochzahlen malgenommen", "3 * 2 * 2")], 1: [(21, "fb.potenz.basis_mal_hochzahl", "die Basis mit der Hochzahl malgenommen", "3 * {1}")]}), g="direkt", regel=R)
# ───────── gleicher_exponent ─────────
neu(T, "gleicher_exponent", "anwenden", Z(
    "Das Volumen eines Würfels mit der Kante a ist a³. Ein Würfel hat die Kante 4 m, ein zweiter die Kante 25 m. Wie groß ist das Produkt der beiden Volumen (in m⁶)?",
    1000000, "(4 * 25) ** 3", "4 ** 3 * 25 ** 3", "Beide Volumen haben die gleiche Hochzahl. Fasse zuerst die Basen zusammen, bevor du ausrechnest.",
    "Die Volumen sind 4³ und 25³. Gleicher Exponent: 4³ · 25³ = (4 · 25)³ = 100³ = 1 000 000 m⁶.",
    [B("100 ** 6", "die Hochzahlen addiert, obwohl sie gleich bleiben"), B("29 ** 3", "die Basen addiert statt malgenommen"), B("100 * 3", "die Basis mit der Hochzahl malgenommen", "fb.potenz.basis_mal_hochzahl")], einheit="m⁶"), g="einkleidung", regel=R)
neu(T, "gleicher_exponent", "verfahren_waehlen", W(
    "Du sollst 2⁵ · 5⁵ im Kopf ausrechnen. Welcher Weg ist am geschicktesten?",
    "Gleiche Hochzahl: (2 · 5)⁵ = 10⁵ = 100 000.",
    [("Gleiche Hochzahl: 2 · 5 = 10 und 5 + 5 = 10, also 10¹⁰.", "die Hochzahlen addiert, obwohl sie beim Zusammenfassen der Basen gleich bleiben"), ("Erst 2⁵ = 32 und 5⁵ = 3 125 ausrechnen und dann 32 · 3 125 schriftlich rechnen.", "ein umständlicher, fehleranfälliger Weg statt der Basen zusammenzufassen"),
     ("Gleiche Basis gibt es nicht, also lässt sich nichts vereinfachen.", "nur auf gleiche Basen geachtet")],
    "Prüfe zuerst: Welche Zahlen sind bei beiden Faktoren gleich, die Basen oder die Hochzahlen?",
    "Beide Potenzen haben die Hochzahl 5. Dann gilt aⁿ · bⁿ = (a · b)ⁿ: 2⁵ · 5⁵ = (2 · 5)⁵ = 10⁵ = 100 000. Das geht im Kopf.",
    lambda: 2 ** 5 * 5 ** 5 == 10 ** 5 == 100000 and 10 ** 10 != 100000), g="mehrschritt", regel=R)
neu(T, "gleicher_exponent", "umkehren", Z(
    "Für welche natürliche Zahl im Kästchen gilt 14⁴ = 2⁴ · □⁴ ?",
    7, "14 // 2", 7, "Bei gleicher Hochzahl werden die Basen malgenommen. Welche Zahl ergibt mit 2 zusammen die Basis 14?",
    "Nach dem Gesetz aⁿ · bⁿ = (a · b)ⁿ muss 2 · □ = 14 gelten. Also ist □ = 7. Probe: 2⁴ · 7⁴ = 16 · 2 401 = 38 416 = 14⁴.",
    [B("14 - 2", "die Basen subtrahiert statt geteilt"), B("14 ** 4 - 2 ** 4", "die Hochzahl 4 mitgerechnet und die Potenzen subtrahiert"), B("14 + 2", "die Basen addiert statt geteilt")]), g="rueckwaerts", regel=R)
# ───────── potenz_von_potenz ─────────
neu(T, "potenz_von_potenz", "anwenden", Z(
    "Jede Person, die einen Kettenbrief bekommt, schickt ihn an 2³ neue Personen weiter. Die erste Person verschickt ihn in Runde 1. In Runde 4 bekommen (2³)⁴ Personen den Brief neu. Wie viele Personen sind das?",
    4096, "(2 ** 3) ** 4", "8 ** 4", "Die Potenz 2³ wird noch einmal hoch 4 genommen. Wie viele Faktoren 2 sind das zusammen?",
    "(2³)⁴ = 2³ · 2³ · 2³ · 2³ = 2¹² = 4 096. Bei einer Potenz von einer Potenz werden die Hochzahlen malgenommen: 3 · 4 = 12.",
    [B("2 ** 7", "die Hochzahlen addiert statt malgenommen"), B("2 * 3 * 4", "Basis und Hochzahlen malgenommen", "fb.potenz.basis_mal_hochzahl"), B("8 * 4", "die Zahl 8 mit der Hochzahl 4 malgenommen")], einheit="Personen"), g="einkleidung", regel=R)
neu(T, "potenz_von_potenz", "bruecke", W(
    "Kim soll (x²)³ vereinfachen. Welche Aussage beschreibt die Potenz richtig?",
    "x⁶, denn x² steht dreimal als Faktor da: x² · x² · x² hat zusammen 6 Faktoren x.",
    [("x⁵, denn bei einer Potenz von einer Potenz werden die Hochzahlen addiert.", "die Hochzahlen addiert"), ("x⁹, denn es sind 3 Faktoren mit jeweils 3 Faktoren x.", "Hochzahl und Faktorzahl verwechselt")],
    "Schreibe (x²)³ als Produkt: Wie oft steht der Faktor x² da? Aus wie vielen Faktoren x besteht jeder davon?",
    "(x²)³ = x² · x² · x². Jedes x² besteht aus 2 Faktoren x, es gibt 3 davon: zusammen 2 · 3 = 6 Faktoren. Also (x²)³ = x⁶.",
    lambda: 2 * 3 == 6 and 2 + 3 == 5 and 3 * 3 == 9), g="darstellung", regel=R)
neu(T, "potenz_von_potenz", "umkehren", Z(
    "Für welche Hochzahl n gilt (5ⁿ)⁴ = 5²⁴?",
    6, "24 // 4", 6, "Wie hängen die Hochzahlen n, 4 und 24 bei einer Potenz von einer Potenz zusammen?",
    "Bei (5ⁿ)⁴ werden die Hochzahlen malgenommen: n · 4 = 24. Also ist n = 24 : 4 = 6. Probe: (5⁶)⁴ = 5²⁴.",
    [B("24 - 4", "die Hochzahlen subtrahiert statt geteilt"), B("24 * 4", "die Hochzahlen malgenommen statt geteilt"), B("24 + 4", "die Hochzahlen addiert")]), g="rueckwaerts", regel=R)
# ───────── geteilt_gleiche_basis ─────────
neu(T, "geteilt_gleiche_basis", "anwenden", Z(
    "In einem Hafenlager stehen 5⁶ Bananenkisten. Ein Lkw nimmt bei jeder Fahrt 5⁴ Kisten mit. Wie viele Fahrten sind nötig, bis das Lager leer ist?",
    25, "5 ** 6 // 5 ** 4", "5 ** (6 - 4)", "Gesucht ist, wie oft 5⁴ in 5⁶ passt. Teile die beiden Potenzen mit gleicher Basis.",
    "Gesucht ist 5⁶ : 5⁴. Bei gleicher Basis subtrahiert man die Hochzahlen: 6 − 4 = 2. Also 5² = 25 Fahrten.",
    [B("6 / 4", "die Hochzahlen geteilt statt subtrahiert"), B("5 ** 10", "die Hochzahlen addiert statt subtrahiert"), B("2", "nur die Differenz der Hochzahlen angegeben und die Potenz nicht ausgerechnet")], einheit="Fahrten"), g="einkleidung", regel=R)
neu(T, "geteilt_gleiche_basis", "fehler_detektiv", FD(
    "Alex soll 7⁹ : 7⁴ berechnen und schreibt auf:",
    [("Die Basis ist gleich, also werden die Hochzahlen subtrahiert.", True, True),
     ("Es gilt 9 − 4 = 5, also ist 7⁹ : 7⁴ = 7⁵.", 9 - 4 == 5, True),
     ("Ausgerechnet ist 7⁵ = 7 · 5 = 35.", 7 * 5 == 7 ** 5, 7 * 5 == 35)],
    "Was bedeutet 7⁵? Schreibe es als Produkt aus Faktoren.",
    "7⁵ = 7 · 7 · 7 · 7 · 7 = 16 807. Die Hochzahl sagt, wie oft die Basis als Faktor vorkommt; man rechnet nicht Basis mal Hochzahl. Der Fehler steckt in Zeile 3. Die Zeilen 1 und 2 sind richtig."), g="fehler", regel=R)
neu(T, "geteilt_gleiche_basis", "lueckenweg", L(
    "Du berechnest 4⁷ : 4⁵ Schritt für Schritt. Erst vereinfachst du zu einer einzigen Potenz mit der Basis 4: Das ist 4^①. Dann rechnest du diese Potenz aus: ②.",
    "① = □; ② = □", [2, 16], ["7 - 5", "4 ** {1}"], ["2", "16"],
    "Bei gleicher Basis beim Teilen werden die Hochzahlen verrechnet. Wie? Die Basis bleibt.",
    "Teilen mit gleicher Basis: Die Hochzahlen werden subtrahiert, 7 − 5 = 2. Also 4⁷ : 4⁵ = 4². Ausgerechnet: 4² = 16.",
    {0: [(12, None, "die Hochzahlen addiert", "7 + 5"), (35, "fb.potenz.basis_mal_hochzahl", "die Hochzahlen malgenommen", "7 * 5")], 1: [(8, "fb.potenz.basis_mal_hochzahl", "die Basis mit der Hochzahl malgenommen", "4 * {1}")]}), g="direkt", regel=R)
# ───────── anwenden ─────────
neu(T, "anwenden", "anwenden", Z(
    "Beim Reisfeld-Spiel liegt auf Feld 1 ein Korn, auf jedem nächsten Feld doppelt so viele wie auf dem Feld davor. Auf Feld 11 liegen 2¹⁰ Körner, auf Feld 7 liegen 2⁶ Körner. Wie oft ist die Zahl der Körner auf Feld 7 in der Zahl auf Feld 11 enthalten?",
    16, "2 ** 10 // 2 ** 6", "2 ** 4", "Gesucht ist ein Quotient. Beide Zahlen sind Potenzen von 2.",
    "Gesucht ist 2¹⁰ : 2⁶. Gleiche Basis beim Teilen: Hochzahlen subtrahieren, 10 − 6 = 4. Also 2⁴ = 16. Auf Feld 11 liegen 16-mal so viele Körner wie auf Feld 7.",
    [B("2 ** 16", "die Hochzahlen addiert statt subtrahiert"), B("4", "die Differenz der Hochzahlen angegeben, ohne die Potenz auszurechnen"), B("2 * 4", "die Basis mit der Hochzahl malgenommen", "fb.potenz.basis_mal_hochzahl")]), g="mehrschritt", regel=R)
neu(T, "anwenden", "verfahren_waehlen", W(
    "Eines dieser Produkte lässt sich mit keinem Potenzgesetz zu einer einzigen Potenz zusammenfassen. Welches?",
    "2⁵ · 3⁴", [("2⁵ · 2⁴", "hat gleiche Basis"), ("2⁵ · 3⁵", "hat gleiche Hochzahl"), ("(2⁵)⁴", "ist eine Potenz von einer Potenz")],
    "Prüfe bei jedem Produkt: Sind die Basen gleich, oder sind die Hochzahlen gleich, oder steckt eine Potenz in einer Potenz?",
    "2⁵ · 2⁴ = 2⁹ (gleiche Basis). 2⁵ · 3⁵ = 6⁵ (gleiche Hochzahl). (2⁵)⁴ = 2²⁰. Bei 2⁵ · 3⁴ sind Basen und Hochzahlen verschieden, hier hilft kein Potenzgesetz.",
    lambda: 2 ** 5 * 2 ** 4 == 2 ** 9 and 2 ** 5 * 3 ** 5 == 6 ** 5 and (2 ** 5) ** 4 == 2 ** 20 and 2 ** 5 * 3 ** 4 not in (2 ** 9, 6 ** 5, 6 ** 4)), g="pruefung", regel=R)
neu(T, "anwenden", "anwenden", Z(
    "Eine Rechenmaschine soll (2⁴ · 2⁵)² : 2¹⁰ berechnen, ohne die Potenzen einzeln auszurechnen. Welches Ergebnis ist richtig?",
    256, "(2 ** 4 * 2 ** 5) ** 2 // 2 ** 10", "2 ** ((4 + 5) * 2 - 10)", "Fasse zuerst die Klammer zusammen. Dann nimm die Potenz von der Potenz und teile am Ende.",
    "Klammer: 2⁴ · 2⁵ = 2⁹. Potenz von einer Potenz: (2⁹)² = 2¹⁸. Teilen: 2¹⁸ : 2¹⁰ = 2⁸ = 256.",
    [(0.5, None, "das Quadrat vergessen: 2⁹ : 2¹⁰ ergibt einen Bruch", "2 ** (9 - 10)"), B("2 ** 28", "beim Teilen die Hochzahlen addiert statt subtrahiert"), (2048, None, "bei (2⁹)² die Hochzahlen addiert (2¹¹) und das Teilen durch 2¹⁰ vergessen", "2 ** 11")]), g="verknuepfen", regel=R)
