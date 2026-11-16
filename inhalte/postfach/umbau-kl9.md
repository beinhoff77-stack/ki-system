# Postfach umbau-kl9 (Achte Runde: Umbau der Lernkarten auf das neue Muster, Klasse 9)

Neueste Meldung oben.

## 2026-11-16 03:15 – FERTIG: Paket U9 (Zweig umbau-kl9, nicht gemergt)

| Thema | Karten | mit fehler_bild | Aufgaben | Unterschiede zu lernen-app | inhalt_pruefen Fehler / Hinweise |
|---|---|---|---|---|---|
| zahlen.wurzeln_basis | 6 | 4 | 168 | 0 | 0 / 0 |
| zahlen.reell | 6 | 4 | 168 | 0 | 0 / 0 |
| zahlen.rationale_exponenten | 6 | 5 | 168 | 0 | 0 / 0 |
| gleichungen.quadratisch | 7 | 2 | 196 | 0 | 0 / 0 |
| gleichungen.potenz | 6 | 4 | 168 | 0 | 0 / 0 |
| gleichungen.lgs3 | 6 | 4 | 168 | 0 | 0 / 0 |
| funktionen.quadratisch | 7 | 3 | 196 | 0 | 0 / 0 |
| funktionen.potenz | 6 | 2 | 168 | 0 | 0 / 0 |
| abbildungen.aehnlichkeit | 6 | 5 | 168 | 0 | 0 / 0 |
| trigo.pythagoras | 6 | 3 | 168 | 0 | 0 / 0 |
| trigo.rechtwinklig | 6 | 3 | 168 | 0 | 0 / 0 |
| trigo.allgemein | 7 | 2 | 196 | 0 | 0 / 0 |
| gleichungen.trig | 6 | 3 | 168 | 0 | 0 / 0 |
| stochastik.verknuepft | 6 | 1 | 168 | 0 | 0 / 0 |
| **Summe** | **87** | **45** | **2436** | **0** | **0 / 0** |

- Jede Karte hat einstieg (≤ 35 Wörter), woerter (≤ 3, jedes kommt in einstieg oder schritten vor), Kartenbild, 2–5 Schritte als {text, bild} mit Bild je Bildänderung, fehler, regel (erster Satz ≤ 12 Wörter als „Kurz gesagt“). Die alte probe ist weg.
- Technik: UMBAU-Abschnitt je Generator hinter KLAR; `umbau()` in `_kl9.py`. Für den Dopplungsabgleich gelten weiter die alten Beispielschritte, darum sind alle Aufgaben wörtlich gleich (Vergleich jeder Aufgabe als JSON gegen `origin/lernen-app`). Titel und Lernziele unverändert.
- Nur vorhandene Zeichnungsarten (koordinaten, figur, tabelle, zahlenstrahl mit punkte/boegen/bereich, bruchstreifen). Neu benutzt: Graph `potenz` mit n = 1/3 für ∛x (rechnet die App mit x ** n, für x ≥ 0 korrekt).
- Gerendert mit `lernErklaerung` aus lernen.js (Playwright, 820 px): alle 87 Karten ohne JS-Fehler, Stichproben angesehen. Kein fehlendes Kartenbild, darum kein Eintrag unter „offen“.
- Ohne fehler_bild bleiben Karten, deren Fehler ein Rechen-, Vorzeichen- oder Deutungsfehler ist, den ein Bild nicht zeigt (Einzelheiten in den STATUS-Meldungen).
- Situationen je Thema: Teppich/Würfel, Beete, Bakterien, Fliesen/Gemüsebeet, Zahlenautomat, Kiosk/Bonbons, Skaterbahn/Springbrunnen, Rechenmaschine, Schattenspiel/Foto, Beet/Leiter/Schachtel, Rampe, Uhrzeiger/Wanderung, Riesenrad, Schulfest. Alle Zahlen nachgerechnet.
- Annahmen: Sätze ≤ 15 Wörter, weil das Prüfskript den kleinsten Wert aus `klasse` nimmt – hier die IB-MYP-Stufe 3 oder 4, nicht Klasse 9. Vermutlich unbeabsichtigt (App-Wunsch: gym_by maßgeblich machen); kürzere Sätze schaden aber nicht. Beispiele der Karten teils angepasst, damit Bild und Beispiel zusammenpassen (z. B. ∛8 statt ∛64, Einheitskreis-Schritte); die Aufgaben sind davon nicht berührt.
- Hinweis: Laut AUFTRAEGE.md sollte U9 erst nach dem Test mit den Kindern starten; Sebastian hat das Paket direkt beauftragt.
- Offene Fragen: keine. Kein Merge.

## 2026-11-16 03:14 – STATUS
stochastik.verknuepft umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator (umbau() in _kl9.py).
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/stochastik.verknuepft.json`: 168 Aufgaben, alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: verknuepfen, additionssatz, tafel_wkeit, bedingt, verstehen (Deutungsfehler, im Bild nicht sinnvoll zu zeigen).

## 2026-11-16 03:13 – STATUS
gleichungen.trig umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator (umbau() in _kl9.py).
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/gleichungen.trig.json`: 168 Aufgaben, alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: tangens, umformen, anwendung (Rechen- bzw. Prüffehler, im Bild nicht sinnvoll zu zeigen).

## 2026-11-16 03:12 – STATUS
trigo.allgemein umgebaut (7 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator (umbau() in _kl9.py).
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/trigo.allgemein.json`: 196 Aufgaben, alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: einheitskreis, flaeche, sinussatz_winkel, kosinussatz_winkel, satz_waehlen (Vorzeichen- bzw. Auswahlfehler, im Bild nicht sinnvoll zu zeigen).

## 2026-11-16 03:11 – STATUS
trigo.rechtwinklig umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator (umbau() in _kl9.py).
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/trigo.rechtwinklig.json`: 168 Aufgaben, alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: verhaeltnisse, winkel, beziehungen (Rechenfehler, im Bild nicht sinnvoll zu zeigen).

## 2026-11-16 03:10 – STATUS
trigo.pythagoras umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator (umbau() in _kl9.py).
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/trigo.pythagoras.json`: 168 Aufgaben, alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: hypotenuse, umkehrung, raum (Rechen- bzw. Zuordnungsfehler, im Bild nicht sinnvoll zu zeigen).

## 2026-11-16 03:09 – STATUS
abbildungen.aehnlichkeit umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator (umbau() in _kl9.py).
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/abbildungen.aehnlichkeit.json`: 168 Aufgaben, alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: flaeche_volumen (das Kartenbild zeigt den Fehler schon).

## 2026-11-16 03:07 – STATUS
funktionen.potenz umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator (umbau() in _kl9.py).
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/funktionen.potenz.json`: 168 Aufgaben, alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: werte, parameter, negativ, wurzelfunktion (Rechenfehler, im Bild nicht sinnvoll zu zeigen).

## 2026-11-16 03:06 – STATUS
funktionen.quadratisch umgebaut (7 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator (umbau() in _kl9.py).
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/funktionen.quadratisch.json`: 196 Aufgaben, alle wörtlich gleich. inhalt_pruefen: 0 Fehler, 0 Hinweise. Ohne fehler_bild: scheitel, punkte, bestimmen, extremwert (Ablese- bzw. Rechenfehler, im Bild nicht sinnvoll zu zeigen).

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
