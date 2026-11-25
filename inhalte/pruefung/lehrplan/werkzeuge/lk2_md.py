import json, collections
J = json.load(open('/tmp/lp/inhalte/pruefung/lehrplan/lk_teilung_2211.json'))
SPN = {'gym_by': 'Gym', 'rs_I': 'RS I', 'rs_II_III': 'RS II/III', 'ib_standard': 'IB Std', 'ib_extended': 'IB Ext'}
def k(x): return '–' if not x else ('/'.join(map(str, x)) if isinstance(x, list) else str(x))
nT = sum(len(t['teile']) for t in J['teilungsliste']); nTh = len(J['teilungsliste'])
VC = collections.Counter((v['spur'], v['art']) for v in J['verstoesse'])
L = []

MK = J['mehrere_klassen']
def sp_rows(filt):
    out = []
    for m in MK:
        if not filt(m): continue
        neu = ', '.join(f"`{e}`" for e in m['neue_etappen']) or '–'
        out.append(f"| {m['thema']} {m['titel']} | {SPN[m['spur']]} | {m['erste_klasse']} → {m['klasse']} | {', '.join(map(str, m['punkte']))} | {neu} | **{m['entscheidung']}** | {m['anzeige']} | {m['begruendung']} |")
    return '\n'.join(out)
IBC = collections.Counter(m['entscheidung'] for m in MK if m['spur'].startswith('ib'))
IBW = sorted({(m['thema'], m['titel'], m['klasse']) for m in MK if m['spur'].startswith('ib') and m['entscheidung'] == 'wiederholung'})
NM = J['nicht_mehr_mehrere_klassen'][0]
ZK = [k for k in J['kanten_je_schulart'] if k['art'] in ('Zusatz', 'empfohlen') or k['grund'] == 'letzter Pflicht-Teil davor']
ZK_TXT = '\n'.join(f"| {k['schulart']} | {k['braucht_von']} | {k['braucht']} | **{k['art']}** | {k['grund']} |" for k in ZK)
NKA = len(J['kanten']); NKZ = sum(1 for k in J['kanten'] if 'Zusatz' in k['art_je_schulart'].values())

SCHN = {'gym': 'Gym', 'rs_I': 'RS I', 'rs_II_III': 'RS II/III', 'ib_standard': 'IB Std', 'ib_extended': 'IB Ext'}
def pf_row(th, tp):
    P = tp['pflicht_etappen_je_schulart']
    cells = ' | '.join((f"{len(P[s])}/{len(tp['etappen'])}" + (' (Zusatz)' if not P[s] else '')) for s in SCHN)
    kuer = '; '.join(f"`{e['lernziel']}`: " + ', '.join(SCHN[x] for x in e['kuer_in']) for e in tp['etappen'] if e['kuer_in']) or '–'
    st = ' · '.join(f"K{k}: {v['erledigt']}/{v['pflicht']}" + (' **vollständig**' if v['vollstaendig'] else '') for k, v in tp['stand_je_kind'].items())
    vo = ' · '.join(f"K{k}: {v['erledigt']}/{v['etappen']}" for k, v in tp['stand_je_kind_vorher'].items())
    return f"| {th['thema']} Teil {tp['teil']}/{tp['von']} | {cells} | {kuer} | {st} | {vo} |"
PF_TAB = '\n'.join(pf_row(th, tp) for th in J['teilungsliste'] for tp in th['teile'])
UNG = [x for x in J['stand_je_kind_ungeteilt'] if x['vollstaendig'] != x['vorher_alle_etappen'] or x['vollstaendig'] != x['flug_geschafft']]
UNG_TXT = '\n'.join(f"| {x['kind']} | {x['thema']} {x['titel']} | {x['erledigt']}/{x['pflicht']} | {'ja' if x['vorher_alle_etappen'] else 'nein'} | {'ja' if x['flug_geschafft'] else 'nein'} |" for x in UNG)
VP = J['vertiefung_aber_lehrplanpunkt']
VP_GYM = [f"{v['thema']} `{v['lernziel']}`" for v in VP if 'gym' in v['pflicht_in']]
NE = sum(len(x['etappen']) for x in J['etappen_kuer']); NK = collections.Counter(s for x in J['etappen_kuer'] for e in x['etappen'] for s in e['kuer_in'])
ARTC = collections.Counter((sch, v['status'], v['art']) for x in J['etappen_kuer'] for e in x['etappen'] for sch, v in e['status_je_schulart'].items())
def art_txt(sch):
    return (f"{ARTC[(sch, 'pflicht', 'zugeordnet')]} zugeordnet · {ARTC[(sch, 'pflicht', 'integrativ') ] + ARTC[(sch, 'pflicht', 'integrativ_ib')]} integrativ Pflicht · "
            f"{ARTC[(sch, 'kuer', 'entschieden')]} Kür (entschieden) · {ARTC[(sch, 'kuer', 'kein_lehrplanstoff')]} Kür (Thema dort kein Lehrplanstoff)")
ART_TAB = '\n'.join(f"| {SCHN[s]} | {art_txt(s)} |" for s in SCHN)
EINS = [f"{th['thema']} Teil {tp['teil']}" for th in J['teilungsliste'] for tp in th['teile'] if len(tp['pflicht_etappen_je_schulart']['gym']) == 1]
NULL = [f"{th['thema']} Teil {tp['teil']} ({', '.join(SCHN[s] for s, v in tp['status_je_schulart'].items() if v == 'Zusatz')})" for th in J['teilungsliste'] for tp in th['teile'] if 'Zusatz' in tp['status_je_schulart'].values()]
def bsp(t, e, sch):
    for x in J['etappen_kuer']:
        if x['thema'] == t:
            for y in x['etappen']:
                if y['lernziel'] == e:
                    v = y['status_je_schulart'][sch]
                    return f"{t} `{e}` ({SCHN[sch]}): **{v['status']}**" + (f", Quelle {', '.join(map(str, v['quelle']))} (Kl. {v['klasse']})" if v['quelle'] else '') + f" – {v['grund']}"
L.append(f"""# LK-D 4 – Pflicht und Kür je Etappe, Schulart und Gruppe (22.11.2026; „Entscheidungen 17:05“ und „Rückläufer ChatGPT 942/943“, 17:40)

## Ergebnis vorab

- **A1 (Muss) – √2:** Neue Lernkarte **20 `irrational_beweis`** „Warum √2 kein Bruch ist“ (Gym 9 1/k3, Punkt 202).
  - Die Aufgaben üben drei Dinge: Beweisschritte ordnen (Lücken mit Schrittnummern), Fehler im Beweis finden (Näherungswert statt Beweis, fehlender zweiter Teil) und einen Schritt begründen (Paritätsargument, gekürzter Bruch, Widerspruch).
  - Umfang: 22 Aufgaben, Prüfskript ohne Fehler.
  - Punkt 202 hat jetzt `zahlarten, irrational_beweis`, also nicht mehr „durch Zahlarten abgedeckt“.
  - In RS (758/971: Irrationalität nur nennen/erklären) ist die Etappe Kür. Klassen unverändert.
- **B1 (Muss) – Pflicht/Kür aus dem Punkt-Mapping mit Quellen-Punkt:** Jede Etappe hat je Schulart und Gruppe `status_je_schulart` mit `status` (pflicht/kuer), `art`, `quelle` (Punkt-IDs), `klasse`, `gruppe` und `grund`.
  - Die Art sagt, woher der Status kommt:
    - `zugeordnet`: Ein Hauptpunkt verlangt die Etappe.
    - `integrativ`: Ein Punkt deckt die Etappe inhaltlich mit ab. Das habe ich einzeln entschieden, der Quellen-Punkt kann aus einem anderen Thema stammen.
    - `entschieden`: Kür, einzeln begründet.
    - `kein_lehrplanstoff`: Das Thema hat in dieser Schulart/Gruppe weder Haupt- noch Nebenbezug.
    - `integrativ_ib`: siehe Annahme unten.
  - **„Keine Zuordnung“ ist nicht mehr automatisch Kür.** Gym, RS I und RS II/III habe ich jede Etappe ohne Zuordnung einzeln entschieden: {sum(1 for k in ARTC if k[0] in ('gym', 'rs_I', 'rs_II_III') and k[2] in ('integrativ', 'entschieden') for _ in range(ARTC[k]))} Entscheidungen. Jede Entscheidung steht mit Quelle und Grund je Etappe in `etappen_kuer`.
  - **Annahme IB:** IB ist nur Orientierung (Inhaltsverzeichnisse). Dort gilt eine Etappe in einem Thema mit IB-Bezug als Pflicht (`integrativ_ib`, Quelle = erster IB-Punkt des Themas). Das ist nicht einzeln geprüft.

| Schulart/Gruppe | Etappen (alle {NE}) |
|---|---|
{ART_TAB}

**Beispiele, die ChatGPT nannte:**
- {bsp(46, 'punktspiegelung', 'gym')}
- {bsp(46, 'drehung', 'gym')}
- {bsp(46, 'vektor_drehen', 'gym')}
- {bsp(26, 'geschickt', 'gym')}
- {bsp(26, 'aenderung', 'gym')}
- {bsp(101, 'prisma_volumen', 'rs_I')}

**Folgen gegenüber dem ersten LK-D-4-Stand (nur Zuordnung):**
- **101 Teil 1 ist in RS I und II/III Pflicht, nicht Zusatz.** RS I Kl. 9 (Punkt 783) bzw. RS II/III Kl. 10 (Punkt 1009) verlangt Prismen und Zylinder (Punkt hängt an 92).
- **26 im Gymnasium:** Teil 1 hat 4 Pflicht-Etappen, Teil 2 hat 3. Vervielfachen, Prüfen und geschickte Zwischenschritte gehören zur Schlussrechnung (Punkt 41); nur `aenderung` bleibt Kür.
- Teile mit genau **einer** Pflicht-Etappe im Gymnasium: {', '.join(EINS) or '–'}.
- Ganz Zusatz (0 Pflicht-Etappen): {'; '.join(NULL)}.
  - Gym 44 Teil 2 und 46 Teil 2 bleiben Zusatz. Inhaltlich geprüft: Gym 7 konstruiert nur Dreiecke und kennt nur Achsen- und Punktspiegelung.
- **Kinder (beide Gymnasium):**
  - Kind 2 hat 29 Teil 2 mit 3/3 vollständig.
  - Kind 2 hat 99 vollständig (`drachen_raute` ist im Gymnasium Kür).
  - Kein bereits geflogener Flug wird durch neue Pflicht-Etappen wieder offen.

**Regel (Entscheidung 17:05, Punkt 1):** Eine Etappe, die in der Schulart des Kindes nicht Pflicht ist, ist dort **Kür**: Sie zählt nicht für Flug-Abschluss, Flug-Test und Stempel. Ein Teil ohne Pflicht-Etappe ist „Zusatz“.

**JSON (`lk_teilung_2211.json`):**
- In `teilungsliste`:
  - jede Etappe hat `kuer_in`, `klasse_je_schulart` und `status_je_schulart`;
  - jeder Teil hat `pflicht_etappen_je_schulart` und `status_je_schulart` (Pflicht/Zusatz);
  - `stand_je_kind` zählt nur Pflicht-Etappen; der Stand vor der Kür-Regel steht in `stand_je_kind_vorher`.
- `etappen_kuer`: dasselbe für alle {len(J['etappen_kuer'])} Themen.
- `stand_je_kind_ungeteilt`: Stand der Kinder in den ungeteilten Themen.

### Pflicht-Etappen je Teil und Schulart, Stand je Kind

Spalten Gym bis IB Ext: Pflicht-Etappen / alle Etappen des Teils.

| Teil | Gym | RS I | RS II/III | IB Std | IB Ext | Kür-Etappen (Schulart) | Stand jetzt (nur Pflicht, Gym) | Stand vorher (alle Etappen) |
|---|---|---|---|---|---|---|---|---|
{PF_TAB}

### Ungeteilte Themen: Stand der Kinder

Nur Fälle, in denen sich etwas ändert oder Stand und Flug nicht zusammenpassen.

| Kind | Thema | Pflicht erledigt | vorher alle Etappen? | Flug geschafft? |
|---|---|---|---|---|
{UNG_TXT}

- **Kind 2 in 24, 30, 57 und 100:** Alle Pflicht-Etappen sind erledigt, aber kein Flug ist abgeschlossen. Annahme: Es fehlt der Flug-Test.

### Widerspruch zum Inhalt: „Vertiefung“ in der Themendatei, aber Pflicht nach Lehrplan

- **{len(VP)} Etappen** stehen in der Themendatei unter `lernziele_vertiefung` (heute Kür für alle), sind aber in mindestens einer Schulart Pflicht.
  - Im Gymnasium: {', '.join(VP_GYM)}.
  - Darunter die neuen LK-Etappen, z. B. 20 `irrational_beweis`, 61 `darstellen`, 101 `cavalieri`.
- **Offen, Sebastian/TL-S:** Welche Angabe gilt?
  - Mein Vorschlag: Pflicht/Kür je Schulart nach dieser JSON, und `lernziele_vertiefung` nur noch als Vorgabe für Etappen ohne Lehrplanbezug.
  - Die Liste steht in `vertiefung_aber_lehrplanpunkt`.

### F1 und F3 – geliefert in Commit c7a86ada

- F1: {len(J['mehrere_klassen'])} Fälle in `mehrere_klassen`.
  - 57: Wiederholung ohne neue Etappe.
  - 2: nicht teilen.
- F3: 61 `darstellen`.
- **Für `reise-aufbau`:** Neue Etappen seit LK-D 3 sind 61 `darstellen`, 91 `raumwinkel` und jetzt 20 `irrational_beweis` (20 ist nicht geteilt, also kein neuer Flug).

---

""")
L.append(f"""# LK-D 3 – Teilungsliste nach der neuen Regel (22.11.2026; mit Ergänzung „Rückläufer ChatGPT 939/940“, 16:40)

## LK-D 3, Ergänzung 939/940 – Ergebnis vorab

**(1) Zählung berichtigt.**
- Die 6 Themen der Entscheidung von 16:20 ergeben **13 Teile und 7 neue Flüge** (26: 2 · 29: 2 · 44: 2 · 46: 3 · 61: 2 · 91: 2). Die Angabe „15 Teile, 9 Flüge“ war mein Zählfehler.
- Mit 101 aus dem Gym-Audit: **{nTh} Themen, {nT} Teile, {nT - nTh} neue Flüge.** Daran ändert diese Ergänzung nichts.

**(2) Muss F1 – alle Themen mit Hauptpunkten in mehreren Klassen.**
- Gezählt habe ich maschinell gegen `lk_daten_2211.json`: je Thema und Spur jede Klasse mit Hauptpunkt; als „neu“ zählt eine Etappe, die in keiner früheren Klasse dieser Spur verlangt war.
- Ergebnis: **{len(MK)} Fälle** (Thema × Spur × spätere Klasse). In der JSON steht jeder Fall unter `mehrere_klassen`, mit Entscheidung, Anzeige und Begründung.
- Die Anzeigen für „Wiederholung ohne neue Etappe“ stehen zusätzlich in `wiederholung_anzeige`.
- **Gymnasium:** nur 101 (8 → 10), bereits geteilt.
- **RS I:** 26, 29, 44, 46 (zweimal), 61 und 91 sind geteilt, 57 ist Wiederholung.
- **Thema 2 hat in RS I nur noch Hauptpunkte in Kl. 7.** ChatGPT hat vermutlich den Stand vor LK-D 2 gelesen (Feld `vorher` von 734/749). Begründung siehe unten.
- **101:** geteilt, siehe Gym-Audit.

| Thema | Spur | Klassen | Punkte (spätere Klasse) | neue Etappen dort | Entscheidung | Anzeige | Begründung |
|---|---|---|---|---|---|---|---|
{sp_rows(lambda m: not m['spur'].startswith('ib'))}
| {NM['thema']} {NM['titel']} | RS I, RS II/III | vorher 7 → 8, jetzt nur 7 | {', '.join(map(str, NM['punkte']))} | – | **{NM['entscheidung']}** | {NM['anzeige']} | {NM['begruendung']} |

- **IB (nur Orientierung, löst keine Teilung aus):** {IBC['grenzfall']} Grenzfälle mit neuen Etappen in der späteren Klasse (Anzeige „wird in Kl. x weitergeführt“) und {IBC['wiederholung']} Wiederholungen ohne neue Etappe (Anzeige „wird in Kl. x wieder aufgegriffen“).
  - Die Wiederholungen betreffen: {'; '.join(f'{t} {ti} (Kl. {k})' for t, ti, k in IBW)}.
- **Offen bei 57:** Die Etappe `irrefuehrend` übt das Erkennen verzerrter Diagramme. „Berichtigen/verbessern“ (RS 5 und RS 7) kommt in ihren Aufgaben kaum vor.
  - Das ist keine neue Etappe, sondern eine Lücke in den Aufgaben. Vorschlag: einige Aufgaben „richtige Darstellung wählen“ ergänzen. Nicht geliefert.

**(3) Muss F2 – Zusatz-Regel je Schulart in den JSON-Kanten.**
- Jede der {NKA} Kanten in `kanten` hat jetzt `art_je_schulart` mit „hart“, „empfohlen“ oder „Zusatz“ (null = Kante gilt in dieser Schulart nicht).
- Regeln:
  - Ist der Teil, der etwas braucht, in der Schulart Zusatz, steht dort „Zusatz“: keine Pflicht, sperrt nichts. Das betrifft {NKZ} Kanten.
  - Ist die Voraussetzung Zusatz, steht dort „empfohlen“.
  - Sonst gilt die bisherige Art.
- Jeder Teil hat `status_je_schulart` (Pflicht/Zusatz).
- Gymnasium wie verlangt:
  - **46 Teil 3 ← Teil 1 hart**, ← Teil 2 nur empfohlen;
  - **44 Teil 2 Zusatz** (← Teil 1: „Zusatz“);
  - ebenso 46 Teil 2.
- `kanten_je_schulart` führt die Zusatz-Teile jetzt ausdrücklich mit art „Zusatz“:

| Schulart | Teil | braucht | Art | Grund |
|---|---|---|---|---|
{ZK_TXT}

**(4) Sollte F3 – 61 Teil 1 und 91.**
- **61 Teil 1 – Baumdiagramm und Vierfeldertafel (RS 8 I 7/K1, Punkt 950; II/III 6/K1, Punkt 968): fehlten.**
  - Die Etappen `begriffe` und `rel_haeufigkeit` enthalten in keiner Aufgabe ein Baumdiagramm oder eine Vierfeldertafel. Die Nebenbezüge 60 und 63 liegen in RS I erst in Kl. 9 bzw. 10.
  - Geliefert: **neue Etappe 61 `darstellen` „Baumdiagramm und Vierfeldertafel“** (22 Aufgaben, Vertiefung), zugeordnet zu 950 und 968. Außerdem zu Gym 8 5/k5 (Punkt 185, Baumdiagramm).
  - **61 Teil 1 hat damit 3 Etappen** und ist kein Kurzflug mehr. Klassen bleiben gleich (Gym 8, RS I 8).
- **91 gegen die Anforderungen von Kl. 7 und 8 (RS I) geprüft:**
  - Kl. 7, Punkt 881 – Lage von Geraden/Ebenen und Raumwinkel:
    - Die Lage war gedeckt (`lage`), **Raumwinkel fehlte**.
    - Geliefert: **neue Etappe 91 `raumwinkel` „Winkel im Raum“** (22 Aufgaben). Sie kommt in 91 Teil 1 (RS I 7); dort stehen jetzt 4 Etappen.
  - Kl. 7, Punkt 882 – Schrägbilder mit Verzerrung und Achsenlage zeichnen:
    - `pyramide` übt nur Ecken, Kanten und Flächen; den Verzerrungsfaktor enthält `wahre_groesse`.
    - 882 bekommt deshalb zusätzlich `wahre_groesse`; ebenso II/III 959.
    - Das Zeichnen selbst geht in der App nicht und bleibt Papierarbeit.
  - Kl. 7, Punkt 883 – wahre Größe: gedeckt (`wahre_groesse`).
  - Kl. 8, Punkte 939, 940, 941 – Körpersymmetrie, Axialschnitt und Rotation, Koordinaten: gedeckt (`koerper_symmetrie`, `axialschnitt`, `rotation`, `koordinaten`).
- **Kinder:** Kein Kind hat in 61 oder 91 etwas erledigt, die neuen Etappen ändern also keinen Stand.
- **SQL:**
  - Nur die Begründungstexte von 185 haben sich geändert (Etappe `darstellen`).
  - Die Änderungszahlen bleiben 33/18/13/187.
  - Die RS-Punkte 950, 968, 881, 882 und 959 sind im SQL nicht enthalten, weil sich an ihrer Themenzuordnung nichts ändert. Ihre Etappen stehen in der JSON.
  - Probelauf auf dem vollständigen echten Stand: LP-RS zweimal, dann LK-D zweimal, bestanden; `thema_jahrgang` unverändert.

---

""")
L.append(f"""## Frühere Fassung (LK-D 2/3, Stand nach „Entscheidung Teilung“ 16:20)

## LK-D 3 – was sich gegenüber der Entscheidung von 16:20 ändert

- **Die Entscheidung von 16:20 nennt die alte, falsch gezählte Fassung:** „6 Themen → 15 Teile, 9 neue Flüge“.
  - Richtig waren für diese 6 Themen 13 Teile und 7 neue Flüge (26: 2 · 29: 2 · 44: 2 · 46: 3 · 61: 2 · 91: 2 = 13).
  - Die Aufteilung je Thema in der Entscheidung stimmt, nur die Summe nicht.
- **Gym-Audit (ChatGPT 937, Muss A1) liegt vor** (Abschnitt 1; geliefert mit Commit 83d61a2e). Es bringt **ein weiteres geteiltes Thema: 101 Prismen und Zylinder** (Teil 2 von 2 · schiefe Körper und Cavalieri, Gym 10 / RS I 9).
  - **Damit steht die Liste: 7 Themen, 15 Teile, 8 neue Flüge.**
  - Dazu je eine neue Etappe in den schon geteilten Themen 29 (Teil 2) und 91 (Teil 2); die Zahl der Teile ändert das nicht.
- **Kind 2, Thema 29 (betrifft Punkt 4 der Entscheidung):** Teil 2 hat durch die neue Etappe „Gleichungen mit Klammerprodukten“ jetzt 4 Etappen, Kind 2 hat 3. **Teil 2 ist nach dem Umhängen also nicht vollständig.**
  - Stempel und die 100 Flug-Sterne für Teil 2 kommen erst, wenn die neue Etappe gelandet ist.
  - Alternative: die neue Etappe in Teil 2 als Zusatz führen, dann ist Teil 2 für Kind 2 sofort vollständig. Sebastian entscheidet.
- **Zusatz-Regel umgesetzt:** je Teil und Schulart `zusatz` in der JSON; Kanten je Schulart in `kanten_je_schulart` (Abschnitt 3a).
- **IB-Zählung:** 2 harte Verstöße je Kurs (63 ← 61, 29 ← 102), nicht 3. LK-D-Bericht und Postfach sind berichtigt.
- **Kurzflüge:** 44 Teil 2 und 61 Teil 1 (je 2 Etappen), neu 101 Teil 2 (1 Etappe).

---

Grundlage: AUFTRAEGE `lernen-app`:
- „Teilungsregel NEU“ (15:30), „Berichtigung“ (15:35), „Ergänzung – Benennung und Aufbau“ (15:40);
- „Stand 15:50 – Rückläufer ChatGPT 936/937“ (Muss A1, IB Muss B1).

Daten aus LK-D (`lk_daten_2211.json`, Stand nach dem Live).
- Nichts eingespielt. Kinder nur als Nummern.
- JSON: `lk_teilung_2211.json` (Teile, Grenzfälle, alle Voraussetzungs-Kanten, Verstöße, Aufbau-Kette je Teil).

**Berichtigungen gegenüber der ersten Fassung von LK-D 2:**
- Die erste Fassung meldete „15 Teile, 9 neue Flüge“. Richtig waren **13 Teile, 7 neue Flüge** (6 Themen); ich hatte falsch gezählt.
- Mit dem Audit (Abschnitt 1) kommt 101 Prismen und Zylinder dazu. Stand jetzt: **{nTh} Themen, {nT} Teile, {nT - nTh} neue Flüge.**
- **IB-Voraussetzungen (Muss B1):**
  - Der LK-D-Bericht nannte „3 harte Verstöße je Kurs“. **Das war falsch, es sind 2:** 63 ← 61 und 29 ← 102. Einen dritten gab es in keiner Fassung der Daten.
  - Bericht und Postfach sind berichtigt; die JSON war schon richtig.
  - Stand jetzt je IB-Kurs: {VC[('ib_standard','hart')]} hart, {VC[('ib_standard','empfohlen')]} empfohlen.

## 1 Audit an den Übergängen 7→8, 8→9, 9→10 (Muss A1)

**Vorgehen:**
- Für Gymnasium und RS Gruppe I habe ich jeden Punkt ab Klasse 8 gesucht, der nur Etappen verlangt, die schon in einer früheren Klasse neu waren. Das sind Kandidaten für „der Lehrplan verlangt mehr, als unsere Etappen enthalten“.
- Danach habe ich die Punkte geprüft, deren Kurzfassung einen neuen Aspekt nennt (Beweis, Verallgemeinerung, schiefe Körper, Symmetrie).
- Kriterium: Deckt eine vorhandene Etappe den verlangten Inhalt ab?

| Übergang | Punkt | verlangt (eigene Worte) | bisher | Befund | geliefert |
|---|---|---|---|---|---|
| Gym 8→10 | Gym 10 5/k4 (285) | Volumen schiefer Prismen, Volumengleichheit (Cavalieri) | 101 `prisma_volumen` (gerade Körper, Gym 8) | **fehlte** | neue Etappe **101 `cavalieri`** „Schiefe Körper und Cavalieri“ → eigener Teil (101 Teil 2 von 2, Gym 10) |
| RS 8→9 | RS 9 I 5/K1 (781), II/III 10 2/K2 (1007) | Cavalieri bzw. Grenzwertidee für Volumen | 92 `verstehen` | **teilweise** | jetzt 101 `cavalieri` (92 bleibt Neben); RS-I-Klasse von 101 Teil 2 = 9 |
| RS 7→8 | RS 8 I 3/K1 (939) | Symmetrische Körper: Symmetrieebenen, -achsen, -zentren | 91 `pyramide` (Ecken, Kanten) | **fehlte** | neue Etappe **91 `koerper_symmetrie`** „Symmetrie von Körpern“ (91 Teil 2, RS 8) |
| RS 7→8 | RS 8 I 4/K3 (734), II/III 3/K3 (749) | lineare Gleichungen mit binomischen Ausdrücken auf beiden Seiten | 2 `klammern`, `beide_seiten` (RS 7) | **fehlte** | neue Etappe **29 `gleichungen_binomisch`** „Gleichungen mit Klammerprodukten“ (29 Teil 2, RS 8); 2 bleibt Neben |
| RS 7→8 | RS 8 I 1/K1 (930) | Vierecke nach Eigenschaften unterscheiden | 46 `vierecke_ordnen` (RS 6) | gedeckt | – (Wiederholung, Anzeige „weitergeführt“) |
| RS 8→9 | RS 9 I 8/K3 (800) | Ergebnisraum bilden | 61 `begriffe` (RS 8) | gedeckt | – |
| Gym 8→9 | Gym 9 1/k3 (202) | Irrationalität von √2 durch indirekten Beweis | 20 `zahlarten` | **teilweise** (Beweisgedanke fehlt) | nicht geliefert: Ein Beweis lässt sich in der App nur als Lückentext abbilden. Vorschlag: Begründen-Aufgabe in 20 ergänzen (offen) |
| Gym 9→10 | Gym 10 3/k3 (271) | große und negative Winkel auf 0 bis 2π zurückführen | 38 `periode` | gedeckt (Periodizität) | – |

**Neue Inhalte:**
- Je Etappe 12 Übungen (Stufe 1–3, alle Aufgabentypen), 1 Test, 3 Korrektur, 6 Sicherung, dazu ein Kann-Satz.
- Alle Lösungen sind berechnet, die Texte selbst formuliert.
- Sie stehen in `_lk_etappen_2211.py`, eingehängt in `messen.prisma_zylinder.py`, `terme_umformen.py` und `raum.schraegbilder.py`; diese Generatoren erzeugen die Dateien danach unverändert.
- Prüfskript: alle Inhalte OK. Die Karten sind wie in LK-D Vertiefung; Flug und Stempel bestehender Themen bleiben unverändert.

**Folgen:**
- Die Zuordnung in `lk_daten_2211.json` und `lk_korrektur_2211.sql` ist angepasst:
  - 285 bekommt die Etappe `cavalieri` (Thema unverändert);
  - 781: 92 → 101;
  - 734: 2 → 29;
  - 939 bekommt die Etappe `koerper_symmetrie`.
- **Das SQL hat sich damit geändert:** 33/18/13/187 statt 31/18/13/185 Änderungen.
- Probelauf auf dem vollständigen echten Stand erneut bestanden: LP-RS, dann LK-D zweimal. Klassen unverändert.
- **Der Probelauf des Haupt-Chats von 15:50 galt der alten Fassung.**

## 2 Verfahren der Teilung

- **Klasse einer Etappe je Schulart:** die erste Klasse, in der ein Lehrplanpunkt sie als Hauptthema verlangt.
- **Teilung:** Etappen mit gleichem Klassenpaar (Gym, RS I) bilden einen Teil, also die feinste gemeinsame Teilung, sortiert nach Klasse.
  - Hat eine Etappe nur in einer Schulart eine Klasse, kommt sie zum passenden Teil.
  - Hat sie in keiner eine Klasse, kommt sie zum Teil der Etappe davor (nur 26: 2 Etappen).
- **IB und RS II/III** lösen keine Teilung aus; wo ein Teil dort mehrere Klassen hat, steht er bei den Grenzfällen.

## 3 Teilungsliste: {nTh} Themen, {nT} Teile

- Im Gymnasium liegen die Teile eines Themas in derselben Klasse und kommen dort als Teil 1, 2, 3 nacheinander. Ausnahme: 101, Teil 2 liegt im Gymnasium in Klasse 10.
- Keine Gym-Klasse ändert sich.
""")
for th in J['teilungsliste']:
    L.append(f"\n### {th['thema']} {th['titel']}" + (f" · Flug geschafft: Kind {', '.join(map(str, th['flug_geschafft_kinder']))}" if th['flug_geschafft_kinder'] else '') + "\n")
    L.append("| Teil | Titel · Untertitel | Etappen | Gym | RS I | RS II/III | IB Std / Ext | Kind 1 | Kind 2 |\n|---|---|---|---|---|---|---|---|---|")
    for p in th['teile']:
        kl = p['klasse']
        g = f"{kl['gym'] if kl['gym'] else '–'}" + (' *' if kl['gym_ohne_eigenen_punkt'] else '')
        r = f"{kl['rs_I'] if kl['rs_I'] else '–'}" + (' *' if kl['rs_I_ohne_eigenen_punkt'] else '')
        ets = ', '.join(e['titel'] + (' °' if e['lernziel'] in p['etappen_ohne_lehrplanpunkt'] else '') for e in p['etappen'])
        st = lambda x: f"{p['stand_je_kind_vorher'][x]['erledigt']}/{p['stand_je_kind_vorher'][x]['etappen']} (Pflicht Gym {p['stand_je_kind'][x]['erledigt']}/{p['stand_je_kind'][x]['pflicht']})"
        L.append(f"| {p['teil']}/{p['von']} | {p['titel']} · {p['untertitel']}{' **(dünn)**' if p['zu_duenn'] else ''} | {ets} | {g} | {r} | {k(kl['rs_II_III'])} | {k(kl['ib_standard'])} / {k(kl['ib_extended'])} | {st('1')} | {st('2')} |")
L.append("""
Legende:
- `*`: Diese Schulart hat für den Teil keinen eigenen Lehrplanpunkt; die Klasse folgt aus der Reihenfolge.
- `°`: Etappe ohne Lehrplanpunkt in Gym und RS I.
- „–“: kein Lehrplanstoff in dieser Spur.
- Stand: erledigt/Etappen des Teils (gelandet, gesetzt oder nachgewiesen).

**Zu dünn (nur gemeldet, nichts ergänzt):**
- 44 Teil 2 (2 Etappen), 61 Teil 1 (2) und 101 Teil 2 (1, neu).
- Vorschlag: Kurzflug mit 1–2 Städten.

**Lernstand (Regel Punkt 6):**
- Nur Kind 2 hat Lernstand in einem geteilten Thema: 29 Terme umformen, Flug geschafft.
- Teil 1 ist vollständig (5/5).
- **Teil 2 hat durch die neue Etappe „Gleichungen mit Klammerprodukten“ jetzt 4 Etappen, Kind 2 hat 3/4.** Ohne die Audit-Ergänzung wäre Teil 2 vollständig (3/3).
- Nichts geht verloren: Der Flug-Abschluss von 29 bleibt. Teil 2 gilt erst nach der neuen Etappe als geschafft, Stempel dann nach der Regel.
- Vorschlag: die neue Etappe für Kind 2 als „nachholen“ einplanen. Sebastian entscheidet.

**Benennung:** „‹Titel› – Teil x von y“ mit Untertitel wie oben.
""")
SN = {'gym': 'Gym', 'rs_I': 'RS I', 'rs_II_III': 'RS II/III', 'ib_standard': 'IB Std', 'ib_extended': 'IB Ext'}
L.append("""## 3a Zusatz je Teil und Schulart (Regel 16:20)

Ein Teil ohne Lehrplanpunkt in der Schulart ist dort Zusatz: keine Pflicht, sperrt nichts, und Voraussetzungen auf ihn sind nur „empfohlen“.

| Teil | Gym | RS I | RS II/III | IB Std | IB Ext |
|---|---|---|---|---|---|""")
for th in J['teilungsliste']:
    for p in th['teile']:
        L.append(f"| {p['titel']} | " + ' | '.join('Zusatz' if p['zusatz'][x] else 'Pflicht' for x in ('gym', 'rs_I', 'rs_II_III', 'ib_standard', 'ib_extended')) + ' |')
L.append("""
**Kanten, die sich durch die Zusatz-Regel ändern** (vollständig in `kanten_je_schulart`):""")
for kk in J['kanten_je_schulart']:
    if not (kk['art'] == 'hart' and kk['grund'] == 'Teilung'):
        L.append(f"- {SN[kk['schulart']]}: {kk['braucht_von']} ← {kk['braucht']}: **{kk['art']}** ({kk['grund']})")
L.append("""
- Im Gymnasium braucht 46 Teil 3 hart nur Teil 1, wie entschieden.
- 101 Teil 2 braucht Teil 1 in RS I und II/III nur empfohlen: Prismen und Zylinder stehen in der Realschule bei 92. Damit ist der II/III-Verstoß „101 Teil 2 ← Teil 1“ aufgelöst.
""")
L.append(f"""## 4 Aufbau nach der Teilung

- **Teilung:** Teil n braucht Teil n−1, hart ({sum(len(t['teile']) - 1 for t in J['teilungsliste'])} Kanten).
- **Bisherige Voraussetzungen** (128, ohne stillgelegte Themen) sind dem passenden Teil zugeordnet:
  - „braucht“ geht an den ersten Teil, dessen Klasse in Gym und RS I nicht vor der Voraussetzung liegt.
  - „wird gebraucht von“ geht an den letzten Teil, der nicht nach dem abhängigen Thema liegt.
  - Drei Fälle sind inhaltlich gesetzt (Annahme): 47, 44 und 4 brauchen nur Teil 1 von 46 bzw. 29.
- Zusammen {len(J['kanten'])} Kanten, alle in der JSON.

**Wichtige Zuordnungen:**
- 29 Terme umformen:
  - Teil 1 braucht 28 und 102 (hart).
  - Teil 2 wird gebraucht von 8, 31, 97 (hart) und 35 (empfohlen).
  - 4 braucht Teil 1.
- 61 Zufall und Laplace: Teil 1 wird gebraucht von 63; Teil 2 von 62 und 64 (alle hart).
- 46 Kongruenzabbildungen: Teil 2 wird gebraucht von 74, Teil 3 von 49, Teil 1 von 47 und 44.
- 26 Proportionalität: Teil 1 braucht 25; Teil 2 wird gebraucht von 93 (hart).
- 91 Schrägbilder: Teil 1 braucht 52 (hart).
- 101 Prismen und Zylinder: Teil 2 (Cavalieri) wird gebraucht von 92 Pyramide, Kegel, Kugel (empfohlen). Das passt: Gym 10 und RS 9 begründen damit das Pyramidenvolumen.

**Prüfung der ganzen Kette gegen die Klassenlage:**
- **Gymnasium: 0 Verstöße. RS Gruppe I: 0 Verstöße.**
- RS II/III: {VC[("rs_II_III","hart")] + VC[("rs_II_III","empfohlen")]} vor der Zusatz-Regel, danach 1.
  - 37 ← 103 (empfohlen; 103 ist in II/III kein Lehrplanstoff).
  - 101 Teil 2 ← Teil 1: Nach der Zusatz-Regel ist das nur empfohlen, der Verstoß entfällt (Abschnitt 3a).
- IB je Kurs: {VC[('ib_standard','hart')]} hart, {VC[('ib_standard','empfohlen')]} empfohlen.
  - Hart: 63 ← 61 Teil 1 (MYP 1 gegen 2) und 29 Teil 1 ← 102. Das zweite ist **Sebastians Entscheidung, bleibt**, nur gemeldet.
  - Empfohlen, u. a.: 92 ← 101 Teil 2 (101 hat keine IB-Klasse), 44 ← 46, 34 ← 93, 37 ← 103, 45 ← 73, 23 ← 16, 100 ← 25.

**46 im Gymnasium:** entschieden (16:20) und umgesetzt: Teil 2 ist Zusatz, Teil 3 braucht hart nur Teil 1.

**Sollte A2 (Voraussetzungen je Etappe):** offen. Die 87 Reihenfolge-Hinweise aus LK-D sind die Grundlage. Mit der Teilung lösen sich die meisten davon auf, weil die betroffenen Etappen jetzt in getrennten Teilen liegen (26, 29, 46). Eine Liste je Etappe liefere ich auf Ansage.

## 5 Grenzfälle (keine Teilung, Anzeige „weitergeführt“)

| Thema | Teil | Spur | Klassen | Empfehlung |
|---|---|---|---|---|""")
for g in J['grenzfaelle']:
    L.append(f"| {g['thema']} {g['titel']} | {g['teil'] or '–'} | {SPN[g['spur']]} | {', '.join(map(str, g['klassen']))} | nicht teilen |")
L.append("""
- RS II/III: 8 (9 + 10) und 33 (8 + 9). Würde II/III teilen, kämen genau diese zwei Themen dazu.
- IB: Schulbuch-Orientierung, kein Teilungsgrund.

## 6 Aufbau-Kette je Teil (Anzeige)

| Teil | Baut auf | Geht weiter in |
|---|---|---|""")
for c in J['aufbau_kette']:
    if '– Teil' in c['knoten']:
        L.append(f"| {c['knoten']} | {c['baut_auf']} | {c['geht_weiter_in']} |")
L.append("""
Für alle übrigen Themen steht die Kette in `aufbau_kette` (JSON).

## Gesichert / Annahme / offen

**Gesichert:**
- Teilung nach der Regel.
- 0 Verstöße in Gymnasium und RS I.
- Keine Klassenänderung; SQL-Probelauf mit der neuen Fassung bestanden.
- Prüfskript OK.
- Die IB-Zahl der harten Verstöße ist 2 (berichtigt).

**Annahme:**
- Etappen-Klassen aus meiner Etappenzuordnung.
- Drei inhaltlich gesetzte Voraussetzungen.
- Audit-Urteil „gedeckt / teilweise / fehlte“.
- Untertitel als Vorschlag.

**Offen (Sebastian):**
- Liste mit 101 bestätigen (7 Themen, 15 Teile, 8 neue Flüge).
- Kurzflug 101 Teil 2.
- Kind 2 in 29 Teil 2: neue Etappe nachholen oder als Zusatz führen.
- 43/69/71 als Vertiefung (A3).
- Beweis-Aufgabe zu √2 (Gym 9).
- Etappen-Voraussetzungen (A2).
- Neuer Probelauf des Haupt-Chats mit der geänderten `lk_korrektur_2211.sql`.
""")
open('/tmp/lp/inhalte/pruefung/lehrplan/lk_teilung_2211.md', 'w').write('\n'.join(L))
