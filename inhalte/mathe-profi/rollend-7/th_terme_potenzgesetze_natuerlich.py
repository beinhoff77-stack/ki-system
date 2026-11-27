T = "terme.potenzgesetze_natuerlich"
# ───────── mal_gleiche_basis ─────────
neu(T, "mal_gleiche_basis", "lueckenweg", L(
    "Vereinfache 3⁴ · 3⁵ zu einer Potenz mit der Basis 3. Die Hochzahl ist dann ①. Multiplizierst du dieses Ergebnis noch mit 3², hat die Potenz die Hochzahl ②.",
    KOMM(2), [9, 11], ["4 + 5", "4 + 5 + 2"], ["9", "11"], "Gleiche Basis beim Malnehmen: Was passiert mit den Hochzahlen?",
    "3⁴ · 3⁵ = 3⁹, denn 4 + 5 = 9. Mit 3² dazu: 3¹¹, denn 9 + 2 = 11.",
    {0: [(20, "fb.potenz.hochzahlen_malgenommen", "die Hochzahlen malgenommen")], 1: [(18, "fb.potenz.hochzahlen_malgenommen", "9 · 2 gerechnet")]}), regel="rr.potenz")
neu(T, "mal_gleiche_basis", "fehler_detektiv", FD(
    "Kim vereinfacht a³ · a⁴ · a². Die Zeilen bauen aufeinander auf.",
    [("Die Basis ist überall a, die Hochzahlen werden malgenommen: 3 · 4 · 2 = 24.", gl("a**3*a**4*a**2", "a**(3*4*2)")), ("Also ist a³ · a⁴ · a² = a²⁴.", True), ("Das Ergebnis lautet a²⁴.", True)],
    "Was geschieht mit den Hochzahlen, wenn man Potenzen mit gleicher Basis malnimmt? Probe mit a = 2 und kleinen Hochzahlen: 2² · 2³.",
    "Beim Malnehmen werden die Hochzahlen addiert: 3 + 4 + 2 = 9. Richtig ist a⁹. Probe mit 2² · 2³ = 4 · 8 = 32 = 2⁵ und nicht 2⁶."), regel="rr.potenz")
neu(T, "mal_gleiche_basis", "zwei_wege", Z(
    "Berechne 2⁴ · 2³ auf zwei Wegen. Weg A: beide Potenzen einzeln ausrechnen und dann malnehmen. Weg B: erst die Hochzahlen zusammenfassen und dann die Potenz ausrechnen. Welchen Wert hat das Produkt?",
    128, "2 ** (4 + 3)", "16 * 8", "Beide Wege müssen denselben Wert ergeben.",
    "Weg A: 16 · 8 = 128. Weg B: 2⁷ = 128.",
    [(4096, "fb.potenz.hochzahlen_malgenommen", "die Hochzahlen malgenommen: 2¹²"), (14, "fb.potenz.basis_mal_hochzahl", "Basis mal Hochzahl: 2 · 7")]), regel="rr.potenz")

# ───────── gleicher_exponent ─────────
neu(T, "gleicher_exponent", "lueckenweg", L(
    "Berechne 24³ : 6³ geschickt. Beide Potenzen haben dieselbe Hochzahl. Du teilst zuerst die Basen und erhältst ①. Dieses Ergebnis nimmst du hoch drei und erhältst ②.",
    KOMM(2), [4, 64], ["24 // 6", "(24 // 6) ** 3"], ["4", "4 * 4 * 4"], "Bei gleichen Hochzahlen darfst du die Basen zuerst teilen.",
    "24 : 6 = 4. 4³ = 64. Probe: 24³ : 6³ = 13824 : 216 = 64.",
    {0: [(18, "fb.potenz.basis_mal_hochzahl", "24 − 6 gerechnet")], 1: [(12, "fb.potenz.basis_mal_hochzahl", "4 · 3 statt 4³ gerechnet")]}), regel="rr.potenz")
neu(T, "gleicher_exponent", "bruecke", W(
    "Das Produkt 2 · 2 · 2 · 2 · 5 · 5 · 5 · 5 soll als eine einzige Potenz geschrieben werden. Welche Potenz ist das?",
    "10⁴", [("7⁴", "die Basen addiert statt malgenommen"), ("10⁸", "die Hochzahlen addiert, obwohl die Basen verschieden sind"), ("4¹⁰", "falsch zusammengezählt")],
    "Es gibt gleich viele Faktoren 2 und 5. Fasse je einen Faktor 2 und einen Faktor 5 zusammen.",
    "Vier Paare 2 · 5 = 10. Also 10 · 10 · 10 · 10 = 10⁴. Probe: 16 · 625 = 10 000.",
    lambda: 2 ** 4 * 5 ** 4 == 10 ** 4 and 7 ** 4 != 10 ** 4 and 10 ** 8 != 10 ** 4 and 4 ** 10 != 10 ** 4), regel="rr.potenz")
neu(T, "gleicher_exponent", "umkehren", Z(
    "Für welche Zahl a gilt a³ = 2³ · 7³?",
    14, "2 * 7", 14, "Wenn die Hochzahlen gleich sind, darfst du die Basen malnehmen.",
    "2³ · 7³ = (2 · 7)³ = 14³. Also ist a = 14. Probe: 8 · 343 = 2 744 = 14³.",
    [(9, "fb.potenz.basis_mal_hochzahl", "2 + 7 gerechnet"), (98, "fb.potenz.hochzahlen_malgenommen", "2 · 7² oder ähnlich falsch gerechnet"), (42, None, "2 · 7 · 3 gerechnet")]), g="umkehr", regel="rr.potenz")
assert 14 ** 3 == 2 ** 3 * 7 ** 3

# ───────── potenz_von_potenz ─────────
neu(T, "potenz_von_potenz", "lueckenweg", L(
    "Vereinfache (2³)⁴ zu einer Potenz 2^k. Die Hochzahlen werden verrechnet: k = ①. Der Wert der Potenz 2^k ist ②.",
    KOMM(2), [12, 4096], ["3 * 4", "2 ** (3 * 4)"], ["12", "4096"], "Eine Potenz wird noch einmal hoch genommen. Was geschieht mit den Hochzahlen?",
    "(2³)⁴ = 2³ · 2³ · 2³ · 2³ = 2¹². 2¹² = 4 096.",
    {0: [(7, "fb.potenz.hochzahlen_malgenommen", "die Hochzahlen addiert statt malgenommen")], 1: [(128, None, "2⁷ gerechnet")]}), regel="rr.potenz")
neu(T, "potenz_von_potenz", "zwei_wege", Z(
    "Berechne (3²)³ auf zwei Wegen. Weg A: erst die Klammer 3² ausrechnen und das Ergebnis hoch 3 nehmen. Weg B: die Hochzahlen verrechnen und dann die Potenz ausrechnen. Welchen Wert hat (3²)³?",
    729, "9 ** 3", "3 ** (2 * 3)", "Beide Wege müssen denselben Wert ergeben.",
    "Weg A: 9³ = 729. Weg B: 3⁶ = 729.",
    [(243, "fb.potenz.hochzahlen_malgenommen", "die Hochzahlen addiert: 3⁵"), (27, None, "nur 3³ gerechnet")]), regel="rr.potenz")
neu(T, "potenz_von_potenz", "bruecke", W(
    "Der Term (x⁴)² soll als Produkt geschrieben werden. Welches Produkt ist dasselbe wie (x⁴)²?",
    "x⁴ · x⁴", [("x⁴ · x²", "die Hochzahl 2 als Faktor x² gelesen"), ("x⁴ + x⁴", "Hoch zwei als Verdopplung verstanden"), ("2 · x⁴", "Hoch zwei als Malnehmen mit 2 verstanden")],
    "Hoch 2 heißt: Der Inhalt der Klammer kommt zweimal als Faktor vor.",
    "(x⁴)² = x⁴ · x⁴ = x⁸.",
    lambda: gl("(x**4)**2", "x**4*x**4") and not gl("(x**4)**2", "x**4*x**2") and not gl("(x**4)**2", "x**4+x**4") and not gl("(x**4)**2", "2*x**4")), regel="rr.potenz")

# ───────── geteilt_gleiche_basis ─────────
neu(T, "geteilt_gleiche_basis", "lueckenweg", L(
    "Vereinfache 7⁹ : 7⁴ zu einer Potenz mit der Basis 7. Die Hochzahl ist dann ①. Teilst du das Ergebnis noch durch 7², hat die Potenz die Hochzahl ②.",
    KOMM(2), [5, 3], ["9 - 4", "9 - 4 - 2"], ["5", "3"], "Gleiche Basis beim Teilen: Was passiert mit den Hochzahlen?",
    "7⁹ : 7⁴ = 7⁵, denn 9 − 4 = 5. Noch durch 7²: 7³, denn 5 − 2 = 3.",
    {0: [(13, "fb.potenz.hochzahlen_malgenommen", "die Hochzahlen addiert")], 1: [(7, None, "5 + 2 gerechnet")]}), regel="rr.potenz")
neu(T, "geteilt_gleiche_basis", "umkehren", Z(
    "In der Rechnung 5^k : 5⁴ = 5⁷ fehlt die Hochzahl k. Wie groß ist k?",
    11, "7 + 4", 11, "Beim Teilen werden die Hochzahlen subtrahiert. Rechne rückwärts.",
    "k − 4 = 7, also k = 11. Probe: 5¹¹ : 5⁴ = 5⁷.",
    [(3, "fb.gegenrechnung.gleiche_rechnung", "7 − 4 gerechnet"), (28, "fb.potenz.hochzahlen_malgenommen", "7 · 4 gerechnet")]), g="umkehr", regel="rr.potenz")
neu(T, "geteilt_gleiche_basis", "fehler_detektiv", FD(
    "Kim vereinfacht a⁸ : a³ : a. Die Zeilen bauen aufeinander auf.",
    [("a⁸ : a³ = a⁵, denn 8 − 3 = 5.", gl("a**8/a**3", "a**5")), ("a⁵ : a = a⁵, weil a keine Hochzahl hat.", gl("a**5/a", "a**5")), ("Das Ergebnis lautet a⁵.", True)],
    "Welche Hochzahl hat a, wenn nichts dransteht? Probe mit a = 2.",
    "a ist dasselbe wie a¹. Also a⁵ : a¹ = a⁴. Probe mit a = 2: 32 : 2 = 16 = 2⁴."), regel="rr.potenz")

# ───────── anwenden ─────────
neu(T, "anwenden", "anwenden", Z(
    "Eine Zelle teilt sich jede Stunde in zwei Zellen. Nach 3 Stunden sind aus einer Zelle 2³ Zellen geworden. Jede dieser Zellen vermehrt sich in 7 weiteren Stunden genauso weiter. Wie viele Zellen sind es dann insgesamt?",
    1024, "2 ** (3 + 7)", "8 * 128", "Jede Zelle wird in 7 Stunden zu 2⁷ Zellen. Wie viele solcher Gruppen gibt es?",
    "Es gibt 2³ = 8 Zellen. Jede wird zu 2⁷ = 128. Insgesamt 8 · 128 = 1 024 = 2¹⁰ Zellen.",
    [(2097152, "fb.potenz.hochzahlen_malgenommen", "die Hochzahlen malgenommen: 2²¹"), (56, "fb.potenz.basis_mal_hochzahl", "8 · 7 gerechnet")], "Zellen"), g="einkleidung", regel="rr.potenz")
neu(T, "anwenden", "anwenden", Z(
    "Ein Würfel hat die Kantenlänge 2⁴ cm. Das Volumen ist Kante mal Kante mal Kante. Es lässt sich als Potenz 2^k cm³ schreiben. Wie groß ist k?",
    12, "4 * 3", 12, "Schreibe das Volumen als (2⁴)³ und verrechne die Hochzahlen.",
    "V = (2⁴)³ = 2⁴ · 2⁴ · 2⁴ = 2¹². Das sind 4 096 cm³.",
    [(7, "fb.potenz.hochzahlen_malgenommen", "die Hochzahlen addiert: 4 + 3"), (64, "fb.potenz.basis_mal_hochzahl", "4³ gerechnet statt (2⁴)³")]), g="transfer", regel="rr.potenz")
neu(T, "anwenden", "verfahren_waehlen", W(
    "Du sollst 5⁶ : 5² berechnen. Welcher Weg ist richtig?",
    "Die Hochzahlen subtrahieren: 5⁴ = 625.",
    [("Die Hochzahlen teilen: 5³ = 125.", "die Hochzahlen geteilt statt subtrahiert"), ("Die Basen teilen und die Hochzahlen subtrahieren: 1⁴ = 1.", "die Basen geteilt, obwohl sie gleich bleiben"), ("Die Hochzahlen addieren: 5⁸ = 390 625.", "die Rechenart für das Malnehmen benutzt")],
    "Beim Teilen gleicher Basen bleibt die Basis. Nur die Hochzahlen werden verrechnet.",
    "5⁶ : 5² = 5⁶⁻² = 5⁴ = 625. Probe: 15 625 : 25 = 625.",
    lambda: 5 ** 6 // 5 ** 2 == 625 == 5 ** 4 and 5 ** 3 != 625 and 1 != 625 and 5 ** 8 != 625), regel="rr.potenz")
