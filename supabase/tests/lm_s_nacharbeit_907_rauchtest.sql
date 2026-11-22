-- Rauchtest Nacharbeit 907, Teil LM-S (nach 20261121_lm_s_lehrplan_matrix.sql und 20261122_nacharbeit_907.sql).
-- Negative Tests über die api-Funktionen mit einem Lern-Zugang des Testkinds und einem Eltern-Zugang. Beide legt der Test in der Transaktion selbst an
-- (Name „Rauchtest“, zufälliger Sitzungs-Hash) – keine echten Schlüssel in der Datei; alles wird zurückgerollt.
-- Dazu: Größe mit octet_length, etappe_jetzt = erste noch nicht gelandete Etappe.
begin;

do $$
declare v_l bigint; v_fremd bigint; v_k text; v_ke text; v_login bigint; v_loge bigint; m jsonb; d jsonb; v_t bigint; v_fehler text; v_e bigint; v_lz text[]; v_n int;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  select id into v_fremd from schule.lernender where id <> v_l order by id limit 1;
  -- Zugänge nur für diesen Test
  insert into schule.lern_login (name, rolle, lernender_id, code_hash, angelegt_von) values ('Rauchtest', 'kind', v_l, 'rauchtest-' || gen_random_uuid(), 'rauchtest') returning id into v_login;
  insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) values (md5(random()::text) || md5(random()::text), v_login, now() + interval '1 hour') returning 'lern:' || token_hash into v_k;
  insert into schule.lern_login (name, rolle, lernender_id, code_hash, angelegt_von) values ('Rauchtest', 'eltern', null, 'rauchtest-' || gen_random_uuid(), 'rauchtest') returning id into v_loge;
  insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) values (md5(random()::text) || md5(random()::text), v_loge, now() + interval '1 hour') returning 'lern:' || token_hash into v_ke;
  select t.id into v_t from schule.thema t where t.fach = 'Mathematik' and schule.thema_einheit(t.id) is not null
   order by (select count(*) from schule.voraussetzung v where v.thema_id = t.id or v.braucht_id = t.id) desc, t.id limit 1;

  -- 1 Kind: nur es selbst, Kindsicht
  m := api.schule_lehrplan_matrix(v_k, '{}'::jsonb);
  if not (m->>'kindsicht')::boolean or jsonb_array_length(m->'kinder') <> 1 or (m->'kinder'->0->>'id')::bigint <> v_l
     or (select count(*) from jsonb_object_keys(m->'lernstand')) <> 1 or not (m->'lernstand' ? v_l::text) then raise exception 'FEHLER 1 Kind-Raster'; end if;
  if exists (select 1 from jsonb_array_elements(m->'themen') x where x ?| array['lernbereich', 'jahrgang', 'pflicht', 'lehrplan_reihenfolge', 'eigenstaendig']) then raise exception 'FEHLER 1 Lehrer-Felder'; end if;
  -- 2 fremde lernender_id wird ignoriert
  if v_fremd is not null then
    m := api.schule_lehrplan_matrix(v_k, jsonb_build_object('lernender_id', v_fremd));
    if not (m->>'kindsicht')::boolean or jsonb_array_length(m->'kinder') <> 1 or (m->'kinder'->0->>'id')::bigint <> v_l or m->'lernstand' ? v_fremd::text then
      raise exception 'FEHLER 2 fremde lernender_id'; end if;
  end if;
  -- 3 mit_testkind ändert für ein Kind nichts
  m := api.schule_lehrplan_matrix(v_k, '{"mit_testkind": true}'::jsonb);
  if not (m->>'kindsicht')::boolean or jsonb_array_length(m->'kinder') <> 1 then raise exception 'FEHLER 3 mit_testkind'; end if;
  -- 4 Detail als Kind (auch mit fremder lernender_id): ohne Lehrplan, eigenständig, Pflicht, Begründungen
  d := api.schule_lehrplan_thema(v_k, jsonb_build_object('thema_id', v_t, 'lernender_id', v_fremd));
  if not (d->>'kindsicht')::boolean or d ?| array['lehrplan', 'eigenstaendig']
     or exists (select 1 from jsonb_array_elements(coalesce(d->'etappen', '[]'::jsonb)) x where x ? 'pflicht')
     or exists (select 1 from jsonb_array_elements(coalesce(d->'braucht', '[]'::jsonb) || coalesce(d->'baut_darauf', '[]'::jsonb)) x where x ? 'begruendung') then
    raise exception 'FEHLER 4 Kind-Detail mit Lehrer-Feldern'; end if;
  raise notice 'ok 1–4 Lern-Zugang des Kindes: nur es selbst, fremde lernender_id und mit_testkind ohne Wirkung, Detail ohne Lehrer-Felder';

  -- 5 Eltern-Zugang: Lehrer-Sicht
  m := api.schule_lehrplan_matrix(v_ke, '{"mit_testkind": true}'::jsonb);
  d := api.schule_lehrplan_thema(v_ke, jsonb_build_object('thema_id', v_t));
  if (m->>'kindsicht')::boolean or (d->>'kindsicht')::boolean or not exists (select 1 from jsonb_array_elements(m->'kinder') x where (x->>'id')::bigint = v_l) then
    raise exception 'FEHLER 5 Eltern-Zugang'; end if;
  raise notice 'ok 5 Eltern-Zugang: Lehrer-Sicht (mit Testkind auf Wunsch)';

  -- 6 Größe (Bytes): Lehrer mit allen aktiven Kindern und Testkind, Kindsicht, Detail
  if octet_length(m::text) >= 90000 then raise exception 'FEHLER 6 Raster Lehrer zu groß: % Bytes', octet_length(m::text); end if;
  if octet_length(api.schule_lehrplan_matrix(v_k, '{}'::jsonb)::text) >= 90000 then raise exception 'FEHLER 6 Raster Kind zu groß'; end if;
  if octet_length(d::text) >= 30000 then raise exception 'FEHLER 6 Detail zu groß'; end if;
  raise notice 'ok 6 Größe: Lehrer % Bytes, Kind % Bytes, Detail % Bytes', octet_length(m::text), octet_length(api.schule_lehrplan_matrix(v_k, '{}'::jsonb)::text), octet_length(d::text);

  -- 7 gesperrter Zugang, abgelaufene Sitzung
  update schule.lern_login set aktiv = false where id = v_login;
  begin
    m := api.schule_lehrplan_matrix(v_k, '{}'::jsonb); v_fehler := 'kein Fehler';
  exception when others then v_fehler := sqlerrm; end;
  if v_fehler = 'kein Fehler' then raise exception 'FEHLER 7 gesperrter Zugang sieht das Raster'; end if;
  begin
    d := api.schule_lehrplan_thema(v_k, jsonb_build_object('thema_id', v_t)); v_fehler := 'kein Fehler';
  exception when others then v_fehler := sqlerrm; end;
  if v_fehler = 'kein Fehler' then raise exception 'FEHLER 7 gesperrter Zugang sieht das Detail'; end if;
  update schule.lern_login set aktiv = true where id = v_login;
  update schule.lern_sitzung set laeuft_ab = now() - interval '1 minute' where login_id = v_login;
  begin
    m := api.schule_lehrplan_matrix(v_k, '{}'::jsonb); v_fehler := 'kein Fehler';
  exception when others then v_fehler := sqlerrm; end;
  if v_fehler = 'kein Fehler' then raise exception 'FEHLER 7 abgelaufene Sitzung sieht das Raster'; end if;
  raise notice 'ok 7 gesperrter Zugang und abgelaufene Sitzung: abgewiesen (%)', v_fehler;

  -- 8 etappe_jetzt = erste noch nicht gelandete Etappe in Reihenfolge
  select e.id into v_e from schule.einheit e where e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id)
     and jsonb_array_length(coalesce(e.inhalt->'etappen', '[]'::jsonb)) >= 3 order by e.id limit 1;
  if v_e is null then raise exception 'FEHLER 8 Vorbereitung: kein Flug mit 3 Etappen'; end if;
  select array_agg(et.x->>'lernziel' order by et.nr) into v_lz from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') with ordinality et(x, nr) where e.id = v_e;
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel) select v_l, v_e, z from unnest(v_lz) z on conflict do nothing;
  update schule.karte_stand set sitzt = (lernziel <> v_lz[2]) where lernender_id = v_l and einheit_id = v_e;   -- 1 gelandet, 2 offen, 3… gelandet
  if schule.etappe_jetzt(v_l, v_e) <> 2 then raise exception 'FEHLER 8 etappe_jetzt %, erwartet 2', schule.etappe_jetzt(v_l, v_e); end if;
  update schule.karte_stand set sitzt = true where lernender_id = v_l and einheit_id = v_e;
  if schule.etappe_jetzt(v_l, v_e) is not null then raise exception 'FEHLER 8 alle gelandet, trotzdem %', schule.etappe_jetzt(v_l, v_e); end if;
  update schule.karte_stand set sitzt = false where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[1];
  if schule.etappe_jetzt(v_l, v_e) <> 1 then raise exception 'FEHLER 8 erste offen'; end if;
  -- im Raster: wo etappe_jetzt steht, ist die Stufe „dran“ und der Wert = schule.etappe_jetzt
  m := schule.lehrplan_matrix(array[v_l], false);
  select count(*) into v_n from jsonb_each(m->'lernstand'->v_l::text) s
   where (s.value ? 'etappe_jetzt' and (s.value->>'stufe' <> 'dran' or (s.value->>'etappe_jetzt')::int is distinct from schule.etappe_jetzt(v_l, schule.thema_einheit(s.key::bigint))))
      or (s.value->>'stufe' = 'dran' and not s.value ? 'etappe_jetzt' and schule.etappe_jetzt(v_l, schule.thema_einheit(s.key::bigint)) is not null);
  if v_n > 0 then raise exception 'FEHLER 8 Raster: % Themen mit falschem etappe_jetzt', v_n; end if;
  raise notice 'ok 8 etappe_jetzt = erste noch nicht gelandete Etappe (2; alle gelandet → keine; 1)';
end $$;

rollback;
