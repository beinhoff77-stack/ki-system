# Postfach stufen-kl6 (Zwanzigste Runde, Klasse 6: echte Stufe 3 und Knobel-Bordkarten)

Neueste Meldung oben.

## 2026-11-17 19:50 – FERTIG: Zwanzigste Runde, Klasse 6 (Zweig stufen-kl6)

Alle 11 Themen mit gym_by 6 bearbeitet (85 Lernkarten), je Thema ein Commit. Bei allen 11 Dateien meldet `tools/inhalt_pruefen.py` OK, ohne Fehler zu Typen,
und 0 Gruppen „gleich gebaut hintereinander“. Nachweis `inhalte/generatoren/_stufen_kl6_nachweis.py <thema>` bei allen OK:
alte Aufgaben unverändert bis auf g (und s, wo umgestuft), nur Übungen innerhalb ihrer Lernkarte umsortiert, Test/Korrektur/Sicherung unverändert.

**Vorgehen (Fakten)**
- Werkzeug `inhalte/generatoren/_stufen_kl6.py`: Typ-Vorschlag nach Textmerkmalen; jede Lernkarte von Hand durchgesehen und abweichende Typen/Stufen im Generator festgelegt (Abschnitt „STUFEN“ am Ende jedes Generators).
- Neue Übungen einzeln entworfen, jede mit eigenem Satzbau; Lösung über den Rechenausdruck „c“ vom Programm nachgerechnet; bei Auswahl nur eine richtige Antwort.
- Reihenfolge je Lernkarte: Stufe 1 → 2 → 3, nie zwei gleiche Typen und nie drei gleich gebaute Fragen hintereinander.
- messen.flaechen_vielecke und messen.volumen: Die Prüfungsvorbild-Aufgaben der Achtzehnten Runde sind als „pruefung“ markiert (nachgeschlagen über ein neues Verzeichnis ARTEN in `_luecken_neu.py`, das die Ausgabe nicht ändert).

**Annahme (bitte bestätigen oder anders entscheiden)**
- Überzählige Übungen (dritte und weitere gleich gebaute desselben Typs je Stufe; auf Stufe 3 mehr als drei je Typ) haben **kein g**.
  Mit g meldete das Prüfskript „mehr als 2 gleich gebaute“ als Fehler. Ohne g prüft das Skript die Typ-Regeln für diese Lernkarten in der Datei nicht vollständig;
  deshalb prüft der Nachweis zusätzlich eine Kopie **ohne** die überzähligen – so, wie es nach dem Sperren ist. Dort: alle Typ-Regeln erfüllt.
- Inhaltliche Grenze: Knobel-Bordkarten zu finanzen.zinsen ohne Zinseszins (Modell der Karten); terme.potenzgesetze bleibt inhaltlich wie bisher (siehe Durchsicht-Bericht: Potenzgesetze nennt LehrplanPLUS M6 nicht).

### (3) Zahlen
- Lernkarten: 85 · Typen vergeben: alle nicht überzähligen Übungen
- umgestuft (nur Feld s): 81
- neue Übungen: 386 · neue Knobel-Bordkarten (Pool bonus): 170 (2 je Lernkarte)
- überzählig (ohne g, zum Sperren): 281
- Jede Lernkarte (ohne überzählige): Stufe 1 ≥ 4 mit 2 Typen, Stufe 2 ≥ 6 mit ≥ 3 Typen, Stufe 3 ≥ 8 mit ≥ 4 Typen, je Typ höchstens 3.

### (6) Beispiel: bruch.brueche / bruchteil_von – drei Bordkarten je Stufe im Wortlaut
- **Stufe 1**
  - (direkt) Berechne 1/2 von 24 m.
  - (direkt) Berechne 8/9 von 90 kg.
  - (erkennen) Mit welcher Rechnung bekommst du 3/4 von 20 m? – Auswahl: 20 m · 4 : 3 | 20 m − 3/4 | 20 m : 3 · 4 | 20 m : 4 · 3
- **Stufe 2**
  - (mehrschritt) Wie viele Minuten sind 13/20 Stunde?
  - (einkleidung) Eine Klasse hat 20 Kinder. 1/2 der Kinder fahren mit dem Bus. Wie viele Kinder sind das?
  - (umkehr) Welcher Bruchteil von 60 € sind 45 €? Gib den Bruch vollständig gekürzt an.
- **Stufe 3**
  - (transfer) Von 40 € Erspartem gibt ein Kind 1/2 für Bücher und 1/5 für Kino aus. Wie viel Euro bleiben übrig?
  - (begruenden) Was ist mehr: 2/3 von 90 € oder 3/4 von 80 €? Gib den Unterschied in Euro an.
  - (fehler) Ein Kind rechnet 3/5 von 40 m so: 40 · 5 : 3. Welches Ergebnis ist richtig? Gib es in Metern an.
- **Knobel (freiwillig)**
  - (knobel) Ein Kind liest am ersten Tag die Hälfte eines Buchs, am zweiten Tag 1/3 vom Rest und am dritten Tag 1/4 vom neuen Rest. Jetzt fehlen noch 30 Seiten. Wie viele Seiten hat das Buch?
  - (knobel) Drei Geschwister teilen 72 Murmeln: Das erste bekommt 1/3, das zweite 1/4, das dritte den Rest. Dann gibt das dritte dem ersten so viele ab, dass beide gleich viele haben. Wie viele hat das erste jetzt?

Woran man den Unterschied sieht: Stufe 1 rechnet wie das Beispiel der Karte, Stufe 2 kleidet ein oder dreht die Frage um, Stufe 3 verlangt einen anderen Gedanken
(Rest bestimmen, vergleichen und begründen, einen Fehler erklären); die Knobel-Bordkarten brauchen eine eigene Idee (rückwärts über mehrere Reste, Gleichverteilen).

### (5) Quellen der Prüfungsvorbilder
Für „pruefung“ wurden Typ und Niveau nachgebaut, nie Wortlaut oder Zahlen. Vorbilder (Art der Aufgaben):
- ISB, Jahrgangsstufentest Mathematik 6 (Realschule Bayern), z. B. 2019, 2022, 2023, 2024: kurze Rechen-, Runden- und Einheitenaufgaben, Platzhalter-Aufgaben, Würfel aus kleinen Würfeln mit bemalten Flächen.
  https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2019/2019_jt_mathe_6_angabe.pdf ·
  https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2023/2023_JT_Mathe_6_Angabe.pdf ·
  https://isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2024/2024_JT_Mathe_6_Angabe.pdf
- ISB, Jahrgangsstufentest 6 (2014): Aussage „Hat … recht? Begründe“ (Vorbild für die begründenden Prüfungsaufgaben).
  https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2014/2014_07_17_jahrgangsstufe_6_angabe_geschwaerzt.pdf
- ISB, Illustrierende Aufgaben zum LehrplanPLUS Gymnasium M6 1.3 (Rechenregeln plausibel machen, Überschlag).
  https://www.lehrplanplus.bayern.de/sixcms/media.php/71/LPP-GY-M_613-A_GrundlegendeKFF_vorbereitend.pdf
- SMART-Aufgabensammlung Jgst. 6 (Universität Bayreuth), u. a. „Hälfte, Hälfte des Rests, Rest bleibt“ (Vorbild für Rest-Aufgaben rückwärts).
  https://btmdx1.mat.uni-bayreuth.de/smart/buch/smart_gym_j06.pdf
- Knobel-Bordkarten: Art der Känguru- und Mathematik-Olympiade-Aufgaben (mehrere Ideen, kurze Lösung) – eigene Aufgaben, keine übernommen.
- Weitere Vorbilder aus den früheren Runden (Zehnte und Neunzehnte Runde: BMT 8, Grundwissenstest 7, VERA-8) wurden nicht erneut abgerufen.

### (1) Stufen-Leiter je Lernkarte

**bruch.brueche**

- bruchteil_von: **S1** Bruchteil einer Größe ausrechnen: durch den Nenner teilen, mal den Zähler nehmen. **S2** Bruchteil in Sachsituationen und mit Umrechnen von Einheiten; erkennen, welcher Bruchteil eine Größe ist. **S3** Rest nach mehreren Bruchteilen, rückwärts zum Ausgangsbetrag, Fehler deuten, mit Flächen verknüpfen, für welche Nenner es aufgeht.
- anteil_bestimmen: **S1** Anteil an einem Bild ablesen oder „Teil von Ganzem“ als Bruch schreiben. **S2** Anteil in Sachsituationen, mit Einheiten und am Bild mit ungleich gezählten Teilen bestimmen und kürzen. **S3** Rest-Anteil, Anteil vom Rest, Verhältnis gegen Anteil, Fehler beim Teilen durch den Rest, Anteile von Gruppen vergleichen, mögliche Gruppengrößen.
- ganzes_bestimmen: **S1** Aus einem Teil das Ganze bestimmen: durch den Zähler teilen, mal den Nenner nehmen. **S2** In Sachsituationen das Ganze bestimmen; umgekehrt den Bruchteil aus Teil und Ganzem finden. **S3** Das Fehlende statt des Ganzen, rückwärts über Ausgaben, Fehler deuten, mit Flächen verknüpfen, Aussagen prüfen, Nenner bestimmen.
- erweitern: **S1** Zähler und Nenner mit derselben Zahl malnehmen; gleichwertige Brüche erkennen. **S2** Fehlenden Zähler oder Nenner ergänzen, den Erweiterungsfaktor finden, auf große Nenner erweitern, in Sachsituationen. **S3** Rückwärts zum Ausgangsbruch, Fehler deuten, Aussagen prüfen, mit Vielfachen verknüpfen, Bedingungen an Zähler und Nenner, Prüfungsaufgabe.
- kuerzen: **S1** Zähler und Nenner durch dieselbe Zahl teilen; einen passenden Teiler erkennen. **S2** Vollständig kürzen, prüfen ob ein Bruch vollständig gekürzt ist, Anteile aus Sachsituationen kürzen, vom gekürzten Bruch zurück. **S3** Rückwärts über mehrere Kürzungen, Fehler deuten (auch „Ziffern streichen“), Produkte vor dem Ausrechnen kürzen, für wie viele Zähler es geht, Prüfungsaufgabe.
- gemischte_zahlen: **S1** Gemischte Zahl in unechten Bruch umwandeln und umgekehrt; gemischte Zahlen erkennen. **S2** Umwandeln mit Kürzen, vergleichen, einordnen zwischen ganzen Zahlen, am Zahlenstrahl, in Sachsituationen, fehlenden Zähler finden. **S3** Fehler deuten, mit Größen verknüpfen, Zahlen dazwischen finden, Ziffern-Rätsel, Aussagen prüfen, rückwärts aus dem Zähler.
- vergleichen: **S1** Brüche mit gleichem Nenner oder gleichem Zähler vergleichen. **S2** Mit Hauptnenner vergleichen und ordnen, in Sachsituationen und am Zahlenstrahl. **S3** Abstand zu 1, Bruch dazwischen, Mischungen vergleichen, Lücke einsetzen, Aussagen und Fehler prüfen, Prüfungsaufgabe.
- zahlenstrahl: **S1** Einen Bruch am Zahlenstrahl markieren, wenn die Teile zum Nenner passen; einen Bruch ablesen. **S2** Markieren mit Erweitern, über 1 hinaus, in Sachsituationen, Ablesen mit Kürzen. **S3** Strahl beginnt nicht bei 0, Mitte und Abstand, rückwärts zur Teilung, Fehler deuten, Aussagen prüfen, passende Teilung für mehrere Brüche.
- zahlbereiche: **S1** Brüche als Zahlen schreiben (auch Division), am Zahlenstrahl markieren, positive und negative Brüche vergleichen. **S2** Negative Brüche ordnen, am Zahlenstrahl markieren, in Sachsituationen, Zahlbereiche zuordnen. **S3** Mitte zwischen negativem und positivem Bruch, Begriffe verknüpfen, Fehler deuten, Aussage „nächste Zahl“ prüfen, Anzahl der Brüche in einem Bereich, rückwärts über Spiegeln.
- verstehen: **S1** Einfache Aussagen über Brüche prüfen; einen Anteil als Bruch schreiben. **S2** Aussagen prüfen, für die man rechnen, kürzen, erweitern oder umkehren muss; Aussagen in Sachsituationen. **S3** Falsche Regeln durch Gegenbeispiel widerlegen, Fehler deuten, Anteile verschieden großer Gruppen, Zahlen finden, für die eine Aussage stimmt, rückwärts, mit Teilern verknüpfen.

**bruch.dezimal**

- stellenwerte: **S1** Ziffern einer Dezimalzahl ihrer Stelle zuordnen, Zahlen aus der Stellenwerttafel lesen. **S2** Zahlen aus Stellenwerten und Brüchen mit Nenner 10, 100, 1 000 zusammensetzen, Wert einer Ziffer, Zahlen aus dem Alltag. **S3** Bündeln über eine Stelle hinweg, größte Zahl aus Ziffern, Zahlenrätsel, Fehler deuten, Aussagen prüfen, Größen umrechnen, Prüfungsaufgabe.
- vergleichen_ordnen: **S1** Zwei Dezimalzahlen Stelle für Stelle vergleichen. **S2** Mehrere Zahlen ordnen, am Zahlenstrahl markieren, die Mitte finden, Preise vergleichen. **S3** Fehlende Ziffer bestimmen, Anzahl der Zahlen dazwischen, Strahl mit anderem Anfang, Fehler deuten, Aussagen prüfen, mit negativen Zahlen, Zahlenrätsel, Prüfungsaufgabe.
- runden: **S1** Auf Ganze und Zehntel runden; erkennen, auf welche Stelle gerundet wurde. **S2** Auf Hundertstel und Tausendstel runden, Preise auf Cent runden, Zahlen finden, die einen gerundeten Wert ergeben, am Zahlenstrahl. **S3** Fehler beim Runden in Schritten, größte oder kleinste mögliche Zahl, Aussagen prüfen, wie viele Ziffern passen, mit Größen verknüpfen, Messwerte deuten.
- bruch_zu_dezimal: **S1** Brüche mit Nenner 10, 100, 1 000 oder einem passenden Nenner als Dezimalzahl schreiben. **S2** Unechte Brüche und gemischte Zahlen umwandeln, in Sachsituationen, am Zahlenstrahl, fehlenden Zähler finden. **S3** Rest-Anteile, Unterschied zwischen Bruch und Dezimalzahl, Nenner für endliche Dezimalzahlen, Fehler deuten, Aussagen prüfen, rückwärts zum Nenner, mit Umfang verknüpfen.
- dezimal_zu_bruch: **S1** Eine Dezimalzahl als Bruch mit Nenner 10, 100 oder 1 000 schreiben und kürzen. **S2** Zahlen über 1 als Bruch oder gemischte Zahl, Anteile von Größen, fehlende Ziffer, am Zahlenstrahl ablesen. **S3** Periodische Zahlen als Bruch, Summen, wie viele Ziffern passen, Fehler deuten, Aussagen prüfen, rückwärts vom gekürzten Bruch, Prüfungsaufgabe.
- merkwerte: **S1** Wichtige Brüche, Dezimalzahlen und Prozente im Kopf ineinander umwandeln. **S2** Weniger bekannte Merkwerte (Achtel, Fünftel) umwandeln, Prozent und Bruch, in Sachsituationen. **S3** Bedingungen an Zähler und Nenner, Taschenrechner-Anzeige deuten, Mitte, Unterschied, Fehler, rückwärts, passende Ziffer, Prüfungsaufgabe.
- periodisch: **S1** Erkennen, ob ein Bruch endlich oder periodisch ist; bekannte periodische Zahlen zuordnen. **S2** Periodische Dezimalzahl ausrechnen und schreiben, Ziffer an einer bestimmten Stelle, Sachsituation. **S3** Erst kürzen, dann entscheiden; Stellen weit hinten; vergleichen; Fehler deuten; rückwärts zum Zähler; wie viele Zähler passen.
- verstehen: **S1** Einfache Aussagen über Dezimalzahlen prüfen; Zahlen aus Stellenwerten schreiben. **S2** Aussagen prüfen, für die man runden, vergleichen oder umwandeln muss, auch in Sachsituationen und am Zahlenstrahl. **S3** Falsche Regeln widerlegen, mit Brüchen und Perioden verknüpfen, Rundungsfehler deuten, für welche Ziffern eine Aussage stimmt.

**bruch.rechnen**

- brueche_plus_minus: **S1** Brüche mit gleichem oder leicht zu findendem Nenner addieren und subtrahieren; den gemeinsamen Nenner erkennen. **S2** Mit Hauptnenner rechnen, mehrere Brüche, gemischte Zahlen, Lücken füllen, Sachsituationen. **S3** Rest bei mehreren Ausgaben, Stammbruch-Lücke, Fehler deuten, Aussagen widerlegen, rückwärts, mit Umfang verknüpfen, Prüfungsaufgabe.
- dezimal_plus_minus: **S1** Dezimalzahlen Komma unter Komma addieren und subtrahieren. **S2** Unterschiedlich viele Stellen, mehrere Zahlen, Rückgeld, Ergänzen bis zu einer Zahl. **S3** Einheiten wechseln, Kassenbon prüfen, rückwärts, Fehler deuten, Aussagen widerlegen, fehlende Ziffer, Umfang, mehrteilige Sachaufgabe.
- vorzeichen: **S1** Positive und negative Brüche und Dezimalzahlen addieren, subtrahieren, malnehmen; das Vorzeichen eines Ergebnisses erkennen. **S2** Mal und Geteilt mit Vorzeichen, Hauptnenner mit negativen Brüchen, Lücken, Kontostand und Temperatur. **S3** Vorzeichen bei vielen Faktoren, Fehler deuten, Aussagen widerlegen, für welche Zahlen, rückwärts, mit Bruchteilen verknüpfen, Sprungfolge, Prüfungsaufgabe.
- brueche_mal: **S1** Bruch mal natürliche Zahl, Bruchteil vom Bruchteil am Bild erkennen. **S2** Bruch mal Bruch mit Kürzen, gemischte Zahlen, Flächen und Mengen in Sachsituationen, fehlenden Faktor finden. **S3** Anteil vom Anteil, Mengen umrechnen, Fehler deuten, Aussagen widerlegen, rückwärts, für welche Zahlen, wiederholtes Malnehmen, Prüfungsaufgabe.
- brueche_geteilt: **S1** Bruch durch natürliche Zahl teilen, Kehrbruch angeben. **S2** Durch einen Bruch teilen, gemischte Zahlen, Füllen und Aufteilen, fehlende Seite eines Rechtecks, fehlenden Teiler finden. **S3** Ergebnis ohne Rechnen beurteilen, Fehler deuten, rückwärts, Terme aus Worten, für welche Zahlen, Rest beim Aufteilen.
- dezimal_mal: **S1** Dezimalzahl mal natürliche Zahl, Zahl der Nachkommastellen im Ergebnis erkennen. **S2** Dezimalzahl mal Dezimalzahl, Preis mal Menge, fehlenden Faktor finden. **S3** Aus einem bekannten Produkt schließen, mehrteilige Sachaufgabe, Fehler deuten, Aussagen widerlegen, rückwärts, für welche Zahlen, Fläche, Größenvorstellung.
- dezimal_geteilt: **S1** Dezimalzahl durch natürliche Zahl teilen, eine Division ohne Komma im Teiler aufschreiben. **S2** Durch eine Dezimalzahl teilen, aufteilen und gerecht verteilen, runden, fehlenden Teiler finden. **S3** Einheiten umrechnen, Preise vergleichen, rückwärts, Ergebnis ohne Rechnen beurteilen, Fehler deuten, für welche Teiler, mehrteilige Sachaufgabe.
- potenzen: **S1** Quadrat und Kubikzahl von Brüchen und Dezimalzahlen berechnen; erkennen, was eine Potenz bedeutet. **S2** Potenzen mit negativer Basis, gemischten Zahlen, kleinen Dezimalzahlen; Flächen; Basis zu einem Quadrat finden. **S3** −a² gegen (−a)², Potenzen vergleichen, für welche Zahlen das Quadrat kleiner ist, Fehler deuten, Halbieren als Potenz, Vorzeichen begründen.
- rechenvorteile: **S1** Faktoren vertauschen, damit ein Paar 1, 10 oder 100 ergibt; solche Paare erkennen. **S2** Geschickt rechnen mit Brüchen und Dezimalzahlen, beim Teilen nicht umklammern, Lücke im Produkt. **S3** Klammern setzen, Fehler beim Umklammern deuten, Teiler vertauschen begründen, rückwärts, Zahl finden, Rechnungen vergleichen, Sachaufgabe.
- gemischt: **S1** Punkt vor Strich bei Dezimalzahlen; erkennen, was zuerst gerechnet wird. **S2** Klammern, Brüche und Dezimalzahlen gemischt, Einkauf mit Rückgeld, Lücke in einer Rechnung. **S3** Rechner-Eingabe deuten, Term aus Worten, Rechenzeichen finden, Aussagen widerlegen, rückwärts, Fläche eines Weges, Klammern setzen, Prüfungsaufgabe.
- fehler_finden: **S1** Einfache Fehler benennen (Nenner addiert, Komma falsch) und Aussagen mit Überschlag prüfen. **S2** Ein Ergebnis mit Überschlag auswählen, falsche Ergebnisse berichtigen, fehlende Zahl aus einem Ergebnis finden, Fehler am Zahlenstrahl. **S3** Fehler bei Punkt vor Strich, Vorzeichen und Komma deuten; verwechselte Rechenart rückwärts; für welche Zahlen eine Behauptung stimmt; Kassenfehler; fehlerhafte Rechnung finden.
- sach: **S1** Anteil vom Anteil ausrechnen und die passende Rechnung erkennen. **S2** Anteil vom Anteil in Sachsituationen, Rest-Mengen, Überschlag, vom Anteil zurück zum Bruch. **S3** Rest nach mehreren Schritten, rückwärts zum Ganzen, Fehler deuten, Aussagen prüfen, Teilgruppen zusammenführen, Prüfungsaufgabe.

**zahlen.potenzen_zehner**

- zehnerpotenz: **S1** 10ⁿ ausschreiben und die Zahl der Nullen ablesen. **S2** Zahlen und Zahlwörter als Zehnerpotenz schreiben, Tausender zählen, Zehnerpotenzen einordnen. **S3** Verhältnisse von Zehnerpotenzen, Stückzahlen über mehrere Stufen, Fehler deuten, Bereiche für n, Aussagen prüfen, rückwärts zum Exponenten.
- gross_wissenschaftlich: **S1** Große Zahlen als a · 10ⁿ schreiben und zurück. **S2** Große Zahlen aus dem Alltag umschreiben, die richtige Schreibweise auswählen, Summen ausschreiben, die Zahl a bestimmen. **S3** Mantisse korrigieren, Stapelhöhe, Bruchteile großer Zahlen, Stellenzahl, Fehler deuten, Größen vergleichen, für welche Ziffern, mehrteilige Sachaufgabe.
- vorsilben_gross: **S1** Vorsilben k, M, G, T ihrer Zehnerpotenz zuordnen und einfache Werte umrechnen. **S2** Mit Komma und in beide Richtungen umrechnen, Datenmengen und Leistungen vergleichen. **S3** Wie viele passen hinein, Zeit beim Download, Haushalte mit Strom versorgen, Fehler deuten, Aussagen prüfen, für welche Zahlen.
- negativer_exponent: **S1** 10⁻ⁿ als Dezimalzahl oder Bruch schreiben; erkennen, welche Zahl zu 10⁻ⁿ gehört. **S2** Dezimalzahl als 10ⁿ schreiben, Nullen zählen, kleine Zehnerpotenzen vergleichen, Größen im Alltag. **S3** Wie oft passt …, Verhältnisse, Nullen rückwärts, Fehler deuten, für welchen Exponenten, Aussagen prüfen, mit Brüchen verknüpfen.
- klein_wissenschaftlich: **S1** a · 10⁻ⁿ als Dezimalzahl schreiben; die richtige Schreibweise erkennen. **S2** Kleine Zahlen als a · 10ⁿ schreiben, auswählen, Nullen zählen, kleine Größen aus dem Alltag. **S3** Wie viele passen auf eine Länge, Stapelhöhe, Teilen durch Zehnerpotenzen, Fehler deuten, Aussagen prüfen, Exponent bestimmen.
- vorsilben_klein: **S1** Vorsilben m, µ, n ihrer Zehnerpotenz zuordnen und einfach umrechnen. **S2** Umrechnen mit Komma und zur Grundeinheit zurück, Zeiten am Computer, kleinste Länge finden. **S3** Wie viele passen auf eine Strecke, Bilder pro Sekunde, Fehler deuten, Aussagen prüfen, rückwärts zur Dicke, mehrteilige Sachaufgabe.
- vergleichen_pruefen: **S1** Zwei Zahlen in Zehnerpotenz-Schreibweise vergleichen; eine Zehnerpotenz ausschreiben. **S2** Die kleinste oder größte Zahl finden, ordnen, Verhältnisse, Größen aus dem Alltag, Exponent zu einer Zahl. **S3** Fehler in der Schreibweise deuten, Aussagen prüfen, Verhältnisse kleiner Größen, Bereich für den Exponenten.

**terme.potenzgesetze**

- potenz_begriff: **S1** Potenzen natürlicher Zahlen ausrechnen, Basis und Exponent benennen. **S2** Potenzen von Brüchen, Dezimalzahlen und negativen Zahlen; Würfelvolumen; Basis zu einer Potenz finden. **S3** Potenzen vergleichen, Wachstum, −a² gegen (−a)², Endziffern, Würfel aus Würfeln, Fehler deuten, rückwärts über zweimal Quadrieren.
- negativer_exponent: **S1** a⁻ⁿ als Bruch schreiben, a⁰ = 1 kennen. **S2** Potenzen von Brüchen mit negativem Exponenten, Brüche als Potenz schreiben, Summen, Größen aus dem Alltag. **S3** Verhältnisse, Vorzeichen, kleinste Zahl finden, Exponent bestimmen, Fehler deuten, rückwärts, Zahlen ordnen.
- mal_gleiche_basis: **S1** Bei gleicher Basis die Exponenten addieren; die passende Regel erkennen. **S2** Mit negativen Exponenten und Variablen, drei Faktoren, fehlenden Exponenten ergänzen, als Dezimalzahl. **S3** Lichtjahre, Zahl als Potenz umschreiben, Paare zählen, Fehler deuten, Aussagen prüfen, rückwärts, Zerlegen in Faktoren.
- geteilt_gleiche_basis: **S1** Bei gleicher Basis die Exponenten subtrahieren; die passende Regel erkennen. **S2** Negative Ergebnisse, Variablen, Malnehmen und Teilen gemischt, fehlenden Exponenten ergänzen, Sachsituation. **S3** Festplatte und Filme, rückwärts zum Exponenten, gemischte Basen zerlegen, Fehler deuten, Aussagen prüfen, für welche n, Speicher als Prüfungsaufgabe.
- gleicher_exponent: **S1** Bei gleichem Exponenten die Basen malnehmen; das Ergebnis erkennen. **S2** Geschickt rechnen mit Produkten 10, 1 oder 100, auch beim Teilen und mit Brüchen; fehlende Basis finden; Quadrat vergrößern. **S3** Drei Faktoren, Bruchbasen, Fehler deuten, Aussage „Summe“ widerlegen, rückwärts, für welche Basis, Würfel aus Würfeln, Nullen zählen.
- anwenden: **S1** Eine Zahl als Potenz schreiben und Exponenten addieren; die passende Regel erkennen. **S2** Geschickt mit 2 · 5 = 10 rechnen, Teilen, Falten, Zahlen als Zweier- oder Zehnerpotenz darstellen. **S3** Stapelhöhe, große Potenzen vergleichen, Nullen am Ende, Fehler deuten, rückwärts zur Zahl der Faltungen, für welche n, Bevölkerungsdichte.
- fehler_finden: **S1** Einfache Potenzrechnungen auf Richtigkeit prüfen; eine Potenz ausrechnen. **S2** Den Fehler bei einer Regel benennen und berichtigen, auch in Sachsituationen; vom falschen Exponenten zum richtigen. **S3** Basis falsch, Exponent falsch, −4², Summe statt Produkt deuten; für welche Basis eine falsche Regel zufällig stimmt; rückwärts aus einem falschen Ergebnis.

**messen.flaechen_vielecke**

- parallelogramm: **S1** A = g · h mit gegebener Grundseite und Höhe; die richtige Höhe erkennen. **S2** Einheiten umrechnen, mehrere Flächen in Sachsituationen, die passende Höhe zur gewählten Seite. **S3** Fläche im Koordinatensystem, Höhe zu einer anderen Seite, Verdoppeln begründen, schief gedrückter Rahmen, Diagonale, Kosten, Fehler deuten.
- dreieck: **S1** A = g · h : 2 mit gegebener Grundseite und Höhe; erkennen, was die Höhe ist. **S2** Höhe außen, rechtwinklige Dreiecke, Einheiten, die passende Rechnung auswählen. **S3** Dreieck im Rechteck rückwärts, Koordinaten, wandernde Spitze, Drachen, Fehler deuten, gleiche Fläche begründen.
- trapez: **S1** A = (a + c) · h : 2 mit gegebenen Maßen; die parallelen Seiten erkennen. **S2** Grundstücke und rechtwinklige Trapeze, Einheiten, die passende Rechnung auswählen. **S3** Formel begründen, Koordinaten, Rechteck mit abgeschnittenen Ecken, Mittellinie, Kosten einer Wiese, Zerlegen, Fehler bei Punkt vor Strich.
- rueckwaerts: **S1** Aus Fläche und einer Länge die fehlende Länge beim Parallelogramm bestimmen. **S2** Fehlende Höhe oder Grundseite bei Dreieck und Trapez, mit Einheiten. **S3** Höhe zu einer anderen Seite, gleich große Figuren, Einheitenwechsel, fehlende parallele Seite, Abstand der Seiten in einer Sachsituation.
- zusammengesetzt: **S1** Eine Figur in Rechtecke und Dreiecke zerlegen und die Teile addieren. **S2** Abschneiden oder Ausschneiden (subtrahieren), Figuren aus mehreren Grundformen. **S3** Vierecke im Koordinatensystem, Loch mit vorgegebener Größe, Quadrat in Quadrat, Rahmen, Giebelwand, fehlende Höhe rückwärts.
- oberflaeche: **S1** Oberfläche eines Prismas aus Grundflächen und Rechtecken zusammensetzen; Flächen eines Körpers erkennen. **S2** Schachteln, Zelte, Behälter und Netze mit Dreieck oder Trapez als Grundfläche. **S3** Würfel mit herausgenommener Ecke begründen, zusammengeklebte Körper, Kantenmodell, Schachtel aus Karton, Spielhaus, offener Trog.
- verstehen: **S1** Flächen vergleichen und einfache Aussagen beurteilen; Flächeninhalt eines Rechtecks berechnen. **S2** Schief drücken, verdoppeln, gleiche Grundseite und Höhe, fehlende Seite eines Rechtecks, Fläche schätzen. **S3** Fläche und Umfang unterscheiden, Maßstab, gleiche Fläche begründen, schätzen bei gebogenen Rändern, Fehler deuten, fehlende Höhe.

**messen.volumen**

- einheitswuerfel: **S1** Würfel in einem Quader zählen; Volumen aus Länge, Breite, Höhe in Würfeln. **S2** Größere Würfel in Kartons, Umrechnen zwischen Würfelgrößen, Schichten rückwärts. **S3** Treppen und Pyramiden aus Würfeln, bemalte Würfel, Quader aus vorgegebener Würfelzahl, Ecke herausnehmen, Stapel im Regal.
- quader: **S1** V = a · b · c für Quader und V = a³ für Würfel mit gegebenen Kanten; die Formel erkennen. **S2** Dezimalzahlen und gemischte Einheiten, Sandkasten und Kisten, passende Rechnung auswählen. **S3** Halbes Volumen planen, Würfel teilen, Quader mit 24 cm³ zählen, Kosten, Kante aus Volumen, Kantenmodell rückwärts, Stapeln, Vergleich.
- einheiten: **S1** Volumeneinheiten mit der Umrechnungszahl 1 000 umrechnen. **S2** Über zwei Stufen umrechnen, gemischte Angaben in Kommaschreibweise, in die größere Einheit, Größen vergleichen. **S3** Gleiche Volumen erkennen, Summen gemischter Einheiten, Würfel in Würfel zerlegen und aneinanderreihen, Fehler deuten, Reihenfolge begründen, Kante rückwärts.
- liter: **S1** Liter, Milliliter und dm³ umrechnen; wissen, wie viel ml ein Liter hat. **S2** cm³ und dm³ in Liter, Aquarien, Pools, Gläser aus einer Flasche. **S3** Regen auf Dächern, Messbecher, tropfender Hahn, Behälter vergleichen, Füllhöhe rückwärts, Teilfüllung, Verbrauch über Tage.
- rueckwaerts: **S1** Aus Volumen und zwei Kanten die dritte Kante bestimmen. **S2** Grundfläche aus Volumen und Höhe, Füllhöhe in Becken und Aquarien, Höhe aus Litern. **S3** Luftkissen und Kartons als Quader, Stein im Aquarium, Umfüllen in ein anderes Gefäß, Säule und Würfel gleich groß, Teilfüllung.
- zusammengesetzt: **S1** Volumen eines Körpers aus zwei Quadern addieren; erkennen, ob addiert oder subtrahiert wird. **S2** Stufen und Treppen, Kisten mit Wänden, aufgesetzte Würfel. **S3** Ausgeschnittene Ecken, L-Bauteile, durchbohrte Würfel, Rinnen, Mauern mit Durchgang, Becken mit zwei Tiefen, Rahmen, Fehler deuten.
- verstehen: **S1** Einheiten und Größen von Volumen einschätzen; Würfelvolumen berechnen. **S2** Rechnungen prüfen, Kanten verdreifachen, halbieren, Inhalte schätzen. **S3** Maßstab, Volumen und Oberfläche unterscheiden, Würfel mit dreifacher Kante, Liter und Kilogramm, Luft je Person, Aussagen begründen.

**bruch.prozent**

- prozent_bedeutung: **S1** Hundertstel als Prozent lesen und schreiben, Prozent am Hunderterfeld erkennen. **S2** Brüche, Dezimalzahlen und Prozent ineinander umwandeln, vergleichen, Anteile in Bildern und Sachsituationen. **S3** Rest-Anteile, fehlender Tabellenwert, Prozentpunkte, Fehler deuten, über 100 % begründen, rückwärts, passender Nenner, Prüfungsaufgabe.
- prozentwert: **S1** Prozentwert mit einfachen Prozentsätzen berechnen; die passende Rechnung erkennen. **S2** Krumme Prozentsätze, über 100 %, Sachsituationen, Überschlag, Prozentstreifen. **S3** Überschlag begründen, Anteil vom Anteil, Rest, Schluss von einem Prozentsatz auf einen anderen, Fehler deuten, Prozentsatz zu einem Wert finden, mehrteilige Aufgabe.
- prozentsatz: **S1** Prozentsatz bei Grundwert 100 oder einem einfachen Grundwert bestimmen; einfache Anteile in Prozent erkennen. **S2** Prozentsatz in Sachsituationen, mit Einheiten, Rest-Anteil, Preisänderung, am Hunderterfeld. **S3** Änderung bezogen auf den alten Wert, steigen gegen sinken, Fläche, Fehler deuten, Aussage begründen, wie viele Punkte reichen, Wahl.
- grundwert: **S1** Vom Prozentwert über 1 % oder 10 % zum Grundwert; die passende Rechnung erkennen. **S2** Grundwert bei krummen Prozentsätzen, in Sachsituationen, Preis vor dem Rabatt aus der Ersparnis. **S3** Rest gegeben, „20 % weniger als“, Preis nach Rabatt, Restseiten, Fehler deuten, Aussage prüfen, Grundwert für gleiche Werte, Bruch und Prozent verknüpfen.
- rabatt_aufschlag: **S1** Neuen Preis nach Rabatt oder Aufschlag berechnen; den Faktor erkennen. **S2** Rabatt und Preiserhöhung in Sachsituationen, Angebote vergleichen, Rabatt in Prozent aus altem und neuem Preis. **S3** Läden und Gutscheine vergleichen, rückwärts über zwei Änderungen, Mengenrabatt, doppelter Rabatt, ab welchem Preis sich ein Gutschein lohnt.
- zinsen: **S1** Jahreszinsen aus Kapital und Zinssatz berechnen; wissen, was Zinsen sind. **S2** Zinssatz bestimmen, Guthaben nach einem Jahr, Zinsen für Monate, Banken vergleichen. **S3** Kapital rückwärts, Guthaben rückwärts, Kredit für Monate, Zinseszins, Fehler deuten, Aussage begründen, ab welchem Zinssatz, mehrteilige Aufgabe.
- verstehen: **S1** Einfache Aussagen über Prozent prüfen; einfache Prozentwerte ausrechnen. **S2** Aussagen über Rabatte, Zinsen, Prozentpunkte und Anteile in Sachsituationen prüfen; „jeder Vierte“ in Prozent. **S3** Prozent gegen Prozentpunkte, Bezugsgröße bei Gruppen, Fehler in Zeitungsaussagen deuten, Prozent von Prozent, rückwärts zum alten Anteil.

**finanzen.zinsen**

- begriffe: **S1** Kapital, Zinssatz und Zinsen in einem Text erkennen und den Kontostand nach einem Jahr angeben. **S2** Kontostand vorwärts und rückwärts, zwei Jahre, Zinsen aus der Differenz. **S3** Ungenaue Sprache begründen, Zinssätze vergleichen, Grundwert-Falle deuten, doppeltes Kapital, Zinsen aus dem Endstand rückwärts, Bruch als Zinssatz.
- rollen: **S1** Erkennen, wer in einer Situation Zinsen zahlt oder bekommt. **S2** Situationen mit Freunden, Krediten und Angeboten beurteilen, Zinsen aus Rückzahlung. **S3** Warum Banken zahlen können, Zinsspanne, Fehlvorstellung beim Kredit, Sparen und Kredit gleichzeitig, rückwärts zum Kredit, Ratenkauf, Prüfungsfrage.
- jahreszinsen: **S1** Jahreszinsen mit Z = K · p/100 berechnen; die Formel erkennen. **S2** Guthaben und Rückzahlung, zusammengelegtes Kapital, mehrere Jahre mit Abheben, Zinssatz aus Zinsen. **S3** Fehler deuten, Zinssatz für gleiche Zinsen, Vertauschen von Kapital und Zinssatz begründen, rückwärts zum Kapital, Bruchteile verknüpfen, Hochrechnen, Prüfungsaufgabe.
- jahreszinsen_komma: **S1** Jahreszinsen bei Zinssätzen mit Komma berechnen; den Zinssatz als Rechenzahl erkennen. **S2** Bankvergleich, Kredit, Guthaben, Zinssatz mit Komma aus Zinsen bestimmen. **S3** Fehler beim Malnehmen mit dem Prozentsatz deuten, Kapital rückwärts, Überschlag begründen, gleicher Ertrag, Gebühren, Zinssatzerhöhung, kleines Kapital für 1 €.
- zinssatz: **S1** Zinssatz = Zinsen durch Kapital mal 100 bei glatten Zahlen; die Rechnung erkennen. **S2** Zinssatz aus Kontostand oder Rückzahlung, Banken vergleichen, Zinsen zu anderem Kapital. **S3** Fehler deuten, halbes Jahr, Zinsen ohne Zinseszins über Jahre, Prozentpunkte, Aussage begründen, rückwärts über zwei Jahre, Bruchteile, Prüfungsaufgabe.
- kapital: **S1** Kapital aus Zinsen und Zinssatz über 1 % bestimmen; die Rechnung erkennen. **S2** Kredit aus Zinsen, Zinssatz mit Komma, gewünschte Zinsen, Zinsen zu anderem Kapital. **S3** Fehler deuten, Kapital aus dem Endstand, Banken vergleichen, halbes Jahr, Aussage begründen, gleiche Zinsen, Monatszinsen als Ziel, Zinsen aus dem Endstand.
- monatszinsen: **S1** Zinsen für ganze Monate mit Jahreszinsen · m/12; den Zeitanteil erkennen. **S2** Monatszinsen bei großem Kapital, Zeitraum aus Daten, Rückzahlung eines Kredits, Kapital aus Monatszinsen. **S3** Fehler deuten, Monate rückwärts, Angebote vergleichen, Hochrechnen, höchstens erlaubte Monate, Bruchteil eines Jahres, Prüfungsaufgabe mit Daten.
- zeitanteil: **S1** Zinsen für ein halbes Jahr und ein Vierteljahr; wissen, wie viele Monate das sind. **S2** Dreivierteljahr, Guthaben und Kredite für Teile eines Jahres, Kapital aus Halbjahreszinsen, anderthalb Jahre. **S3** Fehler deuten, Halbjahr auf Vierteljahr umrechnen, Angebote begründen, Dauer rückwärts, Zinssatz für 1 % im Vierteljahr, Drittel und Dreiviertel, Prüfungsaufgabe.

**daten.darstellen**

- absolute_haeufigkeit: **S1** Striche und Nennungen zählen, eine Strichliste lesen. **S2** Summen, Unterschiede und „oder“/„weder noch“ aus Listen und Strichlisten, häufigsten Wert finden. **S3** Fehlender Wert, Rangfolge erschließen, Bedingungen kombinieren, Würfelsummen begründen, doppelt so oft, Zählfehler deuten, Fünferbündel, mehrteilige Umfrage.
- relative_haeufigkeit: **S1** Relative Häufigkeit als Bruch „Anzahl durch Gesamtzahl“ angeben; wissen, was sie bedeutet. **S2** In Prozent und gekürzt angeben, rückwärts zur Anzahl, Rest-Anteile. **S3** Gruppen verschiedener Größe vergleichen, Diagramm mit Bruch verknüpfen, Buchstaben zählen, neue Kinder kommen dazu, Fehler deuten, wie oft muss es fallen.
- tabelle_auswerten: **S1** Einen Wert aus einer Häufigkeitstabelle ablesen. **S2** Summen, „nicht“, Prozent und Rangfolge aus Tabellen, Teilgruppen, Rest ohne Tabelle. **S3** Kopiergeld gewichtet, fehlende Werte rückwärts, zwei Klassen vergleichen, Fehler beim Prozent deuten, fehlender Wert mit Bedingung, Vierfeldertafel, Prüfungsaufgabe.
- saeulendiagramm: **S1** Säulenhöhe mit Maßstab in Anzahl umrechnen; eine Säule ablesen. **S2** Summen, Unterschiede, Prozent aus Diagrammen, Säulenhöhe aus Tabelle mit Maßstab. **S3** Maßstab wählen, fehlende Säule rückwärts, Gesamtzahl aus Prozent, Verhältnis der Höhen, Anteil eines Tages, Fehler beim Maßstab.
- kreisdiagramm: **S1** Winkel für einen Prozentsatz oder Anteil berechnen. **S2** Anzahlen aus dem Kreisdiagramm ablesen, Winkel aus Anzahlen, Prozent aus Winkeln, dritter Teil. **S3** Anzahl aus Winkel, Gesamtzahl rückwärts, Teile in Beziehung, Noten-Diagramm, Fehler deuten, Winkelsumme begründen, Befragtenzahl für einen Winkel.
- irrefuehrend: **S1** Achsenanfang und Teile eines Kreisdiagramms erkennen; ein ehrliches Diagramm ablesen. **S2** Wirkung eines abgeschnittenen Achsenanfangs ausrechnen, Summe 100 % prüfen, Bildflächen, Sachsituationen. **S3** Irreführende Aussagen begründen, Fläche und Volumen bei Bild-Diagrammen, fehlende Säulen, Prozentpunkte gegen Verdoppeln, rückwärts zum verdeckten Wert.

**daten.kennwerte**

- mittelwert: **S1** Mittelwert weniger Zahlen berechnen; wissen, was er bedeutet. **S2** Mittelwert aus Diagrammen, mit Dezimalzahlen und negativen Zahlen, in Sachsituationen, Gruppen vergleichen. **S3** Richtige Rechnung wählen, aufeinanderfolgende Zahlen, Notenspiegel finden, Aussage prüfen, Fehler deuten, rückwärts, fehlende Zahl, Wettkampf als Prüfungsaufgabe.
- mittel_tabelle: **S1** Mittelwert aus einer Häufigkeitstabelle berechnen; das Vorgehen erkennen. **S2** Tabellen mit Noten, Toren und Geschwistern, die gleiche Rechnung aus einem Text. **S3** Wie viele müssen dazukommen, Fehler beim ungewichteten Rechnen deuten, Anteile in Prozent als Gewichte, verwischte Anzahl rückwärts, Aussage prüfen, Notenspiegel.
- mittel_rueckwaerts: **S1** Aus Mittelwert und Anzahl die Summe berechnen; die passende Rechnung erkennen. **S2** Fehlenden Wert bestimmen, ein Wert kommt dazu, Ziel-Mittelwert erreichen, Gesamtzeit aus Mittelwert. **S3** Note für einen Zielschnitt, ein Kind verlässt die Gruppe, x gleich Mittelwert, gewichtete Klassen, Fehler deuten, Aussage begründen, Teilgruppen rückwärts, Zeugnis als Prüfungsaufgabe.
- modal_spannweite: **S1** Modalwert und Spannweite einer kurzen Reihe bestimmen; die Begriffe erkennen. **S2** Lange Reihen, negative Zahlen und Dezimalzahlen, zwei Modalwerte, Temperaturen, kleinster Wert aus der Spannweite. **S3** Kein Modalwert begründen, Zahl ergänzen, Grenze im Diagramm, Fehler deuten, Brüche verknüpfen, Würfel-Rätsel, Summe aus Kennwerten.
- median: **S1** Median einer geordneten kurzen Reihe bestimmen; wissen, dass man vorher ordnet. **S2** Ungeordnete Reihen mit gerader und ungerader Anzahl, negative Zahlen, Strichlisten, Sachdaten. **S3** Fehler deuten, Ausreißer begründen, Tabelle mit 150 Werten, Zahl ergänzen, Median gleich Mittelwert, Brüche, Laufzeiten, ein Wert kommt dazu.
- verstehen: **S1** Einfache Aussagen über Mittelwert prüfen; Kennwerte benennen und berechnen. **S2** Aussagen über Spannweite, Ausreißer und Verdoppeln prüfen, Summe aus dem Mittelwert, typischer Wert. **S3** Median gegen Mittelwert bei Ausreißern, Unterschied ausrechnen, Fehler beim Zusammenfassen von Klassen, Median ist kein Datenwert, Mindestwert, passender Kennwert für eine Meldung.

### (2) Übungen je Stufe und Typ – vorher → nachher
Vorher hatte keine Übung einen Typ; „vorher“ zählt die Übungen je Stufe. „nachher“ ohne die überzähligen.

**bruch.brueche**

| Lernkarte | vorher (S1/S2/S3, ohne Typ) | nachher mit Typ (ohne überzählige) | überzählig | Knobel |
|---|---|---|---|---|
| bruchteil_von | 6/13/5 | S1 6 (direkt 5, erkennen 1) · S2 13 (einkleidung 7, mehrschritt 5, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, rueckwaerts 1, transfer 3, verknuepfen 1) | 2 | 2 |
| anteil_bestimmen | 6/13/5 | S1 7 (direkt 1, erkennen 6) · S2 13 (darstellung 6, einkleidung 3, mehrschritt 4) · S3 8 (begruenden 1, fehler 1, parameter 1, rueckwaerts 1, transfer 3, verknuepfen 1) | 0 | 2 |
| ganzes_bestimmen | 6/12/6 | S1 7 (direkt 6, erkennen 1) · S2 11 (einkleidung 9, mehrschritt 1, umkehr 1) · S3 9 (begruenden 1, fehler 1, parameter 1, rueckwaerts 1, transfer 3, verknuepfen 2) | 2 | 2 |
| erweitern | 7/13/4 | S1 6 (direkt 5, erkennen 1) · S2 9 (einkleidung 1, mehrschritt 2, umkehr 6) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 1, verknuepfen 2) | 8 | 2 |
| kuerzen | 6/13/5 | S1 4 (direkt 3, erkennen 1) · S2 9 (einkleidung 1, mehrschritt 7, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 11 | 2 |
| gemischte_zahlen | 4/6/8 | S1 5 (direkt 4, erkennen 1) · S2 7 (darstellung 1, einkleidung 2, mehrschritt 3, umkehr 1) · S3 8 (begruenden 1, fehler 2, rueckwaerts 1, transfer 3, verknuepfen 1) | 2 | 2 |
| vergleichen | 8/15/7 | S1 4 (direkt 2, erkennen 2) · S2 14 (darstellung 1, einkleidung 1, mehrschritt 12) · S3 8 (begruenden 2, fehler 1, parameter 1, pruefung 1, transfer 2, verknuepfen 1) | 10 | 2 |
| zahlenstrahl | 6/12/6 | S1 4 (direkt 2, erkennen 2) · S2 6 (darstellung 2, einkleidung 1, mehrschritt 2, umkehr 1) · S3 9 (begruenden 1, fehler 1, parameter 1, rueckwaerts 1, transfer 3, verknuepfen 2) | 12 | 2 |
| zahlbereiche | 4/6/8 | S1 4 (direkt 1, erkennen 3) · S2 9 (darstellung 1, einkleidung 1, mehrschritt 7) · S3 8 (begruenden 1, fehler 1, parameter 1, rueckwaerts 1, transfer 3, verknuepfen 1) | 0 | 2 |
| verstehen | 9/10/5 | S1 9 (direkt 1, erkennen 8) · S2 10 (einkleidung 1, mehrschritt 8, umkehr 1) · S3 8 (begruenden 3, fehler 1, parameter 1, rueckwaerts 1, transfer 1, verknuepfen 1) | 3 | 2 |

**bruch.dezimal**

| Lernkarte | vorher (S1/S2/S3, ohne Typ) | nachher mit Typ (ohne überzählige) | überzählig | Knobel |
|---|---|---|---|---|
| stellenwerte | 8/11/5 | S1 6 (direkt 2, erkennen 4) · S2 12 (darstellung 2, einkleidung 1, mehrschritt 8, umkehr 1) · S3 8 (begruenden 1, fehler 1, pruefung 1, rueckwaerts 1, transfer 3, verknuepfen 1) | 3 | 2 |
| vergleichen_ordnen | 6/13/5 | S1 4 (direkt 2, erkennen 2) · S2 9 (darstellung 2, einkleidung 1, mehrschritt 6) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, transfer 3, verknuepfen 1) | 10 | 2 |
| runden | 6/12/6 | S1 5 (direkt 4, erkennen 1) · S2 10 (darstellung 1, einkleidung 3, mehrschritt 5, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 8 | 2 |
| bruch_zu_dezimal | 6/14/4 | S1 4 (direkt 3, erkennen 1) · S2 10 (darstellung 1, einkleidung 1, mehrschritt 7, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 11 | 2 |
| dezimal_zu_bruch | 6/11/7 | S1 4 (direkt 3, erkennen 1) · S2 10 (darstellung 1, einkleidung 2, mehrschritt 6, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 11 | 2 |
| merkwerte | 4/6/8 | S1 5 (direkt 4, erkennen 1) · S2 10 (einkleidung 2, mehrschritt 7, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 0 | 2 |
| periodisch | 7/11/6 | S1 6 (direkt 2, erkennen 4) · S2 6 (darstellung 2, einkleidung 1, mehrschritt 2, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, rueckwaerts 1, transfer 3, verknuepfen 1) | 8 | 2 |
| verstehen | 6/11/7 | S1 5 (direkt 1, erkennen 4) · S2 13 (darstellung 1, einkleidung 1, mehrschritt 11) · S3 8 (begruenden 3, fehler 1, parameter 1, verknuepfen 3) | 2 | 2 |

**bruch.rechnen**

| Lernkarte | vorher (S1/S2/S3, ohne Typ) | nachher mit Typ (ohne überzählige) | überzählig | Knobel |
|---|---|---|---|---|
| brueche_plus_minus | 6/14/6 | S1 5 (direkt 4, erkennen 1) · S2 14 (einkleidung 2, mehrschritt 11, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 6 | 2 |
| dezimal_plus_minus | 6/14/4 | S1 5 (direkt 4, erkennen 1) · S2 9 (einkleidung 2, mehrschritt 5, umkehr 2) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 1, verknuepfen 2) | 7 | 2 |
| vorzeichen | 6/14/4 | S1 6 (direkt 5, erkennen 1) · S2 17 (einkleidung 2, mehrschritt 13, umkehr 2) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 1 | 2 |
| brueche_mal | 6/15/5 | S1 4 (direkt 3, erkennen 1) · S2 10 (einkleidung 4, mehrschritt 5, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 10 | 2 |
| brueche_geteilt | 6/13/7 | S1 4 (direkt 3, erkennen 1) · S2 10 (einkleidung 4, mehrschritt 5, umkehr 1) · S3 8 (begruenden 3, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, verknuepfen 1) | 8 | 2 |
| dezimal_mal | 6/14/4 | S1 4 (direkt 3, erkennen 1) · S2 7 (einkleidung 2, mehrschritt 4, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 12 | 2 |
| dezimal_geteilt | 6/14/4 | S1 4 (direkt 3, erkennen 1) · S2 9 (einkleidung 4, mehrschritt 4, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 10 | 2 |
| potenzen | 4/6/8 | S1 5 (direkt 4, erkennen 1) · S2 8 (einkleidung 1, mehrschritt 6, umkehr 1) · S3 8 (begruenden 2, fehler 2, parameter 1, transfer 3) | 0 | 2 |
| rechenvorteile | 6/15/5 | S1 4 (direkt 3, erkennen 1) · S2 15 (einkleidung 1, mehrschritt 13, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 6 | 2 |
| gemischt | 6/14/4 | S1 4 (direkt 3, erkennen 1) · S2 12 (einkleidung 2, mehrschritt 9, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 7 | 2 |
| fehler_finden | 9/8/7 | S1 8 (direkt 1, erkennen 7) · S2 6 (darstellung 1, einkleidung 1, mehrschritt 3, umkehr 1) · S3 8 (begruenden 1, fehler 3, parameter 1, pruefung 1, rueckwaerts 1, transfer 1) | 8 | 2 |
| sach | 4/6/8 | S1 4 (direkt 3, erkennen 1) · S2 8 (einkleidung 5, mehrschritt 2, umkehr 1) · S3 8 (begruenden 1, fehler 2, pruefung 1, rueckwaerts 1, transfer 3) | 1 | 2 |

**zahlen.potenzen_zehner**

| Lernkarte | vorher (S1/S2/S3, ohne Typ) | nachher mit Typ (ohne überzählige) | überzählig | Knobel |
|---|---|---|---|---|
| zehnerpotenz | 6/11/7 | S1 8 (direkt 6, erkennen 2) · S2 11 (einkleidung 1, mehrschritt 5, umkehr 5) · S3 8 (begruenden 1, fehler 1, parameter 1, rueckwaerts 1, transfer 3, verknuepfen 1) | 0 | 2 |
| gross_wissenschaftlich | 6/13/5 | S1 4 (direkt 3, erkennen 1) · S2 13 (einkleidung 5, mehrschritt 7, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 3 | 2 |
| vorsilben_gross | 7/10/7 | S1 7 (direkt 5, erkennen 2) · S2 10 (einkleidung 2, mehrschritt 6, umkehr 2) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, transfer 3, verknuepfen 1) | 1 | 2 |
| negativer_exponent | 6/12/6 | S1 7 (direkt 6, erkennen 1) · S2 12 (einkleidung 1, mehrschritt 9, umkehr 2) · S3 8 (begruenden 1, fehler 1, parameter 1, rueckwaerts 1, transfer 3, verknuepfen 1) | 1 | 2 |
| klein_wissenschaftlich | 6/10/8 | S1 7 (direkt 6, erkennen 1) · S2 9 (einkleidung 2, mehrschritt 3, umkehr 4) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, transfer 3, verknuepfen 1) | 3 | 2 |
| vorsilben_klein | 6/11/7 | S1 6 (direkt 3, erkennen 3) · S2 11 (einkleidung 2, mehrschritt 8, umkehr 1) · S3 8 (begruenden 1, fehler 1, pruefung 1, rueckwaerts 1, transfer 3, verknuepfen 1) | 2 | 2 |
| vergleichen_pruefen | 7/9/8 | S1 8 (direkt 1, erkennen 7) · S2 11 (einkleidung 1, mehrschritt 9, umkehr 1) · S3 8 (begruenden 3, fehler 3, parameter 1, transfer 1) | 0 | 2 |

**terme.potenzgesetze**

| Lernkarte | vorher (S1/S2/S3, ohne Typ) | nachher mit Typ (ohne überzählige) | überzählig | Knobel |
|---|---|---|---|---|
| potenz_begriff | 8/10/6 | S1 8 (direkt 6, erkennen 2) · S2 11 (einkleidung 2, mehrschritt 8, umkehr 1) · S3 8 (begruenden 2, fehler 1, rueckwaerts 1, transfer 3, verknuepfen 1) | 0 | 2 |
| negativer_exponent | 6/12/6 | S1 6 (direkt 3, erkennen 3) · S2 13 (einkleidung 1, mehrschritt 11, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 0 | 2 |
| mal_gleiche_basis | 8/11/5 | S1 9 (direkt 8, erkennen 1) · S2 13 (einkleidung 1, mehrschritt 10, umkehr 2) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 0 | 2 |
| geteilt_gleiche_basis | 6/14/4 | S1 7 (direkt 6, erkennen 1) · S2 16 (einkleidung 1, mehrschritt 14, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 0 | 2 |
| gleicher_exponent | 6/12/6 | S1 8 (direkt 4, erkennen 4) · S2 12 (einkleidung 1, mehrschritt 8, umkehr 3) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 2 | 2 |
| anwenden | 6/12/6 | S1 7 (direkt 6, erkennen 1) · S2 14 (darstellung 3, einkleidung 2, mehrschritt 9) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 0 | 2 |
| fehler_finden | 6/12/6 | S1 7 (direkt 1, erkennen 6) · S2 14 (einkleidung 1, mehrschritt 12, umkehr 1) · S3 8 (begruenden 2, fehler 3, parameter 1, rueckwaerts 1, verknuepfen 1) | 0 | 2 |

**messen.flaechen_vielecke**

| Lernkarte | vorher (S1/S2/S3, ohne Typ) | nachher mit Typ (ohne überzählige) | überzählig | Knobel |
|---|---|---|---|---|
| parallelogramm | 4/6/8 | S1 4 (direkt 2, erkennen 2) · S2 6 (darstellung 2, einkleidung 2, mehrschritt 2) · S3 8 (begruenden 1, fehler 1, pruefung 1, rueckwaerts 1, transfer 3, verknuepfen 1) | 0 | 2 |
| dreieck | 4/6/8 | S1 5 (direkt 4, erkennen 1) · S2 6 (darstellung 3, einkleidung 1, mehrschritt 2) · S3 8 (begruenden 1, fehler 1, pruefung 1, rueckwaerts 1, transfer 3, verknuepfen 1) | 0 | 2 |
| trapez | 4/6/8 | S1 4 (direkt 3, erkennen 1) · S2 6 (darstellung 1, einkleidung 3, mehrschritt 2) · S3 8 (begruenden 1, fehler 1, pruefung 1, rueckwaerts 1, transfer 3, verknuepfen 1) | 1 | 2 |
| rueckwaerts | 4/6/8 | S1 4 (direkt 2, erkennen 2) · S2 6 (darstellung 1, einkleidung 2, mehrschritt 3) · S3 8 (pruefung 1, rueckwaerts 2, transfer 2, verknuepfen 3) | 0 | 2 |
| zusammengesetzt | 4/6/8 | S1 5 (direkt 4, erkennen 1) · S2 6 (darstellung 3, einkleidung 2, mehrschritt 1) · S3 8 (pruefung 1, rueckwaerts 2, transfer 3, verknuepfen 2) | 0 | 2 |
| oberflaeche | 4/6/8 | S1 4 (direkt 2, erkennen 2) · S2 6 (darstellung 3, einkleidung 2, mehrschritt 1) · S3 8 (begruenden 1, pruefung 2, transfer 3, verknuepfen 2) | 0 | 2 |
| verstehen | 4/6/8 | S1 5 (direkt 1, erkennen 4) · S2 7 (einkleidung 2, mehrschritt 4, umkehr 1) · S3 8 (begruenden 2, fehler 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 0 | 2 |

**messen.volumen**

| Lernkarte | vorher (S1/S2/S3, ohne Typ) | nachher mit Typ (ohne überzählige) | überzählig | Knobel |
|---|---|---|---|---|
| einheitswuerfel | 4/6/8 | S1 4 (direkt 2, erkennen 2) · S2 6 (einkleidung 2, mehrschritt 3, umkehr 1) · S3 8 (pruefung 2, rueckwaerts 1, transfer 3, verknuepfen 2) | 0 | 2 |
| quader | 4/6/8 | S1 5 (direkt 4, erkennen 1) · S2 6 (darstellung 2, einkleidung 1, mehrschritt 3) · S3 8 (parameter 1, pruefung 2, rueckwaerts 2, transfer 2, verknuepfen 1) | 0 | 2 |
| einheiten | 4/6/8 | S1 5 (direkt 4, erkennen 1) · S2 6 (darstellung 1, mehrschritt 4, umkehr 1) · S3 8 (begruenden 1, fehler 1, pruefung 2, rueckwaerts 1, transfer 3) | 1 | 2 |
| liter | 4/6/8 | S1 5 (direkt 4, erkennen 1) · S2 6 (darstellung 1, einkleidung 4, mehrschritt 1) · S3 8 (begruenden 1, pruefung 2, rueckwaerts 1, transfer 3, verknuepfen 1) | 0 | 2 |
| rueckwaerts | 4/6/8 | S1 4 (direkt 2, erkennen 2) · S2 6 (darstellung 1, einkleidung 3, mehrschritt 2) · S3 8 (pruefung 2, rueckwaerts 2, transfer 2, verknuepfen 2) | 0 | 2 |
| zusammengesetzt | 4/6/8 | S1 4 (direkt 3, erkennen 1) · S2 7 (darstellung 1, einkleidung 2, mehrschritt 4) · S3 8 (fehler 1, pruefung 2, transfer 3, verknuepfen 2) | 2 | 2 |
| verstehen | 4/6/8 | S1 5 (direkt 1, erkennen 4) · S2 6 (einkleidung 2, mehrschritt 3, umkehr 1) · S3 8 (begruenden 3, pruefung 1, transfer 3, verknuepfen 1) | 0 | 2 |

**bruch.prozent**

| Lernkarte | vorher (S1/S2/S3, ohne Typ) | nachher mit Typ (ohne überzählige) | überzählig | Knobel |
|---|---|---|---|---|
| prozent_bedeutung | 6/14/4 | S1 6 (direkt 4, erkennen 2) · S2 14 (darstellung 2, einkleidung 1, mehrschritt 11) · S3 8 (begruenden 2, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2) | 2 | 2 |
| prozentwert | 6/13/5 | S1 7 (direkt 6, erkennen 1) · S2 10 (darstellung 1, einkleidung 2, mehrschritt 7) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 4 | 2 |
| prozentsatz | 6/13/5 | S1 4 (direkt 3, erkennen 1) · S2 14 (darstellung 1, einkleidung 8, mehrschritt 5) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, transfer 3, verknuepfen 1) | 5 | 2 |
| grundwert | 6/14/4 | S1 5 (direkt 4, erkennen 1) · S2 13 (einkleidung 5, mehrschritt 6, umkehr 2) · S3 8 (begruenden 1, fehler 1, parameter 1, rueckwaerts 1, transfer 3, verknuepfen 1) | 3 | 2 |
| rabatt_aufschlag | 6/11/7 | S1 7 (direkt 6, erkennen 1) · S2 12 (einkleidung 8, mehrschritt 3, umkehr 1) · S3 8 (begruenden 1, parameter 1, pruefung 1, rueckwaerts 2, transfer 3) | 0 | 2 |
| zinsen | 6/12/6 | S1 4 (direkt 3, erkennen 1) · S2 9 (einkleidung 4, mehrschritt 2, umkehr 3) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 2, transfer 1, verknuepfen 1) | 9 | 2 |
| verstehen | 6/16/8 | S1 7 (direkt 1, erkennen 6) · S2 15 (darstellung 1, einkleidung 9, mehrschritt 5) · S3 8 (begruenden 2, fehler 3, rueckwaerts 1, transfer 1, verknuepfen 1) | 1 | 2 |

**finanzen.zinsen**

| Lernkarte | vorher (S1/S2/S3, ohne Typ) | nachher mit Typ (ohne überzählige) | überzählig | Knobel |
|---|---|---|---|---|
| begriffe | 4/6/4 | S1 4 (direkt 1, erkennen 3) · S2 6 (einkleidung 3, mehrschritt 1, umkehr 2) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 3 | 2 |
| rollen | 4/8/4 | S1 5 (direkt 1, erkennen 4) · S2 7 (einkleidung 4, mehrschritt 1, umkehr 2) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 1 | 2 |
| jahreszinsen | 4/6/4 | S1 4 (direkt 3, erkennen 1) · S2 6 (einkleidung 2, mehrschritt 3, umkehr 1) · S3 8 (begruenden 2, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 1, verknuepfen 1) | 4 | 2 |
| jahreszinsen_komma | 4/6/4 | S1 4 (direkt 3, erkennen 1) · S2 6 (einkleidung 3, mehrschritt 1, umkehr 2) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 4 | 2 |
| zinssatz | 4/5/4 | S1 4 (direkt 3, erkennen 1) · S2 6 (einkleidung 3, mehrschritt 2, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 3 | 2 |
| kapital | 4/6/4 | S1 4 (direkt 3, erkennen 1) · S2 8 (einkleidung 5, mehrschritt 2, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 3 | 2 |
| monatszinsen | 4/7/4 | S1 4 (direkt 3, erkennen 1) · S2 7 (einkleidung 5, mehrschritt 1, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 3 | 2 |
| zeitanteil | 5/5/4 | S1 5 (direkt 4, erkennen 1) · S2 7 (einkleidung 4, mehrschritt 2, umkehr 1) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 1 | 2 |

**daten.darstellen**

| Lernkarte | vorher (S1/S2/S3, ohne Typ) | nachher mit Typ (ohne überzählige) | überzählig | Knobel |
|---|---|---|---|---|
| absolute_haeufigkeit | 9/10/5 | S1 7 (direkt 6, erkennen 1) · S2 10 (darstellung 4, einkleidung 5, mehrschritt 1) · S3 8 (begruenden 1, fehler 1, pruefung 1, rueckwaerts 1, transfer 3, verknuepfen 1) | 2 | 2 |
| relative_haeufigkeit | 6/12/6 | S1 7 (direkt 6, erkennen 1) · S2 10 (darstellung 1, einkleidung 2, mehrschritt 5, umkehr 2) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 3 | 2 |
| tabelle_auswerten | 6/13/5 | S1 7 (direkt 1, erkennen 6) · S2 15 (darstellung 7, einkleidung 1, mehrschritt 7) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 0 | 2 |
| saeulendiagramm | 6/12/6 | S1 4 (direkt 2, erkennen 2) · S2 11 (darstellung 6, einkleidung 1, mehrschritt 4) · S3 8 (begruenden 1, fehler 1, parameter 2, rueckwaerts 2, transfer 1, verknuepfen 1) | 3 | 2 |
| kreisdiagramm | 6/12/6 | S1 4 (direkt 3, erkennen 1) · S2 11 (darstellung 3, einkleidung 1, mehrschritt 7) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 2, transfer 2) | 3 | 2 |
| irrefuehrend | 6/11/7 | S1 7 (direkt 1, erkennen 6) · S2 9 (darstellung 3, einkleidung 1, mehrschritt 5) · S3 8 (begruenden 3, fehler 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 3 | 2 |

**daten.kennwerte**

| Lernkarte | vorher (S1/S2/S3, ohne Typ) | nachher mit Typ (ohne überzählige) | überzählig | Knobel |
|---|---|---|---|---|
| mittelwert | 6/13/5 | S1 6 (direkt 4, erkennen 2) · S2 12 (darstellung 4, einkleidung 6, mehrschritt 2) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 2 | 2 |
| mittel_tabelle | 6/12/6 | S1 7 (direkt 6, erkennen 1) · S2 9 (darstellung 7, einkleidung 1, mehrschritt 1) · S3 8 (begruenden 1, fehler 2, parameter 1, pruefung 1, rueckwaerts 1, transfer 1, verknuepfen 1) | 5 | 2 |
| mittel_rueckwaerts | 6/12/6 | S1 4 (direkt 3, erkennen 1) · S2 11 (einkleidung 6, mehrschritt 3, umkehr 2) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 7 | 2 |
| modal_spannweite | 6/13/5 | S1 5 (direkt 4, erkennen 1) · S2 12 (einkleidung 2, mehrschritt 9, umkehr 1) · S3 8 (begruenden 2, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 1, verknuepfen 1) | 4 | 2 |
| median | 6/13/5 | S1 5 (direkt 4, erkennen 1) · S2 12 (darstellung 1, einkleidung 1, mehrschritt 10) · S3 8 (begruenden 1, fehler 1, parameter 1, pruefung 1, rueckwaerts 1, transfer 2, verknuepfen 1) | 4 | 2 |
| verstehen | 6/11/7 | S1 5 (direkt 1, erkennen 4) · S2 11 (einkleidung 2, mehrschritt 8, umkehr 1) · S3 8 (begruenden 3, fehler 2, parameter 1, pruefung 1, transfer 1) | 4 | 2 |

### (4) Überzählig (ohne g; zum Sperren) – Fragetexte je Lernkarte, getrennt durch ‖
- bruch.brueche / bruchteil_von: Berechne 1/2 von 6 m. ‖ Wie viele Minuten sind 3/4 Stunde?
- bruch.brueche / ganzes_bestimmen: 9 Kinder sind 1/9 aller Kinder auf dem Schulhof. Wie viele Kinder sind auf dem Schulhof? ‖ Ein Wassertank ist zu 5/6 gefüllt und enthält 300 l. Wie viele Liter passen in den vollen Tank?
- bruch.brueche / erweitern: Erweitere 2/5 mit 2. ‖ Erweitere 8/9 mit 9. ‖ Erweitere 2/7 mit 6. ‖ Erweitere 1/2 mit 6. ‖ Ergänze: 1/4 = □/8 ‖ Ergänze: 5/7 = □/42 ‖ Mit welcher Zahl wurde 8/9 erweitert, wenn 56/63 herauskommt? ‖ Ergänze: 7/12 = □/60
- bruch.brueche / kuerzen: Kürze 12/15 mit 3. ‖ Kürze 6/12 mit 6. ‖ Kürze 15/27 mit 3. ‖ Kürze 10/25 mit 5. ‖ Kürze 20/45 vollständig. ‖ Kürze 8/10 vollständig. ‖ Kürze 3/6 vollständig. ‖ Kürze 10/15 vollständig. ‖ Kürze 175/325 vollständig. ‖ Kürze 42/56 vollständig. ‖ Kürze 64/80 vollständig.
- bruch.brueche / gemischte_zahlen: Schreibe 4 5/6 als unechten Bruch. ‖ Schreibe 23/8 als gemischte Zahl.
- bruch.brueche / vergleichen: Welcher Bruch ist größer: 4/14 oder 9/14? ‖ Welcher Bruch ist größer: 2/12 oder 2/4? ‖ Welcher Bruch ist größer: 14/15 oder 9/15? ‖ Welcher Bruch ist größer: 7/8 oder 6/8? ‖ Welcher Bruch ist größer: 1/3 oder 1/2? ‖ Welcher Bruch ist größer: 2/3 oder 2/7? ‖ Welcher Bruch ist größer: 4/9 oder 3/5? ‖ Welcher Bruch ist größer: 5/8 oder 7/12? ‖ Bestimme den Hauptnenner von 7/15 und 9/20 mit der Primfaktorzerlegung. ‖ Welcher Bruch ist größer: 7/12 oder 11/18?
- bruch.brueche / zahlenstrahl: Markiere 1/3 am Zahlenstrahl (von 0 bis 1, 3 gleiche Teile). ‖ Markiere 1/2 am Zahlenstrahl (von 0 bis 1, 2 gleiche Teile). ‖ Markiere 3/10 am Zahlenstrahl (von 0 bis 1, 10 gleiche Teile). ‖ Markiere 2/9 am Zahlenstrahl (von 0 bis 1, 9 gleiche Teile). ‖ Markiere 5/3 am Zahlenstrahl (von 0 bis 2, 6 gleiche Teile). ‖ Markiere 2/3 am Zahlenstrahl (von 0 bis 1, 6 gleiche Teile). ‖ Markiere 6/5 am Zahlenstrahl (von 0 bis 2, 10 gleiche Teile). ‖ Markiere 1/6 am Zahlenstrahl (von 0 bis 1, 12 gleiche Teile). ‖ Markiere 1/4 am Zahlenstrahl (von 0 bis 2, 16 gleiche Teile). ‖ Markiere 3/4 am Zahlenstrahl (von 0 bis 2, 16 gleiche Teile). ‖ Markiere 3/2 am Zahlenstrahl (von 0 bis 3, 12 gleiche Teile). ‖ Markiere 2/5 am Zahlenstrahl (von 0 bis 1, 10 gleiche Teile).
- bruch.brueche / verstehen: Stimmt die Aussage? „1/8 ist größer als 1/2, weil 8 > 2.“ ‖ Stimmt die Aussage? „3/5 von 55 sind 44.“ ‖ Stimmt die Aussage? „Zwischen 1/3 und 1/2 liegt kein weiterer Bruch.“
- bruch.dezimal / stellenwerte: Welche Zahl steht in der Stellenwerttafel? ‖ Welche Zahl steht in der Stellenwerttafel? ‖ Schreibe als Dezimalzahl: 9 + 7/100 + 2/1 000
- bruch.dezimal / vergleichen_ordnen: Welche Zahl ist größer: 0,5 oder 0,23? ‖ Welche Zahl ist größer: 6,6 oder 6,26? ‖ Welche Zahl ist größer: 0,4 oder 0,59? ‖ Welche Zahl ist größer: 3,4 oder 3,73? ‖ Markiere 8,6 am Zahlenstrahl (von 8 bis 9, 10 gleiche Teile). ‖ Markiere 4,44 am Zahlenstrahl (von 4,4 bis 4,5, 10 gleiche Teile). ‖ Markiere 2,83 am Zahlenstrahl (von 2,8 bis 2,9, 10 gleiche Teile). ‖ Markiere 4,78 am Zahlenstrahl (von 4,7 bis 4,8, 10 gleiche Teile). ‖ Markiere 2,17 am Zahlenstrahl (von 2,1 bis 2,2, 10 gleiche Teile). ‖ Markiere 0,35 am Zahlenstrahl (von 0 bis 0,5, 10 gleiche Teile).
- bruch.dezimal / runden: Runde 38,4 auf Ganze. ‖ Runde 45,56 auf Zehntel. ‖ Runde 3,6286 auf Hundertstel. ‖ Runde 6,9321 auf Hundertstel. ‖ Runde 3,249 auf Zehntel. ‖ Runde 6,348 auf Zehntel. ‖ Runde 0,0738 auf Tausendstel. ‖ Runde 7,996 auf Hundertstel.
- bruch.dezimal / bruch_zu_dezimal: Schreibe 1/5 als Dezimalzahl. ‖ Schreibe 1/4 als Dezimalzahl. ‖ Schreibe 1/2 als Dezimalzahl. ‖ Schreibe 14/25 als Dezimalzahl. ‖ Schreibe 5/4 als Dezimalzahl. ‖ Welche Dezimalzahl ist gleich 15/8? ‖ Schreibe 9/12 als Dezimalzahl. ‖ Schreibe 99/220 als Dezimalzahl. ‖ Berechne 2/5 + 1,4 und gib das Ergebnis als Dezimalzahl an. ‖ Berechne 7/4 + 0,2 und gib das Ergebnis als Dezimalzahl an. ‖ Schreibe 13/50 als Dezimalzahl.
- bruch.dezimal / dezimal_zu_bruch: Schreibe 0,3 als vollständig gekürzten Bruch. ‖ Schreibe 0,9 als vollständig gekürzten Bruch. ‖ Schreibe 0,4 als vollständig gekürzten Bruch. ‖ Schreibe 0,6 als vollständig gekürzten Bruch. ‖ Schreibe 0,399 als vollständig gekürzten Bruch. ‖ Schreibe 3,333 als vollständig gekürzten Bruch. Ein Bruch größer als 1 ist erlaubt. ‖ Schreibe 3,09 als vollständig gekürzten Bruch. Ein Bruch größer als 1 ist erlaubt. ‖ Schreibe 4,97 als vollständig gekürzten Bruch. Ein Bruch größer als 1 ist erlaubt. ‖ Schreibe 1,96 als vollständig gekürzten Bruch. Ein Bruch größer als 1 ist erlaubt. ‖ Schreibe 0,85 als vollständig gekürzten Bruch. ‖ Schreibe 2,4 als vollständig gekürzten Bruch. Ein Bruch größer als 1 ist erlaubt.
- bruch.dezimal / periodisch: Ist 7/30 als Dezimalzahl endlich oder periodisch? ‖ Welche Dezimalzahl ist gleich 37/30? ‖ Welche Dezimalzahl ist gleich 13/12? ‖ Welche Dezimalzahl ist gleich 10/7? ‖ Welche Dezimalzahl ist gleich 23/15? ‖ Welche Dezimalzahl ist gleich 20/11? ‖ Welche Dezimalzahl ist gleich 5/6? ‖ Ist 7/40 als Dezimalzahl endlich oder periodisch?
- bruch.dezimal / verstehen: Stimmt die Aussage? „6,11 ist größer als 6,7, weil die Zahl hinter dem Komma größer ist.“ ‖ Stimmt die Aussage? „3,1 und 3,10 sind gleich groß.“
- bruch.rechnen / brueche_plus_minus: Berechne 1/2 − 1/4. ‖ Berechne 5/6 − 5/12. ‖ Berechne 5/6 − 7/12. ‖ Berechne 7/9 − 1/12. ‖ Berechne 3 − 8/9 − 3/7. ‖ Berechne 5/6 − 3/8.
- bruch.rechnen / dezimal_plus_minus: Berechne 3,5 + 15,7. ‖ Berechne 18,37 − 9,61. ‖ Berechne 31,14 − 18,3. ‖ Ein Einkauf kostet 7,51 €, 8,49 €, 12,07 €. Bezahlt wird mit einem 100-€-Schein. Wie viel Euro gibt es zurück? ‖ Ein Einkauf kostet 0,72 €, 6,46 €, 13,74 €. Bezahlt wird mit einem 100-€-Schein. Wie viel Euro gibt es zurück? ‖ Berechne 12 − 3,47. ‖ Berechne 0,6 + 0,45 + 0,055.
- bruch.rechnen / vorzeichen: Berechne (−7,7) + 0,6.
- bruch.rechnen / brueche_mal: Berechne 6/7 · 8. ‖ Berechne 4/5 · 2. ‖ Berechne 5/7 · 3. ‖ Berechne 1/35 · 7/4. Kürze vorher. ‖ Berechne 1/2 · 6/5. Kürze vorher. ‖ Berechne 3/40 · 8/3. Kürze vorher. ‖ Berechne 1/4 · 16/3. Kürze vorher. ‖ In einer Flasche sind 3/8 l Saft. Davon wird 1/5 getrunken. Wie viele Liter sind das? ‖ In einer Flasche sind 1/4 l Saft. Davon wird 1/2 getrunken. Wie viele Liter sind das? ‖ Berechne 2/3 · 9/16. Kürze vorher.
- bruch.rechnen / brueche_geteilt: Berechne 3/8 : 3. ‖ Berechne 3/4 : 3. ‖ Berechne 1/3 : 5/8. ‖ Berechne 2/3 : 3/5. ‖ Berechne 1/3 : 3/7. ‖ Berechne 3/4 : 4/5. ‖ Ein Rechteck hat den Flächeninhalt 8/15 m² und ist 2/3 m breit. Wie lang ist es? ‖ Berechne 5/6 : 10/9.
- bruch.rechnen / dezimal_mal: Berechne 4,7 · 9. ‖ Berechne 1,1 · 10. ‖ Berechne 8,8 · 10. ‖ Berechne 1,5 · 6. ‖ Berechne 8,57 · 0,8. ‖ Berechne 3,85 · 1,5. ‖ Berechne 2,1 · 0,4. ‖ Berechne 6,93 · 1,7. ‖ Ein Kilogramm Äpfel kostet 1,94 €. Was kosten 4,3 kg? Runde auf Cent. ‖ Was ergibt 0,2 · 0,05? ‖ Berechne 0,25 · 0,36. ‖ Berechne 12,5 · 0,08.
- bruch.rechnen / dezimal_geteilt: Berechne 4 : 5. ‖ Berechne 24,6 : 100. ‖ Berechne 29,4 : 7. ‖ Berechne 11,6 : 2. ‖ Berechne 4,96 : 0,8. ‖ Berechne 0,924 : 0,84. ‖ Berechne 21,08 : 0,68. ‖ Berechne 0,7 : 0,5. ‖ Berechne 1,8 : 0,06. ‖ Berechne 0,09 : 0,3.
- bruch.rechnen / rechenvorteile: Berechne geschickt: 15,1 · 0,25 · 4 ‖ Berechne geschickt: 5 · 0,2 · 14,8 ‖ Berechne geschickt: 5 · 0,2 · 12,6 ‖ Berechne geschickt: 4 · 3,3 · 0,25 ‖ Berechne geschickt: 3/8 · 2 · 1/2 ‖ Berechne geschickt: 2/5 · 17 · 5/2
- bruch.rechnen / gemischt: Berechne 3,7 + 3 · 6,2. ‖ Berechne 8,4 + 4 · 6,9. ‖ Berechne 4,2 + 6 · 7,5. ‖ Berechne 0,1 + 5 · 3,8. ‖ Berechne 1/4 + 1/5 · 3/2. Gib das Ergebnis als Dezimalzahl an. ‖ Berechne (1/5 + 1/4) · 0,5. Gib das Ergebnis als Dezimalzahl an. ‖ Berechne 3/2 · 5/2 − 1/8 · 1/5. Gib das Ergebnis als Dezimalzahl an.
- bruch.rechnen / fehler_finden: Stimmt die Aussage? „1,4 · 0,2 ist größer als 1,4.“ ‖ Ein Kind rechnet: 1/3 : 2/3 = 3/1 · 2/3. Was ist der Fehler? ‖ Ein Kind rechnet: 3/4 + 2/7 = 5/11. Was ist der Fehler? ‖ Ein Kind rechnet: 2/3 + 1/4 = 3/7. Was ist der Fehler? ‖ Ein Kind rechnet: 2/3 + 1/2 = 3/5. Was ist der Fehler? ‖ Ein Kind rechnet: 1/2 : 3/5 = 2/1 · 3/5. Was ist der Fehler? ‖ Ein Kind rechnet 7,2 : 0,9 = 0,8. Wie heißt das richtige Ergebnis? ‖ Ein Kind rechnet 2 − 1/3 · 3 = 5/3 · 3 = 5. Wie heißt das richtige Ergebnis?
- bruch.rechnen / sach: Wie viel ist 3/5 von 5/6?
- zahlen.potenzen_zehner / gross_wissenschaftlich: 1 630 000 000 = 1,63 · 10ⁿ. Wie groß ist n? ‖ 1 500 000 = 1,5 · 10ⁿ. Wie groß ist n? ‖ 90 000 000 = 9 · 10ⁿ. Wie groß ist n?
- zahlen.potenzen_zehner / vorsilben_gross: Wie viele Kilobyte (kB) sind ein Terabyte (TB)? Schreibe das Ergebnis als 10ⁿ. Wie groß ist n?
- zahlen.potenzen_zehner / negativer_exponent: 0,0000001 = 10ⁿ. Wie groß ist n?
- zahlen.potenzen_zehner / klein_wissenschaftlich: Welche Darstellung von 0,00055 ist die wissenschaftliche Schreibweise? ‖ Welche Darstellung von 0,0008 ist die wissenschaftliche Schreibweise? ‖ Welche Darstellung von 0,033 ist die wissenschaftliche Schreibweise?
- zahlen.potenzen_zehner / vorsilben_klein: Ein Rechenschritt eines Computers dauert 5 ns. Wie viele Schritte schafft er in 1 Sekunde? ‖ Wie viele Nanometer sind ein Millimeter? Schreibe das Ergebnis als 10ⁿ. Wie groß ist n?
- terme.potenzgesetze / gleicher_exponent: Berechne geschickt: 2² · 50² ‖ Berechne geschickt: 2³ · 5³
- messen.flaechen_vielecke / trapez: Berechne den Flächeninhalt des Trapezes mit a = 10 dm, c = 6 dm und h = 8 dm.
- messen.volumen / einheiten: Rechne um: 0,025 m³ = ? cm³
- messen.volumen / zusammengesetzt: Die Stufe besteht aus zwei Quadern: unten 8 dm · 6 dm · 1 dm, oben 2 dm · 6 dm · 2 dm. Wie groß ist ihr Volumen? ‖ Die Stufe besteht aus zwei Quadern: unten 7 dm · 3 dm · 2 dm, oben 2 dm · 3 dm · 2 dm. Wie groß ist ihr Volumen?
- bruch.prozent / prozent_bedeutung: Schreibe 2,44 in Prozent. ‖ Wie viel Prozent sind 7/25?
- bruch.prozent / prozentwert: Berechne 59 % von 1 000 km. ‖ Berechne 1,5 % von 360 €. ‖ Berechne 2,5 % von 320 €. ‖ Berechne 150 % von 36 €.
- bruch.prozent / prozentsatz: Wie viel Prozent sind 73 von 200? ‖ Wie viel Prozent sind 31 von 100? ‖ Wie viel Prozent sind 19 von 20? ‖ Wie viel Prozent sind 101 von 200? ‖ In einem Verein sind 30 Mädchen und 24 Jungen. Um wie viel Prozent sind es weniger Jungen als Mädchen?
- bruch.prozent / grundwert: 20 % sind 188 €. Wie viel sind 100 %? ‖ 10 % sind 52 €. Wie viel sind 100 %? ‖ 60 Kinder einer Schule fahren mit dem Bus. Das sind 25 % aller Kinder. Wie viele Kinder hat die Schule?
- bruch.prozent / zinsen: Ein Kapital von 500 € wird ein Jahr lang zu 2 % angelegt. Wie viel Euro Zinsen gibt es? ‖ Ein Kapital von 300 € wird ein Jahr lang zu 4 % angelegt. Wie viel Euro Zinsen gibt es? ‖ Ein Kapital von 2 000 € wird ein Jahr lang zu 1 % angelegt. Wie viel Euro Zinsen gibt es? ‖ Ein Kapital von 1 500 € wird ein Jahr lang zu 5 % angelegt. Wie viel Euro Zinsen gibt es? ‖ Für 700 € zahlt eine Bank in einem Jahr 17,5 € Zinsen. Wie hoch ist der Zinssatz? ‖ Für 700 € zahlt eine Bank in einem Jahr 28 € Zinsen. Wie hoch ist der Zinssatz? ‖ Für 3 000 € zahlt eine Bank in einem Jahr 60 € Zinsen. Wie hoch ist der Zinssatz? ‖ Bank A zahlt 2 %, Bank B zahlt 3 % Zinsen im Jahr. Wie viel Euro mehr Zinsen bringt die bessere Bank für 2 000 € in einem Jahr? ‖ 2 600 € werden nur 3 Monate lang zu 3 % (pro Jahr) angelegt. Wie viel Euro Zinsen gibt es?
- bruch.prozent / verstehen: Stimmt die Aussage? „Bei 3 % Zinsen bekommt man für 5 000 € in einem Jahr 150 € Zinsen.“
- finanzen.zinsen / begriffe: Jemand legt 4 800 € für ein Jahr auf ein Sparkonto. Die Bank zahlt 3 % Zinsen pro Jahr, das sind 144 €. Was ist hier der Jahreszinssatz? ‖ Jemand legt 4 100 € für ein Jahr auf ein Sparkonto. Die Bank zahlt 4 % Zinsen pro Jahr, das sind 164 €. Was ist hier der Jahreszinssatz? ‖ Auf einem Sparkonto liegen 3 600 €. Nach einem Jahr gibt die Bank 180 € Zinsen dazu. Wie viel Geld ist dann auf dem Konto?
- finanzen.zinsen / rollen: Du leihst dir 1 500 € von der Bank. Nach einem Jahr zahlst du 1 635 € zurück. Wie viel Zinsen hast du gezahlt?
- finanzen.zinsen / jahreszinsen: Berechne die Jahreszinsen für 2 200 € bei 4 % Jahreszinssatz. ‖ Berechne die Jahreszinsen für 3 000 € bei 9 % Jahreszinssatz. ‖ Berechne die Jahreszinsen für 1 480 € bei 4 % Jahreszinssatz. ‖ Berechne die Jahreszinsen für 5 630 € bei 7 % Jahreszinssatz.
- finanzen.zinsen / jahreszinsen_komma: Berechne die Jahreszinsen für 3 200 € bei 2,5 % Jahreszinssatz. ‖ Berechne die Jahreszinsen für 2 500 € bei 2,5 % Jahreszinssatz. ‖ Berechne die Jahreszinsen für 2 500 € bei 3,25 % Jahreszinssatz. ‖ Berechne die Jahreszinsen für 600 € bei 1,5 % Jahreszinssatz.
- finanzen.zinsen / zinssatz: 2 800 € bringen in einem Jahr 112 € Zinsen. Wie hoch ist der Jahreszinssatz in Prozent? ‖ 2 700 € bringen in einem Jahr 108 € Zinsen. Wie hoch ist der Jahreszinssatz in Prozent? ‖ 1 700 € bringen in einem Jahr 127,50 € Zinsen. Wie hoch ist der Jahreszinssatz in Prozent?
- finanzen.zinsen / kapital: Bei 2 % Jahreszinssatz bringt ein Kapital in einem Jahr 106 € Zinsen. Wie groß ist das Kapital? ‖ Bei 8 % Jahreszinssatz bringt ein Kapital in einem Jahr 152 € Zinsen. Wie groß ist das Kapital? ‖ Bei 6 % Jahreszinssatz bringt ein Kapital in einem Jahr 258,60 € Zinsen. Wie groß ist das Kapital?
- finanzen.zinsen / monatszinsen: Berechne die Zinsen für 5 400 € bei 4 % Jahreszinssatz für 4 Monate. ‖ Berechne die Zinsen für 6 900 € bei 4 % Jahreszinssatz für 4 Monate. ‖ Berechne die Zinsen für 7 200 € bei 3 % Jahreszinssatz für 9 Monate.
- finanzen.zinsen / zeitanteil: 1 200 € liegen ein halbes Jahr zu 6 % Jahreszinssatz auf einem Konto. Wie viel Zinsen gibt es?
- daten.darstellen / absolute_haeufigkeit: Würfelergebnisse: 4, 1, 6, 4, 4, 1, 4, 1, 5, 3, 4. Wie oft wurde die 5 gewürfelt? ‖ Würfelergebnisse: 5, 5, 1, 3, 1, 3, 3, 3, 3, 6, 5. Wie oft wurde die 1 gewürfelt?
- daten.darstellen / relative_haeufigkeit: 117 von 200 Pflanzen blühen. Gib die relative Häufigkeit in Prozent an. ‖ 78 von 125 Besuchern kommen aus der Stadt. Gib die relative Häufigkeit in Prozent an. ‖ Bei 20 Münzwürfen lag die relative Häufigkeit für „Zahl“ bei 5 %. Wie oft fiel „Zahl“?
- daten.darstellen / saeulendiagramm: In einem Säulendiagramm steht 1 cm für 10 Kinder. Wie hoch wird die Säule für 35 Kinder? ‖ In einem Säulendiagramm steht 1 cm für 4 Kinder. Wie hoch wird die Säule für 18 Kinder? ‖ Das Säulendiagramm zeigt eine Umfrage zum Thema Haustier. Wie viele Kinder wurden befragt?
- daten.darstellen / kreisdiagramm: Wie groß ist der Winkel für 55 % im Kreisdiagramm? ‖ Wie groß ist der Winkel für 10 % im Kreisdiagramm? ‖ 2 von 36 Befragten wählen „ja“. Wie groß ist der Winkel im Kreisdiagramm?
- daten.darstellen / irrefuehrend: Ein Säulendiagramm zeigt 1 005 und 1 025 Besucher. Die Hochachse beginnt bei 1 000. Wie viel Mal so hoch wirkt die zweite Säule? ‖ Ein Säulendiagramm zeigt 525 und 550 Besucher. Die Hochachse beginnt bei 500. Wie viel Mal so hoch wirkt die zweite Säule? ‖ Ein Säulendiagramm zeigt 525 und 575 Besucher. Die Hochachse beginnt bei 500. Wie viel Mal so hoch wirkt die zweite Säule?
- daten.kennwerte / mittelwert: Gruppe A sammelt 4 kg, 6 kg, 2 kg, 2 kg Altpapier, Gruppe B 8 kg, 11 kg, 9 kg, 2 kg. Welche Gruppe hat im Mittel mehr gesammelt? ‖ Gruppe A sammelt 5 kg, 12 kg, 10 kg, 9 kg Altpapier, Gruppe B 2 kg, 9 kg, 11 kg, 2 kg. Welche Gruppe hat im Mittel mehr gesammelt?
- daten.kennwerte / mittel_tabelle: Die Tabelle zeigt einen Notenspiegel. Berechne die Durchschnittsnote. ‖ Die Tabelle zeigt die Umfrage „Wie viele Geschwister hast du?“. Wie viele Geschwister hat ein Kind im Mittel? ‖ Die Tabelle zeigt die Umfrage „Wie viele Geschwister hast du?“. Wie viele Geschwister hat ein Kind im Mittel? ‖ Die Tabelle zeigt, wie viele Tore eine Mannschaft in ihren Spielen geschossen hat. Wie viele Tore schießt sie im Mittel pro Spiel? ‖ Die Tabelle zeigt einen Notenspiegel. Berechne die Durchschnittsnote.
- daten.kennwerte / mittel_rueckwaerts: 4 Kinder haben im Mittel 18 Bücher gelesen. Wie viele Bücher sind das zusammen? ‖ 3 Kinder haben im Mittel 13 Bücher gelesen. Wie viele Bücher sind das zusammen? ‖ 6 Kinder haben im Mittel 11 Bücher gelesen. Wie viele Bücher sind das zusammen? ‖ 4 Kinder haben im Mittel 11 Bücher gelesen. Wie viele Bücher sind das zusammen? ‖ In 4 Tests (je höchstens 30 Punkte) hat ein Kind im Mittel 22 Punkte. Bekannt sind 17, 24, 30 Punkte. Wie viele Punkte hatte es im fehlenden Test? ‖ In 4 Tests (je höchstens 30 Punkte) hat ein Kind im Mittel 11 Punkte. Bekannt sind 3, 16, 6 Punkte. Wie viele Punkte hatte es im fehlenden Test? ‖ In 4 Tests (je höchstens 30 Punkte) hat ein Kind im Mittel 19 Punkte. Bekannt sind 16, 16, 15 Punkte. Wie viele Punkte hatte es im fehlenden Test?
- daten.kennwerte / modal_spannweite: Bestimme die Spannweite von 144, 129, 125, 120, 132, 160, 125. ‖ Bestimme den Modalwert von 42, 41, 37, 37, 37, 33, 35. ‖ Bestimme die Spannweite von 2, 6, 6, 8, 7, 7, 5, 4, 2, 6. ‖ Bestimme die Spannweite von 124, 139, 151, 148, 157, 160, 122, 157, 155, 141, 144, 121.
- daten.kennwerte / median: Bestimme den Median von 21, 37, 7, 22, 14. ‖ Bestimme den Median von 20, 27, 2, 23, 1, 32, 31. ‖ Bestimme den Median von 21, 11, 20, 40, 33, 7, 32, 30, 39. ‖ Bestimme den Median von 3, 9, 4, 9, 1, 7.
- daten.kennwerte / verstehen: Stimmt die Aussage? „Der Mittelwert von 4, 7, 12, 7, 11 ist 20,5.“ ‖ Stimmt die Aussage? „Der Mittelwert von 11, 11, 6, 11, 10 ist 9,8.“ ‖ Stimmt die Aussage? „Der Mittelwert von 2, 5, 7, 9, 11 ist 17.“ ‖ Stimmt die Aussage? „Die Spannweite von 10, 11, 12, 7 ist 7.“

### Nicht geprüft
- Wie die neuen Bordkarten in der App aussehen (Stufenzeichen, Knobel-Angebot).
- Ob das Einspielen mit `einheit_abgleichen(…, 'lassen')` die Reihenfolge der Übungen übernimmt (in der Datei umsortiert).

### Fakten, Annahmen, Meinung
- **Fakten:** Zahlen aus `/tmp/stufen_<thema>.json` und dem Nachweis; Prüfskript-Ausgaben.
- **Annahmen:** Behandlung der überzähligen (siehe oben); die Typzuordnung der alten Aufgaben ist eine fachliche Einschätzung je Lernkarte.
- **Meinung:** Die stärkste Veränderung haben bruch.rechnen, bruch.dezimal und finanzen.zinsen – dort war Stufe 3 vorher fast nur Rechnen mit größeren Zahlen.

## 2026-11-17 19:30 – STATUS
**daten.kennwerte** fertig: 4 umgestuft, 29 neue Übungen, 12 Knobel-Bordkarten, 26 überzählige. Prüfskript OK, 0 Gruppen, Nachweis OK.

## 2026-11-17 19:10 – STATUS
**daten.darstellen** fertig: 2 umgestuft, 20 neue Übungen, 12 Knobel-Bordkarten, 14 überzählige. Prüfskript OK, 0 Gruppen, Nachweis OK.

## 2026-11-17 18:50 – STATUS
**finanzen.zinsen** fertig: 10 umgestuft, 59 neue Übungen, 16 Knobel-Bordkarten, 22 überzählige. Prüfskript OK, 0 Gruppen, Nachweis OK. Knobel ohne Zinseszins (Modell der Karten).

## 2026-11-17 18:25 – STATUS
**bruch.prozent** fertig: 3 umgestuft, 33 neue Übungen, 14 Knobel-Bordkarten, 24 überzählige. Prüfskript OK, 0 Gruppen, Nachweis OK.

## 2026-11-17 18:05 – STATUS
**messen.volumen** fertig: 2 umgestuft, 8 neue Übungen, 14 Knobel-Bordkarten, 3 überzählige. Prüfskript OK, 0 Gruppen, Nachweis OK.

## 2026-11-17 18:00 – STATUS
**messen.flaechen_vielecke** fertig: Typen vergeben (die Prüfungsvorbild-Aufgaben der Achtzehnten Runde als „pruefung“), 5 neue Übungen, 14 Knobel-Bordkarten, 1 überzählige. Prüfskript OK, 0 Gruppen, Nachweis OK.

## 2026-11-17 17:35 – STATUS
**terme.potenzgesetze** fertig: 10 umgestuft, 35 neue Übungen, 14 Knobel-Bordkarten, 2 überzählige. Prüfskript OK, 0 Gruppen, Nachweis OK.

## 2026-11-17 17:15 – STATUS
**zahlen.potenzen_zehner** fertig: 6 umgestuft, 22 neue Übungen, 14 Knobel-Bordkarten, 10 überzählige. Prüfskript OK, 0 Gruppen, Nachweis OK.

## 2026-11-17 16:50 – STATUS
**bruch.rechnen** fertig: 17 umgestuft, 70 neue Übungen, 24 Knobel-Bordkarten, 76 überzählige. Prüfskript OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 16:05 – STATUS
**bruch.dezimal** fertig: 14 umgestuft, 50 neue Übungen, 16 Knobel-Bordkarten, 54 überzählige. Prüfskript OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 15:30 – STATUS
**bruch.brueche** fertig: jede Übung hat ihren Typ g (13 umgestuft), 55 neue Übungen, 20 Knobel-Bordkarten, 50 überzählige (ohne g, Liste im Abschlussbericht).
Prüfskript OK, 0 Gruppen „gleich gebaut hintereinander“; Nachweis OK (alte Aufgaben nur g/s geändert; Prüfung ohne die überzähligen OK).
Annahme (FRAGE an den Haupt-Chat, ich arbeite so weiter): Überzählige Übungen behalten kein g. Bekämen sie eines, meldete das Prüfskript „mehr als 2 gleich gebaute“ als Fehler.
Ohne g greifen die Typ-Regeln in der Datei nicht für die ganze Lernkarte; deshalb prüft der Nachweis zusätzlich eine Kopie ohne die überzähligen – so, wie es nach dem Sperren ist.
