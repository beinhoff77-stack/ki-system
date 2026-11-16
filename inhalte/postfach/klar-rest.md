# Postfach klar-rest (Runde 7b: Erklärungen verständlich machen – die letzten sechs Themen)

Teil A (ohne Generator): Überlagerung inhalte/klar/<thema>.json. Teil B (mit Generator): Abschnitt KLAR, eingesetzt erst nach dem Erzeugen der Aufgaben (inhalte/generatoren/_klar_rest.py). Neueste Meldung oben.

## 2026-11-16 02:18 – FERTIG – Abschlussbericht klar-rest (Runde 7b)
Alle sechs Themen haben jetzt verständliche Erklärungen (einstieg, woerter, schritte 3–5 mit Ergebnis in ⟦…⟧, regel als „So …“, fehler mit Zahlen und Bezug zur Situation).

| Thema | Teil | Datei | Karten | Prüfung |
|---|---|---|---|---|
| zahlen.natuerlich | A | inhalte/klar/zahlen.natuerlich.json | 12 | Prüfskript OK |
| terme.umformen | A | inhalte/klar/terme.umformen.json | 8 | Prüfskript OK |
| zahlen.teilbarkeit | A | inhalte/klar/zahlen.teilbarkeit.json | 8 | Prüfskript OK |
| finanzen.zinsen | A | inhalte/klar/finanzen.zinsen.json | 8 | Prüfskript OK |
| gleichungen.einfach | B | KLAR in gleichungen_einfach.py | 7 | 189 Aufgaben wörtlich gleich, inhalt_pruefen OK |
| groessen.indirekt | B | KLAR in groessen_indirekt.py | 7 | 189 Aufgaben wörtlich gleich, inhalt_pruefen OK |

Teil A: Prüfskript je Datei: gültiges JSON, genau die Lernziele aus quelle.md in derselben Reihenfolge, woerter als [Wort, Erklärung], 3–5 Schritte, einstieg ≥ 60 Zeichen mit ⟦…⟧, keine Verbotswörter in einstieg/schritte, Klammern ⟦⟧ paarig, Zahlformat (Leerzeichen als Tausendertrenner, − als Minus). Kein Feld bild; Beispielzahlen der Karten mit Bild beibehalten. Alle Zahlen und Proben nachgerechnet. fehler neu ergänzt, wo quelle.md keinen hatte (11 Karten).
Teil B: Neue Hilfsdatei inhalte/generatoren/_klar_rest.py – legt sich um baue() aus _nachbau.py, setzt KLAR erst nach dem Erzeugen der Aufgaben ein (Prüfung wie _klar_kl6.klar) und schreibt die Datei neu. Bilder unverändert.
inhalt_pruefen über alle Themen: OK.
Hinweis an den Haupt-Chat: Die Überlagerungen in inhalte/klar/*.json müssen beim Einspielen in die Datenbank noch über die bestehenden Lernkarten gelegt werden – ein Import dafür ist nicht Teil dieses Auftrags (Datenbank war verboten).
Nicht angefasst: Datenbank, Serverfunktionen, App-Code, Tests, inhalte/pruefung/, main. Merge offen – wartet auf Freigabe.

## 2026-11-16 02:18 – STATUS
groessen.indirekt fertig: Abschnitt KLAR im Generator groessen_indirekt.py (über _klar_rest.py), 7 Karten (einstieg, woerter neu; schritte 3–4, regel „So …“, fehler überarbeitet).
Situationen: Zimmer streichen, Futter für Pferde, Tippgemeinschaft teilt 120 €, Pumpen im Schwimmbecken, Etikett mit 12 cm², Taxi mit Grundgebühr, Urlaubsfahrt. Bilder (Tabellen, Hyperbel) unverändert.
inhalt_pruefen: OK. Vergleich gegen git show HEAD: 189 Aufgaben wörtlich gleich, übrige Datei gleich.

## 2026-11-16 02:17 – STATUS
gleichungen.einfach fertig: Abschnitt KLAR im Generator gleichungen_einfach.py, 7 Karten (einstieg, woerter neu; schritte 4, regel „So …“, fehler überarbeitet). Neue Hilfsdatei inhalte/generatoren/_klar_rest.py: legt sich um baue() aus _nachbau.py und setzt KLAR erst NACH dem Erzeugen der Aufgaben ein.
Situationen: Murmeln in der Dose auf der Waage, Geldbeutel, Hefte, Kino mit Popcorn, Probe der Freundin, Sammelkarten, Aufzug ins Untergeschoss. Bilder unverändert.
inhalt_pruefen: OK. Vergleich gegen git show HEAD: 189 Aufgaben wörtlich gleich, übrige Datei gleich.

## 2026-11-16 02:15 – STATUS
finanzen.zinsen fertig: inhalte/klar/finanzen.zinsen.json, alle 8 Lernziele (einstieg, woerter, schritte 3–4, regel „So …“, fehler; probe bei jahreszinsen, jahreszinsen_komma, zinssatz, kapital, monatszinsen).
Situationen: Omas Geld auf der Bank, Kredit/Sparkonto/Spardose, Tims, Leas, Opas und Jonas’ Sparbeträge. Beispielzahlen aus quelle.md beibehalten.
Neu ergänzte fehler: jahreszinsen, zinssatz, kapital, monatszinsen, zeitanteil. Prüfskript OK, alle Beträge nachgerechnet.

## 2026-11-16 02:14 – STATUS
zahlen.teilbarkeit fertig: inhalte/klar/zahlen.teilbarkeit.json, alle 8 Lernziele (einstieg, woerter, schritte 3–4, regel „So …“, fehler; probe bei primfaktoren).
Durchgehende Situation: Klassenfest – Muffins auf Teller verteilen (Teiler, Primzahl, ggT), Packungen beim Bäcker (Vielfache), Kasse in Münzen (Endziffer), Bonbons auf 3 Klassen (Quersumme), Lena und Tim laufen Runden (kgV). Beispielzahlen aus quelle.md beibehalten.
Neu ergänzte fehler: endziffer, ggt. Prüfskript OK, Zahlen nachgerechnet (u. a. 4 251 : 3 = 1 417).

## 2026-11-16 02:12 – STATUS
terme.umformen fertig: inhalte/klar/terme.umformen.json, alle 8 Lernziele (einstieg, woerter, schritte 4, regel „So …“, fehler; probe bei minusklammer, ausmultiplizieren, summe_mal_summe, ausklammern).
Durchgehende Situation: Einkauf mit Heften (x) und Stiften (y), Ausflugstüten (Ausmultiplizieren/Ausklammern), Beet/Garten (Produkte, Summe mal Summe, binomische Formeln). Beispielterme aus quelle.md beibehalten.
Neu ergänzte fehler: aequivalenz. Prüfskript OK, Proben mit Zahlen nachgerechnet.

## 2026-11-16 02:11 – STATUS
zahlen.natuerlich fertig: inhalte/klar/zahlen.natuerlich.json, alle 12 Lernziele aus quelle.md (einstieg, woerter, schritte 4–5, regel „So …“, fehler; probe bei roemisch_schreiben).
Durchgehende Situationen: Kronkorken sammeln, Spendenbarometer (Zahlenstrahl, Runden mit Übertrag), Stadion/Schulfest. Beispielzahlen der Karten mit Bild beibehalten (4 052; 12 | 008 | 000; Strahl 0–100 mit Pfeil bei 3 bzw. 7).
Neu ergänzte fehler: vergleichen, runden_uebertrag, runden_sinnvoll, unendlich, roemisch_system. Prüfskript: JSON gültig, Lernziele vollständig, 3–5 Schritte, einstieg ≥ 60 Zeichen, keine Verbotswörter – OK. Zahlen nachgerechnet.

## Ende
