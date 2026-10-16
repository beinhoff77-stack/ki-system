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

## Unterkunftssuche (Werkstatt #41, App 0.5.0)

Navigation „Unterkunft“ (`#/suche`): Reisedaten eingeben, anlegen und starten.
Die bestehende Anmeldung wird verwendet; keine Schlüssel im Frontend ergänzen.
Alle Aufrufe gehen als `{aktion, daten}` an `POST /app-api/aktion`:

1. `unterkunft_suchauftrag_anlegen` liefert die Auftrags-ID.
2. `unterkunft_suche_starten` startet nur nach Klick. Bei einem Fehler bleibt der gespeicherte Auftrag verlinkt.
3. `unterkunft_suchlauf_lesen` aktualisiert den geöffneten Lauf alle sieben Sekunden. Endstatus, Navigation oder Lesefehler beenden das Polling. „Aktualisieren“ liest erneut, ohne einen neuen Suchlauf zu starten.

Letzte Aufträge und Direktlinks (`#/suche/2`) erlauben das Wiederöffnen nach einem Neuladen. Ein Entwurf kann ausdrücklich gestartet werden. Nach unklarer Anlege-Antwort zuerst die letzten Aufträge prüfen, um Doppelanlagen zu vermeiden.

A/B sind vorläufige Listen aus der serverseitigen Vorprüfung. Ausgeschlossene Treffer stehen separat, Treffer ohne Zuordnung werden nicht automatisch A oder B zugeordnet. Score, Preis, Datenlage, Bewertungsanzahl, Entfernung und Name sind sortierbar; fehlende Zahlen bleiben immer hinten. Teilnoten erscheinen erst, wenn geliefert. Auf kleinen Bildschirmen werden Tabellenzeilen als Karten dargestellt. Rakuten-Schätzpreise und Quellenhinweis sind sichtbar, unbekannte Warncodes bleiben erhalten.

### Tests

Voraussetzung: Node.js >= 20.

```sh
npm ci
npx playwright install chromium
npm test
```

Die Browsertests verwenden ausschließlich synthetische API-Antworten und starten keine kostenpflichtige Suche. Sie prüfen Formularvalidierung, Doppelklick, Anlegen/Starten/Lesen, Sortierung, XSS/Links, Polling-Ende, Navigation, Netzwerkfehler, 401, mobile Breite und Offline-Hülle. Screenshots liegen ignoriert unter `test-results/`.

Live geprüft am 16.10.2026: `/status` liefert app-api 0.5.0; alle drei Aktionen ohne Anmeldung liefern 401. Der authentifizierte Council-Lesezugang liefert Suchlauf #2 mit inzwischen 258 Treffern einschließlich Rakuten/Trivago. `luftlinie_ziel_m` fehlt in der gelesenen Antwort; die Oberfläche zeigt deshalb „unbekannt“. Keine Live-Daten sind als Testfixtures eingecheckt.

Noch vor Veröffentlichung prüfen: authentifizierter kompletter Browser-Durchlauf gegen app-api mit freigegebenem Suchbudget sowie Prüfung durch Claude in der Werkstatt. Featurezweig und Entwurfs-PR sind keine Freigabe für Merge oder Deploy.
