-- Rauchtest LM-S (Stand LM-S 2: Raster + Detail). Nach 20261121_lm_s_lehrplan_matrix.sql ausführen (vor oder nach 20261121_lehrplan_zuordnung_voraussetzungen.sql).
-- Transaktion mit Rollback, nur Testkind, keine Namen in der Ausgabe.
-- Läuft über schule.lehrplan_matrix und schule.lehrplan_thema (die api-Aktionen rufen genau diese nach schule.lehrplan_sicht auf – ein Schlüssel gehört nicht in eine Datei).
-- Prüfungen 1–9 vergleichen mit den Tabellen selbst (keine festen Zahlen aus dem Bestand); Prüfung 6 legt sich „Fehler offen“ im Testkind selbst an,
-- Prüfung 9 setzt „eigenständig“ bei einem Thema selbst (nur wenn die Spalte schon da ist).
-- Prüfung 10 (Selbstprüfung Dreißigste Runde) meldet die Regeln als NOTICE mit Anzahl und Nummern – kein Abbruch. Soll eine Regel hart werden: NOTICE → EXCEPTION.
begin;

do $$
declare v_l bigint; v_m jsonb; v_k jsonb; v_d jsonb; v_dk jsonb; v_n int; v_soll int; v_th jsonb; v_e bigint; v_lz text; v_t bigint; v_txt text; v_spalte boolean;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  select exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'eigenstaendig') into v_spalte;

  v_m := schule.lehrplan_matrix(array[v_l], false);   -- Sicht Eltern/Lehrer (nur mit dem Testkind)
  v_k := schule.lehrplan_matrix(array[v_l], true);    -- Kindsicht

  -- 1: jedes Mathe-Thema genau einmal
  select count(*) into v_soll from schule.thema where fach = 'Mathematik';
  if jsonb_array_length(v_m->'themen') <> v_soll then raise exception 'FEHLER 1 Themen: % statt %', jsonb_array_length(v_m->'themen'), v_soll; end if;
  select count(distinct (x->>'thema_id')) into v_n from jsonb_array_elements(v_m->'themen') x;
  if v_n <> v_soll then raise exception 'FEHLER 1 Thema doppelt'; end if;
  raise notice 'ok 1 Themen je einmal (%)', v_soll;

  -- 2: Raster knapp: Pflichtfelder da, Detailfelder nicht da; ohne_flug genau dann, wenn keine freigegebene Einheit
  if exists (select 1 from jsonb_array_elements(v_m->'themen') x where not (x ? 'titel' and x ? 'gebiet_id' and x ? 'jahrgang' and x ? 'pflicht')) then
    raise exception 'FEHLER 2 Pflichtfeld fehlt (titel/gebiet_id/jahrgang/pflicht)'; end if;
  if exists (select 1 from jsonb_array_elements(v_m->'themen') x where x ?| array['lehrplan', 'merke', 'beispiel', 'etappen', 'was_gefordert', 'kurz']) then
    raise exception 'FEHLER 2 Detailfeld im Raster'; end if;
  if exists (select 1 from jsonb_array_elements(v_m->'themen') x where (x ? 'ohne_flug') <> (schule.thema_einheit((x->>'thema_id')::bigint) is null)
                                                                      or (x ? 'einheit_id') = (x ? 'ohne_flug')) then
    raise exception 'FEHLER 2 ohne_flug/einheit_id passt nicht zu schule.thema_einheit'; end if;
  if exists (select 1 from jsonb_array_elements(v_m->'themen') x where x ? 'einheit_id' and (x->>'etappen_anzahl')::int
               <> jsonb_array_length(coalesce((select e.inhalt->'etappen' from schule.einheit e where e.id = (x->>'einheit_id')::bigint), '[]'::jsonb))) then
    raise exception 'FEHLER 2 etappen_anzahl'; end if;
  select count(*) into v_n from jsonb_array_elements(v_m->'themen') x where x ? 'ohne_flug';
  raise notice 'ok 2 Raster knapp, ohne_flug bei % Themen', v_n;

  -- 3: Verbindungen = alle Mathe-Verbindungen aus schule.voraussetzung als [thema, braucht, h|e]
  select count(*) into v_soll from schule.voraussetzung v join schule.thema a on a.id = v.thema_id and a.fach = 'Mathematik' join schule.thema b on b.id = v.braucht_id and b.fach = 'Mathematik';
  if jsonb_array_length(v_m->'verbindungen') <> v_soll then raise exception 'FEHLER 3 Verbindungen: % statt %', jsonb_array_length(v_m->'verbindungen'), v_soll; end if;
  if exists (select 1 from jsonb_array_elements(v_m->'verbindungen') x where jsonb_array_length(x) <> 3 or x->>2 not in ('h', 'e')) then raise exception 'FEHLER 3 Form'; end if;
  if v_m->'verbindungen' <> v_k->'verbindungen' then raise exception 'FEHLER 3 Kindsicht andere Verbindungen'; end if;
  raise notice 'ok 3 Verbindungen (%)', v_soll;

  -- 4: Lernstand je Kind und Thema, knapp; Etappe x von y nur bei ▶
  if jsonb_array_length(v_m->'kinder') <> 1 or (v_m->'kinder'->0->>'id')::bigint <> v_l then raise exception 'FEHLER 4 Kinderliste'; end if;
  select count(*) into v_n from jsonb_object_keys(v_m->'lernstand'->v_l::text);
  if v_n <> jsonb_array_length(v_m->'themen') then raise exception 'FEHLER 4 Lernstand: % Themen statt %', v_n, jsonb_array_length(v_m->'themen'); end if;
  if exists (select 1 from jsonb_each(v_m->'lernstand'->v_l::text) s where not (s.value ? 'stufe') or s.value ?| array['etappen', 'gesetzt', 'ohne_test', 'wdh_stufe_min']
               or exists (select 1 from jsonb_each(s.value) f where f.value in ('null'::jsonb, 'false'::jsonb))) then raise exception 'FEHLER 4 Lernstand-Felder'; end if;
  if exists (select 1 from jsonb_each(v_m->'lernstand'->v_l::text) s where (s.value->>'stufe' = 'dran') <> (s.value ? 'etappe_jetzt')) then
    raise exception 'FEHLER 4 etappe_jetzt nur und immer bei Stufe dran'; end if;
  if exists (select 1 from jsonb_each(v_m->'lernstand'->v_l::text) s where s.value ? 'etappe_jetzt'
              and (s.value->>'etappe_jetzt')::int > greatest(coalesce((schule.thema_stufe(v_l, s.key::bigint)->>'etappen')::int, 1), 1)) then raise exception 'FEHLER 4 Etappe x größer als y'; end if;
  raise notice 'ok 4 Lernstand je Thema';

  -- 5: Kindsicht ohne Lehrer-Felder, mit Zeile; nur das Kind
  if exists (select 1 from jsonb_array_elements(v_k->'themen') x where x ?| array['lernbereich', 'jahrgang', 'pflicht', 'lehrplan_reihenfolge', 'eigenstaendig']) then
    raise exception 'FEHLER 5 Kindsicht enthält Lehrer-Felder'; end if;
  if exists (select 1 from jsonb_array_elements(v_k->'themen') x where not (x ? 'zeile')) then raise exception 'FEHLER 5 Kindsicht ohne Zeile'; end if;
  if (v_k->'kinder'->0) ? 'schulart' then raise exception 'FEHLER 5 Kindsicht mit Schulart'; end if;
  if exists (select 1 from jsonb_each(v_k->'lernstand'->v_l::text) s where s.value ? 'fehler_offen') then raise exception 'FEHLER 5 Kindsicht mit fehler_offen'; end if;
  if jsonb_array_length(v_k->'kinder') <> 1 or (select count(*) from jsonb_object_keys(v_k->'lernstand')) <> 1 then raise exception 'FEHLER 5 Kindsicht mit anderen Kindern'; end if;
  if jsonb_array_length(v_k->'themen') <> jsonb_array_length(v_m->'themen') then raise exception 'FEHLER 5 Kindsicht Themenzahl'; end if;
  raise notice 'ok 5 Kindsicht';

  -- 6: „Fehler offen“ – eine Pflicht-Etappe des Testkinds auf fehler setzen (Rollback nimmt es zurück)
  select t.id, e.id, p.lz into v_t, v_e, v_lz
    from schule.thema t join schule.einheit e on e.id = schule.thema_einheit(t.id)
    cross join lateral jsonb_array_elements_text(coalesce(e.inhalt->'bewertung'->'lernziele_pflicht', '[]'::jsonb)) p(lz)
   where t.fach = 'Mathematik' order by t.id limit 1;
  if v_e is null then raise notice 'übersprungen 6 (keine Einheit mit Pflicht-Etappe)';
  else
    insert into schule.lernziel_stand (lernender_id, einheit_id, lernziel, pflicht, status, fehler_anzahl)
    values (v_l, v_e, v_lz, true, 'fehler', 1)
    on conflict (lernender_id, einheit_id, lernziel) do update set status = 'fehler', pflicht = true, fehler_anzahl = 1;
    v_m := schule.lehrplan_matrix(array[v_l], false);
    if not coalesce((v_m->'lernstand'->v_l::text->v_t::text->>'fehler_offen')::boolean, false) then raise exception 'FEHLER 6 fehler_offen nicht gesetzt'; end if;
    if exists (select 1 from jsonb_each(v_m->'lernstand'->v_l::text) s where s.value ? 'fehler_offen'
          and not exists (select 1 from schule.lernziel_stand ls where ls.lernender_id = v_l and ls.einheit_id = schule.thema_einheit(s.key::bigint) and ls.pflicht and ls.status = 'fehler')) then
      raise exception 'FEHLER 6 fehler_offen ohne Fehler'; end if;
    raise notice 'ok 6 fehler_offen';
  end if;

  -- 7: Größe – Raster für Eltern/Lehrer mit allen aktiven Kindern (ohne Namen in der Ausgabe) deutlich unter 100 KB
  v_m := schule.lehrplan_matrix((select array_agg(l.id) from schule.lernender l where l.aktiv), false);
  v_n := length(v_m::text);
  if v_n >= 90000 then raise exception 'FEHLER 7 Raster zu groß: % Zeichen', v_n; end if;
  raise notice 'ok 7 Größe Raster Lehrer (alle aktiven Kinder): % Zeichen, Kindsicht: % Zeichen', v_n, length(v_k::text);
  v_m := schule.lehrplan_matrix('{}'::bigint[], false);
  if jsonb_array_length(v_m->'themen') = 0 or v_m->'lernstand' <> '{}'::jsonb or v_m->'kinder' <> '[]'::jsonb then raise exception 'FEHLER 7 ohne Kinder'; end if;

  -- 8: Detail eines Themas mit Einheit – Lehrer mit Wortlaut, merke, Etappen mit Pflicht, Beispiel, Verbindungen mit Begründung; Kind ohne Lehrer-Felder
  select t.id into v_t from schule.thema t where t.fach = 'Mathematik' and schule.thema_einheit(t.id) is not null
   order by (select count(*) from schule.voraussetzung v where v.thema_id = t.id) desc, t.id limit 1;
  v_d := schule.lehrplan_thema(v_t, false);
  v_dk := schule.lehrplan_thema(v_t, true);
  select to_jsonb(en) into v_th from schule.einheit en where en.id = schule.thema_einheit(v_t);
  if (v_d->'merke') is distinct from (v_th->'inhalt'->'merke') then raise exception 'FEHLER 8 merke'; end if;
  if jsonb_array_length(coalesce(v_d->'etappen', '[]'::jsonb)) <> jsonb_array_length(coalesce(v_th->'inhalt'->'etappen', '[]'::jsonb)) then raise exception 'FEHLER 8 Etappen'; end if;
  if exists (select 1 from jsonb_array_elements(v_d->'etappen') x where (x->>'pflicht')::boolean
               <> coalesce(v_th->'inhalt'->'bewertung'->'lernziele_pflicht', '[]'::jsonb) ? (x->>'lernziel')) then raise exception 'FEHLER 8 Pflicht der Etappen'; end if;
  if v_d ? 'beispiel' and length(v_d->>'beispiel') >= 160 then raise exception 'FEHLER 8 Beispiel zu lang'; end if;
  if (v_d->'lehrplan') is distinct from (select t.lehrplan from schule.thema t where t.id = v_t) then raise exception 'FEHLER 8 Lehrplan-Wortlaut'; end if;
  if jsonb_array_length(v_d->'braucht') <> (select count(*) from schule.voraussetzung v join schule.thema b on b.id = v.braucht_id and b.fach = 'Mathematik' where v.thema_id = v_t)
     or jsonb_array_length(v_d->'baut_darauf') <> (select count(*) from schule.voraussetzung v join schule.thema a on a.id = v.thema_id and a.fach = 'Mathematik' where v.braucht_id = v_t) then
    raise exception 'FEHLER 8 Verbindungen im Detail'; end if;
  if v_dk ?| array['lehrplan', 'eigenstaendig']
     or exists (select 1 from jsonb_array_elements(v_dk->'etappen') x where x ? 'pflicht')
     or exists (select 1 from jsonb_array_elements((v_dk->'braucht') || (v_dk->'baut_darauf')) x where x ? 'begruendung') then raise exception 'FEHLER 8 Kind-Detail mit Lehrer-Feldern'; end if;
  if (v_dk->'merke') is distinct from (v_d->'merke') then raise exception 'FEHLER 8 Kind-Detail ohne merke'; end if;
  if length(v_d::text) >= 30000 then raise exception 'FEHLER 8 Detail zu groß: %', length(v_d::text); end if;
  select t.id into v_t from schule.thema t where t.fach = 'Mathematik' and schule.thema_einheit(t.id) is null order by t.id limit 1;
  if v_t is not null and not coalesce((schule.lehrplan_thema(v_t, false)->>'ohne_flug')::boolean, false) then raise exception 'FEHLER 8 Detail ohne_flug'; end if;
  raise notice 'ok 8 Detail (Lehrer % Zeichen)', length(v_d::text);

  -- 9: eigenständig = Text (Begründung; null = nicht gekennzeichnet) – Raster: true, Detail: Text, Kind: nichts
  if not v_spalte then raise notice 'übersprungen 9 (Spalte schule.thema.eigenstaendig noch nicht da)';
  else
    select t.id into v_t from schule.thema t where t.fach = 'Mathematik' order by t.id limit 1;
    execute 'update schule.thema set eigenstaendig = $1 where id = $2' using 'Rauchtest LM-S: Begründung', v_t;
    v_m := schule.lehrplan_matrix(array[v_l], false);
    if not coalesce((select (x->>'eigenstaendig')::boolean from jsonb_array_elements(v_m->'themen') x where (x->>'thema_id')::bigint = v_t), false) then raise exception 'FEHLER 9 Raster'; end if;
    if schule.lehrplan_thema(v_t, false)->>'eigenstaendig' <> 'Rauchtest LM-S: Begründung' then raise exception 'FEHLER 9 Detail'; end if;
    if schule.lehrplan_thema(v_t, true) ? 'eigenstaendig' then raise exception 'FEHLER 9 Kind'; end if;
    execute 'update schule.thema set eigenstaendig = null where id = $1' using v_t;
    v_m := schule.lehrplan_matrix(array[v_l], false);
    if exists (select 1 from jsonb_array_elements(v_m->'themen') x where (x->>'thema_id')::bigint = v_t and x ? 'eigenstaendig') then raise exception 'FEHLER 9 null = nicht gekennzeichnet'; end if;
    raise notice 'ok 9 eigenständig als Text';
  end if;

  -- 10: Selbstprüfung Dreißigste Runde (NOTICE, kein Abbruch)
  -- 10a: kein Thema mit Klasse ohne Verbindung, außer eigenständig (Begründung gesetzt)
  select count(*), string_agg(t.id::text, ',' order by t.id) into v_n, v_txt from schule.thema t
   where t.fach = 'Mathematik' and schule.thema_jahrgang(t.id) <> '{}'::jsonb
     and not exists (select 1 from schule.voraussetzung v where v.thema_id = t.id or v.braucht_id = t.id)
     and to_jsonb(t)->>'eigenstaendig' is null;
  raise notice '10a Themen mit Klasse ohne Verbindung und nicht eigenständig: % (%)', v_n, coalesce(v_txt, '–');
  -- 10b: keine Voraussetzung in einer späteren Klasse als das Thema (je Schulart, in der beide eine Klasse haben)
  select count(*), string_agg(distinct v.thema_id || '←' || v.braucht_id || ' ' || s.sa, ', ') into v_n, v_txt
    from schule.voraussetzung v cross join lateral (select k.sa from jsonb_object_keys(schule.thema_jahrgang(v.thema_id)) k(sa)) s
   where schule.thema_jahrgang(v.braucht_id) ? s.sa
     and (schule.thema_jahrgang(v.braucht_id)->>s.sa)::int > (schule.thema_jahrgang(v.thema_id)->>s.sa)::int;
  raise notice '10b Voraussetzung in späterer Klasse: % (%)', v_n, coalesce(v_txt, '–');
  -- 10c: Themen 100–103 verknüpft
  select count(*), string_agg(t.id::text, ',' order by t.id) into v_n, v_txt from schule.thema t
   where t.id between 100 and 103 and not exists (select 1 from schule.voraussetzung v where v.thema_id = t.id or v.braucht_id = t.id);
  raise notice '10c Themen 100–103 ohne Verbindung: % (%)', v_n, coalesce(v_txt, '–');
  -- 10d (Teil A der Nachbesserung): keine Verbindung von oder zu einem Thema ohne freigegebene Einheit
  select count(*), string_agg(v.thema_id || '←' || v.braucht_id, ', ') into v_n, v_txt from schule.voraussetzung v
   where schule.thema_einheit(v.thema_id) is null or schule.thema_einheit(v.braucht_id) is null;
  raise notice '10d Verbindungen mit Thema ohne Flug: % (%)', v_n, coalesce(v_txt, '–');

  raise notice 'LM-S Rauchtest durchgelaufen';
end $$;

rollback;
