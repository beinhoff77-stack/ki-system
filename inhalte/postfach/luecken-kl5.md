# Postfach luecken-kl5 (Achtzehnte Runde, Teil B, Klasse 5)

Neueste Meldung oben.

## 2026-11-17 15:00 – STATUS: messen.flaechen fertig (Lücke Nr. 10, niedrig)
Die vorhandene Karte sachaufgaben bekommt 4 Stufe-3-Übungen „Näherungswerte mit Rechtecken“ (LehrplanPLUS M5 4.2), hinten angehängt (Zufallsstart 18_5_8): See über einem Kästchengitter
(ganze Kästchen zählen, Grenzen „mehr als 20 km², weniger als 40 km²“, passender Näherungswert) und Teich zwischen innerem und äußerem Rechteck (Lücken 15 m² / 54 m²).
Kartentext unverändert. Zählung der Kästchen vom Programm (Probepunkte), Maße der Rechtecke per Skript gegen die Koordinaten geprüft (maßstäblich).
Prüfskript OK; Nachweis mit `--erweitert sachaufgaben`: alle 238 alten Aufgaben und 7 Karten unverändert, NACHWEIS OK.
Hinweis: Der Seeumriss hat an den schrägen Kanten schmale angeschnittene Kästchen (2–3 % Fläche). Deshalb wird nie die genaue Zahl der angeschnittenen Kästchen abgefragt, nur robuste Grenzen.

## 2026-11-17 14:30 – STATUS: zahlen.rechengesetze fertig
Vier neue Lernkarten (Pflicht), 112 neue Aufgaben (je Karte 4/6/8 Übungen, 1 Test, 3 Korrektur, 6 Sicherung), hinten angehängt, Zufallsstarts 18_5_4–7:
kopfrechnen (Stelle 7, nach verteilen), umkehraufgabe_mal (Stelle 10, nach geteilt_ganz), schriftlich_geteilt (Stelle 13, direkt nach der unveränderten Karte schriftlich), sach (Stelle 14, am Ende).
Neuer Abschnitt „Anwenden“ (nur sach) hinter „Große Rechnungen“ → 5 Abschnitte statt 2–4; neue Teilfähigkeiten gleichungen und anwenden, kopfrechnen hängt an gesetze, schriftlich_geteilt an verfahren.
Prüfskript OK ohne Hinweise; Nachweis: alle 310 alten Aufgaben und 10 alten Karten unverändert, NACHWEIS OK. Alle 112 Aufgaben gelesen; dabei verbessert: Auswahl „Fehler finden“ bei der Division ließ bei Ergebnissen mit Endnull zwei richtige Antworten zu (jetzt ausgeschlossen), Bus-Aufgabe höchstens zweimal, Stufe 1 der Division mit kleineren Zahlen.

## 2026-11-17 13:40 – STATUS: zahlen.ganz fertig
Drei neue Lernkarten (Pflicht), 84 neue Aufgaben (je Karte 18 Übungen 4/6/8, 1 Test, 3 Korrektur, 6 Sicherung), hinten angehängt, Zufallsstarts 18_5_1–3:
schriftlich_plus_minus (Stelle 5, vor addieren), umkehraufgabe (Stelle 8, nach subtrahieren), verstehen (Stelle 10, nach ketten).
Prüfskript OK ohne Hinweise; Nachweis `python3 -I inhalte/generatoren/_luecken_kl5_nachweis.py zahlen.ganz`: alle 272 alten Aufgaben und 8 alten Karten unverändert, NACHWEIS OK.
Neue Teilfähigkeiten: schriftlich, gleichungen, begruenden (alte unverändert). Alle 84 Aufgaben gelesen, Zahlwerte vom Programm berechnet und vom Prüfskript nachgerechnet.

## 2026-11-17 12:55 – STATUS: Bestandsaufnahme (Liste inhalte/pruefung/aufbau/klasse5.json, Feld „luecken“, Stand 14.11.)
Geprüft gegen inhalte/themen und inhalte/themenliste.json (Stand lernen-app 4a71771). Lehrplan-Wortlaut M5 1.1, 1.2, 3.1, 3.2 heute auf lehrplanplus.bayern.de nachgelesen.

| # | Lücke (Kurzform) | Dringl. | Stand heute |
|---|---|---|---|
| 1 | Natürliche Zahlen: Stellenwert, große Zahlen, Zahlenstrahl, Runden, römisch | hoch | **erledigt** (zahlen.natuerlich, 12 Lernkarten) – nicht Teil dieses Auftrags |
| 2 | Teilbarkeit, Primfaktoren, ggT/kgV | hoch | **erledigt** (zahlen.teilbarkeit, 8 Lernkarten) – nicht Teil dieses Auftrags |
| 3 | Gleichungen durch Probieren/Umkehraufgaben (a + x = b … a : x = b) | hoch | **teilweise erledigt**: gleichungen.einfach (Kl. 5, am 15.11. neu gebaut) übt alle sechs Formen in den Karten umkehr_plus und umkehr_mal – aber fast nur mit natürlichen Zahlen (2 von 66 Aufgaben mit negativen Zahlen). Der Lehrplan stellt die Gleichungen in M5 1.2/3.1 zu den ganzen Zahlen. **offen** → zahlen.ganz/umkehraufgabe und zahlen.rechengesetze/umkehraufgabe_mal, Schwerpunkt ganze Zahlen (jede Aufgabe mit mindestens einer negativen Zahl). |
| 4 | Schriftlich addieren/subtrahieren (auch > 1 Million) mit Überschlag | mittel | **offen** → zahlen.ganz/schriftlich_plus_minus vor addieren |
| 5 | Schriftliche Division mit Teilern über 10 | mittel | **offen**. Das Teilen der Karte „schriftlich“ in zwei Karten würde freigegebene Aufgaben umhängen – **nur gemeldet, nicht gemacht**. Stattdessen neue Karte zahlen.rechengesetze/schriftlich_geteilt direkt nach „schriftlich“ (vorgerechnet 7 488 : 24); „schriftlich“ bleibt unverändert. |
| 6 | Kopfrechnen, Strategien mit dem Verteilungsgesetz | mittel | **offen** → zahlen.rechengesetze/kopfrechnen nach verteilen |
| 7 | zahlen.ganz ohne Verstehen-Karte (Aussagen prüfen, Gegenbeispiel) | mittel | **offen** → zahlen.ganz/verstehen nach ketten |
| 8 | Sachaufgaben, Vorwärts-/Rückwärtsarbeiten in zahlen.rechengesetze | mittel | **offen** → zahlen.rechengesetze/sach am Ende |
| 9 | Schrägbilder und Netze von Quadern | mittel | **Übergang erledigt**: messen.koerper_berechnung/quader hat Würfelnetz-Aufgaben mit Figur. Quadernetze mit Maßen und Schrägbilder brauchen eine Körper-Zeichnung der App – **nicht Teil dieses Auftrags** (App-Wunsch, steht schon unter „offen“ in der Datei). |
| 10 | Näherungswerte krummer Flächen mit Rechtecken | niedrig | **offen** → messen.flaechen/sachaufgaben, neue Stufe-3-Übungen mit Figur über einem Gitter |
| 11 | Winkel mit dem Geodreieck messen/zeichnen | niedrig | **Übergang erledigt**: geometrie.grundbegriffe/winkelarten hat 6 Aufgaben „Schätze: Wie groß ist der Winkel α ungefähr?“ mit Figur. Hinweis in der Eltern-Ansicht ist App-Arbeit – **nicht Teil dieses Auftrags**. |

Reihenfolge der Arbeit: zahlen.ganz (Nr. 3, 4, 7), zahlen.rechengesetze (Nr. 3, 5, 6, 8), messen.flaechen (Nr. 10).
Hinweis: zahlen.rechengesetze hat danach 14 Lernkarten, zahlen.ganz 11 (README nennt 4–10). Die Lücken-Liste verlangt die Karten genau dort; ich halte mich an die Liste und melde es hier.
