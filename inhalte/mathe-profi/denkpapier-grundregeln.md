# Denkpapier: Grundregeln – von der Zahl zum Ausdruck

Mathe-Profi, 25.11.2026. Kein Bau. Stand `lernen-app` dc9673c. **[G]** gesichert (im Repo gezählt, gerechnet, gelesen; Forschung mit Quelle) · **[A]** Annahme · **[M]** Meinung. Zahlen: `grundregeln_probe.py` (nur Inhalte, keine Lerndaten).
**Vorbehalt:** Der Text von Denkauftrag 2 (Fragen 1–7) hat mich nicht erreicht. Grundlage sind die Ergänzung (Fragen 8–10) und der Protokoll-Eintrag „Grundregeln schweben über den Themen“ in `inhalte/AUFTRAEGE.md`. Abschnitt 1 beantwortet dessen offene Punkte.

## Kern

1. Die Sicht stimmt zur Hälfte: Die Regeln sind dieselben. Der Schritt liegt aber **nicht** beim Buchstaben, sondern an drei anderen Stellen (Abschnitt 2). [G/M]
2. Die Brücke heißt **„Zahl, aber nicht ausrechnen“**: dieselbe Regel an Zahlen, bei denen Ausrechnen sich nicht lohnt. Die fehlt im Bestand fast ganz, in Klasse 6 völlig. [G]
3. Jede Grundregel braucht ihre **Grenze** („gilt nicht bei …“). Regeln als Merksatz ohne Grenze erzeugen genau die Fehler, die wir heilen wollen. [M]
4. „Älteres Kind erklärt“ taugt als freiwilliges, kleines Angebot mit Gegenrolle für das jüngere – nicht als fester Baustein. [M]

## 1. Trägt die Idee „Grundregeln über den Themen“?

**Ja, für Zahlen, Terme, Gleichungen, Prozent, Funktionen.** [M] In Geometrie und Daten sind es wiederkehrende Ideen (zerlegen, Verhältnis, Symmetrie), keine Rechenregeln; bei Sachaufgaben und Begründen hilft die Achse kaum.

**Der Bestand zeigt die Wiederkehr – und die Lücke** [G, grobe Textzählung, Gymnasium Bayern]:

| Im Aufgabentext | Kl. 5 | Kl. 6 | Kl. 7 | Kl. 8 |
|---|---|---|---|---|
| Minus vor negativer Zahl, a − (−b) | 25 | 2 | 0 | 3 |
| Minus vor Klammer, a − (b ± c) | 8 | 0 | 39 | 8 |
| … davon mit Buchstabe | 0 | 0 | 38 | 8 |
| Faktor vor Klammer, a · (b ± c) | 14 | 0 | 128 | 81 |
| … davon mit Buchstabe | 2 | 0 | 126 | 81 |
| Gleichung, x kommt einmal vor | 99 | 0 | 46 | 263 |
| Gleichung, x kommt mehrfach vor | (14)* | 0 | 116 | 129 |

*Probe-Aufgaben, in denen „x = 9“ zusätzlich im Satz steht; in der Gleichung selbst steht x einmal.
Lesart: Die Klammerregeln werden in Klasse 5 an Zahlen kaum geübt (8 und 14 Aufgaben von 4 121), in Klasse 6 gar nicht, und stehen in Klasse 7 plötzlich mit Buchstaben da. Beide Beispiele des Nutzers stehen im Bestand.

**Wie einbauen** [M]: Regel-Etikett am **Aufgabenmuster** im Generator, nicht an 30 000 Einzelaufgaben. Jedes Fehlbild (siehe `denkpapier-diagnose.md`) zeigt auf eine Regel und über sie auf die Etappe, in der sie mit Zahlen geübt wird. Stand je Regel und Kind lässt sich aus dem vorhandenen „sitzt“ je Etappe ableiten.
**Sichtbar für die Kinder?** [M] Ja, sparsam: als Name in der Erklärung und nach einem Fehler („Werkzeug: Minus vor der Klammer“). An der Aufgabe selbst erst sichtbar, dann als Frage („Welches Werkzeug brauchst du?“), dann weg. In der Schulaufgabe steht kein Etikett; **erkennen, welche Regel dran ist, ist die eigentliche Leistung**.

## 2. Frage 8: Wo liegt der Schritt von der Zahl zum Ausdruck?

**Nicht beim Zeichen.** Klasse 5 rechnet im Flug „Einfache Gleichungen“ schon mit x [G]. Kästchen oder Buchstabe ist für das Kind derselbe Platzhalter, solange er einmal vorkommt. Der Schritt hat drei Teile:

| | Klasse 5 | Klasse 8 | Folge |
|---|---|---|---|
| **A. Abschluss** | Am Ende steht eine Zahl. | 2x + 2 bleibt stehen. | Kinder erzwingen ein „Ergebnis“: 2x + 2 → 4x. Ein Ausdruck ist für sie eine unerledigte Rechnung, kein Ding. [A] |
| **B. Unbekannte mehrfach** | 4 · (□ − 12) = −20: rückwärts rechnen (−20 : 4, dann + 12). | 5x − (3x − 2) = 12: Rückwärts geht nicht. Man muss **mit** der Unbekannten rechnen. | Hier liegt der in der Forschung beschriebene Bruch zwischen Rechnen und Algebra. [G, Quelle 1] |
| **C. Gleichheitszeichen** | „ergibt“ | „ist gleich viel wert wie“ | Wer „=“ als „ergibt“ liest, löst Gleichungen schlechter. [G, Quelle 2] |

Dazu **D. Kontrolle:** Die Zahl kann man nachrechnen, den Ausdruck nicht. Ersatz ist die Zahlenprobe – sie muss gelernt werden wie eine Regel.

**Zur Einschätzung des Projektleiters** [M]: „Klasse 5 ist das Fundament“ – ja. „Sitzen vor Tempo“ – ja in der Reihenfolge; die vier, fünf meistgebrauchten Regeln müssen am Ende aber auch flüssig sein, sonst fehlt in Klasse 8 der Kopf für die Struktur. „Fehler von Kind 2 als Vorschau“ – als Hinweisliste brauchbar, mehr nicht: ein Kind, eine Lerngeschichte. „Zurück zur Zahl hilft“ – ja, aber nur zur **unausgerechneten** Zahl. Wer 20 − (8 − 3) sofort zu 15 macht, sieht die Regel nicht.
**Korrektur am Beispielpaar** [G]: 9 − (−5) ist das Fundament für das Vorzeichen (−(−2) = +2). Das Fundament für die **Minusklammer** ist ein anderes: eine Differenz abziehen, 20 − (8 − 3) = 20 − 8 + 3. Genau das fehlt.

**Eine Regel durchgehend: „Minus vor der Klammer“** [G gerechnet, Stufung M]

| Stufe | Wo | Was das Kind tut | Beispiel |
|---|---|---|---|
| 1 | Kl. 5 | rechnen und vergleichen | 20 − (8 − 3) = 15; 20 − 8 − 3 = 9; 20 − 8 + 3 = 15. „3 € Rabatt: du zahlst weniger als 8.“ |
| 2 | Kl. 5 | dieselbe Idee mit negativer Zahl | 9 − (−5) = 14: Schulden abziehen. |
| 3 | Kl. 5–6 | **nicht ausrechnen**, Struktur sehen | 78 − (49 − 22) = 78 − 49 + □. Welche Terme sind gleich viel wert? In Kl. 6 mit Dezimalzahlen: 3,5 − (1,2 − 0,7). |
| 4 | Kl. 6–7 | gedachte Zahl kommt zweimal vor; Tabelle | 5 · □ − (3 · □ − 2) für □ = 1, 2, 3 ergibt 4, 6, 8. Welche Kurzform passt: 2 · □ + 2 oder 2 · □ − 2? |
| 5 | Kl. 7 | Buchstabe, mit Zahlenprobe | 5x − (3x − 2) = 2x + 2. Probe x = 3: 8 = 8. Das Fehlbild 2x − 2 gäbe 4. |
| 6 | Kl. 8 | die Regel steckt in etwas Größerem | 5x − (3x − 2) = 12 → x = 5; Differenz zweier Funktionsterme; Zähler eines Bruchterms. |

Regeln zur Brücke: (a) Jeder neue Flug beginnt eine Stufe **unter** seinem Niveau („Das kennst du schon“). (b) Hängt das Kind in 5 oder 6, geht es eine Stufe zurück – nach 4 oder 3, nicht nach 1. (c) Zahlenprobe mit 2 oder 3, nie mit 0 oder 1: x = 0 übersieht 8x + 2, x = 1 übersieht x² statt x [G]. (d) Eine Probe widerlegt, sie beweist nicht.
Stufe 3 passt zu den Mustern M2 und M3 aus `auftrag3.md` und braucht keinen Bau.

## 3. Frage 9: Welche Grundregeln müssen sitzen – und woran erkennt man es?

Liste für Klasse 5 und 6 [M; Zuordnung zu Klassen nach dem Bestand, nicht gegen den Lehrplan geprüft]:

| # | Regel in Kinderworten | fest in | Klasse 8 baut darauf | Grenze (hier gilt sie nicht) |
|---|---|---|---|---|
| 1 | Plus und Minus mit negativen Zahlen: Richtung auf der Zahlengeraden | 5 | alles | – |
| 2 | Minus vor der Klammer dreht jedes Zeichen darin | 5 | Terme, Gleichungen, Bruchterme | Plus vor der Klammer dreht nichts |
| 3 | Mal und geteilt: gleiche Zeichen plus, verschiedene minus | 5 | Terme, Potenzen | **nicht beim Addieren**: (−5) + (−3) ist nicht 8 |
| 4 | Klammer, dann Punkt, dann Strich; die letzte Rechnung gibt dem Term den Namen | 5 | Struktur sehen, Kürzen | – |
| 5 | Verteilen: jeder in der Klammer wird malgenommen; rückwärts ausklammern | 5 | Ausmultiplizieren, Binome | nicht beim Quadrat: (a + b)² ≠ a² + b² |
| 6 | Tauschen und Verbinden | 5 | Zusammenfassen | nur bei plus und mal |
| 7 | Gleich heißt gleich viel; auf beiden Seiten dasselbe tun | 5 | Gleichungen, Formeln | nicht nur auf einer Seite; nicht durch 0 |
| 8 | Einsetzen und Probe | 5 | Selbstkontrolle überall | eine Probe beweist nichts |
| 9 | Erweitern und Kürzen ändern den Wert nicht | 6 | Bruchterme | nur Faktoren kürzen, nie aus Summen |
| 10 | Brüche rechnen: gleicher Nenner bei ±, Kehrwert beim Teilen | 6 | Bruchterme, Bruchgleichungen | Nenner nicht addieren |
| 11 | Potenz ist wiederholtes Malnehmen | 5–6 | Potenzgesetze | a² ist nicht 2a |
| 12 | Komma und Stellenwert; Bruch, Dezimalzahl, Prozent sind dieselbe Zahl | 6 | Prozent, Funktionen | – |
| 13 | Verhältnis: „je“ und Dreisatz | 5–6 | lineare Funktion, Steigung | nicht mit Grundgebühr |

Die Spalte „Grenze“ ist der wichtigste Teil. Der bekannte Fehler „Minus und Minus gibt Plus“ beim Addieren ist Regel 3 am falschen Ort [A]. Jede Regel also als Dreiklang: Satz, Zahlenbeispiel, Gegenfall.

**„Fest genug“** [M] – alle sechs, nicht eines:
1. richtig im ersten Versuch, ohne Tipp;
2. **gemischt**: zwischen anderen Regeln, ohne Etikett;
3. **verteilt**: an mindestens drei Tagen über drei Wochen, einmal davon nach zwei Wochen Pause;
4. **Brückenform**: richtig in der Fassung „nicht ausrechnen“ (Stufe 3) und rückwärts;
5. **ohne Regel-Fehlbild** in den letzten sechs Trennaufgaben;
6. **auf Papier** in einer Papier-Runde; für die Regeln 1–5 zusätzlich flüssig (braucht die Antwortzeit, die noch nicht gespeichert wird [G]).

„Fest“ ist kein Abzeichen für immer: Ein Regel-Fehlbild in einem späteren Flug setzt die Regel auf „wackelt“ zurück. Die App führt je Etappe schon „sitzt“ mit Wiederholungsstufen [G]; neu wären das Etikett je Muster und die Punkte 2, 4, 5.

## 4. Frage 10: Das ältere Kind erklärt dem jüngeren

**Was die Forschung sagt** [G, Quelle 3]: Erklären nützt dem Erklärenden, im Mittel aber wenig – weil Erklärende meist nur wiedergeben, was sie wissen, statt neu zu durchdenken. Gewinn entsteht, wenn sie Beispiele selbst bauen und auf Rückfragen antworten müssen.
**Urteil** [M]: als fester Baustein nein, als freiwilliges Angebot ja. Gründe gegen „fest“: Geschwister sind keine Lerngruppe; Pflicht macht aus Hilfe Last; das jüngere Kind erlebt sich als das schwächere; falsche Erklärungen wandern weiter; zwei Kinder liefern keinen Beleg, ob es wirkt.

**So könnte es aussehen**
- **Erklär-Karte.** Das ältere Kind baut für eine Regel, die bei ihm fest ist, eine Karte an Zahlen: Beispiel wählen, drei Schritte füllen, einen typischen Fehler warnen. Die App prüft die Rechnung, der Erwachsene gibt frei, das jüngere Kind sieht die Karte bei dieser Regel als Tipp. Nutzen für das ältere: Es geht selbst zurück zur Zahl – genau Stufe 1 bis 3.
- **Gegenrolle: Zahlenprüfer.** Das jüngere Kind bekommt gelegentlich eine Umformung des älteren Stoffs als Zahlenaufgabe: „Stimmt das für 3? 5 · 3 − (3 · 3 − 2) und 2 · 3 + 2“. Es prüft, das ältere braucht die Prüfung. So hat jedes eine Rolle, die das andere nicht hat.
- **Am Tisch.** Die App meldet dem Erwachsenen nur den passenden Moment: Regel bei einem Kind fest, beim anderen gerade begonnen. Das Gespräch selbst gehört der Familie.

**Damit es keine Last wird:** freiwillig; höchstens einmal je Woche, fünf Minuten; nie ausgelöst durch einen Fehler des jüngeren Kindes; kein Kind sieht Stand oder Fehler des anderen; nur Regeln, die beim älteren fest sind; keine Punkte, die fehlen, wenn man ablehnt; zweimal abgelehnt heißt Pause. Vier Wochen ausprobieren, dann entscheiden die Kinder mit.

## 5. Vorsicht

- „Es ist immer dasselbe“ tröstet, stimmt aber nur für die Regel, nicht für die Schwierigkeit: Dieselbe Regel in neuer Verkleidung zu erkennen **ist** das Schwere. [M]
- Die Zählung in Abschnitt 1 liest nur den Aufgabentext; Regeln, die im Rechenweg stecken, erfasst sie nicht. [G]
- **Nicht geprüft:** LehrplanPLUS je Regel; Vollständigkeit der Liste; ob Klasse 6 die Klammerregeln im Schulbuch an Brüchen übt.

**Quellen:** (1) Filloy & Rojano 1989, Solving Equations: the Transition from Arithmetic to Algebra, https://flm-journal.org/Articles/3DA2C5DE336DFD448BCF339B51168E.pdf · (2) Knuth, Stephens, McNeil & Alibali 2006, Does Understanding the Equal Sign Matter?, https://jwilson.coe.uga.edu/EMAT7050/articles/KnuthAndOthers.pdf · (3) Roscoe & Chi 2007, Understanding Tutor Learning, https://education.asu.edu/sites/default/files/lcl/rod_chi_rer_07_3.pdf
