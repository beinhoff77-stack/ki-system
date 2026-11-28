# Runde 15 einspielen (Paket-Anleitung, nichts ist eingespielt)

Voraussetzung: RB-S (`20261204_rb_s_regelbezug.sql`) und FT-S (`20261203_ft_s_form_takt.sql`) sind eingespielt (Stand 28.11.2026: ja). Nur auf ausdrücklichen Satz des Nutzers ausführen. Je Datei ein `execute` (der ganze Dateiinhalt in einem Aufruf, kein psql-Meta, kein eigenes BEGIN/COMMIT).

## Reihenfolge

1. `tools/tests/aus/rollend15_probe.sql`: Probelauf der 207 Aufgaben mit 585 Fehlbildern; rollt am Ende ABSICHTLICH zurück. Erwartete Meldung: beginnt mit `BERICHT Runde 15 Aufgaben-Paket: 207 Aufgaben, 585 Fehlbilder, 0 Regelzuordnungen neu …` und endet mit `PROBELAUF bestanden, ALLES zurückgerollt`.
2. `tools/tests/aus/rollend15_einspielen.sql`: spielt ein. Ergebnis: eine Zeile `bericht` (dieselbe Zeile als Meldung).
3. `tools/tests/aus/rb_nachtrag_r15_probe.sql`: Probelauf der Regel-Kennungen; rollt zurück. Erwartete Meldung: `BERICHT Runde 15 Regel-Nachtrag: 0 Aufgaben, 0 Fehlbilder, 169 Regelzuordnungen neu …`.
4. `tools/tests/aus/rb_nachtrag_r15.sql`: schreibt die 169 Regeln.

Schritt 3 und 4 erst NACH Schritt 2 (sonst Abbruch ohne Änderung: die Aufgaben fehlen).

## Erwartete Zahlen

| | Aufgaben | Fehlbilder | Regelzuordnungen |
|---|---|---|---|
| Bestand vorher (28.11.2026, nur erwartet) | 32 440 | 5 756 | 2 004 |
| nach Schritt 2 | +207 = 32 647 | +585 = 6 341 | +0 |
| nach Schritt 4 | +0 | +0 | +169 = 2 173 |

Die Bestandszahlen vorher sind nur Erwartung: Weichen sie ab, steht „WEICHT AB“ im Bericht, das Paket bricht nicht ab. Fest geprüft sind nur die Differenzen; jede Abweichung davon rollt alles zurück. Die 207 Aufgaben: 14 Einheiten, 66 Auswahl, 26 Lücken, 115 Zahl; zaehlt = ja 181, nein 26 (Lückenwege).

Wiederholung: Schritt 2 ein zweites Mal bricht ab („Reihenfolge-Nummern des Pakets sind schon belegt“) und ändert nichts; Schritt 4 ein zweites Mal ergibt 0 neue Regeln.

## Lernpause

Nicht nötig, wie bei Runde 14. Begründung:
- Alle vier Pakete schreiben nur NEUE Zeilen (INSERT in `schule.aufgabe`, `schule.aufgabe_fehlbild`, `schule.aufgabe_regel`). Keine bestehende Zeile wird geändert, keine Einheit gesperrt, kein Status gesetzt (anders als `bestand_berichtigung1`, das Aufgaben sperrt und deshalb eine Lernpause braucht).
- Es gibt keine Tabellensperre über `lock_timeout 3 s` hinaus; die Zeitgrenzen (lock 3 s, statement 120 s) stehen als erste Anweisung und gelten nur für diese Transaktion.
- Die neuen Aufgaben erscheinen sofort in den Lernkarten, zu denen sie gehören. Das Ziel einer Karte (`karte_ziel`, höchstens 4) kann steigen, wenn sie bisher weniger als 4 Übungen hatte; ein Kind mitten in einer Karte sieht dann eine weitere Aufgabe. Das ist gewollt und schadet nicht.
- Die Regel-Kennungen wirken erst beim nächsten Fehler eines Kindes an einer R15-Aufgabe.

## Nachkontrolle

1. Bericht prüfen (Differenzen +207 / +585 / +0, dann +0 / +0 / +169).
2. `select count(*) from schule.aufgabe;` (Soll 32 647), `schule.aufgabe_fehlbild` (6 341), `schule.aufgabe_regel` (2 173).
3. Je Einheit: `select einheit_id, count(*) filter (where pool = 'uebung') from schule.aufgabe where reihenfolge >= 15000 group by 1;` zusammen 207 über 14 Einheiten.
4. Stichprobe im Client: eine R15-Aufgabe falsch beantworten und prüfen, dass Regel und Fehlbild-Satz erscheinen.

## Erzeugen und Prüfen

`python3 -I tools/rollend_paket_sql.py --runde 15` schreibt die vier Dateien, `--pruefen` vergleicht sie mit dem Stand der Inhalte; `python3 -I tools/tests/regelbezug_sql_test.py` spielt sie in einem lokalen Nachbau ein (auch mit `RB_PG_ICU=de-DE` und `en-US`).
