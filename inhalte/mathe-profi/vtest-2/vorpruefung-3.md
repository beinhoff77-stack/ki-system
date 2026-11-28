# Dritte Vorprüfung VT2 (Nachprüfung der Runde-2-Korrektur)

Stand: Zweig `vorpruefer-vt2c` auf `helfer-vtest-r2` (69076e9a). Geprüft: alle 33 genannten Aufgaben, alle 76 seit 852d461b geänderten (die 33 sind darin enthalten bis auf VT2-005, das unverändert ist), außerdem alle 44 Auswahlaufgaben und alle 19 Lernziele auf Schema-Nähe. Rechenskript: `vorpruefung_rechnen_3.py` (nur Standardbibliothek, Brüche, Aufzählen; `python3 -I inhalte/mathe-profi/vtest-2/vorpruefung_rechnen_3.py`).

## Urteil

**Nach kleiner Korrektur einspielbar:** Keine falsche Lösung und keine falsche Auswahloption gefunden (0 A); aber 12 B-Befunde, darunter drei Test-/Übungsdoppelungen zum Bestand (001, 015, 005/044), eine erratbare Aufgabe (080, 055), ein Fehlbild an falscher Lücke (057) und ein Bauartmuster bei den Fehler-Detektiven (nie Zeile 1, alle vier Tests Zeile 2). Vor dem Einspielen sollten die B-Befunde 1 bis 9 und 11 erledigt sein.

## Was geprüft wurde und womit

- **Sollwerte:** 90 Zahl-/Lücken-Aufgaben mit eigener Rechnung nachgerechnet (Brüche, Einsetzen an Stützstellen, Aufzählen, Koordinaten, römische Zahlen per Funktion): 0 Abweichungen zu `loesung_rechnung` und zu `o`. Für die übrigen Zahl-/Lücken-Aufgaben nur die allgemeine Prüfung (Rechenausdruck = Soll; jedes Fehlbild: Rechnung = Antwort, Antwort ≠ Lösung, keine doppelte Fehlantwort).
- **Auswahl:** alle 44 mit je 4 Möglichkeiten einzeln beurteilt (14 mechanisch im Skript, 30 von Hand begründet); je Aufgabe genau eine richtige, jede falsche mit Fehlbild und passendem Text. Befund: keine Doppelrichtigkeit.
- **Gegenläufige Prüfwerkzeuge** (nur lesend ausgeführt): `tools/vtest_pruefen.py --runde 2` OK (drei bekannte Hinweise 106, 108, 118 – Alarm bestätigt, da Runden nur in der Voraussetzung), `gegenrechnung.py` 0 Abweichungen.
- **Tipp (`h`):** in keiner der 133 Aufgaben vorhanden; deshalb nichts zu prüfen. Lösungswege (`w`) passen zu allen Aufgaben; in VT2-087 ist der Weg sprachlich unbeholfen (C).
- **Fakt vs. Annahme:** „Fakt“ = nachgerechnet oder im Repo/auf der Lehrplan-Seite gelesen; „Annahme“ = meine Einschätzung (Schema-Nähe, Erratbarkeit, Lehrplan jenseits des gelesenen Textes).

## Befunde A (falsch, Muss)

Keine.

## Befunde B (Soll)

1. **VT2-001 (Test) ist Bestand mit neuen Zahlen.** Beleg: `themen/finanzen.zinsen.json`, Lernkarte rollen, Übung „Jemand hat 1 000 € auf dem Sparkonto zu 1 % und gleichzeitig 1 000 € Kredit zu 8 %. Wie viel Euro verliert er in einem Jahr durch die Zinsen?“ – gleiche Netto-Rechnung; neu ist nur die Frage nach dem Prozentsatz. `bestandsvergleich.md` nennt 001 selbst „nah“. Vorschlag: Test neu bauen, z. B. rückwärts (Nettozinsen und beide Zinssätze gegeben, Kredithöhe gesucht) oder mit Teilbeträgen, und 001 als Korrektur behalten.
2. **VT2-015 (Test) ist Bestand mit neuen Zahlen.** Beleg: `themen/finanzen.zinsen.json`, Bonus „Ein Kapital bringt bei 3 % in einem Jahr 36 € mehr Zinsen als bei 2 %. Wie groß ist das Kapital?“ (Wortüberlappung 0,87 gegen mein Maß; selbe Struktur, nur Zahlen anders). Die Korrektur hat eine Doppelung durch eine andere ersetzt. Vorschlag: andere Idee (z. B. zwei Kapitalien, ein Kapital 500 € größer, gleiche Zinsen bei verschiedenen Sätzen) oder 020 als Test-Aufgabe nehmen.
3. **VT2-005 deckt sich mit dem Bestand** (`themen/finanzen.zinsen.json`, kapital: „Nach einem Jahr mit 3 % Zinsen sind 1 545 € auf dem Konto. Wie viel Geld wurde eingezahlt?“ = 1 545 : 1,03); nur „Kredit/Rückzahlung“ statt „Konto“. Lehrplanfrage siehe unten. Vorschlag: durch eine Aufgabe ersetzen, die die Rollen prüft (z. B. Rückzahlung bei zwei Krediten zu verschiedenen Sätzen, welcher Kredit ist größer).
4. **VT2-044 ≈ Bestand** (aequivalenz-Übung „Setze x = 4 in 3(x + 2) und in 3x + 2 ein. Um wie viel ist der erste Wert größer?“). 044 fügt nur ein zweites x hinzu. Vorschlag: Idee „der Unterschied bleibt gleich“ als Auswahl mit Begründung („Für welches x sind die Terme gleich?“ – für keins) oder ersetzen.
5. **VT2-080 ist erratbar und Bestand-nah.** Die Lösung [1, 2, 3] folgt genau der Reihenfolge, in der die drei Fälle im Text genannt werden (innerhalb (1), auf der Seite (2), außerhalb (3)) und der Reihenfolge der Dreiecke A, B, C. Der Bestand hat dieselbe Frage „Wo liegt der Umkreismittelpunkt?“ je Dreieck (umkreis_inkreis, Übung und Sicherung). Vorschlag: Dreiecke so ordnen, dass die Lösung z. B. [3, 1, 2] ist, oder statt der Zuordnung nach einem fehlenden Winkel fragen (α = 70°, β = 20°: Ist γ stumpf, wo liegt der Mittelpunkt?).
6. **VT2-055: die Antwort steht im Text.** „… größten gemeinsamen Faktor 9x …“ und gesucht ist k = 9. Ein Kind ohne Einsicht schreibt 9. Vorschlag: so umbauen, dass die gesuchte Zahl nicht im Text vorkommt, z. B. „18x² + kx hat den größten gemeinsamen Faktor 6x, k ist eine positive ganze Zahl kleiner als 10, k ist kein Vielfaches von 4“ (k = 6 ist dann einzig möglich, 12 scheidet durch k < 10 aus; vor dem Einbauen eindeutig nachprüfen).
7. **VT2-057 (Test): Fehlbild an falscher Lücke.** Das Fehlbild „Zeile 1 für falsch gehalten“ (antwort 1) steht bei `luecke: 2` (Beiwert von x²), gehört aber zu Lücke 1; Lücke 1 hat kein Fehlbild. Folge: falsches Feedback bei Eingabe 1 in Lücke 2. Vorschlag: `luecke` auf 1 setzen. Das Prüfwerkzeug fängt das nicht (`vorpruefung_rechnen_3.py`, Teil 1).
8. **VT2-017: falscher Fehlbild-Text.** Zur Option „52 · 0,04 = □“ steht „… sondern ein Hundertstel der Zinsen“; 52 · 0,04 sind vier Hundertstel der Zinsen (2,08). Vorschlag: „… nicht das Kapital: 52 · 0,04 = 2,08 sind nur ein kleiner Teil der Zinsen“.
9. **Fehler-Detektiv: Fehlerzeile ist fast immer Zeile 2.** Von 18 Fehler-Detektiv-Aufgaben liegt der erste Fehler 12-mal in Zeile 2, 6-mal in Zeile 3, nie in Zeile 1, nur 3-mal in der letzten Zeile (004, 067, 102). Alle vier Tests (008, 036, 057, 120) haben Zeile 2. Das Skript zeigt die Liste. Wer „Zeile 2“ rät, trifft zwei Drittel; bei Auswahl (036, 062) lenkt es ebenfalls. Vorschlag: bei mindestens 4 Aufgaben die Fehlerzeile verschieben, mindestens einen Test (z. B. 008 → Zeile 3, 120 → Zeile 4 oder 1) und in zwei Aufgaben den Fehler in Zeile 1 legen.
10. **VT2-079 und VT2-081 (beide Korrektur, selbe Verwechslung).** 079 fragt „Mittelsenkrechten, denn gleich weit von den Ecken“; 081 verlangt dieselbe Erkenntnis und nennt sie in Zeile 1 („gleich weit von allen drei Ecken“) und in der Antwort (Mittelsenkrechten). Wer beide hintereinander als Verbesserung bekommt, hat die zweite durch die erste gelöst. Dazu berühren 082 und 084 dieselbe Achse (Mittelsenkrechte/Winkelhalbierende), 079–084 haben also nur zwei bis drei echte Ideen neben dem Zählen (078) und der Winkelrechnung (083). Vorschlag: 081 in den Pool sicherung verschieben und 079 ersetzen, z. B. durch „Wo liegt der Umkreismittelpunkt eines Dreiecks mit α = 35°, β = 55°?“ mit Begründung; mindestens aber die Reihenfolge so festlegen, dass 079 und 081 nicht nacheinander kommen.
11. **Schema-nahe Aufgaben je Lernziel: fünf Lernziele über der Grenze zwei** (Tabelle unten): zeitanteil (023, 025, 026), minusklammer (037, 040, 042), aequivalenz (043, 045, 046, 048), ausklammern (051, 053, 056), runden_sinnvoll (113, 114, 116, 118). Annahme: Einschätzung ist meine; Rezept = „einmal gelerntes Verfahren genau so ausführen“. Vorschlag je Lernziel: das schwächste Schema-Stück ersetzen (zeitanteil 025, minusklammer 042, aequivalenz 048, ausklammern 051, runden_sinnvoll 116 oder 118).
12. **Auswahl: Länge und Nebensatz verraten die richtige Option häufiger als Zufall.** Fakt: in 8 von 41 Textaufgaben ist die richtige Möglichkeit mindestens 25 % länger als die längste falsche (054, 059, 064, 094, 110, 111, 115, 129); in 13 von 41 ist sie strikt die längste (32 %, Zufall 25 %); Möglichkeiten mit „;“ oder „aber“ oder „, nicht/auch …“ enthalten 37 % der richtigen, aber nur 12 % der falschen. Die Prüfung im Bauskript betrachtet nur das mittlere Längenverhältnis (1,10). Betrifft den Test VT2-064. Vorschlag: bei den acht genannten die richtige kürzen oder die falschen auf gleiche Länge und gleiche Satzform bringen; Prüfung im Bauskript um „Anteil richtig ≥ 1,25 × längste falsche“ (höchstens 15 %) ergänzen.

## Befunde C (Kann)

1. VT2-006: `idee` lautet „Zinssatz aus Differenz“, gesucht ist aber das Kapital für gleiche Zinsen.
2. VT2-013: README nennt 36/36; jetzt 36 und 39 (README veraltet). Die Aufgabe selbst ist reine Rechnung (zwei Zinsen mit Komma); zählt unter den Schema-nahen des Lernziels.
3. VT2-030: kein Fehlbild für „1“ (Vorzeichen von −x² verloren), obwohl das die typische Verwechslung ist.
4. VT2-033: Fehlbild-Text „die 3 des Ergebnisses statt der abzuziehenden Zahl“ passt nur lose zur Rechnung 5 − 2.
5. VT2-042: Anweisung „Erkläre dir den Trick …“ ist kein Auftrag; 2 500 − 2 457 ist auch ohne Einsicht leicht; als Verstehen schwach.
6. VT2-051: ist Ausmultiplizieren (3x · (2x + 5)), nicht Ausklammern; gehört thematisch zu binomisch/ausmultiplizieren.
7. VT2-075: Fehlbild 4 (12 − 8, „Radius 4,5 auf 4 gerundet“) ist konstruiert; Kinder rechnen kaum so.
8. VT2-014, 100, 107: `typ` begruenden, aber keine Begründung verlangt. 100: die krumme Zahl 800 fällt ohne Skalenverständnis auf (alle anderen sind Vielfache von 250).
9. VT2-108: die Antwort 50 ist die „Hälfte von 100“ und damit ohne Einsicht erratbar; die Einsicht liegt im Gegenfall (49).
10. Test nicht klar die anspruchsvollste: 036 (Auswahl, 25 % Rateweg; 041 verlangt drei freie Werte), 064 (Auswahl; 070 verlangt drei Winkel), 113 (zwei Produkte; 118/119 mindestens gleich schwer), 001 (nicht schwerer als 002/007). Alle 19 Tests sind Stufe 3 und genau einer je Lernziel (Fakt).
11. Hinweise ohne Fehlbild: VT2-057 und 070, 123 haben für Lücke 1 kein Fehlbild.
12. README: Sammel-Möglichkeiten sind 7 (richtig 3: 110, 115, 129), nicht 5/2; `bestandsvergleich.md` ordnet 022 (zeitanteil) in die Zeile kapital und 078 (umkreis_inkreis) in die Zeile lage ein; Lernbereichsbezeichnung „M7 5 (Kreis)“ ist ein Repo-Etikett, der Lehrplanabschnitt heißt „Kongruenz, besondere Dreiecke und Dreieckskonstruktionen“.
13. Platzfolge der richtigen Möglichkeit nach Kennung: ABDBABDCCDBABDCDABDABDCCCDBABDCABDCABDCCDBAB; das Motiv „ABD“ kommt 8-mal vor (Zufall: etwa 1-mal). Auswirkung nur, wenn die App die Aufgaben in Kennungsreihenfolge ausspielt; je Pool (korrektur: ABDBDADCBCCADCACCBB, sicherung: BACCDBDADBDCDBBBDABDCDA, test: BA) ist kein Muster erkennbar. Kein Handlungsbedarf, nur merken.
14. Nahe am Bestand, aber im Fragefokus verschieden (behalten): 065 (Bestand fragt Radius, 065 die Höhe), 066 (Radius ↔ Durchmesser, sehr leicht), 070 (Bestand: α = 40° → β), 074, 075, 076, 086 (Bestand: „In 5 555 hat jede 5 denselben Wert“), 007, 099, 109, 110, 130. Die übrigen Nennungen der Liste „nahe am Bestand“ in `bestandsvergleich.md` (024, 027, 046 bis 049, 079 bis 082, 085, 087, 091, 093) sind im Fragefokus eigenständig.

## Antworten auf die Prüfpunkte

### 1. Lösungen
Alle Sollwerte stimmen (siehe oben). Fehlbilder plausibel und verschieden von der Lösung; Ausnahmen B7, B8, C3, C4, C7. Lösungswege passen.

### 2. Eindeutigkeit, Erratbarkeit
Eindeutig, mit Randfällen ausdrücklich im Text: 071, 078, 085, 106, 124, 126, 127 (nachgezählt per Aufzählung). Erratbar: 080 (B5), 055 (B6), 108 (C9). Kleine Antwortmengen mit Rateanteil, aber vertretbar: 073, 075, 103 (Antwort 1).

### 3. Schema-Nähe je Lernziel

Annahme: meine Einschätzung; „Schema“ = einmal gelerntes Verfahren genau so ausführen, ohne Begründung, Umkehrung oder Fehlvorstellung.

| Lernziel | Schema-nahe Aufgaben | Anzahl | Bewertung |
|---|---|---|---|
| rollen | 002, 007 | 2 | ok |
| jahreszinsen_komma | 010, 013 | 2 | ok |
| kapital | – (017 ist Darstellungswechsel) | 0 | ok |
| zeitanteil | 023, 025, 026 | 3 | B11 |
| zusammenfassen | 030, 034 | 2 | ok |
| minusklammer | 037, 040, 042 | 3 | B11 |
| aequivalenz | 043, 045, 046, 048 | 4 | B11 |
| ausklammern | 051, 053, 056 | 3 | B11 |
| binomisch | 058, 061 (060 Grenzfall) | 2–3 | Grenzfall |
| umkehrung | 066 | 1 | ok |
| lage | 072, 074 | 2 | ok |
| umkreis_inkreis | 079, 080 (083 Grenzfall) | 2–3 | Grenzfall |
| stellenwert | 087, 090 | 2 | ok |
| ziffern_zu_zahlwort | 093, 098 | 2 | ok |
| strahl_eintragen | 101, 104 (100 Grenzfall) | 2–3 | Grenzfall |
| runden_regel | 107, 112 | 2 | ok |
| runden_sinnvoll | 113, 114, 116, 118 | 4 | B11 |
| roemisch_schreiben | 122, 123 | 2 | ok |
| dualsystem | 128, 131 | 2 | ok |

### 4. Test = anspruchsvollste
19 von 19 Tests sind Stufe 3, eine je Lernziel. Offen bleibt C10 (036, 064, 113, 001). Alle anderen Tests (008, 015, 022, 029, 043, 050, 057, 071, 078, 085, 092, 099, 106, 120, 127) sind mindestens so schwer wie die schwersten Sicherungs-Aufgaben ihres Lernziels (Annahme).

### 5. Doppelung zum Bestand
Methode: je Aufgabe Wort- und Zahlenüberlappung gegen alle Übungs-, Test-, Bonus- und `rollend-*`-Aufgaben derselben Einheit, danach die nächsten Nachbarn von Hand gelesen. Echte Doppelungen: B1 (001), B2 (015), B3 (005), B4 (044). Zu nah in der Idee: 080 (B5). Die Liste „nahe am Bestand“ ist unter C14 einzeln beurteilt. Restunsicherheit: Aufgaben, deren Rechenweg im Bestand mit anderen Worten vorkommt, erkennt mein Maß nicht.

### 6. Auswahl-Muster (44 Aufgaben)

| Merkmal | Befund |
|---|---|
| Platz der richtigen Möglichkeit | A 9, B 13, C 10, D 12 (alle zwischen 20 % und 30 %); derselbe Platz in zwei Aufgaben hintereinander nur 4-mal (Zufall: etwa 11-mal) |
| Folge nach Kennung | ABDBABDCCDBABDCDABDABDCCCDBABDCABDCABDCCDBAB; Motiv „ABD“ 8-mal; je Pool kein Muster (C13) |
| Länge | richtige strikt am längsten 13 von 41 Textaufgaben (32 %); Rang 1 inkl. Gleichstand 19 von 44; mittleres Verhältnis richtig/falsch 1,10; ≥ 25 % länger als die längste falsche: 8 (B12) |
| denn/weil | richtig 61 %, falsch 61 %; kein Einzelgänger (Prüfung: richtige weicht von allen drei falschen ab) |
| Absolutwörter (immer, nie, nur, stets, jede, alle, keine …) | richtig 32 %, falsch 32 % |
| Sammel-Möglichkeiten („Beide …“, „Alle …“, „Weder …“) | 7, davon 3 richtig (110, 115, 129) |
| Nebensatz-Marker („;“, „aber“, „, nicht …“) | richtig 16 von 43 (37 %), falsch 15 von 129 (12 %) → B12 |
| Zahlen/Beispiele in der Möglichkeit | richtig 29 von 44 (66 %), falsch 70 von 132 (53 %): leichter Hang, nur merken |
| Wortüberlappung (Option, die den anderen am ähnlichsten ist, ist richtig) | 14 von 41 (34 %, Zufall 25 %): typisch für 2×2-Bauten wie 079 |
| Verdikt-Form „Richtig/Falsch“, „hat recht/unrecht“ | 039, 069, 077, 082, 117; in 039 und 077 ist das Mehrheitsverdikt (3 von 4) das richtige |
| Auswahl im Test-Pool | 2 (036, 064) |
| Fehler-Detektiv als Auswahl | 032, 036, 062, 094: die Fehlerzeile ist 3, 2, 2, 3 (B9) |

### 7. Lehrplan (LehrplanPLUS Gymnasium Bayern, G9)

Quelle: lehrplanplus.bayern.de, Fachlehrplan Gymnasium Mathematik, Jahrgangsstufe 6 und 7, gelesen am 28.11.2026 (Seitentext über Abruf; Jahrgangsstufe 8 war nicht abrufbar).

- **Umkehrung des Satzes des Thales:** Jahrgangsstufe 7, Lernbereich 5 („Kongruenz, besondere Dreiecke und Dreieckskonstruktionen“): Die Schüler beweisen den Satz des Thales und seine Umkehrung aus Winkelzusammenhängen und wenden beides bei rechtwinkligen Dreiecken an. Sicherheit: hoch (etwa 90 %). Die Aufgaben VT2-064 bis 070 sind damit im Lehrplan.
- **Umkreis, Inkreis:** Im Lernbereich 5 nur als Beispielliste in der Klammer („u. a. Umkreis eines Dreiecks, Inkreis eines Dreiecks, Satz des Thales“); Konstruktion von Mittelsenkrechte und Winkelhalbierende steht in Lernbereich 2.1. Die Lage des Umkreismittelpunkts (stumpf → außen) steht nicht im Lehrplantext. Sicherheit: mittel (etwa 65 %) für Klasse 7, der Bestand im Repo behandelt das ebenso.
- **Lage Gerade/Kreis (Passante/Sekante, Abstand ↔ Radius):** Die Wörter Passante und Sekante kommen im Text der Jahrgangsstufe 7 nicht vor; belegt ist nur die Konstruktion der Tangente an einen Kreis durch einen äußeren Punkt. Ob die Lage Gerade/Kreis in Klasse 7 oder erst später behandelt wird, kann ich nicht bestätigen (Sicherheit etwa 50 %). Raten will ich nicht: bitte bei der Schule bzw. im Schulbuch von Kind 1 und Kind 2 nachsehen. Die Aufgaben VT2-071 bis 077 sind davon betroffen; der Bestand (`themen/geometrie.kreis.json`) enthält denselben Stoff, das Risiko ist also nicht neu.
- **VT2-005 (vermehrter Grundwert 5 150 : 1,03):** Jahrgangsstufe 6, Lernbereich 3 heißt „Prozentrechnung, Daten und Diagramme“ und verlangt einfache Prozentaufgaben aus dem Alltag, u. a. zu Rabatt und Zins, mit Grundgleichung und Schlussrechnung. „Vermehrter Grundwert“ steht dort nicht; Jahrgangsstufe 7, Lernbereich 3 („Vertiefung der Prozentrechnung“) erweitert das. Über die Schlussrechnung (103 % entsprechen 5 150 €) ist 005 in Klasse 6 lösbar, aber grenzwertig. Sicherheit: etwa 60 %. Da der Bestand dieselbe Aufgabe enthält (B3), erledigt sich die Frage mit dem Ersetzen.
- **Monats-/Tageszinsen (zeitanteil):** im gelesenen Klasse-6-Text nicht ausdrücklich genannt (dort nur „Zins“ in Alltagsaufgaben). Sicherheit gering; Bestand enthält es ebenfalls. Nur als Zweifel notiert.

### 8. Überschneidung 079/081
Bestätigt, siehe B10: gleiche Verwechslung, beide im Pool korrektur; 081 verrät 079 und umgekehrt. 079 prüft Wissen (Auswahl, 2×2-Bau), 081 Fehlersuche; der Fragefokus ist verschieden, die Einsicht dieselbe.

## Offene Zweifel

- Lehrplan Klasse 7 für Lage Gerade/Kreis (VT2-071 bis 077) nicht bestätigt; Jahrgangsstufe 8 nicht abrufbar.
- Meine Schema-Einschätzung und die Test-Schwierigkeit (C10) sind Urteile, keine Messung; die Kinder-Erprobung ist unabhängig davon nötig.
- Doppelungsmaß findet nur sprachliche und zahlenmäßige Nähe, keine Aufgaben mit gleichem Rechenweg in anderer Einkleidung.
