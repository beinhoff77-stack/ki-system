# Postfach designer (Designer, Chat des Nutzers)

Neueste oben.

## 2026-11-25 02:00 – FERTIG: Bestandsaufnahme

Zweig `designer`, ausgehend von `lernen-app` 4351182 (App 0.93.4). Vorgaben gelesen auf `pruefung-kinderansicht` ab6a9fb. Kein App-Code, keine Datenbank, keine Namen, nichts Neues entworfen.

**Geliefert**
- `inhalte/design/bestandsaufnahme.md`: Stand der Vorgaben, eigene Befunde mit Messwerten, drei Vorschläge.
- `inhalte/design/bestandsaufnahme/bilder/`: 15 Bilder aus einem eigenen Rundgang (als Kind angemeldet, Testdaten der Suite; 400, 820, 1280 px, hell und dunkel; Übung zusätzlich 390 × 664).
- Kern:
  - Alle Vorgaben des Vorgängers sind gebaut, außer FX (nichts im Code) und den Kann-Punkten K1, K3, K5, K8 der Prüfung KJ.
  - Übung: Bei 390 × 664 und 360 × 640 px ist beim Öffnen keine Aufgabe zu sehen (Bordkarte ab 386 px, Tastenfeld ab 385 bzw. 361 px). Bei 400 × 860 sind die Antwortfelder im unteren Drittel und „Tipp“ ganz verdeckt. Bei 1280 × 800 liegt „Prüfen“ unter dem Fensterrand.
  - Nachts wird die Etappen-Kachel unter dem Zeiger hell mit weißer Schrift; der Chip „Expedition wartet“ bleibt hell. Tablet: Schrift im Landungs-Blatt 11–14 px.
- Vorschlag nach Wirkung je Aufwand: 1. Übungs-Bildschirm „Aufgabe zuerst“ · 2. Aufräum-Paket Lesbarkeit · 3. FX erste Stufe (Motor, Legendary Drop, Respawn, Dezember-Saison).

**Offen**
- Entscheidung des Nutzers, was ich zuerst entwerfe.
- FX: Freigabe („warten“ vom 24.11.); Server-Felder für „Etappe sicher“ und „wieder offen“; Prüfliste ohne Muss / Soll / Kann.
- Im Auftrag steht FX „Fassung 2“, im Repo liegt Fassung 4 vom 24.11. Gelesen habe ich Fassung 4.

**Nicht geprüft**
- Echte Geräte, echter Server, echte Daten; Bewegung und Ton.
- Welt- und Land-Ebene der Karte, Expedition, Check-in, „abgelegt“, Flug geschafft, Flug-Test, Knobel: nur Code, Meldungen und Vorschau-Bilder.
- Lehrer- und Eltern-Ansichten (K6), 360 px außer der Übung (K7).

**Annahmen**
- Kinder melden sich mit eigenem Lern-Code an und sehen „Ändern lassen“ nicht (`ctx.leitung`).
- 390 × 664 steht für ein Handy im Browser mit Leisten; die Geräte der Kinder kenne ich nicht.
- Werkstatt-Regeln W1–W7 nicht im Council nachgelesen: nur eigene Dateien auf eigenem Zweig.

**App-Wunsch (für später, nicht Teil dieser Meldung):** keiner. Die Befunde aus 3.1 und 3.2 der Bestandsaufnahme kommen als Vorgabe, sobald der Nutzer die Reihenfolge festlegt.
