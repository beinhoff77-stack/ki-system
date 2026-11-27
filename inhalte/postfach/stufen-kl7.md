# Postfach stufen-kl7 (Zwanzigste Runde, Klasse 7)

Neueste Meldung oben.

## 2026-11-18 – STATUS: Prüfung aller neuen Aufgaben Kl. 7
Stand: `origin/lernen-app` (76beb1d) in `stufen-kl7` geholt (Fast-Forward, keine Konflikte). „Neu“ = Pool uebung oder bonus, Fragetext in keiner Themendatei von 4eda8cb.
Geprüft: **454 neue Aufgaben** (315 Übungen, 139 Knobel) in 9 Themen, jede vollständig gelesen (Frage, Optionen, Tipp, Lösungsweg) und nachgerechnet.
Knobel mit „höchstens/mindestens/wie viele/immer“ zusätzlich per Programm geprüft (Klammerungen, Springerzüge, Dreiecke mit Umfang 12, Stäbe, Würfelwürfe, Modalwert-Aufgaben, Parkett, Kino, Fläche): alle Lösungen bestätigt.
Geändert: **47 neue Aufgaben in 8 Themen**, alte Aufgaben Zeichen für Zeichen unverändert, g und s gleich. Je Thema: Prüfskript OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK. geometrie.kreis: alles korrekt, keine Änderung.

| Thema | geprüft | geändert | a | b | c | d | e | f |
|---|---|---|---|---|---|---|---|---|
| terme.aufstellen | 33 | 11 | 0 | 0 | 10 | 0 | 0 | 1 |
| terme.umformen | 99 | 12 | 1 | 0 | 3 | 4 | 1 | 3 |
| abbildungen.kongruenz | 71 | 11 | 1 | 0 | 3 | 2 | 0 | 5 |
| geometrie.winkelsaetze | 52 | 4 | 0 | 0 | 2 | 0 | 1 | 1 |
| gleichungen.linear | 34 | 2 | 0 | 0 | 0 | 0 | 1 | 1 |
| bruch.prozent_grundwert | 42 | 2 | 0 | 0 | 0 | 1 | 0 | 1 |
| daten.boxplot | 48 | 3 | 0 | 0 | 0 | 0 | 0 | 3 |
| geometrie.konstruktion | 41 | 2 | 1 | 0 | 0 | 1 | 0 | 0 |
| geometrie.kreis | 34 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Summe** | **454** | **47** | **3** | **0** | **18** | **8** | **3** | **15** |

**Je Fehlerart ein Beispiel (vorher → nachher)**
- **a) falsch/nicht eindeutig (3):** geometrie.konstruktion/vierecke, Knobel „Parallelogramm, das kein Rechteck ist … die vier Winkelhalbierenden begrenzen sicher ein Rechteck“. Bei einer Raute fallen die Halbierenden auf die Diagonalen und schneiden sich in einem Punkt, dann gibt es kein Viereck. → „Parallelogramm, das weder ein Rechteck noch eine Raute ist“. (Weitere: Drehregel-Probe mit (1 | 0) schloss (y | x) nicht aus; Begründung „2x nicht durch 3 teilbar“ falsch für x = 3.)
- **b) mehrdeutige Zählweise (0):** keine gefunden. In Klasse 7 kommen keine Strich- oder Stellen-Zählungen vor; „an 4. Stelle der geordneten Liste“ ist eindeutig.
- **c) späterer Stoff (18):** terme.aufstellen/uebersetzen, Lösungsweg „a · (x + 2) = ax + 2a“ (Ausmultiplizieren kommt erst in terme.umformen) → „Setze für x eine Zahl ein, z. B. x = 0: 2a = 6, also a = 3; Probe mit x = 1“. Ebenso: Gleichungsumformungen mit Pfeilen vor dem Thema gleichungen.linear durch Rückwärtsrechnen ersetzt; „Potenz einer Potenz“ (4⁵ = 2¹⁰, 100⁵ = 10¹⁰) durch Zählen der Faktoren erklärt; Thales-Aussage in kongruenz, „x = 3“ als Geradenschreibweise → „x-Wert 3“.
- **d) unklare Frage (8):** terme.umformen/binomisch: „Ein quadratischer Platz … wird auf beiden Seiten um 3 m verlängert“ (+3 oder +6?) → „Jede Seite wird um 3 m länger, der Platz bleibt quadratisch“. Weitere: „die Koordinatenachse“ → „die y-Achse“ bzw. „die x-Achse“, „Wie viele verschiedene gleichschenklige Dreiecke“ → „… Winkelkombinationen“, „mindestens beides“ präzisiert.
- **e) Antwortoptionen (3):** gleichungen.linear/probe „In einer Packung sind 9 Stifte – stimmt das?“: Optionen „Nein: 4 · 9 + 3 = 40.“ (falsche Rechnung) und „Ja: 39 : 4 ≈ 9.“ (zweites Ja mit unpassender Begründung) → „Nein: 4 · 10 = 40, also sind es 10 Stifte.“ und „Nein: 39 ist ungerade, das geht mit Packungen nicht.“ Weitere: Option „Exponenten teilen: a⁷ʹ³“ (kaputtes Zeichen) → „Exponenten teilen: 7 : 3“; „denn es sind Wechselwinkel“ → passend zum Lösungsweg.
- **f) Lösungsweg (15):** daten.boxplot/mittel_median, Knobel „Modalwert 3, Median 4, Mittelwert 5“: „(Summe 25, also a + b = 14)“ (Rechenfehler) → „a + b = 25 − 10 = 15“ mit Begründung, warum die 3 auf Platz 1 und 2 steht. Weitere: negative „Abstände zur Achse“ (−7) in 5 Spiegelaufgaben → „P liegt 7 unter der Achse“; falsches Würfelbeispiel (Summe 11 statt 10); „1 + 4 · 50 % = 5“; Lösungswege mit „…“; Pentagramm-Beweis ohne benannte Punkte.

**Technik und Lesarten**
- Änderungen im Generator: STUFEN-Aufgaben direkt an ihrer Quelle. Die beim Bereinigen umformulierten Spiegelaufgaben ändert ein neuer letzter Schritt KORREKTUR (`_korrektur_kl7.py`, in abbildungen.kongruenz.py); er trifft nur neue Aufgaben und rechnet die Lösungswege aus den Zahlen der Aufgabe neu.
- Aus anderen Generatoren umgezogene Karten habe ich an ihrer Quelle geändert: Potenz-Karten in terme.potenzgesetze.py, Kennwert-Aufgaben in daten.kennwerte.py. terme.potenzgesetze.json und daten.kennwerte.json bleiben unverändert.
- Nachweis: Das bisherige `_stufen_nachweis.py` meldet gegen origin/lernen-app jede geänderte neue Aufgabe als Fehler, weil die Zwanzigste Runde dort schon enthalten ist. Deshalb gibt es neu `_pruefung_kl7_nachweis.py <thema>`. Es prüft: alte Aufgaben (Text in 4eda8cb) Zeichen für Zeichen gleich; nur neue Aufgaben geändert; Lernkarte, Pool, g, s und y gleich; alles außerhalb von „aufgaben“ gleich.
- Lesart zu c): Der Maßstab ist die Reihenfolge der Themen. Innerhalb eines Themas ist der Stoff einer späteren Lernkarte erlaubt (z. B. Ausmultiplizieren in terme.umformen). Einfache Schritte wie „3α = 180°, also α = 60°“ in Themen nach gleichungen.linear zählen nicht als späterer Stoff.
- Zwei Themen haben einen Nachtrag-Commit (Lösungswege mit „…“, terme.umformen und geometrie.konstruktion).

**Nicht prüfen konnte ich**
- Grafiken: Ob Bilder (Koordinatensysteme, Boxplots) zu den Texten passen, habe ich nur über die Daten geprüft, nicht als Bild.
- Darstellung in der App, z. B. Lückenaufgaben mit negativen Werten (−3 in „□x + □y“).
- Lehrbuchabhängige Begriffe: ob „Wechselwinkel“ auch für die äußeren Z-Winkel üblich ist und ob das Quadrat im „Haus der Vierecke“ als gleichschenkliges Trapez und Drachenviereck gilt. Ich habe die gängige Festlegung angenommen und nur die Option angepasst, die dem Lösungsweg widersprach.
- Alte Aufgaben (nicht im Umfang).

## 2026-11-17 – ABSCHLUSSBERICHT Zwanzigste Runde (Klasse 7)

Zweig `stufen-kl7`, 9 Themen, je ein Commit. Alle Themen: `python3 -I tools/inhalt_pruefen.py` OK ohne Typfehler, 0 Gruppen „gleich gebaut hintereinander“; `python3 -I inhalte/generatoren/_stufen_nachweis.py <thema>` OK (alte Aufgaben nur in g/s geändert, Lernkarten-Texte unverändert).

### (1) Stufen-Leiter je Lernkarte


### terme.aufstellen

- **struktur**
  - S1: Termart eines einfachen Terms an der letzten Rechnung erkennen.
  - S2: Punkt-vor-Strich-Fallen und Klammern beachten; zu einer Beschreibung den Term finden; Term in Worten.
  - S3: Verschachtelte Beschreibungen in Terme übersetzen, Tabellen-Formeln deuten, falsche Begründungen widerlegen, Klammern gezielt setzen.
- **termwert**
  - S1: Eine Zahl in einen einfachen Term einsetzen und ausrechnen.
  - S2: Terme mit Quadrat, zwei Variablen, negativen Zahlen; Wertetabelle ausfüllen; Sachsituation.
  - S3: Vom Termwert zurückrechnen, Parameter bestimmen, Fehler beim Einsetzen deuten, Aussagen über alle Zahlen prüfen, Tabellen-Formeln.
- **uebersetzen**
  - S1: Einfache Wortterme („die Summe aus dem Vierfachen von x und 3“) direkt übersetzen.
  - S2: Differenzen in der richtigen Reihenfolge, „das Doppelte der Summe“ mit Klammer, Terme in Worten, Zahlenrätsel.
  - S3: Übersetzen und zusammenfassen, rückwärts zur gedachten Zahl, Rätsel begründen, falsche Übersetzungen finden, Parameter bestimmen.
- **sachsituation**
  - S1: Grundgebühr plus Preis pro Einheit als Term aufschreiben.
  - S2: Situationen mit zwei Bezügen, Rabatt, Einheitenwechsel, Tabelle → Term, Vergleich zweier Angebote.
  - S3: Rest-Terme („der Rest“), Bedeutung von x deuten, Fehler im Ansatz finden, Grundgebühr rückwärts bestimmen, Kosten pro Person als Quotient.
- **muster**
  - S1: Eine Figurenfolge um wenige Figuren fortsetzen.
  - S2: Den Term zur Folge aus Bild oder Tabelle aufstellen; mit dem Term große Figuren berechnen; Figur zu einer Anzahl finden.
  - S3: Term aus dem Aufbau begründen, rückwärts zur Figur, fremde Formeln (Diagonalen), quadratisches Wachstum, falsche Terme erkennen, Parameter.
- **deuten**
  - S1: Sagen, wofür eine Zahl im Term steht (Grundgebühr, Preis pro Einheit).
  - S2: Eine Rechnung oder einen Termwert in der Situation deuten; vom Wert zurück zur Zeit; Term zu einer Situation wählen.
  - S3: Teilterme in Figuren deuten, Tarife vergleichen und deuten, Fehlschlüsse erkennen, einen Parameter aus einem Messwert bestimmen.

### terme.umformen

- **zusammenfassen**
  - S1: Gleichartige Glieder mit x und y zusammenfassen.
  - S2: Terme mit x², Zahlen und mehreren Gliedern; Umfang als Term; fehlenden Summanden bestimmen.
  - S3: Fehler beim Zusammenfassen deuten, rückwärts den Term T finden, Seite aus dem Umfang, Potenzen unterscheiden, Parameter, Prüfungsaufgabe mit Produkten.
- **produkte**
  - S1: Zwei Faktoren mit Zahl und Variable malnehmen (2x · 5y).
  - S2: Vorzeichen bei mehreren Faktoren, gleiche Variablen werden zum Quadrat, Fläche als Term, fehlende Seite.
  - S3: Fehler x statt x², Volumen mit a³, fehlenden Faktor rückwärts, Vorzeichen bei drei Minus, Verdopplung der Seiten, Parameter, Prüfungsaufgabe.
- **minusklammer**
  - S1: Eine Minusklammer auflösen und zusammenfassen; richtige Umformung erkennen.
  - S2: Zwei Klammern, Minus vor einem Faktor, Sachsituation Konto, fehlenden Term in der Klammer finden.
  - S3: Fehler deuten, verschachtelte Klammern, Ausgaben einer Kasse, Lücke rückwärts, Gegenbeispiel zu a − (b − c), Seite aus dem Umfang, Prüfungsaufgabe.
- **ausmultiplizieren**
  - S1: Eine Zahl vor der Klammer mit jedem Glied malnehmen.
  - S2: x vor der Klammer, negative Faktoren, zwei Klammern vereinfachen, Fläche als Term, Faktoren ergänzen.
  - S3: Zuwachs unabhängig von x, Faktor rückwärts, Fehler mit Vorzeichen und x · 4, Parameter a, Gegenbeispiel zu 2(ab), geschickt rechnen, Prüfungsaufgabe.
- **summe_mal_summe**
  - S1: (x + a)(x + b) ausmultiplizieren; die Anzahl der Produkte kennen.
  - S2: Minuszeichen und Faktoren vor x, Garten als Sachsituation, Rechteck aus vier Teilflächen als Produkt schreiben.
  - S3: Fehlende Glieder deuten, Flächenänderung, Zahl rückwärts, Parameter k, geschickt rechnen 21 · 19, Prüfungsaufgabe, Rechnung beurteilen.
- **ausklammern**
  - S1: Den größten gemeinsamen Zahlfaktor ausklammern.
  - S2: Zahl und x ausklammern, fehlenden Faktor ergänzen, Länge aus Fläche und Breite.
  - S3: Unvollständiges Ausklammern beurteilen, zwei Variablen, negative Faktoren, Länge rückwärts, Parameter, geschickt rechnen, Prüfungsaufgabe (Lücken).
- **aequivalenz**
  - S1: Termwerte berechnen und einsetzen, um zu vergleichen; ausmultiplizierte Form erkennen.
  - S2: Zwei Terme mit einer Zahl vergleichen, äquivalente Paare finden, Gegenbeispiel wählen, Wertetabelle → Term, Sachsituation zweier Kassen.
  - S3: Fehlschluss aus einem Beispiel, Parameter, Term rückwärts, Zählweisen vergleichen, (−x)² und −x², Prüfungsaufgabe „nicht äquivalent“.
- **binomisch**
  - S1: (x + a)² und (x − a)² mit der passenden Formel ausmultiplizieren; Formel erkennen.
  - S2: Faktoren vor x, quadratischer Platz als Sachsituation, Quadrat erkennen und zurückschreiben, Flächenbild deuten.
  - S3: Geschickt rechnen (51², 49 · 51), Fehler „Mittelglied vergessen“, ergänzen rückwärts, (a − b)² = (b − a)² begründen, Parameter, Prüfungsaufgabe.

### abbildungen.kongruenz

- **achsenspiegelung**
  - S1: An x- oder y-Achse spiegeln; erkennen, welche Koordinate das Vorzeichen wechselt.
  - S2: An waagrechten und senkrechten Achsen sowie der Winkelhalbierenden spiegeln; Urbild zurückrechnen; Sachsituation.
  - S3: Achse aus Punkt und Bild finden, Achse einer Raute, Bild eines zweiten Punkts, Hintereinanderausführung, Fehler deuten, Prüfungsaufgabe mit Dreieck.
- **punktspiegelung**
  - S1: Am Ursprung spiegeln: beide Vorzeichen wechseln.
  - S2: An einem beliebigen Zentrum spiegeln, Urbild zurückrechnen, Dreieck spiegeln, Sachsituation Drehkreuz.
  - S3: Zentrum aus Punkt und Bild, vierte Ecke und Zentrum eines Parallelogramms, zwei Spiegelungen, Begründung, Fehler, Prüfungsaufgabe mit Fläche.
- **verschiebung**
  - S1: Einen Punkt mit einem Pfeil verschieben; Eigenschaft der Verschiebung erkennen.
  - S2: Pfeil aus Punkt und Bild, zwei Verschiebungen nacheinander, Dreieck verschieben, Sachsituation Schiff.
  - S3: Ersatzpfeil, falscher Pfeil, Pfeil an anderem Punkt, unbekannter Pfeil rückwärts, Quadrat verschieben, Fehler, Parameter, Prüfungsaufgabe.
- **drehung**
  - S1: Um O um 90°, 180°, 270° drehen; die Koordinatenregel für 90° erkennen.
  - S2: Drehwinkel aus Punkt und Bild, Drehung im Uhrzeigersinn, Sachsituation Riesenrad.
  - S3: Drehen um ein anderes Zentrum, Bild einer Geraden, Fehler mit der Drehrichtung, Urbild, Mehrfachdrehung, Parameter, Prüfungsaufgabe mit Quadrat.
- **symmetrie**
  - S1: Symmetrieachsen bekannter Vierecke und des Sechsecks zählen.
  - S2: Buchstaben, Punktsymmetrie von Rechteck und Trapez, kleinster Drehwinkel regelmäßiger Vielecke, Eckenzahl aus dem Drehwinkel, Windrad.
  - S3: Buchstaben mit Symmetrie-Kombinationen, Figur aus Eigenschaften, Gegenbeispiel deckungsgleich, Drehwinkel-Vielfache, Verkehrsschild, zusammengesetzte Figur.
- **parkett**
  - S1: Winkel an einer Ecke addieren; Innenwinkel regelmäßiger Vielecke erkennen.
  - S2: Lücke an einer Ecke berechnen, Innenwinkel aus der Anzahl, Fliesen im Bad.
  - S3: Fehlende Vielecke ergänzen, Eckenzahl aus dem Innenwinkel, gemischte Ecken prüfen und begründen, Fußball als Anwendung.
- **eigenschaften**
  - S1: Längen und Winkel bleiben erhalten; richtige Aussage erkennen.
  - S2: Abbildung aus Bild und Urbild bestimmen, Umlaufsinn bei Drehung und Spiegelung, Flächeninhalt bleibt.
  - S3: Zwei Spiegelungen als Verschiebung oder Drehung, Umlaufsinn umkehren, Fixpunkte, Fehler, Spiegeluhr, Prüfungsaufgabe mit zwei Abbildungen.
- **mittelsenkrechte**
  - S1: Mittelpunkt einer Strecke, Lage der Mittelsenkrechten, Eigenschaft „gleich weit“.
  - S2: Lot fällen, Abstand zu einer Geraden, Spielplatz an der Straße, Konstruktionsschritte deuten.
  - S3: Ortslinien schneiden (Leuchttürme, Funkmast, drei Häuser), Anzahl von Punkten begründen, Lot auf schräge Gerade, Fehler, Prüfungsaufgabe.
- **winkelhalbierende**
  - S1: Winkel halbieren; Punkte auf der Winkelhalbierenden sind von beiden Schenkeln gleich weit entfernt.
  - S2: Winkel aus der Hälfte, Nebenwinkel, Punkte gleich weit von zwei Achsen, Konstruktionsschritt.
  - S3: Ortslinie mit Weg schneiden, Nebenwinkel-Halbierende begründen, Anzahl von Punkten, Fehler mit dem Winkelfeld, Parameter.
- **vierecke_ordnen**
  - S1: Vierecke an Symmetrieachsen erkennen; wahre Aussagen im Haus der Vierecke.
  - S2: Falsche Aussagen finden, Vierecke in Bildern benennen, Nachbarn im Haus der Vierecke, Tischplatte.
  - S3: Gegenbeispiel, Viereck aus zwei Eigenschaften, Anzahlen begründen, unterscheidende Eigenschaft, Fehler, Prüfungsaufgabe mit Koordinaten.

### geometrie.winkelsaetze

- **scheitel_neben**
  - S1: Neben- und Scheitelwinkel an einer Kreuzung bestimmen; erkennen, welche gleich groß sind.
  - S2: Drei Geraden durch einen Punkt, Lagebeschreibungen, Nummerierung deuten, Winkel aus „um … größer“.
  - S3: Verhältnisse, Summen von Winkeln zurückrechnen, Sachsituation Kreuzung, Scheitelwinkelsatz begründen, Fehler deuten.
- **stufen_wechsel**
  - S1: Stufen- und Wechselwinkel an Parallelen ablesen; Winkelpaare erkennen.
  - S2: Winkel in anderer Lage über Neben- und Scheitelwinkel bestimmen, Winkelpaare benennen, Gleise und Straße.
  - S3: Rampe mit Handlauf, Dreieck zwischen Parallelen, Knickweg, Verhältnis rückwärts, Fehler mit der Lage, Parameter, Prüfungsaufgabe Parallelogramm.
- **parallel_pruefen**
  - S1: Mit gleichen Stufen- oder Wechselwinkeln auf Parallelität schließen; das Kriterium erkennen.
  - S2: Lagen über Neben- und Scheitelwinkel umrechnen, nötige Drehung bestimmen, drei Parallelen, Regalbretter.
  - S3: Begründung beurteilen, Schnittwinkel nicht paralleler Geraden, Senkrechte verknüpfen, parallele Paare auswählen, Fehler, Prüfungsaufgabe Viereck.
- **innenwinkelsumme**
  - S1: Den dritten Winkel aus zwei Winkeln berechnen; die Winkelsumme 180° kennen.
  - S2: Gleich große Winkel, rechter Winkel, Existenz eines Dreiecks prüfen, Beweisschritte mit Wechselwinkeln, Segel.
  - S3: Größten Winkel begründen, Beweis mit Teilwinkeln, Fehler beim Zerlegen, Verhältnis und Differenzen rückwärts.
- **aussenwinkel**
  - S1: Außenwinkel als Summe der beiden nicht anliegenden Innenwinkel oder als Nebenwinkel berechnen.
  - S2: Innenwinkel aus Außenwinkel zurückrechnen, Außenwinkel an anderer Ecke, Dachgiebel.
  - S3: Zwei Außenwinkel verknüpfen, Verhältnis rückwärts, drei spitze Außenwinkel begründen, Kreisfigur, Fehler „Innen- statt Außenwinkel“.
- **vieleck**
  - S1: Fehlenden Winkel im Viereck berechnen, Winkelsumme eines n-Ecks bestimmen.
  - S2: Zerlegung in Dreiecke, fehlender Winkel im Fünf- und Sechseck, Innenwinkel regelmäßiger Vielecke, Gartenbeet.
  - S3: Eckenzahl und Diagonalen aus der Winkelsumme, Formel begründen, Viereck mit Vielfachen, Fehler beim Zerlegen.
- **figuren**
  - S1: Winkel am Dreieck zwischen Parallelen und im Parallelogramm ablesen; gleiche Winkel erkennen.
  - S2: Gegenüberliegende Winkel, Trapez und Raute, Fenster, benachbarte Winkel aus ihrer Differenz.
  - S3: Schnittwinkel zweier Geraden, Diagonalen im Parallelogramm, Spiegel, Knickwege, Fehler im Trapez, Prüfungsaufgabe Raute.
- **beweisen**
  - S1: Passenden Winkelsatz zu einer Lage oder Begründung erkennen.
  - S2: Beweiskette ordnen, Zirkelschluss erkennen, Fundamentalsatz und abgeleitete Sätze, Umkehrung im Alltag.
  - S3: Beweis in Kärtchen ordnen, Aussagen über spitze und stumpfe Winkel begründen, Fehlschlüsse beurteilen, Messung gegen Satz, Tischplatte.

### gleichungen.linear

- **waage**
  - S1: x ± a = b mit einer Umformung lösen; passende Umformung erkennen.
  - S2: ax ± b = c in zwei Schritten, Umformungen notieren, Bruch als Faktor, Waage mit Päckchen.
  - S3: Brüche als Faktoren verknüpfen, Kästchen für eine Lösung, Zahlenrätsel rückwärts, Fehler „durch x teilen“, Umformungen begründen, Prüfungsaufgabe mit Dezimalzahlen.
- **beide_seiten**
  - S1: x auf beiden Seiten mit einem Schritt auf eine Seite bringen; sinnvollen ersten Schritt erkennen.
  - S2: Mehrere x- und Zahlglieder, negative Faktoren, Umformungen notieren, Sparvergleich.
  - S3: Lösungen als Bruch, Kästchen für eine Lösung, Waage mit Kugeln und Würfeln, Zahlenrätsel, Fehler beim Seitenwechsel, Prüfungsaufgabe mit Dezimalzahlen.
- **klammern**
  - S1: Klammer ausmultiplizieren und a(x + b) = c lösen; gleichwertige Gleichung erkennen.
  - S2: Minusklammern, Klammern auf beiden Seiten, zwei Klammern, Kinokasse, Klammer zurückgewinnen.
  - S3: Produkt zweier Klammern, Fehler mit dem Vorzeichen, Kästchen, Dreieck, Zahlenrätsel rückwärts, Prüfungsaufgabe.
- **probe**
  - S1: Einsetzen und prüfen, ob eine Zahl Lösung ist; Sinn der Probe erkennen.
  - S2: Fehlerzeile in einer Rechnung finden, Probe richtig aufschreiben, Kandidaten testen, Stiftepackungen.
  - S3: Unzulässige Umformungen (· 0, falsch geteilt, Quadrieren) begründen, Fehler finden und korrigieren, Kästchen, Prüfungsaufgabe mit Auswahl.
- **sonderfaelle**
  - S1: Erkennen, ob eine Gleichung keine, eine oder unendlich viele Lösungen hat.
  - S2: Lösungsmenge angeben, Kästchen für unendlich viele Lösungen, Handytarife ohne Treffpunkt.
  - S3: Tarif-Deutung, Parameter für keine oder unendlich viele Lösungen, Grundmenge, Fehler „L = {6}“, Gleichung ohne Lösung begründen.
- **sach**
  - S1: Einfache Sachaufgabe mit einer Gleichung lösen; passende Gleichung erkennen.
  - S2: Alter, Pfand, Sparen, Kino, Seil, Zahlenfolgen; Gleichung zu einer Situation auswählen.
  - S3: Geld rückwärts, Ergebnis deuten, Tarife, Züge, Kanister, Theaterkasse, Gehege, Altersrätsel, Prüfungsaufgabe Klassenfahrt.

### bruch.prozent_grundwert

- **faktor**
  - S1: Zu „um p % erhöhen/verringern“ den Wachstumsfaktor angeben; passenden Faktor erkennen.
  - S2: Vom Faktor zur Prozentänderung, „auf“ statt „um“, Verdopplung und Verdreifachung, Sale, Balkenbild.
  - S3: Fehler beim Faktor, Filteranlage, Gleichung zum Chor, Rechteckfläche, Rückweg-Faktor, Parameter, Grenze 100 %, Prüfungsaufgabe Term.
- **vermehrt**
  - S1: Neuen Wert nach einer Erhöhung mit dem Faktor berechnen; passende Rechnung erkennen.
  - S2: Mehrwertsteuer, Zinsen, Mieten, Einwohner; Erhöhung in Euro; Streifenbild.
  - S3: Erhöhung plus feste Zulage, Term deuten, Handwerkerrechnung, Guthaben aus den Zinsen, Aufschlag rückwärts, Fehler 1,5 statt 1,15, Zinssatz, Prüfungsaufgabe Vorverkauf.
- **vermindert**
  - S1: Neuen Wert nach einer Abnahme berechnen; passende Rechnung erkennen.
  - S2: Rabatt, Wertverlust, Schülerzahlen, Rabatt mit Skonto, Rabatt aus dem Zahlanteil.
  - S3: Diagramm lesen, Gesamtsenkung rückwärts, Akku über Jahre, Preis aus der Ersparnis, zwei Läden vergleichen, Fehler „nur Rabatt“, Reihenfolge zweier Rabatte, Prüfungsaufgabe.
- **zurueck**
  - S1: Den Grundwert aus dem vermehrten oder verminderten Wert mit einer Division berechnen; Rechnung erkennen.
  - S2: Nettopreis aus Bruttopreis, alter Preis nach Rabatt oder Erhöhung, Ersparnis in Euro.
  - S3: Teilnehmerzahl aus Anteil, Mehrwertsteuer im Preis, Fehler „+ 20 %“, zwei Änderungen rückwärts, Begründung, Prozentsatz der Erhöhung, Prüfungsaufgabe, Zinsen rückwärts.
- **prozentsatz**
  - S1: Prozentuale Änderung aus altem und neuem Wert berechnen; Bezugswert erkennen.
  - S2: Änderungen bei Mitgliedern und Klassen, gleicher Anteil, Erhöhung aus Euro-Betrag.
  - S3: Falscher Bezugswert, zwei Schritte, „mehr als“ und „weniger als“, Prozentpunkte, Rückblick vom neuen Wert.
- **mehrfach**
  - S1: Zwei Änderungen nacheinander mit Faktoren berechnen; Gesamtfaktor erkennen.
  - S2: Gesamtänderung in Prozent, Miete über zwei Jahre, Rabatt und Mehrwertsteuer, gleicher Prozentsatz zweimal.
  - S3: Anfangswert rückwärts, drei Erhöhungen, „zweimal 25 % = halber Preis“, Zinseszins, Rückweg nach einer Senkung, Parameter p.
- **argumente**
  - S1: Rechnungen mit Faktoren als Begründung erkennen; Prozentpunkte und Faktor direkt angeben.
  - S2: Aussagen und Zeitungsmeldungen prüfen, zwei Läden vergleichen, doppelte Rabatte, 100 % Rabatt deuten.
  - S3: Hin und zurück ist nicht gleich, Prozentpunkte gegen Prozent, Anteile mit verschiedenen Grundwerten, Angebote vergleichen, Wiederholungen begründen.

### daten.boxplot

- **median**
  - S1: Median einer kurzen ungeraden Liste bestimmen; Ordnen als ersten Schritt erkennen.
  - S2: Median bei gerader Anzahl, fehlenden Wert aus dem Median, Anzahl unter dem Median, Median nach einem neuen Wert.
  - S3: Median aus Häufigkeitstabelle und Diagramm, Prozentangaben, Ersetzen begründen, Mindestwert rückwärts, Fehler „ungeordnet“, Prüfungsaufgabe Weitsprung.
- **kennwerte**
  - S1: Spannweite und Modalwert ablesen; Kennwert am Namen erkennen.
  - S2: Arithmetisches Mittel berechnen, Summe aus dem Mittel, Spannweite nach Verschieben, gerecht teilen.
  - S3: Fehlenden Wert aus dem Mittel, Durchschnittsnote aus Prozenten, Formel in der Tabellenkalkulation, Klammerfehler, nötige Punktzahl, Begründung, Parameter, Prüfungsaufgabe.
- **mittel_median**
  - S1: Arithmetisches Mittel berechnen; Rechenweg erkennen.
  - S2: Mittelwert und Median vergleichen, typische Mitte wählen, Kennwert, der sich nicht ändert.
  - S3: Gehälter mit Ausreißer, Prozentverteilungen, Wert so ändern, dass das Mittel passt, Ausreißer entfernen, Fehler „Mitte der Spannweite“, Begründung, Prüfungsaufgabe.
- **quartile**
  - S1: Oberes Quartil einer ungeraden Liste bestimmen; Anteil unter Q₁ erkennen.
  - S2: Quartile bei gerader Anzahl, Quartilsabstand, Bildschirmzeiten, Q₁ aus Q₃ und Quartilsabstand.
  - S3: Werte in der Box zählen, fehlenden Wert rückwärts, Anzahlen begründen, Verdoppeln und Verschieben, Fehler bei Q₁, Lauf mit 200 Personen, Prüfungsaufgabe.
- **boxplot**
  - S1: Median, Quartile und Maximum am Boxplot ablesen; fünf Kennwerte erkennen.
  - S2: Anteile unter oder über einer Marke ablesen, Spannweite, Finalplätze beim Wettlauf.
  - S3: Boxplot zu Daten wählen, Anzahlen bei bekannter Gesamtzahl, falsche Aussage finden, Datenreihe zum Boxplot, Antenne.
- **vergleichen**
  - S1: Aussagen über Median und Streuung an zwei Boxplots erkennen; Mediane vergleichen.
  - S2: Gleichmäßigkeit über den Quartilsabstand, besseres Abschneiden über den Median, Anteile über einer Marke.
  - S3: Falsche Aussage finden, Anzahlen in zwei Klassen, gleiche Kennwerte deuten, Quartilsabstände vergleichen, Fehler „längere Box = mehr Kinder“, Box rückwärts, Prüfungsaufgabe.

### geometrie.konstruktion

- **parallelen**
  - S1: Stufen- und Wechselwinkel an Parallelen ablesen; Z-Form erkennen.
  - S2: Markierte Winkel in anderer Lage, Winkelbeziehungen benennen, Parallelität prüfen, gleich große Winkel zählen.
  - S3: Winkel mit Variable, Fehlaussagen beurteilen, nicht parallele Geraden, Dreieck zwischen Parallelen, Knickweg, Leitern.
- **winkelsumme**
  - S1: Dritten Winkel aus zwei Winkeln berechnen; Folgerung für stumpfe Winkel erkennen.
  - S2: Außenwinkel, rechtwinkliges Dreieck, Beweis mit der Parallelen deuten, Winkel aus dem Außenwinkel zurückrechnen.
  - S3: Vielfache rückwärts, Fehlaussagen, größten Winkel begründen, Summenbedingung, Verhältnisse, Pentagramm.
- **gleichschenklig**
  - S1: Basiswinkel aus dem Spitzenwinkel berechnen; gleich große Winkel erkennen.
  - S2: Spitzenwinkel aus dem Basiswinkel, beide Fälle bei einem bekannten Winkel, Außenwinkel, Giebel.
  - S3: Außenwinkel rückwärts, Dachneigung, Kreisfiguren mit Radien, gleichseitig und gleichschenklig verknüpft, beide Lösungen begründen.
- **kongruenzsatz**
  - S1: Passenden Kongruenzsatz bei Standardlage erkennen; dritten Winkel bei WSW berechnen.
  - S2: Kongruenzsatz bei ungewohnter Lage der Angaben, drei Winkel, SsW mit Gegenwinkel, Grundstück.
  - S3: Zwei Lösungen bei SsW, Kongruenz zweier Dreiecke begründen, ähnliche Dreiecke, Drachenviereck, Fehler „irgendein Winkel“, Prüfungsaufgabe SsW.
- **konstruierbar**
  - S1: Mit der Dreiecksungleichung entscheiden, ob drei Seiten ein Dreieck ergeben.
  - S2: Konstruierbarkeit mit Winkeln, Grenzen für die dritte Seite, Anzahl möglicher Längen, Holzleisten.
  - S3: Anzahl der Längen verknüpfen, Ortslinien schneiden, Brunnen, ganzzahlige Umfänge, gleichschenkliger Fall, Fehler „flaches Dreieck“, Prüfungsaufgabe.
- **planfigur**
  - S1: Bezeichnungen im Dreieck und den ersten Konstruktionsschritt erkennen; Radius ablesen.
  - S2: Ortslinie für C bei gegebener Höhe, fehlende Schritte, Punkt C im Koordinatensystem, Segel.
  - S3: Konstruktionsbeschreibung wählen und ergänzen, C aus Winkel und Höhe, Anzahl möglicher Punkte begründen, stumpfer Winkel und Höhenfußpunkt.
- **vierecke**
  - S1: Winkel im Parallelogramm und fehlenden Winkel im Viereck berechnen; gleiche Winkel erkennen.
  - S2: Drachenviereck, gleichschenkliges Trapez, Raute mit Diagonale, Differenz zweier Winkel, Trapezfenster.
  - S3: Geländer, Diagonaleneigenschaften, Winkel mit fester Differenz und Vielfachen rückwärts, Fehler „vier gleiche Seiten“, Drachen verknüpfen, Parameter, Prüfungsaufgabe Rechteck.
- **satz_kehrsatz**
  - S1: Kehrsatz zu einem Wenn-dann-Satz bilden; Bauprinzip erkennen.
  - S2: Kehrsatz prüfen, Gegenbeispiel finden, Fehlschluss „Satz wahr, also Kehrsatz wahr“, Bus-Regel.
  - S3: Kehrsatz des Thalessatzes, Beweisschritte ordnen, „genau dann, wenn“, Beispiele sind kein Beweis, Fehler bei Teilbarkeit, ursprünglichen Satz rückwärts, Prüfungsaufgabe.

### geometrie.kreis

- **thales**
  - S1: Rechten Winkel bei C und fehlenden Winkel im Thalesdreieck angeben; Radius des Thaleskreises.
  - S2: Winkel rückwärts, Radius und [MC], Halbkreisfenster, Punkt auf dem Thaleskreis prüfen.
  - S3: Mittelpunktswinkel, Vielfache und Differenzen rückwärts, Zeichendreieck an Nägeln, größte Höhe, Flächen begründen, Rechteck im Kreis, Fehler „rechter Winkel bei A“.
- **umkehrung**
  - S1: Mittelpunkt und Radius des Kreises angeben, auf dem C bei rechtem Winkel liegt; Umkehrung erkennen.
  - S2: Radius in cm, Winkelsumme prüfen, Umkreis rechtwinkliger Dreiecke, möglichen Punkt C prüfen, Beet abstecken.
  - S3: Nicht rechtwinklige Fälle begründen, Nachweis mit M, [MC] aus [AB], C innerhalb des Kreises, Winkel mit Variable, Fehler stumpfer Winkel, Tischlerecke, Prüfungsaufgabe.
- **beweis**
  - S1: Aussagen über Vermutung, Beispiel und Gegenbeispiel erkennen; einen Beweisschritt ausrechnen.
  - S2: Begründungen zu markierten Beweisschritten, falsche Aussage finden, gleichschenkliges Dreieck aus Radien, Beweis mit Variablen.
  - S3: Beweise ordnen, Begründungen beurteilen, Mittelpunktswinkel, Gegenbeispiel zu Sehnenvierecken, Herkunft einer Beweiszeile.
- **lage**
  - S1: Sekante, Tangente, Passante über den Vergleich von Abstand und Radius benennen.
  - S2: Anzahl gemeinsamer Punkte mit dem Durchmesser, Abstände für Sekanten, Geraden im Koordinatensystem, rundes Beet.
  - S3: Lage zu Achsen und Geraden, Abstand definieren, Punkte im festen Abstand begründen, zwei Kreise, Fehler bei d = r, Radius aus der Lage.
- **tangente**
  - S1: Rechten Winkel zwischen Tangente und Radius kennen, halben Winkel und gleich lange Tangentenabschnitte nutzen.
  - S2: Winkel ∠BMB′ und ∠BPB′ ineinander umrechnen, Tangente im Koordinatensystem, Fahrradreifen, gleichseitiges Tangentendreieck.
  - S3: Winkel im Tangentendreieck, Thaleskreis bei der Konstruktion begründen, Radius aus dem Abstand, Treibriemen, Fehler 80°, Prüfungsaufgabe Kreis an der y-Achse.
- **umkreis_inkreis**
  - S1: Linien für Umkreis- und Inkreismittelpunkt und ihre Abstandseigenschaft erkennen.
  - S2: Lage des Umkreismittelpunkts nach Winkeln, Winkel am Inkreismittelpunkt, gleichseitiges Dreieck, Winkel aus der Halbierenden.
  - S3: Winkel ∠BIC verknüpfen, Funkmast und Spielplatz, Umkreismittelpunkt auf einer Seite, Winkel rückwärts, Fehler mit den Linien, Prüfungsaufgabe ∠AIB.

### (2) Übungen je Stufe und Typ, vorher → nachher

„vorher“: Anzahl alter Übungen der Stufe (ohne Typ). „nachher“: Übungen mit Typ, aufgeschlüsselt; überzählige Übungen behalten keinen Typ und sind getrennt ausgewiesen. Umstufungen sind schon eingerechnet.

### terme.aufstellen

| Karte | Stufe 1 vorher → nachher | Stufe 2 vorher → nachher | Stufe 3 vorher → nachher | Knobel |
|---|---|---|---|---|
| struktur | 6 → 7 (direkt 6, erkennen 1) | 6 → 7 (mehrschritt 5, umkehr 1, darstellung 1) | 8 → 8 (rueckwaerts 2, verknuepfen 1, begruenden 1, fehler 1, transfer 3) | 2 |
| termwert | 4 → 5 (direkt 4, erkennen 1) | 11 → 12 (mehrschritt 9, einkleidung 1, darstellung 2) | 5 → 8 (rueckwaerts 1, verknuepfen 2, begruenden 1, fehler 1, transfer 2, parameter 1) | 2 |
| uebersetzen | 4 → 5 (direkt 4, erkennen 1) | 9 → 11 (mehrschritt 5, einkleidung 1, umkehr 3, darstellung 2) | 8 → 8 (rueckwaerts 1, verknuepfen 2, begruenden 2, fehler 1, transfer 1, parameter 1) | 2 |
| sachsituation | 9 → 9 (direkt 8, erkennen 1) + 1 überzählig | 5 → 9 (mehrschritt 4, einkleidung 3, umkehr 1, darstellung 1) | 8 → 8 (verknuepfen 1, begruenden 1, fehler 1, transfer 3, parameter 1, pruefung 1) | 2 |
| muster | 4 → 5 (direkt 4, erkennen 1) | 8 → 9 (mehrschritt 3, umkehr 1, darstellung 5) + 2 überzählig | 8 → 8 (rueckwaerts 2, verknuepfen 1, begruenden 1, fehler 1, transfer 2, parameter 1) | 2 |
| deuten | 4 → 5 (direkt 1, erkennen 4) | 8 → 7 (einkleidung 1, umkehr 3, darstellung 3) + 1 überzählig | 8 → 9 (begruenden 3, fehler 3, transfer 2, parameter 1) | 2 |

### terme.umformen

| Karte | Stufe 1 vorher → nachher | Stufe 2 vorher → nachher | Stufe 3 vorher → nachher | Knobel |
|---|---|---|---|---|
| zusammenfassen | 5 → 5 (direkt 4, erkennen 1) | 6 → 7 (mehrschritt 5, einkleidung 1, umkehr 1) | 5 → 8 (rueckwaerts 1, verknuepfen 1, begruenden 1, fehler 2, transfer 1, parameter 1, pruefung 1) | 2 |
| produkte | 4 → 4 (direkt 3, erkennen 1) + 1 überzählig | 6 → 7 (mehrschritt 5, einkleidung 1, umkehr 1) | 5 → 8 (rueckwaerts 1, verknuepfen 1, begruenden 2, fehler 1, transfer 1, parameter 1, pruefung 1) | 2 |
| minusklammer | 6 → 6 (direkt 4, erkennen 2) | 7 → 9 (mehrschritt 7, einkleidung 1, umkehr 1) | 4 → 8 (rueckwaerts 1, verknuepfen 1, begruenden 1, fehler 1, transfer 2, parameter 1, pruefung 1) | 2 |
| ausmultiplizieren | 5 → 4 (direkt 3, erkennen 1) + 2 überzählig | 8 → 10 (mehrschritt 8, einkleidung 1, umkehr 1) | 4 → 8 (rueckwaerts 1, verknuepfen 1, begruenden 1, fehler 2, transfer 1, parameter 1, pruefung 1) | 2 |
| summe_mal_summe | 4 → 4 (direkt 3, erkennen 1) + 2 überzählig | 8 → 8 (mehrschritt 5, einkleidung 2, darstellung 1) + 1 überzählig | 4 → 8 (rueckwaerts 1, verknuepfen 1, begruenden 2, fehler 1, transfer 1, parameter 1, pruefung 1) | 2 |
| ausklammern | 4 → 4 (direkt 3, erkennen 1) + 2 überzählig | 6 → 6 (mehrschritt 4, einkleidung 1, umkehr 1) + 2 überzählig | 4 → 8 (rueckwaerts 1, verknuepfen 2, begruenden 1, fehler 1, transfer 1, parameter 1, pruefung 1) | 2 |
| aequivalenz | 7 → 6 (direkt 4, erkennen 2) + 4 überzählig | 6 → 6 (mehrschritt 2, einkleidung 1, umkehr 2, darstellung 1) | 4 → 8 (rueckwaerts 1, verknuepfen 1, begruenden 2, fehler 1, transfer 1, parameter 1, pruefung 1) | 2 |
| binomisch | 4 → 5 (direkt 4, erkennen 1) + 1 überzählig | 5 → 6 (mehrschritt 3, einkleidung 1, umkehr 1, darstellung 1) + 1 überzählig | 5 → 8 (rueckwaerts 2, verknuepfen 2, begruenden 1, fehler 1, parameter 1, pruefung 1) | 2 |

### abbildungen.kongruenz

| Karte | Stufe 1 vorher → nachher | Stufe 2 vorher → nachher | Stufe 3 vorher → nachher | Knobel |
|---|---|---|---|---|
| achsenspiegelung | 4 → 5 (direkt 4, erkennen 1) | 9 → 8 (mehrschritt 6, einkleidung 1, umkehr 1) + 3 überzählig | 7 → 9 (rueckwaerts 3, verknuepfen 2, fehler 1, transfer 2, pruefung 1) | 2 |
| punktspiegelung | 4 → 4 (direkt 3, erkennen 1) + 2 überzählig | 10 → 6 (mehrschritt 3, einkleidung 1, umkehr 2) + 8 überzählig | 6 → 9 (rueckwaerts 3, verknuepfen 2, begruenden 1, fehler 1, transfer 1, pruefung 1) | 2 |
| verschiebung | 4 → 4 (direkt 3, erkennen 1) + 2 überzählig | 11 → 7 (mehrschritt 4, einkleidung 1, umkehr 2) + 5 überzählig | 5 → 8 (rueckwaerts 1, verknuepfen 2, begruenden 1, fehler 1, transfer 1, parameter 1, pruefung 1) | 2 |
| drehung | 4 → 4 (direkt 3, erkennen 1) + 2 überzählig | 8 → 6 (mehrschritt 4, einkleidung 1, umkehr 1) + 3 überzählig | 8 → 8 (rueckwaerts 1, verknuepfen 3, begruenden 1, fehler 1, parameter 1, pruefung 1) + 2 überzählig | 2 |
| symmetrie | 4 → 4 (direkt 2, erkennen 2) | 8 → 10 (mehrschritt 5, einkleidung 1, umkehr 1, darstellung 3) | 8 → 8 (rueckwaerts 1, verknuepfen 3, begruenden 2, transfer 2) | 2 |
| parkett | 4 → 5 (direkt 4, erkennen 1) | 8 → 9 (mehrschritt 7, einkleidung 1, umkehr 1) | 8 → 9 (rueckwaerts 2, verknuepfen 3, begruenden 3, transfer 1) | 2 |
| eigenschaften | 3 → 5 (direkt 2, erkennen 3) + 1 überzählig | 12 → 6 (mehrschritt 3, einkleidung 1, darstellung 2) + 5 überzählig | 5 → 8 (verknuepfen 3, begruenden 2, fehler 1, transfer 1, pruefung 1) | 2 |
| mittelsenkrechte | 4 → 4 (direkt 3, erkennen 1) | 6 → 6 (mehrschritt 3, einkleidung 1, darstellung 2) | 8 → 10 (verknuepfen 3, begruenden 3, fehler 1, transfer 2, pruefung 1) | 2 |
| winkelhalbierende | 4 → 4 (direkt 2, erkennen 2) | 6 → 6 (mehrschritt 4, umkehr 1, darstellung 1) | 8 → 10 (verknuepfen 3, begruenden 2, fehler 1, transfer 3, parameter 1) | 2 |
| vierecke_ordnen | 4 → 4 (direkt 1, erkennen 3) | 6 → 7 (mehrschritt 3, einkleidung 1, darstellung 3) | 8 → 10 (verknuepfen 3, begruenden 3, fehler 1, transfer 2, pruefung 1) | 2 |

### geometrie.winkelsaetze

| Karte | Stufe 1 vorher → nachher | Stufe 2 vorher → nachher | Stufe 3 vorher → nachher | Knobel |
|---|---|---|---|---|
| scheitel_neben | 4 → 5 (direkt 4, erkennen 1) | 6 → 6 (mehrschritt 3, umkehr 2, darstellung 1) | 8 → 9 (rueckwaerts 3, verknuepfen 3, begruenden 1, fehler 1, transfer 1) | 2 |
| stufen_wechsel | 4 → 5 (direkt 4, erkennen 1) | 9 → 9 (mehrschritt 6, einkleidung 1, darstellung 2) + 1 überzählig | 5 → 8 (rueckwaerts 2, verknuepfen 2, fehler 1, transfer 1, parameter 1, pruefung 1) | 2 |
| parallel_pruefen | 4 → 5 (direkt 4, erkennen 1) | 8 → 9 (mehrschritt 6, einkleidung 1, umkehr 2) | 6 → 8 (verknuepfen 3, begruenden 3, fehler 1, pruefung 1) | 2 |
| innenwinkelsumme | 4 → 4 (direkt 3, erkennen 1) + 1 überzählig | 6 → 7 (mehrschritt 4, einkleidung 1, darstellung 2) | 8 → 8 (rueckwaerts 3, verknuepfen 3, begruenden 1, fehler 1) | 2 |
| aussenwinkel | 4 → 5 (direkt 4, erkennen 1) | 6 → 8 (mehrschritt 1, einkleidung 1, umkehr 6) | 8 → 9 (rueckwaerts 3, verknuepfen 3, begruenden 1, fehler 1, transfer 1) | 2 |
| vieleck | 4 → 4 (direkt 3, erkennen 1) + 1 überzählig | 6 → 7 (mehrschritt 5, einkleidung 1, darstellung 1) | 8 → 9 (rueckwaerts 3, verknuepfen 3, begruenden 1, fehler 1, transfer 1) | 2 |
| figuren | 4 → 5 (direkt 4, erkennen 1) | 6 → 8 (mehrschritt 6, einkleidung 1, umkehr 1) | 8 → 10 (rueckwaerts 3, verknuepfen 3, fehler 1, transfer 2, pruefung 1) | 2 |
| beweisen | 4 → 5 (direkt 1, erkennen 4) | 6 → 7 (mehrschritt 5, einkleidung 1, darstellung 1) | 8 → 9 (verknuepfen 2, begruenden 3, fehler 3, transfer 1) | 2 |

### gleichungen.linear

| Karte | Stufe 1 vorher → nachher | Stufe 2 vorher → nachher | Stufe 3 vorher → nachher | Knobel |
|---|---|---|---|---|
| waage | 5 → 5 (direkt 4, erkennen 1) + 1 überzählig | 11 → 10 (mehrschritt 7, einkleidung 1, darstellung 2) + 3 überzählig | 7 → 8 (rueckwaerts 1, verknuepfen 3, begruenden 1, fehler 1, parameter 1, pruefung 1) + 1 überzählig | 2 |
| beide_seiten | 5 → 6 (direkt 5, erkennen 1) | 11 → 13 (mehrschritt 11, einkleidung 1, darstellung 1) + 1 überzählig | 7 → 8 (rueckwaerts 1, verknuepfen 3, fehler 1, transfer 1, parameter 1, pruefung 1) | 2 |
| klammern | 5 → 5 (direkt 4, erkennen 1) + 1 überzählig | 12 → 17 (mehrschritt 15, einkleidung 1, umkehr 1) | 9 → 8 (rueckwaerts 1, verknuepfen 3, fehler 1, transfer 1, parameter 1, pruefung 1) | 2 |
| probe | 5 → 6 (direkt 5, erkennen 1) | 11 → 12 (mehrschritt 9, einkleidung 1, darstellung 2) | 7 → 8 (verknuepfen 1, begruenden 2, fehler 3, parameter 1, pruefung 1) | 2 |
| sonderfaelle | 5 → 4 (direkt 2, erkennen 2) + 1 überzählig | 11 → 12 (mehrschritt 9, einkleidung 1, umkehr 2) | 7 → 8 (verknuepfen 1, begruenden 2, fehler 1, transfer 1, parameter 3) | 2 |
| sach | 4 → 4 (direkt 3, erkennen 1) | 10 → 10 (mehrschritt 2, einkleidung 7, darstellung 1) + 1 überzählig | 9 → 10 (rueckwaerts 1, verknuepfen 3, begruenden 2, transfer 3, pruefung 1) | 2 |

### bruch.prozent_grundwert

| Karte | Stufe 1 vorher → nachher | Stufe 2 vorher → nachher | Stufe 3 vorher → nachher | Knobel |
|---|---|---|---|---|
| faktor | 6 → 5 (direkt 4, erkennen 1) + 2 überzählig | 6 → 9 (mehrschritt 3, einkleidung 1, umkehr 4, darstellung 1) + 3 überzählig | 8 → 8 (rueckwaerts 1, verknuepfen 2, begruenden 1, fehler 1, transfer 1, parameter 1, pruefung 1) | 2 |
| vermehrt | 8 → 6 (direkt 5, erkennen 1) + 3 überzählig | 9 → 10 (mehrschritt 2, einkleidung 7, darstellung 1) | 5 → 8 (rueckwaerts 2, verknuepfen 1, begruenden 1, fehler 1, transfer 1, parameter 1, pruefung 1) | 2 |
| vermindert | 4 → 5 (direkt 4, erkennen 1) | 13 → 13 (mehrschritt 4, einkleidung 8, umkehr 1) | 5 → 8 (rueckwaerts 2, verknuepfen 2, begruenden 1, fehler 1, transfer 1, pruefung 1) | 2 |
| zurueck | 4 → 5 (direkt 4, erkennen 1) | 12 → 9 (mehrschritt 1, einkleidung 4, umkehr 4) + 4 überzählig | 4 → 8 (rueckwaerts 2, verknuepfen 1, begruenden 1, fehler 1, transfer 1, parameter 1, pruefung 1) | 2 |
| prozentsatz | 7 → 4 (direkt 3, erkennen 1) + 5 überzählig | 7 → 6 (mehrschritt 3, einkleidung 2, umkehr 1) + 1 überzählig | 8 → 8 (rueckwaerts 1, verknuepfen 2, begruenden 1, fehler 2, transfer 2) | 2 |
| mehrfach | 4 → 4 (direkt 3, erkennen 1) + 1 überzählig | 8 → 9 (mehrschritt 6, einkleidung 2, umkehr 1) | 8 → 8 (rueckwaerts 3, verknuepfen 2, fehler 1, transfer 1, parameter 1) | 2 |
| argumente | 3 → 4 (direkt 2, erkennen 2) + 1 überzählig | 9 → 7 (mehrschritt 3, einkleidung 3, darstellung 1) + 2 überzählig | 9 → 9 (verknuepfen 1, begruenden 3, fehler 3, transfer 2) | 2 |

### daten.boxplot

| Karte | Stufe 1 vorher → nachher | Stufe 2 vorher → nachher | Stufe 3 vorher → nachher | Knobel |
|---|---|---|---|---|
| median | 7 → 8 (direkt 7, erkennen 1) | 8 → 8 (mehrschritt 6, einkleidung 1, umkehr 1) | 6 → 8 (rueckwaerts 1, verknuepfen 3, begruenden 1, fehler 1, transfer 1, pruefung 1) | 2 |
| kennwerte | 10 → 11 (direkt 10, erkennen 1) | 5 → 6 (mehrschritt 4, einkleidung 1, umkehr 1) | 5 → 8 (rueckwaerts 2, verknuepfen 1, begruenden 1, fehler 1, transfer 1, parameter 1, pruefung 1) | 2 |
| mittel_median | 4 → 5 (direkt 4, erkennen 1) | 11 → 10 (mehrschritt 7, einkleidung 2, umkehr 1) + 1 überzählig | 5 → 8 (rueckwaerts 1, verknuepfen 3, begruenden 1, fehler 1, transfer 1, pruefung 1) | 2 |
| quartile | 4 → 5 (direkt 4, erkennen 1) | 14 → 15 (mehrschritt 13, einkleidung 1, umkehr 1) | 5 → 8 (rueckwaerts 1, verknuepfen 1, begruenden 3, fehler 1, transfer 1, pruefung 1) | 2 |
| boxplot | 4 → 5 (direkt 4, erkennen 1) | 8 → 8 (mehrschritt 1, einkleidung 1, darstellung 6) + 1 überzählig | 8 → 8 (rueckwaerts 1, verknuepfen 3, begruenden 1, transfer 3) | 2 |
| vergleichen | 5 → 6 (direkt 1, erkennen 5) + 1 überzählig | 10 → 9 (mehrschritt 5, einkleidung 3, darstellung 1) | 5 → 9 (rueckwaerts 1, verknuepfen 2, begruenden 3, fehler 1, transfer 1, pruefung 1) | 2 |

### geometrie.konstruktion

| Karte | Stufe 1 vorher → nachher | Stufe 2 vorher → nachher | Stufe 3 vorher → nachher | Knobel |
|---|---|---|---|---|
| parallelen | 4 → 5 (direkt 4, erkennen 1) | 8 → 8 (mehrschritt 4, umkehr 2, darstellung 2) | 8 → 9 (verknuepfen 3, fehler 2, transfer 1, parameter 3) | 2 |
| winkelsumme | 4 → 4 (direkt 3, erkennen 1) + 2 überzählig | 8 → 8 (mehrschritt 5, umkehr 1, darstellung 2) | 8 → 8 (rueckwaerts 2, verknuepfen 2, begruenden 1, fehler 2, transfer 1) | 2 |
| gleichschenklig | 4 → 4 (direkt 3, erkennen 1) + 2 überzählig | 8 → 7 (mehrschritt 4, einkleidung 1, umkehr 2) + 2 überzählig | 8 → 8 (rueckwaerts 3, verknuepfen 3, begruenden 1, transfer 1) | 2 |
| kongruenzsatz | 4 → 5 (direkt 1, erkennen 4) + 1 überzählig | 8 → 9 (mehrschritt 6, einkleidung 1, darstellung 2) | 8 → 8 (verknuepfen 2, begruenden 3, fehler 1, transfer 1, pruefung 1) + 2 überzählig | 2 |
| konstruierbar | 4 → 4 (direkt 3, erkennen 1) + 2 überzählig | 10 → 11 (mehrschritt 6, einkleidung 1, umkehr 4) | 6 → 8 (verknuepfen 3, begruenden 1, fehler 1, transfer 2, pruefung 1) | 2 |
| planfigur | 4 → 4 (direkt 1, erkennen 3) | 6 → 7 (mehrschritt 3, einkleidung 1, darstellung 3) | 8 → 8 (rueckwaerts 1, verknuepfen 3, begruenden 3, transfer 1) | 2 |
| vierecke | 8 → 5 (direkt 4, erkennen 1) + 4 überzählig | 8 → 7 (mehrschritt 5, einkleidung 1, umkehr 1) + 2 überzählig | 4 → 8 (rueckwaerts 2, verknuepfen 1, begruenden 1, fehler 1, transfer 1, parameter 1, pruefung 1) | 2 |
| satz_kehrsatz | 4 → 5 (direkt 4, erkennen 1) | 12 → 13 (mehrschritt 9, einkleidung 1, umkehr 3) | 4 → 8 (rueckwaerts 1, verknuepfen 2, begruenden 2, fehler 1, transfer 1, pruefung 1) | 2 |

### geometrie.kreis

| Karte | Stufe 1 vorher → nachher | Stufe 2 vorher → nachher | Stufe 3 vorher → nachher | Knobel |
|---|---|---|---|---|
| thales | 7 → 7 (direkt 6, erkennen 1) + 1 überzählig | 6 → 6 (mehrschritt 3, einkleidung 1, umkehr 2) | 7 → 8 (rueckwaerts 2, verknuepfen 1, begruenden 2, fehler 1, transfer 2) | 2 |
| umkehrung | 7 → 5 (direkt 4, erkennen 1) + 3 überzählig | 8 → 7 (mehrschritt 5, einkleidung 1, umkehr 1) + 2 überzählig | 5 → 8 (rueckwaerts 1, verknuepfen 2, begruenden 2, fehler 1, transfer 1, pruefung 1) | 2 |
| beweis | 4 → 4 (direkt 2, erkennen 2) + 2 überzählig | 8 → 8 (mehrschritt 6, umkehr 1, darstellung 1) | 8 → 8 (verknuepfen 3, begruenden 3, fehler 1, transfer 1) | 2 |
| lage | 4 → 4 (direkt 3, erkennen 1) + 2 überzählig | 8 → 6 (mehrschritt 3, einkleidung 1, umkehr 1, darstellung 1) + 4 überzählig | 8 → 10 (verknuepfen 3, begruenden 2, fehler 1, transfer 3, parameter 1) | 2 |
| tangente | 6 → 5 (direkt 4, erkennen 1) + 1 überzählig | 8 → 6 (mehrschritt 3, einkleidung 1, umkehr 1, darstellung 1) + 4 überzählig | 6 → 8 (rueckwaerts 1, verknuepfen 3, begruenden 1, fehler 1, transfer 1, pruefung 1) | 2 |
| umkreis_inkreis | 4 → 5 (direkt 1, erkennen 4) | 10 → 6 (mehrschritt 4, umkehr 1, darstellung 1) + 4 überzählig | 6 → 8 (rueckwaerts 1, verknuepfen 2, begruenden 1, fehler 1, transfer 2, pruefung 1) | 2 |

### (3) Neue Übungen und Knobel-Bordkarten

- Neue Übungen: **268**, Knobel-Bordkarten: **130** (2 je Lernkarte, 65 Lernkarten), umgestufte alte Übungen: **25**.
  - terme.aufstellen: 21 neu, 12 Knobel, 8 umgestuft
  - terme.umformen: 51 neu, 16 Knobel, 4 umgestuft
  - abbildungen.kongruenz: 42 neu, 20 Knobel, 1 umgestuft
  - geometrie.winkelsaetze: 28 neu, 16 Knobel, 0 umgestuft
  - gleichungen.linear: 22 neu, 12 Knobel, 6 umgestuft
  - bruch.prozent_grundwert: 28 neu, 14 Knobel, 5 umgestuft
  - daten.boxplot: 24 neu, 12 Knobel, 1 umgestuft
  - geometrie.konstruktion: 30 neu, 16 Knobel, 0 umgestuft
  - geometrie.kreis: 22 neu, 12 Knobel, 0 umgestuft

### (4) überzählig (130 Übungen, nicht gelöscht)

Je Lernkarte, Stufe und Typ höchstens 2 alte Übungen mit demselben Satzbau; jede weitere ist hier gelistet und hat kein Feld g.

- terme.aufstellen / sachsituation / Stufe 1: „Eine Kinokarte kostet 10 €. Eine Gruppe kauft x Karten und zusammen einmal Popcorn für 5 €. Gib den Term für den Gesamtpreis (in €) an.“
- terme.aufstellen / muster / Stufe 2: „Plättchen in einer Figurenfolge: Figur 1: 7, Figur 2: 12, Figur 3: 17. Gib einen Term für die Anzahl bei Figur n an.“ · „Plättchen in einer Figurenfolge: Figur 1: 4, Figur 2: 9, Figur 3: 14. Gib einen Term für die Anzahl bei Figur n an.“
- terme.aufstellen / deuten / Stufe 2: „P = 2x + 3,5 (x = gefahrene km, P in €). Was bedeutet die Rechnung 2 · 4 + 3,5 = 11,5?“
- terme.umformen / produkte / Stufe 1: „Vereinfache: 9x · 9y“
- terme.umformen / ausmultiplizieren / Stufe 1: „Multipliziere aus: 8(5x + 9)“ · „Multipliziere aus: 7(7x + 5)“
- terme.umformen / summe_mal_summe / Stufe 1: „Multipliziere aus: (x + 4)(x + 2)“ · „Multipliziere aus: (x + 4)(x + 4)“
- terme.umformen / summe_mal_summe / Stufe 2: „Ein quadratischer Garten mit Seite x m wird 2 m länger und 2 m breiter. Gib die neue Fläche (x + 2)(x + 2) ohne Klammern an.“
- terme.umformen / ausklammern / Stufe 1: „Klammere den größten gemeinsamen Faktor aus: 4x + 16“ · „Klammere den größten gemeinsamen Faktor aus: 30x + 36“
- terme.umformen / ausklammern / Stufe 2: „Klammere den größten gemeinsamen Faktor aus: 20x² + 16x“ · „Klammere den größten gemeinsamen Faktor aus: 4x² + 2x“
- terme.umformen / aequivalenz / Stufe 1: „Berechne den Wert des Terms 2(x + 7) für x = 3.“ · „Welcher Term ist äquivalent zu 5(x + 2)?“ · „Welcher Term ist äquivalent zu 4(x + 2)?“ · „Welcher Term ist äquivalent zu 2(x + 2)?“
- terme.umformen / binomisch / Stufe 1: „Wende die 1. binomische Formel an: (x + 6)²“
- terme.umformen / binomisch / Stufe 2: „Multipliziere mit einer binomischen Formel aus: (2x + 4)²“
- abbildungen.kongruenz / achsenspiegelung / Stufe 2: „Spiegle P(−1 | −7) an der Geraden y = 3 (parallel zur x-Achse).“ · „Spiegle P(−8 | 6) an der Geraden y = 4 (parallel zur x-Achse).“ · „Spiegle P(−3 | 1) an der Geraden y = −4 (parallel zur x-Achse).“
- abbildungen.kongruenz / punktspiegelung / Stufe 1: „Spiegle P(−6 | −6) am Ursprung O(0 | 0).“ · „Spiegle P(−5 | 5) am Ursprung O(0 | 0).“
- abbildungen.kongruenz / punktspiegelung / Stufe 2: „Spiegle P(2 | −6) am Punkt Z(−4 | −2).“ · „Spiegle P(−6 | −3) am Punkt Z(1 | −1).“ · „Spiegle P(−7 | 4) am Punkt Z(4 | −4).“ · „Spiegle P(−4 | 5) am Punkt Z(1 | −1).“ · „Spiegle P(−1 | −6) am Punkt Z(1 | 3).“ · „Spiegle P(−7 | 2) am Punkt Z(−2 | 1).“ · „Spiegle P(3 | −5) am Punkt Z(0 | −2).“ · „Spiegle P(−1 | 4) am Punkt Z(2 | 2).“
- abbildungen.kongruenz / verschiebung / Stufe 1: „Verschiebe P(−5 | 7) mit v = (1 | −6).“ · „Verschiebe P(3 | −3) mit v = (−1 | −5).“
- abbildungen.kongruenz / verschiebung / Stufe 2: „P(−4 | 4) wird auf P'(−2 | 6) verschoben. Gib den Verschiebungspfeil an.“ · „P(−5 | 5) wird auf P'(−11 | 3) verschoben. Gib den Verschiebungspfeil an.“ · „P(3 | 2) wird auf P'(8 | −4) verschoben. Gib den Verschiebungspfeil an.“ · „P(3 | −1) wird auf P'(0 | 5) verschoben. Gib den Verschiebungspfeil an.“ · „P(−4 | 4) wird erst mit (5 | 2), dann mit (6 | 1) verschoben. Wohin kommt P?“
- abbildungen.kongruenz / drehung / Stufe 1: „Drehe P(−5 | −6) um O(0 | 0) um 180° gegen den Uhrzeigersinn.“ · „Drehe P(−4 | −6) um O(0 | 0) um 90° gegen den Uhrzeigersinn.“
- abbildungen.kongruenz / drehung / Stufe 2: „Drehe P(5 | −1) um O(0 | 0) um 90° gegen den Uhrzeigersinn.“ · „Drehe P(6 | 1) um O(0 | 0) um 270° gegen den Uhrzeigersinn.“ · „Drehe P(−5 | 3) um O(0 | 0) um 90° gegen den Uhrzeigersinn.“
- abbildungen.kongruenz / drehung / Stufe 3: „Drehe P(6 | −6) um Z(1 | −2) um 270° gegen den Uhrzeigersinn.“ · „Drehe P(−1 | −4) um Z(3 | −3) um 270° gegen den Uhrzeigersinn.“
- abbildungen.kongruenz / eigenschaften / Stufe 1: „Welche Aussage über Kongruenzabbildungen ist richtig?“
- abbildungen.kongruenz / eigenschaften / Stufe 2: „Das Dreieck ABC wird auf A'B'C' (gestrichelt) abgebildet. Welche Abbildung ist es?“ · „Das Dreieck ABC wird auf A'B'C' (gestrichelt) abgebildet. Welche Abbildung ist es?“ · „Das Dreieck ABC wird auf A'B'C' (gestrichelt) abgebildet. Welche Abbildung ist es?“ · „Das Dreieck ABC wird auf A'B'C' (gestrichelt) abgebildet. Welche Abbildung ist es?“ · „Das Dreieck ABC wird auf A'B'C' (gestrichelt) abgebildet. Welche Abbildung ist es?“
- geometrie.winkelsaetze / stufen_wechsel / Stufe 2: „g ∥ h. Bei S ist der Winkel links oberhalb 154° groß. Wie groß ist der Winkel bei T rechts oberhalb?“
- geometrie.winkelsaetze / innenwinkelsumme / Stufe 1: „In einem Dreieck ist α = 42° und γ = 76°. Wie groß ist β?“
- geometrie.winkelsaetze / vieleck / Stufe 1: „In einem Viereck ist α = 107°, β = 93° und γ = 87°. Wie groß ist δ?“
- gleichungen.linear / waage / Stufe 1: „Löse x − 13 = 2.“
- gleichungen.linear / waage / Stufe 2: „Löse 2,5x + 4 = 29.“ · „Löse −8x − 26 = −50.“ · „Löse 0,4x − 1,2 = 2.“
- gleichungen.linear / waage / Stufe 3: „Löse −3/5 x + 2 = 8.“
- gleichungen.linear / beide_seiten / Stufe 2: „Löse 2,5x − 6 = 4,5x + 10.“
- gleichungen.linear / klammern / Stufe 1: „Wie lautet 5(x + 2) ohne Klammer?“
- gleichungen.linear / sonderfaelle / Stufe 1: „Wie viele Lösungen hat 2(x + 13) = 2x + 26?“
- gleichungen.linear / sach / Stufe 2: „Lena hat 48 € und spart jede Woche 5 € dazu. Tom hat 102 € und gibt jede Woche 1 € aus. Nach wie vielen Wochen haben beide gleich viel?“
- bruch.prozent_grundwert / faktor / Stufe 1: „Ein Wert wird um 12 % verringert. Mit welchem Faktor multiplizierst du?“ · „Ein Wert wird um 4 % erhöht. Mit welchem Faktor multiplizierst du?“
- bruch.prozent_grundwert / faktor / Stufe 2: „Ein Wert wird mit dem Faktor 1,35 multipliziert. Um wie viel Prozent ändert er sich? (Zunahme positiv, Abnahme negativ angeben)“ · „Ein Wert wird mit dem Faktor 0,84 multipliziert. Um wie viel Prozent ändert er sich? (Zunahme positiv, Abnahme negativ angeben)“ · „Ein Wert wird mit dem Faktor 1,125 multipliziert. Um wie viel Prozent ändert er sich? (Zunahme positiv, Abnahme negativ angeben)“
- bruch.prozent_grundwert / vermehrt / Stufe 1: „Ein Sparguthaben beträgt 800 €. In einem Jahr kommen 2 % Zinsen dazu. Wie hoch ist das Guthaben danach?“ · „Ein Sparguthaben beträgt 3000 €. In einem Jahr kommen 1 % Zinsen dazu. Wie hoch ist das Guthaben danach?“ · „Ein Sparguthaben beträgt 2000 €. In einem Jahr kommen 2,5 % Zinsen dazu. Wie hoch ist das Guthaben danach?“
- bruch.prozent_grundwert / zurueck / Stufe 2: „Nach 45 % Rabatt kostet eine Ware 33 €. Wie viel kostete sie ursprünglich?“ · „Nach 3 % Rabatt kostet eine Ware 300,70 €. Wie viel kostete sie ursprünglich?“ · „Nach einer Erhöhung um 2 % kostet eine Ware 61,20 €. Wie viel kostete sie vorher?“ · „Nach einer Erhöhung um 35 % kostet eine Ware 222,75 €. Wie viel kostete sie vorher?“
- bruch.prozent_grundwert / prozentsatz / Stufe 1: „Ein Preis ändert sich von 150 € auf 187,50 €. Um wie viel Prozent ändert er sich? (Zunahme positiv, Abnahme negativ)“ · „Ein Preis ändert sich von 150 € auf 75 €. Um wie viel Prozent ändert er sich? (Zunahme positiv, Abnahme negativ)“ · „Ein Preis ändert sich von 500 € auf 540 €. Um wie viel Prozent ändert er sich? (Zunahme positiv, Abnahme negativ)“ · „Ein Preis ändert sich von 400 € auf 432 €. Um wie viel Prozent ändert er sich? (Zunahme positiv, Abnahme negativ)“ · „Ein Preis ändert sich von 50 € auf 41 €. Um wie viel Prozent ändert er sich? (Zunahme positiv, Abnahme negativ)“
- bruch.prozent_grundwert / prozentsatz / Stufe 2: „Ein Preis ändert sich von 25 € auf 24,25 €. Um wie viel Prozent ändert er sich? (Zunahme positiv, Abnahme negativ)“
- bruch.prozent_grundwert / mehrfach / Stufe 1: „Ein Preis von 200 € ändert sich um +5 %, dann +10 %. Wie hoch ist der Endpreis?“
- bruch.prozent_grundwert / argumente / Stufe 2: „Welche Aussage ist mathematisch richtig begründet?“ · „Welche Aussage ist mathematisch richtig begründet?“
- bruch.prozent_grundwert / argumente / Stufe 1: „Ein Preis von 80 € sinkt um 10 % auf 72 €. Welche Begründung zeigt das mathematisch?“
- daten.boxplot / mittel_median / Stufe 2: „Werte: 14; 90; 16; 18; 15; 10; 12. Um wie viel unterscheiden sich Mittelwert und Median? (größerer minus kleinerer Wert)“
- daten.boxplot / boxplot / Stufe 2: „Der Boxplot zeigt die Ergebnisse einer Erhebung (Zeit für 1 000 m). Etwa wie viel Prozent der Werte liegen unter 230 s?“
- daten.boxplot / vergleichen / Stufe 1: „Ergebnisse zweier Klassen beim 1 000-m-Lauf (in s), siehe Boxplots. Welche Aussage ist richtig?“
- geometrie.konstruktion / winkelsumme / Stufe 1: „In einem Dreieck ist α = 38° und β = 110°. Berechne γ.“ · „In einem Dreieck ist α = 54° und β = 83°. Berechne γ.“
- geometrie.konstruktion / gleichschenklig / Stufe 1: „Ein gleichschenkliges Dreieck hat den Spitzenwinkel γ = 24°. Wie groß ist ein Basiswinkel?“ · „Ein gleichschenkliges Dreieck hat den Spitzenwinkel γ = 66°. Wie groß ist ein Basiswinkel?“
- geometrie.konstruktion / gleichschenklig / Stufe 2: „Ein gleichschenkliges Dreieck hat den Basiswinkel 24°. Wie groß ist der Spitzenwinkel?“ · „Ein gleichschenkliges Dreieck hat einen Winkel von 164°. Wie groß sind die beiden anderen Winkel? Gib einen davon an.“
- geometrie.konstruktion / kongruenzsatz / Stufe 1: „Gegeben: c = 3 cm, α = 35°, β = 45°. Welcher Kongruenzsatz garantiert ein eindeutiges Dreieck?“
- geometrie.konstruktion / kongruenzsatz / Stufe 3: „Gegeben: a = 2 cm, c = 5 cm, α = 35° (α liegt a gegenüber). Wie viele Dreiecke gibt es?“ · „Gegeben: a = 3 cm, c = 6 cm, α = 30° (α liegt a gegenüber). Wie viele Dreiecke gibt es?“
- geometrie.konstruktion / konstruierbar / Stufe 1: „Kann man ein Dreieck mit a = 7 cm, b = 2 cm und c = 10 cm konstruieren?“ · „Kann man ein Dreieck mit a = 3 cm, b = 9 cm und c = 10 cm konstruieren?“
- geometrie.konstruktion / vierecke / Stufe 1: „In einem Parallelogramm ABCD ist α = 75°. Wie groß ist β?“ · „In einem Parallelogramm ABCD ist α = 40°. Wie groß ist β?“ · „In einem Viereck ist α = 68°, β = 96° und γ = 72°. Berechne δ.“ · „In einem Viereck ist α = 117°, β = 70° und γ = 76°. Berechne δ.“
- geometrie.konstruktion / vierecke / Stufe 2: „Ein Drachenviereck ABCD ist symmetrisch zur Diagonalen AC. Es ist α = 70° und γ = 60°. Wie groß ist β (= δ)?“ · „Ein Drachenviereck ABCD ist symmetrisch zur Diagonalen AC. Es ist α = 60° und γ = 75°. Wie groß ist β (= δ)?“
- geometrie.kreis / thales / Stufe 1: „Über einer 4 cm langen Strecke [AB] wird der Thaleskreis gezeichnet. Wie groß ist sein Radius?“
- geometrie.kreis / umkehrung / Stufe 1: „Das Dreieck ABC hat bei C einen rechten Winkel, A(3 | 3), B(3 | 13). Gib den Mittelpunkt des Kreises an, auf dem C liegt.“ · „Das Dreieck ABC hat bei C einen rechten Winkel, A(−6 | 1), B(−6 | 7). Gib den Mittelpunkt des Kreises an, auf dem C liegt.“ · „Das Dreieck ABC hat bei C einen rechten Winkel, A(−4 | 4), B(−4 | 10). Welchen Radius hat der Kreis, auf dem C liegen muss? (1 Einheit = 1 cm)“
- geometrie.kreis / umkehrung / Stufe 2: „Das Dreieck ABC hat bei C einen rechten Winkel, A(−5 | −1), B(1 | −1). Welchen Radius hat der Kreis, auf dem C liegen muss? (1 Einheit = 1 cm)“ · „Im Dreieck ABC ist α = 20° und β = 50°. Liegt C auf dem Kreis mit dem Durchmesser [AB]?“
- geometrie.kreis / beweis / Stufe 1: „Welche Aussage über Vermutung und Beweis ist richtig?“ · „Welche Aussage über Vermutung und Beweis ist richtig?“
- geometrie.kreis / lage / Stufe 1: „Ein Kreis hat den Radius r = 8 cm. Eine Gerade g hat vom Mittelpunkt den Abstand d = 8 cm. Wie heißt g?“ · „Ein Kreis hat den Radius r = 6 cm. Eine Gerade g hat vom Mittelpunkt den Abstand d = 6 cm. Wie heißt g?“
- geometrie.kreis / lage / Stufe 2: „Ein Kreis hat den Durchmesser 10 cm. Eine Gerade hat vom Mittelpunkt den Abstand 5 cm. Wie viele gemeinsame Punkte haben Kreis und Gerade?“ · „Ein Kreis hat den Durchmesser 4 cm. Eine Gerade hat vom Mittelpunkt den Abstand 4 cm. Wie viele gemeinsame Punkte haben Kreis und Gerade?“ · „Ein Kreis hat den Durchmesser 10 cm. Eine Gerade hat vom Mittelpunkt den Abstand 4,5 cm. Wie viele gemeinsame Punkte haben Kreis und Gerade?“ · „Ein Kreis hat den Durchmesser 18 cm. Eine Gerade hat vom Mittelpunkt den Abstand 8 cm. Wie viele gemeinsame Punkte haben Kreis und Gerade?“
- geometrie.kreis / tangente / Stufe 1: „Von P aus werden zwei Tangenten an den Kreis um M gelegt; sie bilden den Winkel ∠BPB' = 54°. Wie groß ist ∠BPM?“
- geometrie.kreis / tangente / Stufe 2: „Von P aus werden zwei Tangenten an den Kreis um M gelegt, Berührpunkte B und B'. Es ist ∠BPB' = 94°. Wie groß ist ∠BMB'?“ · „Von P aus werden zwei Tangenten an den Kreis um M gelegt, Berührpunkte B und B'. Es ist ∠BPB' = 80°. Wie groß ist ∠BMB'?“ · „Von P aus werden zwei Tangenten an den Kreis um M gelegt, Berührpunkte B und B'. Es ist ∠BPB' = 40°. Wie groß ist ∠BMB'?“ · „Von P aus werden zwei Tangenten an den Kreis um M gelegt, Berührpunkte B und B'. Es ist ∠BPB' = 48°. Wie groß ist ∠BMB'?“
- geometrie.kreis / umkreis_inkreis / Stufe 2: „Ein Dreieck hat α = 49°, β = 50°. Wo liegt der Umkreismittelpunkt?“ · „Ein Dreieck hat α = 23°, β = 67°. Wo liegt der Umkreismittelpunkt?“ · „Ein Dreieck hat α = 38°, β = 95°. Wo liegt der Umkreismittelpunkt?“ · „Ein Dreieck hat α = 83°, β = 85°. Wo liegt der Umkreismittelpunkt?“

### (5) Quellen der Prüfungsvorbilder

Übernommen wurden nur Aufgabentyp und Niveau, nie Wortlaut oder Zahlen. Die Vorbilder stammen aus der Recherche der Zehnten, Achtzehnten und Neunzehnten Runde (dort geöffnet und belegt); in dieser Runde wurden keine neuen Prüfungsdokumente geöffnet. Je Thema steht das Vorbild als Kommentar am Anfang des STUFEN-Abschnitts im Generator.

- Bayerischer Mathematik-Test 8 (ISB), Gruppe A/B: [2019](https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2019/bmt8_2019_aufgaben_gruppe_b.pdf), [2021](https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2021/bmt8_2021_aufgaben_gruppe_a.pdf), [2022](https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2022/bmt8_2022_aufgaben_gruppe_a.pdf), [2023](https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2023/BMT8_2023_Aufgaben_Gruppe_A.pdf), [2024](https://isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2024/BMT8_2024_Aufgaben_Gruppe_A.pdf), [2025](https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/BMT8_2025_Aufgaben_Gruppe_A.pdf) – Terme vereinfachen, ausklammern ergänzen, äquivalente Terme, Terme im Sachzusammenhang, Gleichungen mit Dezimalzahlen und Klammern, Prozent-Terme, Grundwert aus reduziertem Preis.
- Jahrgangsstufentest Realschule 8 (ISB): [2019 I](https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2019/2019_jt_mathe_8_i_angabe.pdf), [2019 II](https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2019/2019_jt_mathe_8_ii_angabe.pdf), [2020 II Lösung](https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2020/2020_jt_mathe_8_ii_loesung.pdf), [2025 II Lösung](https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/2025_JT_Mathematik_8_II_Loesung.pdf) – Abbildungen im Koordinatensystem, Viereck aus Koordinaten, Boxplots vergleichen, Kennwerte, Thaleskreis-Nachweis, Kreis und Gerade.
- Knobel-Stil (keine Einzelaufgabe übernommen): [Känguru der Mathematik 2023, Klassen 7/8](https://didaktik.mathematik.hu-berlin.de/user/beierarx/kaenguru2023_78.pdf) und Mathematik-Olympiade (Schulrunde). Klassiker ohne Quelle im Einzelnen: Flasche und Korken, Ziegelstein, Wassermelone, Diophant, Euler-Polynom n² + n + 41, Kartenregel (Wason), Hühner und Kaninchen.

### Annahmen und Entscheidungen

1. **Überzählig ohne Typ (Annahme):** „Jede Übung bekommt einen Typ“ und die Prüfregel „höchstens 2 Übungen je Stufe, Typ und Satzbau“ widersprechen sich, wenn eine Karte 3 und mehr gleich gebaute Übungen hat. Die überzähligen Übungen behalten kein g (nicht gelöscht, Liste oben). Weil dadurch nicht alle Übungen einer Karte ein g haben, laufen die „alle mit g“-Regeln des Prüfers für diese Karten nicht; `_stufen_kl7.py` prüft dieselben Regeln selbst (Mindestzahlen und Typen je Stufe, höchstens 3 je Typ in Stufe 3, höchstens 2 je Satzbau) und bricht sonst ab. Alternative: überzählige Übungen löschen – das wäre eine Entscheidung für den Nutzer.
2. **Umstufungen (25):** nur, wo der Typ nicht zur Stufe passte – vor allem reine Rechenaufgaben, die in Stufe 3 standen (z. B. „Löse 7x − (4x − 9) = 30“, Faktor-Rechnungen) → Stufe 2; einzelne Fehleraufgaben aus Stufe 2 → Stufe 3; reine Erkennen-Fragen aus Stufe 2 → Stufe 1. Frage und Antworten unverändert.
3. **Typzuordnung bei Grenzfällen:** Wo eine Karte in Stufe 3 sonst mehr als 3 Aufgaben eines Typs gehabt hätte, ist die nächstpassende Kategorie gewählt (z. B. Diagonalenzahl aus der Winkelsumme als „transfer“). Das ist eine Ermessensentscheidung, kein Rechenergebnis.
4. **Lehrplan-Reihenfolge:** Neue Aufgaben nutzen nur Inhalte bis zum jeweiligen Thema (keine Geradengleichungen, kein Pythagoras, keine Trigonometrie). Alte Aufgaben mit späterem Stoff (z. B. Thales in geometrie.konstruktion/satz_kehrsatz) sind nicht angefasst, nur typisiert.
5. **Knobel-Tipps** nennen die Blickrichtung, nicht die Idee; Lösungswege sind ausführlich (mindestens 60 Zeichen, meist mit Probe). Bei Zählaufgaben ohne Rechnung steht in c die Zählsumme (z. B. `1 + 2 + 4 + 6`), sonst die echte Rechnung.

### Offene Punkte

- Kein Merge, keine Datenbank, kein App-Code. Merge nach lernen-app erst nach Freigabe.
- Prüfer-Hinweis „mit g / ohne g“ bleibt bei Karten mit überzähligen Übungen bestehen (siehe Annahme 1).

### (6) Beispiel-Bordkarten: abbildungen.kongruenz / punktspiegelung

Je drei Bordkarten pro Stufe im vollen Wortlaut (bevorzugt neue), dazu beide Knobel-Bordkarten.


#### Stufe 1

- **Stufe 1, Typ direkt** (neu)
  - Aufgabe: Spiegle Q(−3 | 0) am Ursprung.
  - Lösung: Q'(3 | 0)
  - Tipp: Was passiert mit −3, was mit 0?
  - Lösungsweg: Beide Vorzeichen wechseln: Q'(3 | 0). Die 0 bleibt 0.
- **Stufe 1, Typ erkennen** (neu)
  - Aufgabe: Was passiert mit den Koordinaten bei einer Punktspiegelung am Ursprung?
  - Auswahl: Nur x wechselt das Vorzeichen. | x und y werden vertauscht. | Beide wechseln das Vorzeichen. | Nur y wechselt das Vorzeichen.
  - Lösung: Beide wechseln das Vorzeichen.
  - Tipp: Probiere es mit P(2 | 1).
  - Lösungsweg: Der Bildpunkt liegt genau gegenüber: gleich weit vom Ursprung, aber in der Gegenrichtung. Aus (x | y) wird (−x | −y).
- **Stufe 1, Typ direkt** (alt)
  - Aufgabe: Spiegle P(2 | 4) am Ursprung O(0 | 0).
  - Lösung: P'(−2 | −4)
  - Tipp: Gehe von P zum Ursprung und noch einmal so weit.
  - Lösungsweg: Am Ursprung ändern beide Koordinaten ihr Vorzeichen: P'(−2 | −4).

#### Stufe 2

- **Stufe 2, Typ mehrschritt** (neu)
  - Aufgabe: Das Dreieck A(1 | 1), B(3 | 1), C(1 | 4) wird am Punkt Z(4 | 2) gespiegelt. Gib B' an.
  - Lösung: B'(5 | 3)
  - Tipp: Gehe von B zu Z und denselben Weg weiter.
  - Lösungsweg: Von B nach Z: 1 nach rechts, 1 nach oben. Noch einmal: B'(5 | 3).
- **Stufe 2, Typ umkehr** (neu)
  - Aufgabe: Nach einer Spiegelung am Punkt Z(1 | 2) liegt der Bildpunkt bei P'(4 | −1). Wo lag P?
  - Lösung: P(−2 | 5)
  - Tipp: Spiegle P' an Z zurück.
  - Lösungsweg: Von P' nach Z: 3 nach links, 3 nach oben. Denselben Weg noch einmal: P(−2 | 5). Probe: Z ist die Mitte von (−2 | 5) und (4 | −1) ✓.
- **Stufe 2, Typ einkleidung** (neu)
  - Aufgabe: Ein Drehkreuz hat die Mitte M(3 | 3). Ein Arm endet bei (5 | 6). Der gegenüberliegende Arm ist gleich lang und zeigt genau in die Gegenrichtung. Wo endet er?
  - Lösung: E(1 | 0)
  - Tipp: Das ist eine Punktspiegelung an M.
  - Lösungsweg: Von M zum Armende: 2 nach rechts, 3 nach oben. Gegenrichtung: 2 nach links, 3 nach unten: E(1 | 0).

#### Stufe 3

- **Stufe 3, Typ begruenden** (neu)
  - Aufgabe: Warum ist jedes Parallelogramm punktsymmetrisch?
  - Auswahl: Seine Diagonalen halbieren sich; am Schnittpunkt gespiegelt fällt jede Ecke auf die gegenüberliegende. | Weil es eine Symmetrieachse hat. | Weil benachbarte Seiten senkrecht aufeinander stehen. | Weil es vier Ecken hat.
  - Lösung: Seine Diagonalen halbieren sich; am Schnittpunkt gespiegelt fällt jede Ecke auf die gegenüberliegende.
  - Tipp: Was ist der Schnittpunkt der Diagonalen für die Strecken [AC] und [BD]?
  - Lösungsweg: Im Parallelogramm halbieren sich die Diagonalen gegenseitig. Der Schnittpunkt ist also die Mitte von [AC] und von [BD]: A geht auf C, B auf D – und damit die ganze Figur auf sich selbst.
- **Stufe 3, Typ pruefung** (neu)
  - Aufgabe: Das Dreieck A(1 | 0), B(3 | 0), C(3 | 2) wird am Punkt Z(4 | 1) gespiegelt. Wie groß ist der Flächeninhalt des Vierecks ABA'B' (in Flächeneinheiten)?
  - Lösung: 4
  - Tipp: Bestimme zuerst A' und B'.
  - Lösungsweg: A'(7 | 2) und B'(5 | 2). Das Viereck A(1 | 0), B(3 | 0), A'(7 | 2), B'(5 | 2) ist ein Parallelogramm: [AB] und [A'B'] sind waagrecht und je 2 lang, der Abstand ist 2. Fläche 2 · 2 = 4.
- **Stufe 3, Typ fehler** (neu)
  - Aufgabe: Jemand spiegelt P(5 | 1) am Punkt Z(2 | 3) und rechnet: P'(2 − 5 | 3 − 1) = P'(−3 | 2). Was stimmt?
  - Auswahl: Falsch: Von Z aus muss es noch einmal den Weg von P nach Z gehen; richtig ist P'(−1 | 5). | Falsch: Richtig ist P'(−3 | −2). | Falsch: Richtig ist P'(7 | 4). | Richtig gerechnet.
  - Lösung: Falsch: Von Z aus muss es noch einmal den Weg von P nach Z gehen; richtig ist P'(−1 | 5).
  - Tipp: Ist Z die Mitte von P und (−3 | 2)?
  - Lösungsweg: Von P(5 | 1) nach Z(2 | 3): 3 nach links, 2 nach oben. Von Z aus noch einmal: (−1 | 5). Die Rechnung „Z − P“ ergibt nur den Weg, nicht den Bildpunkt.

#### Knobel (Pool bonus, s = 3)

- **Stufe 3, Typ knobel** (neu)
  - Aufgabe: Der Punkt P(0 | 0) wird abwechselnd an A(1 | 0) und an B(1 | 1) gespiegelt: zuerst an A, dann an B, dann wieder an A usw. Wo liegt er nach 10 Spiegelungen?
  - Lösung: P(0 | 10)
  - Tipp: Rechne vier Spiegelungen aus und vergleiche die Lage nach der 2. und der 4.
  - Lösungsweg: Schrittweise: (0 | 0) → an A (2 | 0) → an B (0 | 2) → an A (2 | −2) → an B (0 | 4). Nach je zwei Spiegelungen ist der Punkt um 2 nach oben gewandert (zwei Punktspiegelungen ergeben eine Verschiebung um den doppelten Weg von A nach B). 10 Spiegelungen = 5 Paare: (0 | 10).
- **Stufe 3, Typ knobel** (neu)
  - Aufgabe: Ein Punkt X wird an A(1 | 2) gespiegelt, sein Bild an B(4 | 2) und dieses Bild an C(4 | 5). Danach liegt der Punkt wieder genau bei X. Wo liegt X?
  - Lösung: X(1 | 5)
  - Tipp: Was bewirken die ersten beiden Spiegelungen zusammen?
  - Lösungsweg: Die Spiegelungen an A und dann an B wirken zusammen wie eine Verschiebung um den doppelten Weg von A nach B, also um (6 | 0). X + (6 | 0) muss an C auf X zurückgehen, also ist C die Mitte von X und X + (6 | 0): X liegt 3 links von C, also X(1 | 5). Probe: (1 | 5) → an A (1 | −1) → an B (7 | 5) → an C (1 | 5) ✓.

## 2026-11-17 – STATUS
geometrie.kreis fertig: alle alten Übungen mit Typ (außer überzähligen), 0 umgestuft, 22 neue Übungen, 12 Knobel-Bordkarten, 23 überzählig. Prüfer OK, 0 Gruppen, Nachweis OK.

## 2026-11-17 – STATUS
geometrie.konstruktion fertig: alle alten Übungen mit Typ (außer überzähligen), 0 umgestuft, 30 neue Übungen, 16 Knobel-Bordkarten, 17 überzählig. Prüfer OK, 0 Gruppen, Nachweis OK.

## 2026-11-17 – STATUS
daten.boxplot fertig: alle alten Übungen mit Typ (außer überzähligen), 1 umgestuft, 24 neue Übungen, 12 Knobel-Bordkarten, 3 überzählig. Prüfer OK, 0 Gruppen, Nachweis OK.

## 2026-11-17 – STATUS
bruch.prozent_grundwert fertig: 125 alte Übungen mit Typ, 5 umgestuft (reine Faktor-Rechnungen nach Stufe 2, Fehleraufgabe „Tom“ nach Stufe 3), 28 neue Übungen, 14 Knobel-Bordkarten, 22 überzählig. Prüfer OK, 0 Gruppen, Nachweis OK.

## 2026-11-17 – STATUS
gleichungen.linear fertig: 132 alte Übungen mit Typ, 6 umgestuft (reine Rechenaufgaben von Stufe 3 nach 2), 22 neue Übungen, 12 Knobel-Bordkarten, 9 überzählig. Prüfer OK, 0 Gruppen, Nachweis OK.

## 2026-11-17 – STATUS
geometrie.winkelsaetze fertig: alle alten Übungen mit Typ, 0 umgestuft, 28 neue Übungen, 16 Knobel-Bordkarten, 3 überzählig. Prüfer OK, 0 Gruppen, Nachweis OK.

## 2026-11-17 – STATUS
abbildungen.kongruenz fertig (10 Karten): 161 alte Übungen mit Typ, 1 umgestuft, 42 neue Übungen, 20 Knobel-Bordkarten, 33 überzählig. Prüfer OK, 0 Gruppen, Nachweis OK.

## 2026-11-17 – STATUS
terme.umformen fertig: 110 alte Übungen mit Typ, 4 umgestuft, 51 neue Übungen (vor allem Stufe 3), 16 Knobel-Bordkarten, 16 überzählig. Prüfer OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 – STATUS
terme.aufstellen fertig: alle 119 nicht überzähligen alten Übungen mit Typ, 8 umgestuft, 21 neue Übungen, 12 Knobel-Bordkarten, 4 überzählig. Prüfer OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK (`python3 -I inhalte/generatoren/_stufen_nachweis.py terme.aufstellen`).
