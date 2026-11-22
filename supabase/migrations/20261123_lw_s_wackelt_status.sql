-- LW-S (22.11.): Server für LW-3 „Was wackelt“ als Arbeitsliste (inhalte/AUFTRAEGE.md „Bau-Auftrag LW – ‚Unser Lehrplan‘“, Abschnitt LW-S;
-- Vorgabe inhalte/pruefung/lehrer/werkstatt/umsetzung.md, Abschnitt 1a). Unabhängig von LK-S und den WD/FP-Dateien; braucht LA-3 (schule.besprochen).
--   1. Tabelle schule.wackelt_status: gespeicherter Status je Kind und Thema – bei Bedarf je Etappe (einheit_id + lernziel) –
--      'zu_besprechen' | 'beobachten' | 'besprochen', mit Zeitpunkt (am) und wer (von).
--   2. Wirksamer Status: Gibt es nach dem gespeicherten Zeitpunkt eine neue endgültig falsche Antwort im selben Thema (bzw. in der Etappe),
--      ist der Eintrag wieder 'zu_besprechen' (wieder_offen = true). Das wird beim Lesen ausgewertet – kein Trigger im Antwortweg, nichts wird
--      beim Antworten geschrieben. „Endgültig falsch“ wie LA-3: falsch, außer dem 1. Versuch mit zweiter Chance außerhalb eines Tests.
--   3. Ohne gespeicherten Status (Vorgabe, damit die Liste ab dem ersten Tag stimmt): 'zu_besprechen', wenn eine Etappe des Eintrags wackelt
--      (wie in der App: nicht gelandet und wieder offen, oder mindestens 3 falsche und mehr falsche als richtige) und nicht als besprochen
--      markiert ist (LA-3); 'besprochen', wenn alle Etappen mit Fehlern als besprochen markiert sind (LA-3); sonst 'beobachten'.
--   4. Aktionen (nur Eltern/Lehrer, Zugriff auf das Kind wird geprüft):
--      api.schule_wackelt_lesen {lernender_id} → {ok, lernender_id, zu_besprechen (Zahl für den Reiter), eintraege [...]}
--      api.schule_wackelt_setzen {lernender_id, thema_id, status, einheit_id?, lernziel?} → {ok, eintrag, zu_besprechen}
-- Kein DROP, kein DELETE. Lernstand, Stufen, Plan, Sterne bleiben unverändert (am Ende geprüft). Wiederholt ausführbar.

create temp table if not exists lw_vorher (t text, s text) on commit drop;
truncate lw_vorher; -- nur die Hilfstabelle dieser Sitzung
insert into lw_vorher
  select 'karte', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x
  union all select 'lernziel', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x
  union all select 'sterne', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x
  union all select 'route', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.route x
  union all select 'lernender', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernender x;

-- 1. gespeicherter Status
create table if not exists schule.wackelt_status (
  lernender_id bigint not null references schule.lernender(id),
  thema_id bigint not null references schule.thema(id),
  einheit_id bigint references schule.einheit(id),
  lernziel text,
  bezug text generated always as (case when einheit_id is null then '' else einheit_id::text || ':' || lernziel end) stored,
  status text not null,
  am timestamptz not null default now(),
  von text not null,
  primary key (lernender_id, thema_id, bezug),
  constraint wackelt_status_status_check check (status in ('zu_besprechen', 'beobachten', 'besprochen')),
  constraint wackelt_status_etappe_check check ((einheit_id is null) = (lernziel is null))
);
alter table schule.wackelt_status enable row level security; -- nur über die api-Funktionen (security definer), wie die übrigen schule-Tabellen
comment on table schule.wackelt_status is 'LW-S: „Was wackelt“ – Status je Kind und Thema (bezug = '''') oder je Etappe (bezug = einheit_id:lernziel); neue endgültig falsche Antworten danach machen den Eintrag beim Lesen wieder „zu besprechen“';

-- endgültig falsche Antworten eines Kindes im Thema (oder in einer Etappe), optional erst nach einem Zeitpunkt
create or replace function schule.wackelt_fehler(p_l bigint, p_thema bigint, p_e bigint, p_lz text, p_seit timestamptz default null)
 returns table (anzahl bigint, zuletzt timestamptz) language sql stable set search_path to ''
as $function$
  select count(*), max(v.am)
    from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id join schule.einheit e on e.id = a.einheit_id
   where v.lernender_id = p_l and e.thema_id = p_thema and not v.richtig
     and not (coalesce(v.anlauf, 0) = 1 and v.testsitzung_id is null)            -- wie LA-3: 1. Versuch mit zweiter Chance zählt nicht
     and (p_e is null or (a.einheit_id = p_e and a.variante_gruppe = p_lz))
     and (p_seit is null or v.am > p_seit);
$function$;
revoke all on function schule.wackelt_fehler(bigint, bigint, bigint, text, timestamptz) from public, anon, authenticated;

-- 2./3. Arbeitsliste eines Kindes: ein Eintrag je Thema mit Fehlern; Etappen mit eigenem Status sind eigene Einträge
create or replace function schule.wackelt_liste(p_l bigint)
 returns jsonb language sql stable set search_path to ''
as $function$
  with fe as (   -- Etappen mit endgültig falschen Antworten
    select e.thema_id, a.einheit_id, a.variante_gruppe lernziel, count(*) fehler, max(v.am) zuletzt
      from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id join schule.einheit e on e.id = a.einheit_id
     where v.lernender_id = p_l and not v.richtig and not (coalesce(v.anlauf, 0) = 1 and v.testsitzung_id is null)
     group by 1, 2, 3),
  et as (        -- dazu Lage der Etappe
    select fe.*, coalesce(k.sitzt, false) sitzt,
           not coalesce(k.sitzt, false) and (k.sitzt_am is not null or (coalesce(k.falsch, 0) >= 3 and coalesce(k.falsch, 0) > coalesce(k.richtig, 0))) wackelt,
           (schule.besprochen_aktiv(p_l, fe.einheit_id, fe.lernziel)).am besprochen_am,
           (select q->>'titel' from schule.einheit x, jsonb_array_elements(coalesce(x.inhalt->'etappen', '[]'::jsonb)) q
             where x.id = fe.einheit_id and q->>'lernziel' = fe.lernziel limit 1) titel,
           exists (select 1 from schule.wackelt_status s where s.lernender_id = p_l and s.thema_id = fe.thema_id
                    and s.einheit_id = fe.einheit_id and s.lernziel = fe.lernziel) eigen
      from fe left join schule.karte_stand k on k.lernender_id = p_l and k.einheit_id = fe.einheit_id and k.lernziel = fe.lernziel),
  ein as (       -- Einträge: Thema (Etappen ohne eigenen Status) und Etappen mit eigenem Status; dazu gespeicherte ohne Fehler
    select thema_id, null::bigint einheit_id, null::text lernziel from et where not eigen
    union select s.thema_id, null, null from schule.wackelt_status s where s.lernender_id = p_l and s.bezug = ''
    union select s.thema_id, s.einheit_id, s.lernziel from schule.wackelt_status s where s.lernender_id = p_l and s.bezug <> ''),
  z as (
    select i.*, s.status s_status, s.am s_am, s.von s_von,
           (select jsonb_agg(jsonb_build_object('einheit_id', et.einheit_id, 'lernziel', et.lernziel, 'titel', et.titel, 'fehler', et.fehler,
                     'letzter_fehler_am', et.zuletzt, 'wackelt', et.wackelt, 'sitzt', et.sitzt, 'besprochen_am', et.besprochen_am) order by et.zuletzt desc)
              from et where et.thema_id = i.thema_id and (case when i.einheit_id is null then not et.eigen else et.einheit_id = i.einheit_id and et.lernziel = i.lernziel end)) etappen,
           (select coalesce(sum(et.fehler), 0) from et where et.thema_id = i.thema_id
               and (case when i.einheit_id is null then not et.eigen else et.einheit_id = i.einheit_id and et.lernziel = i.lernziel end)) fehler,
           (select max(et.zuletzt) from et where et.thema_id = i.thema_id
               and (case when i.einheit_id is null then not et.eigen else et.einheit_id = i.einheit_id and et.lernziel = i.lernziel end)) zuletzt,
           (select bool_or(et.wackelt and et.besprochen_am is null) from et where et.thema_id = i.thema_id
               and (case when i.einheit_id is null then not et.eigen else et.einheit_id = i.einheit_id and et.lernziel = i.lernziel end)) offen_wackelt,
           (select bool_and(et.besprochen_am is not null) from et where et.thema_id = i.thema_id
               and (case when i.einheit_id is null then not et.eigen else et.einheit_id = i.einheit_id and et.lernziel = i.lernziel end)) alle_besprochen
      from ein i left join schule.wackelt_status s on s.lernender_id = p_l and s.thema_id = i.thema_id
                  and s.bezug = case when i.einheit_id is null then '' else i.einheit_id::text || ':' || i.lernziel end),
  w as (
    select z.*, (schule.wackelt_fehler(p_l, z.thema_id, z.einheit_id, z.lernziel, z.s_am)).anzahl neu
      from z),
  r as (
    select w.*, case when w.s_status is not null and w.neu > 0 then 'zu_besprechen'
                     when w.s_status is not null then w.s_status
                     when coalesce(w.offen_wackelt, false) then 'zu_besprechen'
                     when w.alle_besprochen then 'besprochen'
                     else 'beobachten' end wirksam
      from w)
  select jsonb_build_object(
    'zu_besprechen', count(*) filter (where r.wirksam = 'zu_besprechen'),
    'eintraege', coalesce(jsonb_agg(jsonb_build_object(
        'thema_id', r.thema_id, 'titel', t.unterthema, 'einheit_id', r.einheit_id, 'lernziel', r.lernziel,
        'status', r.wirksam, 'quelle', case when r.s_status is null then 'vorgabe' else 'gespeichert' end,
        'status_gespeichert', r.s_status, 'status_am', r.s_am, 'status_von', r.s_von,
        'wieder_offen', r.s_status is not null and r.s_status <> 'zu_besprechen' and r.neu > 0,
        'fehler', r.fehler, 'fehler_neu', case when r.s_am is null then r.fehler else r.neu end, 'letzter_fehler_am', r.zuletzt,
        'etappe', r.etappen->0, 'etappen', coalesce(r.etappen, '[]'::jsonb))
      order by case r.wirksam when 'zu_besprechen' then 0 when 'beobachten' then 1 else 2 end, r.zuletzt desc nulls last, r.thema_id), '[]'::jsonb))
    from r join schule.thema t on t.id = r.thema_id;
$function$;
revoke all on function schule.wackelt_liste(bigint) from public, anon, authenticated;

-- 4. Aktionen (nur Eltern/Lehrer)
create or replace function api.schule_wackelt_lesen(p_schluessel text, p_daten jsonb default null)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id', '')::bigint;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  perform schule.zugriff(p_schluessel, v_l);
  if not exists (select 1 from schule.lernender where id = v_l and aktiv) then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  return jsonb_build_object('ok', true, 'lernender_id', v_l) || schule.wackelt_liste(v_l);
end $function$;

create or replace function schule.wackelt_setzen(p_l bigint, p_t bigint, p_e bigint, p_lz text, p_s text, p_von text)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_liste jsonb;
begin
  if p_s is null or p_s not in ('zu_besprechen', 'beobachten', 'besprochen') then
    raise exception 'status muss zu_besprechen, beobachten oder besprochen sein' using errcode = 'P0001'; end if;
  if not exists (select 1 from schule.thema where id = p_t) then raise exception 'Thema nicht gefunden' using errcode = 'P0001'; end if;
  if (p_e is null) <> (p_lz is null) then raise exception 'Etappe braucht einheit_id und lernziel' using errcode = 'P0001'; end if;
  if p_e is not null and not exists (select 1 from schule.einheit x, jsonb_array_elements(coalesce(x.inhalt->'etappen', '[]'::jsonb)) q
                                      where x.id = p_e and x.thema_id = p_t and q->>'lernziel' = p_lz) then
    raise exception 'Etappe gehört nicht zu diesem Thema' using errcode = 'P0001'; end if;
  insert into schule.wackelt_status (lernender_id, thema_id, einheit_id, lernziel, status, am, von)
  values (p_l, p_t, p_e, p_lz, p_s, now(), p_von)
  on conflict (lernender_id, thema_id, bezug) do update set status = excluded.status, am = excluded.am, von = excluded.von;
  v_liste := schule.wackelt_liste(p_l);
  return jsonb_build_object('ok', true, 'zu_besprechen', v_liste->'zu_besprechen',
    'eintrag', (select e from jsonb_array_elements(v_liste->'eintraege') e
                 where (e->>'thema_id')::bigint = p_t and (e->>'einheit_id') is not distinct from p_e::text and (e->>'lernziel') is not distinct from p_lz));
end $function$;
revoke all on function schule.wackelt_setzen(bigint, bigint, bigint, text, text, text) from public, anon, authenticated;

create or replace function api.schule_wackelt_setzen(p_schluessel text, p_daten jsonb default null)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id', '')::bigint;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  perform schule.zugriff(p_schluessel, v_l);
  if not exists (select 1 from schule.lernender where id = v_l and aktiv) then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  return schule.wackelt_setzen(v_l, nullif(p_daten->>'thema_id', '')::bigint, nullif(p_daten->>'einheit_id', '')::bigint, nullif(p_daten->>'lernziel', ''),
           p_daten->>'status', coalesce((select i.rolle || ':' || i.name from schule.lern_ich(p_schluessel) i where schule.ist_lern(p_schluessel)), 'eltern:App'));
end $function$;

grant execute on function api.schule_wackelt_lesen(text, jsonb) to council_mcp;
grant execute on function api.schule_wackelt_setzen(text, jsonb) to council_mcp;
revoke all on function api.schule_wackelt_lesen(text, jsonb) from public, anon, authenticated;
revoke all on function api.schule_wackelt_setzen(text, jsonb) from public, anon, authenticated;

-- Bestand unverändert?
do $mig$
declare v_t text;
begin
  select string_agg(v.t, ', ') into v_t from lw_vorher v
   where v.s <> (select case v.t
       when 'karte' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x)
       when 'lernziel' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x)
       when 'sterne' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x)
       when 'route' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.route x)
       when 'lernender' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernender x) end);
  if v_t is not null then raise exception 'LW-S: Bestand verändert (%)', v_t; end if;
  raise notice 'LW-S: Karten, Lernstände, Sterne, Plan, Kinder unverändert';
end $mig$;
