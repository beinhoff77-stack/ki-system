# Postfach luecken-kl5 (Achtzehnte Runde, Teil B, Klasse 5)

Neueste Meldung oben.

## 2026-11-17 15:20 – FERTIG: Abschlussbericht luecken-kl5
Zweig luecken-kl5 (von lernen-app 4a71771), drei Commits, je Thema einer. Nur Dateien unter inhalte/; keine Datenbank, kein App-Code, keine Tests, kein Merge.
Einspielen laut Auftrag mit einheit_abgleichen(…, 'sperren'); neue Etappen sind sofort sichtbar.

### Neue Lernkarten (alle Pflicht, je 18 Übungen 4/6/8, 1 Test, 3 Korrektur, 6 Sicherung; je mind. 2 nach Prüfungsvorbild + 1 Knobelaufgabe)
| Thema | Lernkarte (Stelle) | Lehrplan-Bezug (lehrplanplus.bayern.de, Gym. M5, heute nachgelesen) | Prüfungsvorbild / Knobel |
|---|---|---|---|
| zahlen.ganz | schriftlich_plus_minus (5/11, vor addieren) | M5 1.2: schriftliches Addieren/Subtrahieren auch über einer Million, Kontrolle per Überschlag; Abziehverfahren mit Entbündeln (ISB-Hinweis „Vorwissen Grundschule – Strichrechenarten“) | Fehler beschreiben (JT 6 RS 2025), Lücke ergänzen (JT 6 RS 2019 Nr. 7, Probeunterricht Gym 2014 Nr. 6); Knobel Ziffernkarten (Känguru-Art) |
| zahlen.ganz | umkehraufgabe (8/11, nach subtrahieren) | M5 1.2: a + x = b, x − a = b, a − x = b durch Probieren oder Umkehraufgabe – hier mit ganzen Zahlen | Gleichung mit großen Zahlen (Probeunterricht Gym 2014 Nr. 6), Klammer-Lücke (JT 6 RS 2019 Nr. 7); Knobel x + x = x − 5 |
| zahlen.ganz | verstehen (10/11, nach ketten) | M5 1.1: Aussagen prüfen, mit Gegenbeispielen widerlegen (Beispiel des Lehrplans: „größerer Betrag = größere Zahl“) | Gegenbeispiel finden, richtige Rechnung mit falscher Begründung (JT 6 RS, „begründe/beschreibe den Fehler“); Knobel „wie viele Aussagen stimmen immer?“ |
| zahlen.rechengesetze | kopfrechnen (7/14, nach verteilen) | M5 3.1: Produkte/Quotienten ganzer Zahlen bei geeigneten Zahlen im Kopf; Strategien über Verteilungs-/Vertauschungsgesetz | Klammer-Term (JT 6 RS 2025 Nr. 1a), Rechenvorteil (ISB Illustrierende Aufgaben M6 1.3, Aufgabe 1); Knobel „Trick 15 · 15“ übertragen |
| zahlen.rechengesetze | umkehraufgabe_mal (10/14, nach geteilt_ganz) | M5 3.1: a · x = b, x : a = b, a : x = b durch Probieren oder Umkehraufgabe | Lücke in Division (JT 6 RS 2024 Nr. 7), Klammer-Lücke (JT 6 RS 2019 Nr. 7); Knobel x · (−3) = x + 8 |
| zahlen.rechengesetze | schriftlich_geteilt (13/14, nach schriftlich) | M5 3.1: schriftlich dividieren auch mit mehrstelligen Teilern über zehn, Überschlag | Division mit zweistelligem Teiler (JT 6 RS 2016 Nr. 2, 2021 Nr. 1a, 2025 Nr. 1b), erst teilen dann vervielfachen (JT 6 RS 2020 Nr. 13); Knobel größte vierstellige Zahl durch 37 |
| zahlen.rechengesetze | sach (14/14, am Ende) | M5 3.2: Vorwärts- und Rückwärtsarbeiten, Sachaufgaben mit allen Grundrechenarten, Kontrolle im Sachzusammenhang | Rückwärtsarbeiten „Hälfte und noch 6“ (JT 8 RS 2005 in SMART Gym 6), Term zum Text (JT 6 RS 2016), fehlende Angabe (JT 6 RS 2019 Nr. 14); Knobel Zahlenrätsel mit (−2) |

Alle Prüfungsaufgaben nur als Vorbild für Typ und Niveau; Wortlaut, Einkleidung und Zahlen sind eigene.

### Erweiterte Karten
- messen.flaechen / sachaufgaben: 4 Stufe-3-Übungen „Näherungswerte mit Rechtecken“ (M5 4.2; See über Kästchengitter, Teich zwischen zwei Rechtecken). Kartentext unverändert.

### Nachweis und Prüfung
- `python3 -I tools/inhalt_pruefen.py` OK für alle drei Dateien, ohne Hinweise.
- `python3 -I inhalte/generatoren/_luecken_kl5_nachweis.py zahlen.ganz zahlen.rechengesetze` und `… messen.flaechen --erweitert sachaufgaben`: alle alten Aufgaben an gleicher Stelle unverändert, alle alten Karten unverändert, in abschnitte/teilfaehigkeiten/bewertung nur Neues ergänzt – NACHWEIS OK.
- Neue Karten zusätzlich streng nach „Vorgabe seit 16.11.“ geprüft (pruefe_karte aus _umbau_kl5.py: Längen, Wörter, Schritte, Bilder im Wertebereich).
- Alle 200 neuen Aufgaben gelesen; Zahlwerte vom Programm berechnet und vom Prüfskript über „c“ nachgerechnet; bei Auswahl-Aufgaben die richtige Antwort per Programm bestimmt (genau eine) und von Hand nachgesehen.

### Offen geblieben / zur Entscheidung
1. Karte „schriftlich“ in zwei Karten teilen (Liste Nr. 5): nicht gemacht, weil freigegebene Aufgaben umgehängt würden. Ersatz: neue Karte schriftlich_geteilt direkt dahinter.
2. Überschneidung mit gleichungen.einfach (umkehr_plus, umkehr_mal): dort dieselben Gleichungsformen mit natürlichen Zahlen, die neuen Karten üben sie mit ganzen Zahlen. Vorschlag: beide behalten; falls doppelt empfunden, die neuen Karten als Vertiefung führen.
3. Kartenzahl über der README-Spanne: zahlen.ganz 11, zahlen.rechengesetze 14 Lernkarten; rechengesetze hat 5 Abschnitte (neu „Anwenden“ mit sach). So von der Lücken-Liste vorgegeben.
4. Neue Teilfähigkeiten-Schlüssel: zahlen.ganz schriftlich, gleichungen, begruenden; zahlen.rechengesetze gleichungen, anwenden. Bitte beim Einspielen prüfen, ob der Import neue Schlüssel anlegt.
5. Liste Nr. 9 (Quadernetze mit Maßen, Schrägbilder) und Nr. 11 (Hinweis „Winkel messen im Heft“ in der Eltern-Ansicht): App-Arbeit, nicht Teil dieses Auftrags.
6. zahlen.ganz / verstehen benutzt a und b als Namen für Zahlen („Paar a = −6 und b = 2“). Erklärt wird das nur über die Aufgaben selbst; wenn das für Klasse 5 zu früh ist, bitte melden.

### Quellen
- LehrplanPLUS Gymnasium Mathematik 5: https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/5/mathematik
- ISB/SMART, Vorwissen Grundschule – Strichrechenarten (Abziehverfahren): https://btmdx1.mat.uni-bayreuth.de/smart/isb/j05/M%205.1.2%20Vorwissen%20Grundschule%20-%20Strichrechenarten.pdf
- Jahrgangsstufentest Mathematik 6 Realschule Bayern: 2016 https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2016/2016_07_07_jgst_2016_klasse_6_loesung.pdf ,
  2019 https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2019/2019_jt_mathe_6_loesung.pdf ,
  2020 https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2020/2020_jt_mathe_6_loesung.pdf ,
  2021 https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2021/2021_jt_mathe_6_loesung.pdf ,
  2024 https://isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2024/2024_JT_Mathe_6_Angabe.pdf ,
  2025 https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/2025_JT_Mathematik_6_Loesung.pdf
- Probeunterricht Gymnasium Bayern 2014, Mathematik Tag 1: https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Probeunterricht/Mathematik/2014/probeunterricht_2014_mathematik_jahrgangsstufe_5_tag_1.pdf
- SMART Aufgabensammlung Gymnasium Jgst. 6 (u. a. JT 8 RS 2005, Rückwärtsarbeiten): https://btmdx1.mat.uni-bayreuth.de/smart/buch/smart_gym_j06.pdf
- ISB Illustrierende Aufgaben M6 1.3 (Kopfrechnen, Rechenvorteile): https://www.lehrplanplus.bayern.de/sixcms/media.php/71/LPP-GY-M_613-A_GrundlegendeKFF_vorbereitend.pdf
- Känguru der Mathematik 2023, Kl. 5/6 (Art der Knobelaufgaben): https://www.mo-ni.de/fileadmin/user_upload/kaenguru2023_56.pdf

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
