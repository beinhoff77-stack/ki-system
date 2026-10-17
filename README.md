# ki-system

Web- und Handy-App für Sebastians persönliches KI-System: Council und Unterkunftssuche.

- Bestehende Seite: https://beinhoff77-stack.github.io/ki-system/
- Veröffentlichter Stand bei Arbeitsbeginn: **0.15.2** (main). Korrektur **0.16.0** auf `fix/unterkunft-ergebnisansichten` zur Gegenprüfung.
- Daten und Suchlogik liegen in Supabase hinter `app-api`. Keine Schlüssel oder Live-Testdaten im Repository.
- Kein Merge oder Deploy aus diesem Featurezweig ohne Sebastians ausdrückliche Freigabe.

## Aufbau und Gestaltung

`index.html` enthält die App-Hülle und Login-Vorlage, `app.js` die Bedienlogik, `stay-tools.js` Fotos, Merkliste, Filter und Karte, `stay-districts.js` die Viertelübersicht und ihre Suchauswahl, `style.css` die Gestaltung. Manifest, Service Worker und Icons ermöglichen die installierbare App-Hülle.

Die Startseite `#/start` bietet zwei gleichwertige Bereiche: **Council** und **Unterkunft**. Der Bereichswechsler bleibt erreichbar. Council enthält Aufträge, Auftragserstellung, Einstellungen und Werkstatt. Unterkunft enthält Suchen (`#/suche`), Ergebnisse (`#/ergebnisse`) und Viertel (`#/viertel`); gespeicherte Suchläufe öffnen über `#/suche/<id>`.

Unterkunft übernimmt die Designbasis des Original-Prototyps V0.4.1: Creme, Waldgrün, Serifentitel, grüner Hero und nummerierte Formulargruppen. Tabelle, Liste und Karte sind auf jedem Gerät getrennt wählbar. Als Vorgabe startet der Desktop ab 1200 Pixeln mit der Tabelle, das Handy mit der Liste. Die Wahl bleibt pro Suchauftrag erhalten. Alle drei Ansichten verwenden dieselben Filter; ausgeschlossene Treffer bleiben außerhalb der Karte.

## Korrektur 0.16.0: kompakte Ergebnisansichten

Die bestehende Ergebnisansicht nutzt die verfügbare Breite. Die Tabelle enthält pro Unterkunft eine kompakte Zeile mit 50 × 40 Pixel Foto, Score/Datenlage, Gesamtpreis, Schlafzimmern, Bettentypen, Gehzeit/Station, Gästenote, Warnungsanzahl und Anbieterlink. Jeder Spaltenkopf sortiert; unbekannte Werte bleiben auch absteigend hinten. Die vorhandene serverseitige Rangfolge bleibt Standard. Neue lokale Filter ergänzen Schlafzimmer, Bettentyp und Warnungen.

„Details“ klappt Nachweise, sämtliche Warntexte, Teilnoten, Begründungen, Rohdaten und Rückmeldungen über die volle Tabellenbreite auf. Die Liste zeigt dieselben Kerndaten als kompakte Karten. Auf kleinen Bildschirmen bleibt die explizit gewählte Tabelle horizontal innerhalb ihres Bereichs bedienbar, ohne die Seite zu verbreitern. Filter, Auswahl, Sortierung, Recherche und Rückmeldungsentwürfe verwenden weiter die bestehenden Zustände und Schnittstellen.

Schlafzimmer und Betten werden nur aus einer eindeutig zugeordneten Kategorie des Hauptangebots übernommen; keine Vermischung anderer Angebote. Bettentypen werden ausschließlich aus einem gelieferten Textfeld gelesen, nicht aus Namen abgeleitet. Der aktuelle Server liefert meist nur Anzahl/Eindeutigkeit, deshalb steht dort häufig „unbekannt“. K.-o.-Kriterien, Bewertungsgewichte, Scores und A/B-Gruppierung sind unverändert.

Prüfung: vollständige bestehende Browsersuite plus neue Tests für drei Ansichten, gemeinsame Filter/Marker, 50 × 40 Fotos, kompakte Zeilen, Detailzustand, 320/375/390/430 Pixel und große Schrift. Optionaler lokaler Test mit bereits gelesener Kyoto-Antwort: keine echten Schreibaktionen, keine neue Suche. Physisches iPhone/Safari und angemeldeter Live-Test bleiben gesonderte Abnahmen. Die Abschnitte mit älteren Versionsständen weiter unten sind historische Prüfprotokolle.

## Suchablauf

`stay-form.js` ergänzt das Suchformular aus dem Serverkatalog `unterkunft_suchprofile_lesen`. Städtereise ist als Hauptart aktiv; kommende Hauptarten bleiben sichtbar gesperrt. Eine Nebenart lässt sich mit 10–50 Prozent mischen (70/30, 50/50 oder eigener Anteil). Unterkunftsform und Suite-Wunsch, ein abschaltbarer Qualitätsfilter sowie sechs aufklappbare Filterblöcke mit Pflicht/Wunsch/Egal sind angebunden. Balkon und Schlafzimmer starten als Wunsch, Suite bietet keine Pflicht-Auswahl. Schlafzimmer verwendet denselben sichtbaren Zahlenwert wie die Grundangaben. Auch ältere Profile ohne Schlafzimmer-Kriterium bleiben beim Wunsch. Ausdrückliches Egal deaktiviert die Vorgabe und sendet `schlafzimmer_min=0`; damit sind auch Einzimmer-Angebote möglich. Zahlen aktiver Kriterien werden vor dem Anlegen geprüft.

Suchprofile übernehmen die Voreinstellungen in das Formular; Zielort und Reisezeit bleiben stehen. Die sichtbaren Werte werden anschließend vollständig neu eingelesen, ohne eine erneute serverseitige Profilzusammenführung: Ein gelöschtes Budget oder eine abgewählte Nebenart kehrt damit nicht aus dem Profil zurück. Quellen aus einem Profil bleiben sichtbar und werden übernommen. „Als Profil speichern“ verwendet nur erlaubte Voreinstellungen, ohne Ziel und Reisedaten; diese müssen zum Speichern noch nicht eingetragen sein. Ein gleicher Name wird sichtbar als Ersatz gekennzeichnet. Unbestätigte Schreibantworten sperren erneutes Speichern bis zum Lesen, ohne den aktuellen Formularentwurf zu verlieren.

Die Serverkorrektur aus Werkstatt-Nachricht 215 erhält ausdrücklich gespeicherte Egal-Kriterien. Der Profil-Rundlauf wurde für Balkon/Egal und den gemeinsamen Schlafzimmerwert in synthetischen Browsertests geprüft; die bereitgestellten Serverfunktionen wurden lesend abgeglichen.

Die bestehende Anmeldung wird verwendet. Alle Aktionen gehen als `{aktion, daten}` an `POST /app-api/aktion`, die Antwort hat die Hülle `{ok, ergebnis}`.

1. Das Formular validiert Ziel, Zeitraum, Personen, Kinderalter, Schlafräume, Aufenthaltsbudget und Suchkostenlimit.
2. Ein Klick ruft `unterkunft_suchauftrag_anlegen` und danach `unterkunft_suche_starten` auf. Bei unklarer Startantwort bleibt die gespeicherte ID erreichbar; es gibt keine automatische Schreibwiederholung.
3. `unterkunft_suche_status` liest alle sieben Sekunden den Fortschritt. Wartende Suchen zeigen ihre Position und starten serverseitig automatisch. „Aktualisieren“ liest auch bei laufenden Suchen die Treffer neu und kann dadurch unklare Auswahl-/Rückmeldungszustände auflösen.
4. Automatisch lädt `unterkunft_suchlauf_lesen` die Treffer erst bei `fertig: true`, Fehler oder Abbruch. Während eines Laufs kann der Nutzer „Vorläufige Treffer ansehen“ oder „Aktualisieren“ wählen. Die Bewertung und Statusabfrage laufen weiter; diese Treffer bleiben ausdrücklich vorläufig. Als final gilt ausschließlich `status=fertig` zusammen mit `fertig=true`.
5. `unterkunft_suche_abbrechen` steht für laufende/wartende Suchen bereit. Vorhandene Teilergebnisse bleiben lesbar und werden nicht als finales Ranking ausgegeben.

Navigation beendet ausstehende Unterkunftsabfragen und Polling. Lesefehler pausieren die Aktualisierung; „Aktualisieren“ liest erneut. Späte Antworten einer verlassenen Council-Ansicht ersetzen keine inzwischen geöffnete Unterkunftsseite. HTTP-Fehler und fehlende Antwortdaten gelten nicht als erfolgreiche Speicherung.

## Ergebnisse und Rückmeldungen

Quellenabdeckung erscheint sowohl während des Laufs als auch im Ergebnis. `deckung.vollstaendig=false` oder eine nicht leere Fehlquellenliste zeigt „Keine vollständige Marktsuche“. Ohne Abdeckungsdaten wird Vollständigkeit nicht behauptet. Bei weniger als zehn fachlich bewerteten A-Treffern erscheint der Hinweis zur unzureichenden Datenlage; aktive Anzeige-Filter lösen ihn nicht aus.

Treffer und Karten-Popups zeigen Preisalter, Abrufzeit und belegte/unbelegte Verfügbarkeit. „Belegt“ bezieht sich auf den Abruf, nicht auf eine Garantie aktueller Buchbarkeit. Balkon-Angaben unterscheiden bestätigte Kategorien, widersprüchliche/fehlende Angaben und die gelieferte Filterbewertung. Neue Warncodes bleiben in verständlicher Sprache sichtbar. Sprungknöpfe führen zu Unbewerteten und nach Ausschlussgrund gegliederten Treffern; deren Seitengröße bleibt begrenzt.

„Unterkunft im Detail“ öffnet eine mit Tastatur schließbare Detailansicht: Bild, Zimmerkategorien mit Quelle/Abrufzeit, alle Angebote, getrennte Gästenoten, Teilnoten mit Gewicht, Begründung und Gegenprüfungs-Einwände. Nicht gelieferte Nachweise bleiben unbekannt. Insbesondere werden Noten der Hauptquelle nicht auf weitere Anbieter übertragen. Die in Nachricht 201 angefragten Kategorie-Abrufzeiten und Noten weiterer Quellen wurden mit Nachricht 215 ergänzt und an den 113 Treffern von Kyoto #5 lesend verifiziert.

Rückmeldungen bieten Schnell-Gründe als editierbaren Entwurf; erst ein Urteil speichert. Der Verlauf liest mit `unterkunft_suchlauf_lesen {}` die gemeinsame Merkliste aller Reisen und die letzten zehn Suchaufträge. Gemerkte ältere Reisen bleiben enthalten; es gibt keine zusätzliche Einzelabfrage pro Reise. Bilder, Preisstand, Gästenoten und fachliche Ausschlüsse bleiben erkennbar. Ein Direktlink öffnet die richtige Listenseite und fokussiert den gemerkten Treffer. Lesefehler lassen die zuletzt gelesene Merkliste stehen. Links zur Merkliste je Reise erscheinen nur bei `gemerkt>0`. Ein Profil-Link öffnet das vorausgefüllte Suchformular. Rohdaten-Löschung nach 30 Tagen wird erklärt. Die neue Antwortform aus Nachricht 215 wurde live lesend geprüft; die derzeit leere Merkliste wurde dabei nicht verändert.

A/B-Listen, noch nicht vollständig bewertete und ausgeschlossene Treffer bleiben getrennt. `topf=unbewertet` bleibt auch bei vorläufigem A/B-Kennzeichen außerhalb der Ranglisten. Liste A startet nach dem serverseitigen Rang; ein höherer Score ersetzt diese Rangfolge nicht. Warnungen, geschätzte Preise, Gegenprüfungseinwände, Datenlage und fünf Teilnoten sind sichtbar. Die Ampel beschreibt Verlässlichkeit, nicht Unterkunftsqualität. Bildurteile sind ausdrücklich KI-Einschätzungen.

Ein Filter sucht in Name und Anbieter. Je Liste werden 10, 25 oder 50 Treffer pro Seite dargestellt. Sortiert wird über alle gefilterten Treffer, bevor die Seite ausgewählt wird: Rang, Preis, Score, Datenlage, Bewertungsanzahl, Luftlinie, Gehzeit und fünf Teilnoten. Fehlende Zahlen bleiben in beiden Richtungen hinten; 0 bleibt gültig, leere oder falsche Datentypen gelten als unbekannt.

Weitere Filter: Ergebnisgruppe, Unterkunftsform, Gesamtpreis, Gehzeit, Gästenote (auf 10 normiert), Bewertungsanzahl, Score, Datenlage und Hotelsterne. Unbekannte Werte bleiben standardmäßig sichtbar und können abgewählt werden. Hotelsterne gelten nur für Hotel/Aparthotel/Ryokan. „Nur Gemerkte“ zeigt die persönliche Auswahl. Filter, Sortierung, Seitengröße und Listen-/Kartenansicht bleiben pro Suchauftrag im Sitzungsspeicher dieses Browser-Tabs erhalten; keine geräteübergreifende Ansichtssynchronisierung.

Merken, Ausschließen, Wiederherstellen und Rückgängig schreiben ausschließlich nach Klick über `unterkunft_treffer_status_setzen`. Nur eine vollständig bestätigte Antwort gilt als gespeichert. Bei unklarer Antwort wird vor weiteren Änderungen erneut gelesen. Parallele ältere Leseantworten überschreiben keine inzwischen gespeicherte Auswahl. Persönliche Ausschlüsse erscheinen bei ausgeschlossenen Treffern und verschwinden von der Karte. Fachliche Ausschlüsse (`topf=ausgeschlossen`, etwa Budget) bleiben unabhängig vom persönlichen Status bestehen. Die Merkliste ist von Passt/Passt nicht und dem Rückmeldungsbericht getrennt.

## Gezielte Nachrecherche

`stay-research.js` bindet den Lückenfüller an: In Liste B können bis zu 30 aktive Treffer mit Warnungen oder Datenlücken gewählt werden. Auswahl und Felder (Zimmer/Betten, Gesamtpreis, Balkon, Storno) bleiben beim Sortieren, Filtern und Blättern erhalten; inzwischen ausgeschlossene Treffer werden aus der Auswahl entfernt. Erst „Lücken füllen (n)“ legt über `unterkunft_lueckenfueller_anlegen` einen Auftrag an. Doppelklickschutz, Bestätigung des Auftrags und ein für denselben Versuch stabiler Idempotenzschlüssel verhindern unbemerkte Wiederholungen.

Die App zeigt den kopierbaren Text „Lückenfüller Auftrag <ID> ausführen“. Sie startet keine Claude-Recherche und sendet keine Nachricht automatisch. Bei verweigerter Zwischenablage lässt sich der Text manuell kopieren. Bestehende offene Aufträge können je Treffer erneut geöffnet werden. `unterkunft_lueckenfueller_lesen` zeigt die letzten 50 Aufträge: angelegt/in Arbeit/erledigt/teilweise/nicht möglich. Unklare Schreibantworten erfordern zuerst eine Statusaktualisierung; passende angelegte Aufträge werden dabei wiedergefunden. Lesefehler lassen Treffer und zuletzt gelesene Statusangaben stehen.

Statusantworten und bestätigte Recherche-Aufträge aktualisieren ausschließlich die Recherche-Bedienelemente. Die Trefferliste wird dabei nicht neu aufgebaut: Ein gerade geschriebener Rückmeldungsgrund behält Fokus und Cursor, offene Angaben und Leseposition bleiben stehen. Nach dem Schließen eines Kandidatendialogs bleibt der ursprüngliche Knopf erreichbar. Unveränderte Recherche-Knöpfe werden auch beim Auswählen weiterer Treffer beibehalten.

## Fotos und Landkarte

Fotos aus `bild` werden ausschließlich als HTTPS-Hotlinks ohne Referrer und verzögert geladen. Referrer-Regel und Lazy-Loading werden vor `src` gesetzt, damit auch ältere Browser den Abruf bereits richtig beginnen. Fehlerhafte oder fehlende Fotos erhalten einen Platzhalter; Bilddateien werden weder kopiert noch im Service-Worker-Cache gespeichert. Die Quellenangabe stammt aus `bild_quelle`. Angebots- und Viertelquellenlinks erfordern HTTPS ohne eingebettete Zugangsdaten; Council-Beleglinks erlauben zusätzlich HTTP, ebenfalls ohne Zugangsdaten.

Leaflet **1.9.4** liegt mit BSD-2-Clause-Lizenz unter `vendor/leaflet-1.9.4/`. Die Dateien entsprechen den offiziellen SHA-256-Werten: JS `20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=`, CSS `p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=`. Eigene Markierungen verwenden keine Standard-Markerbilder.

Erst die Kartenansicht lädt den OpenStreetMap-Hintergrund; kein Vorladen oder Offline-Kartenarchiv. HTTP-Caching und Browser-Referrer bleiben für Kartenkacheln unverändert. Die Namensnennung bleibt sichtbar. A-Marker tragen den Rang, B-Marker sind grau, unbewertete Treffer hohl, Ziele mit Stern und Stationen mit Punkten dargestellt. Klick führt zur richtigen Seite der Ergebnisliste. Alle gefilterten aktiven Treffer sind berücksichtigt, unabhängig von der Listenseite. Ungültige Koordinaten werden gezählt; Treffer über 25 km Zielluftlinie bleiben als Marker vorhanden, aber außerhalb der anfänglichen Ausschnittsberechnung. Bei fehlendem Hintergrund bleiben Marker und Liste nutzbar.

Gehzeiten zeigen bei `geschaetzt` ein „ca.“, bei `route` (alter Alias `ors`) „berechneter Fußweg“. Stationsname und Stationsluftlinie erscheinen, wenn geliefert. Die Zielluftlinie wird aus `luftlinie_ziel_m` angezeigt; fehlende Werte bleiben unbekannt. Weitere Angebote zeigen Quelle, Preis und sichere Links sowie den Hinweis, dass Zimmer nicht abgeglichen wurden. Rakuten-Quellenhinweis und unbekannte Warncodes bleiben erhalten.

Jeder Treffer bietet Passt / Passt nicht / Zu teuer / Gebucht mit optionalem Grund (maximal 1000 Zeichen). Nur ein Klick schreibt über `unterkunft_rueckmeldung_geben`. Entwürfe bleiben beim Sortieren und Blättern erhalten. Aktualisieren übernimmt neue Serverurteile, ohne ungespeicherte Gründe zu verwerfen. Eine bereits laufende Leseantwort überschreibt keine zwischenzeitlich gespeicherte Rückmeldung. Die Rangfolge wird nicht geändert.

Der Rückmeldungsbericht wird auf Klick über `unterkunft_rueckmeldung_report` gelesen. Unter der Schwelle liefert der Server einen Zählerstand (derzeit 20 Urteile). Inhaltlich wird der Text nicht umgeschrieben. Markdown wird mit erlaubten Formatierungselementen dargestellt, bei fehlender Bibliothek als Text. Ausführbare Inhalte und Attribute werden entfernt. Sichere HTTP(S)-Beleglinks bleiben in Council-Texten nutzbar; der Rückmeldungsbericht enthält keine aktiven Links.

## Viertel entdecken und für die Suche wählen

Wunsch 61 ergänzt `#/viertel`: freie Ortsabfrage, Aufruf aus einem Suchlauf und direkte Links vom Treffer sowie aus dessen Detailansicht. `unterkunft_viertel_lesen` liefert die Übersicht. Die elf Kyoto-Viertel und `zone` der 113 Treffer in Suchauftrag #5 wurden nur gelesen; die Aktionsnamen und Argumente wurden zusätzlich im bereitgestellten `app-api`-Code abgeglichen.

Viertelkarten zeigen Namen, Beschreibung, Familienhinweise, Highlights, Lärm/Preisniveau, acht Noten und sichere Quellenlinks. Fehlende Noten bleiben unbekannt; eine gelieferte Null bleibt 0/10. Automatische Vorschläge sind ausdrücklich ungeprüft. Suchlaufansichten ergänzen Trefferzahl, A-Zahl, besten Rang und Preis-Median je Nacht. Die Erklärung der Noten und die OpenStreetMap-Namensnennung bleiben erreichbar. Anzeige-Filter für ruhig/ÖPNV/Nahversorgung/Gastronomie/Grün/Sehenswürdigkeiten/Zentrumsnähe sowie Sortierung wirken lokal; fehlende Zahlen stehen beim Sortieren hinten.

Die Karte lädt erst nach Klick. Kreise zeigen ungefähre Radien; ruhig/belebt/laut ist grün/gelb/rot, ungeprüft gestrichelt und bestätigt durchgezogen. Klick bzw. Tastatur führt zum Viertel. Ungültige Koordinaten werden gezählt, beim Kartenausfall bleibt die Liste nutzbar. Trefferpunkte als zusätzliche Kartenebene sind nicht implementiert (optional im Auftrag).

Bestätigen, Streichen mit Rückfrage, Wiederaufnehmen und Umbenennen/Notiz gehen ausschließlich nach Klick an `unterkunft_zone_entscheiden`. Nur passende ID und Status sowie ein anschließend passender gelesener Stand bestätigen die Speicherung; andernfalls sind weitere Änderungen bis zum erneuten Lesen gesperrt. Eine vorhandene Notiz kann die derzeitige Schnittstelle nur ersetzen, nicht leeren; die Oberfläche erklärt das. Ein während der laufenden Ermittlung geschriebener Notizentwurf samt Cursor bleibt bei neuen Leseantworten erhalten.

Mehrfachauswahl öffnet ein neues Suchformular mit `kriterien.viertel_auswahl={modus:pflicht|wunsch,werte:[...]}`. Es wird noch keine Suche gestartet. Der Entwurf liegt nur im Sitzungsspeicher dieses Tabs. Der Formularblock „Viertel“ übernimmt die tatsächlich erlaubten Kriterien aus dem Suchprofilkatalog. Konkrete Viertel werden für den aktuellen Zielort gelesen und geprüft; Ortswechsel leeren sie. Profil-IDs brauchen vor dem Suchen dieselbe Prüfung. Nicht mehr verfügbare IDs werden mit Hinweis entfernt.

„Viertel ermitteln“ nennt vor dem Klick Kosten (ca. 0,06 USD) und Dauer (1–5 Minuten). Nur dieser Klick ruft `unterkunft_viertel_erstellen` auf. Danach wird ausschließlich gelesen, auch bei unklarer Startantwort. Ein älterer abgeschlossener Lauf gilt nicht als Bestätigung der neuen Ermittlung. Bei ausbleibendem neuen Lauf endet das automatische Warten nach etwa fünf Minuten; manuelles Lesen bleibt möglich. Navigation beendet Abfragen und Timer. Bestätigte Viertel werden laut Serververtrag bei erneuter Ermittlung erhalten.

Offener Vertragsabgleich, Werkstatt-Nachricht 210: `viertel_lesen.filter_katalog` nennt `viertel_zentrumsnaehe_min` und `viertel_strand_min`, die `kriterien_pruefen` noch ablehnt. Die lokale Anzeige kann Zentrumsnähe filtern, das Suchformular sendet diese beiden noch nicht akzeptierten Kriterien nicht. Sobald der gemeinsame Suchprofilkatalog sie anbietet, kann die generische Oberfläche sie darstellen.

## Korrekturen aus Claudes Prüfung 211

Die Pflichtpunkte Foto-Attributreihenfolge und Formularüberlauf bei 375 px sind korrigiert. Angebotslinks sind HTTPS ohne Zugangsdaten, manuelles Aktualisieren liest auch laufende Treffer, Rückmeldungen verlangen `ok`, eine positive Rückmeldungs-ID sowie passenden Treffer und Urteil. Unklare Rückmeldungen sperren erneutes Schreiben bis zum Lesen. Der Merkliste-Direktlink überschreibt keine gespeicherten Normalfilter. Die nachfolgende Serverkorrektur aus Nachricht 215 ist in App 0.15.1 berücksichtigt: Schlafzimmer/Egal hebt die Vorgabe auf, explizites Balkon/Egal bleibt im Profil erhalten, zusätzliche Nachweise werden angezeigt und die gemeinsame Merkliste nutzt den erweiterten vorhandenen Leseendpunkt.

## Offline und Anmeldung

Der Service Worker speichert nur die ausdrücklich aufgeführten App-Dateien. Der Cache ist an den Installationspfad gebunden; andere Anwendungen behalten ihre Caches. Skript und Stylesheet tragen die App-Version in ihrer URL, damit ein Browser beim Update keine alten Dateien mit der neuen Oberfläche mischt. Die Offline-Hülle verwendet dieselben URLs; Netzwerkabrufe validieren den HTTP-Cache. API-Antworten und beliebige Dateien derselben Domain werden nicht zwischengespeichert. Offline steht die App-Hülle zur Verfügung, Suche und Ergebnisse benötigen eine Verbindung. Die Markdown-Bibliothek ist optional und wird nicht offline gespeichert.

Zur Installation die Seite in Safari/Chrome öffnen und „Zum Home-Bildschirm“ wählen. Die Anmeldung wird durch die bestehende app-api verwaltet.

## Tests und Prüfstand

Stand 0.15.2 (Nachricht 220): Die Viertelansicht zeigt `letzter_lauf.ki.fehler` als Klartextwarnung, auch wenn die Umgebungsdaten bereits fertig geladen sind. Vorhandene Viertel bleiben sichtbar; keine automatische kostenpflichtige Wiederholung. Ein neuer Browsertest prüft Anzeige, sichere Textdarstellung, erhaltene Viertel und das Entfernen einer nicht mehr gelieferten Fehlermeldung.

Aktueller Lauf: 68 von 70 Tests bestanden. Die beiden echten Netzwerk-/Service-Worker-Tests konnten wegen `ERR_NETWORK_ACCESS_DENIED` auf localhost nicht ausgeführt werden. Der frühere 69/69-Stand gilt für 0.15.1 und ersetzt diese erneute Prüfung nicht. Syntax und Diff geprüft. Für isolierte Darstellungstests kann `PW_TEST_OFFLINE_ASSETS=1` App-Dateien direkt als Testantwort bereitstellen; dies prüft ausdrücklich keinen HTTP-Cache und keinen Service Worker. `PW_TEST_EXECUTABLE` erlaubt die Auswahl eines vorhandenen Testbrowsers. Dieser Lauf nutzte Playwright 1.57.0 aus der vorhandenen Laufzeit mit Chromium-Build 1234; die Projektabhängigkeit bleibt 1.62.1. Vor Veröffentlichung die beiden Netzwerktests und Gegenprüfung nachholen.

Voraussetzung: Node.js >= 20.

```sh
npm ci
npx playwright install chromium
npm test
```

**69 Browsertests** prüfen Formular/API-Reihenfolge, Doppelklick, Warteschlange/Bewertung, Abbruch, Fehler/401, unvollständige Antworten, Navigation, Ranking, Sortierung/Filter/Seiten, Rückmeldungen und persönliche Auswahl samt überlappender Lese-/Schreibvorgänge, Fotos/Referrer/Platzhalter, Kartenfilter/Ausschlüsse/Nullkoordinaten/Listensprung, gespeicherte Filter, Lückenfüller-Auswahl/30er-Grenze/Doppelklick/Fehlerwiederherstellung/Kopieren/Status, Reisearten/Kriterien/Profilwechsel/Profil-Speicherung/Katalogfehler, vorläufige Ergebnisse/Polling, Abdeckung/Preisnachweise, Kandidatendialog/Fokus, Schnell-Gründe und Verlauf, globale Merkliste mit älteren Reisen/Lesefehlern/Treffersprung, Schlafzimmer-Standards und Profil-Rundlauf, Viertel/Karte/Ortswechsel/Entscheidungen/Ermittlung und deren Fehlerfälle, Markdown/Links, mobile und Tablet-Breiten, Tastaturbedienung sowie Offline-Hülle/Cache-Isolation und das Update mit bereits gefülltem HTTP-Cache. Die Tests verwenden synthetische Antworten und starten keine echte Suche, Auswahländerung oder Rückmeldung. Fotos und Kartenkacheln werden in den Tests simuliert, ohne externe Kartendienste abzufragen. Screenshots liegen ignoriert in `test-results/`.

Am 16.10.2026 wurden Suchlauf #2 und der Rückmeldungsbericht über den vorhandenen Lesezugang geprüft; ihre Daten werden nicht eingecheckt. Claudes Kyoto-Lauf #5 wurde durch diese UI-Arbeiten nicht gestartet, gestoppt oder verändert.

Claude hat die Schnittstellen in Werkstatt-Nachricht 165 geprüft und die App nach der Pflichtkorrektur `route` als freigabefähig bewertet. Die Korrektur ist in 0.10.1 enthalten. Sebastian hat am 16.10.2026 die Veröffentlichung von App 0.10.x ausdrücklich freigegeben. Der anschließende angemeldete Browser-Live-Test mit dem vorhandenen Suchauftrag #5 wird mit dem Veröffentlichungsstand in Wunsch 41 dokumentiert. Die automatisierten Browserprüfungen ersetzen diese Abnahme nicht.

## Zusammenarbeit

Werkstatt-Wunsch 41: App-Verantwortung bei ChatGPT, Backend bei Claude. Vor Änderungen `app:repo` sperren, vorhandenen Featurestand prüfen, danach Änderungen protokollieren und die Sperre freigeben. Größere Änderungen gehen zur Gegenprüfung; Sebastian entscheidet über Veröffentlichung.

Der Ausbau 0.11.0 gehört zu Wunsch 50 (Fotos/Karte) und Wunsch 33 (Filter/Auswahl). Die für 0.10.x erteilte Veröffentlichungserlaubnis ersetzt nicht die Abnahme dieses Ausbaus. Ausbau 0.12.0 ergänzt Wunsch 51 (Lückenfüller) in einem eigenen Folge-PR. Ausbau 0.13.0 ergänzt Wunsch 54 (erweiterte Suche/Suchprofile); 0.14.1 ergänzt Wunsch 57 (Konzept-Abgleich und Fokuskorrektur). Ausbau 0.15.1 ergänzt Wunsch 61, die App-Korrekturen aus Gegenprüfung 211 und die Anbindung der Serverkorrektur 215 einschließlich gemeinsamer Merkliste (Wunsch 62).


### Kyoto-Abgleich (App 0.10.1)

Historischer Stand vor Claudes Budgetkorrektur aus Nachricht 170. Aktuell nach der Korrektur: A16, B23, unbewertet48, ausgeschlossen26. Der neue Lesevertrag liefert 113 Fotos und 34 Stationen. Die App-Arbeiten haben diese Daten nicht verändert.

Werkstatt-Nachricht 162 und Suchlauf #5 wurden lesend abgeglichen: 143 gesammelt, 30 Doppel zusammengeführt, 113 verbleibend (A16, B26, noch nicht vollständig bewertet65, ausgeschlossen6). 15 Fußwege tragen `route`, 92 `geschaetzt`. Die Anzeige wurde lokal mit der gelesenen Antwort bei 390/768/1366 Pixeln nachgespielt; dabei wurden ausschließlich Leseaktionen simuliert. Dieser Darstellungstest ist kein angemeldeter End-to-End-Test gegen app-api. Echte Daten bleiben außerhalb der eingecheckten Testfixtures.

### 0.17.0 · Wunsch 71 (Nachricht 241)

- Ergebnisansichten Liste, Tabelle und Tinder. Ansicht und bis zu sechs Anzeige-Infos werden gerätebezogen in `localStorage` gespeichert (`ks_result_view`, `ks_anzeige`); Speicherfehler lassen die UI bedienbar. Auswahl/Reihenfolge und Reset unter „Anzeige“; Pfeile ergänzen Ziehen für Touch/Tastatur.
- Gleiche Infofelder in allen Ansichten. Unbekannte Angaben bleiben `–`; Zimmerangaben stammen ausschließlich aus der zugeordneten, widerspruchsfreien Angebotskategorie. `note_geeicht` ist Hauptnote und Grundlage für Sortierung/Filter; Original und Skala bleiben sichtbar. Fehlende Eichung wird nicht clientseitig erfunden.
- Tinder arbeitet neue Runden vor älteren ab und überspringt beurteilte/übernommene Treffer gemäß Nachricht 241. Knöpfe sowie Wischen rechts/links/hoch, getrennte Fotogalerie (max. zehn HTTPS-Links), optionale Gründe und Rückgängig. Rückkehr vom Anbieter zeigt „Und?“. Liste/Tabelle nutzen für Merken/Ausschließen dieselbe Urteils-API. Unklare Schreibantworten verlangen Aktualisieren; verspätete Leseantworten überschreiben keine neuen Urteile.
- Endrunde nur mit Favoriten: Ziehen oder Pfeile sowie Paarvergleich mittels Einfügesortierung. Speicherung erst auf „Rangfolge speichern“. Eigener Rang ist sichtbar und wird in der Merkliste bevorzugt.
- „Weitere suchen“ verlangt den Kostenhinweis zu bestätigen und startet `unterkunft_suche_starten` für den vorhandenen Auftrag. Nach Fertigstellung zählt die UI die Treffer der bestätigten Runde, zeigt „X neue Unterkünfte“ und öffnet bei neuen Treffern Tinder. Null neue zeigt den Hinweis auf ausgeschöpfte Filter.
- Die vorhandene Gehzeit ist eine Gehzeit **zur Station**; dies steht neben dem Wert. Es wird keine Gehzeit zum Stadtziel erfunden. Nicht gelieferte Raucher-/Stornodaten bleiben unbekannt.

Validierung: 84 Browsertests bestanden, ein optionaler Kyoto-Echtdaten-Test ohne Fixture übersprungen. Testbrowser: Chromium 153 über `PW_TEST_EXECUTABLE`; regulärer Playwright-Download in dieser Arbeitsumgebung fehlgeschlagen. Sämtliche Schreibtests verwenden synthetische Serverantworten, keine echten Suchläufe oder Urteile. Prüfung von physischem iPhone/Safari und angemeldeter Live-API steht aus. Version 0.17.0 / Cache v27 vorbereitet, **nicht veröffentlicht**. Die Gründe `zu_klein`, `laerm`, `ausstattung` wurden von Claude in Nachricht 251 serverseitig bestätigt.


### 0.18.0 · Integrierter PR9/PR10 (Nachricht 251)

PR10 bleibt die Basis und der gemeinsame Prüf-PR; Nachricht 241 hat Vorrang. Aus PR9 übernommen: sichtbare/filterbare/sortierbare Fläche, größere Fotos in der Liste, deutsche Bettbegriffe einschließlich Filter, lange Fußwege in Stunden/Minuten, Karten-Unterkunft unter dem Marker samt Tastaturauswahl und Nachbar-Markern, öffentlicher Rakuten-Hotelüberblick sowie Filter „Meine Entscheidung“. Die gerätebezogene Auswahl von höchstens sechs Infos bleibt in allen Ansichten maßgeblich.

Tinder überspringt bewertete Treffer einschließlich „Na ja“. Ausnahme: ein aktiver Treffer mit übernommenem Urteil und Preishinweis erscheint erneut als „Jetzt günstiger“. Bestätigte Entscheidungen entfernen ihn wieder aus der offenen Runde. Rückkehr vom Anbieter stellt eine Frage und speichert kein Urteil. Falsche Treffer-ID, Urteil oder Status sperren weitere Entscheidungen auch nach Ansichtswechsel bis zum erneuten Lesen. Die Endrunde fügt Favoriten im Paarvergleich per Halbierung ein.

Die drei zusätzlichen PR9-Browsertests wurden in die gemeinsame Suite übernommen und an den vorrangigen Vertrag aus Nachricht 241 angepasst (kein wiederholtes Na-ja am Rundenende, explizites Speichern optionaler Gründe, Tinder als dritte Ansicht). Zusätzliche Integrationstests prüfen Anbieter-Rückkehr, widersprüchlichen Status und zehn Favoriten im Paarvergleich. Version 0.18.0 / Service-Worker-Cache v28. Kein Merge oder Deploy; abschließende Prüfung durch Claude erforderlich.

Validierung des integrierten Standes: 89 Browsertests bestanden, 0 Fehler; ein optionaler Kyoto-Echtdaten-Test ohne Fixture übersprungen (90 insgesamt). Chromium 153 über `PW_TEST_EXECUTABLE=/tmp/w71-chromium npm test`. Mobile Darstellung und Tabellenabmessungen geprüft. Keine echten API-Schreibaktionen in den Tests.

### 0.18.1 · Tinder kompakter und ruhiger bedienen (Wunsch 73)

Die Bedienprobe mit langen Namen, sechs Angaben, mehreren Fotos und aufeinanderfolgenden Urteilen zeigte viel vorgelagerte Navigation sowie einen Gründe-Block, der die nächste Karte nach unten schob. Tinder nutzt jetzt einen kompakten Arbeitsbereich: Suchlauf-Aktionen im aufklappbaren Menü, sechs Infofelder in zwei Spalten, Bildnavigation über dem Foto und feste Entscheidungsknöpfe außerhalb des scrollbaren Karteninhalts. Auf dem Desktop stehen Foto und Infos nebeneinander. Details bleiben erreichbar; der Gesamtpreis nennt die Zahl der Nächte. Noten-Eichung und Stationsname werden kurz angezeigt, ausführliche Nachweise stehen in Details.

Gründe öffnen sich nach einem Urteil nur auf „Gründe ergänzen“ in einem Dialog; Chips ändern nur den Entwurf, gespeichert wird ausdrücklich. Karte und gewähltes Foto bleiben bei Gründe-Bearbeitung erhalten. Links=Weg, rechts=Favorit; vertikales Touch-Scrollen löst kein Na-ja-Urteil aus (der Na-ja-Knopf bleibt). Rückgängig und Fehlersperre bleiben erhalten, unklare Antworten bieten direkt Aktualisieren an. Kein echtes Urteil wurde für die Bedienprobe gespeichert.

Prüfung: automatisierte Browser-Bedienprobe mit synthetischen Unterkünften; Screenshots vor/nach Änderung, Breiten 320/375/390/430 und Desktop1440. Prüfungen auf unveränderte Kartenposition nach Urteil, sichtbare mindestens44px-Entscheidungsknöpfe, Gründe-Entwurf/Speichern, Fotopersistenz, vertikale Touch-Geste ohne Urteil und Fokus-Rückkehr aus Details. Der separate interaktive Cloud-Browser konnte den lokalen Prüfserver nicht erreichen; die Live-App war dort nicht angemeldet. Deshalb keine Behauptung eines angemeldeten Live-Anwendertests. Version0.18.1/Cachev29 zur Gegenprüfung; Veröffentlichung separat.

Validierung: vollständige Suite 90 bestanden / 0 Fehler / 1 optionaler Kyoto-Test ohne Fixture übersprungen (91 insgesamt), Chromium153. Abschließende Layout-Bedienprobe nach Desktop-Höhenbegrenzung ebenfalls bestanden.
