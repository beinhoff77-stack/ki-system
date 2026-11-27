# Postfach pruefung-potenz (Siebenundzwanzigste Runde: Prüfung der geteilten Potenzgesetz-Flüge)

Neueste Meldung oben.

## 2026-11-20 – FERTIG: Prüfung Potenz

Zweig `pruefung-potenz` (von `lernen-app` 1cc6edc). Bericht: `inhalte/pruefung/potenz/bericht.md`, Skripte `nachrechnen.py` und `ausgeben.py` daneben. Nichts an den Inhalten geändert, nichts in die Datenbank, kein App-Code, keine Kinderdaten.

- **Nachgerechnet:** Flug A (191), Flug B (175), Gym 6 „Fehler finden“ (32) – 144 per eigenem Skript, 254 von Hand. **Keine falsche Lösung, keine richtige Ablenker-Antwort.**
- **Muss (2), beides Tipps:**
  1. Gym 6, `negativer_exponent`, „Wie viel Mal so groß ist 2² wie 2⁻²?“: Tipp „Exponenten subtrahieren: n − (−n)“ (Potenzgesetz mit negativen Exponenten in Klasse 6).
  2. Flug A, `mal_gleiche_basis`, „a⁵ · a¹ = aᵏ“: Tipp „Auch negative Exponenten werden addiert …“.
- **Sollte (6):** Hoch-0-Tipps in Gym 6 mit 2³⁻³; zwei Aufgaben mit kleinerem erstem Exponenten in Flug A („2¹⁰ : 2ⁿ = 1/4“, „10⁴ : 10⁴ : 10⁴ · 10⁸“); 6 unpassende Ablenker in den umgezogenen Fehler-Aufgaben; Stufe 3 „fehler“ passt bei 10 der 23 umgezogenen Aufgaben nicht (Entscheidung Haupt-Chat); IB: Flug A (MYP 4) nach `terme.umformen` (MYP 3), das ein Potenzgesetz braucht; zwei Übungen ohne Typ und gleich gebaute Aufgaben mit verschiedenem Typ in Flug A.
- **Kann (8):** u. a. „Bruchterm“ in RS 7/MYP 4 vor den Bruchtermen, veraltetes `offen` in Gym 6, `lehrplan_rs` von `terme.umformen`, „Potenzen von Potenzen“ in Flug A (Entscheidung des Nutzers).
- **Ohne Befund:** Flug B vollständig (Lösungen, Stufen, Typen, Erklärungen, Lehrplan M8 4); `terme.umformen` – genau die vier Karten fehlen, Rest unverändert; Themenliste lückenlos; kann-Texte treffen den Inhalt.
- **Für den Haupt-Chat vor dem Umhängen:** prüfen, ob in der Datenbank alte Aufgaben der vier Lernziele von `terme.umformen` mit negativen Exponenten liegen (laut `offen` gibt es dort Aufgaben aus der Zeit vor dem Bausatz, die nicht im Repo stehen).
