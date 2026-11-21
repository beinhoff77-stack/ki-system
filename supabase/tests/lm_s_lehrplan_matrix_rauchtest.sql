-- Rauchtest LM-S (Daten der Lehrplan-Matrix). Nach 20261121_lm_s_lehrplan_matrix.sql ausführen. Transaktion mit Rollback, nur Testkind, keine Namen in der Ausgabe.
-- Läuft über schule.lehrplan_matrix (api.schule_lehrplan_matrix ruft genau diese Funktion nach der Rollen-/Zugriffsprüfung auf – ein Schlüssel gehört nicht in eine Datei).
-- Prüfungen 1–7 vergleichen die Ausgabe mit den Tabellen selbst (keine festen Zahlen aus dem Bestand); Prüfung 6 legt sich ihren Fehler im Testkind selbst an.
-- Prüfung 8 (Selbstprüfung Dreißigste Runde) meldet die drei Regeln als NOTICE mit Anzahl und Thema-Nummern – kein Abbruch, weil Verbindungen noch fehlen
-- (Stand 21.11.: Themen 100–103 ohne Verbindung) und „eigenständig“ noch nicht gespeichert wird. Soll eine Regel später hart werden: NOTICE → EXCEPTION.
begin;

do $$
declare v_l bigint; v_m jsonb; v_k jsonb; v_n int; v_soll int; v_th jsonb; v_e bigint; v_lz text; v_t bigint; v_txt text;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;

  v_m := schule.lehrplan_matrix(array[v_l], false);   -- Sicht Eltern/Lehrer (nur mit dem Testkind)
  v_k := schule.lehrplan_matrix(array[v_l], true);    -- Kindsicht

  -- 1: jedes Mathe-Thema genau einmal (die Übersicht liefert je Thema × Ort)
  select count(*) into v_soll from schule.thema where fach = 'Mathematik';
  if jsonb_array_length(v_m->'themen') <> v_soll then raise exception 'FEHLER 1 Themen: % statt %', jsonb_array_length(v_m->'themen'), v_soll; end if;
  select count(distinct (x->>'thema_id')) into v_n from jsonb_array_elements(v_m->'themen') x;
  if v_n <> v_soll then raise exception 'FEHLER 1 Thema doppelt'; end if;
  raise notice 'ok 1 Themen je einmal (%)', v_soll;

  -- 2: Felder der Lehrer-Sicht; merke und Etappen genau dann, wenn eine freigegebene Einheit da ist
  if exists (select 1 from jsonb_array_elements(v_m->'themen') x where not (x ? 'titel' and x ? 'gebiet' and x ? 'jahrgang' and x ? 'etappen' and x ? 'pflicht')) then
    raise exception 'FEHLER 2 Pflichtfeld fehlt (titel/gebiet/jahrgang/etappen/pflicht)'; end if;
  if exists (select 1 from jsonb_array_elements(v_m->'themen') x where (x ? 'einheit_id') <> (schule.thema_einheit((x->>'thema_id')::bigint) is not null)) then
    raise exception 'FEHLER 2 einheit_id passt nicht zu schule.thema_einheit'; end if;
  select x into v_th from jsonb_array_elements(v_m->'themen') x where x ? 'einheit_id' and jsonb_array_length(x->'etappen') > 0 limit 1;
  if v_th is not null then
    select count(*) into v_soll from jsonb_array_elements((select e.inhalt->'etappen' from schule.einheit e where e.id = (v_th->>'einheit_id')::bigint));
    if jsonb_array_length(v_th->'etappen') <> v_soll then raise exception 'FEHLER 2 Etappen-Anzahl'; end if;
    select count(*) into v_soll from jsonb_array_elements(v_th->'etappen') x
     where (x->>'pflicht')::boolean <> coalesce((select e.inhalt->'bewertung'->'lernziele_pflicht' from schule.einheit e where e.id = (v_th->>'einheit_id')::bigint), '[]'::jsonb) ? (x->>'lernziel');
    if v_soll <> 0 then raise exception 'FEHLER 2 Pflicht-Kennzeichen der Etappen'; end if;
    if (v_th->'merke') is distinct from (select e.inhalt->'merke' from schule.einheit e where e.id = (v_th->>'einheit_id')::bigint) then raise exception 'FEHLER 2 merke'; end if;
  end if;
  if exists (select 1 from jsonb_array_elements(v_m->'themen') x where x ? 'beispiel' and length(x->>'beispiel') >= 160) then raise exception 'FEHLER 2 Beispiel zu lang'; end if;
  raise notice 'ok 2 Felder, merke, Etappen mit Pflicht, Beispiel < 160';

  -- 3: Verbindungen = alle Mathe-Verbindungen aus schule.voraussetzung, mit Art und (Lehrer) Begründung
  select count(*) into v_soll from schule.voraussetzung v join schule.thema a on a.id = v.thema_id and a.fach = 'Mathematik' join schule.thema b on b.id = v.braucht_id and b.fach = 'Mathematik';
  if jsonb_array_length(v_m->'verbindungen') <> v_soll then raise exception 'FEHLER 3 Verbindungen: % statt %', jsonb_array_length(v_m->'verbindungen'), v_soll; end if;
  if exists (select 1 from jsonb_array_elements(v_m->'verbindungen') x where not (x ? 'art')) then raise exception 'FEHLER 3 Art fehlt'; end if;
  select count(*) into v_soll from schule.voraussetzung v join schule.thema a on a.id = v.thema_id and a.fach = 'Mathematik' join schule.thema b on b.id = v.braucht_id and b.fach = 'Mathematik' where v.begruendung is not null;
  select count(*) into v_n from jsonb_array_elements(v_m->'verbindungen') x where x ? 'begruendung';
  if v_n <> v_soll then raise exception 'FEHLER 3 Begründungen: % statt %', v_n, v_soll; end if;
  raise notice 'ok 3 Verbindungen (%)', jsonb_array_length(v_m->'verbindungen');

  -- 4: Lernstand je Kind und Thema, Etappe x von y nur bei ▶
  if jsonb_array_length(v_m->'kinder') <> 1 or (v_m->'kinder'->0->>'id')::bigint <> v_l then raise exception 'FEHLER 4 Kinderliste'; end if;
  select count(*) into v_n from jsonb_object_keys(v_m->'lernstand'->v_l::text);
  if v_n <> jsonb_array_length(v_m->'themen') then raise exception 'FEHLER 4 Lernstand: % Themen statt %', v_n, jsonb_array_length(v_m->'themen'); end if;
  if exists (select 1 from jsonb_each(v_m->'lernstand'->v_l::text) s where not (s.value ? 'stufe' and s.value ? 'im_plan' and s.value ? 'fehler_offen')) then raise exception 'FEHLER 4 Lernstand-Felder'; end if;
  if exists (select 1 from jsonb_each(v_m->'lernstand'->v_l::text) s where (s.value->>'stufe' = 'dran') <> (s.value ? 'etappe_jetzt' and s.value->'etappe_jetzt' <> 'null'::jsonb)) then
    raise exception 'FEHLER 4 etappe_jetzt nur und immer bei Stufe dran'; end if;
  if exists (select 1 from jsonb_each(v_m->'lernstand'->v_l::text) s where s.value->>'stufe' = 'dran'
              and (s.value->>'etappe_jetzt')::int > greatest(coalesce((s.value->>'etappen')::int, 1), 1)) then raise exception 'FEHLER 4 Etappe x größer als y'; end if;
  raise notice 'ok 4 Lernstand je Thema';

  -- 5: Kindsicht ohne Lehrplan-Wortlaut, Lernbereiche, Klassen je Schulart, Pflicht-Kennzeichen, Begründungen, Schulart, fehler_offen – mit Zeile (Klasse) je Thema
  if exists (select 1 from jsonb_array_elements(v_k->'themen') x where x ?| array['lehrplan', 'lernbereich', 'jahrgang', 'pflicht', 'lehrplan_reihenfolge', 'eigenstaendig']) then
    raise exception 'FEHLER 5 Kindsicht enthält Lehrer-Felder'; end if;
  if exists (select 1 from jsonb_array_elements(v_k->'themen') x where not (x ? 'zeile')) then raise exception 'FEHLER 5 Kindsicht ohne Zeile'; end if;
  if exists (select 1 from jsonb_array_elements(v_k->'verbindungen') x where x ? 'begruendung') then raise exception 'FEHLER 5 Kindsicht mit Begründung'; end if;
  if (v_k->'kinder'->0) ? 'schulart' or v_k ? 'schulart_kind' then raise exception 'FEHLER 5 Kindsicht mit Schulart'; end if;
  if exists (select 1 from jsonb_each(v_k->'lernstand'->v_l::text) s where s.value ? 'fehler_offen') then raise exception 'FEHLER 5 Kindsicht mit fehler_offen'; end if;
  if jsonb_array_length(v_k->'kinder') <> 1 or (select count(*) from jsonb_object_keys(v_k->'lernstand')) <> 1 then raise exception 'FEHLER 5 Kindsicht mit anderen Kindern'; end if;
  if v_k->'themen' is null or jsonb_array_length(v_k->'themen') <> jsonb_array_length(v_m->'themen') then raise exception 'FEHLER 5 Kindsicht Themenzahl'; end if;
  raise notice 'ok 5 Kindsicht';

  -- 6: „Fehler offen“ – eine Pflicht-Etappe des Testkinds auf fehler setzen (Rollback nimmt es zurück)
  select x->>'thema_id', (x->>'einheit_id')::bigint, e->>'lernziel' into v_t, v_e, v_lz
    from jsonb_array_elements(v_m->'themen') x cross join lateral jsonb_array_elements(x->'etappen') e
   where x ? 'einheit_id' and (e->>'pflicht')::boolean order by (x->>'thema_id')::bigint limit 1;
  if v_e is null then raise notice 'übersprungen 6 (keine Einheit mit Pflicht-Etappe)';
  else
    insert into schule.lernziel_stand (lernender_id, einheit_id, lernziel, pflicht, status, fehler_anzahl)
    values (v_l, v_e, v_lz, true, 'fehler', 1)
    on conflict (lernender_id, einheit_id, lernziel) do update set status = 'fehler', pflicht = true, fehler_anzahl = 1;
    v_m := schule.lehrplan_matrix(array[v_l], false);
    if not (v_m->'lernstand'->v_l::text->v_t::text->>'fehler_offen')::boolean then raise exception 'FEHLER 6 fehler_offen nicht gesetzt'; end if;
    if (select count(*) from jsonb_each(v_m->'lernstand'->v_l::text) s where (s.value->>'fehler_offen')::boolean
          and not exists (select 1 from schule.lernziel_stand ls where ls.lernender_id = v_l and ls.einheit_id = schule.thema_einheit(s.key::bigint) and ls.pflicht and ls.status = 'fehler')) > 0 then
      raise exception 'FEHLER 6 fehler_offen ohne Fehler'; end if;
    raise notice 'ok 6 fehler_offen';
  end if;

  -- 7: leere Kinderliste (Eltern/Lehrer ohne aktives Kind) liefert Themen, aber keinen Lernstand
  v_m := schule.lehrplan_matrix('{}'::bigint[], false);
  if jsonb_array_length(v_m->'themen') = 0 or v_m->'lernstand' <> '{}'::jsonb or v_m->'kinder' <> '[]'::jsonb then raise exception 'FEHLER 7 ohne Kinder'; end if;
  raise notice 'ok 7 ohne Kinder';

  -- 8: Selbstprüfung Dreißigste Runde (NOTICE, kein Abbruch)
  -- 8a: kein Thema mit Klasse ohne Verbindung, außer ausdrücklich eigenständig (Spalte schule.thema.eigenstaendig, sobald es sie gibt)
  select count(*), string_agg(t.id::text, ',' order by t.id) into v_n, v_txt from schule.thema t
   where t.fach = 'Mathematik' and schule.thema_jahrgang(t.id) <> '{}'::jsonb
     and not exists (select 1 from schule.voraussetzung v where v.thema_id = t.id or v.braucht_id = t.id)
     and not coalesce((to_jsonb(t)->>'eigenstaendig')::boolean, false);
  raise notice '8a Themen mit Klasse ohne Verbindung und nicht eigenständig: % (%)', v_n, coalesce(v_txt, '–');
  -- 8b: keine Voraussetzung in einer späteren Klasse als das Thema (je Schulart, in der beide eine Klasse haben)
  select count(*), string_agg(distinct v.thema_id || '←' || v.braucht_id || ' ' || s.sa, ', ') into v_n, v_txt
    from schule.voraussetzung v cross join lateral (select k.sa from jsonb_object_keys(schule.thema_jahrgang(v.thema_id)) k(sa)) s
   where schule.thema_jahrgang(v.braucht_id) ? s.sa
     and (schule.thema_jahrgang(v.braucht_id)->>s.sa)::int > (schule.thema_jahrgang(v.thema_id)->>s.sa)::int;
  raise notice '8b Voraussetzung in späterer Klasse: % (%)', v_n, coalesce(v_txt, '–');
  -- 8c: Themen 100–103 verknüpft
  select count(*), string_agg(t.id::text, ',' order by t.id) into v_n, v_txt from schule.thema t
   where t.id between 100 and 103 and not exists (select 1 from schule.voraussetzung v where v.thema_id = t.id or v.braucht_id = t.id);
  raise notice '8c Themen 100–103 ohne Verbindung: % (%)', v_n, coalesce(v_txt, '–');

  raise notice 'LM-S Rauchtest durchgelaufen';
end $$;

rollback;
