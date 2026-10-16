# ki-system

Web- und Handy-App für Sebastians persönliches KI-System: Council und Unterkunftssuche.

- Bestehende Seite: https://beinhoff77-stack.github.io/ki-system/
- App-Stand: **0.10.1**, Featurezweig `feature/unterkunft-suchseite-w41`, Entwurfs-PR #1.
- Daten und Suchlogik liegen in Supabase hinter `app-api`. Keine Schlüssel oder Live-Testdaten im Repository.
- Kein Merge oder Deploy aus diesem Featurezweig ohne Sebastians ausdrückliche Freigabe.

## Aufbau und Gestaltung

`index.html` enthält die App-Hülle und Login-Vorlage, `app.js` die Bedienlogik, `style.css` die Gestaltung. Manifest, Service Worker und Icons ermöglichen die installierbare App-Hülle.

Die Startseite `#/start` bietet zwei gleichwertige Bereiche: **Council** und **Unterkunft**. Der Bereichswechsler bleibt erreichbar. Council enthält Aufträge, Auftragserstellung, Einstellungen und Werkstatt. Unterkunft enthält Suchen (`#/suche`) und Ergebnisse (`#/ergebnisse`); gespeicherte Suchläufe öffnen über `#/suche/<id>`.

Unterkunft übernimmt die Designbasis des Original-Prototyps V0.4.1: Creme, Waldgrün, Serifentitel, grüner Hero und nummerierte Formulargruppen. Große Bildschirme zeigen eine Vergleichstabelle; Handys und kleinere Tablets bis 1199 Pixeln zeigen Karten. Nicht angebundene Prototyp-Funktionen wie Landkarte und Merkliste werden nicht als funktionierende Navigation dargestellt.

## Suchablauf

Die bestehende Anmeldung wird verwendet. Alle Aktionen gehen als `{aktion, daten}` an `POST /app-api/aktion`, die Antwort hat die Hülle `{ok, ergebnis}`.

1. Das Formular validiert Ziel, Zeitraum, Personen, Kinderalter, Schlafräume, Aufenthaltsbudget und Suchkostenlimit.
2. Ein Klick ruft `unterkunft_suchauftrag_anlegen` und danach `unterkunft_suche_starten` auf. Bei unklarer Startantwort bleibt die gespeicherte ID erreichbar; es gibt keine automatische Schreibwiederholung.
3. `unterkunft_suche_status` liest alle sieben Sekunden den Fortschritt. Wartende Suchen zeigen ihre Position und starten serverseitig automatisch.
4. Erst bei `fertig: true`, Fehler oder Abbruch lädt `unterkunft_suchlauf_lesen` die vollständigen Treffer. Als final gilt ausschließlich `status=fertig` zusammen mit `fertig=true`.
5. `unterkunft_suche_abbrechen` steht für laufende/wartende Suchen bereit. Vorhandene Teilergebnisse bleiben lesbar und werden nicht als finales Ranking ausgegeben.

Navigation beendet ausstehende Unterkunftsabfragen und Polling. Lesefehler pausieren die Aktualisierung; „Aktualisieren“ liest erneut. Späte Antworten einer verlassenen Council-Ansicht ersetzen keine inzwischen geöffnete Unterkunftsseite. HTTP-Fehler und fehlende Antwortdaten gelten nicht als erfolgreiche Speicherung.

## Ergebnisse und Rückmeldungen

A/B-Listen, noch nicht vollständig bewertete und ausgeschlossene Treffer bleiben getrennt. `topf=unbewertet` bleibt auch bei vorläufigem A/B-Kennzeichen außerhalb der Ranglisten. Liste A startet nach dem serverseitigen Rang; ein höherer Score ersetzt diese Rangfolge nicht. Warnungen, geschätzte Preise, Gegenprüfungseinwände, Datenlage und fünf Teilnoten sind sichtbar. Die Ampel beschreibt Verlässlichkeit, nicht Unterkunftsqualität. Bildurteile sind ausdrücklich KI-Einschätzungen.

Ein Filter sucht in Name und Anbieter. Je Liste werden 10, 25 oder 50 Treffer pro Seite dargestellt. Sortiert wird über alle gefilterten Treffer, bevor die Seite ausgewählt wird: Rang, Preis, Score, Datenlage, Bewertungsanzahl, Luftlinie, Gehzeit und fünf Teilnoten. Fehlende Zahlen bleiben in beiden Richtungen hinten; 0 bleibt gültig, leere oder falsche Datentypen gelten als unbekannt.

Gehzeiten zeigen bei `geschaetzt` ein „ca.“, bei `route` (alter Alias `ors`) „berechneter Fußweg“. Stationsname und Stationsluftlinie erscheinen, wenn geliefert. Die noch fehlende Zielluftlinie bleibt unbekannt. Weitere Angebote zeigen Quelle, Preis und sichere Links sowie den Hinweis, dass Zimmer nicht abgeglichen wurden. Rakuten-Quellenhinweis und unbekannte Warncodes bleiben erhalten.

Jeder Treffer bietet Passt / Passt nicht / Zu teuer / Gebucht mit optionalem Grund (maximal 1000 Zeichen). Nur ein Klick schreibt über `unterkunft_rueckmeldung_geben`. Entwürfe bleiben beim Sortieren und Blättern erhalten. Aktualisieren übernimmt neue Serverurteile, ohne ungespeicherte Gründe zu verwerfen. Eine bereits laufende Leseantwort überschreibt keine zwischenzeitlich gespeicherte Rückmeldung. Die Rangfolge wird nicht geändert.

Der Rückmeldungsbericht wird auf Klick über `unterkunft_rueckmeldung_report` gelesen. Unter der Schwelle liefert der Server einen Zählerstand (derzeit 20 Urteile). Inhaltlich wird der Text nicht umgeschrieben. Markdown wird mit erlaubten Formatierungselementen dargestellt, bei fehlender Bibliothek als Text. Ausführbare Inhalte und Attribute werden entfernt. Sichere HTTP(S)-Beleglinks bleiben in Council-Texten nutzbar; der Rückmeldungsbericht enthält keine aktiven Links.

## Offline und Anmeldung

Der Service Worker speichert nur die ausdrücklich aufgeführten App-Dateien. Der Cache ist an den Installationspfad gebunden; andere Anwendungen behalten ihre Caches. API-Antworten und beliebige Dateien derselben Domain werden nicht zwischengespeichert. Offline steht die App-Hülle zur Verfügung, Suche und Ergebnisse benötigen eine Verbindung. Die Markdown-Bibliothek ist optional und wird nicht offline gespeichert.

Zur Installation die Seite in Safari/Chrome öffnen und „Zum Home-Bildschirm“ wählen. Die Anmeldung wird durch die bestehende app-api verwaltet.

## Tests und Prüfstand

Voraussetzung: Node.js >= 20.

```sh
npm ci
npx playwright install chromium
npm test
```

**27 Browsertests** prüfen Formular/API-Reihenfolge, Doppelklick, Warteschlange/Bewertung, Abbruch, Fehler/401, unvollständige Antworten, Navigation, Ranking, Sortierung/Filter/Seiten, Rückmeldungen samt überlappender Lese-/Schreibvorgänge, Markdown/Links, mobile und Tablet-Breiten, Tastaturbedienung sowie Offline-Hülle/Cache-Isolation. Die Tests verwenden synthetische Antworten und starten keine echte Suche oder Rückmeldung. Screenshots liegen ignoriert in `test-results/`.

Am 16.10.2026 wurden Suchlauf #2 und der Rückmeldungsbericht über den vorhandenen Lesezugang geprüft; ihre Daten werden nicht eingecheckt. Claudes Kyoto-Lauf #5 wurde durch diese UI-Arbeiten nicht gestartet, gestoppt oder verändert.

Vor Veröffentlichung stehen Claudes Gegenprüfung und der angemeldete vollständige Browser-Live-Test gegen app-api aus. Die automatisierten Browserprüfungen ersetzen diese Abnahme nicht.

## Zusammenarbeit

Werkstatt-Wunsch 41: App-Verantwortung bei ChatGPT, Backend bei Claude. Vor Änderungen `app:repo` sperren, vorhandenen Featurestand prüfen, danach Änderungen protokollieren und die Sperre freigeben. Größere Änderungen gehen zur Gegenprüfung; Sebastian entscheidet über Veröffentlichung.


### Kyoto-Abgleich (App 0.10.1)
Werkstatt-Nachricht 162 und Suchlauf #5 wurden lesend abgeglichen: 143 gesammelt, 30 Doppel zusammengeführt, 113 verbleibend (A16, B26, noch nicht vollständig bewertet65, ausgeschlossen6). 15 Fußwege tragen `route`, 92 `geschaetzt`. Die Anzeige wurde lokal mit der gelesenen Antwort bei 390/768/1366 Pixeln nachgespielt; dabei wurden ausschließlich Leseaktionen simuliert. Dieser Darstellungstest ist kein angemeldeter End-to-End-Test gegen app-api. Echte Daten bleiben außerhalb der eingecheckten Testfixtures.
