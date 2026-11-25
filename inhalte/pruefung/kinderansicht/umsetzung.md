# Kinderansicht und Stand über Schularten – Umsetzung (Stand 2026-11-16, nach des Nutzers Auswahl)

Grundlage: `bericht.md` (Befunde B1–B14, Auswahl Abschnitt 7 und 7.1) und die klickbaren Entwürfe:
- „Aufbau der Kinderansicht“
- „Wo stehe ich? – kombinierter Entwurf“

Ersetzt die frühere Fassung dieser Datei. Alles im Zweig `lernen-app`, kein Merge nach `main` ohne des Nutzers „Live“.

## Entschieden

| Thema | Entscheidung |
|---|---|
| Navigation | Menü ≡ bleibt. Einträge: Abflugtafel · Mein Weg · Merkheft · Reisepass. Die Weltkarte zieht in „Mein Weg“ um. |
| Startseite (Abflugtafel) | bleibt; oben neu: **drei Mini-Linien** GYM · RS · IB MYP (Klasse, Balken, gelandet/gesamt). Antippen öffnet „Mein Weg · Stand“. |
| Mein Weg | drei Reiter: **Stand** (Start) · **Kontinente** · **Karte** |
| Stand (Kind) | 3 Ebenen: Mini-Linien + Linienplan → Haltestelle = Bordkarte der Klasse mit Fortschritt je Kontinent (‹ › blättert) → Kontinent = Flüge mit „zählt auch für …“. Oben ein Pfad zurück. |
| Kontinente | je Kontinent eine Karte mit eigenem Fortschritt, aufklappbar zu den Flügen (Entwurf „Mein Weg“ B) |
| Karte | Weltkarte nur mit den Orten der eigenen Klasse, mit Route; Antarktis als Polarkarte von oben |
| Stempel | **Ort = eine Klasse**, Stempel je Ort; dafür 13 Orte neu zuordnen (Daten, mit Freigabe) |
| Merkheft | nur Geschafftes; Kontinent → Flug → Etappe; Suche oben |
| Wörter (Kindertexte) | **Reisewörter durchgehend:** Flug = Thema · Etappe = Lernkarte · Bordkarte = Aufgabe · Kontinent = Gebiet · Ort |
| Frühere/höhere Klassen | bleibt wie heute (noch unentschieden), aber der Fehler B4 wird behoben |
| Rückreise | eigene Karte „Kurz zurück nach …“ mit Grund und „danach geht es weiter mit …“ |
| Eltern/Lehrer | 3 Ebenen: beide Kinder × drei Schularten → Lehrplan-Landkarte (Kontinente × Klassen) mit Schalter „Einstieg prüfen: Kl. X“ (Klassen ab X ausgegraut, Ampel, Liste „fehlt“) → Feld = Flüge mit Stand der Etappen |

## Rechenregel „Stand“

- Für Schulart `s` (gym_by, rs_by, ib_myp) und Klasse `k` zählen alle Themen mit `jahrgang[s] = k` (heute schon in `schule_uebersicht.einheiten[].jahrgang`).
- **Gelandet:** Ein Thema gilt als gelandet, wenn alle Pflicht-Lernkarten fertig sind (`fertig >= pflicht_anzahl`).
- **Läuft:** mindestens eine Lernkarte ist fertig, aber nicht alle.
- **Wackelt:** `fehler > 0` oder Rückreise offen.
- **Eigene Stufe je Schulart:** kommt aus dem Kind (`klasse`, `schulart`). Für die zwei anderen Schularten braucht es ein neues Feld je Kind (`stufen: {gym_by, rs_by, ib_myp}`), das Eltern im Plan setzen. Vorschlag: Standard = gleiche Klasse; für IB MYP gilt Klasse − 4.
- **Einstiegs-Check Klasse X:** Anteil gelandeter Themen mit `jahrgang[s] < X`. Ampel: grün ab 90 %, gelb ab 70 %, sonst rot. Hinweis immer dazu: „Orientierung, keine Einstufung durch eine Schule“.

## Pakete

| Paket | Inhalt | Fertig, wenn … |
|---|---|---|
| **K1 Fehler** | U1 Stempel-Band richtig zählen · U2 Flugname statt Ortsname in Mein Weg/Merkheft · U3 „Kommt noch“ wie die Abflugtafel einteilen · U4 Menü im Reisepass markieren · U5 nur eigene Schulart im Flug-Kopf · U8 Rückreise-Karte · Reisewörter in allen Kindertexten | `rundgang.test.cjs` (dieser Ordner): kein Ortsname doppelt in Mein Weg; „Kommt noch“ bei Klasse 8 ohne Klasse 5–7; Rom-Band = alle Etappen aller Flüge des Ortes; „Etappe/Bordkarte/Flug/Kontinent“ einheitlich, kein „Lernkarte“, „Aufgabe“ oder „Gebiet“ in Kinderansichten. |
| **K2 Mein Weg** | Reiter Stand · Kontinente · Karte; Weltkarte aus dem Menü in „Mein Weg“; Karte nur eigene Klasse, Antarktis von oben; Merkheft nur Geschafftes (Kontinent → Flug → Etappe) | Menü hat 4 Einträge; Weltkarte zeigt nur Orte der eigenen Klasse; Merkheft ohne „noch nicht geübt“. |
| **K3 Stand** | Mini-Linien auf der Abflugtafel; „Stand“ mit 3 Ebenen wie im Entwurf; Feld `stufen` je Kind (Datenbank, Werkstatt-Regeln) | Ansicht entspricht dem Entwurf „Wo stehe ich? – kombiniert“; Zahlen stimmen mit der Rechenregel. |
| **K4 Eltern** | Eltern/Lehrer-Ansicht mit 3 Ebenen und Einstiegs-Check (ergänzt „Was wackelt?“, das in Ebene 3 verlinkt wird) | wie Entwurf; Einstiegs-Check mit Hinweis „Orientierung“. |
| **K5 Daten** (erst nach D1 im Gesamtauftrag) | 13 Orte so neu zuordnen, dass jeder Ort eine Klasse hat; Reihenfolge der Flüge im Ort nach Lehrplan | Liste mit Vorschlag an der Nutzer, nach Freigabe eine Migration. |
