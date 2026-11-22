-- LK-S / LK-S 2 (22.11.): ein Thema in mehreren Klassen, für alle Schularten (inhalte/AUFTRAEGE.md „Bau-Auftrag LK“, Abschnitt LK-S, mit den Nachträgen
-- „vorhandener Lernstand der Kinder“ und „Route: zweiter Teil eines Themas fliegt ins Nachbarland“; Nacharbeit „Nachtrag LW-S 2 / LK-S 2 – ChatGPT 934“).
-- Grundlage: inhalte/pruefung/lehrplan/rs_pruefung_2211.md Abschnitt 6 und lk_pruefung_2211.md. Daten: lk_daten_2211.json (alle drei Schularten).
-- Einspielen NACH rs_korrektur_2211.sql UND lk_korrektur_2211.sql (Schritt 0 prüft das), in EINER Transaktion. Unabhängig von LW-S.
--   1. Felder: schule.zuordnung.rolle ('neu' | 'weitergefuehrt', Aussage der Lehrplan-Prüfung je Punkt) und .etappen (Lernziel-Schlüssel, die dieser Punkt
--      verlangt; '{*}' = ausdrücklich das ganze Thema; null = unbekannt – NICHT „alle Etappen“, LK-S 2 B2); schule.lernender.zweig ('rs_I' | 'rs_II_III').
--   2. Sichten: schule.lehrplan_zweig (Quelle → Schulart, Zweig, Klasse; RS 5/6 „allgemein“ gilt für rs_I und rs_II_III, IB „myp_beide“ für Standard und
--      Extended), schule.thema_lage_klasse (je Schulart, Zweig, Thema und Klasse), schule.thema_lage (je Thema bzw. Etappe: klasse_ab, klasse_route,
--      klassen[], Rolle je Klasse) und schule.lehrplan_abdeckung (je Lernbereich: Stunden, Punkte, Punkte mit Thema, Stunden mit Themenzuordnung).
--      Regeln: aktive Basis-Quellen, nicht archivierte Einträge, Hauptbezüge ohne pruefstatus 'klaerungsbedarf'.
--      LK-S 2 B1: Die Klassenliste zeigt ALLE belegten Klassen, auch vor klasse_fest (z. B. Thema 61: RS I in 8 und 9). klasse_fest bestimmt nur den Start
--      in Route/Stufen (klasse_route; Wert null = nicht in der Route dieser Schulart) und steht immer in der Liste. Rolle je Klasse: früheste Klasse 'neu',
--      spätere 'weitergefuehrt' (Aussage der Prüfung zusätzlich in rolle_lehrplan). Etappe: klasse_ab = früheste Klasse, die sie nennt (oder „ganzes Thema“).
--   3. Befüllen: schule.lehrplan_rolle_setzen(jsonb) – wiederholbar, ändert nur rolle/etappen vorhandener Zuordnungen. Unbekannte Etappen-Schlüssel
--      (LK-S 2 B5): Zuordnung bleibt unverändert und wird gemeldet. Hier mit lk_daten_2211.json (690 Hauptbezüge, alle mit Etappen).
--   4. Schnittstelle: schule_lehrplan_matrix – je Thema `klassen`, oben `lehrplan_zuordnung` (Stunden mit Themenzuordnung, eine Schätzung – keine
--      Lernabdeckung) und je Kind `zweig`; Kindsicht `klassen_kind`. schule_lehrplan_thema – `klassen`, `baut_auf`, `weiter_in`, mit Kind `klassen_kind`
--      mit Stand der Etappen dieser Klasse. Alle alten Felder bleiben.
--   5. Teilen eines Themas: schule.thema_teilen(plan, probelauf) – geprüfte Vorlage, hier NICHT aufgerufen (nach LK-D erfüllt derzeit kein Thema die Regel).
-- Unverändert (am Ende geprüft): thema_stufe aller Kinder und Themen (Stufe, im Plan), Reiseoptionen, Plan (route), Lernstand (karte_stand,
-- lernziel_stand), Sterne, Flug-Abschlüsse, Visum-Regeln (v_ort_visum), Klassen (thema_jahrgang). Kein DROP, kein DELETE. Wiederholt ausführbar.

do $$ begin   -- Schritt 0: Reihenfolge
  if not exists (select 1 from schule.zuordnung where begruendung like 'LK-D 22.11.2026%') then
    raise exception 'LK-S: zuerst rs_korrektur_2211.sql und lk_korrektur_2211.sql einspielen'; end if;
end $$;


create temp table if not exists lk_vorher (t text, s text) on commit drop;
truncate lk_vorher; -- nur die Hilfstabelle dieser Sitzung
create or replace function pg_temp.lk_stand() returns table (t text, s text) language plpgsql as $f$
declare v text;
begin
  t := 'thema_stufe'; select md5(coalesce(string_agg(l.id || ':' || th.id || ':' || coalesce(schule.thema_stufe(l.id, th.id)::text, ''), '|' order by l.id, th.id), ''))
    into s from schule.lernender l cross join schule.thema th; return next;
  t := 'reiseoptionen'; select md5(coalesce(string_agg(l.id || ':' || coalesce(schule.reiseoptionen(l.id)::text, ''), '|' order by l.id), '')) into s from schule.lernender l; return next;
  t := 'jahrgang'; select md5(coalesce(string_agg(th.id || ':' || schule.thema_jahrgang(th.id)::text, '|' order by th.id), '')) into s from schule.thema th; return next;
  t := 'lernender'; select md5(coalesce(string_agg((to_jsonb(x) - 'zweig')::text, '|' order by x.id), '')) into s from schule.lernender x; return next;
  foreach v in array array['route', 'karte_stand', 'lernziel_stand', 'sterne', 'flug_erstabschluss', 'v_ort_visum', 'voraussetzung', 'thema', 'block_thema'] loop
    t := v;
    if to_regclass('schule.' || v) is null then s := 'fehlt';
    else execute format('select md5(coalesce(string_agg(x::text, %L order by x::text), %L)) from schule.%I x', '|', '', v) into s; end if;
    return next;
  end loop;
end $f$;
insert into lk_vorher select * from pg_temp.lk_stand();

-- 1. Felder
alter table schule.zuordnung add column if not exists rolle text;
alter table schule.zuordnung add column if not exists etappen text[];
alter table schule.lernender add column if not exists zweig text;
do $$ begin
  if not exists (select 1 from pg_constraint where conname = 'zuordnung_rolle_check') then
    alter table schule.zuordnung add constraint zuordnung_rolle_check check (rolle is null or rolle in ('neu', 'weitergefuehrt')); end if;
  if not exists (select 1 from pg_constraint where conname = 'lernender_zweig_check') then
    alter table schule.lernender add constraint lernender_zweig_check check (zweig is null or zweig in ('rs_I', 'rs_II_III')); end if;
end $$;
comment on column schule.zuordnung.rolle is 'LK-S: Aussage der Lehrplan-Prüfung je Punkt: neu | weitergefuehrt (die Anzeige rechnet die Rolle je Klasse aus der Klassenlage)';
comment on column schule.zuordnung.etappen is 'LK-S 2: Lernziel-Schlüssel der Etappen, die dieser Punkt verlangt; {*} = ausdrücklich das ganze Thema; null = unbekannt (nicht „alle“)';
comment on column schule.lernender.zweig is 'LK-S: Wahlpflichtfächergruppe Realschule (rs_I | rs_II_III); leer = rs_I (Entscheidung 22.11.)';

-- Zweig eines Kindes (Vorgaben: RS leer = rs_I; IB = myp_standard, Annahme; Gymnasium = allgemein)
create or replace function schule.kind_zweig(p_schulart text, p_zweig text)
 returns text language sql immutable set search_path to ''
as $function$
  select case p_schulart when 'rs_by' then coalesce(p_zweig, 'rs_I') when 'ib_myp' then 'myp_standard' else 'allgemein' end;
$function$;

-- Lernbereich eines Eintrags: er selbst oder der nächste Vorfahr mit art = 'lernbereich'
create or replace function schule.eintrag_lernbereich(p_eintrag bigint)
 returns bigint language sql stable set search_path to ''
as $function$
  with recursive k(id, parent_id, art, tiefe) as (
    select e.id, e.parent_id, e.art, 0 from schule.eintrag e where e.id = p_eintrag
    union all select e.id, e.parent_id, e.art, k.tiefe + 1 from schule.eintrag e join k on e.id = k.parent_id where k.art <> 'lernbereich' and k.tiefe < 10)
  select id from k where art = 'lernbereich' order by tiefe limit 1;
$function$;

-- 2. Sichten
create or replace view schule.lehrplan_zweig as
select q.id quelle_id, q.schulart, q.jahr_von klasse, z.zweig
  from schule.quelle q
  cross join lateral unnest(case when q.schulart = 'rs_by' and q.zweig = 'allgemein' then array['rs_I', 'rs_II_III']
                                 when q.schulart = 'ib_myp' and q.zweig = 'myp_beide' then array['myp_standard', 'myp_extended']
                                 else array[q.zweig] end) z(zweig)
 where q.aktiv and q.rolle = 'basis';
comment on view schule.lehrplan_zweig is 'LK-S: aktive Basis-Quelle je Schulart, Zweig und Klasse (RS 5/6 allgemein gilt für beide Gruppen, IB myp_beide für Standard und Extended)';

create or replace view schule.thema_lage_klasse as
with z as (   -- Hauptbezüge je Schulart, Zweig, Thema und Klasse
  select lz.schulart, lz.zweig, zu.thema_id, lz.klasse, zu.eintrag_id, zu.rolle, zu.etappen
    from schule.zuordnung zu
    join schule.eintrag e on e.id = zu.eintrag_id and not e.archiviert
    join schule.lehrplan_zweig lz on lz.quelle_id = e.quelle_id
   where zu.bezug = 'haupt' and zu.pruefstatus <> 'klaerungsbedarf'),
fest as (     -- klasse_fest je Schulart (Zahl: Start in der Route; null: nicht in der Route dieser Schulart)
  select t.id thema_id, f.key schulart, case when jsonb_typeof(f.value) = 'number' then (f.value #>> '{}')::int end klasse
    from schule.thema t cross join lateral jsonb_each(coalesce(t.klasse_fest, '{}'::jsonb)) f),
sz as (select distinct schulart, zweig from schule.lehrplan_zweig),
kl as (       -- alle belegten Klassen (B1: auch vor klasse_fest) und die Klasse aus klasse_fest
  select distinct z.schulart, z.zweig, z.thema_id, z.klasse, false nur_fest from z
  union
  select f.schulart, sz.zweig, f.thema_id, f.klasse, true from fest f join sz on sz.schulart = f.schulart
   where f.klasse is not null and not exists (select 1 from z where z.schulart = f.schulart and z.zweig = sz.zweig and z.thema_id = f.thema_id and z.klasse = f.klasse)),
k as (
  select kl.*, min(kl.klasse) over (partition by kl.schulart, kl.zweig, kl.thema_id) klasse_ab,
         case when f.thema_id is not null then f.klasse
              else min(kl.klasse) filter (where not kl.nur_fest) over (partition by kl.schulart, kl.zweig, kl.thema_id) end klasse_route
    from kl left join fest f on f.thema_id = kl.thema_id and f.schulart = kl.schulart)
select k.schulart, k.zweig, k.thema_id, k.klasse, k.klasse_ab, k.klasse_route,
       case when k.klasse = k.klasse_ab then 'neu' else 'weitergefuehrt' end rolle,
       (select array_agg(distinct z.rolle order by z.rolle) filter (where z.rolle is not null) from z
         where z.schulart = k.schulart and z.zweig = k.zweig and z.thema_id = k.thema_id and z.klasse = k.klasse) rolle_lehrplan,
       (select array_agg(distinct x order by x) from z z2 cross join lateral unnest(z2.etappen) x
         where z2.schulart = k.schulart and z2.zweig = k.zweig and z2.thema_id = k.thema_id and z2.klasse = k.klasse and x <> '*') etappen,
       coalesce(bool_or('*' = any(z.etappen)), false) ganzes_thema,                    -- ausdrücklich geliefert
       coalesce(bool_or(z.eintrag_id is not null and z.etappen is null), false) etappen_unbekannt,   -- B2: nicht „alle“
       (select coalesce(jsonb_agg(jsonb_build_object('eintrag_id', lb.id, 'pfad', lb.pfad, 'titel', lb.text, 'stunden', lb.stunden) order by lb.reihenfolge, lb.id), '[]'::jsonb)
          from schule.eintrag lb where lb.id in (select schule.eintrag_lernbereich(z3.eintrag_id) from z z3
                                                where z3.schulart = k.schulart and z3.zweig = k.zweig and z3.thema_id = k.thema_id and z3.klasse = k.klasse)) lernbereiche,
       count(z.eintrag_id) punkte,
       k.nur_fest nur_klasse_fest
  from k left join z on z.schulart = k.schulart and z.zweig = k.zweig and z.thema_id = k.thema_id and z.klasse = k.klasse
 group by k.schulart, k.zweig, k.thema_id, k.klasse, k.klasse_ab, k.klasse_route, k.nur_fest;
comment on view schule.thema_lage_klasse is 'LK-S 2: je Schulart, Zweig, Thema und belegter Klasse: Rolle (früheste neu, sonst weitergefuehrt), klasse_route (klasse_fest gewinnt nur für die Route), Etappen dieser Klasse (ganzes_thema nur ausdrücklich; etappen_unbekannt = Punkt ohne Etappen), Lernbereiche mit Stunden';

create or replace view schule.thema_lage as
with et as (
  select t.id thema_id, q->>'lernziel' lernziel
    from schule.thema t join schule.einheit e on e.id = schule.thema_einheit(t.id)
    cross join lateral jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) q)
select k.schulart, k.zweig, k.thema_id, null::text lernziel, min(k.klasse_ab) klasse_ab, min(k.klasse_route) klasse_route,
       array_agg(k.klasse order by k.klasse) klassen, jsonb_object_agg(k.klasse::text, k.rolle) rollen, null::int[] unbekannt_in
  from schule.thema_lage_klasse k group by 1, 2, 3
union all
select k.schulart, k.zweig, k.thema_id, et.lernziel,
       min(k.klasse) filter (where k.ganzes_thema or et.lernziel = any(k.etappen)) klasse_ab, min(k.klasse_route) klasse_route,
       array_agg(k.klasse order by k.klasse) filter (where k.ganzes_thema or et.lernziel = any(k.etappen)) klassen,
       jsonb_object_agg(k.klasse::text, k.rolle) filter (where k.ganzes_thema or et.lernziel = any(k.etappen)) rollen,
       array_agg(k.klasse order by k.klasse) filter (where k.etappen_unbekannt) unbekannt_in
  from schule.thema_lage_klasse k join et on et.thema_id = k.thema_id group by 1, 2, 3, 4;
comment on view schule.thema_lage is 'LK-S 2: je Schulart, Zweig, Thema (lernziel null) und Etappe: klasse_ab (Lehrplan), klasse_route (Route/Stufen), klassen[], Rolle je Klasse, unbekannt_in (Klassen mit Punkten ohne Etappen)';

create or replace view schule.lehrplan_abdeckung as
with p as (   -- Punkte je Lernbereich: Kompetenzen darunter; ein Lernbereich ohne Kompetenzen zählt als ein Punkt
  select q.lb_id, q.punkt_id from (select schule.eintrag_lernbereich(k.id) lb_id, k.id punkt_id from schule.eintrag k where k.art = 'kompetenz' and not k.archiviert) q
   where q.lb_id is not null),
p2 as (
  select lb_id, punkt_id from p
  union all
  select lb.id, lb.id from schule.eintrag lb where lb.art = 'lernbereich' and not lb.archiviert and not exists (select 1 from p where p.lb_id = lb.id)),
m as (
  select p2.lb_id, count(*) punkte,
         count(*) filter (where exists (select 1 from schule.zuordnung z where z.eintrag_id = p2.punkt_id and z.bezug = 'haupt' and z.pruefstatus <> 'klaerungsbedarf')) punkte_mit_thema
    from p2 group by 1)
select lz.schulart, lz.zweig, lz.klasse, lb.quelle_id, lb.id eintrag_id, lb.pfad, lb.text lernbereich, lb.stunden, m.punkte, m.punkte_mit_thema,
       round(coalesce(lb.stunden, 0) * m.punkte_mit_thema / nullif(m.punkte, 0), 1) stunden_zugeordnet, lb.reihenfolge
  from schule.eintrag lb join m on m.lb_id = lb.id and not lb.archiviert join schule.lehrplan_zweig lz on lz.quelle_id = lb.quelle_id;
comment on view schule.lehrplan_abdeckung is 'LK-S 2 (B6): Zuordnungsgrad je Lernbereich – Stunden, Punkte, Punkte mit Hauptthema, stunden_zugeordnet = Stunden × Anteil der Punkte mit Thema (Schätzung, keine Lernabdeckung)';

revoke all on schule.lehrplan_zweig, schule.thema_lage_klasse, schule.thema_lage, schule.lehrplan_abdeckung from public, anon, authenticated;

-- 3. Befüllen (wiederholbar): [{eintrag_id, thema_id|thema, rolle?, etappen? (Liste, "a, b" oder ["*"] = ganzes Thema), ganzes_thema?}]
-- Nur vorhandene Zuordnungen, nur übergebene Felder. LK-S 2 B5: unbekannte oder leere Etappen → Zuordnung unverändert, gemeldet.
create or replace function schule.lehrplan_rolle_setzen(p_daten jsonb)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare x jsonb; v_e bigint; v_t bigint; v_r text; v_et text[]; v_bekannt text[]; v_n int; v_gesetzt int := 0; v_gleich int := 0;
  v_fehlt jsonb := '[]'::jsonb; v_unbekannt jsonb := '[]'::jsonb; v_hat_et boolean;
begin
  if jsonb_typeof(p_daten) is distinct from 'array' then raise exception 'Liste erwartet' using errcode = 'P0001'; end if;
  for x in select * from jsonb_array_elements(p_daten) loop
    v_e := (x->>'eintrag_id')::bigint; v_t := coalesce(x->>'thema_id', x->>'thema')::bigint; v_r := x->>'rolle';
    if v_r is not null and v_r not in ('neu', 'weitergefuehrt') then raise exception 'rolle % unbekannt (Eintrag %)', v_r, v_e using errcode = 'P0001'; end if;
    v_hat_et := x ? 'etappen' or coalesce((x->>'ganzes_thema')::boolean, false);
    v_et := case when coalesce((x->>'ganzes_thema')::boolean, false) then array['*']
                 when jsonb_typeof(x->'etappen') = 'array' then array(select jsonb_array_elements_text(x->'etappen'))
                 when jsonb_typeof(x->'etappen') = 'string' then array(select trim(s) from unnest(string_to_array(x->>'etappen', ',')) s where trim(s) <> '') end;
    if not exists (select 1 from schule.zuordnung z where z.eintrag_id = v_e and z.thema_id = v_t) then
      v_fehlt := v_fehlt || jsonb_build_object('eintrag_id', v_e, 'thema_id', v_t); continue;
    end if;
    if v_hat_et then
      select array_agg(q->>'lernziel') into v_bekannt from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) q
       where e.id = schule.thema_einheit(v_t);
      if v_et is null or cardinality(v_et) = 0 or ('*' = any(v_et) and cardinality(v_et) > 1)
         or exists (select 1 from unnest(v_et) s where s <> '*' and not s = any(coalesce(v_bekannt, '{}'))) then
        v_unbekannt := v_unbekannt || jsonb_build_object('eintrag_id', v_e, 'thema_id', v_t,
                         'etappen', to_jsonb(array(select s from unnest(coalesce(v_et, '{}')) s where s <> '*' and not s = any(coalesce(v_bekannt, '{}')))),
                         'grund', case when v_et is null or cardinality(v_et) = 0 then 'leer' when '*' = any(v_et) and cardinality(v_et) > 1 then '* nur allein'
                                       else 'unbekannter Schlüssel' end);
        continue;   -- B5: diese Zuordnung bleibt ganz unverändert
      end if;
    end if;
    update schule.zuordnung z set rolle = case when x ? 'rolle' then v_r else z.rolle end,
                                  etappen = case when v_hat_et then v_et else z.etappen end
     where z.eintrag_id = v_e and z.thema_id = v_t
       and (z.rolle is distinct from case when x ? 'rolle' then v_r else z.rolle end or z.etappen is distinct from case when v_hat_et then v_et else z.etappen end);
    get diagnostics v_n = row_count;
    if v_n > 0 then v_gesetzt := v_gesetzt + 1; else v_gleich := v_gleich + 1; end if;
  end loop;
  return jsonb_build_object('gesetzt', v_gesetzt, 'gleich', v_gleich, 'ohne_zuordnung', v_fehlt, 'unbekannte_etappen', v_unbekannt);
end $function$;
revoke all on function schule.lehrplan_rolle_setzen(jsonb) from public, anon, authenticated;

-- Alle drei Schularten aus lk_daten_2211.json (punkte[] mit bezug 'haupt': eintrag_id, thema, rolle, etappen). Rolle und Etappen der Realschule aus
-- der ersten Fassung (rs_pruefung_2211.json) sind damit ersetzt. Gruppe II/III ist im Korrektur-SQL nicht eingespielt – deren Punkte treffen nur,
-- wo die Zuordnung schon so besteht; der Rest steht unter „ohne Zuordnung“.
do $$
declare r jsonb;
begin
  r := schule.lehrplan_rolle_setzen($json$[{"eintrag_id":3,"thema_id":15,"rolle":"neu","etappen":["unendlich","ziffern_zu_zahlwort","zahlwort_zu_ziffern"]},{"eintrag_id":4,"thema_id":15,"rolle":"neu","etappen":["stellenwert","roemisch_schreiben","roemisch_system"]},{"eintrag_id":5,"thema_id":15,"rolle":"neu","etappen":["strahl_ablesen","strahl_eintragen","vergleichen"]},{"eintrag_id":6,"thema_id":15,"rolle":"neu","etappen":["runden_regel","runden_uebertrag","runden_sinnvoll"]},{"eintrag_id":7,"thema_id":16,"rolle":"neu","etappen":["deuten","sach"]},{"eintrag_id":8,"thema_id":16,"rolle":"neu","etappen":["zahlengerade","ordnen","betrag"]},{"eintrag_id":9,"thema_id":16,"rolle":"neu","etappen":["verstehen"]},{"eintrag_id":11,"thema_id":16,"rolle":"neu","etappen":["schriftlich_plus_minus"]},{"eintrag_id":12,"thema_id":16,"rolle":"neu","etappen":["addieren","subtrahieren","ketten"]},{"eintrag_id":13,"thema_id":1,"rolle":"neu","etappen":["zwei_schritte","probe"]},{"eintrag_id":14,"thema_id":18,"rolle":"neu","etappen":["vorteil","differenz_summe"]},{"eintrag_id":15,"thema_id":18,"rolle":"neu","etappen":["klammern","termaufbau"]},{"eintrag_id":17,"thema_id":42,"rolle":"neu","etappen":["koordinaten","strecken"]},{"eintrag_id":18,"thema_id":42,"rolle":"neu","etappen":["lagebeziehungen","kreis_lage"]},{"eintrag_id":19,"thema_id":73,"rolle":"neu","etappen":["kreislinie","parallelen","zwei_kreise","verknuepfen"]},{"eintrag_id":20,"thema_id":42,"rolle":"neu","etappen":["winkelarten"]},{"eintrag_id":21,"thema_id":42,"rolle":"neu","etappen":["vierecke"]},{"eintrag_id":24,"thema_id":18,"rolle":"neu","etappen":["schriftlich","schriftlich_geteilt","ueberschlag"]},{"eintrag_id":25,"thema_id":17,"rolle":"neu","etappen":["primfaktoren","endziffer","quersumme","teiler","primzahl"]},{"eintrag_id":26,"thema_id":60,"rolle":"neu","etappen":["zaehlprinzip","baumdiagramm","systematisch","grenzen"]},{"eintrag_id":27,"thema_id":18,"rolle":"neu","etappen":["mal_ganz","geteilt_ganz"]},{"eintrag_id":28,"thema_id":67,"rolle":"neu","etappen":["schreibweise","berechnen","quadrat","zehner","negativ"]},{"eintrag_id":29,"thema_id":1,"rolle":"neu","etappen":["zwei_schritte","probe"]},{"eintrag_id":31,"thema_id":18,"rolle":"neu","etappen":["termaufbau","klammern"]},{"eintrag_id":32,"thema_id":18,"rolle":"neu","etappen":["punkt_strich"]},{"eintrag_id":33,"thema_id":18,"rolle":"neu","etappen":["verteilen","vorteil","kopfrechnen"]},{"eintrag_id":34,"thema_id":18,"rolle":"neu","etappen":["sach"]},{"eintrag_id":35,"thema_id":18,"rolle":"neu","etappen":["sach","ueberschlag"]},{"eintrag_id":38,"thema_id":25,"rolle":"neu","etappen":["laenge","masse","zeit","kommaschreibweise"]},{"eintrag_id":39,"thema_id":25,"rolle":"neu","etappen":["rechnen"]},{"eintrag_id":40,"thema_id":25,"rolle":"neu","etappen":["schaetzen"]},{"eintrag_id":41,"thema_id":26,"rolle":"neu","etappen":["einheit","dreisatz","sach","erkennen"]},{"eintrag_id":42,"thema_id":25,"rolle":"neu","etappen":["massstab"]},{"eintrag_id":44,"thema_id":50,"rolle":"neu","etappen":["einheitsquadrate","rechteck"]},{"eintrag_id":45,"thema_id":50,"rolle":"neu","etappen":["einheiten","kommaschreibweise"]},{"eintrag_id":46,"thema_id":50,"rolle":"neu","etappen":["verstehen","sachaufgaben"]},{"eintrag_id":47,"thema_id":50,"rolle":"neu","etappen":["zerlegen"]},{"eintrag_id":48,"thema_id":53,"rolle":"neu","etappen":["oberflaeche","zusammengesetzt","quader"]},{"eintrag_id":51,"thema_id":21,"rolle":"neu","etappen":["anteil_bestimmen","bruchteil_von"]},{"eintrag_id":52,"thema_id":21,"rolle":"neu","etappen":["bruchteil_von","ganzes_bestimmen"]},{"eintrag_id":53,"thema_id":21,"rolle":"neu","etappen":["erweitern","kuerzen","ggt"]},{"eintrag_id":54,"thema_id":21,"rolle":"neu","etappen":["vergleichen","kgv"]},{"eintrag_id":55,"thema_id":22,"rolle":"neu","etappen":["merkwerte"]},{"eintrag_id":56,"thema_id":21,"rolle":"neu","etappen":["zahlbereiche"]},{"eintrag_id":57,"thema_id":21,"rolle":"neu","etappen":["zahlenstrahl","zahlbereiche"]},{"eintrag_id":59,"thema_id":22,"rolle":"neu","etappen":["stellenwerte"]},{"eintrag_id":60,"thema_id":22,"rolle":"neu","etappen":["runden"]},{"eintrag_id":61,"thema_id":21,"rolle":"neu","etappen":["anteil_bestimmen"]},{"eintrag_id":62,"thema_id":22,"rolle":"neu","etappen":["periodisch","bruch_zu_dezimal"]},{"eintrag_id":63,"thema_id":22,"rolle":"neu","etappen":["bruch_zu_dezimal","dezimal_zu_bruch","merkwerte"]},{"eintrag_id":64,"thema_id":22,"rolle":"neu","etappen":["vergleichen_ordnen","verstehen"]},{"eintrag_id":66,"thema_id":23,"rolle":"neu","etappen":["brueche_plus_minus"]},{"eintrag_id":67,"thema_id":23,"rolle":"neu","etappen":["brueche_plus_minus","dezimal_plus_minus","vorzeichen"]},{"eintrag_id":68,"thema_id":23,"rolle":"neu","etappen":["rechenvorteile"]},{"eintrag_id":69,"thema_id":23,"rolle":"neu","etappen":["gemischt"]},{"eintrag_id":70,"thema_id":23,"rolle":"neu","etappen":["fehler_finden"]},{"eintrag_id":72,"thema_id":23,"rolle":"neu","etappen":["brueche_mal","brueche_geteilt","dezimal_mal","dezimal_geteilt"]},{"eintrag_id":73,"thema_id":23,"rolle":"neu","etappen":["potenzen"]},{"eintrag_id":74,"thema_id":30,"rolle":"neu","etappen":["negativer_exponent","potenz_begriff"]},{"eintrag_id":75,"thema_id":19,"rolle":"neu","etappen":["negativer_exponent","klein_wissenschaftlich","vorsilben_klein"]},{"eintrag_id":76,"thema_id":23,"rolle":"neu","etappen":["rechenvorteile"]},{"eintrag_id":78,"thema_id":23,"rolle":"neu","etappen":["gemischt"]},{"eintrag_id":79,"thema_id":23,"rolle":"neu","etappen":["gemischt"]},{"eintrag_id":80,"thema_id":23,"rolle":"neu","etappen":["rechenvorteile"]},{"eintrag_id":81,"thema_id":23,"rolle":"neu","etappen":["sach"]},{"eintrag_id":82,"thema_id":23,"rolle":"neu","etappen":["sach"]},{"eintrag_id":85,"thema_id":99,"rolle":"neu","etappen":["parallelogramm","dreieck","trapez"]},{"eintrag_id":86,"thema_id":99,"rolle":"neu","etappen":["rueckwaerts","zusammengesetzt"]},{"eintrag_id":87,"thema_id":99,"rolle":"neu","etappen":["zusammengesetzt","verstehen"]},{"eintrag_id":88,"thema_id":99,"rolle":"neu","etappen":["verstehen"]},{"eintrag_id":89,"thema_id":99,"rolle":"neu","etappen":["oberflaeche"]},{"eintrag_id":91,"thema_id":100,"rolle":"neu","etappen":["einheitswuerfel","quader"]},{"eintrag_id":92,"thema_id":100,"rolle":"neu","etappen":["einheitswuerfel","einheiten"]},{"eintrag_id":93,"thema_id":100,"rolle":"neu","etappen":["einheiten","liter"]},{"eintrag_id":94,"thema_id":100,"rolle":"neu","etappen":["quader","rueckwaerts"]},{"eintrag_id":95,"thema_id":100,"rolle":"neu","etappen":["verstehen"]},{"eintrag_id":96,"thema_id":100,"rolle":"neu","etappen":["zusammengesetzt"]},{"eintrag_id":98,"thema_id":24,"rolle":"neu","etappen":["prozentwert","prozentsatz","grundwert","rabatt_aufschlag"]},{"eintrag_id":99,"thema_id":24,"rolle":"neu","etappen":["verstehen"]},{"eintrag_id":100,"thema_id":24,"rolle":"neu","etappen":["prozent_bedeutung"]},{"eintrag_id":101,"thema_id":57,"rolle":"neu","etappen":["absolute_haeufigkeit","relative_haeufigkeit"]},{"eintrag_id":102,"thema_id":57,"rolle":"neu","etappen":["saeulendiagramm","kreisdiagramm"]},{"eintrag_id":103,"thema_id":57,"rolle":"neu","etappen":["irrefuehrend","tabelle_auswerten"]},{"eintrag_id":104,"thema_id":58,"rolle":"neu","etappen":["mittelwert","mittel_tabelle","mittel_rueckwaerts"]},{"eintrag_id":107,"thema_id":28,"rolle":"neu","etappen":["uebersetzen","sachsituation","deuten"]},{"eintrag_id":108,"thema_id":28,"rolle":"neu","etappen":["termwert"]},{"eintrag_id":109,"thema_id":28,"rolle":"neu","etappen":["termwert"]},{"eintrag_id":110,"thema_id":28,"rolle":"neu","etappen":["struktur"]},{"eintrag_id":112,"thema_id":102,"rolle":"neu","etappen":["mal_gleiche_basis","gleicher_exponent","potenz_von_potenz","geteilt_gleiche_basis","anwenden"]},{"eintrag_id":113,"thema_id":29,"rolle":"neu","etappen":["zusammenfassen","produkte","minusklammer","aequivalenz"]},{"eintrag_id":114,"thema_id":29,"rolle":"neu","etappen":["aequivalenz"]},{"eintrag_id":115,"thema_id":29,"rolle":"neu","etappen":["ausklammern","ausmultiplizieren"]},{"eintrag_id":116,"thema_id":29,"rolle":"neu","etappen":["binomisch","summe_mal_summe"]},{"eintrag_id":117,"thema_id":29,"rolle":"neu","etappen":["aequivalenz"]},{"eintrag_id":120,"thema_id":46,"rolle":"neu","etappen":["achsenspiegelung","punktspiegelung","symmetrie"]},{"eintrag_id":121,"thema_id":46,"rolle":"neu","etappen":["mittelsenkrechte","winkelhalbierende"]},{"eintrag_id":122,"thema_id":46,"rolle":"neu","etappen":["mittelsenkrechte"]},{"eintrag_id":123,"thema_id":46,"rolle":"neu","etappen":["vierecke_ordnen"]},{"eintrag_id":124,"thema_id":46,"rolle":"neu","etappen":["symmetrie"]},{"eintrag_id":126,"thema_id":98,"rolle":"neu","etappen":["scheitel_neben","stufen_wechsel"]},{"eintrag_id":127,"thema_id":98,"rolle":"neu","etappen":["innenwinkelsumme"]},{"eintrag_id":128,"thema_id":98,"rolle":"neu","etappen":["vieleck"]},{"eintrag_id":129,"thema_id":98,"rolle":"neu","etappen":["figuren","aussenwinkel"]},{"eintrag_id":130,"thema_id":98,"rolle":"neu","etappen":["parallel_pruefen"]},{"eintrag_id":132,"thema_id":2,"rolle":"neu","etappen":["sach"]},{"eintrag_id":133,"thema_id":2,"rolle":"neu","etappen":["waage","beide_seiten","klammern","sonderfaelle"]},{"eintrag_id":134,"thema_id":2,"rolle":"neu","etappen":["probe"]},{"eintrag_id":135,"thema_id":2,"rolle":"neu","etappen":["sach"]},{"eintrag_id":136,"thema_id":94,"rolle":"neu","etappen":["faktor","vermehrt","vermindert","zurueck","prozentsatz","mehrfach"]},{"eintrag_id":137,"thema_id":94,"rolle":"neu","etappen":["argumente"]},{"eintrag_id":139,"thema_id":95,"rolle":"neu","etappen":["median","mittel_median"]},{"eintrag_id":140,"thema_id":95,"rolle":"neu","etappen":["quartile","kennwerte"]},{"eintrag_id":141,"thema_id":95,"rolle":"neu","etappen":["boxplot"]},{"eintrag_id":142,"thema_id":95,"rolle":"neu","etappen":["vergleichen"]},{"eintrag_id":144,"thema_id":44,"rolle":"neu","etappen":["kongruenzsatz"]},{"eintrag_id":145,"thema_id":44,"rolle":"neu","etappen":["kongruenzsatz","konstruierbar"]},{"eintrag_id":146,"thema_id":44,"rolle":"neu","etappen":["gleichschenklig"]},{"eintrag_id":147,"thema_id":44,"rolle":"neu","etappen":["satz_kehrsatz"]},{"eintrag_id":148,"thema_id":45,"rolle":"neu","etappen":["beweis","umkreis_inkreis"]},{"eintrag_id":149,"thema_id":45,"rolle":"neu","etappen":["thales","umkehrung"]},{"eintrag_id":150,"thema_id":45,"rolle":"neu","etappen":["tangente","lage"]},{"eintrag_id":151,"thema_id":44,"rolle":"neu","etappen":["planfigur","konstruierbar"]},{"eintrag_id":152,"thema_id":44,"rolle":"neu","etappen":["planfigur"]},{"eintrag_id":154,"thema_id":32,"rolle":"neu","etappen":["wertetabelle","mengen","sachzusammenhang"]},{"eintrag_id":155,"thema_id":32,"rolle":"neu","etappen":["eindeutig"]},{"eintrag_id":156,"thema_id":32,"rolle":"neu","etappen":["eindeutig"]},{"eintrag_id":157,"thema_id":32,"rolle":"neu","etappen":["graph_lesen"]},{"eintrag_id":158,"thema_id":32,"rolle":"neu","etappen":["nullstellen","punkt_graph"]},{"eintrag_id":159,"thema_id":32,"rolle":"neu","etappen":["sachzusammenhang"]},{"eintrag_id":161,"thema_id":33,"rolle":"neu","etappen":["ablesen","wirkung"]},{"eintrag_id":162,"thema_id":33,"rolle":"neu","etappen":["graph_ablesen","ablesen"]},{"eintrag_id":163,"thema_id":33,"rolle":"neu","etappen":["aufstellen","zwei_punkte"]},{"eintrag_id":164,"thema_id":33,"rolle":"neu","etappen":["schnittpunkte"]},{"eintrag_id":165,"thema_id":33,"rolle":"neu","etappen":["schnittpunkte"]},{"eintrag_id":166,"thema_id":33,"rolle":"neu","etappen":["deuten"]},{"eintrag_id":167,"thema_id":3,"rolle":"neu","etappen":["umformen","umdrehen","intervall","grafisch"]},{"eintrag_id":168,"thema_id":33,"rolle":"neu","etappen":["proportional"]},{"eintrag_id":170,"thema_id":34,"rolle":"neu","etappen":["definitionsmenge","achsenpunkte"]},{"eintrag_id":171,"thema_id":34,"rolle":"neu","etappen":["parameter"]},{"eintrag_id":172,"thema_id":34,"rolle":"neu","etappen":["asymptoten","beurteilen"]},{"eintrag_id":173,"thema_id":93,"rolle":"neu","etappen":["erkennen","produkt","graph","unterscheiden","dreisatz"]},{"eintrag_id":175,"thema_id":31,"rolle":"neu","etappen":["definitionsmenge","kuerzen","erweitern"]},{"eintrag_id":176,"thema_id":31,"rolle":"neu","etappen":["addieren","multiplizieren","fehler_finden"]},{"eintrag_id":177,"thema_id":103,"rolle":"neu","etappen":["warum_gilt","gleiche_basis_ganz","exponent_und_potenz","terme_vereinfachen"]},{"eintrag_id":178,"thema_id":5,"rolle":"neu","etappen":["definitionsmenge","ein_bruch","ueber_kreuz","hauptnenner","scheinloesung","graphisch"]},{"eintrag_id":179,"thema_id":4,"rolle":"neu","etappen":["ein_schritt","zwei_schritte","einsetzen","geometrie"]},{"eintrag_id":181,"thema_id":61,"rolle":"neu","etappen":["begriffe","gegenereignis"]},{"eintrag_id":182,"thema_id":61,"rolle":"neu","etappen":["rel_haeufigkeit"]},{"eintrag_id":183,"thema_id":61,"rolle":"neu","etappen":["grosse_zahlen"]},{"eintrag_id":184,"thema_id":61,"rolle":"neu","etappen":["laplace_pruefen"]},{"eintrag_id":185,"thema_id":61,"rolle":"neu","etappen":["laplace"]},{"eintrag_id":187,"thema_id":6,"rolle":"neu","etappen":["sachaufgabe"]},{"eintrag_id":188,"thema_id":6,"rolle":"neu","etappen":["grafisch","einsetzen","gleichsetzen","addition"]},{"eintrag_id":189,"thema_id":6,"rolle":"neu","etappen":["verfahren"]},{"eintrag_id":190,"thema_id":6,"rolle":"neu","etappen":["loesbarkeit","pruefen"]},{"eintrag_id":192,"thema_id":51,"rolle":"neu","etappen":["umfang","flaeche"]},{"eintrag_id":193,"thema_id":51,"rolle":"neu","etappen":["exakt"]},{"eintrag_id":194,"thema_id":51,"rolle":"neu","etappen":["verstehen"]},{"eintrag_id":195,"thema_id":52,"rolle":"neu","etappen":["prisma","netz","zylinder","schraegbild"]},{"eintrag_id":196,"thema_id":101,"rolle":"neu","etappen":["zylinder_oberflaeche"]},{"eintrag_id":197,"thema_id":101,"rolle":"neu","etappen":["prisma_volumen","zylinder_volumen"]},{"eintrag_id":198,"thema_id":101,"rolle":"neu","etappen":["sach","prisma_oberflaeche","prisma_umstellen","verstehen"]},{"eintrag_id":200,"thema_id":68,"rolle":"neu","etappen":["quadratwurzel","wurzel_dezimal"]},{"eintrag_id":201,"thema_id":68,"rolle":"neu","etappen":["abschaetzen"]},{"eintrag_id":202,"thema_id":20,"rolle":"neu","etappen":["zahlarten"]},{"eintrag_id":203,"thema_id":20,"rolle":"neu","etappen":["zahlarten"]},{"eintrag_id":204,"thema_id":20,"rolle":"neu","etappen":["heron","eingrenzen"]},{"eintrag_id":205,"thema_id":20,"rolle":"neu","etappen":["wurzel_mal","zusammenfassen"]},{"eintrag_id":206,"thema_id":20,"rolle":"neu","etappen":["nenner_rational","teilweise"]},{"eintrag_id":207,"thema_id":68,"rolle":"neu","etappen":["wurzel_deuten"]},{"eintrag_id":210,"thema_id":35,"rolle":"neu","etappen":["parameter","spiegeln","scheitel"]},{"eintrag_id":211,"thema_id":35,"rolle":"neu","etappen":["nullstellen"]},{"eintrag_id":212,"thema_id":35,"rolle":"neu","etappen":["umformen"]},{"eintrag_id":213,"thema_id":35,"rolle":"neu","etappen":["scheitel","punkte"]},{"eintrag_id":214,"thema_id":8,"rolle":"neu","etappen":["reinquadratisch","ausklammern","faktorisieren","ergaenzung","loesungsformel"]},{"eintrag_id":215,"thema_id":8,"rolle":"neu","etappen":["diskriminante"]},{"eintrag_id":216,"thema_id":35,"rolle":"neu","etappen":["bestimmen"]},{"eintrag_id":218,"thema_id":7,"rolle":"neu","etappen":["pruefen","stufenform","eliminieren","loesen"]},{"eintrag_id":219,"thema_id":35,"rolle":"neu","etappen":["bestimmen"]},{"eintrag_id":220,"thema_id":8,"rolle":"neu","etappen":["bruchgleichung"]},{"eintrag_id":221,"thema_id":35,"rolle":"neu","etappen":["extremwert"]},{"eintrag_id":222,"thema_id":35,"rolle":"neu","etappen":["extremwert"]},{"eintrag_id":224,"thema_id":63,"rolle":"neu","etappen":["elemente","schnitt","venn","vierfeld"]},{"eintrag_id":225,"thema_id":63,"rolle":"neu","etappen":["verknuepfen","mengen_verstehen"]},{"eintrag_id":226,"thema_id":63,"rolle":"neu","etappen":["tafel_wkeit"]},{"eintrag_id":227,"thema_id":63,"rolle":"neu","etappen":["additionssatz"]},{"eintrag_id":228,"thema_id":63,"rolle":"neu","etappen":["tafel_wkeit","additionssatz","verstehen"]},{"eintrag_id":230,"thema_id":47,"rolle":"neu","etappen":["aehnlich"]},{"eintrag_id":231,"thema_id":47,"rolle":"neu","etappen":["strahlensatz1","strahlensatz2","anwendung"]},{"eintrag_id":232,"thema_id":47,"rolle":"neu","etappen":["anwendung"]},{"eintrag_id":233,"thema_id":47,"rolle":"neu","etappen":["flaeche_volumen"]},{"eintrag_id":235,"thema_id":36,"rolle":"neu","etappen":["werte","symmetrie","verlauf","parameter"]},{"eintrag_id":236,"thema_id":9,"rolle":"neu","etappen":["gerade","ungerade","umformen"]},{"eintrag_id":237,"thema_id":9,"rolle":"neu","etappen":["anzahl"]},{"eintrag_id":238,"thema_id":96,"rolle":"neu","etappen":["umwandeln","potenz_wert","nte_wurzel"]},{"eintrag_id":239,"thema_id":96,"rolle":"neu","etappen":["zusammenfassen"]},{"eintrag_id":241,"thema_id":54,"rolle":"neu","etappen":["umkehrung"]},{"eintrag_id":242,"thema_id":54,"rolle":"neu","etappen":["hypotenuse","kathete"]},{"eintrag_id":243,"thema_id":54,"rolle":"neu","etappen":["anwendung","koordinaten","raum"]},{"eintrag_id":246,"thema_id":55,"rolle":"neu","etappen":["seiten","verhaeltnisse"]},{"eintrag_id":247,"thema_id":55,"rolle":"neu","etappen":["seite","winkel"]},{"eintrag_id":248,"thema_id":55,"rolle":"neu","etappen":["beziehungen"]},{"eintrag_id":249,"thema_id":55,"rolle":"neu","etappen":["anwendung"]},{"eintrag_id":251,"thema_id":56,"rolle":"neu","etappen":["einheitskreis"]},{"eintrag_id":252,"thema_id":56,"rolle":"neu","etappen":["einheitskreis"]},{"eintrag_id":253,"thema_id":14,"rolle":"neu","etappen":["sinus","kosinus","anzahl"]},{"eintrag_id":254,"thema_id":56,"rolle":"neu","etappen":["sinussatz_seite","sinussatz_winkel"]},{"eintrag_id":255,"thema_id":56,"rolle":"neu","etappen":["kosinussatz_seite","kosinussatz_winkel"]},{"eintrag_id":256,"thema_id":56,"rolle":"neu","etappen":["satz_waehlen","anwendung","flaeche"]},{"eintrag_id":258,"thema_id":37,"rolle":"neu","etappen":["linear_oder_exponentiell","faktor"]},{"eintrag_id":259,"thema_id":37,"rolle":"neu","etappen":["graph","werte"]},{"eintrag_id":260,"thema_id":10,"rolle":"neu","etappen":["logarithmus"]},{"eintrag_id":261,"thema_id":10,"rolle":"neu","etappen":["gleiche_basis","mit_log_loesen","potenzregel"]},{"eintrag_id":262,"thema_id":37,"rolle":"neu","etappen":["modell"]},{"eintrag_id":264,"thema_id":62,"rolle":"neu","etappen":["baum_ergaenzen","ohne_zuruecklegen"]},{"eintrag_id":265,"thema_id":62,"rolle":"neu","etappen":["pfad_mult","pfad_add","gegenereignis","unabhaengig"]},{"eintrag_id":266,"thema_id":64,"rolle":"neu","etappen":["zufallsgeraet","regel","zufallsziffern","auswerten","beurteilen"]},{"eintrag_id":267,"thema_id":64,"rolle":"neu","etappen":["monte_carlo"]},{"eintrag_id":269,"thema_id":38,"rolle":"neu","etappen":["bogenmass"]},{"eintrag_id":270,"thema_id":38,"rolle":"neu","etappen":["werte"]},{"eintrag_id":271,"thema_id":38,"rolle":"neu","etappen":["periode"]},{"eintrag_id":272,"thema_id":38,"rolle":"neu","etappen":["periode","eigenschaften"]},{"eintrag_id":273,"thema_id":38,"rolle":"neu","etappen":["parameter","verschiebung_x"]},{"eintrag_id":274,"thema_id":38,"rolle":"neu","etappen":["zuordnen"]},{"eintrag_id":275,"thema_id":38,"rolle":"neu","etappen":["anwendung"]},{"eintrag_id":277,"thema_id":39,"rolle":"neu","etappen":["grad","randverhalten","ausmultiplizieren"]},{"eintrag_id":278,"thema_id":11,"rolle":"neu","etappen":["ausklammern","nullprodukt","substitution","vielfachheit"]},{"eintrag_id":279,"thema_id":39,"rolle":"neu","etappen":["graph_term","term_bestimmen"]},{"eintrag_id":280,"thema_id":39,"rolle":"neu","etappen":["symmetrie"]},{"eintrag_id":282,"thema_id":91,"rolle":"neu","etappen":["pyramide"]},{"eintrag_id":283,"thema_id":91,"rolle":"neu","etappen":["rotation"]},{"eintrag_id":284,"thema_id":92,"rolle":"neu","etappen":["kegel_mantel"]},{"eintrag_id":285,"thema_id":101,"rolle":"weitergefuehrt","etappen":["prisma_volumen"]},{"eintrag_id":286,"thema_id":92,"rolle":"neu","etappen":["pyr_volumen"]},{"eintrag_id":287,"thema_id":92,"rolle":"neu","etappen":["kegel_volumen"]},{"eintrag_id":288,"thema_id":92,"rolle":"neu","etappen":["kugel"]},{"eintrag_id":289,"thema_id":92,"rolle":"neu","etappen":["sachkontext","verstehen"]},{"eintrag_id":292,"thema_id":15,"rolle":"neu","etappen":["unendlich"]},{"eintrag_id":293,"thema_id":15,"rolle":"neu","etappen":["stellenwert"]},{"eintrag_id":294,"thema_id":15,"rolle":"neu","etappen":["strahl_ablesen","vergleichen"]},{"eintrag_id":295,"thema_id":15,"rolle":"neu","etappen":["runden_regel","runden_uebertrag","runden_sinnvoll"]},{"eintrag_id":297,"thema_id":15,"rolle":"neu","etappen":["dualsystem","roemisch_schreiben"]},{"eintrag_id":298,"thema_id":15,"rolle":"neu","etappen":["roemisch_system"]},{"eintrag_id":300,"thema_id":18,"rolle":"neu","etappen":["schriftlich","schriftlich_geteilt"]},{"eintrag_id":301,"thema_id":18,"rolle":"neu","etappen":["sach","ueberschlag"]},{"eintrag_id":302,"thema_id":18,"rolle":"neu","etappen":["vorteil","verteilen","kopfrechnen"]},{"eintrag_id":303,"thema_id":67,"rolle":"neu","etappen":["zehner"]},{"eintrag_id":304,"thema_id":67,"rolle":"neu","etappen":["schreibweise","berechnen","quadrat"]},{"eintrag_id":305,"thema_id":17,"rolle":"neu","etappen":["teiler","vielfache","primfaktoren"]},{"eintrag_id":307,"thema_id":60,"rolle":"neu","etappen":["zaehlprinzip","systematisch"]},{"eintrag_id":308,"thema_id":60,"rolle":"neu","etappen":["baumdiagramm"]},{"eintrag_id":310,"thema_id":16,"rolle":"neu","etappen":["deuten"]},{"eintrag_id":311,"thema_id":16,"rolle":"neu","etappen":["deuten","sach"]},{"eintrag_id":312,"thema_id":16,"rolle":"neu","etappen":["betrag"]},{"eintrag_id":313,"thema_id":16,"rolle":"neu","etappen":["zahlengerade","ordnen"]},{"eintrag_id":314,"thema_id":16,"rolle":"neu","etappen":["addieren","subtrahieren"]},{"eintrag_id":315,"thema_id":16,"rolle":"neu","etappen":["ketten"]},{"eintrag_id":316,"thema_id":16,"rolle":"neu","etappen":["sach","ketten"]},{"eintrag_id":318,"thema_id":42,"rolle":"neu","etappen":["kreis_lage"]},{"eintrag_id":319,"thema_id":42,"rolle":"neu","etappen":["lagebeziehungen"]},{"eintrag_id":320,"thema_id":42,"rolle":"neu","etappen":["vierecke"]},{"eintrag_id":321,"thema_id":42,"rolle":"neu","etappen":["koordinaten","strecken"]},{"eintrag_id":322,"thema_id":42,"rolle":"neu","etappen":["winkelarten"]},{"eintrag_id":323,"thema_id":42,"rolle":"neu","etappen":["winkelarten"]},{"eintrag_id":324,"thema_id":52,"rolle":"neu","etappen":["prisma"]},{"eintrag_id":325,"thema_id":52,"rolle":"neu","etappen":["netz","schraegbild"]},{"eintrag_id":326,"thema_id":52,"rolle":"neu","etappen":["ansichten"]},{"eintrag_id":328,"thema_id":25,"rolle":"neu","etappen":["schaetzen"]},{"eintrag_id":329,"thema_id":25,"rolle":"neu","etappen":["laenge","masse","zeit"]},{"eintrag_id":330,"thema_id":25,"rolle":"neu","etappen":["kommaschreibweise"]},{"eintrag_id":331,"thema_id":25,"rolle":"neu","etappen":["massstab"]},{"eintrag_id":332,"thema_id":26,"rolle":"neu","etappen":["dreisatz","einheit"]},{"eintrag_id":333,"thema_id":25,"rolle":"neu","etappen":["rechnen"]},{"eintrag_id":335,"thema_id":50,"rolle":"neu","etappen":["rechteck"]},{"eintrag_id":336,"thema_id":50,"rolle":"neu","etappen":["sachaufgaben"]},{"eintrag_id":337,"thema_id":50,"rolle":"neu","etappen":["zerlegen"]},{"eintrag_id":338,"thema_id":50,"rolle":"neu","etappen":["einheiten"]},{"eintrag_id":339,"thema_id":50,"rolle":"neu","etappen":["rechteck"]},{"eintrag_id":340,"thema_id":50,"rolle":"neu","etappen":["zerlegen"]},{"eintrag_id":342,"thema_id":57,"rolle":"neu","etappen":["tabelle_auswerten","absolute_haeufigkeit"]},{"eintrag_id":343,"thema_id":57,"rolle":"neu","etappen":["tabelle_auswerten"]},{"eintrag_id":344,"thema_id":57,"rolle":"neu","etappen":["irrefuehrend"]},{"eintrag_id":346,"thema_id":21,"rolle":"neu","etappen":["zahlbereiche"]},{"eintrag_id":347,"thema_id":21,"rolle":"neu","etappen":["gemischte_zahlen","anteil_bestimmen"]},{"eintrag_id":348,"thema_id":21,"rolle":"neu","etappen":["bruchteil_von","ganzes_bestimmen"]},{"eintrag_id":349,"thema_id":21,"rolle":"neu","etappen":["erweitern","kuerzen","ggt"]},{"eintrag_id":350,"thema_id":22,"rolle":"neu","etappen":["stellenwerte","runden"]},{"eintrag_id":351,"thema_id":22,"rolle":"neu","etappen":["periodisch"]},{"eintrag_id":352,"thema_id":22,"rolle":"neu","etappen":["bruch_zu_dezimal","dezimal_zu_bruch","merkwerte"]},{"eintrag_id":353,"thema_id":21,"rolle":"neu","etappen":["vergleichen","kgv"]},{"eintrag_id":354,"thema_id":21,"rolle":"neu","etappen":["zahlenstrahl","zahlbereiche"]},{"eintrag_id":355,"thema_id":23,"rolle":"neu","etappen":["brueche_plus_minus","dezimal_plus_minus","brueche_mal","brueche_geteilt","dezimal_mal","dezimal_geteilt"]},{"eintrag_id":356,"thema_id":23,"rolle":"neu","etappen":["vorzeichen","rechenvorteile"]},{"eintrag_id":357,"thema_id":23,"rolle":"neu","etappen":["sach"]},{"eintrag_id":359,"thema_id":46,"rolle":"neu","etappen":["achsenspiegelung","eigenschaften"]},{"eintrag_id":360,"thema_id":46,"rolle":"neu","etappen":["achsenspiegelung"]},{"eintrag_id":361,"thema_id":46,"rolle":"neu","etappen":["mittelsenkrechte","winkelhalbierende"]},{"eintrag_id":362,"thema_id":46,"rolle":"neu","etappen":["symmetrie"]},{"eintrag_id":363,"thema_id":46,"rolle":"neu","etappen":["symmetrie","vierecke_ordnen"]},{"eintrag_id":365,"thema_id":99,"rolle":"neu","etappen":["verstehen"]},{"eintrag_id":366,"thema_id":99,"rolle":"neu","etappen":["parallelogramm","dreieck","trapez","drachen_raute"]},{"eintrag_id":367,"thema_id":99,"rolle":"neu","etappen":["dreieck"]},{"eintrag_id":368,"thema_id":99,"rolle":"neu","etappen":["zusammengesetzt"]},{"eintrag_id":369,"thema_id":99,"rolle":"neu","etappen":["rueckwaerts","zusammengesetzt"]},{"eintrag_id":370,"thema_id":53,"rolle":"neu","etappen":["oberflaeche","quader","sachaufgaben"]},{"eintrag_id":372,"thema_id":100,"rolle":"neu","etappen":["einheitswuerfel"]},{"eintrag_id":373,"thema_id":100,"rolle":"neu","etappen":["einheiten","liter"]},{"eintrag_id":374,"thema_id":100,"rolle":"neu","etappen":["quader","zusammengesetzt"]},{"eintrag_id":375,"thema_id":100,"rolle":"neu","etappen":["rueckwaerts","verstehen"]},{"eintrag_id":377,"thema_id":28,"rolle":"neu","etappen":["uebersetzen","sachsituation"]},{"eintrag_id":378,"thema_id":28,"rolle":"neu","etappen":["deuten","struktur"]},{"eintrag_id":379,"thema_id":28,"rolle":"neu","etappen":["termwert"]},{"eintrag_id":380,"thema_id":28,"rolle":"neu","etappen":["deuten"]},{"eintrag_id":381,"thema_id":1,"rolle":"neu","etappen":["aufstellen","zwei_schritte"]},{"eintrag_id":382,"thema_id":1,"rolle":"neu","etappen":["waage"]},{"eintrag_id":383,"thema_id":1,"rolle":"neu","etappen":["aufstellen","probe"]},{"eintrag_id":385,"thema_id":26,"rolle":"weitergefuehrt","etappen":["erkennen"]},{"eintrag_id":386,"thema_id":26,"rolle":"weitergefuehrt","etappen":["pruefen","erkennen"]},{"eintrag_id":387,"thema_id":26,"rolle":"weitergefuehrt","etappen":["vervielfachen"]},{"eintrag_id":388,"thema_id":26,"rolle":"weitergefuehrt","etappen":["dreisatz","einheit"]},{"eintrag_id":389,"thema_id":24,"rolle":"neu","etappen":["prozent_bedeutung"]},{"eintrag_id":390,"thema_id":24,"rolle":"neu","etappen":["prozentwert","prozentsatz","grundwert"]},{"eintrag_id":528,"thema_id":15,"rolle":"neu","etappen":["stellenwert","zahlwort_zu_ziffern","ziffern_zu_zahlwort","vergleichen"]},{"eintrag_id":529,"thema_id":15,"rolle":"neu","etappen":["stellenwert"]},{"eintrag_id":530,"thema_id":15,"rolle":"neu","etappen":["dualsystem"]},{"eintrag_id":531,"thema_id":67,"rolle":"neu","etappen":["schreibweise","berechnen","quadrat"]},{"eintrag_id":532,"thema_id":17,"rolle":"neu","etappen":["teiler","vielfache","primzahl","primfaktoren"]},{"eintrag_id":533,"thema_id":17,"rolle":"neu","etappen":["primfaktoren"]},{"eintrag_id":534,"thema_id":17,"rolle":"neu","etappen":["endziffer","quersumme","neunerregel"]},{"eintrag_id":535,"thema_id":18,"rolle":"neu","etappen":["punkt_strich","klammern"]},{"eintrag_id":536,"thema_id":15,"rolle":"neu","etappen":["roemisch_schreiben","roemisch_system"]},{"eintrag_id":537,"thema_id":24,"rolle":"neu","etappen":["prozent_bedeutung"]},{"eintrag_id":538,"thema_id":24,"rolle":"neu","etappen":["prozent_bedeutung"]},{"eintrag_id":539,"thema_id":24,"rolle":"neu","etappen":["prozent_bedeutung"]},{"eintrag_id":540,"thema_id":24,"rolle":"neu","etappen":["prozentwert","prozentsatz","grundwert"]},{"eintrag_id":541,"thema_id":24,"rolle":"neu","etappen":["rabatt_aufschlag"]},{"eintrag_id":542,"thema_id":28,"rolle":"neu","etappen":["muster"]},{"eintrag_id":543,"thema_id":29,"rolle":"neu","etappen":["zusammenfassen","produkte"]},{"eintrag_id":544,"thema_id":28,"rolle":"neu","etappen":["muster","uebersetzen"]},{"eintrag_id":545,"thema_id":32,"rolle":"neu","etappen":["wertetabelle","funktionswert"]},{"eintrag_id":546,"thema_id":1,"rolle":"neu","etappen":["waage","zwei_schritte","probe","aufstellen"]},{"eintrag_id":547,"thema_id":28,"rolle":"neu","etappen":["muster"]},{"eintrag_id":548,"thema_id":42,"rolle":"neu","etappen":["lagebeziehungen"]},{"eintrag_id":549,"thema_id":42,"rolle":"neu","etappen":["winkelarten"]},{"eintrag_id":550,"thema_id":43,"rolle":"neu","etappen":["kreuzung","ergaenzen","um_punkt"]},{"eintrag_id":551,"thema_id":42,"rolle":"neu","etappen":["verstehen"]},{"eintrag_id":552,"thema_id":98,"rolle":"neu","etappen":["innenwinkelsumme","aussenwinkel"]},{"eintrag_id":553,"thema_id":21,"rolle":"neu","etappen":["anteil_bestimmen","bruchteil_von","gemischte_zahlen"]},{"eintrag_id":554,"thema_id":21,"rolle":"neu","etappen":["vergleichen","erweitern","kuerzen"]},{"eintrag_id":555,"thema_id":23,"rolle":"neu","etappen":["brueche_mal","brueche_geteilt"]},{"eintrag_id":556,"thema_id":23,"rolle":"neu","etappen":["brueche_plus_minus"]},{"eintrag_id":557,"thema_id":23,"rolle":"neu","etappen":["gemischt"]},{"eintrag_id":558,"thema_id":57,"rolle":"neu","etappen":["absolute_haeufigkeit"]},{"eintrag_id":559,"thema_id":57,"rolle":"neu","etappen":["tabelle_auswerten","saeulendiagramm"]},{"eintrag_id":560,"thema_id":57,"rolle":"neu","etappen":["saeulendiagramm","kreisdiagramm"]},{"eintrag_id":561,"thema_id":57,"rolle":"neu","etappen":["tabelle_auswerten"]},{"eintrag_id":562,"thema_id":57,"rolle":"neu","etappen":["irrefuehrend"]},{"eintrag_id":563,"thema_id":63,"rolle":"neu","etappen":["elemente","schnitt","venn","mengen_verstehen"]},{"eintrag_id":564,"thema_id":50,"rolle":"neu","etappen":["zerlegen","rechteck"]},{"eintrag_id":565,"thema_id":53,"rolle":"neu","etappen":["quader"]},{"eintrag_id":566,"thema_id":53,"rolle":"neu","etappen":["quader"]},{"eintrag_id":567,"thema_id":53,"rolle":"neu","etappen":["oberflaeche","quader"]},{"eintrag_id":568,"thema_id":53,"rolle":"neu","etappen":["verstehen"]},{"eintrag_id":569,"thema_id":21,"rolle":"weitergefuehrt","etappen":["verhaeltnis_kuerzen"]},{"eintrag_id":570,"thema_id":21,"rolle":"weitergefuehrt","etappen":["gleichwertig"]},{"eintrag_id":571,"thema_id":21,"rolle":"weitergefuehrt","etappen":["verhaeltnis_kuerzen","gleichwertig"]},{"eintrag_id":572,"thema_id":26,"rolle":"neu","etappen":["pruefen","einheit","dreisatz"]},{"eintrag_id":573,"thema_id":26,"rolle":"neu","etappen":["erkennen","vervielfachen"]},{"eintrag_id":574,"thema_id":61,"rolle":"neu","etappen":["begriffe"]},{"eintrag_id":575,"thema_id":61,"rolle":"neu","etappen":["begriffe"]},{"eintrag_id":576,"thema_id":61,"rolle":"neu","etappen":["laplace"]},{"eintrag_id":577,"thema_id":61,"rolle":"neu","etappen":["laplace"]},{"eintrag_id":578,"thema_id":61,"rolle":"neu","etappen":["gegenereignis"]},{"eintrag_id":579,"thema_id":61,"rolle":"neu","etappen":["rel_haeufigkeit","grosse_zahlen","laplace_pruefen"]},{"eintrag_id":580,"thema_id":61,"rolle":"neu","etappen":["grosse_zahlen"]},{"eintrag_id":581,"thema_id":16,"rolle":"neu","etappen":["deuten","zahlengerade","ordnen"]},{"eintrag_id":582,"thema_id":16,"rolle":"neu","etappen":["betrag"]},{"eintrag_id":583,"thema_id":42,"rolle":"weitergefuehrt","etappen":["koordinaten"]},{"eintrag_id":584,"thema_id":18,"rolle":"weitergefuehrt","etappen":["mal_ganz","geteilt_ganz"]},{"eintrag_id":585,"thema_id":16,"rolle":"neu","etappen":["addieren","subtrahieren","ketten"]},{"eintrag_id":586,"thema_id":18,"rolle":"weitergefuehrt","etappen":["punkt_strich","klammern"]},{"eintrag_id":587,"thema_id":28,"rolle":"weitergefuehrt","etappen":["struktur"]},{"eintrag_id":588,"thema_id":29,"rolle":"weitergefuehrt","etappen":["zusammenfassen","produkte","ausmultiplizieren"]},{"eintrag_id":589,"thema_id":28,"rolle":"weitergefuehrt","etappen":["uebersetzen","sachsituation"]},{"eintrag_id":590,"thema_id":2,"rolle":"neu","etappen":["waage","beide_seiten","klammern"]},{"eintrag_id":591,"thema_id":2,"rolle":"neu","etappen":["sach"]},{"eintrag_id":592,"thema_id":2,"rolle":"neu","etappen":["sach"]},{"eintrag_id":593,"thema_id":3,"rolle":"neu","etappen":["intervall"]},{"eintrag_id":594,"thema_id":3,"rolle":"neu","etappen":["umformen","umdrehen"]},{"eintrag_id":595,"thema_id":50,"rolle":"weitergefuehrt","etappen":["sachaufgaben"]},{"eintrag_id":596,"thema_id":50,"rolle":"weitergefuehrt","etappen":["zerlegen"]},{"eintrag_id":597,"thema_id":51,"rolle":"neu","etappen":["umfang","flaeche"]},{"eintrag_id":598,"thema_id":53,"rolle":"weitergefuehrt","etappen":["oberflaeche"]},{"eintrag_id":599,"thema_id":53,"rolle":"weitergefuehrt","etappen":["quader"]},{"eintrag_id":600,"thema_id":53,"rolle":"weitergefuehrt","etappen":["quader"]},{"eintrag_id":601,"thema_id":26,"rolle":"neu","etappen":["einheit"]},{"eintrag_id":602,"thema_id":25,"rolle":"neu","etappen":["laenge","masse","zeit"]},{"eintrag_id":603,"thema_id":25,"rolle":"neu","etappen":["rechnen"]},{"eintrag_id":604,"thema_id":26,"rolle":"neu","etappen":["einheit","sach"]},{"eintrag_id":605,"thema_id":26,"rolle":"neu","etappen":["sach"]},{"eintrag_id":606,"thema_id":26,"rolle":"neu","etappen":["aenderung"]},{"eintrag_id":607,"thema_id":57,"rolle":"weitergefuehrt","etappen":["tabelle_auswerten"]},{"eintrag_id":608,"thema_id":58,"rolle":"neu","etappen":["mittelwert"]},{"eintrag_id":609,"thema_id":58,"rolle":"neu","etappen":["mittelwert"]},{"eintrag_id":610,"thema_id":95,"rolle":"neu","etappen":["quartile","kennwerte"]},{"eintrag_id":611,"thema_id":95,"rolle":"neu","etappen":["boxplot"]},{"eintrag_id":612,"thema_id":20,"rolle":"neu","etappen":["zahlarten"]},{"eintrag_id":613,"thema_id":20,"rolle":"neu","etappen":["zahlarten"]},{"eintrag_id":614,"thema_id":30,"rolle":"neu","etappen":["potenz_begriff","negativer_exponent"]},{"eintrag_id":615,"thema_id":19,"rolle":"neu","etappen":["gross_wissenschaftlich","klein_wissenschaftlich"]},{"eintrag_id":616,"thema_id":33,"rolle":"neu","etappen":["ablesen","graph_ablesen"]},{"eintrag_id":617,"thema_id":33,"rolle":"neu","etappen":["zwei_punkte","aufstellen"]},{"eintrag_id":618,"thema_id":33,"rolle":"neu","etappen":["schnittpunkte","lage"]},{"eintrag_id":619,"thema_id":6,"rolle":"neu","etappen":["pruefen","grafisch"]},{"eintrag_id":620,"thema_id":2,"rolle":"weitergefuehrt","etappen":["waage","beide_seiten","klammern","sonderfaelle"]},{"eintrag_id":621,"thema_id":6,"rolle":"neu","etappen":["einsetzen","gleichsetzen","addition"]},{"eintrag_id":622,"thema_id":6,"rolle":"neu","etappen":["sachaufgabe"]},{"eintrag_id":623,"thema_id":52,"rolle":"neu","etappen":["prisma","netz","ansichten"]},{"eintrag_id":624,"thema_id":52,"rolle":"neu","etappen":["zylinder"]},{"eintrag_id":625,"thema_id":92,"rolle":"neu","etappen":["kegel_volumen","kegel_mantel"]},{"eintrag_id":626,"thema_id":92,"rolle":"neu","etappen":["pyr_volumen","pyr_oberflaeche"]},{"eintrag_id":627,"thema_id":92,"rolle":"neu","etappen":["kugel"]},{"eintrag_id":628,"thema_id":46,"rolle":"neu","etappen":["achsenspiegelung","verschiebung","drehung"]},{"eintrag_id":629,"thema_id":98,"rolle":"weitergefuehrt","etappen":["parkett"]},{"eintrag_id":630,"thema_id":46,"rolle":"neu","etappen":["eigenschaften","achsenspiegelung","punktspiegelung","drehung","verschiebung"]},{"eintrag_id":631,"thema_id":47,"rolle":"neu","etappen":["streckung","aehnlich"]},{"eintrag_id":632,"thema_id":44,"rolle":"weitergefuehrt","etappen":["kongruenzsatz","konstruierbar"]},{"eintrag_id":633,"thema_id":44,"rolle":"weitergefuehrt","etappen":["satz_kehrsatz"]},{"eintrag_id":634,"thema_id":54,"rolle":"neu","etappen":["hypotenuse","kathete","umkehrung"]},{"eintrag_id":635,"thema_id":55,"rolle":"neu","etappen":["seiten","verhaeltnisse","seite","winkel"]},{"eintrag_id":636,"thema_id":59,"rolle":"neu","etappen":["ablesen"]},{"eintrag_id":637,"thema_id":59,"rolle":"neu","etappen":["zusammenhang"]},{"eintrag_id":638,"thema_id":59,"rolle":"neu","etappen":["gerade","ausreisser"]},{"eintrag_id":639,"thema_id":59,"rolle":"neu","etappen":["kausal"]},{"eintrag_id":641,"thema_id":29,"rolle":"weitergefuehrt","etappen":["binomisch","ausklammern","summe_mal_summe"]},{"eintrag_id":642,"thema_id":32,"rolle":"weitergefuehrt","etappen":["eindeutig","mengen","funktionswert"]},{"eintrag_id":643,"thema_id":33,"rolle":"weitergefuehrt","etappen":["aufstellen","schnittpunkte","lage","deuten"]},{"eintrag_id":644,"thema_id":6,"rolle":"weitergefuehrt","etappen":["grafisch","einsetzen","addition"]},{"eintrag_id":645,"thema_id":49,"rolle":"neu","etappen":["rechnen","inverse"]},{"eintrag_id":646,"thema_id":35,"rolle":"neu","etappen":["scheitel","nullstellen","schnittpunkte"]},{"eintrag_id":647,"thema_id":47,"rolle":"weitergefuehrt","etappen":["aehnlich","strahlensatz1","strahlensatz2"]},{"eintrag_id":648,"thema_id":44,"rolle":"weitergefuehrt","etappen":["kongruenzsatz"]},{"eintrag_id":649,"thema_id":46,"rolle":"weitergefuehrt","etappen":["verschiebung","achsenspiegelung","drehung"]},{"eintrag_id":650,"thema_id":45,"rolle":"neu","etappen":["thales","tangente","lage"]},{"eintrag_id":651,"thema_id":55,"rolle":"weitergefuehrt","etappen":["seite","winkel","anwendung"]},{"eintrag_id":652,"thema_id":37,"rolle":"neu","etappen":["werte","graph","logfunktion"]},{"eintrag_id":653,"thema_id":92,"rolle":"weitergefuehrt","etappen":["pyr_volumen","kegel_volumen","kugel"]},{"eintrag_id":654,"thema_id":56,"rolle":"neu","etappen":["einheitskreis","flaeche","sinussatz_seite","sinussatz_winkel"]},{"eintrag_id":655,"thema_id":20,"rolle":"weitergefuehrt","etappen":["zahlarten","teilweise","nenner_rational"]},{"eintrag_id":656,"thema_id":76,"rolle":"neu","etappen":["arithmetisch","geometrisch","summenzeichen","arith","geom"]},{"eintrag_id":657,"thema_id":63,"rolle":"weitergefuehrt","etappen":["verknuepfen","additionssatz","vierfeld","tafel_wkeit"]},{"eintrag_id":658,"thema_id":59,"rolle":"weitergefuehrt","etappen":["ablesen","zusammenhang","gerade"]},{"eintrag_id":659,"thema_id":65,"rolle":"neu","etappen":["grundbegriffe","euler","kuerzester","spannbaum"]},{"eintrag_id":661,"thema_id":29,"rolle":"weitergefuehrt","etappen":["binomisch","ausklammern","summe_mal_summe"]},{"eintrag_id":662,"thema_id":32,"rolle":"weitergefuehrt","etappen":["eindeutig","mengen","funktionswert"]},{"eintrag_id":663,"thema_id":33,"rolle":"weitergefuehrt","etappen":["aufstellen","lage","schnittpunkte"]},{"eintrag_id":664,"thema_id":6,"rolle":"weitergefuehrt","etappen":["einsetzen","addition","loesbarkeit"]},{"eintrag_id":665,"thema_id":49,"rolle":"neu","etappen":["rechnen","inverse"]},{"eintrag_id":666,"thema_id":39,"rolle":"neu","etappen":["grad","ausmultiplizieren","nullstellen","graph_term"]},{"eintrag_id":667,"thema_id":47,"rolle":"weitergefuehrt","etappen":["aehnlich","strahlensatz1","strahlensatz2"]},{"eintrag_id":668,"thema_id":44,"rolle":"weitergefuehrt","etappen":["kongruenzsatz"]},{"eintrag_id":669,"thema_id":49,"rolle":"neu","etappen":["bildpunkt","abbildungsmatrix","drehung"]},{"eintrag_id":670,"thema_id":45,"rolle":"neu","etappen":["thales","tangente","lage","umkreis_inkreis"]},{"eintrag_id":671,"thema_id":55,"rolle":"weitergefuehrt","etappen":["seite","winkel","anwendung"]},{"eintrag_id":672,"thema_id":37,"rolle":"neu","etappen":["werte","graph","logfunktion"]},{"eintrag_id":673,"thema_id":92,"rolle":"weitergefuehrt","etappen":["pyr_volumen","kegel_volumen","kugel"]},{"eintrag_id":674,"thema_id":56,"rolle":"neu","etappen":["einheitskreis","sinussatz_seite","kosinussatz_seite"]},{"eintrag_id":675,"thema_id":20,"rolle":"weitergefuehrt","etappen":["zahlarten","teilweise","nenner_rational"]},{"eintrag_id":676,"thema_id":76,"rolle":"neu","etappen":["arithmetisch","geometrisch","summenzeichen","arith","geom"]},{"eintrag_id":677,"thema_id":63,"rolle":"weitergefuehrt","etappen":["bedingt","vierfeld","tafel_wkeit"]},{"eintrag_id":678,"thema_id":79,"rolle":"neu","etappen":["abweichung","varianz","sigma","deuten"]},{"eintrag_id":679,"thema_id":65,"rolle":"neu","etappen":["grundbegriffe","euler","kuerzester","spannbaum"]},{"eintrag_id":680,"thema_id":63,"rolle":"weitergefuehrt","etappen":["elemente","schnitt","verknuepfen","venn"]},{"eintrag_id":681,"thema_id":63,"rolle":"weitergefuehrt","etappen":["verknuepfen","additionssatz"]},{"eintrag_id":682,"thema_id":63,"rolle":"weitergefuehrt","etappen":["bedingt","rueckschluss"]},{"eintrag_id":683,"thema_id":28,"rolle":"neu","etappen":["uebersetzen","sachsituation"]},{"eintrag_id":684,"thema_id":44,"rolle":"neu","etappen":["kongruenzsatz","konstruierbar"]},{"eintrag_id":685,"thema_id":33,"rolle":"neu","etappen":["zwei_punkte","aufstellen"]},{"eintrag_id":702,"thema_id":29,"rolle":"neu","etappen":["zusammenfassen","produkte","minusklammer","ausmultiplizieren","aequivalenz"]},{"eintrag_id":703,"thema_id":2,"rolle":"neu","etappen":["waage","beide_seiten","klammern"]},{"eintrag_id":704,"thema_id":3,"rolle":"neu","etappen":["umformen","umdrehen","intervall"]},{"eintrag_id":705,"thema_id":2,"rolle":"neu","etappen":["sach"]},{"eintrag_id":717,"thema_id":29,"rolle":"neu","etappen":["zusammenfassen","produkte","minusklammer","ausmultiplizieren","aequivalenz"]},{"eintrag_id":718,"thema_id":2,"rolle":"neu","etappen":["waage","beide_seiten","klammern"]},{"eintrag_id":719,"thema_id":3,"rolle":"neu","etappen":["umformen","umdrehen","intervall"]},{"eintrag_id":720,"thema_id":2,"rolle":"neu","etappen":["sach"]},{"eintrag_id":732,"thema_id":29,"rolle":"weitergefuehrt","etappen":["summe_mal_summe","binomisch","ausmultiplizieren","ausklammern"]},{"eintrag_id":733,"thema_id":97,"rolle":"neu","etappen":["ergaenzen","scheitelform","extremwert","mit_faktor","optimierung"]},{"eintrag_id":734,"thema_id":2,"rolle":"weitergefuehrt","etappen":["klammern","beide_seiten"]},{"eintrag_id":736,"thema_id":31,"rolle":"neu","etappen":["definitionsmenge"]},{"eintrag_id":737,"thema_id":5,"rolle":"neu","etappen":["definitionsmenge","verhaeltnis"]},{"eintrag_id":747,"thema_id":29,"rolle":"weitergefuehrt","etappen":["summe_mal_summe","binomisch","ausmultiplizieren","ausklammern"]},{"eintrag_id":748,"thema_id":97,"rolle":"neu","etappen":["ergaenzen","scheitelform","extremwert","mit_faktor","optimierung"]},{"eintrag_id":749,"thema_id":2,"rolle":"weitergefuehrt","etappen":["klammern","beide_seiten"]},{"eintrag_id":751,"thema_id":31,"rolle":"neu","etappen":["definitionsmenge"]},{"eintrag_id":752,"thema_id":5,"rolle":"neu","etappen":["definitionsmenge","verhaeltnis"]},{"eintrag_id":758,"thema_id":20,"rolle":"neu","etappen":["zahlarten"]},{"eintrag_id":759,"thema_id":8,"rolle":"neu","etappen":["reinquadratisch"]},{"eintrag_id":760,"thema_id":20,"rolle":"neu","etappen":["teilweise","nenner_rational","zusammenfassen","wurzel_mal"]},{"eintrag_id":762,"thema_id":47,"rolle":"neu","etappen":["streckung"]},{"eintrag_id":763,"thema_id":47,"rolle":"neu","etappen":["streckung"]},{"eintrag_id":764,"thema_id":47,"rolle":"neu","etappen":["flaeche_volumen","streckung"]},{"eintrag_id":765,"thema_id":47,"rolle":"neu","etappen":["strahlensatz1","strahlensatz2","anwendung"]},{"eintrag_id":766,"thema_id":47,"rolle":"neu","etappen":["streckung_vektor"]},{"eintrag_id":767,"thema_id":47,"rolle":"neu","etappen":["bildgerade"]},{"eintrag_id":768,"thema_id":47,"rolle":"neu","etappen":["schwerpunkt"]},{"eintrag_id":769,"thema_id":47,"rolle":"neu","etappen":["aehnlich"]},{"eintrag_id":771,"thema_id":54,"rolle":"neu","etappen":["hypotenuse","kathete","anwendung"]},{"eintrag_id":772,"thema_id":54,"rolle":"neu","etappen":["umkehrung"]},{"eintrag_id":773,"thema_id":54,"rolle":"neu","etappen":["koordinaten"]},{"eintrag_id":774,"thema_id":54,"rolle":"neu","etappen":["anwendung"]},{"eintrag_id":775,"thema_id":54,"rolle":"neu","etappen":["raum"]},{"eintrag_id":776,"thema_id":55,"rolle":"neu","etappen":["verhaeltnisse","seite","winkel"]},{"eintrag_id":778,"thema_id":51,"rolle":"neu","etappen":["umfang","flaeche","verstehen","exakt"]},{"eintrag_id":779,"thema_id":51,"rolle":"neu","etappen":["sektor","zusammengesetzt"]},{"eintrag_id":781,"thema_id":92,"rolle":"neu","etappen":["verstehen"]},{"eintrag_id":782,"thema_id":92,"rolle":"neu","etappen":["pyr_oberflaeche","kegel_mantel"]},{"eintrag_id":783,"thema_id":92,"rolle":"neu","etappen":["pyr_volumen","kegel_volumen","kugel","sachkontext"]},{"eintrag_id":784,"thema_id":92,"rolle":"neu","etappen":["sachkontext"]},{"eintrag_id":786,"thema_id":6,"rolle":"neu","etappen":["grafisch","einsetzen","gleichsetzen","addition"]},{"eintrag_id":788,"thema_id":35,"rolle":"neu","etappen":["scheitel","parameter"]},{"eintrag_id":789,"thema_id":35,"rolle":"neu","etappen":["bestimmen","umformen"]},{"eintrag_id":790,"thema_id":35,"rolle":"neu","etappen":["scheitel","punkte"]},{"eintrag_id":791,"thema_id":35,"rolle":"neu","etappen":["extremwert"]},{"eintrag_id":792,"thema_id":35,"rolle":"neu","etappen":["parameter"]},{"eintrag_id":793,"thema_id":8,"rolle":"neu","etappen":["loesungsformel","diskriminante","ergaenzung"]},{"eintrag_id":794,"thema_id":8,"rolle":"neu","etappen":["loesungsformel"]},{"eintrag_id":795,"thema_id":35,"rolle":"neu","etappen":["schnittpunkte"]},{"eintrag_id":796,"thema_id":13,"rolle":"neu","etappen":["definitionsmenge","quadrieren","isolieren","probe","zwei_seiten"]},{"eintrag_id":798,"thema_id":61,"rolle":"weitergefuehrt","etappen":["grosse_zahlen"]},{"eintrag_id":799,"thema_id":61,"rolle":"weitergefuehrt","etappen":["laplace","laplace_pruefen"]},{"eintrag_id":800,"thema_id":61,"rolle":"weitergefuehrt","etappen":["begriffe"]},{"eintrag_id":801,"thema_id":61,"rolle":"weitergefuehrt","etappen":["gegenereignis"]},{"eintrag_id":802,"thema_id":61,"rolle":"weitergefuehrt","etappen":["laplace"]},{"eintrag_id":804,"thema_id":8,"rolle":"neu","etappen":["reinquadratisch"]},{"eintrag_id":815,"thema_id":6,"rolle":"neu","etappen":["grafisch","einsetzen","gleichsetzen","addition"]},{"eintrag_id":819,"thema_id":56,"rolle":"neu","etappen":["einheitskreis"]},{"eintrag_id":820,"thema_id":56,"rolle":"neu","etappen":["einheitskreis"]},{"eintrag_id":821,"thema_id":38,"rolle":"neu","etappen":["werte","periode"]},{"eintrag_id":822,"thema_id":56,"rolle":"neu","etappen":["einheitskreis"]},{"eintrag_id":823,"thema_id":56,"rolle":"neu","etappen":["einheitskreis"]},{"eintrag_id":824,"thema_id":56,"rolle":"neu","etappen":["additionstheoreme"]},{"eintrag_id":825,"thema_id":56,"rolle":"neu","etappen":["sinussatz_seite","sinussatz_winkel","kosinussatz_seite","kosinussatz_winkel","flaeche"]},{"eintrag_id":826,"thema_id":56,"rolle":"neu","etappen":["anwendung","satz_waehlen"]},{"eintrag_id":827,"thema_id":14,"rolle":"neu","etappen":["sinus","kosinus","tangens","umformen","anwendung"]},{"eintrag_id":828,"thema_id":49,"rolle":"neu","etappen":["skalarprodukt"]},{"eintrag_id":829,"thema_id":49,"rolle":"neu","etappen":["skalarprodukt","abstand"]},{"eintrag_id":831,"thema_id":49,"rolle":"neu","etappen":["bildpunkt","abbildungsmatrix","drehung"]},{"eintrag_id":832,"thema_id":49,"rolle":"neu","etappen":["bildpunkt"]},{"eintrag_id":833,"thema_id":37,"rolle":"neu","etappen":["punkte"]},{"eintrag_id":834,"thema_id":49,"rolle":"neu","etappen":["rechnen"]},{"eintrag_id":836,"thema_id":96,"rolle":"neu","etappen":["potenz_wert","zusammenfassen"]},{"eintrag_id":837,"thema_id":96,"rolle":"neu","etappen":["nte_wurzel","umwandeln"]},{"eintrag_id":838,"thema_id":36,"rolle":"neu","etappen":["negativ","verlauf","umkehrbar","wurzelfunktion"]},{"eintrag_id":839,"thema_id":36,"rolle":"neu","etappen":["parameter"]},{"eintrag_id":841,"thema_id":10,"rolle":"neu","etappen":["logarithmus","mit_log_loesen","potenzregel"]},{"eintrag_id":842,"thema_id":37,"rolle":"neu","etappen":["graph","logfunktion"]},{"eintrag_id":843,"thema_id":37,"rolle":"neu","etappen":["modell","faktor","linear_oder_exponentiell"]},{"eintrag_id":845,"thema_id":62,"rolle":"neu","etappen":["baum_ergaenzen","pfad_mult"]},{"eintrag_id":846,"thema_id":62,"rolle":"neu","etappen":["pfad_mult","pfad_add","gegenereignis"]},{"eintrag_id":852,"thema_id":10,"rolle":"neu","etappen":["mit_log_loesen","logarithmus"]},{"eintrag_id":855,"thema_id":35,"rolle":"neu","etappen":["scheitel","parameter"]},{"eintrag_id":856,"thema_id":35,"rolle":"neu","etappen":["bestimmen","umformen"]},{"eintrag_id":857,"thema_id":35,"rolle":"neu","etappen":["scheitel","punkte"]},{"eintrag_id":858,"thema_id":35,"rolle":"neu","etappen":["extremwert"]},{"eintrag_id":859,"thema_id":8,"rolle":"weitergefuehrt","etappen":["loesungsformel","diskriminante","ergaenzung","faktorisieren","ausklammern"]},{"eintrag_id":860,"thema_id":8,"rolle":"weitergefuehrt","etappen":["loesungsformel"]},{"eintrag_id":864,"thema_id":30,"rolle":"neu","etappen":["negativer_exponent"]},{"eintrag_id":865,"thema_id":102,"rolle":"neu","etappen":["mal_gleiche_basis","gleicher_exponent","potenz_von_potenz","geteilt_gleiche_basis"]},{"eintrag_id":866,"thema_id":19,"rolle":"neu","etappen":["zehnerpotenz","vorsilben_gross","vorsilben_klein","gross_wissenschaftlich","klein_wissenschaftlich"]},{"eintrag_id":868,"thema_id":46,"rolle":"weitergefuehrt","etappen":["eigenschaften","verschiebung"]},{"eintrag_id":869,"thema_id":46,"rolle":"weitergefuehrt","etappen":["verschiebung"]},{"eintrag_id":870,"thema_id":46,"rolle":"weitergefuehrt","etappen":["gegenvektor"]},{"eintrag_id":871,"thema_id":46,"rolle":"weitergefuehrt","etappen":["vektor_koordinaten"]},{"eintrag_id":872,"thema_id":74,"rolle":"neu","etappen":["det_berechnen","parallelogramm","dreieck","viereck","vieleck"]},{"eintrag_id":873,"thema_id":98,"rolle":"neu","etappen":["stufen_wechsel","parallel_pruefen"]},{"eintrag_id":874,"thema_id":98,"rolle":"neu","etappen":["aussenwinkel","vieleck","innenwinkelsumme"]},{"eintrag_id":876,"thema_id":44,"rolle":"neu","etappen":["konstruierbar"]},{"eintrag_id":877,"thema_id":44,"rolle":"neu","etappen":["planfigur"]},{"eintrag_id":878,"thema_id":44,"rolle":"neu","etappen":["kongruenzsatz"]},{"eintrag_id":879,"thema_id":44,"rolle":"neu","etappen":["satz_kehrsatz"]},{"eintrag_id":881,"thema_id":91,"rolle":"neu","etappen":["lage"]},{"eintrag_id":882,"thema_id":91,"rolle":"neu","etappen":["pyramide"]},{"eintrag_id":883,"thema_id":91,"rolle":"neu","etappen":["wahre_groesse"]},{"eintrag_id":885,"thema_id":73,"rolle":"neu","etappen":["kreislinie","parallelen","zwei_kreise"]},{"eintrag_id":886,"thema_id":45,"rolle":"neu","etappen":["lage","tangente"]},{"eintrag_id":887,"thema_id":73,"rolle":"neu","etappen":["sachsituationen","verstehen"]},{"eintrag_id":888,"thema_id":73,"rolle":"neu","etappen":["verknuepfen"]},{"eintrag_id":889,"thema_id":45,"rolle":"neu","etappen":["umkreis_inkreis"]},{"eintrag_id":891,"thema_id":94,"rolle":"neu","etappen":["vermehrt","vermindert","faktor","zurueck"]},{"eintrag_id":892,"thema_id":71,"rolle":"neu","etappen":["jahreszinsen","zinssatz","kapital"]},{"eintrag_id":893,"thema_id":93,"rolle":"neu","etappen":["erkennen","graph","produkt"]},{"eintrag_id":894,"thema_id":93,"rolle":"neu","etappen":["dreisatz","vervielfachen"]},{"eintrag_id":895,"thema_id":93,"rolle":"neu","etappen":["unterscheiden"]},{"eintrag_id":897,"thema_id":58,"rolle":"neu","etappen":["mittelwert"]},{"eintrag_id":898,"thema_id":95,"rolle":"neu","etappen":["mittel_median","median","kennwerte"]},{"eintrag_id":899,"thema_id":81,"rolle":"neu","etappen":["repraesentativ","begriffe","fehlerquellen"]},{"eintrag_id":900,"thema_id":57,"rolle":"weitergefuehrt","etappen":["irrefuehrend"]},{"eintrag_id":902,"thema_id":30,"rolle":"neu","etappen":["negativer_exponent"]},{"eintrag_id":903,"thema_id":102,"rolle":"neu","etappen":["mal_gleiche_basis","gleicher_exponent","potenz_von_potenz","geteilt_gleiche_basis"]},{"eintrag_id":904,"thema_id":19,"rolle":"neu","etappen":["zehnerpotenz","vorsilben_gross","vorsilben_klein","gross_wissenschaftlich","klein_wissenschaftlich"]},{"eintrag_id":906,"thema_id":46,"rolle":"weitergefuehrt","etappen":["eigenschaften"]},{"eintrag_id":907,"thema_id":46,"rolle":"weitergefuehrt","etappen":["verschiebung"]},{"eintrag_id":908,"thema_id":46,"rolle":"weitergefuehrt","etappen":["gegenvektor"]},{"eintrag_id":909,"thema_id":46,"rolle":"weitergefuehrt","etappen":["vektor_koordinaten"]},{"eintrag_id":910,"thema_id":74,"rolle":"neu","etappen":["det_berechnen","dreieck","viereck","parallelogramm"]},{"eintrag_id":911,"thema_id":98,"rolle":"neu","etappen":["stufen_wechsel","parallel_pruefen"]},{"eintrag_id":912,"thema_id":98,"rolle":"neu","etappen":["innenwinkelsumme","aussenwinkel","vieleck","figuren"]},{"eintrag_id":914,"thema_id":73,"rolle":"neu","etappen":["kreislinie","parallelen","zwei_kreise"]},{"eintrag_id":915,"thema_id":45,"rolle":"neu","etappen":["lage","tangente"]},{"eintrag_id":916,"thema_id":73,"rolle":"neu","etappen":["verknuepfen","sachsituationen"]},{"eintrag_id":917,"thema_id":45,"rolle":"neu","etappen":["umkreis_inkreis"]},{"eintrag_id":919,"thema_id":94,"rolle":"neu","etappen":["vermehrt","vermindert","faktor"]},{"eintrag_id":920,"thema_id":71,"rolle":"neu","etappen":["jahreszinsen","zinssatz","kapital"]},{"eintrag_id":921,"thema_id":93,"rolle":"neu","etappen":["erkennen","graph","produkt"]},{"eintrag_id":922,"thema_id":93,"rolle":"neu","etappen":["dreisatz","vervielfachen"]},{"eintrag_id":923,"thema_id":93,"rolle":"neu","etappen":["unterscheiden"]},{"eintrag_id":925,"thema_id":58,"rolle":"neu","etappen":["mittelwert"]},{"eintrag_id":926,"thema_id":95,"rolle":"neu","etappen":["median","kennwerte","mittel_median"]},{"eintrag_id":927,"thema_id":81,"rolle":"neu","etappen":["repraesentativ","begriffe","fehlerquellen"]},{"eintrag_id":928,"thema_id":57,"rolle":"weitergefuehrt","etappen":["irrefuehrend"]},{"eintrag_id":930,"thema_id":46,"rolle":"weitergefuehrt","etappen":["vierecke_ordnen"]},{"eintrag_id":931,"thema_id":44,"rolle":"weitergefuehrt","etappen":["vierecke","vierecke_konstruieren"]},{"eintrag_id":933,"thema_id":46,"rolle":"weitergefuehrt","etappen":["drehung","eigenschaften"]},{"eintrag_id":934,"thema_id":46,"rolle":"weitergefuehrt","etappen":["punktspiegelung"]},{"eintrag_id":935,"thema_id":46,"rolle":"weitergefuehrt","etappen":["drehung"]},{"eintrag_id":936,"thema_id":46,"rolle":"weitergefuehrt","etappen":["drehung","symmetrie"]},{"eintrag_id":937,"thema_id":46,"rolle":"weitergefuehrt","etappen":["vektor_drehen"]},{"eintrag_id":939,"thema_id":91,"rolle":"weitergefuehrt","etappen":["pyramide"]},{"eintrag_id":940,"thema_id":91,"rolle":"weitergefuehrt","etappen":["rotation","axialschnitt"]},{"eintrag_id":941,"thema_id":91,"rolle":"weitergefuehrt","etappen":["koordinaten"]},{"eintrag_id":943,"thema_id":32,"rolle":"neu","etappen":["eindeutig","sachzusammenhang"]},{"eintrag_id":944,"thema_id":32,"rolle":"neu","etappen":["mengen","funktionswert","wertetabelle","nullstellen","graph_lesen"]},{"eintrag_id":945,"thema_id":33,"rolle":"neu","etappen":["ablesen","wirkung"]},{"eintrag_id":946,"thema_id":33,"rolle":"neu","etappen":["graph_ablesen","ablesen"]},{"eintrag_id":947,"thema_id":33,"rolle":"neu","etappen":["aufstellen","zwei_punkte","lage","einsetzen","wirkung","bueschel"]},{"eintrag_id":948,"thema_id":33,"rolle":"neu","etappen":["deuten"]},{"eintrag_id":950,"thema_id":61,"rolle":"neu","etappen":["begriffe"]},{"eintrag_id":951,"thema_id":61,"rolle":"neu","etappen":["rel_haeufigkeit"]},{"eintrag_id":953,"thema_id":44,"rolle":"neu","etappen":["konstruierbar"]},{"eintrag_id":954,"thema_id":44,"rolle":"neu","etappen":["planfigur"]},{"eintrag_id":955,"thema_id":44,"rolle":"neu","etappen":["kongruenzsatz"]},{"eintrag_id":956,"thema_id":46,"rolle":"weitergefuehrt","etappen":["vierecke_ordnen"]},{"eintrag_id":957,"thema_id":44,"rolle":"neu","etappen":["vierecke","vierecke_konstruieren"]},{"eintrag_id":959,"thema_id":91,"rolle":"neu","etappen":["pyramide"]},{"eintrag_id":960,"thema_id":91,"rolle":"neu","etappen":["wahre_groesse"]},{"eintrag_id":962,"thema_id":32,"rolle":"neu","etappen":["eindeutig","sachzusammenhang"]},{"eintrag_id":963,"thema_id":32,"rolle":"neu","etappen":["mengen","funktionswert","wertetabelle","nullstellen"]},{"eintrag_id":964,"thema_id":33,"rolle":"neu","etappen":["proportional"]},{"eintrag_id":965,"thema_id":33,"rolle":"neu","etappen":["graph_ablesen"]},{"eintrag_id":966,"thema_id":33,"rolle":"neu","etappen":["lage"]},{"eintrag_id":968,"thema_id":61,"rolle":"neu","etappen":["begriffe"]},{"eintrag_id":969,"thema_id":61,"rolle":"neu","etappen":["rel_haeufigkeit"]},{"eintrag_id":971,"thema_id":20,"rolle":"neu","etappen":["zahlarten"]},{"eintrag_id":972,"thema_id":20,"rolle":"neu","etappen":["teilweise","zusammenfassen"]},{"eintrag_id":974,"thema_id":47,"rolle":"neu","etappen":["streckung"]},{"eintrag_id":975,"thema_id":47,"rolle":"neu","etappen":["streckung","flaeche_volumen"]},{"eintrag_id":976,"thema_id":47,"rolle":"neu","etappen":["strahlensatz1","strahlensatz2","anwendung"]},{"eintrag_id":978,"thema_id":54,"rolle":"neu","etappen":["hypotenuse","kathete","anwendung"]},{"eintrag_id":979,"thema_id":54,"rolle":"neu","etappen":["umkehrung"]},{"eintrag_id":980,"thema_id":54,"rolle":"neu","etappen":["koordinaten"]},{"eintrag_id":981,"thema_id":54,"rolle":"neu","etappen":["anwendung"]},{"eintrag_id":982,"thema_id":54,"rolle":"neu","etappen":["raum"]},{"eintrag_id":983,"thema_id":55,"rolle":"neu","etappen":["verhaeltnisse","seite","winkel"]},{"eintrag_id":985,"thema_id":51,"rolle":"neu","etappen":["umfang","flaeche","exakt"]},{"eintrag_id":986,"thema_id":51,"rolle":"neu","etappen":["sektor","zusammengesetzt"]},{"eintrag_id":988,"thema_id":33,"rolle":"weitergefuehrt","etappen":["ablesen","wirkung"]},{"eintrag_id":989,"thema_id":33,"rolle":"weitergefuehrt","etappen":["graph_ablesen","aufstellen"]},{"eintrag_id":990,"thema_id":33,"rolle":"weitergefuehrt","etappen":["aufstellen","zwei_punkte","lage","bueschel"]},{"eintrag_id":991,"thema_id":33,"rolle":"weitergefuehrt","etappen":["deuten"]},{"eintrag_id":993,"thema_id":61,"rolle":"weitergefuehrt","etappen":["grosse_zahlen"]},{"eintrag_id":994,"thema_id":61,"rolle":"weitergefuehrt","etappen":["laplace","laplace_pruefen"]},{"eintrag_id":995,"thema_id":61,"rolle":"weitergefuehrt","etappen":["begriffe"]},{"eintrag_id":996,"thema_id":61,"rolle":"weitergefuehrt","etappen":["gegenereignis"]},{"eintrag_id":997,"thema_id":61,"rolle":"weitergefuehrt","etappen":["laplace"]},{"eintrag_id":999,"thema_id":56,"rolle":"neu","etappen":["einheitskreis"]},{"eintrag_id":1000,"thema_id":56,"rolle":"neu","etappen":["einheitskreis"]},{"eintrag_id":1001,"thema_id":38,"rolle":"neu","etappen":["werte","periode"]},{"eintrag_id":1002,"thema_id":56,"rolle":"neu","etappen":["einheitskreis"]},{"eintrag_id":1003,"thema_id":56,"rolle":"neu","etappen":["sinussatz_seite","sinussatz_winkel","kosinussatz_seite","kosinussatz_winkel","flaeche"]},{"eintrag_id":1004,"thema_id":56,"rolle":"neu","etappen":["anwendung"]},{"eintrag_id":1006,"thema_id":91,"rolle":"weitergefuehrt","etappen":["rotation","axialschnitt"]},{"eintrag_id":1007,"thema_id":92,"rolle":"neu","etappen":["verstehen"]},{"eintrag_id":1008,"thema_id":92,"rolle":"neu","etappen":["pyr_oberflaeche","kegel_mantel"]},{"eintrag_id":1009,"thema_id":92,"rolle":"neu","etappen":["pyr_volumen","kegel_volumen","kugel","sachkontext"]},{"eintrag_id":1010,"thema_id":92,"rolle":"neu","etappen":["sachkontext"]},{"eintrag_id":1012,"thema_id":37,"rolle":"neu","etappen":["werte","graph","linear_oder_exponentiell"]},{"eintrag_id":1013,"thema_id":37,"rolle":"neu","etappen":["modell","faktor"]},{"eintrag_id":1015,"thema_id":62,"rolle":"neu","etappen":["baum_ergaenzen","pfad_mult"]},{"eintrag_id":1016,"thema_id":62,"rolle":"neu","etappen":["pfad_mult","pfad_add"]}]$json$::jsonb);
  raise notice 'LK-S Befüllen (lk_daten_2211.json): % gesetzt, % unverändert, % ohne Zuordnung, % mit unbekannten Etappen (unverändert): %',
    r->'gesetzt', r->'gleich', jsonb_array_length(r->'ohne_zuordnung'), jsonb_array_length(r->'unbekannte_etappen'), r->'unbekannte_etappen';
end $$;

-- 4. Schnittstelle
-- Klassen eines Themas: Schulart → Zweig → [{klasse, rolle, route_start?, etappen?, ganzes_thema?, etappen_unbekannt?, rolle_lehrplan?, lernbereiche, stunden,
-- nur_klasse_fest?}] (p_schulart/p_zweig: nur diese; p_kurz: ohne Lehrplan-Einzelheiten)
create or replace function schule.thema_klassen(p_thema bigint, p_schulart text default null, p_zweig text default null, p_kurz boolean default false)
 returns jsonb language sql stable set search_path to ''
as $function$
  select coalesce(jsonb_object_agg(s.schulart, s.j), '{}'::jsonb) from (
    select z.schulart, jsonb_object_agg(z.zweig, z.j) j from (
      select k.schulart, k.zweig, jsonb_agg(jsonb_strip_nulls(jsonb_build_object('klasse', k.klasse, 'rolle', k.rolle,
               'route_start', case when k.klasse = k.klasse_route then true end,
               'etappen', to_jsonb(k.etappen),
               'ganzes_thema', case when k.ganzes_thema then true end,
               'etappen_unbekannt', case when k.etappen_unbekannt then true end,
               'rolle_lehrplan', case when not p_kurz then to_jsonb(k.rolle_lehrplan) end,
               'lernbereiche', case when not p_kurz then k.lernbereiche end,
               'stunden', case when not p_kurz then (select sum((l->>'stunden')::numeric) from jsonb_array_elements(k.lernbereiche) l) end,
               'nur_klasse_fest', case when not p_kurz and k.nur_klasse_fest then true end)) order by k.klasse) j
        from schule.thema_lage_klasse k
       where k.thema_id = p_thema and (p_schulart is null or k.schulart = p_schulart) and (p_zweig is null or k.zweig = p_zweig)
       group by 1, 2) z group by 1) s;
$function$;

-- Lehrplan-Zuordnung nach Stunden (B6: „Lehrplan zugeordnet: x von y Stunden“, Schätzung): Schulart → Zweig → Klasse → {stunden, stunden_zugeordnet, lernbereiche[]}
create or replace function schule.lehrplan_zuordnung_json()
 returns jsonb language sql stable set search_path to ''
as $function$
  select coalesce(jsonb_object_agg(a.schulart, a.j), '{}'::jsonb) from (
    select b.schulart, jsonb_object_agg(b.zweig, b.j) j from (
      select c.schulart, c.zweig, jsonb_object_agg(c.klasse::text, c.j) j from (
        select x.schulart, x.zweig, x.klasse, jsonb_build_object('stunden', sum(x.stunden), 'stunden_zugeordnet', sum(x.stunden_zugeordnet),
                 'lernbereiche', jsonb_agg(jsonb_build_object('eintrag_id', x.eintrag_id, 'pfad', x.pfad, 'titel', x.lernbereich, 'stunden', x.stunden,
                   'punkte', x.punkte, 'punkte_mit_thema', x.punkte_mit_thema, 'stunden_zugeordnet', x.stunden_zugeordnet) order by x.reihenfolge, x.eintrag_id)) j
          from schule.lehrplan_abdeckung x group by 1, 2, 3) c group by 1, 2) b group by 1) a;
$function$;

-- Matrix ergänzen (alte Felder bleiben)
create or replace function schule.lehrplan_matrix_lk(p_r jsonb, p_kind bigint)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare v_sa text; v_zw text;
begin
  if p_kind is not null then   -- Kindsicht: nur Schulart und Zweig des Kindes, kurz
    select coalesce(l.schulart, 'gym_by'), schule.kind_zweig(coalesce(l.schulart, 'gym_by'), l.zweig) into v_sa, v_zw from schule.lernender l where l.id = p_kind;
    return jsonb_set(p_r, '{themen}', coalesce((select jsonb_agg(t.j || jsonb_build_object('klassen_kind',
             coalesce(schule.thema_klassen((t.j->>'thema_id')::bigint, v_sa, v_zw, true)->v_sa->v_zw, '[]'::jsonb)) order by t.o)
             from jsonb_array_elements(p_r->'themen') with ordinality t(j, o)), '[]'::jsonb))
           || jsonb_build_object('zweig', v_zw);
  end if;
  return jsonb_set(jsonb_set(p_r, '{themen}', coalesce((select jsonb_agg(t.j || jsonb_build_object('klassen', schule.thema_klassen((t.j->>'thema_id')::bigint)) order by t.o)
           from jsonb_array_elements(p_r->'themen') with ordinality t(j, o)), '[]'::jsonb)),
         '{kinder}', coalesce((select jsonb_agg(k.j || jsonb_build_object('zweig', schule.kind_zweig(coalesce(l.schulart, 'gym_by'), l.zweig)) order by k.o)
           from jsonb_array_elements(p_r->'kinder') with ordinality k(j, o) left join schule.lernender l on l.id = (k.j->>'id')::bigint), '[]'::jsonb))
         || jsonb_build_object('lehrplan_zuordnung', schule.lehrplan_zuordnung_json());
end $function$;

-- Stand eines Kindes je Klasse (B2): verlangt = ausdrücklich genannte Etappen (ganzes Thema: alle); nur unbekannt → verlangt/erledigt leer
create or replace function schule.thema_klassen_kind(p_thema bigint, p_kind bigint)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare v_sa text; v_zw text; v_e bigint := schule.thema_einheit(p_thema); v_alle text[]; v jsonb;
begin
  select coalesce(l.schulart, 'gym_by'), schule.kind_zweig(coalesce(l.schulart, 'gym_by'), l.zweig) into v_sa, v_zw from schule.lernender l where l.id = p_kind;
  select array_agg(q->>'lernziel') into v_alle from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) q where e.id = v_e;
  select coalesce(jsonb_agg(jsonb_strip_nulls(jsonb_build_object('klasse', x.klasse, 'rolle', x.rolle, 'route_start', case when x.klasse = x.klasse_route then true end,
           'etappen', to_jsonb(x.verlangt), 'ganzes_thema', case when x.ganzes_thema then true end,
           'etappen_unbekannt', case when x.etappen_unbekannt then true end,
           'etappen_verlangt', cardinality(x.verlangt),
           'etappen_erledigt', case when x.verlangt is not null then (select count(*) from schule.karte_stand ks where ks.lernender_id = p_kind and ks.einheit_id = v_e
                                     and (ks.sitzt or ks.gesetzt_am is not null) and ks.lernziel = any(x.verlangt)) end)) order by x.klasse), '[]'::jsonb)
    into v
    from (select k.*, case when k.ganzes_thema then v_alle else k.etappen end verlangt
            from schule.thema_lage_klasse k where k.thema_id = p_thema and k.schulart = v_sa and k.zweig = v_zw) x;
  return jsonb_build_object('zweig', v_zw, 'klassen_kind', v);
end $function$;

-- Thema-Detail ergänzen: klassen, baut_auf, weiter_in; mit Kind: klassen_kind mit Stand je Klasse
create or replace function schule.lehrplan_thema_lk(p_r jsonb, p_thema bigint, p_kind bigint, p_kindsicht boolean)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare v_sa text; v_zw text; v_kk jsonb := '{}'::jsonb; v_e bigint := schule.thema_einheit(p_thema);
begin
  if p_kind is not null then
    v_kk := schule.thema_klassen_kind(p_thema, p_kind);
    select coalesce(l.schulart, 'gym_by'), schule.kind_zweig(coalesce(l.schulart, 'gym_by'), l.zweig) into v_sa, v_zw from schule.lernender l where l.id = p_kind;
  end if;
  if p_kindsicht then
    return p_r || v_kk || jsonb_build_object(
      'baut_auf', (select coalesce(jsonb_agg(jsonb_build_object('thema_id', v.braucht_id, 'titel', tb.unterthema, 'art', v.art,
                     'klasse', (select g.klasse_ab from schule.thema_lage g where g.thema_id = v.braucht_id and g.lernziel is null and g.schulart = v_sa and g.zweig = v_zw)) order by v.braucht_id), '[]'::jsonb)
                     from schule.voraussetzung v join schule.thema tb on tb.id = v.braucht_id where v.thema_id = p_thema));
  end if;
  return p_r || v_kk || jsonb_strip_nulls(jsonb_build_object(
    'klassen', schule.thema_klassen(p_thema),
    'etappen_titel', (select jsonb_object_agg(q->>'lernziel', q->>'titel') from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) q where e.id = v_e),
    -- Voraussetzungen mit ihrer frühesten Klasse je Schulart/Zweig; verstoss: liegt später als dieses Thema
    'baut_auf', (select coalesce(jsonb_agg(jsonb_build_object('thema_id', v.braucht_id, 'titel', tb.unterthema, 'art', v.art,
                   'klassen', (select coalesce(jsonb_object_agg(g.schulart || '/' || g.zweig, g.klasse_ab), '{}'::jsonb) from schule.thema_lage g
                                where g.thema_id = v.braucht_id and g.lernziel is null),
                   'verstoss', (select coalesce(jsonb_agg(g.schulart || '/' || g.zweig order by g.schulart, g.zweig), '[]'::jsonb) from schule.thema_lage g
                                 join schule.thema_lage h on h.thema_id = p_thema and h.lernziel is null and h.schulart = g.schulart and h.zweig = g.zweig
                                where g.thema_id = v.braucht_id and g.lernziel is null and g.klasse_ab > h.klasse_ab)) order by v.braucht_id), '[]'::jsonb)
                   from schule.voraussetzung v join schule.thema tb on tb.id = v.braucht_id where v.thema_id = p_thema),
    -- spätere Klassen mit den Etappen, die dort verlangt werden
    'weiter_in', (select coalesce(jsonb_object_agg(w.schulart || '/' || w.zweig, w.j), '{}'::jsonb) from (
                    select k.schulart, k.zweig, jsonb_agg(jsonb_strip_nulls(jsonb_build_object('klasse', k.klasse, 'etappen', to_jsonb(k.etappen),
                             'ganzes_thema', case when k.ganzes_thema then true end, 'etappen_unbekannt', case when k.etappen_unbekannt then true end)) order by k.klasse) j
                      from schule.thema_lage_klasse k where k.thema_id = p_thema and k.rolle = 'weitergefuehrt' group by 1, 2) w)));
end $function$;

create or replace function api.schule_lehrplan_matrix(p_schluessel text, p_daten jsonb default null)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_l bigint; v_kinder bigint[];
begin
  v_l := schule.lehrplan_sicht(p_schluessel, p_daten);
  if v_l is null then
    select coalesce(array_agg(l.id order by l.id), '{}') into v_kinder from schule.lernender l
     where l.aktiv and (not l.ist_test or coalesce((p_daten->>'mit_testkind')::boolean, false));
    return schule.lehrplan_matrix_lk(schule.lehrplan_matrix(v_kinder, false), null);   -- LK-S: Klassen je Thema, Lehrplan-Zuordnung, Zweig
  end if;
  return schule.lehrplan_matrix_lk(schule.lehrplan_matrix(array[v_l], true), v_l);
end $function$;

create or replace function api.schule_lehrplan_thema(p_schluessel text, p_daten jsonb default null)
 returns jsonb language plpgsql security definer set search_path to ''
as $function$
declare v_th bigint := nullif(p_daten->>'thema_id', '')::bigint; v_kind bigint; v_l bigint;
begin
  v_kind := schule.lehrplan_sicht(p_schluessel, p_daten);   -- Zugang zuerst prüfen
  if v_th is null then raise exception 'thema_id fehlt' using errcode = 'P0001'; end if;
  v_l := coalesce(v_kind, nullif(p_daten->>'lernender_id', '')::bigint);
  if v_kind is null and v_l is not null then perform schule.zugriff(p_schluessel, v_l); end if;   -- Eltern/Lehrer mit Kind: Zugriff auf das Kind
  return schule.lehrplan_thema_lk(schule.lehrplan_thema(v_th, v_kind is not null), v_th, v_l, v_kind is not null);   -- LK-S
end $function$;

revoke all on function schule.kind_zweig(text, text), schule.eintrag_lernbereich(bigint), schule.thema_klassen(bigint, text, text, boolean),
  schule.lehrplan_zuordnung_json(), schule.lehrplan_matrix_lk(jsonb, bigint), schule.thema_klassen_kind(bigint, bigint), schule.lehrplan_thema_lk(jsonb, bigint, bigint, boolean) from public, anon, authenticated;
grant execute on function api.schule_lehrplan_matrix(text, jsonb), api.schule_lehrplan_thema(text, jsonb) to council_mcp;
revoke all on function api.schule_lehrplan_matrix(text, jsonb), api.schule_lehrplan_thema(text, jsonb) from public, anon, authenticated;

-- 5. Teilen eines Themas (Nachtrag „Route“, 22.11.; LK-S 2 B3/B4): geprüfte Vorlage, hier NICHT aufgerufen.
-- Plan (jsonb):
--   alt_thema, alte_einheit_id?  Thema, das geteilt wird (Einheit: Vorgabe schule.thema_einheit)
--   etappen             Lernziel-Schlüssel des neuen Teils
--   neu                 {schluessel, unterthema, block, beschreibung, kurz, klasse_fest, lehrplan_reihenfolge, lernbereich, lehrplan, reihenfolge}
--   block_id, block_reihenfolge   Ort des neuen Flugs (Nachbarland), optional
--   neue_einheit_id     Einheit des neuen Teils (vorher mit schule.einheit_importieren angelegt; ihr Etappenkatalog = genau die Etappen des neuen Teils).
--                       Ohne sie nur Schritt 1 (Thema, Texte, Ort, Voraussetzung, Zuordnungen); Lernstand und alter Katalog bleiben.
--   aufgaben_umhaengen  Vorgabe true; false ist verboten, sobald es zu diesen Etappen Lernstand oder Antworten gibt (B3).
-- Bedingungen (B3): neuer Teil und Rest je mindestens 3 verschiedene Etappen, disjunkt, zusammen genau der alte Katalog; neue Einheit hat genau diese
--   Etappen; keine offene Test-Sitzung der alten Einheit (ein laufender Flug-Test lässt sich nicht teilen – erst abschließen).
-- Schritt 2 (mit neuer Einheit), atomar in derselben Transaktion: alten Etappenkatalog verkleinern (inhalt.etappen, bewertung.lernziele_pflicht,
--   bewertung.lernziele_vertiefung, bewertung.testaufgaben_je_lernziel); Aufgaben, Karten, Lernziel-Stand, besprochen, Was wackelt, Wiederholungs-Runden,
--   Staffel-Sicherung, abgelegt, Rückmeldungen, offene Misch-Ausgaben (Lage) umhängen; Sterne-Bezüge landung:/wdh: mitziehen (Menge gleich, kein zweiter Bonus).
-- Vorher/Nachher je Kind (B4) – muss gleich sein, sonst Abbruch: Lernstand je Etappe (über beide Einheiten nach Schlüssel), Lernziel-Stand, Sterne-Buchungen
--   mit Bezug (Einheit im Bezug neutralisiert), Flug-Abschlüsse, abgelegt (Stempel), Plan (route), offene Misch-Ausgaben. Berichtet (darf sich ändern,
--   weil es den neuen Teil gibt): thema_stufe/im_plan beider Teile, Reiseoptionen, Visum-Regeln. Je Kind neu_vollstaendig (Nachtrag Stempel/Bonus für den
--   neuen Teil nach Festlegung 14 ist ein eigener Schritt).
-- probelauf = true (Vorgabe): alles wird ausgeführt und geprüft, dann zurückgerollt; Rückgabe ist der Bericht.
create or replace function schule.thema_teilen(p_plan jsonb, p_probelauf boolean default true)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_bericht jsonb;
begin
  begin
    v_bericht := schule.thema_teilen_ausfuehren(p_plan);
    if p_probelauf then raise exception using errcode = 'LKPRB', message = v_bericht::text; end if;
    return v_bericht || jsonb_build_object('probelauf', false);
  exception when sqlstate 'LKPRB' then
    return sqlerrm::jsonb || jsonb_build_object('probelauf', true);
  end;
end $function$;

-- Stand je Kind (B4): fest = muss gleich bleiben; bericht = darf sich ändern
create or replace function schule.thema_teilen_stand(p_ae bigint, p_ne bigint, p_alt bigint, p_neu bigint)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare v jsonb; v_e bigint[] := array_remove(array[p_ae, p_ne], null);
  v_re text := '^(landung|wdh):(' || p_ae || coalesce('|' || p_ne, '') || '):'; v_visum text;
begin
  if to_regclass('schule.v_ort_visum') is not null then   -- Visum-Regeln (Bericht)
    execute 'select md5(coalesce(string_agg(x::text, ''|'' order by x::text), '''')) from schule.v_ort_visum x' into v_visum; end if;
  select coalesce(jsonb_object_agg(l.id, jsonb_build_object(
    'fest', jsonb_build_object(
      'etappen', (select coalesce(jsonb_object_agg(k.lernziel, jsonb_build_object('sitzt', k.sitzt, 'sitzt_am', k.sitzt_am, 'gesetzt_am', k.gesetzt_am,
                    'wdh_stufe', k.wdh_stufe, 'faellig_am', k.faellig_am, 'richtig', k.richtig, 'falsch', k.falsch, 'eigene_loesungen', k.eigene_loesungen,
                    'landung', k.landung)), '{}'::jsonb) from schule.karte_stand k where k.lernender_id = l.id and k.einheit_id = any(v_e)),
      'lernziel_stand', (select coalesce(jsonb_object_agg(s.lernziel, jsonb_build_object('status', s.status, 'pflicht', s.pflicht, 'fehler', s.fehler_anzahl)), '{}'::jsonb)
                           from schule.lernziel_stand s where s.lernender_id = l.id and s.einheit_id = any(v_e)),
      'sterne', (select coalesce(jsonb_agg(jsonb_build_array(s.grund, s.menge, regexp_replace(s.bezug, v_re, '\1:E:')) order by s.grund, regexp_replace(s.bezug, v_re, '\1:E:'), s.menge), '[]'::jsonb)
                   from schule.sterne s where s.lernender_id = l.id),
      'flug_abschluesse', (select coalesce(jsonb_agg(jsonb_build_array(f.einheit_id, f.am) order by f.einheit_id, f.am), '[]'::jsonb) from schule.flug_erstabschluss f where f.lernender_id = l.id),
      'abgelegt', (select coalesce(jsonb_agg(jsonb_build_array(a.art, regexp_replace(a.bezug, '^etappe:(' || p_ae || coalesce('|' || p_ne, '') || '):', 'etappe:E:'), a.sterne)
                     order by a.art, a.bezug), '[]'::jsonb) from schule.abgelegt a where a.lernender_id = l.id),
      'plan', (select md5(coalesce(string_agg(r::text, '|' order by r::text), '')) from schule.route r where r.lernender_id = l.id),
      'misch_offen', (select count(*) from schule.misch_ausgabe m where m.lernender_id = l.id and m.eingeloest_am is null and m.verfallen_am is null)),
    'bericht', jsonb_build_object(
      'stufe_alt', schule.thema_stufe(l.id, p_alt) - array['hinweis'],
      'stufe_neu', case when p_neu is not null then schule.thema_stufe(l.id, p_neu) - array['hinweis'] end,
      'reiseoptionen', md5(coalesce(schule.reiseoptionen(l.id)::text, '')),
      'visum', v_visum))), '{}'::jsonb)
    into v from schule.lernender l
   where exists (select 1 from schule.karte_stand k where k.lernender_id = l.id and k.einheit_id = any(v_e))
      or exists (select 1 from schule.versuch x join schule.aufgabe a on a.id = x.aufgabe_id where x.lernender_id = l.id and a.einheit_id = any(v_e));
  return v;
end $function$;

create or replace function schule.thema_teilen_ausfuehren(p_plan jsonb)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_alt bigint := (p_plan->>'alt_thema')::bigint; v_et text[] := array(select distinct jsonb_array_elements_text(p_plan->'etappen'));
  v_n jsonb := p_plan->'neu'; v_neu bigint; v_ae bigint; v_ne bigint := nullif(p_plan->>'neue_einheit_id', '')::bigint; v_b bigint := nullif(p_plan->>'block_id', '')::bigint;
  v_kat text[]; v_rest text[]; v_nkat text[]; v_tab text; v_cnt int; v_um jsonb := '{}'::jsonb; v_vor jsonb; v_nach jsonb; v_kinder jsonb; v_zu int; v_diff jsonb;
  v_auf boolean := coalesce((p_plan->>'aufgaben_umhaengen')::boolean, true);
begin
  if v_alt is null or not exists (select 1 from schule.thema where id = v_alt) then raise exception 'alt_thema fehlt oder unbekannt' using errcode = 'P0001'; end if;
  if coalesce(v_n->>'schluessel', '') = '' or coalesce(v_n->>'unterthema', '') = '' then raise exception 'neu.schluessel und neu.unterthema fehlen' using errcode = 'P0001'; end if;
  v_ae := coalesce(nullif(p_plan->>'alte_einheit_id', '')::bigint, schule.thema_einheit(v_alt));
  if v_ae is null or not exists (select 1 from schule.einheit where id = v_ae and thema_id = v_alt) then raise exception 'alte Einheit nicht gefunden' using errcode = 'P0001'; end if;
  -- B3: Kataloge – je Teil mindestens 3 verschiedene Etappen, disjunkt, zusammen vollständig
  select array_agg(distinct q->>'lernziel') into v_kat from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) q where e.id = v_ae;
  if not v_et <@ coalesce(v_kat, '{}') then raise exception 'nicht jede Etappe steht im Katalog der alten Einheit %', v_ae using errcode = 'P0001'; end if;
  v_rest := array(select x from unnest(v_kat) x where not x = any(v_et));
  if cardinality(v_et) < 3 or cardinality(v_rest) < 3 then
    raise exception 'je Teil mindestens 3 Etappen (neu %, Rest %)', cardinality(v_et), cardinality(v_rest) using errcode = 'P0001'; end if;
  if v_ne is not null then
    select array_agg(distinct q->>'lernziel') into v_nkat from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) q where e.id = v_ne;
    if not (coalesce(v_nkat, '{}') @> v_et and v_et @> coalesce(v_nkat, '{}')) then
      raise exception 'Katalog der neuen Einheit % ist nicht genau der neue Teil (%)', v_ne, v_nkat using errcode = 'P0001'; end if;
    if not v_auf and (exists (select 1 from schule.karte_stand k where k.einheit_id = v_ae and k.lernziel = any(v_et))
                      or exists (select 1 from schule.versuch x join schule.aufgabe a on a.id = x.aufgabe_id where a.einheit_id = v_ae and a.variante_gruppe = any(v_et))) then
      raise exception 'aufgaben_umhaengen = false ist bei vorhandenem Lernstand nicht erlaubt' using errcode = 'P0001'; end if;
    if exists (select 1 from schule.testsitzung t where t.einheit_id = v_ae and t.abgeschlossen_am is null) then
      raise exception 'offene Test-Sitzung der alten Einheit – erst abschließen' using errcode = 'P0001'; end if;
  end if;

  select id into v_neu from schule.thema where schluessel = v_n->>'schluessel';
  v_vor := schule.thema_teilen_stand(v_ae, v_ne, v_alt, v_neu);

  -- 1. Thema, Texte, Ort, Voraussetzung, Zuordnungen
  if v_neu is null then
    insert into schule.thema (fach, schluessel, block, unterthema, beschreibung, reihenfolge, pruefstatus, klasse_fest, lehrplan_reihenfolge, lernbereich, lehrplan, kurz)
    select t.fach, v_n->>'schluessel', coalesce(v_n->>'block', t.block), v_n->>'unterthema', v_n->>'beschreibung', coalesce((v_n->>'reihenfolge')::int, t.reihenfolge + 1),
           'ungeprueft', coalesce(v_n->'klasse_fest', t.klasse_fest), coalesce(v_n->'lehrplan_reihenfolge', '{}'::jsonb), v_n->'lernbereich', v_n->'lehrplan', v_n->>'kurz'
      from schule.thema t where t.id = v_alt returning id into v_neu;
  end if;
  insert into schule.etappe_text (thema_id, lernziel, kann) select v_neu, x.lernziel, x.kann from schule.etappe_text x
   where x.thema_id = v_alt and x.lernziel = any(v_et) on conflict (thema_id, lernziel) do nothing;
  if v_b is not null then
    insert into schule.block_thema (block_id, thema_id, reihenfolge) values (v_b, v_neu, coalesce((p_plan->>'block_reihenfolge')::int, 0)) on conflict (block_id, thema_id) do nothing;
  end if;
  insert into schule.voraussetzung (thema_id, braucht_id, begruendung, art)
  select v_neu, v_alt, 'Teil 2 braucht Teil 1 (Thema geteilt nach LK-Regel)', 'hart'
   where not exists (select 1 from schule.voraussetzung v where v.thema_id = v_neu and v.braucht_id = v_alt);
  update schule.zuordnung z set thema_id = v_neu   -- Punkte, die nur Etappen des neuen Teils verlangen
   where z.thema_id = v_alt and z.etappen is not null and not ('*' = any(z.etappen)) and z.etappen <@ v_et
     and not exists (select 1 from schule.zuordnung y where y.eintrag_id = z.eintrag_id and y.thema_id = v_neu);
  get diagnostics v_zu = row_count;

  -- 2. mit neuer Einheit: Katalog verkleinern und Lernstand umhängen (atomar)
  if v_ne is not null then
    if not exists (select 1 from schule.einheit e where e.id = v_ne and e.thema_id = v_neu) then raise exception 'neue Einheit % gehört nicht zum neuen Thema %', v_ne, v_neu using errcode = 'P0001'; end if;
    if exists (select 1 from schule.karte_stand k where k.einheit_id = v_ne and k.lernziel = any(v_et)
                 and exists (select 1 from schule.karte_stand a where a.lernender_id = k.lernender_id and a.einheit_id = v_ae and a.lernziel = k.lernziel)) then
      raise exception 'Kind hat schon Stand in beiden Einheiten – bitte prüfen' using errcode = 'P0001'; end if;
    update schule.einheit e set inhalt = jsonb_set(jsonb_set(jsonb_set(jsonb_set(e.inhalt,
             '{etappen}', coalesce((select jsonb_agg(q order by o) from jsonb_array_elements(e.inhalt->'etappen') with ordinality x(q, o) where not (q->>'lernziel') = any(v_et)), '[]'::jsonb)),
             '{bewertung,lernziele_pflicht}', coalesce((select jsonb_agg(q) from jsonb_array_elements_text(coalesce(e.inhalt#>'{bewertung,lernziele_pflicht}', '[]'::jsonb)) q where not q = any(v_et)), '[]'::jsonb)),
             '{bewertung,lernziele_vertiefung}', coalesce((select jsonb_agg(q) from jsonb_array_elements_text(coalesce(e.inhalt#>'{bewertung,lernziele_vertiefung}', '[]'::jsonb)) q where not q = any(v_et)), '[]'::jsonb)),
             '{bewertung,testaufgaben_je_lernziel}', case when jsonb_typeof(e.inhalt#>'{bewertung,testaufgaben_je_lernziel}') = 'object'
                                                         then (e.inhalt#>'{bewertung,testaufgaben_je_lernziel}') - v_et
                                                         else coalesce(e.inhalt#>'{bewertung,testaufgaben_je_lernziel}', 'null'::jsonb) end)
     where e.id = v_ae and e.inhalt ? 'bewertung';
    update schule.einheit e set inhalt = jsonb_set(e.inhalt, '{etappen}',
             coalesce((select jsonb_agg(q order by o) from jsonb_array_elements(e.inhalt->'etappen') with ordinality x(q, o) where not (q->>'lernziel') = any(v_et)), '[]'::jsonb))
     where e.id = v_ae and not e.inhalt ? 'bewertung';
    if v_auf then
      update schule.aufgabe set einheit_id = v_ne, thema_id = v_neu where einheit_id = v_ae and variante_gruppe = any(v_et);
      get diagnostics v_cnt = row_count; v_um := v_um || jsonb_build_object('aufgabe', v_cnt);
    end if;
    foreach v_tab in array array['karte_stand', 'lernziel_stand', 'besprochen', 'wdh_runde_etappe', 'wdh_staffel_sicherung', 'rueckmeldung'] loop
      if to_regclass('schule.' || v_tab) is not null then
        execute format('update schule.%I set einheit_id = $1 where einheit_id = $2 and lernziel = any($3)', v_tab) using v_ne, v_ae, v_et;
        get diagnostics v_cnt = row_count; v_um := v_um || jsonb_build_object(v_tab, v_cnt);
      end if;
    end loop;
    update schule.misch_ausgabe set einheit_id = v_ne   -- offene Ausgaben, deren Lage eine Etappe des neuen Teils ist
     where einheit_id = v_ae and lernziel = any(v_et) and eingeloest_am is null and verfallen_am is null;
    get diagnostics v_cnt = row_count; v_um := v_um || jsonb_build_object('misch_ausgabe', v_cnt);
    if to_regclass('schule.wackelt_status') is not null then
      execute 'update schule.wackelt_status set einheit_id = $1, thema_id = $2 where einheit_id = $3 and lernziel = any($4)' using v_ne, v_neu, v_ae, v_et;
      get diagnostics v_cnt = row_count; v_um := v_um || jsonb_build_object('wackelt_status', v_cnt);
    end if;
    update schule.abgelegt set einheit_id = v_ne, thema_id = v_neu, bezug = 'etappe:' || v_ne || ':' || lernziel
     where einheit_id = v_ae and lernziel = any(v_et) and bezug = 'etappe:' || v_ae || ':' || lernziel;
    get diagnostics v_cnt = row_count; v_um := v_um || jsonb_build_object('abgelegt', v_cnt);
    update schule.sterne s set bezug = regexp_replace(s.bezug, '^(landung|wdh):' || v_ae || ':', '\1:' || v_ne || ':')
     where s.bezug ~ ('^(landung|wdh):' || v_ae || ':') and split_part(s.bezug, ':', 3) = any(v_et);
    get diagnostics v_cnt = row_count; v_um := v_um || jsonb_build_object('sterne_bezug', v_cnt);
  end if;

  -- Vorher/Nachher je Kind (B4)
  v_nach := schule.thema_teilen_stand(v_ae, v_ne, v_alt, v_neu);
  select jsonb_object_agg(k, jsonb_build_object('vorher', v_vor->k->'fest', 'nachher', v_nach->k->'fest'))
    into v_diff from (select jsonb_object_keys(v_vor) k union select jsonb_object_keys(v_nach)) x
   where (v_vor->k->'fest') is distinct from (v_nach->k->'fest');
  if v_diff is not null then raise exception 'Vorher/Nachher je Kind verschieden: %', v_diff using errcode = 'P0001'; end if;
  select coalesce(jsonb_agg(jsonb_build_object('kind', l.k::bigint,
           'neu_vollstaendig', v_ne is not null and (select count(*) from schule.karte_stand ks where ks.lernender_id = l.k::bigint and ks.einheit_id = v_ne
                                                      and ks.lernziel = any(v_et) and (ks.sitzt or ks.gesetzt_am is not null)) = cardinality(v_et),
           'etappen_neu_erledigt', (select count(*) from schule.karte_stand ks where ks.lernender_id = l.k::bigint and ks.einheit_id = coalesce(v_ne, v_ae)
                                     and ks.lernziel = any(v_et) and (ks.sitzt or ks.gesetzt_am is not null)),
           'bericht_vorher', v_vor->l.k->'bericht', 'bericht_nachher', v_nach->l.k->'bericht') order by l.k::bigint), '[]'::jsonb)
    into v_kinder from (select jsonb_object_keys(v_nach) k) l;
  return jsonb_build_object('ok', true, 'alt_thema', v_alt, 'neu_thema', v_neu, 'alte_einheit', v_ae, 'neue_einheit', v_ne,
    'einheit_fehlt', v_ne is null, 'katalog_alt', to_jsonb(v_rest), 'katalog_neu', to_jsonb(v_et), 'zuordnungen', v_zu, 'umgehaengt', v_um,
    'fest_je_kind', v_nach, 'kinder', v_kinder);
end $function$;
revoke all on function schule.thema_teilen(jsonb, boolean), schule.thema_teilen_ausfuehren(jsonb), schule.thema_teilen_stand(bigint, bigint, bigint, bigint)
  from public, anon, authenticated;

-- Bestand unverändert?
do $mig$
declare v_t text;
begin
  select string_agg(v.t, ', ') into v_t from lk_vorher v join pg_temp.lk_stand() n on n.t = v.t where n.s <> v.s;
  if v_t is not null then raise exception 'LK-S: Bestand verändert (%)', v_t; end if;
  raise notice 'LK-S: Stufen/Plan aller Kinder, Reiseoptionen, Klassen, Lernstand, Sterne, Flug-Abschlüsse, Visum-Regeln, Themen, Voraussetzungen unverändert';
end $mig$;
