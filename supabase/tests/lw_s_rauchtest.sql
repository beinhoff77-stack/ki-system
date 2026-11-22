-- Rauchtest LW-S / LW-S 2 („Was wackelt“ mit gespeichertem Status). Nach 20261123_lw_s_wackelt_status.sql. Transaktion mit Rollback, nur Testkind, keine Namen.
-- Unabhängig vom Bestand: ein Thema, auf das das Testkind nie geantwortet hat; Antworten werden mit festen Zeitpunkten angelegt
-- (in einer Transaktion ist now() fest, „danach“ braucht also eigene Zeitpunkte).
begin;

do $$
declare v_l bigint; v_t bigint; v_e bigint; v_lz text[]; v_a bigint[]; w jsonb; x jsonb; v_n0 int; v_n int; v_b0 text; v_b1 text; v_fehler boolean;
  v_l2 bigint; v_k text; v_le text; v_lg text; v_la text; v_lo bigint;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER Vorbereitung: kein Testkind'; end if;
  -- Thema mit zwei Etappen (je eine Übungsaufgabe), ohne Antworten und ohne Status des Testkinds
  select e.thema_id, e.id, array[q1.lz, q2.lz], array[q1.a, q2.a] into v_t, v_e, v_lz, v_a
    from schule.einheit e
    cross join lateral (select a.variante_gruppe lz, min(a.id) a from schule.aufgabe a where a.einheit_id = e.id and a.pool = 'uebung'
                         group by 1 order by 1 limit 1) q1
    cross join lateral (select a.variante_gruppe lz, min(a.id) a from schule.aufgabe a where a.einheit_id = e.id and a.pool = 'uebung' and a.variante_gruppe > q1.lz
                         group by 1 order by 1 limit 1) q2
   where exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) q where q->>'lernziel' = q1.lz)
     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) q where q->>'lernziel' = q2.lz)
     and not exists (select 1 from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id join schule.einheit y on y.id = a.einheit_id
                      where v.lernender_id = v_l and y.thema_id = e.thema_id)
     and not exists (select 1 from schule.wackelt_status s where s.lernender_id = v_l and s.thema_id = e.thema_id)
     and not exists (select 1 from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = e.id)
   order by e.thema_id, e.id limit 1;
  if v_t is null then raise exception 'FEHLER Vorbereitung: kein passendes Thema'; end if;
  v_n0 := (schule.wackelt_liste(v_l)->>'zu_besprechen')::int;

  -- 1 drei endgültig falsche Antworten in Etappe 1 (vor 60 Minuten, ohne zweite Chance): Eintrag „zu besprechen“ (Vorgabe, Etappe wackelt)
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, am)
  select v_l, v_a[1], 'lw-s-' || gen_random_uuid(), '{}'::jsonb, false, 0, 1, 0, i, now() - interval '60 minutes' + i * interval '1 second' from generate_series(1, 3) i;
  w := schule.wackelt_liste(v_l);
  select e into x from jsonb_array_elements(w->'eintraege') e where (e->>'thema_id')::bigint = v_t and e->>'einheit_id' is null;
  if x is null or x->>'status' <> 'zu_besprechen' or x->>'quelle' <> 'vorgabe' or (x->>'fehler')::int <> 3 or x->'etappe'->>'lernziel' <> v_lz[1]
     or (w->>'zu_besprechen')::int <> v_n0 + 1 then raise exception 'FEHLER 1 Vorgabe: %', x; end if;
  raise notice 'ok 1 drei Fehler: Eintrag „zu besprechen“ (Vorgabe), Zahl für den Reiter +1';

  -- 2 besprochen setzen (Thema): gespeichert, Zahl wieder wie vorher; Lernstand, Sterne, Plan dabei unverändert
  select md5(string_agg(t, '|' order by t)) into v_b0 from (
    select y::text t from schule.karte_stand y union all select y::text from schule.sterne y union all select y::text from schule.route y
    union all select y::text from schule.lernender y union all select y::text from schule.versuch y) q;
  w := schule.wackelt_setzen(v_l, v_t, null, null, 'besprochen', 'eltern:Rauchtest');
  select md5(string_agg(t, '|' order by t)) into v_b1 from (
    select y::text t from schule.karte_stand y union all select y::text from schule.sterne y union all select y::text from schule.route y
    union all select y::text from schule.lernender y union all select y::text from schule.versuch y) q;
  if v_b0 <> v_b1 then raise exception 'FEHLER 2 Setzen verändert Lernstand/Sterne/Plan'; end if;
  if w->'eintrag'->>'status' <> 'besprochen' or w->'eintrag'->>'quelle' <> 'gespeichert' or w->'eintrag'->>'status_von' <> 'eltern:Rauchtest'
     or (w->'eintrag'->>'fehler_neu')::int <> 0 or (w->>'zu_besprechen')::int <> v_n0 then raise exception 'FEHLER 2 besprochen: %', w; end if;
  update schule.wackelt_status set am = now() - interval '20 minutes' where lernender_id = v_l and thema_id = v_t and bezug = ''; -- Zeitpunkt vor den nächsten Antworten
  raise notice 'ok 2 besprochen gespeichert (wer, wann), Zahl zurück, Lernstand/Sterne/Plan unverändert';

  -- 3 LW-S 2 (A1): 1. Anlauf falsch (noch offen) öffnet nicht; wird er durch Weitergehen endgültig, öffnet er wieder; ein neutraler 2. Anlauf öffnet nicht
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf, am)
  values (v_l, v_a[1], 'lw-s-' || gen_random_uuid(), '{}'::jsonb, false, 0, 1, 0, 4, 1, now() - interval '15 minutes');
  select e into x from jsonb_array_elements(schule.wackelt_liste(v_l)->'eintraege') e where (e->>'thema_id')::bigint = v_t and e->>'einheit_id' is null;
  if x->>'status' <> 'besprochen' then raise exception 'FEHLER 3a offener 1. Anlauf öffnet schon: %', x; end if;
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, am)  -- weitergegangen (andere Aufgabe, richtig)
  values (v_l, v_a[2], 'lw-s-' || gen_random_uuid(), '{}'::jsonb, true, 1, 1, 0, 1, now() - interval '14 minutes');
  w := schule.wackelt_liste(v_l);
  select e into x from jsonb_array_elements(w->'eintraege') e where (e->>'thema_id')::bigint = v_t and e->>'einheit_id' is null;
  if x->>'status' <> 'zu_besprechen' or not (x->>'wieder_offen')::boolean or x->>'status_gespeichert' <> 'besprochen' or (x->>'fehler_neu')::int <> 1
     or (w->>'zu_besprechen')::int <> v_n0 + 1 then raise exception 'FEHLER 3b 1. Anlauf endgültig, aber nicht wieder offen: %', x; end if;
  perform schule.wackelt_setzen(v_l, v_t, null, null, 'besprochen', 'eltern:Rauchtest');
  update schule.wackelt_status set am = now() - interval '10 minutes' where lernender_id = v_l and thema_id = v_t and bezug = '';
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf, am)   -- 1. Anlauf, längst endgültig
  values (v_l, v_a[1], 'lw-s-' || gen_random_uuid(), '{}'::jsonb, false, 0, 1, 0, 6, 1, now() - interval '50 minutes');
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf, am)   -- 2. Anlauf danach: neutral
  values (v_l, v_a[1], 'lw-s-' || gen_random_uuid(), '{}'::jsonb, false, 0, 1, 0, 7, 2, now() - interval '8 minutes');
  if schule.versuch_wertung((select v from schule.versuch v where v.lernender_id = v_l and v.aufgabe_id = v_a[1] and v.anlauf = 2 order by v.am desc limit 1)) <> 'neutral' then
    raise exception 'FEHLER 3c Vorbereitung: 2. Anlauf ist nicht neutral'; end if;
  select e into x from jsonb_array_elements(schule.wackelt_liste(v_l)->'eintraege') e where (e->>'thema_id')::bigint = v_t and e->>'einheit_id' is null;
  if x->>'status' <> 'besprochen' then raise exception 'FEHLER 3c neutraler Fehler öffnet: %', x; end if;
  raise notice 'ok 3 1. Anlauf: offen öffnet nicht, endgültig (Weitergehen) öffnet wieder; neutraler 2. Anlauf öffnet nicht';

  -- 4 Etappe 2 mit eigenem Status „beobachten“: eigener Eintrag, der Thema-Eintrag enthält Etappe 2 nicht mehr
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, am)
  values (v_l, v_a[2], 'lw-s-' || gen_random_uuid(), '{}'::jsonb, false, 0, 1, 0, 2, now() - interval '1 minute');
  w := schule.wackelt_setzen(v_l, v_t, v_e, v_lz[2], 'beobachten', 'lehrer:Rauchtest');
  if w->'eintrag'->>'status' <> 'beobachten' or w->'eintrag'->>'lernziel' <> v_lz[2] or (w->'eintrag'->>'fehler')::int <> 1 then raise exception 'FEHLER 4 Etappe: %', w; end if;
  select e into x from jsonb_array_elements(schule.wackelt_liste(v_l)->'eintraege') e where (e->>'thema_id')::bigint = v_t and e->>'einheit_id' is null;
  if exists (select 1 from jsonb_array_elements(x->'etappen') q where q->>'lernziel' = v_lz[2]) then raise exception 'FEHLER 4 Etappe doppelt: %', x; end if;
  w := schule.wackelt_setzen(v_l, v_t, v_e, v_lz[2], 'besprochen', 'lehrer:Rauchtest'); -- erneut setzen überschreibt
  if w->'eintrag'->>'status' <> 'besprochen' or (select count(*) from schule.wackelt_status where lernender_id = v_l and thema_id = v_t) <> 2 then
    raise exception 'FEHLER 4 Überschreiben: %', w; end if;
  raise notice 'ok 4 Status je Etappe: eigener Eintrag, kein Doppel, erneutes Setzen überschreibt';

  -- 5 Eingaben prüfen
  v_n := 0;
  begin perform schule.wackelt_setzen(v_l, v_t, null, null, 'erledigt', 'x'); exception when others then v_n := v_n + 1; end;
  begin perform schule.wackelt_setzen(v_l, v_t, v_e, 'gibt-es-nicht', 'besprochen', 'x'); exception when others then v_n := v_n + 1; end;
  begin perform schule.wackelt_setzen(v_l, v_t, v_e, null, 'besprochen', 'x'); exception when others then v_n := v_n + 1; end;
  begin perform api.schule_wackelt_lesen('ohne-recht-rauchtest', jsonb_build_object('lernender_id', v_l)); exception when others then v_n := v_n + 1; end;
  begin perform api.schule_wackelt_setzen('ohne-recht-rauchtest', jsonb_build_object('lernender_id', v_l, 'thema_id', v_t, 'status', 'besprochen')); exception when others then v_n := v_n + 1; end;
  if v_n <> 5 then raise exception 'FEHLER 5 Eingaben/Zugriff: nur % von 5 abgelehnt', v_n; end if;
  raise notice 'ok 5 falscher Status, fremde Etappe, halbe Etappe, Aufruf ohne Eltern-/Lehrer-Recht abgelehnt';

  -- 6 LW-S 2 (A2): Zugänge über Lern-Zugänge, die der Test selbst anlegt (zufällige Schlüssel, keine echten)
  insert into schule.lernender (anzeigename, ist_test, aktiv, klasse, schulart) values ('Testkind Rauchtest', true, true, 6, 'gym_by') returning id into v_l2;
  v_k := 'lw-s-' || gen_random_uuid(); v_le := 'lw-s-' || gen_random_uuid(); v_lg := 'lw-s-' || gen_random_uuid(); v_la := 'lw-s-' || gen_random_uuid();
  insert into schule.lern_login (name, rolle, lernender_id, code_hash, aktiv) values ('Rauchtest Kind', 'kind', v_l, 'lw-s-' || gen_random_uuid(), true) returning id into v_lo;
  insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) values (v_k, v_lo, now() + interval '1 hour');
  insert into schule.lern_login (name, rolle, code_hash, aktiv) values ('Rauchtest Lehrer', 'lehrer', 'lw-s-' || gen_random_uuid(), true) returning id into v_lo;
  insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) values (v_le, v_lo, now() + interval '1 hour'), (v_la, v_lo, now() - interval '1 minute');
  insert into schule.lern_login (name, rolle, code_hash, aktiv) values ('Rauchtest gesperrt', 'eltern', 'lw-s-' || gen_random_uuid(), false) returning id into v_lo;
  insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) values (v_lg, v_lo, now() + interval '1 hour');
  v_n := 0;   -- abgelehnt werden müssen: Kind (eigenes und fremdes Kind, lesen und setzen), gesperrter Zugang, abgelaufene Sitzung
  begin perform api.schule_wackelt_lesen('lern:' || v_k, jsonb_build_object('lernender_id', v_l)); exception when others then v_n := v_n + 1; end;
  begin perform api.schule_wackelt_lesen('lern:' || v_k, jsonb_build_object('lernender_id', v_l2)); exception when others then v_n := v_n + 1; end;
  begin perform api.schule_wackelt_setzen('lern:' || v_k, jsonb_build_object('lernender_id', v_l, 'thema_id', v_t, 'status', 'besprochen')); exception when others then v_n := v_n + 1; end;
  begin perform api.schule_wackelt_lesen('lern:' || v_lg, jsonb_build_object('lernender_id', v_l)); exception when others then v_n := v_n + 1; end;
  begin perform api.schule_wackelt_lesen('lern:' || v_la, jsonb_build_object('lernender_id', v_l)); exception when others then v_n := v_n + 1; end;
  if v_n <> 5 then raise exception 'FEHLER 6 Zugänge: nur % von 5 abgelehnt', v_n; end if;
  -- Lehrer (Lern-Zugang): Eltern/Lehrer sehen laut schule.sieht alle Kinder – Testkind und zweites Testkind lesbar, setzen mit Namen
  if not (api.schule_wackelt_lesen('lern:' || v_le, jsonb_build_object('lernender_id', v_l))->>'ok')::boolean
     or not (api.schule_wackelt_lesen('lern:' || v_le, jsonb_build_object('lernender_id', v_l2))->>'ok')::boolean then raise exception 'FEHLER 6 Lehrer liest nicht'; end if;
  w := api.schule_wackelt_setzen('lern:' || v_le, jsonb_build_object('lernender_id', v_l, 'thema_id', v_t, 'status', 'beobachten'));
  if w->'eintrag'->>'status_von' <> 'lehrer:Rauchtest Lehrer' then raise exception 'FEHLER 6 Lehrer setzt: %', w; end if;
  raise notice 'ok 6 Zugänge: Kind (eigenes/fremdes), gesperrt, abgelaufen abgelehnt; Lehrer liest und setzt (mit Namen)';
  raise notice 'LW-S Rauchtest durchgelaufen';
end $$;

rollback;
