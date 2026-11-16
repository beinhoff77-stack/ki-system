# Postfach daten-klassen-2 (Vierzehnte Runde)

Neueste Meldung oben.

## 2026-11-16 06:55 – STATUS Teil 2
Vertiefungen gekennzeichnet (aus bewertung.lernziele_pflicht nach lernziele_vertiefung, je ein Argument `vertiefung=` im Generator):
- geometrie.winkel: kreuzung („Winkel an einer Geradenkreuzung“). In themenliste.json umfang auf Klasse-5-Stoff gekürzt; Titel „Mit Winkeln rechnen“ stand schon dort.
- abbildungen.kongruenz: verschiebung, drehung, parkett.
- raum.schraegbilder: lage (windschief), koordinaten (Punkte im Raum).
Nachweis `python3 -I inhalte/generatoren/_vertiefung_nachweis.py <thema>`: in allen drei Dateien nur inhalt.bewertung geändert, Aufgaben und Lernkarten-Texte gleich. Prüfskript OK.
Hinweis: inhalte/README.md hat (noch) keinen Abschnitt „Vertiefung“, auf den der Auftrag verweist. Ich habe das vorhandene Feld bewertung.lernziele_vertiefung benutzt.
Die Themendateien tragen eine eigene Titelzeile nicht; „offen“ in geometrie.winkel nennt noch die alte Lage („Winkelsätze Kl. 5“) – laut Auftrag nicht geändert.

## 2026-11-16 06:40 – STATUS Teil 1
Neuer Flug `geometrie.winkelsaetze` (thema_id 98, block 80 Addis Abeba, gym_by 7, LehrplanPLUS M7 2.2) fertig:
8 Lernkarten im neuen Muster (einstieg, woerter, Schritte mit Zeichnungen, fehler/fehler_bild, regel), je 18 Übungen (4/6/8), 1 Test, 3 Korrektur, 6 Sicherung = 224 Aufgaben.
Je Lernkarte 2 Stufe-3-Aufgaben nach Prüfungsvorbild und 1 Knobelaufgabe. Prüfskript OK ohne Hinweise. Eintrag in themenliste.json vor geometrie.konstruktion.
Lernkarten: Scheitel-/Nebenwinkel · Stufen-/Wechselwinkel · Parallelität prüfen · Innenwinkelsumme begründen · Außenwinkel · Winkelsumme im Vieleck · Winkel in Figuren · Begründen mit Winkelsätzen.
Offen (Entscheidung Sebastian): geometrie.konstruktion am selben Ort hat schon die Karten „parallelen“, „winkelsumme“, „vierecke“ – Überschneidung. Vorschlag: dort später auf Konstruktion/Kongruenz kürzen oder als Wiederholung lassen.
