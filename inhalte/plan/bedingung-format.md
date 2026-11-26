# Antworttyp „bedingung“ – Format und Grenzen (Schritt 2, Arbeitsstand)

Stand 27.11.2026. **Im Arbeitsstand fertig:** Referenz in Python (`tools/bedingung.py`), Datenbank-Fassung als Datei (`supabase/migrations/20261201_bd_s1_bedingung_rechner.sql`), gemeinsame Prüf-Fälle, Vergleichstest. **Nichts eingespielt:** nichts an Datenbank, Serverfunktion oder App geändert. Grundlage: `bauplan-fundament.md`, zwei Gegenprüfungen durch ChatGPT (Werkstatt, zu Wunsch 176), Muster des Mathe-Profis.

## Wozu
Aufgaben mit vielen richtigen Antworten: „Nenne drei verschiedene ganze Zahlen mit der Summe 0, genau eine positiv.“ Richtig ist jede Antwort, die alle Bedingungen erfüllt. Die Rückmeldung nennt die erste verletzte Bedingung mit der Zahl des Kindes („Deine Summe ist 1.“). Trägt die Aufgabentypen 6, 7, 8 und, mit späteren Feldarten, 9, 12, 13, 15, 16.

## Aufgabe

```json
{"y": "bedingung",
 "f": {"text": "…", "felder": [{"art": "ganz"}, {"art": "ganz"}, {"art": "ganz", "min": -100, "max": 100}]},
 "o": {"bedingungen": [
        {"name": "Summe ist 0", "pruefe": ["=", ["summe", "$alle"], 0],
         "zeige": ["summe", "$alle"], "hinweis": "Deine Summe ist {}."}],
       "beispiel": [5, -2, -3],
       "gut": [[1, 0, -1]],
       "gegenbeispiele": [{"werte": [4, -1, -2], "verletzt": "Summe ist 0"}]}}
```

- **Felder:** 1 bis 6. Art `ganz` oder `rational`. `min`/`max` je Feld, **nur ganze Zahlen**, sonst −999 999 bis 999 999.
- **Bedingungen:** 1 bis 8, jede mit eigenem `name` (nichtleerer Text); `hinweis`, wenn vorhanden, ist Text. Geprüft wird der Reihe nach; die erste verletzte bestimmt die Rückmeldung. `hinweis` ist frei; steht `{}` darin, muss `zeige` angeben, welche Zahl eingesetzt wird.
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
3. **Grenzen gegen Überlast.** Höchstens 6 Felder, 8 Bedingungen, 60 Knoten je Bedingung (Prüfung und Anzeige zusammen), Tiefe 8, Exponent zwischen −6 und 6, jeder Zwischenwert höchstens 10³⁰ in Zähler und Nenner. Eingabe je Feld höchstens 14 Zeichen. Wird ein Zwischenwert zu groß, wird die Eingabe abgewiesen („Nimm kleinere Zahlen“), nicht als falsch gewertet. Gemessen: 9 ms je Bewertung im Fall mit den meisten Knoten (480 Knoten, Mittel aus 200 Bewertungen). Das ist nicht zwingend der teuerste Fall überhaupt; große Brüche, Potenzen und Ausnahmewege werden beim Einspielen zusätzlich gemessen.
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

**Dritte Gegenprüfung (Werkstatt, Nachricht 1007): bedingte Freigabe für Teil 1.** Bedingung: Einspielen in einer Sitzung und einer Transaktion, die sich selbst prüft; bei jeder Abweichung Rollback. Dafür gibt es `tools/tests/bedingung_einspielen.py`. Das Paket hält den Vorher-Stand fest, führt die Migration zweimal aus und prüft: zweiter Lauf ändert nichts; drei Mischstände werden abgewiesen, die Gegenprobe gelingt; der Zweig in `schule.antwort_bewerten` liefert für alle Prüf-Fälle dieselben Prüfsummen wie die Referenz; die fünf alten Antworttypen liefern für bis zu 500 echte gespeicherte Antworten je Typ und für gebaute Fehl-Eingaben dasselbe wie vorher; Rechte; Constraint unverändert und zu; Laufzeit in zwei Fällen. Nachgemessen (harmlos): Mehrere Befehle in einem Aufruf des Werkzeugs laufen als eine Transaktion.

**Seine vier Restpunkte, eingearbeitet am 27.11. (nach seiner Prüfung, von ihm noch nicht gesehen):** Längengrenze greift vor dem Putzen (41 Leerzeichen sind „Format falsch“, 40 sind „leer“); `name` muss nichtleerer Text sein, `hinweis` Text; die Referenz kann JSON exakt lesen (`lade_json`, Kommazahlen als Decimal), damit 1,00000000000000001 nicht still zu 1 wird; Dokument berichtigt, zweite Zeitmessung mit großen Brüchen im Paket.

**Vierte Gegenprüfung (Werkstatt, Nachricht 1009): „Nein“ zum Paket, drei fehlende Prüfungen – eingearbeitet am 27.11.:**
- Sperre: Probe jetzt per Einfügen (vor Änderungen steht ein Schutz-Trigger); jeder andere Ausgang als der Abbruch an `aufgabe_antworttyp_check` ist ein Fehler.
- Rechte in beide Richtungen: Der Bewertungsweg wird im Kontext der Eigentümer der SECURITY-DEFINER-Einstiege (Schema `api`) wirklich ausgeführt und muss „richtig“ liefern; jede App-Rolle wird wirklich angenommen, der direkte Aufruf muss an fehlendem Recht scheitern.
- Altvergleich: je Typ zusätzlich gebaute richtige und falsche Antworten für 40 Aufgaben; das Paket bricht ab, wenn bei einem Typ richtig, falsch oder Formatfehler fehlt.
- Exakter Leseweg durchgängig: `lade_json` (Kommazahlen behalten ihre Schreibweise, rechnen sonst wie bisher), `schreibe_json` für die verlustfreie Weitergabe; auch `tools/inhalt_pruefen.py` und der Vergleichstest lesen so. Regressionsfall 1.00000000000000001 in den Prüf-Fällen.
- Dritter Messfall mit Potenzen, Divisionen, Betrag und dem Weg „nicht definiert“ in Prüfung und Hinweis.

**Stand der Prüfung dieser letzten Änderungen:** nur gegen die Python-Referenz („OK – 17 Aufgaben, 178 Prüfungen“). Der Vergleich mit der Datenbank für genau diesen Stand findet im Einspiel-Paket statt, vor dem Gültigwerden. Der frühere Vergleich (6 200 Antworten) galt dem Stand davor.

**Offen aus dem Gegenlesen des Mathe-Profis:** In der Muster-Aufgabe 6-K8-1 verraten die Namen der Bedingungen den Lösungsgedanken; Namen werden nach dem ersten Fehlversuch gezeigt. Regel für Autoren: Der Name nennt die Forderung aus dem Aufgabentext, nicht den Weg.

## Teil 2 (BD-S2) – als Datei geschrieben am 27.11., nicht eingespielt, noch nicht gegengeprüft
`supabase/migrations/20261202_bd_s2_bedingung_ausgabe.sql`. Eine Transaktion: Schutz und Öffnung gemeinsam.
- **Eine Stelle für alles, was von einer Lösung den Server verlässt:** `schule.loesung_sicht(aufgabe)`. Typ `bedingung`: nur `beispiel` und die Namen der Bedingungen. Alle anderen Typen wie bisher.
- **Sechs Ausgaben umgestellt** (in der Datenbank gelesen, andere gibt es nicht): `uebung_pruefen_intern` (5 Stellen), `test_abschliessen_intern`, `expeditionen_kind`, `expeditionen_alle`, `api.schule_lernstand`, `api.schule_inhalt_lesen`. Die Anker der Text-Patches sind gegen die echten Definitionen gezählt (nur lesend): alle zehn Zählungen stimmen.
- **Übung:** `verletzt` und `hinweis` gehen beim ersten Fehlversuch, bei wiederholter Übertragung und am Ende an die App. Im laufenden Test bleibt es beim Formatstatus (dort war nichts zu ändern).
- **Versionen:** Felder, Bedingungen und Beispiel sind fest, sobald es einen Versuch gibt (eigener Trigger; gilt auch für Expeditionen).
- **Constraint:** Antworttyp `bedingung` zugelassen; zweiter Constraint prüft jede solche Aufgabe mit `schule.bed_gueltig`.
- **Offen:** Einspiel-Paket für Teil 2 (wie bei Teil 1, mit Probe der tatsächlichen Antwortobjekte je Weg und Rolle); Gegenprüfung durch ChatGPT; App (Eingabe mit mehreren Feldern, Anzeige von Hinweis, Namen, „Zum Beispiel“); Feld für Regel-Kennung und Fehlbild; Eltern-Ansicht.
- **Reihenfolge:** Teil 2 erst, wenn Teil 1 eingespielt ist und die App die neuen Felder anzeigen kann. Vorher gibt es keine Aufgabe des Typs.

## Was als Nächstes kommt
- Teil 1 einspielen (Paket liegt bereit; Satz des Nutzers steht aus).
- App: Eingabe mit mehreren Zahlenfeldern nach Vorgabe ÜB des Designers, Hinweis, „Zum Beispiel“. Tests.
- Einspiel-Paket für Teil 2, Gegenprüfung, Satz des Nutzers.
- Spätere Feldarten `wahl` und `menge`.

## Nicht geprüft
- Siehe „Stand des Baus“: alles, was nur mit der echten Migration geht.
- Bedienung am Handy mit fünf oder sechs Feldern (Vorgabe des Designers liegt vor, gebaut ist nichts).
- Kein Kind hat eine Aufgabe dieses Typs gerechnet.
