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
