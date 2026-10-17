# Wunsch 88 · Aufenthaltsfotos und Reiseverlauf

Eigener PR nach PR14-Veröffentlichung, App 0.21.0 / Cache v33. Serververtrag aus Werkstatt 342 (app-api 0.15.0).

- Je Aufenthalt maximal drei eigene Fotos, Vorschaubilder, Großansicht und Löschen mit ausdrücklicher Rückfrage.
- Browser dekodiert das Original; Canvas erzeugt JPEG mit Qualität 0,82 und längster Seite höchstens 1600 Pixel. Grenze 3 MB nach Umwandlung. Bei nicht unterstütztem HEIC verständlicher Hinweis auf JPEG/PNG; kein universeller HEIC-Decoder behauptet.
- Kurzlebige HTTPS-Bildlinks nur im Arbeitsspeicher. Kein LocalStorage/IndexedDB oder Service-Worker-Cache für Fotos. Bildfehler stößt höchstens eine automatische Neulesung an; manuelles Neulesen bleibt möglich.
- Unklare Upload-/Löschantwort sperrt weitere Änderungen bis zum Neulesen. Keine automatische Wiederholung eines Uploads.
- Vergangene Aufenthalte (Abreise vor lokalem heutigen Kalenderdatum) standardmäßig unter „Bisherige Aufenthalte (n)“ eingeklappt. Deren Fotos werden erst beim Öffnen gelesen. Aktuelle/künftige bleiben oben; vergangene Vorschläge wandern ebenfalls in den Verlauf.
- Leerer EUR-Preis mit vorhandener Buchungsnotiz: „Preis siehe Notiz“, Notiz aufklappbar. Keine erfundenen Euro-Umrechnungen.

Browserprüfungen mit synthetischen Daten: Verlauf, Notizpreis, Bildverkleinerung (2400×1200 → 1600×800 JPEG), Dreiergrenze, Großansicht, Abbruch/Bestätigung beim Löschen, abgelaufener Link, verlorene Uploadantwort und lesende Wiederaufnahme. Kein persönliches Foto hochgeladen oder gelöscht. iPhone-HEIC-Dekodierung ist vom Browser abhängig und noch nicht auf einem physischen Gerät geprüft.

Screenshots: `previews/w88-fotos-mobile.png`, `previews/w88-vergangene-mobile.png` (synthetische Testbilder).
