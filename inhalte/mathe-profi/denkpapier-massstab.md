# Denkpapier: Maßstab – und wie die App insgesamt besser wird

Mathe-Profi, 25.11.2026. Kein Bau. Stand `lernen-app` dc9673c. Antwort auf Denkauftrag 3 (Fragen 1–8) und die Ergänzung (Fragen 9–14).
**[G]** gesichert (selbst gelesen, gezählt, gerechnet; Forschung mit Quelle) · **[A]** Annahme · **[M]** Meinung · **[H]** Angabe der Helfer, von mir nicht geprüft. Zahlen: `massstab_probe.py` (nur Inhalte, keine Lerndaten).
**Stand:** Hauptteil vor Eingang der Recherche-Berichte geschrieben; der **Nachtrag** am Ende arbeitet sie ein und berichtigt zwei Aussagen (Erfolgsquote „Übertragen“, erst knobeln).

## Kern

1. Die Zuordnung der Helfer stimmt in der Größenordnung. Genauer: 32 % der Bewertungseinheiten gehen allein mit den 15 Regeln, weitere 10 % mit Regel plus Geometrie-Formel. Das ergibt Note 4, in zwei von drei Jahrgängen ohne die Formeln Note 5. [G]
2. Der Sprung auf Note 2 bis 3 kommt vom **Übertragen und Umkehren** (19 %, landesweit 2025 nur 16 % richtig). Die Note 1 bis 2 hängt am **Begründen** (24 %, davon 9 von 15 Einheiten in Geometrie). [G]
3. Die App ist im Kleinen gut gebaut – Aufgaben, Stufen, Regel für „gelandet“. Was fehlt, ist das, was der Test prüft und die App nicht verlangt: aufschreiben, übertragen, begründen, zeichnen. [G/M]
4. Für vier Wochen: wöchentliche Papier-Runde, tägliche gemischte Fünf mit Umkehraufgaben, Heft mit Stichprobe. Alles ohne oder mit sehr kleinem Bau. [M]

## 1. Eigene Zuordnung der drei Tests (Frage 1)

Gruppe A der Jahrgänge 2023–2025, 48 Teilaufgaben, 63 Bewertungseinheiten (BE). Quelle: Aufgabenblätter des Staatsinstituts, gegengelesen mit dem Katalog im Repo – Nummern und BE stimmen überein [G]. Ich trenne **Tätigkeit** und **Inhalt**; die Helfer haben beides auf einer Achse gemischt.

| Tätigkeit | BE | Anteil | richtig 2025 | Helfer |
|---|---|---|---|---|
| Rechnen nach Regel, nur die 15 Regeln | 20 | 32 % | zusammen 49 % | 35 % |
| Rechnen nach Regel plus Geometrie-Formel (Volumen, Dreieck, Parallelogramm) | 6 | 10 % | | in „Geometrie“ |
| Übertragen, Umkehren, Term aufstellen | 12 | 19 % | **16 %** | 16 % |
| Begründen, Erläutern, Gegenbeispiel | 15 | 24 % | 42 % | 19 % |
| Zeichnen, Konstruieren, im Bild sehen | 4 | 6 % | 74 % | 14 % mit Geometrie |
| Ablesen, Datenbegriff | 4 | 6 % | – | 11 % |
| Deuten, Schätzen | 2 | 3 % | – | 5 % |

| Inhalt | Zahlen/Algebra | Geometrie/Raum | Prozent, Verhältnis, Größen | Daten |
|---|---|---|---|---|
| BE | 23 (37 %) | 21 (33 %) | 11 (17 %) | 8 (13 %) |

**Was ein Kind erreicht, das genau das kann und sonst nichts** [G, Notenschlüssel 16/13/10/7/4]:

| Kann | BE 2023 / 2024 / 2025 | Note |
|---|---|---|
| nur die 15 Regeln | 6 / 8 / 6 | 5 / 4 / 5 |
| + Geometrie-Formeln | 9 / 8 / 9 | 4 / 4 / 4 |
| + Übertragen und Umkehren | 13 / 12 / 13 | 2 / 3 / 2 |
| + Ablesen, Zeichnen, Deuten | 18 / 16 / 14 | 1 / 1 / 2 |

**Wo ich abweiche**
- „49 % außerhalb der Regeln“ ist überdehnt. 10 % sind Regel plus eine von etwa zwölf Formeln; das ist ein kleiner Formel-Koffer, kein neuer Strang.
- Begründen ist größer als angegeben (24 statt 19 %), weil Begründungen in Geometrie mitzählen. Geometrie ist dafür als eigene Tätigkeit kleiner (6 %), als Inhalt aber ein Drittel des Tests.
- „Regeln bringen Note 4“ gilt nur mit den Formeln und nur bei fehlerfreiem Rechnen. Selbst ein einfacher Termwert wurde 2025 landesweit nur zu 28 % richtig gelöst, die Regel-Aufgaben insgesamt zu 49 %. Regeln **sicher** zu können ist schon mehr, als der Landesschnitt kann (8,71 BE, Note 3,75). [G]
- Tabellenkalkulation: in zwei meiner drei Jahrgänge, je 1 BE. Beide Aufgaben sind im Kern die Regel Rangfolge in anderem Gewand.

Nicht geprüft: Arbeitszeit, Hilfsmittel, Anteil Ankreuzen [H]. Die Erfolgsquoten 2025 sind aus dem Diagramm des Berichts gelesen; die Summe stimmt mit dem Bericht überein (41,5 %).

## 2. Was folgt für die Liste? (Frage 2)

Die 15 Regeln bleiben. Dazu sechs **Stränge** quer zu den Flügen [M]:

| Strang | In der App, vorhandene Formen | Auf Papier |
|---|---|---|
| **Formel-Koffer** (rund zwölf Formeln Klasse 5–8, jede mit Bild) | Zahl; Umkehrung („Höhe aus Volumen“) | Formel hinschreiben, einsetzen, Einheit |
| **Übertragen/Umkehren** | Zahl und Lücken mit eindeutiger Umkehrung gehen heute; offene brauchen eine Bedingungs-Prüfung (Abschnitt 3) | „Gib an, sodass …“ mit kurzer Probe |
| **Begründen** | Gegenbeispiel, immer/manchmal/nie mit Beleg, Lücke in der Begründung (Abschnitt 4) | zwei bis drei Sätze, Abgleich mit Bausteinen |
| **Zeichnen/Konstruieren** | `punkte` (Auftrag 2) für Gitter; Zirkel-Konstruktion nicht | Geodreieck und Zirkel, Foto als Stichprobe |
| **Daten lesen** | Zahl und Mehrfach-Antippen („drei Aussagen: stimmt/stimmt nicht“); Formel einer Tabellenkalkulation als Term-Lücke | Diagramm ergänzen, Median begründen |
| **Sachansatz/Deuten** | Auswahl „Welcher Term passt?“, Lücke „x steht für …“ | gegeben – gesucht – Ansatz – Antwortsatz mit Teilpunkten |

Tabellenkalkulation wird kein eigener Strang: Zellbezug lesen ist „Einsetzen“, die Formel ist „Rangfolge“.

## 3. Offene Umkehraufgaben (Frage 3)

**Prüfregel** [G, Referenz `pruefe` im Skript]: Die Lösung ist keine Zahl, sondern eine Liste von **Bedingungen**. Der Server liest die Antwort exakt (ganze Zahl oder Dezimalzahl mit höchstens drei Stellen, Betrag bis eine Million), prüft die Bedingungen der Reihe nach und meldet die erste verletzte als Hinweis („Die Summe stimmt, aber keine Zahl ist positiv“). Unsinn zählt nie als Fehler. Das ist ein kleiner Bau am Server; die Eingabe geht mit `zahl` und `luecken`. Ohne Bau gehen heute nur Umkehrungen mit genau einer Lösung (K8-1).

| | Muster (eigene Beispiele) | Bedingungen |
|---|---|---|
| K5-1 | Nenne eine ganze Zahl, die man von 7 abziehen kann, sodass mehr als 7 herauskommt. | 7 − x > 7 |
| K5-2 | Nenne zwei verschiedene ganze Zahlen mit Summe −5, eine davon positiv. | a + b = −5; eine > 0; a ≠ b |
| K5-3 | Setze für □ ein, sodass 3 · (□ − 4) kleiner als −6 ist. | 3 · (x − 4) < −6 |
| K5-4 | Länge und Breite (ganze cm) eines Rechtecks mit Umfang 20 cm und mehr als 20 cm² Fläche. | beide > 0; 2(l + b) = 20; l · b > 20 |
| K5-5 | Nenne eine Zahl, die durch 2 und 3 teilbar ist, aber nicht durch 12. | n > 0; 6 teilt n; 12 teilt n nicht |
| K8-1 | Durch welche Zahl muss man die 12 in 5x − (3x − 2) = 12 ersetzen, damit x = 4 die Lösung ist? | Einsetzen von 4 ergibt die Zahl (eindeutig: 10) |
| K8-2 | Gib m und t so an, dass y = m · x + t fällt und durch P(2 \| 3) geht. | 2m + t = 3; m < 0 |
| K8-3 | Gib a so an, dass die Lösung von a · x + 3 = 2x + 5 negativ ist. | a ≠ 2; 2 : (a − 2) < 0 |
| K8-4 | Nenne ein x, für das 1 : (x − 3) größer als 1 ist. | x ≠ 3; 1 : (x − 3) > 1 |
| K8-5 | A(0 \| 0), B(4 \| 0). Nenne einen Gitterpunkt C, sodass das Dreieck ABC die Fläche 6 hat. | ½ · 4 · \|y\| = 6 |

Getestet mit 45 Antworten und je 8 Unsinn-Eingaben [G]. Regeln für den Stapel [M]: Die Bedingung darf nie durch eine in der Aufgabe genannte Zahl erfüllt sein; mindestens drei richtige Antworten, die verschieden aussehen; der Lösungsweg zeigt **eine** Antwort und sagt, welche anderen gehen.

## 4. Begründen ohne freie Textbewertung (Frage 4)

Geordnet danach, wie ehrlich die Form prüft [M]:

1. **Gegenbeispiel nennen.** „Jede durch 2 und 3 teilbare Zahl ist durch 12 teilbar.“ – Zahl eingeben, Server prüft. Ehrlich, weil nichts zum Wiedererkennen dasteht.
2. **Immer, manchmal, nie – mit Beleg.** Bei „manchmal“ ein Beispiel, bei dem es stimmt, und eines, bei dem nicht. Zwei geprüfte Eingaben.
3. **Lücke in der Begründung** mit Zahl oder Term, nicht mit Wort: „Die Radien MA und MC sind gleich lang, also sind die Winkel bei A und C gleich: je □°.“
4. **Fehlerzeile in einer Begründung** antippen.
5. **Argumente ordnen** – nur wenn jeder Schritt den vorigen braucht; sonst mehrere richtige Reihenfolgen.
6. **Auswahl „weil …“** (heute 864 von 938): schwächste Form, bleibt als Einstieg. Aufwerten durch Stufe 1 oder 2 als zweite Frage.
7. **Papier:** zwei Sätze schreiben, dann Abgleich mit Bausteinen („Steht bei dir: Radius gleich Radius? Also gleichschenklig?“). Je Baustein ein Punkt, Stichprobe durch den Erwachsenen.

Ehrlich gesagt: Einen geschriebenen Begründungssatz prüft nur ein Mensch. Die Formen 1–5 üben die Bausteine; 15 von 63 BE verlangen den Satz.

## 5. Aus dem Ausland übernehmen? (Frage 5)

| | Urteil [M] | Klasse 5 | Klasse 8 |
|---|---|---|---|
| **Balkenmodell** | Ja, für Verhältnis, Bruchteil, Prozent, Sachaufgaben bis Klasse 7 – als Bild in der Erklärung und als Aufgabe „Balken beschriften“. Nicht als Pflichtweg, wenn die Gleichung schneller ist. | Heft kostet 3-mal so viel wie ein Stift, zusammen 6 €: vier gleiche Teile, einer 1,50 €. | Nach 20 % Rabatt 60 €: fünf Teile, vier bleiben, einer 15 €, alt 75 €. |
| **Zwei Wege vergleichen** | Ja, als Baustein der Erklärung und als Aufgabe „Was unterscheidet die Wege?“. Passt zur Regel-Idee. [H: belegt] | 6 · 18 als 6 · 20 − 6 · 2 und als 6 · 10 + 6 · 8 | 3(x + 2) = 12: erst teilen oder erst ausmultiplizieren |
| **Erst knobeln, dann erklären** | Sparsam: eine Einstiegsfrage vor der Erklärung, ohne Wertung, höchstens zwei Minuten. Ohne Lehrer fehlt das Aufgreifen – die App muss danach zwei typische Versuche zeigen. | Welcher Garten ist größer, 3 m mal 8 m oder 5 m mal 5 m? | Zwei Tarife: Ab wann lohnt der teurere Grundpreis? |
| **Stichprobe nach Sparx-Art** | Ja, zusammen mit Kontrollzahlen: nach der Sitzung das Ergebnis einer früheren, richtig gelösten Aufgabe aus dem Heft nennen. Beweist, dass geschrieben wurde. | „Was hattest du bei Aufgabe 3?“ | dazu ein Zwischenergebnis |
| Freier KI-Chat als Tutor | Nein. In der Studie 17 % schlechter in der Prüfung ohne KI; der gesicherte Tutor brachte beim Üben +127 %, in der Prüfung nichts. [G, Quelle 2] | | |
| Anpassung der Schwierigkeit als Hauptsache | Nein, nicht zuerst. [H] | | |

## 6. Der Fehler-Katalog mit 114 Einträgen (Frage 6)

**Prüfung, bevor er Grundlage wird** [M]:
1. **Rechenbar:** Jeder Eintrag hat einen Fehlbild-Ausdruck und ein Beispiel, bei dem sein Ergebnis von der Lösung und von allen anderen Einträgen derselben Regel abweicht – per Programm.
2. **Eigene Erklärung:** Zwei Einträge, die dieselbe Erklärung bekämen, sind einer.
3. **Herkunft sichtbar:** belegt (35) oder vermutet (79). Vermutete bleiben Hypothese, bis sie in einer falschen Antwort oder am Tisch gesehen wurden.
4. **Genau eine Regel** oder „Bedeutung“; dazu Grenze und drei Trennaufgaben.
5. **Stichprobe** von 20 Einträgen durch den Mathe-Profi.

**Wie viele?** Drei bis fünf je Regel, dazu etwa zehn Bedeutungsfehler: 55 bis 85. Dünn besetzte Regeln (Probe, Nullprodukt) dürfen dünn bleiben – dort gibt es wenig zu verwechseln. 114 ist für zwei Kinder zu fein; die Zahl 2 800 eines Anbieters ist kein Ziel, sondern Zählweise.

## 7. Welche Befunde sind überdehnt? (Frage 7)

- **„Regeln allein = Note 4“** – siehe Abschnitt 1: mit Formeln ja, ohne eher 5, und nur fehlerfrei.
- **Indische Lernsoftware** – das untersuchte Angebot war ein Lernzentrum mit Software **und** Kleingruppen-Unterricht, 619 Kinder, viereinhalb Monate, viele Kinder mehrere Jahre hinter dem Klassenstoff [G, Quelle 3]. Als Beleg „Software allein schließt Lücken“ zu stark. Die Aussage zu den Schulprüfungen habe ich nicht nachgeprüft.
- **KI-Tutor** – richtig gelesen. Wichtiger als die 17 % ist der zweite Teil: Gute Leistung beim Üben mit Hilfe sagt nichts über die Prüfung ohne Hilfe. Das gilt genauso für unsere 80 und 89 % mit Tipp und zweitem Versuch. [G]
- **„Adaptiv nicht besser als statisch“** – eine Studie; gemessen wird meist die Anpassung der Schwierigkeit. Über Diagnose nach Fehlbild sagt das nichts. [A]
- **„Höhere Schwelle bringt wenig, Abstände zählen“** – plausibel, darf aber nicht heißen, dass die Schwelle egal ist: Sie muss Glück ausschließen. [M]
- **Singapur, Japan, China „stützen die Brücke“** – als Richtung ja. Es sind ganze Lehrgänge mit Lehrkraft; ein einzelnes Element herauszulösen belegt dort niemand. [A]
- **bettermarks, Mathegym, Math Academy, Sparx** – Angaben der Anbieter. Unabhängig belegt ist davon wenig. [H]
- **Fehler-Katalog** – zwei Drittel unbelegt; siehe Abschnitt 6.

## 8. Kleinste Fassung für vier Wochen (Frage 8)

| | Was | Bau | Messen |
|---|---|---|---|
| 1 | **Papier-Runde, einmal je Woche:** 20 Minuten, sechs Aufgaben aus dem Stoff der Woche (3 Regel, 1 Umkehr, 1 Begründen, 1 Geometrie oder Daten), kein Tipp. Erwachsener bewertet in 10 Minuten nach Schema. | keiner – Blatt und Schema liefert der Mathe-Profi | Punkte je Tätigkeit, Woche 1 gegen Woche 4; Abstand zur Quote in der App |
| 2 | **Tägliche Fünf:** fünf gemischte Aufgaben ohne Etikett am Anfang jeder Sitzung, darunter eine Umkehraufgabe und eine Brückenaufgabe. | klein, oder als eigener kurzer Flug nur mit Inhalt | Quote im ersten Versuch je Woche; Zahl der Regel-Fehlbilder |
| 3 | **Heft mit Stichprobe:** Rechenweg ins Heft; nach der Sitzung fragt der Erwachsene zwei Ergebnisse früherer Aufgaben ab. | keiner | Anteil bestandener Stichproben; Seiten je Woche |

Ehrlich: Zwei Kinder, vier Wochen – das sind Beobachtungen, keine Belege. Die Papier-Runde ist trotzdem die einzige Zahl, die am Maßstab gemessen ist.

## 9. Zwei Erklärungen, neu geschrieben (Frage 9)

Beide vorhandenen Erklärungen sind **ordentlich**: Einstieg, Regel, Schritte, typischer Fehler, Wörter, Bild [G]. Es fehlt, bei beiden gleich: (a) eine Frage **vor** der Erklärung, (b) der Gegensatz, an dem man den Fehler versteht, (c) ein zweites Beispiel in die andere Richtung, (d) eine Probe, (e) eine Mini-Aufgabe mit Lösung, bevor das Üben beginnt.

**Klasse 5 – Flächeneinheiten umrechnen** (`messen.flaechen`, Etappe `einheiten`)

- **Erst du:** Dein Zimmerboden ist 12 m² groß. Eine Fliese bedeckt 1 dm². Brauchst du eher 120 oder eher 1 200 Fliesen?
- **Bild:** Quadrat mit 1 m Seite, ausgelegt mit 10 Reihen zu je 10 kleinen Quadraten (vorhanden).
- **Schritt 1:** 1 m ist 10 dm lang. In das große Quadrat passen 10 Reihen mit je 10 kleinen: 100. Also 1 m² = 100 dm².
- **Schritt 2:** 12 m² sind 12 solche Quadrate: 12 · 100 = 1 200 dm².
- **Schritt 3, zurück:** 350 dm² sind 350 : 100 = 3,5 m².
- **Schritt 4, zwei Stufen:** 2 m² = 200 dm² = 20 000 cm².
- **Regel:** Eine Stufe kleiner: mal 100. Eine Stufe größer: durch 100.
- **Gegensatz:** Länge: 3 m = 30 dm, mal 10. Fläche: 3 m² = 300 dm², mal 100 – weil es in zwei Richtungen mal 10 geht.
- **Probe:** Kleinere Einheit, größere Zahl. Stimmt das bei deinem Ergebnis?
- **Typische Fehler:** 1 m² = 10 dm². Und: aus 350 dm² werden 35 m² – das Komma rückt zwei Stellen, nicht eine.
- **Jetzt du:** 5 dm² = □ cm². (500)

**Klasse 8 – Laplace-Wahrscheinlichkeit** (`stochastik.grundbegriffe`, Etappe `laplace`)

- **Erst du:** In der Trommel liegen 3 rote, 5 blaue und 2 grüne Kugeln. Du ziehst blind. Schreib eine Zahl von 0 bis 1 für „rot“ auf, bevor du weiterliest.
- **Schritt 1, prüfen:** Jede der 10 Kugeln wird gleich leicht gezogen. Gezählt werden **Kugeln**, nicht Farben.
- **Schritt 2:** Alle Ergebnisse: 10. Günstig für „rot“: 3.
- **Schritt 3:** P(rot) = 3/10 = 0,3 = 30 %.
- **Was die Zahl bedeutet:** Ziehst du sehr oft und legst zurück, ist etwa 30-mal von 100 eine rote dabei. Nicht genau, aber ungefähr.
- **Regel:** Sind alle Ergebnisse gleich wahrscheinlich, gilt P = günstige : alle. Erst prüfen, dann zählen.
- **Gegensatz:** „Drei Farben, also 1/3“ ist falsch. Die Farben sind nicht gleich wahrscheinlich, die Kugeln schon.
- **Probe:** Alle Farben zusammen: 3/10 + 5/10 + 2/10 = 1. Jede Wahrscheinlichkeit liegt zwischen 0 und 1.
- **Typischer Fehler:** 3/7 – rot zu nicht-rot. Im Nenner stehen alle 10.
- **Jetzt du:** P(nicht blau) = □. (5/10 – auf zwei Wegen: 3 + 2 günstige, oder 1 − 5/10.)

Jede neue Zeile kostet Lesezeit. Regel für den Erklärer [M]: höchstens zehn Zeilen, jede Zeile ein Satz, die Frage vorne und die Mini-Aufgabe hinten sind Pflicht.

## 10. Üben (Frage 10)

Die Regel für „gelandet“ ist durchdacht: sechs eigene Lösungen, zwei Typen, eine schwere, die letzten drei in Folge, keine Minuspunkte; „sicher“ erst nach 14 Lerntagen, Mischkarte und Nachtest [G]. Ändern würde ich [M]:

| Was | Heute [G] | Vorschlag | Warum |
|---|---|---|---|
| Reihenfolge | Stufe steigt mit den Lösungen | erste zwei Karten als Paar: vorgerechnetes Beispiel, dann Zwilling | Einstieg ohne Lehrer |
| Verteilung | Landen an einem Tag möglich | „gelandet“ erst mit einer Lösung an einem **zweiten Tag** | Abstände zählen mehr als die Schwelle [H] |
| Mischen | jede 4. Karte (bis Klasse 6 jede 6.), erst ab drei gelandeten Etappen | zusätzlich die tägliche Fünf über alle Flüge und Regeln | Erkennen ohne Etikett ist Prüfungsleistung |
| Stufe 3 | eine schwere Aufgabe genügt | zwei, davon eine Umkehr- oder Begründungsaufgabe | Stufe 3 ist das Niveau des Tests |
| Zweiter Versuch | bei allen Formen | bei Auswahl kein zweiter Versuch, stattdessen Zwillingsaufgabe | Rate-Chance 1/2 bei vier Antworten |
| Tipp | ein Tipp | zwei Stufen: erst eine Frage, dann der erste Schritt | Tipps nennen oft gleich die Formel (Abschnitt 12) |
| Papier | zählt nicht | eine Papier-Aufgabe mit Kontrollzahl je Etappe für „gelandet“ | Maßstab |
| Knobel | am Ende, freiwillig | bleibt; dazu gelegentlich eine Knobelfrage **vor** der Erklärung | erst denken, dann lesen |

Menge: sechs ist genug, wenn der zweite Tag dazukommt. Mehr Karten am selben Tag bringen wenig.

## 11. Welche Aufgabenformen fehlen am dringendsten? (Frage 11)

| Rang | Form | Gebiet | Beispiel |
|---|---|---|---|
| 1 | **Gitterpunkte setzen** (`punkte`, Vorgabe liegt vor) | Geometrie, Funktionen | Parallele durch P zeichnen; Gerade zu einer Gleichung |
| 2 | **Bedingung statt Lösung** (Abschnitt 3) | alle | „Nenne einen Punkt C, sodass …“; Gegenbeispiel |
| 3 | **Mehrfach-Antippen** | Daten, Begriffe | drei Aussagen zu einem Diagramm: stimmt / stimmt nicht |
| 4 | **Papier mit Kontrollzahl und Schema** | Sachaufgaben, Begründen | Ansatz, Rechnung, Antwortsatz mit Teilpunkten |
| 5 | **Term aufstellen**, geprüft durch Einsetzen | Algebra, Sachaufgaben, Tabellenkalkulation | Umfang einer Figur als Term; Formel für eine Zelle |
| 6 | **Im Diagramm handeln** | Daten | fehlende Säule auf die richtige Höhe setzen |
| 7 | **Balken beschriften** | Geld, Sachaufgaben | Teile eines Balkens mit Zahlen füllen |
| – | Zirkel und Geodreieck | Geometrie | nur auf Papier |

Rang 3, 5, 6 und 7 lassen sich aus vorhandenen Bausteinen bauen (Auswahl, Lücken, Markierung am Strahl).

## 12. Aufgabenqualität: 60 Aufgaben aus drei Flügen (Frage 12)

Zufällig gezogen, je 20 Übungen: Winkel (Klasse 5, Geometrie), Kennwerte (Klasse 6, Daten), Funktionsbegriff (Klasse 8). [G gezählt, Urteil M]

**Gut**
- Stufen sind echt gestuft; Stufe 3 verlangt Denken (Parameter, rückwärts, Fehler finden), nicht größere Zahlen.
- Vielfalt: acht bis zehn verschiedene Aufgabentypen in 20 Karten.
- Sachkontexte sind glaubwürdig und knapp (Tarife, Schranke, Notenschnitt).
- Falsche Antworten bei Auswahl sind benannte Denkfehler, kein Füllstoff.
- Lösungswege im Funktionen-Flug folgen „Gegeben – Gesucht – Ansatz – Rechnung“.

**Schwach**
- **Formen:** 100 %, 100 % und 95 % Zahl oder Auswahl. Im Winkel-Flug wird kein Winkel gemessen oder gezeichnet, bei Kennwerten keine Datenreihe erzeugt, bei Funktionen kein Graph gezeichnet.
- **Tipps verraten den Weg:** Bei Kennwerten nennt der Tipp in 8 von 20 Karten die Formel („Mittelwert mal Anzahl“). Dann ist der Tipp die Lösung.
- **Typ fehlt** bei 7 von 60 Karten; solche Karten zählen nicht für die Zwei-Typen-Regel.
- **Stufe passt nicht immer:** eine Umkehrung als „leicht, direkt“ eingestuft; zwei Karten „Berechne den Mittelwert von …“ unterscheiden sich nur in den Zahlen.
- **Ein Weg:** Kein Lösungsweg zeigt einen zweiten Weg. Das Schema „Gegeben – Gesucht“ gibt es nur in einem der drei Flüge.
- **Begründen** ist immer Auswahl.
- **Hinweis an den Projektleiter:** Eine Karte im Kennwerte-Flug fragt nach der richtigen Rechnung für den Mittelwert zweier Zahlen und benutzt dieselben beiden Zahlen wie eine Aufgabe des Tests 2025. Das gehört in die offene Stichprobe „nichts wörtlich“.

## 13. Was machen andere klar besser? (Frage 13)

Aus eigener Kenntnis, nicht nachgeschlagen [A]:
- **Bayerische Schulbücher:** vermischte Aufgaben und „Teste dich“-Seiten am Kapitelende; Grundwissen-Seiten je Jahrgang, auf die spätere Kapitel zurückgreifen; Aufgaben „Begründe“, „Finde den Fehler“, „Gib ein Beispiel an“ in jedem Kapitel.
- **Singapur-Lehrwerke:** wenige Beispiele, dafür in fester Folge Material – Bild – Zeichen; das Balkenmodell als durchgehendes Werkzeug.
- **Japanischer Unterricht:** eine Aufgabe, mehrere Wege, dann der Vergleich.
- **Aufgabenfolgen mit Variation:** von Aufgabe zu Aufgabe ändert sich genau eine Sache. Das Kind sieht, was die Änderung bewirkt. Unsere Karten kommen gemischt, diese Wirkung entsteht nicht.
- **Rückmeldung mit den eigenen Zahlen** (bettermarks [H]): Die Musterlösung rechnet mit der Eingabe des Kindes weiter und zeigt die Stelle, an der es kippt.
- **Heft-Pflicht mit Stichprobe** (Sparx [H]).

Übernehmen würde ich davon zuerst: Variations-Folge für die ersten vier Karten einer Etappe, Grundwissen als tägliche Fünf, Stichprobe.

## 14. Wofür ist eine Lehrer-Stunde je Woche am wertvollsten? (Frage 14)

Für das, was die App nicht kann [M]:

| Zeit | Was | Warum der Mensch |
|---|---|---|
| 20 min | **Heft und Papier-Runde durchsehen:** Rechenweg, Schreibweise, Antwortsatz, Begründungssätze | Darstellung bewertet nur ein Mensch; 24 % des Tests |
| 15 min | **„Erklär mir diese Aufgabe“:** Das Kind erklärt laut, der Lehrer fragt „warum?“ | findet Bedeutungsfehler, die kein Ergebnis zeigt |
| 15 min | **Eine reiche Aufgabe gemeinsam:** Sachaufgabe oder Konstruktion, der Lehrer denkt laut vor | Ansatz finden lernt man am Vorbild |
| 10 min | **Vorschau:** die schwerste Idee der nächsten Woche in zwei Minuten; was lief gut | Motivation und Richtung |

Nicht dafür: Verfahren erklären, die die App erklärt; Ergebnisse abhaken. Die App bereitet die Stunde vor: drei Heftstellen, zwei Aufgaben zum Erklären, eine reiche Aufgabe.

## Nachtrag nach Lektüre der Recherche-Berichte (Stand `lernen-app` e8a373f)

Gelesen: die Kernteile von `tief-5`, `tief-3`, `tief-2`, `tief-6`, `tief-7`, dazu `tief-8`, `tief-10`, `tief-4`, `tief-12` – nicht jede Zeile. Rechnungen: `recherche_stichprobe.py`. Alles aus den Berichten bleibt [H], soweit nicht anders vermerkt.

**1. Erfolgsquoten jetzt für alle drei Jahrgänge.** `tief-5` nennt die Quote jeder Teilaufgabe. Die Einzelwerte ergeben genau die Gesamtquoten der Berichte (47,1 / 49,4 / 41,5 %) [G gerechnet]. Nach meiner Zuordnung:

| Tätigkeit | BE | landesweit richtig 2023–2025 |
|---|---|---|
| Rechnen, nur die 15 Regeln | 20 | 54 % |
| Rechnen mit Geometrie-Formel | 6 | 43 % |
| Übertragen, Umkehren, Term aufstellen | 12 | **33 %** |
| Begründen | 15 | 37 % – in Geometrie 34 % |
| Zeichnen, Sehen | 4 | 53 % |
| Ablesen, Datenbegriff | 4 | 71 % |

Der Wert 16 % für „Übertragen“ in Abschnitt 1 galt nur für 2025. Über drei Jahre sind Übertragen und Begründen etwa gleich schwer. Die Reihenfolge der Hebel bleibt.
**2. Rahmen des Tests**, bisher bei mir „nicht geprüft“: 40 Minuten, Geodreieck und Zirkel, kein Taschenrechner, keine Formelsammlung; etwa 30 % der BE als Lücke oder Ankreuzen [H, mit Verweis auf Eltern- und Lehrerinformation des Staatsinstituts]. „Keine Formelsammlung“ stützt den Formel-Koffer aus Abschnitt 2.
**3. Zuordnung des Helfers neben meiner:** Wir unterscheiden uns bei acht Teilaufgaben, immer an derselben Grenze: Er bucht Aufgaben mit Flächen- oder Volumenformel als „Geometrie, keine Regel“, ich als „Regel plus Formel“. Seine 22 und meine 20 BE für „nur Regeln“ sind dieselbe Aussage.

**4. Was ich an meinem Papier ändere**
- **Frage 8, vier Wochen:** Die erste und die letzte Papier-Runde des älteren Kindes sollten **ein ganzer amtlicher Test** sein (Eich-Plan in `tief-5`, Abschnitt 7a): jetzt der Jahrgang 2025, nach vier bis sechs Wochen 2024, unter Originalbedingungen. Das gibt sofort eine Zahl gegen den Landesschnitt. Für das jüngere Kind gibt es nichts Gleichwertiges; am nächsten liegt der Realschul-Test der Jahrgangsstufe 6 – erst am Ende des Stoffs von Klasse 5 sinnvoll. Eigene Papier-Runden füllen die Wochen dazwischen.
- **Frage 5, erst knobeln:** Laut `tief-8` zeigt die Sammelstudie den Vorteil nicht für jüngere Kinder (Klasse 2–5 eher umgekehrt). Für das jüngere Kind also nur die kurze Vorhersage-Frage, kein Knobeln am neuen Stoff.
- **Frage 10, „gelandet“:** Mein „zweiter Tag“ deckt sich mit „vorläufig gelandet, fest erst nach bestandener erster Wiederholung“ aus `tief-3` und `tief-8`. Ich übernehme zwei Dinge: Abstände in **Kalendertagen**, und der Tipp zählt für die Folge wie ein Fehler.
- **Frage 6, Katalog:** Der Helfer markiert selbst, welche Einträge nur aus Fachwissen stammen. Meine fünf Prüfungen bleiben; dazu: „richtige Antwort trotz Denkfehler“ je Eintrag ausschließen (Checkliste in `tief-2`, Abschnitt 4).
- **Frage 13:** Was ich „aus eigener Kenntnis“ über Sparx schrieb, ist in `tief-7` belegt und genauer: Geprüft werden nur **richtig** gelöste Aufgaben, die Frage wird **nicht gezeigt**, die Häufigkeit sinkt bei Bestehen. Für die Wirkung des Checks selbst gibt es keinen Beleg.

**5. Wo ich den Berichten widerspreche**
- **„Schritt-Systeme 0,76 gegen Antwort-Systeme 0,31 – wichtigster Einzelbefund“ (`tief-8`):** überdehnt. `tief-7` berichtet eine niederländische Studie mit schrittweiser Eingabe und reiner Richtig-falsch-Rückmeldung: nie besser, im Behaltenstest schlechter. `tief-8` selbst nennt für Tutorsysteme in Schulmathematik Effekte nahe null. Schritte eintippen hilft nicht von selbst; es kommt auf die Rückmeldung je Schritt an. [H gegen H]
- **„Gitter 10 × 10 auf 340 px, etwa 34 px Abstand“ (`tief-10`):** gilt nur ohne Rand. Im vorhandenen Bild bleiben 26 Einheiten, am Handy gemessen 23 px [G]. Die Pfeil-Knöpfe aus `auftrag2.md` bleiben Pflicht.
- **Erklärung mit 10 bis 18 Eingaben in 6 bis 12 Minuten (`tief-10`):** Die Belege stammen aus Laborstudien, großteils mit Erwachsenen [A]. Ich bleibe bei höchstens sechs Bildschirmen. Dass die Funktionen-Erklärung „vermutlich“ deshalb nicht verstanden wurde, ist eine Vermutung des Helfers.
- **Kontrollzahl als Auswahl aus vier Werten (`tief-7`, 10.4):** zeigt dem Kind die typischen falschen Werte und lässt raten. Freie Eingabe.
- **„15 bis 30 Stunden Etikettieren“ (`tief-3`):** Schätzung ohne Probe. Erst an drei Flügen messen.
- **Prüfskripte der Helfer liegen nicht im Repo** (laut `tief-12` in einem Zwischenordner). Zwölf Beispiele habe ich nachgerechnet, alle stimmen [G]. Für alles Übrige gilt „nachgerechnet“ nur auf Zusage.

## Nicht geprüft

Arbeitszeit, Hilfsmittel und Erfolgsquoten 2023 und 2024 nur über `tief-5`, nicht an der Quelle; alle mit [H] markierten Befunde außer den zwei nachgeschlagenen; die sieben Berichte, die nicht genannt waren (`sucher-a` bis `-d`, `tief-1`, `-9`, `-11`); Lehrplan-Passung der zehn Umkehr-Muster; ob die Formen aus Abschnitt 11 wirklich klein zu bauen sind.

**Quellen:** (1) Staatsinstitut für Schulqualität und Bildungsforschung, Bayerischer Mathematik-Test Jahrgangsstufe 8, Aufgaben Gruppe A 2023–2025, Lösungshinweise und Ergebnisse 2025, https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/BMT8_2025_Ergebnisse.pdf · (2) Bastani u. a. 2025, Generative AI without guardrails can harm learning, PNAS 122, https://papers.ssrn.com/abstract=4895486 · (3) Muralidharan, Singh & Ganimian, Disrupting Education?, Zusammenfassung J-PAL, https://www.povertyactionlab.org/print/pdf/node/2242?lang=en
