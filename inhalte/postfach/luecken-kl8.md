# Postfach luecken-kl8 (Achtzehnte Runde, Teil B, Klasse 8)

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
