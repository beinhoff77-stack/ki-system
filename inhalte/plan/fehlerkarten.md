# Fehler-Bordkarten (FB-S) – falsch gelöste Aufgaben kommen in der Wiederholung zurück

Stand 28.11.2026, Zweig `helfer-fehlerkarten`. Nichts eingespielt. Entscheidung des Auftraggebers (28.11.): „Ja, zurück in der Wiederholung, aber NICHT mit Kennzeichnung.“

## 1. Die Regel in einfachen Worten

1. Hat das Kind eine Übungsaufgabe nicht selbst gelöst (falsch, nur mit Tipp oder erst im zweiten Versuch), merkt sich das System diese Aufgabe als „Fehler-Bordkarte“.
2. Nach zwei Lerntagen Pause (Tage ohne Mathe zählen nicht) kommt genau diese Aufgabe als Erstes, wenn ihre Etappe in der Wiederholung oder als Mischkarte dran ist – ohne Hinweis, dass sie früher falsch war.
3. Löst das Kind sie dann selbst richtig (erster Versuch, ohne Tipp), ist sie erledigt und wird wieder ganz normal behandelt.
4. Ist sie wieder falsch, kommt sie nach derselben Pause wieder – höchstens dreimal hintereinander; danach wird sie normal behandelt, damit eine einzelne harte Aufgabe die Etappe nicht blockiert.
5. In Tests, beim Üben im Flug und bei Lückenwegen (Aufwärm-Gerüsten) ändert sich nichts; einschalten und ausschalten geht mit einem Schalter.

## 2. Fundstellen (heutiger Stand)

| Was | Wo |
|---|---|
| Auswahl Wiederholung/Mischkarte `wdh_aufgabe_waehlen` | `supabase/migrations/20261122_wd_s3_frische_aufgaben.sql` Z. 55–65, FT-S-Patch „nur zählende“ `20261203_ft_s_form_takt.sql` Z. 165–166 |
| Sperre der letzten 3 Lerntage `wdh_sperre_ab`, Lerntag `lern_datum` | `20261122_wd_s3_frische_aufgaben.sql` Z. 40–53; Regel `wdh_sperre_lerntage` Z. 34–37 |
| `heute_tag` (Tag in der Zeitzone des Kindes) | `20261120_i2_lernregeln.sql` Z. 176–184 |
| `wdh_aufgabe_da` (3 Argumente, ohne Zufall, gleiche Bedingung wie die Auswahl) | `20261122_wd_s4_nacharbeit_921.sql` Z. 184–193 (+ FT-S Z. 167); alte Fassung (2 Argumente) `20261122_wd_s_wiederholungen.sql` Z. 190–195 (+ FT-S Z. 169) – ruft die Auswahl NICHT auf |
| Aufrufer der Auswahl | `wiederholung_intern` (`wd_s3` Z. 160 ff., `cross join lateral … wdh_aufgabe_waehlen(…, false)`), `mischkarten_waehlen` (Patch `wd_s3` Z. 289–299, `…, true`) – sonst niemand (Übung im Flug: die App wählt selbst aus `einheit_lesen_intern`) |
| Tagesrunde `wdh_runde_holen` / `wdh_runde_pruefen` | `wd_s3` Z. 132–157, `wd_s4` Z. 104–117 (zählen über `wdh_aufgabe_da`, Größe `wdh_runde_groesse` `wd_s` Z. 128) |
| Mischkarten ausgeben `mischkarten` | `20261120_i4_misch_ausgabe_wieder.sql` Z. 12–60, Patches `wd_s` Z. 322–330, `wd_s3` Z. 302–306 (Stelle „schon beantwortet“) |
| Mischkarte einlösen `misch_gueltig` | `i4` Z. 64–80, Patches `fp_s2` Z. 45, `wd_s4` Z. 36–42 – prüft KEINE frühere Bearbeitung |
| „eigene Lösung“ | `versuch_wertung` `20261120_i3_lernregeln_nachpruefung.sql` Z. 24–46: `eigen` = richtig, `hilfe` 0, `anlauf` 1 (oder leer), nicht im Test; `wdh_nur_selbst` (`wd_s3` Z. 16–19) |
| Spalten `versuch` | `richtig`, `hilfe` (2. Anlauf setzt ≥ 1), `anlauf` (`w150_r2` Z. 6), `misch` (`w176_t3` Z. 17), `testsitzung_id`, `wertung_fest` (`i3` Z. 16), `am`, `client_id`; Trigger `versuch_hilfe_merken` (BEFORE), `versuch_misch_verfall` (`wd_s3` Z. 94–104) |
| `zaehlt`, `form` (Lückenweg) | `20261203_ft_s_form_takt.sql` Z. 5–13, `aufgabe_zaehlt` Z. 81 |
| Bestand Wiederholung | `inhalte/plan/neuer-stil/bestand.md` Abschnitt d) |

## 3. Was sich ändert – was nicht

**Definition Fehler-Bordkarte** (je Kind und Aufgabe, nur aus `schule.versuch` abgeleitet, keine neue Tabelle):
- *Bearbeitung* = ein Versuch ohne Test (`testsitzung_id` leer) mit `anlauf` ≠ 2; der 2. Anlauf gehört zur Bearbeitung davor. Auch Mischkarten-Antworten sind Bearbeitungen.
- *selbst gelöst* = diese Bearbeitung (ihr erster Versuch) richtig ohne Tipp (`hilfe` 0) – genau die `eigen`-Bedingung von `versuch_wertung`. Falsch, mit Tipp oder erst im 2. Anlauf richtig = nicht selbst.
- *Serie* = Zahl der Bearbeitungen seit der letzten eigenen Lösung (`schule.fehlerkarte_serie`). Fehler-Bordkarte = Serie 1 bis `fehlerkarten_max` (3).
- *fällig* = Schalter an, letzte Bearbeitung liegt vor `fehlerkarte_ab` (gleiche Lerntag-Rechnung wie `wdh_sperre_ab`, mit `fehlerkarten_pause_lerntage` = 2 Lerntagen Pause) – und die bestehende Sperre (heute + 2 vorige Lerntage) gilt weiter. Mit den heutigen Werten fallen beide zusammen: Fehler am Lerntag X, zurück am dritten Lerntag danach.
- Nur freigegebene, zählende Übungsaufgaben der Etappe (die Kandidatenmenge bleibt exakt dieselbe). `zaehlt = nein` war schon nie Kandidat. **Lückenwege** (`form = 'lueckenweg'`, auch wenn sie zählen) werden nie bevorzugt: Gerüste sind Hilfe nach Fehlern, kein Nachweis – sie bleiben normale Kandidaten.
- Warum Obergrenze 3: sonst stünde eine Aufgabe, die das Kind (noch) nicht kann, an jedem Wiederholungstag vorn; nach drei vergeblichen Runden ist „Was wackelt“/Nachtest der bessere Weg. Danach rückt sie wie jede andere nach „am längsten her“.

**Auswahl** (`wdh_aufgabe_waehlen`, eine Stelle): neuer erster Sortierschlüssel `schule.fehlerkarte_faellig(…) desc`, dann unverändert „nie bearbeitet zuerst, dann am längsten her, Stufe 1 hinten, Zufall“. Mehrere fällige: die älteste (am längsten her). Gilt für Wiederholung (Runde und freiwillig) und Mischkarte. **Mischkarten bleiben Stufe 2/3: eine Fehler-Aufgabe der Stufe 1 kommt nur in der normalen Wiederholung zurück** (gewollt, im Test geprüft; die Probe zählt sie als `davon_stufe_1_nur_wiederholung`).

**Mischkarten ausgeben** (`mischkarten`, eine Stelle): Heute verfällt eine offene Ausgabe beim nächsten Laden, wenn die Aufgabe *jemals* beantwortet wurde. Eine Fehler-Bordkarte ist immer schon beantwortet – sie verfiele beim nächsten Laden des Flugs, und ihre Antwort zählte nicht als Mischkarte (Test zeigt das am alten Stand). Mit Schalter an zählt nur noch eine Antwort *seit der Ausgabe* (eine Antwort außerhalb der Mischkarte lässt sie ohnehin sofort per Trigger verfallen). Mit Schalter aus: wörtlich wie bisher. `misch_gueltig` selbst verwirft eine früher bearbeitete Aufgabe nicht (geprüft) und bleibt unverändert.

**Unverändert** (im Nachbau geprüft, wo angegeben): Karten-Logik („sitzt“, Fälligkeit, `karte_buchen`, `karte_wdh_ereignis`), Sterne, Tests (Flugtest/Korrektur/Nachtest: andere Pools, eigene Auswahl), Übung im Flug (ruft die Auswahl nicht), `wdh_aufgabe_da` (unverändert; „keine Aufgabe“ genau so oft wie vorher, weil die Kandidatenmenge gleich bleibt – geprüft mit Schalter aus/an), Tagesrunde (Anzahl/Deckel über `wdh_aufgabe_da` und `wdh_runde_groesse` – geprüft gleich), App (keine Kennzeichnung, keine neuen Felder).

**Ladezeit:** Mit Schalter aus kostet jede Kandidaten-Aufgabe einen Regel-Zugriff. Mit Schalter an je bearbeiteter Kandidaten-Aufgabe zwei kleine Abfragen (Lerntage, Versuche dieser Aufgabe). Alle Zugriffe gehen über (Kind, Aufgabe) und nutzen den TEMPO-S1-Index `versuch_kind_aufgabe_idx`, wenn er da ist. Die Probe misst beides (`ms_auswahl_aus` / `ms_auswahl_an`, ein Aufruf je sitzender Karte) und meldet, ob der Index da ist.

## 4. Einstellwerte (`schule.regel`)

| Schlüssel | Standard | Bedeutung |
|---|---|---|
| `fehlerkarten_an` | `0` | 0 aus, 1 an, 2 nur Testkinder (`ist_test`) – zum Nachkontrollieren am Testkind |
| `fehlerkarten_pause_lerntage` | `2` | Lerntage Pause zwischen Fehler und Wiederkehr (0–30; die Sperre `wdh_sperre_lerntage` gilt zusätzlich) |
| `fehlerkarten_max` | `3` | höchstens so oft hintereinander bevorzugt (0–20; 0 = nie) |

Ungültige Werte bricht das Paket ab; ein später von Hand falsch gesetzter Wert gilt als Standard (bricht nie die Wiederholung). Ein zweiter Lauf setzt nichts zurück.
Einschalten: `update schule.regel set wert = '2'::jsonb where schluessel = 'fehlerkarten_an';` (Testkind), danach `'1'` (alle). Ausschalten: `'0'` – sofort wie vorher.

## 5. Ausführung

Pakete (erzeugt von `tools/tests/fb_einspielen.py`, Migration = Einspiel-Datei):
`tools/tests/aus/fb_s_probe.sql` (rollt alles zurück, Meldung beginnt mit „FB-S PROBELAUF bestanden – Kinder …, Etappen …, Vergleiche …, Abweichungen AUS 0 | AN heute: …“), `tools/tests/aus/fb_s_einspielen.sql`.
Aufruf wie gewohnt: Dateiinhalt in EINEM `execute` (oder direkt), eine Transaktion; erste Anweisung setzt `lock_timeout` 3 s und `statement_timeout` 300 s; keine Untertransaktion, keine xmin-Zählung.

**Lernpause: nein.** Keine Tabellen-DDL, kein Index, keine Datenänderung außer drei neuen Regel-Zeilen; Funktionen werden ersetzt (laufende Aufrufe sehen bis zum Commit die alte Fassung). Der Vergleich alt/neu läuft in einer Anweisung (ein Schnappschuss), Antworten der Kinder währenddessen stören ihn nicht. Der Schalter steht beim Einspielen auf 0, das Einspielen allein ändert also nichts.

Reihenfolge:
1. Projektleiter bestätigt lesend die md5/Längen (Abschnitt 7).
2. Probelauf → Bericht an Gegenprüfung/Nutzer. 3. Satz des Nutzers → Einspielen. 4. Schalter 2 (Testkind), Nachkontrolle. 5. Satz des Nutzers → Schalter 1.

**Mit den anderen offenen Paketen: beliebige Reihenfolge.**
- TEMPO-S1 ändert nur `etappen_stand` und legt `aufgabe_einheit_pool_lz_idx` und `versuch_kind_aufgabe_idx` an; FB-S berührt keines davon, TEMPO-S1 keine FB-S-Funktion. Empfehlung: Schalter **an** erst, wenn TEMPO-S1 (Index) eingespielt ist oder die Probe `ms_auswahl_an` unbedenklich zeigt.
- ADVENT-S (Zweig `helfer-advent-server`, `20261209_advent_s.sql`) legt nur neue Tabellen/Funktionen und Regeln `advent_*` an und erweitert `sterne_grund_check`; keine Überschneidung (andere Regel-Schlüssel, keine gemeinsame Funktion).

## 6. Nachkontrolle am Testkind (lernender 3, echte App)

Der Test läuft nur im Nachbau (`tools/tests/fb_nachbau.py`): `wiederholung_intern`, `uebung_pruefen_*`, Trigger, Sterne und die App sind dort nicht nachgebaut. Deshalb nach Schalter 2:
1. Am Testkind in einer gelandeten Etappe eine Übungsaufgabe absichtlich falsch beantworten (Aufgaben-ID notieren), eine zweite mit Tipp lösen.
2. Lesend: `select schule.fehlerkarte_serie(3, <id>);` → 1.
3. An zwei weiteren Lerntagen etwas üben (andere Etappe), am dritten Lerntag die Wiederholung öffnen (bzw. die Etappe fällig): erste Aufgabe dieser Etappe = die notierte (`select schule.wdh_aufgabe_waehlen(3, <einheit>, '<lernziel>', false);` liefert sie jedes Mal). In der App kein Hinweis, Ablauf wie immer.
4. Selbst richtig lösen → Serie 0, kommt nicht mehr bevorzugt. Wiederholung gilt als bestanden wie sonst (Sterne, Stufe).
5. Mischkarte: Flug laden, Mischkarte aus der Etappe mit Fehler-Bordkarte (Stufe 2/3) erscheint; Flug neu laden – dieselbe Karte; beantworten → Antwort hat `misch.gueltig = true`.
6. Kind 1/2 unverändert (Schalter 2).

## 7. Vor dem Einspielen lesend an der echten Datenbank bestätigen

`select p.oid::regprocedure, md5(p.prosrc), length(p.prosrc) from pg_proc p where p.oid in (…)` – erwartet:

| Funktion | md5(prosrc) | Länge |
|---|---|---|
| `schule.wdh_aufgabe_waehlen(bigint, bigint, text, boolean)` (wird ersetzt) | `7a6d76c619d1edfb6cdd8ee4a4a5cb1f` | 537 |
| `schule.mischkarten(bigint, bigint, integer)` (wird ersetzt) | `1d8a3466c1698cfe9d4d0dd00d5ca638` | 5123 |
| `schule.wdh_sperre_ab(bigint)` (Bezug) | `e3b104414d506c83dcd3f84b6d3f2283` | 334 |
| `schule.lern_datum(bigint, timestamp with time zone)` (Bezug) | `b9261f7da175fb15ed4f3fea69009d93` | 127 |
| `schule.heute_tag(bigint)` (Bezug) | `830213a58d5fcfc463779b5b13ba9285` | 126 |
| `schule.wdh_aufgabe_da(bigint, bigint, text)` (Bezug) | `0ee8e92220272826c52ceb3aa68a4cc0` | 521 |
| `schule.misch_gueltig(bigint, schule.aufgabe, jsonb)` (Bezug) | `437509567899b8e75a48ee46c250a537` | 1729 |

Außerdem: es gibt noch keine Funktion `schule.fehlerkarte_*` und keine Regel `fehlerkarten_*`; Eigenschaften der beiden ersetzten Funktionen = Soll in `fb_einspielen.py` (`SOLL`: VOLATILE, Invoker, nicht STRICT, keine Menge, PARALLEL UNSAFE, Kosten 100, nicht leakproof, `search_path=""`); kein anderer Aufrufer von `wdh_aufgabe_waehlen` als `wiederholung_intern` und `mischkarten_waehlen` (`select … from pg_proc where prosrc like '%wdh_aufgabe_waehlen%'`).
Weicht etwas ab: nicht einspielen, Live-Text als Datei nach `/home/claude/arbeit/live/` legen.

## 8. Messung nach zwei Wochen

Kennzahl: **Quote „beim Wiederkommen selbst gelöst“** – unter allen Bearbeitungen von Aufgaben, deren vorherige Bearbeitung nicht selbst gelöst war, der Anteil mit eigener Lösung; getrennt nach „vor dem Einschalten“ (gleich lange Zeit davor, Wiederkehr zufällig) und „danach“. Dazu Zahl dieser Wiederkehren je Kind (wie viele Fehler kommen überhaupt zurück) und mittlere Lerntage bis zur Wiederkehr.

```sql
with b as (select v.lernender_id l, v.aufgabe_id a, v.am, coalesce(v.richtig, false) and coalesce(v.hilfe, 0) = 0 selbst,
                  lag(coalesce(v.richtig, false) and coalesce(v.hilfe, 0) = 0) over (partition by v.lernender_id, v.aufgabe_id order by v.am, v.id) vorher_selbst
             from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
            where a.pool = 'uebung' and v.testsitzung_id is null and coalesce(v.anlauf, 1) <> 2)
select l, v.am >= :eingeschaltet_am danach, count(*) wiederkehren, round(avg(selbst::int), 2) quote_selbst
  from b v where vorher_selbst = false and v.am >= :eingeschaltet_am - (now() - :eingeschaltet_am) group by 1, 2 order by 1, 2;
```
Erfolg: Quote „danach“ deutlich über „davor“ und mehr Wiederkehren je Kind. Nur Zahlen weitergeben.
