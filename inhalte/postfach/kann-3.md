# Postfach kann-3 (AB-I – Texte „kann“ und „kurz“, Chat 3)

## 2026-11-20 – FERTIG
Zweig `kann-3` (von `lernen-app` @ dc76450). 37 Dateien `inhalte/kann/<thema_schluessel>.json` mit `kurz` und je Etappe `kann`, 242 Etappen-Texte. Grundlage je Etappe: Titel, Regel, Einstieg und die Übungs-/Test-/Korrekturaufgaben der Themendatei.

**Umfang laut `inhalte/themenliste.json`:** Klasse 9 (14 Themen), Klasse 10 (9 Themen), ohne Gymnasium-Klasse (14 Themen). Die 10 aufgelösten Themen sind ausgelassen (davon 10 ohne Gymnasium-Klasse; in Kl. 9/10 war keins betroffen).

**Commits (je Klasse einer, Bericht extra):**
- `AB-I kann-3: Texte kann/kurz Klasse 9 (14 Themen)`
- `AB-I kann-3: Texte kann/kurz Klasse 10 (9 Themen)`
- `AB-I kann-3: Texte kann/kurz Themen ohne Gymnasium-Klasse (14 Themen)`
- dieser Bericht

Geändert wurden nur Dateien unter `inhalte/kann/` (und dieser Bericht). Keine Themendateien, Generatoren, App-Code, Datenbank, kein Merge.

| Klasse | Thema | Etappen | Zeichen kurz | längstes kann |
|---|---|---|---|---|
| 9 | abbildungen.aehnlichkeit | 8 | 86 | 83 |
| 9 | funktionen.potenz | 10 | 89 | 73 |
| 9 | funktionen.quadratisch | 9 | 94 | 77 |
| 9 | gleichungen.lgs3 | 6 | 96 | 77 |
| 9 | gleichungen.potenz | 6 | 91 | 77 |
| 9 | gleichungen.quadratisch | 8 | 87 | 81 |
| 9 | gleichungen.trig | 6 | 86 | 80 |
| 9 | stochastik.verknuepft | 11 | 75 | 81 |
| 9 | trigo.allgemein | 9 | 99 | 75 |
| 9 | trigo.pythagoras | 6 | 76 | 82 |
| 9 | trigo.rechtwinklig | 7 | 103 | 84 |
| 9 | zahlen.rationale_exponenten | 6 | 66 | 79 |
| 9 | zahlen.reell | 7 | 88 | 80 |
| 9 | zahlen.wurzeln_basis | 6 | 92 | 73 |
| 10 | funktionen.exponential_log | 7 | 92 | 90 |
| 10 | funktionen.ganzrational | 7 | 86 | 84 |
| 10 | funktionen.trig | 8 | 97 | 80 |
| 10 | gleichungen.exponential | 6 | 87 | 79 |
| 10 | gleichungen.polynom | 5 | 86 | 79 |
| 10 | raum.pyramide_kegel_kugel | 7 | 94 | 76 |
| 10 | raum.schraegbilder | 5 | 95 | 81 |
| 10 | stochastik.mehrstufig | 9 | 101 | 82 |
| 10 | stochastik.simulation | 6 | 82 | 77 |
| ohne | abbildungen.determinanten2 | 6 | 93 | 78 |
| ohne | abbildungen.matrizen | 7 | 77 | 74 |
| ohne | daten.normalverteilung | 5 | 97 | 86 |
| ohne | daten.standardabweichung | 5 | 86 | 77 |
| ohne | daten.stichproben | 5 | 82 | 75 |
| ohne | daten.zweidimensional | 5 | 91 | 85 |
| ohne | funktionen.betrag | 5 | 98 | 76 |
| ohne | funktionen.reihen | 8 | 86 | 80 |
| ohne | gleichungen.wurzel | 6 | 70 | 78 |
| ohne | sonder.graphentheorie | 5 | 90 | 75 |
| ohne | sonder.logik | 5 | 84 | 84 |
| ohne | sonder.optimierung | 5 | 90 | 86 |
| ohne | terme.quadratische_extreme | 5 | 94 | 82 |
| ohne | zahlen.schranken | 5 | 92 | 83 |

### Schreibregeln, die ich zusätzlich angewandt habe
- **„klein begonnen“ streng gelesen:** Jeder `kann`-Text beginnt mit einem klein geschriebenen Wort (Verb, Artikel, Präposition, Adjektiv, Formelzeichen wie σ). Satzanfänge mit Hauptwort wurden umgestellt („die Varianz …“, „für log_b(x) …“). Ob das so gemeint war, ist eine Annahme – falls Hauptwort am Anfang erlaubt ist, wären einige Texte flüssiger.
- **Titel nicht wörtlich:** Das Skript prüft, dass der Etappen-Titel nicht als Ganzes (ohne Groß-/Kleinschreibung) im `kann`-Text steckt. Einzelne Titelwörter kommen vor.
- **`kurz` ohne neues Fachwort:** Vermieden wurden Begriffe, die der Flug erst einführt (z. B. Matrix, Determinante, Baumdiagramm, Hypotenuse, Normalverteilung). Begriffe aus früheren Flügen (Wurzel, Potenz, Exponent, Wahrscheinlichkeit, Graph) sind drin.
- Konkrete Beispiele in `kann` stammen aus den Aufgaben der jeweiligen Etappe.

### Selbstprüfung (Skript, ausgeführt im Repo-Wurzelordner)
```python
import json, os, glob
AUS = {'groessen.verhaeltnisse','mengen.grundbegriffe','abbildungen.vektoren','funktionen.scharen','funktionen.folgen',
       'finanzen.zinseszins','gleichungen.reinquadratisch','funktionen.transformation','funktionen.umkehr','stochastik.bedingt'}
L = json.load(open('inhalte/themenliste.json'))
soll = {t['thema_schluessel']: t['klasse'].get('gym_by') for t in L
        if t['klasse'].get('gym_by') in (9, 10, None) and t['thema_schluessel'] not in AUS}
fehler = []; et_n = 0; kmax = 0; emax = 0
for s in soll:
    p = f'inhalte/kann/{s}.json'
    if not os.path.exists(p): fehler.append(f'{s}: Datei fehlt'); continue
    d = json.load(open(p))                                  # gültiges JSON
    if set(d) != {'thema_schluessel', 'kurz', 'etappen'}: fehler.append(f'{s}: Felder {set(d)}')
    if d['thema_schluessel'] != s: fehler.append(f'{s}: thema_schluessel')
    k = d['kurz']; kmax = max(kmax, len(k))
    if len(k) > 110: fehler.append(f'{s}: kurz {len(k)} Zeichen')
    th = json.load(open(f'inhalte/themen/{s}.json'))
    lz = [e['lernziel'] for e in th['inhalt']['etappen']]
    tit = {e['lernziel']: e['titel'] for e in th['inhalt']['etappen']}
    if len(lz) != len(set(lz)): fehler.append(f'{s}: doppelte lernziele in Themendatei')
    fehlt = set(lz) - set(d['etappen']); zuviel = set(d['etappen']) - set(lz)
    if fehlt: fehler.append(f'{s}: fehlt {sorted(fehlt)}')
    if zuviel: fehler.append(f'{s}: überzählig {sorted(zuviel)}')
    for l, v in d['etappen'].items():
        et_n += 1; emax = max(emax, len(v))
        if len(v) > 90: fehler.append(f'{s}/{l}: {len(v)} Zeichen')
        if v.rstrip().endswith('.'): fehler.append(f'{s}/{l}: Punkt am Ende')
        if not v[0].islower(): fehler.append(f'{s}/{l}: nicht klein begonnen')
        if l in tit and tit[l].lower() in v.lower(): fehler.append(f'{s}/{l}: enthält Titel wörtlich')
extra = sorted(os.path.basename(f)[:-5] for f in glob.glob('inhalte/kann/*.json') if os.path.basename(f)[:-5] not in soll)
print('Themen soll:', len(soll), '| davon Kl. 9:', sum(v == 9 for v in soll.values()),
      '| Kl. 10:', sum(v == 10 for v in soll.values()), '| ohne Gym-Klasse:', sum(v is None for v in soll.values()))
print('Etappen-Einträge:', et_n, '| längstes kurz:', kmax, '| längstes kann:', emax)
print('Fremde Dateien in inhalte/kann/:', extra or 'keine')
print('Fehler:', len(fehler)); [print(' -', f) for f in fehler]
```
Ausgabe:
```
Themen soll: 37 | davon Kl. 9: 14 | Kl. 10: 9 | ohne Gym-Klasse: 14
Etappen-Einträge: 242 | längstes kurz: 103 | längstes kann: 90
Fremde Dateien in inhalte/kann/: keine
Fehler: 0
```
Geprüft: jede Etappe jeder Themendatei hat genau einen Eintrag, keine überzähligen Schlüssel, nur die Felder `thema_schluessel`/`kurz`/`etappen`, `kurz` ≤ 110, `kann` ≤ 90 Zeichen, kein Punkt am Ende, klein begonnen, Titel nicht wörtlich, gültiges JSON (jede Datei mit `json.load` gelesen), keine fremden Dateien in `inhalte/kann/`.

**Nicht maschinell prüfbar (von Hand angesehen):** „konkret und prüfbar“, „kein Lob“, „nichts versprechen, was die Etappe nicht übt“. Wer gegenliest: am ehesten Grenzfälle sind `raum.schraegbilder` (Flug heißt „Schrägbilder“, die Etappen üben aber keine Schrägbild-Zeichnung – `kurz` beschreibt deshalb das, was geübt wird) und `funktionen.potenz` (enthält die Umkehrfunktionen; `kurz` nennt das „Rechnungen umkehren“).

FERTIG: AB-I, Chat 3
