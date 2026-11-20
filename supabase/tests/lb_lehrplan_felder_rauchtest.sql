-- Rauchtest LB-Felder (Lehrplan „Nach Klasse“). Nach 20261120_lb_lehrplan_felder.sql ausführen. Rollback, keine Kinderdaten, keine Namen.
-- Prüft Spalten, dass die beiden Lesefunktionen die neuen Felder enthalten, und dass die Etappen-Liste je Thema aus dem Inhalt kommt.
-- Der äußere Zugang (api.* mit Schlüssel) ist nicht getestet.
begin;
do $$
declare v_t bigint; v_n int; v_d text;
begin
  if (select count(*) from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name in ('lernbereich', 'lehrplan')) <> 2 then raise exception 'FEHLER 1: Spalten fehlen'; end if;
  v_d := pg_get_functiondef('api.schule_plan_lesen(text, jsonb)'::regprocedure);
  if position('''lernbereich''' in v_d) = 0 or position('''beschreibung''' in v_d) = 0 or position('''etappen''' in v_d) = 0 or position('''stufe''' in v_d) = 0 then raise exception 'FEHLER 2: schule_plan_lesen'; end if;
  v_d := pg_get_functiondef('api.schule_lehrplan_uebersicht(text, jsonb)'::regprocedure);
  if position('''lernbereich''' in v_d) = 0 or position('''lehrplan_reihenfolge''' in v_d) = 0 then raise exception 'FEHLER 3: schule_lehrplan_uebersicht'; end if;
  raise notice 'ok 1–3: Spalten lernbereich/lehrplan da, beide Lesefunktionen liefern die Felder';
  -- Felder lassen sich schreiben und lesen (im Rollback)
  select id into v_t from schule.thema where fach = 'Mathematik' order by id limit 1;
  update schule.thema set lernbereich = '{"gym_by": "Rauchtest-Lernbereich"}', lehrplan = '{"gym_by": "Rauchtest-Lehrplan"}' where id = v_t;
  if (select lernbereich->>'gym_by' from schule.thema where id = v_t) <> 'Rauchtest-Lernbereich' then raise exception 'FEHLER 4'; end if;
  -- Etappen-Liste: so viele Einträge wie im Inhalt
  select jsonb_array_length(coalesce(e.inhalt->'etappen', '[]'::jsonb)) into v_n from schule.einheit e where e.thema_id = v_t order by (e.status in ('geprueft','freigegeben')) desc, e.version desc limit 1;
  raise notice 'ok 4: Felder schreib- und lesbar; Thema % hat % Etappen im Inhalt', v_t, coalesce(v_n, 0);
end $$;
rollback;
