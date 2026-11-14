# Postfach einarbeiten-kl5

## 2026-11-14 17:40 – FERTIG
Paket „Einarbeiten Klasse 5“ vollständig: alle 11 Themen eingearbeitet, je Thema ein Commit auf `einarbeiten-kl5`, Prüfskript bei allen OK, alle Generatoren laufen reproduzierbar. Nur Dateien unter `inhalte/` geändert (Generatoren, Themen, `_kl5.py`, `_kl5_rest.py`, dieses Postfach).

| Thema | umgesetzt | abgelehnt | neue Lernkarten | Bilder Lernkarten / Aufgaben | Lernkarten / Aufgaben |
|---|---|---|---|---|---|
| zahlen.ganz | 35 | 0 | – | 3 / 2 (+ Markierungsaufgaben) | 8 / 224 |
| zahlen.rechengesetze | 33 | 0 | differenz_summe | 0 / 0 | 10 / 250 |
| zahlen.potenzen_basis | 27 | 0 | – | 1 / 0 | 7 / 175 |
| groessen.proportional | 34 | 0 | – | 3 / 10 | 7 / 175 |
| groessen.einheiten | 18 | 0 | – | 2 / 1 | 8 / 224 |
| geometrie.grundbegriffe | 20 | 0 | – | 6 / 73 | 7 / 196 |
| geometrie.winkel | 15 | 0 | – | 6 / 80 | 7 / 196 |
| geometrie.ortslinien | 14 | 0 | – | 4 / 63 | 6 / 168 |
| messen.flaechen | 12 | 0 (1 zurückgestellt) | – | 4 / 41 | 7 / 196 |
| messen.koerper_berechnung | 14 | 1 | – | 3 / 22 | 6 / 168 |
| stochastik.kombinatorik | 14 | 0 | – | 2 / 13 | 7 / 196 |

Zählweise: jedes Feld unter karten[].neu je Karte, handlungsrelevante thema_hinweise, jeder fehlende Aufgabentyp, jede Generator-Regel, jeder Fehler.
Korrektur: In den Commit-Nachrichten bzw. STATUS-Zeilen stehen für geometrie.winkel 19, geometrie.ortslinien 17 und messen.flaechen 15 – nach dieser Zählweise sind es 15, 14 und 12.

Abgelehnt / zurückgestellt (mit Begründung unter offen der Themen-Datei):
- messen.koerper_berechnung: Volumeneinheiten (dm³, Liter) nicht eingebaut – Raumeinheiten sind laut LehrplanPLUS Kl. 6, die Karte volumen bleibt Vertiefung.
- messen.flaechen: Vorschlag einer eigenen Lernkarte „Näherungswerte mit Rechtecken“ (krumme Fläche im Kästchengitter) noch nicht gebaut.

Verbleibende offen-Punkte (Auszug):
- groessen.proportional: Ursprungsgerade bewusst weggelassen (Lehrplan Kl. 5); Produktgleichheit gehört zu Kl. 8.
- groessen.einheiten: Flächen-/Raumeinheiten in eigenen Themen; Karte mit Maßstabsleiste nicht gezeichnet.
- geometrie.grundbegriffe/winkel: Messen und Zeichnen durch das Kind geht nicht; eigentliche Winkelsätze (Neben-/Scheitel-/Stufenwinkel) Kl. 7.
- geometrie.ortslinien: Mittelsenkrechte und Winkelhalbierende Kl. 7; Flächen färben geht nicht.
- messen.koerper_berechnung: Netze von Quadern mit Maßen und Falten durch das Kind gehen nicht (Würfelnetze und Schrägbilder jetzt als Figur aus Linien).
- stochastik.kombinatorik: große Baumdiagramme (> 9 Pfade) nur in Worten.

App-Wunsch (kein Muss): `inhalte/README.md` sagt „Noch nicht möglich: Schrägbilder und Netze“. Beides geht als Figur aus Linien (siehe messen.koerper_berechnung, Funktionen `schraeg` und `netzbild`).

## 2026-11-14 17:15 – STATUS
messen.koerper_berechnung fertig: 14 Prüfpunkte umgesetzt, 1 abgelehnt (Volumeneinheiten dm³/Liter: Raumeinheiten sind Stoff Kl. 6, die Karte volumen bleibt Vertiefung – unter offen begründet). Schrägbilder von Quadern und Würfelnetze („Ist das ein Würfelnetz?“, alle 11 Netze und 24 Nicht-Netze werden durch Abrollen geprüft) als Figur aus Linien. 6 Lernkarten / 168 Aufgaben, Prüfskript OK.
App-Wunsch (kein Muss): In README „Noch nicht möglich: Schrägbilder und Netze“ stimmt nicht mehr ganz – beides geht als Figur aus Linien; ggf. README anpassen.
Weiter mit stochastik.kombinatorik.

## 2026-11-14 16:50 – STATUS
messen.flaechen fertig: 15 Prüfpunkte umgesetzt, 0 abgelehnt, 1 Vorschlag zurückgestellt (eigene Lernkarte „Näherungswerte mit Rechtecken“ – steht weiter unter offen). Bild in einheiten korrigiert, neue U-Form-Figur. 7 Lernkarten / 196 Aufgaben, Prüfskript OK.
Weiter mit messen.koerper_berechnung.

## 2026-11-14 16:30 – STATUS
geometrie.ortslinien fertig: 17 Prüfpunkte umgesetzt, 0 abgelehnt. Neues Lernkarten-Bild in verknuepfen (Kreis mit Parallelenpaar). 6 Lernkarten / 168 Aufgaben, Prüfskript OK.
Weiter mit messen.flaechen.

## 2026-11-14 16:10 – STATUS
geometrie.winkel fertig: 19 Prüfpunkte umgesetzt, 0 abgelehnt. Uhr (Zifferblatt mit Zeigern) und Windrose jetzt als Figur in Lernkarten und Aufgaben; der offen-Punkt „Uhr/Windrose nicht zeichenbar“ ist gestrichen. 7 Lernkarten / 196 Aufgaben, Prüfskript OK.
Weiter mit geometrie.ortslinien.

## 2026-11-14 15:45 – STATUS
geometrie.grundbegriffe fertig: 20 Prüfpunkte umgesetzt, 0 abgelehnt. 2 Lernkarten-Bilder ersetzt (Kreis mit Passante, Raute), neue Aufgaben mit Bild: Punkt im Koordinatensystem erkennen, Linienarten erkennen, Winkel schätzen, Viereck aus Koordinaten. 7 Lernkarten / 196 Aufgaben, Prüfskript OK.
Weiter mit geometrie.winkel.

## 2026-11-14 15:20 – STATUS
groessen.einheiten fertig: 18 Prüfpunkte umgesetzt, 0 abgelehnt. 2 neue Bilder (Einheitentafel als Stellentafel in laenge und kommaschreibweise). Prüfskript OK, 8 Lernkarten / 224 Aufgaben.
Weiter mit geometrie.grundbegriffe.
