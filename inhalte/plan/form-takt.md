# Neue Aufgabenformen im festen Takt („Form-Takt“) – Vorgabe für den Bau

Stand 27.11.2026. **Entschieden vom Nutzer („ja ja“):** A – jede dritte Aufgabe einer Lernkarte kommt in neuer Form; B – eine Lernkarte gilt erst als „sitzt“, wenn mindestens eine Sachaufgabe dabei war (nur für Lernkarten, die noch nicht gelandet sind; Geschafftes bleibt geschafft).
Grundlagen: Antwort des Mathe-Profis `inhalte/mathe-profi/rollend-2/verhaeltnis.md`, Gegenprüfung Werkstatt 1020 und 1022 (Fragen A–C), Befund zur Auswahl in `aufgabentypen-auswahl.md`, Abschnitt „Neue Aufgabenformen bevorzugt ziehen“.

## Warum
Die App zieht je Lernkarte die erste passende Aufgabe in der gelieferten Reihenfolge. Neue Aufgaben stünden hinten und kämen fast nie dran. Alle nach vorn zu stellen ist abgelehnt (dann rechnen die Kinder nicht mehr). Der Bestand ist nach Tätigkeit schon gemischt (rechnen 52 %, verstehen 30 %, anwenden 19 %); was fehlt, ist die neue **Form**.

## Regeln (verbindlich)
1. **Zwei neue Angaben je Aufgabe**, getrennt von allem Vorhandenen (`art` und `typ` der Tabelle sind belegt und werden nicht umgedeutet):
   - `form`: leer = Bestand. Sonst eine von: `lueckenweg`, `fehler_detektiv`, `verfahren_waehlen`, `zwei_wege`, `umkehren`, `bruecke`, `anwenden`, `viele_antworten`. Unbekannte Werte werden abgewiesen.
   - `zaehlt`: `ja` oder `nein`. Leer = `ja` (Bestand verhält sich wie bisher). `folge` gibt es nicht mehr (Vorschlag des Mathe-Profis); die drei vorhandenen Aufgaben mit `folge` werden vor dem Einspielen auf `ja` oder `nein` gesetzt.
2. **Takt:** Innerhalb einer Lernkarte ist jede dritte Aufgabe eine mit `form` (Plätze 3, 6, 9 … der Bearbeitungen dieses Kindes an dieser Lernkarte), passend zur Stufe, die gerade dran ist. Gibt es in dieser Stufe keine ungelöste Aufgabe mit `form`, kommt eine normale Aufgabe; nichts wird aufgestaut. Die Zahl 3 ist eine Regel in `schule.regel` (`form_jede`, Vorgabe 3), nicht fest im Code. Der Platz ergibt sich aus der Zahl der bisherigen Bearbeitungen des Kindes an der Lernkarte (über Sitzungen und Geräte hinweg gleich), nicht aus einem Zähler im Gerät.
3. **Vorrang:** Was die Karten-Regeln heute verlangen (schwere Aufgabe noch nötig, noch ungezählte Aufgaben zuerst, nie zweimal derselbe Typ), gilt weiter. Der Takt wählt nur, aus welchem Vorrat die nächste Aufgabe kommt.
4. **Nach zwei Fehlern in Folge** (heute: eine Stufe leichter): die nächste Aufgabe ist ein `lueckenweg` dieser Lernkarte, wenn es einen ungelösten gibt – höchstens einmal, nie zwei Gerüste hintereinander. Kein Fehler-Detektiv direkt nach einem eigenen Fehler.
5. **„Sitzt“ nur über Aufgaben, die zählen – durchgesetzt in der Datenbank, nicht in der App:** Eine Aufgabe mit `zaehlt = nein` wird bewertet und als Versuch gespeichert, ändert aber nichts an eigenen Lösungen, gezählten Aufgaben, Typen, schwerer Aufgabe und Folge der Karte (für die Folge neutral: sie verlängert und unterbricht nichts). Derselbe Filter gilt überall, wo Rechenbelege entstehen oder gezählt werden: Buchung der Karte, Nachrechnen der Folge, Ziel/Typen/schwer nötig, Wiederholungen und Mischkarten (dort werden Aufgaben mit `zaehlt = nein` gar nicht gezogen), Wiederlandung.
6. **Sachaufgaben-Pflicht (B):** Eine Lernkarte landet nur, wenn unter den gezählten Aufgaben mindestens eine der Art „anwenden“ ist (Typ `g` aus der Zuordnungstabelle des Mathe-Profis: `einkleidung`, `transfer`, `pruefung`; maßgeblich ist die Tabelle in `verhaeltnis.md`) – **aber nur, wenn die Lernkarte überhaupt eine freigegebene Übung dieser Art hat.** Sonst entfällt die Pflicht (wie heute bei „schwer nötig“). Gilt nur für Karten, die noch nicht „sitzt“ sind; nichts wird zurückgenommen. Die App zeigt dem Kind, wenn nur noch die Sachaufgabe fehlt, und legt dann eine vor.
7. **Tests:** Flug-Test und Nachtest ziehen aus den Vorräten `test`/`sicherung`. Die neuen Aufgaben sind Übungen; an den Tests ändert dieser Bau nichts.
8. **Kein Verweis ins Regel-Universum vor der Aufgabe** (kommt später in der Rückmeldung).

## Was gebaut wird
- **Datenbank (ein Schritt, selbstprüfend):** Spalten `form`, `zaehlt` mit Prüfbedingungen; Ausgabe in `schule.aufgabe_anzeige`; Mitnahme in `schule.aufgaben_einfuegen` (Felder `form`, `zaehlt` im JSON); Regel `form_jede`; Filter „zählt“ an allen Stellen aus Punkt 5; Sachaufgaben-Pflicht aus Punkt 6 mit Ausgabe „Sachaufgabe nötig / erfüllt“ an die App.
- **App:** Takt in `lernWaehleBordkarte`, Lückenweg nach zwei Fehlern, Anzeige „Sachaufgabe fehlt noch“.
- **Werkzeug:** `tools/rollend_sql.py` gibt `form` und `zaehlt` aus den Dateien des Mathe-Profis mit (`typ` → `form`).
- **Inhalte:** je Lernkarte etwa drei Aufgaben in neuer Form; es fehlen rund 105.

## Reihenfolge
1. Bau Datenbank als Dateien (Migration und Einspiel-Paket), Probe gegen die Live-Fassung nur lesend → Gegenprüfung → Satz des Nutzers → einspielen.
2. Bau App → Gesamttest → „Live“.
3. Vorrats-Aufgaben einspielen (nach eigener Inhaltsprüfung), mit `form` und `zaehlt`.
Bis Schritt 3 ändert sich für die Kinder nur Regel 6 (Sachaufgaben-Pflicht) – sie greift mit Schritt 1 und 2.
