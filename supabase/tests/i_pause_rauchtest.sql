-- Rauchtest I-10 (Reisetage und Pausen). Nach 20261120_i_pause.sql ausführen. Rollback, nur Testkind, keine Namen.
-- Hängt nicht von vorhandenen Daten ab (legt eigene Einträge an). Der Weg über api.schule_notiz_setzen braucht einen Zugangsschlüssel und ist hier nicht getestet;
-- geprüft werden Tabelle, Prüfregeln, Markieren statt Löschen und dass die Funktionen den neuen Zweig bzw. pausen[] enthalten.
begin;
do $$
declare v_l bigint; v_p bigint; v_ok boolean; v_n int;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  -- 1. eintragen
  insert into schule.pause(lernender_id, von, bis, grund, wer) values (v_l, current_date, current_date + 3, 'Reisetag', 'lehrer:Test') returning id into v_p;
  insert into schule.pause(lernender_id, von, bis, wer) values (v_l, current_date - 20, current_date - 18, 'eltern:Test'); -- vergangen, ohne Grund
  raise notice 'ok 1: Einträge angelegt (mit und ohne Grund)';
  -- 2. Prüfregeln: bis vor von, Grund zu lang, mehr als ein Jahr
  v_ok := false; begin insert into schule.pause(lernender_id, von, bis, wer) values (v_l, current_date, current_date - 1, 'x'); exception when check_violation then v_ok := true; end;
  if not v_ok then raise exception 'FEHLER 2a: bis vor von angenommen'; end if;
  v_ok := false; begin insert into schule.pause(lernender_id, von, bis, grund, wer) values (v_l, current_date, current_date, repeat('x', 41), 'x'); exception when check_violation then v_ok := true; end;
  if not v_ok then raise exception 'FEHLER 2b: Grund über 40 Zeichen angenommen'; end if;
  v_ok := false; begin insert into schule.pause(lernender_id, von, bis, wer) values (v_l, current_date, current_date + 400, 'x'); exception when check_violation then v_ok := true; end;
  if not v_ok then raise exception 'FEHLER 2c: mehr als ein Jahr angenommen'; end if;
  raise notice 'ok 2: Prüfregeln greifen';
  -- 3. ändern und löschen (markieren) – vergangene bleiben
  update schule.pause set bis = current_date + 5, geaendert_am = now() where id = v_p;
  update schule.pause set geloescht_am = now() where id = v_p;
  select count(*) into v_n from schule.pause where lernender_id = v_l and geloescht_am is null;
  if v_n <> 1 then raise exception 'FEHLER 3: % sichtbare Einträge, erwartet 1 (der vergangene)', v_n; end if;
  if not exists (select 1 from schule.pause where id = v_p) then raise exception 'FEHLER 3b: gelöschter Eintrag ist weg statt markiert'; end if;
  raise notice 'ok 3: geändert, als gelöscht markiert; der vergangene Eintrag bleibt sichtbar';
  -- 4. Funktionen enthalten den neuen Zweig bzw. pausen[]
  if position('''pause''' in pg_get_functiondef('api.schule_notiz_setzen(text, jsonb)'::regprocedure)) = 0
     or position('''pausen''' in pg_get_functiondef('api.schule_lernstand(text, jsonb)'::regprocedure)) = 0 then raise exception 'FEHLER 4: Funktionen nicht angepasst'; end if;
  if position('''besprochen''' in pg_get_functiondef('api.schule_notiz_setzen(text, jsonb)'::regprocedure)) = 0 then raise exception 'FEHLER 4b: Zweig „besprochen“ (LA-3) fehlt'; end if;
  raise notice 'ok 4: schule_notiz_setzen (pause, besprochen, Notiz) und schule_lernstand (pausen) angepasst';
end $$;
rollback;
