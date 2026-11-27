# Vorgabe WK, dritte Runde: „Was wackelt“ – Auswertung, letzte Fehler, nach Themen

Designer, 27.11.2026. Ersetzt `../entwurf1/` und `../entwurf2/` (beide abgelehnt). Entwurf: `index.html` (eine Datei, ohne Netz), Bilder: `bilder/`.
Grundlage sind die Antworten des Nutzers: „mehrfach eine Struktur, vielleicht eine Auswertung, letzte Fehler, dann schön strukturiert nach den Themen und wann, und wenn abgearbeitet muss es auch wieder verschwinden“. Bearbeitung nur „Abhaken“ und „Nachüben schicken“.
Adresse für feste Zustände: `#k=1|2&z=z7|z14|alles&g=hell|nacht&leer=1&erl=1`. Daten erfunden („Kind 1“ Kl. 5, „Kind 2“ Kl. 8, heute Fr 27.11.2026).

## 1 Aufbau (eine Seite, drei Teile, von oben nach unten)
Kopf wie in der App: „Lernen Schule“ · Kind-Umschalter (Kind 1 Kl. 5 | Kind 2 Kl. 8) · Reiter Überblick | **Was wackelt** | Lehrplan · rechts Zeitraum (7 Tage | **14 Tage** | Alles). Titel „Was wackelt bei Kind 2“, rechts unauffällig „Erledigtes ansehen“ (klappt eine schlichte Liste mit „zurückholen“ auf).

**1 Auswertung** – vier Kacheln nebeneinander (unter 1100 px zwei, am Handy eine Spalte), darunter ein Satz Fazit:
- *Fehler je Thema*: waagrechte Balken, rot = offene falsche, grün = richtig oder erledigt, Zahl „3 von 4“; nach offenen Fehlern sortiert, höchstens 6. Klick springt zum Thema in Teil 3.
- *Letzte Lerntage*: die letzten 7 Tage mit Antworten als Säulen richtig (grün) / falsch (rot).
- *Kommt immer wieder*: höchstens 3 Fehlerarten, die im Zeitraum ≥ 2-mal vorkamen und noch mindestens einmal offen sind; Name, „4×“, Themen. Klick springt zum ersten Thema.
- *Nur einmal passiert*: Zahl der Lernkarten mit genau einem offenen Fehler (ohne wiederkehrende Fehlerart), darunter „davon n danach richtig gelöst“.
- *Fazit*: „Am meisten hakt es bei **{häufigste wiederkehrende Fehlerart}** (n×), dann bei **{Thema mit den meisten offenen Fehlern außerhalb davon}** (n falsch); {Themen der Einmal-Fehler, die danach richtig waren} waren Ausrutscher.“

**2 Letzte Fehler** – die 4 neuesten offenen falschen Aufgaben, zweispaltig (Handy einspaltig), sofort vollständig.
**3 Nach Themen** – alle offenen Fehler: Thema (nach Zahl offener Fehler) → Lernkarte → Aufgaben, neueste zuerst. Je Lernkarte „Alle abhaken“ und „Nachüben schicken“.

**Ein Baustein für Teil 2 und 3** (Karte, Ecken 19 px): Zeile „Thema · Lernkarte“ links, Tag rechts · Aufgabentext · Tabelle/Zeichnung klein (210 px) bzw. die Zeilen des Fehler-Detektivs (gewählte rot, richtige grün) · zwei Felder nebeneinander **eingegeben** (zartes Rot) | **richtig** (zartes Grün) · eine Zeile „Fehler: …“ (+ „im 2. Anlauf“, „mit Tipp“, „danach richtig gelöst“) · „Lösungsweg“ zum Aufklappen · Knöpfe **Abhaken** und **Nachüben schicken**.

Optik: Farben und Ecken aus `style.css`, `body[data-area="lernen"]` (Grund #f6f4ec, Karten #fffefa, Schrift #22372e, Überschriften/Akzent #254d3e, ok/err/warn/info aus Zeile 3583); Systemschrift; keine Versalien-Überschriften. Dunkel nach `:root` (prefers-color-scheme: dark) mit grünem Akzent #62d8c4 – **[Hinweis]** der Lehrerbereich der App ist heute nur hell (`color-scheme: light` für `data-area="lernen"`).

## 2 Regeln fürs Verschwinden
1. **Offen** = endgültig falsche Antwort (wie R0-Grundmenge in umsetzung1 Abschnitt 3) im Zeitraum, nicht abgehakt, nicht durch Nachüben erledigt.
2. **Abhaken** (Aufgabe oder ganze Lernkarte) nimmt die Antwort sofort aus allen drei Teilen; die Auswertung rechnet neu; 5 s „Rückgängig“. Abgehaktes steht nur unter „Erledigtes ansehen“.
3. **Nachüben schicken** lässt die Aufgabe stehen mit dem Hinweis „Nachüben liegt in der nächsten Übung von Kind 2 (seit T.M.)“; „Abhaken“ bleibt möglich.
4. Löst das Kind **nach** dem Schicken eine Aufgabe derselben Lernkarte richtig (ohne Tipp), verschwindet die Antwort von selbst (zählt als erledigt).
5. Ein neuer Fehler ist eine neue offene Antwort – nichts „öffnet sich wieder“, er steht einfach oben in „Letzte Fehler“.
6. Leer (nichts offen): ein Satz „Alles abgearbeitet – Kind 1 hat gerade keine offenen Fehler. Weiter so.“, darunter die Auswertung des Zeitraums und als Fazit „In den letzten 7 Tagen n Aufgaben, davon m richtig.“

## 3 Datenbedarf
Wie `../entwurf1/umsetzung1.md` Abschnitt 5 (Lese-Aktion `schule_wackelt_analyse` mit allen endgültig falschen Antworten im Zeitraum samt Aufgabe, Lösungsweg, Anlauf, Tipp, Folge danach; Fehlbild-Kennungen aus `aufgabe.fehlbilder` in Stufe 2). Neu bzw. geändert:
- **Abhaken je Antwort**: heute gibt es nur `schule.wackelt_status` je Thema/Etappe und `schule.besprochen` je Etappe. Nötig: Tabelle `schule.fehler_erledigt (lernender_id, versuch_id, art 'abgehakt'|'nachgeuebt', am, von)` und Aktion `schule_fehler_abhaken {lernender_id, versuch_ids[]}` (+ Rückgängig). Stufe 1 ersatzweise: Etappe über `schule_notiz_setzen {besprochen}` / `schule_wackelt_setzen` als „besprochen“ – wirkt aber nur je Lernkarte, nicht je Aufgabe.
- **Nachüben schicken – heute vorhanden** [im Repo gelesen]: die Kinder-Abflugtafel hat eine Liste „Nachbessern“ für Etappen, die *wieder offen* sind (H1: zwei Fehler in der Wiederholung); „Kann er – aber wiederholen“ / „Wieder in die Wiederholung“ im Lehrplan holt einen ganzen Flug in die Wiederholung (Takt: höchstens 6 Etappen je Lerntag). Eine gezielte Auswahl einzelner Aufgaben für das Kind gibt es nicht.
- **Nachüben schicken – fehlt**: Tabelle `schule.nachueben (lernender_id, versuch_id, aufgabe_id, einheit_id, lernziel, geschickt_am, erledigt_am)`; Aktion `schule_nachueben_schicken {lernender_id, versuch_ids[]}`; die Übung des Kindes nimmt offene Nachübe-Einträge zuerst (dieselbe Lernkarte, eine noch nicht gesehene Aufgabe, sonst die falsche selbst); beim nächsten richtigen Versuch der Lernkarte ohne Tipp `erledigt_am` setzen. Für den Hinweis liefert `schule_wackelt_analyse` je Antwort `nachueben_am`.
- Auswertung: alles aus denselben Versuchsdaten (Fehler je Thema = offene / alle Antworten je `thema_id`; Lerntage = Antworten je Tag; Fehlerart = `fehlbild` bzw. `grund`).

## 4 Bilder (`bilder/`, 1440 × 900 und 400 × 860)
01 oben hell · 02 Mitte (Letzte Fehler) · 03 Nach Themen · 04 Seitenende · 05 nach Abhaken (Meldung, ein Fehler weniger) · 06 Nachüben geschickt (Hinweis an der Aufgabe) · 07 leer · 08 oben dunkel · 09 Kind 1 oben · 10 Erledigtes ansehen · 11 Handy oben · 12 Handy Fehler · 13 Handy dunkel Fehler · 14 ganze Seite.
