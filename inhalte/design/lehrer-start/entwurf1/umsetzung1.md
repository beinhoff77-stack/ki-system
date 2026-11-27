# Vorgabe LS, erste Runde: Lehrer-Startseite „Was ist los?“

Designer, 27.11.2026. Entwurf: `index.html` (eine Datei, ohne Netz), Bilder: `bilder/`. Adresse: `#g=nacht`, `#leer=1`.
Sprache wie der freigegebene Entwurf 4 von „Was wackelt“ (`../../wackelt/entwurf4/`): dieselben Farben aus `style.css` (`data-area="lernen"`), Karten 19 px, Abschnittskopf „Titel + graue Zahl“, Tabellenzeilen 40–44 px mit 1-px-Linien, kleine Knöpfe 30 px. Daten erfunden („Kind 1“, „Kind 2“, „Testkind“).

## 1 Was am Ist-Zustand stört (Live-App, 1522 px angesehen)
1. „Die Kinder“ steht links neben der Tabelle; Tabelle schmaler als „Zu tun“ – keine gemeinsame Kante.
2. GYM/RS/IB mit Prozent und Mini-Balken: drei Zahlen, deren Bezug (Klasse? Schulart?) man erst lernen muss.
3. „Lernt“ und „Wackelt“ als grün/orange gefüllte Zellen – Ampel-Flecken statt Information.
4. Keine Woche: weder Aufgaben noch Anteil richtig, kein Verlauf; „Jetzt“ in Reisewörtern (Ort · Flug).
5. Nachschlagen/Verwalten als lose Versal-Etiketten mit Textlinks; die Hälfte der Seite leer.

## 2 Aufbau (1440 × 900: alles in einer Bildschirmhöhe, gemessen 900 px; Handy 400 px: 1 798 px, einspaltig)
Kopf „Lernen Schule“ · Titel „Was ist los?“ mit „So funktioniert’s“ rechts.
1. **Zu tun** (Karte, höchstens 4 Zeilen à 44 px): Punkt (rot = kein Lerntag seit 3 Tagen / Rückreise · gelb = Fehler offen · blau = Antwort auf Auftrag, Wunsch einlösen), Satz, rechts das Ziel („Was wackelt ›“, „Überblick ›“, „Aufträge ›“); Wünsche mit „Bestätigen | Ablehnen“ in der Zeile. Rechts im Kopf „+ Reisetag eintragen“. Leer: „Alles ruhig – heute ist nichts zu tun.“
2. **Die Kinder** – eine Kachel je Kind, zwei nebeneinander (unter 900 px untereinander). Kopf: Name (verlinkt zur Kind-Seite), „Gymnasium · Klasse 8“, rechts „Lernen starten“ (nur Eltern) und „Einstellen“. Darunter fünf Zeilen (Bezeichnung grau 104 px | Wert):
   - *Diese Woche*: 7 Punkte = die letzten 7 Tage (voll = Lerntag, gestrichelt = Reisetag/Pause, Ring = heute) · „n Lerntage · zuletzt gestern · Vorwoche n“
   - *Aufgaben*: „31 gelöst · 68 % richtig“ + Balken richtig/falsch + „4× mit Tipp“
   - *Gerade dran*: „Thema · Lernkarte“ (einzeilig gekürzt) · „Karte 2/5“
   - *Was wackelt*: „10 Fehler offen ›“ (rot, führt zu „Was wackelt“ des Kindes) bzw. „nichts offen ✓“ (grün)
   - *Schuljahr*: „13 % von Klasse 8 gelandet“ + Balken in der eigenen Schulart; „andere Schularten ▸“ klappt „Realschule Kl. 8: 20 % · IB MYP-Jahr 3: 15 %“ auf.
3. **Nachschlagen** (Karte, Links in drei Spalten mit kurzer Erklärung): Lehrplan · Regeln (Regel-Universum) · Expeditionen · Meine Aufträge (mit „1 offen“) · So funktioniert’s. **Verwalten** (schmale Karte rechts): Testkind · Zugänge.

## 3 Daten je Element
| Element | liefert heute | fehlt |
|---|---|---|
| Zu tun: kein Lerntag seit n Tagen, Pausen | `schule_lernstand.lerntage` (28 Tage), `.pausen`; Regel `lernLerntAmpel` | – |
| Zu tun: Rückreise | `schule_uebersicht.lernende[].route` (`art = 'rueckreise'`) | – |
| Zu tun: „n Fehler offen – am meisten bei …“ | heute je Etappe „wackelt“ aus `schule_lernstand` bzw. Zahl `schule_wackelt_lesen.zu_besprechen` | Zahl offener Fehler nach „Was wackelt“ E4 (Abhaken je Antwort, `schule_wackelt_analyse`); „am meisten bei …“ braucht die Fehlbild-Kennung (`aufgabe.fehlbilder`, Stufe 2) – bis dahin ohne Zusatz |
| Zu tun: Antwort auf Auftrag | `schule_rueckmeldungen` (`antwort`, `status`, `beantwortet_am`) | – |
| Zu tun: Wunsch einlösen | `schule_eltern.einloesungen` (`status = 'beantragt'`), `schule_einloesung_entscheiden` | – |
| Kopf: Name, Schulart, Klasse | `schule_uebersicht.lernende[]` (`name`, `schulart`, `klasse`) | – |
| Diese Woche: Punkte, zuletzt, Vorwoche | `schule_lernstand.lerntage` (28 Tage) und `.pausen` | – |
| Aufgaben gelöst, % richtig, mit Tipp | `schule_lernstand.woche` (`aufgaben`, `richtig`, `mit_tipp`, letzte 7 Tage) | Vorwochenwert für „richtig“ (nicht gezeigt) |
| Gerade dran | `lernReiseDaten(u, id).naechste` (`titel`, `fertig`, `n`) aus `schule_uebersicht` | Name der Lernkarte (Etappe) statt Flug: aus `schule_lernstand.einheiten[].karten[]` (erste nicht gelandete) – vorhanden, nur verbinden |
| Schuljahr % je Schulart | `lernStandZellen` / `lernStandModell` aus `schule_uebersicht` (gelandete Flüge / Flüge der Klasse) | – |
| Nachschlagen, Verwalten | Adressen `#/lehrplan`, `#/regeln`, `#/expeditionen`, `#/lernauftraege`, `#/info`, `#/reise/<Testkind>`, `#/zugaenge` | – |

Weggefallen gegenüber heute: Tabelle mit drei Schularten-Spalten (jetzt aufklappbar), Ampel-Zellen, Versal-Etiketten.

## 4 Bilder
01 1440 hell · 02 1440 dunkel · 03 400 hell (ganze Seite) · 04 400 dunkel · 05 „Alles ruhig“ · 06 andere Schularten aufgeklappt.
