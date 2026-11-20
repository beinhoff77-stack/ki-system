# Postfach kann-1 – AB-I, Texte „kann“ und „kurz“ (Klasse 5 und 6)

**Zweig:** `kann-1-b` (lokal als `kann-1` vom Stand `lernen-app` @ `dc76450` angelegt; gepusht als `kann-1-b`)

**Wichtig – Doppelarbeit:** Beim Pushen lag auf GitHub bereits ein Zweig `kann-1` mit einer vollständigen Fassung desselben Auftrags (Commits `4c0c3ec`, `3ec7a5f`, 20.11. 06:03, eigener Bericht mit „FERTIG: AB-I, Chat 1“). Er wurde **nicht überschrieben**. Diese Fassung liegt daneben auf `kann-1-b`. Sebastian bzw. der Haupt-Chat entscheidet, welche übernommen wird.
Unterschied laut demselben Prüfskript: Die Fassung auf `kann-1` lässt viele `kann`-Texte mit einem groß geschriebenen Substantiv beginnen (z. B. „Zahlen …“) und hat bei `bruch.prozent/verstehen` ein Fragezeichen am Ende; sonst keine Befunde (Schlüssel, Längen, JSON in Ordnung). Diese Fassung hier beginnt jeden Text mit einem klein geschriebenen Wort und hat keine Befunde.
**Auftrag:** `inhalte/AUFTRAEGE.md`, „Bau-Auftrag AB (20.11.)“, Unterabschnitt „AB-I – Texte ‚kann‘ und ‚kurz‘“

## Ergebnis
- 25 Dateien `inhalte/kann/<thema_schluessel>.json` – alle Themen mit `klasse.gym_by` 5 oder 6 laut `inhalte/themenliste.json`; keines der 10 aufgelösten Themen gehört zu Klasse 5/6, ausgelassen wurde also nichts.
- 193 Etappen-Texte `kann`, 25 Texte `kurz`. Grundlage je Etappe: Titel, Regel, Erklärung und die Aufgaben aller Stufen der Etappe in `inhalte/themen/<thema>.json`.
- Commits (auf `kann-1-b`): einer für Klasse 5 (14 Themen, 112 Etappen), einer für Klasse 6 (11 Themen, 81 Etappen) samt diesem Bericht.
- Nichts außer `inhalte/kann/` und diesem Bericht angelegt oder geändert. Kein Merge.

### Klasse 5
| Thema | Etappen | Länge `kurz` | längstes `kann` |
|---|---|---|---|
| `zahlen.natuerlich` | 13 | 92 | 89 |
| `zahlen.ganz` | 11 | 72 | 85 |
| `zahlen.rechengesetze` | 14 | 76 | 89 |
| `zahlen.potenzen_basis` | 7 | 83 | 83 |
| `zahlen.teilbarkeit` | 7 | 91 | 76 |
| `groessen.einheiten` | 8 | 82 | 78 |
| `groessen.proportional` | 8 | 89 | 80 |
| `geometrie.grundbegriffe` | 7 | 97 | 89 |
| `geometrie.winkel` | 7 | 83 | 85 |
| `geometrie.ortslinien` | 6 | 103 | 90 |
| `messen.flaechen` | 7 | 94 | 73 |
| `messen.koerper_berechnung` | 5 | 100 | 76 |
| `stochastik.kombinatorik` | 7 | 74 | 80 |
| `gleichungen.einfach` | 5 | 90 | 74 |

### Klasse 6
| Thema | Etappen | Länge `kurz` | längstes `kann` |
|---|---|---|---|
| `zahlen.potenzen_zehner` | 7 | 80 | 82 |
| `bruch.brueche` | 14 | 79 | 89 |
| `bruch.dezimal` | 8 | 75 | 89 |
| `bruch.rechnen` | 12 | 81 | 89 |
| `terme.potenzgesetze` | 3 | 83 | 82 |
| `bruch.prozent` | 6 | 82 | 87 |
| `finanzen.zinsen` | 8 | 78 | 71 |
| `daten.darstellen` | 6 | 93 | 80 |
| `daten.kennwerte` | 3 | 61 | 77 |
| `messen.flaechen_vielecke` | 7 | 99 | 79 |
| `messen.volumen` | 7 | 94 | 87 |

## Selbstprüfung (Skript unten, Stand dieses Zweigs)
```
Klassen [5]: Themen soll 14, Etappen 112, längstes kurz 103, längstes kann 90
Dateien außerhalb dieser Klassen: ['bruch.dezimal', 'bruch.brueche', 'daten.kennwerte', 'messen.volumen', 'zahlen.potenzen_zehner', 'daten.darstellen', 'bruch.prozent', 'finanzen.zinsen', 'messen.flaechen_vielecke', 'terme.potenzgesetze', 'bruch.rechnen']
Keine Fehler.
Klassen [6]: Themen soll 11, Etappen 81, längstes kurz 99, längstes kann 89
Dateien außerhalb dieser Klassen: ['zahlen.ganz', 'groessen.proportional', 'geometrie.winkel', 'zahlen.potenzen_basis', 'zahlen.rechengesetze', 'geometrie.grundbegriffe', 'geometrie.ortslinien', 'zahlen.teilbarkeit', 'stochastik.kombinatorik', 'zahlen.natuerlich', 'gleichungen.einfach', 'groessen.einheiten', 'messen.koerper_berechnung', 'messen.flaechen']
Keine Fehler.
Klassen [5, 6]: Themen soll 25, Etappen 193, längstes kurz 103, längstes kann 90
Dateien außerhalb dieser Klassen: keine
Keine Fehler.
```
Geprüft je Datei: gültiges JSON; genau die Schlüssel `thema_schluessel`, `kurz`, `etappen`; `thema_schluessel` passt zum Dateinamen; jede Etappe (`lernziel`) der Themendatei hat genau einen Eintrag, keine überzähligen Schlüssel; `kurz` ≤ 110 Zeichen und beginnt mit „Du“; `kann` ≤ 90 Zeichen, beginnt mit Kleinbuchstaben, ohne Satzzeichen am Ende, ohne doppelte Leerzeichen; `kann` enthält den Etappen-Titel nicht wörtlich (als ganzes Wort/Wortgruppe). Zusätzlich: keine Datei in `inhalte/kann/`, die nicht zu Klasse 5/6 gehört.

**Hinweis zu „klein begonnen“:** Weil Substantive im Deutschen groß bleiben müssen, beginnt jeder `kann`-Text mit einem klein geschriebenen Wort (Artikel, Verb, Adjektiv, Präposition), z. B. „eine Zahl …“, „mit negativen Zahlen …“. So ist die Vorgabe erfüllt, ohne die Rechtschreibung zu verletzen.

## Nicht maschinell prüfbar – von Hand eingehalten, bitte stichprobenhaft gegenlesen
- **Kein Lob, nichts versprechen, was die Etappe nicht übt:** Jeder Text wurde gegen Regel und Aufgaben der Etappe geschrieben. Formulierungen wie „auch rückwärts“, „auch mit Minuszeichen“, „auch mit Rest“ stehen nur dort, wo Aufgaben der Etappe das verlangen.
- **`kurz` ohne Fachwort, das erst im Flug erklärt wird:** z. B. „Potenz“, „Primzahl“, „Dreisatz“, „Koordinatensystem“, „Kubikmeter“ wurden in `kurz` umschrieben. Grenzfälle, die ich als aus der Grundschule bzw. dem Alltag bekannt gewertet habe: „Prozent“, „Umfang“, „Flächeninhalt“, „Brüche“, „Maßstab“, „Quader“, „Würfel“, „Gleichung“ steht nicht drin (umschrieben als „Zahlenrätsel“).

## Auffälligkeiten (nur gemeldet, nichts geändert)
1. `umfang` in der Themenliste verspricht mehr, als die Etappen der Themendatei enthalten. Die `kurz`-Texte richten sich nach den Etappen, nicht nach `umfang`:
   - `zahlen.teilbarkeit`: `umfang` nennt ggT und kgV – die stehen als Etappen in `bruch.brueche`, nicht hier.
   - `messen.koerper_berechnung`: `umfang` nennt Volumen, Prisma, Zylinder, Pyramide, Kegel, Kugel – die Etappen behandeln nur Quader/Würfel und Oberfläche.
   - `daten.kennwerte`: `umfang` nennt Median, Modalwert, Spannweite, Quartile, Boxplot – die 3 Etappen behandeln nur den Mittelwert.
   - `terme.potenzgesetze`: Titel/`umfang` nennen Potenzgesetze und rationale Exponenten – die 3 Etappen üben Potenzbegriff, negative Exponenten/Hoch 0 und Fehlersuche, keine Potenzgesetze als eigene Etappe.
   - `bruch.prozent`: Titel „Prozent- und Zinsrechnung“, aber keine Zins-Etappe (Zinsen in `finanzen.zinsen`).
   Folge für die App: Fällt sie bei fehlendem `kurz` auf `umfang` zurück, verspricht sie bei diesen Themen zu viel; mit den neuen `kurz`-Texten nicht mehr.
2. `gleichungen.einfach` hat `klasse.gym_by` 5, steht in der Themenliste aber hinter den Klasse-6-Themen – nur zur Kenntnis, für AB-I ohne Belang.

## Prüfskript
```python
import json,sys,os,re
root=sys.argv[1]; klassen=[int(x) for x in sys.argv[2].split(',')]
aus={'groessen.verhaeltnisse','mengen.grundbegriffe','abbildungen.vektoren','funktionen.scharen','funktionen.folgen','finanzen.zinseszins','gleichungen.reinquadratisch','funktionen.transformation','funktionen.umkehr','stochastik.bedingt'}
L=json.load(open(root+'/inhalte/themenliste.json'))
soll={t['thema_schluessel']:t for t in L if (t.get('klasse') or {}).get('gym_by') in klassen and t['thema_schluessel'] not in aus}
fehler=[]; n_et=0; maxk=0; maxe=0
for s,t in soll.items():
  p=f'{root}/inhalte/kann/{s}.json'
  if not os.path.exists(p): fehler.append(f'{s}: Datei fehlt'); continue
  try: d=json.load(open(p,encoding='utf-8'))
  except Exception as e: fehler.append(f'{s}: kein gültiges JSON ({e})'); continue
  if set(d)!={'thema_schluessel','kurz','etappen'}: fehler.append(f'{s}: Schlüssel {sorted(d)}')
  if d.get('thema_schluessel')!=s: fehler.append(f'{s}: thema_schluessel falsch')
  k=d['kurz']; maxk=max(maxk,len(k))
  if len(k)>110: fehler.append(f'{s}: kurz {len(k)} Zeichen')
  if not k.startswith('Du '): fehler.append(f'{s}: kurz beginnt nicht mit „Du“')
  th=json.load(open(root+'/'+t['datei'],encoding='utf-8'))
  lz=[e['lernziel'] for e in th['inhalt']['etappen']]
  tit={e['lernziel']:e.get('titel','') for e in th['inhalt']['etappen']}
  if len(set(lz))!=len(lz): fehler.append(f'{s}: doppelte lernziele in Themendatei')
  et=d['etappen']
  for x in set(lz)-set(et): fehler.append(f'{s}: Etappe {x} fehlt')
  for x in set(et)-set(lz): fehler.append(f'{s}: überzähliger Schlüssel {x}')
  for x,v in et.items():
    n_et+=1; maxe=max(maxe,len(v))
    if len(v)>90: fehler.append(f'{s}/{x}: {len(v)} Zeichen')
    if not v or not v[0].islower(): fehler.append(f'{s}/{x}: nicht klein begonnen')
    if v.rstrip()[-1:] in '.!?': fehler.append(f'{s}/{x}: Satzzeichen am Ende')
    if v!=v.strip() or '  ' in v: fehler.append(f'{s}/{x}: Leerzeichen')
    tt=tit.get(x,'').lower().rstrip('?').strip()
    if tt and re.search(r'(?<!\w)'+re.escape(tt)+r'(?!\w)', v.lower()): fehler.append(f'{s}/{x}: wiederholt Titel wörtlich')
extra=[f[:-5] for f in os.listdir(root+'/inhalte/kann') if f.endswith('.json') and f[:-5] not in soll]
print(f'Klassen {klassen}: Themen soll {len(soll)}, Etappen {n_et}, längstes kurz {maxk}, längstes kann {maxe}')
print('Dateien außerhalb dieser Klassen:',extra or 'keine')
print('FEHLER:' if fehler else 'Keine Fehler.'); [print(' -',f) for f in fehler]
```
Aufruf: `python3 pruefen.py <repo> 5,6`

FERTIG: AB-I, Chat 1
