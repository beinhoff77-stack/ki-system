T = "terme.aufstellen"
# ───────── struktur ─────────
a1(T, "struktur", Z(
    "Kim rechnet den Term 3 + x · 2, Sam rechnet den Term (3 + x) · 2. Beide setzen x = 4 ein. Um wie viel ist Sams Ergebnis größer als Kims Ergebnis?",
    3, "(3 + 4) * 2 - (3 + 4 * 2)", "14 - 11", "Rechne beide Terme einzeln aus. Beachte: Klammern zuerst, dann Punkt vor Strich.",
    "Kim: 3 + 4 · 2 = 3 + 8 = 11 (Punkt vor Strich). Sam: (3 + 4) · 2 = 7 · 2 = 14 (Klammer zuerst). Unterschied: 14 − 11 = 3.",
    [B("(3 + 4) * 2", "nur Sams Ergebnis angegeben"), B("3 + 4 * 2", "nur Kims Ergebnis angegeben"), B("3 * 2", "nur die Zahl 3 mit 2 malgenommen")]))
a2(T, "struktur", Z(
    "Berechne den Wert des Terms 36 : (x − 3) + 2 · x für x = 9. Beachte, welche Rechnungen zuerst kommen.",
    24, "36 / (9 - 3) + 2 * 9", "6 + 18", "Die Klammer kommt zuerst. Danach: Punktrechnung vor Strichrechnung. Zuletzt addierst du.",
    "Klammer: 9 − 3 = 6. Dann 36 : 6 = 6 und 2 · 9 = 18. Zuletzt 6 + 18 = 24.",
    [B("(36 / (9 - 3) + 2) * 9", "von links nach rechts gerechnet, ohne Punkt vor Strich"), B("36 / 9 - 3 + 2 * 9", "die Klammer nicht beachtet"), B("36 / (9 - 3 + 2 * 9)", "die Klammer zu weit gesetzt")]))
a3(T, "struktur", Z(
    "Kim berechnet für eine Zahl x den Term 2 + 3x, Sam berechnet den Term (2 + 3) · x. Für genau eine Zahl x kommen beide auf dasselbe Ergebnis. Welche Zahl ist x?",
    1, "2 / (5 - 3)", "1", "Fasse Sams Term zusammen: (2 + 3) · x. Wie viele x hat jeder Term, und was bleibt übrig?",
    "Sams Term ist 5x. Kims Term ist 3x + 2. Beide sind gleich, wenn 3x + 2 = 5x ist. Das ist 2 = 2x, also x = 1. Probe: 2 + 3 · 1 = 5 und (2 + 3) · 1 = 5.",
    [B("5 - 3", "den Unterschied 5x − 3x = 2 als Lösung genommen"), B("2 / 5", "2 durch 5 geteilt"), B("2 + 3", "die beiden Zahlen addiert")]), g="pruefung")
# ───────── termwert ─────────
a1(T, "termwert", Z(
    "Ein Handyvertrag kostet 5 € Grundgebühr im Monat und 0,05 € für jede Minute. Der Preis in Euro ist 5 + 0,05 · m, wobei m die Zahl der Minuten ist. Wie viel Euro kostet der Vertrag bei m = 120 Minuten?",
    11, "5 + 0.05 * 120", "5 + 6", "Setze m = 120 ein. Rechne Punktrechnung vor Strichrechnung.",
    "5 + 0,05 · 120 = 5 + 6 = 11. Der Vertrag kostet 11 €.",
    [B("(5 + 0.05) * 120", "die Grundgebühr mit der Zahl der Minuten malgenommen"), B("5 + 0.05 + 120", "alle Zahlen addiert"), B("5 * 120 + 0.05", "die Grundgebühr mit 120 malgenommen")], "€"))
a2(T, "termwert", Z(
    "Alex hat auf einem Konto 50 €. Das Guthaben in Euro wird nach t Wochen durch den Term 50 − 4 · (t + 2) angegeben. Wie viel Euro sind es nach t = 3 Wochen?",
    30, "50 - 4 * (3 + 2)", "50 - 20", "Die Klammer kommt zuerst. Dann die Multiplikation, zuletzt die Subtraktion.",
    "Klammer: 3 + 2 = 5. Dann 4 · 5 = 20. Dann 50 − 20 = 30. Alex hat 30 €.",
    [B("50 - 4 * 3 + 2", "die Klammer weggelassen"), B("(50 - 4) * (3 + 2)", "zuerst 4 vom Guthaben abgezogen und dann mit der Klammer malgenommen"), B("50 - 4 * 3 - 2", "die Klammer als Minus 3 minus 2 gelesen")], "€"))
a3(T, "termwert", Z(
    "Aus einem Tank laufen Liter ab. Nach t Minuten sind noch 120 − 3 · (2t + 5) Liter im Tank. Nach wie vielen Minuten sind noch genau 63 Liter im Tank?",
    7, "((120 - 63) / 3 - 5) / 2", "(19 - 5) / 2", "Setze den Term gleich 63. Arbeite von außen nach innen rückwärts: Was kommt zuletzt, was zuerst?",
    "120 − 3 · (2t + 5) = 63. Dann 3 · (2t + 5) = 57, also 2t + 5 = 19, 2t = 14 und t = 7. Probe: 2 · 7 + 5 = 19, 3 · 19 = 57, 120 − 57 = 63.",
    [B("(120 - 63) / 3 - 5", "durch 2 nicht geteilt"), B("(120 - 63) / 3 / 2", "die 5 nicht abgezogen"), B("(120 - 63) / 3", "nur durch 3 geteilt")], "Minuten"), g="rueckwaerts")
# ───────── uebersetzen ─────────
a1(T, "uebersetzen", Z(
    "Kim denkt sich die Zahl 8. Sie bildet die Summe aus dem Doppelten dieser Zahl und 7. Welches Ergebnis erhält Kim?",
    23, "2 * 8 + 7", "16 + 7", "Übersetze Wort für Wort: das Doppelte der Zahl heißt 2 mal die Zahl. Dazu kommt 7.",
    "Das Doppelte von 8 ist 2 · 8 = 16. Die Summe aus 16 und 7 ist 23. Als Term: 2x + 7 mit x = 8.",
    [B("2 + 8 + 7", "nur addiert, das Doppelte nicht gerechnet"), B("2 * (8 + 7)", "die Summe verdoppelt statt nur die Zahl"), B("2 * 8 * 7", "malgenommen statt addiert")]))
a2(T, "uebersetzen", Z(
    "Kim übersetzt: „Das Doppelte der Differenz aus x und 4, dazu das Dreifache von x.“ Welchen Wert hat der Term für x = 10?",
    42, "2 * (10 - 4) + 3 * 10", "12 + 30", "Die Differenz aus x und 4 heißt x − 4 (in dieser Reihenfolge). Davon das Doppelte braucht eine Klammer.",
    "Term: 2 · (x − 4) + 3x. Für x = 10: 2 · 6 + 30 = 12 + 30 = 42.",
    [B("2 * 10 - 4 + 3 * 10", "die Klammer weggelassen"), B("2 * (4 - 10) + 3 * 10", "die Differenz in falscher Reihenfolge gebildet"), B("2 * (10 - 4) * 3 * 10", "die beiden Teile malgenommen statt addiert")]))
a3(T, "uebersetzen", Z(
    "Ein Rechteck ist x cm breit. Die Länge ist 5 cm länger als das Doppelte der Breite. Der Umfang beträgt 70 cm. Wie breit ist das Rechteck in Zentimetern?",
    10, "(70 - 10) / 6", "(70 / 2 - 5) / 3", "Schreibe die Länge als Term mit x. Stelle den Umfang 2 · (Breite + Länge) auf.",
    "Länge: 2x + 5. Umfang: 2 · (x + 2x + 5) = 2 · (3x + 5) = 6x + 10. Aus 6x + 10 = 70 folgt 6x = 60 und x = 10. Probe: Länge 25 cm, Umfang 2 · (10 + 25) = 70.",
    [B("(70 - 10) / 3", "6x = 60 nur durch 3 geteilt"), B("70 - 10", "das Ergebnis 60 = 6x als Breite angegeben"), B("70 / 2 - 5", "vom halben Umfang nur 5 abgezogen")], "cm"), g="rueckwaerts")
# ───────── sachsituation ─────────
a1(T, "sachsituation", Z(
    "Ein Lieferdienst berechnet 2,50 € Liefergebühr und 8 € für jede Pizza. Wie viel Euro kosten 3 Pizzen mit Lieferung?",
    26.5, "2.5 + 8 * 3", "24 + 2.5", "Die Liefergebühr zahlt man nur einmal. Die 8 € zahlt man für jede Pizza.",
    "Die Pizzen kosten 3 · 8 = 24 €. Dazu kommt die Liefergebühr 2,50 €. Zusammen 24 + 2,50 = 26,50 €. Als Term: 2,5 + 8 · x mit x = 3.",
    [B("(2.5 + 8) * 3", "die Liefergebühr dreimal bezahlt"), B("2.5 * 3 + 8", "die Liefergebühr mit 3 malgenommen und nur eine Pizza gerechnet"), B("2.5 + 8 + 3", "alle Zahlen addiert")], "€"))
a2(T, "sachsituation", Z(
    "Auf Kims Sparbuch liegen 120 €. Jede Woche kommen 15 € dazu. Nach der 4. Woche werden einmal 30 € abgehoben. Wie viel Euro sind nach 8 Wochen auf dem Sparbuch?",
    210, "120 + 15 * 8 - 30", "120 + 120 - 30", "Wie oft kommen 15 € dazu? Die 30 € werden nur einmal abgehoben.",
    "Einzahlungen: 8 · 15 = 120 €. Startbetrag 120 €. Eine Abhebung: −30 €. Gesamt: 120 + 120 − 30 = 210 €.",
    [B("120 + 15 * 8", "die Abhebung vergessen"), B("(120 + 15) * 8 - 30", "den Startbetrag mit 8 malgenommen"), B("120 + 15 + 8 - 30", "die Zahlen einfach addiert")], "€"))
a3(T, "sachsituation", Z(
    "Eine Kletterhalle hat zwei Angebote. Gruppenkarte: 36 € Grundpreis und 4 € je Person. Einzelkarten: 10 € je Person. Ab wie vielen Personen ist die Gruppenkarte günstiger als die Einzelkarten?",
    7, "36 / (10 - 4) + 1", "6 + 1", "Stelle für beide Angebote einen Term auf. Wann sind beide gleich teuer? Ab wann ist die Gruppenkarte günstiger?",
    "Gruppe: 36 + 4n. Einzeln: 10n. Gleich teuer: 36 + 4n = 10n, also 36 = 6n und n = 6. Bei 6 Personen kosten beide gleich viel (60 €). Erst bei 7 Personen ist die Gruppenkarte günstiger (64 € gegen 70 €).",
    [B("36 / (10 - 4)", "die Personenzahl genannt, bei der beide Angebote gleich teuer sind"), B("36 / 4", "nur durch 4 geteilt"), B("36 / (10 - 4) - 1", "eine Person zu wenig genommen")], "Personen"), g="verknuepfen")
# ───────── muster ─────────
a1(T, "muster", Z(
    "Eine Folge von Figuren aus Plättchen: Figur 1 hat 5 Plättchen, Figur 2 hat 9 Plättchen, Figur 3 hat 13 Plättchen. So geht es weiter. Wie viele Plättchen hat Figur 15?",
    61, "4 * 15 + 1", "5 + 4 * 14", "Um wie viele Plättchen wird es von Figur zu Figur mehr? Prüfe deinen Term mit Figur 1.",
    "Es kommen immer 4 Plättchen dazu. Der Term ist 4n + 1. Probe: n = 1 gibt 5, n = 2 gibt 9, n = 3 gibt 13. Für n = 15: 4 · 15 + 1 = 61 Plättchen.",
    [B("5 + 4 * 15", "die 4 Plättchen 15-mal dazugerechnet, obwohl Figur 1 schon 5 hat"), B("15 * 5", "15 mal die Zahl der Plättchen von Figur 1"), B("13 + 15", "zu Figur 3 einfach 15 addiert")], "Plättchen"))
a2(T, "muster", Z(
    "Im Kursraum werden Tische in einer Reihe zusammengeschoben. An einem Tisch sitzen 4 Kinder, an zwei zusammengeschobenen Tischen 6 Kinder, an drei Tischen 8 Kinder. So geht es weiter. Für 30 Kinder wird eine Tischreihe gebraucht. Wie viele Tische müssen zusammengeschoben werden?",
    14, "(30 - 2) / 2", "28 / 2", "Wie viele Plätze kommen mit jedem weiteren Tisch dazu? Stelle den Term für n Tische auf.",
    "Mit jedem Tisch kommen 2 Plätze dazu. Der Term ist 2n + 2. Probe: n = 1 gibt 4, n = 2 gibt 6. Aus 2n + 2 = 30 folgt 2n = 28 und n = 14 Tische.",
    [B("30 / 2", "die 2 Plätze am Anfang vergessen"), B("30 - 2", "den Wert 28 als Zahl der Tische angegeben"), B("30 / 4", "durch die 4 Plätze am ersten Tisch geteilt")], "Tische"))
a3(T, "muster", Z(
    "Zwei Muster aus Plättchen: Muster A hat bei Figur n genau 4n + 2 Plättchen. Muster B hat bei Figur n genau 6n − 4 Plättchen. Bei welcher Figur haben beide Muster gleich viele Plättchen?",
    3, "(2 + 4) / (6 - 4)", "6 / 2", "Setze die beiden Terme gleich. Bringe alle Glieder mit n auf eine Seite.",
    "4n + 2 = 6n − 4. Auf beiden Seiten 4n abziehen: 2 = 2n − 4. Dann 4 addieren: 6 = 2n, also n = 3. Probe: 4 · 3 + 2 = 14 und 6 · 3 − 4 = 14.",
    [B("2 + 4", "den Wert 6 = 2n nicht durch 2 geteilt"), B("6 - 4", "den Unterschied der Zahlen vor n als Lösung genommen"), B("6 + 4", "die Zahlen von Muster B addiert")]), g="pruefung")
# ───────── deuten ─────────
a1(T, "deuten", Z(
    "Der Term 40 − 5t gibt an, wie viele Kilometer noch bis zum Ziel fehlen, wenn eine Wandergruppe t Stunden unterwegs ist. Wie viele Kilometer wandert die Gruppe in jeder Stunde?",
    5, "5", "40 - 35", "Wie ändert sich der Term, wenn t um 1 größer wird? Was bedeutet die Zahl vor dem t?",
    "Wenn t um 1 wächst, wird 5t um 5 größer und der Term um 5 kleiner. Die Zahl vor dem t zählt pro Stunde: Die Gruppe wandert 5 km in jeder Stunde. Die 40 ist die Strecke am Anfang.",
    [B("40", "die Strecke am Anfang als Tempo genommen"), B("40 / 5", "die Dauer der ganzen Wanderung angegeben"), B("40 - 5", "die Zahlen subtrahiert")], "km"))
a2(T, "deuten", Z(
    "Die Höhe einer Kerze in Zentimetern ist nach t Stunden 24 − 2t. Nach wie vielen Stunden ist die Kerze ganz abgebrannt?",
    12, "24 / 2", "24 - 2 * 12 + 12", "Die Kerze ist abgebrannt, wenn ihre Höhe 0 ist. Wann ist 24 − 2t gleich 0?",
    "24 − 2t = 0 heißt 2t = 24, also t = 12. Nach 12 Stunden ist die Höhe 0. Probe: 24 − 2 · 12 = 0.",
    [B("24 - 2", "die beiden Zahlen subtrahiert"), B("24 * 2", "die beiden Zahlen malgenommen"), B("24 / 2 + 24", "zur Lösung noch die Anfangshöhe addiert")], "Stunden"))
a3(T, "deuten", Z(
    "Kim übersetzt „das Doppelte der Summe aus x und 3“ in den Term 2x + 3. Der richtige Term ist 2 · (x + 3). Um wie viel unterscheiden sich die beiden Werte für x = 5?",
    3, "2 * (5 + 3) - (2 * 5 + 3)", "16 - 13", "Berechne beide Terme einzeln für x = 5. Was wird bei Kims Term nur einmal und was zweimal gerechnet?",
    "Kims Term: 2 · 5 + 3 = 13. Richtiger Term: 2 · (5 + 3) = 16. Unterschied: 16 − 13 = 3. Der Fehler: Im richtigen Term wird auch die 3 verdoppelt, bei Kim nicht.",
    [B("2 * (5 + 3)", "nur den richtigen Wert angegeben"), B("2 * 5 + 3", "nur Kims Wert angegeben"), B("2 * 3", "die Verdopplung der 3 als Unterschied angegeben")]), g="fehler")
