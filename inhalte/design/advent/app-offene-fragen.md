# Advent – App-Teil: offene Fragen und Hinweise (Stand 28.11.2026, Zweig `helfer-advent-app`)

Gebaut gegen `server.md` (ADVENT-S). Nichts eingespielt, nichts live, Version nicht erhöht.

## Offene Fragen an die Server-Schnittstelle (nicht geraten)

1. **Krampus-Tür vorher erkennbar?** `schule_advent_stand` liefert für geschlossene Türen nur `nr` und `zustand` (richtig so, Inhalte verlassen den Server nicht). Die dunkle Krampus-Tür des Entwurfs lässt sich deshalb erst **beim Öffnen** zeigen: Die App tauscht die grüne Tür gegen die dunkle, sobald `oeffnen` `art: krampus` meldet, dann geht sie auf. Soll die Tür vorher dunkel sein, bräuchte `stand` ein Kennzeichen (z. B. `dunkel: true`) für die Tür `naechste_nr`.
2. **Tauschkarte bei `advent_tausch = 0`:** Der Server verbietet `einloesen` für die Tauschkarte („wird beim Tauschen verbraucht“). Die App zeigt sie bei Tausch aus wie einen Gutschein (Titel/Text der Eltern), aber **ohne** „Eingelöst“-Knopf, mit „Zeig ihn Mama oder Papa.“; die Eltern können sie ausschalten. Gewünscht? Sonst bräuchte der Server eine Einlöse-Erlaubnis bei Tausch aus.
3. **„Meine Gutscheine“ nach dem 6.1.:** Der Server meldet `menue.gutscheine` auch nach dem Ende, solange etwas offen ist. Der Auftrag verlangt außerhalb 1.12.–6.1. keinen Advent-Abruf – deshalb gibt es nach dem 6.1. **keinen Menüeintrag** mehr. Die Seite `#/gutscheine/<kind>` funktioniert weiter, wenn man sie direkt öffnet (dann ein Abruf). Soll der Menüeintrag länger bleiben (z. B. bis 31.1.), reicht eine Änderung von `LERN_ADVENT.bis` in `lernen.js` – dann aber auch Karte und Stand-Abruf bis dahin.
4. **Gerätedatum vs. Lernort-Tag:** Das App-Fenster richtet sich nach dem Gerätedatum, der Server nach der Lernort-Zeitzone. In der Nacht des 30.11./1.12. bzw. 6./7.1. kann es eine Stunde lang auseinanderlaufen (Server sagt `vor_start`/`vorbei`); die App zeigt dann nichts aus dem Kalender, nur die Kartenebene.
5. **`letzte_nr` bei `keine_etappe`/`limit`:** Die App zeigt diese Tür mit `tuer_lesen` als „Schon offen – auf einem anderen Gerät“. Bitte bestätigen, dass `letzte_nr` immer eine heute geöffnete Tür meint.
6. **Eltern-Seite außerhalb des Fensters:** Der Link in „Verwalten“ steht nur vom 1.12. bis 6.1. Die Seite `#/adventeltern` geht immer (z. B. zum Prüfen vor dem Start). Früher verlinken (ab 15.11.)?
7. **Tausch-Regel** ist laut Auftrag noch offen: Die Kind-Bedienung erscheint nur bei `tausch.aktiv` (Server) und `LERN_ADVENT.tausch` (App, ein Schalter in `lernen.js`), wählt je einen eigenen und einen fremden offenen Gutschein und schickt `schule_advent_tauschen` mit `client_id`.

## Hinweise zum Einbau

- Routen: `#/advent/<kind>` (Kalender, `-oeffnen` öffnet die bereite Tür direkt), `#/gutscheine/<kind>`, `#/adventeltern` (Eltern). In `app.js` und `lernen/schule.js`; Kinder kommen nicht auf `adventeltern`.
- Nachgeladen werden `lernen-advent.js` und `lernen-advent.css` mit dem `?v=` von `lernen.js` (beide in `HUELLE` von `sw.js`, Release-Regel unverändert: beim nächsten Release mit umstellen).
- `lernCall`: `schule_advent_stand|gutscheine|eltern|protokoll` gelten als Lese-Aktionen (vergessen nichts).
- Jugendwort-Sticker: neue Anlässe `advent`, `advent_niete`, `advent_krampus` (J60–J68) in `daten/jugendwoerter.json` und der Vorgabe-Kopie `inhalte/pruefung/kind/jugendwoerter/woerter.json` (beide gleich).
