# Postfach bau-eltern (Bau-Chat App-Code)

## 2026-11-16 07:40 – FERTIG – Paket E-1 (App 0.74.1, Zweig bau-eltern, nicht gemergt)

**Gebaut** (Commits 955b179, dc37665):
1. **Flugplan speichert sofort** (`viewPlan`): Jede Änderung (↑ ↓ ⤒, hinzufügen, entfernen, „kann es schon“) ruft sofort `schule_plan_setzen` mit `revision` auf. Die Revision aus der Antwort gilt für die nächste Änderung. Schnelle Folgeänderungen werden nacheinander gespeichert, nie gleichzeitig. Der Knopf „Plan speichern“ ist entfallen.
   - Unten erscheint die Leiste „Gespeichert · Rückgängig“ (8 s). „Rückgängig“ stellt den Stand vor der letzten Änderung wieder her und speichert ihn; mehrfach möglich, bis 30 Schritte.
   - **Versionskonflikt** (Fehlertext der Datenbank „inzwischen geändert“): Meldung „Der Plan wurde inzwischen von jemand anderem geändert. Deine letzte Änderung ist nicht gespeichert – es wird nichts überschrieben.“ mit Knopf „Neu laden“. Die Liste und „Ort hinzufügen“ sind bis zum Neuladen gesperrt.
   - Bei anderen Fehlern erscheint „Nicht gespeichert: …“ mit dem Knopf „Erneut versuchen“.
2. **Info-Seite „So funktioniert’s“** (`#/info`, `viewInfo`):
   - Oben stehen vier Karten „Erste Schritte“: Flugplan prüfen, Lernstand lesen, Inhalte ansehen, Ändern lassen. Die ersten beiden haben Links je Kind.
   - Darunter folgen 7 aufklappbare Fragen aus `info-seite.md`.
   - Erreichbar mit einem Tipp über „ⓘ So funktioniert’s“ oben rechts auf der Startseite der Eltern und Lehrer, im Flugplan und zusätzlich in der Lehrplan-Übersicht. Dort misst das Nachprüf-Skript den Link.
   - Kinder werden von `#/info` weggeleitet, weil die Seite nicht unter `KIND_ANSICHTEN` steht.
3. **Reisewörter** in allen Eltern- und Lehrertexten: Startseite, Flugplan, Lehrplan-Übersicht, Inhalte, Lernstand, Rückmeldungen, Zugänge, „✎ Anmerkung“-Beschriftungen und Arten (z. B. „Flug fehlt“, „Mehr Bordkarten“). Aus „Themenplan“ wurde „Flugplan“, aus „Thema hinzufügen“ wurde „Ort hinzufügen“, weil dort Orte eingefügt werden. Code, Datenbank und `inhalte/README.md` sind unverändert.
4. Version 0.74.1 überall, Cache `v133`; in `tests/search.test.cjs` Cache `v130`.

**Prüfpunkte aus umsetzung.md (E-1):**

| Prüfpunkt | Ergebnis |
|---|---|
| `rundgang.test.cjs`: Ort verschieben, Seite verlassen, zurück → Änderung ist da | **erfüllt**: Melbourne steht danach auf Platz 2, auf Tablet, Handy und Rechner. Zusätzlich prüft der neue Test „Flugplan: Änderung bleibt nach Verlassen der Seite …“ dasselbe mit einem Mock, der wie die Datenbank speichert und die Revision prüft. |
| Info-Seite von der Startseite und vom Plan mit einem Tipp erreichbar | **erfüllt** (eigener Test; im Rundgang meldet `hilfe` „ⓘ So funktioniert’s“) |
| E1: Sofort-Speichern mit `revision`, „Gespeichert · Rückgängig“, Konfliktmeldung, kein „Plan speichern“ | **erfüllt** (Tests) |
| Info-Seite aufgebaut aus Erste Schritte und Fragen, Text in Reisewörtern | **erfüllt**. Ein Test stellt sicher, dass auf allen Eltern- und Lehrerseiten in festen Texten kein „Lernkarte/Aufgabe/Thema/Themen/Lernziel/Gebiet“ vorkommt. |

**Tests:**
- `tests/lernen.test.cjs`: 18 von 18 bestanden. 3 Tests sind neu, die übrigen sind an die neuen Texte angepasst.
- `tests/search.test.cjs`: dieselben 9 alten Fehler wie auf `lernen-app` (gegengeprüft). Nr. 108 schlug einmal fehl und lief danach dreimal einzeln durch. Er ist instabil und gehört nicht zu diesem Auftrag.
- **Nachprüf-Skript** `rundgang.test.cjs`: läuft durch (4/4); vorübergehend kopiert, danach wieder entfernt. Für den Lauf habe ich die Kopie an zwei Stellen angepasst:
  - Es suchte den entfallenen Knopf „Plan speichern“ und brach ab. Das Feld `speichernY` ist jetzt optional, der Status kommt aus der neuen Leiste.
  - Sein Mock speicherte `schule_plan_setzen` nicht. Ohne Speichern ließe sich „Änderung ist da“ nicht messen.
  - **Der Prüf-Chat sollte diese zwei Stellen im Skript ebenfalls anpassen.** Gemessen bleibt: Platz 10 → 2 braucht weiterhin 8 Tipps. Das gehört zu E-2 (Ziehen).

**Info-Seite gegen Code und Antworten vom 16.11. geprüft – geändert gegenüber info-seite.md:**
- „Etappe sitzt: 2–4 Bordkarten hintereinander“ ersetzt durch die Regel vom 16.11.:
  - 6 Punkte, +1 bei richtig im ersten Versuch ohne Tipp, −2 bei Fehler.
  - Mindestens eine schwere Bordkarte muss im ersten Versuch richtig sein.
  - Bei wenigen Bordkarten genügen weniger Punkte, mindestens 2.
  - Die Stufe steigt mit den Punkten.
- Neu aufgenommen: Eine neue Etappe zeigt zuerst die Erklärung. Bei einem Fehler gibt es zuerst einen zweiten Versuch (Ausnahme: Auswahl mit zwei Antworten). Ein richtiger zweiter Versuch bringt keinen Punkt.
- Wiederholung: „Tage“ heißt jetzt Lerntage. Ergänzt sind: höchstens 6 vor einem Flug; ein Fehler bringt die Etappe am nächsten Lerntag wieder; zwei Fehler hintereinander bedeuten neu üben.
- Statt „14–18 Bordkarten“ steht „im Schnitt etwa 20“ (Stand 16.11.: 21,8 je Etappe).
- Statt „Korrektur-Test“ steht „Verbessern“, wie der Knopf in der App heißt.
- Statt „Entwurf → in Prüfung → freigegeben“ beschreibt die Seite, was die App tatsächlich zeigt: „in Prüfung“ (nur das Testkind sieht den Flug) und „fertig“.
- Ergänzt: Belohnungen mit konkreten Zahlen (10/20 Sterne, wie im Reisepass); Planen geht nur für ganze Orte (der heutige Stand vor E-2); Sofort-Speichern und Konflikt beim Flugplan.
- Kapitel 6 beschreibt den heutigen Weg: „✎ Anmerkung“ in „Inhalte ansehen“ zu Etappe oder Flug, an Bordkarten nur in der Lernreise eines Kindes; „Rückmeldungen an die Entwicklung“; „Bauen lassen“. Dazu die heutigen 8 Arten. E-3 ändert das, dann muss der Text nachgezogen werden.

**Nicht geprüft werden konnte:**
- **Nachtests „nach 10, 25 und 60 Lerntagen“:** Diese Werte stehen nicht im App-Code und in keiner Migration im Repository. Die Funktion lebt nur in der Datenbank, und die habe ich nicht angerührt. Ich habe sie unverändert aus `info-seite.md` übernommen; der Haupt-Chat sollte sie an der Datenbank prüfen. Geprüft sind dagegen: 3 Runden, die Schwellen 80 % und 60 % und die Rückreise.
- „Derzeit 87 Flüge“ und „16 Flüge in Prüfung der Klassen-Zuordnung“: Beides habe ich aus `inhalte/themenliste.json` nachgezählt. Die Zahlen veralten mit D1 und stehen fest im Text (`LERN_INFO_FRAGEN` in lernen.js).
- Echte Geräte: geprüft nur in Chromium (Playwright) bei 390, 820 und 1280 px.

**Offene Fragen / Hinweise (Annahmen getroffen, nichts blockiert):**
1. **Rückgängig nach „Entfernen“ eines geschafften Ortes:** `schule_plan_setzen` setzt einen wieder hinzugefügten Ort von `entfernt` auf `offen`. Ein zuvor `fertig` markierter Ort verliert damit die Markierung. Das liegt an der Datenbank, nicht an der App. Mein Vorschlag für E-2 oder eine Migration: beim Entfernen den alten Status merken oder `fertig` nicht überschreiben. Keine Migration angelegt, E-1 kommt ohne aus.
2. **Antworten der Entwicklung** (z. B. „6 neue Aufgaben ergänzt.“) erscheinen wörtlich auf der Startseite. Sie sollten künftig ebenfalls Reisewörter benutzen. Das ist Inhalt, kein App-Text.
3. **Pflege der Info-Seite:** Der Text steht in `LERN_INFO_FRAGEN` (lernen.js) mit dem Kommentar, ihn bei Regeländerungen im selben Schritt anzupassen.
4. Die Lehrplan-Übersicht hat den Info-Link zusätzlich bekommen; das ging über den Auftrag hinaus und kostete nichts.
