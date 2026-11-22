# Vorgabe „Unser Lehrplan“ – Matrix, Fahrplan und Detail auf einer Seite (Eltern/Lehrer)

Stand 22.11.2026. Klickbarer Prototyp: `entwurf/unser-lehrplan.html` (Breite 400 / 820 / 1280 oben umschaltbar; Themen, Klassen, Etappen, Verbindungen echt; Lernstand und Plan von „Kind B“ erfunden). Bilder: `bilder/`.
Nur Vorgabe, kein App-Code. Ziel (Sebastian): eigenen Lehrplan machen – sehen, was es gibt, auswählen, Stufe setzen, Reihenfolge festlegen, Lehrstoff ansehen und genau sehen, wo das Kind steht – **an einer Stelle**, platzsparend und schön.

## 1 Einordnung in die Kind-Seite
- Reiter der Kind-Seite: **Überblick · Was wackelt · Lehrplan** (3 statt 4). „Lehrplan“ ersetzt **„Stand“ und „Plan“**. Alte Links `#/kind/<id>-stand` und `-plan` führen auf den neuen Reiter.
- Nachschlagen → Lehrplan (LM, alle Kinder, „Beide vergleichen“) bleibt die Übersicht ohne Bearbeiten; im Detail dort zusätzlich „Für ‹Kind› planen ›“ → dieser Reiter mit dem Thema geöffnet.
- Die Stufen-Knöpfe gibt es danach **nur noch hier** (heute drei Stellen).

### 1a Kopf: Kinder durchklicken, Reiter verknüpft (Sebastian 22.11.)
- Statt nur „Kind B“: **Kinder-Umschalter** im Kopf: `‹ [A Kind A · Realschule · Kl. 6] [B Kind B · Gymnasium · Kl. 8] ›`. Klick auf ein Kind oder ‹ › wechselt das Kind, **der gewählte Reiter bleibt** (man vergleicht z. B. Lehrplan A und B direkt). Tastatur Alt+← / Alt+→. Handy: nur das aktive Kind ausgeschrieben, andere als Buchstabe.
- Beim Wechsel: Schule und Klassen-Filter übernehmen die Werte des Kindes, Detail zu, Auswahl leer, Rückgängig verfällt.
- Reiter „Was wackelt“ zeigt eine **rote Zahl** = Einträge „Zu besprechen“.
- **Überblick** (Vorschlag, bild ueberblick.png): Karten „Gerade dran“ (Thema, Etappe, Balken, → „Im Lehrplan öffnen“), „Als Nächstes“ (Platz 2–4, → „Fahrplan ändern“), „Zu besprechen“ (Zahl, Themen, → „Was wackelt“), „Diese Woche“, Ringe rund um die Klasse des Kindes. Vorhandene Inhalte des heutigen Überblicks bleiben darunter.
- **Was wackelt als Arbeitsliste** (bild was-wackelt.png): Gruppen **Zu besprechen · Beobachten · Besprochen**, je Eintrag Thema, Etappe, Anzahl Fehler, wann; Knöpfe „✓ Besprochen“, „Beobachten“, „Im Lehrplan“ (öffnet Lehrplan mit dem Thema). Aufgabe + Antwort des Kindes aufklappbar wie heute. Neue Fehler im selben Thema → Eintrag wieder „Zu besprechen“. Braucht einen gespeicherten Status je Kind und Thema (Datenbank) – eigener Schritt LW-3.

## 2 Aufbau (Rechner ≥ 1100 px)
```
┌ Kopf: ‹  Kind B  Gymnasium · Kl. 8                    Überblick · Was wackelt · [Lehrplan] ┐
├ Leiste: EINORDNEN [Gym|RS|IB]  ZEIGEN [Lehrplan Gym|+ andere Schularten|Alles]   [Einstieg prüfen ▾] [Suchen] [Auswählen] ┤
├ Legende (eine Zeile, klein) ─────────────────────────────────────────────────────────────────┤
│ FAHRPLAN 268 px │ MATRIX: Spalten = Themengebiete (Kopf klebt), Zeilen = Klassen (links klebt) │
│ ▶ gerade dran   │  Kl.-Kasten + Ring (% kann/Wdh) │ Karten …                                     │
│ ○ kommt noch 2… │                                                                               │
│ + hierher ziehen│                                   ┌ DETAIL als Schublade von rechts (390 px) ┐ │
│ ↻ Wdh (14) ›    │                                   └ öffnet beim Antippen, ✕ schließt          ┘ │
│ ◉ Kann er (20) ›│                                                                               │
└─────────────────┴───────────────────────────────────────────────────────────────────────────────┘
```
- **Detail als Schublade über der Matrix**, nicht als feste Spalte – so bleibt die volle Breite für die Matrix (löst N1 der Nachprüfung Matrix: zu schmale Spalten bei 1280).
- **Fertige Klassen eingeklappt:** Klassen, in denen alles „kann er“/„Wiederholung“ ist, stehen als eine Zeile „Gym Kl. 5 · ✓ Alles gekonnt · 14 Themen · davon 3 in Wiederholung · aufklappen ▾“. Beim Öffnen scrollt die Seite zur Klasse des Kindes.
- Klassen-Kasten links: Schulart + Klasse in Klassenfarbe (LA-8), darunter **drei Ringe** (Sebastian 22.11.): groß die gewählte Schule, klein darunter die beiden anderen („RS 8 25 %“, „MYP 3 53 %“).
- **Rechnung je Ring:** gelandete Etappen / alle Etappen der Pflichtthemen dieser Schule in dieser Klasse (IB: MYP-Jahr = Klasse − 5), unabhängig davon, in welcher Zeile die Themen stehen. Gelandet = Etappe gelandet (auch in Wiederholung); gesetzte Themen („Kann er …“) zählen mit allen Etappen. Farben im Ring: grün kann er, hellgrün Wiederholung, gelb angefangene Themen. Unter dem großen Ring „9/10 Themen“ (ganz fertige Themen). Aufgelöste Themen zählen nicht. Darüberfahren: „Gym 8: 12 von 101 Etappen gelandet · 1/15 Themen fertig“.

## 3 Die Karte (ein Thema in der Matrix)
- Zeile 1: Titel (höchstens 2 Zeilen, Silbentrennung, dann „…“).
- Zeile 2 links: Stand – `◉ kann er` / `◉ gesetzt` / `↻ Wdh 2/5` / `▶ Etappe 3/7` / `Platz 4` / `2/7 begonnen` / leer.
- Zeile 2 rechts: **Schul-Kennzeichen** `Gym 8 · RS 7 · IB 4` (gewählte Schulart dunkel, fehlende durchgestrichen, „Gym –“ orange). Tablet/Handy kurz: `G8 R7 I4`.
- **Farben (Sebastian 22.11.: „blau, wo er gerade dran ist, hellgelb, was schon in seinem Plan liegt“):**
  - **▶ gerade dran:** **blau** – Fläche #DCEAFB, blauer Ring #3F7FD0, Titel fett dunkelblau, Platznummer blau. Das Auffälligste auf der Seite. Im Fahrplan derselbe blaue Eintrag mit blauem Fortschrittsbalken.
  - **im Plan (kommt noch):** **hellgelb** – Fläche #FFF4CF, gelber Strich links, „Platz 4“, Platznummer goldgelb (#C99600). Im Fahrplan alle „kommt noch“-Einträge hellgelb.
  - **↻ in Wiederholung:** hellgrün (#F0F7E8), hellgrüner Strich, „↻ Wdh 2/5“.
  - **✓ fertig (kann er, auch gesetzt):** durchsichtig, Titel grau, „✓ fertig“ / „✓ gesetzt“; beim Darüberfahren weiß.
  - **+ einplanen, gehört zur gewählten Schule:** **weiß** mit feinem Rahmen, Text „+ einplanen“ bzw. „1/7 Etappen“.
  - **+ einplanen, nur andere Schule:** **grau** (#E6E3DC) ohne Rahmen, Titel grau; beim Darüberfahren weiß. (Ersetzt den gestrichelten Rand.)
  - Ring je Klasse: grün kann er, hellgrün Wiederholung, blau angefangene Etappen.
  - Ganz fertige Klassen zusätzlich eingeklappt (siehe 2).
- **Blaue Zahl** oben rechts = Platz im Fahrplan; bei Themen außerhalb erscheint beim Darüberfahren ein „+“.
- Rechner: Karte ziehbar (in den Fahrplan).

## 4 Fahrplan (links)
- „Gerade dran“ (gelb, mit Fortschrittsbalken „Etappe 3/7“), darunter „Kommt noch“ nummeriert. Ziehen (Griff ⋮⋮) oder ↑ ↓ (Rechner beim Darüberfahren, Tablet/Handy immer sichtbar).
- **Reihenfolge-Hinweis:** steht ein Thema vor einer harten Voraussetzung, roter Rand und „braucht ‹Thema› – kommt erst auf Platz n“.
- „+ Thema hierher ziehen“ (Rechner); Ablegen zwischen zwei Einträgen zeigt eine blaue Linie.
- Unten zugeklappt: „↻ In Wiederholung (n) ›“, „✓ Fertig (kann er) (n) ›“ (öffnet die Liste; dort „Wieder in die Wiederholung“).
- Darüberfahren über einen Fahrplan-Eintrag hebt die Karte in der Matrix hervor.

### 4a Rausziehen und Reihenfolge-Warnung (Sebastian 22.11.)
- **Aus dem Plan ziehen:** Eintrag aus dem Fahrplan zurück in die Matrix ziehen = aus dem Plan genommen. Beim Ziehen über die Matrix wird sie rot gestrichelt mit „Hier loslassen = aus dem Plan nehmen“. Danach Einblendung mit „↶ Rückgängig“. Baut ein Thema im Plan darauf auf, steht das mit ⚠ in derselben Einblendung.
- **Warnung, keine Sperre:** Nur harte Voraussetzungen (`schule.voraussetzung`, hart) lösen sie aus, empfohlene nicht. Prüfung nach jedem Einplanen, Ziehen, ↑/↓, „Als Nächstes“ und „Ans Ende“:
  1. Thema steht **vor** seiner Voraussetzung → „⚠ „B“ baut auf „A“ auf – das kommt erst auf Platz 4“, Knopf **„„A“ davor setzen“**.
  2. Voraussetzung wird **hinter** ein Thema geschoben, das darauf aufbaut → „⚠ „B“ baut hierauf auf und steht schon auf Platz 2“, Knopf **„hinter „B“ setzen“**.
  3. Voraussetzung ist **weder gekonnt noch im Plan** → „⚠ … das kann er noch nicht und es ist nicht im Plan“, Knopf **„„A“ davor einplanen“**.
  Die Einblendung ist dunkelrot, Rückgängig bleibt daneben. Der Lehrer darf es trotzdem so lassen.
- **Dauerhaft im Fahrplan:** betroffener Eintrag mit rotem Rand und Zeile „braucht A – kommt erst auf Platz 4“ bzw. „braucht A – nicht gelernt, nicht im Plan“, solange der Konflikt besteht.
- Gekonnt/Wiederholung/gesetzt gilt als erfüllt; aufgelöste Themen werden ignoriert.

## 5 Detail-Schublade (beim Antippen einer Karte)
1. Kopf: Titel, Themengebiet, Schul-Kennzeichen, ✕.
2. **Stand von ‹Kind›:** Stufen-Marke (z. B. „↻ in Wiederholung · Wdh 2 von 5 · nächste in 3 Lerntagen“), darunter **jede Etappe** mit Punkt: gelandet / Wiederholung / gerade dran („4 von 6“) / begonnen mit Fehlern / offen / freiwillig.
3. **Planen:** nicht im Plan → geteilter Knopf „In den Plan: als Nächstes ▾“ (Menü: „… ans Ende“, „… nach Lehrplan einsortieren“); im Plan → „Als Nächstes“, „Ans Ende“, „Aus dem Plan“.
4. **Stufe setzen:** Segment „Lernen | Kann er – wiederholen | Kann er komplett“ (aktive Stufe markiert). Wirkung wie LB-3/LB-5 (Server-Aufrufe unverändert).
5. **Lehrstoff:** Kurzbeschreibung, „Inhalte ansehen (n Etappen) ›“, „Fehler besprechen (n) ›“ (nur bei offenen Fehlern).
6. **Zusammenhang:** „Braucht vorher“ als kleine Karten mit Stand (✓ / Platz n / fehlt), „Darauf baut auf“; antippen öffnet dieses Thema.
- Jede Änderung speichert sofort; unten erscheint eine Meldung „‹Thema› als Nächstes eingeplant · ↶ Rückgängig“ (5 s; Rückgängig nur für den letzten Schritt wie heute).

## 6 Werkzeuge der Leiste (vereinfacht nach Sebastians Rückmeldung 22.11.: „ich will alles in unseren Lehrplan aufnehmen“)
- **Immer alle Themen sichtbar** (alle Schularten, Entdecker-Inseln; nur aufgelöste Themen ohne Flug fehlen). Kein Filter, der Themen ausblendet.
- **„Klassen nach“ Gymnasium | Realschule | IB:** bestimmt nur, **in welcher Zeile** ein Thema steht (Klasse dieser Schule). Standard = Schulart des Kindes. Themen, die diese Schule nicht hat, stehen gestrichelt in der Klasse der anderen Schule.
- **„Zeigen“ Alle Themen | Noch nicht im Plan · n | Im Plan · n:** hebt hervor, alles andere wird blass (nichts verschwindet).
- **„Klassen 5 6 7 8 9 10“ – Mehrfachauswahl** (Sebastian 22.11.: „wenn Leo in der 9 ist, brauche ich 5–8 nicht mehr sehen“): Knöpfe in Klassenfarbe zum An-/Abschalten; abgeschaltete Klassen verschwinden ganz aus der Matrix (der Fahrplan zeigt weiter alles). **Standard: Klasse des Kindes bis 10**, je Kind gemerkt (Gerät). Ein blauer Punkt am Knopf zeigt, dass die Klasse Themen aus dem Fahrplan enthält – auch wenn sie ausgeblendet ist. Mindestens eine Klasse bleibt an. „Noch nicht im Plan“ und „Alle n einplanen“ gelten nur für die gewählten Klassen.
- Bei „Noch nicht im Plan“ oben im Fahrplan: „n Themen (bis Kl. X) noch nicht im Plan · [Alle n einplanen (nach Klasse und Lehrplan)]“ – damit kommt mit einem Klick alles in den Plan.
- **Suchen**, **Auswählen** (Sammelleiste) wie beschrieben.
- Kleine % je Schulart stehen im Überblick-Reiter.

## 7 Tablet (760–1099 px)
Matrix volle Breite, Karten-Kennzeichen kurz (`G8 R7 I4`), Fahrplan als Schublade von links über Knopf „Fahrplan · 5“ in der Leiste, Detail als Schublade von rechts.

## 8 Handy (< 760 px)
- Kopf zweizeilig (Name, darunter die drei Reiter).
- Umschalter **„Fahrplan · 5 | Alle Themen“**.
- „Alle Themen“: je Klasse eine Karte (Kasten + Ring), darin nach Themengebiet die Karten in voller Breite; fertige Klassen eingeklappt.
- Fahrplan: Liste mit ↑ ↓ immer sichtbar; statt „hierher ziehen“: „Einplanen: unter ‚Alle Themen‘ ein Thema antippen“.
- Detail als **Blatt von unten** (82 % Höhe).

## 9 Optik
Ruhige Sandfläche, weiße Karten mit 3-px-Stufenstrich links, nur eine Akzentfarbe für „im Plan“ (Blau) und eine für „gerade dran“ (Gelb). Segment-Schalter statt Knopfreihen. Schatten nur beim Darüberfahren und bei Schubladen. Schrift 12–13 px in Karten, 600–650 fett für Titel. Bewegungen ≤ 0,25 s.

## 10 Daten (Annahmen, im Bau prüfen)
- Raster und Stufen: `schule_lehrplan_matrix` (LM-S) mit `lernstand` des Kindes.
- Plan: `schule_plan_lesen` / `schule_plan_setzen` (Revision, Rückgängig). **Annahme:** „an Platz n einfügen“ und „mehrere auf einmal“ gehen über die vorhandene Sammel-Aktion von „Auswählen“; sonst kleine Erweiterung nach W1–W7.
- Etappen-Stand im Detail (gelandet/Wdh/begonnen mit Fehlerzahl): heute in `schule_lernstand` (Was wackelt) – im Detail nachladen (`schule_lehrplan_thema` mit `lernender_id`).
- Heute fasst ein Plan-Eintrag einen Ort mit mehreren Flügen zusammen. Bis zum Reise-Aufbau zeigt der Fahrplan je Ort einen Eintrag mit „0/4 Flüge“ und klappt auf; danach ist jeder Eintrag ein Thema (einfacher).

## 11 Schritte
1. **LW-1:** Seite mit Matrix + Fahrplan + Detail, Reiter „Lehrplan“ ersetzt Stand und Plan, Zeigen-Filter, Einstieg prüfen, fertige Klassen eingeklappt, Handy/Tablet.
2. **LW-2:** Ziehen aus der Matrix und zurück (4a), Reihenfolge-Warnungen mit Reparieren-Knopf (4a), „Alle fehlenden einplanen“, Detail mit Etappen-Stand, Farben nach Abschnitt 3.
3. **LW-3:** Kinder-Umschalter im Kopf (1a), Überblick-Karten mit Sprüngen, Was wackelt als Arbeitsliste mit gespeichertem Status.

## 12 LK – ein Thema in mehreren Klassen (Vorgabe LK-G, 22.11.)
Grundlage: Bau-Auftrag LK mit den Nachträgen „vorhandener Lernstand“ und „Route: zweiter Teil fliegt ins Nachbarland“. Daten kommen aus LK-S (`schule_lehrplan_matrix`/`_thema`: Klassen je Thema mit Rolle, Etappen, Stunden; `baut_auf`, `weiter_in`; Abdeckung je Klasse). **Im Entwurf sind Lage und Stunden Beispielwerte** (Terme umformen, Lineare Gleichungen, Lineare Funktionen, Bruchterme), bis LK-D/LK-S liefern. Bilder: `bilder/lk-*.png`. Fehlen die neuen Felder, bleibt die Anzeige aus LW-1/2 (eine Karte je Thema) – **LW-1/2 warten nicht auf LK.**

**12.1 Karte je Klasse**
- Das Thema steht in **jeder Klassenzeile, in der der Lehrplan es verlangt** (gewählte Schulart, bei RS der Zweig des Kindes).
- **Erste Klasse („neu“):** normale Karte wie bisher. Stand = Etappen dieser Klasse.
- **Spätere Klasse („weitergeführt“):** schmalere Karte unter den neuen Themen der Zelle, Kopfzeile „↪ weitergeführt“, Titel, „neu in Kl. 8: Äquivalente Terme +1“ (erste neue Etappe, Rest als Zahl; alle im Tooltip/Detail). Stand nur für **diese** Etappen: „2/3 neue Etappen“, „✓ dieser Teil erledigt“. Antippen öffnet **dasselbe Detail**.
- Farben wie Abschnitt 3, je Karte nach ihrem Teil: ist das Thema gerade dran und die aktuelle Etappe liegt in diesem Teil → blau; liegt sie in einem anderen Teil → hellgelb „danach“. Nicht im Plan, nichts gelandet → weiß, Rand gestrichelt.
- **Fertig bleibt fertig:** Thema „kann er“/„Wiederholung“ oder abgeschlossener Flug → in **allen** Zeilen ✓ bzw. ↻ (Nachtrag Lernstand 1–3). Nichts wird doppelt gezählt, Sterne/Stempel je Thema bzw. je Flug unverändert.
- **Geteiltes Thema (≥ 3 eigene Etappen in der späteren Klasse, Nachtrag Route):** Kopfzeile „✈ Teil 2 · eig. Flug“ statt „↪ weitergeführt“. Nach dem echten Teilen (eigene Themen-Nummer) wird daraus eine normale „neu“-Karte mit Titel von `lehrplan-lb`; bis dahin nur Kennzeichen. Bei 1–2 Etappen bleibt es „weitergeführt“, ein Flug.
- Fahrplan: ein Platz je Thema (bzw. je Flug nach dem Teilen), Nummer erscheint auf allen Karten des Themas.

**12.2 Kennzeichen**
- Statt `Gym 8 · RS 7 · IB 4`: je Schulart alle Klassen als Spanne `Gym 8–9 · RS 7–8 · IB 3` (Lücke: `Gym 7, 9`). Gewählte Schulart dunkel, andere hell, nicht verlangt durchgestrichen wie bisher. Kein Zeilenumbruch in einem Kennzeichen.

**12.3 Klassen-Kopf**
- Ring und „x/y Themen“ rechnen mit den Etappen, die **in dieser Klasse** verlangt werden (Teil zählt als fertig, wenn alle seine Etappen gelandet/gesetzt sind).
- Neu darunter: **Lehrplan-Abdeckung** „104/112 Std. mit Inhalt“ mit dünnem Balken (Stunden der Lernbereiche, deren Punkte ein Thema haben, aus `lehrplan_abdeckung`; IB ohne Stunden → Punkte „14/16 Punkte“). Nur Eltern/Lehrer, nie Kinderseite. Tooltip erklärt die Zahl.

**12.4 Detail**
- Etappenliste nach Klassen gegliedert: „KL. 8 · NEU“, „KL. 9 · WEITERGEFÜHRT“ bzw. „KL. 9 · TEIL 2 · EIGENER FLUG“, je Etappe Stand wie bisher.
- **„Baut auf“** (ersetzt „Braucht vorher“): Voraussetzungen mit Klasse in der gewählten Schulart („Lineare Gleichungen · Kl. 7“), Stand ✓ / Platz / fehlt, empfohlene mit „· empfohlen“; antippbar.
- **„Geht weiter in“** (ersetzt „Darauf baut auf“): zuerst die späteren Klassen **dieses** Themas mit ihren neuen Etappen (bei Teilung „✈ eigener Flug“), dann Themen, die darauf aufbauen, mit Klasse.
- **„Lage im Lehrplan“**: je Schulart „Kl. 8 neu (7 Et.) → Kl. 9 weitergeführt (4 Et.)“ oder „kein Pflichtstoff“ (LK-D 3d).
- Warnung beim Einplanen wie 4a; harte Voraussetzungen kommen aus `baut_auf`. Neu: Warnung auch, wenn die Voraussetzung **in einer späteren Klasse** liegt als das Thema (Aufbau-Verstoß aus LK-D 3a) – Text „⚠ laut Lehrplan erst Kl. 9“, kein Knopf.

**12.5 Kinderseite „Meine Route 5–10“ (knapp)**
- Gleiche Regel: Thema erscheint in jeder Klasse; spätere Klasse als kleine Zeile „↪ geht weiter: 2 neue Etappen“ mit Stand dieser Etappen. Geschaffte Flüge bleiben in allen Klassen mit Stempel/✓.
- Geteilte Themen erscheinen als **zwei Flüge** (Teil 2 = Nachbarland, Name aus `reise-aufbau`). Keine Stunden, keine Abdeckung, kein „weitergeführt“-Fachwort: Kindertext „geht weiter“.

**12.6 Prüfen nach LK-App**
- Ein Thema in zwei Klassen erscheint in beiden; Stand der zweiten Karte = nur ihre Etappen; Kind mit allen Etappen sieht beide fertig.
- Ring Kl. 8 ändert sich nur durch verlangte Etappen, nicht durch doppelte Zählung; Summe Etappen je Thema über alle Klassen = Etappen des Themas.
- Kennzeichen-Spannen gegen `lk_daten_2211.json`; Abdeckung RS 8 I Lernbereich 4 = 40 Std.
- Ohne neue Felder: Anzeige wie LW-2.

## Prüfen nach dem Bau
400/820/1280; keine Funktion aus „Plan“ verloren (Auswählen, Sammelaktion, Rückgängig, Konflikt „Neu laden“, Wieder in die Wiederholung); Stand-Zahlen gleich wie in der Matrix unter Nachschlagen; Testkind und erfundene Daten.
