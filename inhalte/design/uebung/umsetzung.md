# Vorgabe ÜB: Übungsbildschirm am Handy (360 und 400 px)

Designer, 26.11.2026. Kein App-Code, keine Datenbank. Entwurf zum Anklicken: `entwurf/uebung.html` (eine Datei, kein Nachladen; oben rechts wählt man den Zustand, Adresse `?s=m3-hinweis&g=hell`). Bilder: `bilder/`.
Grundlage: `inhalte/recherche/tief-11-bedienung-eltern.md` Lieferung 2 und Lieferung 5 Punkte 1, 2, 7; `inhalte/plan/bedingung-format.md`; Nachtrag „Regel dahinter“.
**[G]** im Entwurf gebaut und gemessen · **[A]** Annahme · **[M]** Meinung. Farben sind die der App („Abflug“ hell und dunkel).

## 1 Aufbau von oben nach unten [G]
| Teil | Maße | Inhalt |
|---|---|---|
| Kopf, **eine Zeile** | 48 px hoch | links „×“ (Tippfläche 48 px, Kreis 34 px; Tipp fragt „Pause? Dein Stand bleibt.“) · Mitte **die einzige Fortschrittsleiste**: Segmente 8 px hoch, Abstand 5 px, fertig = gelb, aktuell = gelb mit Ring in Textfarbe · rechts „?“ (öffnet die Erklärung) |
| Kontextzeile | 14 px, leise, eine Zeile, abgeschnitten mit „…“ | „Rom · Negative Zahlen · Etappe 1 von 3“. Kein Knopf, kein Zähler. |
| Aufgabe | Karte, Rand 1,5 px, Radius 16, Innenabstand 12/14, Text 19 px halbfett, Rechnung 24 px Festbreite | höchstens vier Zeilen, danach rollt die Karte in sich |
| Antwortfeld(er) | 56 px hoch (bei fünf und sechs Feldern 50 px), Radius 14, Rand 2 px, Ziffern 26 px Festbreite, Abstand 8 px | direkt unter der Aufgabe |
| Hinweis (nur nach Fehlversuch) | Rand 2 px, Radius 14, zwei bis drei Zeilen 17 px | zwischen Feldern und Tastatur |
| Tastatur | **255 px** hoch; 4 Spalten × 4 Reihen, Tasten 52 px hoch, mindestens 78 px breit (360 px), Abstand 8 px, Ziffern 23 px | unten fest |

Weg fallen: Menü-Zeile, Reiter Erklären | Üben | Fehler, Etappenleiste mit Pfeilen, weitere Zähler, Etikett „Bordkarte“.

## 2 Tastatur [G]
```
1  2  3  ⌫
4  5  6  −      ← nur wenn die Aufgabe negative Zahlen braucht
7  8  9  ,      ← nur wenn Dezimalzahlen erlaubt sind
0     /  [Prüfen]   („/“ nur bei Brüchen; sonst ist die 0 doppelt breit)
```
- Die Ziffern stehen **immer an derselben Stelle**. Eine nicht gebrauchte Sondertaste fehlt, ihr Platz bleibt leer (Bild `start-und-sondertasten-360-hell`, rechts mit allen drei).
- „−“ schaltet das Vorzeichen des aktiven Feldes um. Höchstens 6 Ziffern je Feld im Entwurf [A; das Format erlaubt 14 Zeichen – ab 6 Zeichen schrumpft die Schrift auf 19 px].
- **Ein Hauptknopf**, gelb, doppelt breit: „Prüfen“.
- Aufgabe und Feld bleiben über der Tastatur: Die Seite ist eine Spalte in voller Bildschirmhöhe (`100dvh`), die Tastatur gehört zur Seite (keine System-Tastatur), nur die Mitte rollt. Gemessen bei 360 × 640: ein Feld 155 px Luft über der Tastatur, drei Felder 138 px, sechs Felder 112 px.

## 3 Mehrere Zahlenfelder (2 bis 6) [G]
- Anordnung: 2 Felder nebeneinander · 3 in einer Reihe · 4 als 2 × 2 · 5 und 6 als zwei Reihen zu drei. Jedes Feld trägt klein (13 px) seine Nummer oben links.
- **Aktives Feld:** Rand 3 px in Blau (hell #1F5FBF, dunkel #7CB7FF), weicher Ring 3 px, blinkende Schreibmarke. Das ist das einzige blaue Element auf dem Bildschirm.
- **Weiterspringen:** Der Hauptknopf heißt „Nächstes Feld“, solange noch ein Feld leer ist und im aktiven etwas steht; er springt ins nächste leere Feld. Sind alle Felder gefüllt, heißt er „Prüfen“. Antippen eines Feldes macht es aktiv. „⌫“ im leeren Feld springt ein Feld zurück.
- Sechs Felder auf 360 × 640: Bild `m6-360-dunkel`. Mit Hinweis rollt die Aufgabe 8 px nach oben; Felder und Hinweis bleiben ganz sichtbar.

## 4 Rückmeldung [G]
Immer **Symbol, Wort und Farbe zugleich**. Sachlich, keine Sticker, kein Alarmrot.

| Zustand | Wo | Was steht da |
|---|---|---|
| Fehlversuch bei mehreren Feldern | Hinweis-Kasten über der Tastatur; Tastatur bleibt, Felder bleiben änderbar | halb gefüllter Kreis · „**Noch nicht: Summe ist 0**“ (Name der verletzten Bedingung) · „Deine Summe ist 1. Ändere deine Zahlen. Noch 1 Versuch.“ |
| richtig | Blatt von unten, Tastatur weg; grün (hell Fläche #E4F3E9, Rand #1E7A46; dunkel #12261B, #4FBF7B) | Haken im Kreis · „**Richtig**“ · bei mehreren Feldern die Namen aller Bedingungen mit Haken · Knopf „Weiter“ |
| endgültig falsch, ein Feld | Blatt, warm (hell #FFF3CF, Rand #9A7400; dunkel #2A2414, #E0B63A); die Antwort bleibt oben im Feld stehen | halb gefüllter Kreis · „**Nicht ganz**“ · „Richtig wäre: 5“ · Kasten „Kurzregel“ · Feld „Regel dahinter“ · „Weiter“ |
| endgültig falsch, mehrere Felder | Blatt, warm | „**Nicht ganz**“ · „Deine Zahlen: 4, −1, −2“ · verletzte Bedingung mit Hinweis · „**Zum Beispiel: 5, −2, −3**“ · Kasten „Alle Bedingungen“ (die verletzte fett mit Pfeil) · „Regel dahinter“ · „Weiter“ |

Das Kind sieht nur, was der Server laut Format herausgibt: Name und Hinweis der ersten verletzten Bedingung, am Ende das Beispiel und die Namen aller Bedingungen.
„Prüfen“ zeigt nach 1 s ein Arbeitszeichen im Knopf, nach 10 s „Verbindung langsam. Antwort gespeichert.“ [nicht gebaut]

## 5 Feld „Regel dahinter“ (Nachtrag) [G]
- Feld: mindestens 56 px hoch, links gelber Balken 6 px, Zeile „REGEL DAHINTER“ (13 px, Versalien), darunter der Merksatz (17 px fett), rechts „›“. Steht in der Erklärung, im Lösungsweg und im Blatt „Nicht ganz“.
- Tipp öffnet die Regel als **Blatt über der Seite** (92 % der Höhe): Regel-Nummer und Name, Merksatz, „Genau gesagt“, die Zeichnung aus dem Regel-Universum. Hauptknopf „Zurück zur Aufgabe“ oder „Zurück zur Erklärung“, darunter „Im Regel-Universum ansehen ›“.
- **Rückweg:** Schließen (Knopf, „×“ oder Tipp daneben) führt an dieselbe Stelle, auf dieselbe Rollhöhe; Eingaben und Übungsstand bleiben. Bilder `regel-dahinter-360-hell`, `regel-dahinter-400-dunkel`.

## 6 Schalter „am Tisch / nur am Handy“ [G]
Erste Seite einer Sitzung: Frage „Wo übst du heute?“, zwei große Wahlflächen (mindestens 72 px, gewählt = blauer Rand 3 px und gefüllter Punkt), darunter „Am Tisch diese Woche: 1 von 3“ mit drei Punkten, unten der eine Hauptknopf „Los“.

## 7 Prüfliste
**Muss**
1. Aufgabe und alle Felder sind bei 360 × 640 mit offener Tastatur ganz sichtbar.
2. Kopf eine Zeile, genau eine Fortschrittsleiste.
3. Sondertasten nur, wenn die Aufgabe sie braucht; Ziffern wandern nie.
4. Genau ein gelber Hauptknopf je Zustand.
5. Aktives Feld eindeutig; „Nächstes Feld“ springt ins nächste leere Feld.
6. Fehlversuch: Name der Bedingung und Hinweis, Felder bleiben änderbar.
7. Ende: „Zum Beispiel: …“; die eigene Antwort bleibt lesbar.
8. Jede Rückmeldung mit Symbol, Wort und Farbe.
9. „Regel dahinter“: Blatt auf, Blatt zu, gleiche Stelle, Stand erhalten.
10. Keine Schrift unter 13 px, Tippflächen mindestens 48 px. Hell und dunkel.

**Soll:** Arbeitszeichen nach 1 s · Rückfrage bei „×“ · Blatt fährt in 0,2 s ein, bei „Bewegung reduzieren“ ohne Bewegung.
**Kann:** Querformat zweigeteilt (Aufgabe links, Tastatur rechts).

## 8 Annahmen und nicht geprüft
- [A] Zwei Versuche bei Aufgaben mit Bedingungen, einer bei einem Feld. Die Zahl kommt aus der App-Regel, nicht von mir.
- [A] Fünf Segmente in der Leiste; Ort, Thema und Etappe in der Kontextzeile sind erfunden. Erfunden sind auch die Aufgaben „3 − (−2)“ und „sechs Zahlen“, die Kurzregel, der Erklärtext und „1 von 3“.
- [A] Welche Regel hinter einer Aufgabe steht, legt der Mathe-Profi fest (Auftrag 14 Teil A); im Entwurf ist es überall Rechenregel 2.
- **Nicht geprüft:** echtes Handy; Bildschirme niedriger als 640 px; System-Schriftvergrößerung; Kontrastwerte nachgerechnet; Vorlesefunktion; ob `100dvh` in der App-Hülle so greift; Verhalten bei fünf Feldern mit langen Zahlen.
- Gemessen in Chrome bei 360 × 640 und 400 × 800, hell und dunkel, 19 Zustände: kein Querrollen, kleinste Schrift 13 px, kleinste Taste 52 px, keine Skriptfehler.
