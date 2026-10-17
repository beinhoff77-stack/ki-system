# Pakete B–D · Arbeitsstand 0.20.0

Sebastian hat A–D aus Werkstatt-Nachricht 315 freigegeben. Reihenfolge: A (PR13) veröffentlichen, danach B+C, danach D. Dieser Branch basiert auf dem korrigierten PR13. Kein Merge/Deploy dieses Branches ohne Sebastians weitere Live-Freigabe.

## B · Entscheiden und buchen

- Mitteilungs-Posteingang mit Zähler, sicheren internen Links, bestätigtem Gelesen-Status. Push nur nach bewusster Betätigung, Gerät abschaltbar, Testmeldung. iOS-Installationshinweis. Service Worker zeigt auch bei sichtbarer App und fehlerhaftem Payload eine Mitteilung; externe Klickziele werden verworfen.
- Favoriten-Einstieg führt zu Etappen. Je Etappe Favoriten / Na ja / Weg, Liste / Tabelle / Durchsehen, Sortierung, einzelne und gesammelte Statuswechsel. Sammelaktion nennt die tatsächliche Anzahl und verlangt Bestätigung. Rückgängig stellt vorherige Urteile und Gründe wieder her. Weg löscht nichts.
- Buchungsdialog zeigt Unterkunft, Zimmer, Gesamtpreis, Storno und Notiz zur Korrektur. Ein Vorschlag bzw. andere aktive Tage brauchen eine explizite Bestätigung im selben Speichervorgang. Kein automatisches Archivieren anderer Favoriten.
- „Keiner passt“ bietet neue Kriterien oder andere Tage als Variante. Technische Suchlaufdetails beanspruchen nicht mehr den gesamten Ergebniseinstieg.

## C · Suche auffrischen

- Anbindung an die gelesenen Definitionen von `unterkunft_auffrischen_vorschau`, `_starten`, `_lesen` und `auffrischen_json` (17.10.). Endgültige Server-Abnahme durch Claude noch erforderlich.
- Vorschau nennt Tage, Personen, Quellenfähigkeiten, Credits und zusätzliche USD-Kosten. Start mit Vorschauversion, Kostenlimit und festem Idempotenzschlüssel.
- Verlorene Startantwort wird über die bekannte Lauf-ID gelesen; kein automatischer kostenpflichtiger Wiederholungsaufruf. Bei erneutem ausdrücklichem Start bleibt der Schlüssel erhalten.
- Pfeile nur bei bestätigtem Angebot, bestätigter Vergleichbarkeit und zwei vorhandenen Preisen. Unbekannte/geänderte Bedingungen sowie nicht gefundene Angebote bekommen keinen irreführenden Preis-Pfeil. „Nicht gefunden“ wird nie als „ausgebucht“ bezeichnet.
- Neue Treffer werden anhand der vom Server gemeldeten Treffer-IDs markiert. Gerätebezogene NEU-Markierung nach Lesen des Auffrischungsergebnisses; bewertete Treffer verlieren die Markierung.

## D · Vergleichen

- Vergleich von 2–4 bewusst ausgewählten Unterkünften. Unterschiede und offene Angaben zuerst; gleiche Angaben optional einblendbar.
- Verschiedene Reisetage bleiben deutlich gewarnt; Preisvorteil-Aussagen werden dann nicht hervorgehoben.
- Karte ausschließlich der Auswahl. Fehlende Koordinaten werden als fehlend gezählt; keine geratenen Positionen.

## Tests und Grenzen

Browsertests decken Sammelbestätigung/Abbrechen/Rückgängig, Buchung mit expliziter Etappenbestätigung, Push-Opt-in und Ablehnung, Posteingang, verlorene Auffrischungsantwort, Vergleichbarkeit und Auswahlkarte ab. Service-Worker-Tests prüfen sichtbare Push-Meldungen und sichere Klickziele. Alle Tests verwenden synthetische Daten; keine persönlichen Unterkünfte oder kostenpflichtigen Suchen wurden verändert.

Echter Push-Empfang am iPhone ist erst nach Installation der veröffentlichten App und Opt-in prüfbar. Der Server versendet `push_test` derzeit an alle aktiven Geräte; die Oberfläche benennt das ausdrücklich. Screenshots unter `docs/previews` zeigen die echte App mit synthetischen Beispieldaten, keine gebuchten Angebote.

## Ergänzende Anwenderprobe

Kompletter Browserablauf: Favoriten → erneut durchsehen und behalten → Na ja und Rückgängig → zwei Unterkünfte vergleichen → Auswahlkarte → Weg und Rückgängig → Auffrischen → Buchung vermerken. Synthetische Daten, keine kostenpflichtigen Live-Suchen oder Änderungen persönlicher Buchungen.

Dabei behoben: ungenutzte Bildschirmhöhe beim erneuten Durchsehen, versehentlicher Text „null“ in Vergleich/Auffrischung und zu schmale Vergleichsspalten auf dem Handy. Die Vergleichstabelle lässt sich seitlich wischen. Screenshots: `previews/paket-b-durchsehen-mobile.png`, `previews/paket-d-vergleich-mobile.png`.
