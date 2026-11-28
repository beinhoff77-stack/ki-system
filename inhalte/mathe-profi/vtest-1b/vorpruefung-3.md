# Dritte Vorprüfung vtest-1b (Stand nach Commit 51ff5bb0, 119 Aufgaben, 17 Lernziele)

Werkzeug: `vorpruefung_rechnen_3.py` (eigene exakte Neurechnung aus den Angaben im Text, je Möglichkeit ein Wahrheitswert, Fehlbild-Rechnungen, Lücken-Abdeckung). Es wurde nichts an Aufgaben geändert. Bestandssuche: Wortsuche in `inhalte/themen` und `mathe-profi/rollend-*` (lexikalisch, danach von Hand gelesen), also eine Mindestmenge.

## Urteil

**Nach kleiner Korrektur einspielbar:** Alle 119 Lösungen, 409 Fehlbilder und alle Auswahl-Plätze rechnen richtig (0 Abweichungen, jede Lücke hat ein Fehlbild, kein Fehlbild gleicht der Lösung), aber 2 neue Bestandsklone (117, 054), 1 Dreieck-Klon (096) und `vorsilben_klein` mit 5 von 7 Schema-Aufgaben müssen vorher ersetzt werden (4 A-Befunde).

## Fakt und Einschätzung

- Fakt (gerechnet): Lösungen, Fehlbilder, Auswahl (25 Aufgaben rechnerisch; 10 rein begründet: 020, 032, 034, 041, 062, 069, 084, 091, 105, 118, von Hand je eine richtige Möglichkeit bestätigt), Eindeutigkeit der Texte, keine Lösung (>9) im eigenen Text.
- Fakt (Quelle: Bestandstext): Treffer unten.
- Einschätzung (von Hand): Schema/Verstehen, Denkfiguren, „Kern gleich“. Regel: Schema = Rezept, reine Umrechnung, Fehler-Detektiv mit Verrechner oder Rezeptfehler; Verstehen = Begründen, Fehlvorstellung, Rückwärts, Darstellungswechsel mit Einsicht, Transfer, Herleiten.
- Geprüft und in Ordnung: 022 (24), 029 (18: ohne k = 0 Scheinlösung und k = 4 keine), 036 (18: nur b = −1), 050 ([−7, 5]), 043, 060 (jetzt ohne beide Ergebnisse im Text), 080, 105 (genau eine Aussage als Aussage richtig, die anderen haben falsche Folgerung). Kein Ablenker mit richtiger Folgerung und nur falscher Begründung gefunden (091 [2] fragt ausdrücklich nach der Begründung).

## Befunde A (Muss)

| Kennung | Beleg | Vorschlag |
|---|---|---|
| A1 VT1B-117 | Bestand: „Ein Quadrat hat 10 cm Seitenlänge. Jede Seite wird um 10 % länger. Um wie viel Prozent wächst der Flächeninhalt?“ Gleiche Zahlen (10, 10 %, 121, 21 %), gleiche Einsicht; neu ist nur die Fehler-Detektiv-Hülle. | Andere Zahlen und anderen Kern (z. B. Seite 25 % länger, Rückwärts: Fläche wächst um 44 %). |
| A2 VT1B-054 | Bestand: „Ben sagt: ‚10⁻⁴ ist größer als 10⁻², weil 4 größer ist als 2.‘ Was stimmt?“ Gleiche Fehlvorstellung, gleiche Form; nur Basis 2 und Exponenten −3/−4. (Die Vorprüfung 2 meldete „Muster“, die Ersatzaufgabe ist ein neuer Klon.) | Ersetzen, z. B. Gegenbeispiel zu „je größer die Hochzahl, desto kleiner die Potenz“ mit Basis kleiner 1 weglassen; oder Vergleich zweier Potenzen mit verschiedenen Basen (2⁻⁵ gegen 3⁻³). |
| A3 VT1B-096 | Bestand: „Rechteck (12 cm lang, 5 cm breit), Dreieck mit Grundseite untere Seite, Spitze auf der oberen. Wie groß ist die Fläche außerhalb?“ Gleiches Rechteck, gleiche Einsicht (Spitze egal, Hälfte). | Anderes Rechteck und anderer Zusatz (z. B. Spitze außerhalb des Rechtecks, Fläche gegeben, Höhe gesucht). |
| A4 `vorsilben_klein` (078 bis 084) | Schema in 5 von 7: 078 (Faktor, dann Einheit), 080 (nm in mm als a · 10ⁿ), 081 (mg in µg, teilen; Bestand ähnlich „Blutkörperchen 7,5 µm auf 3 mm“), 082 (Fehler-Detektiv mit Potenzquotient), 083 (µm in cm). Nur 079 und 084 verlangen Einsicht, und beide tragen dieselbe Denkfigur (Maßzahl gegen Einheit). A5 der Vorprüfung 2 ist nur äußerlich geschlossen. | Mindestens 078 (Test), 081, 083 durch Einsichtsaufgaben ersetzen (Größe ohne Umrechnen vergleichen, Rückwärts „welche Vorsilbe“, Fehlvorstellung „kleiner Einheit, kleinere Zahl“ als Fehler-Detektiv, Skalierung 10ᵏ-fach). |

## Befunde B (Soll)

| Kennung | Beleg | Vorschlag |
|---|---|---|
| B1 Schema über zwei | Schema-Tabelle unten: prozentwert 3 (002, 006, 007), verhaeltnis 3 (043, 047, 049), gross_wissenschaftlich 3 (065, 068, 070), vergleichen_pruefen 3 (085, 086, 088). | Je Lernziel eine Aufgabe in Einsicht umbauen (z. B. 007 als Begründung Bruch gegen Prozent, 047 als Auswahl-Fehlvorstellung Außen/Innen, 065 als Rückwärts, 086 als „welche gleich, warum“). |
| B2 Denkfigur über zweimal | grundwert „Grundwert = Teil : Satz“ (009, 013, 014); definitionsmenge „Nenner = 0 setzen“ (025, 026, 027); verhaeltnis „Teile-Ansatz k“ (045, 048, 049); gross_wiss. „Vorfaktor in [1; 10) herstellen, Exponent ausgleichen“ (064, 066, 069, 070); negativer_exponent (Zehner) „Stellen ↔ Exponent“ (071, 075, 076); vergleichen_pruefen „Exponenten angleichen“ (085, 087, 088, 089); rueckwaerts „h = A : g“ (099, 103, 104). Folge: gross_wiss. und vergleichen_pruefen haben nur 4 verschiedene Figuren (README sagt 6). | Je eine Aufgabe pro genannter Gruppe ändern; README-Tabelle neu zählen. |
| B3 Bestand, Kern gleich | 049: Bestand „a : b = 2 : 3 und b : c = 4 : 5, gib a : b : c an“ (gemeinsames Glied). 035: Bestand „500 ml Saft Sirup : Wasser = 1 : 4, wie viel Sirup dazugeben, damit 1 : 2“ (Zugießen bis zum Mischungsverhältnis). 009: Bestand „88 Kinder sind 20 % aller Kinder, wie viele hat die Schule“ (nur „ungefähr“ und Auswahl neu). 052: Bestand „Wie viele Zehntausendstel sind 7/16?“ (auf 10 000 erweitern). 057: Bestand „Du sollst 2⁻³ + 2⁻³ berechnen. Welcher Weg ist richtig?“. 039: Bestand „Für welche Zahl c hat 2/(x − 1) = c keine Lösung?“ (anderer Mechanismus, gleiche Fragenart). | 049, 035, 009 ersetzen; 052, 057, 039 prüfen (Hinweis in README). |
| B4 VT1B-002 | B16 der Vorprüfung 2 offen: Gefragt ist weiter nur „12 % von 75 €“; Bens Weg ändert die Antwort nicht. | Fragen, welcher Weg schneller ist und warum beide dasselbe geben, oder Zahl so wählen, dass nur ein Weg im Kopf geht. |

## Befunde C (Kann)

| Kennung | Beleg | Vorschlag |
|---|---|---|
| C1 Fehlbild-Beschreibung | 027 Fehlbild „drei Nenner im Text“ (es sind zwei); 085 Fehlbild 1 „Exponent −6 der größte“ (größter ist −4, Lücken 1 und 2); 043 Lücke 3 Fehlbild 1 („beide Glieder durch 12 geteilt, die 6 vergessen“ ergibt nicht 6/6); 022 Fehlbild 2 („die Null“ gehört nicht zur Antwort 2). | Texte anpassen. |
| C2 Grenzfälle Schema | grundwert (009, 010), scheinloesung (040, 042), negativer_exponent Terme (053, 055), definitionsmenge (027), zusammengesetzt (108, 112): je nach Strenge 3 bis 4 statt 2. | Bei der Gegenprüfung entscheiden. |
| C3 Tests | 043 ist als Test leichter als 045 und 049 (lineare Gleichung); 022, 029, 036 sind drei Tests mit demselben Format „zähle ganze Zahlen im Bereich“ (Ratechance klein, aber gleiche Form). | 043 durch 049-artige Rückwärtsaufgabe, ein Zähl-Test als Lücke mit zwei gekoppelten Werten. |
| C4 009 | Möglichkeit [3] „etwa 100“ liegt nur 33 % neben 150, bei „ungefähr“ nicht ganz scharf. | Möglichkeit ändern (etwa 1 000). |
| C5 Bestandsnähe | 062 (5⁰, Bestand „Tabelle 5², 5¹, 5⁰ fortsetzen“), 088 (Bestand „3 · 10ⁿ zwischen 0,02 und 0,5“), 026 (Bestand „für wie viele ganze x von −5 bis 5 nicht definiert“), 037/038/041 („Kandidat gegen D“ dreimal). | Hinweis für die Gegenprüfung. |
| C6 Lehrplan | Parameteraufgaben (024, 029, 036, 039), wissenschaftliche Schreibweise und nano/mikro bleiben ohne Lehrplanbeleg Jgst. 6 (nichts gefunden, nichts geraten). | Sammelprüfung. |

## Schema je Lernziel (unabhängig gezählt)

| Lernziel | Schema sicher | Grenzfall | Urteil (höchstens 2) |
|---|---|---|---|
| prozentwert | 3 (002, 006, 007) | 003, 004 | B1 |
| grundwert | 2 (013, 014) | 009, 010 | C2 |
| verstehen (Prozent) | 1 (017) | – | ok |
| definitionsmenge | 2 (025, 026) | 027 | ok |
| ueber_kreuz | 1 (030) | 031 | ok |
| scheinloesung | 2 (037, 038) | 040, 042 | C2 |
| verhaeltnis | 3 (043, 047, 049) | 048 | B1 |
| negativer_exponent (Terme) | 2 (051, 052) | 053, 055 | C2 |
| fehler_finden | 2 (061, 063) | – | ok |
| gross_wissenschaftlich | 3 (065, 068, 070) | – | B1 |
| negativer_exponent (Zehner) | 1 (076) | 072, 075 | ok (Denkfigur B2) |
| vorsilben_klein | 5 (078, 080, 081, 082, 083) | – | A4 |
| vergleichen_pruefen | 3 (085, 086, 088) | 087 | B1 |
| dreieck | 1 (095) | 093 | ok |
| rueckwaerts | 1 (103) | 099 | ok (Denkfigur B2) |
| zusammengesetzt | 2 (110, 111) | 108, 112 | C2 |
| verstehen (Flächen) | 1 (114) | 119 | ok |

Die Vorprüfung 2 zählte 11 Lernziele mit drei bis sechs; jetzt 5 Lernziele über zwei (vorsilben_klein 5, vier mit 3). Der Schreiber behauptet weiter überall höchstens zwei.

## Denkfiguren (Kurzfassung)

Mindestens 5 verschiedene Figuren in 15 von 17 Lernzielen; nur gross_wissenschaftlich (4) und vergleichen_pruefen (4) liegen darunter (B2). Figuren über zweimal: siehe B2.

## Schluss der A und B der Vorprüfung 2

Geschlossen (Stichprobe aller A, B1 bis B6, B9 bis B13): A1 (080), A2 (043 neuer Kern), A3 (060), A4 (105 und alle Auswahl), B1 (001, 015), B2 (045, 048), B3 (056, 063), B4 (066, 068, 075, 081, 085, 087), B5 (110, 112, 113 bis 116, 119), B6 (098/100, 052/074), B9 (029, 057, 106), B10 (029), B11 (035, 066, 099), B12 (jede Lücke hat ein Fehlbild, 042 neu), B13 (079, 078, 066/070).
Nicht geschlossen: A5 (jetzt A4), A6 nur teilweise (Schema ok, Denkfigur B2), B1 (009), B2 (049, 035), B3 (054 als neuer Klon, A2), B7/B8 (siehe B1, B2), B16 (002), 096 neu.

## Zählung

A 4, B 4, C 6.
