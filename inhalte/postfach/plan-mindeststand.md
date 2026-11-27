# Postfach plan-mindeststand (Einundzwanzigste Runde, Teil B)

Neueste Meldung oben.

## 2026-11-18 02:00 (Adelaide) – FERTIG
Ergebnis: `inhalte/pruefung/klassen/vorschlag-mindeststand.md`, ein Commit auf `plan-mindeststand`. Nur Vorschlag: Themenliste, Themendateien, Datenbank (nur gelesen) und App unverändert, kein Merge.

**Kern (Tatsachen, gerechnet):**
- Plan-Klassen für alle 95 Themen. Flüge je Klasse heute (Gym) → neu: 5: 14→16 · 6: 11→15 · 7: 9→16 · 8: 14→16 · 9: 14→21 · 10: 9→11.
- 10 Gym-Themen rutschen wegen RS nach vorn: `daten.darstellen` 6→5, `messen.koerper_darstellung` 8→5, `terme.aufstellen` 7→6, `abbildungen.kongruenz` 7→6, `zahlen.intervalle` 8→7, `gleichungen.ungleichungen` 8→7, `groessen.indirekt` 8→7, `raum.schraegbilder` 10→8, `stochastik.simulation` 10→9, `raum.pyramide_kegel_kugel` 10→9.
- 14 IB-/klassenlose Themen verteilt: je Klasse 0/3/3/3/2/3 (Kl. 5–10).
- Orte: 15 Orte bekommen eine (neue) Klasse, 6 Flüge ziehen um, danach jeder Ort genau eine Klasse, höchstens 4 Flüge (nur Rom). Neuer Ort nur für ein neues Thema (Accra, Kl. 8, Geometrie).
- 4 neue Themen vorgeschlagen: Vierecke und Drehung (8), Zentrische Streckung im KS (9), Trigonometrie-Ergänzungen (10), Graphen abbilden (10).
- Kind A (Kl. 5): +24 Flüge über Kl. 5–10 (+2/+4/+7/+2/+7/+2), dazu 4 neue Themen. Kind B (Kl. 8): 13 Flüge liegen in abgeschlossenen Klassen 5–7 (4 freigegebene Gym-Flüge, die nur früher eingeordnet sind; 9 RS-/IB-Entwürfe), Kl. 8 +2, Kl. 9 +7, Kl. 10 +2.

**Befund (Tatsache):** In der Datenbank sind genau die 71 Gym-Themen freigegeben; alle 24 übrigen sind `entwurf`. Für die Kinder werden RS-/IB-Flüge erst mit Freigabe spielbar.

**Annahmen:** Vorwissen an Etappen-Titeln, Merksätzen und Stichproben der Aufgaben geprüft (z. B. 8 π-Aufgaben in `messen.koerper_darstellung`/zylinder, 7 Netz-Aufgaben mit Dreiecksfläche, 10 Anteil/Prozent-Aufgaben in `daten.darstellen`/tabelle_auswerten, 2 Wurzel-Aufgaben in `raum.schraegbilder`). Beide Kinder folgen heute dem Gym-Plan. Teil A (läuft parallel) noch nicht eingerechnet; Berührungspunkte stehen in der Datei.

**Rechenweg:** `themenliste.json` + RS-Korrekturen/Nachträge → Plan-Klasse = min(Gym, RS korr.); Orte aus `schule.block`/`schule.block_thema` (stimmen mit `block_id` überein); Prüfung „jeder Ort genau eine Klasse, ≤ 4 Flüge“ und Zählung je Klasse per Python-Skript gegen diese Daten.

**Für den Nutzer zu entscheiden** (Liste am Ende der Datei): Plan-Klassen; Etappen-Verschiebungen bei 3 Themen und Sperren einzelner Aufgaben; IB-Verteilung (Ausweichen `funktionen.betrag` → 10, falls Kl. 9 mit 21 zu voll); Orte/Ortstitel; neue Themen (Vierecke/Drehung als ein oder zwei Flüge); Umgang mit Kind B; `rs_by` für `messen.flaechen_vielecke`, `messen.volumen`, `messen.prisma_zylinder` (6, 6, 9).
