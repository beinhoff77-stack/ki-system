# Vorprüfung Welle 1 (Runde 2, nach Urteil 1222) – zahlen.natuerlich und terme.umformen

Stand 29.11.2026, geprüfter Stand `67a9f804`. Umfang: VT2-085 … VT2-133 (zahlen.natuerlich, 7 Lernziele) und VT2-029 … VT2-049 (terme.umformen, 3 Lernziele), je 7 Aufgaben (1 Test, 3 Korrektur, 3 Sicherung) = 70 Aufgaben.
Maßstab: Urteil 1222 (strenger Schema-Begriff), Auftragsblatt `vtest-1/auftrag.md`, Prüfpunkte 1–10 des Prüfauftrags, dazu die neue 5er-Regel (1 Test + 2 Korrektur + 2 Sicherung; unter den 5 höchstens eine Schema-Aufgabe, mindestens 4 verschiedene Denkfiguren, Test = anspruchsvollste, Test und Korrektur prüfen nicht dieselbe Einzelfrage).

Nachrechnung: `vorpruefung_w1_rechnen.py` (eigene Rechnung, exakt mit `Fraction`, wo möglich durch vollständiges Durchprobieren; nicht aus `gegenrechnung.py` übernommen). Ergebnis: **0 Abweichungen** bei 70 Sollantworten; alle Fehlbild-Rechnungen ergeben ihre Antwort, kein Fehlbild gleich der Lösung, jede Lücke hat mindestens ein eigenes Fehlbild, alle `loesung_rechnung` stimmen. Lösbarkeit und Rechnung sind also nicht das Problem, sondern Schema-Anteil, Bestandsnähe und zwei Eindeutigkeitsfehler.

## Urteil

| Einheit | bereit für die Gegenprüfung? | Hauptgründe |
|---|---|---|
| zahlen.natuerlich | **nein** | 6 von 7 Lernzielen mit mehr als zwei Schema-Aufgaben (ziffern_zu_zahlwort sogar 6 von 7, auch der Test); 8 Bestands-Doppelungen nach dem Kern (097, 098, 107, 112, 117, 123, 125, 128, 130); 122 nicht eindeutig; Test 120 nicht die anspruchsvollste |
| terme.umformen | **nein** | 029 (Test) mit negativer Seitenlänge für „jede Zahl x“; alle drei Lernziele mit mehr als zwei Schema-Aufgaben; Test 036 hat wieder den Kern einer Bestandsaufgabe; 039, 033, 047, 048, 049 = Bestand nach dem Kern |

Mit der neuen 5er-Regel und dem Streichvorschlag unten erfüllen **runden_regel** und **runden_sinnvoll** den Maßstab (nach den B-Korrekturen). Alle anderen acht Lernziele brauchen zusätzlich neue oder umgebaute Aufgaben.

### Wie ich gezählt habe (Kalibrierung)
- **S** = sicher Schema: durch Ausrechnen, Umwandeln, Ablesen oder eine bekannte Regel lösbar, auch als Fehler-Detektiv oder Zahlenvergleich verpackt.
- **Z** = Zweifel. Nach Prüfauftrag wird das **als Schema gezählt**. Es bleibt aber eine Einsicht, die man mit Wohlwollen als Verstehen werten kann.
- Offen gesagt: Bei dualsystem und roemisch_schreiben hat das Urteil 1222 auf fast denselben Aufgaben nur 2 Schema gezählt. Ich zähle dort 4 bzw. 5, wenn Z mitzählt. Wo die A-Wertung **nur** wegen Z-Aufgaben fällt, steht das in der Tabelle; dann ist es das schwächste A.

---

## Befunde A (Muss)

**A1 – VT2-029 (Test zusammenfassen): Definitionsbereich.** Laut Text ist der Umfang „für jede Zahl x“ gleich, die Seiten sind (3x + 2) cm, (x + 6) cm und (2x + a) cm. Für x = −1 ist eine Seite −1 cm lang (Skript-Notiz), also derselbe Fehlertyp wie im Urteil 1222 (negativer Umfang). *Vorschlag:* „für jede positive Zahl x“ (bzw. x > 0). Der Koeffizientenvergleich bleibt gültig, die Lösung a = 4 ändert sich nicht.

**A2 – VT2-122 (Korrektur roemisch): nicht eindeutig.** Unter „ohne Subtraktionsregel (es wird nur addiert …)“ ist 1 999 auch MCCCCCCCCCLXXXXVIIII (20 Zeichen) und anders schreibbar. 16 ergibt sich nur, wenn man möglichst wenige Zeichen bzw. immer das größte Zeichen nimmt. *Vorschlag:* „… und jeweils mit möglichst wenigen Zeichen“ ergänzen. Ohnehin Schema; im 5er-Satz besser ersetzen (siehe A8).

**A3 – stellenwert: Schema 3 + 1 Z (086 S, 087 S, 088 S, 090 Z).**
- 087 ist reine Subtraktion: Beide Zahlen (7 777 und 7 007) stehen im Text. Kern wie themen #13/#26/#28/#33 (Ziffer ändert sich → um wie viel ändert sich die Zahl).
- 086 löst man durch 5 000 : 5. Nähe zu themen #22 („In 5 555 hat jede 5 denselben Wert“).
- 088 ist ein Fehler-Detektiv, den das bloße Bestimmen des Stellenwerts löst.

*Vorschlag:* 087 und 090 streichen. 086 ersetzen durch eine Rückwärtsaufgabe, z. B. „In einer Zahl ist die vordere 7 genau 10 000-mal so viel wert wie die hintere 7. Wie viele Ziffern stehen zwischen den beiden Siebenen?“ (3).

**A4 – ziffern_zu_zahlwort: 6 von 7 Schema, Test eingeschlossen.**
- 092 (Test), 093 und 098 heißen jeweils „Zahlwort in Ziffern schreiben, dann zählen bzw. auswählen“: S, S, S, dieselbe Denkfigur dreimal.
- 094 und 097 sind Fehler-Detektive, die richtiges Lesen löst: S, S.
- 096 nennt die Ziffern im Text. Damit ist der Vergleich trivial, und die Abgrenzung („ohne Ziffernschreibweise“) stimmt nicht: S.

Die Denkfiguren kreisen um ein Verfahren (Dreiergruppen bilden); nur 095 ist Verstehen. Bestand:
- **097 = rollend-11 S3-V002**: Dreiergruppen, mittlere (Tausender-)Klasse falsch gesprochen, Zeilensuche. Gleiche Rechnung, gleicher Fehler, gleiche Frage.
- **098 = themen #77/#89**: Zahlwort mit leerer Klasse in Ziffern schreiben.

*Vorschlag:* 093 und 098 streichen; Test und zwei weitere neu mit Einsicht, z. B.:
- Test: „Wie viele Zahlen zwischen einer Million und zwei Millionen liest man ohne das Wort ‚tausend‘?“ (999: 1 000 001 … 1 000 999).
- „Warum hat jede Zahl, deren Zahlwort mit ‚zehn Millionen‘ beginnt, genau acht Stellen?“ als Auswahl, jede Option mit eigenem Urteil.
- 096 ohne Ziffern im Text, mit Zahlwörtern, deren Länge in die Irre führt.

**A5 – strahl_eintragen: Schema 3 + 1 Z (100 S, 101 S, 102 S, 104 Z); Denkfigur „Maßstab cm ↔ Zahl“ dreimal (099, 102, 104).**
- 100: Schrittweite ausrechnen und prüfen.
- 101: 700 + 7 · 50.
- 102: Fehler-Detektiv, den 7 500 : 1 000 · 2 löst.
- 102 fragt dasselbe wie der Test 099 (Entfernung einer Zahl in cm über den Maßstab).

*Vorschlag:* 102 und 104 streichen. 101 als Rückwärtsaufgabe mit Strich/Abstand-Einsicht bauen, z. B. „Zwischen den Strichen 700 und 1 050 liegen genau 6 weitere Striche. Welchen Abstand haben benachbarte Striche?“ (50).

**A6 – runden_regel: Bestand und Schema (109 S, 112 S, 107 Z).**
- **107 Lücke 1 = themen #238** („Wie viele natürliche Zahlen ergeben auf Hunderter gerundet 1 200?“ → 100). Nur die Zahl ist geändert; Lücke 2 ist dieselbe Rechnung eine Stufe gröber.
- **112 = themen #237/#247, rollend-5 K5A-V020** (kleinste bzw. größte Zahl, die auf eine Hunderterzahl rundet), dazu #233/#243. Gleiche Rechnung, gleicher Randfehler, gleiche Frage.

*Vorschlag:* 107 und 112 streichen (siehe Streichvorschlag); danach erfüllt.

**A7 – VT2-117 (Sicherung runden_sinnvoll) = themen #326.** „Fahrkarte rund 20 €, mitgegeben 20 €, Karte kostet 20,40 €, was ist schiefgegangen?“ hat denselben Kern: Durch Runden verschwindet ein kleiner Unterschied, an dem eine Entscheidung „reicht es?“ hängt. Gleiche Einsicht, gleiche Frage, nur andere Zahlen. Dazu B7. *Vorschlag:* streichen.

**A8 – roemisch_schreiben: Schema 3 + 2 Z (121 S, 122 S, 123 S, 120 Z, 125 Z); der Test ist nicht die anspruchsvollste Aufgabe; Bestand; Denkfigur „Regelverstoß erkennen“ dreimal (120, 121, 125).**
- Test 120 nennt die Regel („höchstens dreimal“) selbst, der Verstoß VIIII ist direkt sichtbar. Das Zeichenzählen prüft nur Abzählen. 126 (kleinste Zahl mit sechs Zeichen) und 124 verlangen mehr. Nähe zu themen #381 (MCDXLIIII als Ablenker für 1 444).
- **123 = rollend-5 K5A-V031**: dieselbe Zahl MCMXLIV, dieselben Bausteine M, CM, XL, IV, dieselbe Frage.
- **125 = themen #393**: „99 als IC – was ist falsch?“, also derselbe Fehler (I vor einem zu großen Zeichen) und dieselbe Frage.
- 121 liegt nahe an #390 (XD/LD).

*Vorschlag:* 126 wird Test. 123 und 125 streichen. Neu eine Korrektur und eine Sicherung mit Einsicht, z. B.:
- „Welche Zahl unter 100 spart durch die Subtraktionsregel die meisten Zeichen gegenüber der rein additiven Schreibweise mit möglichst wenigen Zeichen?“ (99: 10 gegen 4 Zeichen, eindeutig).
- „Warum braucht die römische Schrift kein Zeichen für die Null, das Zehnersystem aber schon?“ als Auswahl, jede Option mit eigenem Urteil.

120 entfällt; 121 bleibt die eine Schema-Aufgabe.

**A9 – dualsystem: Bestand und Schema (130 S, 131 S, 128 Z, 129 Z).**
- **130 = rollend-12 R5-V026 + themen #432**: Ziffernfolge 1011/1101 vertauscht (Wert 13 statt 11), Zeilensuche, dieselben Zahlen.
- **128 = themen #450** („Wie viele der Zahlen 1 bis 31 haben genau eine Ziffer 1?“); nur die Zahlenliste ist anders.
- 131 löst man durch 13 − 5; nahe an K5A-V037.

*Vorschlag:* 130 und 131 streichen. 128 ersetzen durch einen Darstellungswechsel mit Entscheidung, z. B. „Eine Zahl hat im Zweiersystem genau 10 Stellen. Wie viele Stellen hat sie im Zehnersystem höchstens?“ (4; Bereich 512 bis 1 023).

**A10 – zusammenfassen: Schema 3 + 3 Z (030 S, 031 S, 032 S, 033 Z, 034 Z, 035 Z); Bestand.**
- 030: gleichartige Glieder erkennen (Routine, nahe themen #11).
- 031: ausrechnen bei x = 2.
- 032: Fehler-Detektiv, den Nachrechnen löst.
- **033 = themen #23** („5x + 4y − T soll zusammengefasst 2x + 7y ergeben“), ebenso #8/#25: fehlende Koeffizienten aus dem Ergebnis.
- 034 löst direktes Einsetzen von x = 1 000 ohne Einsicht.
- 035 nennt das zusammengefasste Ergebnis 4x + y im Text, damit ist die 4 ablesbar (B14).

*Vorschlag:* 031 und 033 streichen. In 035 das Ergebnis nicht vorgeben. In 034 eine unbequeme Zahl wählen (z. B. x = 987 654). 030 durch eine Verstehens-Aufgabe ersetzen (Fehlvorstellung „3x + 2 = 5x“ mit Urteil je Option).

**A11 – minusklammer: Test mit Bestands-Kern, Bestand, Schema (037 S, 041 S, 042 S, 038 Z, 040 Z).**
- **Test 036 = Kern von rollend-13 R8-V006** („Für welche Zahl b gilt 5x − (2x + b) − (x − 3) = 2x − 1 für alle x?“) sowie themen #91 und #88: Parameter per Koeffizientenvergleich nach der Minusklammer, gleicher Vorzeichenfehler. Zwei Parameter statt einem sind nur eine Erweiterung derselben Rechnung. Der Ersatz für die alte Bestands-036 aus Urteil 1222 trifft also wieder Bestand.
- **039 = themen #96** („7x − (3x − 5) = 4x − 5. Was stimmt?“) und #93: Nur das erste Vorzeichen wird gedreht, eine Behauptung wird geprüft.
- 037 und 042 sind Auflösen und Ausrechnen. 041 ist ein Fehler-Detektiv, den Nachrechnen löst.

*Vorschlag:* neuer Test mit Einsicht, z. B. „Um wie viel ist 20 − (x − 5) größer als 20 − x − 5, und hängt der Unterschied von x ab?“ (immer 10: die 5 wird einmal addiert statt abgezogen). 039 und 042 streichen. 037 ersetzen; 041 bleibt die eine Schema-Aufgabe.

**A12 – aequivalenz: Bestand und Schema (045 S, 046 S, 043 Z, 048 Z); Test und Korrektur fragen dasselbe.**
- **047 = themen #233** (Werte für x = 0, 1, 2 → Term), nur andere Zahlen plus ein Einsetzschritt.
- **048 = themen #238** („Für wie viele ganze x zwischen −10 und 10 haben x² und 3x denselben Wert?“), ebenso rollend-13 R8-V010.
- **049 = rollend-11 S3-V032** („4(x + 3) − k(x − 1) und 2x + 14 für jede Zahl x … k“), ebenso #228, K8-V015, R15-V046.
- Test 043 und Korrektur 045 fragen beide „wie viele dieser Terme sind gleichwertig“.
- 046 kann man zweimal ausrechnen, ohne zu sehen, dass das Ergebnis konstant ist.

*Vorschlag:* 045 und 047 streichen; 048 und 049 ersetzen. 046 umbauen zu einer Rückwärtsaufgabe mit Einsicht, z. B. „Welche Zahl muss Mia statt 6 addieren, damit immer 10 herauskommt?“ (14). Für 043 eine Aufgabe mit Einsicht prüfen (siehe B19).

## Befunde B (Soll)

- **B1 – 085:** Die Probe im Lösungsweg schreibt „03 000 wird zu 30 000“, eine Zahl mit führender Null. Das widerspricht 090. Außerdem ist 27 000 genau die Zahl aus themen #10 (dort vorwärts gerechnet). Die Rückwärtsrichtung darf bleiben, die Zahl sollte sich ändern. *Vorschlag:* z. B. Zuwachs 36 000 (d = 4), Probe 104 215 → 140 215.
- **B2 – 091 wird durch 085 verraten:** Derselbe Gedanke (Zuwachs = 9 · Stellenwert), und der Lösungsweg des Tests zeigt ihn vorher. Wird mit dem Streichen von 090 und dem Behalten von 091 hingenommen; besser 091 auf eine andere Verschiebung bauen (z. B. zwei Nullen anhängen, Zuwachs 99 · n).
- **B3 – 093 Fehlbild-Beschreibungen passen nicht zur Rechnung:** „8 − 2“ soll heißen, „die 2 und die 3 der Tausenderklasse“ seien als eine Ziffer gezählt, aber die Tausenderklasse ist 003. „9 − 2“ = „eine Stelle zu viel“ ergäbe 9 − 3 = 6. Entfällt mit dem Streichen.
- **B4 – Warum-Fragen 095 und 105:** Alle falschen Möglichkeiten übernehmen das richtige Urteil aus der Frage („kein richtiger Zahlenstrahl“ bzw. „man liest so“) und unterscheiden sich nur in der Begründung. Wörtlich ist das die verbotene Ablenkerart. *Vorschlag:* Urteil und Begründung in jede Möglichkeit, z. B. „Mias Strahl ist richtig, weil … / falsch, weil …“.
- **B5 – Bauart Absolutwörter:** „immer/nie/stets/niemals“ steht in 14 von 57 falschen, aber nur in 1 von 19 richtigen Möglichkeiten (Skript). In **105** und **110** tragen alle drei falschen ein Absolutwort; die richtige ergibt sich durch Ausschluss. In 115 sind es zwei. Dazu steht die Sammel-Option nur in der richtigen Möglichkeit: 110 („alle drei Fälle“) und 129 („Beide“). *Vorschlag:* Absolutwörter auch in richtige Möglichkeiten (z. B. „nie größer“ wie in 111), Sammel-Optionen auch als Ablenker.
- **B6 – Bauart „Einzelgänger-Urteil“ (neues Muster):** In 039 heißt es dreimal „Nele hat recht“, die richtige ist die einzige mit „irrt sich“. In 117 dreimal „Mia hat recht“, die richtige die einzige mit „unrecht“. Wer das abweichende Urteil wählt, trifft sicher. *Vorschlag:* Urteile verteilen (2 : 2). Beide Aufgaben sind ohnehin zum Streichen vorgesehen; die Regel gilt für Neubauten.
- **B7 – 110 Sprache:** Die Frage ist ein Satzrumpf („… ist im Vergleich zur ursprünglichen Zahl …“), „alle drei Fälle“ wird nicht eingeführt, und die Begründung „es kommt auf die Stelle hinter der Rundungsstelle an“ ist für „gleich“ ungenau (dafür müssen alle folgenden Stellen 0 sein). *Vorschlag:* Frage als ganzer Satz mit den drei Fällen; Begründung „es kommt auf die Stellen hinter der Rundungsstelle an“.
- **B8 – 114 Lehrplan:** „1 000 : 36 (etwa 27,8)“: Dezimalbrüche kommen erst in M6. *Vorschlag:* „1 000 : 36 = 27 Rest 28“.
- **B9 – 116:** Kern wie themen #308/#311/#314 (rund 9 000 Zuschauer → höchstens/mindestens), nur mal 15. Außerdem fragt der Test 118 dasselbe (Rundungsbereich übernehmen und weiterrechnen), und 118 verrät 116. Streichen.
- **B10 – 119:** nahe an rollend-11 S3-V005 (einzeln runden gegen genaue Summe, Beträge 14xx). Die Einsicht ist gleich, die Denkleistung (Erklärung wählen statt Betrag) eine andere, also darf sie bleiben. *Vorschlag:* andere Größenordnung (z. B. 3 460, 3 420, 3 440, 3 470 auf Tausender), damit die Zahlen nicht nach Bestand aussehen.
- **B11 – 126 Voraussetzung:** „nach den üblichen Regeln“ steht ohne die Regel. Ohne „höchstens dreimal“ wäre 19 = XVIIII schon sechsstellig. *Vorschlag:* Regeln wie in 121 ausschreiben.
- **B12 – dualsystem: Denkfiguren 127, 132 und 133 kreisen um „n Stellen ↔ 2ⁿ Werte“;** 131 liegt nahe an K5A-V037, 132 an #438 (5 Lampen, größte Zahl 31). Mit dem Ersatz für 128 (A9) bleiben 4 verschiedene Figuren; 132 und 133 nicht noch näher zusammenbauen.
- **B13 – weitere Bestandsnähe (gleiche Einsicht, andere Denkleistung, darf bleiben, aber in der Gegenprüfung angreifbar):**
  - 031 (x und x² zu x³ zusammengefasst) ↔ #27
  - 030 ↔ #11
  - 038 ↔ #88
  - 040 ↔ #71/#75
  - 043 ↔ #211
  - 044 ↔ #237 (Rahmenplättchen, zwei Zählterme)
  - 086 ↔ #22
  - 094 ↔ S3-V002/R5-V006
  - 121 ↔ #390
- **B14 – 035:** Das zusammengefasste Ergebnis 4x + y steht im Text, die Antwort 4 ist ablesbar (siehe A10).
- **B15 – Fehlbild-Beschreibungen in terme:**
  - 033 Lücke 1: Rechnung „5 − 2“, Beschreibung „die 3 des Ergebnisses eingesetzt“ (dann wäre die Rechnung „3“). Lücke 2: Die Beschreibung nennt die Rechnung „−2 + 1“ nicht.
  - 041 Lücke 2: Rechnung „4 − 2 − 1“ zieht auch das a ab; die Beschreibung („die 2a abgezogen statt addiert“) ergäbe 4 − 2 + 1 = 3.
  - 037: Fehlbild 11 heißt nur „eine Zahl falsch verrechnet“.
  - 104: Fehlbild 40 mit „… oder …“.
- **B16 – Denkfigur über die Einheit terme.umformen:** Der Koeffizientenvergleich „für jedes x gleich → Parameter“ steckt in 029 (Test), 036 (Test), 049 und (als Einsetzen) 038. Zwei von drei Tests haben dieselbe Denkfigur. *Vorschlag:* Neuer Test für minusklammer ohne Parameter (siehe A11).
- **B17 – 096:** Die Ziffern stehen in Klammern im Text, die Abgrenzung behauptet das Gegenteil (siehe A4).
- **B18 – 089 und 129:** Die Null-Platzhalter-Einsicht steht in zwei Lernzielen (stellenwert 089, dualsystem 129). Das ist zulässig, aber im 5er-Satz von dualsystem ist 129 dann die eine Schema- bzw. Z-Aufgabe; sie nicht noch weiter vereinfachen.
- **B19 – Test 043:** vereinfachen und zählen (Z); erst 044 (Modell) und 049 verlangen eine Einsicht. Zählt man 043 als Schema, ist der Test nicht die anspruchsvollste Aufgabe. *Vorschlag:* Test mit Entscheidung, z. B. drei Zählweisen für ein neues Muster, von denen eine nur für n ≥ 2 stimmt.

## Befunde C (Kann)

- C1 – 089: Die Ablenker 0 („Null zählt als ein Einer“) und 1 („mal 0 → 7 090 = 0“) sind wenig plausible Fehlvorstellungen.
- C2 – 095: Die Erklärung im Fehlbild 1 widerlegt „tausend in die Mitte“ nur über ein Beispiel ohne Einerklasse. 105: Das Fehlbild 3 widerlegt die Möglichkeit nicht („der Abstand von 0 bis 100 ist hier der kleinste“).
- C3 – 120: Die Abgrenzung ist sachlich falsch („die römische Subtraktionsschreibweise wird nicht verwendet“, obwohl CD und XL vorkommen).
- C4 – 118 und 116 prüfen den Rundungsbereich, eher Inhalt von runden_regel als von runden_sinnvoll. Vertretbar, weil sie im Sachkontext stehen.
- C5 – Eine Ziffer steht nur in der richtigen Möglichkeit: 096, 105. Umgekehrt in 129.
- C6 – 098: doppelte Frage („Welche Zahl wird gesprochen …? Welche Ziffernfolge ist richtig?“). Die Möglichkeiten sind Zahlen, die Fehlbilder haben aber keine `rechnung` (Auftragsblatt Abschnitt 5).
- C7 – 047 passt eher zu „Term aufstellen“ als zu Äquivalenz.
- C8 – 133: `loesung_rechnung` „8 − 1“ ohne Bezug zum Lösungsweg; Fehlbild 6 vage beschrieben.
- C9 – 106 ↔ themen #253 (Zehner- und Hunderterrundung gemeinsam) und 108 ↔ #313/#324: gleiche Einsicht, andere Denkleistung, zulässig.
- C10 – 042 löst eine lineare Gleichung (12x + 11 = 35). Über die Umkehraufgabe geht das mit M6-Wissen, im Lernbereich Terme aber Randstoff.

---

## Tabelle je Lernziel

S = sicher Schema, Z = Zweifel (zählt als Schema). „5er ok?“ = Maßstab nach dem Streichvorschlag ohne weitere Neubauten.

| Lernziel | Schema (S / Z) | Anzahl | Denkfiguren (verschieden) | Test ok? | Streichen: Korrektur / Sicherung | 5er ok? | danach noch nötig |
|---|---|---|---|---|---|---|---|
| stellenwert | 086, 087, 088 / 090 | 4 | 6 (085≈091) | ja (085), B1 | **087 / 090** | nein (086, 088 = 2 Schema) | 086 durch Rückwärtsaufgabe ersetzen (A3) |
| ziffern_zu_zahlwort | 092, 093, 094, 096, 097, 098 / – | 6 | 4; 092/093/098 gleich | **nein** (092 Schema) | **093 / 098** | nein (4 Schema) | neuer Test + 2 neue, 096 umbauen (A4) |
| strahl_eintragen | 100, 101, 102 / 104 | 4 | 5; Maßstab 3× | ja (099) | **102 / 104** | nein (100, 101 = 2) | 101 als Rückwärtsaufgabe (A5) |
| runden_regel | 109, 112 / 107 | 3 | 6 (107≈112) | ja (106) | **107 / 112** | **ja** (Schema 109; 5 Figuren) | B5/B7 an 110 |
| runden_sinnvoll | 113 / 116 | 2 | 6 (116≈118) | ja (118) | **116 / 117** | **ja** (Schema 113; 5 Figuren) | B8 an 114, B5 an 115, B10 |
| roemisch_schreiben | 121, 122, 123 / 120, 125 | 5 | 5; Regelverstoß 3× | **nein** (120 < 124/126) | **123 / 125** | nein | 126 als Test, 2 neue (A8), 120 entfällt |
| dualsystem | 130, 131 / 128, 129 | 4 (A nur mit Z) | 5; 127/132/133 nahe | ja (127) | **130 / 131** | nein (128 Z + Bestand, 129 Z) | 128 ersetzen (A9) → dann ja |
| zusammenfassen | 030, 031, 032 / 033, 034, 035 | 6 | 7 | ja (029) nach A1 | **031 / 033** | nein (030, 032 + 034/035 Z) | 035 und 034 umbauen, 030 ersetzen (A10) |
| minusklammer | 037, 041, 042 / 038, 040 | 5 | 7 | **nein** (036 Bestands-Kern) | **039 / 042** | nein | neuer Test, 037 ersetzen (A11) |
| aequivalenz | 045, 046 / 043, 048 | 4 | 6 (043≈045) | Zweifel (043 Z), B19 | **045 / 047** | nein (048, 049 Bestand; 046 S) | 048/049 ersetzen, 046 umbauen (A12) |

Zur Einzelfrage zwischen Test und Korrektur: Diese Paare fallen mit dem Streichvorschlag weg: 099/102, 118/116 (Korrektur 116 gegen Test 118) und 043/045. Bei stellenwert ist 087 die Vorwärtsform des Tests 085 und fällt ebenfalls weg.

---

## Protokoll je Aufgabe

Spalten: Kennung · Pool · Lösung (eigen = JSON) · Klasse (S/Z/V) · Denkfigur · Bestand nach dem Kern · Befund.

### zahlen.natuerlich
| Kennung | Pool | Lösung | Kl. | Denkfigur | Bestand | Befund |
|---|---|---|---|---|---|---|
| 085 | test | 3 ✓ eindeutig | V | Ziffertausch → Zuwachs 9 000·d rückwärts | #10 Umkehrung, gleiche Zahl 27 000 | B1 |
| 086 | korr | Option 1 ✓ | S | Wertverhältnis gleicher Ziffern | nahe #22 | A3, B13 |
| 087 | korr | 770 ✓ | S | Wegfall von Stellenwerten | Kern #13/#26 | A3, streichen |
| 088 | korr | [2, 60 000] ✓ | S | Stelle ↔ Stellenwert (Fehler-Detektiv) | – | A3 |
| 089 | sich | Option 3 ✓ | V | Null als Platzhalter | #21 andere Denkleistung | C1 |
| 090 | sich | 4 ✓ (406, 460, 604, 640) | Z | führende Null, Zählen | – | streichen |
| 091 | sich | 450 ✓ | V | Null anhängen = ·10, rückwärts | S3-V001 andere Leistung | B2 |
| 092 | test | [9, 7] ✓ | S | Zahlwort → Ziffern, Stellen zählen | K5A-V007 nahe | A4 |
| 093 | korr | 5 ✓ | S | Zahlwort → Ziffern, Nullen zählen | #77/#89 nahe | A4, B3, streichen |
| 094 | korr | Option 2 ✓ | S | Klasse beim Lesen falsch (Fehler-Detektiv) | S3-V002/R5-V006 nahe | A4, B13 |
| 095 | korr | Option 0 ✓ | V | Aufbau des Zahlworts aus Klassen begründen | #96 nahe | B4, C2 |
| 096 | sich | Option 1 ✓ | S | Vergleich über Stellenzahl (Ziffern gegeben) | #87 gleiche Zahl 2 000 300 | A4, B17, C5 |
| 097 | sich | [3, 10] ✓ | S | Tausenderklasse falsch gesprochen (Fehler-Detektiv) | **= S3-V002** | A4 |
| 098 | sich | Option 3 ✓ | S | Zahlwort mit leerer Klasse → Ziffern | **= #77/#89** | A4, C6, streichen |
| 099 | test | [11, 3 000] ✓ | V | Maßstab aus zwei Marken ohne Nullpunkt | – | – |
| 100 | korr | Option 2 (800) ✓ eindeutig | S | Schrittweite prüfen | #174 nahe | A5 |
| 101 | korr | 1 050 ✓ | S | Striche/Abstände | #164 nahe | A5 |
| 102 | korr | [3, 15] ✓ | S | Maßstab (Fehler-Detektiv), gleiche Einzelfrage wie Test | R5-V010 anderer Fehler | A5, streichen |
| 103 | sich | 1 (nur 600) ✓ | V | zwei Teilungen, gemeinsame Striche | – | – |
| 104 | sich | 39 (41 … 79) ✓ | Z | Maßstab → Zahlbereich, Rand ausgeschlossen | – | A5, B15, streichen |
| 105 | sich | Option 0 ✓ | V | gleiche Strecke = gleicher Unterschied | – | B4, B5, C2, C5 |
| 106 | test | 10 ✓ (1–4, 95–100) | V | zwei Rundungen über einen Bereich | #253 andere Leistung | C9 |
| 107 | korr | [100, 1 000] ✓ | Z | Breite des Rundungsbereichs | **= #238** | A6, streichen |
| 108 | korr | 50 ✓ (über 0 … 99 999 geprüft) | V | größte Rundungsabweichung | #313/#324 andere | C9 |
| 109 | korr | [2, 4 900] ✓ | S | Rundungsrichtung (Fehler-Detektiv) | #249/R5-V014 anderer Fehler | – (die eine Schema-Aufgabe) |
| 110 | sich | Option 1 ✓ (alle drei Fälle vorhanden) | V | immer/manchmal/nie | #250 andere | B5, B7 |
| 111 | sich | Option 3 ✓ (Monotonie geprüft) | V | Reihenfolge bleibt erhalten, Gleichheit möglich | – | – |
| 112 | sich | Option 2 ✓ (1 950 … 2 049) | S | Grenzen des Rundungsbereichs | **= #237/#247/K5A-V020** | A6, streichen |
| 113 | sich | [108, 48] ✓ | S | Schätzfehler beim Produkt | K5A-V025 nahe | – (die eine Schema-Aufgabe) |
| 114 | korr | [27, 28] ✓ | V | gleiche Rechnung, Rundungsrichtung nach Sachlage | K5A-V027 Teil B | B8 |
| 115 | korr | Option 2 ✓ | V | Wahl der Rundungsstelle = Genauigkeit | – | B5 |
| 116 | korr | [63 750, 65 235] ✓ | Z | Rundungsbereich · Preis | #308/#311 + ·15 | B9, streichen |
| 117 | sich | Option 3 ✓ | V | Runden ungeeignet für Entscheidungen | **= #326** | A7, B6, streichen |
| 118 | test | [8, 11] ✓ (25 … 34 m) | V | Rundungsbereich + Rest | #321 andere | C4 |
| 119 | sich | Option 1 ✓ (Summe 5 830, Fehler 1 830) | V | gleichgerichtete Rundungsfehler addieren sich | S3-V005 nahe | B10 |
| 120 | test | [4, 10, 7] ✓ | Z | Regelverstoß VIIII, Zeichen zählen | #381 nahe | A8, C3 |
| 121 | korr | Option 0 (VC) ✓ einzige ungültige | S | Regelverstoß erkennen | #390 nahe | A8, B13 |
| 122 | korr | [16, 7] nur bei „möglichst wenigen Zeichen“ | S | Zeichen sparen durch Subtraktion | – | **A2**, A8 |
| 123 | korr | [1 000, 900, 40, 4] ✓ | S | Bausteine lesen | **= K5A-V031** | A8, streichen |
| 124 | sich | 18 ✓ (1 … 50 durchgezählt) | V | Paare über Endziffer und Zehner zählen | #395 andere | – |
| 125 | sich | Option 1 ✓ | Z | Regelverstoß I vor M | **= #393** | A8, streichen |
| 126 | sich | 28 ✓ (kleinste mit 6 Zeichen) | V | Zeichenzahl über viele Zahlen suchen | #383/#391 andere | B11 (als Test vorgeschlagen) |
| 127 | test | 11 ✓ (21 … 31) | V | Stellenzahl → Wertebereich | #438 nahe | – |
| 128 | korr | 3 ✓ (32, 64, 128) | Z | Zweierpotenz = eine 1 | **= #450** | A9 |
| 129 | korr | Option 3 ✓ | Z | führende Null | – | B5, B18, C5 |
| 130 | korr | [2, 11] ✓ | S | Stellenwerte zuordnen (Fehler-Detektiv) | **= R5-V026 + #432** | A9, streichen |
| 131 | sich | 8 ✓ | S | Wert der vordersten Stelle | K5A-V037 nahe | A9, streichen |
| 132 | sich | 32 ✓ | V | Anzahl darstellbarer Zahlen | #438 nahe | B12 |
| 133 | sich | 7 ✓ | V | lauter Einsen rückwärts | #436 nahe | B12, C8 |

### terme.umformen
| Kennung | Pool | Lösung | Kl. | Denkfigur | Bestand | Befund |
|---|---|---|---|---|---|---|
| 029 | test | 4 ✓ | V | zwei Umfangsterme gleichsetzen, Koeffizientenvergleich | K8-V002/R8-V002 andere | **A1**, B16 |
| 030 | korr | 3 ✓ | S | gleichartige Glieder erkennen | #11 nahe | A10, B13 |
| 031 | korr | 34 ✓ | S | Gegenbeispiel durch Einsetzen | #27 gleicher Fehler | A10, streichen |
| 032 | korr | Option 2 ✓ | S | Vorzeichenfehler y-Glied (Fehler-Detektiv) | R15-V034 anderer Fehler | – (die eine Schema-Aufgabe) |
| 033 | sich | [2, 1] ✓ eindeutig | Z | fehlende Koeffizienten rückwärts | **= #23 (#8, #25)** | A10, B15, streichen |
| 034 | sich | 6 ✓ | Z | x-Glieder heben sich auf | – | A10 |
| 035 | sich | 4 ✓ | Z | Koeffizient als Zuwachs je Schritt | – | A10, B14 |
| 036 | test | [5, 4] ✓ eindeutig | V | zwei Parameter nach der Minusklammer | **Kern R8-V006, #91, #88** | A11, B16 |
| 037 | korr | 7 ✓ | S | x fällt beim Auflösen weg | – | A11, B15 |
| 038 | korr | 6 ✓ | Z | Parameter durch Einsetzen | #88 nahe | A11, B13 |
| 039 | korr | Option 0 ✓ | Z | Behauptung mit Zahlprobe widerlegen | **= #96/#93** | A11, B6, streichen |
| 040 | sich | 3 ✓ (C, D, E) | Z | gleichwertige Formen zählen | #71/#75 nahe | A11, B13 |
| 041 | sich | [2, 7, −4] ✓ | S | Plus- gegen Minusklammer (Fehler-Detektiv) | K8-V009/R15-V040 anderer Fehler | B15 (die eine Schema-Aufgabe) |
| 042 | sich | 2 ✓ | S | auflösen, dann Gleichung rückwärts | – | A11, C10, streichen |
| 043 | test | 4 ✓ (A-B, A-C, B-C, D-E) | Z | Terme vereinfachen, Gruppen zählen | #211 nahe | A12, B19 |
| 044 | korr | [2, 31] ✓ | V | zwei Zählweisen eines Musters | #237 nahe | B13 |
| 045 | korr | 3 ✓ (T3, T4, T5) | S | Umformungskette prüfen, gleiche Einzelfrage wie Test | – | A12, streichen |
| 046 | korr | [3, 3] ✓ | S | Zahlenrätsel, Ergebnis konstant | – | A12 |
| 047 | sich | 34 ✓ | V | Term aus Wertetabelle | **= #233** | A12, C7, streichen |
| 048 | sich | [2, 15] ✓ (x = 2, 3) | Z | Übereinstimmung an Stellen ≠ Gleichwertigkeit | **= #238 / R8-V010** | A12 |
| 049 | sich | 4 ✓ | V | Parameter im Koeffizienten | **= S3-V032 (#228, K8-V015, R15-V046)** | A12, B16 |

---

## Zahlen
- A (Muss): **12**. 2 Einzelaufgaben (029 Definitionsbereich, 122 Eindeutigkeit) und 10 Lernziel-Befunde (Schema-Überzahl, Bestand, Test).
- B (Soll): **19**. C (Kann): **10**.
- Bestands-Doppelungen nach dem Kern: 097, 098, 107, 112, 117, 123, 125, 128, 130 (natürliche Zahlen), 033, 036 (Test), 039, 047, 048, 049 (Terme).
