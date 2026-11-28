# Korrektur nach der Vorprüfung (Runde 15)

Grundlage: `vorpruefung.md`. Nach der Korrektur läuft `bauen.py` mit `OK`, `vorrat_pruefen` meldet 0 in allen Gruppen, die Doppelungsprüfung gegen den Bestand findet nichts. Zwei neue feste Proben in `bauen.py`: (1) Bei jeder Zahlaufgabe mit `toleranz` liegt kein Fehlbild innerhalb Soll ± Toleranz (inklusiv); (2) Lückenwege dürfen nicht zwei Lücken in beliebiger Reihenfolge füllbar lassen (Muster „① und ②“ im Text wird abgelehnt; ausgenommen die Formulierung „zwischen ① und ②“ in V128, dort legen die Gleichungen ①² = 9 und ②² = 16 die Rollen fest).

Alle 26 Lückenwege wurden von Hand auf vertauschbare Lücken gelesen: nur V140 (②/③) war betroffen, V128 wurde zusätzlich mit „für positive Zahlen“ abgesichert.

| Kennung | Befund | Was geändert (alt → neu) bzw. warum nicht |
|---|---|---|
| V120 | A: Toleranz 0,1 wertet 9,3 als richtig | `toleranz` entfernt (Soll 9,2 exakt gerundet) |
| V140 | A: Lücken ② ③ vertauschbar | Text „② ist die positive und ③ die negative Lösung“ |
| V143 | A: Fehlerzeile mehrdeutig | Neu gefasst, 4 Zeilen, genau Zeile 3 falsch: Zeile 1 „alles auf eine Seite“, Zeile 2 „6x ausklammern“ (beide richtig), Zeile 3 „nur der Faktor x − 3 muss null sein“ (falsch, Faktor 6x übersehen), Zeile 4 folgt daraus. Lösungsweg nennt Nullprodukt mit beiden Faktoren, Probe x = 0. Regel `id.algebra.hoeherer_grad` bleibt |
| V022 | B | „natürliche Zahl“ in den Text |
| V031 | B | Fehlbildtext: „bei (2⁹)² die Hochzahlen addiert (2¹¹) und das Teilen durch 2¹⁰ vergessen“ (Wert 2048 bleibt) |
| V059 | B | Fehlbildtext: „vom Vollwinkel 360° statt von 180° gerechnet“ |
| V085 | B | Fehlbildtext: „nur 13 − 3 gerechnet und die Grenzen nicht beachtet“ (Wert 10) |
| V114 | B | 130: „0,13 m in Millimeter statt in Zentimeter umgerechnet“; 1,3: „mit 10 statt mit 100 in Zentimeter umgerechnet“ |
| V153 | B | Text: „bei −b das Vorzeichen falsch gesetzt (9 statt −9) und durch 4 geteilt“ (Wert 12) |
| V193 | B | Text: „die einstellige 9 und die 99 (Ziffernsumme 18) mitgezählt“ |
| V195 | B | „Vielfachen von 6 zwischen 1 und 60 (60 eingeschlossen)“, ebenso die Vielfachen von 4 |
| V003/V011 | C: sehr ähnlich | V011 umgebaut: Fähre nach Sardinien, 480 €, +12 % dann +5 %; Sollwert 564,48 €, Fehlbilder 561,60 / 537,60 / 542,60. V003 unverändert |
| V202/V203 | C: gleiche Zahlen | V203 umgebaut: Therme, 55 % Frauen, 44 % Sauna, 33 % beides, Sollwert 0,6; Fehlbilder 0,75 / 0,1815 / 0,22. V202 unverändert |
| V054/V055 | C: Achteck doppelt | V054: Sechseck und Zwölfeck, Soll 6 / 12 / 18, Fehlbilder 3 / 6 / 72. V055 unverändert |
| V033 | C | Text: „alle Glieder zu 14a zusammengefasst, b nicht mehr beachtet“ |
| V038 | C | Text: „x = 2 beim falschen Glied eingesetzt: 7 + 9 · 2 statt 7 · 2 + 9“ |
| V066 | C | Text: „nur die 20 halbiert, ohne die Gleichung zu lösen“ |
| V075 | C | Fehlbild −65 ersetzt durch 100 („Nebenwinkel von α statt von δ“); 245 bleibt |
| V089 | C | Frage: „α = 35° (bei A) und β = 70° (bei B)“; Option 4 erklärt „70° gehört zu β bei B“ |
| V103 | C | Text: „x-Glieder beider Seiten zu 2x zusammengefasst und dann 2 · 11 − 9 + 13 gerechnet“ |
| V105 | C | Text: „nach dem Zusammenfassen stehen links 10 und rechts 13, das ist nie gleich“ |
| V108 | C | Text: „Kims Fahrzeit statt Alex' Fahrzeit angegeben“ |
| V116 | C | Text: „… und gerundet (√343 ≈ 18)“ |
| V127 | C | „√(2,25)“ in Frage und Lösungsweg |
| V128 | C | „Für positive Zahlen gilt ①² = 9 und ②² = 16“ |
| V188 | C | Optionen 110° und 160° (Winkel über 90°) ersetzt durch 45° und 50°; Probe prüft auch diese |
| V121 | C: Form | nicht geändert: Form `verfahren_waehlen` mit Tätigkeit `begruenden` ist die im System vorgesehene Auswahlform für Begründungen |
| V126, V180 | C: Stufe 1 zählend | nicht geändert: jeweils Auswahl auf Stufe 1 (erkennen), die Etappe hat mindestens eine weitere zählende Aufgabe auf Stufe 2 oder 3; Stufe-1-Zähler sind erlaubt |
| V045, V131 | C: Form | nicht geändert: Umkehren ist hier der Rückweg Antwort → Ausgangsgröße (V045 Behauptung prüfen, V131 Rechteck mit neuer Länge → Breite); Einordnung vertretbar |
| `toleranz` allgemein | C | Konvention: Toleranz höchstens eine Einheit der letzten gefragten Stelle; durch die neue Probe in `bauen.py` darf kein Fehlbild darin liegen |
| V130, V131, V133 | Regel `id.zahlen.hoch_zurueck` trägt nicht | Regel entfernt, jetzt „ohne Regel“ mit Begründung (Heron-Rechenschritt, Flächenerhaltung, Wurzelgesetze); `regeln-zuordnung.md`, `regeln.py` und README nachgeführt: 176 Aufgaben mit, 31 ohne Regel |
| V207 | Lehrplan-Zweifel (Unabhängigkeit) | ersetzt durch Fehler-Detektiv zur bedingten Wahrscheinlichkeit (P(P | K) mit P(K | P) verwechselt, Kinder im Urlaubsclub); Fehlerzeile 3, Regel `id.daten.anteil` mit Zweifel |
| V205 | Lehrplan-Zweifel (Rückschluss) | nicht geändert: gerechnet mit absoluten Häufigkeiten in der Vierfeldertafel, ohne Formel von Bayes; die Etappe `rueckschluss` gehört zur Einheit |
| V013/V014 | Lehrplan-Zweifel (Zinseszins in Klasse 7) | nicht geändert: Zinseszins kommt im Bestand dieser Einheit (`bruch.prozent_grundwert`) bereits vielfach vor, die Etappe `formel` gehört zur Einheit |
| V138/V139 | Lehrplan-Zweifel (Irrationalitätsbeweis) | nicht geändert: eigene Etappe `irrational_beweis` der Klasse-9-Einheit; nach meiner Kenntnis steht die Irrationalität von √2 im Lehrplan Klasse 9. V138 ist als Begründung geführt, V139 als Fehler-Detektiv |

## Offene Zweifel

- Lehrplan: Ich konnte den bayerischen LehrplanPLUS (G9) hier nicht im Wortlaut einsehen; die Entscheidungen zu V205, V013/V014 und V138/V139 stützen sich auf die vorhandenen Etappen der Einheiten im Repo und mein Wissen. Wer sicher gehen will, prüft diese vier Aufgaben gegen den Lehrplan; sie lassen sich ohne Folgen herausnehmen (jede Etappe hat weitere zählende Aufgaben).
- Regel-Kennung bei Sinus, Kosinus und Tangens (7 Aufgaben) bleibt Teilregel mit Zweifel; Entscheidung beim Katalog.
- `auswahl.md` weiterhin nachträglich angelegt; die Klasse-7-Auswahl folgt dem Kriterium „in R8/9/10/14 nicht bedient“.
