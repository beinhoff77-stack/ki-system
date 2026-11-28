# Zweite Vorprüfung Welle 1 (Runde 2) – zahlen.natuerlich und terme.umformen, Fassung 5 je Lernziel

Stand 29.11.2026, geprüfter Stand `9a986063` (Zweig `schreiber-w1-r2`). Umfang: 50 Aufgaben, VT2-085 … 119 (zahlen.natuerlich, 7 Lernziele) und VT2-029 … 043 (terme.umformen, 3 Lernziele), je 1 Test + 2 Korrektur + 2 Sicherung.

Maßstab je Lernziel:
- höchstens eine Schema-Aufgabe unter den fünf (im Zweifel Schema);
- der Test ist nie Schema und ist die anspruchsvollste Aufgabe;
- mindestens vier verschiedene Denkfiguren; die Tests einer Einheit haben verschiedene Denkfiguren;
- kein Bestandskern derselben Etappe (gleiche Rechnung, gleicher Fehler, gleiche Frage);
- genau eine richtige Möglichkeit, kein Ablenker mit richtigem Urteil und nur falscher Begründung, keine wörtlich wahren Ablenker;
- kein Bauart-Merkmal;
- eindeutig, für die Klassenstufe lösbar und verständlich;
- neu: realistische Schwierigkeit der Tests.

Grundlage: Urteil 1222 und `vorpruefung-w1.md`. Den Bestand (Etappen der Themen-Dateien, `rollend-5`, `-7`, `-11` bis `-15`) habe ich gegen alle 27 neuen oder umgebauten Aufgaben neu gelesen; er ist seit `67a9f804` unverändert.

**Nachrechnung:** `vorpruefung_w1_rechnen.py` ist für diese Fassung neu geschrieben, eigene Rechnung, exakt, wo möglich durch vollständiges Durchprobieren. Ergebnis: **0 Abweichungen bei 50 Sollantworten**. Alle Fehlbild-Rechnungen ergeben ihre Antwort, jede Lücke hat ein eigenes Fehlbild. Gezielt bestätigt:
- 085: 984 764 (alle sechsstelligen Zahlen geprüft)
- 086: Differenz immer 4, sechs Ziffernpaare möglich
- 090: 999
- 093: 900 000
- 094: 3 und 100 100 100
- 110: 49 ist die einzige Zahl mit Ersparnis 5
- 113: 3 999
- 115: 10 Spiegelzahlen
- 117: Unterschied immer 63
- 118: jede Endung 00 ist durch 4 teilbar
- 029: a = 4, alle Seiten positiv für x > 0
- 034: a = 9, eindeutig
- 041: k = 20

## Urteil

| Einheit | bereit für die Gegenprüfung? | Gründe |
|---|---|---|
| zahlen.natuerlich | **nein** | strahl_eintragen: Test 095 ist ein bekanntes Verfahren (A1). runden_sinnvoll und roemisch_schreiben haben je zwei Schema-Aufgaben (A2, A3). 118 hat den Kern von themen #437 (A4). |
| terme.umformen | **nein** | Alle drei Lernziele haben je zwei Schema-Aufgaben (A5–A7). 040 hat den Kern von themen #237 (A8). |

Den Maßstab erfüllen jetzt **stellenwert, ziffern_zu_zahlwort und runden_regel**. Die übrigen sieben Lernziele scheitern je an **einer** Aufgabe; ein gezielter Ersatz je Lernziel genügt, ein Neubau ganzer Sätze ist nicht nötig.

**Ehrliche Einordnung der Strenge.**
- Sicher würde die Gegenprüfung A1 (Test 095), A4 (118), A8 (040) und A7 (042) finden.
- A2 (106), A3 (113), A5 (031) und A6 (038) folgen aus „im Zweifel Schema“: Die Antwort ergibt sich durch einmaliges Auflösen, Einsetzen oder Abarbeiten einer im Text vorgegebenen Anleitung. Eine mildere Gegenprüfung ließe einzelne davon als Verstehen durchgehen.
- Immer/manchmal/nie-Aufgaben, bei denen man ein Gegenbeispiel selbst finden muss (096, 103, 104, 112, 118), zähle ich nicht als Schema.

---

## Befunde A (Muss)

**A1 – strahl_eintragen: Test 095 ist Schema, nicht die anspruchsvollste Aufgabe, und fragt dasselbe wie die Korrektur 097.**
- 095: Wert je cm aus zwei Marken bestimmen, dann Differenz teilen bzw. vervielfachen. Das ist genau das Verfahren aus rollend-5 K5A-V013 („Ein Abschnitt ist (3 000 − 2 000) : 5 = ① wert, die Zahl liegt (2 600 − 2 000) : ① = ② Abschnitte nach dem Anfang“), dazu themen #154/#164. Ein gutes Kind löst es in 1–2 Minuten.
- 097: zwei Divisionen 600 : 50 und 600 : 200 (Schema) und dieselbe Einzelfrage wie 095 Lücke 1 (Abstand zweier Marken in cm aus dem Maßstab). 098 ist ein Zweifelsfall (durch Auflisten lösbar).
- 096 und 099 verlangen mehr als der Test.

*Vorschlag:* neuer Test mit Einsicht, z. B. „Zwei Zahlen liegen auf Strahl A 6 cm, auf Strahl B 4 cm auseinander. Auf A steht 1 cm für 50. Wofür steht 1 cm auf B?“ (75; gleicher Unterschied 300, umgekehrtes Verhältnis). 095 und 097 streichen. Als zweite Korrektur z. B. 099 vorziehen oder eine Rückwärtsaufgabe mit Strich/Abstand-Wahl. Danach bleibt 098 die eine Zweifels- bzw. Schema-Aufgabe.

**A2 – runden_sinnvoll: zwei Schema-Aufgaben (108, 106).**
- 108: drei Produkte ausrechnen.
- 106: Jede Hälfte ist die in Klasse 5 geübte Deutung einer Division mit Rest („höchstens“ → abrunden, „mindestens“ → aufrunden), im Bestand als K5A-V027 und R5-V017 vorhanden. Das Gegenüberstellen ist gut, verlangt aber keinen Schritt über die Routine hinaus.

*Vorschlag:* 108 durch eine Aufgabe mit Urteil ersetzen, z. B. „Lea schätzt 48 · 29 mit 50 · 30, Tom mit 50 · 28. Welche Aussage stimmt?“. Richtig: „Nur Leas Schätzung liegt sicher über dem genauen Wert, weil sie beide Faktoren aufgerundet hat; bei Tom hängt es von den Zahlen ab.“ Dann ist 106 die eine Schema-Aufgabe.

**A3 – roemisch_schreiben: zwei Schema-Aufgaben (111, 113).** 113 gibt die Bauanleitung selbst vor („jede Stufe für sich“, „für die Tausender nur M“, „höchstens dreimal“). Dann ist die größte Zahl MMM + CM + XC + IX, also Abarbeiten. *Vorschlag:* 113 ohne die Anleitung stellen, z. B. „Nach den üblichen Regeln (höchstens dreimal hintereinander, kein Zeichen über M): Welches ist die größte schreibbare Zahl?“. Die Einsicht „bei 4 000 bräuchte man vier M“ muss dann das Kind haben. Oder 113 ersetzen.

**A4 – VT2-118 (Sicherung dualsystem) hat den Kern von themen #437.** #437: „Jede Zweierzahl, die auf 0 endet, ist gerade – Ja: Alle Stellenwerte außer der 1 ganz rechts sind gerade Zahlen.“ 118: „… endet auf 00 … durch 4 teilbar, denn alle Stellenwerte außer 1 und 2 sind Vielfache von 4.“ Gleiche Begründung, gleiche Frage (welche Aussage über die Teilbarkeit folgt), nur 0/2 gegen 00/4. *Vorschlag:* Ersatz mit eigener Denkfigur, z. B. der Übertrag im Zweiersystem: „Ein Zähler aus 6 Lampen zeigt 101111. Nach wie vielen Schritten (+1) leuchten zum ersten Mal nur noch zwei Lampen?“ (1, denn 110000).

**A5 – zusammenfassen: zwei Schema-Aufgaben (030, 031).** In 031 nennen die Möglichkeiten selbst die Prüfwerte x = 0 und x = 1. Einsetzen von 0, 1 (und 2) schließt alle drei Ablenker aus, also löst bloßes Ausrechnen die Aufgabe. Nähe zu themen #6/#27. *Vorschlag:* 031 durch eine Aufgabe ersetzen, die man nicht durch Testwerte entscheidet, z. B. „In 3x² + 5x − 2 + □ steht für □ genau ein Glied (a · x², a · x oder eine Zahl, a ganz und nicht 0). Wie viele Glieder hat das zusammengefasste Ergebnis mindestens, wie viele höchstens?“ (2 und 3).

**A6 – minusklammer: zwei Schema-Aufgaben (035, 038).** 038: Einmaliges Auflösen −(x − 7) = −x + 7 = 7 − x entscheidet die Frage, und Einsetzen von x = 10 widerlegt Ben. Nähe zu themen #93. *Vorschlag:* 038 ersetzen durch eine Aufgabe, deren Antwort nicht aus einem einzigen Auflösen folgt, z. B. eine Modellwahl mit zwei Klammern in einem anderen Sachkontext als 036, oder eine Rückwärtsaufgabe mit Wahl.

**A7 – aequivalenz: zwei Schema-Aufgaben (042, 043).** 042: 3(x + 4) − x vereinfachen zu 2x + 12, mit 2x + 9 vergleichen, Antwort 0. Das ist Vereinfachen und Vergleichen. *Vorschlag:* 042 als Klassifikation mit Urteil: „Für welche Zahlen a und b haben a · x + 9 und 2x + b für genau eine, für keine bzw. für jede Zahl x denselben Wert?“ (Auswahl mit je eigenem Urteil; a ≠ 2 → genau eine; a = 2, b ≠ 9 → keine; a = 2, b = 9 → jede).

**A8 – VT2-040 (Korrektur aequivalenz) hat den Kern von themen #237.** #237: Rahmen um ein n × n-Quadrat, „Anna zählt 4n + 4, Ben 4(n + 2) − 4. Was stimmt?“. 040: Hölzchenreihe, Mia 4 + 3(n − 1), Ben 3n + 1, Lena 4n − n − 1, wie viele stimmen. Gleiche Rechnung (Zählterme vereinfachen und vergleichen), gleicher Fehler (ein Term falsch), gleiche Frage (welche Terme stimmen). Der andere Kontext und die Zusatzfrage „Figur 10“ ändern den Kern nicht. Dazu rollend-13 R8-V009. *Vorschlag:* Darstellungswechsel in die andere Richtung, z. B. „Zu welcher Zählweise passt der Term 4 + 3(n − 1)?“ mit vier beschriebenen Zählweisen.

## Befunde B (Soll)

- **B1 – Test 110 lösen wohl nur sehr starke Kinder.** Langer Text mit zwei vollständigen Regelwerken, dazu die Einsicht „Ersparnis nur bei den Ziffern 4 und 9 je Stufe, bei 9 mehr“. In 2–3 Minuten schafft das kaum ein Kind der 5. Klasse. *Vorschlag:* Art 1 kürzer fassen (Beispiel IIII, XXXX statt Regeltext) oder den Bereich auf 1 bis 50 verkleinern.
- **B2 – Test 115 lösen wohl nur sehr starke Kinder.** Man muss erkennen, dass Mias Lesart die Zahl rückwärts liest, und dann alle Spiegelzahlen mit bis zu 5 Ziffern vollständig aufzählen (10). Realistisch braucht das eher 5 Minuten. *Vorschlag:* „höchstens vier Ziffern“ (1 bis 15, Lösung 6), dann bleibt die Einsicht und die Aufzählung wird kurz.
- **B3 – Test 100:** Dass 1 bis 49 auf Hunderter gerundet 0 ergeben, ist für Kinder der 5. Klasse ungewohnt und führt zu Unsicherheit („ist 0 eine Hunderterzahl?“). *Vorschlag:* „(Auch 0 kann als Ergebnis herauskommen.)“ ergänzen.
- **B4 – Bauart: Die Möglichkeit „nicht entscheidbar / nichts Sicheres“ ist nie richtig.** Sie steht in 039 (zweimal), 086, 091, 096, 097, 099 und 118, immer falsch. Wer sie ausschließt, hat bei 8 Aufgaben nur noch 3 Möglichkeiten. *Vorschlag:* in mindestens einer neuen Aufgabe „nicht entscheidbar“ zur richtigen Möglichkeit machen (z. B. beim Ersatz für 108: „bei Tom hängt es von den Zahlen ab“).
- **B5 – Bauart: Die Sammel-Möglichkeit steht nur in der richtigen.** In 103 („Jeder der drei Fälle“) ist sie zugleich die Vereinigung der drei Teilfälle aus den Ablenkern; in 116 („Beide sind gleich groß“). Über alle Aufgaben ist es ausgeglichen (Sammel-Urteile: 3 richtig, 5 falsch in 036, 038, 107), aber innerhalb von 103 und 116 ist es ein Hinweis. *Vorschlag:* In 103 einen Ablenker ebenfalls als Sammel-Aussage („Alle drei Fälle sind möglich, aber nur bei Zahlen über 100 000“).
- **B6 – Bauart Länge, 104:** Die richtige Möglichkeit ist mit 134 Zeichen deutlich die längste (sonst 99–114) und die einzige mit zwei Teilaussagen („nie größer und kann gleich sein“). *Vorschlag:* Ablenker ebenfalls zweiteilig („kann größer sein und ist nie gleich“).
- **B7 – 109, Ablenker 2:** „Mia hätte zuerst genau addieren und erst danach runden müssen …“. Das Urteil ist als Rat vertretbar (genauer), nur die Begründung „dann kommt genau die richtige Summe heraus“ ist falsch. Damit grenzt es an die verbotene Ablenkerart. *Vorschlag:* ein falsches Urteil, z. B. „Mia hat sich verrechnet, denn vier gerundete Zahlen ergeben zusammen 14 000.“
- **B8 – Dieselbe Denkfigur in zwei Lernzielen der Einheit:**
  - 086 (Tausch zweier Stellen im Zehnersystem: nur die getauschten Stellen ändern den Wert) und 117 (dasselbe im Zweiersystem).
  - 093 (falsche Einteilung von links: wann zufällig richtig, zählen) und Test 115 (falsche Leserichtung: wann zufällig richtig, zählen).

  Die Systeme sind verschieden, die Denkfigur ist dieselbe; 115 ist durch 093 vorgeübt. *Vorschlag:* 117 oder 093 auf eine andere Figur umstellen.
- **B9 – Tests der Einheit zahlen.natuerlich: gleiche Aufgabenform.** 090, 100, 110 und 115 fragen alle „über einen Zahlbereich zählen oder das Maximum suchen“. Die Einsichten sind verschieden (leere Klasse, Rundungsbereiche, Ersparnis je Stufe, Spiegelzahl), deshalb kein Muss. Vier von sieben Tests in derselben Form fallen aber auf. *Vorschlag:* den Ersatztest für strahl_eintragen (A1) und ggf. 115 (B2) nicht wieder als Bereichs-Zählung bauen.
- **B10 – terme.umformen, Schlussform:**
  - 029 (4a = 16), 034 (2a = 18) und 042 enden alle mit „x-Teil gleich, es kommt auf das Zahlglied an“.
  - Klar entschieden: Die Tests **029 und 039 haben nicht dieselbe Denkfigur**. 029 nutzt den Koeffizientenvergleich als Werkzeug, 039 begründet, warum zwei Einsetzungen a · x + b festlegen; das ist zulässig.
  - 029 und 034 haben verschiedene Einsichten (Umfang modellieren gegen Wirkung des Vorzeichenfehlers), aber dieselbe Schlussform. Mit dem Umbau von 042 (A7) entschärft.
- **B11 – Bestandsnähe (gleiche Einsicht, andere Denkleistung; darf bleiben, ist aber angreifbar):**
  - 090 ↔ themen #100 („wie oft sagt man ‚tausend‘ von 1 bis 10 000“, gleiche Etappe)
  - 094 ↔ #85/#95 (ein Wort je Klasse)
  - 086 ↔ #10
  - 092 ↔ S3-V002/R5-V006
  - 109 ↔ S3-V005
  - 031 ↔ #6/#27
  - 036 ↔ #89 (Konto 8x − (3x − 5))
  - 038 ↔ #93
- **B12 – 112 Lernziel-Passung:** „Mehr Zeichen heißt nicht größer, anders als im Stellenwertsystem“ ist der Kern der Nachbar-Etappe roemisch_system (#424, #429, #408 ff.), nicht von roemisch_schreiben. Als Bestandskern derselben Etappe zählt das nicht, die Gegenprüfung könnte die Passung aber bemängeln.

## Befunde C (Kann)

- C1 – 090 und 091 (Test und Korrektur) drehen sich beide um die nicht gesprochene Klasse; die Einzelfragen sind verschieden (wann fällt „tausend“ weg, wie viele Stellen bleiben), deshalb zulässig.
- C2 – 039 widerspricht bewusst der Merkregel aus dem Bestand („Einsetzen beweist nichts“, R15-V045). Der Lösungsweg erklärt die Ausnahme gut; ein Satz im Lösungsweg „das gilt nur, weil die Form a · x + b vorgegeben ist“ steht schon da. In Ordnung.
- C3 – 042: `loesung_rechnung` „12 − 9 − 3“ ist künstlich (ergibt 0 ohne Bezug).
- C4 – 112: „nach den üblichen Regeln“ ist nicht ausgeschrieben. Unkritisch, weil die Beispiele keine Subtraktion brauchen.
- C5 – 117: Fehlbild 999 999 („wie im Zehnersystem“) ist wenig plausibel.
- C6 – 105: Rundungsbereich im Test runden_sinnvoll (Zuschnitt eher runden_regel); weiter vertretbar.

---

## Schwierigkeit der Tests (je eine Zeile: Würde ein gutes Kind der Klassenstufe das in 2–3 Minuten lösen? Was muss es verstanden haben?)

| Test | Kl. | 2–3 Min? | was verstanden sein muss |
|---|---|---|---|
| 085 | 5 | ja, knapp | 1 000-mal so viel = drei Stellen weiter links; große Ziffern nach vorn, Vieren so weit rechts wie möglich |
| 090 | 5 | ja | „tausend“ fällt nur weg, wenn die Tausenderklasse 000 ist; Bereich 1 000 001 … 1 000 999 ohne Randfehler zählen |
| 095 | 5 | ja, leicht (1–2 Min) | nur Wert je cm bestimmen und anwenden, also ein Verfahren (A1) |
| 100 | 5 | ja | Rundungsbereiche für Zehner und Hunderter; Hürde: Ergebnis 0 (B3) |
| 105 | 5 | ja | „rund 30 m“ heißt 25 bis 34 m; Division mit Rest, Rest fällt weg |
| 110 | 5 | **nur sehr starke Kinder** | zwei Regelwerke lesen; Ersparnis nur bei 4 und 9 je Stufe; beides kombinieren (B1) |
| 115 | 5 | **nur sehr starke Kinder** (eher 5 Min) | Mias Lesart = rückwärts lesen, also Spiegelzahl; alle bis 5 Ziffern aufzählen (B2) |
| 029 | 7 | ja | Umfang als Term, zusammenfassen, für jedes positive x gleich → Zahlglieder gleich |
| 034 | 7 | ja | die beschriebene falsche Regel verstehen; Unterschied liegt nur im letzten Glied: +a gegen −a = 2a |
| 039 | 7 | ja (für gute Kinder) | x = 0 liefert b, x = 1 liefert a + b; warum hier zwei Einsetzungen genügen |

---

## Tabelle je Lernziel

| Lernziel | Schema | Denkfiguren | Test ok? | Maßstab erfüllt? | was fehlt |
|---|---|---|---|---|---|
| stellenwert | 087 | 5 | ja (085) | **ja** | – |
| ziffern_zu_zahlwort | 092 | 5 (090/091 verwandt) | ja (090) | **ja** | B11 (090 ↔ #100) beachten |
| strahl_eintragen | 095 (Test), 097, Zweifel 098 | 4 | **nein** (Schema, nicht die schwerste) | nein | A1: neuer Test, 097 ersetzen |
| runden_regel | 102 | 5 | ja (100) | **ja** | B3, B5, B6 |
| runden_sinnvoll | 108, 106 | 5 | ja (105) | nein | A2: 108 ersetzen |
| roemisch_schreiben | 111, 113 | 5 | ja (110), B1 | nein | A3: 113 ohne Anleitung |
| dualsystem | 116 | 5 | ja (115), B2 | nein (Bestandskern 118) | A4: 118 ersetzen |
| zusammenfassen | 030, 031 | 5 | ja (029) | nein | A5: 031 ersetzen |
| minusklammer | 035, 038 | 5 | ja (034) | nein | A6: 038 ersetzen |
| aequivalenz | 043, 042 | 5 | ja (039) | nein (dazu Bestandskern 040) | A7: 042 umbauen, A8: 040 ersetzen |

**Entscheidungen zu den Angriffspunkten des Schreibers:**
- Test 095 ist ein **Verfahren**, also Schema und nicht die anspruchsvollste Aufgabe (A1).
- Tests 029/039: **keine Doppelung** der Denkfigur (B10).
- 039: lösbar in Klasse 7; Auswahl als Test ist zulässig.
- 086/117 und 093/115: **gleiche Denkfigur**, B8.
- Schema-nah:
  - 036: **kein Schema** (Modellwahl im Sachkontext).
  - 042: **Schema** (A7).
  - 097: **Schema** (A1).
  - 118: **kein Schema**, aber Bestandskern (A4).
  - 114: **kein Schema** (welche Ziffern lange Schreibweisen erzeugen).
  - 106: **Schema** (A2).
- Sammel-Möglichkeiten: in der Summe ausgeglichen, in 103 und 116 ein Hinweis (B5).
- Länge 104: B6.
- Bestandsnähe:
  - 040 ist Bestandskern (A8).
  - 094 und 092 sind nah, aber zulässig (B11).
  - 118 ist Bestandskern (A4).

---

## Protokoll je Aufgabe

Spalten: Kennung · Pool · Lösung (eigen = JSON) · Klasse (S = Schema, Z = Zweifel, V = Verstehen) · Denkfigur · Bestand nach dem Kern · Befund.

### zahlen.natuerlich
| Kennung | Pool | Lösung | Kl. | Denkfigur | Bestand | Befund |
|---|---|---|---|---|---|---|
| 085 | test | 984 764 ✓ (alle 6-stelligen geprüft) | V | Wertverhältnis → Stellenabstand, größte Zahl | #10/#22 andere | – |
| 086 | korr | Option 1 ✓ (Differenz immer 4) | V | Tausch: nur Ziffernunterschied zählt | #10 vorwärts | B8, B11, B4 |
| 087 | korr | [2, 60 000] ✓ | S | Stelle ↔ Stellenwert (Fehler-Detektiv) | – | die eine Schema-Aufgabe |
| 088 | sich | Option 3 ✓ | V | beide Nullen als Platzhalter | #21 andere | – |
| 089 | sich | [39, 9 300] ✓ (alle Verteilungen) | V | Plättchen nach Stellenwert verteilen | – | – |
| 090 | test | 999 ✓ | V | leere Klasse wird nicht gesprochen | #100 nah | B11, C1 |
| 091 | korr | Option 2 ✓ | V | nicht gesprochene Klassen behalten Stellen | zahlwort_zu_ziffern #50 (andere Etappe) | B4, C1 |
| 092 | korr | Option 0 ✓ | S | Klasse falsch zugeordnet (Fehler-Detektiv) | S3-V002/R5-V006 nah | die eine Schema-Aufgabe |
| 093 | sich | 900 000 ✓ (1 000 … 999 999 geprüft) | V | Gruppierung von rechts | K5A-V008/#75 andere | B8 |
| 094 | sich | [3, 100 100 100] ✓ | V | „hundert“ höchstens einmal je Klasse | #85/#95 nah | B11 |
| 095 | test | [11, 3 000] ✓ | **S** | Maßstab aus zwei Marken | K5A-V013, #154/#164 (Verfahren) | **A1** |
| 096 | korr | Option 1 ✓ | V | Doppeltes bei verschobenem Anfang | – | B4 |
| 097 | korr | Option 2 ✓ (12 cm gegen 3 cm) | **S** | zwei Maßstäbe, gleiche Einzelfrage wie Test | – | **A1**, B4 |
| 098 | sich | 1 ✓ | Z | zwei Teilungen, gemeinsame Striche | – | – |
| 099 | sich | Option 0 ✓ | V | gleiche Strecke = gleicher Unterschied | – | B4 |
| 100 | test | 10 ✓ | V | zwei Rundungen über einen Bereich | #253 andere | B3, B9 |
| 101 | korr | 50 ✓ | V | größte Rundungsabweichung | #313/#324 andere Etappe | – |
| 102 | korr | [2, 4 900] ✓ | S | Rundungsrichtung (Fehler-Detektiv) | #249/R5-V014 anderer Fehler | die eine Schema-Aufgabe |
| 103 | sich | Option 1 ✓ | V | größer/kleiner/gleich mit Gegenbeispielen | #250 andere | B5 |
| 104 | sich | Option 3 ✓ (Monotonie geprüft) | V | Reihenfolge bleibt erhalten | – | B6 |
| 105 | test | [8, 11] ✓ | V | Rundungsbereich + Rest | #321 andere | C6 |
| 106 | korr | [27, 28] ✓ | **S** | Division mit Rest sachgerecht deuten | K5A-V027, R5-V017 | **A2** |
| 107 | korr | Option 2 ✓ | V | Rundungsstelle = Genauigkeit | – | – |
| 108 | sich | [108, 48] ✓ | **S** | Schätzfehler beim Produkt | K5A-V025 nah | **A2** |
| 109 | sich | Option 0 ✓ (Summe 13 790, Fehler 1 790) | V | gleichgerichtete Rundungsfehler | S3-V005 nah | B7, B11 |
| 110 | test | [49, 5] ✓ eindeutig | V | Ersparnis der Subtraktionsregel je Stufe | roemisch_system #409/#425 andere | B1, B9 |
| 111 | korr | Option 3 (VC) ✓ | S | Regelverstoß erkennen | #390/#393 nah | die eine erlaubte Schema-Aufgabe |
| 112 | korr | Option 1 ✓ | V | mehr Zeichen ≠ größer | roemisch_system #424/#429 | B12, C4 |
| 113 | sich | 3 999 ✓ | **S** | Systemgrenze (Anleitung im Text) | – | **A3** |
| 114 | sich | 28 ✓ | V | kleinste Zahl mit 6 Zeichen | #383/#391 andere | – |
| 115 | test | 10 ✓ | V | falsche Leserichtung → Spiegelzahlen | #447 andere | B2, B8, B9 |
| 116 | korr | Option 0 ✓ | S | führende Null | – | die eine Schema-Aufgabe |
| 117 | korr | 63 ✓ (alle 7-stelligen) | V | Tausch erste/letzte Stelle | K5A-V037 andere | B8, C5 |
| 118 | sich | Option 1 ✓ | V | Endung 00 → durch 4 teilbar | **#437 Kern** | **A4**, B4 |
| 119 | sich | [3, 4] ✓ | V | Stellenzahl in beiden Systemen | #449/#438 andere | – |

### terme.umformen
| Kennung | Pool | Lösung | Kl. | Denkfigur | Bestand | Befund |
|---|---|---|---|---|---|---|
| 029 | test | 4 ✓ (x > 0, alle Seiten positiv) | V | Umfänge gleichsetzen, Zahlglieder vergleichen | K8-V002/R8-V002 andere | B10 |
| 030 | korr | Option 2 ✓ | S | Vorzeichenfehler beim y-Glied (Fehler-Detektiv) | R15-V034 anderer Fehler | Schema |
| 031 | korr | Option 0 ✓ (nur x = 1) | **S** | falsche Zusammenfassung an Testwerten prüfen | #6/#27 nah | **A5**, B11 |
| 032 | sich | 6 ✓ | V | x-Glieder heben sich auf | #26 andere | – |
| 033 | sich | 1 ✓ (für alle a, b) | V | Koeffizient als Änderung je Schritt | – | – |
| 034 | test | 9 ✓ eindeutig | V | Wirkung einer falschen Klammerregel, rückwärts | #96 andere Denkleistung | B10 |
| 035 | korr | [2, 7, −4] ✓ | S | Plus- gegen Minusklammer (Fehler-Detektiv) | K8-V009/R15-V040 andere | Schema |
| 036 | korr | Option 1 ✓ | V | Minusklammer im Sachkontext wählen | #89 nah | B11 |
| 037 | sich | [1, 49] ✓ | V | Muster geschachtelter Minusklammern | #69 andere | – |
| 038 | sich | Option 2 ✓ | **S** | −(x − 7) = 7 − x durch Auflösen | #93 nah | **A6**, B11 |
| 039 | test | Option 0 ✓ | V | zwei Stellen legen a · x + b fest | #213/R15-V045 Gegenregel | C2, B4 |
| 040 | korr | [2, 31] ✓ | V | Zählterme eines Musters prüfen | **#237 Kern**, R8-V009 | **A8** |
| 041 | korr | 20 ✓ | V | Zahlenrätsel rückwärts, Ergebnis konstant | – | – |
| 042 | sich | 0 ✓ | **S** | vereinfachen, Zahlglied vergleichen | #209 umgekehrt | **A7**, B10, C3 |
| 043 | sich | 4 ✓ | S | Gruppen gleichwertiger Terme | #211 nah | Schema |

## Zahlen
- A (Muss): **8** (A1–A8). Sicher: A1, A4, A7, A8. Aus der Zweifelsregel: A2, A3, A5, A6.
- B (Soll): **12**. C (Kann): **6**.
- Erfüllen den Maßstab: stellenwert, ziffern_zu_zahlwort, runden_regel. Die übrigen sieben brauchen je einen gezielten Ersatz bzw. Umbau (strahl_eintragen zwei: Test und 097).
