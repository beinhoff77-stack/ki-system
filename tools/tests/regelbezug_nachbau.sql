-- RB-S: kleiner NACHBAU der Datenbank für den lokalen Test (tools/tests/regelbezug_sql_test.py, leere lokale Postgres-Instanz).
-- Nur die Teile, die RB-S berührt; Spalten und Funktionsstellen so, wie die Migrationen im Repo sie beschreiben. NICHT die echte Datenbank:
-- schule.antwort_bewerten kommt aus 20261116_w150_r2_fehlermuster_zweiter_versuch.sql (der Test hängt sie an), uebung_pruefen_intern ist eine
-- verkürzte Fassung mit genau den Stellen, die BD-S2 hinterlassen hat (vier endgültige Rückgaben, erster Fehlversuch, zwei Wiederholungen).
create role anon nologin;
create role authenticated nologin;
create schema schule;
create table schule.lernender (id bigserial primary key, ist_test boolean not null default false);
create table schule.thema (id bigint primary key, schluessel text not null unique);
create table schule.einheit (id bigint primary key, thema_id bigint references schule.thema(id), status text not null default 'freigegeben', inhalt jsonb default '{}');
create table schule.aufgabe (
  id bigserial primary key, einheit_id bigint references schule.einheit(id), thema_id bigint, teilfaehigkeit text, art text default 'uebung', stufe smallint,
  variante_gruppe text, antworttyp text not null, frage jsonb not null, antworten jsonb, loesung jsonb, tipp text, loesungsweg text, punkte_max int default 1,
  reihenfolge int, pool text not null default 'uebung', freigegeben boolean not null default true, typ text, form text, zaehlt text, expedition_id bigint, teil text);
create table schule.versuch (
  id bigserial primary key, lernender_id bigint not null references schule.lernender(id), aufgabe_id bigint not null references schule.aufgabe(id), client_id text,
  antwort jsonb, richtig boolean not null, punkte int, punkte_max int, hilfe smallint, versuch_nr int, anlauf smallint, testsitzung_id bigint,
  misch boolean not null default false, am timestamptz not null default now(), unique (lernender_id, client_id));
alter table schule.aufgabe enable row level security;
alter table schule.versuch enable row level security;
grant usage on schema schule to anon, authenticated;

create or replace function schule.aufgabe_schutz() returns trigger language plpgsql as $function$
begin
  if coalesce(new.pool, old.pool) = 'expedition' and coalesce(old.pool, new.pool) = 'expedition' then return coalesce(new, old); end if;
  if exists (select 1 from schule.einheit e where e.id = coalesce(old.einheit_id, new.einheit_id) and e.status = 'freigegeben') then
    raise exception 'Aufgaben einer freigegebenen Einheit sind unveränderlich';
  end if;
  return coalesce(new, old);
end $function$;
create trigger aufgabe_schutz before update or delete on schule.aufgabe for each row execute function schule.aufgabe_schutz();

create or replace function schule.loesung_sicht(a schule.aufgabe) returns jsonb language sql immutable set search_path to '' as $$ select a.loesung $$;
create or replace function schule.aufgabe_zaehlt(a schule.aufgabe) returns boolean language sql immutable set search_path to '' as $$ select a.zaehlt is distinct from 'nein' $$;

-- verkürzt: Bewertung, Versuch speichern, Rückgaben an den Stellen wie nach BD-S2 (vier endgültige Rückgaben: bonus, misch, expedition, übung)
create or replace function schule.uebung_pruefen_intern(p_lernender bigint, p_daten jsonb)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare a schule.aufgabe; b jsonb; v_cid text := coalesce(nullif(p_daten->>'client_id',''), 'srv:' || gen_random_uuid()); v_alt schule.versuch;
  v_anlauf smallint := case p_daten->>'anlauf' when '1' then 1 when '2' then 2 end; v_ri boolean;
begin
  select * into a from schule.aufgabe where id = (p_daten->>'aufgabe_id')::bigint;
  if a.id is null or a.pool not in ('uebung', 'bonus', 'expedition') then raise exception 'Keine Übungsaufgabe' using errcode = 'P0001'; end if;
  if p_daten ? 'client_id' then
    select * into v_alt from schule.versuch where lernender_id = p_lernender and client_id = v_cid;
    if v_alt.id is not null then
      if v_alt.aufgabe_id is distinct from a.id then raise exception 'Diese Antwort gehört zu einer anderen Aufgabe' using errcode = 'P0001'; end if;
      b := case when a.antworttyp = 'bedingung' and not v_alt.richtig then schule.antwort_bewerten(a, v_alt.antwort) end; -- BD-S2: Rückmeldung aus dem gespeicherten Versuch
      if coalesce(v_alt.anlauf, 0) = 1 and not v_alt.richtig then
        return jsonb_strip_nulls(jsonb_build_object('ok', true, 'format_ok', true, 'richtig', false, 'nochmal', true, 'wiederholt', true, 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis'));
      end if;
      return jsonb_build_object('ok', true, 'format_ok', true, 'richtig', v_alt.richtig, 'loesung', schule.loesung_sicht(a), 'loesungsweg', a.loesungsweg, 'wiederholt', true) || jsonb_strip_nulls(jsonb_build_object('verletzt', b->>'verletzt', 'hinweis', b->>'hinweis'));
    end if;
  end if;
  b := schule.antwort_bewerten(a, p_daten->'antwort');
  if not (b->>'format_ok')::boolean then
    return jsonb_build_object('ok', true, 'format_ok', false, 'hinweis', b->>'hinweis');
  end if;
  v_ri := (b->>'richtig')::boolean;
  insert into schule.versuch(lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf, misch)
  values (p_lernender, a.id, v_cid, p_daten->'antwort', v_ri, case when v_ri then 1 else 0 end, 1, 0,
          (select count(*) + 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id), v_anlauf, coalesce((p_daten->>'misch')::boolean, false));
  if a.pool = 'bonus' then
    return jsonb_strip_nulls(jsonb_build_object('ok', true, 'format_ok', true, 'richtig', v_ri, 'bonus', true, 'grund', b->>'grund', 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis', 'loesung', schule.loesung_sicht(a), 'loesungsweg', a.loesungsweg));
  end if;
  if coalesce((p_daten->>'misch')::boolean, false) then
    return jsonb_strip_nulls(jsonb_build_object('ok', true, 'format_ok', true, 'richtig', v_ri, 'misch', true, 'grund', b->>'grund', 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis', 'loesung', schule.loesung_sicht(a), 'loesungsweg', a.loesungsweg));
  end if;
  if a.pool = 'expedition' then
    return jsonb_strip_nulls(jsonb_build_object('ok', true, 'format_ok', true, 'richtig', v_ri, 'expedition', true, 'grund', b->>'grund', 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis', 'loesung', schule.loesung_sicht(a), 'loesungsweg', a.loesungsweg));
  end if;
  if v_anlauf = 1 and not v_ri then
    return jsonb_strip_nulls(jsonb_build_object('ok', true, 'format_ok', true, 'richtig', false, 'nochmal', true, 'grund', b->>'grund', 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis'));
  end if;
  return jsonb_strip_nulls(jsonb_build_object('ok', true, 'format_ok', true, 'richtig', v_ri, 'grund', b->>'grund', 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis', 'loesung', schule.loesung_sicht(a), 'loesungsweg', a.loesungsweg,
    'karte', null));
end $function$;
create or replace function schule.uebung_pruefen_wd(p_l bigint, p_daten jsonb) returns jsonb language plpgsql set search_path to '' as $$
begin return schule.uebung_pruefen_intern(p_l, p_daten); end $$;
create or replace function schule.aufgabe_anzeige(a schule.aufgabe, p_mit_tipp boolean) returns jsonb language sql stable set search_path to '' as $$
  select jsonb_build_object('id', a.id, 'antworttyp', a.antworttyp, 'frage', a.frage, 'antworten', a.antworten, 'einheit', a.loesung->>'einheit', 'tipp', case when p_mit_tipp then a.tipp end) $$;
insert into schule.lernender (ist_test) values (true), (false);
