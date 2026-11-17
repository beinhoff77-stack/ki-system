# Postfach pruefung-eltern (Eltern- und Lehrerseite)

## 2026-11-17 11:40 – FERTIG – Nachprüfung E-1 (lernen-app 0bdbde8, App 0.74.1) und Flug „Winkelsätze“ (Entwurf)

### E-1: alle vier Prüfpunkte erfüllt
| Prüfpunkt (umsetzung.md) | Ergebnis | Nachweis |
|---|---|---|
| Ort verschieben, Seite verlassen, zurück → Änderung ist da | **erfüllt** (Tablet, Handy, Rechner: Melbourne bleibt auf Platz 2) | `rundgang.test.cjs` (angepasst, siehe unten), `messung-e1.json` |
| Sofort-Speichern mit `revision`, „Gespeichert · Rückgängig“, Konfliktmeldung, kein „Plan speichern“ | **erfüllt**. Rückgängig wirkt und bleibt nach Verlassen der Seite gespeichert. Bei einem Konflikt erscheinen Meldung und „Neu laden“, die Liste ist bis dahin gesperrt; nach dem Neuladen wird wieder gespeichert. | Rundgang; Code `viewPlan` gelesen; Datenbankfunktion `schule_plan_setzen` prüft `revision` |
| Info-Seite mit einem Tipp von Startseite und Flugplan erreichbar | **erfüllt** (je 1 Link „ⓘ So funktioniert’s“) | Rundgang, `bilder-e1/*-6-info.png` |
| Info-Seite aus „Erste Schritte“ + Fragen, Reisewörter | **erfüllt** (4 Karten, 7 Fragen) | Rundgang; Reisewörter-Test selbst nachgeprüft |

Tests: `tests/lernen.test.cjs` 18/18 bestanden (selbst ausgeführt).
Regeln der Info-Seite an der Datenbank geprüft (nur gelesen): Nachtests nach 10/25/60 Lerntagen (`schule.regel` + `nachtest_stand`) ✓, 80 %/60 % ✓, 10/20 Sterne ✓, Wiederholung 1-3-7-14-30, ein Fehler → nächster Lerntag, zwei Fehler → neu üben (`karte_buchen`) ✓.

**Befunde (keiner blockiert E-1):**
1. **Info-Seite veraltet (mittel):** „derzeit 87 Flüge“ – die Themenliste hat jetzt 92. „Bei 16 Flügen … wird die Klassen-Zuordnung noch geprüft“ ist nach D2 überholt. Es fehlt „100 Sterne für einen geschafften Ort“ (`sterne_ort_geschafft` = 100). Vorschlag: Zahl der Flüge nicht fest in den Text schreiben (aus der Lehrplan-Übersicht zählen oder „über 90“). Im nächsten Bau-Schritt anpassen (Regel „Info-Seite pflegen“).
2. **Rückgängig nach „Entfernen“ (mittel, Datenbank):** Wird ein geschaffter Ort entfernt und per „Rückgängig“ zurückgeholt, setzt `schule_plan_setzen` ihn auf `offen` – die Markierung „geschafft“ geht verloren. Bestätigt den Hinweis des Bau-Chats; durch Sofort-Speichern und Rückgängig kommt das jetzt öfter vor. Lösung in E-2 oder per Migration: alten Status beim Entfernen merken.
3. **Positionen entfernter Orte wachsen (niedrig, Datenbank):** Bei jedem Speichern werden entfernte Einträge um 200 000 weitergeschoben (`position` ist `integer`). Nach etwa 10 000 Speichervorgängen je Kind bricht `schule_plan_setzen` mit Zahlenüberlauf ab. Mit Sofort-Speichern ist jeder Tipp ein Speichervorgang. Fern, aber billig zu beheben: entfernte Einträge im ersten `update` auslassen.
4. **„Rückgängig“ nur 8 Sekunden sichtbar (niedrig):** Danach ist der Knopf weg, obwohl bis zu 30 Schritte gemerkt sind. Vorschlag für E-2: Knopf dauerhaft in der Kopfzeile des Plans.
5. **Lücke im Reisewörter-Test (niedrig):** Das Muster `\bThemen?\b` trifft „Thema“ nicht (nur „Theme“/„Themen“). Mit korrigiertem Muster gibt es auf allen 8 Seiten genau einen Treffer: die gewollte Erklärung „Flug = ein Mathe-Thema“ auf der Info-Seite. Muster im Test auf `\bThema\b|\bThemen\b` ändern (die Erklärung ausnehmen).
6. **Weiterhin offen (gehört zu E-2):** Platz 10 → 2 braucht 8 Tipps; eine Zeile im Plan ist zugeklappt 507 px (Tablet) bzw. 695 px (Handy) hoch.

**Nachprüf-Skript angepasst** (wie vom Bau-Chat erbeten): `rundgang.test.cjs` sucht den Knopf „Plan speichern“ nicht mehr. Sein Mock speichert `schule_plan_setzen` jetzt wie die Datenbank: Er prüft die Revision und übernimmt die Reihenfolge. Neu gemessen werden Rückgängig, Versionskonflikt und der Info-Link. Ergebnis: `messung-e1.json`, Bilder `bilder-e1/`. Die alte Messung bleibt zum Vergleich.

### Flug „Winkelsätze“ (geometrie.winkelsaetze, Thema 98, Einheit 92, Entwurf)
Aufbau in Ordnung: `inhalt_pruefen` OK, der Generator erzeugt die Datei unverändert neu. 8 Etappen im neuen Lernkarten-Muster mit je 18 Übungen (4/6/8), 1 Test, 3 Korrektur und 6 Sicherung; keine doppelten Fragetexte. Alle 167 Zahl-Aufgaben rechnet das Prüfskript nach. Alle 56 Auswahl- und die eine Lückenaufgabe habe ich von Hand gelesen; die Stufe-3-Zahlaufgaben habe ich zusätzlich von Hand nachgerechnet.

**Vor der Freigabe beheben:**
1. **Zeichnung widerspricht der Lösung (hoch):** In 3 Aufgaben mit der Lösung „Nein“ (nicht parallel) sind g und h exakt parallel gezeichnet: Index 74 (Test), 75 und 76 (Korrektur), alle mit dem Text „k schneidet g in S und h in T … Sind g und h parallel?“. Ein Kind, das auf das Bild schaut, antwortet „Ja“. Im Generator die Gerade h bei „nicht parallel“ leicht kippen, so wie in Aufgabe 66.
2. **„weder noch“ fachlich angreifbar (mittel):** Index 51 (Sicherung): „Winkel bei S rechts oberhalb und bei T links unterhalb“ hat die Lösung „weder noch“. Diese beiden Winkel sind an Parallelen gleich groß. Nach der in vielen Schulbüchern üblichen Definition (verschiedene Seiten der Schnittgeraden und verschiedene Seiten der Parallelen) sind sie Wechselwinkel. Generator Zeile 348: den Fall `('ro', 'lu', 'weder noch')` z. B. durch `('ro', 'lo', 'weder noch')` ersetzen. Dieses Paar ist nie gleich groß, wenn der Winkel nicht 90° ist.
3. **Lückenaufgabe nicht eindeutig (mittel):** Index 206 (Beweis-Kärtchen, Lösung 2, 4, 1, 3): Die Reihenfolge 2, 1, 4, 3 ist genauso schlüssig, weil die Kärtchen 1 und 4 voneinander unabhängig sind. Kärtchen 1 so umformulieren, dass es Kärtchen 4 braucht, z. B. „Also liegen α, γ und β nebeneinander auf p: α + γ + β = 180°.“

**Kleinigkeiten:**
- Index 42: Im Lösungsweg steht „6 · 16 + 0 = 96°“ („+ 0“ ist ein Rest der Vorlage).
- Index 203, 216, 217, 219, 220, 222 (Nebenwinkel-Begründungen): Im Text fehlt „an derselben Kreuzung“ – bei den Scheitelwinkel-Aufgaben steht es dabei.
- Index 67, 69, 71, 73 (Etappe „parallel_pruefen“, Stufe 3) nutzen den Außenwinkelsatz, der erst in Etappe 5 kommt. Der Lösungsweg erklärt ihn, deshalb vertretbar; besser „Stufenwinkel-Unterschied“ ohne Namen nennen.
- 9 Zeichnungen weichen um 4–17° vom angeschriebenen Wert ab (z. B. 40, 54, 202). Das ist laut „offen“ bekannt (nicht maßstäblich) und unkritisch, außer bei Punkt 1.
- Die Überschneidung mit geometrie.konstruktion (gleicher Ort Addis Abeba, Karten „parallelen“, „winkelsumme“, „vierecke“) steht unter „offen“ und braucht eine Entscheidung von Sebastian.

**Empfehlung:** Erst die Punkte 1–3 im Generator beheben, dann freigeben. Der Rest kann bleiben.

## 2026-11-16 05:25 – FERTIG
Sebastians Auswahl umgesetzt in `inhalte/pruefung/eltern/umsetzung.md` (Pakete E-1 bis E-4).
Gewählt: Startseite je Kind · Plan in zwei Spalten (Plan + Lehrplan, ziehen) · Orte bleiben, Flüge darin abwählbar · Plan aus Lehrplan-Vorlage · „Ändern lassen“ überall + „Meine Aufträge“ · Info-Seite „Erste Schritte + Fragen“.
Muss: Planänderungen speichern sofort mit Rückgängig (E1). Eingeordnet in den Gesamtauftrag (Zweig pruefung-kinderansicht, UMBAU-AUFTRAG.md): E-1 Phase 1, E-2/E-3 Phase 2, E-4 Phase 3.

## 2026-11-16 04:50 – ENTWURF ZUR AUSWAHL
Bericht `inhalte/pruefung/eltern/bericht.md` (E1–E10), Rundgang `…/eltern/rundgang.test.cjs`, Entwurf Info-Seite `…/eltern/info-seite.md`.
Wichtigste Befunde: ungespeicherte Planänderungen gehen ohne Warnung verloren (E1); Platz 10 → 2 = 8 Tipps (E2); nur ganze Orte planbar (E4); keine Info-Seite (E9).
Sebastian wählt die Varianten im klickbaren Entwurf; danach folgt der Umsetzungsauftrag.
