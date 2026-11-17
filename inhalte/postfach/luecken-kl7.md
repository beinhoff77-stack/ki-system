# Postfach luecken-kl7 (Achtzehnte Runde, Teil B, Klasse 7)

## 2026-11-17 – FERTIG: Abschlussbericht

Zweig luecken-kl7 (von lernen-app 4a71771), zwei Commits: abbildungen.kongruenz (6cacb46), geometrie.konstruktion (6f151a9). Kein Merge.

**Neue Lernkarten** (alle Pflicht; je 18 Übungen 4/6/8 mit 2 Prüfungsvorbild- und 1 Knobelaufgabe auf Stufe 3, 1 Test, 3 Korrektur, 6 Sicherung; Karten im neuen Muster mit einstieg, woerter, Bildergeschichte mit Zeichnung je Schritt, fehler + fehler_bild, regel, probe):

| Thema | Lernkarte | Stelle | Lehrplan-Bezug (selbst geprüft auf lehrplanplus.bayern.de, Gym. M7) | Prüfungsvorbilder (Typ/Niveau, eigene Zahlen) |
|---|---|---|---|---|
| abbildungen.kongruenz | mittelsenkrechte („Mittelsenkrechte und Lot“) | nach punktspiegelung | M7 2.1: „konstruieren Mittelsenkrechte, Lote und Winkelhalbierende und beschreiben ihr Vorgehen“; Abstandsprobleme (Schwerpunktsetzung 2021) | BMT8 2024 A4b (Schiff gleich weit von zwei Leuchttürmen), 2019 A4 / 2014 B (Punkt gleich weit von drei Orten), 2022 A1c (Abstand von g und von C) |
| abbildungen.kongruenz | winkelhalbierende | nach mittelsenkrechte | M7 2.1 (wie oben) | Abstandsproblem nach BMT8 2022 A1; Nebenwinkel-Winkelhalbierende (Standard-Schulaufgabe) |
| abbildungen.kongruenz | vierecke_ordnen („Symmetrische Vierecke ordnen“) | nach symmetrie | M7 2.1: „ordnen … die Menge aller symmetrischen Vierecke anhand ihrer Symmetrieeigenschaften“ | BMT8 2023 A3 (Raute, Gegenbeispiel); „Haus der Vierecke“ (Grundwissen Kl. 7) |
| geometrie.konstruktion | planfigur („Planfigur und Konstruktionsbeschreibung“) | nach konstruierbar | M7 5: „konstruieren Dreiecke aus verschiedenen Bestimmungsstücken (darunter insbesondere Höhen) und nutzen zur Ideenfindung Planfiguren“ | ISB/Uni Bayreuth SMART „Konstruktionen in Jgst. 7“; Schulaufgabe Kl. 7 (klassenarbeiten.de 3023); BMT8 2012 A8 |

Quelle je Thema zusätzlich unter inhalt.quellen.luecken_kl7, Begründung unter „offen“ (neuer Eintrag).

**Erweiterte Karten:** keine. Lücke 6 (Vierecke) wurde als eigene Karte gelöst, damit die freigegebene Karte symmetrie unverändert bleibt.

**Nachweis:** `python3 -I inhalte/generatoren/_luecken_kl7_nachweis.py <thema>` gegen origin/lernen-app: alle alten Karten und Aufgaben Zeichen für Zeichen gleich und vorn; abschnitte/teilfaehigkeiten/bewertung nur um die neuen Lernziele ergänzt; quellen/offen nur ergänzt. `tools/inhalt_pruefen.py`: beide OK, ohne Warnung. Generatoren laufen reproduzierbar (eigener Abschnitt, Seeds 7180 und 7250, Werkzeug inhalte/generatoren/_luecken_kl7.py).
Alle 112 neuen Aufgaben gelesen; Zahl/Lücken über „c“ nachgerechnet, bei Auswahl prüft der Generator, dass genau eine Antwort richtig ist (Punkte gleich weit, Vierecks-Beziehungen, Radien).
Zeichnungen maßstäblich berechnet (Kreisschnittpunkte, 35°-Hälften, Lote, 50°-Schenkel); in der App nicht angesehen.

**Offen geblieben / Hinweise:**
- Selbst konstruieren (Zirkel, Lineal) kann das Kind in der App nicht. Abgefragt werden Eigenschaften, Schritte der Konstruktionsbeschreibung (Auswahl), Abstände, Radien und Lagen im Koordinatensystem. App-Wunsch bleibt: Eingabe durch Zeichnen.
- Aufgaben vermeiden schräge Längen (Pythagoras erst später); Mittelsenkrechten im Koordinatensystem daher waagrecht/senkrecht oder mit Kästchenzählen.
- Lücke 4: Umzug der Potenzgesetz-Karten von terme.potenzgesetze nach terme.umformen nur gemeldet (Umzug gehört nicht zu diesem Auftrag).
- geometrie.konstruktion, alter „offen“-Eintrag verweist für Mittelsenkrechte/Winkelhalbierende noch auf geometrie.ortslinien (Kl. 5) – überholt, aber laut Auftrag unverändert; der neue Eintrag sagt das.
- Überschneidung: geometrie.konstruktion/konstruierbar enthält schon zwei Stufe-3-Aufgaben mit Mittelsenkrechten/Abständen (Schwer-Runde); unverändert.
- Einspielen (Haupt-Chat): neue Lernkarten in freigegebenen Themen – Weg wie bei geänderten Erklärungen (einheit_abgleichen …).

## 2026-11-17 – STATUS
geometrie.konstruktion fertig: neue Pflicht-Lernkarte planfigur nach konstruierbar (LehrplanPLUS M7 5), 28 Aufgaben. Prüfer OK, Nachweis OK (7 alte Karten, 210 alte Aufgaben unverändert). Unter „offen“ ein neuer Eintrag, alte Einträge unverändert.

## 2026-11-17 – STATUS
abbildungen.kongruenz fertig: neue Lernkarten mittelsenkrechte und winkelhalbierende (nach punktspiegelung) und vierecke_ordnen (nach symmetrie), alle Pflicht (LehrplanPLUS M7 2.1), je 28 Aufgaben. Prüfer OK, Nachweis OK (`python3 -I inhalte/generatoren/_luecken_kl7_nachweis.py abbildungen.kongruenz`: 7 alte Karten und 210 alte Aufgaben unverändert).

## 2026-11-17 – STATUS: Bestandsaufnahme (inhalte/pruefung/aufbau/klasse7.json, Feld „luecken“, Stand origin/lernen-app 4a71771)

| # | Lücke | Dringlichkeit | Stand |
|---|---|---|---|
| 1 | Winkelsätze (M7 2.2) | hoch | erledigt: eigenes Thema geometrie.winkelsaetze (8 Karten, freigegeben). Nicht Teil dieses Auftrags (neues Thema). |
| 2 | Mittelsenkrechte, Lot, Winkelhalbierende; Abstandsprobleme (M7 2.1) | hoch | offen → in diesem Auftrag erledigt (abbildungen.kongruenz, Karten mittelsenkrechte, winkelhalbierende). Vorher nur Einzelaufgaben in geometrie.konstruktion/konstruierbar (Stufe 3: „Abstand von g und von C“, „Brunnen gleich weit von drei Häusern“). |
| 3 | Lineare Gleichungen (M7 3) | hoch | erledigt: eigenes Thema gleichungen.linear. Nicht Teil dieses Auftrags (neues Thema). |
| 4 | Terme umformen inkl. Potenzgesetze (M7 1.2) | hoch | erledigt: eigenes Thema terme.umformen. Nicht Teil dieses Auftrags (neues Thema). Das Verschieben der Gesetze-Karten aus terme.potenzgesetze (Kl. 6) nach terme.umformen ist ein Umzug zwischen Themen – nur gemeldet, nicht ausgeführt: terme.umformen hat keine Potenz-Karte; die Potenzgesetze (mal/geteilt gleiche Basis, gleicher Exponent, anwenden) stehen weiter in terme.potenzgesetze. |
| 5 | Dreiecke konstruieren mit Planfigur und Konstruktionsbeschreibung, auch mit Höhen (M7 5) | mittel | offen → in diesem Auftrag: geometrie.konstruktion, neue Karte planfigur nach konstruierbar. |
| 6 | Symmetrische Vierecke ordnen, „Haus der Vierecke“ (M7 2.1) | niedrig | offen → in diesem Auftrag erledigt als eigene Karte vierecke_ordnen in abbildungen.kongruenz (nach symmetrie); die Karte symmetrie bleibt unverändert. |
| 7 | Boxplots zeichnen/ablesen (M7 4) | mittel | erledigt (wo: daten.boxplot): Karte boxplot hat Bild „boxplot“, Karte vergleichen Bild „boxplot“ mit zwei Reihen (Klasse A/B); 56 Aufgaben mit Boxplot-Zeichnung, darunter „Lies den Median/das Maximum/das untere Quartil ab“ und „Welcher Boxplot passt zu diesen Daten?“. Der veraltete Eintrag unter „offen“ (nur Tabellen) steht dort nicht mehr. Nichts zu tun. |

Hinweis (nur gemeldet): Der Eintrag unter „offen“ in geometrie.konstruktion („Mittelsenkrechte und Winkelhalbierende als Ortslinien sind Stoff von geometrie.ortslinien (Klasse 5)“) ist mit diesem Auftrag überholt; alte Einträge bleiben laut Auftrag unverändert, ein neuer Eintrag erklärt den Stand.
