# Postfach pruefung-neu-1 (Fünfundzwanzigste Runde, unabhängige Prüfung)

Neueste Meldung oben. Prüfer: Chat `pruefung-neu-1`, hat keines der geprüften Themen geschrieben.

Allgemein gilt für alle Berichte:
- „Nachgerechnet“ heißt: Lösung unabhängig vom Generator bestimmt – entweder mit einem eigenen Prüfskript, das die Zahlen aus dem **Fragetext** liest und neu rechnet (nicht aus `c`), oder von Hand.
- Übungen ohne `g` sind laut Zwanzigster Runde „überzählig“ und werden beim Einspielen gesperrt. Sie wurden auf richtige Lösung (a) geprüft, nicht auf Stufe/Typ (f).
- Lehrplan: Die Seiten von lehrplanplus.bayern.de konnte ich in dieser Sitzung nicht direkt abrufen (Abruf brauchte eine Freigabe, die nicht beantwortet wurde). Lehrplanaussagen stützen sich daher auf `lehrplan_andere` in `themenliste.json` und auf ISB-Dokumente aus der Websuche (Abruf 20.11.2026); was nicht belegt ist, steht als Annahme da.

## 2026-11-20 – daten.stichproben (RS 7, IB MYP 2): mit Korrekturen in Ordnung

**Gelesen und nachgerechnet (Fakt):** 5 Lernkarten und alle 188 Aufgaben (128 Übungen, 10 Knobel, 5 Test, 15 Korrektur, 30 Sicherung). Alle 74 Zahl-Aufgaben von Hand nachgerechnet (Hochrechnung, Prozentpunkte, Spannweite, Fang-Wiederfang, geschichtete Stichprobe, Knobel 37 %/43 %/Würfelmethode) – keine falsche Zahl. Alle 114 Auswahl-Aufgaben einzeln auf „genau eine vertretbare Antwort“ gelesen; dabei die Fehler unten gefunden.

**Änderungen je Fehlerart:** a) 10 · b) 3 · c) 0 · d) 2 · e) 7 · f) 2 (in a enthalten)

a) Zweite vertretbare Antwort:
- **Test** `repraesentativ`: „… werden 100 Personen befragt: nur die Besucher des alten Hallenbads. Warum ist das keine geeignete Stichprobe?“ – alte Optionen: „Eine einseitige Gruppe wird befragt.“ / „Fans der Bahn sind zu stark vertreten.“ / „Wer die Kantine meidet, fehlt.“ / richtig „Schwimmer sind eher dafür.“ Die erste Option ist ebenfalls richtig. Neu: „100 Personen sind zu viele.“ / „Verärgerte sind zu stark vertreten.“ / „Man darf nie nur einen Teil befragen, nur alle.“ / richtig „Schwimmer sind eher dafür.“ Ursache im Generator: Falschantworten kamen aus den Gründen anderer Szenen, darunter allgemeine („eine einseitige Gruppe …“, „nur eine Altersgruppe …“), die auf jede schlechte Auswahl passen. Jetzt zwei echte Denkfehler plus ein fremder „… zu stark vertreten“-Grund (betrifft auch 1 Übung und 5 Sicherungen, siehe e).
- „Nur Freiwillige antworten“ (4 Übungen, 1 Korrektur, 1 Sicherung): alt z. B. „Eine Zeitschrift ruft ihre Leser auf, im Internet zum Thema „Handyverbot an Schulen“ abzustimmen. Es kommen 9 000 Antworten. Welche Fehlerquelle liegt vor?“ – „Die Auswahl ist einseitig“ war ebenfalls vertretbar (nur Leser/Hörer/wer an der Schultür vorbeikommt, die Grundgesamtheit war offen). Neu: „Eine Zeitschrift will wissen, was ihre Leser zum Thema „Handyverbot an Schulen“ denken, und ruft sie auf, im Internet abzustimmen. …“ (ebenso Radiosender: „… will wissen, was seine Hörer … denken, und bittet sie anzurufen.“; Schule: „Eine Schule will wissen, was ihre Kinder zum Thema … denken. An der Schultür hängt ein Zettel: Wer möchte, wirft seine Meinung in den Briefkasten.“). Lösung bleibt „Nur Freiwillige antworten.“
- „Wie verbessert man die Umfrage am wirksamsten?“ bei einseitiger Auswahl bzw. Freiwilligen (4 Übungen): Falschoption „Mehr Personen zufällig auswählen.“ war ebenfalls eine Verbesserung. Neu: „Einfach mehr Personen auf dieselbe Art befragen.“ (der echte Denkfehler „größer = besser“). Bei „Stichprobe zu klein“ bleibt „Mehr Personen zufällig auswählen.“ die richtige Antwort.

b) „Es sollen genau 60 Personen werden.“ → „… befragt werden.“; „Finden Sie nicht auch, dass der Spielplatz erneuert wird?“ / „… dass mehr Radwege gebaut werden?“ → „Finden Sie nicht auch, dass es gut wäre, wenn …?“ (Satz war schief, Fehlerquelle bleibt suggestiv).
d) Karte `begriffe`: „Vollerhebung“ kam in 9 Aufgaben (davon 5 Korrektur/Sicherung) vor, wurde aber nicht erklärt → Regel ergänzt: „Befragt man alle, heißt das ⟦Vollerhebung⟧.“ Karte `hochrechnen`: „Prozentpunkte“ in 2 Aufgaben, erklärt erst in der späteren Karte `aussagen` → Wort ergänzt.
e) 6 Auswahl-Aufgaben „Warum ist das keine geeignete Stichprobe?“ hatten Falschantworten ohne Bezug zur Frage („Sie sind gar nicht wahlberechtigt“ bei Busfahrgästen) – siehe a). Knobel „gerundet 43 %“: Lösungsweg nannte 14 % und 29 % als Werte für n ≤ 6 (das sind 1/7 und 2/7) – berichtigt.
f) Schul-Briefkasten mit 9 000 bzw. 3 500 Antworten unrealistisch → 450 bzw. 350.

**Lehrplan:** Passt zu RS 7 („Stichprobeneignung/Repräsentativität beurteilen“, `lehrplan_andere`); die Hochrechnung ist laut `offen` bewusst ergänzt (Meinung: sinnvoll, nicht zu schwer). IB MYP 2: Annahme, nicht gegen das IB-Dokument geprüft. Nichts Wesentliches fehlt.

**Nicht geprüft:** Säulen- und Bruchstreifenbilder nur im JSON gelesen. Übungen ohne `g` (10, gesperrt) nur auf Lösung geprüft.

Prüfskript: OK, 0 Gruppen „gleich gebaut hintereinander“. Zufallsfolge des Generators beibehalten: Außer den genannten Aufgaben hat sich keine Aufgabe geändert (Vergleich alt/neu).

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
