# ki-system

Web- und Handy-Oberfläche (installierbare Web-App) für Sebastians persönliches KI-System.

- **Seite:** https://beinhoff77-stack.github.io/ki-system/
- **Daten und Logik:** liegen in Supabase (Schnittstelle `app-api`). Dieses Repository enthält nur den Oberflächen-Code – keine Daten, keine Schlüssel.
- **Zugang:** Passwort einmal je Gerät; die Sitzung bleibt 30 Tage (gleitend) gespeichert.
- **Installation am Handy:** Seite in Safari/Chrome öffnen → „Zum Home-Bildschirm“.

## Dateien

| Datei | Zweck |
|---|---|
| `index.html` | Grundgerüst, Login-Vorlage |
| `app.js` | Logik: Anmeldung, Aufträge, Ergebnis, Neuer Auftrag, Einstellungen, Werkstatt |
| `style.css` | Gestaltung (Rohbau; Feingestaltung folgt) |
| `manifest.webmanifest`, `sw.js`, `icon*.{svg,png}` | Web-App-Installation und Offline-Hülle |

## Zusammenarbeit (Werkstatt #4)

Claude baut den funktionierenden Rohbau, ChatGPT übernimmt die Gestaltung. Vor jeder Änderung: Sperre `app:repo` in der Werkstatt holen, aktuellen Stand von `main` laden, Änderung protokollieren, Sperre lösen. Gestaltung ändert keine Funktionsnamen und keine Schnittstellenaufrufe.

## App-Struktur und Unterkunftssuche (Werkstatt #41, App 0.8.0)

Startseite (`#/start`, auch Standard nach Anmeldung): zwei gleichwertige Bereiche **Council** und **Unterkunft**. Der globale Bereichswechsler bleibt auf allen angemeldeten Seiten erreichbar. Council behält seine Aufträge, Auftragserstellung, Einstellungen und Werkstatt. Unterkunft hat eine eigene Navigation **Suchen** (`#/suche`) und **Ergebnisse** (`#/ergebnisse`); Suchlauf-Direktlinks bleiben gültig.

Die Unterkunftsgestaltung übernimmt die Designbasis des Werkstatt-Prototyps V0.4.1: Creme (#f6f4ec), Waldgrün (#254d3e), Serifentitel, grüner Hero, nummerierte Formulargruppen, helle Panels und kompakte Vergleichstabelle. Die App enthält keine fiktiven Prototyp-Angebote. Noch nicht angebundene Prototyp-Funktionen (z. B. Merkliste, Landkarte, erweiterte Kriterien) werden nicht als funktionierende Live-Navigation dargestellt.

Unter „Suchen“: Reisedaten eingeben, anlegen und starten.
Die bestehende Anmeldung wird verwendet; keine Schlüssel im Frontend ergänzen.
Alle Aufrufe gehen als `{aktion, daten}` an `POST /app-api/aktion`:

1. `unterkunft_suchauftrag_anlegen` liefert die Auftrags-ID.
2. `unterkunft_suche_starten` startet nur nach Klick. Bei einem Fehler bleibt der gespeicherte Auftrag verlinkt.
3. `unterkunft_suche_status` aktualisiert den Fortschritt alle sieben Sekunden. Wartende Suchen starten serverseitig automatisch. Erst bei `fertig: true`, Fehler oder Abbruch lädt die App die Treffer über `unterkunft_suchlauf_lesen`. Navigation und Lesefehler beenden das Polling. „Aktualisieren“ liest erneut, ohne eine neue Suche zu starten.
4. „Suche abbrechen“ ruft einmal `unterkunft_suche_abbrechen` auf und liest anschließend den Status. Vorhandene Treffer bleiben lesbar; bei einem Fehler wird kein Schreibaufruf automatisch wiederholt.

Letzte Aufträge und Direktlinks (`#/suche/2`) erlauben das Wiederöffnen nach einem Neuladen. Ein Entwurf kann ausdrücklich gestartet werden. Nach unklarer Anlege-Antwort zuerst die letzten Aufträge prüfen, um Doppelanlagen zu vermeiden.

A/B folgen der serverseitigen Prüfung; bis zum Abschluss der Bewertungsstufe bleibt die Rangliste vorläufig. Ausgeschlossene Treffer stehen separat, Treffer ohne Zuordnung werden nicht automatisch A oder B zugeordnet. Score, Preis, Datenlage, Bewertungsanzahl, Entfernung und Name sind sortierbar; fehlende Zahlen bleiben immer hinten. Teilnoten erscheinen erst, wenn geliefert. Auf kleinen Bildschirmen werden Tabellenzeilen als Karten dargestellt. Rakuten-Schätzpreise und Quellenhinweis sind sichtbar, unbekannte Warncodes bleiben erhalten.

### Tests

Voraussetzung: Node.js >= 20.

```sh
npm ci
npx playwright install chromium
npm test
```

Die vierzehn Browsertests verwenden ausschließlich synthetische API-Antworten und starten keine kostenpflichtige Suche. Sie prüfen Formularvalidierung, Doppelklick, Anlegen/Starten/Lesen, Sortierung, XSS/Links, Polling-Ende, Navigation, Netzwerkfehler, 401, mobile Breite und Offline-Hülle sowie Startseite, getrennte Bereichsnavigation und Prototyp-Farben. Die Tabelle wird bei 1366 px ohne horizontalen Überlauf geprüft. Screenshots von Einstieg, Suche und Ergebnissen auf Desktop und Mobil liegen ignoriert unter `test-results/`.

Live geprüft am 16.10.2026: `/status` liefert app-api 0.5.0; alle drei Aktionen ohne Anmeldung liefern 401. Der authentifizierte Council-Lesezugang liefert Suchlauf #2 mit inzwischen 258 Treffern einschließlich Rakuten/Trivago. `luftlinie_ziel_m` fehlt in der gelesenen Antwort; die Oberfläche zeigt deshalb „unbekannt“. Keine Live-Daten sind als Testfixtures eingecheckt.

Noch vor Veröffentlichung prüfen: authentifizierter kompletter Browser-Durchlauf gegen app-api mit freigegebenem Suchbudget sowie Prüfung durch Claude in der Werkstatt. Featurezweig und Entwurfs-PR sind keine Freigabe für Merge oder Deploy.

### Endranking und Prüfungen (App 0.7.0)

Liste A startet in der vom Server gelieferten Rangfolge (`bewertung.rang`); der Score ersetzt diese Rangfolge nicht, weil die Top 10 eine Mischung der Unterkunftsarten berücksichtigen. Die Sortierschaltflächen erlauben weiterhin eigene Reihenfolgen. Die Score-Abdeckung stammt aus `spaltennoten.datenlage_score`; nur wenn dieses Feld fehlt, wird die ältere Datenlage verwendet. Null ist unbekannt, 0 bleibt eine gültige Note.

Die fünf Teilnoten Raum, Lage, Preis-Leistung, Bewertungen und Eignung erscheinen als Balken (0–10). Bildurteile werden ausdrücklich als KI-Einschätzung der Bilder dargestellt; Gegenprüfungseinwände einschließlich ihrer Liste bleiben außerhalb der aufklappbaren Details sichtbar. Die Ampel kennzeichnet Verlässlichkeit, nicht Qualität. Stationsname/Gehzeit werden verwendet, sobald die Leseschnittstelle sie liefert; fehlende Werte bleiben unbekannt.

Seit app-api 0.6.0 ist die leichte Statusabfrage maßgeblich: `status=fertig` und `fertig=true` kennzeichnen das Endranking. Fehler und Abbruch zeigen Teilergebnisse ausdrücklich vorläufig. Die frühere Wartefrist für fehlende Bewertungsschritte entfällt. 14 Browsertests decken zusätzlich Warteschlange → Bewertung → Abschluss ohne vorzeitiges Laden der Treffer, Abbrechen/Doppelklick, Abbruchfehler, ungültige Statusantwort und Entwurfsstart ab.

Die Live-Statusantwort von Suchlauf #2 wurde lesend geprüft. Ein angemeldeter vollständiger Browser-Live-Test und Claudes Prüfung bleiben vor Veröffentlichung offen. Rückmeldungen/Reports aus Wunsch 47 sind noch nicht integriert; der Backend-Baustein ist derzeit in Arbeit.
