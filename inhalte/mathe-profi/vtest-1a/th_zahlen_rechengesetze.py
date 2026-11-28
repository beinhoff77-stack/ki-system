T = "zahlen.rechengesetze"
RR, RT, RA, RG = "rr.reihenfolge", "rr.tauschen", "rr.ausmultiplizieren", "rr.gegenrechnung"
OU = "Kein Eintrag im Regelkatalog trägt das Überschlagen und Runden (id.zahlen.buendeln betrifft den Stellenwert, nicht den Überschlag)."
# Runde VT1A nach Vorprüfung W1: je Lernziel 5 Aufgaben (1 Test, 2 Korrektur, 2 Sicherung). Felder wie in th_zahlen_potenzen_basis.py.
# ═════════ klammern ═════════
neu(T, "klammern", "test", "parameter", Z(
    "In der Rechnung 483 917 − 129 486 + 37 500 wird ein Klammerpaar um 129 486 + 37 500 gesetzt. Um wie viel ist das Ergebnis mit Klammer kleiner als das Ergebnis ohne Klammer?",
    75000, "2 * 37500", lambda: (483917 - 129486 + 37500) - (483917 - (129486 + 37500)),
    "Ohne Klammer wird 129 486 abgezogen und 37 500 addiert. Mit Klammer wird die Summe abgezogen, also wird auch 37 500 abgezogen. "
    "Die 37 500 wird nicht mehr dazugezählt, sondern abgezogen; das macht zweimal 37 500 = 75 000 aus. Probe: 391 931 − 316 931 = 75 000.",
    [(37500, "Nur gesehen, dass 37 500 nicht mehr addiert wird, nicht dass sie jetzt abgezogen wird", "37500"),
     (166986, "Den Wert der Klammer genannt: 129 486 + 37 500", "129486 + 37500"),
     (0, "Gedacht, eine Klammer in einer Rechnung mit Plus und Minus ändert nichts", "0")]), regel=RR, idee="klammer_wirkung", bauplan="e", schema=False, alt=None,
    bestand="themen klammern „Jemand rechnet 30 − (10 − 4) = 30 − 10 − 4 = 16. Was ist falsch?“; rollend-12 „(48 − 12) : 6 auf zwei Wegen“",
    unterschied="Dort wird ein Term ausgerechnet oder ein Fehler benannt; hier wird die Wirkung einer Klammer über die Struktur bestimmt (eine Zahl wechselt von Plus zu Minus), Ausrechnen sechsstelliger Zahlen ist unattraktiv.")
neu(T, "klammern", "korrektur", "umkehr", Z(
    "Ein Kind rechnet Terme mit Klammern immer nach derselben falschen Regel. Es schreibt: 3 · (4 + 5) = 17, (8 − 2) · 3 = 2 und 2 · (10 − 4) = 16. Welches Ergebnis schreibt es mit seiner Regel bei (6 + 4) · (5 − 3)?",
    23, "6 + 4 * 5 - 3", lambda: 6 + 20 - 3,
    "Das Kind lässt die Klammern weg und rechnet Punkt vor Strich: 3 · 4 + 5 = 17, 8 − 2 · 3 = 2, 2 · 10 − 4 = 16. Bei (6 + 4) · (5 − 3) rechnet es also 6 + 4 · 5 − 3 = 6 + 20 − 3 = 23. "
    "Richtig ist 10 · 2 = 20.",
    [(20, "Richtig gerechnet (10 · 2 = 20) statt mit der Regel des Kindes", "(6 + 4) * (5 - 3)"),
     (47, "Nur die zweite Klammer weggelassen: (6 + 4) · 5 − 3", "(6 + 4) * 5 - 3"),
     (14, "Nur die erste Klammer weggelassen: 6 + 4 · (5 − 3)", "6 + 4 * (5 - 3)")]), form="umkehren", regel=RR, idee="fehlregel_erschliessen", bauplan="b", schema=False, alt=None,
    bestand="themen klammern „Jemand rechnet 30 − (10 − 4) = 30 − 10 − 4 = 16. Was ist falsch?“; rollend-12 „Jan berechnet (30 − 6) · 3 − 4 · 2 … erster Fehler in Zeile …“",
    unterschied="Dort wird ein einzelner Fehler benannt oder eine Zeile gesucht; hier muss aus drei Ergebnissen die falsche Regel (Klammern weglassen) erschlossen und auf einen Term mit zwei Klammern angewendet werden.")
neu(T, "klammern", "korrektur", "darstellung", W(
    "Mia hat 50 €. Sie kauft 3 Bücher zu je 9 €. Für jedes Buch bekommt sie 2 € Rabatt. Welcher Term gibt an, wie viel Geld ihr danach bleibt?",
    "50 − 3 · (9 − 2)",
    [("50 − 3 · 9 − 2", "Klammer vergessen: Der Rabatt wird nur einmal gezählt und sogar abgezogen statt gutgeschrieben (Wert 21)", 50 - 3 * 9 - 2 == 21),
     ("50 − (3 · 9 − 2)", "Den Rabatt nur einmal statt für jedes Buch gutgeschrieben (Wert 25)", 50 - (3 * 9 - 2) == 25),
     ("50 − 3 · (9 + 2)", "Den Rabatt zum Preis addiert statt abgezogen (Wert 17)", 50 - 3 * (9 + 2) == 17)],
    "Ein Buch kostet nach dem Rabatt 9 € − 2 € = 7 €. Drei Bücher kosten 3 · (9 − 2) = 21 €. Es bleiben 50 − 3 · (9 − 2) = 50 − 21 = 29 €. "
    "Die Klammer ist nötig, weil der Rabatt bei jedem Buch abgezogen wird.",
    50 - 3 * (9 - 2) == 29), form="bruecke", regel=RR, idee="modellwahl_klammer", bauplan="h", schema=True, alt=None,
    bestand="themen sach „Ein Fest: 39 Gäste zahlen je 4 € Eintritt. Davon gehen 43 € für Getränke ab. Welcher Term …?“; themen termaufbau „24 Kinder zahlen je 7 € … Welcher Term …?“",
    unterschied="Gleiches Format (Text → Term), aber die Klammer ist hier nötig, weil der Rabatt je Stück gilt; die Ablenker sind Modellfehler mit eigenem Wert. Format des Bestands, darum als Schema gezählt.")
neu(T, "klammern", "sicherung", "begruenden", W(
    "Eine Rechenkette besteht aus mindestens drei Zahlen und nur einer Rechenart, zum Beispiel 20 − 8 − 3. In eine solche Kette wird ein Klammerpaar um zwei benachbarte Zahlen gesetzt. Welche Aussage stimmt?",
    "Bei einer Kette nur mit Plus ändert die Klammer den Wert nie.",
    [("Bei einer Kette nur mit Minus ändert die Klammer den Wert nie.", "Das Verbinden beim Plus auf Minus übertragen; 20 − (8 − 3) = 15, aber 20 − 8 − 3 = 9", 20 - (8 - 3) != 20 - 8 - 3),
     ("Bei einer Kette nur mit Geteilt ändert die Klammer den Wert nie.", "Das Verbinden beim Mal auf Geteilt übertragen; 48 : (8 : 2) = 12, aber 48 : 8 : 2 = 3", 48 // (8 // 2) != 48 // 8 // 2),
     ("Bei einer Kette nur mit Mal ändert die Klammer den Wert jedes Mal.", "Gedacht, eine Klammer verändert immer etwas; (2 · 3) · 4 = 2 · (3 · 4) = 24", (2 * 3) * 4 == 2 * (3 * 4))],
    "Bei Plus darf man beliebig verbinden: (5 + 7) + 3 = 5 + (7 + 3). Bei Mal ebenso: (2 · 3) · 4 = 2 · (3 · 4), dort ändert die Klammer also nicht jedes Mal etwas. "
    "Bei Minus und Geteilt kann sie den Wert ändern: 20 − (8 − 3) = 15, aber 20 − 8 − 3 = 9; 48 : (8 : 2) = 12, aber 48 : 8 : 2 = 3.",
    all((a + b) + c == a + (b + c) for a in range(1, 9) for b in range(1, 9) for c in range(1, 9))), regel=RR, idee="verbinden_in_ketten", bauplan="f", schema=False, alt=None,
    bestand="themen vorteil „Welche Gleichung ist falsch? (69 + 8) + 5 = 69 + (8 + 5) / 69 · 8 = 8 · 69 / 69 − 8 = 8 − 69 …“; themen klammern „30 − (10 − 4) = 30 − 10 − 4. Was ist falsch?“",
    unterschied="Dort wird eine einzelne Gleichung beurteilt; hier werden allgemeine Aussagen über alle Ketten einer Rechenart geprüft (immer – nie) und mit Gegenbeispielen widerlegt.")
neu(T, "klammern", "sicherung", "darstellung", W(
    "Welcher der vier Terme hat den größten Wert? Entscheide, ohne alle Terme auszurechnen.",
    "97 · (348 + 6)",
    [("97 · 348 + 6", "Gedacht, ohne Klammer komme dasselbe heraus; hier wird aber nur 6 statt 97 · 6 dazugezählt", 97 * 348 + 6 < 97 * (348 + 6)),
     ("(97 + 348) · 6", "Gedacht, das Malnehmen am Schluss mache den Wert am größten; 445 · 6 ist aber viel kleiner", (97 + 348) * 6 < 97 * (348 + 6)),
     ("97 + 348 · 6", "Gedacht, der Term mit dem Mal hinten sei am größten; 97 + 2 088 ist viel kleiner", 97 + 348 * 6 < 97 * (348 + 6))],
    "97 · (348 + 6) = 97 · 348 + 97 · 6: Hier kommt zu 97 · 348 noch 97 · 6 dazu, bei 97 · 348 + 6 nur 6. Also ist 97 · (348 + 6) größer. "
    "Die beiden anderen Terme sind viel kleiner: (97 + 348) · 6 und 97 + 348 · 6 liegen unter 3 000, während 97 · 348 über 30 000 liegt.",
    97 * (348 + 6) > max(97 * 348 + 6, (97 + 348) * 6, 97 + 348 * 6)), regel=RR, idee="klammer_vergleich_struktur", bauplan="g", schema=False, alt=None,
    bestand="themen klammern „Stimmt die Aussage? Sind a, b und c größer als 1, dann ist (a + b) · c größer als a + b · c.“; „Bei welchem Term kommt 88 heraus?“",
    unterschied="Ähnliche Einsicht (die Klammer bewirkt, dass mehr malgenommen wird), aber eine andere Leistung: vier Terme mit großen Zahlen werden über ihre Struktur und Größenordnung verglichen statt ausgerechnet oder allgemein bestätigt.")
# ═════════ termaufbau ═════════
neu(T, "termaufbau", "test", "transfer", W(
    "Im Term (136 · 89 + 64 · 112 − 20) : 4 steht die 20 für einen Rabatt in Euro. Der Rabatt wird auf 36 € erhöht, sonst bleibt alles gleich. Wie verändert sich der Wert des Terms?",
    "Er wird um 4 kleiner, denn 16 € mehr Rabatt werden durch 4 geteilt.",
    [("Er wird um 16 kleiner, denn der Rabatt wird um 16 € größer als vorher.", "Das Teilen durch 4 vergessen", (136 * 89 + 64 * 112 - 20) // 4 - (136 * 89 + 64 * 112 - 36) // 4 != 16),
     ("Er wird um 36 kleiner, denn jetzt werden 36 € statt 20 € abgezogen.", "Den neuen Rabatt statt der Änderung genommen", (136 * 89 + 64 * 112 - 20) // 4 - (136 * 89 + 64 * 112 - 36) // 4 != 36),
     ("Er wird um 9 kleiner, denn der neue Rabatt 36 wird durch 4 geteilt.", "Nur den neuen Rabatt durch 4 geteilt statt die Änderung", (136 * 89 + 64 * 112 - 20) // 4 - (136 * 89 + 64 * 112 - 36) // 4 != 9)],
    "Der Rabatt wird um 36 − 20 = 16 € größer. Diese 16 werden zusätzlich abgezogen, bevor durch 4 geteilt wird. Also wird der Wert um 16 : 4 = 4 kleiner. "
    "Probe: (12 104 + 7 168 − 20) : 4 = 4 813 und (12 104 + 7 168 − 36) : 4 = 4 809.",
    (136 * 89 + 64 * 112 - 20) // 4 - (136 * 89 + 64 * 112 - 36) // 4 == 4 and (136 * 89 + 64 * 112 - 36) % 4 == 0), regel=RR, idee="aenderungswirkung_im_term", bauplan="e", schema=False, alt="VT1A-042",
    bestand="themen termaufbau „24 Kinder zahlen je 7 € … Der Rest wird gleich auf 4 Gruppen verteilt. Welcher Term …?“; rollend-12 „Term A 6 + 4 · 5, Term B (6 + 4) · 5 … Um wie viel ist B größer?“",
    unterschied="Dort wird ein Term aufgestellt oder ausgerechnet; hier wird die Wirkung einer Änderung über den Aufbau (Differenz im Dividenden) bestimmt. Gegenüber der früheren Fassung große Zahlen, damit Ausrechnen nicht lohnt.")
neu(T, "termaufbau", "korrektur", "darstellung", W(
    "Eine Geschichte: „Im Bus sitzen 30 Kinder. An der ersten Haltestelle steigen 6 Kinder aus, an der zweiten steigen 4 Kinder aus.“ Vier Terme stehen zur Wahl: ① 30 − 6 − 4  ② 30 − (6 + 4)  ③ 30 − 6 + 4  ④ 30 − (6 − 4). Welche Terme passen zur Geschichte?",
    "Genau ① und ②: Beide ziehen nacheinander oder zusammen 6 und 4 Kinder ab.",
    [("Genau ②: Nur bei ② fasst eine Klammer beide Haltestellen zusammen.", "Nur den Term mit Klammer für richtig gehalten (① ergibt ebenfalls 20)", 30 - 6 - 4 == 30 - (6 + 4)),
     ("Genau ① und ③: Bei ③ steht die 4 wie in der Geschichte am Schluss.", "Das Minus vor der 4 übersehen (③ ergibt 28)", 30 - 6 + 4 != 20),
     ("Genau ② und ④: Bei beiden fasst eine Klammer die Haltestellen zusammen.", "Übersehen, dass ④ nur 6 − 4 = 2 Kinder abzieht (④ ergibt 28)", 30 - (6 - 4) != 20)],
    "Insgesamt steigen 6 + 4 = 10 Kinder aus, im Bus bleiben 30 − 10 = 20 Kinder. Term ① zieht nacheinander 6 und 4 ab: 24, dann 20. Term ② zieht 6 + 4 = 10 auf einmal ab: 20. "
    "Term ③ addiert die 4 und ergibt 28, Term ④ zieht nur 6 − 4 = 2 ab und ergibt ebenfalls 28.",
    30 - 6 - 4 == 20 == 30 - (6 + 4) and 30 - 6 + 4 == 28 == 30 - (6 - 4)), regel=RR, idee="mehrere_terme_zur_geschichte", bauplan="d", schema=True, alt="VT1A-036",
    bestand="themen termaufbau „Welcher Term passt? Subtrahiere das Produkt aus 4 und 6 von 30.“; themen klammern „30 − (10 − 4) = 30 − 10 − 4. Was ist falsch?“",
    unterschied="Dort passt genau ein Term; hier passen zwei gleichwertige Terme, und die Ablenker sind Klammer- und Zeichenfehler. Weil man die vier Werte ausrechnen und mit der Geschichte vergleichen kann, zähle ich die Aufgabe im Zweifel als Schema.")
neu(T, "termaufbau", "korrektur", "umkehr", W(
    "Im Term (6 + 4) · 5 − 2 soll genau ein Rechenzeichen durch ein anderes ersetzt werden, sodass der Term ein Produkt ist, also der letzte Rechenschritt ein Malnehmen. Welche Änderung erreicht das?",
    "Das − durch · ersetzen",
    [("Das + durch · ersetzen", "Gedacht, mehr Malzeichen machen ein Produkt; (6 · 4) · 5 − 2 bleibt eine Differenz", None),
     ("Das − durch : ersetzen", "Jede Punktrechnung für ein Malnehmen gehalten; (6 + 4) · 5 : 2 ist ein Quotient", None),
     ("Das · durch + ersetzen", "Das einzige Malzeichen entfernt; (6 + 4) + 5 − 2 ist eine Differenz", None)],
    "Gerechnet wird zuerst die Klammer, dann Punkt vor Strich, Gleichrangiges von links nach rechts. Bei (6 + 4) · 5 · 2 ist der letzte Schritt das Malnehmen mit 2, der Term ist ein Produkt. "
    "Bei (6 · 4) · 5 − 2 und (6 + 4) + 5 − 2 ist der letzte Schritt das Minus (Differenz), bei (6 + 4) · 5 : 2 ist es das Teilen (Quotient).",
    (6 + 4) * 5 * 2 == 100), form="umkehren", regel=RR, idee="termart_herstellen", bauplan="c", schema=False, alt=None,
    bestand="themen termaufbau „Welche Art von Term ist (2 + 6) · 5?“; „Welcher Term ist ein Produkt, dessen erster Faktor eine Summe ist?“",
    unterschied="Dort wird die Art eines gegebenen Terms erkannt; hier wird rückwärts vom Ziel (Produkt) zur nötigen Änderung gedacht, die Ablenker sind Verwechslungen von Malzeichen, Punktrechnung und letztem Schritt.")
neu(T, "termaufbau", "sicherung", "begruenden", W(
    "Ein Kind benennt Terme nach einer falschen Regel. Es sagt: „4 + 6 · 2 ist ein Produkt, 12 : 3 − 1 ist eine Differenz, 20 − (5 + 3) ist eine Summe.“ Nach welcher Regel benennt es die Terme?",
    "Es benennt den Term nach dem Rechenzeichen, das ganz rechts steht.",
    [("Es benennt den Term nach dem Rechenzeichen, das ganz links steht.", "Nicht an allen Beispielen geprüft: Bei 4 + 6 · 2 steht links ein +, das Kind sagt aber Produkt", None),
     ("Es benennt den Term nach der Rechnung, die man zuerst ausrechnet.", "Nicht an allen Beispielen geprüft: Bei 12 : 3 − 1 rechnet man zuerst 12 : 3, das Kind sagt aber Differenz", None),
     ("Es benennt den Term nach der Rechnung, die man zuletzt ausrechnet.", "Die richtige Regel angenommen; mit ihr wäre 4 + 6 · 2 eine Summe, nicht ein Produkt", None)],
    "Prüfe jede Regel an allen drei Beispielen. Ganz rechts steht bei 4 + 6 · 2 das Malzeichen, bei 12 : 3 − 1 das Minus, bei 20 − (5 + 3) das Plus: Das passt zu Produkt, Differenz, Summe. "
    "Die anderen Regeln passen nicht zu allen drei. Richtig benannt (nach dem letzten Rechenschritt) ist 4 + 6 · 2 eine Summe und 20 − (5 + 3) eine Differenz.",
    True), regel=RR, idee="fehlregel_benennen", bauplan="b", schema=False, alt=None,
    bestand="themen termaufbau „Jemand sagt: 7 + 3 · 5 ist ein Produkt, weil ein Malzeichen vorkommt. Was ist falsch?“; rollend-5 „Kim benennt den Term 3 · (5 + 2) … erster Fehler in Zeile …“",
    unterschied="Dort wird eine einzelne falsche Benennung beurteilt; hier muss aus drei Benennungen die verborgene Regel bestimmt werden, indem vier mögliche Regeln an allen Beispielen geprüft werden.")
neu(T, "termaufbau", "sicherung", "darstellung", W(
    "Text A: „Multipliziere die Summe aus 4 und 5 mit 6.“ Text B: „Addiere das Produkt aus 4 und 6 zum Produkt aus 5 und 6.“ Welche Aussage über die Terme zu den beiden Texten stimmt?",
    "Die Terme sind verschieden, ihre Werte sind gleich.",
    [("Die Terme sind gleich, ihre Werte sind gleich.", "Gleichen Wert mit gleichem Term verwechselt: A ergibt ein Produkt, B eine Summe", (4 + 5) * 6 == 4 * 6 + 5 * 6),
     ("Die Terme sind verschieden, ihre Werte sind verschieden.", "Gedacht, verschiedene Terme müssten verschiedene Werte haben; beide ergeben 54", (4 + 5) * 6 == 54 == 4 * 6 + 5 * 6),
     ("Die Terme sind gleich, ihre Werte sind verschieden.", "Wegen derselben Zahlen 4, 5 und 6 denselben Term vermutet und beim Rechnen die Reihenfolge verwechselt", 4 + 5 * 6 != (4 + 5) * 6)],
    "Text A ergibt (4 + 5) · 6, ein Produkt. Text B ergibt 4 · 6 + 5 · 6, eine Summe. Die Terme sind also verschieden. Ihre Werte sind gleich: 9 · 6 = 54 und 24 + 30 = 54. "
    "Das zeigt das Verteilungsgesetz: Verschiedene Terme können denselben Wert haben.",
    (4 + 5) * 6 == 4 * 6 + 5 * 6), form="bruecke", regel=RR, idee="term_gegen_wert", bauplan="d", schema=False, alt=None,
    bestand="themen termaufbau „Welcher Term passt? Multipliziere die Summe aus 10 und 3 mit 6.“; rollend-12 „Term A 6 + 4 · 5, Term B (6 + 4) · 5 … Um wie viel ist B größer?“",
    unterschied="Dort wird zu einem Text ein Term gewählt oder ein Unterschied berechnet; hier werden Aufbau und Wert zweier Terme getrennt beurteilt (zwei mal zwei Urteile).")
# ═════════ vorteil ═════════
neu(T, "vorteil", "test", "parameter", Z(
    "In der Rechnung □ · 37 · △ = 3 700 stehen für □ und △ natürliche Zahlen, und □ ist kleiner als △. Wie viele verschiedene Möglichkeiten gibt es für das Paar aus □ und △?",
    4, "4", lambda: sum(1 for a in range(1, 101) for b in range(a + 1, 101) if a * 37 * b == 3700),
    "Man darf die Faktoren vertauschen: □ · 37 · △ = 37 · (□ · △). Damit 3 700 herauskommt, muss □ · △ = 100 sein. "
    "Zerlegungen von 100 mit □ kleiner als △: 1 · 100, 2 · 50, 4 · 25 und 5 · 20. Das sind 4 Möglichkeiten; 10 · 10 zählt nicht, weil □ kleiner als △ sein soll.",
    [(5, "Auch die Zerlegung mit zwei gleichen Faktoren mitgezählt, obwohl □ kleiner als △ sein soll", "4 + 1"),
     (9, "Alle Zerlegungen gezählt, auch die Paare mit □ größer als △", "9"),
     (1, "Nur eine einzige Zerlegung gefunden", "1")]), form="umkehren", regel=RT, idee="zerlegungen_nach_vertauschen", bauplan="c", schema=False, alt=None,
    bestand="themen vorteil „Ergänze: 25 · □ · 4 = 3 700“; rollend-12 „4 · □ · 25 = 1 700“",
    unterschied="Dort ist eine Lücke bei zwei bekannten Faktoren zu füllen; hier gibt es zwei Lücken, erst das Vertauschen zeigt □ · △ = 100, dann müssen alle passenden Zerlegungen gefunden werden.")
neu(T, "vorteil", "korrektur", "mehrschritt", W(
    "Ohne die Produkte auszurechnen: Welche Aussage über 36 · 4 375 · 5 und 18 · 4 375 · 10 stimmt?",
    "Sie sind gleich groß, denn 36 · 5 und 18 · 10 ergeben beide 180.",
    [("Das zweite ist größer, denn 10 ist 2 · 5, also doppelt so groß wie 5.", "Nur 10 und 5 verglichen, 36 und 18 übersehen", 36 * 4375 * 5 == 18 * 4375 * 10),
     ("Das erste ist größer, denn 36 ist 2 · 18, also doppelt so groß wie 18.", "Nur 36 und 18 verglichen, 5 und 10 übersehen", 36 * 4375 * 5 == 18 * 4375 * 10),
     ("Das lässt sich nur durch vollständiges Ausrechnen entscheiden, denn die Faktoren sind verschieden.", "Das Vertauschen und Zusammenfassen der Faktoren nicht genutzt", 36 * 5 == 18 * 10)],
    "Tausche die Faktoren: 36 · 4 375 · 5 = (36 · 5) · 4 375 = 180 · 4 375 und 18 · 4 375 · 10 = (18 · 10) · 4 375 = 180 · 4 375. Beide sind gleich groß (787 500). "
    "36 ist zwar doppelt so groß wie 18, aber 5 ist nur halb so groß wie 10.",
    36 * 4375 * 5 == 18 * 4375 * 10 == 787500), form="zwei_wege", regel=RT, idee="umordnen_und_vergleichen", bauplan="g", schema=False, alt="VT1A-043",
    bestand="themen vorteil „Rechne geschickt: 125 · 15 · 8“; rollend-5 „Du rechnest 25 · 17 · 4 geschickt …“",
    unterschied="Dort wird ein Produkt geschickt ausgerechnet; hier werden zwei Produkte durch Umordnen verglichen. Gegenüber der früheren Fassung große Zahlen, damit Ausrechnen (über 700 000) nicht lohnt.")
neu(T, "vorteil", "korrektur", "mehrschritt", Z(
    "Ein Kind rechnet 748 362 − 199 997 geschickt so: 748 362 − 200 000 − 3. Um wie viel ist sein Ergebnis zu klein?",
    6, "3 + 3", lambda: (748362 - 199997) - (748362 - 200000 - 3),
    "200 000 ist um 3 größer als 199 997. Wer 200 000 abzieht, hat also 3 zu viel abgezogen und muss 3 wieder addieren: 748 362 − 200 000 + 3. "
    "Das Kind zieht die 3 aber noch einmal ab. Damit fehlen zweimal 3, sein Ergebnis ist um 6 zu klein.",
    [(3, "Nur gesehen, dass 3 zu viel abgezogen wurden, nicht dass das Kind die 3 noch einmal abzieht", "3"),
     (0, "Den Ausgleich mit „− 3“ für richtig gehalten", "0")]), form="zwei_wege", regel=RT, idee="ausgleich_richtung", bauplan="b", schema=False, alt=None,
    bestand="themen vorteil „Rechne geschickt: 198 + 467 + 2“",
    unterschied="Dort wird ein Rechenvorteil angewendet; hier wird ein Ausgleich in die falsche Richtung erkannt und seine Wirkung bestimmt, Ausrechnen sechsstelliger Zahlen ist unattraktiv.")
neu(T, "vorteil", "sicherung", "begruenden", W(
    "In einer Rechnung sollen Zahlen umgestellt werden, damit man leichter rechnen kann, zum Beispiel bei 763 − 289 + 237. Welche Aussage stimmt?",
    "Bei nur Plus und Minus darf man umstellen, dabei nehmen die Zahlen ihre Rechenzeichen mit.",
    [("Bei nur Plus und Minus darf man umstellen, dabei bleiben die Rechenzeichen an ihrem Platz.", "Die Zeichen nicht mitgenommen: 763 − 237 + 289 = 815, richtig ist 711", 763 - 237 + 289 == 815 != 763 - 289 + 237),
     ("Sobald ein Minus vorkommt, darf man gar nicht umstellen, auch nicht mit dem Rechenzeichen.", "Das Verbot 69 − 8 ≠ 8 − 69 auf Ketten mit mitgenommenem Zeichen übertragen: 763 + 237 − 289 = 711", 763 + 237 - 289 == 763 - 289 + 237),
     ("Bei nur Mal und Geteilt darf man umstellen, dabei bleiben die Rechenzeichen an ihrem Platz.", "Die Zeichen nicht mitgenommen: 60 : 3 · 2 = 40, aber 60 : 2 · 3 = 90", 60 // 3 * 2 != 60 // 2 * 3)],
    "Jede Zahl gehört zu dem Rechenzeichen davor. Nimmt sie es beim Umstellen mit, bleibt der Wert gleich: 763 − 289 + 237 = 763 + 237 − 289 = 1 000 − 289 = 711. "
    "Bleiben die Zeichen an ihrem Platz, ändert sich der Wert: 763 − 237 + 289 = 815. Auch bei Mal und Geteilt geht das nicht: 60 : 3 · 2 = 40, aber 60 : 2 · 3 = 90.",
    763 - 289 + 237 == 763 + 237 - 289 == 711), regel=RT, idee="umstellen_mit_zeichen", bauplan="f", schema=False, alt=None,
    bestand="themen vorteil „Welche Gleichung ist falsch? … 69 − 8 = 8 − 69 …“; „Jemand rechnet 80 : 8 : 2 = 80 : 4 = 20. Was ist falsch?“",
    unterschied="Dort wird eine einzelne falsche Gleichung gefunden; hier werden Regeln für das Umstellen in Ketten (mit oder ohne Rechenzeichen) geprüft, die Ablenker sind verallgemeinerte Fehlvorstellungen.")
neu(T, "vorteil", "sicherung", "mehrschritt", Z(
    "Ein Kind soll 4 368 · 75 ausrechnen. Es rechnet stattdessen 1 456 · 25, weil es beide Faktoren durch 3 geteilt hat, und glaubt, der Wert bleibe gleich. Wievielmal so groß ist das richtige Ergebnis wie das Ergebnis des Kindes?",
    9, "3 * 3", lambda: (4368 * 75) // (1456 * 25),
    "Teilt man einen Faktor durch 3, wird das Produkt dreimal so klein. Das Kind teilt beide Faktoren durch 3, also wird das Produkt 3 · 3 = 9-mal so klein. Das richtige Ergebnis ist 9-mal so groß. "
    "Damit der Wert gleich bleibt, müsste man einen Faktor durch 3 teilen und den anderen mit 3 malnehmen.",
    [(3, "Nur eine der beiden Teilungen durch 3 berücksichtigt", "3"),
     (6, "Die beiden Faktoren 3 addiert statt malgenommen: 3 + 3", "3 + 3"),
     (1, "Dem Kind geglaubt, der Wert bleibe gleich", "1")]), form="zwei_wege", regel=RT, idee="beide_faktoren_aendern", bauplan="e", schema=False, alt=None,
    bestand="themen vorteil „Rechne geschickt: 5 · 17 · 200“ (Faktoren umordnen und zusammenfassen)",
    unterschied="Dort wird mit einer erlaubten Umformung gerechnet; hier wird die Wirkung einer unerlaubten (gleichsinnigen) Änderung beider Faktoren auf das Produkt bestimmt, ohne die Produkte auszurechnen.")
# ═════════ verteilen ═════════
neu(T, "verteilen", "test", "begruenden", W(
    "Drei der vier Rechnungen haben denselben Wert wie 368 · 47. Welche Rechnung hat einen anderen Wert?",
    "300 · 40 + 68 · 7",
    [("370 · 47 − 2 · 47", "Für anders gehalten, weil mit Minus zerlegt wird; aber 368 = 370 − 2, und beide Teile werden mit 47 malgenommen", 370 * 47 - 2 * 47 == 368 * 47),
     ("368 · 40 + 368 · 7", "Für anders gehalten, weil der zweite Faktor zerlegt wird; aber 47 = 40 + 7, und beide Teile werden mit 368 malgenommen", 368 * 40 + 368 * 7 == 368 * 47),
     ("300 · 47 + 68 · 47", "Für anders gehalten, weil 68 eine ungewöhnliche Zahl ist; aber 368 = 300 + 68, und beide Teile werden mit 47 malgenommen", 300 * 47 + 68 * 47 == 368 * 47)],
    "Beim Verteilungsgesetz wird ein Faktor zerlegt, und jeder Teil wird mit dem ganzen anderen Faktor malgenommen: 368 · 47 = 300 · 47 + 68 · 47 = 368 · 40 + 368 · 7 = 370 · 47 − 2 · 47. "
    "Bei 300 · 40 + 68 · 7 wurden beide Faktoren zerlegt und nur Teil mit Teil malgenommen; es fehlen 300 · 7 und 68 · 40. Darum ist der Wert kleiner: 12 476 statt 17 296.",
    300 * 40 + 68 * 7 == 12476 != 368 * 47 == 17296), regel=RA, idee="zerlegung_pruefen", bauplan="d", schema=False, alt=None,
    bestand="themen verteilen „Welcher Term ist gleich 3 · (10 + 3)?“; rollend-12 „8 · 27: Zerlege 27 in 20 + 7 und rechne 8 · 20 + 8 · 7“",
    unterschied="Dort wird eine einzelne Zerlegung angewendet; hier werden vier Zerlegungen (Plus, Minus, erster oder zweiter Faktor, beide Faktoren) über ihre Struktur geprüft, Ausrechnen fünfstelliger Produkte ist unattraktiv.")
neu(T, "verteilen", "korrektur", "darstellung", Z(
    "Im Produkt 2 347 · 86 wird der zweite Faktor um 3 größer, aus 86 wird 89. Um wie viel wird das Produkt größer?",
    7041, "3 * 2347", lambda: 2347 * 89 - 2347 * 86,
    "2 347 · 89 = 2 347 · (86 + 3) = 2 347 · 86 + 2 347 · 3. Das Produkt wird also um 3 · 2 347 = 7 041 größer. "
    "Am Rechteck gesehen: Es wird um einen Streifen länger, der 3 breit und 2 347 lang ist.",
    [(3, "Nur die Änderung des Faktors genannt: 89 − 86", "89 - 86"),
     (2347, "Nur einmal den ersten Faktor dazugezählt", "2347"),
     (258, "Die 3 mit 86 malgenommen statt mit 2 347", "3 * 86")]), form="bruecke", regel=RA, idee="faktor_aendern_wirkung", bauplan="e", schema=False, alt=None,
    bestand="themen verteilen „Rechne geschickt: 17 · 99 + 17“; „Rechne geschickt: 7 · 299“",
    unterschied="Dort wird ein Produkt mit dem Verteilungsgesetz ausgerechnet; hier wird nur die Wirkung einer Änderung eines Faktors bestimmt, ohne das Produkt auszurechnen.")
neu(T, "verteilen", "korrektur", "darstellung", W(
    "4 Kinder kaufen jeweils ein Eis für 2 € und ein Getränk für 3 €. Sie können die Kosten als 4 · (2 + 3) oder als 4 · 2 + 4 · 3 berechnen. Welcher Bezahlweg gehört zur Rechnung 4 · 2 + 4 · 3?",
    "Erst werden alle vier Eis bezahlt, danach alle vier Getränke.",
    [("Jedes Kind bezahlt sein Eis und sein Getränk zusammen.", "Den Weg zur anderen Rechnung 4 · (2 + 3) gewählt", None),
     ("Erst werden alle vier Eis bezahlt, danach ein Getränk für alle.", "Nur ein Getränk bezahlt; das wäre 4 · 2 + 3", 4 * 2 + 3 != 4 * 2 + 4 * 3),
     ("Erst wird ein Eis bezahlt, danach alle vier Getränke.", "Nur ein Eis bezahlt; das wäre 2 + 4 · 3", 2 + 4 * 3 != 4 * 2 + 4 * 3)],
    "4 · 2 heißt: viermal 2 € für die Eis, 4 · 3 heißt: viermal 3 € für die Getränke. Also werden erst alle Eis und dann alle Getränke bezahlt: 8 € + 12 € = 20 €. "
    "Bezahlt jedes Kind beides zusammen, rechnet man 4 · (2 + 3) = 4 · 5 = 20 €. Beide Wege ergeben dasselbe; das ist das Verteilungsgesetz.",
    4 * 2 + 4 * 3 == 4 * (2 + 3) == 20), form="bruecke", regel=RA, idee="terme_deuten", bauplan="d", schema=False, alt=None,
    bestand="themen verteilen „Ein Kino verkauft am Samstag 37 und am Sonntag 63 Karten zu je 9 €. Wie viel Geld …?“; rollend-5 „Zwei Teile eines Rechtecks: Welcher Term gibt die ganze Fläche?“",
    unterschied="Dort wird zur Situation ein Term gesucht oder ausgerechnet; hier werden zwei gleichwertige Terme nach ihrer Bedeutung (Bezahlweg) unterschieden.")
neu(T, "verteilen", "sicherung", "begruenden", Z(
    "Ein Kind wendet das Verteilungsgesetz auch an, wenn in der Klammer ein Produkt steht. Es rechnet: 2 · (3 · 5) = 60 und 3 · (2 · 4) = 72. Welches Ergebnis erhält es mit derselben Regel für 5 · (2 · 7)?",
    350, "5 * 2 * 5 * 7", lambda: 5 * 2 * 5 * 7,
    "Das Kind nimmt jeden Faktor in der Klammer mit der Zahl davor mal: 2 · 3 · 2 · 5 = 60 und 3 · 2 · 3 · 4 = 72. Bei 5 · (2 · 7) rechnet es 5 · 2 · 5 · 7 = 350. "
    "Richtig ist 5 · 14 = 70: Verteilen darf man nur über eine Summe oder Differenz; steht in der Klammer ein Produkt, wird nur einmal malgenommen.",
    [(70, "Richtig gerechnet (5 · 14 = 70) statt mit der Regel des Kindes", "5 * (2 * 7)"),
     (45, "Wie bei einer Summe verteilt und addiert: 5 · 2 + 5 · 7", "5 * 2 + 5 * 7"),
     (140, "Nur einmal zusätzlich verdoppelt: 5 · 2 · 7 · 2", "5 * 2 * 7 * 2")]), regel=RA, idee="fehlregel_verteilen_produkt", bauplan="b", schema=False, alt=None,
    bestand="themen verteilen „Jemand rechnet 6 · (20 + 4) = 6 · 20 + 4 = 124. Was ist falsch?“; rollend-12 „Nina berechnet 6 · 43 … erster Fehler in Zeile …“",
    unterschied="Andere Fehlvorstellung als im Bestand (Verteilen über ein Produkt statt nur einen Summanden malnehmen); sie muss aus zwei Ergebnissen erschlossen und angewendet werden.")
neu(T, "verteilen", "sicherung", "darstellung", W(
    "Ein Rechteck besteht aus zwei Teilrechtecken, die nebeneinander liegen und gleich hoch sind. Die Höhe wird verdreifacht, die beiden Breiten bleiben gleich. Wie verändert sich der Flächeninhalt des ganzen Rechtecks?",
    "Er wird dreimal so groß.",
    [("Er wird neunmal so groß.", "Gedacht, bei zwei Teilen wirke die Verdreifachung zweimal (3 · 3)", None),
     ("Der Flächeninhalt des breiteren Teils wird dreimal so groß, der andere bleibt.", "Übersehen, dass die Höhe in beiden Teilen vorkommt", None),
     ("Er wird um das Dreifache der Höhe größer.", "Den Zuwachs der Höhe mit dem Zuwachs der Fläche verwechselt", None)],
    "Jede Teilfläche ist Höhe mal Breite. Wird die Höhe verdreifacht, wird jede Teilfläche dreimal so groß, also auch ihre Summe. "
    "Beispiel mit Höhe 8 und Breiten 30 und 2: vorher 8 · 30 + 8 · 2 = 256, nachher 24 · 30 + 24 · 2 = 768 = 3 · 256.",
    24 * 30 + 24 * 2 == 3 * (8 * 30 + 8 * 2)), regel=RA, idee="gemeinsamer_faktor_skalieren", bauplan="e", schema=False, alt="VT1A-054",
    bestand="rollend-5 verteilen „Die Tabelle beschreibt zwei Teile eines Rechtecks, die nebeneinander liegen. Welcher Term gibt die ganze Fläche?“",
    unterschied="Dort wird ein Term zur Fläche gewählt; hier wird ohne Zahlen die Wirkung einer Änderung des gemeinsamen Faktors auf die ganze Summe beurteilt. Gegenüber der früheren Fassung ohne Zahlen, damit Ausrechnen nicht genügt.")
# ═════════ umkehraufgabe_mal ═════════
neu(T, "umkehraufgabe_mal", "test", "parameter", Z(
    "Für wie viele natürliche Zahlen a von 1 bis 12 (beide Grenzen eingeschlossen) hat die Gleichung a · x = 36 eine Lösung in den natürlichen Zahlen?",
    7, "7", lambda: sum(1 for a in range(1, 13) if 36 % a == 0),
    "Die Gleichung hat genau dann eine Lösung, wenn 36 in der Reihe von a steht, also wenn a ein Teiler von 36 ist. Die Teiler von 36 bis 12 sind 1, 2, 3, 4, 6, 9 und 12. Das sind 7 Zahlen.",
    [(6, "Den Teiler 12 nicht mitgezählt (die Grenze gilt einschließlich): 7 − 1", "7 - 1"),
     (12, "Alle Zahlen von 1 bis 12 gezählt: 13 − 1", "13 - 1"),
     (9, "Alle Teiler von 36 gezählt, auch die, die über der Grenze liegen", "9")]), form="umkehren", regel=RG, idee="loesbarkeit_teiler", bauplan="c", schema=False, alt="VT1A-057",
    bestand="themen umkehraufgabe_mal (Bonus) „Für wie viele ganze Zahlen x ist (−60) : x eine ganze Zahl, die größer als 5 ist?“",
    unterschied="Dort wird eine Divisionsaufgabe mit ganzen Zahlen durchsucht; hier wird die Lösbarkeit einer Gleichung mit Parameter als Teilbarkeit gedeutet (nur natürliche Zahlen, Grenzen eingeschlossen).")
neu(T, "umkehraufgabe_mal", "korrektur", "umkehr", Z(
    "Ein Kind löst Gleichungen immer nach derselben Regel. Es schreibt: Bei x : 7 = 3 ist x = 21. Bei 48 : x = 6 ist x = 288. Bei 60 : x = 5 ist x = 300. Welches x schreibt es mit seiner Regel bei 72 : x = 8?",
    576, "72 * 8", lambda: 72 * 8,
    "Das Kind nimmt bei jeder Geteilt-Gleichung die beiden Zahlen mal. Bei x : 7 = 3 stimmt das (x = 3 · 7 = 21). Steht x aber hinter dem Geteilt-Zeichen, ist das falsch: Bei 48 : x = 6 ist x = 48 : 6 = 8. "
    "Bei 72 : x = 8 schreibt das Kind also 72 · 8 = 576; richtig ist x = 72 : 8 = 9.",
    [(9, "Richtig gelöst (72 : 8 = 9) statt mit der Regel des Kindes", "72 // 8"),
     (64, "Die Umkehrung von Geteilt für Minus gehalten: 72 − 8", "72 - 8"),
     (80, "Die Umkehrung von Geteilt für Plus gehalten: 72 + 8", "72 + 8")]), form="umkehren", regel=RG, idee="fehlregel_divisor", bauplan="b", schema=False, alt=None,
    bestand="themen umkehraufgabe_mal „Löse 72 : x = 9“; „Stimmt die Aussage? Bei x : 8 = 5 rechnet man x = 5 : 8.“",
    unterschied="Dort wird eine Gleichung gelöst oder eine Rechenregel bestätigt; hier muss aus drei Lösungen erschlossen werden, dass das Kind nicht unterscheidet, ob x vor oder hinter dem Geteilt-Zeichen steht.")
neu(T, "umkehraufgabe_mal", "korrektur", "darstellung", W(
    "Zu welcher Geschichte gehört die Gleichung 48 : x = 6?",
    "48 Murmeln werden gleichmäßig verteilt. Jedes Kind bekommt 6. Wie viele Kinder sind es?",
    [("Jedes Kind bekommt 48 Murmeln. Es gibt 6 Kinder. Wie viele Murmeln sind es?", "Mal statt geteilt: 48 · 6", 48 * 6 != 48 // 6),
     ("Ein Kind hat 48 Murmeln und verliert 6. Wie viele Murmeln bleiben ihm übrig?", "Minus statt geteilt: 48 − 6", 48 - 6 != 48 // 6),
     ("6 Kinder teilen sich eine Zahl von Murmeln. Jedes bekommt 48. Wie viele Murmeln sind es?", "Zahlen vertauscht: x : 6 = 48", 48 * 6 != 48 // 6)],
    "48 : x = 6 heißt: 48 wird durch x geteilt, jeder Teil ist 6. Das passt zu 48 Murmeln, die gleichmäßig verteilt werden, wobei jedes Kind 6 bekommt. x = 48 : 6 = 8 Kinder. "
    "Die anderen Geschichten gehören zu 48 · 6, 48 − 6 und x : 6 = 48.",
    48 // 8 == 6), form="bruecke", regel=RG, idee="gleichung_zu_geschichte", bauplan="d", schema=True, alt="VT1A-061",
    bestand="themen umkehraufgabe_mal „Welche Gleichung passt zu: Das (−4)-Fache einer Zahl ist 28?“",
    unterschied="Umgekehrte Richtung (Gleichung → Geschichte), Ablenker vertauschen die Rollen von Gesamtzahl, Anteil und Anzahl. Weil es im Kern das Bestandsformat „Text ↔ Gleichung“ ist, zähle ich die Aufgabe als Schema.")
neu(T, "umkehraufgabe_mal", "sicherung", "parameter", W(
    "Die Gleichung a · x = 360 hat eine Lösung x in den natürlichen Zahlen. Nun wird die Zahl a verdreifacht, die 360 bleibt gleich, und die neue Gleichung hat wieder eine natürliche Lösung. Was geschieht mit der Lösung?",
    "Sie wird dreimal so klein.",
    [("Sie wird dreimal so groß.", "Gedacht, die Lösung verändere sich wie a", 12 * 30 == 360 and 30 < 90),
     ("Sie bleibt gleich.", "Gedacht, nur die 360 bestimme die Lösung", 4 * 90 == 360 and 12 * 90 != 360),
     ("Sie wird um 3 kleiner.", "Verdreifachen mit dem Abziehen von 3 verwechselt", 90 - 3 != 30)],
    "Das Produkt a · x soll 360 bleiben. Wird a dreimal so groß, muss x dreimal so klein werden, damit das Produkt gleich bleibt. "
    "Beispiel: 4 · 90 = 360, und mit 12 statt 4 ist 12 · 30 = 360; aus 90 wird 30.",
    all((360 // a) == 3 * (360 // (3 * a)) for a in range(1, 121) if 360 % (3 * a) == 0)), regel=RG, idee="parameter_wirkung", bauplan="e", schema=False, alt=None,
    bestand="themen umkehraufgabe_mal „Für welche Zahl a hat die Gleichung a · x = −48 die Lösung x = −6?“",
    unterschied="Dort wird ein Parameter aus einer gegebenen Lösung bestimmt; hier wird ohne konkrete Zahlen beurteilt, wie sich die Lösung ändert, wenn sich der Parameter ändert.")
neu(T, "umkehraufgabe_mal", "sicherung", "umkehr", W(
    "Welche der vier Gleichungen hat die größte Lösung x? Entscheide, ohne alle Gleichungen zu lösen.",
    "x : 74 = 224",
    [("74 · x = 8 288", "Gedacht, die größten Zahlen geben die größte Lösung; hier ist x = 8 288 : 74 = 112", 8288 // 74 == 112),
     ("37 · x = 8 288", "Gedacht, eine Mal-Gleichung mit der großen Zahl 8 288 habe die größte Lösung; hier ist x = 224", 8288 // 37 == 224),
     ("x : 37 = 224", "Gedacht, Teilen durch die kleinere Zahl gebe die größere Lösung; hier ist x = 224 · 37 = 8 288", 224 * 37 == 8288)],
    "Bei x : 74 = 224 ist x = 224 · 74, also mehr als 224 · 70 = 15 680. Bei x : 37 = 224 ist x = 224 · 37, nur halb so viel. "
    "Bei den Mal-Gleichungen ist x = 8 288 : 37 = 224 oder x = 8 288 : 74 = 112, also viel kleiner. Die größte Lösung hat x : 74 = 224 (x = 16 576).",
    224 * 74 == 16576 > max(8288 // 74, 8288 // 37, 224 * 37)), regel=RG, idee="loesungen_vergleichen", bauplan="g", schema=False, alt=None,
    bestand="themen umkehraufgabe_mal „Welche Rechnung führt zur Lösung von x : 6 = 27?“; „Löse 72 : x = 9“",
    unterschied="Dort wird eine Umkehrrechnung gewählt oder ausgeführt; hier werden die Lösungen von vier Gleichungen über ihre Umkehrrechnungen der Größe nach verglichen, ohne sie auszurechnen.")
# ═════════ ueberschlag ═════════
neu(T, "ueberschlag", "test", "transfer", W(
    "Drei der vier Fragen lassen sich mit einem einfachen Überschlag sicher beantworten. Bei welcher Frage muss man genau rechnen?",
    "Reichen 500 € für 26 Karten zu je 19 €?",
    [("Reichen 100 € für 4 Spiele zu je 19 €?", "Nicht gesehen, dass schon der aufgerundete Überschlag 4 · 20 = 80 € reicht; dann reicht es sicher", 4 * 19 <= 4 * 20 <= 100),
     ("Passen 6 Kisten zu je 38 kg auf einen Wagen für 300 kg?", "Nicht gesehen, dass schon 6 · 40 = 240 kg unter 300 kg liegen; aufgerundet und trotzdem darunter heißt sicher", 6 * 38 <= 6 * 40 <= 300),
     ("Reichen 400 Plätze für 9 Klassen mit je 27 Kindern?", "Nicht gesehen, dass schon 10 · 30 = 300 Kinder unter 400 liegen; aufgerundet und trotzdem darunter heißt sicher", 9 * 27 <= 10 * 30 <= 400)],
    "Rundet man alle Zahlen auf und liegt der Überschlag trotzdem unter der Grenze, reicht es sicher: 4 · 20 = 80 ist höchstens 100, 6 · 40 = 240 ist höchstens 300, 10 · 30 = 300 ist höchstens 400. "
    "Bei 26 · 19 ergibt der aufgerundete Überschlag 30 · 20 = 600, das liegt über 500 und entscheidet nichts; bei 25 · 20 = 500 ist eine Zahl ab- und eine aufgerundet. Genau gerechnet ist 26 · 19 = 494, es reicht knapp.",
    26 * 19 == 494 <= 500 < 30 * 20), regel=None, ohne=OU, idee="sicher_entscheiden", bauplan="h", schema=False, alt=None,
    bestand="themen ueberschlag „Ein Kino hat 12 Reihen mit je 28 Plätzen. Reichen die Plätze für 3 Klassen mit je 105 Kindern? Entscheide mit einem Überschlag.“",
    unterschied="Dort wird eine einzelne Frage mit einem Überschlag entschieden; hier muss beurteilt werden, wann ein Überschlag überhaupt sicher entscheidet (Rundungsrichtung und Abstand zur Grenze).")
neu(T, "ueberschlag", "korrektur", "umkehr", Z(
    "Ein Kind überschlägt Summen immer nach derselben Regel: Für 6 812 + 2 487 schreibt es 6 000 + 2 000, für 3 391 + 1 765 schreibt es 3 000 + 1 000. Welches Ergebnis hat sein Überschlag für 5 951 + 2 978?",
    7000, "5000 + 2000", lambda: (5951 // 1000) * 1000 + (2978 // 1000) * 1000,
    "Das Kind schneidet bei jeder Zahl alles hinter der Tausenderstelle ab, statt zu runden: 2 487 wird 2 000, 1 765 wird 1 000. Für 5 951 + 2 978 schreibt es also 5 000 + 2 000 = 7 000. "
    "Richtig auf Tausender gerundet wäre 6 000 + 3 000 = 9 000; das genaue Ergebnis ist 8 929.",
    [(9000, "Richtig auf Tausender gerundet statt mit der Regel des Kindes", "6000 + 3000"),
     (8929, "Genau gerechnet statt überschlagen", "5951 + 2978"),
     (8000, "Nur die erste Zahl richtig gerundet: 6 000 + 2 000", "6000 + 2000")]), form="umkehren", regel=None, ohne=OU, idee="fehlregel_abschneiden", bauplan="b", schema=False, alt=None,
    bestand="rollend-5 ueberschlag „Kim überschlägt 4 987 · 21 … Zeile 1: Ich runde 4 987 auf Tausender: 4 000 … erster Fehler in Zeile …“",
    unterschied="Dieselbe Fehlvorstellung (Abschneiden statt Runden), aber eine andere Leistung: Dort wird die Fehlerzeile gesucht, hier wird die Regel aus zwei Beispielen erschlossen und angewendet.")
neu(T, "ueberschlag", "korrektur", "mehrschritt", W(
    "Zwei Kinder überschlagen 4 812 + 3 487. Kind A rundet auf Tausender: 5 000 + 3 000. Kind B rundet auf Hunderter: 4 800 + 3 500. Das genaue Ergebnis ist 8 299. Welche Aussage stimmt?",
    "B ist genauer als A, weil feiner gerundet wurde; brauchbar sind beide.",
    [("A ist besser, weil Tausender einfacher zu rechnen sind und das Ergebnis dann genauer ist.", "Einfach mit genau verwechselt (A ergibt 8 000)", abs(8000 - 8299) > abs(8300 - 8299)),
     ("Gleich gut sind sie, weil beide auf volle Hunderter oder Tausender gerundet haben.", "Die Rundungsstelle nicht verglichen", abs(8000 - 8299) != abs(8300 - 8299)),
     ("B ist falsch, weil man bei einer Summe nur auf Tausender runden darf.", "Eine falsche Rundungsregel erfunden", 4800 + 3500 == 8300)],
    "A ergibt 5 000 + 3 000 = 8 000, B ergibt 4 800 + 3 500 = 8 300. Das genaue Ergebnis ist 8 299. B liegt nur um 1 daneben, A um 299. "
    "Je feiner man rundet, desto genauer wird der Überschlag, aber desto mehr muss man rechnen.",
    4812 + 3487 == 8299 and abs(8300 - 8299) < abs(8000 - 8299)), form="zwei_wege", regel=None, ohne=OU, idee="genauigkeit_der_rundung", bauplan="a", schema=True, alt="VT1A-067",
    bestand="rollend-5 ueberschlag „Überschlage 612 + 349 + 98. Weg A rundet auf Hunderter, Weg B auf Zehner. Um wie viel ist B größer?“",
    unterschied="Dort wird der Unterschied zweier Überschläge berechnet; hier wird die Genauigkeit beurteilt. Weil das genaue Ergebnis genannt ist, genügt Ausrechnen und Vergleichen; ich zähle die Aufgabe als Schema.")
neu(T, "ueberschlag", "sicherung", "transfer", Z(
    "Wie viele Stellen hat das Ergebnis von 6 718 · 2 493? Entscheide mit Überschlägen, ohne genau zu rechnen.",
    8, "8", lambda: len(str(6718 * 2493)),
    "6 718 liegt zwischen 6 000 und 7 000, 2 493 zwischen 2 000 und 3 000. Das Produkt liegt also zwischen 6 000 · 2 000 = 12 000 000 und 7 000 · 3 000 = 21 000 000. "
    "Beide Grenzen haben 8 Stellen, also hat auch das Ergebnis 8 Stellen (genau: 16 747 974).",
    [(7, "Beim Überschlag eine Null verloren und deshalb eine Stelle zu wenig gezählt", "8 - 1"),
     (9, "Beim Überschlag eine Null zu viel angehängt und eine Stelle zu viel gezählt", "8 + 1")]), form="anwenden", regel=None, ohne=OU, idee="groessenordnung_eingrenzen", bauplan="g", schema=False, alt=None,
    bestand="themen ueberschlag „Ein Stadion hat 18 900 Plätze. Wie oft passt eine Schule mit 612 Kindern ungefähr hinein?“",
    unterschied="Dort wird ein ungefährer Wert geschätzt; hier wird das Ergebnis mit einer unteren und einer oberen Abschätzung eingegrenzt, um eine sichere Aussage (Stellenzahl) zu erhalten.")
neu(T, "ueberschlag", "sicherung", "mehrschritt", W(
    "Ein Kind überschlägt 7 236 : 9 mit 7 000 : 10 = 700. Ist das genaue Ergebnis größer oder kleiner als 700?",
    "Größer: Beide Rundungen machen das Ergebnis des Überschlags kleiner.",
    [("Kleiner: Die 9 wurde aufgerundet, also ist der Überschlag zu groß.", "Gedacht, Aufrunden mache immer ein zu großes Ergebnis; beim Teilen durch eine größere Zahl wird es aber kleiner", 7236 // 9 > 700),
     ("Genau gleich: Die beiden Rundungen gleichen sich aus.", "Gedacht, Ab- und Aufrunden höben sich auf", 7236 / 9 != 700),
     ("Das lässt sich ohne genaue Rechnung nicht sagen: Es wurde einmal ab- und einmal aufgerundet.", "Nicht gesehen, dass beim Teilen beide Rundungen in dieselbe Richtung wirken", 7000 / 10 < 7236 / 10 < 7236 / 9)],
    "7 236 wurde auf 7 000 abgerundet: Wer weniger verteilt, bekommt je Teil weniger. 9 wurde auf 10 aufgerundet: Wer auf mehr Teile verteilt, bekommt je Teil auch weniger. "
    "Beide Rundungen machen den Überschlag kleiner, also ist das genaue Ergebnis größer als 700. Genau: 7 236 : 9 = 804.",
    7236 // 9 == 804 > 700 and 7236 % 9 == 0), form="zwei_wege", regel=None, ohne=OU, idee="richtung_beim_teilen", bauplan="g", schema=False, alt=None,
    bestand="themen ueberschlag „Stimmt die Aussage? Rundet man beim Überschlag einer Summe beide Zahlen auf, ist der Überschlag größer als das genaue Ergebnis.“; „Überschlage 4 812 : 6“",
    unterschied="Dort geht es um die Richtung bei einer Summe oder um das Bilden eines Überschlags; hier wird die Richtung beim Teilen beurteilt, wo Aufrunden des Teilers das Ergebnis kleiner macht.")
# ═════════ sach ═════════
neu(T, "sach", "test", "verknuepfen", Z(
    "Tarif A kostet 12 € Grundgebühr und 2 € für jedes Gigabyte. Tarif B kostet 4 € Grundgebühr und 4 € für jedes Gigabyte. Es werden nur volle Gigabyte berechnet. Ab wie vielen Gigabyte ist Tarif B teurer als Tarif A?",
    5, "(12 - 4) // (4 - 2) + 1", lambda: next(g for g in range(0, 100) if 4 + 4 * g > 12 + 2 * g),
    "B ist am Anfang 12 − 4 = 8 € billiger, aber jedes Gigabyte kostet bei B 4 − 2 = 2 € mehr. Nach 8 : 2 = 4 Gigabyte sind beide gleich teuer (A: 12 + 4 · 2 = 20 €, B: 4 + 4 · 4 = 20 €). "
    "Ab 5 Gigabyte ist B teurer (A: 22 €, B: 24 €).",
    [(4, "Die Zahl genannt, bei der beide gleich teuer sind: 8 : 2", "(12 - 4) // (4 - 2)"),
     (8, "Nur die Grundgebühren verglichen: 12 − 4", "12 - 4"),
     (2, "Nur die Preise je Gigabyte verglichen: 4 − 2", "4 - 2")], einheit="Gigabyte"), form="zwei_wege", regel=RG, idee="zwei_modelle_vergleichen", bauplan="h", schema=False, alt="VT1A-071",
    bestand="themen sach (Bonus) „Kinderkarten kosten 6 €, Erwachsenenkarten 10 €. 30 Personen zahlen zusammen 220 €. Wie viele Kinder?“",
    unterschied="Dort wird eine Aufteilung gesucht; hier werden zwei Kostenmodelle (Grundgebühr und Preis je Einheit) aufgestellt und der Punkt bestimmt, ab dem sich die Reihenfolge umkehrt. Gegenüber der früheren Fassung wird nach „ab wann teurer“ statt „gleich teuer“ gefragt.")
neu(T, "sach", "korrektur", "darstellung", W(
    "189 Kinder fahren mit Bussen zu einem Fest. In jeden Bus passen 52 Kinder. Es gilt 189 : 52 = 3 Rest 33. Bei welcher Frage ist die Antwort 4?",
    "Wie viele Busse werden gebraucht?",
    [("Wie viele Busse sind ganz voll besetzt?", "Den Rest nicht beachtet: 3 Busse sind voll", 189 // 52 == 3),
     ("Wie viele Kinder sitzen im letzten Bus?", "Die Antwort mit dem Rest verwechselt: im letzten Bus sitzen 33 Kinder", 189 % 52 == 33),
     ("Wie viele Plätze bleiben im letzten Bus frei?", "Die freien Plätze mit der Zahl der Busse verwechselt: 52 − 33 = 19 Plätze sind frei", 52 - 189 % 52 == 19)],
    "189 : 52 = 3 Rest 33 heißt: 3 Busse werden voll (3 · 52 = 156 Kinder), 33 Kinder bleiben übrig. Für sie braucht man einen 4. Bus. "
    "Also braucht man 4 Busse. Ganz voll sind 3 Busse, im letzten sitzen 33 Kinder, dort bleiben 52 − 33 = 19 Plätze frei.",
    -(-189 // 52) == 4), form="bruecke", regel=RG, idee="rest_deuten", bauplan="d", schema=False, alt=None,
    bestand="themen sach „Eine Klasse fährt mit dem Bus ins Museum. Der Bus kostet 420 €, jedes Kind zahlt 15 €. Welche Angabe fehlt …?“",
    unterschied="Dort wird nach einer fehlenden Angabe gefragt; hier ist die Rechnung gegeben, und der Rest einer Division muss je nach Frage verschieden gedeutet werden (aufrunden, abrunden, Rest, Ergänzung).")
neu(T, "sach", "korrektur", "umkehr", Z(
    "Ein Kind löst Zahlenrätsel rückwärts immer nach derselben Regel. Bei „Ich nehme eine Zahl mal 3 und addiere 12. Ich erhalte 45.“ schreibt es 3. Bei „Ich nehme eine Zahl mal 2 und addiere 10. Ich erhalte 30.“ schreibt es 5. "
    "Welche Zahl schreibt es bei „Ich nehme eine Zahl mal 5 und addiere 15. Ich erhalte 80.“?",
    1, "80 // 5 - 15", lambda: 80 // 5 - 15,
    "Das Kind kehrt die Schritte in der falschen Reihenfolge um: Es teilt zuerst und zieht dann ab, 45 : 3 − 12 = 3 und 30 : 2 − 10 = 5. Bei 80 rechnet es 80 : 5 − 15 = 1. "
    "Richtig wird der letzte Schritt zuerst umgekehrt: (80 − 15) : 5 = 13. Probe: 13 · 5 + 15 = 80.",
    [(13, "Richtig rückwärts gerechnet ((80 − 15) : 5 = 13) statt mit der Regel des Kindes", "(80 - 15) // 5"),
     (31, "Erst durch 5 geteilt und dann 15 addiert statt abgezogen", "80 // 5 + 15"),
     (65, "Nur 15 abgezogen und das Teilen vergessen", "80 - 15")]), form="umkehren", regel=RG, idee="fehlregel_umkehrreihenfolge", bauplan="b", schema=False, alt=None,
    bestand="rollend-5 sach „Ich denke mir eine Zahl. Ich addiere 12 und multipliziere die Summe mit 4. Dann erhalte ich 120. Rückwärts kehrst du zuerst den letzten Schritt um …“; themen „Ich multipliziere sie mit 4 und addiere 3. Ich erhalte 51.“",
    unterschied="Dort wird ein Zahlenrätsel (mit Gerüst) rückwärts gelöst; hier muss aus zwei falschen Lösungen die falsche Umkehr-Reihenfolge erschlossen und angewendet werden.")
neu(T, "sach", "sicherung", "begruenden", W(
    "Mia und Tom starten mit derselben natürlichen Zahl. Mia addiert zuerst 6 und verdoppelt dann. Tom verdoppelt zuerst und addiert dann 6. Welche Aussage über die beiden Ergebnisse stimmt?",
    "Mias Ergebnis ist immer um 6 größer als Toms.",
    [("Die Ergebnisse sind immer gleich groß.", "Die Reihenfolge der Schritte für egal gehalten", (9 + 6) * 2 != 9 * 2 + 6),
     ("Mias Ergebnis ist immer doppelt so groß wie Toms.", "Gedacht, weil Mia am Schluss verdoppelt, sei ihr Ergebnis das Doppelte", (9 + 6) * 2 != 2 * (9 * 2 + 6)),
     ("Mal ist Mias, mal Toms Ergebnis größer, je nach Startzahl.", "Gedacht, es hänge von der Startzahl ab; Mia hat aber immer 12 dazu, Tom nur 6", all((x + 6) * 2 > x * 2 + 6 for x in range(100)))],
    "Mia rechnet (Zahl + 6) · 2, das ist Zahl · 2 + 12, denn auch die 6 wird verdoppelt. Tom rechnet Zahl · 2 + 6. Beide haben das Doppelte der Zahl, Mia dazu 12, Tom nur 6. "
    "Also ist Mias Ergebnis immer um 6 größer, egal mit welcher Zahl beide starten. Beispiel mit 9: Mia 30, Tom 24.",
    all((x + 6) * 2 - (x * 2 + 6) == 6 for x in range(1000))), regel=RG, idee="reihenfolge_wirkung", bauplan="f", schema=False, alt=None,
    bestand="rollend-5 sach „Ich denke mir eine Zahl. Ich addiere 12 und multipliziere die Summe mit 4 …“",
    unterschied="Dort wird ein einzelnes Rätsel rückwärts gelöst; hier wird die Wirkung der Reihenfolge zweier Schritte für alle Startzahlen beurteilt (immer – manchmal), begründet mit dem Verteilungsgesetz.")
neu(T, "sach", "sicherung", "umkehr", W(
    "Vier Gruppen sammeln jede gleich viele Flaschen, x Flaschen je Gruppe. Dazu kommen 12 Flaschen vom Hausmeister, 4 Flaschen gehen kaputt. Am Ende sind es 108 Flaschen. Welche Gleichung beschreibt die Geschichte, und was ergibt x?",
    "4 · x + 12 − 4 = 108: Rückwärts ist 108 − 12 + 4 = 100 und 100 : 4 = 25, also x = 25.",
    [("4 · (x + 12) − 4 = 108: Rückwärts ist 108 + 4 = 112, dann 112 : 4 = 28 und 28 − 12 = 16, also x = 16.", "Die 12 Flaschen zu jeder Gruppe gezählt statt einmal dazu", 4 * (16 + 12) - 4 == 108 and 4 * 16 + 12 - 4 != 108),
     ("4 · x − 12 + 4 = 108: Rückwärts ist 108 + 12 − 4 = 116 und 116 : 4 = 29, also x = 29.", "Plus und Minus bei den 12 und den 4 vertauscht", 4 * 29 - 12 + 4 == 108 and 4 * 29 + 12 - 4 != 108),
     ("4 · x + 12 + 4 = 108: Rückwärts ist 108 − 12 − 4 = 92 und 92 : 4 = 23, also x = 23.", "Die kaputten Flaschen dazugezählt statt abgezogen", 4 * 23 + 12 + 4 == 108 and 4 * 23 + 12 - 4 != 108)],
    "Vier Gruppen mit je x Flaschen sind 4 · x. Dazu kommen 12 (plus), 4 gehen kaputt (minus): 4 · x + 12 − 4 = 108. Rückwärts: erst die 4 wieder dazu und die 12 weg, 108 − 12 + 4 = 100, dann durch 4 teilen: x = 25. "
    "Probe: 4 · 25 + 12 − 4 = 108.",
    4 * 25 + 12 - 4 == 108), regel=RG, idee="modellwahl_gleichung", bauplan="h", schema=True, alt="VT1A-076",
    bestand="themen sach „Ein Fest: 39 Gäste zahlen je 4 € Eintritt. Davon gehen 43 € für Getränke ab. Welcher Term …?“",
    unterschied="Modellwahl mit echten Modellfehlern, jede Option mit eigenem, im Modell richtig gerechnetem Ergebnis. Weil man die Geschichte auch direkt rückwärts lösen und die Option mit x = 25 suchen kann, zähle ich die Aufgabe als Schema.")
