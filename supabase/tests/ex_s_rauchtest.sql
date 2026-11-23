-- Rauchtest EX-S (Expeditionen vor die Nase legen: Angebot, „Später“, 150/200 Sterne). Läuft vollständig in einer Transaktion mit Rollback.
-- Spielt die Migration 20261125_ex_s_expedition.sql selbst ein (wiederholbar; vorher oder schon eingespielt, beides geht).
-- Aufruf aus dem Repo-Wurzelverzeichnis: psql -v ON_ERROR_STOP=1 -f supabase/tests/ex_s_rauchtest.sql
-- Nur Testkind; drei Test-Expeditionen als Entwurf (nur fürs Testkind sichtbar) mit Voraussetzungen in Thema 15. Ausgabe nur Zahlen.
begin;

-- Test 0: noch keine gebuchten Expeditionen (keine Sterne, keine Antworten außerhalb des Testkinds) → keine Nachbuchung nötig
do $$
declare v_s int; v_v int;
begin
  select count(*) into v_s from schule.sterne where grund = 'expedition';
  select count(*) into v_v from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id join schule.lernender l on l.id = v.lernender_id
   where a.pool = 'expedition' and not l.ist_test;
  if v_s > 0 or v_v > 0 then raise exception 'Test 0: schon % Expeditions-Sterne / % Antworten auf Expeditionen – Nachbuchung 50 → 150/200 klären', v_s, v_v; end if;
  raise notice 'Test 0 ok: keine Expeditions-Sterne, keine Antworten auf Expeditionen – keine Nachbuchung nötig';
end $$;

create temp table ex_rt_vorher on commit drop as
  select 'karte_stand' t, md5(coalesce(string_agg(k::text, '|' order by k.lernender_id, k.einheit_id, k.lernziel), '')) h from schule.karte_stand k
  union all select 'lernziel_stand', md5(coalesce(string_agg(s::text, '|' order by s.lernender_id, s.einheit_id, s.lernziel), '')) from schule.lernziel_stand s
  union all select 'lernstand', md5(coalesce(string_agg(s::text, '|' order by s.lernender_id, s.thema_id), '')) from schule.lernstand s
  union all select 'sterne', md5(coalesce(string_agg(s::text, '|' order by s.id), '')) from schule.sterne s
  union all select 'route', md5(coalesce(string_agg(r::text, '|' order by r.id), '')) from schule.route r
  union all select 'reiseoptionen_' || l.id, md5(schule.reiseoptionen(l.id)::text) from schule.lernender l where l.aktiv;

\ir ../migrations/20261125_ex_s_expedition.sql
\ir ../migrations/20261125_ex_s_expedition.sql

do $$
declare v_t text; v_r jsonb := schule.sterne_regeln();
begin
  -- Test 1: Regelwerte
  if schule.sterne_regel('sterne_expedition_geschafft') <> 150 or schule.sterne_regel('sterne_expedition_fehlerfrei') <> 200
     or (v_r->>'sterne_expedition_geschafft')::int <> 150 or (v_r->>'sterne_expedition_fehlerfrei')::int <> 200 then
    raise exception 'Test 1: Regelwerte falsch'; end if;
  raise notice 'Test 1 ok: Regelwerte 150 / 200 (auch in sterne_regeln)';
  -- Test 2: Einspielen ändert Lernstand, Sterne, Route, Reiseoptionen nicht
  select string_agg(v.t, ', ') into v_t from ex_rt_vorher v
   where v.h is distinct from (case v.t
     when 'karte_stand' then (select md5(coalesce(string_agg(k::text, '|' order by k.lernender_id, k.einheit_id, k.lernziel), '')) from schule.karte_stand k)
     when 'lernziel_stand' then (select md5(coalesce(string_agg(s::text, '|' order by s.lernender_id, s.einheit_id, s.lernziel), '')) from schule.lernziel_stand s)
     when 'lernstand' then (select md5(coalesce(string_agg(s::text, '|' order by s.lernender_id, s.thema_id), '')) from schule.lernstand s)
     when 'sterne' then (select md5(coalesce(string_agg(s::text, '|' order by s.id), '')) from schule.sterne s)
     when 'route' then (select md5(coalesce(string_agg(r::text, '|' order by r.id), '')) from schule.route r)
     else (select md5(schule.reiseoptionen(substr(v.t, 15)::bigint)::text)) end);
  if v_t is not null then raise exception 'Test 2: verändert: %', v_t; end if;
  raise notice 'Test 2 ok: Einspielen (zweimal) ändert Lernstand, Sterne, Route, Reiseoptionen nicht; % Angebote für bestehende Stände',
    (select count(*) from schule.expedition_angebot);
end $$;

-- Ablauf mit dem Testkind
do $$
declare v_l bigint; v_e bigint; v_lz text[]; v_x bigint[] := '{}'; v_a bigint[] := '{}'; v_i int; v_k jsonb; v_j jsonb; v_st0 jsonb; v_st jsonb;
  v_ro text; v_ts text; v_sterne_vor text; v_ks_vor text; v_ls_vor text; v_n int; v_id bigint; v_t0 timestamptz;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'kein Testkind'; end if;
  v_e := schule.thema_einheit(15);
  select array_agg(x->>'lernziel' order by o) into v_lz from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') with ordinality q(x, o) where e.id = v_e;
  -- Ausgang: Voraussetzung 1 sitzt, Voraussetzung 2 nicht
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am) values (v_l, v_e, v_lz[1], true, now() - interval '2 days'), (v_l, v_e, v_lz[2], false, null)
  on conflict (lernender_id, einheit_id, lernziel) do update set sitzt = excluded.sitzt, sitzt_am = excluded.sitzt_am, gesetzt_am = null;
  -- drei Test-Expeditionen (Entwurf = nur Testkind), je zwei Teile
  for v_i in 1..3 loop
    insert into schule.expedition (schluessel, titel, status, voraussetzungen)
    values ('rt-ex-s-' || v_i, 'Rauchtest ' || v_i, 'entwurf',
            jsonb_build_array(jsonb_build_object('thema_id', 15, 'lernziel', v_lz[1]), jsonb_build_object('thema_id', 15, 'lernziel', v_lz[2])))
    returning id into v_id;
    v_x := v_x || v_id;
    insert into schule.aufgabe (einheit_id, thema_id, art, variante_gruppe, antworttyp, frage, loesung, pool, freigegeben, expedition_id, teil, reihenfolge)
    values (v_e, 15, 'uebung', v_lz[1], 'zahl', '{"text":"rt"}', '1', 'expedition', true, v_id, 'a', 1),
           (v_e, 15, 'uebung', v_lz[2], 'zahl', '{"text":"rt"}', '1', 'expedition', true, v_id, 'b', 2);
  end loop;
  select string_agg(a.id::text, ',' order by a.id) into v_ts from schule.aufgabe a where a.expedition_id = any(v_x);
  v_a := string_to_array(v_ts, ',')::bigint[];   -- je Expedition i: Teile v_a[2i-1], v_a[2i]

  -- Test 3: kein Angebot, solange eine Voraussetzung fehlt
  if exists (select 1 from schule.expedition_angebot where lernender_id = v_l and expedition_id = any(v_x))
     or exists (select 1 from jsonb_array_elements(schule.expeditionen_kind(v_l)) e where (e->>'id')::bigint = any(v_x)) then
    raise exception 'Test 3: Angebot vor der letzten Voraussetzung'; end if;
  v_st0 := schule.expedition_stand(v_l);
  v_ro := md5(schule.reiseoptionen(v_l)::text);
  v_ts := md5((select string_agg(schule.thema_stufe(v_l, t.id)::text, '|' order by t.id) from schule.thema t where t.id <> 15));
  v_ls_vor := md5(coalesce((select string_agg(s::text, '|' order by s.einheit_id, s.lernziel) from schule.lernziel_stand s), ''));

  -- Landung der letzten Voraussetzung → Angebot mit „seit“ = diese Landung
  v_t0 := now();
  update schule.karte_stand set sitzt = true, sitzt_am = v_t0 where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[2];
  select count(*) into v_n from schule.expedition_angebot where lernender_id = v_l and expedition_id = any(v_x) and angeboten_am = v_t0 and spaeter_bis is null;
  if v_n <> 3 then raise exception 'Test 3: % statt 3 Angebote nach der letzten Voraussetzung', v_n; end if;
  v_k := schule.expeditionen_kind(v_l);
  if (select count(*) from jsonb_array_elements(v_k) e where (e->>'id')::bigint = any(v_x) and e->>'zustand' = 'angeboten'
        and not (e->>'ausgeblendet')::boolean and (e->>'angeboten_am') is not null) <> 3 then raise exception 'Test 3: expeditionen_kind ohne Angebot'; end if;
  v_st := schule.expedition_stand(v_l);
  if (v_st->>'stationen_gesamt')::int <> (v_st0->>'stationen_gesamt')::int or (v_st->>'vorn')::int <> (v_st0->>'vorn')::int + 3
     or (v_st->>'oben_id') is null then raise exception 'Test 3: expedition_stand falsch: %', v_st - 'angebote'; end if;
  raise notice 'Test 3 ok: Angebot erst nach der letzten Voraussetzung, seit = deren Landung; Stationen % gesamt, % vorn', v_st->>'stationen_gesamt', v_st->>'vorn';

  -- Test 4: nichts gesperrt – Reiseoptionen, Stufen, Lernziel-Stände unverändert durch das Angebot
  if md5(schule.reiseoptionen(v_l)::text) <> v_ro then raise exception 'Test 4: Reiseoptionen geändert'; end if;
  if md5((select string_agg(schule.thema_stufe(v_l, t.id)::text, '|' order by t.id) from schule.thema t where t.id <> 15)) <> v_ts then raise exception 'Test 4: Stufen geändert'; end if;
  if md5(coalesce((select string_agg(s::text, '|' order by s.einheit_id, s.lernziel) from schule.lernziel_stand s), '')) <> v_ls_vor then raise exception 'Test 4: Lernziel-Stände geändert'; end if;
  raise notice 'Test 4 ok: Angebot sperrt nichts (Reiseoptionen, Stufen aller übrigen Themen, Lernziel-Stände unverändert)';

  -- Test 5: „Später“ blendet bis zum nächsten Lerntag aus
  v_j := schule.expedition_spaeter(v_l, v_x[1]);
  if (v_j->>'spaeter_bis')::date <> schule.kind_heute(v_l) then raise exception 'Test 5: spaeter_bis falsch'; end if;
  if not (schule.expedition_angebot_json(v_l, v_x[1])->>'ausgeblendet')::boolean then raise exception 'Test 5: nach „Später“ nicht ausgeblendet'; end if;
  if (schule.expedition_stand(v_l)->>'vorn')::int <> (v_st->>'vorn')::int - 1 or (schule.expedition_stand(v_l)->>'oben_id')::bigint = v_x[1] then
    raise exception 'Test 5: ausgeblendete Expedition noch vorn'; end if;
  if (select (e->>'id')::bigint from jsonb_array_elements(schule.expeditionen_kind(v_l)) with ordinality q(e, o) where (e->>'id')::bigint = any(v_x) order by o desc limit 1) <> v_x[1] then
    raise exception 'Test 5: ausgeblendete Expedition nicht hinter den übrigen Angeboten'; end if;
  begin
    perform schule.expedition_spaeter(v_l, -1);
    raise exception 'Test 5: „Später“ für nicht angebotene Expedition angenommen';
  exception when sqlstate 'P0001' then if sqlerrm like 'Test 5%' then raise; end if; end;
  update schule.expedition_angebot set spaeter_bis = schule.kind_heute(v_l) - 1 where lernender_id = v_l and expedition_id = v_x[1];   -- wie am Vortag gedrückt
  if (schule.expedition_angebot_json(v_l, v_x[1])->>'ausgeblendet')::boolean then raise exception 'Test 5: am nächsten Lerntag noch ausgeblendet'; end if;
  begin
    perform api.schule_expedition_spaeter('ungueltig', jsonb_build_object('lernender_id', v_l, 'expedition_id', v_x[1]));
    raise exception 'Test 5: Aktion ohne gültigen Schlüssel';
  exception when sqlstate 'P0001' then if sqlerrm like 'Test 5%' then raise; end if; end;
  raise notice 'Test 5 ok: „Später“ blendet bis zum nächsten Lerntag aus, danach wieder vorn; Aktion prüft den Zugriff';

  -- Test 6: Sterne 150 / 200 genau einmal; Lernstand und übrige Sterne unverändert
  v_sterne_vor := md5(coalesce((select string_agg(s::text, '|' order by s.id) from schule.sterne s), ''));
  v_ks_vor := md5(coalesce((select string_agg((k.lernender_id, k.einheit_id, k.lernziel, k.sitzt, k.sitzt_am, k.wdh_stufe, k.richtig, k.falsch)::text, '|'
                                              order by k.lernender_id, k.einheit_id, k.lernziel) from schule.karte_stand k where k.lernender_id <> v_l), ''));
  create temp table ex_rt_sterne_id on commit drop as select id from schule.sterne;
  -- Expedition 1: Teil a mit Tipp → 150
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, hilfe, anlauf) values
    (v_l, v_a[1], 'rt-ex-1a', '1', true, 1, 1), (v_l, v_a[2], 'rt-ex-1b', '1', true, 0, 1);
  -- Expedition 2: alles im ersten Versuch ohne Tipp → 200
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, hilfe, anlauf) values
    (v_l, v_a[3], 'rt-ex-2a', '1', true, 0, 1), (v_l, v_a[4], 'rt-ex-2b', '1', true, 0, 1);
  -- Expedition 3: Teil a erst falsch, im zweiten Anlauf richtig → 150
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, hilfe, anlauf, am) values (v_l, v_a[5], 'rt-ex-3a1', '2', false, 0, 1, now() - interval '1 minute');
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, hilfe, anlauf) values
    (v_l, v_a[5], 'rt-ex-3a2', '1', true, 0, 2), (v_l, v_a[6], 'rt-ex-3b', '1', true, 0, 1);
  -- noch einmal richtig beantworten: keine zweite Buchung
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, hilfe, anlauf) values (v_l, v_a[2], 'rt-ex-1b-2', '1', true, 0, 1), (v_l, v_a[4], 'rt-ex-2b-2', '1', true, 0, 1);
  perform schule.expedition_buchen(v_l, v_a[4], true, 0::smallint, 1::smallint, now());
  for v_i in 1..3 loop
    select count(*), max(menge) into v_n, v_id from schule.sterne where lernender_id = v_l and grund = 'expedition' and bezug = 'expedition:' || v_x[v_i];
    if v_n <> 1 or v_id <> (case v_i when 2 then 200 else 150 end) then raise exception 'Test 6: Expedition %: % Buchungen, % Sterne', v_i, v_n, v_id; end if;
  end loop;
  -- übrige Sterne: alte Zeilen unverändert; neu nur Expeditions-Sterne und die bisherigen Übungs-Sterne für Antworten auf die Test-Expeditionen
  if exists (select 1 from schule.sterne s where s.id not in (select id from ex_rt_sterne_id)
              and not (s.lernender_id = v_l and (s.grund = 'expedition' or (s.grund = 'uebung' and s.bezug = any(array(select 'aufgabe:' || x from unnest(v_a) x)))))) then
    raise exception 'Test 6: fremde neue Sterne'; end if;
  if md5(coalesce((select string_agg(s::text, '|' order by s.id) from schule.sterne s where s.id in (select id from ex_rt_sterne_id)), '')) <> v_sterne_vor then
    raise exception 'Test 6: bestehende Sterne verändert'; end if;
  if md5(coalesce((select string_agg((k.lernender_id, k.einheit_id, k.lernziel, k.sitzt, k.sitzt_am, k.wdh_stufe, k.richtig, k.falsch)::text, '|'
                                     order by k.lernender_id, k.einheit_id, k.lernziel) from schule.karte_stand k where k.lernender_id <> v_l), '')) <> v_ks_vor then
    raise exception 'Test 6: Lernstand anderer Kinder verändert'; end if;
  if md5(coalesce((select string_agg(s::text, '|' order by s.einheit_id, s.lernziel) from schule.lernziel_stand s), '')) <> v_ls_vor then raise exception 'Test 6: Lernziel-Stände verändert'; end if;
  if md5(schule.reiseoptionen(v_l)::text) <> v_ro then raise exception 'Test 6: Reiseoptionen geändert'; end if;
  v_k := schule.expeditionen_kind(v_l);
  if (select count(*) from jsonb_array_elements(v_k) e where (e->>'id')::bigint = any(v_x) and e->>'zustand' = 'geschafft') <> 3
     or (select (e->>'fehlerfrei')::boolean from jsonb_array_elements(v_k) e where (e->>'id')::bigint = v_x[2]) is not true
     or (select (e->>'fehlerfrei')::boolean from jsonb_array_elements(v_k) e where (e->>'id')::bigint = v_x[3]) is not false
     or (select (e->>'sterne')::int from jsonb_array_elements(v_k) e where (e->>'id')::bigint = v_x[2]) <> 200 then
    raise exception 'Test 6: expeditionen_kind nach dem Lösen falsch'; end if;
  v_st := schule.expedition_stand(v_l);
  if (v_st->>'stationen_geschafft')::int <> (v_st0->>'stationen_geschafft')::int + 3 or (v_st->>'vorn')::int <> (v_st0->>'vorn')::int then
    raise exception 'Test 6: Stationen geschafft falsch: %', v_st - 'angebote'; end if;
  raise notice 'Test 6 ok: 150 / 200 / 150 Sterne je genau einmal; Stationen % von % geschafft; übrige Sterne, Lernstand und Reiseoptionen unverändert',
    v_st->>'stationen_geschafft', v_st->>'stationen_gesamt';

  -- Test 7: Ausgabe in schule_konto und schule_uebersicht (Quelltext; Schlüssel der App gibt es hier nicht)
  if position('schule.expedition_stand(v_l)' in pg_get_functiondef('api.schule_konto(text, jsonb)'::regprocedure)) = 0 then
    raise exception 'Test 7: expeditionen_stand fehlt in schule_konto'; end if;
  if to_regprocedure('api.schule_uebersicht(text, jsonb)') is not null then
    if position('schule.expedition_stand(l.id)' in pg_get_functiondef(to_regprocedure('api.schule_uebersicht(text, jsonb)'))) = 0 then
      raise exception 'Test 7: expeditionen_stand fehlt in schule_uebersicht'; end if;
  end if;
  raise notice 'Test 7 ok: expeditionen_stand in schule_konto und schule_uebersicht';
end $$;

rollback;
