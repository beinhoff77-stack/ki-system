T = "zahlen.potenzen_basis"
P = "rr.potenz"
# Runde VT1A nach Vorprüfung W1: je Lernziel 5 Aufgaben (1 Test, 2 Korrektur, 2 Sicherung).
# Felder je Aufgabe: bauplan (a–h laut Auftrag), schema (ja/nein, im Zweifel ja), idee (Denkfigur), alt (frühere Kennung oder None),
# bestand (nächstliegender Bestandskern), unterschied (was die Aufgabe anders macht). bauen.py schreibt daraus bestandsvergleich.md.
# ═════════ schreibweise ═════════
neu(T, "schreibweise", "test", "begruenden", W(
    "Drei der vier Potenzen haben denselben Wert wie 2²⁰. Welche Potenz hat einen anderen Wert?",
    "8⁵",
    [("4¹⁰", "Für anders gehalten, weil die Hochzahl nur halb so groß ist; aber 4 = 2 · 2, also stehen in 4¹⁰ wieder zwanzig Zweier", 4 ** 10 == 2 ** 20),
     ("32⁴", "Für anders gehalten, weil die Hochzahl viel kleiner ist; aber 32 = 2 · 2 · 2 · 2 · 2, also stehen in 32⁴ viermal fünf, also zwanzig Zweier", 32 ** 4 == 2 ** 20),
     ("1 024²", "Für anders gehalten, weil nur zwei Faktoren dastehen; aber 1 024 = 2¹⁰, also stehen in 1 024² zweimal zehn, also zwanzig Zweier", 1024 ** 2 == 2 ** 20)],
    "Zähle die Zweier. 4 = 2 · 2, also hat 4¹⁰ zehnmal zwei Zweier, das sind 20 Zweier. 32 = 2 · 2 · 2 · 2 · 2, also hat 32⁴ viermal fünf Zweier, das sind 20. "
    "1 024 = 2¹⁰, also hat 1 024² zweimal zehn Zweier, das sind 20. 8 = 2 · 2 · 2, also hat 8⁵ nur fünfmal drei Zweier, das sind 15. 8⁵ = 2¹⁵ ist kleiner als 2²⁰.",
    8 ** 5 == 2 ** 15 != 2 ** 20), regel=P, idee="faktoren_umgruppieren", bauplan="d", schema=False, alt=None,
    bestand="themen schreibweise „Schreibe 6 · 6 · 6 · 2 · 2 · 2 als eine einzige Potenz“; rollend-5 berechnen „4³ als 2⁶ (Weg B)“",
    unterschied="Dort wird eine Darstellung gebildet oder ausgerechnet; hier werden vier Darstellungen über die Zahl der Faktoren verglichen, Ausrechnen (über eine Million) ist keine Hilfe.")
neu(T, "schreibweise", "korrektur", "darstellung", W(
    "Eine Potenz hat eine ungerade Basis, zum Beispiel 3, 5 oder 7, und eine beliebige Hochzahl. Welche Aussage über den Wert der Potenz stimmt?",
    "Sie ist immer ungerade.",
    [("Sie ist gerade, wenn die Hochzahl gerade ist.", "Die Hochzahl für entscheidend gehalten; aber 3² = 3 · 3 = 9 ist ungerade", 3 ** 2 % 2 == 1),
     ("Sie ist mal gerade, mal ungerade.", "Nicht gesehen, dass nur ungerade Faktoren malgenommen werden", all(b ** n % 2 == 1 for b in (3, 5, 7, 9) for n in range(1, 9))),
     ("Sie ist immer gerade, sobald die Hochzahl größer als 1 ist.", "Gedacht, mehrere Faktoren machen eine Zahl gerade; aber 5³ = 125 ist ungerade", 5 ** 3 % 2 == 1)],
    "Eine Potenz ist ein Produkt aus lauter gleichen Faktoren. Bei einer ungeraden Basis sind alle Faktoren ungerade. Ungerade mal ungerade ergibt wieder eine ungerade Zahl (3 · 3 = 9, 9 · 3 = 27, …). "
    "Also bleibt der Wert immer ungerade, egal wie groß die Hochzahl ist.",
    all(b ** n % 2 == 1 for b in range(1, 30, 2) for n in range(1, 12))), form="bruecke", regel=P, idee="potenz_gerade_ungerade", bauplan="f", schema=False, alt=None,
    bestand="themen quadrat (Bonus) „Wie viele der Quadratzahlen 1², 2², …, 20² sind gerade?“ (andere Etappe); themen schreibweise „Was bedeutet 3²?“",
    unterschied="Dort wird gezählt oder eine Bedeutung gelesen; hier wird eine allgemeine Aussage über alle Potenzen mit ungerader Basis begründet (Produkt ungerader Faktoren). Warum kein Schema: Basis und Hochzahl sind beliebig, Beispiele widerlegen nur die Ablenker; die richtige Aussage braucht die Begründung über die Faktoren. Ersetzt 002 (B2).")
neu(T, "schreibweise", "korrektur", "umkehr", W(
    "Der Wert der Potenz 3¹² soll genau verdreifacht werden. Welche Änderung an der Potenz bewirkt das?",
    "Die Hochzahl 12 durch 13 ersetzen",
    [("Die Hochzahl 12 durch 36 ersetzen", "Gedacht: eine dreimal so große Hochzahl gibt einen dreimal so großen Wert; es kämen aber 24 Faktoren 3 dazu", 3 ** 36 != 3 * 3 ** 12),
     ("Die Basis 3 durch 9 ersetzen", "Gedacht: eine dreimal so große Basis gibt einen dreimal so großen Wert; 9¹² hat aber 24 Faktoren 3", 9 ** 12 != 3 * 3 ** 12),
     ("Die Hochzahl 12 durch 15 ersetzen", "Gedacht: verdreifachen heißt 3 zur Hochzahl addieren; das sind drei Faktoren 3 mehr, also 27-mal so viel", 3 ** 15 == 27 * 3 ** 12)],
    "3¹² ist das Produkt aus zwölf Faktoren 3. Ein Faktor 3 mehr verdreifacht den Wert: 3¹³ = 3¹² · 3. Mit der Hochzahl 15 kämen drei Faktoren 3 dazu, das ist 27-mal so viel. "
    "Mit der Hochzahl 36 oder mit der Basis 9 (9¹² = 3²⁴) kämen sogar 24 Faktoren 3 dazu.",
    3 ** 13 == 3 * 3 ** 12), form="umkehren", regel=P, idee="wirkung_hochzahl", bauplan="e", schema=False, alt=None,
    bestand="themen schreibweise „Die Zahlenfolge 3, 9, 27, 81, … Welche Zahl steht an der 6. Stelle?“",
    unterschied="Dort wird eine Folge fortgesetzt (ausrechnen); hier wird die Wirkung von Änderungen an Basis und Hochzahl verglichen, ohne die Potenz (über 500 000) auszurechnen.")
neu(T, "schreibweise", "sicherung", "begruenden", W(
    "Lea behauptet: „Eine Potenz ist immer größer als das Produkt aus ihrer Basis und ihrer Hochzahl.“ Basis und Hochzahl sind natürliche Zahlen, beide mindestens 2. Welche Antwort auf Leas Behauptung stimmt?",
    "Fast immer: Bei 2² ist das Produkt gleich groß, sonst ist die Potenz größer.",
    [("Immer: Bei einer Potenz wird mehr malgenommen als bei Basis mal Hochzahl.", "Nicht geprüft, ob es eine Ausnahme gibt; bei 2² = 4 = 2 · 2 sind beide gleich", 2 ** 2 == 2 * 2),
     ("Nie: Die Potenz und das Produkt aus Basis und Hochzahl sind gleich groß.", "Potenz mit Basis mal Hochzahl gleichgesetzt; aber 2³ = 8 und 2 · 3 = 6", 2 ** 3 != 2 * 3),
     ("Bei kleinen Zahlen nicht: Bei 2³ und 3² ist das Produkt größer.", "Falsch gerechnet: 2³ = 8 ist größer als 2 · 3 = 6, 3² = 9 ist größer als 3 · 2 = 6", 2 ** 3 > 2 * 3 and 3 ** 2 > 3 * 2)],
    "Probiere kleine Zahlen: 2² = 4 und 2 · 2 = 4, hier sind beide gleich. 2³ = 8 und 2 · 3 = 6, 3² = 9 und 3 · 2 = 6: Hier ist die Potenz größer. "
    "Wird Basis oder Hochzahl noch größer, wächst die Potenz viel schneller als das Produkt: Jeder weitere Faktor (mindestens 2) verdoppelt die Potenz mindestens, während das Produkt nur um die Basis wächst. Also stimmt Leas Satz fast immer, nur 2² ist eine Ausnahme.",
    2 ** 2 == 2 * 2 and all(a ** b > a * b for a in range(2, 12) for b in range(2, 12) if (a, b) != (2, 2))), regel=P, idee="potenz_gegen_produkt", bauplan="f", schema=False, alt=None,
    bestand="themen berechnen „Jemand rechnet 7² = 14. Was ist falsch?“ (und 9² = 18, 5³ = 15)",
    unterschied="Dort wird ein einzelner Fehler (Basis mal Hochzahl) benannt; hier wird eine allgemeine Aussage über Potenz und Produkt geprüft und die einzige Ausnahme gefunden.")
neu(T, "schreibweise", "sicherung", "darstellung", W(
    "Zu welcher Geschichte passt die Rechnung 4³?",
    "In 4 Kisten stehen je 4 Schachteln, in jeder Schachtel liegen 4 Stifte. Wie viele Stifte sind es?",
    [("In 3 Kisten stehen je 4 Schachteln, in jeder Schachtel liegen 4 Stifte. Wie viele Stifte sind es?", "Die Hochzahl 3 als Anzahl der Kisten gelesen: 3 · 4 · 4", 3 * 4 * 4 != 4 ** 3),
     ("In 4 Kisten stehen je 3 Schachteln, in jeder Schachtel liegen 3 Stifte. Wie viele Stifte sind es?", "Basis und Hochzahl vermischt: 4 · 3 · 3", 4 * 3 * 3 != 4 ** 3),
     ("In 4 Kisten stehen je 3 Schachteln, in jeder Schachtel liegt 1 Stift. Wie viele Stifte sind es?", "Basis mal Hochzahl gerechnet: 4 · 3 = 12", 4 * 3 * 1 != 4 ** 3)],
    "4³ = 4 · 4 · 4: Die 4 steht dreimal als Faktor da. Das passt zu 4 Kisten mit je 4 Schachteln mit je 4 Stiften, also 4 · 4 · 4 = 64 Stifte. "
    "Die anderen Geschichten gehören zu 3 · 4 · 4 = 48, 4 · 3 · 3 = 36 und 4 · 3 · 1 = 12.",
    4 * 4 * 4 == 4 ** 3 == 64), form="bruecke", regel=P, idee="situation_potenz", bauplan="d", schema=True, alt=None,
    bestand="themen sach „Ein Karton enthält 10 Packungen. In jeder Packung sind 10 Beutel mit je 10 Bonbons. Wie viele Bonbons?“",
    unterschied="Dort wird eine Geschichte ausgerechnet; hier wird zu einer Potenz die passende Geschichte unter Geschichten mit vertauschten Rollen von Basis und Hochzahl gewählt. Im Kern das Format „Term ↔ Text“, darum als Schema gezählt.")
# ═════════ quadrat ═════════
neu(T, "quadrat", "test", "rueckwaerts", Z(
    "Ein Quadrat ist aus gleich großen quadratischen Plättchen gelegt. Rundherum wird ein Rand gelegt, ein Plättchen breit, sodass wieder ein Quadrat entsteht. Für den Rand braucht man genau 44 Plättchen. Aus wie vielen Plättchen bestand das Quadrat vorher?",
    100, "((44 - 4) // 4) ** 2", lambda: next(n * n for n in range(1, 100) if (n + 2) ** 2 - n ** 2 == 44),
    "Hat das alte Quadrat n Plättchen je Seite, so liegen am neuen Rand an jeder der vier Seiten n Plättchen und dazu 4 Eckplättchen. Also 4 · n + 4 = 44, "
    "das heißt 4 · n = 40 und n = 10. Das alte Quadrat hatte 10 · 10 = 100 Plättchen. Probe: Das neue Quadrat hat 12 · 12 = 144 Plättchen, 144 − 100 = 44.",
    [(121, "Die Ecken vergessen: 44 : 4 = 11 Plättchen je Seite, also 11 · 11", "(44 // 4) ** 2"),
     (144, "Die Zahl der Plättchen nach dem Anlegen des Randes genannt: 12 · 12", "((44 - 4) // 4 + 2) ** 2"),
     (81, "Die Ecken doppelt abgezogen: (44 − 8) : 4 = 9, also 9 · 9", "((44 - 8) // 4) ** 2")], einheit="Plättchen"), form="umkehren", regel=P, idee="zuwachs_rueckwaerts", bauplan="c", schema=False, alt=None,
    bestand="themen quadrat „Ein Quadrat ist aus Fliesen gelegt, 15 Fliesen je Seite. Wie viele Fliesen liegen am Rand?“; rollend-12 „Plättchen im Inneren (9 · 9)“",
    unterschied="Dort wird der Rand eines bekannten Quadrats gezählt (vorwärts); hier ist nur der Zuwachs bekannt, und das alte Quadrat muss über ein selbst gebildetes Modell (4 · n + 4) erschlossen werden.")
neu(T, "quadrat", "korrektur", "darstellung", Z(
    "Ein Quadrat hat den Flächeninhalt 50 cm². Seine Seitenlänge wird verdreifacht. Wie viele cm² Flächeninhalt hat das neue Quadrat?",
    450, "50 * 3 * 3", lambda: 50 * 9,
    "Wird die Seite dreimal so lang, passen in jede Richtung dreimal so viele alte Quadrate hinein, also 3 · 3 = 9 alte Quadrate. Der neue Flächeninhalt ist 9 · 50 cm² = 450 cm². "
    "Die Seitenlänge selbst muss man dafür nicht kennen (sie ist keine natürliche Zahl).",
    [(150, "Die Fläche nur verdreifacht wie die Seite: 50 · 3", "50 * 3"),
     (300, "Die Fläche versechsfacht: 50 · 3 · 2", "50 * 3 * 2"),
     (1350, "Mit 27 malgenommen (wie beim Würfel): 50 · 3 · 3 · 3", "50 * (3 * 3 * 3)")], einheit="cm²"), form="bruecke", regel=P, idee="flaeche_skalieren", bauplan="e", schema=False, alt=None,
    bestand="themen quadrat „Ein quadratisches Muster hat 15 Felder je Seite. Wie viele Felder hat es insgesamt?“; rollend-5 „Ein Quadrat hat die Fläche 196 cm². Wie lang ist eine Seite?“",
    unterschied="Dort wird aus der Seite die Fläche (oder umgekehrt) ausgerechnet; hier ist die Seite keine natürliche Zahl, die Wirkung der Verdreifachung muss am Bild der neun Teilquadrate erkannt werden.")
neu(T, "quadrat", "korrektur", "darstellung", W(
    "Ein Kind sagt: „Ein Quadrat mit der Seitenlänge 30 cm + 7 cm ist so groß wie ein Quadrat mit 30 cm Seitenlänge und eines mit 7 cm Seitenlänge zusammen.“ "
    "Zeichne das große Quadrat und lege die beiden kleinen Quadrate in zwei gegenüberliegende Ecken. Was bleibt im großen Quadrat noch frei?",
    "Zwei Rechtecke mit 30 cm Länge und 7 cm Breite",
    [("Ein Rechteck mit 30 cm Länge und 7 cm Breite", "Nur eine der beiden freien Flächen gesehen", 2 * 30 * 7 != 30 * 7),
     ("Ein Streifen mit 37 cm Länge und 7 cm Breite", "Einen durchgehenden Streifen angenommen; die freien Flächen sind aber zwei Rechtecke 30 cm mal 7 cm", 37 * 7 != 2 * 30 * 7),
     ("Nichts, die beiden Quadrate füllen es ganz aus", "Wie das Kind gedacht, das Quadrat einer Summe sei die Summe der Quadrate", 37 * 37 != 30 * 30 + 7 * 7)],
    "Das große Quadrat hat die Seite 37 cm. Das Quadrat mit 30 cm liegt in einer Ecke, das mit 7 cm in der gegenüberliegenden Ecke. Frei bleiben zwei Rechtecke, jedes 30 cm lang und 7 cm breit. "
    "Das Kind irrt sich also um 2 · 30 · 7 = 420 cm²: 37 · 37 = 1 369, aber 30 · 30 + 7 · 7 = 949.",
    37 * 37 - 30 * 30 - 7 * 7 == 2 * 30 * 7), form="bruecke", regel=P, idee="quadrat_einer_summe_zerlegen", bauplan="d", schema=False, alt=None,
    bestand="themen quadrat „Berechne 20² − 2²“; themen berechnen „Berechne (2 + 3)² − (2² + 3²)“",
    unterschied="Dort wird der Unterschied ausgerechnet; hier wird am Flächenbild gedeutet, welche Teile beim Quadrat einer Summe fehlen, ohne zu rechnen.")
neu(T, "quadrat", "sicherung", "darstellung", W(
    "Genau eine der vier Zahlen ist keine Quadratzahl. Welche?",
    "6 727",
    [("7 396", "Gedacht, Quadratzahlen enden nicht auf 6; aber 6 · 6 = 36 endet auf 6 (7 396 = 86 · 86)", 86 * 86 == 7396),
     ("5 929", "Gedacht, ungerade Zahlen seien keine Quadratzahlen; aber 7 · 7 = 49 ist ungerade (5 929 = 77 · 77)", 77 * 77 == 5929),
     ("4 761", "Gedacht, eine Quadratzahl müsse gerade Ziffern haben oder durch 4 teilbar sein; aber 4 761 = 69 · 69", 69 * 69 == 4761)],
    "Die Endziffer einer Quadratzahl hängt nur von der Endziffer der Zahl ab, die quadriert wird: 0·0, 1·1, …, 9·9 enden auf 0, 1, 4, 9, 6, 5, 6, 9, 4, 1. Eine Quadratzahl endet also nie auf 2, 3, 7 oder 8. "
    "6 727 endet auf 7 und ist keine Quadratzahl. Die anderen sind 86 · 86 = 7 396, 77 · 77 = 5 929 und 69 · 69 = 4 761.",
    all(n * n != 6727 for n in range(1, 200))), regel=P, idee="endziffer_quadratzahl", bauplan="g", schema=True, alt="VT1A-009",
    bestand="themen quadrat „Stimmt die Aussage? Jede Quadratzahl endet auf 0, 1, 4, 5, 6 oder 9.“",
    unterschied="Dieselbe Einsicht, aber eine andere Leistung: Dort wird die Regel bestätigt, hier wird sie auf vierstellige Zahlen angewendet, deren Wurzeln man nicht kennt. Weil eine bekannte Regel angewendet wird, zähle ich die Aufgabe als Schema.")
neu(T, "quadrat", "sicherung", "begruenden", W(
    "Zwischen zwei benachbarten Quadratzahlen liegen Zahlen, zum Beispiel zwischen 9 und 16 die Zahlen 10 bis 15. Welche Aussage über die Anzahl der Zahlen dazwischen (ohne die beiden Quadratzahlen) stimmt?",
    "Die Anzahl ist immer gerade.",
    [("Die Anzahl ist immer ungerade.", "Mit dem Unterschied der beiden Quadratzahlen verwechselt (16 − 9 = 7 ist ungerade, dazwischen liegen aber 6 Zahlen)", 16 - 9 - 1 == 6),
     ("Die Anzahl ist mal gerade, mal ungerade.", "Nicht genug Beispiele geprüft: 2, 4, 6, 8, … sind alle gerade", all(((n + 1) ** 2 - n * n - 1) % 2 == 0 for n in range(1, 100))),
     ("Die Anzahl ist immer gleich.", "Nur ein Beispiel angesehen; zwischen 1 und 4 liegen 2 Zahlen, zwischen 4 und 9 liegen 4", 4 - 1 - 1 != 9 - 4 - 1)],
    "Zwischen 1 und 4 liegen 2 Zahlen, zwischen 4 und 9 liegen 4, zwischen 9 und 16 liegen 6, zwischen 16 und 25 liegen 8. Allgemein: Von n · n bis (n + 1) · (n + 1) kommt eine Reihe mit n und eine Spalte mit n + 1 Plättchen dazu, "
    "das sind n + n + 1 Zahlen mehr. Ohne die obere Quadratzahl liegen dazwischen n + n Zahlen, also immer eine gerade Anzahl.",
    all(((n + 1) ** 2 - n * n - 1) == 2 * n for n in range(1, 100))), regel=P, idee="muster_nachbarquadrate", bauplan="f", schema=False, alt=None,
    bestand="themen quadrat „Berechne 15² − 14²“; „Zwei Quadratzahlen, die direkt aufeinander folgen, unterscheiden sich um 31“",
    unterschied="Dort wird ein Unterschied ausgerechnet oder rückwärts gesucht; hier wird eine allgemeine Aussage über alle Nachbarquadrate geprüft (immer – manchmal – nie).")
# ═════════ zehner ═════════
neu(T, "zehner", "test", "parameter", Z(
    "Welche kleinste natürliche Zahl □ macht die Zahl □ · 10⁸ größer als 7 · 10¹¹ (also nicht nur gleich groß)?",
    7001, "7 * 10 ** 3 + 1", lambda: next(x for x in range(1, 10 ** 5) if x * 10 ** 8 > 7 * 10 ** 11),
    "7 · 10¹¹ = 7 · 10³ · 10⁸ = 7 000 · 10⁸, denn drei Nullen der Zehnerpotenz kann man an die 7 hängen. □ · 10⁸ ist größer als 7 000 · 10⁸, wenn □ größer als 7 000 ist. "
    "Die kleinste solche Zahl ist 7 001. Mit □ = 7 000 sind beide Zahlen gleich groß.",
    [(8, "Nur die Ziffern verglichen: 8 ist größer als 7", "7 + 1"),
     (7000, "Gleich groß statt größer gewählt: Mit 7 000 vorn sind beide Zahlen gleich", "7 * 10 ** 3"),
     (701, "Den Unterschied der Hochzahlen um eins zu klein genommen: zwei statt drei Nullen", "7 * 10 ** 2 + 1")]), form="umkehren", regel=P, idee="faktor_hochzahl_verrechnen", bauplan="g", schema=False, alt=None,
    bestand="themen zehner „Für welchen Exponenten n gilt 25 · 10ⁿ = 2 500 000?“; „4 300 000 = 43 · 10 hoch … Welcher Exponent passt?“",
    unterschied="Dort ist eine ausgeschriebene Zahl gegeben und der Exponent gesucht; hier werden zwei Zehnerpotenz-Schreibweisen ohne Ausschreiben (12 Stellen) verglichen und eine Grenze (größer, nicht gleich) bestimmt.")
neu(T, "zehner", "korrektur", "darstellung", W(
    "Eine natürliche Zahl hat genau 8 Stellen. Welche Aussage über sie stimmt für jede solche Zahl?",
    "Sie ist mindestens 10⁷ und kleiner als 10⁸.",
    [("Sie ist kleiner als 9 · 10⁷ und mindestens 10⁷.", "Die obere Grenze zu klein gewählt, als beginne jede achtstellige Zahl mit höchstens 8; aber 95 000 000 hat auch 8 Stellen", len(str(95000000)) == 8 and 95000000 > 9 * 10 ** 7),
     ("Sie ist mindestens 10⁸ und kleiner als 10⁹.", "Stellenzahl und Hochzahl gleichgesetzt; 10⁸ hat aber 9 Stellen", len(str(10 ** 8)) == 9),
     ("Sie ist mindestens 10⁶ und kleiner als 10⁷.", "Die Hochzahl um zwei zu klein genommen; 10⁷ hat schon 8 Stellen", len(str(10 ** 7)) == 8)],
    "10ⁿ ist eine 1 mit n Nullen und hat n + 1 Stellen. Die kleinste Zahl mit 8 Stellen ist 10 000 000 = 10⁷, die kleinste mit 9 Stellen ist 10⁸. "
    "Also ist jede Zahl mit 8 Stellen mindestens 10⁷ und kleiner als 10⁸.",
    all(10 ** 7 <= z < 10 ** 8 for z in (10 ** 7, 12345678, 99999999))), form="bruecke", regel=P, idee="stellenzahl_zu_zehnerpotenz", bauplan="c", schema=False, alt=None,
    bestand="themen zehner „Wie viele Nullen hat die Zahl 10⁸?“; „Ein Lichtjahr ist etwa 9 · 10¹² km. Wie viele Nullen …?“",
    unterschied="Dort wird eine Schreibweise gelesen; hier wird von der Stellenzahl auf die Lage zwischen Zehnerpotenzen geschlossen, einschließlich der Grenzen. Warum kein Schema: Die Zahl ist beliebig; ein Beispiel entscheidet nicht, ob 10⁷ und 10⁸ selbst dazugehören, dafür braucht man „10ⁿ hat n + 1 Stellen“. Ersetzt 012 (A1).")
neu(T, "zehner", "korrektur", "darstellung", W(
    "Die Zahl 7 · 10⁹ + 5 · 10⁶ + 3 · 10² wird verändert: In jedem der drei Teile wird die Hochzahl um 1 größer. Was geschieht mit der Zahl?",
    "Sie wird 10-mal so groß.",
    [("Sie wird 1 000-mal so groß.", "Für jeden der drei Teile einen Faktor 10 gerechnet: 10 · 10 · 10", 10 * (7 * 10 ** 9 + 5 * 10 ** 6 + 3 * 10 ** 2) != 1000 * (7 * 10 ** 9 + 5 * 10 ** 6 + 3 * 10 ** 2)),
     ("Sie wird um 3 größer.", "Die drei zusätzlichen Einsen der Hochzahlen zur Zahl addiert", 10 * (7 * 10 ** 9 + 5 * 10 ** 6 + 3 * 10 ** 2) != 7 * 10 ** 9 + 5 * 10 ** 6 + 3 * 10 ** 2 + 3),
     ("Sie wird um 30 größer.", "Für jeden Teil 10 dazugezählt: 10 + 10 + 10", 10 * (7 * 10 ** 9 + 5 * 10 ** 6 + 3 * 10 ** 2) != 7 * 10 ** 9 + 5 * 10 ** 6 + 3 * 10 ** 2 + 30)],
    "Eine Hochzahl mehr heißt ein Faktor 10 mehr: 7 · 10¹⁰ ist das Zehnfache von 7 · 10⁹, ebenso bei den anderen Teilen. Wird jeder Teil einer Summe zehnmal so groß, wird die ganze Summe zehnmal so groß. "
    "Jede Ziffer rückt eine Stelle nach links: aus 7 005 000 300 wird 70 050 003 000.",
    10 ** 10 * 7 + 5 * 10 ** 7 + 3 * 10 ** 3 == 10 * (7 * 10 ** 9 + 5 * 10 ** 6 + 3 * 10 ** 2)), form="bruecke", regel=P, idee="hochzahl_in_summe", bauplan="e", schema=False, alt=None,
    bestand="themen zehner „Schreibe 3 · 10⁵ + 4 · 10³ als Zahl“; „Schreibe als Zahl: 2 · 10⁶ + 7 · 10⁴ + 5 · 10“",
    unterschied="Dort wird eine solche Summe ausgeschrieben; hier wird die Wirkung einer Änderung aller Hochzahlen auf die ganze Zahl beurteilt.")
neu(T, "zehner", "sicherung", "darstellung", W(
    "Vergleiche die Zahl 9 · 10⁵ + 9 · 10⁴ + 9 · 10³ mit 10⁶. Welche Aussage stimmt?",
    "10⁶ ist um 1 000 größer.",
    [("10⁶ ist um 1 größer.", "Gedacht, die Neuner füllen alle Stellen bis zur Einerstelle: 999 999", 10 ** 6 - (9 * 10 ** 5 + 9 * 10 ** 4 + 9 * 10 ** 3) != 1),
     ("Sie sind gleich groß.", "Gedacht, drei Neuner ergeben wie beim Bündeln schon die nächste Stufe", 10 ** 6 != 9 * 10 ** 5 + 9 * 10 ** 4 + 9 * 10 ** 3),
     ("Die Summe ist größer als 10⁶.", "Gedacht, eine Summe aus drei großen Teilen sei größer als eine einzelne Zehnerpotenz", 9 * 10 ** 5 + 9 * 10 ** 4 + 9 * 10 ** 3 < 10 ** 6)],
    "9 · 10⁵ + 9 · 10⁴ + 9 · 10³ = 900 000 + 90 000 + 9 000 = 999 000. Bis 10⁶ = 1 000 000 fehlen noch 1 000. Erst mit 9 · 10² + 9 · 10 + 9 · 1 dazu käme man auf 999 999, und mit 1 mehr auf 10⁶.",
    10 ** 6 - (9 * 10 ** 5 + 9 * 10 ** 4 + 9 * 10 ** 3) == 1000), form="bruecke", regel=P, idee="stellenwert_buendeln", bauplan="g", schema=True, alt=None,
    bestand="themen zehner „Schreibe 6 · 10⁵ + 3 · 10² + 8 als Zahl und runde sie auf Tausender“",
    unterschied="Ähnliche Rechnung (Summe von Stufenzahlen ausschreiben), aber andere Frage: Vergleich mit der nächsten Zehnerpotenz und Fehlvorstellung „lauter Neuner = nächste Stufe“. Weil Ausrechnen genügt, zähle ich die Aufgabe als Schema.")
neu(T, "zehner", "sicherung", "begruenden", W(
    "Lena sagt: „Schreibt man eine Zahl der Form □ · 10ⁿ aus, hat sie genau n Nullen.“ Für □ steht eine natürliche Zahl. Welche Antwort auf Lenas Aussage stimmt?",
    "Manchmal: 50 · 10³ ist 50 000 und hat 4 Nullen.",
    [("Immer: 3 · 10² ist 300 und hat 2 Nullen.", "Aus einem Beispiel verallgemeinert, bei dem die Zahl vorn keine Null hat", 3 * 10 ** 2 == 300),
     ("Nie: 3 · 10² ist 3 000 und hat 3 Nullen.", "Falsch ausgeschrieben (eine Null zu viel) und daraus „nie“ geschlossen", 3 * 10 ** 2 != 3000),
     ("Wenn vorn die 1 steht, sonst nie: 1 · 10³ ist 1 000 und hat 3 Nullen.", "Übersehen, dass es auch mit anderen Zahlen ohne Null klappt, z. B. 3 · 10² = 300", 3 * 10 ** 2 == 300)],
    "10ⁿ hat n Nullen. Hat die Zahl vorn selbst Nullen am Ende, kommen diese dazu: 50 · 10³ = 50 000 hat 1 + 3 = 4 Nullen. Ohne Null am Ende der Zahl vorn stimmt Lenas Satz, z. B. 3 · 10² = 300. "
    "Also gilt er manchmal, aber nicht immer.",
    str(50 * 10 ** 3).count("0") == 4 and str(3 * 10 ** 2).count("0") == 2), regel=P, idee="aussage_nullen_pruefen", bauplan="f", schema=False, alt=None,
    bestand="themen zehner „Wie viele Nullen hat die Zahl 50 · 10⁴, wenn man sie ausschreibt?“",
    unterschied="Dieselbe Einsicht (die Nullen der Zahl vorn zählen mit), aber eine andere Leistung: Dort wird gezählt, hier wird eine allgemeine Aussage geprüft und mit einem Gegenbeispiel entschieden (immer – manchmal – nie).")
# ═════════ sach ═════════
neu(T, "sach", "test", "begruenden", Z(
    "Eine Pflanze hat am Anfang 2 Blätter und verdreifacht jeden Tag ihre Blätterzahl. Ein Kind will die Blätterzahl nach 6 Tagen ausrechnen und schreibt 6⁶, weil 2 · 3 = 6 ist. Wie viele Faktoren 2 stehen in der Rechnung des Kindes mehr als in der richtigen Rechnung 2 · 3 · 3 · 3 · 3 · 3 · 3?",
    5, "6 - 1", lambda: 6 - 1,
    "Richtig ist 2 · 3 · 3 · 3 · 3 · 3 · 3 = 2 · 3⁶: einmal die 2 (die Startzahl) und sechsmal die 3. Das Kind rechnet 6⁶ = (2 · 3) · (2 · 3) · (2 · 3) · (2 · 3) · (2 · 3) · (2 · 3): sechsmal die 2 und sechsmal die 3. "
    "Es hat also 6 − 1 = 5 Faktoren 2 zu viel; sein Ergebnis ist 2 · 2 · 2 · 2 · 2 = 32-mal zu groß.",
    [(6, "Vergessen, dass auch in der richtigen Rechnung die Startzahl 2 einmal vorkommt", "6"),
     (1, "Gedacht, das Kind habe nur eine 2 zu viel", "1"),
     (0, "Gedacht, 6⁶ und die richtige Rechnung enthielten gleich viele Zweier", "0")]), regel=P, idee="falsche_basis_folgen", bauplan="b", schema=False, alt=None,
    bestand="themen berechnen „Jemand rechnet 2 · 5² = 10² = 100. Was ist falsch?“; rollend-5 sach „Bakterien verdoppeln sich, 5 am Anfang, nach 4 Stunden?“",
    unterschied="Dort wird der Fehler benannt oder vorwärts gerechnet; hier wird die Folge der falschen Basis (Startzahl unter der Hochzahl) über die Zahl der Faktoren bestimmt. Nach B4 wird nach den überzähligen Faktoren gefragt, nicht mehr nach dem Verhältnis (46 656 : 1 458).")
neu(T, "sach", "korrektur", "umkehr", Z(
    "Die Zahl der Bakterien in einer Schale verdoppelt sich jede Stunde. Lea zählt 96 Bakterien. Sie weiß nicht, wie viele Stunden die Schale schon steht, aber es ist mindestens eine volle Stunde. Die Zahl verdoppelt sich immer genau zur vollen Stunde, und am Anfang war es eine natürliche Zahl von Bakterien. Wie viele verschiedene Anfangszahlen sind möglich?",
    5, "5", lambda: sum(1 for a in range(1, 96) for n in range(1, 10) if a * 2 ** n == 96),
    "Rückwärts wird jede Stunde halbiert: 96 → 48 → 24 → 12 → 6 → 3. Die 3 lässt sich nicht mehr halbieren. Nach mindestens einer Stunde kommen als Anfangszahl 48, 24, 12, 6 und 3 in Frage, "
    "das sind 5 Anfangszahlen. Die 96 selbst zählt nicht, weil schon mindestens eine Stunde vergangen ist.",
    [(6, "Die 96 selbst mitgezählt, obwohl mindestens eine Stunde vergangen ist", "5 + 1"),
     (1, "Nur eine Anfangszahl gesucht, als wäre die Zahl der Stunden bekannt", "1"),
     (4, "Die kleinste, ungerade Anfangszahl vergessen", "5 - 1")]), form="umkehren", regel=P, idee="rueckwaerts_mit_wahl", bauplan="c", schema=False, alt=None,
    bestand="rollend-12 sach „Eine Bakterienkultur verdoppelt ihre Zahl jede Stunde. Nach 8 Stunden sind es 1 280. Wie viele waren es am Anfang?“; themen sach „dreimal verdoppelt, Ergebnis 200, Anfang?“",
    unterschied="Dort ist die Zahl der Verdopplungen bekannt und es gibt genau eine Anfangszahl; hier ist sie unbekannt, und alle möglichen Anfangszahlen müssen über die Teilbarkeit durch 2 bestimmt werden.")
neu(T, "sach", "korrektur", "darstellung", W(
    "Zu welcher Geschichte passt die Rechnung 3 · 2⁵?",
    "Ein Stapel hat am Anfang 3 Blätter. Er wird 5-mal hintereinander verdoppelt.",
    [("Ein Stapel hat am Anfang 2 Blätter. Er wird 5-mal hintereinander verdreifacht.", "Startzahl und Faktor vertauscht: 2 · 3⁵", 2 * 3 ** 5 != 3 * 2 ** 5),
     ("Ein Stapel hat am Anfang 3 Blätter. Er bekommt 5-mal hintereinander 2 Blätter dazu.", "Verdoppeln als Dazulegen gedeutet: 3 + 5 · 2", 3 + 5 * 2 != 3 * 2 ** 5),
     ("Ein Stapel hat am Anfang 5 Blätter. Er wird 3-mal hintereinander verdoppelt.", "Startzahl und Hochzahl vertauscht: 5 · 2³", 5 * 2 ** 3 != 3 * 2 ** 5)],
    "In 3 · 2⁵ ist 3 die Startzahl und 2⁵ heißt: 5-mal hintereinander mal 2, also 5-mal verdoppeln. Das ergibt 3 · 32 = 96 Blätter. "
    "Die anderen Geschichten gehören zu 2 · 3⁵ = 486, zu 3 + 5 · 2 = 13 und zu 5 · 2³ = 40.",
    3 * 2 ** 5 == 96), form="bruecke", regel=P, idee="term_zu_geschichte", bauplan="d", schema=True, alt="VT1A-025",
    bestand="themen sach „Eine Zahl wird, beginnend bei 1, fünfmal verdoppelt. Welche Potenz beschreibt das Ergebnis?“",
    unterschied="Umgekehrte Richtung (Vorschlag B5): Zur Rechnung wird die Geschichte gewählt; die Ablenker vertauschen Startzahl und Faktor, deuten Verdoppeln als Dazulegen oder vertauschen Startzahl und Hochzahl (nicht mehr „6⁵“, das ist die Fehlvorstellung des Tests, B7). Im Kern das Format „Term ↔ Text“, darum als Schema gezählt.")
neu(T, "sach", "sicherung", "mehrschritt", Z(
    "Netzwerk A hat am Anfang 5 Mitglieder, Netzwerk B hat 10. Beide verdreifachen jeden Tag ihre Mitgliederzahl. Nach 20 Tagen hat Netzwerk B wievielmal so viele Mitglieder wie Netzwerk A?",
    2, "10 // 5", lambda: (10 * 3 ** 20) // (5 * 3 ** 20),
    "Nach 20 Tagen hat A genau 5 · 3²⁰ Mitglieder und B genau 10 · 3²⁰. Beide werden mit demselben Faktor 3²⁰ malgenommen. Deshalb bleibt das Verhältnis wie am Anfang: 10 : 5 = 2. "
    "Man muss 3²⁰ (fast 3,5 Milliarden) dafür nicht ausrechnen.",
    [(5, "Den Unterschied am Anfang genommen: 10 − 5", "10 - 5"),
     (20, "Die Zahl der Tage genommen", "20"),
     (3, "Den Faktor pro Tag genommen", "3")]), form="zwei_wege", regel=P, idee="verhaeltnis_bleibt", bauplan="e", schema=False, alt="VT1A-026",
    bestand="themen sach „In einer Schale sind 5 Bakterien. Alle 20 Minuten verdoppelt sich die Anzahl. Wie viele sind es nach 3 Stunden?“",
    unterschied="Dort wird ein Endwert ausgerechnet; hier ist Ausrechnen (3²⁰) nicht machbar, entscheidend ist, dass gleiches Wachstum das Verhältnis nicht ändert. Gegenüber der früheren Fassung (4 Tage, ausrechenbar) auf 20 Tage gesetzt.")
neu(T, "sach", "sicherung", "begruenden", W(
    "In Schale A sind am Anfang 100 Bakterien, und jede Stunde kommen 100 dazu. In Schale B ist am Anfang 1 Bakterium, und ihre Zahl verdoppelt sich jede Stunde. Welche Aussage über die beiden Schalen stimmt?",
    "B überholt A irgendwann und bleibt danach immer vorn.",
    [("A bleibt immer vorn, weil A mit viel mehr Bakterien anfängt.", "Nur auf den Anfang geschaut; nach 11 Stunden hat B 2 048, A nur 1 200", 2 ** 11 > 100 + 100 * 11),
     ("B überholt A, aber danach holt A wieder auf.", "Nicht gesehen, dass B danach jede Stunde um viel mehr als 100 wächst", all(2 ** n > 100 + 100 * n for n in range(11, 60))),
     ("B holt A nie ganz ein, kommt aber immer näher heran.", "Verdoppeln wie gleichmäßiges Wachsen gedacht; B überholt A nach 11 Stunden", 2 ** 11 > 100 + 100 * 11)],
    "Am Anfang ist A weit vorn. B wächst aber jede Stunde um so viel, wie es gerade hat. Sobald B mehr als 100 Bakterien hat (nach 7 Stunden sind es 128), wächst B in jeder Stunde mehr als A. "
    "Nach 10 Stunden hat A 1 100 und B 1 024, nach 11 Stunden hat A 1 200 und B 2 048: B ist vorn. Danach wächst B jede Stunde um mehr als 2 000, A nur um 100, also kann A nicht wieder aufholen.",
    next(n for n in range(60) if 2 ** n > 100 + 100 * n) == 11 and all(2 ** n > 100 + 100 * n for n in range(11, 60))), regel=P, idee="linear_gegen_verdoppeln", bauplan="f", schema=False, alt="VT1A-022",
    bestand="themen sach „Eine Seerose bedeckt 1 m². Jede Woche verdoppelt sich die Fläche. Wie viele m² nach 6 Wochen?“",
    unterschied="Dort wird ein einzelnes Wachstum vorwärts gerechnet; hier werden zwei Wachstumsarten (gleichmäßiges Dazukommen, Verdoppeln) langfristig verglichen und begründet, warum B nach dem Überholen vorn bleibt. Frühere Fassung (VT1A-022, Zahlantwort 11) war durch eine Tabelle lösbar, darum umgebaut; „Kultur“ nach C3 durch „Schale“ ersetzt.")
