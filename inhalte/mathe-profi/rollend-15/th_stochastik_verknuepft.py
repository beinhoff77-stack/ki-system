T = "stochastik.verknuepft"
AN = "id.daten.anteil"
ST = "id.daten.stufen"
OHNE_M = "Mengen und Mengenoperationen zählen (Elemente, Schnitt, Vereinigung): keine Regel des Katalogs trägt den Lösungsweg"
OHNE_V = "Vierfeldertafel ausfüllen (Zeilen- und Spaltensummen): keine Regel des Katalogs trägt den Lösungsweg"
OHNE_ADD = "Additionssatz für zwei Ereignisse (Schnitt nicht doppelt zählen): keine Regel des Katalogs trägt den Lösungsweg"
teil = lambda n: {d for d in range(1, n + 1) if n % d == 0}
# ───────── elemente ─────────
neu(T, "elemente", "anwenden", Z(
    "Kim schreibt alle Quadratzahlen auf, die größer als 70 und kleiner als 700 sind, und bildet daraus eine Menge. Wie viele Elemente hat die Menge?",
    18, "26 - 9 + 1", sum(1 for n in range(71, 700) if math.isqrt(n) ** 2 == n), "Suche die kleinste und die größte Quadratzahl in diesem Bereich. Welche Zahlen werden dafür quadriert, und wie viele sind das?",
    "8² = 64 liegt noch unter 70, 9² = 81 ist die erste Quadratzahl im Bereich. 26² = 676 ist die letzte, denn 27² = 729 ist größer als 700. Es sind die Quadrate der Zahlen 9 bis 26: 26 − 9 + 1 = 18 Elemente.",
    [B("26 - 9", "die Zahlen 9 bis 26 nur mit 26 − 9 gezählt, also das erste Element vergessen"), B("26 - 8 + 1", "schon bei 8² = 64 begonnen, obwohl 64 kleiner als 70 ist"), B("26", "alle Quadratzahlen von 1² an bis 676 mitgezählt")]), g="mehrschritt", ohne=OHNE_M)
# ───────── schnitt ─────────
neu(T, "schnitt", "anwenden", Z(
    "A ist die Menge aller Teiler von 60, B die Menge aller Teiler von 45. Wie viele Elemente liegen in A, aber nicht in B?",
    8, "12 - 4", len(teil(60) - teil(45)), "Schreibe beide Teilermengen auf. Welche Zahlen kommen in beiden vor (Schnitt A ∩ B)? Diese gehören nicht zur gesuchten Menge.",
    "Die Teiler von 60 sind 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60 (12 Elemente). Die Teiler von 45 sind 1, 3, 5, 9, 15, 45. In beiden stehen 1, 3, 5 und 15, das sind 4 Elemente. In A, aber nicht in B liegen 12 − 4 = 8 Elemente.",
    [B("12", "alle Teiler von 60 gezählt, die gemeinsamen Teiler nicht herausgenommen"), B("4", "nur den Schnitt A ∩ B gezählt"), B("6 - 4", "die Elemente gezählt, die nur in B liegen")]), g="verknuepfen", ohne=OHNE_M)
# ───────── verknuepfen ─────────
neu(T, "verknuepfen", "anwenden", Z(
    "A ist die Menge der Vielfachen von 6 zwischen 1 und 60 (60 eingeschlossen), B die Menge der Vielfachen von 4 zwischen 1 und 60 (60 eingeschlossen). Wie viele Elemente hat die Vereinigung A ∪ B?",
    20, "10 + 15 - 5", sum(1 for n in range(1, 61) if n % 6 == 0 or n % 4 == 0), "Zähle erst A und B, dann die Zahlen, die in beiden stehen. Welche Zahlen sind das?",
    "A hat 10 Elemente (6, 12, …, 60), B hat 15 Elemente (4, 8, …, 60). In beiden stehen die Vielfachen von 12: 12, 24, 36, 48, 60, das sind 5. Vereinigung: 10 + 15 − 5 = 20.",
    [B("10 + 15", "die Elemente beider Mengen addiert, die gemeinsamen doppelt gezählt"), B("5", "nur den Schnitt genommen"), B("15", "nur die größere Menge genommen")]), g="mehrschritt", ohne=OHNE_M)
# ───────── additionssatz ─────────
neu(T, "additionssatz", "lueckenweg", L(
    "In einer Reisegruppe von 40 Personen haben 24 Sonnencreme dabei, 18 einen Hut und 10 beides. Mindestens eines von beiden haben ① Personen. Keines von beiden haben ② Personen. Das sind ③ Prozent der Gruppe.",
    "① = □; ② = □; ③ = □", [32, 8, 20], ["24 + 18 - 10", "40 - {1}", "{2} * 100 / 40"], ["24 + 18 - 10", "40 - 32", "8 / 40 * 100"],
    "Wer beides hat, steht in beiden Zahlen 24 und 18. Wie oft darf man ihn zählen?",
    "Mindestens eines: 24 + 18 − 10 = 32. Keines: 40 − 32 = 8. Anteil: 8 : 40 = 0,2 = 20 %.",
    {0: [(42, None, "die 10 mit beidem doppelt gezählt", "24 + 18")], 1: [(16, None, "von der Gruppe nur die Sonnencreme-Träger abgezogen", "40 - 24")], 2: [(8, None, "die Anzahl als Prozentzahl genommen", "{2}")]}), regel=None, ohne=OHNE_ADD)
neu(T, "additionssatz", "anwenden", Z(
    "In einem Reisebüro gewinnt man mit Wahrscheinlichkeit 0,35 einen Hotelgutschein (A) und mit 0,28 einen Flugrabatt (B). Mit Wahrscheinlichkeit 0,09 gewinnt man beides. Wie groß ist die Wahrscheinlichkeit, mindestens einen der beiden Preise zu gewinnen?",
    0.54, "0.35 + 0.28 - 0.09", 0.54, "Wer beides gewinnt, ist in beiden Wahrscheinlichkeiten enthalten. Wie oft soll er zählen?",
    "P(A ∪ B) = P(A) + P(B) − P(A ∩ B) = 0,35 + 0,28 − 0,09 = 0,54.",
    [B("0.35 + 0.28", "die Wahrscheinlichkeit für beides doppelt gezählt"), B("0.35 + 0.28 + 0.09", "den Schnitt addiert statt abgezogen"), B("0.35 - 0.28", "die Wahrscheinlichkeiten voneinander abgezogen")]), g="mehrschritt", ohne=OHNE_ADD)
# ───────── venn ─────────
neu(T, "venn", "anwenden", Z(
    "Im Venn-Diagramm liegen von 25 Elementen 14 in A, 11 in B und 6 in beiden. Wie viele Elemente liegen in genau einer der beiden Mengen?",
    13, "(14 - 6) + (11 - 6)", 13, "Trenne jede Menge in den Teil, der nur ihr gehört, und den Teil im Schnitt.",
    "Nur in A: 14 − 6 = 8. Nur in B: 11 − 6 = 5. Genau eine Menge: 8 + 5 = 13.",
    [B("14 + 11", "die Schnittelemente doppelt gezählt"), B("14 + 11 - 6", "den Schnitt nur einmal abgezogen, also die Vereinigung statt genau eine Menge"), B("14 - 6", "nur die Elemente genommen, die nur in A liegen")]), g="mehrschritt", ohne=OHNE_M)
# ───────── mengen_verstehen ─────────
neu(T, "mengen_verstehen", "verfahren_waehlen", W(
    "Es gilt A ⊂ B: Jedes Element von A liegt auch in B. Welche Aussage über die Schnittmenge und die Vereinigung gilt immer?",
    "A ∩ B = A und A ∪ B = B", [("A ∩ B = B und A ∪ B = A", "Schnitt und Vereinigung vertauscht (das gilt nur im Sonderfall A = B)"), ("A ∩ B = ∅ und A ∪ B = B", "der Schnitt ist A und ist nur dann leer, wenn A leer ist"), ("A ∩ B = A und A ∪ B = A", "die Vereinigung ist B; sie ist nur dann gleich A, wenn A = B")],
    "Wähle selbst ein Beispiel: A = {2, 4} und B = {1, 2, 3, 4}. Bestimme beide Mengen.",
    "Im Beispiel A = {2, 4} und B = {1, 2, 3, 4} gilt A ∩ B = {2, 4} = A und A ∪ B = {1, 2, 3, 4} = B. Das gilt allgemein: Was in A liegt, liegt auch in B.",
    lambda: ({2, 4} & {1, 2, 3, 4} == {2, 4}) and ({2, 4} | {1, 2, 3, 4} == {1, 2, 3, 4})), g="begruenden", ohne=OHNE_M)
# ───────── vierfeld ─────────
neu(T, "vierfeld", "lueckenweg", L(
    "In einem Skiort sind 100 Gäste. Davon sind 64 Frauen, 41 fahren Ski, und 27 Frauen fahren Ski. Frauen ohne Ski gibt es ①. Männer mit Ski gibt es ②. Männer ohne Ski gibt es ③.",
    "① = □; ② = □; ③ = □", [37, 14, 22], ["64 - 27", "41 - 27", "100 - 64 - {2}"], ["64 - 27", "41 - 27", "36 - 14"],
    "Trage die Zahlen in eine Vierfeldertafel ein. Jede Zeile und jede Spalte ergibt die angegebene Summe.",
    "Frauen ohne Ski: 64 − 27 = 37. Männer mit Ski: 41 − 27 = 14. Männer insgesamt: 100 − 64 = 36, davon 14 mit Ski, also 36 − 14 = 22 ohne Ski.",
    {0: [(91, None, "die Zahlen addiert statt subtrahiert", "64 + 27")], 1: [(68, None, "die Zahlen addiert statt subtrahiert", "41 + 27")], 2: [(36, None, "die Männer mit Ski nicht abgezogen", "100 - 64")]}), regel=None, ohne=OHNE_V)
neu(T, "vierfeld", "anwenden", Z(
    "Von 120 Reisenden sind 72 Frauen. 47 Reisende fahren Rad, davon sind 19 Männer. Wie viele Frauen fahren nicht Rad?",
    44, "72 - (47 - 19)", 44, "Zeichne eine Vierfeldertafel mit Frau/Mann und Rad/nicht Rad. Beginne mit den Radfahrern.",
    "Frauen mit Rad: 47 − 19 = 28. Frauen insgesamt 72, also Frauen ohne Rad: 72 − 28 = 44.",
    [B("72 - 19", "die Männer mit Rad von den Frauen abgezogen"), B("47 - 19", "nur die Frauen mit Rad berechnet"), B("120 - 72", "die Anzahl der Männer genommen")]), g="mehrschritt", ohne=OHNE_V)
# ───────── tafel_wkeit ─────────
neu(T, "tafel_wkeit", "anwenden", Z(
    "Bei Gästen eines Hotels gilt: Mit Wahrscheinlichkeit 0,6 ist ein Gast eine Frau, mit 0,45 fährt er Ski, und mit 0,27 ist er eine Frau, die Ski fährt. Wie groß ist die Wahrscheinlichkeit, dass ein Gast ein Mann ist, der nicht Ski fährt?",
    0.22, "1 - (0.6 + 0.45 - 0.27)", 0.22, "Fülle eine Vierfeldertafel mit Wahrscheinlichkeiten. Männer ohne Ski ist das letzte Feld.",
    "Mann: 1 − 0,6 = 0,4. Mann und Ski: 0,45 − 0,27 = 0,18. Mann ohne Ski: 0,4 − 0,18 = 0,22.",
    [B("0.6 + 0.45 - 0.27", "die Wahrscheinlichkeit für Frau oder Ski statt ihres Gegenteils genommen"), B("0.4 - 0.27", "von den Männern den Wert für Frau und Ski abgezogen"), B("0.45 - 0.27", "nur Männer mit Ski berechnet")]), g="mehrschritt", regel=AN,
    zweifel="Vierfeldertafel mit Wahrscheinlichkeiten: id.daten.anteil trägt die Deutung als Anteil, das Ausfüllen der Tafel hat keine eigene Regel")
# ───────── bedingt ─────────
neu(T, "verknuepfen", "anwenden", Z(
    "Von den Besuchern einer Therme sind 55 % Frauen, 44 % nutzen die Sauna, und 33 % sind Frauen, die die Sauna nutzen. Wie viel Prozent aller Besucher sind weder Frau noch nutzen die Sauna?",
    34, "100 - (55 + 44 - 33)", 34, "Die Besucher, die Frau sind oder die Sauna nutzen, bilden die Vereinigung. Wer beides ist, darf nur einmal zählen. Wie viel bleibt vom Ganzen übrig?",
    "Frau oder Sauna: 55 + 44 − 33 = 66 (die 33 stehen in beiden Zahlen). Weder noch ist das Gegenteil: 100 − 66 = 34. Es sind 34 % aller Besucher.",
    [B("55 + 44 - 33", "den Anteil für Frau oder Sauna statt für keines von beiden angegeben"), B("100 - 55 - 44", "die Besucher mit beidem doppelt abgezogen"), B("100 - 55", "nur die Besucher genommen, die keine Frau sind")], einheit="%"), g="mehrschritt", regel=None, ohne=OHNE_ADD)
neu(T, "venn", "anwenden", Z(
    "Auf einem Campingplatz leihen 52 % der Gäste ein Fahrrad, 31 % ein Kajak und 18 % beides. Wie viel Prozent aller Gäste leihen genau eines der beiden Geräte?",
    47, "52 + 31 - 2 * 18", 47, "Wer beides leiht, soll nicht zählen. Trenne: nur Fahrrad, nur Kajak. Wie viel vom Fahrrad-Anteil gehört auch zum Kajak-Anteil?",
    "Nur Fahrrad: 52 − 18 = 34. Nur Kajak: 31 − 18 = 13. Genau eines: 34 + 13 = 47. Es sind 47 % aller Gäste.",
    [B("52 + 31 - 18", "die Vereinigung (Fahrrad oder Kajak) statt genau eines der beiden Geräte angegeben"), B("52 + 31", "beide Anteile addiert, die Gäste mit beidem doppelt gezählt"), B("52 - 18", "nur die Gäste genommen, die nur ein Fahrrad leihen")], einheit="%"), g="mehrschritt", regel=None, ohne=OHNE_ADD)
# ───────── rueckschluss ─────────
neu(T, "additionssatz", "umkehren", Z(
    "Bei einer Verlosung gewinnt man mit Wahrscheinlichkeit 0,42 einen Hotelgutschein (A) und mit 0,35 einen Flugrabatt (B). Mit Wahrscheinlichkeit 0,61 gewinnt man mindestens einen der beiden Preise. Wie groß ist die Wahrscheinlichkeit, beide Preise zu gewinnen?",
    0.16, "0.42 + 0.35 - 0.61", 0.16, "Der Additionssatz gilt auch rückwärts: P(A ∪ B) = P(A) + P(B) − P(A ∩ B). Stelle nach P(A ∩ B) um.",
    "Aus P(A ∪ B) = P(A) + P(B) − P(A ∩ B) folgt P(A ∩ B) = P(A) + P(B) − P(A ∪ B) = 0,42 + 0,35 − 0,61 = 0,16.",
    [B("0.42 + 0.35", "die beiden Wahrscheinlichkeiten nur addiert, die Vereinigung nicht abgezogen"), B("1 - 0.61", "die Wahrscheinlichkeit für keinen der beiden Preise genommen"), B("0.61 - 0.42", "die Vereinigung minus P(A) gerechnet, also den Anteil nur B")]), g="rueckwaerts", regel=None, ohne=OHNE_ADD)
# ───────── verstehen ─────────
neu(T, "verstehen", "verfahren_waehlen", W(
    "Für zwei Ereignisse A und B gilt P(A ∪ B) = P(A) + P(B). Was folgt daraus?",
    "Der Schnitt hat die Wahrscheinlichkeit 0: P(A ∩ B) = 0.", [("A liegt ganz in B (A ⊂ B).", "bei A ⊂ B ist die Vereinigung gleich B, es gilt P(A ∪ B) = P(B)"), ("A und B sind gleich wahrscheinlich.", "über die Einzelwahrscheinlichkeiten sagt die Gleichung nichts aus")],
    "Vergleiche mit dem Additionssatz P(A ∪ B) = P(A) + P(B) − P(A ∩ B). Was muss P(A ∩ B) sein, damit beide Gleichungen stimmen?",
    "Der Additionssatz lautet P(A ∪ B) = P(A) + P(B) − P(A ∩ B). Soll P(A ∪ B) = P(A) + P(B) gelten, muss P(A ∩ B) = 0 sein. Mehr folgt aus der Gleichung allein nicht.",
    lambda: (F(1, 6) + F(1, 6) == F(2, 6)) and (F(1, 6) + F(2, 6) != F(2, 6)) and (F(2, 6) + F(3, 6) != F(3, 6))), g="begruenden", regel=None, ohne=OHNE_ADD)
neu(T, "verstehen", "fehler_detektiv", FD(
    "Alex untersucht die Gäste eines Skiorts: 40 % fahren Ski (A), 30 % sind Kinder (B), und 12 % sind Kinder, die Ski fahren. Er schreibt:",
    [("Es gilt P(A ∩ B) = 0,12.", True, True),
     ("Gäste, die Ski fahren und keine Kinder sind: 0,40 − 0,12 = 0,28.", True, True),
     ("Man addiert die beiden Wahrscheinlichkeiten, also ist die Wahrscheinlichkeit für Ski oder Kind P(A ∪ B) = 0,70.", False, True)],
    "Wie oft werden die Kinder, die Ski fahren, in 0,40 + 0,30 gezählt? Wie oft sollen sie in der Vereinigung zählen?",
    "Die Kinder, die Ski fahren, stecken in 0,40 und in 0,30, sie werden also doppelt gezählt. Der Additionssatz zieht den Schnitt ab: P(A ∪ B) = 0,40 + 0,30 − 0,12 = 0,58. Die Zeilen 1 und 2 sind richtig. Der Fehler steckt in Zeile 3."), g="fehler", regel=None, ohne=OHNE_ADD)
