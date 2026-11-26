# Antworttyp „bedingung“ – Format und Grenzen (Schritt 2, Arbeitsstand)

Stand 27.11.2026. **Im Arbeitsstand fertig:** Referenz in Python (`tools/bedingung.py`), Datenbank-Fassung als Datei (`supabase/migrations/20261201_bd_s1_bedingung_rechner.sql`), gemeinsame Prüf-Fälle, Vergleichstest. **Nichts eingespielt:** nichts an Datenbank, Serverfunktion oder App geändert. Grundlage: `bauplan-fundament.md`, zwei Gegenprüfungen durch ChatGPT (Werkstatt, zu Wunsch 176), Muster des Mathe-Profis.

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

- **Felder:** 1 bis 6. Art `ganz` oder `rational`. `min`/`max` je Feld, **nur ganze Zahlen**, sonst −999 999 bis 999 999.
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
`{"werte": ["5", "−2", "−3"]}` – so viele Werte wie Felder. Erlaubt: ganze Zahl mit bis zu sechs Stellen; bei `rational` zusätzlich Dezimalzahl mit Komma (bis drei Nachkommastellen) oder Bruch `a/b` (Nenner nicht null). Leerzeichen und das typografische Minus werden angenommen. **Genau ein freiwilliges Vorzeichen:** `+3` und `-3` gelten, `+-3` nicht. Rohe Eingabe höchstens 40 Zeichen (vor dem Entfernen der Leerzeichen), danach höchstens 14. Als Wert zugelassen sind Text und JSON-Zahlen mit ganzem Wert (es zählt der Wert: 5, 5.0 und 5e0 sind dasselbe); Wahrheitswert, Liste, Objekt und Kommazahl als JSON-Zahl sind Format falsch. Punkt als Dezimaltrenner, Text, zu viele Stellen, falsche Anzahl: **Format falsch**, es wird nichts gewertet und nichts gespeichert.

## Festlegungen nach der Gegenprüfung
1. **Was das Kind erfährt.** Nach einem Fehlversuch: Name der verletzten Bedingung und Hinweis. Nach der endgültigen Antwort zusätzlich `beispiel` und die Namen aller Bedingungen. **Die Prüf-Bäume verlassen den Server nie**, auch nicht bei wiederholter Übertragung, Bonus oder Rückblick. Im laufenden Test: nur „Format in Ordnung“ oder nicht.
2. **Versionen.** Felder, Bedingungen und Beispiel einer freigegebenen Aufgabe werden nicht geändert. Eine inhaltliche Änderung ist eine neue Aufgabe mit neuer Kennung; alte Versuche bleiben so bewertet, wie sie waren.
3. **Grenzen gegen Überlast.** Höchstens 6 Felder, 8 Bedingungen, 60 Knoten je Bedingung (Prüfung und Anzeige zusammen), Tiefe 8, Exponent zwischen −6 und 6, jeder Zwischenwert höchstens 10³⁰ in Zähler und Nenner. Eingabe je Feld höchstens 14 Zeichen. Wird ein Zwischenwert zu groß, wird die Eingabe abgewiesen („Nimm kleinere Zahlen“), nicht als falsch gewertet. **Noch nicht gemessen:** Laufzeit der teuersten zulässigen Aufgabe in der Datenbank.
4. **Nicht definiert.** Division durch null und unerlaubter Exponent machen die Bedingung falsch (kein Absturz). Deshalb gehört „Term ist definiert“ als eigene Bedingung davor.
5. **Doppelte Übertragung** wird als eigene, getrennt prüfbare Änderung behandelt (nicht Teil dieses Formats).
6. **Sitzungsbezug.** Für freies Üben genügt die heutige Prüfung (Aufgabe gehört zu einer für das Kind sichtbaren Einheit). Keine allgemeine Ausgabe-Tabelle in Schritt 2.
7. **Regel und Fehlbild.** Jede Aufgabe bekommt eine stabile Regel-Kennung, jedes erkennbare Fehlermuster eine Fehlbild-Kennung. **Offen:** Die Kennungen hängen an der Regel-Liste des „Regel-Universums“, die noch in Arbeit ist. Das Feld wird vorgesehen, gefüllt wird es erst, wenn die Liste steht. Aus einer verletzten Bedingung allein folgt kein Fehlbild.

## Stand des Baus (27.11.2026)
**Zweite Gegenprüfung eingearbeitet** (Werkstatt, Nachricht nach 1004):
- Die Datenbank prüft die Aufgabe jetzt selbst: `schule.bed_gueltig(frage, loesung)` – Felder, Bedingungen, Tiefe, Knoten, Konstanten, **Typen in jedem Ast**, `zeige` muss eine Zahl liefern, das Beispiel muss bestehen. Dasselbe Urteil wie `pruefe_aufgabe(a, nur_form=True)`. Teil 2 hängt das als Constraint an die Tabelle; damit gilt es für jeden Schreibweg.
- Eine Aufgabe ohne Felder oder ohne Bedingungen wird nicht bewertet (Fehler statt „richtig“).
- Behobene Abweichungen: `min`/`max` nur ganzzahlig (kein Gleitkomma-Vergleich mehr); `und`/`oder` prüfen jeden Operanden; ein einziges Vorzeichen; JSON-Zahlen nach Wert; rohe Eingabe begrenzt; Anzeige von Dezimalzahlen ohne Gleitkomma.
- Der Einbau in `schule.antwort_bewerten` erkennt drei Zustände: alt (einbauen), fertig (nichts tun), Mischstand (Abbruch).

**Vergleich Referenz gegen Datenbank** (`tools/tests/bedingung_sql_test.py`, Funktionen nur vorübergehend in pg_temp, nichts ist in der Datenbank geblieben): 15 Aufgaben, 6 200 Antworten, 42 Urteile „zulässig oder nicht“ – **alle 16 Prüfsummen gleich.** Jede der 29 Operationen kommt vor; dazu nicht definiert und zu groß, jeweils in `pruefe` und in `zeige`; Grenzen genau am Limit (Tiefe 8, 60 Knoten) und knapp darüber; beide Enden eines Feldbereichs.

**Laufzeit:** teuerste zulässige Aufgabe (6 Felder, 8 Bedingungen mit je 60 Knoten, alle durchlaufen, Hinweis am Ende): **9 ms je Bewertung** (Mittel aus 200 Läufen, eine Messung).

**Noch nicht geprüft – geht nur mit der echten Migration, also erst beim Einspielen oder in einer Kopie der Datenbank:**
- die vollständige Migration zweimal hintereinander; Abbruch bei Mischstand;
- der Zweig in `schule.antwort_bewerten` mit einem gebauten Aufgaben-Datensatz; unveränderte Ergebnisse der fünf alten Antworttypen;
- die Rechte der App-Rollen; der weiter geschlossene Constraint.
Im kurzen Lauf weggelassen (gleiche Operationen wie andere): vier Muster-Aufgaben und 19 der 20 neuen Aufgaben des Mathe-Profis; der Lauf „alles“ ist vorbereitet, aber zu groß für einen Aufruf über das Werkzeug.
Eine Zahl in Exponentialschreibweise als JSON-Zahl lässt sich in der Datenbank nicht von der ausgeschriebenen unterscheiden; deshalb zählt auf beiden Seiten der Wert.

**Offen aus dem Gegenlesen des Mathe-Profis:** In der Muster-Aufgabe 6-K8-1 verraten die Namen der Bedingungen den Lösungsgedanken; Namen werden nach dem ersten Fehlversuch gezeigt. Regel für Autoren: Der Name nennt die Forderung aus dem Aufgabentext, nicht den Weg.

## Was als Nächstes kommt
- **Teil 2 der Migration (BD-S2):** Constraint öffnen; `hinweis` und `verletzt` beim ersten Fehlversuch durchreichen; überall, wo `loesung` den Server verlässt, beim Typ `bedingung` nur `beispiel` und die Namen der Bedingungen senden. Betroffen (in der Datenbank gelesen): `uebung_pruefen_intern`, `test_abschliessen_intern`, `aufgabe_anzeige`, `api.schule_lernstand`, `api.schule_inhalt_lesen`, `expeditionen_kind`, `expeditionen_alle`, `einheit_abgleichen`. Feld für Regel-Kennung und Fehlbild. **Nicht eingespielt ohne ausdrücklichen Satz des Nutzers.**
- App: Eingabe mit mehreren Zahlenfeldern, Hinweis, „Zum Beispiel“. Tests.
- Spätere Feldarten `wahl` und `menge`.

## Nicht geprüft
- Siehe „Stand des Baus“: alles, was nur mit der echten Migration geht.
- Bedienung am Handy mit fünf oder sechs Feldern (Vorgabe des Designers liegt vor, gebaut ist nichts).
- Kein Kind hat eine Aufgabe dieses Typs gerechnet.
