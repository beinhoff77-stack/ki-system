-- WW-S2 („Was wackelt“, Teil Datenbank, schlanke Fassung zu Entwurf 4): Analyse der offenen Fehler und Abhaken – NUR LESEN und Abhaken speichern.
-- Entscheidung des Nutzers (27.11.2026): kein „Nachüben schicken“; Wiederholungs- und Mischkarten, Logik und Ablauf bleiben, wie sie sind.
-- Vorgabe: inhalte/design/wackelt/entwurf4/umsetzung4.md (Darstellung), entwurf3/umsetzung3.md Abschnitte 2 und 3 (Regeln fürs Verschwinden, Datenbedarf).
-- Plan, Antwortformen und Nachweis „Berührt die Lernlogik nicht“: inhalte/plan/wackelt-server.md. Einspielen NUR über tools/tests/wackelt_einspielen.py
-- (eine Transaktion, prüft sich selbst). Unabhängig von RB-S: Ist RB-S eingespielt, kommt die Fehlerart aus dem erkannten Fehlbild
-- (schule.versuch_regelbezug), sonst aus dem groben „grund“ von schule.antwort_bewerten (vorzeichen, komma, vertauscht, gerundet, falsche_einheit) oder sie bleibt leer.
--
-- WAS
-- 1. Tabelle (RLS an, keine Policy, keine Rechte für anon/authenticated; nur über die Funktionen):
--      schule.fehler_erledigt (id, lernender_id, versuch_id, am, von, zurueckgenommen_am, zurueckgenommen_von)  – „Abhaken“ je falscher Antwort
--    Rückgängig = zurueckgenommen_am setzen (kein DELETE). Je Versuch höchstens ein gültiger Eintrag (eindeutiger Teilindex).
--    Die Tabelle wird von KEINER Funktion der Lernlogik gelesen (Karte, Wiederholung, Check-in, Mischkarten, Sterne, Auswahl der nächsten Aufgabe).
-- 2. schule.wackelt_analyse(kind, tage, mit_erledigt) -> jsonb (Form in wackelt-server.md). Regeln (umsetzung3 Abschnitt 2, ohne Nachüben):
--      falsch      = endgültig falsche Antwort (schule.fehler_endgueltig_am, wie LW-S 2) – ein falscher 1. Anlauf mit zweiter Chance zählt nicht
--      offen       = falsch, im Zeitraum (am > jetzt − tage; tage 0/leer = alles), nicht abgehakt
--      Auswertung: Fehler je Thema (offen / alle Antworten im Zeitraum), die letzten 7 Lerntage (richtig/falsch, Tag in der Zeitzone des Kindes),
--      wiederkehrende Fehlerarten (≥ 2 falsche im Zeitraum, mindestens eine offen; höchstens 3), „nur einmal passiert“ (Lernkarten mit genau einem
--      offenen Fehler, dessen Fehlerart nicht wiederkehrt; davon danach richtig). „Danach richtig“ ist nur eine Anzeige (beim Lesen ausgewertet).
--    Schreibt nur in eigene Hilfstabellen dieser Sitzung (pg_temp, on commit drop).
-- 3. schule.fehler_abhaken(kind, versuch_ids, zurueck, von): schreibt ausschließlich schule.fehler_erledigt.
-- 4. Aktionen (api, security definer; Muster api.schule_wackelt_lesen):
--      api.schule_wackelt_analyse {lernender_id, tage?, erledigt?}         nur Eltern/Lehrer
--      api.schule_fehler_abhaken  {lernender_id, versuch_ids[], zurueck?}  nur Eltern/Lehrer
--    Rechte: execute nur für council_mcp (wie die übrigen api.schule_*), revoke von public, anon, authenticated.
--
-- WAS NICHT: keine Änderung an bestehenden Funktionen, Tabellen oder Triggern; kein Schreiben in schule.versuch, schule.karte_stand,
-- schule.misch_ausgabe, schule.lerntag, schule.sterne oder eine andere bestehende Tabelle; kein neuer Trigger (auch kein interner: keine Fremdschlüssel
-- auf bestehende Tabellen); keine neue Regel in schule.regel.
-- Kein UPDATE/DELETE von Bestandsdaten, kein DROP. Kein Nachüben (Entscheidung des Nutzers). Wiederholbar: ein zweiter Lauf ändert nichts.

select set_config('lock_timeout', '3s', true);

do $$ begin
  if to_regprocedure('schule.fehler_endgueltig_am(schule.versuch)') is null or to_regprocedure('schule.zugriff(text, bigint)') is null
     or to_regprocedure('schule.ist_leiter(text)') is null or to_regprocedure('schule.wer_tn(text)') is null
     or to_regprocedure('schule.loesung_sicht(schule.aufgabe)') is null or to_regprocedure('schule.antwort_bewerten(schule.aufgabe, jsonb)') is null
  then raise exception 'WW-S: Voraussetzung fehlt (LW-S, BD-S2, Lern-Zugänge)'; end if;
end $$;

-- 1. Tabelle
create table if not exists schule.fehler_erledigt (
  id bigint generated always as identity primary key,
  lernender_id bigint not null,   -- bewusst OHNE Fremdschlüssel: ein Fremdschlüssel legte interne Trigger an schule.versuch/schule.lernender an
  versuch_id bigint not null,     -- und sperrte schule.versuch beim Anlegen. Zugehörigkeit prüft schule.ww_versuche vor jedem Eintrag.
  am timestamptz not null default now(),
  von text not null,
  zurueckgenommen_am timestamptz,
  zurueckgenommen_von text
);
create unique index if not exists fehler_erledigt_gueltig on schule.fehler_erledigt (versuch_id) where zurueckgenommen_am is null;
create index if not exists fehler_erledigt_kind on schule.fehler_erledigt (lernender_id);
alter table schule.fehler_erledigt enable row level security;   -- nur über die security-definer-Funktionen, wie die übrigen schule-Tabellen
revoke all on table schule.fehler_erledigt from public, anon, authenticated;
comment on table schule.fehler_erledigt is 'WW-S: „Abhaken“ einer falschen Antwort auf der Seite „Was wackelt“ (nur Anzeige für Eltern/Lehrer, ohne Wirkung auf Karte, Wiederholung, Mischkarten); Rückgängig = zurueckgenommen_am';

-- 2. Fehlerart einer falschen Antwort: Fehlbild (RB-S, wenn eingespielt) > grober Grund > leer
create or replace function schule.ww_fehlerart(v schule.versuch, a schule.aufgabe)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare r jsonb; g text;
begin
  if to_regprocedure('schule.versuch_regelbezug(schule.versuch)') is not null then   -- RB-S eingespielt
    begin r := schule.versuch_regelbezug(v); exception when others then r := null; end;
  end if;
  begin g := schule.antwort_bewerten(a, v.antwort)->>'grund'; exception when others then g := null; end;
  return jsonb_strip_nulls(jsonb_build_object(
    'quelle', case when r ? 'fehlbild_nr' then 'fehlbild' when g is not null then 'grund' end,
    'schluessel', case when r ? 'fehlbild' then 'fb:' || (r->>'fehlbild') when r ? 'fehlbild_nr' then 'a:' || a.id || ':' || (r->>'fehlbild_nr')
                       when g is not null then 'g:' || g end,
    'kennung', r->>'fehlbild', 'text', r->>'text', 'fehlbild_regel', r->>'fehlbild_regel', 'regel', r->>'regel', 'grund', g));
end $function$;

create or replace function schule.ww_von(p_schluessel text)
 returns text language sql stable security definer set search_path to ''
as $function$
  select coalesce((select i.rolle || ':' || i.name from schule.lern_ich(p_schluessel) i where schule.ist_lern(p_schluessel)), 'eltern:App');
$function$;

-- 2. Analyse
create or replace function schule.wackelt_analyse(p_l bigint, p_tage integer default 14, p_mit_erledigt boolean default false)
 returns jsonb language plpgsql set search_path to ''   -- volatil nur wegen der Hilfstabellen dieser Sitzung (pg_temp, on commit drop); liest sonst nur
as $function$
declare v_seit timestamptz := case when coalesce(p_tage, 0) <= 0 then null else now() - make_interval(days => p_tage) end;
  v_tz text := coalesce((select l.zeitzone from schule.lernender l where l.id = p_l), 'Europe/Berlin'); r jsonb;
begin
  create temp table if not exists ww_v (ver schule.versuch, auf schule.aufgabe, id bigint, am timestamptz, richtig boolean, hilfe smallint, anlauf smallint,
    aufgabe_id bigint, einheit_id bigint, lz text, thema_id bigint) on commit drop;
  truncate ww_v;   -- nur die Hilfstabelle dieser Sitzung
  insert into ww_v select x, a, x.id, x.am, x.richtig, x.hilfe, x.anlauf, x.aufgabe_id, a.einheit_id, a.variante_gruppe, e.thema_id
    from schule.versuch x join schule.aufgabe a on a.id = x.aufgabe_id join schule.einheit e on e.id = a.einheit_id where x.lernender_id = p_l;
  create temp table if not exists ww_f (id bigint, am timestamptz, aufgabe_id bigint, einheit_id bigint, lz text, thema_id bigint, im_zeitraum boolean,
    abgehakt_am timestamptz, abgehakt_von text, aufgabe_richtig_am timestamptz, lk_richtig_am timestamptz, erst_antwort jsonb, art jsonb, eintrag jsonb) on commit drop;
  truncate ww_f;
  insert into ww_f
  select f.id, f.am, f.aufgabe_id, f.einheit_id, f.lz, f.thema_id, v_seit is null or f.am > v_seit,
         fe.am, fe.von,
         (select min(y.am) from ww_v y where y.aufgabe_id = f.aufgabe_id and y.richtig and (y.am, y.id) > (f.am, f.id)),
         (select min(y.am) from ww_v y where y.einheit_id = f.einheit_id and y.lz = f.lz and y.richtig and coalesce(y.hilfe, 0) = 0 and (y.am, y.id) > (f.am, f.id)),
         case when f.anlauf = 2 then (select (y.ver).antwort from ww_v y where y.aufgabe_id = f.aufgabe_id and y.anlauf = 1 and not y.richtig and y.am <= f.am
                                       order by y.am desc, y.id desc limit 1) end,
         schule.ww_fehlerart(f.ver, f.auf), null
    from ww_v f
    left join schule.fehler_erledigt fe on fe.versuch_id = f.id and fe.zurueckgenommen_am is null
   where not f.richtig and schule.fehler_endgueltig_am(f.ver) is not null;
  update ww_f w set eintrag = jsonb_strip_nulls(jsonb_build_object(
      'versuch_id', w.id, 'am', w.am, 'tag', (w.am at time zone v_tz)::date, 'thema_id', w.thema_id,
      'thema', (select coalesce(t.unterthema, t.schluessel) from schule.thema t where t.id = w.thema_id),
      'einheit_id', w.einheit_id, 'lernziel', w.lz,
      'lernkarte', (select q->>'titel' from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) q where e.id = w.einheit_id and q->>'lernziel' = w.lz limit 1),
      'aufgabe', (select jsonb_strip_nulls(jsonb_build_object('id', (v.auf).id, 'antworttyp', (v.auf).antworttyp, 'form', (v.auf).form, 'typ', (v.auf).typ,
                    'stufe', (v.auf).stufe, 'frage', (v.auf).frage, 'antworten', (v.auf).antworten, 'loesung', schule.loesung_sicht(v.auf), 'loesungsweg', (v.auf).loesungsweg))
                    from ww_v v where v.id = w.id),
      'antwort', (select (v.ver).antwort from ww_v v where v.id = w.id), 'erst_antwort', w.erst_antwort,
      'anlauf', (select v.anlauf from ww_v v where v.id = w.id), 'mit_tipp', (select coalesce(v.hilfe, 0) > 0 from ww_v v where v.id = w.id),
      'fehlerart', nullif(w.art, '{}'::jsonb),
      'danach_richtig', nullif(jsonb_strip_nulls(jsonb_build_object('aufgabe_am', w.aufgabe_richtig_am, 'lernkarte_am', w.lk_richtig_am)), '{}'::jsonb),
      'erledigt', case when w.abgehakt_am is not null then jsonb_build_object('art', 'abgehakt', 'am', w.abgehakt_am) end));
  with offen as (select * from ww_f where im_zeitraum and abgehakt_am is null),
       falsch_z as (select * from ww_f where im_zeitraum),
       arten as (select f.art->>'schluessel' s, count(*) n, count(*) filter (where o.id is not null) n_offen,
                        min(f.art->>'kennung') kennung, min(f.art->>'text') text, min(f.art->>'grund') grund,
                        jsonb_agg(distinct f.thema_id) themen, max(f.am) zuletzt
                   from falsch_z f left join offen o on o.id = f.id where f.art ? 'schluessel' group by 1),
       wieder as (select * from arten where n >= 2 and n_offen > 0 order by n desc, zuletzt desc limit 3),
       je_lk as (select einheit_id, lz, count(*) n, min(id) id from offen group by 1, 2),
       einmal as (select o.* from je_lk j join offen o on o.id = j.id where j.n = 1
                    and not exists (select 1 from wieder w where w.s = o.art->>'schluessel'))
  select jsonb_build_object(
    'ok', true, 'lernender_id', p_l, 'tage', coalesce(nullif(p_tage, 0), 0), 'seit', v_seit, 'heute', (now() at time zone v_tz)::date,
    'mit_fehlbild', to_regprocedure('schule.versuch_regelbezug(schule.versuch)') is not null,
    'offen_zahl', (select count(*) from offen),
    'offen', coalesce((select jsonb_agg(o.eintrag order by o.am desc, o.id desc) from (select * from offen order by am desc, id desc limit 300) o), '[]'::jsonb),
    'auswertung', jsonb_build_object(
      'antworten', (select count(*) from ww_v v where v_seit is null or v.am > v_seit),
      'richtig', (select count(*) from ww_v v where (v_seit is null or v.am > v_seit) and v.richtig),
      'themen', coalesce((select jsonb_agg(jsonb_build_object('thema_id', t.thema_id, 'thema', (select coalesce(x.unterthema, x.schluessel) from schule.thema x where x.id = t.thema_id),
                                   'offen', t.offen, 'gesamt', t.gesamt) order by t.offen desc, t.gesamt desc, t.thema_id)
                          from (select v.thema_id, count(*) gesamt, (select count(*) from offen o where o.thema_id = v.thema_id) offen
                                  from ww_v v where v_seit is null or v.am > v_seit group by 1) t), '[]'::jsonb),
      'lerntage', coalesce((select jsonb_agg(jsonb_build_object('tag', d.tag, 'richtig', d.r, 'falsch', d.f) order by d.tag)
                            from (select (v.am at time zone v_tz)::date tag, count(*) filter (where v.richtig) r, count(*) filter (where not v.richtig) f
                                    from ww_v v group by 1 order by 1 desc limit 7) d), '[]'::jsonb),
      'wiederkehrend', coalesce((select jsonb_agg(jsonb_strip_nulls(jsonb_build_object('schluessel', w.s, 'kennung', w.kennung, 'text', w.text, 'grund', w.grund,
                                    'anzahl', w.n, 'offen', w.n_offen, 'themen', w.themen)) order by w.n desc, w.zuletzt desc) from wieder w), '[]'::jsonb),
      'einmal', jsonb_build_object('lernkarten', (select count(*) from einmal), 'danach_richtig', (select count(*) from einmal where lk_richtig_am is not null),
                                   'themen_danach_richtig', coalesce((select jsonb_agg(distinct thema_id) from einmal where lk_richtig_am is not null), '[]'::jsonb))),
    'erledigt', case when p_mit_erledigt then coalesce((select jsonb_agg(f.eintrag order by f.abgehakt_am desc, f.id desc)
                                                         from (select * from ww_f where im_zeitraum and abgehakt_am is not null
                                                                order by abgehakt_am desc, id desc limit 200) f), '[]'::jsonb) end)
    into r;
  return jsonb_strip_nulls(r);
end $function$;
comment on function schule.wackelt_analyse(bigint, integer, boolean) is 'WW-S: offene falsche Antworten eines Kindes im Zeitraum mit Aufgabe, Fehlerart, Folge danach; Auswertung (inhalte/plan/wackelt-server.md). Nur lesend.';

-- 3. Abhaken. Prüfung der übergebenen Versuche (gehören dem Kind, endgültig falsch)
create or replace function schule.ww_versuche(p_l bigint, p_ids jsonb)
 returns table (versuch_id bigint, ok boolean, grund text) language plpgsql stable set search_path to ''
as $function$
begin
  if jsonb_typeof(p_ids) is distinct from 'array' or jsonb_array_length(p_ids) = 0 or jsonb_array_length(p_ids) > 200 then
    raise exception 'versuch_ids: Liste mit 1 bis 200 Einträgen' using errcode = 'P0001'; end if;
  if exists (select 1 from jsonb_array_elements(p_ids) x where jsonb_typeof(x) not in ('number', 'string') or (x #>> '{}') !~ '^\d{1,18}$') then
    raise exception 'versuch_ids: nur Zahlen' using errcode = 'P0001'; end if;
  return query
    select i.id, v.id is not null and not v.richtig and schule.fehler_endgueltig_am(v) is not null,
           case when v.id is null then 'nicht gefunden' when v.richtig then 'richtig' when schule.fehler_endgueltig_am(v) is null then 'nicht endgültig falsch' end
      from (select distinct (x #>> '{}')::bigint id from jsonb_array_elements(p_ids) x) i
      left join schule.versuch v on v.id = i.id and v.lernender_id = p_l;
end $function$;

create or replace function schule.fehler_abhaken(p_l bigint, p_ids jsonb, p_zurueck boolean, p_von text)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare n int := 0; c int; z record; v_nicht jsonb := '[]';
begin
  for z in select * from schule.ww_versuche(p_l, p_ids) loop
    if not z.ok then v_nicht := v_nicht || jsonb_build_object('versuch_id', z.versuch_id, 'grund', z.grund); continue; end if;
    if coalesce(p_zurueck, false) then
      update schule.fehler_erledigt set zurueckgenommen_am = now(), zurueckgenommen_von = p_von
       where versuch_id = z.versuch_id and lernender_id = p_l and zurueckgenommen_am is null;
    else
      insert into schule.fehler_erledigt (lernender_id, versuch_id, von) values (p_l, z.versuch_id, p_von)
        on conflict (versuch_id) where zurueckgenommen_am is null do nothing;
    end if;
    get diagnostics c = row_count; n := n + c;
  end loop;
  return jsonb_build_object('ok', true, 'geaendert', n, 'uebersprungen', v_nicht);
end $function$;

revoke all on function schule.ww_fehlerart(schule.versuch, schule.aufgabe), schule.ww_von(text), schule.wackelt_analyse(bigint, integer, boolean),
  schule.ww_versuche(bigint, jsonb), schule.fehler_abhaken(bigint, jsonb, boolean, text)
  from public, anon, authenticated;

-- 4. Aktionen
create or replace function api.schule_wackelt_analyse(p_schluessel text, p_daten jsonb default null)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id', '')::bigint; v_t int := coalesce(nullif(p_daten->>'tage', '')::int, 14);
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  perform schule.zugriff(p_schluessel, v_l);
  if not exists (select 1 from schule.lernender where id = v_l and aktiv) then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  if v_t not in (0, 7, 14) then raise exception 'tage: 7, 14 oder 0 (alles)' using errcode = 'P0001'; end if;
  return schule.wackelt_analyse(v_l, v_t, coalesce((p_daten->>'erledigt')::boolean, false));
end $function$;

create or replace function api.schule_fehler_abhaken(p_schluessel text, p_daten jsonb default null)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint := nullif(p_daten->>'lernender_id', '')::bigint;
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  perform schule.zugriff(p_schluessel, v_l);
  if not exists (select 1 from schule.lernender where id = v_l and aktiv) then raise exception 'Kind nicht gefunden' using errcode = 'P0001'; end if;
  return schule.fehler_abhaken(v_l, p_daten->'versuch_ids', coalesce((p_daten->>'zurueck')::boolean, false), schule.ww_von(p_schluessel));
end $function$;

do $$ begin
  if exists (select 1 from pg_roles where rolname = 'council_mcp') then
    grant execute on function api.schule_wackelt_analyse(text, jsonb), api.schule_fehler_abhaken(text, jsonb) to council_mcp;
  end if;
end $$;
revoke all on function api.schule_wackelt_analyse(text, jsonb), api.schule_fehler_abhaken(text, jsonb) from public, anon, authenticated;
