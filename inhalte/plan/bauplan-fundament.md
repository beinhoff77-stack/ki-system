# Bauplan-Entwurf: Fundament „Bedingungs-Prüfung" (26.11.2026)

Vorbereitet von einem Helfer des Projektleiters, nur durch Lesen des Codes (Stand `lernen-app` 817e917). **Kein Bau, keine Einspielung.** Noch nicht von ChatGPT und Mathe-Profi gegengeprüft. **[G]** im Code gelesen · **[A]** Annahme oder Vorschlag.

## Befunde

- **[G]** Geprüft wird heute vollständig in der Datenbank (`schule.antwort_bewerten`, plpgsql). Die Edge Function `lernen-api` reicht nur durch; der Client prüft nicht und bekommt die Lösung erst mit der Antwort.
- **[G]** Fünf Antworttypen: `zahl`, `auswahl`, `luecken`, `markierung`, `text`. `punkte` ist nicht gebaut. Mehrfach-Auswahl gibt es nicht (`markierung` und `auswahl` nehmen genau einen Index).
- **[G]** Doppelte Übertragung zählt schon heute nur einmal (`client_id`). Einen Sitzungsbezug gibt es beim Üben nicht, nur bei Test, Mischkarte und Wiederholungs-Runde.
- **[G]** Die App zeichnet elf Bildarten als SVG aus Daten (unter anderem Koordinatensystem, Säulen, Kreisdiagramm, Boxplot). Säulen können eine abgeschnittene Achse. Der Diagramm-Lügendetektor (Typ 20) braucht für Säulen keinen Bau.
- **[G]** Die Wiederholung zu Sitzungsbeginn („Check-in") gibt es schon: Runde je Lerntag am Server, 6 bis 12 Karten, Takt 1/3/7/14/30 Lerntage. Sie zeigt heute Etappe und Stadt über der Aufgabe.
- **[G]** Risiko: Die Server-Funktionen stehen im Repo nur als Text-Ersetzungen am Live-Stand. Vor dem Bau müssen die Live-Definitionen gelesen werden.

## Vorschlag [A]

**Ein neuer Antworttyp `bedingung`** (mehrere Felder, Bedingungen als Daten, Prüfung in der Datenbank) trägt alle drei Bausteine, die der Mathe-Profi verlangt:

| Baustein | Lösung | trägt Typen |
|---|---|---|
| Term-Rechner | feste Operationsliste in plpgsql, exakte Brüche, kein dynamisches SQL | 6, 7, 8 |
| Zwei Antworten in einer Karte | Feldart `wahl` im selben Typ; eine Karte, ein Versuch, richtig nur wenn alles stimmt | 12, 13, 15 |
| Mehrfach-Auswahl | Feldart `menge` (Kästchen, Obergrenze, Rückmeldung „passt auch auf …") | 9, 16 |

Warum plpgsql und nicht die Edge Function: Bewerten, Speichern und Buchen laufen in einer Transaktion; `antwort_bewerten` wird auch nachträglich auf gespeicherte Antworten angewandt.

**Typ 21 „gemischte Fünf"** ist kein neuer Ablauf, sondern eine Einstellung des vorhandenen Check-ins: Herkunft erst nach der Antwort zeigen. Sonst gäbe es zwei Wiederholungen hintereinander.

## Schritte

1. Live-Stand lesen (nur lesen): `antwort_bewerten`, `uebung_pruefen_intern`, `api.schule_uebung_pruefen`, Test-Antwort-Funktion, `aufgabe_antworttyp_check`, Spalten von `schule.versuch`.
2. Format festschreiben (`inhalte/README.md`): Felder mit Art, Bereich, Stellen; Bedingungen mit Name, Prüfung, Hinweis; Beispiel; Grenzen (höchstens 6 Felder, 6 + 3 Stellen, Baumtiefe, Exponent). Gegenprüfung.
3. Prüf-Fälle als Datei: die Musteraufgaben der Typen 6, 7, 8 des Mathe-Profis mit guten und schlechten Antworten.
4. Python-Referenz in `tools/inhalt_pruefen.py`, läuft gegen Schritt 3.
5. Migration Server (eine Datei, eine Transaktion, kein DROP): Bruch-Hilfen, Term-Rechner, Bedingungs-Prüfung, Zweig in `antwort_bewerten`, Constraint, Hinweis auch bei „falsch" durchreichen, optional `versuch.bewertung`.
6. SQL-Rauchtest mit Rollback, nur Testkind.
7. Edge Function: nur Versionsnummer.
8. Client: Eingabe mit mehreren Zahlenfeldern, Hinweis mit Zahl beim ersten Fehler, „Zum Beispiel: …" statt „Richtig ist: …", alle Rückblick-Stellen.
9. Client-Tests.
10. Probe-Inhalt: 8 bis 12 Aufgaben nur für das Testkind, Bedienung am Handy mit 3 und 5 Feldern prüfen.
11. Zusatz Feldart `wahl`.
12. Zusatz Feldart `menge`.
13. Später, eigener Bau: Ausgabe-Tabelle für alle Karten (Grundlage für „Zusatzbedingung beim Wiedersehen"); Typ 3 auf demselben Rechner.

Schritte 3 und 4 gehen ohne Datenbank und ohne App. **Aufwand [A]:** 1–10 mittel, 11 klein, 12 klein bis mittel, 13 groß.

## Offene Fragen

- An ChatGPT: Genügt beim Üben „Aufgabe gehört zu einer für das Kind sichtbaren Einheit", oder braucht es eine Ausgabe-Tabelle für alle Karten?
- Zweiter Versuch bei `wahl` mit nur zwei Möglichkeiten: Der Hinweis nach dem ersten Fehler verrät das Urteil.
- Bedienung am Handy mit fünf oder sechs Zahlenfeldern ist nicht erprobt.
- Reihenfolge `punkte` (frühere Entscheidung des Nutzers: Bau 1) gegen diesen Plan: Entscheidung des Nutzers offen.
- Nicht geprüft: Live-Stand der Datenbank, Lauf der Python-Skripte, `tools/inhalt_sql.py` im Detail.

## Live-Stand gelesen (26.11.2026, Projektleiter, nur lesend)

Schritt 1 ist erledigt. Gelesen: `schule.antwort_bewerten`, `schule.uebung_pruefen_intern`, `schule.test_antwort_intern`, die Constraints von `schule.aufgabe` und `schule.versuch`, alle Aufrufer von `antwort_bewerten`. **[G]** = in der Datenbank gelesen.

- **[G]** `antwort_bewerten(schule.aufgabe, jsonb)` ist `IMMUTABLE`, `search_path ''`, kennt genau fünf Typen und liefert `{format_ok, richtig, grund?, hinweis?}`. Der neue Zweig muss ebenfalls rein rechnen (kein Tabellenzugriff), sonst passt `IMMUTABLE` nicht mehr.
- **[G]** Vier Aufrufer: `uebung_pruefen_intern`, `test_antwort_intern`, `fehler_gruende`, `api.schule_lernstand`. Die zwei letzten rechnen gespeicherte Antworten nach. Der neue Typ muss dort ohne Sonderfall durchlaufen; eine Spalte `versuch.bewertung` ist deshalb nicht zwingend, spart aber Rechnen und hält die Rückmeldung fest.
- **[G]** `uebung_pruefen_intern`: Beim ersten falschen Anlauf geht nur `nochmal` und `grund` zurück, kein `hinweis`. Für „Deine Summe ist −6“ muss `hinweis` (und der Name der verletzten Bedingung) dort und im Zweig „wiederholt“ durchgereicht werden. Am Ende geht `a.loesung` an den Client – beim neuen Typ wären das die Bedingungen samt Beispiel. Vorschlag: nach der endgültigen Antwort nur `beispiel` und die Namen der Bedingungen senden, nicht die Prüf-Bäume.
- **[G]** Doppelte Übertragung: erst `select`, dann `insert`, ohne Sperre; `UNIQUE (lernender_id, client_id)` verhindert Doppelzählung, zwei gleichzeitige Anfragen enden aber mit einem Fehler statt mit `wiederholt`. Kein neuer Mangel, bei der Gelegenheit mit `on conflict` behebbar.
- **[G]** `test_antwort_intern` nutzt `antwort_bewerten` und speichert je Testsitzung und Aufgabe eine Antwort. Der neue Typ läuft im Test ohne Hinweis mit, braucht dort aber die Format-Prüfung.
- **[G]** `aufgabe_antworttyp_check` erlaubt `auswahl, zahl, text, markierung, luecken` – muss um `bedingung` erweitert werden.
- **[G]** `aufgabe_typ_check` kennt schon die Aufgaben-Arten `umkehr`, `rueckwaerts`, `fehler`, `begruenden`, `darstellung`, `verknuepfen`, `transfer`. Die neuen Aufgabentypen der Auswahl lassen sich darauf abbilden; die Regel „verschiedene Typen für sitzt“ (`karte_typen_noetig`) greift dann von selbst.
- **[G]** Ein Feld für Grundregel und Fehlbild je Aufgabe gibt es nicht (weder in `aufgabe` noch in `versuch`). Für „Hier hat die Minusklammer geklemmt“ und die Regel-Übersicht ist das ein eigener kleiner Bau: Vorschlag `aufgabe.regel` (Nummer) und in der Lösung je falscher Antwort ein Fehlbild mit Regel; `antwort_bewerten` gibt es als `fehlbild` zurück. Das gehört zu Schritt 2, nicht später.

**Nicht gelesen:** `uebung_pruefen_wd`, `fehler_gruende`, `api.schule_lernstand` im Wortlaut; Trigger auf `versuch`; `misch_gueltig`.
