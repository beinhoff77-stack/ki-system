T = "stochastik.verknuepft"
AN = "id.daten.anteil"
ST = "id.daten.stufen"
OHNE_M = "Mengen und Mengenoperationen zählen (Elemente, Schnitt, Vereinigung): keine Regel des Katalogs trägt den Lösungsweg"
OHNE_V = "Vierfeldertafel ausfüllen (Zeilen- und Spaltensummen): keine Regel des Katalogs trägt den Lösungsweg"
OHNE_ADD = "Additionssatz für zwei Ereignisse (Schnitt nicht doppelt zählen): keine Regel des Katalogs trägt den Lösungsweg"
teil = lambda n: {d for d in range(1, n + 1) if n % d == 0}
# ───────── elemente ─────────
neu(T, "elemente", "anwenden", Z(
    "Wie viele zweistellige Zahlen haben die Ziffernsumme 9?",
    9, "9", sum(1 for n in range(10, 100) if n // 10 + n % 10 == 9), "Schreibe die Zahlen geordnet auf: Die Zehnerziffer läuft von 1 bis 9, die Einerziffer ergänzt zur Ziffernsumme.",
    "Es sind 18, 27, 36, 45, 54, 63, 72, 81 und 90. Das sind 9 Zahlen. 09 zählt nicht, weil es keine zweistellige Zahl ist.",
    [B("8", "die 90 vergessen"), B("10", "die 09 mitgezählt"), B("11", "die Zahlen 9 und 99 mitgezählt, obwohl ihre Ziffernsumme 9 und 18 ist")]), g="mehrschritt", ohne=OHNE_M)
# ───────── schnitt ─────────
neu(T, "schnitt", "anwenden", Z(
    "A ist die Menge aller Teiler von 36, B die Menge aller Teiler von 48. Wie viele Elemente hat der Schnitt A ∩ B?",
    6, "6", len(teil(36) & teil(48)), "Schreibe beide Teilermengen auf und streiche, was nur in einer von beiden vorkommt. Oder: Welche Zahl teilt beide, und welche Teiler hat sie?",
    "Die Teiler von 36 sind 1, 2, 3, 4, 6, 9, 12, 18, 36. Die Teiler von 48 sind 1, 2, 3, 4, 6, 8, 12, 16, 24, 48. In beiden stehen 1, 2, 3, 4, 6 und 12. Das sind 6 Elemente.",
    [B("3", "nur die Zahlen 1, 2 und 3 gefunden"), B("12", "den größten gemeinsamen Teiler als Anzahl genommen"), B("9", "die Anzahl der Teiler von 36 genommen")]), g="verknuepfen", ohne=OHNE_M)
# ───────── verknuepfen ─────────
neu(T, "verknuepfen", "anwenden", Z(
    "A ist die Menge der Vielfachen von 6 bis 60, B die Menge der Vielfachen von 4 bis 60. Wie viele Elemente hat die Vereinigung A ∪ B?",
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
    "Es gilt A ⊂ B: Jedes Element von A liegt auch in B. Welche Aussage über die Schnittmenge und die Vereinigung stimmt?",
    "A ∩ B = A und A ∪ B = B", [("A ∩ B = B und A ∪ B = A", "Schnitt und Vereinigung vertauscht"), ("A ∩ B = ∅ und A ∪ B = B", "die Mengen haben gemeinsame Elemente, der Schnitt ist nicht leer"), ("A ∩ B = A und A ∪ B = A", "die Vereinigung enthält auch die Elemente von B")],
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
neu(T, "bedingt", "anwenden", Z(
    "Mit Wahrscheinlichkeit 0,6 ist ein Gast eine Frau, mit 0,45 fährt er Ski, und mit 0,24 ist er eine Frau, die Ski fährt. Ein Gast ist eine Frau. Wie groß ist die Wahrscheinlichkeit, dass sie Ski fährt?",
    0.4, "0.24 / 0.6", 0.4, "Es geht nur um die Frauen. Welcher Anteil der Frauen fährt Ski?",
    "P(Ski | Frau) = P(Frau ∩ Ski) : P(Frau) = 0,24 : 0,6 = 0,4.",
    [BR("0.24 / 0.45", "durch die Wahrscheinlichkeit für Ski geteilt, also die umgekehrte bedingte Wahrscheinlichkeit", None, 2), B("0.24 * 0.6", "die Wahrscheinlichkeiten malgenommen"), B("0.6 - 0.24", "den Wert für Frauen ohne Ski berechnet")]), g="mehrschritt", regel=AN,
    zweifel="Bedingte Wahrscheinlichkeit als Anteil: id.daten.anteil trägt Günstige durch Mögliche")
w_g, c_g = rd("6 / 10 * 5 / 9", 3)
neu(T, "bedingt", "anwenden", Z(
    "Aus einer Tüte mit 6 roten und 4 gelben Gummibärchen zieht Kim zwei ohne Zurücklegen. Wie groß ist die Wahrscheinlichkeit, dass beide rot sind? Runde auf drei Dezimalstellen.",
    w_g, c_g, "round(1 / 3, 3)", "Nach dem ersten Zug hat sich die Tüte verändert. Wie viele rote und wie viele Bärchen insgesamt sind noch darin?",
    "Erster Zug rot: 6 von 10. Dann sind noch 5 rote unter 9 Bärchen. Entlang des Pfads wird malgenommen: 6/10 · 5/9 = 30/90 = 1/3 ≈ 0,333.",
    [B("0.6 * 0.6", "wie beim Ziehen mit Zurücklegen gerechnet", "fb.stufen.ohne_zuruecklegen_uebersehen"), BR("6 / 10 * 4 / 9", "im zweiten Zug die gelben statt der roten gezählt", None, 3), B("0.6 + 5 / 9", "entlang des Pfads addiert statt malgenommen", "fb.stufen.addiert_statt_malgenommen")], toleranz=0.001), g="mehrschritt", regel=ST)
# ───────── rueckschluss ─────────
w_r, c_r = rd("8 / 26", 2)
neu(T, "rueckschluss", "umkehren", Z(
    "Von 200 Reisenden haben 80 eine Reiseversicherung. Von den Versicherten melden 10 % einen Schaden, von den Nichtversicherten 15 %. Ein Reisender hat einen Schaden gemeldet. Wie groß ist die Wahrscheinlichkeit, dass er versichert ist? Runde auf zwei Dezimalstellen.",
    w_r, c_r, "round(4 / 13, 2)", "Berechne zuerst, wie viele Reisende insgesamt einen Schaden melden, und davon, wie viele versichert sind.",
    "Versichert mit Schaden: 10 % von 80 = 8. Nicht versichert (120 Personen) mit Schaden: 15 % von 120 = 18. Insgesamt 26 Schäden. Anteil versichert: 8 : 26 ≈ 0,31.",
    [BR("8 / 18", "durch die Schäden ohne Versicherung statt durch alle Schäden geteilt", "fb.anteil.guenstig_durch_unguenstig", 2), B("0.1", "die gegebene Wahrscheinlichkeit für Schaden bei Versicherten genommen"), BR("8 / 200", "durch alle Reisenden statt durch alle mit Schaden geteilt", None, 2)], toleranz=0.01), g="rueckwaerts", regel=AN)
# ───────── verstehen ─────────
neu(T, "verstehen", "verfahren_waehlen", W(
    "An einem Urlaubsort gilt: Wahrscheinlichkeit für Regen unter der Bedingung „Wolken am Morgen“ ist 0,8. Welche Aussage passt dazu?",
    "Von allen Tagen mit Wolken am Morgen regnet es an 80 %.", [("Von allen Regentagen haben 80 % Wolken am Morgen.", "die Bedingung vertauscht: das wäre P(Wolken | Regen)"), ("An 80 % aller Tage regnet es.", "die Bedingung „Wolken am Morgen“ nicht beachtet")],
    "Die Bedingung steht hinter dem senkrechten Strich: Auf welche Tage bezieht sich der Anteil 0,8?",
    "P(Regen | Wolken) betrachtet nur die Tage mit Wolken am Morgen. Von diesen regnet es an 80 %. Das ist etwas anderes als der Anteil der Wolkentage unter den Regentagen.",
    lambda: True), g="begruenden", regel=AN, zweifel="Deutung der bedingten Wahrscheinlichkeit: id.daten.anteil (Anteil von was?)")
neu(T, "verstehen", "fehler_detektiv", FD(
    "Alex untersucht Reisende: 30 % fliegen (F), 40 % buchen ein Hotel (H), 12 % tun beides. Er schreibt:",
    [("Es gilt P(F ∩ H) = 0,12.", True, True),
     ("Außerdem ist P(F) · P(H) = 0,3 · 0,4 = 0,12, also sind F und H unabhängig.", True, True),
     ("Unabhängige Ereignisse schließen sich aus, also ist F ∩ H leer.", False, True)],
    "Wenn F ∩ H leer wäre, was wäre P(F ∩ H)? Passt das zu Zeile 1?",
    "Unabhängig und unvereinbar sind verschiedene Begriffe. Unabhängig heißt P(F ∩ H) = P(F) · P(H). Unvereinbar heißt, dass F ∩ H leer ist, also P(F ∩ H) = 0. Hier ist P(F ∩ H) = 0,12, also nicht leer. Der Fehler steckt in Zeile 3."), g="fehler", ohne="Unabhängigkeit und Unvereinbarkeit unterscheiden: keine Regel des Katalogs trägt den Lösungsweg")
