# Postfach luecken-kl8 (Achtzehnte Runde, Teil B, Klasse 8)

## 2026-11-17 – FERTIG – Abschlussbericht
Zweig `luecken-kl8` (von lernen-app 4a71771), 4 Themen, je ein Commit. Keine Datenbank, kein App-Code, keine Tests, kein Merge.

**Prüfung je Thema:**
- `python3 -I tools/inhalt_pruefen.py inhalte/themen/<thema>.json` meldet OK, ohne Hinweise.
- `python3 -I inhalte/generatoren/_luecken_nachweis.py <thema> [--erweitert umfang]` meldet NACHWEIS OK:
  - alle alten Lernkarten Zeichen für Zeichen gleich, außer der erweiterten Karte „umfang“ (dort genau ein Schritt dazu);
  - alle alten Aufgaben unverändert und in alter Reihenfolge vorne;
  - in teilfaehigkeiten, abschnitte und bewertung nur neue Einträge dazu;
  - ziel, merke, quellen und offen unverändert.
- Die Generatoren erzeugen die Dateien bei erneutem Lauf unverändert.
- Jede neue Aufgabe habe ich gelesen und von Hand nachgerechnet. Das Programm rechnet jede Zahl- und Lückenaufgabe zusätzlich über `c` nach.

**Neue Lernkarten** (alle Pflicht, neues Muster: einstieg, woerter, Bildergeschichte mit Bild je Schritt, fehler + fehler_bild, regel, probe; je 18 Übungen 4/6/8 mit 2 Prüfungsvorbildern und 1 Knobelaufgabe, 1 Test, 3 Korrektur, 6 Sicherung):

| Thema | Lernkarte (Stelle) | Inhalt | Lehrplan-Bezug |
|---|---|---|---|
| funktionen.linear | graph_ablesen (nach „ablesen“) | Gerade zeichnen: t auf der y-Achse, Steigungsdreieck aus ganzen Kästchen (auch m = a/b, fallend). Graph zur Gleichung zuordnen, m und t am Graphen ablesen. | M8 2 Lineare Funktionen (Graphen zeichnen, Parameter am Graphen deuten) |
| funktionen.grundbegriffe | sachzusammenhang (am Ende) | Tarife als Tabelle, Term und Graph; Rückwärtsrechnen; Term aus Tabelle; Temperaturkurve ablesen und deuten; Tarifvergleich; Knobel „Temperatur → Uhrzeit ist keine Funktion“. | M8 1 Funktion und Term („funktionale Zusammenhänge (z. B. Stromtarife, Temperaturverläufe) mit Tabellen, Diagrammen und … Termen“) |
| funktionen.gebrochen | indirekt_sach (nach „indirekt“) | Umgekehrter Dreisatz: Kosten teilen, Vorrat, Fahrzeit; erkennen, ob direkt, indirekt oder weder noch; Zahnräder; Tabelle; Ausfall bzw. Verkauf mitten im Vorgang; Pumpen mit Menge und Zeit; Druck · Volumen (Physik). | M8 3 („y = a/x als indirekt proportionale Zuordnung zweier Größen … auch in naturwissenschaftlichen Kontexten“) |

**Erweiterte Karte:**
- messen.kreisberechnung / umfang:
  - 5. Schritt „Warum etwa 3,14? Sechseck innen hat 3 · d, Quadrat außen 4 · d.“ mit maßstäblicher Zeichnung;
  - 6 neue Übungen (je 2 auf Stufe 1, 2, 3): π aus Messung (Teller, Fahrradreifen), Vielecke innen und außen, „π = 3 genügt?“.
  - Bezug: M8 7, π näherungsweise bestimmen.

**Nicht umgesetzt bzw. nur gemeldet:**
- Prismen und Zylinder (messen.prisma_zylinder) baut Teil A. Das Verschieben der Karte „zylinder“ aus messen.kreisberechnung ist nur gemeldet.
- gleichungen.bruch: Die Karte „graphisch“ steht am Ende statt wie vorgeschlagen nach „scheinloesung“. Verschieben ist nicht Teil dieses Auftrags, deshalb nur gemeldet.
- Das Kind zeichnet in der App nicht selbst. „Gerade zeichnen“ wird deshalb über Zwischenschritte geprüft: welcher Gitterpunkt nach dem Steigungsdreieck, welches kleinste Steigungsdreieck, welcher Graph passt. Der Eintrag unter `offen` in funktionen.linear bleibt richtig und unverändert.

**Quellen:**
- Lehrplan:
  - ISB, „Verbindliche Hinweise zu Schwerpunktsetzungen in den Lehrplänen, Gymnasium, Mathematik Jgst. 8“ (Stand 08/2021), mit Auszügen aus M8 1, M8 2 und M8 3: https://www.distanzunterricht.bayern.de/fileadmin/user_upload/lernenzuhause/Gymnasium/deutsch_englisch_mathe/M_Schwerpunktsetzungen_8.pdf
  - Lehrplan-Seite: https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/8/mathematik. Ihr Abruf in diesem Chat blieb an einer offenen Freigabe hängen. Der Bezug für π (M8 7) stützt sich deshalb auf die Angabe in klasse8.json und nicht auf den selbst gelesenen Lehrplantext.
- Prüfungsvorbilder (nur Typ und Niveau; Wortlaut, Einkleidung und Zahlen eigen; Fundstellen aus der Zehnten Runde, postfach/schwer-kl8.md):
  - BMT8 2022/2024/2025 und BMT10 2017/2024 (ISB, https://www.isb.bayern.de/…/Jahrgangsstufenarbeiten/Mathematik/): Tarif, Steigung einer Treppe oder Straße, Schnittpunkt zweier Tarife;
  - VERA-8 (IQB): Kurve lesen und deuten;
  - Schulaufgaben-Typ Kl. 8 laut Stark-Leseprobe: „Welcher Graph gehört zu welcher Funktion?“.

**Neue Hilfsdateien:** `inhalte/generatoren/_luecken_kl8.py` (Einbau neuer Karten mit eigenem Zufallsstart) und `inhalte/generatoren/_luecken_nachweis.py` (Nachweis gegen origin/lernen-app). Beide können die Chats der anderen Klassen mitbenutzen.

## 2026-11-17 – STATUS: Bestandsaufnahme (Liste „luecken“ in inhalte/pruefung/aufbau/klasse8.json vom 14.11., geprüft gegen lernen-app 4a71771)

| # | Lücke (Kurzform) | Dringlichkeit | Stand heute |
|---|---|---|---|
| 1 | Volumen/Oberfläche gerader Prismen, Sachaufgaben Prisma/Zylinder (M8 7); Karte „zylinder“ aus messen.kreisberechnung verschieben | hoch | **nicht Teil dieses Auftrags.** Neues Thema messen.prisma_zylinder baut Teil A (Zweig luecken-neu). Das Verschieben der Karte „zylinder“ ist nur gemeldet: Teil A soll laut Auftrag darauf verweisen und sie nicht verschieben. |
| 2 | Lineare Gleichungen und Termumformungen inkl. binomischer Formeln (Kl. 7) fehlen | hoch | **erledigt:** gleichungen.linear (Kl. 7: waage … sach) und terme.umformen (Kl. 7, mit Karte „binomisch“). |
| 3a | Graphen: Geraden zeichnen, Parameter am Steigungsdreieck ablesen | hoch | **offen, teilweise erledigt.** Die Karte „ablesen“ in funktionen.linear hat inzwischen Bordkarten mit Graph und Steigungsdreieck. Die Erklärung zum Zeichnen der Geraden fehlt aber, ebenso Aufgaben zu Bruch-Steigungen. Deshalb kommt die neue Karte „graph_ablesen“ nach „ablesen“. |
| 3b | LGS graphisch | hoch | **erledigt:** gleichungen.lgs2, Karte „grafisch“ (dort nach „pruefen“). |
| 3c | Ungleichungen graphisch | hoch | **erledigt:** gleichungen.ungleichungen, Karte „grafisch“ (vor „sachaufgabe“). |
| 3d | Bruchgleichungen graphisch | hoch | **erledigt:** gleichungen.bruch, Karte „graphisch“ (am Ende, nach „verhaeltnis“; laut Liste war die Stelle nach „scheinloesung“ vorgesehen – Verschieben nur gemeldet). |
| 3e | funktionen.gebrochen, Karte „parameter“ mit Bild | hoch | **erledigt:** Die Karte hat Kartenbild (Hyperbel) und Schrittbilder. |
| 4 | Funktionale Zusammenhänge aus dem Alltag (Tarife, Temperaturverläufe) | mittel | **offen** → funktionen.grundbegriffe, neue Karte „sachzusammenhang“ am Ende. |
| 5 | π näherungsweise bestimmen; Kreisfläche nicht-linear | niedrig | **offen** (π-Schritt) → messen.kreisberechnung, Karte „umfang“ um einen Schritt „Warum etwa 3,14?“ erweitern. Die Nicht-Linearität deckt „verstehen“ ab: erledigt. |
| 6 | Indirekte Proportionalität in Sachaufgaben (Produktgleichheit, Dreisatz „umgekehrt“) | mittel | **offen** → funktionen.gebrochen, neue Karte „indirekt_sach“ nach „indirekt“. |

Reihenfolge der Arbeit: funktionen.linear (hoch) → funktionen.grundbegriffe → funktionen.gebrochen → messen.kreisberechnung.

Werkzeuge:
- `inhalte/generatoren/_luecken_kl8.py`: neue Karte einfügen oder vorhandene Karte erweitern. Neue Aufgaben werden hinten angehängt, mit eigenem Zufallsstart und eigener Antwort-Positionsverteilung.
- `inhalte/generatoren/_luecken_nachweis.py`: Nachweis gegen origin/lernen-app.

## 2026-11-17 – STATUS funktionen.linear
Neue Karte „graph_ablesen“ (Gerade zeichnen und am Graphen ablesen) nach „ablesen“, Pflicht, mit 28 Aufgaben (Prüfungsvorbild 2, Knobel 1). `inhalt_pruefen` OK; Nachweis OK (210 alte Aufgaben unverändert vorne, 7 alte Karten gleich).

## 2026-11-17 – STATUS funktionen.grundbegriffe
Neue Karte „sachzusammenhang“ (Zusammenhänge aus dem Alltag beschreiben) am Ende, Pflicht, 28 Aufgaben: Tarife in Tabelle, Term und Graph; Temperaturkurve lesen und deuten; Tarifvergleich. `inhalt_pruefen` OK; Nachweis OK (240 alte Aufgaben unverändert vorne).

## 2026-11-17 – STATUS funktionen.gebrochen
Neue Karte „indirekt_sach“ (Sachaufgaben: umgekehrter Dreisatz) nach „indirekt“, Pflicht, 28 Aufgaben.
- Inhalte: Kosten teilen, Vorrat, Fahrzeit; erkennen, ob direkt, indirekt oder weder noch; Zahnräder, Tabelle mit Produktgleichheit; Ausfall oder Verkauf mitten im Vorgang; Pumpen mit Menge und Zeit; Physik-Beispiel Druck · Volumen.
- `inhalt_pruefen` OK; Nachweis OK (180 alte Aufgaben unverändert vorne).

## 2026-11-17 – STATUS messen.kreisberechnung
Karte „umfang“ um den 5. Schritt „Warum etwa 3,14? Sechseck innen hat 3 · d, Quadrat außen 4 · d.“ erweitert. Der Schritt hat eine maßstäbliche Zeichnung (Kreis mit Sechseck innen und Quadrat außen).
Dazu 6 neue Übungen zu π-Näherungen (Messen, Vielecke innen und außen), je 2 auf Stufe 1, 2 und 3. `inhalt_pruefen` OK; Nachweis OK: nur die Karte „umfang“ geändert, genau ein Schritt eingefügt, 210 alte Aufgaben unverändert vorne.
