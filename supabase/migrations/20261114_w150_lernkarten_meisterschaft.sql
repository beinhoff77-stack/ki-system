-- W150 (Claude): Lernkarten mit Meisterschaft und Wiederholung.
-- Lernkarte = Lernziel einer Einheit. „Sitzt“, wenn die letzten N Übungsaufgaben ohne Tipp richtig waren (N = 4, bei kleinen Vorräten weniger).
-- Danach Wiederholung nach 1, 3, 7, 14, 30 Tagen; ein Fehler setzt die Karte zurück auf „üben“.

alter table schule.aufgabe add column if not exists freigegeben boolean not null default true;

create table if not exists schule.karte_stand (
  lernender_id bigint not null references schule.lernender(id) on delete cascade,
  einheit_id bigint not null references schule.einheit(id),
  lernziel text not null,
  serie smallint not null default 0,
  richtig int not null default 0,
  falsch int not null default 0,
  sitzt boolean not null default false,
  sitzt_am timestamptz,
  wdh_stufe smallint not null default 0,
  faellig_am timestamptz,
  zuletzt timestamptz,
  primary key (lernender_id, einheit_id, lernziel)
);
alter table schule.karte_stand enable row level security;
revoke all on schule.karte_stand from public, anon, authenticated;

create or replace function schule.karte_ziel(p_einheit bigint, p_lz text) returns int
language sql stable set search_path to '' as $$
  select least(4, greatest(2, count(*)))::int from schule.aufgabe a
   where a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben;
$$;

create or replace function schule.karte_buchen(p_l bigint, p_aufgabe bigint, p_richtig boolean, p_hilfe smallint, p_zeit timestamptz) returns void
language plpgsql set search_path to '' as $$
declare a schule.aufgabe; k schule.karte_stand; v_ziel int;
  v_abst interval[] := array[interval '1 day', interval '3 days', interval '7 days', interval '14 days', interval '30 days'];
begin
  select * into a from schule.aufgabe where id = p_aufgabe;
  if a.id is null or a.pool <> 'uebung' then return; end if;
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) values (p_l, a.einheit_id, a.variante_gruppe) on conflict do nothing;
  select * into k from schule.karte_stand where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe for update;
  v_ziel := schule.karte_ziel(a.einheit_id, a.variante_gruppe);
  if p_richtig then k.richtig := k.richtig + 1; else k.falsch := k.falsch + 1; end if;
  if not k.sitzt then
    if not p_richtig then k.serie := 0;
    elsif coalesce(p_hilfe, 0) = 0 then k.serie := k.serie + 1;   -- mit Tipp richtig: zählt nicht für die Serie, bricht sie aber nicht
    end if;
    if k.serie >= v_ziel then
      k.sitzt := true; k.sitzt_am := p_zeit; k.wdh_stufe := 0; k.faellig_am := p_zeit + v_abst[1];
    end if;
  else
    if not p_richtig then
      k.sitzt := false; k.serie := 0; k.wdh_stufe := 0; k.faellig_am := null;
    elsif k.faellig_am is null or k.faellig_am <= p_zeit then
      k.wdh_stufe := least(k.wdh_stufe + 1, 4); k.faellig_am := p_zeit + v_abst[k.wdh_stufe + 1];
    end if;
  end if;
  update schule.karte_stand set serie = k.serie, richtig = k.richtig, falsch = k.falsch, sitzt = k.sitzt, sitzt_am = k.sitzt_am,
    wdh_stufe = k.wdh_stufe, faellig_am = k.faellig_am, zuletzt = p_zeit
   where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;
end $$;

create or replace function schule.versuch_karte() returns trigger
language plpgsql set search_path to '' as $$
begin
  if new.testsitzung_id is null then perform schule.karte_buchen(new.lernender_id, new.aufgabe_id, new.richtig, new.hilfe, now()); end if;
  return new;
end $$;
drop trigger if exists versuch_karte on schule.versuch;
create trigger versuch_karte after insert on schule.versuch for each row execute function schule.versuch_karte();

-- Bisherige Übungsversuche nachbuchen (in zeitlicher Reihenfolge), dann im Test nachgewiesene Lernziele als „sitzt, gleich wiederholen“ übernehmen.
do $$
declare r record;
begin
  for r in select x.lernender_id, x.aufgabe_id, x.richtig, x.hilfe, x.am from schule.versuch x where x.testsitzung_id is null order by x.id loop
    perform schule.karte_buchen(r.lernender_id, r.aufgabe_id, r.richtig, r.hilfe, coalesce(r.am, now()));
  end loop;
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) select s.lernender_id, s.einheit_id, s.lernziel from schule.lernziel_stand s
   where s.status in ('nachgewiesen','korrigiert','gesichert') on conflict do nothing;
  update schule.karte_stand k set sitzt = true, sitzt_am = coalesce(k.sitzt_am, now()), wdh_stufe = 0, faellig_am = now()
   where not k.sitzt and exists (select 1 from schule.lernziel_stand s where s.lernender_id = k.lernender_id and s.einheit_id = k.einheit_id
     and s.lernziel = k.lernziel and s.status in ('nachgewiesen','korrigiert','gesichert'));
end $$;

-- Etappen-/Kartenstand: fertig = sitzt oder im Test nachgewiesen.
create or replace function schule.etappen_stand(p_lernender bigint, p_einheit bigint) returns jsonb
language sql stable set search_path to '' as $$
  select coalesce(jsonb_object_agg(z.lz, jsonb_build_object('geloest', z.geloest, 'gesamt', z.gesamt,
           'serie', coalesce(k.serie, 0), 'ziel', schule.karte_ziel(p_einheit, z.lz), 'sitzt', coalesce(k.sitzt, false),
           'faellig', coalesce(k.sitzt and k.faellig_am <= now(), false), 'wdh_stufe', coalesce(k.wdh_stufe, 0),
           'fertig', coalesce(k.sitzt, false) or coalesce(s.status in ('nachgewiesen','korrigiert','gesichert'), false))), '{}'::jsonb)
  from (select e->>'lernziel' lz,
          (select count(*) from schule.aufgabe a where a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = e->>'lernziel' and a.freigegeben) gesamt,
          (select count(distinct v.aufgabe_id) from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
             where v.lernender_id = p_lernender and v.richtig and v.testsitzung_id is null and a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = e->>'lernziel') geloest
        from schule.einheit x, jsonb_array_elements(coalesce(x.inhalt->'etappen', '[]'::jsonb)) e where x.id = p_einheit) z
  left join schule.lernziel_stand s on s.lernender_id = p_lernender and s.einheit_id = p_einheit and s.lernziel = z.lz
  left join schule.karte_stand k on k.lernender_id = p_lernender and k.einheit_id = p_einheit and k.lernziel = z.lz;
$$;

-- Übungen mit eigenem Stand je Aufgabe; neue (noch nicht freigegebene) Aufgaben nur fürs Testkind.
do $$
declare d text;
begin
  select pg_get_functiondef('schule.einheit_lesen_intern'::regproc) into d;
  d := replace(d, $x$select coalesce(jsonb_agg(schule.aufgabe_anzeige(a, true) order by a.reihenfolge), '[]') into v_ueb
    from schule.aufgabe a where a.einheit_id = p_einheit and a.pool = 'uebung';$x$,
  $x$select coalesce(jsonb_agg(schule.aufgabe_anzeige(a, true) || jsonb_build_object(
      'versuche', (select count(*) from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id and v.testsitzung_id is null),
      'geloest', exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id and v.testsitzung_id is null and v.richtig))
      order by a.stufe nulls last, a.reihenfolge), '[]') into v_ueb
    from schule.aufgabe a where a.einheit_id = p_einheit and a.pool = 'uebung'
     and (a.freigegeben or exists (select 1 from schule.lernender l where l.id = p_lernender and l.ist_test));$x$);
  if position('geloest' in d) = 0 then raise exception 'einheit_lesen_intern nicht angepasst'; end if;
  execute d;

  select pg_get_functiondef('schule.uebung_pruefen_intern'::regproc) into d;
  d := replace(d, $x$  return jsonb_build_object('ok', true, 'format_ok', true, 'richtig', (b->>'richtig')::boolean, 'loesung', a.loesung, 'loesungsweg', a.loesungsweg);$x$,
  $x$  return jsonb_build_object('ok', true, 'format_ok', true, 'richtig', (b->>'richtig')::boolean, 'loesung', a.loesung, 'loesungsweg', a.loesungsweg,
    'karte', (select jsonb_build_object('serie', k.serie, 'ziel', schule.karte_ziel(k.einheit_id, k.lernziel), 'sitzt', k.sitzt,
                'neu_sitzt', k.sitzt and k.sitzt_am >= now() - interval '5 seconds' and k.wdh_stufe = 0, 'wdh_stufe', k.wdh_stufe)
              from schule.karte_stand k where k.lernender_id = p_lernender and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe));$x$);
  d := replace(d, $x$  if a.id is null or a.pool <> 'uebung' then raise exception 'Keine Übungsaufgabe' using errcode = 'P0001'; end if;$x$,
  $x$  if a.id is null or a.pool <> 'uebung' then raise exception 'Keine Übungsaufgabe' using errcode = 'P0001'; end if;
  if not a.freigegeben and not exists (select 1 from schule.lernender l where l.id = p_lernender and l.ist_test) then
    raise exception 'Diese Aufgabe ist noch nicht freigegeben' using errcode = 'P0001';
  end if;$x$);
  if position('''karte''' in d) = 0 or position('noch nicht freigegeben' in d) = 0 then raise exception 'uebung_pruefen_intern nicht angepasst'; end if;
  execute d;

  select pg_get_functiondef('api.schule_merkheft(text, jsonb)'::regprocedure) into d;
  d := replace(d, $x$'etappen', e.inhalt->'etappen', $x$, $x$'etappen', e.inhalt->'etappen', 'abschnitte', e.inhalt->'abschnitte', $x$);
  if position('abschnitte' in d) = 0 then raise exception 'merkheft nicht angepasst'; end if;
  execute d;
end $$;

-- Wiederholung: fällige Karten (sitzt, Termin erreicht), je Karte eine Übungsaufgabe, die das Kind am seltensten gesehen hat.
create or replace function api.schule_wiederholung(p_schluessel text, p_daten jsonb) returns jsonb
language plpgsql security definer set search_path to '' as $$
declare v_l bigint := (p_daten->>'lernender_id')::bigint; v_n int := least(coalesce(nullif(p_daten->>'anzahl','')::int, 3), 6);
  v_test boolean; v_leiter boolean; v_erg jsonb;
begin
  perform schule.zugriff(p_schluessel, v_l);
  select ist_test into v_test from schule.lernender where id = v_l;
  v_leiter := schule.ist_leiter(p_schluessel);
  select coalesce(jsonb_agg(x.j order by x.faellig_am), '[]'::jsonb) into v_erg from (
    select k.faellig_am, schule.aufgabe_anzeige(a, true) || jsonb_build_object('einheit_id', k.einheit_id, 'stadt', b.stadt,
             'etappe', (select et->>'titel' from jsonb_array_elements(e.inhalt->'etappen') et where et->>'lernziel' = k.lernziel limit 1)) j
      from schule.karte_stand k join schule.einheit e on e.id = k.einheit_id join schule.block b on b.id = e.block_id
      cross join lateral (select a.* from schule.aufgabe a where a.einheit_id = k.einheit_id and a.pool = 'uebung' and a.variante_gruppe = k.lernziel
                            and (a.freigegeben or coalesce(v_test, false))
                          order by (select count(*) from schule.versuch vs where vs.lernender_id = v_l and vs.aufgabe_id = a.id), random() limit 1) a
     where k.lernender_id = v_l and k.sitzt and k.faellig_am <= now()
       and (e.status in ('geprueft','freigegeben') or (e.status = 'entwurf' and coalesce(v_test, false) and v_leiter))
     order by k.faellig_am limit v_n) x;
  return jsonb_build_object('ok', true, 'aufgaben', v_erg,
    'faellig', (select count(*) from schule.karte_stand k where k.lernender_id = v_l and k.sitzt and k.faellig_am <= now()));
end $$;
grant execute on function api.schule_wiederholung(text, jsonb) to council_mcp;
revoke all on function api.schule_wiederholung(text, jsonb) from public, anon, authenticated;
