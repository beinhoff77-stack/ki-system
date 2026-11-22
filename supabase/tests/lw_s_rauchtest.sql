-- Rauchtest LW-S („Was wackelt“ mit gespeichertem Status). Nach 20261123_lw_s_wackelt_status.sql. Transaktion mit Rollback, nur Testkind, keine Namen.
-- Unabhängig vom Bestand: ein Thema, auf das das Testkind nie geantwortet hat; Antworten werden mit festen Zeitpunkten angelegt
-- (in einer Transaktion ist now() fest, „danach“ braucht also eigene Zeitpunkte).
begin;

do $$
declare v_l bigint; v_t bigint; v_e bigint; v_lz text[]; v_a bigint[]; w jsonb; x jsonb; v_n0 int; v_n int; v_b0 text; v_b1 text; v_fehler boolean;
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

  -- 1 drei endgültig falsche Antworten in Etappe 1 (vor 10 Minuten): Eintrag „zu besprechen“ (Vorgabe, Etappe wackelt)
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, am)
  select v_l, v_a[1], 'lw-s-' || gen_random_uuid(), '{}'::jsonb, false, 0, 1, 0, i, now() - interval '10 minutes' + i * interval '1 second' from generate_series(1, 3) i;
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
  update schule.wackelt_status set am = now() - interval '5 minutes' where lernender_id = v_l and thema_id = v_t and bezug = ''; -- Zeitpunkt vor den nächsten Antworten
  raise notice 'ok 2 besprochen gespeichert (wer, wann), Zahl zurück, Lernstand/Sterne/Plan unverändert';

  -- 3 1. Versuch mit zweiter Chance zählt nicht; danach ein neuer endgültiger Fehler: wieder „zu besprechen“
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf, am)
  values (v_l, v_a[1], 'lw-s-' || gen_random_uuid(), '{}'::jsonb, false, 0, 1, 0, 4, 1, now() - interval '2 minutes');
  select e into x from jsonb_array_elements(schule.wackelt_liste(v_l)->'eintraege') e where (e->>'thema_id')::bigint = v_t and e->>'einheit_id' is null;
  if x->>'status' <> 'besprochen' then raise exception 'FEHLER 3a 1. Versuch mit zweiter Chance zählt: %', x; end if;
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, am)
  values (v_l, v_a[1], 'lw-s-' || gen_random_uuid(), '{}'::jsonb, false, 0, 1, 0, 5, now() - interval '1 minute');
  w := schule.wackelt_liste(v_l);
  select e into x from jsonb_array_elements(w->'eintraege') e where (e->>'thema_id')::bigint = v_t and e->>'einheit_id' is null;
  if x->>'status' <> 'zu_besprechen' or not (x->>'wieder_offen')::boolean or x->>'status_gespeichert' <> 'besprochen' or (x->>'fehler_neu')::int <> 1
     or (w->>'zu_besprechen')::int <> v_n0 + 1 then raise exception 'FEHLER 3b neuer Fehler: %', x; end if;
  raise notice 'ok 3 neuer Fehler im Thema: wieder „zu besprechen“ (1. Versuch mit zweiter Chance zählt nicht)';

  -- 4 Etappe 2 mit eigenem Status „beobachten“: eigener Eintrag, der Thema-Eintrag enthält Etappe 2 nicht mehr
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, am)
  values (v_l, v_a[2], 'lw-s-' || gen_random_uuid(), '{}'::jsonb, false, 0, 1, 0, 1, now() - interval '1 minute');
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
  raise notice 'LW-S Rauchtest durchgelaufen';
end $$;

rollback;
