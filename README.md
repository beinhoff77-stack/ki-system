# ki-system

Web- und Handy-App für Sebastians persönliches KI-System: Council und Unterkunftssuche.

- Bestehende Seite: https://beinhoff77-stack.github.io/ki-system/
- Veröffentlichter Stand: **0.10.2**. Ausbau **0.13.0** auf `feature/unterkunft-suchprofile-w54`, aufbauend auf den Folge-PRs für 0.11.0 und 0.12.0, zur Gegenprüfung.
- Daten und Suchlogik liegen in Supabase hinter `app-api`. Keine Schlüssel oder Live-Testdaten im Repository.
- Kein Merge oder Deploy aus diesem Featurezweig ohne Sebastians ausdrückliche Freigabe.

## Aufbau und Gestaltung

`index.html` enthält die App-Hülle und Login-Vorlage, `app.js` die Bedienlogik, `stay-tools.js` Fotos, Merkliste, Filter und Karte, `style.css` die Gestaltung. Manifest, Service Worker und Icons ermöglichen die installierbare App-Hülle.

Die Startseite `#/start` bietet zwei gleichwertige Bereiche: **Council** und **Unterkunft**. Der Bereichswechsler bleibt erreichbar. Council enthält Aufträge, Auftragserstellung, Einstellungen und Werkstatt. Unterkunft enthält Suchen (`#/suche`) und Ergebnisse (`#/ergebnisse`); gespeicherte Suchläufe öffnen über `#/suche/<id>`.

Unterkunft übernimmt die Designbasis des Original-Prototyps V0.4.1: Creme, Waldgrün, Serifentitel, grüner Hero und nummerierte Formulargruppen. Große Bildschirme zeigen eine Vergleichstabelle; Handys und kleinere Tablets bis 1199 Pixeln zeigen Trefferkarten. Liste und Landkarte verwenden dieselben Filter.

## Suchablauf

`stay-form.js` ergänzt das Suchformular aus dem Serverkatalog `unterkunft_suchprofile_lesen`. Städtereise ist als Hauptart aktiv; kommende Hauptarten bleiben sichtbar gesperrt. Eine Nebenart lässt sich mit 10–50 Prozent mischen (70/30, 50/50 oder eigener Anteil). Unterkunftsform und Suite-Wunsch, ein abschaltbarer Qualitätsfilter sowie fünf aufklappbare Filterblöcke mit Pflicht/Wunsch/Egal sind angebunden. Balkon startet entsprechend dem Server als Wunsch, Suite bietet keine Pflicht-Auswahl. Schlafzimmer verwendet denselben sichtbaren Zahlenwert wie die Grundangaben. Zahlen aktiver Kriterien werden vor dem Anlegen geprüft.

Suchprofile übernehmen die Voreinstellungen in das Formular; Zielort und Reisezeit bleiben stehen. Die sichtbaren Werte werden anschließend vollständig neu eingelesen, ohne eine erneute serverseitige Profilzusammenführung: Ein gelöschtes Budget oder eine abgewählte Nebenart kehrt damit nicht aus dem Profil zurück. Quellen aus einem Profil bleiben sichtbar und werden übernommen. „Als Profil speichern“ verwendet nur erlaubte Voreinstellungen, ohne Ziel und Reisedaten; diese müssen zum Speichern noch nicht eingetragen sein. Ein gleicher Name wird sichtbar als Ersatz gekennzeichnet. Unbestätigte Schreibantworten sperren erneutes Speichern bis zum Lesen, ohne den aktuellen Formularentwurf zu verlieren.

Vor Veröffentlichung ist der Serverhinweis aus Werkstatt-Nachricht 195 zu klären: Beim Profil-Speichern wurden explizite Egal-Kriterien entfernt, wodurch ein abgewählter Balkon beim erneuten Laden wieder zum Standardwunsch werden könnte. Die App sendet Balkon/Egal ausdrücklich; sie erfindet keinen dauerhaften Ersatz für den Serververtrag.

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

Weitere Filter: Ergebnisgruppe, Unterkunftsform, Gesamtpreis, Gehzeit, Gästenote (auf 10 normiert), Bewertungsanzahl, Score, Datenlage und Hotelsterne. Unbekannte Werte bleiben standardmäßig sichtbar und können abgewählt werden. Hotelsterne gelten nur für Hotel/Aparthotel/Ryokan. „Nur Gemerkte“ zeigt die persönliche Auswahl. Filter, Sortierung, Seitengröße und Listen-/Kartenansicht bleiben pro Suchauftrag im Sitzungsspeicher dieses Browser-Tabs erhalten; keine geräteübergreifende Ansichtssynchronisierung.

Merken, Ausschließen, Wiederherstellen und Rückgängig schreiben ausschließlich nach Klick über `unterkunft_treffer_status_setzen`. Nur eine vollständig bestätigte Antwort gilt als gespeichert. Bei unklarer Antwort wird vor weiteren Änderungen erneut gelesen. Parallele ältere Leseantworten überschreiben keine inzwischen gespeicherte Auswahl. Persönliche Ausschlüsse erscheinen bei ausgeschlossenen Treffern und verschwinden von der Karte. Fachliche Ausschlüsse (`topf=ausgeschlossen`, etwa Budget) bleiben unabhängig vom persönlichen Status bestehen. Die Merkliste ist von Passt/Passt nicht und dem Rückmeldungsbericht getrennt.

## Gezielte Nachrecherche

`stay-research.js` bindet den Lückenfüller an: In Liste B können bis zu 30 aktive Treffer mit Warnungen oder Datenlücken gewählt werden. Auswahl und Felder (Zimmer/Betten, Gesamtpreis, Balkon, Storno) bleiben beim Sortieren, Filtern und Blättern erhalten; inzwischen ausgeschlossene Treffer werden aus der Auswahl entfernt. Erst „Lücken füllen (n)“ legt über `unterkunft_lueckenfueller_anlegen` einen Auftrag an. Doppelklickschutz, Bestätigung des Auftrags und ein für denselben Versuch stabiler Idempotenzschlüssel verhindern unbemerkte Wiederholungen.

Die App zeigt den kopierbaren Text „Lückenfüller Auftrag <ID> ausführen“. Sie startet keine Claude-Recherche und sendet keine Nachricht automatisch. Bei verweigerter Zwischenablage lässt sich der Text manuell kopieren. Bestehende offene Aufträge können je Treffer erneut geöffnet werden. `unterkunft_lueckenfueller_lesen` zeigt die letzten 50 Aufträge: angelegt/in Arbeit/erledigt/teilweise/nicht möglich. Unklare Schreibantworten erfordern zuerst eine Statusaktualisierung; passende angelegte Aufträge werden dabei wiedergefunden. Lesefehler lassen Treffer und zuletzt gelesene Statusangaben stehen.

## Fotos und Landkarte

Fotos aus `bild` werden ausschließlich als HTTPS-Hotlinks ohne Referrer und verzögert geladen. Fehlerhafte oder fehlende Fotos erhalten einen Platzhalter; Bilddateien werden weder kopiert noch im Service-Worker-Cache gespeichert. Die Quellenangabe stammt aus `bild_quelle`.

Leaflet **1.9.4** liegt mit BSD-2-Clause-Lizenz unter `vendor/leaflet-1.9.4/`. Die Dateien entsprechen den offiziellen SHA-256-Werten: JS `20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=`, CSS `p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=`. Eigene Markierungen verwenden keine Standard-Markerbilder.

Erst die Kartenansicht lädt den OpenStreetMap-Hintergrund; kein Vorladen oder Offline-Kartenarchiv. HTTP-Caching und Browser-Referrer bleiben für Kartenkacheln unverändert. Die Namensnennung bleibt sichtbar. A-Marker tragen den Rang, B-Marker sind grau, unbewertete Treffer hohl, Ziele mit Stern und Stationen mit Punkten dargestellt. Klick führt zur richtigen Seite der Ergebnisliste. Alle gefilterten aktiven Treffer sind berücksichtigt, unabhängig von der Listenseite. Ungültige Koordinaten werden gezählt; Treffer über 25 km Zielluftlinie bleiben als Marker vorhanden, aber außerhalb der anfänglichen Ausschnittsberechnung. Bei fehlendem Hintergrund bleiben Marker und Liste nutzbar.

Gehzeiten zeigen bei `geschaetzt` ein „ca.“, bei `route` (alter Alias `ors`) „berechneter Fußweg“. Stationsname und Stationsluftlinie erscheinen, wenn geliefert. Die Zielluftlinie wird aus `luftlinie_ziel_m` angezeigt; fehlende Werte bleiben unbekannt. Weitere Angebote zeigen Quelle, Preis und sichere Links sowie den Hinweis, dass Zimmer nicht abgeglichen wurden. Rakuten-Quellenhinweis und unbekannte Warncodes bleiben erhalten.

Jeder Treffer bietet Passt / Passt nicht / Zu teuer / Gebucht mit optionalem Grund (maximal 1000 Zeichen). Nur ein Klick schreibt über `unterkunft_rueckmeldung_geben`. Entwürfe bleiben beim Sortieren und Blättern erhalten. Aktualisieren übernimmt neue Serverurteile, ohne ungespeicherte Gründe zu verwerfen. Eine bereits laufende Leseantwort überschreibt keine zwischenzeitlich gespeicherte Rückmeldung. Die Rangfolge wird nicht geändert.

Der Rückmeldungsbericht wird auf Klick über `unterkunft_rueckmeldung_report` gelesen. Unter der Schwelle liefert der Server einen Zählerstand (derzeit 20 Urteile). Inhaltlich wird der Text nicht umgeschrieben. Markdown wird mit erlaubten Formatierungselementen dargestellt, bei fehlender Bibliothek als Text. Ausführbare Inhalte und Attribute werden entfernt. Sichere HTTP(S)-Beleglinks bleiben in Council-Texten nutzbar; der Rückmeldungsbericht enthält keine aktiven Links.

## Offline und Anmeldung

Der Service Worker speichert nur die ausdrücklich aufgeführten App-Dateien. Der Cache ist an den Installationspfad gebunden; andere Anwendungen behalten ihre Caches. Skript und Stylesheet tragen die App-Version in ihrer URL, damit ein Browser beim Update keine alten Dateien mit der neuen Oberfläche mischt. Die Offline-Hülle verwendet dieselben URLs; Netzwerkabrufe validieren den HTTP-Cache. API-Antworten und beliebige Dateien derselben Domain werden nicht zwischengespeichert. Offline steht die App-Hülle zur Verfügung, Suche und Ergebnisse benötigen eine Verbindung. Die Markdown-Bibliothek ist optional und wird nicht offline gespeichert.

Zur Installation die Seite in Safari/Chrome öffnen und „Zum Home-Bildschirm“ wählen. Die Anmeldung wird durch die bestehende app-api verwaltet.

## Tests und Prüfstand

Voraussetzung: Node.js >= 20.

```sh
npm ci
npx playwright install chromium
npm test
```

**44 Browsertests** prüfen Formular/API-Reihenfolge, Doppelklick, Warteschlange/Bewertung, Abbruch, Fehler/401, unvollständige Antworten, Navigation, Ranking, Sortierung/Filter/Seiten, Rückmeldungen und persönliche Auswahl samt überlappender Lese-/Schreibvorgänge, Fotos/Referrer/Platzhalter, Kartenfilter/Ausschlüsse/Nullkoordinaten/Listensprung, gespeicherte Filter, Lückenfüller-Auswahl/30er-Grenze/Doppelklick/Fehlerwiederherstellung/Kopieren/Status, Reisearten/Kriterien/Profilwechsel/Profil-Speicherung/Katalogfehler, Markdown/Links, mobile und Tablet-Breiten, Tastaturbedienung sowie Offline-Hülle/Cache-Isolation und das Update mit bereits gefülltem HTTP-Cache. Die Tests verwenden synthetische Antworten und starten keine echte Suche, Auswahländerung oder Rückmeldung. Fotos und Kartenkacheln werden in den Tests simuliert, ohne externe Kartendienste abzufragen. Screenshots liegen ignoriert in `test-results/`.

Am 16.10.2026 wurden Suchlauf #2 und der Rückmeldungsbericht über den vorhandenen Lesezugang geprüft; ihre Daten werden nicht eingecheckt. Claudes Kyoto-Lauf #5 wurde durch diese UI-Arbeiten nicht gestartet, gestoppt oder verändert.

Claude hat die Schnittstellen in Werkstatt-Nachricht 165 geprüft und die App nach der Pflichtkorrektur `route` als freigabefähig bewertet. Die Korrektur ist in 0.10.1 enthalten. Sebastian hat am 16.10.2026 die Veröffentlichung von App 0.10.x ausdrücklich freigegeben. Der anschließende angemeldete Browser-Live-Test mit dem vorhandenen Suchauftrag #5 wird mit dem Veröffentlichungsstand in Wunsch 41 dokumentiert. Die automatisierten Browserprüfungen ersetzen diese Abnahme nicht.

## Zusammenarbeit

Werkstatt-Wunsch 41: App-Verantwortung bei ChatGPT, Backend bei Claude. Vor Änderungen `app:repo` sperren, vorhandenen Featurestand prüfen, danach Änderungen protokollieren und die Sperre freigeben. Größere Änderungen gehen zur Gegenprüfung; Sebastian entscheidet über Veröffentlichung.

Der Ausbau 0.11.0 gehört zu Wunsch 50 (Fotos/Karte) und Wunsch 33 (Filter/Auswahl). Die für 0.10.x erteilte Veröffentlichungserlaubnis ersetzt nicht die Abnahme dieses Ausbaus. Ausbau 0.12.0 ergänzt Wunsch 51 (Lückenfüller) in einem eigenen Folge-PR. Ausbau 0.13.0 ergänzt Wunsch 54 (erweiterte Suche/Suchprofile) im nächsten Folge-PR.


### Kyoto-Abgleich (App 0.10.1)

Historischer Stand vor Claudes Budgetkorrektur aus Nachricht 170. Aktuell nach der Korrektur: A16, B23, unbewertet48, ausgeschlossen26. Der neue Lesevertrag liefert 113 Fotos und 34 Stationen. Die App-Arbeiten haben diese Daten nicht verändert.

Werkstatt-Nachricht 162 und Suchlauf #5 wurden lesend abgeglichen: 143 gesammelt, 30 Doppel zusammengeführt, 113 verbleibend (A16, B26, noch nicht vollständig bewertet65, ausgeschlossen6). 15 Fußwege tragen `route`, 92 `geschaetzt`. Die Anzeige wurde lokal mit der gelesenen Antwort bei 390/768/1366 Pixeln nachgespielt; dabei wurden ausschließlich Leseaktionen simuliert. Dieser Darstellungstest ist kein angemeldeter End-to-End-Test gegen app-api. Echte Daten bleiben außerhalb der eingecheckten Testfixtures.
