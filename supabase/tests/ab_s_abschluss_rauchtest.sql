-- Rauchtest AB-S (Abschluss nach Etappe, Flug und Ort – Serverteil). Nach 20261120_ab_s_abschluss.sql ausführen. Rollback, nur Testkind, keine Namen.
-- Prüfung 9 (Nachträge aus ChatGPT 885/888) setzt zusätzlich 20261120_ab_s_flug_abschluss_einmal.sql (Feld flug_geschafft) und 20261121_ab_s_flug_geschafft_robust.sql (schule.flug_fertig_nach) voraus.
-- Läuft über die inneren Funktionen schule.uebung_pruefen_intern / test_starten_intern / test_abschliessen_intern / einheit_lesen_intern / konto
-- (die api-Funktionen rufen genau diese nach der Zugriffsprüfung auf – ein Schlüssel gehört nicht in eine Datei).
-- Aus der Datenbank kommen nur Inhalte; Karten-Stände, Versuche, Plan und Texte legt der Test selbst an.
-- Etappen: nur Auswahl-Bordkarten (Antwort = loesung, falsch = anderer Index), mindestens 3, landbar (Stufe-3-Bedingung erfüllbar), vom Testkind noch nie geübt.
begin;
create or replace function pg_temp.ab_reihe(p_e bigint, p_lz text) returns bigint[] language sql as $f$
  -- Reihenfolge, in der die Etappe mit genau „ziel“ eigenen Lösungen landet: zuerst eine schwere, dann je Typ eine, dann der Rest
  select array_agg(id order by (stufe = 3 and (typ is null or typ in ('rueckwaerts', 'verknuepfen', 'begruenden', 'fehler', 'transfer', 'parameter', 'pruefung'))) desc,
                               (typ is not null and rn = 1) desc, reihenfolge, id)
    from (select a.*, row_number() over (partition by a.typ order by a.reihenfolge, a.id) rn from schule.aufgabe a
           where a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'uebung' and a.freigegeben) q;
$f$;
create or replace function pg_temp.ab_antwort(p_l bigint, p_aid bigint, p_richtig boolean, p_hilfe int, p_anlauf int, p_cid text) returns jsonb language plpgsql as $f$
declare a schule.aufgabe; d jsonb;
begin
  select * into a from schule.aufgabe where id = p_aid;
  d := jsonb_build_object('aufgabe_id', p_aid, 'client_id', p_cid, 'hilfe', p_hilfe,
         'antwort', case when p_richtig then a.loesung else jsonb_build_object('index', ((a.loesung->>'index')::int + 1) % jsonb_array_length(a.antworten)) end);
  if p_anlauf is not null then d := d || jsonb_build_object('anlauf', p_anlauf); end if;
  return schule.uebung_pruefen_intern(p_l, d);
end $f$;
create or replace function pg_temp.ab_landen(p_l bigint, p_ids bigint[], p_cid text) returns jsonb language plpgsql as $f$
-- richtig antworten (reihum), bis die Etappe landet; jede Antwort vor der Landung darf kein Feld „landung“ haben
declare r jsonb; i int := 0;
begin
  loop
    i := i + 1;
    if i > 30 then raise exception 'FEHLER: Etappe landet nicht nach 30 Antworten'; end if;
    r := pg_temp.ab_antwort(p_l, p_ids[1 + (i - 1) % cardinality(p_ids)], true, 0, 1, p_cid || i);
    if not (r->>'richtig')::boolean then raise exception 'FEHLER: richtige Antwort als falsch gewertet: %', r; end if;
    exit when coalesce((r->'karte'->>'sitzt')::boolean, false);
    if r ? 'landung' then raise exception 'FEHLER: „landung“ ohne Landung: %', r; end if;
  end loop;
  return r;
end $f$;

-- Prüfung 9: eine laufende Testsitzung mit einer Bordkarte je Pflicht-Etappe (p_status: nur Etappen mit diesem Stand, null = alle), Antworten richtig/falsch.
-- Bordkarte: bevorzugt aus dem passenden Pool, sonst irgendeine der Etappe (test_abschliessen_intern wertet je Etappe über variante_gruppe).
create or replace function pg_temp.ab9_sitzung(p_l bigint, p_e bigint, p_art text, p_richtig boolean, p_status text, p_cid text) returns bigint language plpgsql as $f$
declare v_ids bigint[]; v_sid bigint; e schule.einheit;
begin
  select * into e from schule.einheit where id = p_e;
  select array_agg(q.id order by q.lz) into v_ids from (
    select s.lernziel lz, (select a.id from schule.aufgabe a where a.einheit_id = p_e and a.variante_gruppe = s.lernziel
                            order by (a.pool = case p_art when 'korrektur' then 'korrektur' when 'nachtest' then 'sicherung' else 'test' end) desc, a.pool = 'test' desc, a.id limit 1) id
      from schule.lernziel_stand s where s.lernender_id = p_l and s.einheit_id = p_e and s.pflicht and (p_status is null or s.status = p_status)) q;
  if coalesce(cardinality(v_ids), 0) = 0 or array_position(v_ids, null) is not null then raise exception 'FEHLER 9 Vorbereitung (%): keine Bordkarten', p_cid; end if;
  insert into schule.testsitzung(lernender_id, art, block_id, thema_id, einheit_id, nachtest_runde, aufgaben, status, punkte_max, gestartet_am)
  values (p_l, p_art, e.block_id, e.thema_id, p_e, case when p_art = 'nachtest' then 1 end, v_ids, 'laeuft', cardinality(v_ids), now()) returning id into v_sid;
  insert into schule.versuch(lernender_id, aufgabe_id, testsitzung_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr)
  select p_l, x, v_sid, 'ab-s-' || p_cid || '-' || x, null, p_richtig, case when p_richtig then 1 else 0 end, 1, 0, 1 from unnest(v_ids) x;
  return v_sid;
end $f$;

do $$
declare v_l bigint; v_et record; v_e bigint[] := '{}'; v_lz text[] := '{}'; v_o bigint[]; r jsonb; j jsonb; k0 jsonb; k1 jsonb; v_ziel int; v_n int;
  v_f bigint; v_ft bigint; v_b bigint; v_b2 bigint; v_t2 bigint; v_sid bigint; t jsonb; v_kurz text := 'Rauchtest: worum es in diesem Flug geht.';
  v_f9 bigint; v_t9 bigint; v_b9 bigint; v_s9 bigint; v_lz9 text; v_feld text; v_s9a bigint; v_s9c bigint;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  for v_et in
    select q.einheit_id, q.variante_gruppe from (
      select a.einheit_id, a.variante_gruppe, count(*) n,
             bool_and(a.antworttyp = 'auswahl' and jsonb_array_length(coalesce(a.antworten, '[]'::jsonb)) >= 2 and a.loesung ? 'index') alle_auswahl,
             bool_or(a.stufe = 3) s3,
             bool_or(a.stufe = 3 and (a.typ is null or a.typ in ('rueckwaerts', 'verknuepfen', 'begruenden', 'fehler', 'transfer', 'parameter', 'pruefung'))) s3ok
        from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
       where a.pool = 'uebung' and a.freigegeben and e.status = 'freigegeben' group by 1, 2) q
     where q.alle_auswahl and q.n >= 3 and (not q.s3 or q.s3ok)
       and not exists (select 1 from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id where v.lernender_id = v_l and a.einheit_id = q.einheit_id and a.variante_gruppe = q.variante_gruppe)
     order by 1, 2 limit 3 loop
    v_e := v_e || v_et.einheit_id; v_lz := v_lz || v_et.variante_gruppe;
  end loop;
  if cardinality(v_e) < 3 then raise exception 'FEHLER: nur % passende Etappen', cardinality(v_e); end if;
  -- Ausgangslage dieser drei Etappen: frisch
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) select v_l, v_e[i], v_lz[i] from generate_series(1, 3) i on conflict do nothing;
  update schule.karte_stand set sitzt = false, sitzt_am = null, eigene_loesungen = 0, gezaehlt = '{}', typen = '{}', folge = 0, fehler_folge = 0, stufe_senkung = 0,
         schwer_ok = false, geoeffnet_am = null, wdh_stufe = 0, wdh_fehler = 0, landung_art = null, landung = null, gesetzt_am = null
   where lernender_id = v_l and ((einheit_id = v_e[1] and lernziel = v_lz[1]) or (einheit_id = v_e[2] and lernziel = v_lz[2]) or (einheit_id = v_e[3] and lernziel = v_lz[3]));
  k0 := schule.konto(v_l)->'abzeichen';
  if k0 is null then raise exception 'FEHLER: konto ohne abzeichen'; end if;

  -- 1. Direktflug: genau „ziel“ Bordkarten, alle im ersten Versuch richtig, ohne Tipp
  v_o := pg_temp.ab_reihe(v_e[1], v_lz[1]);
  r := pg_temp.ab_landen(v_l, v_o, 'ab-s-1-');
  v_ziel := schule.karte_ziel(v_e[1], v_lz[1]);
  if r->'landung'->>'landung_art' <> 'direkt' or (r->'landung'->>'bordkarten')::int <> v_ziel or (r->'landung'->>'ziel')::int <> v_ziel
     or (r->'landung'->>'fehler_endgueltig')::int <> 0 or (r->'landung'->>'wieder_gelandet')::boolean then raise exception 'FEHLER 1: %', r->'landung'; end if;
  if (select landung_art from schule.karte_stand where lernender_id = v_l and einheit_id = v_e[1] and lernziel = v_lz[1]) is distinct from 'direkt' then raise exception 'FEHLER 1b: nicht gespeichert'; end if;
  raise notice 'ok 1: Direktflug (% von % Bordkarten), gespeichert, „landung“ nur in der Lande-Antwort', r->'landung'->>'bordkarten', v_ziel;

  -- 2. Saubere Landung: 1 endgültiger Fehler, 1 Antwort mit Tipp, 1 zweiter Versuch (der erste Anlauf davor zählt nicht als Fehler)
  v_o := pg_temp.ab_reihe(v_e[2], v_lz[2]);
  r := pg_temp.ab_antwort(v_l, v_o[cardinality(v_o)], false, 0, null, 'ab-s-2a');          -- ohne zweite Chance: endgültig falsch
  r := pg_temp.ab_antwort(v_l, v_o[cardinality(v_o)], true, 1, 1, 'ab-s-2b');              -- mit Tipp richtig
  r := pg_temp.ab_antwort(v_l, v_o[cardinality(v_o) - 1], false, 0, 1, 'ab-s-2c');         -- 1. Anlauf falsch …
  if not coalesce((r->>'nochmal')::boolean, false) then raise exception 'FEHLER 2: kein zweiter Anlauf angeboten: %', r; end if;
  r := pg_temp.ab_antwort(v_l, v_o[cardinality(v_o) - 1], true, 0, 2, 'ab-s-2d');          -- … 2. Anlauf richtig
  r := pg_temp.ab_landen(v_l, v_o, 'ab-s-2-');
  if r->'landung'->>'landung_art' <> 'sauber' or (r->'landung'->>'fehler_endgueltig')::int <> 1 or (r->'landung'->>'mit_tipp')::int <> 1
     or (r->'landung'->>'zweite_versuche')::int <> 1 or (r->'landung'->>'stufe_gesenkt')::int <> 0 then raise exception 'FEHLER 2: %', r->'landung'; end if;
  raise notice 'ok 2: Saubere Landung (% Bordkarten, 1 Fehler, 1 Tipp, 1 zweiter Versuch)', r->'landung'->>'bordkarten';

  -- 3. Sturmflug: 3 endgültige Fehler (der zweite senkt die Stufe)
  v_o := pg_temp.ab_reihe(v_e[3], v_lz[3]);
  for v_n in 1..3 loop r := pg_temp.ab_antwort(v_l, v_o[1], false, 0, null, 'ab-s-3f' || v_n); end loop;
  r := pg_temp.ab_landen(v_l, v_o, 'ab-s-3-');
  if r->'landung'->>'landung_art' <> 'sturm' or (r->'landung'->>'fehler_endgueltig')::int <> 3 or (r->'landung'->>'stufe_gesenkt')::int <> 1 then raise exception 'FEHLER 3: %', r->'landung'; end if;
  k1 := schule.konto(v_l)->'abzeichen';
  if (k1->>'direkt')::int - (k0->>'direkt')::int <> 1 or (k1->>'sauber')::int - (k0->>'sauber')::int <> 1 or (k1->>'sturm')::int - (k0->>'sturm')::int <> 1 then
    raise exception 'FEHLER 3b: Reisepass % → %', k0, k1; end if;
  raise notice 'ok 3: Sturmflug (3 Fehler, Stufe 1× gesenkt); Reisepass zählt je +1: %', k1;

  -- 4. Wieder gelandet: Etappe 1 durch zwei Fehler in der Wiederholung wieder offen, danach neu gelandet → sauber (Szene 1b), überschrieben
  v_o := pg_temp.ab_reihe(v_e[1], v_lz[1]);
  r := pg_temp.ab_antwort(v_l, v_o[1], false, 0, null, 'ab-s-4f1');
  r := pg_temp.ab_antwort(v_l, v_o[1], false, 0, null, 'ab-s-4f2');
  if (select sitzt or geoeffnet_am is null from schule.karte_stand where lernender_id = v_l and einheit_id = v_e[1] and lernziel = v_lz[1]) then raise exception 'FEHLER 4: nicht wieder offen'; end if;
  -- in einer Transaktion ist now() fest: die Zeit vor dem Öffnen nach hinten schieben, damit „seit dem letzten wieder offen“ trennbar ist
  update schule.versuch v set am = v.am - interval '10 minutes' from schule.aufgabe a
   where a.id = v.aufgabe_id and v.lernender_id = v_l and a.einheit_id = v_e[1] and a.variante_gruppe = v_lz[1];
  update schule.karte_stand set geoeffnet_am = now() - interval '1 minute' where lernender_id = v_l and einheit_id = v_e[1] and lernziel = v_lz[1];
  r := pg_temp.ab_landen(v_l, v_o, 'ab-s-4-');
  if r->'landung'->>'landung_art' <> 'sauber' or not (r->'landung'->>'wieder_gelandet')::boolean
     or (r->'landung'->>'bordkarten')::int <> least(3, schule.karte_ziel(v_e[1], v_lz[1])) or (r->'landung'->>'fehler_endgueltig')::int <> 0 then raise exception 'FEHLER 4: %', r->'landung'; end if;
  k1 := schule.konto(v_l)->'abzeichen';
  if (k1->>'direkt')::int - (k0->>'direkt')::int <> 0 or (k1->>'sauber')::int - (k0->>'sauber')::int <> 2 or (k1->>'sturm')::int - (k0->>'sturm')::int <> 1 then
    raise exception 'FEHLER 4b: Reisepass % → %', k0, k1; end if;
  raise notice 'ok 4: wieder gelandet → sauber, nur Bordkarten seit dem Öffnen gezählt (%); Reisepass: direkt überschrieben', r->'landung'->>'bordkarten';

  -- 5. Texte: kurz und kann im Flug, in der Lande-Antwort; fehlt ein Text → null
  update schule.thema set kurz = v_kurz where id = (select thema_id from schule.einheit where id = v_e[1]);
  insert into schule.etappe_text(thema_id, lernziel, kann) values ((select thema_id from schule.einheit where id = v_e[1]), v_lz[1], 'eine Rauchtest-Etappe lösen')
  on conflict (thema_id, lernziel) do update set kann = excluded.kann;
  j := schule.einheit_lesen_intern(v_l, v_e[1]);
  if j->>'kurz' <> v_kurz or j->'kann'->>v_lz[1] <> 'eine Rauchtest-Etappe lösen' or j->'landungen'->>v_lz[1] <> 'sauber' then
    raise exception 'FEHLER 5: kurz %, kann %, landungen %', j->'kurz', j->'kann', j->'landungen'; end if;
  if exists (select 1 from jsonb_each(j->'kann') x where x.key <> v_lz[1] and x.value <> 'null'::jsonb
               and not exists (select 1 from schule.etappe_text t where t.thema_id = (select thema_id from schule.einheit where id = v_e[1]) and t.lernziel = x.key)) then
    raise exception 'FEHLER 5b: kann ohne Text nicht null: %', j->'kann'; end if;
  raise notice 'ok 5: einheit_lesen liefert kurz, kann (fehlend = null) und landungen';

  -- 6. Flug-Test: sterne_flug, Ort geschafft, Ort-Sterne, nächster Flug in einem anderen Ort (Plan des Testkinds im Test angelegt)
  select e.id, e.thema_id, e.block_id into v_f, v_ft, v_b from schule.einheit e
   where e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id) and e.block_id is not null
     and exists (select 1 from schule.block_thema bt where bt.block_id = e.block_id and bt.thema_id = e.thema_id)
     and exists (select 1 from schule.aufgabe a where a.einheit_id = e.id and a.pool = 'test')
     and not exists (select 1 from jsonb_array_elements_text(e.inhalt->'bewertung'->'lernziele_pflicht') p
                      where not exists (select 1 from schule.aufgabe a where a.einheit_id = e.id and a.pool = 'test' and a.variante_gruppe = p))
     and not exists (select 1 from schule.testsitzung x where x.lernender_id = v_l and x.einheit_id = e.id)
     and not exists (select 1 from schule.lernziel_stand s where s.lernender_id = v_l and s.einheit_id = e.id)
     and not exists (select 1 from schule.sterne s where s.lernender_id = v_l and s.grund = 'ort' and s.bezug = 'block:' || e.block_id)
   order by e.id limit 1;
  select bt.block_id, bt.thema_id into v_b2, v_t2 from schule.block_thema bt
   where bt.block_id <> v_b and schule.thema_einheit(bt.thema_id) is not null and schule.thema_stand(v_l, bt.thema_id) <> 'erledigt' and bt.thema_id <> v_ft
   order by bt.block_id, bt.reihenfolge, bt.thema_id limit 1;
  if v_f is null or v_b2 is null then raise exception 'FEHLER 6: kein passender Flug/Ort'; end if;
  update schule.route set status = 'entfernt', position = position + 1000000 where lernender_id = v_l and art = 'normal' and status <> 'entfernt';
  insert into schule.route(lernender_id, block_id, position, art, status, ausgelassen, revision, geaendert_von)
  values (v_l, v_b, 1, 'normal', 'offen', array(select bt.thema_id from schule.block_thema bt where bt.block_id = v_b and bt.thema_id <> v_ft), 1, 'rauchtest'),
         (v_l, v_b2, 2, 'normal', 'offen', '{}', 1, 'rauchtest');
  perform schule.lernziele_anlegen(v_l, v_f);
  r := schule.test_starten_intern(v_l, jsonb_build_object('einheit_id', v_f, 'art', 'blocktest'));
  if not coalesce((r->>'ok')::boolean, false) then raise exception 'FEHLER 6: Flug-Test startet nicht: %', r; end if;
  v_sid := (r->>'sitzung_id')::bigint;
  insert into schule.versuch(lernender_id, aufgabe_id, testsitzung_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr)
  select v_l, x, v_sid, 'ab-s-6-' || x, null, true, 1, 1, 0, 1 from unnest((select aufgaben from schule.testsitzung where id = v_sid)) x;
  t := schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_sid));
  if not (t->>'einheit_abgeschlossen')::boolean then raise exception 'FEHLER 6a: Flug nicht abgeschlossen: %', t->'lernziele'; end if;
  if (t->'sterne_flug'->>'test')::int <> (t->>'richtig')::int * schule.sterne_regel('sterne_test_richtig')
     or (t->'sterne_flug'->>'summe')::int < (t->'sterne_flug'->>'test')::int then raise exception 'FEHLER 6b: sterne_flug %', t->'sterne_flug'; end if;
  if not (t->>'ort_geschafft')::boolean or (t->>'ort_sterne')::int <> schule.sterne_regel('sterne_ort_geschafft')
     or jsonb_array_length(t->'ort_fluege') <> 1 then raise exception 'FEHLER 6c: Ort % / % / %', t->'ort_geschafft', t->'ort_sterne', t->'ort_fluege'; end if;
  if (t->'naechster_flug'->>'block_id')::bigint <> v_b2 or not (t->>'ort_wechsel')::boolean or t->'naechster_flug'->'erste_etappe'->>'lernziel' is null
     or (t->'naechster_flug'->'flug'->>'nr')::int < 1 then raise exception 'FEHLER 6d: nächster Flug %', t->'naechster_flug'; end if;
  if (t->'flug'->'flug'->>'nr')::int <> 1 or (t->'flug'->'flug'->>'von')::int <> 1
     or jsonb_array_length(t->'etappen') <> jsonb_array_length(coalesce((select inhalt->'etappen' from schule.einheit where id = v_f), '[]'::jsonb))
     or not (t ? 'kurz') then raise exception 'FEHLER 6e: flug %, etappen %', t->'flug', t->'etappen'; end if;
  if not coalesce((t->>'flug_geschafft')::boolean, false) then raise exception 'FEHLER 6f: flug_geschafft fehlt beim ersten Flug-Abschluss: %', t->'flug_geschafft'; end if; -- Nachtrag 885
  raise notice 'ok 6: Flug-Test – sterne_flug %, Ort geschafft (+%), nächster Flug in anderem Ort (Flug % von %)',
    t->'sterne_flug', t->>'ort_sterne', t->'naechster_flug'->'flug'->>'nr', t->'naechster_flug'->'flug'->>'von';

  -- 7. Test-Ergebnis erneut lesen: Ort bleibt „durch diesen Test geschafft“, alte Felder unverändert vorhanden
  t := schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_sid));
  if not (t->>'ort_geschafft')::boolean or not coalesce((t->>'flug_geschafft')::boolean, false) or not (t ? 'naechster_flug')
     or not (t ? 'ergebnisse' and t ? 'lernziele' and t ? 'einheit_abgeschlossen' and t ? 'ort' and t ? 'nachtest') then
    raise exception 'FEHLER 7: %', t - 'ergebnisse'; end if;
  raise notice 'ok 7: erneut gelesen – ort_geschafft bleibt, bisherige Felder vorhanden (alte App bricht nicht)';

  -- 8. kein weiterer Flug im Plan → naechster_flug null
  update schule.route set status = 'entfernt', position = position + 1000000 where lernender_id = v_l and block_id = v_b2 and art = 'normal';
  if schule.naechster_flug(v_l, v_ft) is not null then raise exception 'FEHLER 8: nächster Flug ohne Plan: %', schule.naechster_flug(v_l, v_ft); end if;
  raise notice 'ok 8: ohne weiteren Flug im Plan → naechster_flug null';

  -- 9. Abschluss-Felder nur, wenn der Flug durch diese Sitzung zum ersten Mal fertig wird (Flug-Test ODER Verbessern) – Nachträge 885, 20.11. nachmittags (A), 888.
  --    Feste Testvorbereitung, kein Überspringen: die Sitzungen legt der Test selbst an (eine Test-Bordkarte je Pflicht-Etappe, Antworten richtig/falsch),
  --    abgeschlossen wird über schule.test_abschliessen_intern. Flug in einem Ort mit weiteren offenen Flügen im Plan (Ort wird nicht geschafft).
  select e.id, e.thema_id, e.block_id into v_f9, v_t9, v_b9 from schule.einheit e
   where e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id) and e.block_id is not null and e.id <> v_f and e.block_id not in (v_b, v_b2)
     and exists (select 1 from schule.block_thema bt where bt.block_id = e.block_id and bt.thema_id = e.thema_id)
     and jsonb_array_length(coalesce(e.inhalt->'bewertung'->'lernziele_pflicht', '[]'::jsonb)) >= 2
     and not exists (select 1 from jsonb_array_elements_text(e.inhalt->'bewertung'->'lernziele_pflicht') p
                      where (select count(*) from schule.aufgabe a where a.einheit_id = e.id and a.variante_gruppe = p) < 1)
     and not exists (select 1 from schule.testsitzung x where x.lernender_id = v_l and x.einheit_id = e.id)
     and not exists (select 1 from schule.lernziel_stand s where s.lernender_id = v_l and s.einheit_id = e.id)
     and exists (select 1 from schule.block_thema bt where bt.block_id = e.block_id and bt.thema_id <> e.thema_id
                  and schule.thema_einheit(bt.thema_id) is not null and schule.thema_stand(v_l, bt.thema_id) <> 'erledigt')
   order by e.id limit 1;
  if v_f9 is null then raise exception 'FEHLER 9: kein passender Flug'; end if;
  insert into schule.route(lernender_id, block_id, position, art, status, ausgelassen, revision, geaendert_von)
  values (v_l, v_b9, 3, 'normal', 'offen', '{}', 1, 'rauchtest');
  perform schule.lernziele_anlegen(v_l, v_f9);
  if (select count(*) from schule.lernziel_stand where lernender_id = v_l and einheit_id = v_f9 and pflicht) < 2 then raise exception 'FEHLER 9: weniger als 2 Pflicht-Etappen'; end if;

  -- 9a nicht bestandener Flug-Test (alles falsch)
  v_s9a := pg_temp.ab9_sitzung(v_l, v_f9, 'blocktest', false, null, '9a');
  t := schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_s9a));
  foreach v_feld in array array['flug', 'naechster_flug', 'sterne_flug', 'etappen', 'ort_wechsel'] loop
    if t ? v_feld then raise exception 'FEHLER 9a: nicht bestanden, trotzdem %: %', v_feld, t->v_feld; end if; end loop;
  if (t->>'einheit_abgeschlossen')::boolean or coalesce((t->>'flug_geschafft')::boolean, true) then raise exception 'FEHLER 9a: %', t - 'ergebnisse'; end if;
  -- 9b erneuter Aufruf derselben Sitzung
  t := schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_s9a));
  if t ? 'naechster_flug' or t ? 'sterne_flug' or t ? 'flug' or coalesce((t->>'flug_geschafft')::boolean, true) then raise exception 'FEHLER 9b: erneuter Aufruf liefert Abschluss-Felder'; end if;
  raise notice 'ok 9a/b: nicht bestandener Flug-Test und erneuter Aufruf – flug_geschafft false, keine Abschluss-Felder';

  -- 9r Regression (888, Muss 1): die nicht bestandene Sitzung wird zur „alten“ Sitzung ohne Wert (wie vor dem Einspielen); der Flug ist noch offen
  update schule.testsitzung set flug_geschafft = null where id = v_s9a;
  if schule.flug_fertig_nach(v_l, v_f9, v_s9a) then raise exception 'FEHLER 9r: Flug nach nicht bestandenem Test als fertig erkannt'; end if;

  -- 9c Verbessern (korrektur), alles richtig → der Flug wird zum ersten Mal fertig → flug_geschafft true mit Abschluss-Feldern (trotz alter Sitzung mit NULL)
  v_s9c := pg_temp.ab9_sitzung(v_l, v_f9, 'korrektur', true, 'fehler', '9c');
  t := schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_s9c));
  if not (t->>'einheit_abgeschlossen')::boolean then raise exception 'FEHLER 9c: Flug nach Verbessern nicht fertig: %', t->'lernziele'; end if;
  if not coalesce((t->>'flug_geschafft')::boolean, false) or not (t ? 'flug' and t ? 'naechster_flug' and t ? 'sterne_flug' and t ? 'etappen') then
    raise exception 'FEHLER 9c: alte Sitzung NULL + Flug offen → Verbessern macht ihn erstmals fertig, aber flug_geschafft %', t->'flug_geschafft'; end if;
  t := schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_s9c));
  if not coalesce((t->>'flug_geschafft')::boolean, false) or not (t ? 'naechster_flug') then raise exception 'FEHLER 9c: erneuter Aufruf anders als beim ersten Mal'; end if;
  raise notice 'ok 9r/9c: alte Sitzung (NULL, nicht bestanden) + Flug offen → Verbessern → flug_geschafft true mit Feldern; erneuter Aufruf gleich';

  -- 9c-2 zweites Verbessern; die erste Verbessern-Sitzung wird zur alten Sitzung ohne Wert, die den Flug fertig gemacht hatte → sperrt (false, keine Felder)
  update schule.testsitzung set flug_geschafft = null where id = v_s9c;
  if not schule.flug_fertig_nach(v_l, v_f9, v_s9c) then raise exception 'FEHLER 9c-2: Flug nach dem Verbessern nicht als fertig erkannt'; end if;
  select s.lernziel into v_lz9 from schule.lernziel_stand s where s.lernender_id = v_l and s.einheit_id = v_f9 and s.pflicht order by s.lernziel limit 1;
  update schule.lernziel_stand set status = 'fehler' where lernender_id = v_l and einheit_id = v_f9 and lernziel = v_lz9;
  v_s9 := pg_temp.ab9_sitzung(v_l, v_f9, 'korrektur', true, 'fehler', '9c2');
  t := schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_s9));
  if not (t->>'einheit_abgeschlossen')::boolean then raise exception 'FEHLER 9c-2 Vorbereitung: Flug nicht wieder fertig'; end if;
  if t ? 'naechster_flug' or t ? 'sterne_flug' or t ? 'flug' or coalesce((t->>'flug_geschafft')::boolean, true) then raise exception 'FEHLER 9c-2: zweites Verbessern liefert Abschluss-Felder'; end if;
  raise notice 'ok 9c-2: zweites Verbessern (früherer Abschluss als alte NULL-Sitzung) – flug_geschafft false, keine Abschluss-Felder';

  -- 9d Nachtragstest: eine Pflicht-Etappe wieder „offen“ (wie nach einer neuen Etappe), späterer Flug-Test für diese Etappe alles richtig
  update schule.lernziel_stand set status = 'offen' where lernender_id = v_l and einheit_id = v_f9 and lernziel = v_lz9;
  v_s9 := pg_temp.ab9_sitzung(v_l, v_f9, 'blocktest', true, 'offen', '9d');
  t := schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_s9));
  if not (t->>'einheit_abgeschlossen')::boolean then raise exception 'FEHLER 9d Vorbereitung: Flug nach Nachtragstest nicht fertig'; end if;
  if t ? 'naechster_flug' or t ? 'sterne_flug' or t ? 'flug' or coalesce((t->>'flug_geschafft')::boolean, true) then raise exception 'FEHLER 9d: Nachtragstest liefert Abschluss-Felder'; end if;
  raise notice 'ok 9d: Nachtragstest – flug_geschafft false, keine Abschluss-Felder';

  -- 9e Nachtest (eigener Negativfall): alles richtig → false, keine Abschluss-Felder
  v_s9 := pg_temp.ab9_sitzung(v_l, v_f9, 'nachtest', true, null, '9e');
  t := schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_s9));
  if t ? 'naechster_flug' or t ? 'sterne_flug' or t ? 'flug' or coalesce((t->>'flug_geschafft')::boolean, true) then raise exception 'FEHLER 9e: Nachtest liefert Abschluss-Felder'; end if;
  raise notice 'ok 9e: Nachtest (Ergebnis %) – flug_geschafft false, keine Abschluss-Felder', t->>'nachtest_ergebnis';
end $$;
rollback;
