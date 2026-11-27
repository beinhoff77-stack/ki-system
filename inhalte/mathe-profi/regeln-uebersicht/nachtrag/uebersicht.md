# Nachtrag zu den Nachschlage-Tafeln: Stand

Entwurf, nichts in die App eingespielt. Dateien: `nachtrag.json` (zwölf neue Einträge), `klassen-nachtrag.json` (Klassen und Berichtigung), `kurzformen.md` (Befund), `pruefen.py`.

## 1. Neue Einträge (geprüft, `nachtrag.json`)
| Kennung | Inhalt | ab Klasse | Beleg |
|---|---|---|---|
| nt-01 | Dreisatz proportional (Verfahren in Schritten) | Gymnasium 5 · Realschule 6 | groessen.proportional/dreisatz |
| nt-02 | Dreisatz antiproportional | Gymnasium 8 · Realschule 7 | groessen.indirekt/dreisatz |
| nt-03 | 1. Strahlensatz (Skizze mit Koordinaten) | Gymnasium 9 · Realschule 9 | abbildungen.aehnlichkeit/strahlensatz1 |
| nt-04 | 2. Strahlensatz | Gymnasium 9 · Realschule 9 | abbildungen.aehnlichkeit/strahlensatz2 |
| nt-05 | Geschwindigkeit v = s : t mit Umstellungen | Gymnasium 8 · Realschule offen | gleichungen.formeln/einsetzen |
| nt-06 | Dichte ρ = m : V mit Umstellungen | Klasse offen | kein Beleg in einer Etappe |
| nt-07 | Quadratische Pyramide: M = 2 · a · hₛ und O = a² + 2 · a · hₛ (O steht auch in fk-19, hier mit hₛ aus h) | Gymnasium 10 · Realschule 9 | raum.pyramide_kegel_kugel/pyr_oberflaeche |
| nt-08 | Kreisring: zwei Ränder uₐ und uᵢ (kein einzelner Umfang) | Gymnasium 8 · Realschule 9 | messen.kreisberechnung/zusammengesetzt |
| nt-09 | Kongruenzsatz SSS (Skizze) | Gymnasium 7 · Realschule 7 | geometrie.konstruktion/kongruenzsatz |
| nt-10 | Kongruenzsatz SWS | wie nt-09 | wie nt-09 |
| nt-11 | Kongruenzsatz WSW | wie nt-09 | wie nt-09 |
| nt-12 | Kongruenzsatz SsW | wie nt-09 | wie nt-09 |

Die Skizzen der Kongruenzsätze und Strahlensätze haben Punkte mit Koordinaten (cm) und Markierungen mit Maß; `pruefen.py` misst Seiten und Winkel nach.

## 2. Klassen für Einträge ohne Klasse (`klassen-nachtrag.json`)
Die Tafel-Dateien bleiben dafür unverändert: `tafeln/pruefen.py` lässt als Beleg nur Etappen zu.
- Klasse ergänzt: zw-w01 Summand (Gymnasium 5 · Realschule 5 · IB 1, frühestes Vorkommen in Aufgaben der Klasse-5-Themen; der Lehrplan-Wortlaut liegt nicht im Repo).
- Klasse offen, mit Begründung: fg-08, fg-11 (Dreiecksarten), zz-09, zz-11, zz-12, zz-15 (Teilbarkeit durch 4, 6, 8, 25: Thema Klasse 5, aber keine Etappe), sw-08, sw-09, sw-10, sw-11 (Vorsilben: erklärt erst bei Zehnerpotenzen, Gymnasium 6 · Realschule 7), ff-13, ff-14, ff-15, ff-16, ff-17 (Umfänge: Figur ab Klasse 6, Umfang kein Lernziel).

## 3. Ungereimtheiten
- Parallelogramm: erledigt. `ff-04`: g = Grundseite, eine der Seiten a oder b, zu ihr gehört h. `ff-14`: a und b heißen „Seite a“ und „Seite b“. `tafel.md` angepasst. `pruefen.py` verlangt, dass „Grundseite“ nur bei g steht.
- V1 „Bei Flächen (Klasse 6)“: Beleg für Klasse 5 vorhanden, `inhalte/pruefung/lehrplan/lk_daten_2211.json` (Gymnasium 4.2 und Realschule 5, Etappe einheiten, Rolle neu) und `inhalte/themen/messen.flaechen.json`. Die Tafel (einheiten.json) sagt schon 5. V1 steht in `daten/regeln-universum.json` und darf hier nicht geändert werden: offen für den App-Bau, Wortlaut in `klassen-nachtrag.json` unter berichtigungen. Der Hinweis in `einheiten/vorschlag.md` („Klasse prüfen“) ist damit geklärt.

## 4. Kurzformen
Siehe `kurzformen.md`: keine falsch; zu ergänzen D4, G25, A19.

## Offen
- V1 im Universum auf Klasse 5 ändern (App-Bau).
- Dreisatz Realschule: Themendatei Klasse 6, Lehrplan-Kopie führt Klasse 5 als neu; Klasse in nt-01 nach der Themendatei, Zweifel bleibt.
- Geschwindigkeit Realschule und Dichte: Klasse offen.
- Nicht beauftragt, weiter ohne Klasse: zw-18, zw-23, zw-29 bis zw-35, zw-g5, zw-g9, zw-g10, zw-w03, zw-w04, zw-w08, zw-w09.
