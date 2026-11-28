# Regel-Zuordnung (VT1B)

Feld `regel` je Aufgabe, je Lernziel einheitlich gesetzt (Kern: `REGEL[(Einheit, Lernziel)]`). Grundlage: Vorschläge der Vorprüfung (Abschnitt „Regel-Kennungen“) und `regeln-uebersicht/kennungen.json`; die Prüfung `tools/vtest_pruefen.py` vergleicht mit der Lernkartenregel.

| Einheit / Lernziel | `regel` | Herkunft | Bemerkung |
|---|---|---|---|
| bruch.prozent / prozentwert, grundwert, verstehen | `id.verhaeltnisse.prozent` | Vorschlag, entspricht der Lernkarte | Bruch↔Prozent (VT1B-007) hätte `id.zahlen.schreibweisen` sein können; Lernziel einheitlich belassen |
| gleichungen.bruch / definitionsmenge | `id.algebra.erlaubte_zahlen` | Vorschlag, Lernkarte | – |
| gleichungen.bruch / ueber_kreuz | `rr.waage` | Vorschlag (Lernkarte hat keine) | 033 (Ausmultiplizieren) hätte `rr.ausmultiplizieren` sein können |
| gleichungen.bruch / scheinloesung | `id.algebra.erlaubte_zahlen` | Vorschlag (Lernkarte hat keine) | – |
| gleichungen.bruch / verhaeltnis | `rr.verhaeltnis` | Vorschlag, Lernkarte | – |
| terme.potenzgesetze / negativer_exponent, fehler_finden | `rr.potenz` | Vorschlag | Umkehr-Aufgaben (051, 053, 063) passen auch zu `id.zahlen.hoch_zurueck`; 058 zu `rr.reihenfolge`, je Lernziel einheitlich belassen |
| zahlen.potenzen_zehner / gross_wissenschaftlich | `rr.stellenwert` | Vorschlag | Bedingungsaufgaben (066, 069) zu `id.zahlen.schreibweisen`, einheitlich belassen |
| zahlen.potenzen_zehner / negativer_exponent | `rr.potenz` | Vorschlag, Lernkarte | – |
| zahlen.potenzen_zehner / vorsilben_klein | `id.verhaeltnisse.groesse` | Vorschlag (Lernkarte: `id.zahlen.buendeln`, passt nicht) | laut Katalog Klasse 5; Abweichung von der Lernkarte, Hinweis der Prüfung erwartet |
| zahlen.potenzen_zehner / vergleichen_pruefen | `id.zahlen.schreibweisen` | Vorschlag | 086, 089 hätten `rr.potenz` sein können |
| messen.flaechen_vielecke / dreieck, zusammengesetzt, verstehen | `id.flaeche_raum.aus_dem_rechteck` | Vorschlag, Lernkarte | – |
| messen.flaechen_vielecke / rueckwaerts | `id.flaeche_raum.aus_dem_rechteck` | **abweichend vom Vorschlag** (`rr.gegenrechnung`) | Das Prüfwerkzeug meldete bei `rr.gegenrechnung` einen Fehler (Abweichung von der Lernkarte); deshalb die Lernkartenregel |

**Ohne Regel / Fehlbilder:** `fehlbild` und `regel_des_fehlbilds` bleiben leer. Die Fehlbild-Kennungen des Katalogs (z. B. `fb.potenz.negative_hochzahl_als_minus`) passen nur teilweise zu den Fehlbildern der neu geschriebenen Aufgaben; eine geratene Kennung wäre schlechter als keine. Das Prüfwerkzeug erzeugt dafür keine Fehler.
