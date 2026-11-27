# Nachtrag zu den Nachschlage-Tafeln: Stand

Entwurf, nichts in die App eingespielt. Dateien: `nachtrag.json` (zwölf neue Einträge), `klassen-nachtrag.json` (Klassen und Berichtigung), `kurzformen.md` (Befund), `pruefen.py`.

## 1. Neue Einträge (geprüft, `nachtrag.json`)
| Kennung | Inhalt | ab Klasse | Beleg |
|---|---|---|---|
| nt-01 | Dreisatz proportional (Verfahren in Schritten) | Gymnasium 5 · Realschule 6 (App-Thema; erste Lehrplan-Zuordnung Klasse 5) | groessen.proportional/dreisatz |
| nt-02 | Dreisatz antiproportional (Prüfschritt: Produkt Menge · Wert gleich, nicht nur gegenläufig) | Gymnasium 8 · Realschule 7 | groessen.indirekt/dreisatz |
| nt-03 | 1. Strahlensatz (Skizze mit Koordinaten) | Gymnasium 9 · Realschule 9 | abbildungen.aehnlichkeit/strahlensatz1 |
| nt-04 | 2. Strahlensatz | Gymnasium 9 · Realschule 9 | abbildungen.aehnlichkeit/strahlensatz2 |
| nt-05 | Geschwindigkeit v = s : t mit Umstellungen (t > 0, v > 0 beim Teilen) | Gymnasium 8 · Realschule offen | gleichungen.formeln/einsetzen |
| nt-06 | Dichte ρ = m : V (Masse pro Volumen) mit Umstellungen | Klasse offen | kein Beleg in einer Etappe |
| nt-07 | Quadratische Pyramide: M = 2 · a · hₛ und O = a² + 2 · a · hₛ (O steht auch in fk-19, hier mit hₛ aus h) | Gymnasium 10 · Realschule 9 | raum.pyramide_kegel_kugel/pyr_oberflaeche |
| nt-08 | Kreisring: Umfang u = uₐ + uᵢ = 2 · π · (R + r), äußerer und innerer Rand | Gymnasium 8 · Realschule 9 | messen.kreisberechnung/zusammengesetzt |
| nt-09 | Kongruenzsatz SSS (Skizze) | Gymnasium 7 · Realschule 7 | geometrie.konstruktion/kongruenzsatz |
| nt-10 | Kongruenzsatz SWS (gesuchte Länge messen; Kosinussatz nur als Kontrolle ab Klasse 10) | wie nt-09 | wie nt-09 |
| nt-11 | Kongruenzsatz WSW | wie nt-09 | wie nt-09 |
| nt-12 | Kongruenzsatz SsW (Winkel messen; Sinussatz nur als Kontrolle ab Klasse 10) | wie nt-09 | wie nt-09 |

Auflagen aus Werkstatt 1155/1156 sind in nt-01 bis nt-12 eingearbeitet (Voraussetzungen, Erkennungsregel beim antiproportionalen Dreisatz, Messen statt Trigonometrie in Klasse 7). Die Skizzen der Kongruenzsätze und Strahlensätze haben Punkte mit Koordinaten (cm) und Markierungen mit Maß; `pruefen.py` misst Seiten und Winkel nach.

## 2. Klassen für Einträge ohne Klasse (`klassen-nachtrag.json`)
Die Tafel-Dateien bleiben dafür unverändert: `tafeln/pruefen.py` lässt als Beleg nur Etappen zu.
- Klasse ergänzt: zw-w01 Summand (Gymnasium 5 · Realschule 5 · IB 1, frühestes Vorkommen in Aufgaben der Klasse-5-Themen; der Lehrplan-Wortlaut liegt nicht im Repo).
- Klasse offen, mit Begründung: fg-08, fg-11 (Dreiecksarten), zz-09, zz-11, zz-12, zz-15 (Teilbarkeit durch 4, 6, 8, 25: Thema Klasse 5, aber keine Etappe), sw-08, sw-09, sw-10, sw-11 (Vorsilben: erklärt erst bei Zehnerpotenzen, Gymnasium 6 · Realschule 7), ff-13, ff-14, ff-15, ff-16, ff-17 (Umfänge: Figur ab Klasse 6, Umfang kein Lernziel).

## 3. Ungereimtheiten
- Parallelogramm: erledigt. `ff-04`: g = Grundseite, eine der Seiten a oder b, zu ihr gehört h. `ff-14`: a und b heißen „Seite a“ und „Seite b“. `tafel.md` angepasst. `pruefen.py` verlangt, dass „Grundseite“ nur bei g steht.
- V1: erledigt. `daten/regeln-universum.json` nennt bei Flächen jetzt Klasse 5, wie Einheitentafel (`einheiten.json`) und Lehrplan-Beleg (`lk_daten_2211.json`, Gymnasium 4.2 und Realschule 5, Etappe einheiten). Die Berichtigung bleibt in `klassen-nachtrag.json` als Beleg (Status erledigt).

## 4. Kurzformen
Siehe `kurzformen.md`: keine falsch. D4, G25 und A19 sind im Bau inzwischen ergänzt (`SONST` und `SONST_MEHR` in `tools/tafeln_bauen.cjs`): D4 mit Ordnen, Mittelwert der beiden mittleren Werte und Modalwert bei Gleichstand; G25 mit „im rechtwinkligen Dreieck, für den betrachteten spitzen Winkel α“ und Hinweisen; A19 mit Diskriminante und Normalform. Die Spalte „Kurzform im Bau“ pflegt der App-Bau.

## Offen
- Dreisatz Realschule: App-Thema Klasse 6, erste Lehrplan-Zuordnung Klasse 5; nt-01 folgt dem App-Thema, Zweifel bleibt (Entscheidung beim App-Bau).
- Geschwindigkeit Realschule und Dichte: Klasse offen.
- Klassen-Nachtrag: bei den 15 offenen Einträgen steht jetzt je ein Vermerk „Vorkommen“ gegen „erste ausdrückliche Behandlung“; die Klassen selbst bleiben offen.
- Nicht beauftragt, weiter ohne Klasse: zw-18, zw-23, zw-29 bis zw-35, zw-g5, zw-g9, zw-g10, zw-w03, zw-w04, zw-w08, zw-w09.
