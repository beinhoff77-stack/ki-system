# Runde vtest-3 (VT3) – Verstehen in Tests, Stufe 1

126 neue Aufgaben (VT3-001 … VT3-126), nichts eingespielt. 18 Verstehens-Lernziele laut `inhalte/mathe-profi/vtest-1/auswahl.json`, keine Abweichung (siehe `auswahl.md`). Je Lernziel: 1 `test` (`ersetzt_test`), 3 `korrektur`, 3 `sicherung`.

Dateien: `auswahl.md`, fünf Aufgabendateien `<einheit>.json`, Bauskript `bauen.py` mit `kern.py`, `ideen.py` und `e_*.py` (Quelltexte), `gegenrechnung.py`, `sonderfaelle.md`, `bestandsvergleich.md`, `korrektur-nach-vorpruefung.md`, `korrektur-nach-vorpruefung-2.md` und `korrektur-nach-vorpruefung-3.md` und `korrektur-nach-gegenpruefung.md` (Überarbeitungen), `vorpruefung*.md` (Berichte der Vorprüfer, nur zum Nachlesen). Jede Aufgabe trägt ein Zusatzfeld `idee` (Denkfigur: Kategorie | Kurzbeschreibung).

## Zahlen

| Einheit | Lernziele | Aufgaben |
|---|---|---|
| messen.volumen (M6 2) | quader, liter, rueckwaerts, verstehen | 28 |
| daten.darstellen (M6 3) | relative_haeufigkeit, saeulendiagramm, irrefuehrend | 21 |
| daten.kennwerte (M6 3) | mittelwert, mittel_rueckwaerts | 14 |
| funktionen.grundbegriffe (M8 1) | mengen, stelle, graph_lesen, punkt_graph, sachzusammenhang | 35 |
| geometrie.winkel (M5 2) | kreuzung, uhr, figuren, verstehen | 28 |
| **zusammen** | 18 | **126** |

- Pool: test 18 · korrektur 54 · sicherung 54.
- Stufe: 3 → 52 (alle 18 Tests, 34 Sicherungen), 2 → 74.
- Antwortform: zahl 37 · auswahl 63 · luecken 26 (keine Toleranz).
- Typ: begruenden 48 · transfer 19 · fehler 19 · darstellung 14 · umkehr 12 · parameter 10 · verknuepfen 3 · rueckwaerts 1.
- Form: ohne 74 · fehler_detektiv 19 · anwenden 18 · umkehren 10 · bruecke 3 · verfahren_waehlen 2. Fehler-Detektive: 18 als Lücken („Zeile □, richtig □“), 1 als Auswahl mit vier Zeilen und Optionen aus Zeile + Begründung (VT3-114).

## Ideen je Lernziel (Feld `idee`, Kategorie vor dem Strich)

Fest geprüft in `bauen.py` (Abbruch bei Verstoß): je Lernziel mindestens 5 verschiedene Denkfiguren, keine mehr als zweimal. Die Kategorie beschreibt, was beim Lösen gedacht werden muss, nicht das Aufgabenformat. Die beiden Lernziele „verstehen“ werden getrennt gezählt. Nach Vorprüfung 3 hat jedes Lernziel 6 oder 7 Kategorien. Zusätzlich wurde in Vorprüfung 3 der Inhalt geprüft: Wo mehrere Aufgaben formal verschieden etikettiert, aber dieselbe Einsicht waren (saeulendiagramm: Maßstab, figuren: Zerlegung des rechten Winkels, mittelwert/mittel_rueckwaerts: Summenänderung), wurde eine Aufgabe durch eine mit anderem Gedanken ersetzt. Inhaltlich verschieden sind jetzt: saeulendiagramm 6 (Faktor beim Neuzeichnen, Umrechnen Höhe und Wert, Maßstab wählen, Verhältnis unabhängig vom Maßstab, Vergleich verschiedener Maßstäbe, gestapelte Säule), figuren 6 (Verhältnis-Zerlegung, Torte/Vollwinkel, Bruchteile verschiedener Winkel, Quadrat auf einer Geraden, mindestens ein kleiner Teilwinkel, gedrehte Quadrate), mittelwert 7 (Rückwärtsrechnen nach Verdreifachen, Nullen zählen mit, Rechenfehler Teiler, Gesamtmittel näher an der größeren Gruppe, ein Wert gleich dem Mittelwert ändert nichts, gleichmäßiger Zuwachs, Ausreißer), mittel_rueckwaerts 7 (Zahl der Mädchen aus Mittelwerten, Abstände gleichen sich aus, Läuferin, „mindestens eine Zahl“, Abweichungen von 100, Summe ändert sich plus und minus, Streichen der größten Zahl). Nach Urteil 1222 sind die Kategorien neu gezählt (Tabelle unten): 012, 013, 021, 040, 041, 049, 068, 074, 077, 086, 099, 100, 106, 113 und 122 haben einen neuen Gedanken oder eine neue Fassung; die Kategorie „darstellung“ ist in liter und saeulendiagramm weggefallen, dafür kamen immer_nie, gegenbeispiel und pruefen hinzu.

| Lernziel | Kategorien | Verteilung |
|---|---|---|
| quader | 6 | transfer 2, fehler, groessenvergleich, rechnung_waehlen, was_waere_wenn, zusammenhang |
| liter | 7 | begruenden, bruecke, fehler, immer_nie, pruefen, transfer, zusammenhang |
| rueckwaerts | 7 | fehler, gegenbeispiel, groessenvergleich, rechnung_waehlen, umkehr, was_waere_wenn, zusammenhang |
| verstehen (Volumen) | 7 | begruenden, fehler, groessenvergleich, transfer, umkehr, was_waere_wenn, zusammenhang |
| relative_haeufigkeit | 7 | darstellung, fehler, groessenvergleich, immer_nie, pruefen, umkehr, zusammenhang |
| saeulendiagramm | 7 | begruenden, fehler, gegenbeispiel, mengen_deuten, pruefen, rechnung_waehlen, was_waere_wenn |
| irrefuehrend | 6 | darstellung 2, begruenden, fehler, groessenvergleich, pruefen, zwei_wege |
| mittelwert | 6 | zusammenhang 2, begruenden, fehler, groessenvergleich, mengen_deuten, umkehr |
| mittel_rueckwaerts | 7 | begruenden, darstellung, fehler, gegenbeispiel, umkehr, was_waere_wenn, zusammenhang |
| mengen | 6 | mengen_deuten 2, begruenden, fehler, gegenbeispiel, immer_nie, umkehr |
| stelle | 6 | umkehr 2, begruenden, fehler, immer_nie, transfer, zusammenhang |
| graph_lesen | 6 | begruenden 2, darstellung, fehler, gegenbeispiel, pruefen, zusammenhang |
| punkt_graph | 7 | bruecke, darstellung, fehler, immer_nie, pruefen, umkehr, zusammenhang |
| sachzusammenhang | 6 | transfer 2, darstellung, fehler, gegenbeispiel, pruefen, was_waere_wenn |
| kreuzung | 7 | begruenden, darstellung, fehler, immer_nie, transfer, umkehr, zusammenhang |
| uhr | 7 | fehler, groessenvergleich, immer_nie, pruefen, transfer, umkehr, zusammenhang |
| figuren | 6 | fehler 2, begruenden, groessenvergleich, immer_nie, transfer, umkehr |
| verstehen (Winkel) | 6 | begruenden 2, fehler, immer_nie, transfer, umkehr, was_waere_wenn |

## Rechnen nach Schema (streng, nach Urteil 1222: 37 von 126, höchstens 2 je Lernziel)

Maßstab (Urteil 1222): schema-nah ist jede Aufgabe, die man durch bloßes Ausrechnen oder Einsetzen löst, auch ein Zahlenvergleich oder ein Fehler-Detektiv, dessen Fehler man durch Nachrechnen findet. Ziel: höchstens zwei je Lernziel; die übrigen Aufgaben des Lernziels brauchen verschiedene Denkfiguren (mindestens fünf, keine mehr als zweimal, siehe oben). Die Gegenprüfung zählte vorher je Lernziel in der Reihenfolge der Kennungen 2 / 4 / 3 / 2 / 2 / 4 / 1 / 2 / 2 / 2 / 3 / 2 / 3 / 2 / 2 / 2 / 2 / 2; über zwei lagen liter, rueckwaerts, saeulendiagramm, stelle und punkt_graph. Dort habe ich so viele Routinen durch Aufgaben mit anderem Gedanken ersetzt, dass jedes Lernziel höchstens zwei hat (liter 012, 013; rueckwaerts 021; saeulendiagramm 040, 041; stelle 074, 077; punkt_graph 086). Meine eigene strenge Zählung (die der Gegenprüfung kann in Einzelfällen anders ausfallen):

| Lernziel | schema-nah | Aufgaben |
|---|---|---|
| quader | 2 | 001, 004 |
| liter | 2 | 010, 011 |
| rueckwaerts | 2 | 015, 016 |
| verstehen (Volumen) | 2 | 022, 024 |
| relative_haeufigkeit | 2 | 029, 031 |
| saeulendiagramm | 2 | 037, 038 |
| irrefuehrend | 1 | 043 |
| mittelwert | 2 | 050, 052 |
| mittel_rueckwaerts | 2 | 057, 061 |
| mengen | 2 | 067, 069 |
| stelle | 2 | 071, 075 |
| graph_lesen | 2 | 079, 080 |
| punkt_graph | 2 | 085, 087 |
| sachzusammenhang | 2 | 092, 094 |
| kreuzung | 2 | 101, 102 |
| uhr | 2 | 106, 108 |
| figuren | 2 | 113, 115 |
| verstehen (Winkel) | 2 | 124, 126 |

Grenzfälle, die je nach Strenge dazukommen: 042 (gestapelte Säule, Teilstück umrechnen), 104 (senkrechte Geraden, spitzer Winkel), 112 (zweite Stunde mit demselben Winkel), 123 (Einteilung nach Winkelart) und 005, 017. VT3-106 ist jetzt die Anzeige 15:30 Uhr (75°) und damit einfacher als vorher; ich habe sie nach Urteil 1222 so gebaut und zähle sie als schema-nah.


## Lehrplan-Bezug (LehrplanPLUS Gymnasium Bayern, G9)

Feld `lehrplan` = nur der Lernbereich der Einheit (M5 2, M6 2, M6 3, M8 1), wie er im Repo steht. Unterpunkte (z. B. 2.1) habe ich nicht angegeben, weil ich sie nicht sicher aus dem Repo belegen konnte. Inhaltlich nur Stoff der jeweiligen Klasse: bei Winkel keine Winkelsumme im Dreieck (Klasse 7), bei Funktionen nur lineare Terme, f(x) = x² in Wertetabellen und einfache Bruchterme mit ausgeschlossener Zahl (wie im Bestand), bei Daten nur Mittelwert, relative Häufigkeit, Säulendiagramm.

## Bilder im Test

Es gibt kein Bild und kein `grafik`-Feld. Diagramme sind durch Maßstab und Säulenhöhen in cm, Wertetabellen oder Zahlenangaben beschrieben („Hochachse beginnt bei …, 1 cm steht für …“), Graphen durch Punkte, Wertetabellen oder Steigung und Achsenabschnitt, Winkel an der Kreuzung durch die Reihenfolge α, β, γ, δ um den Schnittpunkt, Uhren durch Uhrzeiten.

## Prüfungen

- `python3 -I tools/vtest_pruefen.py --runde 3` → OK – keine Fehler, keine Hinweise. Die früheren Hinweise waren falsch-positiv und sind erledigt: VT3-010 („60 000 cm³“ mit Einheit las das Werkzeug als falsche Rechenzeile; der Text steht jetzt als „Das Volumen ist 60 000 cm³, denn 50 · 30 · 40 = 60 000.“, die Rechnung selbst war immer richtig), VT3-073 (Zeile 1 war eine Gleichung, die Aufgabe ist ersetzt) und VT3-115 („runde Torte“ meint kein Runden, steht jetzt „kreisförmige Torte“).
- `python3 -I inhalte/mathe-profi/vtest-3/gegenrechnung.py` → 126 Aufgaben, 0 Abweichungen. Je Aufgabe ein eigener Sollwert (Formel, Aufzählung, Brute-Force); bei Auswahl wird die richtige Option über ihren Text gefunden, nicht über die Nummer.
- `python3 -I inhalte/mathe-profi/vtest-3/bauen.py` bricht ab, wenn eine der festen Prüfungen verletzt ist: je Lernziel mindestens 5 Denkfiguren und keine mehr als zweimal; Auswahl mit genau vier Optionen; richtige Option höchstens in 35 % der Fälle die längste; Plätze der richtigen Option gleichmäßig verteilt und in keinem Lernziel zweimal hintereinander gleich; **neu:** in jeder Auswahl-Aufgabe tragen alle vier Optionen „denn/weil“ oder keine; der Anteil der Optionen mit „=“, mit Sammelformeln („Beide …“, „Kein …“, „Alle …“) und mit Absolutwörtern („immer“, „nie“, „alle“, „stets“) unter den richtigen und den falschen Optionen weicht höchstens um zehn Prozentpunkte ab; **neu (Vorprüfung 3):** Abschwächungen („höchstens“, „mindestens“, „wenigstens“) weichen unter richtigen und falschen Optionen höchstens um fünf Prozentpunkte ab, Verneinungen („nicht“, „kein…“, „nie“) höchstens um zehn; keine Zahlenfolge der Plätze über fünf Aufgaben. **Neu (Urteil 1222):** Jede Lücke jeder Lückenaufgabe, auch die Zeilen-Lücke der Fehler-Detektive, hat mindestens ein eigenes Fehlbild; sonst bricht `bauen.py` ab.
- Auswahl-Statistik (63 Aufgaben): richtige Option an Platz 1 bis 4: 15, 16, 16, 16 mal. Die Plätze legt `kern.plaetze` fest: festes Seed (20261128), zufällige, aber ausgeglichene Folge; nie zweimal hintereinander gleich, keine drei aufeinanderfolgenden Aufgaben mit gleichem Schritt modulo 4, je Platz höchstens ⌈n/4⌉ und mindestens ⌊n/4⌋ Aufgaben. In 18 Fällen (29 %) ist die richtige Option die längste (einschließlich Gleichstand bei kurzen Zahlenoptionen), Rang nach Länge (1 = längste) 1 bis 4: 18 · 29 · 10 · 6; mittlere Länge 77,3 gegen 75,6 Zeichen. „denn/weil“: 81 % richtig gegen 81 % falsch. „=“ steht in 9 von 63 richtigen (14 %) und 24 von 189 falschen Optionen (13 %), Sammelformeln in 3 von 63 richtigen und 6 von 189 falschen, Absolutwörter in 3 von 63 richtigen und 8 von 189 falschen, Abschwächungen („höchstens“, „mindestens“, „wenigstens“) in 6 von 63 richtigen (10 %) und 13 von 189 falschen (7 %), Verneinungen in 7 von 63 richtigen (11 %) und 32 von 189 falschen (17 %).
- `sonderfaelle.md`: Durchsicht aller 63 Auswahl-Aufgaben, auch darauf, ob eine falsche Option zufällig dieselbe Zahl liefert wie die richtige (so bei VT3-005 gefunden und geändert), und seit Urteil 1222, ob eine falsche Option ein richtiges Urteil mit nur falscher Begründung trägt (verboten; VT3-084, 086, 100, 121 umgebaut).
- `bestandsvergleich.md`: Handvergleich aller 126 Aufgaben gegen den Bestand des Lernziels (inhalte/themen und alle rollend-*), je Lernziel mit Zahl der verglichenen Aufgaben.

## Überarbeitung nach den Vorprüfungen

- Vorprüfung 1: `korrektur-nach-vorpruefung.md` (Quelle `vorpruefung.md`).
- Vorprüfung 2: `korrektur-nach-vorpruefung-2.md` (Quelle `vorpruefung-2.md`): 13 B-Befunde und die sinnvollen C-Hinweise, Befund für Befund.
- Vorprüfung 3 (letzte Schleife vor der Sammelprüfung): `korrektur-nach-vorpruefung-3.md` (Quelle `vorpruefung-3.md`): 9 Doppelungen mit gleichem Kern ersetzt, Schema im Lernziel „stelle“ auf zwei gesenkt, B2 bis B11 und C1 bis C5 Befund für Befund.
- Urteil 1222 (Gegenprüfung aller vier Runden, Urteil für Runde 3: „Muss vorher“): `korrektur-nach-gegenpruefung.md`, Befund für Befund: Fehlbild je Lücke (20 Lücken ergänzt, feste Prüfung), VT3-027, 049, 068, Ersatz von 122 und 040, Tausch 099/100, 106 über die Anzeige 15:30, 113 mit sechs gleich großen Stücken, strenges Schema (Ersatz von 012, 013, 021, 040, 041, 074, 077, 086), verbotene Ablenker in allen 63 Auswahl-Aufgaben, Vergleich auch mit `rollend-15`.

## Zweifelsfälle (ehrlich)

1. Hilfsausdrücke statt natürlichem Rechenweg in `loesung_rechnung`, weil der Rechner keine Wurzeln und keine Zählweisen kennt (z. B. VT3-006, 115). `gegenrechnung.py` prüft diese Ergebnisse unabhängig durch Aufzählung.
2. VT3-118 (Zerlegung eines rechten Winkels) verlangt Beweisdenken und liegt oben an der Klassengrenze; falls zu schwer, durch eine andere Sicherung ersetzen.
3. VT3-044 beschreibt die ungleiche Skala in Worten und über die Lage der Säulen; ohne Bild bleibt die Aufgabe lösbar, verlangt aber, die Marken zu lesen.
4. VT3-069, 075: Bruchterme mit Definitionslücke gehen in die Richtung der Bestandsaufgaben der Klasse 8, sind aber knapp am Lernbereichsrand.
5. Konventionen: Der Stundenzeiger dreht 0,5° je Minute (VT3-106, 107, 109, 111); die Winkelgröße hängt nicht von der Schenkellänge ab (VT3-125). VT3-022 setzt voraus, dass Päckchen gerade, ohne Drehen eingeräumt werden. VT3-115: Schnitte „durch den Mittelpunkt“, ein Schnitt erzeugt zwei Kanten. VT3-106 hat die ganzzahlige Antwort 75° (Anzeige 15:30 Uhr).
6. Die Oberfläche eines Quaders habe ich bewusst nicht aufgegriffen, obwohl die Vorprüfung sie mehrfach als Gegenbeispiel (gleiche Oberfläche, anderes Volumen) vorschlug: Der Lernbereich der Einheit ist das Volumen, und ich konnte den Bezug der Oberfläche zu diesem Lernbereich nicht sicher aus dem Repo belegen.
7. Alle 18 Tests sind Stufe 3; einzelne Sicherungen (Stufe 3) sind ähnlich schwer, die Reihenfolge im Lernziel ist daher nicht streng nach Schwierigkeit.
8. Die Fehlbild-Beschreibungen nennen teils Zwischenergebnisse; die gespeicherte Zahl ist das Endergebnis.
9. Die Auswahl-Optionen sind vom Bauskript nur formal gleich gebaut (denn/weil, Länge, Zeichen); ob eine Option einem Kind inhaltlich „auffällt“, kann nur der Test mit Kindern zeigen.
10. Der Bestandsvergleich ist ein Handvergleich mit den zwei nächsten Kandidaten je Aufgabe plus Schlagwortsuchen; eine Gewähr für jede denkbare Nähe gibt es nicht (VT3-047 und 025 wurden bei dieser Suche noch als zu nah erkannt, obwohl die Vorprüfung sie nicht beanstandet hatte).
11. Mensch vor dem Einspielen: Schwierigkeit der Stufe-3-Tests in Klasse 5 und 6 gegenlesen (besonders VT3-001, 022, 036, 043, 057, 106).

## Offene Zweifel für die Gegenprüfung (Stand nach Urteil 1222)

Ehrliche Liste dessen, was ich nicht ausräumen konnte. Der Bestand der fünf Einheiten ist für diese Lernziele sehr dicht; für jede ersetzte Aufgabe habe ich den Kern gezielt im Bestand gesucht (Suchwörter stehen in `bestandsvergleich.md`), eine Gewähr gibt es nicht.

Klassenstufe und Schwierigkeit (Sicherheit nach meiner Kenntnis des Lehrplans, ohne Lehrplantext):
- VT3-001: Prozentfaktoren bei drei Kanten, etwa 60 %, dass das in Klasse 6 machbar ist.
- VT3-036: Streckfaktor 2,5 beim Neuzeichnen, etwa 55 %.
- VT3-043: mehrstufig mit Prozent, etwa 60 %; im Bestand liegen #143/#167 („wie viel Mal so hoch wirkt die zweite Säule“) im selben Gedankenfeld, die Frage hier ist aber die wahre prozentuale Änderung.
- VT3-099 (früher 100, jetzt der Test): Paar-Argument bei drei Geraden (sechs Winkel, wie viele spitz); VT3-100 ist jetzt die leichtere Begründungsaufgabe „ein Winkel 90°, alle 90°“.
- VT3-113: jetzt ohne Gleichung, mit sechs gleich großen Stücken (90° : 6); VT3-114 ist ebenfalls eine Zerlegung des rechten Winkels in Stücke (Zählfehler), beide stehen im Lernziel figuren nah beieinander, haben aber verschiedene Fehler (vergessenes Stück gegen falsche Stückzahl 1 + 3).
- VT3-118: Taubenschlag-Argument („mindestens ein Teilwinkel höchstens 30°“) in Klasse 5, schwer einzuschätzen.
- VT3-058 ist jetzt ohne negative Zahlen formuliert („unter“, „über“). VT3-061 und VT3-062 rechnen noch mit Vorzeichen (Abweichungen −2, +1, …), vgl. Klasse 6; VT3-061 steht deshalb auf Stufe 2.
- VT3-117 (Winkelhalbierende) ist ersetzt. Winkelhalbieren kommt nur noch als Wort im Fehlbild („halbiert“ gleich durch 2 geteilt) vor, nicht als Aufgabe; eine Halbierung mit Konstruktion (Klasse 7) steht nirgends. VT3-106 ist jetzt die Anzeige 15:30 Uhr (75°).

Nähe zum Bestand, nach Lesen als „mittel“ eingestuft (Bestandsnummer in `bestandsvergleich.md`):
- VT3-057 (Zahl der Mädchen aus drei Mittelwerten) liegt im Gedankenfeld von #116/#119 (Gruppenmittel und Gesamtmittel), gefragt wird aber das Gewicht, nicht ein Mittelwert.
- VT3-122 ist neu (spitzer Winkel verdoppelt, was gilt immer: kleiner als 180°); #261 und GE3-15 prüfen andere Aussagen.
- VT3-040 (Säulenbreite zählt nicht) liegt nach Lesen in der Nähe der Bestandsaufgaben zu Piktogramm-Breiten (#144 bis #151), betrifft aber Säulen mit Maßstab; VT3-106 (Anzeige 15:30) liegt bei #127 (11:30 Uhr), neu ist die Übertragung der 24-Stunden-Anzeige.
- Die Ersatzaufgaben nach Urteil 1222 (012, 013, 021, 027, 041, 049, 068, 074, 077, 086) habe ich im Kern gesucht (Stichwörter in `bestandsvergleich.md`), auch in `rollend-15`; dort liegt in den fünf Einheiten dieser Runde nichts.
- Strenges Schema: VT3-042 (gestapelte Säule), 104, 112, 123 und 005, 017 sind Grenzfälle; im Lernziel saeulendiagramm kann die Zählung der Gegenprüfung auf drei kommen, wenn sie 042 zu den Routinen rechnet.
- VT3-028 (Länge verdoppelt, Breite halbiert) liegt in der Familie R14-V164/#212 bis #217, Gedanke aber ein anderer (die Änderungen heben sich auf). Von VT3-001 getrennt.
- Die übrigen unter B1 genannten (VT3-014, 029, 033, 038, 039, 040, 044, 046, 053, 054, 056, 059, 062, 064, 067, 068, 076, 085, 091, 094, 095, 097, 098, 102, 103, 108, 109, 112, 114, 126; 035, 042 und 117 sind ersetzt): beim Lesen verschiedener Gedanke, Wortlaut und Zahlen teils ähnlich. Die einfache Wortähnlichkeit zum nächsten Bestandstext liegt zwischen 0,10 und 0,56; die höchsten Werte haben VT3-067 (0,56, Bestand #86 zählt die Elemente von W für x²; hier ist es ein Fehler-Detektiv mit anderer Fehlvorstellung), VT3-112 (0,51, #158: gleiche Uhrzeitfigur, andere Frage), VT3-108 (0,46) und VT3-102 (0,41). Ich habe sie nicht ersetzt, damit die Runde nicht „ins Blaue“ umgebaut wird; sie stehen hier für die Gegenprüfung. VT3-014 (Becken füllen, R14-V156) und VT3-102 (Summe dreier Winkel, GE3-B2) sind nach Lesen die nächsten.
- VT3-001 und VT3-028 sind innerhalb der Runde entwirrt (Prozentfaktoren gegen Verdoppeln und Halbieren).

Werkzeug: Der frühere Hinweis zu VT3-010 war ein Fehlalarm des Werkzeugs (Einheit „cm³“ hinter einer Zahl mit Leerzeichen), siehe Prüfungen; die Rechnung war richtig.
