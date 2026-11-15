# Postfach inhalte-nachbau (Runde 5: Nachbau der drei alten Entwürfe)

Neueste Meldung oben.

## 2026-11-15 13:30 – FERTIG
Alle drei alten Entwürfe nach dem Bausatz neu gebaut (Zweig inhalte-nachbau, ein Commit je Thema, kein Eingriff in fremde Dateien, keine DB/App).

| Thema | Kl. | Lernkarten | Aufgaben | Bilder | Generator |
|---|---|---|---|---|---|
| gleichungen.einfach | 5 | 7 (ohne_loesung = Vertiefung) | 189 | Waage (figur), Rechenkette (tabelle) | gleichungen_einfach.py |
| groessen.indirekt | 8 | 7 | 189 | Wertetabellen, Hyperbeln, Hyperbel vs. Ursprungsgerade | groessen_indirekt.py |
| gleichungen.linear | 7 | 6 | 162 | Waage, Rechteck zum Distributivgesetz | gleichungen_linear.py |

Je Lernkarte 27 Aufgaben (5/7/5 Übungen, 1 Test, 3 Korrektur, 6 Sicherung), Dubletten themenweit ausgeschlossen. Hilfsdatei: inhalte/generatoren/_nachbau.py (nutzt _bausatz.py nur lesend).
Geprüft: Prüfskript OK für alle drei; jede Zahl-Aufgabe beim Bauen mit dem Prüfrechner nachgerechnet; zusätzlich alle „Löse …“-Gleichungen durch Einsetzen der Lösung geprüft (einfach 90, linear 62 + Bruchlösungen); je Lernkarte die Aufgaben gelesen, danach Sprache, Plausibilität (Preise, Mengen, Anzahl Bagger/Busse) und Ablenker nachgebessert.

Umgesetzt laut Auftrag: Waage-Modell, Umkehraufgabe, Probe, Textaufgaben, „keine Lösung in ℕ“ (Kl. 5); Erkennen, Produktgleichheit, Dreisatz, Hyperbel, Abgrenzung direkt/indirekt/weder noch (Kl. 8); Äquivalenzumformungen, Klammern, x auf beiden Seiten, Probe, Sonderfälle, Sachaufgaben (Kl. 7). Verstehen-Karten: probe (Kl. 5 und 7), unterscheiden (Kl. 8).

Offene Punkte / Annahmen (stehen auch unter „offen“ in den Dateien):
- lehrplan_gym ist bei allen drei leer; gebaut nach „umfang“ und Auftragstext.
- gleichungen.einfach/ohne_loesung nutzt negative Zahlen (zahlen.ganz) – Reihenfolge im Lehrplan: nach zahlen.ganz.
- Die Waage ist eine schematische Figur (Balken, Drehpunkt, beschriftete Schalen). App-Wunsch (niedrig): eigener Bildtyp „waage“ mit Gewichtssymbolen/Dosen statt Termen auf den Schalen.
- Die alten Datenbank-Fassungen (12 Aufgaben je Karte) werden durch diese Dateien ersetzt; Lernziel-Schlüssel können sich von den alten unterscheiden – beim Einspielen Lernstand-Zuordnung prüfen.

## 2026-11-15 13:20 – STATUS
gleichungen.linear fertig: 6 Lernkarten (waage, beide_seiten, klammern, probe, sonderfaelle, sach), 162 Aufgaben, Prüfskript OK, alle Zahl-Aufgaben über „c“ nachgerechnet, zusätzlich 62 Gleichungen und alle Bruchlösungen (□/□) durch Einsetzen geprüft. Waage-Bild bei Äquivalenzumformung und „x auf beiden Seiten“, Rechteck-Bild für das Auflösen der Klammer.

## 2026-11-15 12:30 – STATUS
groessen.indirekt fertig: 7 Lernkarten (erkennen, vervielfachen, produkt, dreisatz, graph, unterscheiden, sach), 189 Aufgaben, Prüfskript OK, alle Zahl-Aufgaben über „c“ nachgerechnet. Wertetabellen als Bild (tabelle), Hyperbeln als Koordinatensystem (auch Hyperbel neben Ursprungsgerade und zwei Hyperbeln zum Vergleich). Sachgrößen auf realistische Bereiche begrenzt (z. B. höchstens 60 Kinder pro Bus, höchstens 6 Bagger). Weiter mit gleichungen.linear.

## 2026-11-15 11:40 – STATUS
gleichungen.einfach fertig: 7 Lernkarten (waage, umkehr_plus, umkehr_mal, zwei_schritte, probe, aufstellen, ohne_loesung als Vertiefung), 189 Aufgaben, Prüfskript OK, alle Zahl-Aufgaben über „c“ nachgerechnet, zusätzlich 90 Gleichungen durch Einsetzen der Lösung geprüft. Waage als Figur gezeichnet, Rechenkette als Tabelle.
Generator: inhalte/generatoren/gleichungen_einfach.py (Hilfsdatei _nachbau.py). Weiter mit groessen.indirekt.
