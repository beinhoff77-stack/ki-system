# Zweite Vorprüfung Runde VT2 (nach Überarbeitung, Stand `852d461b`)

Vorprüfer: unabhängig, ohne Webabrufe, keine Aufgabe geändert. Kennzeichnung: [F] = nachgeprüfte Tatsache, [A] = Annahme.

## 1. Gesamturteil

**Freigabe nach kleiner Korrektur.** [F] Keine Sollantwort ist falsch, kein A-Befund. Der A-Befund aus Runde 1 (VT2-025) ist geschlossen. Die Überarbeitung hat die Aufgaben spürbar verbessert (28 der 57 B-Befunde sind geschlossen). Offen sind 14 B-Befunde. Der Schwerpunkt hat sich verschoben: Es gibt kaum noch Rechenfehler, aber **fünf neue Doppelungen mit dem Bestand** (112, 022, 092, 045, 083), weil der Autor wieder keinen Handvergleich gemacht hat, und mehrere Aufgaben, bei denen die Antwort im Text oder in der Nachbaraufgabe steht (038, 081, 112/107).

## 2. Zahlen

| Zahl | Wert |
|---|---|
| geänderte Aufgaben (Diff `efec082b`..`852d461b`) | 99 von 133, alle vollständig gelesen |
| Sollantwort nach eigener Rechnung richtig und eindeutig | alle 99 (und die 34 unveränderten wie in Runde 1) |
| Befund A | 0 |
| Befund B (neu oder offen) | 14 Einzelaufgaben: 022, 038, 045, 054, 081, 082, 083, 092, 107, 110, 112, 114, 120, 124; dazu 1 Gruppenbefund „ohne denn/weil“ (043, 054, 096, 110, 111, 115, 117, 125) |
| Befund C | rund 40 Kennungen in den C-Zeilen (Abschnitt 3) |
| Runde-1-Befunde: A geschlossen; B (57 Kennungen, vom Autor als 56 gezählt) | 28 ja, 21 teilweise, 8 nein |

Werkzeuge [F]:
- `tools/vtest_pruefen.py --runde 2`: „OK – keine Fehler“, 5 Hinweise „Feld runden fehlt“ bei 106, 108, 112, 113, 118. Wieder Fehlalarm: Gerundet wird nur im Aufgabentext, das Ergebnis ist exakt.
- `gegenrechnung.py` des Autors: 133 gelesen, 0 Abweichungen.
- Mein `vorpruefung_rechnen_2.py`: 59 Zahl-/Lücken-Aufgaben unabhängig neu gerechnet (Fraction, Aufzählen, Koordinaten), 0 Abweichungen. 124 gezählt: 18. 078 gezählt: 78. 122: 3 888 ist die einzige Zahl mit 15 Zeichen. 085: nur die Ziffer 3 passt. 071: nur r = 6. 112: genau 350 bis 354. 120: Zeile 2, MCDXLIX hat 7 Zeichen. 10 Auswahlaufgaben, bei denen sich die Möglichkeiten durchrechnen lassen, per Code bestätigt (003, 011, 012, 014, 026, 039, 046, 054, 059, 129), dazu 048 und 010. 300 Fehlbild-Rechnungen werden zu ihrer gespeicherten Antwort ausgewertet: 0 Widersprüche. (Das beweist nur die Zahl; ob der Text zur Rechnung passt, habe ich von Hand gelesen, siehe 124.)
- Die übrigen Auswahlaufgaben habe ich von Hand für jede Möglichkeit auf Sonderfälle geprüft, keine zweite richtige gefunden.

## 3. Befunde

| Kennung | Grad | Befund | Korrekturvorschlag |
|---|---|---|---|
| VT2-112 | B | Neue Doppelung: Bestand `themen/zahlen.natuerlich` hat „Eine dreistellige Zahl ergibt auf Zehner gerundet 350 und auf Hunderter gerundet 300. Wie viele solche Zahlen gibt es?“. 112 ist dieselbe Figur (nur 400 statt 300). Zudem ist die erste Hälfte (345 bis 354) genau die Antwort der unveränderten 107; wer 107 gelöst hat, liest 112 ab. | 112 ersetzen (Rundungsbereiche mit anderer Stelle, z. B. Tausender und Zehner, oder Rückfrage „Kann eine Zahl auf Zehner 350 und auf Hunderter 300 ergeben? Begründe“ ohne die Zahlen 350/345/354). |
| VT2-022 | B | Doppelung als Test: Bestand `themen/finanzen.zinsen` „Wie viele Monate muss man 6 000 € zu 4 % Jahreszinssatz anlegen, um 60 € Zinsen zu bekommen?“. 022 hat nur 3 600 € statt 6 000 € (Soll 5 statt 3). Die Abgrenzung im Feld ist nicht haltbar. | Andere Frage: z. B. „Wie viel Euro Zinsen bringen 3 600 € in 5 Monaten, und ab wie vielen Monaten sind es mehr als 100 €?“ oder Zinssatz aus Monaten und Zinsen. |
| VT2-092 | B | Doppelung als Test: Bestand `themen/zahlen.natuerlich` „Wie viele Nullen hat die Zahl ‚siebenhundertneunzig Millionen siebenundvierzigtausendzwei‘ …“. Gleiche Frage, nur andere Zahl. Zudem Fehlbild 4 (`8 − 4`) beschreibt „Stellen der Tausenderklasse als Nullen gezählt“; das führt nicht auf 4. | Andere Figur (z. B. Zahlwort mit zwei Nullen in einer Klasse, Frage nach der Stellenzahl oder dem Zahlwort zu einer Ziffernfolge mit Nullklassen). Fehlbildtext 4 anpassen. |
| VT2-045 | B | Doppelung: Bestand `themen/terme.umformen` „Für wie viele ganze Zahlen x zwischen −10 und 10 haben x² und 3x denselben Wert?“. Gleiche Zählfigur. | Andere Idee: Terme, die bei x = 2 gleich sind, Gegenbeispiel suchen; oder zählen mit einem nicht-quadratischen Paar. |
| VT2-083 | B | Doppelung: Bestand `themen/geometrie.kreis` „Im Dreieck ABC ist α = 70° und β = 50°. I ist der Inkreismittelpunkt. Wie groß ist ∠AIB?“ 083 vertauscht nur α und β (50°/70°) und fragt zusätzlich nach den zwei Halbwinkeln. Ergebnis 120° gleich. | Andere Winkel und eine Rückwärtsfrage („∠AIB = 125°, α = 60°, wie groß ist β?“). |
| VT2-038 | B | Zufallstreffer: k = 5 und der Wert im Text („erhält man 5“) sind gleich. Wer die genannte 5 einträgt, hat recht. Fehlbilder jetzt passend (−1, 2, 15), das alte B ist geschlossen. | Wert 4 statt 5 (dann k = 6), Fehlbilder neu rechnen: 7 − k − 3 = 4 gibt k = 0; „+3 vergessen“ gibt 3; Summe 14. Etikett „Koeffizientenvergleich“ stimmt nicht (es ist Einsetzen). |
| VT2-081 | B | Antwort im Text: Zeile 2 nennt „Mittelsenkrechten“, das ist die Lösung der zweiten Lücke; die Fehlerzeile erkennt man als die einzige, die nicht von Mittelsenkrechten spricht. Dazu liefert die unveränderte 079 [1] fast denselben Wortlaut (Nachbarantwort). Kaum Verstehen. | Zeile 2 ohne Namen („Er liegt deshalb auf besonderen Geraden zu den Seiten“) oder den Fehler in Zeile 1/2 legen, z. B. „Der Mittelpunkt muss von allen drei Seiten gleich weit entfernt sein“ (Inkreis-Gedanke beim Umkreis). |
| VT2-054 | B | Nicht geschlossen: Die richtige Möglichkeit ist weiter als einzige keine Gleichung („Kein ganzzahliger Faktor … es lässt sich nichts ausklammern“) und als einzige ohne „denn“. Die drei falschen folgen derselben Bauart. | Alle vier als „… = …, denn …“, in der richtigen eine Probe (z. B. „6x² + 4x + 5 lässt sich nicht ausklammern, denn 5 enthält weder 2 noch x“). |
| VT2-110 | B | Nicht geschlossen: Die richtige ist die einzige „manchmal“-Aussage, die drei falschen sind „immer/nie“ und tragen alle ein „denn“. | Falsche Möglichkeiten als weiche Aussagen mit falschem Zusatz („meist größer, weil …“), richtige mit „denn“. |
| VT2-082 | B | Neues Muster statt Nachbarantwort: eine Möglichkeit „Richtig“ gegen drei „Falsch“; die Behauptung wird nie bejaht, wenn man das Muster kennt. Die ablesbare Regel aus Runde 1 ist verschwunden. | Zwei „Richtig“-Optionen mit falscher Begründung oder Behauptung umdrehen („Der Umkreismittelpunkt liegt in jedem Dreieck innerhalb“). |
| VT2-107 | B | Unverändert; Doppelung mit Bestand „Eine Zahl ergibt auf Zehner gerundet 1 000. Wie heißt die kleinste solche Zahl?“ (nur 350 und die größte Zahl zusätzlich). Zahlen „weichen ab“ reicht nicht, es ist dieselbe Figur wie 106. Und sie gibt 112 vor. | 107 so ändern, dass nicht Zehner/350 vorkommt (z. B. Tausender 5 000, Fehlerfrage), oder ersetzen. |
| VT2-114 | B | Nur teilweise geschlossen: Bestand `rollend-12` „Für 342 Personen sollen Busse bestellt werden. In jeden Bus passen 50.“ ist dieselbe Figur (Division mit Rest, Sachgrund bestimmt die Rundungsrichtung); hier nur nach unten statt nach oben. Etikett „Aufrunden aus Sachgründen“ stimmt nicht (es wird abgerundet). | Andere Figur (zwei Sachsituationen gegeneinander begründen) oder ehrlich als Wiederholung kennzeichnen; Etikett korrigieren. |
| VT2-120 | B | Teilweise geschlossen. Die Regel steht nicht mehr im Text (gut), aber auch nicht „nach den üblichen Regeln“. CCCC ist historisch belegt; die Eindeutigkeit hängt an der Schulregel „höchstens dreimal“. Nils benutzt XL und IX, also die Subtraktionsregel: das macht CCCC erkennbar, aber nur durch Mustervergleich. Ähnlich Bestand `rollend-12` „Lena schreibt 49“ (Fehler-Detektiv). | „… nach den üblichen Regeln (kein Zeichen mehr als dreimal hintereinander)“; ggf. Fehler an anderer Stelle (IIX statt VIII). |
| VT2-124 | B | Zählung eindeutig (18, eigen gezählt), Regel „übliche“ jetzt genannt (Beispiele IV, IX, XL). Neu: Fehlbild 8 beschreibt „nur die Zahlen mit XL gezählt“; das sind 10 (40 bis 49), nicht 8. 8 sind die XL-Zahlen ohne 44 und 49. | Beschreibung für 8: „nur die 8 zusätzlichen XL-Zahlen (ohne 44 und 49) gezählt, die 10 mit IV/IX vergessen“. |
| VT2-043, 054, 096, 110, 111, 115, 117, 125 | B (Gruppe) | Neues Muster, das die Längen- und Positionsprüfung des Autors nicht erfasst: Die richtige Möglichkeit ist die **einzige ohne „denn/weil“**. In 10 Aufgaben, in denen genau eine Möglichkeit „denn/weil“ nicht enthält, ist es in 8 die richtige (Zufall wäre 2,5). Insgesamt tragen 32 % der richtigen, aber 51 % der falschen Möglichkeiten ein „denn/weil“. 043 ist ein Test. | In diesen Aufgaben alle Möglichkeiten gleich bauen (alle mit oder alle ohne Begründung). |
| VT2-064 (Test) | C | Richtige ist die einzige mit dem Fachwort „Umkehrung des Satzes des Thales“. Keine Antwortlesbarkeit aus Nachbaren (068 [2] und 069 [0] sagen dasselbe in Worten). | Fachwort aus der richtigen Möglichkeit streichen. |
| VT2-068 | C | Die zwei falschen Möglichkeiten [1] und [3] teilen die Endung „, also mit AB als Radius“, die richtige fällt als Einzelne heraus. | Endungen verschieden. |
| VT2-013, 023, 044 | C | Doppelte Lückenwerte ([36, 36], [50, 50], [3, 3]). Fachlich beabsichtigt (Gleichheit ist die Einsicht). Bei 013 und 023 verrät aber das erste Feld das zweite, sobald das Muster „bei zwei Anlagen kommt dasselbe heraus“ bekannt ist, und es kommt in zwei Aufgaben derselben Einheit vor. | Bei 013 B mit 1 500 € zu 2,4 % durch 1 800 € zu 2 % ersetzen (36 gegen 36 vermeiden) oder nach dem Unterschied fragen. Bei 044 belassen (die Konstanz ist die Aufgabe). |
| VT2-040 | C | „(auch die Zahl 0 darfst du eintragen)“ verrät, dass in den Feldern eine 0 vorkommt. | Hinweis in die Schablone („Je Feld eine ganze Zahl, auch 0 möglich“), ohne Bezug zum Ergebnis. |
| VT2-052 | C | Fehlbild 6 (`12 : 2`) wird beschrieben als „wie Ben 12 : 6 falsch gerechnet“; die Rechnung ist 12 : 2. | Beschreibung an die Rechnung anpassen. |
| VT2-037, 092, 099, 101 | C | 037: Fehlbild −1 „bezogen auf jede Klammer“, die Rechnung gilt nur für die erste. 099: unverändert, ähnliche Bauart wie Bestand „Genau 5 Abschnitte nach der 0 steht 400“; Fehlbild 170 oder 50 beliebig. | 037 „bei der ersten Klammer“ schreiben. |
| VT2-001, 002, 005 | C | 001 ist weiter die Bestandsfigur „Sparkonto und Kredit gleichzeitig“, jetzt mit Zusatz in Prozent (neu und gut). 002 bleibt Familie mit Kredit und Sparkonto wie `rollend-8`, aber mit Entscheidung „zahlt/bekommt“. 005 verlangt den vermehrten Grundwert (5 150 : 1,03); ob das in M6 3 verlangt ist, kann ich ohne Lehrplantext nicht belegen. | keine Pflicht. |
| VT2-008, 029, 032, 036 | C | Fehler-Detektive mit demselben Gerüst wie `rollend-7`, `-8`, `-13`, `-15`. 029 und 032 sind derselbe Vorzeichenfehler beim Verrechnen. 008 [1] enthält eine volle Rechnung. | Bewusst vom Autor behalten; ich teile das nicht ganz. |
| VT2-014 | C | Die falsche Rechnung ist die einzige mit zwei Faktoren statt `+`/`−`: erkennt man an der Form. | Die falsche Rechnung in der Form der anderen halten (z. B. „1 800 · 0,03 + 1 800 · 0,05“). |
| VT2-042, 075, 127, 128 | C | Stufe 3 bei einer einzigen Überlegung: 042 (2 500 − 2 457), 075 (12 − 9), 127 (13 · 2 + 1; ein Kind rechnet 16 + 8 + 2 + 1 direkt), 128 (Zweierpotenzen). | Stufe 2 eintragen; 127 ist als Test die leichteste Aufgabe des Lernziels. |
| VT2-010, 012 | C | Schema „Komma zwei Stellen“; 012 hat aufsteigende Zahlenoptionen, die richtige steht in der Mitte. | akzeptiert. |
| VT2-053, 051, 058, 061 | C | Schema, aber vertretbar und weniger nah am Bestand als in Runde 1: 053 (ggT als Auftrag formuliert), 051/058 (Bestandsfigur mit Parameter), 061 („Überlege mit (50 − 1)²“ verrät das Verfahren, 50² − 49² geht auch direkt). | keine Pflicht. |
| VT2-097, 114, 116, 133 | C | Etikett-Fehler und kleine Texte: 114 siehe oben; 116 verrät in beiden Wegen das Verfahren (soll so sein). | – |
| VT2-077 | C | Der Satz „immer mehr“ ist im schwachen Sinn („nie weniger“) wahr. Jetzt sind alle anderen Möglichkeiten klar falsch, [3] ist die einzig vertretbare. | Satz „immer mehr, ohne Grenze“. |

## 4. Runde 1: Sind die Befunde geschlossen?

A: **VT2-025 geschlossen** [F]. 9 Monate, Soll 15/40/45, Fehlbild „60 · 8 : 3“ gerechnet. Einjahresrahmen eingehalten.

B-Befunde (j = ja, t = teilweise, n = nein):

| Kennung | | Kennung | | Kennung | |
|---|---|---|---|---|---|
| 001 | t (Bestandsfigur bleibt; Zusatz „%“ neu) | 002 | t (Entscheidung ja, rollend-8 ähnlich) | 005 | j |
| 006 | n (bewusst; vertretbar, C) | 009 | j | 012 | t |
| 014 | j | 015 | j | 016 | j |
| 023 | j | 024 | j | 027 | j |
| 029 | n (bewusst; C) | 031 | j | 033 | j |
| 034 | j | 035 | j | 038 | t (Fehlbilder ja; neues B Zufallstreffer) |
| 040 | t | 042 | t (trivial) | 043 | t (neues Muster ohne „denn“) |
| 044 | j | 045 | t (neue Doppelung) | 047 | j |
| 048 | j | 049 | j | 050 | t (weiter Ausmultiplizieren) |
| 051 | t | 053 | t | 054 | n |
| 055 | j | 056 | j | 058 | t |
| 061 | t | 063 | j | 065 | j |
| 068 | j | 069 | j | 070 | j |
| 075 | t | 077 | t | 078 | j |
| 081 | n (Antwort im Text) | 082 | t (neues Muster) | 085 | j |
| 097 | j | 099 | n (bewusst; C) | 100 | t |
| 101 | j | 104 | t | 107 | n |
| 110 | n | 112 | n (neue Doppelung) | 114 | t |
| 120 | t | 124 | t | 133 | j |

Summe: 28 j, 21 t, 8 n. [F] Die Zählung des Autors („56“) weicht um eins von meinen 57 Kennungen ab; ich habe jede Kennung der Befundtabelle einzeln gewertet.

## 5. Echtes Verstehen

Ich habe die sieben Aufgaben jedes Lernziels nebeneinander gelesen. Tabelle: Zahl der wirklich verschiedenen Denkfiguren [A: von mir gezählt, strenger Maßstab].

| Lernziel | Figuren | Bemerkung |
|---|---|---|
| rollen | 6 | gut; 006 bleibt Schema |
| jahreszinsen_komma | 4 | 009/010/012 sind alle „Komma richtig setzen“, 011 und 014 Begründen |
| kapital | 5 | gut |
| zeitanteil | 5 | 025/026/027 Brücke Monate/Jahr; 022 jetzt Bestandsdoppelung |
| zusammenfassen | 5 | 029/032 weiter derselbe Vorzeichenfehler |
| minusklammer | 5 | gut (037, 038, 040, 042 verschieden) |
| aequivalenz | 5 | deutlich besser (043 Beweis, 044 Konstante, 045 Zählen, 046/048 Auswahl, 047 Rückwärts) |
| ausklammern | 5 | 053 Schema |
| binomisch | 5 | 057/062 beide „Quadrat mit Fehler“ |
| umkehrung | 4 | 064/069 Begriff, 065/066 Rechnung, 068 Ortslinie, 070 Winkel; alle hängen an einem Satz, das ist das Lernziel |
| lage | 5 | 071, 073, 074, 075, 077 verschieden |
| umkreis_inkreis | 4 | 078 zählen ist neu; 081/082/084 Regelwissen |
| stellenwert | 5 | gut |
| ziffern_zu_zahlwort | 4 | 095/096/098 „Klassen lesen“ |
| strahl_eintragen | 4 | 100/101/104 Skalenschritt |
| runden_regel | 3 | 106/107/108/112 Rundungsbereich (112 jetzt nur Wiederholung) |
| runden_sinnvoll | 5 | gut |
| roemisch_schreiben | 5 | gut |
| dualsystem | 5 | gut |

Noch reine Schemaaufgaben (höchstens zwei je Lernziel, wie der Autor sagt, plausibel): 006, 009, 010, 029, 032, 034, 053, 056, 058, 061, 090, 104. Schema und Bestandsnähe zugleich sehe ich bei 010, 029, 032 und 104.

Ist der Test die schwerste Aufgabe des Lernziels, lösbar in 2–4 Minuten? [A: nach eigener Einschätzung, ungeprüft an Kindern]
- Ja: 001, 015, 050, 071, 078 (grenzwertig lang, 3 bis 5 Minuten wegen des geordneten Zählens), 085, 113.
- Nein, es gibt leichtere oder gleich schwere Aufgaben im Lernziel: 008 (eine Kommaverschiebung, 013 und 012 sind nicht leichter), 029, 127 (direkt über 16 + 8 + 2 + 1 lösbar, damit leichter als 128/133), 120, 099, 106, 043 (Begriffsfrage, aber Muster ohne „denn“).
- Zu leicht in Bezug auf Nachbarn: 127. Zu schwer: keiner.

## 6. Auswahlstatistik nachgemessen

[F] Zahlen des Autors stimmen: 47 Auswahlaufgaben, 4 im Test (008, 036, 043, 064). Plätze A/B/C/D = 12/13/9/13. Die richtige Möglichkeit ist in 1 von 47 die eindeutig längste (010), in 6 die eindeutig kürzeste, kein Fall mit ≥ 1,3-facher Länge; mittleres Verhältnis richtig/falsch 0,98. Länge und Position sind in Ordnung.

Weitere erkennbare Muster [F, per Skript]:
- „denn/weil“: richtige 32 %, falsche 51 % (siehe Befund Gruppe). 8 von 10 Treffern bei der Regel „die einzige ohne denn“.
- Absolutwörter (immer/nie/nur/jede/alle/kein): richtige 15 %, falsche 28 %. In 110 (weich gegen absolut) und 054, 115 gibt das die Lösung.
- Ziffer: richtige 70 %, falsche 59 %. In 077, 096, 117 hat nur die richtige Zahlen.
- „Beide …/Gleich …“: 11 Möglichkeiten, nur 1 richtig (115 [3]). Der Autor schreibt „4 von 5“; richtig ist 10 von 11 falsch. Wer „Beide gleich“ nie wählt, liegt fast immer richtig, das ist aber ein schwaches Muster.
- Ein Urteil „Richtig“ gegen drei „Falsch“: 082 (siehe Befund).
- Einzelnachweise: 043, 054, 096, 110, 111, 115, 117, 125 (ohne „denn“).

## 7. Doppelungen mit dem Bestand

[F] Ähnlichkeitssuche (Wortmenge + Zahlenmenge) gegen alle JSON-Texte von `inhalte/themen` und `inhalte/mathe-profi/rollend-*`, danach die Treffer von Hand gelesen. Handvergleich je Lernziel: der Test und zwei weitere Aufgaben gegen die Fundstellen der Suche (nicht jede Aufgabe gegen jede Bestandsaufgabe; für die übrigen verlasse ich mich auf die Suche).

Neu gefunden (Befund B): 112, 022, 092, 045, 083 (Abschnitt 3). Wortgleich oder fast wortgleich mit dem Bestand ist keine andere der 99 geänderten Aufgaben. Näher dran, aber vertretbar (C): 001, 002, 008, 029, 036, 051, 058, 099, 114, 120. Bei den Tests der Lernziele sind 022 und 092 die einzigen Fälle, in denen ein Test auf einer Bestandsaufgabe beruht.

## 8. Bewusst unveränderte Aufgaben

- 006: Schema (Gleichsetzen, Division durch 0,02), eindeutig, 6 000 € richtig. Vertretbar als einzige Schemaaufgabe von „rollen“. C.
- 099: Teilstrich-Aufgabe, richtig (17 cm). Nahe an der Bestandsfigur, aber mit cm-Maßstab; als Test das leichteste im Lernziel neben 100. C.
- 107: siehe B; sollte sich ändern, weil 112 daran hängt.
- 018: Fehlbild 2 646 ist ersetzt (jetzt 63 als Kapital, antwort 63); Fehlbilder 150, 63, 3, 1 stimmen. In Ordnung.
- 079: eindeutig; die Möglichkeiten sind ein 2 × 2-Raster (Mittelsenkrechten/Winkelhalbierende × Ecken/Seiten). Gibt 081 die Lösung preis. C.
- 013/023: siehe C-Zeile; Soll [36, 36] und [50, 50] stimmen.

## 9. Was ich nicht prüfen konnte

- Den Wortlaut des LehrplanPLUS [A]: kein Webabruf erlaubt. Der Stoffrahmen folgt `inhalte/themenliste.json` (Sicherheit etwa 75 %). Unsicher: 005 (vermehrter Grundwert in M6 3), 078/083 (Winkel im Umkreis- und Inkreisbild in Jgst. 7, Themenliste deckt beides).
- Wirkung auf Kinder (Zeit, Fehlbilder) [A: nur geschätzt].
- Die Fehlbild-Beschreibungen der unveränderten Aufgaben habe ich nur stichprobenartig neu gelesen.
