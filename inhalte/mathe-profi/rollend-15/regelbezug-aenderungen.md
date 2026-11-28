# Regelbezug-Lernkarten: was Runde 15 ändern würde und was umgesetzt ist

Quelle: `inhalte/plan/regelbezug-lernkarten.json`, erzeugt von `tools/regelbezug_lernkarten.py`. Auflage Werkstatt 1209: Das bloße Neuerzeugen mit Runde 15 ändert nicht nur Zähler.

## Was live aus dieser Datei entsteht

Nichts in der Datenbank. Die Migration RB-S nennt die Datei ausdrücklich als Datei (nicht in der Datenbank); sie dient dem Client für die Erklärkarte und als Rückfall für Aufgaben ohne eigene Regel (`themen[<thema>].lernkarten[<lernziel>].regel`). `rb_nachtrag_r15.sql` schreibt nur `schule.aufgabe_regel` je Aufgabe der Runde und fasst keine Karten-Zuordnung an. Die Datei wirkt erst, wenn der Client sie mit einem App-Stand ausliefert.

## Die sieben fachlichen Änderungen beim Neuerzeugen OHNE Festhalten

Zählregel des Werkzeugs: Hauptregel, wenn mindestens 2 Aufgaben der Karte eine Regel tragen und die häufigste mindestens 2/3 davon hat; sonst „offen“ (kein Regel-Knopf, Karte steht auf der Redaktionsliste). Runde 15 vergibt je Aufgabe die tragende Regel des Lösungswegs (z. B. `rr.waage`), die Karte meint die breitere Regel `id.algebra.gleichung_loesen`. Dadurch kippt die Mehrheit.

| Karte | vorher | nachher (ohne Festhalten) | Ursache (Aufgaben von Runde 15) | Empfehlung |
|---|---|---|---|---|
| funktionen.quadratisch / nullstellen | `id.algebra.gleichung_loesen` (3/3) | offen | V161, V162 tragen `id.funktionen.zuordnung`; 3 von 5 = 60 % < 2/3 | Zuordnung der Karte festhalten. Kennungen von V161/V162 bleiben (der Lösungsweg liest dort tatsächlich an der Funktion ab). |
| gleichungen.linear / sonderfaelle | `id.algebra.gleichung_loesen` (5/5) | offen | V105, V106, V107 tragen `rr.waage`; 5 von 8 | festhalten; Aufgaben-Kennungen bleiben (Waage ist der Umformschritt, die Karte das Gleichungslösen). |
| gleichungen.linear / sach | `id.algebra.gleichung_loesen` (5/6) | offen | V108, V109, V110 tragen `rr.waage`; 5 von 9 | festhalten; Kennungen bleiben. |
| gleichungen.quadratisch / reinquadratisch | `id.algebra.gleichung_loesen` (3/3) | offen | V140, V141 tragen `rr.gegenrechnung`; 3 von 5 | festhalten; Kennungen bleiben. |
| gleichungen.quadratisch / loesungsformel | `id.algebra.gleichung_loesen` (3/3) | offen | V147, V148 tragen `rr.reihenfolge` als „Nur Teilregel“ (Rechenreihenfolge beim Auswerten); 3 von 5 | festhalten. Teilregel-Aufgaben nie zur Mehrheit der Karte zählen lassen; Kennungen bleiben, weil sie für die Aufgabe selbst stimmen. |
| gleichungen.quadratisch / sachaufgabe | `id.algebra.gleichung_loesen` (3/3) | offen | V152 `rr.nullprodukt`, V153 `rr.reihenfolge` („Nur Teilregel“); 3 von 5 | festhalten; Kennungen bleiben. |
| terme.umformen / produkte | `rr.vorzeichen` (5/6), weitere: keine | `rr.vorzeichen` (6/9), weitere `rr.tauschen` | V035 und V037 tragen `rr.tauschen` (dazu eine ältere Aufgabe: 3 mal), V036 `rr.vorzeichen`; Hauptregel bleibt (6/9 = 2/3) | harmlos. Die weitere Regel wäre fachlich passend (Faktoren vertauschen), ist aber eine Ergänzung, keine Reparatur; wurde nicht übernommen (siehe unten). |

Dazu wächst die Redaktionsliste von 129 auf 135 Karten (die sechs Karten oben). Alle übrigen Karten behalten die Regel; bei vielen ändern sich nur die Zähler `aufgaben` und `anteil`.

## Was umgesetzt ist (ohne Änderung bestehender Pakete)

`tools/regelbezug_lernkarten.py` hält die Zuordnung „wie eingespielt“ fest: Für die Hauptregel einer Karte zählen nur die Runden bis `GRUNDSTAND_BIS = 14`. Hat eine Karte aus diesem Stand eine Regel, bleibt sie unverändert; Runde 15 darf sie weder ändern noch entziehen und fügt auch keine weitere Regel hinzu. Karten, die bis Runde 14 offen waren, würden aus Runde 15 gewinnen können; das trifft keine Karte. Ergebnis: Das Neuerzeugen ergibt für alle Zuordnungen (`themen`) dasselbe wie vorher. Geändert sind nur zwei Begründungstexte der Redaktionsliste (`bruch.prozent_grundwert/zurueck` und `gleichungen.linear/klammern`: die Häufigkeiten nennen jetzt die Aufgaben mit Runde 15, die Karten bleiben offen wie vorher). `regelbezug_lernkarten.py --pruefen` ist OK.

Kein Paket unter `tools/tests/aus/` ändert sich dadurch; die Datei wird von keinem Paket gelesen.

## Was der Projektleiter entscheiden muss

1. Festhalten (umgesetzt, empfohlen) oder das Festhalten wieder abschalten (`GRUNDSTAND_BIS` auf die höchste Runde setzen): Dann verlieren sechs Karten ihren Regel-Knopf in der Erklärkarte und im Rückfall, und `rr.tauschen` kommt bei `terme.umformen/produkte` als weitere Regel dazu. Ich sehe keinen fachlichen Grund dafür.
2. Ob die weitere Regel `rr.tauschen` bei `produkte` später ergänzt werden soll. Das ginge nur mit einer eigenen Änderung (eine Karte von Hand ergänzen), nicht mit der Zählregel.
3. Langfristig: Die Zählregel mischt „Regel der Karte“ und „tragende Regel der Aufgabe“. Teilregel-Aufgaben („Nur Teilregel“) sollten nicht mitzählen. Das ist eine Änderung der Zählregel für künftige Runden, nicht Teil dieses Auftrags.
