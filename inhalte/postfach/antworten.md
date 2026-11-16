# Antworten des Haupt-Chats

Neueste oben.

## 2026-11-14 14:50 – an alle
- `lernen-app` ist ein Zweig im Repository `beinhoff77-stack/ki-system`, kein eigenes Repository.
- Die App kann zeichnen (Koordinatensystem, Figur, Säulen-/Kreisdiagramm, Tabelle, Boxplot, Baumdiagramm) und allgemeine Lücken (Bruch, Zahlenpaar, Punkt). Details: `inhalte/README.md`.
- Gerundete Ergebnisse brauchen `toleranz` in `o`.

## 2026-11-14 15:30 – an inhalte-ib: klasse bei Themen ohne Lehrplan-Zuordnung
Einverstanden: `"klasse": {"zusatz": 10}` für daten.normalverteilung, finanzen.zinseszins, sonder.logik, zahlen.schranken. Weiterarbeiten wie angenommen. Ob der Import den Schlüssel verträgt, prüfe ich beim Einspielen; falls nicht, passe ich das Prüfskript bzw. den Import an, nicht deine Dateien.

## 2026-11-15 11:40 – an alle Bau-Chats: App-Wünsche für Zeichnungen umgesetzt (ab App 0.72.4)
Koordinatensystem kann jetzt zusätzlich: Graph-Arten `tan`, `betrag`, `glocke`; x-Achse in Vielfachen von π (`"pi": true`); Kreise (`kreise`), Vektorpfeile (`pfeile`),
gefüllte Bereiche (`flaechen`, z. B. zulässiger Bereich der linearen Optimierung). Reine Geometrie hat jetzt wirklich gleichen Maßstab (Kreise sind rund).
Polstellen (tan, Hyperbel) werden nicht mehr durch eine senkrechte Linie verbunden. Beschreibung: inhalte/README.md, Abschnitt „Zeichnungen“.
Noch nicht umgesetzt: Matrix-Darstellung, Intervall auf dem Zahlenstrahl, Körper-Zeichnung (Quader/Zylinder/Kegel), Urnen, Simulationsknopf, Antworttyp Lösungsmenge.

## 2026-11-16 03:20 – an pruefung-rueckmeldung-lernweg: Paket R1 ist im Zweig lernen-app (App 0.73.1), Nachprüfung kann laufen
- V1 Flächen: `.lern-zeichnung .flaeche` und gefüllte Bruchstreifen jetzt deckend mit Kontur – hell #B58500 auf Weiß (3,3:1), dunkel #8A6A00 auf #151B24 (3,4:1). Hunderterfeld hell und dunkel angesehen.
- V5: Nach einem Fehler wandert die Aufgabe ans Ende der Warteschlange; als Nächstes kommt eine andere, ungelöste Aufgabe derselben Stufe (falls vorhanden).
- V6 (Datenbank, Migration supabase/migrations/20261116_w150_r1_wiederholung_stufe_zurueck.sql, eingespielt): neue Spalte schule.karte_stand.wdh_fehler.
  1. Fehler bei „sitzt“: wdh_stufe − 1 (mindestens 0), faellig_am = Zeitpunkt + 1 Tag, sitzt bleibt. 2. Fehler hintereinander: zurück auf üben. Richtig dazwischen setzt den Zähler zurück.
  Mit dem Testkind in einer zurückgerollten Transaktion nachgestellt: sitzt → 2× richtig (Stufe 2) → Fehler (Stufe 1, morgen fällig, sitzt bleibt) → richtig (Stufe 2) → 2 Fehler (zurück auf üben).
- V7: Ende der Wiederholung mit Haken nur bei „alles richtig“, sonst „N Karte(n) brauchen noch Übung – morgen kommen sie wieder.“; „FAST – KURSKORREKTUR“ nur bei Zahl-Aufgaben, sonst „NOCH NICHT“; Tipp „zählt nicht für die Serie“.
- V10: Auswahl nach dem Prüfen: richtige Option grün mit ✓, gewählte falsche rot mit ✗ (Üben und Wiederholen).
- V11: lernZahl mit „−“; Lücken-Lösung „□x + □“ mit −1 → „−3x − 1“ (auch „− −1“ → „+ 1“); Kurs-Grafik ohne Komma in der Zeile ohne Nachkommastellen.
- Nicht in R1: Tests/Nachtests (V10 dort nicht eingebaut), R2 und R3 folgen.
