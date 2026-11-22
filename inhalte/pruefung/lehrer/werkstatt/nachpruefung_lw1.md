# Prüfung LW-1 „Unser Lehrplan“ – App 0.88.0 (Zweig lernen-app, 8af4fee), 22.11.2026

Geprüft gegen die Vorgabe `lehrer/werkstatt/umsetzung.md` Abschnitte 1–8 (LW-1-Umfang: Reiter, Seite mit Matrix + Fahrplan + Detail-Schublade, Zeigen, Klassen-Mehrfachauswahl, fertige Klassen eingeklappt, Ringe, Tablet/Handy). LW-2/LW-3 und Abschnitt 12 nicht Teil dieser Prüfung. Testkind, erfundene Daten (Testsuite mit nachgebildetem Server). Bilder: `lw1/`.

**Testsuite:** 141 von 141 grün (`PW_TEST_EXECUTABLE=/usr/bin/google-chrome node --test tests/lernen.test.cjs`), darunter die sechs LW-1-Tests (Reiter und alte Adressen, Zeigen/Einstieg/Suche/Detail, Planen + Rückgängig, keine Plan-Funktion verloren, Konflikt „Neu laden“, Abnahme 400/820/1280).

## Erfüllt (nachgestellt)
- Reiter **Überblick · Was wackelt · Lehrplan**; `-stand` / `-plan` führen auf „Lehrplan“.
- Rechner: Fahrplan links (gerade dran **blau** mit Balken „Etappe 3/7“, kommt noch **hellgelb** nummeriert, unten „In Wiederholung 22 ›“, „Fertig (kann er) 16 ›“), Matrix mit klebenden Köpfen, **Detail als Schublade** von rechts.
- Farben nach Abschnitt 3: dran blau, Plan hellgelb mit Platznummer, Wiederholung hellgrün, fertig durchsichtig, eigene Schule weiß, andere Schule grau; Legende passend.
- Klassen-Kasten mit drei Ringen (groß gewählte Schule, klein die anderen), „3/15 Themen“.
- Leiste: Einordnen Gym/RS/IB, Zeigen (hebt nur hervor), Klassen 5–10 als Mehrfachauswahl mit blauem Punkt, Einstieg prüfen, Suchen, Auswählen, Rückgängig, „Alles gespeichert“.
- Detail: Stand mit Stufen-Marke und Etappen-Liste, Planen (Platz 1: „Als Nächstes“ gesperrt, „Ans Ende“, „Aus dem Plan“), Stufe, Lehrstoff, Zusammenhang; ✕ und Esc.
- Tablet: Fahrplan als Schublade über „Fahrplan · 8“; Handy: Umschalter „Fahrplan · 8 | Alle Themen“, ↑ ↓ immer sichtbar, Detail als Blatt von unten, Hinweis „Einplanen: unter ‚Alle Themen‘ ein Thema antippen“.

## Abweichungen

### Muss
– keine –

### Sollte
- **S1 – Handy: erster Bildschirm ohne Inhalt (nachgestellt, 400 × 860).** Über dem Lehrplan stehen App-Kopf, Seitenkopf „Lehrplan Kind A“, Name, „Lernen starten“/„Einstellen“/„So funktioniert’s“, Reiter und die **ganze Leiste ausgeklappt** (Einordnen, Zeigen, Klassen, Einstieg, Suchen, Auswählen, Rückgängig, Umschalter, Legende in 3 Zeilen). Die erste Themen-Karte beginnt bei **795 px** (Fahrplan-Körper 705 px) – sichtbar sind 65 px Inhalt. Vorgabe 8: „Kopf zweizeilig (Name, darunter die drei Reiter)“, Umschalter oben. **Vorschlag:** Handy-Leiste auf eine Zeile: `[Fahrplan · 8 | Alle Themen]  [Filter ▾]`; „Filter ▾“ öffnet ein Blatt mit Einordnen, Zeigen, Klassen, Einstieg, Suchen, Auswählen; Legende hinter „ⓘ“. „Lernen starten / Einstellen / So funktioniert’s“ auf dem Handy in eine Zeile mit Symbolen oder ins Menü. Ziel: erste Karte über 400 px. Bild `lw1-400-alle-themen.png`.
- **S2 – Fahrplan zählt Orte, Platznummer mehrfach (nachgestellt, 1280/820/400).** Fahrplan „8 Orte“, Einträge wie „Lineare Ungleichungen und 1 weitere · 1/2 Flüge“, „Bruchterme und 3 weitere · 0/4 Flüge“; in der Matrix tragen vier Karten **dieselbe „Platz 3“**. Vorgabe 3/4: ein Platz je Thema. Ursache: der Plan hängt heute noch an Orten (alter Reise-Aufbau) – fachlich erwartbar bis zum Reise-Aufbau. **Vorschlag bis dahin:** Platz-Marke mit Unterbuchstaben „3a, 3b, 3c, 3d“ (Reihenfolge innerhalb des Orts) und im Fahrplan-Kopf „8 Plätze · 14 Themen“ statt „8 Orte“ („Ort“ ist ein Kinderwort). Nach dem Reise-Aufbau (1 Flug = 1 Land) entfällt das.

### Kann
- **K1 – Detail: Etappen-Liste und Stand widersprechen sich (nachgestellt mit Testdaten).** Kopf „Gerade dran · 3 von 7 Etappen“, Fahrplan „Etappe 3/7“, aber die Liste zeigt **Etappe 1** als „gerade dran“ und 2–6 „offen“. Die Liste nimmt den Stand je Karte (`proEinheit().karten`), der Kopf `etappe_jetzt`/`gelandet`. In den Testdaten fehlen Karten zu den gelandeten Etappen – **Vermutung:** mit echten Daten stimmt es meist; fehlen aber Karten (gesetzte/alte Etappen), entsteht derselbe Widerspruch. Vorschlag: Etappen vor `etappe_jetzt` ohne Karte als „gelandet“ zeigen.
- **K2 – Seitenkopf „Kind A · Gymnasium · Klasse 5“, Matrix und Klassen-Standard aber Klasse 8 (nachgestellt).** Die Testdaten mischen zwei Klassen (Lernstand-Antwort `klasse: 5`, Lehrplan-Daten Klasse 8). **Vermutung:** Kopf und Klassen-Standard lesen verschiedene Quellen – bitte prüfen, dass beide dieselbe Klasse nutzen.
- **K3 – Tablet 820:** Leiste umbricht auf drei Zeilen + Legende zwei Zeilen; Matrix beginnt bei 507 px von 900. Mit S1-Lösung („Filter ▾“ ab < 1100 px) mit erledigt.

## Nicht geprüft
LW-2 (Ziehen in/aus dem Fahrplan, Warnungen 4a), LW-3 (Kinder-Umschalter, Überblick-Karten, Arbeitsliste), Abschnitt 12 (LK) und 12.7 (Teile) – folgen mit den jeweiligen Versionen. Echte Server-Antworten und echte Kinderdaten nicht.
