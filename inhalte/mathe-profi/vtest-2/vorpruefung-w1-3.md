# Dritte Vorprüfung Welle 1 (Runde 2) – gezielte Nachprüfung, Stand `7cc61b65`

Stand 29.11.2026. Geprüft wurden:
- vollständig die neuen Aufgaben 031, 038, 040, 042, 095, 097, 108, 110, 112, 115, 117 und 118 sowie die geänderten 098, 100, 103, 104, 109, 113 und 116;
- dazu die Gesamtsicht der fünf Aufgaben je Lernziel.

Die Aufgaben 036, 039, 111 und 116 haben nur die Reihenfolge der Möglichkeiten gewechselt; das habe ich mitgeprüft.

Maßstab wie in `vorpruefung-w1-2.md` (Urteil 1222, 5er-Regel, im Zweifel Schema). Den Bestand der jeweiligen Etappe habe ich gegen alle neuen Aufgaben neu gelesen.

**Nachrechnung:** `vorpruefung_w1_rechnen.py` hat einen Abschnitt „Dritte Fassung“ bekommen. Ergebnis: 0 Abweichungen bei 50 Sollantworten; alle Fehlbild-Rechnungen stimmen. Gezielt bestätigt:
- **095:** 75.
- **097:** Jede Marke liegt genau 10 zu weit links (für alle Strichzahlen bis 10 000 geprüft).
- **098:** 19.
- **108:** Lea liegt immer zu hoch (alle Faktoren 11 bis 199 ohne Zehnerzahlen geprüft). Bei Tom kommen beide Richtungen vor. „Lässt sich nicht sagen“ ist damit zwingend.
- **110:** Genau 5 Zeichen gespart werden nur bei 49 und 94. Bei 99 sind es 6 Zeichen.
- **112:** Kürzer als der Vorgänger wird die Schreibweise bei 4, 5, 9, 10, 14, 15, 19, 20 … .
- **113:** 3 999.
- **115:** Zahl + Gegenzahl = 31 → 19 und 12, eindeutig.
- **117:** Beide Gegenbeispiele stimmen.
- **118:** 16.
- **031:** [2, 3] (alle Glieder a · x², a · x, a mit −10 ≤ a ≤ 10, a ≠ 0 geprüft).
- **038:** [8, 24].
- **042:** Alle vier Fälle durchgerechnet; nur Möglichkeit 0 ist richtig.

## Urteil

| Einheit | bereit für die Gegenprüfung? | Grund |
|---|---|---|
| zahlen.natuerlich | **nein**, nach einem Pooltausch ja | A1: Bei strahl_eintragen ist 098 anspruchsvoller als der Test 095 |
| terme.umformen | **nein**, nach einer kleinen Änderung an 038 ja | A2: 038 lässt sich durch Ausrechnen aller 20 Paare lösen, minusklammer hat damit zwei Schema-Aufgaben |

Alle Befunde A1 bis A8 aus `vorpruefung-w1-2.md` sind geschlossen. Die neuen Muss-Befunde sind klein und mit je einer Änderung erledigt.

## Entscheidungen zu den gezielten Fragen

- **Test 095: Einsicht, kein Verfahren.** Die Zahlen sind unbekannt. Entscheidend ist zu sehen, dass ihr Unterschied auf beiden Strahlen derselbe ist, und das kehrt den Maßstab um. Kein Bestandsverfahren deckt das ab; K5A-V013 bestimmt einen Abschnittswert aus Anfang und Ende. Aber: 095 sind nur zwei Rechenschritte, und ein gutes Kind braucht 1–2 Minuten. 096 ist etwa gleich schwer. **098 ist klar anspruchsvoller**: Abstand der gemeinsamen Striche (600) erkennen, weil Auflisten von 59 bzw. 79 Strichen zu lang ist, dazu der Randfall 12 000. Siehe A1.
- **097: kein Schema, aber knapp.** Man muss Lenas falsche Zählregel nachbilden (Striche statt Abstände). Zwei selbst gewählte Beispiele (30 → 20, 50 → 40) legen die Antwort nahe, sind aber kein Verfahren aus dem Bestand. Damit hat strahl_eintragen keine sichere Schema-Aufgabe. Eine strengere Gegenprüfung könnte 097 als „durch Beispiele lösbar“ zählen; dann wäre es die eine erlaubte.
- **038: Schema.** Es gibt nur 20 Paare (a, b). Alle auszurechnen und die verschiedenen Werte zu zählen dauert 2–3 Minuten und braucht die Einsicht „der Wert hängt nur von b − a ab“ nicht. Mit 035 sind das zwei Schema-Aufgaben. Siehe A2.
- **042 neben Test 039: zulässig.** 039 begründet, dass zwei Werte a · x + b festlegen. 042 unterscheidet Fälle (keine, genau eine, jede Übereinstimmung) nach den Zahlen vor x und den Zahlgliedern. Die Denkfigur ist verwandt, die Denkleistung eine andere, und keine verrät die andere. 042 ist etwa so anspruchsvoll wie der Test (C1).
- **117 neben Bestand #442: zulässig.** #442 vergleicht zwei gegebene Zweierzahlen durch Umrechnen. 117 beurteilt allgemein, ob die Zahl der Einsen etwas über die Größe sagt. Gleiche Einsicht, andere Denkleistung, also kein Kern. Bauart-Risiko siehe B1.
- **Test 115 („zusammen immer 31“): eindeutig, für Klasse 5 anspruchsvoll, aber machbar.** Ein gutes Kind braucht etwa 3 Minuten. Es muss verstanden haben, dass an jeder Stelle genau eine der beiden Zahlen eine 1 hat (Summe 11111 = 31), und dann Summe und Unterschied nutzen oder Paare probieren. Nicht nur für sehr starke Kinder.
- **Test 110 (49 und 94): eindeutig, für Klasse 5 in 2–3 Minuten machbar.** Durch die vier Beispiele im Text ist die Leselast gering. Verstanden sein muss: Ersparnis gibt es nur bei den Ziffern 4 (2 Zeichen) und 9 (3 Zeichen), und 5 = 2 + 3. B1 aus der zweiten Prüfung ist geschlossen.
- **„Nicht entscheidbar“: genügt jetzt.** Die Möglichkeit steht 9-mal und ist 2-mal richtig (108, 117). Bei vier Möglichkeiten wären etwa 2,25 Treffer zu erwarten; das ist kein Muster mehr.
- **108: „lässt sich nicht sagen“ ist bei Tom zwingend.** Die beiden Gegenbeispiele im Text stimmen: 12 · 19 = 228 wird zu 200 (zu klein), 18 · 11 = 198 wird zu 200 (zu groß). Die Bedingung „keine Zehnerzahl“ sorgt dafür, dass Lea sicher zu hoch liegt. Richtig ist genau Möglichkeit 0.

## Befunde A (Muss)

**A1 – strahl_eintragen: Der Test ist nicht die anspruchsvollste Aufgabe.**
- *Beleg:* 095 (Test) sind zwei Schritte: Unterschied 300, dann 300 : 4. 098 (Sicherung) verlangt mehr: zwei Teilungen, den Abstand der gemeinsamen Striche, Zählen der Vielfachen und den Randfall.
- *Vorschlag:* **Pools tauschen**, 098 wird Test und 095 Sicherung. Danach stimmt alles: Der Test ist kein Schema, Test und Korrektur fragen Verschiedenes, Schema 0 bis 1.

**A2 – minusklammer: zwei Schema-Aufgaben (035, 038).**
- *Beleg:* 038 lässt sich durch Ausrechnen aller 20 Paare lösen (Notiz im Skript).
- *Vorschlag:* den Zahlbereich so groß machen, dass Auflisten nicht mehr geht, z. B. „zwei verschiedene Zahlen aus 1 bis 20“. Lösung dann 38 verschiedene Werte (b − a = ±1 … ±19), größter Wert 39. Fehlbilder entsprechend: 380 alle Paare, 39 mit dem Wert 20, 19 nur a > b, 1 für a groß und b klein.

## Befunde B (Soll)

- **B1 – 112 und 117: Das entscheidende Gegenbeispiel steht nur in der richtigen Möglichkeit.**
  - 112: „XVIII … fünf Zeichen, XIX … nur drei“.
  - 117: „111 hat mehr Einsen als 1000 und ist weniger wert …“.

  Wer nur das angegebene Beispiel nachprüft, hat die Lösung. Das ist ein Schema-Risiko (Prüfen statt Finden), und in 117 stehen konkrete Zahlen nur in der richtigen Möglichkeit. *Vorschlag:* Auch die Ablenker mit konkreten, aber falsch gedeuteten Beispielen bauen, z. B. „A ist größer, wie 111 = 7 gegen 100 = 4 zeigt“. Oder in der richtigen Möglichkeit das Beispiel weglassen („… denn der Wert hängt davon ab, wo die Einsen stehen“).
- **B2 – 110 verrät 112.** Der Lösungsweg des Tests 110 zeigt, dass die Schreibweise bei einer 9 kürzer wird (VIIII → IX), und die richtige Möglichkeit von 112 nutzt genau XVIII → XIX. Nach einem Fehler im Test sieht das Kind den Lösungsweg und dann 112. *Vorschlag:* Das Beispiel in 112 aus dem Sprung auf ein neues Zeichen nehmen, das 110 nicht behandelt, z. B. XIV (14) → XV (15). Das passt auch zu B1.
- **B3 – 097 Voraussetzung:** „Lena trägt eine Zahl so ein: Sie teilt die Zahl durch 10 …“ setzt stillschweigend voraus, dass die Zahl auf einem Strich liegt und nicht 0 ist (bei 35 oder 0 ist die Regel nicht anwendbar). *Vorschlag:* „eine Zahl, die auf einem Strich liegt (nicht die 0)“.

## Befunde C (Kann)

- **C1 – Test 039 und Sicherung 042** sind etwa gleich anspruchsvoll. Vertretbar, weil 039 die tiefere Einsicht verlangt (Begründen statt Fallunterscheidung).
- **C2 – 108 ↔ themen #321** (Aufzug: Gewichte „rund 80 kg“, sicher nicht überladen?). Verwandte Einsicht (Richtung des Rundungsfehlers), aber Produkt und Fallunterscheidung sind neu. Zulässig.
- **C3 – 040:** Alle vier beschriebenen Zählweisen zählen richtig, entscheidend ist nur der Aufbau des Terms. Das ist eindeutig, weil jede Möglichkeit zu einem anders gebauten Term führt; im Lösungsweg steht das. Ein Satz im Fragetext („Welche Zählweise passt zum Aufbau ihres Terms?“) würde Diskussionen vermeiden.

## Gesamtsicht je Lernziel (Stand `7cc61b65`)

| Lernziel | Schema (höchstens 1) | Denkfiguren | Test kein Schema und die anspruchsvollste? | Verraten? | erfüllt? |
|---|---|---|---|---|---|
| stellenwert | 087 | 5 | ja (085) | nein | **ja** |
| ziffern_zu_zahlwort | 092 | 5 | ja (090) | nein | **ja** |
| strahl_eintragen | – (097 knapp kein Schema) | 5 | kein Schema, **aber nicht die anspruchsvollste** (098 mehr) | nein | nach A1 ja |
| runden_regel | 102 | 5 | ja (100) | nein | **ja** |
| runden_sinnvoll | 106 | 5 (108 neu: Richtung des Schätzfehlers) | ja (105) | nein | **ja** |
| roemisch_schreiben | 111 (112 Risiko, B1) | 5 | ja (110) | 110 → 112 (B2) | **ja**, mit B1/B2 |
| dualsystem | 116 (117 Risiko, B1) | 5 (115 Gegenzahl, 117 Einsen ≠ Größe, 118 kaputte Lampe, 119 Stellenzahl) | ja (115) | nein | **ja**, mit B1 |
| zusammenfassen | 030 | 5 (031 neu: was ein Glied ändern kann) | ja (029) | nein | **ja** |
| minusklammer | 035, **038** | 5 | ja (034) | nein | nach A2 ja |
| aequivalenz | 043 | 5 (040 Term → Zählweise, 042 Fallunterscheidung) | ja (039), C1 | nein | **ja** |

**Tests der Einheiten, verschiedene Denkfiguren:**
- zahlen.natuerlich:
  - 085: Wertverhältnis → Stellenabstand
  - 090: leere Klasse
  - 095: gleicher Unterschied, umgekehrter Maßstab (nach A1: 098, gemeinsame Teilstriche)
  - 100: zwei Rundungsbereiche
  - 105: Rundungsbereich und Rest
  - 110: Ersparnis je Ziffer, rückwärts
  - 115: Zahl + Gegenzahl

  Alle verschieden; die Form „Bereich durchzählen“ kommt nur noch zweimal vor (090, 100).
- terme.umformen:
  - 029: Koeffizientenvergleich
  - 034: Wirkung einer falschen Regel, rückwärts
  - 039: zwei Einsetzungen legen a · x + b fest

  Verschieden.

**Bestandskern gegen die Etappe:** Bei keiner der neuen oder geänderten Aufgaben habe ich einen gefunden.
- 040 ist jetzt die Gegenrichtung zu #237 bzw. R8-V009.
- 118 hat mit #437 nichts mehr gemein.
- 115 und 038 haben keine Entsprechung im Bestand.

**Ablenker:** Kein Ablenker hat ein richtiges Urteil mit nur falscher Begründung; jede Möglichkeit ist genau einmal richtig. Wörtlich wahre Ablenker: keine. Die neuen Ablenker in 103 und 104 sind falsch. Der neue Ablenker in 109 („… ergeben zusammen genau 14 000“) hat ein falsches Urteil. B7 aus der zweiten Prüfung ist geschlossen.

## Zahlen
- A: **2** (A1 Pooltausch 095 ↔ 098, A2 Zahlbereich in 038). B: **3**. C: **3**.
- Nach A1 und A2 erfüllen alle zehn Lernziele den Maßstab; B1 bis B3 sind für die Gegenprüfung empfohlen.
