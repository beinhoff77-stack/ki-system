# Antworttyp „bedingung“ – Format und Grenzen (Schritt 2, Arbeitsstand)

Stand 26.11.2026. **Gebaut ist bisher nur die Referenz in Python** (`tools/bedingung.py`) mit gemeinsamen Prüf-Fällen (`tools/tests/bedingung_faelle.json`, Lauf „OK – 11 Aufgaben, 102 Prüfungen“). Nichts an Datenbank, Serverfunktion oder App geändert. Grundlage: `bauplan-fundament.md`, Gegenprüfung ChatGPT (Werkstatt, zu Wunsch 176), Muster des Mathe-Profis.

## Wozu
Aufgaben mit vielen richtigen Antworten: „Nenne drei verschiedene ganze Zahlen mit der Summe 0, genau eine positiv.“ Richtig ist jede Antwort, die alle Bedingungen erfüllt. Die Rückmeldung nennt die erste verletzte Bedingung mit der Zahl des Kindes („Deine Summe ist 1.“). Trägt die Aufgabentypen 6, 7, 8 und, mit späteren Feldarten, 9, 12, 13, 15, 16.

## Aufgabe

```json
{"y": "bedingung",
 "f": {"text": "…", "felder": [{"art": "ganz"}, {"art": "ganz", "min": -100, "max": 100}]},
 "o": {"bedingungen": [
        {"name": "Summe ist 0", "pruefe": ["=", ["summe", "$alle"], 0],
         "zeige": ["summe", "$alle"], "hinweis": "Deine Summe ist {}."}],
       "beispiel": [5, -2, -3],
       "gut": [[1, 0, -1]],
       "gegenbeispiele": [{"werte": [4, -1, -2], "verletzt": "Summe ist 0"}]}}
```

- **Felder:** 1 bis 6. Art `ganz` oder `rational`. `min`/`max` je Feld, sonst −999 999 bis 999 999.
- **Bedingungen:** 1 bis 8, jede mit eigenem `name`. Geprüft wird der Reihe nach; die erste verletzte bestimmt die Rückmeldung. `hinweis` ist frei; steht `{}` darin, muss `zeige` angeben, welche Zahl eingesetzt wird.
- **`beispiel`** (Pflicht): eine richtige Antwort. Sie ist das Einzige aus der Lösung, das das Kind am Ende sieht („Zum Beispiel: …“).
- **`gut`** (freiwillig): weitere richtige Antworten als Probe.
- **`gegenbeispiele`** (Pflicht): zu jeder Bedingung mindestens eine falsche Antwort, die genau an ihr scheitert.

## Die Rechensprache
Ein Baum aus Listen `["name", argument, …]`. Blätter: ganze Zahlen, Zahlen als Text (`"2,5"`, `"3/4"`), `$1` bis `$6` (Feldwert), `$alle` (Liste aller Feldwerte). Sonst ist nichts erlaubt; es gibt kein freies Programm und kein SQL.

| Gruppe | Namen |
|---|---|
| Rechnen | `+` `-` `*` `/` `hoch` `neg` `betrag` |
| Listen | `liste` `summe` `produkt` `min` `max` `median` `mittelwert` `anzahl` `anzahl_positiv` `anzahl_negativ` |
| Prüfen | `=` `!=` `<` `<=` `>` `>=` `verschieden` `ganzzahlig` `teilbar` |
| Verknüpfen | `und` `oder` `nicht` |

Gerechnet wird exakt mit Brüchen. `pruefe` muss wahr oder falsch liefern.

## Eingabe des Kindes
`{"werte": ["5", "−2", "−3"]}` – so viele Werte wie Felder. Erlaubt: ganze Zahl mit bis zu sechs Stellen; bei `rational` zusätzlich Dezimalzahl mit Komma (bis drei Nachkommastellen) oder Bruch `a/b` (Nenner nicht null). Leerzeichen, Plus und das typografische Minus werden angenommen. Punkt als Dezimaltrenner, Text, zu viele Stellen, falsche Anzahl: **Format falsch**, es wird nichts gewertet und nichts gespeichert.

## Festlegungen nach der Gegenprüfung
1. **Was das Kind erfährt.** Nach einem Fehlversuch: Name der verletzten Bedingung und Hinweis. Nach der endgültigen Antwort zusätzlich `beispiel` und die Namen aller Bedingungen. **Die Prüf-Bäume verlassen den Server nie**, auch nicht bei wiederholter Übertragung, Bonus oder Rückblick. Im laufenden Test: nur „Format in Ordnung“ oder nicht.
2. **Versionen.** Felder, Bedingungen und Beispiel einer freigegebenen Aufgabe werden nicht geändert. Eine inhaltliche Änderung ist eine neue Aufgabe mit neuer Kennung; alte Versuche bleiben so bewertet, wie sie waren.
3. **Grenzen gegen Überlast.** Höchstens 6 Felder, 8 Bedingungen, 60 Knoten je Bedingung (Prüfung und Anzeige zusammen), Tiefe 8, Exponent zwischen −6 und 6, jeder Zwischenwert höchstens 10³⁰ in Zähler und Nenner. Eingabe je Feld höchstens 14 Zeichen. Wird ein Zwischenwert zu groß, wird die Eingabe abgewiesen („Nimm kleinere Zahlen“), nicht als falsch gewertet. **Noch nicht gemessen:** Laufzeit der teuersten zulässigen Aufgabe in der Datenbank.
4. **Nicht definiert.** Division durch null und unerlaubter Exponent machen die Bedingung falsch (kein Absturz). Deshalb gehört „Term ist definiert“ als eigene Bedingung davor.
5. **Doppelte Übertragung** wird als eigene, getrennt prüfbare Änderung behandelt (nicht Teil dieses Formats).
6. **Sitzungsbezug.** Für freies Üben genügt die heutige Prüfung (Aufgabe gehört zu einer für das Kind sichtbaren Einheit). Keine allgemeine Ausgabe-Tabelle in Schritt 2.
7. **Regel und Fehlbild.** Jede Aufgabe bekommt eine stabile Regel-Kennung, jedes erkennbare Fehlermuster eine Fehlbild-Kennung. **Offen:** Die Kennungen hängen an der Regel-Liste des „Regel-Universums“, die noch in Arbeit ist. Das Feld wird vorgesehen, gefüllt wird es erst, wenn die Liste steht. Aus einer verletzten Bedingung allein folgt kein Fehlbild.

## Stand des Baus (26.11.2026, abends)
- **Fertig im Arbeitsstand:** Python-Referenz; Anbindung an `tools/inhalt_pruefen.py` (Typ `bedingung` wird beim Prüfen der Inhalte mitgeprüft); Datenbank-Fassung als Datei `supabase/migrations/20261201_bd_s1_bedingung_rechner.sql` (Rechner, Bewertung, Zweig in `schule.antwort_bewerten`). **Nicht eingespielt.**
- **Vergleich Referenz gegen Datenbank:** `tools/tests/bedingung_sql_test.py`. Die Funktionen wurden dafür nur vorübergehend (pg_temp) angelegt, nichts ist in der Datenbank geblieben. 11 Aufgaben, 6 746 Antworten (alle Prüf-Fälle, dazu je Aufgabe 600 Antworten aus einem festen Vorrat einschließlich unsinniger Eingaben): **alle elf Prüfsummen gleich.**
- **Vom Vergleich nicht erfasst:** `und`, `oder`, `nicht`, `teilbar`, `ganzzahlig`, `betrag`, `neg`, `liste`, `anzahl`, `anzahl_negativ`, negativer Exponent – sie kommen in den elf Muster-Aufgaben nicht vor. Die Laufzeit einer einzelnen teuren Aufgabe ist nicht gemessen. Eine Zahl in Exponentialschreibweise als JSON-Zahl (nicht als Text) liest die Datenbank als ganze Zahl, die Referenz lehnt sie ab; die App sendet Text.
- **Teil 1 ist ohne Wirkung, solange keine Aufgabe des Typs existiert.** Der Constraint wird erst in Teil 2 geöffnet.

## Was als Nächstes kommt
- Prüf-Fälle für die oben genannten, noch nicht verglichenen Operationen ergänzen.
- **Teil 2 der Migration (BD-S2):** Constraint öffnen; `hinweis` und `verletzt` beim ersten Fehlversuch durchreichen; überall, wo `loesung` den Server verlässt, beim Typ `bedingung` nur `beispiel` und die Namen der Bedingungen senden. Betroffen (in der Datenbank gelesen): `uebung_pruefen_intern`, `test_abschliessen_intern`, `aufgabe_anzeige`, `api.schule_lernstand`, `api.schule_inhalt_lesen`, `expeditionen_kind`, `expeditionen_alle`, `einheit_abgleichen`. Feld für Regel-Kennung und Fehlbild. **Nicht eingespielt ohne ausdrücklichen Satz des Nutzers.**
- App: Eingabe mit mehreren Zahlenfeldern, Hinweis, „Zum Beispiel“. Tests.
- Spätere Feldarten `wahl` und `menge`.

## Nicht geprüft
- Kein Lauf in der Datenbank; die plpgsql-Fassung gibt es noch nicht.
- Bedienung am Handy mit fünf oder sechs Feldern.
- Die Hinweistexte in den Prüf-Fällen stammen vom Projektleiter, nicht vom Mathe-Profi.
