# Vorprüfung W1 der Runde VT1A (Stand edb6b678), Maßstab wie Urteil 1222

Geprüft wurden alle 77 Aufgaben in `zahlen.potenzen_basis.json` (001–028) und `zahlen.rechengesetze.json` (029–077). Für jede Aufgabe habe ich die Lösung neu gerechnet, die Ablenker, Schema, Denkfigur, Test, Eindeutigkeit, Fehlbilder, Bestand, Bauart und Sprache geprüft.
Die Rechnungen stehen im eigenen Skript `vorpruefung_w1_rechnen.py` (exakt, mit Brüchen; jede Auswahl-Option einzeln bewertet; nicht aus `gegenrechnung.py` übernommen). Ergebnis: **0 Abweichungen**. Ein Vermerk: Bei 068 ist Option 0 nicht eindeutig falsch (siehe B3).
Bestand: Für jedes Lernziel habe ich alle Aufgaben derselben Etappe gelesen: `inhalte/themen/<einheit>.json` (alle Pools), `rollend-5`, `rollend-11` und `rollend-12`. `rollend-15` und die übrigen `rollend-*` enthalten keine Aufgaben dieser beiden Einheiten.

Zusatz des Projektleiters: Künftig werden je Lernziel nur 5 Aufgaben eingespielt (1 Test, 2 Korrektur, 2 Sicherung). Der Streichvorschlag steht am Ende der Lernziel-Tabelle. Für die verbleibenden 5 gilt: höchstens 1 Schema, mindestens 4 verschiedene Denkfiguren, der Test ist die anspruchsvollste Aufgabe, und Test und Korrektur prüfen nicht dieselbe Einzelfrage.

## Urteil

| Einheit | bereit für die Gegenprüfung | Hauptgrund |
|---|---|---|
| zahlen.potenzen_basis | **nein** | Test 001 ist bloßes Ausrechnen. Schema-Grenze überschritten in schreibweise und quadrat (sach grenzwertig). Doppelt zum Bestand: 005, 016, 027. |
| zahlen.rechengesetze | **nein** | Test 029, 050 und 064 sind Schema oder Bestand. Doppelt zum Bestand: 030, 037, 038, 045, 046, 047, 058, 065, 075. Verbotene Ablenker in 062. verteilen bündelt sich um das Ausklammern, sach um das Rückwärtsrechnen. |

Zahl der Befunde: **A 17, B 17, C 7**.

## Befunde

### A (Muss vor der Gegenprüfung)

| Nr | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| A1 | 001 (Test schreibweise) | Gefragt wird nur der Wert von 3² + 2³. Wer 9 + 8 = 17 rechnet, findet die Option, ohne eine Begründung zu lesen. Das ist bloßes Ausrechnen und die leichteste Aufgabe des Lernziels; 006 und 007 verlangen mehr. Es ist derselbe Musspunkt wie beim früheren Test 043 (Urteil 1222). | 006 (2⁴ = 4², Begründung) zum Test machen. 001 entfällt oder kommt als Sicherung, dann so gebaut, dass Ausrechnen nicht reicht (z. B. Lenas Regel an einem zweiten Beispiel widerlegen lassen). |
| A2 | 005 | Gleicher Kern wie die Bestand-Übungen „Was bedeutet 5⁴?“ und „Was bedeutet 2⁷?“ (themen): gleiche Frage nach der Bedeutung, gleiche Fehler (Plus, Basis mal Exponent, vertauscht), nur andere Zahlen. Außerdem reine Reproduktion. | Streichen (siehe Streichvorschlag). |
| A3 | schreibweise | Schema streng gezählt: 001, 002 (3⁵ − 3⁴ ausrechnen), 003 (Folge 2, 4, 8 um eine Verdopplung fortsetzen), 004 (2⁸ = 256 ausrechnen, dann Basen durchprobieren). Das sind 4 statt höchstens 2. | Siehe Streichvorschlag. Zusätzlich 002 oder 004 durch eine Aufgabe ersetzen, die eine Einsicht verlangt. |
| A4 | quadrat | Schema: 010 (der Text nennt sogar das Verfahren: „rechnet beide Anzahlen aus und zieht ab“), 011 ((5 + 4)² ausrechnen), 014 neu (25 cm² und 100 cm² ausrechnen, dann 100 : 25; der Wert entscheidet). Das sind 3. | 014 streichen. Will man 014 behalten: ohne Zahlen fragen („Die Seite eines Quadrats wird verdoppelt …“). |
| A5 | 027 | Gleicher Kern wie die Bestand-Übungen rollend-12 „verdoppelt jede Stunde, nach 8 Stunden 1 280, Anfang?“ (Antwort ebenfalls 5) und themen „dreimal verdoppelt, Ergebnis 200, Anfang?“: Startwert aus Endwert : Faktorⁿ, nur der Faktor 3 statt 2. | Streichen (siehe Streichvorschlag). |
| A6 | 016 | Gleicher Kern wie rollend-5 „Welche Schreibweise ist gleich der Zahl 3 400 000? (34 · 10⁶ / 34 · 10⁵ / 34 · 10⁴ / 3 400 · 10⁵)“. Hier ist nur die Frage umgedreht (welche ist ungleich); die Rechnung ist dieselbe. Außerdem Schema. | Streichen. |
| A7 | 029 (Test klammern) | Gleicher Kern wie die themen-Übungen „Wo müssen die Klammern stehen, damit das Ergebnis 12 ist?“ und „Setze Klammern so, dass 6 + 18 : 3 + 3 = 11“. Gelöst wird durch Ausrechnen aller 5 Optionen, also Schema im Test. | 033 (wann ist eine Klammer überflüssig?) zum Test machen. Wenn 029 bleibt, dann als Sicherung. |
| A8 | 030 | Gleicher Kern wie rollend-5 „3 · (? + 4) = 27“ und themen „4 · (□ − 9) = 28“: Lücke in der Klammer rückwärts bestimmen, nur ein Schritt (− 5) mehr. | Ersetzen, z. B. durch die Frage, welche Lücke bei zwei Klammerstellungen dasselbe Ergebnis gibt. |
| A9 | 037, 038 (termaufbau) | 037 ist gleich der themen-Übung „Welcher Term ist ein Produkt, dessen erster Faktor eine Summe ist?“ (letzter Schritt Mal = Produkt). 038 ist gleich den themen-Übungen „Welcher Term passt? Subtrahiere das Produkt aus 4 und 6 von 30“ und „Multipliziere die Summe aus …“. Mit 039 (Sachtext zu Term) sind es 3 Schema. | 037 streichen. 038 durch eine Aufgabe mit Einsicht ersetzen (z. B. „Ändere genau ein Rechenzeichen, damit der Term ein Produkt wird“ oder zwei Texte, die denselben Wert, aber verschiedene Terme haben). |
| A10 | 045 | rollend-5 hat dieselbe Rechnung 25 · 17 · 4 („geschickt, Paar nach vorn“). themen fragt „Welche Rechnung ist ein geschickter Weg für 8 · 37 · 125?“, und zwar mit denselben Optionsarten. | Streichen. |
| A11 | 046 (neu) | Gleicher Kern wie die themen-Übungen „Welche Gleichung ist falsch? (… 69 − 8 = 8 − 69 …)“ (zweimal, auch mit 83 − 13): die Rechenart finden, bei der das Vertauschen nicht gilt. Hier nur Teilen statt Minus. | Ersetzen. Die Einsicht sollte über die Bestand-Übung hinausgehen, z. B. „Bei welcher Kette darf man umstellen, wenn jede Zahl ihr Zeichen mitnimmt?“. |
| A12 | 047; vorteil | 047 ist gleich themen „Ergänze 25 · □ · 4 = 3 700“, „4 · a · 25 = 2 300“ und rollend-12 „4 · □ · 25 = 1 700“. Schema im Lernziel: 044 (der Text verrät mit „auf einmal eine Zahl abziehen“ schon die Summe), 047 und 049 („Berechne geschickt“, das Format der Bestand-Übung). Das sind 3; 048 ist ein Grenzfall (486 : 6 genügt). | 047 streichen. 044 so umbauen, dass der Text den Weg nicht nennt. |
| A13 | 050 (Test verteilen) | Gleicher Kern wie themen „Rechne geschickt: 26 · 67 − 26 · 57“, „6 · 13 − 6 · 3“, „8 · 189 − 8 · 89“, „9 · 102 − 9 · 92“. Schema und nicht die anspruchsvollste Aufgabe (054 und 056 verlangen mehr). Das Lernziel bündelt sich um das Ausklammern: 050, 051, 055, 056 (viermal). Schema: 050, 051, 053 (die Frage nennt 108, also genügt es, beide Wege auszurechnen). | 054 (Wirkung der verdoppelten Höhe) zum Test machen. 050 streichen oder zur Sicherung machen. 051 und 055 streichen (siehe unten). 053 ohne die Zahl 108 in der Frage, mit einem versteckten Fehler in einer Zerlegung. |
| A14 | 058 | Gleicher Kern wie themen „Welche Rechnung führt zur Lösung von x : 6 = 27? (27 − 6 / 27 : 6 / 27 · 6 / 6 : 27)“: Umkehrrechnung wählen, dieselben vier Optionsarten. | Streichen. |
| A15 | 062 | Verbotener Ablenker: Alle drei Ablenker führen auf die richtige Folgerung („keine Lösung“) und haben nur eine falsche Begründung (gerade/ungerade, Primzahl, x > 50). Das ist genau die Art, die Urteil 1222 bei VT2 039/069/082 als Muss gewertet hat. Die Aufgabe ist sonst unverändert und wurde damals nicht genannt. Nach dem Maßstab trifft der Befund aber zu. | So umbauen, dass jede Option ein eigenes Urteil hat, z. B. „Welche Gleichung hat keine natürliche Lösung, und warum?“ mit vier Gleichungen, oder Optionen „hat die Lösung 7“, „hat die Lösung 8“ usw. |
| A16 | 064 (Test ueberschlag) | Der Überschlag 600 · 50 steht im Text; zu rechnen bleibt nur 30 000 : 3 000 = 10. Das ist Schema und schwächer als 068 und 069. Die Frage ist zudem doppelt gestellt („Wie oft passt … das heißt: Um welchen Faktor …“). Schema im Lernziel: 064, 066, 070. | 068 (nach der Berichtigung B3) zum Test machen. 064 als Sicherung behalten, mit einer einzigen Frage. |
| A17 | 065; 075; sach (Rechengesetze) | 065 ist gleich themen „Für welche größte natürliche Zahl a ergibt der Überschlag von a · 30 genau 1 800, wenn a auf Zehner gerundet wird?“ (obere Grenze des Rundungsfensters aus einem Überschlagsprodukt). 075 ist gleich themen „verschenkt die Hälfte seiner Sticker und danach noch 6, jetzt 15, Anfang?“ (Halbieren und feste Zahl rückwärts). Im Lernziel sach (Rechengesetze) bündeln sich die Aufgaben um das Rückwärtsrechnen: 072, 074, 075, 076 (Optionen), 077. Schema: 072, 073, 075. | 065 ersetzen (z. B. mit zwei gerundeten Faktoren oder mit der Frage nach der kleinsten Anzahl). 075 und 072 streichen. 077 mit einer anderen Denkfigur bauen (siehe B10). |

### B (Soll)

| Nr | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| B1 | Bauart, 39 Auswahl-Aufgaben (26 mit Textoptionen) | Neues Muster: Die Ablenker begründen mit einer (falschen) Regel, die richtige Option begründet mit einer Rechnung. „darf/muss/man“ steht in 10 % der richtigen und in 25 % der falschen Optionen; „·“ in 64 % gegen 49 %. In den Textoptionen haben 35 % der richtigen und 15 % der falschen mindestens zwei „=“. Eine Ratestrategie ohne Mathematik (mehr „=“ und „·“, kein Regelwort) trifft 11,3 von 26 statt der zufälligen 6,5. Das „=“ allein (54 % gegen 42 %) ist schwächer, verstärkt das Muster aber; ebenso „denn/weil“ (31 % gegen 22 %). Länge ist in Ordnung (die richtige Option ist in 9 von 39 Aufgaben allein die längste). | In jeder Aufgabe mindestens eine falsche Option mit Rechnung (falsch gerechnet oder falsch angewandt) und mindestens eine richtige Option mit Regelwort („Man darf …, denn …“). Dazu in `bauen.py` je Merkmal prüfen (· / darf-muss-man / Zahl der „=“). |
| B2 | 018, 068; 028, 035 | Doppelte Urteile verraten etwas. In 018 sagen zwei Optionen „Beide“, in 068 zwei Optionen „Es passt“. Weil genau eine Option richtig ist, scheiden beide Paare aus, und es bleibt eine Wahl 1 aus 2. In 028 und 035 hat die richtige Option dieselbe Fehlerdiagnose wie genau ein Ablenker; damit schrumpft die Wahl auf diese zwei. | Je Aufgabe jedes Urteil (erster Satzteil) höchstens einmal. Die Prüfung in `bauen.py` von „gleich der richtigen“ auf „irgendwo doppelt“ erweitern. |
| B3 | 068 | Ablenker 0 („Man weiß es nicht … es muss genau gerechnet werden“) ist hier teilweise wahr. Der Überschlag 20 · 50 = 1 000 liegt genau auf der Grenze, und weil eine Zahl auf- und eine abgerundet wurde, entscheidet er allein nicht; auch die richtige Option rechnet genau. Die Fehlbild-Beschreibung „obwohl hier der Abstand zur Grenze groß genug ist“ ist sachlich falsch. | Ablenker 0 ersetzen, z. B. durch „Es passt, denn 1 000 ist erlaubt (höchstens 1 000)“. Die richtige Option begründet dann mit der Rundungsrichtung. |
| B4 | 012 | Sehr nahe an themen „Zwei Quadratzahlen, die direkt aufeinander folgen, unterscheiden sich um 31“: gleiche Rechnung (Unterschied zweier Nachbarquadrate), nur eingekleidet. | Um 2 Reihen und 2 Spalten erweitern lassen: (n + 2)² − n² = 64, also nachher 17 Reihen. |
| B5 | 025 | Sehr nahe an themen „Eine Zahl wird, beginnend bei 1, fünfmal verdoppelt. Welche Potenz beschreibt das Ergebnis?“ (fast derselbe Wortlaut, nur Start 3). | Umdrehen: Zu 3 · 2⁵ die passende Geschichte wählen lassen. |
| B6 | 019 | Nahe an themen „Eine Zahl wird mit 10³ multipliziert und dann durch 10 geteilt. Es kommt 52 000 heraus“. Außerdem Schema. | Streichen (siehe Streichvorschlag). |
| B7 | 015 (Test zehner) | Durch bloßes Ausrechnen lösbar (1 000 000 − 900 000 = 100 000). In der vorigen Runde wurde die Aufgabe nicht beanstandet, nach dem Maßstab ist sie aber ein Risiko. Die `idee` „groessenvergleich“ passt nicht zum Inhalt. | Eine Fehlvorstellung beurteilen lassen, z. B. „Lena: 10⁶ − 10⁵ = 10¹, weil 6 − 5 = 1“ mit 4 Urteilen. |
| B8 | 063 | Nahe an themen „teile durch 7, nimm mal 3, erhalte 27“ und rollend-11 (drei Schritte rückwärts). Gleiche Denkfigur wie 075 im Lernziel sach. | Streichen. |
| B9 | 069, 070 | 069 ist nahe an themen „48 · 52 mit 40 · 50 überschlagen: Was ist ungünstig? 48 stark abgerundet“. 070 ist nahe an themen „auf Hunderter gerundet 800: kleinste Zahl?“ (hier mit Summe aus kleinster und größter Zahl). | 070 streichen. Bei 069 das Neue (Plausibilität eines Ergebnisses beurteilen) in der Frage stärker betonen. |
| B10 | 074, 077 | Gleiches Zahlenmaterial (verdoppeln, plus 6, Ergebnis 30) und gleiche Denkfigur (Reihenfolge der Schritte beim Umkehren). Der Lösungsweg von 074 zeigt Teile von 077. | 077 mit anderer Struktur und anderen Zahlen bauen, z. B. die Probe mit einem Überschlag oder eine Gleichung, die zwei Geschichten gemeinsam haben. |
| B11 | 053 | Die Frage nennt das richtige Ergebnis 108; es genügt, beide Wege auszurechnen (Schema). Die richtige Option ist die einzige mit „Beide“ und hat als einzige zwei vollständige Rechnungen. | Siehe A13. |
| B12 | 049 | Format der Bestand-Übung „Rechne geschickt: … + … − …“; nur das Mitnehmen des Minuszeichens ist neu. | Als Fehler-Aufgabe bauen (wer nimmt das Zeichen nicht mit?) oder streichen. |
| B13 | 039, 073 | Text zu Term wählen, wie bei themen „Welcher Term passt: 6 Kinder zahlen je 4 €, dazu kommen 10 €“ und „Ein Fest: 39 Gäste …“. | Bei 073 zwei Geschichten zu derselben Gleichung vergleichen lassen; 039 als einzige Schema-Aufgabe zulassen. |
| B14 | 064 | Sprache: zwei Fragen in einer („Wie oft passt …, das heißt: Um welchen Faktor …“). | Eine Frage: „Um welchen Faktor ist Tims Ergebnis ungefähr zu klein?“ |
| B15 | 044 | Der Text („auf einmal eine Zahl □ abziehen“) verrät den Lösungsweg. | Nur die Gleichung 94 − 37 − 23 = 94 − □ geben. |
| B16 | 008, 014 | Gleiche Einzelfrage: Die Seite verdoppelt sich, die Fläche vervierfacht sich. Test und Sicherung prüfen dasselbe. | 014 streichen (siehe A4). |
| B17 | 004 | Dieselbe Tatsache 4⁴ = 256 wie der bisherige themen-Test „4 hoch wie viel ergibt 256?“; der Bestand hat außerdem „Exponent 3 und Wert 1 000: Basis?“. Lösbar durch Ausrechnen und Probieren. | Zahlen ändern, z. B. □³ = 2⁹ (□ = 8). Besser mit Begründungsauswahl („weil je drei Zweier eine 8 ergeben“). |

### C (Kann)

| Nr | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| C1 | 009, 016, 033, 037 | Die Fehlbild-Beschreibungen nennen keinen Denkfehler, sondern nur, warum die Option nicht passt: bei 009 dreimal derselbe Text „Ist eine Quadratzahl …“, bei 016 „Stimmt: …“. | Je Ablenker den vermuteten Fehler nennen (z. B. „nur die erste Ziffer geprüft“). |
| C2 | 009 | Gleiche Einsicht wie die themen-Übung „Jede Quadratzahl endet auf 0, 1, 4, 5, 6 oder 9“, aber eine andere Denkleistung (anwenden statt bestätigen). Das darf bleiben. | – |
| C3 | 022 | „Kultur A … Zellen“ ist für Klasse 5 ungewohnt. | „Bakterien in Schale A …“ |
| C4 | 060 | Fehlbild zu „x : 8 = 56“ („Lösung 8 mit 56 verwechselt“) ist keine plausible Fehlvorstellung. | Ablenker „56 : 7 = x · 2“ o. ä. mit echter Verwechslung. |
| C5 | ueberschlag | Regel fehlt (laut Auftrag nur vermerkt). | – |
| C6 | Bestand | `rollend-15` enthält keine Aufgaben dieser Einheiten; geprüft wurden themen, rollend-5, -11, -12. | – |
| C7 | 055 | Ablenker 0 (einzeln ausrechnen) führt zum richtigen Wert; falsch ist nur „am geschicktesten“. Das ist zulässig, die Gegenprüfung könnte es aber als Grenzfall sehen. | Im Ablenker einen Rechenfehler einbauen oder „sicherer“ statt „geschickter“ als Urteil wählen. |

## Tabelle je Lernziel (Schema streng, „im Zweifel Schema“)

T = Test, K = Korrektur, S = Sicherung. „Streichen“: je eine K- und eine S-Aufgabe, so wie der Projektleiter es verlangt.

| Lernziel | Schema (alle 7) | Denkfiguren (inhaltlich) | Test ok? | Streichen K / S | Die verbleibenden 5 erfüllen den Maßstab? |
|---|---|---|---|---|---|
| schreibweise (001–007) | 001, 002, 003, 004 (4) | Basen/Hochzahlen nicht addieren 001 · Hochzahl + 1 = mal Basis 002 · Verdopplung als Potenz 003 · Potenz umschreiben 004 · Bedeutung 005 · Vertauschen gilt nicht allgemein 006 · Potenz vor Mal 007 (7) | **nein** (A1) | K 003 / S 005 | **nein**: 001, 002, 004 sind Schema (3). Mit Test := 006 und Ersatz von 001 und 002 (A1, A3) wird der Maßstab erreicht. |
| quadrat (008–014) | 010, 011, 014 (3) | Seite ·2 → Fläche ·4 008, 014 · Endziffer 009 · Unterschied der Quadrate 010 · (a + b)² ≠ a² + b² 011 · Nachbarquadrate 012 · (a · b)² = a² · b² 013 (6) | ja | K 010 / S 014 | **ja**: Schema nur 011; 5 Denkfiguren; Test 008 ist die anspruchsvollste. Dazu 012 umbauen (B4). |
| zehner (015–021) | 016, 019 (2); Risiko 015, 017 | 10⁶ = 10 · 10⁵ 015 · Faktor und Hochzahl gleichen sich aus 016, 018 · Größe → Potenz 017 · Kette rückwärts 019 · Plus ≠ Hochzahlen addieren 020 · Schranke 021 (6) | knapp (B7) | K 016 / S 019 | **knapp nein**: 015 und 017 sind durch Ausrechnen lösbar (2). Ein Umbau von 015 nach B7 genügt. |
| sach Potenzen (022–028) | 023, 024, 027 (3) | linear gegen Verdopplung 022 · Exponent aus Wachstum 023 · Folgen zählen 024 · Startwert nicht unter die Hochzahl 025, 028 · Verhältnis bleibt 026 · Startwert rückwärts 027 (6) | ja | K 023 / S 027 | **ja**: Schema nur 024; 4 Denkfiguren (025 und 028 gleich); Test 022 ist die anspruchsvollste. 025 umbauen (B5). |
| klammern (029–035) | 029, 032, 034 (3) | Ziel herstellen 029 · Lücke rückwärts 030 · Term ↔ Text 031 · kleinster Wert 032 · überflüssige Klammer 033 · Werte vergleichen 034 · links nach rechts falsch 035 (6–7) | **nein** (A7) | K 032 / S 034 | **nein**: Der Test 029 ist Schema und Bestand, 030 ist Bestand. Mit Test := 033, 029 als Sicherung und 030 ersetzt: ja. |
| termaufbau (036–042) | 037, 038, 039 (3) | Äquivalente Terme zur Geschichte 036 · Struktur 037 · Text → Term 038, 039 · Tarif rückwärts 040 · Parameter 041 · Änderungswirkung 042 (6) | ja | K 037 / S 040 | **nein**: 038 und 039 sind Schema und dieselbe Denkfigur. Mit 038 ersetzt (A9): ja. |
| vorteil (043–049) | 044, 047, 049 (3); Grenzfall 048 | Ausgleich (gegensinnig ändern) 043, 048 · zu 100/1 000 bündeln 045, 047 · Minus zusammenfassen 044 · Vertauschen gilt nicht bei : 046 · Zeichen mitnehmen 049 (5) | ja | K 045 / S 047 | **nein**: 044 und 049 sind Schema, 046 ist Bestand. Mit 046 und 049 umgebaut (A11, B12) und 044 nach B15: ja. |
| verteilen (050–056) | 050, 051, 053 (3) | Ausklammern 050, 051, 055, 056 (viermal) · Situation → Term 052 · zwei Zerlegungen 053 · Wirkung der Höhe 054 (4) | **nein** (A13) | K 051 / S 055 | **nein**: Der Test 050 ist Schema und Bestand, 053 ist Schema. Mit Test := 054, 050 entfernt und 053 umgebaut: Schema nur 052 möglich, 4 Denkfiguren, ja. |
| umkehraufgabe_mal (057–063) | 058, 060, 063 (3) | Lösbarkeit als Teiler bzw. Reihe 057, 062 · Umkehrrechnung wählen 058, 060 · Zahlen aus Produkt und Summe 059 · Geschichte ↔ Gleichung 061 · Kette rückwärts 063 (5) | ja | K 058 / S 063 | **nein, nur wegen 062**: Schema nur 060, 4 Denkfiguren, Test 057 ist die anspruchsvollste. 062 hat aber verbotene Ablenker (A15). Mit 062 umgebaut: ja. |
| ueberschlag (064–070) | 064, 066, 070 (3) | Größenordnung prüfen 064 · Rundungsfenster 065, 070 · Richtung der Abweichung 066 · feiner runden 067 · Grenze und Rundungsrichtung 068 · zu grober Überschlag 069 (6) | **nein** (A16) | K 066 / S 070 | **nein**: Der Test 064 ist Schema, 065 ist Bestand. Mit Test := 068 (nach B3), 064 als Sicherung und 065 ersetzt: ja. |
| sach Rechengesetze (071–077) | 072, 073, 075 (3) | Gleichsetzen 071 · rückwärts 072, 075 · Gleichung aufstellen 073, 076 · Reihenfolge der Schritte 074, 077 · fünfmal Rückwärtsrechnen im Kern (072, 074, 075, 076, 077) | ja | K 072 / S 075 | **knapp nein**: Schema nur 073. Aber 073 und 076 haben dieselbe Denkfigur, 074 und 077 ebenfalls (mit gleichen Zahlen), also nur 3 verschiedene. Mit 077 neu gebaut (B10): ja. |

## Protokoll je Aufgabe

Spalten: Kennung (Pool): Nachrechnung · Ablenker · Schema/Verstehen · Bestand · Befund. „R ok“ heißt: Die eigene Rechnung stimmt mit der Sollantwort überein, und bei Auswahl ist genau eine Option wahr.

- 001 (T): R ok (17) · Ablenker haben andere Werte, kein verbotener Typ · Schema · – · A1
- 002 (K): R ok (162) · Fehlbilder ≠ Lösung, passen zur Rechnung · Schema · – · A3
- 003 (K): R ok (16) · ok · Schema (Folge um eine Verdopplung fortsetzen) · nahe themen Reiskorn/Folge · A3, Streichvorschlag
- 004 (K): R ok (4) · ok · Schema (Probieren) · gleiche Tatsache wie der themen-Test 4⁴ = 256 · B17
- 005 (S): R ok · ok · Reproduktion · = themen „Was bedeutet 5⁴/2⁷“ · A2
- 006 (S): R ok · Ablenker haben falsche Folgerungen (vertauschbar) · Verstehen · – · Testkandidat
- 007 (S): R ok · Diagnosen und Werte verschieden · Verstehen · – · ok
- 008 (T): R ok (576) · ok · Verstehen (Grenzfall) · – · B16
- 009 (K): R ok (6 727; 86², 77², 69² nachgerechnet) · Ablenker sind echte Quadratzahlen · Verstehen · Einsicht wie themen-Endziffer (darf bleiben) · C1, C2
- 010 (K): R ok (72) · ok · Schema, der Text nennt das Verfahren · nahe themen „15² − 14²“ · A4
- 011 (K): R ok (81) · ok · Schema · – · A4
- 012 (S): R ok (14, eindeutig) · ok · Verstehen · nahe themen Nachbarquadrate 31 · B4
- 013 (S): R ok (Kein Fehler) · ok · Verstehen · – · ok
- 014 (S): R ok (4-mal) · Werte verschieden · Schema (ausrechenbar) · – · A4, B16
- 015 (T): R ok (1) · ok · Schema-Risiko · – · B7
- 016 (K): R ok (56 · 10⁵) · ok · Schema · = rollend-5 3 400 000 · A6, C1
- 017 (K): R ok (5) · ok · Schema-Risiko · – · ok
- 018 (K): R ok (Nur Anna) · zweimal „Beide“, beide ausschließbar · Grenzfall · ähnlich themen „43 · 10 hoch …“ · B2
- 019 (S): R ok (1 000) · ok · Schema · nahe themen 52 000 rückwärts · B6
- 020 (S): R ok · Diagnosen und Werte verschieden · Verstehen · anderer Fehler als themen 30⁴ · ok
- 021 (S): R ok (6) · ok · leicht · – · ok
- 022 (T): R ok (11; Stunde 10: 1 100 > 1 024, Stunde 11: 1 200 < 2 048) · ok · Verstehen · – · C3
- 023 (K): R ok (6) · ok · Schema · themen Falten (vorwärts) · Streichvorschlag
- 024 (K): R ok (32) · ok · Schema · – · ok
- 025 (K): R ok (3 · 2⁵) · ok · Grenzfall · nahe themen „fünfmal verdoppelt“ · B5
- 026 (S): R ok (2) · ok · Verstehen · – · ok
- 027 (S): R ok (5) · ok · Schema · = rollend-12 Bakterien und themen 200 → 25 · A5
- 028 (S): R ok (162) · gleiche Diagnose wie Ablenker 0 · Verstehen · – · B2
- 029 (T): R ok ((20 − 4) · 3 + 2 = 50; zwei Klammerpaare unzulässig) · ok · Schema · = themen Klammer-Ziel · A7
- 030 (K): R ok (6) · ok · Verfahren · = rollend-5 und themen Klammer-Lücke · A8
- 031 (K): R ok · ok · Grenzfall · Satz zum Term auch in themen termaufbau (anderes Lernziel) · ok
- 032 (K): R ok (10) · ok · Schema (nur zwei Stellungen möglich) · – · Streichvorschlag
- 033 (S): R ok · ok · Verstehen · – · Testkandidat, C1
- 034 (S): R ok (3) · ok · Schema · – · Streichvorschlag
- 035 (S): R ok (20) · gleiche Diagnose wie Ablenker 0 · Verstehen · anderer Fehler als themen · B2
- 036 (T): R ok (① und ②) · ok · Verstehen (Grenzfall, Werte 20/20/28/28) · – · ok
- 037 (K): R ok · ok · Reproduktion · = themen „Produkt, dessen erster Faktor eine Summe ist“ · A9
- 038 (K): R ok (25) · ok · Schema · = themen Text → Term · A9
- 039 (K): R ok · ok · Schema · nahe themen/rollend-5 Einkauf · B13
- 040 (S): R ok (6) · ok · Verfahren · – · Streichvorschlag
- 041 (S): R ok (1, eindeutig in ℕ) · ok · Verstehen · – · ok
- 042 (S): R ok (4 kleiner) · ok · Verstehen · – · ok
- 043 (T): R ok (gleich, 15 000) · Ablenker haben andere Urteile · Verstehen · – · ok (richtige Option ist die längste, einziges „Beide“)
- 044 (K): R ok (60) · ok · Schema, der Text verrät den Weg · – · B15
- 045 (K): R ok · ok · Grenzfall · = rollend-5 25 · 17 · 4, themen 8 · 37 · 125 · A10
- 046 (K): R ok (36 : 4) · ok · Verstehen · = themen „Welche Gleichung ist falsch?“ · A11
- 047 (S): R ok (4) · ok · Schema · = themen und rollend-12 Lücke · A12
- 048 (S): R ok (81) · ok · Grenzfall (486 : 6) · – · ok
- 049 (S): R ok (8 003) · ok · Schema · Format „Rechne geschickt“ · B12
- 050 (T): R ok (3 240) · ok · Schema · = themen „a · b − a · c geschickt“ · A13
- 051 (K): R ok (36) · ok · Schema · – · Streichvorschlag
- 052 (K): R ok (90) · ok · Grenzfall · nahe rollend-5 Rechteck-Term · ok
- 053 (K): R ok (Beide) · Ablenker haben andere Urteile · Schema (108 genannt) · nahe rollend-12 Zerlegen · A13, B11
- 054 (S): R ok (Verdopplung, 256 → 512) · ok · Verstehen · – · Testkandidat
- 055 (S): R ok · Ablenker 0 hat den richtigen Wert · Grenzfall · nahe themen „geschickter Weg für 19 · 25“ · C7, Streichvorschlag
- 056 (S): R ok (240) · ok · Verstehen · anderer Fehler als themen · ok
- 057 (T): R ok (7: 1, 2, 3, 4, 6, 9, 12) · ok · Verstehen · – · ok
- 058 (K): R ok (36 : 9) · ok · Schema · = themen „Welche Rechnung führt zur Lösung“ · A14
- 059 (K): R ok (8, eindeutig) · ok · Probieren mit Bedingung · – · ok
- 060 (K): R ok (56 : x = 7) · ok · Schema · – · C4
- 061 (S): R ok · ok · Verstehen · – · ok
- 062 (S): R ok · **alle Ablenker mit richtiger Folgerung** · – · – · A15
- 063 (S): R ok (4) · ok · Schema · nahe themen und rollend-11 · B8
- 064 (T): R ok (10) · ok · Schema · ähnlich themen „Entscheide mit Überschlag“ · A16, B14
- 065 (K): R ok (34) · ok · Verfahren · = themen „größte a, a · 30 = 1 800“ · A17
- 066 (K): R ok (6) · ok · Schema · – · Streichvorschlag
- 067 (K): R ok (B: 8 300 gegen 8 000) · ok · Verstehen · Weg A/B in rollend-5 (andere Frage) · ok
- 068 (S): R ok (1 104 > 1 000) · Ablenker 0 teilweise wahr, „Es passt“ doppelt · Verstehen · Kino/Lkw im Bestand (anderer Kern) · B2, B3, Testkandidat
- 069 (S): R ok (596 · 12 = 7 152) · ok · Verstehen · nahe themen 48 · 52 · B9
- 070 (S): R ok (4 550 + 4 649 = 9 199) · ok · Schema · nahe themen „gerundet 800“ · B9
- 071 (T): R ok (4 GB, je 20 €) · ok · Verstehen · – · ok
- 072 (K): R ok (6) · ok · Schema · ähnlich themen Klassenkasse · A17, Streichvorschlag
- 073 (K): R ok (21; die Ablenker haben andere oder keine Lösung) · ok · Schema · nahe themen Text → Term · B13
- 074 (K): R ok (24) · ok · Verstehen · Weiterführung von rollend-5 · B10
- 075 (S): R ok (38) · ok · Schema · = themen Sticker-Hälfte · A17
- 076 (S): R ok (25; Ablenker 16, 29, 23 jeweils in ihrem Modell richtig) · ok · Verstehen · – · ok
- 077 (S): R ok (Kein Fehler, 12) · ok · Verstehen · – · B10
