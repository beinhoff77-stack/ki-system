# Postfach umbau-kl9 (Achte Runde: Umbau der Lernkarten auf das neue Muster, Klasse 9)

Neueste Meldung oben.

## 2026-11-16 03:05 – STATUS
gleichungen.lgs3 umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator (umbau() in _kl9.py).
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/gleichungen.lgs3.json`: 168 Aufgaben, alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: loesen, sachaufgabe (Fehler im Vorgehen bzw. beim Übersetzen, im Bild nicht sinnvoll zu zeigen).

## 2026-11-16 03:03 – STATUS
gleichungen.potenz umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator (umbau() in _kl9.py).
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/gleichungen.potenz.json`: 168 Aufgaben, alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: ungerade, sachaufgabe (Fehler ohne sinnvolles Bild).

## 2026-11-16 03:02 – STATUS
gleichungen.quadratisch umgebaut (7 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator (umbau() in _kl9.py).
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/gleichungen.quadratisch.json`: 196 Aufgaben, alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: reinquadratisch, faktorisieren, ergaenzung, loesungsformel, diskriminante (Rechen- oder Vorzeichenfehler, im Bild nicht sinnvoll zu zeigen).

## 2026-11-16 03:00 – STATUS
zahlen.rationale_exponenten umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator (umbau() in _kl9.py).
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/zahlen.rationale_exponenten.json`: 168 Aufgaben, alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: verstehen (Rechenfehler, im Bild nicht sinnvoll zu zeigen).

## 2026-11-16 02:58 – STATUS
zahlen.reell umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator (umbau() in _kl9.py).
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/zahlen.reell.json`: 168 Aufgaben, alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: zusammenfassen, nenner_rational (Rechenfehler, im Bild nicht sinnvoll zu zeigen).

## 2026-11-16 02:56 – STATUS
zahlen.wurzeln_basis umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator (umbau() in _kl9.py).
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/zahlen.wurzeln_basis.json`: 168 Aufgaben, alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: wurzel_deuten, wurzel_sache (Rechenfehler, im Bild nicht sinnvoll zu zeigen).

## 2026-11-16 02:50 – STATUS
Start Paket U9 auf Auftrag von Sebastian (16.11.). Hinweis: Laut AUFTRAEGE.md sollte U9 erst nach dem Test mit den Kindern starten; Sebastian hat das Paket direkt beauftragt, ich werte das als Freigabe.
Technik: `_kl9.py` hat jetzt `umbau(ETAPPEN, UMBAU)`. Es läuft nach `klar()` und legt die neuen Erklärfelder über die Karten. Für den Dopplungsabgleich bleiben die alten Beispielschritte (ALT_SCHRITTE) maßgeblich, darum bleiben alle Aufgaben wörtlich gleich. Die alte `probe` fällt weg.
