# Postfach schwer-natuerlich (Zwölfte Runde: zahlen.natuerlich auffüllen und schwerer machen)

## 2026-11-16 06:20 – FERTIG
**Generator** `inhalte/generatoren/zahlen_natuerlich.py` → `inhalte/themen/zahlen.natuerlich.json` (thema_id 15, block_id 49, klasse {"gym_by": 5}).
`python3 -I tools/inhalt_pruefen.py inhalte/themen/zahlen.natuerlich.json` → **OK** (12 Lernkarten, 336 Aufgaben, 202 mit Rechenausdruck nachgerechnet). Zwei Läufe ergeben byte-gleiche Dateien.

- Lernziele, Reihenfolge und Titel wie inhalte/klar/quelle.md; Erklärfelder unverändert aus inhalte/klar/zahlen.natuerlich.json (über etappen_aus_klar aus _auffuellen.py, Muster zahlen_teilbarkeit.py).
- Je Lernkarte: 18 Übungen (Stufe 1: 4, Stufe 2: 6, Stufe 3: 8), 1 Test, 3 Korrektur, 6 Sicherung → 28 Aufgaben × 12 = 336.
- Alle Lösungen berechnet: Zahlwörter (eigene Funktion zw, geprüft an den Kartenbeispielen), römische Zahlen (roem/roem_wert, Hin- und Rückweg für 1–3 999 geprüft),
  Runden, Anzahlen und größte/kleinste Zahlen durch Aufzählen. Jede Aufgabe gelesen; Fehler beim Lesen korrigiert (u. a. falsche Aussage bei „XXI + X“, „1 Abschnitte“, Zahlwort „…hundertein Millionen“ ausgeschlossen).
- Beispiele der Lernkarten (4 052, zwölf Millionen achttausend, 3 040 500, 90 909/90 990, 3 472, 2 995, 39) sind als Aufgabe ausgeschlossen.
- Antworttypen: Zahl 197, Auswahl 98, Markierung am Zahlenstrahl 26, Text (römisch, höchstens 11 Zeichen) 10, Lücken 5.

### Stufe 3 je Lernkarte (8 Aufgaben, je Art 2-mal; P = Prüfungsvorbild, K = Knobel)
| Lernkarte | Aufgabenarten Stufe 3 |
|---|---|
| stellenwert | P: Zahl aus Stellenwert-Abkürzungen mit Übertrag (PU 2013 Nr. 5a) · P: größte Zahl aus Zahlenkarten (JT 2025 Nr. 3) · K: Ziffern für alle Seitenzahlen · Ziffern vertauschen |
| zahlwort_zu_ziffern | P: Milliarden/Millionen gemischt mit Ziffern (PU 2013 Nr. 5a) · P: Nullen zählen (Kurztest Stellenwerttafel) · P: Nachfolger über Gruppengrenze (JT 2024 Nr. 6) · K: Zahl aus gleichen Ziffern mit Quersumme |
| ziffern_zu_zahlwort | P: „rund 2,4 Millionen“ ohne Komma (Zeitungszahlen, BMT große Zahlen) · P: Zahlwort mit leerer Millionengruppe · P: Zahlwort zu 1 001 000 000 · K: Wie oft „vierzig“ im Zahlwort? |
| strahl_ablesen | P: großer Strahl bis Millionen (JT 2019 Nr. 6) · P: enger Ausschnitt (PU 2021 Nr. 7) · K: Anfang aus zwei Strichen rückwärts · Fehler: Anfangszahl vergessen |
| strahl_eintragen | P: Zahl im Hunderttausenderbereich markieren (JT 2024 Nr. 4) · P: Mitte zwischen zwei Zahlen (SMART Jgst. 5; JT 2018 Nr. 3) · K: gleich weit auf der anderen Seite · Abschnitte rückwärts |
| vergleichen | P: Ziffer einsetzen mit Größer-Bedingung (PU 2013 Nr. 2b) · P: ordnen eng beieinanderliegender Zahlen (PU 2013 Nr. 2a; JT 2025 Nr. 14) · K: größte Zahl mit verschiedenen Ziffern unter Grenze · K: kleinste Zahl mit Quersumme |
| runden_regel | P: welche Zahl ergibt gerundet … (JT 2020 Nr. 14) · P: Rundungsergebnis ankreuzen (JT 2024 Nr. 5) · K: größte/kleinste Zahl zu einem Rundungswert · K: wie viele Zahlen runden auf … |
| runden_uebertrag | P: Rundung mit Neunen ankreuzen (JT 2019 Nr. 19; JT 2024 Nr. 5) · P: welche Zahl ergibt auf Tausender 400 000 (JT 2020 Nr. 14) · K: Nullen nach Übertrag · Fehler „49(10)0“ |
| runden_sinnvoll | P: höchstens/mindestens hinter „rund 45 000“ (BMT 2002, Rundungstoleranz) – zweimal (höchstens, mindestens) · K: größter Unterschied zweier gleich gerundeter Zahlen · Modellieren: Aufzug mit „rund 80 kg“ |
| unendlich | P: Nachfolger über mehrere Neunen (JT 2024 Nr. 6) · P: Anzahl Zahlen zwischen zwei Zahlen (PU 2013 Nr. 2b) · Begründen: „größte Zahl“ widerlegen · K: Anzahl n-stelliger Zahlen |
| roemisch_schreiben | P: Jahreszahl an einem Tor (Kurztest Römische Zahlen) · P: richtige Schreibweise ankreuzen, typische Fehler (XD, IC, IIII) · K: meiste Zeichen bis 50/100/200/500 · K: römisch rechnen |
| roemisch_system | Aussage zum Stellenwert-/Additionssystem · Zeichen zählen (Ziffern vs. römisch) · K: Zeichen vertauschen · K: Zeichen anhängen vs. 0 anhängen |

Abweichung (ehrlich): Für **roemisch_system** habe ich keine echte Prüfungsaufgabe gefunden, die den Vergleich Stellenwertsystem ↔ römisch abfragt; die beiden nicht-Knobel-Arten folgen Grundwissenskatalogen/Kurztests, nicht einer Prüfung. Für **runden_sinnvoll** ist das Prüfungsvorbild (Rundungstoleranz) eine Aufgabe aus dem Bayerischen Mathematik-Test 2002 in der SMART-Sammlung; ich habe sie nur aus der Inhaltsbeschreibung, nicht im Wortlaut gesehen.

### Quellen (Typ und Niveau als Vorbild, nie Wortlaut oder Zahlen übernommen)
- Probeunterricht 2013 Gymnasium Bayern, Mathematik Jgst. 5, 1. Tag (Stellenwert-Abkürzungen 8 HMrd 13 ZM …, Zahlen vergleichen, Zahlen zwischen 100 und 200): https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Probeunterricht/Mathematik/2013/pu2013_5_1.pdf
- Probeunterricht 2021 Gymnasium, 1. Tag (Zahlen an markierten Stellen des Zahlenstrahls): https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Probeunterricht/Mathematik/2021/mathematik_aufgaben_erster_tag_2021.pdf
- Jahrgangsstufentest 6 Realschule Bayern 2018 (Mitte am Zahlenstrahl): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2018/2018_jt_mathe_6_loesung.pdf
- … 2019 (markierte Zahl A am Strahl bis 3 500 000; Runden 98 736 ankreuzen): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2019/2019_jt_mathe_6_loesung.pdf
- … 2020 (Zahl ankreuzen, die auf Zehntausender gerundet … ergibt): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2020/2020_jt_mathe_6_loesung.pdf
- … 2024 (318 000 am Strahl markieren; Runden auswählen 354 697; Nachfolger): https://isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2024/2024_JT_Mathe_6_Loesung.pdf
- … 2025 (größte Zahl aus Zahlenkarten 22, 220, 202, 200; Größen ordnen): https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2025/2025_JT_Mathematik_6_Loesung.pdf
- SMART-Aufgabensammlung Uni Bayreuth, Gymnasium Jgst. 5 (Zahlenstrahl eintragen, Mitte; Bayerischer Mathematik-Test 2002 Runden/Abschätzen): https://btmdx1.mat.uni-bayreuth.de/smart/buch/smart_gym_j05.pdf
- Fit in Test und Klassenarbeit Mathe 5./6. Klasse Gymnasium (Leseprobe: Kurztest Dezimalsystem/Runden, Kurztest Römische Zahlen): https://www.bange-verlag.de/product-attachments/9783804415928_Fit_in_Test_und_Klassenarbeit__Mathe_5.6.Klasse_Gymnasium__lpr_0.pdf
- Nicht gefunden: frei zugängliche Aufgaben des Gymnasium-Jahrgangsstufentests 6 und VERA-Aufgaben zu diesem Thema (VERA 3/8 passt nicht zu Kl. 5); Känguru 5/6 enthält zu Stellenwert/Runden nur vereinzelt Aufgaben, keine passende genutzt.

### Offene Punkte
- Einspielen mit einheit_abgleichen(…, 'lassen'): Die alten Aufgaben liegen nur in der Datenbank – Dubletten zu ihnen konnte ich nicht prüfen.
- Zahlwort-Schreibweise: „einhundert“, „eintausend“ (statt „hundert“, „tausend“); Gruppen ab Million mit Leerzeichen wie auf der Lernkarte.
- Römische Text-Antworten: Die App vergleicht ohne Groß-/Kleinschreibung; ein Kind, das „xliv“ tippt, wird richtig gewertet.
