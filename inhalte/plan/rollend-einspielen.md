# Vorrats-Aufgaben einspielen (rollend-1 bis -8) – Vorbereitung, nichts eingespielt

Stand 27.11.2026. Werkzeug: `tools/rollend_sql.py` (ohne Schalter: Übersicht und Prüfung; `--sql`: ein selbstprüfendes SQL). Test: `python3 -I tools/tests/rollend_sql_test.py` (endet mit OK).
Der Abschnitt „Befund“ unten beschreibt den Stand der Runden 1 und 2 vom 27.11. früh; die Zahlen aller Pakete stehen im Abschnitt „Pakete“.

## Pakete (Stand Werkzeug-Erweiterung, 27.11.2026)
Jedes Paket ist ein eigenes SQL (eine Transaktion, selbstprüfend). Aufrufe (im Repo-Wurzelverzeichnis; `> x.sql` für die Datei):

| Paket | Aufruf | Aufgaben | Einheiten | Hinweis |
|---|---|---|---|---|
| Altbestand, Runden 1-4 | `python3 -I tools/rollend_sql.py --mit-bedingung --sql` (Vorgabe = `--runden 1,2,3,4`) | 633 | 22 | gleiche Daten wie vor der Erweiterung; ohne `--mit-bedingung` 553 Aufgaben (80 vom Typ „bedingung“ bleiben liegen) |
| rollend-5 (Klasse 5, K5A) | `python3 -I tools/rollend_sql.py --runden 5 --sql` | 174 | 6 | 28 Lückenwege `zaehlt = nein`, 146 `ja` |
| rollend-7 (Klasse 8, K8) | `python3 -I tools/rollend_sql.py --runden 7 --sql` | 183 | 11 | 50 `nein`, 133 `ja` |
| rollend-8 (Klasse 7, K7) | `python3 -I tools/rollend_sql.py --runden 8 --sql` | 156 | 10 | 33 `nein`, 123 `ja`; `form` fehlt in den Dateien, kommt aus `typ` |
| alles | `python3 -I tools/rollend_sql.py --runden alle --mit-bedingung --sql` | 1146 | 49 | zu groß für einen Aufruf, nur zur Kontrolle |

- Jede Runde einzeln prüfen: `python3 -I tools/rollend_sql.py --runden 5` (Übersicht je Runde: Aufgaben, Einheiten, Form- und `zaehlt`-Verteilung, Zahl der Aufgaben mit `t` nicht in `tf`).
- Einzelne Aufgaben herausnehmen: `--ohne K5A-V009,K8-V070` (unbekannte Kennung = Abbruch). Die Nummern der übrigen ändern sich dadurch nicht.
- Die Zeile „`bedingung` liegen geblieben“ gilt nur für Runden 1-4; die Runden 5, 7, 8 enthalten keine Aufgaben dieses Typs.
- Das Werkzeug liest immer alle Runden und meldet Kennungen und Fragen, die über Runden hinweg doppelt vorkommen (nur, wenn eine gewählte Runde beteiligt ist). Stand heute: keine.
- Die Einheiten der Runden 5, 7, 8 und der Runden 1-4 überschneiden sich heute nicht; Runden 1-4 treffen teils dieselbe Einheit (z. B. groessen.proportional: Runden 2, 3, 4).

### Reihenfolge-Nummern (Entscheidung)
- **Runden 1-4:** `max_r` der Einheit + Platz unter allen Aufgaben der Einheit in den Runden 1-4 (Runde 1, dann 2, 3, 4; Dateireihenfolge). Auch herausgenommene und liegen gebliebene Aufgaben zählen mit. Mit `--mit-bedingung` und ohne `--ohne` ergibt das dieselben Nummern wie vor der Erweiterung (Test prüft die Daten Zeile für Zeile gegen den früheren Stand).
- **Runde R ab 5:** `max_r` + 1000·R + Platz in der Runde (Runde 5 ab etwa max_r+5001, Runde 7 ab +7001, Runde 8 ab +8001).
- **Warum feste Bereiche statt „fortlaufend nach dem, was gerade drin ist“:** Die Nummern hängen nur vom Inhalt der Dateien ab, nicht davon, welche Pakete schon eingespielt sind oder welche Auswahl gerade läuft. Dadurch überschneiden sich Pakete nie, auch wenn mehrere Runden dieselbe Einheit treffen, und die **Reihenfolge des Einspielens ist egal**. Die App zieht nach Reihenfolge; Lücken in den Nummern schaden nicht (nur „hinten“ ist wichtig). Nachteil: Nummern sind nicht lückenlos.
- Das SQL prüft je Einheit: (1) Bestand bis `max_r` unverändert (`max(reihenfolge) <= max_r` ist genau `max_r`; bereits eingespielte andere Pakete stören nicht), (2) die Nummern des Pakets sind noch frei (sonst Abbruch „Paket schon eingespielt?“), (3) nach dem Einfügen: Zahl stimmt, `form`/`zaehlt` gesetzt, jede neue Aufgabe lässt sich bewerten.
- Voraussetzung: Wächst eine Runden-Datei nach dem Einspielen des Pakets einer späteren Runde 1-4 (oder `max_r` ändert sich durch anderes Einspielen), muss `rollend-einheiten.json` neu aus der Datenbank gelesen werden – die Prüfung (1) fängt das ab.

### Zuordnung und Prüfungen je Paket
- Runden 1-4: über den Flug (`fluege`) und das Lernziel, wie bisher. Runden ab 5: Feld `thema` jeder Aufgabe muss in `einheiten` stehen, Lernkarte `l` in `lz` dieser Einheit, sonst Fehler mit Kennung. `_teil2`/`_teil3` sind eigene Einheiten (z. B. `raum.schraegbilder_teil2`).
- `form`: Feld `form` der Aufgabe, sonst aus `typ`; stehen beide da, müssen sie zusammenpassen. Rollend-5 schreibt `typ` ohne „(einfache Form)“ – das Werkzeug kennt beide Schreibweisen.
- Weitere Prüfungen vor der Ausgabe (Fehler = Abbruch, Ausgabe auf stderr mit Kennung): unbekannte Form, `zaehlt` nicht ja/nein (`folge` = offen, Abbruch bei `--sql`), Antworttyp nicht erlaubt, Vorrat nicht `uebung`, Tipp/Lösungsweg fehlt, unbekannte Zeichnung, doppelte Kennungen und doppelte Fragen über alle Runden, Teilfähigkeit nicht in `tf`.

### Befund Teilfähigkeit `t` gegen `tf` der Einheit (27.11.2026)
- **Aufgaben mit `t` nicht in `tf`: Runde 1: 0, Runde 2: 0, Runde 3: 0, Runde 4: 0, Runde 5: 0, Runde 7: 0, Runde 8: 0** (Kennungen-Liste: leer). Auch die Lernkarte `l` steht in allen Aufgaben der Runden 5, 7, 8 in `lz` der Einheit.
- Der Mathe-Profi hat `t` in den neuen Runden schon so gesetzt, wie der Bestand es tut (je Lernkarte genau eine Teilfähigkeit; verglichen mit allen Aufgaben derselben Lernkarte in `inhalte/themen/<thema>.json`, 27 Einheiten, keine Abweichung, keine Lernkarte mit zwei verschiedenen `t` im Bestand). Es wird nichts umgebogen. Wo `lz` und `tf` verschieden sind, gilt diese Zuordnung Lernkarte → Teilfähigkeit (aus dem Bestand abgeleitet; stimmt mit den neuen Aufgaben überein):

| Einheit | Lernkarte → Teilfähigkeit |
|---|---|
| zahlen.ganz | deuten→verstehen, zahlengerade→verstehen, ordnen→ordnen, betrag→ordnen, schriftlich_plus_minus→schriftlich, addieren→addieren, subtrahieren→subtrahieren, umkehraufgabe→gleichungen, ketten→verbinden, verstehen→begruenden, sach→verbinden |
| zahlen.rechengesetze | punkt_strich→vorrang, klammern→vorrang, termaufbau→terme, vorteil→gesetze, differenz_summe→gesetze, verteilen→gesetze, kopfrechnen→gesetze, mal_ganz→ganz, geteilt_ganz→ganz, umkehraufgabe_mal→gleichungen, ueberschlag→verfahren, schriftlich→verfahren, schriftlich_geteilt→verfahren, sach→anwenden |
| zahlen.potenzen_basis | schreibweise→begriff, vertauschen→begriff, berechnen→berechnen, quadrat→berechnen, zehner→zehner, negativ→negativ, sach→anwenden |
| gleichungen.linear | waage, beide_seiten, klammern→umformen; probe, sonderfaelle→pruefen; sach→anwenden |
| groessen.indirekt | erkennen, vervielfachen, produkt→erkennen; dreisatz, sach→rechnen; graph, unterscheiden→darstellen |

  Alle anderen Einheiten der Runden 5, 7, 8 haben `lz` ⊂ `tf` mit gleichen Namen (Lernkarte = Teilfähigkeit) oder eine Zuordnung nach dem gleichen Muster; sie stimmen ebenfalls mit dem Bestand überein.
- Das Werkzeug erzwingt `t` ∈ `tf` und bricht sonst mit der Kennungsliste ab; es schreibt `t` nie um. Käme künftig eine Abweichung, wäre diese Tabelle die Grundlage für die Berichtigung durch den Mathe-Profi.

### Offene Punkte (Pakete)
1. Reihenfolge-Nummern ab 5001: bestätigen, dass die App und die Auswahl nichts voraussetzen, was eine Lücke in `reihenfolge` bricht (im Code nicht geprüft, nur aus dem Bestand der Funktionen abgeleitet: Auswahl nach `reihenfolge`, keine Eindeutigkeit gefordert).
2. Die Inhaltsprüfung (Gegenprüfung) der Runden 3, 4, 5, 7, 8 steht aus; der Nachweis oben (Abschnitt „Inhaltsprüfung“) gilt nur für Runden 1 und 2.
3. Die Darstellungs-Hinweise (Tabellen, Kreisdiagramm) gelten für alle Aufgaben mit Zeichnung: 18 (Altbestand), 15 (Runde 5), 20 (Runde 7), 0 (Runde 8); echte Geräte nicht geprüft.
4. Keine Einheit der Pakete wurde auf Versuche von Kind 1 oder Kind 2 geprüft außer für Runden 1 und 2 (siehe „Befund“); vor jedem Paket neu prüfen.
5. Reihenfolge der Pakete im Ablauf (`form-takt.md`, Schritt 5): erst App 0.94.0 und FT-S, dann Pakete; Runden 5, 7, 8 brauchen zusätzlich, dass die Einheiten (`rollend-einheiten.json`) frisch aus der Datenbank gelesen sind (`max_r`).
6. Satz des Nutzers vor jedem Einspielen; je Paket ein SQL, nicht ausführen ohne diesen Satz.


## Befund
- **142 Aufgaben in den alten Antwortformen** verteilen sich auf **14 bestehende, freigegebene Einheiten** (zehn Flüge; drei Flüge bestehen aus zwei oder drei Einheiten). Zuordnung über das Lernziel: `inhalte/plan/rollend-einheiten.json` (aus der Datenbank gelesen, nur Aufbau).
- Jedes Lernziel und jede Teilfähigkeit gibt es in der Ziel-Einheit. Keine Frage doppelt. Jede Aufgabe hat Tipp und Lösungsweg.
- In keiner der 14 Einheiten haben Kind 1 oder Kind 2 bisher einen Versuch. Das Einfügen ändert also keinen laufenden Lernstand.
- Neue Aufgaben kommen als **freigegeben** hinein (Vorgabe der Tabelle; eine freigegebene Einheit lässt nachträgliches Ändern nicht zu). Deshalb: erst Gegenprüfung der Inhalte, dann einspielen.
- 50 Aufgaben des Typs `bedingung` bleiben liegen, bis die App-Seite live ist.

## Die 12 Aufgaben mit Zeichnung (Sichtseite `tests/sicht-rollend-zeichnungen.html`, 420 px breit angesehen)
Alle zwölf werden gezeichnet; die Rechnungen habe ich an den Bildern nachvollzogen. Auffällig:
- **D1-14 (Kreisdiagramm):** Die Legende ist rechts abgeschnitten („Fangen (35“). Am echten Gerät prüfen; notfalls kürzere Beschriftung.
- **Tabellen (D1-05, D1-13, F1-05, G2T2-06, G2T2-07, G8-07):** In der Sichtseite stehen die Zeilen sehr eng. Unklar, ob das an der Sichtseite liegt oder echt ist – am Gerät prüfen.
- **F1-07, F1-15:** Achsenzahlen liegen teils auf dem Graphen bzw. dem Kreis. Lesbar, nicht schön.

## Nachtrag 27.11.: zwei echte Darstellungsfehler gefunden und behoben, LIVE seit 27.11.2026 mit App 0.93.6 (main 9429d03b)
- **Tabellen in Aufgaben:** Die Zeilenhöhe war 0 (`.lr-bild` setzt sie für Zeichnungen auf 0, die Tabelle erbte das). Zeilen lagen ineinander. **Der Fehler steckt auch in der Live-Fassung** (gleiche Stil-Regeln in `main`) und betrifft dort jede Aufgabe mit Tabelle. Behoben in `style.css` (`.lr-bild-tabelle` mit eigener Zeilenhöhe).
- **Kreisdiagramm:** Die Breite war fest, lange Beschriftungen wurden abgeschnitten. Jetzt richtet sich die Breite nach der längsten Beschriftung (`lernKreisdiagramm`).
- Nachher angesehen (Sichtseite, 420 px): Tabellen und Legende sind lesbar. Nicht geprüft: echtes Gerät, dunkle Ansicht.

## Inhaltsprüfung der Gegenprüfung (Werkstatt 1020, 27.11.)
- 142 Aufgaben einzeln geprüft, 156 Rechnungen nachgerechnet, keine Abweichung. Urteil je Datei: `ge1`, `ge2`, `a4` Ja; `f1` Ja mit Auflage (Tabelle); `z2`, `a1`, `d1`, `g1`, `g8`, `g2-teil2` erst nach Berichtigung.
- Inhaltliche Muss-Befunde: Z2-07, A1-04, G1-07, G8-01, G8-04, G1-12, G2T2-03 → Auftrag 20 an den Mathe-Profi (Postfach). Darstellung (Tabellen, Legende) im Arbeitsstand behoben.
- Verhältnis: Vorschlag 1 neue Form auf 2 Bestandsaufgaben je Lernkarte und Stufe, gemischt; „neu“ muss über ein eigenes Kennzeichen erkennbar sein. Technische Fragen (Werkstatt 1019, A–C) noch offen.

## Offen vor dem Einspielen
1. Gegenprüfung der Inhalte durch ChatGPT (fachlich, Sprache, Schwierigkeit).
2. Die beiden Darstellungs-Korrekturen müssen live sein, bevor die Aufgaben mit Tabelle oder Kreisdiagramm hineingehen (siehe Nachtrag).
3. Satz des Nutzers. Das SQL ist rund 70 KB groß; es wird je Einheit einzeln ausgeführt.
4. **Pflicht (Auftrag des Nutzers vom 27.11.):** neue Formen bevorzugt ziehen – siehe `aufgabentypen-auswahl.md`, Abschnitt „Neue Aufgabenformen bevorzugt ziehen“. Bisher offen und nicht nachgesehen: wie die App aus dem Vorrat einer Lernkarte auswählt (ob neue Formen bevorzugt werden oder nur zufällig dazukommen).

## Live 27.11.2026: App 0.93.6
- Auf das Wort des Nutzers. Gesamttest 203/203, Bruch-Tests 7/7, Sichtprüfung des Designers hell/dunkel. Nicht geprüft: echtes Gerät, Safari.
- Zusammenführung: Der gewöhnliche Merge meldete Konflikte (drei gemeinsame Vorfahren durch frühere Kreuz-Merges). `main` war inhaltsgleich mit dem Vorfahren ac2bffe1 von `lernen-app`; deshalb Merge-Commit mit genau dem Baum von `lernen-app` gesetzt (commit-tree) und Gleichheit geprüft. **Beim nächsten Live genauso vorgehen oder vorher `main` in `lernen-app` zusammenführen.**
