# Postfach pruefung-neu-1 (Fünfundzwanzigste Runde, unabhängige Prüfung)

Neueste Meldung oben. Prüfer: Chat `pruefung-neu-1`, hat keines der geprüften Themen geschrieben.

Allgemein gilt für alle Berichte:
- „Nachgerechnet“ heißt: Lösung unabhängig vom Generator bestimmt – entweder mit einem eigenen Prüfskript, das die Zahlen aus dem **Fragetext** liest und neu rechnet (nicht aus `c`), oder von Hand.
- Übungen ohne `g` sind laut Zwanzigster Runde „überzählig“ und werden beim Einspielen gesperrt. Sie wurden auf richtige Lösung (a) geprüft, nicht auf Stufe/Typ (f).
- Lehrplan: Die Seiten von lehrplanplus.bayern.de konnte ich in dieser Sitzung nicht direkt abrufen (Abruf brauchte eine Freigabe, die nicht beantwortet wurde). Lehrplanaussagen stützen sich daher auf `lehrplan_andere` in `themenliste.json` und auf ISB-Dokumente aus der Websuche (Abruf 20.11.2026); was nicht belegt ist, steht als Annahme da.

## 2026-11-20 – abbildungen.determinanten2 (RS 7): mit Korrekturen in Ordnung

**Gelesen und nachgerechnet (Fakt):** 6 Lernkarten (Einstieg, Wörter, Bild, Schritte, Fehler, Regel) und alle 240 Aufgaben (168 Übungen, 12 Knobel, 6 Test, 18 Korrektur, 36 Sicherung). 122 Zahl-Aufgaben mit eigenem Skript aus dem Fragetext nachgerechnet (Determinante, Parallelogramm, Dreieck, Viereck, Vieleck per Gauß-Formel, Maßstab) – 0 Abweichungen. Alle übrigen (Auswahl, Lücken, Parameter, Knobel) von Hand nachgerechnet; zusätzlich geprüft, dass in den Karten parallelogramm/dreieck/viereck/vieleck jede Eckenfolge gegen den Uhrzeigersinn läuft (Betrag wird erst in „umlaufsinn“ erklärt) – stimmt überall. Beispielrechnungen aller 6 Lernkarten stimmen.

**Änderungen je Fehlerart:** a) 0 · b) 2 · c) 1 · d) 0 · e) 0 · f) 0

- c) `det_berechnen`, Stufe 3, parameter: „Für welche Zahlen t hat die Determinante der Vektoren a = (t | 2) und b = (8 | t) den Wert 0?“ verlangte t² = 16 mit Lösungen ±4, also eine reinquadratische Gleichung (RS 9, `gleichungen.reinquadratisch`). Ersetzt durch „… a = (t | 2) und b = (8 | 4) …“ → 4t − 16 = 0, t = 4 (Typ und Stufe gleich). Die Knobel-Karte mit n² = 49 bleibt: n ist natürlich, gesucht ist eine Quadratzahl aus Klasse 5.
- b) Knobel `umlaufsinn`: „C hat ganzzahlige Koordinaten mit −3 ≤ x ≤ 3 …“ – x und y waren nicht an C gebunden. Jetzt „C(x | y) hat …“.
- b) Knobel `umlaufsinn`: „Wie klein kann der Flächeninhalt … höchstens werden“ (dieselbe verwirrende Wendung wie in stufen-kl5 gemeldet). Jetzt „Welchen kleinsten Flächeninhalt kann das Dreieck ABC haben, wenn es ein echtes Dreieck sein soll (Fläche nicht 0)?“

Keine Änderung der Art a) – keine falsche Lösung gefunden.

**Lehrplan:** Passt zu RS 7, Wahlpflichtfächergruppe I (Flächen von Dreiecken, Vierecken und Vielecken mit zweireihigen Determinanten, `lehrplan_andere`); Beleg aus Websuche: ISB-Jahrgangsstufentest 8 I 2022 fragt die Dreiecksfläche mit Determinante aus AB und AC als Vorwissen ab (isb.bayern.de, Abruf 20.11.2026). Nichts Wesentliches fehlt. Annahme (nicht gegen lehrplanplus.bayern.de geprüft): In Bayern kommen Vektoren in RS 7 vor den Determinanten; in `themenliste.json` steht `abbildungen.vektoren` dahinter. Das Thema erklärt „Vektor“ und „Spitze minus Fuß“ selbst, setzt also nichts voraus – nur zur Kenntnis für die Reihenfolge.

**Nicht geprüft / Grenzen:** Zeichnungen nur über die Koordinaten im JSON geprüft, nicht in der App angesehen. Knobel-Karten mit |x + 1| = 5 und „Ausmultiplizieren“ (Determinante von a + b und a − b) sind anspruchsvoll, aber als freiwillige Knobel-Karten mit Beispiel im Lösungsweg vertretbar (Meinung).

Prüfskript: OK, 0 Gruppen „gleich gebaut hintereinander“.
