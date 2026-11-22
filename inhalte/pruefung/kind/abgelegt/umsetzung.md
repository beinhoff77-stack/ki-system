# Vorgabe „abgelegt“ (Bau-Auftrag WD, Teil App) – Check-in, Etappe abgelegt, Flug abgelegt, Gold im Reisepass

Stand 22.11.2026. Entwurf zum Anklicken: `entwurf/abgelegt.html` (Breite 400 / 820 / 1280 oben umschaltbar, Daten erfunden).
Grundlage: `inhalte/AUFTRAEGE.md`, Bau-Auftrag WD mit Nachtrag (Schnittstelle). Stil wie die Abschluss-Ansichten (AB-A): gleiche Knöpfe, Blätter, Bewegungsregeln (≤ 1,8 s, Antippen beendet, „weniger Bewegung“ zeigt sofort den Endzustand). **Neu: Gold ist die Farbe für „abgelegt“ – nur dafür** (nicht für Direktflug-Sterne o. Ä. neu einführen).
Nur Vorgabe, kein App-Code. Texte für Klasse 5; Wörter „endgültig“, „fällig“, „Stufe“, „Wiederholungs-Takt“ kommen im Kindertext nicht vor.

## 1 Ansage auf der Startseite (WD-1)
Wenn `runde > 0` und `runde_gemacht` false. Im Kasten „Jetzt dran“ über dem Startknopf:
- Überschrift: **„Vorher kurz einchecken“**
- Zeile: **„{runde} Bordkarten von früher · etwa {min} Minuten · je richtig ★ 5“**. `{min}` = aufgerundet `runde × 0,5` (Annahme 30 s je Bordkarte; besser vom Server aus der mittleren Antwortzeit des Kindes). Unter 2 Minuten: „ganz kurz“.
- **Koffer-Leiste**: je Pflicht-Bordkarte ein Koffer, in Päckchen: bis 6 → ein Päckchen; 7–9 → Päckchen zu 3; 10–12 → Päckchen zu 4 (bzw. 3 + 3 + 4, gleichmäßig).
- Startknopf bleibt „Weiter geht’s“ (führt in den Check-in, danach ins Thema). Statt heute „Erst 9 Wiederholungen, dann Mumbai.“
- Die Zahl der fälligen Etappen (`faellig`) sieht das Kind nie. `runde_gemacht` true → Kasten entfällt.

## 2 Während des Check-ins
- Kopf: **„CHECK-IN · {i} VON {runde}“** statt „WIEDERHOLEN i VON n“; darunter die Koffer-Leiste; rechts der Sterne-Zähler.
- Unter der Aufgabe klein: „{Etappe} · aus {Stadt}“.
- Richtig: „Richtig!“ mit Marke „+5 ★“ rechts; der Koffer wird gold mit Stern, „+5“ fliegt zum Zähler (0,8 s), Zähler springt. Sterne nur, wenn `wiederholung.sterne` > 0.
- Falsch: „Noch nicht. Richtig ist …“, darunter **„Kein Problem – diese Bordkarte kommt beim nächsten Mal wieder.“** Koffer rötlich. Link „Zur Etappe“ bleibt klein.
- Volles Päckchen wird hellgelb (kein eigener Bildschirm).
- Knopf „Nächste Bordkarte ›“, nach der letzten „Fertig ›“.

## 3 Check-in fertig
- Titel **„Eingecheckt!“**, Koffer-Leiste, Zeile **„{r} von {runde} richtig · +{sterne} ★“** (Summe inkl. 30/100 aus Ablegen).
- Fehler: „{n} Bordkarte(n) kommt/kommen beim nächsten Mal wieder.“ Alles richtig: „Alles richtig – super eingecheckt!“
- Knopf **„Weiter nach {Stadt} ›“** (ins Thema). Textlink **„Noch 3 Extra-Bordkarten? Je richtig ★ 5“** nur, wenn `faellig > runde` (freiwillig, je Klick höchstens 3).
- Merker: `schule_wiederholung_runde_fertig` (WD-2) statt `localStorage`.

## 4 Etappe abgelegt (30 ★, mittelgroß)
Auslöser: `abgelegt.etappe` in der Antwort von `schule_uebung_pruefen` (Check-in, freiwillige Wiederholung oder Mischkarte). Direkt nach der Rückmeldung „Richtig!“.
- Handy: **Blatt von unten**, bis ca. 70 % Höhe; Tablet/Rechner: **Karte in der Mitte**, höchstens 520 px breit. Hintergrund abgedunkelt, die Bordkarte bleibt erkennbar.
- Oben klein: **„FÜR IMMER GELERNT“**, Titel **„Etappe abgelegt!“**
- Ticket (gestrichelter Rand) mit Etappen-Titel und **„5-mal wiederholt, über 30 Lerntage. Kommt nicht mehr zum Wiederholen.“**; goldenes Siegel **„FÜR IMMER“** fällt gedreht auf das Ticket.
- **„+30 ★“** groß, daneben „Sonder-Sterne fürs Ablegen“.
- Fortschritt des Flugs (nur wenn > 1 Etappe): **„{Flug}: {a} von {n} Etappen abgelegt – noch {n−a}, dann wird der Flug golden.“** mit Gold-Leiste (das neue Stück leuchtet auf).
- Knopf: im Check-in **„Weiter einchecken ›“**, sonst „Weiter ›“.
- Bewegung ≤ 1,5 s: Blatt hoch, Siegel, Balkenstück, drei Funken.
- Wird mit derselben Antwort der Flug abgelegt: **dieses Blatt entfällt**, es folgt sofort Ansicht 5.
- Einmal je Kind und Etappe (Server).

## 5 Flug abgelegt (100 ★, ganzer Bildschirm)
Auslöser: `abgelegt.flug`. Größer als „Flug geschafft“ (AB-A): ganzer Bildschirm, Gold auf Dunkel.
- Oben **„ALLE ETAPPEN FÜR IMMER GELERNT“**, Titel **„FLUG ABGELEGT!“** in Gold-Schrift.
- Text: **„Alle {n} Etappen von {Flug} sitzen für immer. Im Reisepass ist der Flug jetzt golden.“**
- Mitte: aufgeschlagener Reisepass mit drei Flug-Zeilen; die Zeile des Flugs glüht auf und wird gold (Bewegung). Dahinter langsame Strahlen.
- Unteres Blatt: **„+100 ★“** groß, daneben „für den ganzen Flug“ und „+30 ★ für die letzte Etappe“.
- Bei `ort_gold`: Zeile mit kleinem goldenen Stempel **„Und: Alle Flüge in {Ort} sind abgelegt. Dein Stempel ist jetzt golden!“** (nach dem Reise-Umbau: Land statt Ort).
- Knopf **„Weiter ›“** (im Check-in zur nächsten Bordkarte), Textlink „Reisepass ansehen“.
- Handy bis 360 × 640 ohne Scrollen. Einmal je Kind und Flug.

## 6 Gold im Reisepass
Daten: `schule_konto` – je Flug `abgelegt`, `etappen_abgelegt`, `etappen`; je Ort `gold`.
- **Flug ganz abgelegt:** Eintrag mit Gold-Verlauf, dunkle Schrift, rechts **„★ ABGELEGT“**, Unterzeile **„{Ort} · alle Etappen für immer gelernt“**.
- **Teilweise:** rechts **„{a} von {n} abgelegt“** mit kleiner Gold-Leiste (ein Kästchen je Etappe). Bei 0 und gelandet: „noch nichts abgelegt“; nicht gelandet: nichts.
- **Orts-Stempel golden** bei `gold`: gleiche Form, Gold-Füllung, dunkle Schrift, Zeile „★ GOLD ★“. Kein zusätzlicher Stempel, kein neues Abzeichen; Direkt/Sauber/Ausdauer bleiben.
- Beim ersten goldenen Eintrag einmal der Satz: „Gold heißt: Das sitzt für immer.“

## 7 Vorschläge zu offenen Punkten aus WD-6
- **Verhältnis zu „sicher“ (◉):** Für das Kind nur ein Zustand nach außen: **Gold = abgelegt**. „Sicher“ kommt im Kindertext nicht mehr vor. Eltern/Lehrer: ◉ „Kann er komplett“ bleibt; abgelegte Flüge zusätzlich mit kleinem Gold-Punkt am ◉ (Matrix, Plan). Zwei Wörter für Ähnliches entfallen damit auf der Kinderseite.
- **Rückfall durch Nachtest:** wie vorgeschlagen (einmalig mit 7 Lerntagen zurück in den Takt). **Gold bleibt**, keine Einblendung, kein Hinweis für das Kind; Eltern/Lehrer sehen in „Was wackelt“ „abgelegt, im Nachtest aufgefallen“.
- **Gesetzte Flüge (WD-4):** Das Kind sieht wartende Etappen nicht. Eltern/Lehrer: „kommt ab {Datum}“.
- **Sterne:** Zeigt die App heute bei einer Wiederholung 10 ★, bleibt die Anzeige bei dem, was der Server meldet (`wiederholung.sterne`) – die Vorgabe zeigt 5 als Beispiel.

## Prüfen nach dem Bau
400 / 820 / 1280; 360 × 640 ohne Scrollen bei 4 und 5; Runde mit 6, 9 und 12 Bordkarten (Päckchen); alter Server ohne neue Felder → wie 0.84.0; Einblendungen nur einmal; „weniger Bewegung“; keine Wörter mitten im Wort umbrochen; Testkind und erfundene Daten.
