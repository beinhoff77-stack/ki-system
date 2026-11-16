# Postfach schwer-kl7 (Zehnte Runde, Klasse 7)

Neueste Meldung oben.

## 2026-11-16 07:45 – FERTIG
Zehnte Runde Klasse 7 abgeschlossen: 7 Themen, 45 Lernkarten, **272 neue Übungen** (Pool uebung), je Lernkarte mindestens 4× Stufe 3 und 2× Stufe 2,
davon je Lernkarte mindestens 2 Stufe-3-Aufgaben nach Prüfungsvorbild und 1 Knobelaufgabe. Jede Lernkarte hat jetzt 8–9 Stufe-3-Übungen.
Alle sieben Themen hatten einen Generator (gleichungen.linear: Generator `gleichungen_linear.py`).

Technik: Neuer Abschnitt „Zehnte Runde (schwer-kl7)“ am Ende jedes Generators mit eigenem festen Zufallsstart; die Hilfsdatei `inhalte/generatoren/_schwer_kl7.py`
hängt die neuen Übungen an die fertige Datei an (rechnet jede Zahl-/Lücken-Lösung nach, prüft Dubletten im ganzen Thema). Lernkarten, Texte, Zeichnungen und alle
alten Aufgaben sind unverändert. Nachweis: `python3 -I inhalte/generatoren/_schwer_kl7_nachweis.py <thema> [<git-ref>]` – Ergebnis für alle 7 Themen gegen den
Ausgangsstand von lernen-app (ecb5134) und gegen den aktuellen Stand (aea5ee3, dort keine Änderung an diesen Dateien): „alle alten Aufgaben unverändert an gleicher Stelle: JA“.
`tools/inhalt_pruefen.py` meldet für alle 7 Dateien OK. Jede neue Aufgabe von Hand nachgerechnet und gelesen.
Hinweis: `tools/__pycache__/inhalt_pruefen.cpython-313.pyc` ist im Repository eingecheckt und ändert sich bei jedem Generatorlauf (Import über `_kl7.py`); ich habe sie
jeweils zurückgesetzt und nicht committet. Vorschlag: aus dem Repository nehmen.

### (1) Befundliste aus Teil 1 (nichts geändert, nur gemeldet)
#### bruch.prozent_grundwert
- vermehrt, Stufe 3 „Ein Fahrrad kostet 720 €. Der Preis steigt um 2,5 %.“ und „Ein Nettopreis beträgt 60 € … 19 % Mehrwertsteuer“: einschrittig wie Stufe 2 – eher Stufe 2 (nur andere Zahlen).
- zurueck, Stufe 3 „Nach einer Erhöhung um 2 % kostet eine Ware 61,20 €“ und „Nach 3 % Rabatt … 300,70 €“: gleiche Rechnung wie Stufe 2, nur krummere Zahlen – eher Stufe 2.
- argumente, Stufe 1: „Welche Aussage ist mathematisch richtig begründet?“ mit vier langen Aussagen voller Fehlvorstellungen (z. B. 30 % + 50 % Rabatt) – für Stufe 1 zu schwer; Stufe 2 „Ein Preis von 60 € sinkt um 40 % auf 36 €. Welche Begründung zeigt das mathematisch?“ (Ablenker „Das klingt fair“) ist leichter als diese Stufe 1 – Stufen 1 und 2 sind hier vertauscht.
- argumente, Ablenker „Sinkt ein Wert um 100 %, halbiert er sich, denn 100 % ist die Hälfte von 200 %“: sprachlich verwirrend, aber eindeutig falsch – kein Fehler.
- Alle gelesenen Lösungen (≥ 10 je Lernkarte) richtig.
- Lücken laut Lehrplan/Schulaufgaben: Prozentpunkte vs. Prozent, Grundwert aus Prozentwert im Sachkontext (Anzahl gesamt), „x % weniger als“ mit wechselndem Grundwert, Aussagen zu Anteilen ohne Gesamtzahl, Diagramm-Ablesen mit Prozentrechnung – fehlten; jetzt als neue Übungen ergänzt.
#### terme.aufstellen
- termwert, Stufe 3 „Berechne den Wert von 5a + 3b für a = 1 und b = −2“ (und die anderen linearen Zwei-Variablen-Terme): leichter als die Stufe-2-Terme mit x² und negativem x – eher Stufe 2.
- struktur, Stufe 1 und 2 überschneiden sich (z. B. Stufe 1 „(y + 4) : 8“, Stufe 2 „(5y − 2) : 3“ – gleicher Schwierigkeitsgrad).
- sachsituation, Stufe 3 „Kletterhalle … Bei wie vielen Besuchen kosten beide gleich viel?“ verlangt eine Gleichung (Stoff von gleichungen.linear); durch Probieren lösbar, Lösung 8 richtig.
- deuten, alle gelesenen Stufe-3-Aufgaben („Jemand übersetzt … in den Term … Stimmt das?“) prüfen Übersetzen, nicht Deuten im Sachzusammenhang; das Deuten von Teiltermen fehlte.
- Alle gelesenen Lösungen richtig.
- Lücken: Tabellenkalkulations-Formeln (LehrplanPLUS 7, BMT8 2022/2025), Zahlenrätsel „Denke dir eine Zahl“ mit Begründung, gleichwertige Terme ankreuzen, Teilterme in Figuren deuten, Variable im Sachkontext deuten – jetzt ergänzt.
#### gleichungen.linear
- waage, Stufe 3 „Löse −11 − x = 5.“ und „Löse 2,5x + 4 = 29.“: ein bzw. zwei Umformungen wie Stufe 2 – eher Stufe 2.
- probe, Stufe 3 „Jemand multipliziert 6x + 6 = 21 auf beiden Seiten mit 0 …“: Ablenker „Nein: Es kommt 0 = c heraus.“ ist unverständlich (c ist nirgends erklärt) – sachlich falsch als Antwort, aber verwirrend.
- probe, Stufe 3 „Die Probe für x = −4 bei x − 6 = −5x − 30 wird so geschrieben: … Welche Aussage stimmt?“: Lösung stimmt; die Aufgabe prüft nur, ob man „−10 = −10“ richtig deutet – eher Stufe 2.
- sach, Stufe 1 „Eine Mutter ist 4 Jahre älter als das 3-Fache …“ verlangt Gleichung aufstellen mit zwei Bezügen – eher Stufe 2.
- Alle gelesenen Lösungen richtig.
- Lücken: Gleichungen mit Brüchen als Koeffizienten/Nenner (BMT8 2021), Lücke so füllen, dass eine gegebene Lösung herauskommt (BMT8 2024, JT RS 2025), Lösungsmenge bei Grundmenge ℕ, Fehler beim Minus vor der Klammer finden, Sachaufgabe mit „Rest“-Term 240 − x (BMT8 2023) – jetzt ergänzt.
#### abbildungen.kongruenz
- symmetrie, Stufe 3: Die Frage „Welcher Großbuchstabe (Blockschrift) ist punktsymmetrisch, hat aber keine Symmetrieachse?“ (Lösung N) kommt zweimal vor, nur mit anderen Ablenkern – inhaltlich doppelt.
- parkett, Stufe 3 „Passen 3 gleichseitige Dreiecke und 2 Quadrate lückenlos um eine Ecke?“: Ablenker „Nein: 3 · 60° + 2 · 90° = 360° ≠ 360°.“ widerspricht sich selbst (360° ≠ 360°) – unsinnig; ebenso bei 4 Dreiecken + 1 Quadrat der Ablenker „Ja: … = 330°“. Kein falscher Lösungsschlüssel, aber schwache Ablenker.
- eigenschaften, Stufe 1: „Zwei Achsenspiegelungen an parallelen Achsen ergeben eine Verschiebung.“ als richtige Antwort ist für Stufe 1 anspruchsvoll (Verkettung) – eher Stufe 2.
- Alle gelesenen Lösungen richtig (Drehungen um Z nachgerechnet).
- Lücken: Symmetrieachse/Zentrum aus Koordinaten einer Figur bestimmen (BMT8 2023/2025), Gegenbeispiel „gleiche Seiten ⇒ nicht deckungsgleich“, Drehwinkel als Vielfache, Pfeil-Repräsentanten mit falscher Orientierung (JT RS 2025), Innenwinkel des regelmäßigen n-Ecks rückwärts – jetzt ergänzt. lehrplan_gym ist für das Thema leer (schon unter „offen“ vermerkt).
#### geometrie.konstruktion
- kongruenzsatz, Stufe 3 (SsW-Fälle „a = 6 cm, c = 9 cm, α = 25° … Wie viele Dreiecke gibt es?“ usw.): Lösungen stimmen (nachgerechnet), aber ein Kind der Klasse 7 kann das nur durch genaues Konstruieren entscheiden (Rechnung bräuchte den Sinus, Kl. 10). Die App kann das Konstruieren nicht abfragen – Raten wahrscheinlich. Vorschlag: Hinweis „Zeichne es auf Papier“ ergänzen oder als Vertiefung kennzeichnen.
- vierecke, Stufe 3 „In einem Viereck ist α = 76°, β = 69° und γ = 76°. Berechne δ.“ (alle vier gelesenen Stufe-3-Aufgaben dieser Art): nur 360° minus Summe, ein Schritt – eher Stufe 1/2.
- satz_kehrsatz: Der Typ „Ein Schüler sagt: ‚Der Satz … ist wahr, also ist auch der Kehrsatz wahr.‘ Ist die Begründung richtig?“ kommt in Stufe 2 und Stufe 3 gleich vor (gleiche Antwort) – keine Steigerung.
- Alle gelesenen Lösungen richtig.
- Lücken: Winkel aus mehreren Beziehungen kombinieren (Schnittwinkel indirekt, Hilfsparallele bei Zickzack), Begründen „größter Innenwinkel ≥ 60°“, Kongruenz zweier gegebener Dreiecke entscheiden (SsW/sSW), Ortslinien-Anzahl (BMT8 2022), Beweisschritte ordnen (BMT8 2021) – jetzt ergänzt. Konstruieren selbst bleibt offen (App kann keine Zeichnung des Kindes prüfen).
#### geometrie.kreis
- thales, Stufe 3 „Ein Halbkreisfenster … eine Strebe bildet mit dem Durchmesser einen Winkel von 50°. Welchen Winkel bilden die beiden Streben …?“: Lösung 90° richtig, aber direkte Anwendung des Thalessatzes (die 50° sind nur Ablenkung) – eher Stufe 2.
- tangente, Stufe 3 „… Der Abschnitt von P bis zum ersten Berührpunkt ist 9 cm lang. Wie lang ist der Abschnitt bis zum zweiten?“ (auch 3 cm): reines Merkwissen, eher Stufe 1.
- umkreis_inkreis, Stufe 3 „∠BIC“ (180° − (β + γ)/2): gute Stufe-3-Aufgaben; alle Lösungen nachgerechnet richtig.
- Alle gelesenen Lösungen richtig.
- Lücken: größte Höhe über [AB] (BMT8 2023), Flächengleichheit am Thaleskreis (BMT8 2024), Mittelpunktswinkel = 2α mit Beweisschritten (BMT8 2025, 2021), rechtwinklig mit Thaleskreis in Koordinaten nachweisen (JT RS 2025), Anzahl Punkte mit Abstandsbedingungen (BMT8 2022), Mittelsenkrechte als Ortslinie im Sachkontext (BMT8 2019/2024) – jetzt ergänzt.

#### daten.boxplot
- kennwerte, Stufe 3 „Berechne das arithmetische Mittel“ (z. B. 10 Werte, Ergebnis 14,7): nur längere Rechnung mit mehr Zahlen, kein anderer Gedanke – eher Stufe 2. Gute Stufe 3 ist dagegen „fehlender Wert bei gegebenem Mittel“.
- vergleichen: Stufe 1 und 2 sind gleich gebaut („Welche Aussage ist richtig?“ mit vier Aussagen zu zwei Boxplots) – keine erkennbare Steigerung; Stufe 1 ist für Einsteiger anspruchsvoll.
- mittel_median, Stufe 3 „Wartezeiten … Welcher Wert beschreibt die typische Mitte besser?“ mit Lösung „beide fast gleich“: richtig, aber eher Stufe 2.
- Alle gelesenen Lösungen richtig (Quartile mit dem Verfahren der Datei nachgerechnet).
- Lücken: Median aus Häufigkeiten/Anteilen bzw. Säulendiagramm (BMT8 2023/2025), gewichteter Mittelwert aus Prozentangaben (BMT8 2022/2023), Mittelwert per Tabellenkalkulation mit Klammerfehler (BMT8 2025), Aussagen zu Boxplots mit Anzahlen bei verschieden großen Gruppen – jetzt ergänzt.

### (2) Genutzte Prüfungsquellen und abgeleitete Aufgabentypen
Alle Aufgaben sind eigene Fassungen (eigene Zahlen, eigene Einkleidung); übernommen wurden nur Typ, Aufbau und Niveau. Der Bayerische Mathematik-Test 8 (BMT8)
prüft zu Beginn der 8. Klasse den Stoff der 7. Klasse und ist deshalb die Hauptquelle.

Quellen (Adressen):
- BMT8 2019 B: https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2019/bmt8_2019_aufgaben_gruppe_b.pdf
- BMT8 2021 A: https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2021/bmt8_2021_aufgaben_gruppe_a.pdf
- BMT8 2022 A: https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2022/bmt8_2022_aufgaben_gruppe_a.pdf
- BMT8 2023 A: https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2023/BMT8_2023_Aufgaben_Gruppe_A.pdf
- BMT8 2024 A: https://isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2024/BMT8_2024_Aufgaben_Gruppe_A.pdf
- BMT8 2025 A: https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/BMT8_2025_Aufgaben_Gruppe_A.pdf
- Jahrgangsstufentest Realschule 8, 2025 II (Lösung): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/2025_JT_Mathematik_8_II_Loesung.pdf
- Jahrgangsstufentest Realschule 8, 2019 I und II: https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2019/2019_jt_mathe_8_i_angabe.pdf und https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2019/2019_jt_mathe_8_ii_angabe.pdf
- Jahrgangsstufentest Realschule 8, 2014 I: https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2014/jahrgangsstufe_8_i_angabe.pdf ; 2020 II: https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2020/2020_jt_mathe_8_ii_loesung.pdf
- ISB-Leistungsaufgaben Realschule 8 I: https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Mathematik/Weiterentwicklung_Abschlusspruefung/Exemplarische_Leistungsaufgaben/rs_m_08_leistungsaufgaben_8i.pdf
- Schulaufgaben Klasse 7 Gymnasium: https://www.klassenarbeiten.de/data/dynamic/pdf/3023.pdf und https://www.klassenarbeiten.de/data/dynamic/pdf/3243.pdf
- Vergleichsarbeit Jgst. 8 (Innenwinkel im n-Eck), zitiert in der SMART-Sammlung der Uni Bayreuth: https://btmdx1.mat.uni-bayreuth.de/smart/buch/smart_gym_j00.pdf
- Känguru der Mathematik, Klassenstufen 7/8 (nur als Vorbild für Knobelaufgaben): https://didaktik.mathematik.hu-berlin.de/user/beierarx/kaenguru2023_78.pdf

Je Thema:
- **bruch.prozent_grundwert** – BMT8 2021 A5 (Gleichung zu „20 % weniger als“ wählen), 2025 A6b (Prozentvergleich mit wechselndem Grundwert: 20 % kleiner / 25 % größer),
  2021 A6c (Prozentpunkte), 2024 A3c (Grundwert aus Prozentwert im Sachkontext), 2023 A6 (99 % entfernt), 2019 B6a/d (Term deuten; gleicher Anteil bei anderer Gesamtzahl),
  2025 A6d (aus Anteilen nicht auf Anzahlen schließen); JT RS 2025 Nr. 17/19 (Zinsen; 10 % mehr → alter Preis). Fallen: „auf“ vs. „um“, Grundwert nach „als“, Prozentpunkte, Rabatte addieren.
- **terme.aufstellen** – BMT8 2022 A3 und 2025 A5 (Tabellenkalkulationsformeln, Punkt vor Strich), 2021 A2 (Zahlenrätsel als Term, Begründung), 2021 A4b (Teilterm deuten),
  2023 A2a (Variable deuten), 2024 A1b (Zahl ersetzen) und A7a (Umfangsterm einer Figur), 2019 B7 (Formel auswerten und rückwärts); JT RS 2025 Nr. 14 (gleichwertigen Term ankreuzen).
- **gleichungen.linear** – BMT8 2024 A1 (Minus vor der Klammer; Zahl ersetzen, damit x = 2 Lösung ist), 2021 A3 (Gleichung mit Brüchen), 2019 B2 (Klammern),
  2023 A2 (Eintrittskarten 7x + 10(200 − x)); JT RS 2025 Nr. 12, 13, 15 (Dezimalkoeffizienten, Zaun-Sachaufgabe, Lücke so füllen, dass L stimmt); Schulaufgabe Kl. 7 (Grundmenge, Fehler finden).
- **abbildungen.kongruenz** – BMT8 2023 A3 (Symmetrieachsen der Raute, Gegenbeispiel), 2025 A7 (Parallelogramm in Koordinaten); JT RS 2025 Nr. 4/7/8 (Pfeil-Repräsentant,
  Orientierung, Mittelpunkt), 2019 I (Gerade bei Drehung um 180°), 2014 I und 2019 II (Drehwinkel), ISB-Leistungsaufgaben RS 8 I (Drehwinkel im Bereich),
  Vergleichsarbeit Jgst. 8 (Innenwinkel des n-Ecks rückwärts); Känguru 2023 (Parkett, Knobel).
- **geometrie.konstruktion** – BMT8 2019 B5 (größter Innenwinkel begründen; Schnittwinkel indirekt), 2019 B4b (Punkt gleich weit von drei Orten), 2021 A8 (Beweisschritte ordnen),
  2022 A1c (Punkte mit zwei Abstandsbedingungen), 2022 A7a (Treppengeländer-Parallelogramm), 2023 A3b (Gegenbeispiel WWW), 2024 A5 / 2025 A8 (Radien → gleichschenklig);
  JT RS 2020 II (Dreieck zwischen Parallelen), 2025 Nr. 10 (Thales-Kehrsatz); ISB-Leistungsaufgaben RS 8 I (Viereck aus Eigenschaften); Schulaufgabe Kl. 7 (SsW/sSW bei zwei Dreiecken).
- **geometrie.kreis** – BMT8 2023 A7c (größte Höhe über [AB]), 2024 A5 (Thales, Flächengleichheit), 2025 A8 (Mittelpunktswinkel = 2α), 2021 A8 (Beweis ordnen),
  2022 A1b/c (Abstand als Lot, Anzahl Punkte), 2019 B4b / 2024 A4b (Mittelsenkrechte im Sachkontext); JT RS 2025 Nr. 10 (rechtwinklig mit Thaleskreis zeigen).
- **daten.boxplot** – BMT8 2021 A7 (Median/Quartile von 13 Werten, Boxplot), 2022 A5c (Durchschnittsnote aus Anteilen), 2023 A5b/c (Median aus Anteilen, Änderung des Mittelwerts),
  2024 A3b (Aussagen zu einer Darstellung beurteilen), 2025 A5 (Mittelwert per Tabellenkalkulation, Klammerfehler), 2025 A6c/d (Median aus Säulendiagramm; Anteil vs. Anzahl).

### (3) Neue Aufgaben je Lernkarte (Stufe 2 / Stufe 3; in Klammern: davon Stufe 3 nach Prüfungsvorbild, Knobel)
| Thema | Lernkarte: neu Stufe 2 / Stufe 3 |
|---|---|
| bruch.prozent_grundwert (+43) | faktor 2/4 (2, 2) · vermehrt 2/4 (3, 1) · vermindert 2/4 (2, 1) · zurueck 2/4 (2, 1) · prozentsatz 2/4 (3, 1) · mehrfach 2/4 (2, 2) · argumente 2/5 (3, 1) |
| terme.aufstellen (+37) | struktur 2/4 (2, 1) · termwert 2/4 (2, 1) · uebersetzen 3/4 (2, 2) · sachsituation 2/4 (3, 1) · muster 2/4 (2, 1) · deuten 2/4 (3, 1) |
| gleichungen.linear (+36) | waage 2/4 (2, 1) · beide_seiten 2/4 (2, 1) · klammern 2/4 (2, 1) · probe 2/4 (3, 1) · sonderfaelle 2/4 (2, 1) · sach 2/4 (3, 1) |
| abbildungen.kongruenz (+42) | achsenspiegelung 2/4 (2, 1) · punktspiegelung 2/4 (3, 1) · verschiebung 2/4 (2, 1) · drehung 2/4 (2, 1) · symmetrie 2/4 (3, 1) · parkett 2/4 (2, 1) · eigenschaften 2/4 (2, 1) |
| geometrie.konstruktion (+42) | parallelen 2/4 (2, 1) · winkelsumme 2/4 (2, 1) · gleichschenklig 2/4 (2, 1) · kongruenzsatz 2/4 (3, 1) · konstruierbar 2/4 (2, 1) · vierecke 2/4 (2, 1) · satz_kehrsatz 2/4 (2, 1) |
| geometrie.kreis (+36) | thales 2/4 (2, 1) · umkehrung 2/4 (2, 1) · beweis 2/4 (2, 1) · lage 2/4 (2, 1) · tangente 2/4 (2, 1) · umkreis_inkreis 2/4 (2, 1) |
| daten.boxplot (+36) | median 2/4 (2, 1) · kennwerte 2/4 (3, 1) · mittel_median 2/4 (2, 1) · quartile 2/4 (2, 1) · boxplot 2/4 (2, 1) · vergleichen 2/4 (2, 1) |

### (4) Themen ohne (ausreichende) echte Prüfungsaufgaben – ehrlich gemeldet
Zu keinem Thema fehlte jede Prüfungsquelle, aber bei einzelnen Lernkarten ist die Grundlage dünn:
- **abbildungen.kongruenz / parkett**: In BMT8 und den Realschul-Jahrgangsstufentests keine Parkett-Aufgabe gefunden. Genutzt: Vergleichsarbeit Jgst. 8 (Innenwinkel im n-Eck, nur über die SMART-Sammlung der Uni Bayreuth zugänglich) und Känguru 2023 (Knobel).
- **abbildungen.kongruenz / drehung**: Drehaufgaben nur in Realschul-Tests (JT RS 2014, 2019) gefunden, nicht im Gymnasial-BMT8. lehrplan_gym ist für das Thema leer.
- **geometrie.kreis / tangente**: Keine BMT8-Aufgabe direkt zu Tangenten gefunden; abgeleitet aus BMT8 2022 A1 (Abstand Punkt–Gerade) und dem Lehrplanpunkt „Tangentenkonstruktion begründen“.
- **geometrie.konstruktion / satz_kehrsatz**: Reine Satz/Kehrsatz-Logik kommt in den gefundenen Tests nicht vor; Vorbild nur Thales-Kehrsatz (JT RS 2025) und Beweisschritte ordnen (BMT8 2021 A8).
- VERA-8-Testhefte (IQB) habe ich nicht im Wortlaut ausgewertet (die gefundenen Dateien waren Handreichungen ohne passende Einzelaufgaben); daher keine VERA-Aufgaben als Vorbild.
- Mehrere BMT-PDFs waren beim Abruf teils unleserlich (Formeln); verwendet wurden nur eindeutig erkennbare Aufgabentypen.

## 2026-11-16 07:40 – STATUS
daten.boxplot fertig: +36 Übungen (je Lernkarte 2× Stufe 2, 4× Stufe 3), Prüfskript OK, Nachweis: alle 144 alten Aufgaben unverändert.

## 2026-11-16 07:20 – STATUS
geometrie.kreis fertig: +36 Übungen (je Lernkarte 2× Stufe 2, 4× Stufe 3), Prüfskript OK, Nachweis: alle 144 alten Aufgaben unverändert. Weiter mit daten.boxplot (letztes Thema).

## 2026-11-16 06:55 – STATUS
geometrie.konstruktion fertig: +42 Übungen (je Lernkarte 2× Stufe 2, 4× Stufe 3), Prüfskript OK, Nachweis: alle 168 alten Aufgaben unverändert. Weiter mit geometrie.kreis.

## 2026-11-16 06:30 – STATUS
abbildungen.kongruenz fertig: +42 Übungen (je Lernkarte 2× Stufe 2, 4× Stufe 3), Prüfskript OK, Nachweis: alle 168 alten Aufgaben unverändert. Weiter mit geometrie.konstruktion.

## 2026-11-16 06:05 – STATUS
gleichungen.linear fertig (Generator gleichungen_linear.py): +36 Übungen (je Lernkarte 2× Stufe 2, 4× Stufe 3), Prüfskript OK, Nachweis: alle 162 alten Aufgaben unverändert. Weiter mit abbildungen.kongruenz.

## 2026-11-16 05:45 – STATUS
terme.aufstellen fertig: +37 Übungen (je Lernkarte 2–3× Stufe 2, 4× Stufe 3), Prüfskript OK, Nachweis: alle 144 alten Aufgaben unverändert. Weiter mit gleichungen.linear.

## 2026-11-16 05:20 – STATUS
bruch.prozent_grundwert fertig: +43 Übungen (je Lernkarte 2× Stufe 2, 4–5× Stufe 3), Prüfskript OK, Nachweis: alle 168 alten Aufgaben unverändert an gleicher Stelle.
Weiter mit terme.aufstellen. Befunde und Quellen folgen gesammelt im Abschlussbericht.
