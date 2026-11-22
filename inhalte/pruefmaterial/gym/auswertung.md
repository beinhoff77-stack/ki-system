# Auswertung Prüfmaterial Gymnasium Bayern – Kl. 5 und Kl. 8

Stand 2026-11-22, 3. Runde (Kl. 8 um Kl.-8-Stoff erweitert). Grundlage: `katalog.json`, Zahlen per `_bau.py` gezählt. Kennzeichnung: **[G]** gesichert (aus der Quelle), **[A]** Annahme/eigene Einschätzung, **[O]** offen.

Jede Arbeit hat jetzt das Feld `kategorie`:
**A** Gymnasium Bayern · **B** Bayern amtlich, aber Realschule/Mittelschule · **C** Bundesland unbekannt/anders oder Verlag.

## 0 Bestand und Lücken

| | Ziel | gefunden | A Gym Bayern | B Bayern RS/MS amtlich | C sonst |
|---|---|---|---|---|---|
| Kl. 5 | 50 | **53 Arbeiten, 829 Aufgaben** | 1 | 28 | 24 |
| Kl. 8 | 50 | **73 Arbeiten, 854 Aufgaben** | 57 | 12 | 4 |

- [G] **Ziel 50 formal erreicht, aber mit Einschränkung.** Kl. 5 kommt nur mit **schulartfremden** amtlichen Tests auf 50: 18 Realschul-Jahrgangsstufentests 6 (2005–2025) und 10 Mittel-/Hauptschul-Jahrgangsstufenarbeiten 6. Sie prüfen den Kl.-5-Stoff ihrer Schulart zu Beginn Kl. 6 (21 bzw. 24 P, 45 min, ohne Taschenrechner, fast nur 1-P-Aufgaben).
- [G] Für das **Gymnasium Kl. 5** gibt es weiter **keinen amtlichen Test**, und frei zugänglich ist **keine sicher bayerische Schulaufgabe**. Kategorie A hat nur den Sigena-Grundwissentest (Muster).
- [G] Bei Kl. 8 sind 20 der 73 Arbeiten **BMT8** (Grundwissen Kl. 5–7, Beginn Kl. 8) und 18 **BMT10-Auszüge** (nur die Teilaufgaben mit Kl.-8-Stoff, je 3–11).
- [G] Zum laufenden Kl.-8-Stoff gibt es jetzt 35 Arbeiten:
  - 13 aus Runde 2 (Schultests, STARK, klassenarbeiten.de)
  - neu: 10 bayerische Schulaufgaben, Exen und Stegreifaufgaben von klassenarbeiten.de. Bayern ist nur bei 3795 (G8) ausdrücklich belegt; bei den anderen ist es eine Annahme über die Begriffe „Schulaufgabe“, „Extemporale“ und „Stegreifaufgabe“. Sechs davon stammen aus 2001–2006, also vermutlich aus dem alten G9 (dazu gehören z. B. Betrag und Vektoren, markiert als „außerhalb“).
  - neu: 12 ISB-Grundwissentests Realschule Jgst. 9, WPFG I (2012, 2015–2025), Kategorie B. Ihre Aufgaben zu quadratischen Termen, Determinanten und Rotationskörpern sind als „außerhalb“ markiert.
- [G] Einen zentralen Mathe-Test zu Beginn von Kl. 9 gibt es am Gymnasium nicht (Jahrgangsstufentests Mathematik nur in 8 und 10).
- [A] Die Zuordnung „Bayern“ für STARK 8 (Klassenarbeiten Mathe 8) ist eine Annahme, weil die Themen dem G8-Lehrplan folgen.
- [G] Die alten RS/MS-Tests (bis 2016) enthalten Brüche, 15 Aufgaben. Diese sind auf `bruch.*` gemappt und als „Kl.-6-Stoff Gym“ markiert. Sie zählen in der Kl.-5-Statistik mit; das verfälscht Kl. 5 leicht.
- [O] Fehlend: echte Gym-Schulaufgaben Kl. 5 (alle vier) und Kl. 8 SA 2–4 aus Bayern.
  - Schul-Homepages veröffentlichen keine; Verlage zeigen nur Leseproben.
  - klassenarbeiten.de führt 167 Kl.-5-Gym-Arbeiten, aber ohne Bundesland.

## 1 Typischer Aufbau

| | Kl. 5 | Kl. 8 |
|---|---|---|
| Zeit | [G] amtl. Tests 45 min. [A] Schulaufgabe 45 min (Klassenarbeiten meist ohne Angabe) | [G] BMT 40 min; Schultests 35–45 min; Stegreif 18 min |
| Punkte | [G] Klassenarbeiten 23–47 P (Median ≈ 35); amtl. Tests 21/24 P | [G] Arbeiten 27–43 P; BMT 21 BE |
| Aufgabenzahl | [G] Klassenarbeiten 6–13 Aufgaben mit 2–10 P; amtl. Tests 19–24 Einzelaufgaben à 1 P | [G] Arbeiten 4–11 Teilaufgaben à 2–6 P; BMT 14–17 Teilaufgaben à 1–2 P |
| Niveau I/II/III (Punkte) | [A] alle 40/53/7 %; Kat B 41/51/8; Kat C 41/54/5 | [A] Kl.-8-Stoff (ohne BMT8) 21/66/13 %; BMT8 18/60/22 % |
| Kompetenz (Anteil Aufgaben) | [A] K5 Rechnen 34 %, K4 Darstellen 23 %, K3 Modellieren 17 %, K2 Problemlösen 11 %, K1 Argumentieren 10 %, K6 Kommunizieren 5 % | [A] K5 48 %, K1 16 %, K4 12 %, K3 10 %, K6 7 %, K2 6 % |
| Hilfsmittel | [G] amtliche Tests ohne Taschenrechner; sonst meist nicht angegeben | [G] fast immer ohne Taschenrechner |

[G] Klassenarbeiten Kl. 5 behandeln meist **ein Thema** (z. B. Zahlensysteme, Maßstab, Geometrie). Die amtlichen Tests mischen 8–10 Themen mit Einzelaufgaben.
[G] In Kl. 8 hat eine Hauptaufgabe oft einen durchgehenden Kontext, z. B. Regentonne (STARK KA 5, KA 3800) oder Mischungsaufgabe.

## 2 Häufigkeit nach Thema/Etappe (Top)

**Kl. 5** (829 Aufgaben; Kat B macht 74 % aus):
- Themen: zahlen.rechengesetze 138, zahlen.natuerlich 101, groessen.einheiten 97, messen.flaechen 89, geometrie.grundbegriffe 80, messen.koerper_berechnung 55, zahlen.ganz 46, teilbarkeit 33, gleichungen.einfach 32, daten.darstellen 32.
- Häufigste Etappen:
  - lagebeziehungen 32
  - flaechen › rechteck 28
  - rechengesetze › sach 25, termaufbau 22
  - stellenwert 21, runden_regel 20
  - massstab 19, flaechen › verstehen 19
  - zeit 17, koordinaten 17
- [A] In der App selten, in Arbeiten häufig:
  - Kombinatorik (19×)
  - Körper- und Netzaufgaben (55 + 14 Lücken)
  - Schätzen (15×)
  - Maßstab (19×)

**Kl. 8, Kl.-8-Stoff** (ohne BMT8, 236 Aufgaben): gleichungen.bruch › hauptnenner 13, funktionen.linear (deuten 9, graph_ablesen 8, schnittpunkte 4), stochastik.grundbegriffe (laplace 9, begriffe 6, gegenereignis 5), potenzgesetze_ganzzahlig › vereinfachen 7, funktionen.gebrochen (parameter 6, asymptoten 5), gleichungen.formeln › zwei_schritte 6, lgs2 › verfahren 5, Zylindervolumen 6.
**Kl. 8, BMT8** (305 Aufgaben): terme.umformen/aufstellen, gleichungen.linear, daten.darstellen, groessen.einheiten (Schätzen 8, Maßstab 9), Prozent, Vielecksflächen, Winkelsätze, Volumen.

## 3 Aufgabentypen, die in der App fehlen oder selten sind

Lücken mit Vorschlag für eine neue Etappe (Häufigkeit in Klammern):
- **Kl. 5**
  - Zahlenfolgen fortsetzen (8)
  - **Quadernetz zeichnen (7)**
  - **Würfelnetz-Lage (7)**
  - Schrägbild Quader (5)
  - Ungleichung über N (4)
  - Termwert bei Veränderung begründen (3)
  - fehlende Angabe in Sachaufgabe (3)
  - Einzelfälle: ggT, Ansichten, Gauß-Summe, Kreissektor, Quersummenregel begründen
- **Kl. 8**
  - Zahl in Gleichung passend wählen (3)
  - Mit Termen beweisen (3)
  - Bruchgleichung aus Text (2)
  - Gerade spiegeln (2)
  - Tabellenkalkulation (3)
  - Mehrfachnennungen (2)
  - Eulerscher Polyedersatz (2)
  - Ungleichungssystem grafisch (1)
  - Vierfeldertafel (1)
- **Außerhalb des Lehrplans:**
  - Kl. 5: Wahrscheinlichkeit (5, nur in RS/MS-Tests)
  - Kl. 8: mehrstufige Zufallsexperimente und Pythagoras/Wurzeln (14, nur BMT10-Auszüge und Berlin)

[A] Formate, die die App kaum hat:
- Ankreuzen mit Begründung, „Fehler finden“ (Kl. 5: 18×), offene „gib ein Beispiel an“
- Zeichnen/Konstruieren (Kl. 5: 68×)
- Schätzen mit Weg

## 4 Etappen, die nie geprüft wurden

[A] „Nie“ heißt: in diesen 53 bzw. 51 Arbeiten nicht.
- **Kl. 5**:
  - zahlen.natuerlich › unendlich
  - zahlen.ganz › deuten
  - rechengesetze › differenz_summe
  - **groessen.proportional** erkennen/vervielfachen/pruefen/geschickt/aenderung (nur Dreisatz/Sach/Einheit geprüft)
  - geometrie.winkel › um_punkt, uhr, figuren, verstehen
  - ortslinien › zwei_kreise, sachsituationen
  - kombinatorik › baumdiagramm, grenzen
  - gleichungen.einfach › probe, ohne_loesung
  - Seit Runde 1 neu belegt: römische Zahlen, Dualsystem, Zahlenstrahl, Teilbarkeitsregeln.
- **Kl. 8**:
  - lgs2 › einsetzen/gleichsetzen/grafisch/prüfen. [A] Die Aufgaben lassen das Verfahren meist frei, deshalb sind sie unter „verfahren“ gezählt.
  - ungleichungen › umformen/intervall
  - zahlen.intervalle › enthalten/beurteilen
  - koerper_darstellung › netz/zylinder/ansichten
  - kreisberechnung › exakt/sektor
  - prisma_zylinder › umstellen/sach
  - stochastik › rel_haeufigkeit/grosse_zahlen
  - funktionen.linear › aufstellen/büschel
  - indirekt › vervielfachen/sach

## 5 Reicht der Flug-Test (1 Testaufgabe je Etappe)?

**Für Schulaufgaben nein, für den Grundwissenstest eher ja** [A, gestützt auf G]:
- Die amtlichen Tests (BMT8, RS/MS-Tests) bestehen aus **vielen 1-Punkt-Einzelaufgaben** über 8–10 Themen. Das ähnelt dem Flug-Test. Ein **gemischter** Test aus mehreren Flügen käme dem nahe.
- Schulaufgaben/Klassenarbeiten haben 6–11 Aufgaben à 2–10 P. Sie sind mehrschrittig, haben einen Kontext und enthalten Zeichnen und Begründen. Das deckt der Flug-Test nicht ab.
- Niveau III hat 7 % (Kl. 5) bis 17–22 % (Kl. 8) der Punkte. K1/K2 machen 21 % (Kl. 5) bzw. 22 % (Kl. 8) der Aufgaben aus; im Flug-Test kommen sie kaum vor.
- Bedingungen fehlen: Zeitlimit, keine Hilfen, kein Taschenrechner.

## 6 Vorschlag „Schulaufgaben-Training“ (nur Vorschlag, nichts gebaut)

1. **Probe-Schulaufgabe je SA-Block**
   - alle Flüge des Lernbereichs gemischt
   - 45 min, 30–40 P, 6–11 Aufgaben
   - Verteilung ca. 25/60/15 % (Kl. 8) bzw. 40/53/7 % (Kl. 5)
   - Notenschlüssel, keine Hilfen
2. **Grundwissen-Test** im amtlichen Stil
   - 20–24 Einzelaufgaben à 1 P, 40–45 min, ohne Taschenrechner, Themen gemischt
   - für Kl. 5 → Beginn Kl. 6 und für BMT8
   - Die 18 RS-Tests und 20 BMT8 liefern dafür ein gutes Raster.
3. **Mehrschritt-Aufgaben** mit Kontext aus Etappenketten (z. B. Füllvorgang → Funktion → Zeitpunkt), Teilpunkte je Schritt.
4. **Neue Formate**: „Gib ein Beispiel an“, Wahr/falsch mit Begründung, Fehler finden, Schätzen mit Spannweite.
5. **Zeichnen/Netze/Schrägbilder** als Papieraufgabe mit Musterbild zur Selbstkontrolle.
6. Lücken aus §3 als neue Etappen prüfen (Auftrag an den Inhalte-Chat). Vorrang: Netze/Würfelnetz und Zahlenfolgen (Kl. 5), Beweisen mit Termen und Zahl passend wählen (Kl. 8).
