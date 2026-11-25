# Mathe-Profi – Auftrag 3: Musterstapel „Weg-Aufgaben“ (25.11.2026)

Auftrag des Nutzers vom 25.11.: Reihenfolge aus `auftrag2.md` bestätigt („Platz 0“ zuerst). Dies ist der Musterstapel dafür.

**Ziel in einem Satz:** In den Etappen, deren Lernziel ein Weg ist, soll das Kind den Weg zeigen müssen – mit den Antwortformen, die es heute schon gibt. Kein Bau an der App nötig.

| Datei | Inhalt |
|---|---|
| `auftrag3.md` | dieser Bericht: 6 Muster mit Regeln, 20 Musteraufgaben, Mengen- und Regelvorschlag |
| `nachrechnen3.py` | rechnet jede Aufgabe auf zwei Wegen nach (von Hand im Skript und mit dem exakten Rechner des Repos), prüft die Musterregeln und die Antwortform mit `pruefe_antwort` aus `tools/inhalt_pruefen.py`. Lauf: `python3 -I inhalte/mathe-profi/nachrechnen3.py` → „OK“ |
| `aufgaben-auftrag3.json` | die 20 Datensätze im Generator-Format (`l, t, p, s, g, y, f, a, o, c, h, w`), dazu `muster`, `weg`, `probe`, `falsch` |

Kennzeichnung: **[G]** gesichert · **[A]** Annahme · **[M]** Meinung.

## 1. Die sechs Muster

Flug `zahlen.rechengesetze` (Rom), Etappen `vorteil`, `differenz_summe`, `verteilen`, `kopfrechnen`, `ueberschlag`, `schriftlich_geteilt`. Jedes Muster nennt die Regeln, die der Aufgaben-Ersteller per Programm prüfen muss.

| Muster | Was das Kind tut | Form | Stufe (`g`) | Regeln für den Stapel |
|---|---|---|---|---|
| **M1 Erster Schritt** | wählt das Zahlenpaar, das zuerst zusammengefasst wird | `auswahl` | 1 (`erkennen`) | Frage nach der **glatten Zahl**, nicht nach „zuerst“ (sonst zwei vertretbare Antworten). Genau ein Paar ergibt 10, 100 oder 1 000. Alle Paare als Antworten. |
| **M2 Lücke im faulen Weg** | füllt Zwischenschritt und Ergebnis eines vorgegebenen geschickten Wegs | `luecken` | 2 (`umkehr`, `darstellung`, `mehrschritt`) | Die erste Lücke ist nur mit dem geschickten Weg sinnvoll füllbar. Zahlen so, dass stures Rechnen im Kopf mühsam ist. Nicht die Zahlen der Lernkarte. |
| **M3 Welcher Weg stimmt?** | findet unter 3–4 Umformungen die eine gleichwertige | `auswahl` | 3 (`begruenden`), in der Fassung „derselbe Wert“ auch 1 (`erkennen`) | Genau eine Antwort hat den Zielwert. Jede falsche Antwort ist ein **benannter** typischer Fehler (z. B. „zieht die 1 nur einmal ab“). Nie nach dem „schnellsten“ Weg fragen – das ist Geschmack. |
| **M4 Fehlerzeile** | findet in einer Rechnung in Zeilen die Zeile, in der der Fehler **entsteht** | `auswahl` + `tabelle` | 3 (`fehler`) | Genau ein Fehler; die Zeilen danach rechnen folgerichtig mit dem falschen Wert weiter. Antworten sind die Zeilen plus „Alles richtig.“ Der Tipp nennt die Zeile nicht. |
| **M5 Nächster Strich** | tippt vor dem Rechnen den Strich am Zahlenstrahl an, der dem Ergebnis am nächsten liegt | `markierung` | 2 (`darstellung`, `einkleidung`) | Genauer Wert höchstens 30 % eines Abschnitts vom Strich entfernt. Lösung nicht am Rand und **nicht in der Skalenmitte**. Jede vernünftige Schätzung landet auf demselben Strich. Typische Fehler (Stelle verloren, plus statt mal) landen auf einem anderen Strich **im Bild**. Nur Anfang und Ende beschriftet. |
| **M6 Freier Überschlag** | schätzt eine Zahl; jede vernünftige Schätzung zählt | `zahl` + `toleranz` | 2 | `wert` = genaues Ergebnis, `toleranz` = 15 % davon, glatt gerundet. Jede Rundung auf die führende Stelle liegt drin; Stellenfehler, plus statt mal und grobes Runden beider Zahlen in dieselbe Richtung liegen draußen. Der Text sagt „jede vernünftige Schätzung zählt“. |

Warum das genügt [M]: M1–M3 prüfen, ob das Kind die Umformung **sieht**; M4, ob es eine Rechnung **prüfen** kann; M5–M6, ob es die **Größe** eines Ergebnisses kennt, bevor es rechnet. Das sind die drei Dinge, die „geschickt rechnen“ ausmachen und die eine reine Ergebnis-Abfrage nicht unterscheidet.

Grenze, offen gesagt [G]: Bei M5 und M6 kann ein Kind auch genau ausrechnen und dann antworten. Verhindern lässt sich das nicht; es kostet aber mehr Zeit als Schätzen. Bei M3 und M4 bleibt die Rate-Chance der Auswahl (mit zweitem Versuch bis 1/2). Das behebt erst das Mehrfach-Antippen (Bau 2).

## 2. Menge und Regel

- **Menge [M]:** je Etappe 6 Weg-Aufgaben (2 je Stufe), dafür ebenso viele gleich gebaute „Rechne geschickt: a · b“-Karten streichen. Für die sechs Etappen sind das 36; 20 liegen hier vor, 16 baut der Aufgaben-Ersteller nach diesen Mustern. Ich prüfe davon eine Stichprobe von 8.
- **Regel „gelandet“ [M]:** In diesen sechs Etappen zählt „gelandet“ erst, wenn mindestens eine Weg-Aufgabe im ersten Versuch richtig war. Das ist ein kleiner Bau am Server und braucht ein Kennzeichen an der Aufgabe. Vorschlag: Feld `weg: true` (steht in den Datensätzen hier). Ob Feld, Teilfähigkeit oder Typ – entscheidet der Projektleiter.
- **Ohne die Regel** wirken die Aufgaben trotzdem, nur schwächer: Das Kind kann an ihnen vorbei landen.

## 3. Die 20 Musteraufgaben

Formen: 10 `auswahl` (davon 4 mit Tabelle), 5 `luecken`, 3 `markierung`, 2 `zahl`. Stufen: 2 leicht, 10 mittel, 8 schwer. „Häufigste falsche Antwort“ ist durchweg **Annahme**.

<!-- AUFGABEN:ANFANG -->
### Etappe `vorteil`

**W1 · Muster M1 · leicht (`erkennen`) · `auswahl`**  
Text: „Du rechnest 2 · 19 · 50 geschickt. Welche zwei Zahlen ergeben malgenommen eine glatte Zahl?“  
Auswahl: 2 und 19 | 19 und 50 | **2 und 50**  
Weg 1: Produkte der drei Paare: 38, 950, 100 – nur 2 · 50 ist glatt.  
Weg 2: Repo-Rechner: 2 · 19 = 38, 19 · 50 = 950, 2 · 50 = 100; 2 · 19 · 50 = 1 900.  
Häufigste falsche Antwort (Annahme): „2 und 19“ – rechnet von links, sucht kein Paar  
Tipp: Eine glatte Zahl ist 10, 100 oder 1 000. Probier die Paare im Kopf.

**W2 · Muster M2 · mittel (`umkehr`) · `luecken`**  
Text: „Rechne faul: Fasse zuerst die zwei Zahlen zusammen, die eine glatte Zahl ergeben.“ `5 · 43 · 20 = □ · 43 = □`  
Lösung: 100; 4 300  
Weg 1: 5 · 20 = 100, 100 · 43 = 4 300.  
Weg 2: Repo-Rechner: 5 · 43 · 20 = 4 300 = 100 · 43; von links: 215 · 20 = 4 300.  
Häufigste falsche Antwort (Annahme): 215 und 4 300 – rechnet von links und trägt das Zwischenergebnis ein  
Tipp: Welche zwei der drei Zahlen passen gut zusammen?

**W3 · Muster M4 · schwer (`fehler`) · `auswahl` + `tabelle`**  
Text: „Jemand rechnet 25 · 16 · 4 geschickt – und macht einen Fehler. In welcher Zeile?“  
Tabelle: Zeile 1: 25 · 16 · 4 = 25 · 4 · 16 · Zeile 2: = 100 · 16 · Zeile 3: = 116  
Auswahl: Zeile 1 | Zeile 2 | **Zeile 3** | Alles richtig.  
Weg 1: 25 · 4 = 100; 100 · 16 = 1 600; 100 + 16 = 116.  
Weg 2: Repo-Rechner: Zeile 1 links und rechts 1 600, Zeile 2 1 600, Zeile 3 behauptet 116.  
Häufigste falsche Antwort (Annahme): „Zeile 1“ – hält das Tauschen für den Fehler  
Tipp: Prüfe jede Zeile für sich: Ist sie gleich viel wert wie die Zeile davor?

### Etappe `differenz_summe`

**D1 · Muster M3 · schwer (`begruenden`) · `auswahl`**  
Text: „83 − 27 − 13 soll geschickt gerechnet werden. Nur eine Umformung hat denselben Wert. Welche?“  
Auswahl: **83 − (27 + 13)** | 83 − (27 − 13) | (83 − 13) + 27 | 27 − 83 − 13  
Weg 1: 83 − 27 − 13 = 43; Optionen: 43, 69, 97, −69.  
Weg 2: Repo-Rechner wertet alle vier Terme aus: nur der erste ergibt 43.  
Häufigste falsche Antwort (Annahme): „83 − (27 − 13)“ – setzt die Klammer, ohne das Rechenzeichen in der Klammer zu ändern  
Tipp: Zweimal abziehen ist dasselbe wie einmal die Summe abziehen.

### Etappe `verteilen`

**V1 · Muster M2 · mittel (`umkehr`) · `luecken`**  
Text: „Rechne 6 · 18 so, als wären es 6 · 20.“ `6 · 18 = 6 · 20 − 6 · □ = □`  
Lösung: 2; 108  
Weg 1: 120 − 12 = 108 = 6 · 18.  
Weg 2: Repo-Rechner: 6 · 20 − 6 · 2 = 108 = 6 · 18.  
Häufigste falsche Antwort (Annahme): 2 und 118 – zieht nur 2 ab statt 6 · 2  
Tipp: Um wie viel ist 20 größer als 18? Das hast du in jeder der 6 Reihen zu viel.

**V2 · Muster M2 · mittel (`darstellung`) · `luecken`**  
Text: „Klammere den gemeinsamen Faktor aus.“ `13 · 47 + 13 · 53 = 13 · □ = □`  
Lösung: 100; 1 300  
Weg 1: 47 + 53 = 100; 13 · 100 = 1 300.  
Weg 2: Repo-Rechner, stur: 611 + 689 = 1 300.  
Häufigste falsche Antwort (Annahme): 100 und 2 600 – zählt die beiden 13 zusammen  
Tipp: Beide Produkte haben die 13. Was bleibt in der Klammer?

**V3 · Muster M3 · schwer (`begruenden`) · `auswahl`**  
Text: „8 · 99 soll im Kopf gerechnet werden. Nur ein Weg stimmt. Welcher?“  
Auswahl: 8 · 100 − 1 | **8 · 100 − 8** | 8 · 90 + 9 | 800 − 99  
Weg 1: 8 · 99 = 792; Optionen: 799, 792, 729, 701.  
Weg 2: Repo-Rechner wertet alle vier Terme aus: nur „8 · 100 − 8“ ergibt 792.  
Häufigste falsche Antwort (Annahme): „8 · 100 − 1“ – zieht die 1 nur einmal ab  
Tipp: 99 ist 100 − 1. Wie oft wird die 1 abgezogen?

**V4 · Muster M4 · schwer (`fehler`) · `auswahl` + `tabelle`**  
Text: „Jemand rechnet 6 · 29 in drei Zeilen. In welcher Zeile entsteht der Fehler?“  
Tabelle: Zeile 1: 6 · 29 = 6 · 30 − 6 · 1 · Zeile 2: = 180 − 1 · Zeile 3: = 179  
Auswahl: Zeile 1 | **Zeile 2** | Zeile 3 | Alles richtig.  
Weg 1: 6 · 30 = 180, 6 · 1 = 6, 180 − 6 = 174.  
Weg 2: Repo-Rechner: Zeile 1 beide Seiten 174; Zeile 2 ergibt 179.  
Häufigste falsche Antwort (Annahme): „Zeile 3“ – sucht den Fehler dort, wo er sichtbar wird, nicht wo er entsteht  
Tipp: Rechne die beiden Teile der ersten Zeile einzeln aus und vergleiche mit der nächsten Zeile.

### Etappe `kopfrechnen`

**P1 · Muster M2 · mittel (`umkehr`) · `luecken`**  
Text: „Verdopple die eine Zahl und halbiere die andere.“ `15 · 24 = 30 · □ = □`  
Lösung: 12; 360  
Weg 1: 30 · 12 = 360.  
Weg 2: Repo-Rechner: 15 · 24 = 360.  
Häufigste falsche Antwort (Annahme): 24 und 720 – verdoppelt, ohne zu halbieren  
Tipp: Aus 15 wurde 30. Was muss dann mit der 24 passieren, damit das Ergebnis gleich bleibt?

**P2 · Muster M2 · mittel (`mehrschritt`) · `luecken`**  
Text: „Mal 5 geht leicht über mal 10. Fülle die Lücken.“ `5 · 68 = 10 · □ = □`  
Lösung: 34; 340  
Weg 1: 68 : 2 = 34; 10 · 34 = 340.  
Weg 2: Repo-Rechner: 5 · 68 = 340.  
Häufigste falsche Antwort (Annahme): 68 und 680 – nimmt mal 10 und vergisst zu halbieren  
Tipp: 5 ist die Hälfte von 10. Wovon nimmst du dann die Hälfte?

**P3 · Muster M3 · schwer (`begruenden`) · `auswahl`**  
Text: „25 · 28 soll im Kopf gerechnet werden. Nur ein Weg stimmt. Welcher?“  
Auswahl: 25 · 4 + 7 | 100 · 28 | **100 · 7** | 25 · 20 + 8  
Weg 1: 25 · 28 = 700; Optionen: 107, 2 800, 700, 508.  
Weg 2: Repo-Rechner wertet alle vier Terme aus: nur „100 · 7“ ergibt 700.  
Häufigste falsche Antwort (Annahme): „25 · 20 + 8“ – zerlegt die 28, nimmt aber die 8 nicht mal 25  
Tipp: Zerlege 28 in zwei Faktoren. Einer davon passt gut zur 25.

**P4 · Muster M3 · leicht (`erkennen`) · `auswahl`**  
Text: „Welche Rechnung hat denselben Wert wie 6 · 49?“  
Auswahl: 6 · 50 − 1 | 6 · 40 + 9 | **6 · 50 − 6**  
Weg 1: 6 · 49 = 294; Optionen: 299, 249, 294.  
Weg 2: Repo-Rechner wertet alle drei Terme aus: nur „6 · 50 − 6“ ergibt 294.  
Häufigste falsche Antwort (Annahme): „6 · 50 − 1“ – zieht die 1 nur einmal ab  
Tipp: 49 ist eins weniger als 50 – und zwar in jedem der 6 Päckchen.

### Etappe `ueberschlag`

**U1 · Muster M5 · mittel (`darstellung`) · `markierung`**  
Text: „Ohne genau zu rechnen: Tippe den Strich an, der am nächsten an 312 · 29 liegt.“  
Zahlenstrahl: 0 bis 15 000 in 10 Abschnitten, nur Anfang und Ende beschriftet  
Lösung: Strich 6  
Weg 1: 300 · 30 = 9 000; Strichwerte 0, 1 500, …; 9 000 = 6 · 1 500.  
Weg 2: Repo-Rechner: 312 · 29 = 9 048, Abstand zum 6. Strich 48 (von 1 500). Auch 9 360, 8 700 und 9 300 liegen am 6. Strich.  
Häufigste falsche Antwort (Annahme): Strich 1 oder Strich 0 (Ergebnis 900 oder 341) – Stelle verloren oder plus statt mal gerechnet  
Tipp: Runde beide Zahlen so, dass du im Kopf malnehmen kannst. Was ist ein Abschnitt wert?

**U2 · Muster M5 · mittel (`einkleidung`) · `markierung`**  
Text: „5 580 Flaschen werden auf 18 Lastwagen verteilt. Tippe den Strich an, der am nächsten an der Zahl je Lastwagen liegt.“  
Zahlenstrahl: 0 bis 1 000 in 10 Abschnitten, nur Anfang und Ende beschriftet  
Lösung: Strich 3  
Weg 1: 6 000 : 20 = 300; 5 400 : 18 = 300.  
Weg 2: Repo-Rechner: 5 580 : 18 = 310, Abstand zum 3. Strich 10 (von 100).  
Häufigste falsche Antwort (Annahme): Strich bei 0 (31) – eine Stelle verloren  
Tipp: Runde beide Zahlen so, dass das Teilen im Kopf geht. Was ist ein Abschnitt wert?

**U3 · Muster M6 · mittel (`mehrschritt`) · `zahl`**  
Text: „Ein Stadionblock hat 38 Reihen mit je 52 Plätzen. Wie viele Plätze sind das ungefähr? Überschlage im Kopf – jede vernünftige Schätzung zählt.“  
Lösung: 1 976 (Toleranz ± 300)  
Weg 1: 40 · 50 = 2 000, liegt 24 neben dem genauen Wert.  
Weg 2: Repo-Rechner: 38 · 52 = 1 976. In der Toleranz: 2 000, 1 900, 2 080, 2 200. Außerhalb: 200, 20 000, 90, 1 500, 2 400.  
Häufigste falsche Antwort (Annahme): 200 – eine Null vergessen (40 · 50 als 4 · 50)  
Tipp: Runde beide Zahlen auf Zehner.

**U4 · Muster M3 · schwer (`begruenden`) · `auswahl`**  
Text: „45 · 65 soll überschlagen werden. Welche Rechnung liegt am nächsten am genauen Ergebnis?“  
Auswahl: 50 · 70 | **50 · 60** | 40 · 60  
Weg 1: Abstände zu 2 925: 575, 75, 525.  
Weg 2: Repo-Rechner: 50 · 70 = 3 500, 50 · 60 = 3 000, 40 · 60 = 2 400.  
Häufigste falsche Antwort (Annahme): „50 · 70“ – rundet beide nach der Schulregel auf  
Tipp: Wenn du beide Zahlen aufrundest, wird das Ergebnis zu groß. Was passiert, wenn du eine auf- und eine abrundest?

### Etappe `schriftlich_geteilt`

**S1 · Muster M4 · schwer (`fehler`) · `auswahl` + `tabelle`**  
Text: „Jemand rechnet 3 888 : 16 schriftlich und erhält 241 Rest 12. In welcher Zeile entsteht der Fehler?“  
Tabelle: Zeile 1: 38 : 16 = 2, 2 · 16 = 32, Rest 6 · Zeile 2: 68 : 16 = 4, 4 · 16 = 64, Rest 2 · Zeile 3: 28 : 16 = 1, 1 · 16 = 16, Rest 12  
Auswahl: Zeile 1 | **Zeile 2** | Zeile 3 | Alles richtig.  
Weg 1: Schritt für Schritt: 38 : 16 = 2 Rest 6; 68 : 16 = 4 Rest 4; 48 : 16 = 3 Rest 0 → 243.  
Weg 2: Repo-Rechner, Probe: 243 · 16 = 3 888; die falsche Lösung ergibt 241 · 16 + 12 = 3 868.  
Häufigste falsche Antwort (Annahme): „Zeile 3“ – dort sieht die Rechnung fremd aus (28 statt 48), der Fehler entsteht aber davor  
Tipp: Prüfe in jeder Zeile die Minus-Rechnung: Zahl minus Produkt gleich Rest?

**S2 · Muster M4 · schwer (`begruenden`) · `auswahl` + `tabelle`**  
Text: „Jemand rechnet 3 264 : 16 = 24. Was ist schiefgegangen?“  
Tabelle: Zeile 1: 32 : 16 = 2, Rest 0 · Zeile 2: 6 herunterholen: 6 : 16 geht nicht, also gleich die 4 dazuholen · Zeile 3: 64 : 16 = 4, Rest 0 · Zeile 4: Ergebnis: 24  
Auswahl: In Zeile 1: 32 : 16 ist nicht 2. | **In Zeile 2: Für „geht nicht“ fehlt eine 0 im Ergebnis.** | In Zeile 3: 64 : 16 ist nicht 4. | Nichts, 24 stimmt.  
Weg 1: Schritt für Schritt: 32 : 16 = 2; 6 : 16 = 0 Rest 6; 64 : 16 = 4 → 204.  
Weg 2: Repo-Rechner, Probe: 204 · 16 = 3 264; 24 · 16 = 384.  
Häufigste falsche Antwort (Annahme): „Nichts, 24 stimmt.“ – jede Zeile sieht für sich richtig aus  
Tipp: Mach die Probe im Kopf: Ist 24 · 16 ungefähr 3 000?

**S3 · Muster M5 · mittel (`darstellung`) · `markierung`**  
Text: „Bevor du schriftlich teilst: Tippe den Strich an, der am nächsten an 8 190 : 39 liegt.“  
Zahlenstrahl: 0 bis 500 in 10 Abschnitten, nur Anfang und Ende beschriftet  
Lösung: Strich 4  
Weg 1: 8 000 : 40 = 200 = 4 · 50.  
Weg 2: Repo-Rechner: 8 190 : 39 = 210, Abstand zum 4. Strich 10 (von 50).  
Häufigste falsche Antwort (Annahme): Strich bei 0 (21) – eine Stelle verloren  
Tipp: Runde beide Zahlen so, dass eine Aufgabe aus dem Einmaleins entsteht.

**S4 · Muster M6 · mittel (`umkehr`) · `zahl`**  
Text: „Ohne zu teilen: Wie viele Stellen hat das Ergebnis von 7 344 : 24?“  
Lösung: 3  
Weg 1: 7 344 : 24 = 306, drei Stellen.  
Weg 2: Schranken: 2 400 ≤ 7 344 < 24 000, also 100 ≤ Ergebnis < 1 000.  
Häufigste falsche Antwort (Annahme): 2 – zählt die Stellen von 7 344 minus die Stellen von 24  
Tipp: Vergleiche 7 344 mit 24 · 100 und mit 24 · 1 000.

<!-- AUFGABEN:ENDE -->

## 4. Nicht geprüft, Annahmen

**Nicht geprüft**
- Die ganze Themen-Datei mit `tools/inhalt_pruefen.py` (die Aufgaben sind nicht in `zahlen.rechengesetze.json` eingebaut – das macht der Aufgaben-Ersteller bzw. der Projektleiter). Geprüft ist je Aufgabe die Antwortform mit `pruefe_antwort` [G].
- Wie die Tabelle mit langen Zeilen (S1, S2) am Handy umbricht.
- Ob die App bei `zahl` mit `toleranz` nach einer richtigen Schätzung den genauen Wert zeigt (für M6 erwünscht).

**Annahmen**
- Alle „häufigsten falschen Antworten“.
- 15 % Toleranz bei M6 und die 30-%-Grenze bei M5 sind von mir gesetzt, nicht aus Daten abgeleitet.

**Versuchsdaten:** Mit Erlaubnis des Nutzers am 25.11. gesichtet (nur Summen, ohne Namen). Ergebnisse stehen nach Teamregel nicht im Repo. Für diese Ablage folgt daraus nur: Keine der Fehler-Annahmen in `auftrag2.md` und hier ist damit belegt – sie bleiben Annahmen.
