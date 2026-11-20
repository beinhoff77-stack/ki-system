# Postfach kann-1 (AB-I, Klasse 5 und 6)

## 2026-11-20 – FERTIG
AB-I, Chat 1: Texte „kurz“ (je Thema) und „kann“ (je Etappe) für alle 25 Themen mit `klasse.gym_by` 5 oder 6 laut `inhalte/themenliste.json` (14 × Klasse 5, 11 × Klasse 6), 193 Etappen-Einträge.
Zweig `kann-1` vom Stand `lernen-app` dc76450. Zwei Commits: Klasse 5, Klasse 6 (mit diesem Bericht). Nur Dateien unter `inhalte/kann/` plus diese Postfach-Datei; keine Themendatei, kein Generator, kein App-Code, keine Datenbank, kein Merge.
Von den 10 aufgelösten Themen liegt keines in Klasse 5/6 – nichts ausgelassen.

Grundlage je Etappe: `titel`, `regel` und die Übungsaufgaben aller Stufen (s1–s3) aus `inhalte/themen/<thema>.json`. „kann“ nennt nur, was die Aufgaben tatsächlich üben.

| Kl. | Thema | Etappen | Zeichen `kurz` (≤ 110) | längstes `kann` (≤ 90) |
|---|---|---|---|---|
| 5 | zahlen.natuerlich | 13 | 106 | 87 |
| 5 | zahlen.ganz | 11 | 104 | 90 |
| 5 | zahlen.rechengesetze | 14 | 100 | 81 |
| 5 | zahlen.potenzen_basis | 7 | 103 | 82 |
| 5 | zahlen.teilbarkeit | 7 | 106 | 83 |
| 5 | groessen.einheiten | 8 | 91 | 82 |
| 5 | groessen.proportional | 8 | 92 | 78 |
| 5 | geometrie.grundbegriffe | 7 | 102 | 87 |
| 5 | geometrie.winkel | 7 | 99 | 82 |
| 5 | geometrie.ortslinien | 6 | 101 | 89 |
| 5 | messen.flaechen | 7 | 105 | 85 |
| 5 | messen.koerper_berechnung | 5 | 99 | 81 |
| 5 | stochastik.kombinatorik | 7 | 109 | 87 |
| 6 | zahlen.potenzen_zehner | 7 | 103 | 75 |
| 6 | bruch.brueche | 14 | 106 | 87 |
| 6 | bruch.dezimal | 8 | 98 | 90 |
| 6 | bruch.rechnen | 12 | 103 | 89 |
| 6 | terme.potenzgesetze | 3 | 85 | 81 |
| 6 | bruch.prozent | 6 | 95 | 73 |
| 6 | finanzen.zinsen | 8 | 108 | 79 |
| 6 | daten.darstellen | 6 | 109 | 84 |
| 6 | daten.kennwerte | 3 | 101 | 84 |
| 6 | messen.flaechen_vielecke | 7 | 105 | 85 |
| 6 | messen.volumen | 7 | 89 | 78 |
| 5 | gleichungen.einfach | 5 | 99 | 77 |

### Selbstprüfung (Skript, Ausgabe unten)
Geprüft: gültiges JSON; genau die Schlüssel `thema_schluessel`, `kurz`, `etappen`; jede Etappe der Themendatei genau ein Eintrag, keine überzähligen Schlüssel; `kurz` ≤ 110, `kann` ≤ 90 Zeichen; kein Punkt am Ende; klein begonnen; Etappen-Titel nicht wörtlich (als ganze Wortfolge) enthalten; keine fehlende oder überzählige Datei.

```
Themen: 25 Soll, 25 Dateien; Etappen-Einträge: 193; längstes kurz: 109; längstes kann: 90
OK – keine Fehler
```

```python
import json,glob,os,sys,re
aus={'groessen.verhaeltnisse','mengen.grundbegriffe','abbildungen.vektoren','funktionen.scharen','funktionen.folgen','finanzen.zinseszins','gleichungen.reinquadratisch','funktionen.transformation','funktionen.umkehr','stochastik.bedingt'}
NOMEN={'Angaben','Anteile','Anzahlen','Aufgaben','Aussagen','Brüche','Dezimalzahlen','Drehungen','Ergebnisse','Fehler','Flächen','Flächenangaben','Flächeninhalt','Fragen','Gleichungen','Größen','Jahreszinsen','Kapital','Kommazahlen','Längen','Mal-Aufgaben','Massen','Möglichkeiten','Nachfolger','Oberflächen','Potenzen','Produkte','Punkte','Quadrat','Rezepte','Sachaufgaben','Säulenhöhen','Teilwinkel','Terme','Verdoppeln','Verhältnisse','Volumen','Volumenangaben','Winkel','Zahlen','Zehnerpotenzen','Zehntel','Zeitspannen','Zinsen','Zähler'}  # Substantive: im Deutschen groß, kein Satzanfang
liste=json.load(open('inhalte/themenliste.json'))
soll={t['thema_schluessel']:t for t in liste if (t.get('klasse') or {}).get('gym_by') in (5,6) and t['thema_schluessel'] not in aus}
fehler=[];n_et=0;max_k=0;max_e=0
dateien={os.path.basename(p)[:-5] for p in glob.glob('inhalte/kann/*.json')}
for s in sorted(set(soll)|dateien):
    if s not in soll: fehler.append(f'{s}: Datei ohne Auftrag'); continue
    p=f'inhalte/kann/{s}.json'
    if s not in dateien: fehler.append(f'{s}: Datei fehlt'); continue
    try: d=json.load(open(p))
    except Exception as e: fehler.append(f'{s}: kein gültiges JSON ({e})'); continue
    if set(d)!={'thema_schluessel','kurz','etappen'}: fehler.append(f'{s}: Schlüssel {sorted(d)}')
    if d.get('thema_schluessel')!=s: fehler.append(f'{s}: thema_schluessel falsch')
    k=d['kurz']; max_k=max(max_k,len(k))
    if len(k)>110: fehler.append(f'{s}: kurz {len(k)} Zeichen')
    th=json.load(open(soll[s]['datei']))
    lz=[e['lernziel'] for e in th['inhalt']['etappen']]; titel={e['lernziel']:e['titel'] for e in th['inhalt']['etappen']}
    et=d['etappen']
    for l in lz:
        if l not in et: fehler.append(f'{s}: Etappe {l} fehlt')
    for l,v in et.items():
        n_et+=1; max_e=max(max_e,len(v))
        if l not in lz: fehler.append(f'{s}: überzähliger Schlüssel {l}')
        if len(v)>90: fehler.append(f'{s}/{l}: {len(v)} Zeichen')
        if v.endswith('.'): fehler.append(f'{s}/{l}: Punkt am Ende')
        w=v.split()[0].rstrip(',')
        if not v[:1].islower() and w not in NOMEN: fehler.append(f'{s}/{l}: nicht klein begonnen ({w})')
        if re.search(r'(?<!\w)'+re.escape(titel[l].lower().rstrip('?'))+r'(?!\w)', v.lower()): fehler.append(f'{s}/{l}: enthält Titel wörtlich')
    if len(lz)!=len(set(lz)): fehler.append(f'{s}: doppelte lernziele in Themendatei')
print(f'Themen: {len(soll)} Soll, {len(dateien)} Dateien; Etappen-Einträge: {n_et}; längstes kurz: {max_k}; längstes kann: {max_e}')
print('FEHLER:' if fehler else 'OK – keine Fehler'); [print(' -',f) for f in fehler]
sys.exit(1 if fehler else 0)
```

### Entscheidungen / Annahmen
- **„klein begonnen“** so verstanden: kein Satzanfang-Großbuchstabe. Beginnt ein Text mit einem Substantiv (z. B. „Brüche …“, „Zinsen …“, „Verdoppeln“ als Hauptwort), bleibt es nach deutscher Rechtschreibung groß. Das Skript lässt nur diese Substantive zu (Liste `NOMEN`), alles andere muss klein beginnen.
- **„keine Wiederholung des Titels Wort für Wort“**: geprüft als ganze Wortfolge (Groß/Klein egal). Texte, die anfangs den Titel enthielten (z. B. „Brüche vollständig kürzen“), sind umformuliert.
- **`kurz` ohne Fachwort aus dem Flug**: Wörter, die erst in einer Etappe erklärt werden, sind im `kurz` vermieden bzw. umschrieben – z. B. Potenz → „Kurzschrift für Mal-Aufgaben“, Dreisatz → Hefte-Beispiel, Primzahl, Zählprinzip, Ortslinie, Volumen, Kapital/Zinssatz, wissenschaftliche Schreibweise. In `kann` sind diese Fachwörter erlaubt, weil das Kind sie dann kennt.
- `zahlen.ganz/zahlengerade`: Text „Zahlen unter null …“ statt „negative Zahlen“, damit der Titel nicht wörtlich vorkommt; Inhalt gleich.
- `geometrie.winkel/kreuzung`: bewusst ohne „Nebenwinkel/Scheitelwinkel“ (Begriffe erst Klasse 7, siehe klar-kl5).

Offen: nichts. Die Texte bringt der Haupt-Chat in die Datenbank (AB-S).

FERTIG: AB-I, Chat 1
