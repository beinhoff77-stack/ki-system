# Postfach inhalte-ib (Paket IB, Vierte Runde)

Neueste Meldung oben.

## 2026-11-14 15:16 – STATUS
3/14 daten.zweidimensional fertig: 5 Lernkarten (Streudiagramm lesen, Art des Zusammenhangs, Ausgleichsgerade, Ausreißer, Korrelation/Kausalität), 140 Aufgaben mit Streudiagrammen, Prüfskript OK.

## 2026-11-14 15:12 – STATUS
2/14 groessen.verhaeltnisse fertig: 6 Lernkarten (kürzen, gleichwertig, aufteilen, Proportionen, Einheitsraten, Änderungsraten), 168 Aufgaben, Prüfskript OK. Hilfsfunktion eu() für Geldbeträge in _ib.py ergänzt.

## 2026-11-14 15:09 – STATUS
1/14 mengen.grundbegriffe fertig: 5 Lernkarten, 140 Aufgaben, Prüfskript OK. Venn-Diagramme als figur (Kreise + Rechteck). Hilfsdatei inhalte/generatoren/_ib.py angelegt.

## 2026-11-14 15:09 – FRAGE
Vier Themen haben in themenliste.json `klasse: {}` (daten.normalverteilung, finanzen.zinseszins, sonder.logik, zahlen.schranken). Das Prüfskript verlangt ein nicht leeres Feld.
- Annahme: dort `"klasse": {"zusatz": 10}` (Niveau Klasse 9/10 laut Auftrag; die App wertet nur gym_by/rs_by/ib_myp als Schulart aus, der Schlüssel stört also nicht). Gesetzt in `_ib.py` (KLASSE_OHNE).
- Ich arbeite damit weiter. Bitte melden, falls ein anderer Wert gewünscht ist – dann nur KLASSE_OHNE ändern und die vier Generatoren neu laufen lassen.
