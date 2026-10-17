# Stufe 2 · Entdecker · 0.19.0

Wunsch 80, Serververtrag app-api 0.12.0 (Werkstatt 283/290), Freigabe von Sebastian am 17.10.2026. Eigenständiger PR auf der veröffentlichten Stufe 1 (0.18.2). **Dieser Stand darf erst nach Claudes Prüfung und Sebastians separater Freigabe gemergt oder veröffentlicht werden.**

## Verhalten und Gestaltung

Navigation Reisen / Entdecken / Favoriten. Neue Suchen benötigen eine Reise; bei gleicher Stadt wird bestehende Etappe oder getrennter Aufenthalt gewählt. Andere Tage entstehen als Suchvariante und werden nicht automatisch zum aktuellen Aufenthalt.

Reisen zeigt Etappen chronologisch, einschließlich vorgeschlagener, geplanter und gebuchter Aufenthalte. Lücken stammen aus der Serverantwort. Favoriten lassen sich in der Merkliste, im Suchergebnis und in der Etappe als bereits gebucht vermerken. Dies löst keine Buchung beim Anbieter aus. Kostenlose Stornierung wird ausschließlich mit konkretem Datum und Quelle zugesagt; Zeitangaben werden nicht erfunden.

Entdecker nutzt Petrol/Koralle, ein großes ausgewähltes Foto hinter der Durchsehen-Karte und eine stets erreichbare Entscheidungsleiste. Preis, Fläche und Schlafzimmer bleiben fest; bis zu vier zusätzliche Angaben werden pro Gerät gewählt. Liste/Tabelle behalten ihre getrennte Auswahl mit höchstens sechs Angaben. Warnungen bleiben sichtbar. Wischen über die Galerie blättert Fotos; horizontales Wischen im Bewertungsbereich entscheidet. Vertikales Scrollen, abgebrochene Gesten und Multitouch treffen kein Urteil. Alle Aktionen sind auch über Knöpfe erreichbar.

## Abnahmematrix

Die acht Abläufe aus Nachricht 289 plus Claudes drei Ergänzungen aus 291 sind durch Browserprüfungen mit synthetischen Serverantworten abgedeckt:

| Nr. | Ablauf | Nachweis in tests/search.test.cjs |
| --- | --- | --- |
| 1 | Vorschlag bestätigen/verwerfen; Lücken erst aus bestätigten Etappen | W80 Reiseübersicht; Bestätigen; Vorschlag verwerfen |
| 2 | Neue Tage: bestehende Etappe oder getrennter Aufenthalt; kein automatisches Aktivieren | W80 Jede neue Suche hat eine Reise |
| 3 | Aktive Variante mit Version ändern; Konflikt erhält Entwurf | W80 Bestätigen und Variantenwechsel |
| 4 | Alter Favorit bleibt sichtbar; frühere Preise getrennt, kein erfundener aktueller Preis | W80 Favorit ohne aktuelles Angebot |
| 5 | Echte Löschfolgen vor Bestätigung; laufende Suche verlangt Abbruch | W80 Löschen erst nach Folgenvorschau; Letzte Suche löschen |
| 6 | Verlorene Schreibantwort: keine blinde Wiederholung | W80 Löschen erst nach Folgenvorschau; neue Reise braucht bestätigte ID |
| 7 | Letzte Suche löschen lässt leere Etappe stehen | W80 Letzte Suche löschen |
| 8 | Wiederherstellen aktiviert keine Variante | W80 Papierkorb stellt wieder her |
| 9 | Reiseübersicht chronologisch mit geplant/gebucht je Etappe | W80 Reiseübersicht |
| 10 | Buchung aus Favorit; Storno nur mit belegtem Datum | W80 Favorit ohne aktuelles Angebot; Stornodatum |
| 11 | Jede neue Suche innerhalb einer Reise | W80 Jede neue Suche hat eine Reise |

Zusätzlich: persönliche Anzeige, Warnungen, Gestenabbruch/Multitouch, Zeitzonen, kleine Displays und bestehende Regressionstests für Suche, Council, Viertel, Zimmerzuordnung, Bewertungen, Endrunde und App-Cache.

## Screenshots

Browseraufnahmen aus der tatsächlichen Implementierung mit **synthetischen Testdaten**. Die Durchsehen-Aufnahme verwendet eine einfache Zimmerillustration als Fotoplatzhalter; sie ist kein echtes Unterkunftsangebot.

- [Reisen · Handy](previews/stufe2-reisen-mobile.png)
- [Reisen · Desktop](previews/stufe2-reisen-desktop.png)
- [Durchsehen · Handy](previews/stufe2-durchsehen-mobile.png)

## Bewusste Grenzen / Prüfung für Claude

- Bei einer bereits gebuchten Etappe ist der Wechsel auf andere aktive Suchdaten gesperrt: Der Server 0.12.0 übernimmt beim Variantenwechsel sonst neue Reisedaten, behält aber die alte Buchung. Die App darf eine Buchung nicht still auf andere Tage übertragen. Ein getrennter Aufenthalt ist möglich. Bitte den gewünschten späteren Umbuchungsablauf gemeinsam klären.
- Verwerfen eines unbestätigten Vorschlags ist laut Serververtrag keine Papierkorb-Aktion. Der Dialog verspricht deshalb weder Wiederherstellen noch 30 Tage; zugehörige Suchen bleiben erhalten.
- Die historischen Preise der allgemeinen Merkliste gehören weiterhin zum dort ausdrücklich datierten Suchlauf. Die Etappenansicht trennt aktive Angebote von früheren Preisen.
- Die Suite verwendet API-Mocks und schreibt keine echten Reisen, Buchungen oder Suchaufträge. Der optionale Kyoto-Test mit echten gelesenen Daten bleibt ohne lokale Eingabedatei übersprungen.
- Keine Preisüberwachung, externe Buchung oder weitere Serveränderung Bestandteil dieses PR.
