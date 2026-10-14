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
