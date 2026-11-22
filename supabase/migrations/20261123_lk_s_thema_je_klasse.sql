-- LK-S (22.11.): ein Thema in mehreren Klassen, für alle Schularten (inhalte/AUFTRAEGE.md „Bau-Auftrag LK“, Abschnitt LK-S, mit den Nachträgen
-- „vorhandener Lernstand der Kinder“ und „Route: zweiter Teil eines Themas fliegt ins Nachbarland“). Grundlage: inhalte/pruefung/lehrplan/rs_pruefung_2211.md,
-- Abschnitt 6 (Datenmodell). Einspielen NACH inhalte/pruefung/lehrplan/rs_korrektur_2211.sql, in EINER Transaktion. Unabhängig von LW-S.
--   1. Felder: schule.zuordnung.rolle ('neu' | 'weitergefuehrt', Aussage der Lehrplan-Prüfung) und .etappen (Lernziel-Schlüssel, die dieser Punkt verlangt;
--      null = ganzes Thema); schule.lernender.zweig ('rs_I' | 'rs_II_III', nur Realschule; leer = rs_I).
--   2. Sichten: schule.lehrplan_zweig (Quelle → Schulart, Zweig, Klasse; RS 5/6 „allgemein“ gilt für rs_I und rs_II_III, IB „myp_beide“ für Standard und
--      Extended), schule.thema_lage_klasse (je Schulart, Zweig, Thema und Klasse: Rolle, Etappen dieser Klasse, Lernbereiche, Stunden),
--      schule.thema_lage (je Schulart, Zweig, Thema und Etappe: klasse_ab, klassen[], Rolle je Klasse) und schule.lehrplan_abdeckung
--      (je Lernbereich: Stunden, Punkte, Punkte mit Thema, abgedeckte Stunden).
--      Regeln: nur aktive Basis-Quellen, nicht archivierte Einträge, Zuordnungen ohne pruefstatus 'klaerungsbedarf' (veraltet), Klassen aus Hauptbezügen.
--      klasse_fest gewinnt weiter: Ist es für die Schulart gesetzt, ist das die erste Klasse (ein Wert null = kein Pflichtstoff dieser Schulart);
--      frühere Hauptbezüge zählen dann nicht. Rolle je Klasse: erste Klasse 'neu', spätere 'weitergefuehrt' (die Aussage der Prüfung steht in rolle_lehrplan).
--      Etappe: klasse_ab = erste Klasse, die sie ausdrücklich nennt, sonst die erste Klasse mit „ganzem Thema“.
--   3. Befüllen: schule.lehrplan_rolle_setzen(jsonb) – wiederholbar, ändert nur rolle/etappen vorhandener Zuordnungen, meldet Fehlendes.
--      Hier mit den Realschul-Daten aus rs_pruefung_2211.json (Gruppe I, II/III, RS 5/6); Gym/IB später aus lk_daten_2211.json mit derselben Funktion.
--   4. Schnittstelle: schule_lehrplan_matrix – je Thema `klassen` (Schulart → Zweig → Liste der Klassen mit Rolle, Etappen, Lernbereichen, Stunden),
--      oben `abdeckung` (Schulart → Zweig → Klasse) und je Kind `zweig`; Kindsicht nur `klassen_kind` (Schulart und Zweig des Kindes).
--      schule_lehrplan_thema – zusätzlich `klassen`, `baut_auf` (Voraussetzungen mit Klasse, Verstöße), `weiter_in` (spätere Klassen mit Etappen)
--      und mit lernender_id `klassen_kind` mit Stand je Klasse („2 von 3 Etappen dieser Klasse“). Alle alten Felder bleiben.
--   5. Teilen eines Themas: schule.thema_teilen(plan, probelauf) – wiederholbares Verfahren (Thema anlegen, Etappen/Aufgaben/Lernstand umhängen,
--      Voraussetzung, Ort, Vorher/Nachher je Kind). Hier nur angelegt, NICHT aufgerufen.
-- Unverändert (am Ende geprüft): thema_stufe aller Kinder und Themen (Stufe, im Plan), Reiseoptionen, Plan (route), Lernstand (karte_stand,
-- lernziel_stand), Sterne, Flug-Abschlüsse, Visum-Regeln (v_ort_visum), Klassen (thema_jahrgang). Kein DROP, kein DELETE. Wiederholt ausführbar.

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
comment on column schule.zuordnung.etappen is 'LK-S: Lernziel-Schlüssel der Etappen, die dieser Punkt verlangt; null = ganzes Thema';
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
fest as (     -- klasse_fest je Schulart (gesetzt: gewinnt; Wert null: kein Pflichtstoff)
  select t.id thema_id, f.key schulart, case when jsonb_typeof(f.value) = 'number' then (f.value #>> '{}')::int end klasse
    from schule.thema t cross join lateral jsonb_each(coalesce(t.klasse_fest, '{}'::jsonb)) f),
ab as (       -- erste Klasse je Schulart, Zweig und Thema
  select s.schulart, s.zweig, s.thema_id,
         case when f.thema_id is not null then f.klasse else min(s.klasse) end klasse_ab, f.thema_id is not null fest
    from (select distinct schulart, zweig, thema_id, klasse from z
          union select f2.schulart, lz.zweig, f2.thema_id, f2.klasse from fest f2 join (select distinct schulart, zweig from schule.lehrplan_zweig) lz on lz.schulart = f2.schulart
           where f2.klasse is not null) s
    left join fest f on f.thema_id = s.thema_id and f.schulart = s.schulart
   group by 1, 2, 3, f.thema_id, f.klasse),
k as (        -- Klassen ab klasse_ab (die Klasse aus klasse_fest steht immer drin)
  select ab.schulart, ab.zweig, ab.thema_id, ab.klasse_ab, ab.fest, c.klasse
    from ab cross join lateral (select distinct z.klasse from z where z.schulart = ab.schulart and z.zweig = ab.zweig and z.thema_id = ab.thema_id and z.klasse >= ab.klasse_ab
                                union select ab.klasse_ab) c
   where ab.klasse_ab is not null)
select k.schulart, k.zweig, k.thema_id, k.klasse, k.klasse_ab,
       case when k.klasse = k.klasse_ab then 'neu' else 'weitergefuehrt' end rolle,
       (select array_agg(distinct z.rolle order by z.rolle) filter (where z.rolle is not null) from z
         where z.schulart = k.schulart and z.zweig = k.zweig and z.thema_id = k.thema_id and z.klasse = k.klasse) rolle_lehrplan,
       case when bool_or(z.eintrag_id is not null and z.etappen is null) or count(z.eintrag_id) = 0 then null
            else (select array_agg(distinct x order by x) from z z2 cross join lateral unnest(z2.etappen) x
                   where z2.schulart = k.schulart and z2.zweig = k.zweig and z2.thema_id = k.thema_id and z2.klasse = k.klasse) end etappen,
       (select coalesce(jsonb_agg(jsonb_build_object('eintrag_id', lb.id, 'pfad', lb.pfad, 'titel', lb.text, 'stunden', lb.stunden) order by lb.reihenfolge, lb.id), '[]'::jsonb)
          from schule.eintrag lb where lb.id in (select schule.eintrag_lernbereich(z3.eintrag_id) from z z3
                                                where z3.schulart = k.schulart and z3.zweig = k.zweig and z3.thema_id = k.thema_id and z3.klasse = k.klasse)) lernbereiche,
       count(z.eintrag_id) punkte,
       count(z.eintrag_id) = 0 nur_klasse_fest
  from k left join z on z.schulart = k.schulart and z.zweig = k.zweig and z.thema_id = k.thema_id and z.klasse = k.klasse
 group by k.schulart, k.zweig, k.thema_id, k.klasse, k.klasse_ab;
comment on view schule.thema_lage_klasse is 'LK-S: je Schulart, Zweig, Thema und Klasse (ab der ersten Klasse): Rolle (erste Klasse neu, sonst weitergefuehrt), Etappen dieser Klasse (null = ganzes Thema), Lernbereiche mit Stunden';

create or replace view schule.thema_lage as
with et as (
  select t.id thema_id, q->>'lernziel' lernziel, o
    from schule.thema t join schule.einheit e on e.id = schule.thema_einheit(t.id)
    cross join lateral jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality x(q, o))
select k.schulart, k.zweig, k.thema_id, null::text lernziel, min(k.klasse_ab) klasse_ab, array_agg(k.klasse order by k.klasse) klassen,
       jsonb_object_agg(k.klasse::text, k.rolle) rollen
  from schule.thema_lage_klasse k group by 1, 2, 3
union all
select k.schulart, k.zweig, k.thema_id, et.lernziel,
       coalesce(min(k.klasse) filter (where et.lernziel = any(k.etappen)), min(k.klasse) filter (where k.etappen is null)) klasse_ab,
       array_agg(k.klasse order by k.klasse) filter (where k.etappen is null or et.lernziel = any(k.etappen)) klassen,
       jsonb_object_agg(k.klasse::text, k.rolle) filter (where k.etappen is null or et.lernziel = any(k.etappen)) rollen
  from schule.thema_lage_klasse k join et on et.thema_id = k.thema_id group by 1, 2, 3, 4;
comment on view schule.thema_lage is 'LK-S: je Schulart, Zweig, Thema (lernziel null) und Etappe: klasse_ab, klassen[], Rolle je Klasse';

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
       round(coalesce(lb.stunden, 0) * m.punkte_mit_thema / nullif(m.punkte, 0), 1) stunden_abgedeckt, lb.reihenfolge
  from schule.eintrag lb join m on m.lb_id = lb.id and not lb.archiviert join schule.lehrplan_zweig lz on lz.quelle_id = lb.quelle_id;
comment on view schule.lehrplan_abdeckung is 'LK-S: je Lernbereich Stunden, Punkte, Punkte mit Hauptthema, abgedeckte Stunden (Stunden × Anteil der Punkte mit Thema)';

revoke all on schule.lehrplan_zweig, schule.thema_lage_klasse, schule.thema_lage, schule.lehrplan_abdeckung from public, anon, authenticated;

-- 3. Befüllen (wiederholbar): [{eintrag_id, thema_id|thema, rolle?, etappen? (Liste oder "a, b")}] – nur vorhandene Zuordnungen, nur übergebene Felder
create or replace function schule.lehrplan_rolle_setzen(p_daten jsonb)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare x jsonb; v_e bigint; v_t bigint; v_r text; v_et text[]; v_bekannt text[]; v_n int; v_gesetzt int := 0; v_gleich int := 0;
  v_fehlt jsonb := '[]'::jsonb; v_unbekannt jsonb := '[]'::jsonb;
begin
  if jsonb_typeof(p_daten) is distinct from 'array' then raise exception 'Liste erwartet' using errcode = 'P0001'; end if;
  for x in select * from jsonb_array_elements(p_daten) loop
    v_e := (x->>'eintrag_id')::bigint; v_t := coalesce(x->>'thema_id', x->>'thema')::bigint; v_r := x->>'rolle';
    if v_r is not null and v_r not in ('neu', 'weitergefuehrt') then raise exception 'rolle % unbekannt (Eintrag %)', v_r, v_e using errcode = 'P0001'; end if;
    v_et := case jsonb_typeof(x->'etappen') when 'array' then array(select jsonb_array_elements_text(x->'etappen'))
                                            when 'string' then array(select trim(s) from unnest(string_to_array(x->>'etappen', ',')) s where trim(s) <> '') end;
    if v_et is not null then
      select array_agg(q->>'lernziel') into v_bekannt from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) q
       where e.id = schule.thema_einheit(v_t);
      if exists (select 1 from unnest(v_et) s where not s = any(coalesce(v_bekannt, '{}'))) then
        v_unbekannt := v_unbekannt || jsonb_build_object('eintrag_id', v_e, 'thema_id', v_t,
                         'etappen', to_jsonb(array(select s from unnest(v_et) s where not s = any(coalesce(v_bekannt, '{}')))));
        v_et := array(select s from unnest(v_et) s where s = any(coalesce(v_bekannt, '{}')));
        if cardinality(v_et) = 0 then v_et := null; end if;
      end if;
    end if;
    if not exists (select 1 from schule.zuordnung z where z.eintrag_id = v_e and z.thema_id = v_t) then
      v_fehlt := v_fehlt || jsonb_build_object('eintrag_id', v_e, 'thema_id', v_t); continue;
    end if;
    update schule.zuordnung z set rolle = case when x ? 'rolle' then v_r else z.rolle end,
                                  etappen = case when x ? 'etappen' then v_et else z.etappen end
     where z.eintrag_id = v_e and z.thema_id = v_t
       and (z.rolle is distinct from case when x ? 'rolle' then v_r else z.rolle end or z.etappen is distinct from case when x ? 'etappen' then v_et else z.etappen end);
    get diagnostics v_n = row_count;
    if v_n > 0 then v_gesetzt := v_gesetzt + 1; else v_gleich := v_gleich + 1; end if;
  end loop;
  return jsonb_build_object('gesetzt', v_gesetzt, 'gleich', v_gleich, 'ohne_zuordnung', v_fehlt, 'unbekannte_etappen', v_unbekannt);
end $function$;
revoke all on function schule.lehrplan_rolle_setzen(jsonb) from public, anon, authenticated;

-- Realschule aus rs_pruefung_2211.json (zuordnung_vorschlag[].klasse_bezug „neu…“/„weitergeführt“; neue_etappen, Titel auf Lernziel-Schlüssel abgebildet:
-- 61 begriffe/laplace/laplace_pruefen/gegenereignis/grosse_zahlen; 33 „Steigung m und Achsenabschnitt t, Parameter“ → ablesen, wirkung;
-- „Geradengleichung aus zwei Angaben, Parallelenscharen“ → zwei_punkte, lage; 44 vierecke; 91 rotation, axialschnitt; 46 drehung, punktspiegelung.
-- 931/44 „Vierecke konstruieren (Etappe fehlt)“ hat keine Etappe → ohne etappen). „nur Nebenbezug“, „vorgezogen“, „stillgelegt“ setzen keine Rolle.
do $$
declare r jsonb;
begin
  r := schule.lehrplan_rolle_setzen($json$[{"eintrag_id":292,"thema_id":15,"rolle":"neu"},{"eintrag_id":293,"thema_id":15,"rolle":"neu"},{"eintrag_id":294,"thema_id":15,"rolle":"neu"},{"eintrag_id":295,"thema_id":15,"rolle":"neu"},{"eintrag_id":296,"thema_id":15,"rolle":"neu"},{"eintrag_id":300,"thema_id":18,"rolle":"neu"},{"eintrag_id":301,"thema_id":18,"rolle":"neu"},{"eintrag_id":302,"thema_id":18,"rolle":"neu"},{"eintrag_id":303,"thema_id":19,"rolle":"neu"},{"eintrag_id":303,"thema_id":67,"rolle":"neu"},{"eintrag_id":304,"thema_id":67,"rolle":"neu"},{"eintrag_id":305,"thema_id":17,"rolle":"neu"},{"eintrag_id":307,"thema_id":60,"rolle":"neu"},{"eintrag_id":308,"thema_id":60,"rolle":"neu"},{"eintrag_id":310,"thema_id":16,"rolle":"neu"},{"eintrag_id":311,"thema_id":16,"rolle":"neu"},{"eintrag_id":312,"thema_id":16,"rolle":"neu"},{"eintrag_id":313,"thema_id":16,"rolle":"neu"},{"eintrag_id":314,"thema_id":16,"rolle":"neu"},{"eintrag_id":314,"thema_id":18,"rolle":"neu"},{"eintrag_id":315,"thema_id":16,"rolle":"neu"},{"eintrag_id":315,"thema_id":18,"rolle":"neu"},{"eintrag_id":316,"thema_id":16,"rolle":"neu"},{"eintrag_id":318,"thema_id":42,"rolle":"neu"},{"eintrag_id":319,"thema_id":42,"rolle":"neu"},{"eintrag_id":320,"thema_id":42,"rolle":"neu"},{"eintrag_id":321,"thema_id":42,"rolle":"neu"},{"eintrag_id":322,"thema_id":42,"rolle":"neu"},{"eintrag_id":323,"thema_id":42,"rolle":"neu"},{"eintrag_id":324,"thema_id":52,"rolle":"neu"},{"eintrag_id":325,"thema_id":52,"rolle":"neu"},{"eintrag_id":325,"thema_id":91,"rolle":"neu"},{"eintrag_id":326,"thema_id":42,"rolle":"neu"},{"eintrag_id":326,"thema_id":52,"rolle":"neu"},{"eintrag_id":328,"thema_id":25,"rolle":"neu"},{"eintrag_id":329,"thema_id":25,"rolle":"neu"},{"eintrag_id":330,"thema_id":25,"rolle":"neu"},{"eintrag_id":331,"thema_id":25,"rolle":"neu"},{"eintrag_id":332,"thema_id":25,"rolle":"neu"},{"eintrag_id":332,"thema_id":26,"rolle":"neu"},{"eintrag_id":333,"thema_id":25,"rolle":"neu"},{"eintrag_id":335,"thema_id":50,"rolle":"neu"},{"eintrag_id":336,"thema_id":50,"rolle":"neu"},{"eintrag_id":337,"thema_id":50,"rolle":"neu"},{"eintrag_id":338,"thema_id":50,"rolle":"neu"},{"eintrag_id":339,"thema_id":50,"rolle":"neu"},{"eintrag_id":340,"thema_id":50,"rolle":"neu"},{"eintrag_id":342,"thema_id":57,"rolle":"neu"},{"eintrag_id":343,"thema_id":57,"rolle":"neu"},{"eintrag_id":344,"thema_id":57,"rolle":"neu"},{"eintrag_id":346,"thema_id":21,"rolle":"neu"},{"eintrag_id":347,"thema_id":21,"rolle":"neu"},{"eintrag_id":348,"thema_id":21,"rolle":"neu"},{"eintrag_id":349,"thema_id":21,"rolle":"neu"},{"eintrag_id":350,"thema_id":22,"rolle":"neu"},{"eintrag_id":351,"thema_id":22,"rolle":"neu"},{"eintrag_id":352,"thema_id":21,"rolle":"neu"},{"eintrag_id":352,"thema_id":22,"rolle":"neu"},{"eintrag_id":352,"thema_id":24,"rolle":"neu"},{"eintrag_id":353,"thema_id":21,"rolle":"neu"},{"eintrag_id":353,"thema_id":22,"rolle":"neu"},{"eintrag_id":354,"thema_id":21,"rolle":"neu"},{"eintrag_id":355,"thema_id":23,"rolle":"neu"},{"eintrag_id":356,"thema_id":23,"rolle":"neu"},{"eintrag_id":357,"thema_id":23,"rolle":"neu"},{"eintrag_id":357,"thema_id":25,"rolle":"weitergefuehrt"},{"eintrag_id":359,"thema_id":46,"rolle":"neu"},{"eintrag_id":360,"thema_id":46,"rolle":"neu"},{"eintrag_id":361,"thema_id":44,"rolle":"neu"},{"eintrag_id":361,"thema_id":46,"rolle":"neu"},{"eintrag_id":362,"thema_id":46,"rolle":"neu"},{"eintrag_id":363,"thema_id":46,"rolle":"neu"},{"eintrag_id":365,"thema_id":50,"rolle":"weitergefuehrt"},{"eintrag_id":365,"thema_id":99,"rolle":"neu"},{"eintrag_id":366,"thema_id":99,"rolle":"neu"},{"eintrag_id":367,"thema_id":99,"rolle":"neu"},{"eintrag_id":368,"thema_id":99,"rolle":"neu"},{"eintrag_id":369,"thema_id":99,"rolle":"neu"},{"eintrag_id":370,"thema_id":50,"rolle":"weitergefuehrt"},{"eintrag_id":370,"thema_id":53,"rolle":"neu"},{"eintrag_id":370,"thema_id":99,"rolle":"neu"},{"eintrag_id":371,"thema_id":53,"rolle":"neu"},{"eintrag_id":371,"thema_id":100,"rolle":"neu"},{"eintrag_id":372,"thema_id":100,"rolle":"neu"},{"eintrag_id":373,"thema_id":100,"rolle":"neu"},{"eintrag_id":374,"thema_id":100,"rolle":"neu"},{"eintrag_id":375,"thema_id":100,"rolle":"neu"},{"eintrag_id":377,"thema_id":28,"rolle":"neu"},{"eintrag_id":378,"thema_id":28,"rolle":"neu"},{"eintrag_id":379,"thema_id":28,"rolle":"neu"},{"eintrag_id":380,"thema_id":28,"rolle":"neu"},{"eintrag_id":380,"thema_id":29,"rolle":"neu"},{"eintrag_id":381,"thema_id":1,"rolle":"neu"},{"eintrag_id":382,"thema_id":1,"rolle":"neu"},{"eintrag_id":383,"thema_id":1,"rolle":"neu"},{"eintrag_id":385,"thema_id":26,"rolle":"weitergefuehrt"},{"eintrag_id":386,"thema_id":26,"rolle":"weitergefuehrt"},{"eintrag_id":387,"thema_id":26,"rolle":"weitergefuehrt"},{"eintrag_id":388,"thema_id":26,"rolle":"weitergefuehrt"},{"eintrag_id":389,"thema_id":24,"rolle":"neu"},{"eintrag_id":390,"thema_id":24,"rolle":"neu"},{"eintrag_id":493,"thema_id":46,"rolle":"weitergefuehrt"},{"eintrag_id":494,"thema_id":52,"rolle":"weitergefuehrt"},{"eintrag_id":494,"thema_id":91,"rolle":"weitergefuehrt"},{"eintrag_id":497,"thema_id":32,"rolle":"neu"},{"eintrag_id":497,"thema_id":33,"rolle":"neu"},{"eintrag_id":499,"thema_id":20,"rolle":"neu"},{"eintrag_id":500,"thema_id":47,"rolle":"neu"},{"eintrag_id":503,"thema_id":53,"rolle":"weitergefuehrt"},{"eintrag_id":503,"thema_id":92,"rolle":"neu"},{"eintrag_id":505,"thema_id":8,"rolle":"neu"},{"eintrag_id":505,"thema_id":13,"rolle":"neu"},{"eintrag_id":505,"thema_id":35,"rolle":"neu"},{"eintrag_id":507,"thema_id":20,"rolle":"neu"},{"eintrag_id":511,"thema_id":33,"rolle":"weitergefuehrt"},{"eintrag_id":514,"thema_id":14,"rolle":"neu"},{"eintrag_id":514,"thema_id":38,"rolle":"neu"},{"eintrag_id":514,"thema_id":56,"rolle":"neu"},{"eintrag_id":515,"thema_id":49,"rolle":"neu"},{"eintrag_id":520,"thema_id":52,"rolle":"weitergefuehrt"},{"eintrag_id":520,"thema_id":53,"rolle":"weitergefuehrt"},{"eintrag_id":520,"thema_id":92,"rolle":"neu"},{"eintrag_id":693,"thema_id":46,"rolle":"weitergefuehrt"},{"eintrag_id":697,"thema_id":52,"rolle":"weitergefuehrt"},{"eintrag_id":697,"thema_id":91,"rolle":"neu"},{"eintrag_id":702,"thema_id":29,"rolle":"neu"},{"eintrag_id":702,"thema_id":102,"rolle":"neu"},{"eintrag_id":703,"thema_id":2,"rolle":"neu"},{"eintrag_id":704,"thema_id":3,"rolle":"neu"},{"eintrag_id":705,"thema_id":2,"rolle":"neu"},{"eintrag_id":705,"thema_id":3,"rolle":"neu"},{"eintrag_id":712,"thema_id":46,"rolle":"weitergefuehrt"},{"eintrag_id":717,"thema_id":29,"rolle":"neu"},{"eintrag_id":717,"thema_id":102,"rolle":"neu"},{"eintrag_id":718,"thema_id":2,"rolle":"neu"},{"eintrag_id":719,"thema_id":3,"rolle":"neu"},{"eintrag_id":720,"thema_id":2,"rolle":"neu"},{"eintrag_id":720,"thema_id":3,"rolle":"neu"},{"eintrag_id":732,"thema_id":29,"rolle":"weitergefuehrt"},{"eintrag_id":733,"thema_id":29,"rolle":"weitergefuehrt"},{"eintrag_id":733,"thema_id":35,"rolle":"neu"},{"eintrag_id":733,"thema_id":97,"rolle":"neu"},{"eintrag_id":734,"thema_id":2,"rolle":"weitergefuehrt"},{"eintrag_id":734,"thema_id":3,"rolle":"weitergefuehrt"},{"eintrag_id":736,"thema_id":31,"rolle":"neu"},{"eintrag_id":737,"thema_id":5,"rolle":"neu"},{"eintrag_id":744,"thema_id":52,"rolle":"weitergefuehrt"},{"eintrag_id":744,"thema_id":91,"rolle":"neu"},{"eintrag_id":747,"thema_id":29,"rolle":"weitergefuehrt"},{"eintrag_id":748,"thema_id":29,"rolle":"weitergefuehrt"},{"eintrag_id":748,"thema_id":35,"rolle":"neu"},{"eintrag_id":748,"thema_id":97,"rolle":"neu"},{"eintrag_id":749,"thema_id":2,"rolle":"weitergefuehrt"},{"eintrag_id":751,"thema_id":31,"rolle":"neu"},{"eintrag_id":752,"thema_id":5,"rolle":"neu"},{"eintrag_id":758,"thema_id":20,"rolle":"neu"},{"eintrag_id":759,"thema_id":8,"rolle":"neu"},{"eintrag_id":760,"thema_id":20,"rolle":"neu"},{"eintrag_id":762,"thema_id":47,"rolle":"neu"},{"eintrag_id":763,"thema_id":47,"rolle":"neu"},{"eintrag_id":764,"thema_id":47,"rolle":"neu"},{"eintrag_id":765,"thema_id":47,"rolle":"neu"},{"eintrag_id":766,"thema_id":47,"rolle":"neu"},{"eintrag_id":767,"thema_id":47,"rolle":"neu"},{"eintrag_id":768,"thema_id":47,"rolle":"neu"},{"eintrag_id":769,"thema_id":47,"rolle":"neu"},{"eintrag_id":771,"thema_id":54,"rolle":"neu"},{"eintrag_id":772,"thema_id":54,"rolle":"neu"},{"eintrag_id":773,"thema_id":54,"rolle":"neu"},{"eintrag_id":774,"thema_id":54,"rolle":"neu"},{"eintrag_id":775,"thema_id":54,"rolle":"neu"},{"eintrag_id":776,"thema_id":54,"rolle":"neu"},{"eintrag_id":776,"thema_id":55,"rolle":"neu"},{"eintrag_id":778,"thema_id":51,"rolle":"neu"},{"eintrag_id":779,"thema_id":51,"rolle":"neu"},{"eintrag_id":781,"thema_id":92,"rolle":"neu"},{"eintrag_id":782,"thema_id":52,"rolle":"weitergefuehrt"},{"eintrag_id":782,"thema_id":92,"rolle":"neu"},{"eintrag_id":783,"thema_id":51,"rolle":"neu"},{"eintrag_id":783,"thema_id":53,"rolle":"weitergefuehrt"},{"eintrag_id":783,"thema_id":92,"rolle":"neu"},{"eintrag_id":784,"thema_id":92,"rolle":"neu"},{"eintrag_id":786,"thema_id":6,"rolle":"neu"},{"eintrag_id":788,"thema_id":8,"rolle":"neu"},{"eintrag_id":788,"thema_id":35,"rolle":"neu"},{"eintrag_id":789,"thema_id":8,"rolle":"neu"},{"eintrag_id":789,"thema_id":35,"rolle":"neu"},{"eintrag_id":790,"thema_id":8,"rolle":"neu"},{"eintrag_id":790,"thema_id":35,"rolle":"neu"},{"eintrag_id":791,"thema_id":8,"rolle":"neu"},{"eintrag_id":791,"thema_id":35,"rolle":"neu"},{"eintrag_id":792,"thema_id":35,"rolle":"neu"},{"eintrag_id":793,"thema_id":8,"rolle":"neu"},{"eintrag_id":794,"thema_id":8,"rolle":"neu"},{"eintrag_id":795,"thema_id":8,"rolle":"neu"},{"eintrag_id":795,"thema_id":35,"rolle":"neu"},{"eintrag_id":796,"thema_id":13,"rolle":"neu"},{"eintrag_id":798,"thema_id":61,"rolle":"neu","etappen":["grosse_zahlen"]},{"eintrag_id":799,"thema_id":61,"rolle":"neu","etappen":["laplace","laplace_pruefen"]},{"eintrag_id":800,"thema_id":61,"rolle":"neu","etappen":["begriffe"]},{"eintrag_id":801,"thema_id":61,"rolle":"neu","etappen":["gegenereignis"]},{"eintrag_id":802,"thema_id":61,"rolle":"neu","etappen":["laplace"]},{"eintrag_id":804,"thema_id":8,"rolle":"neu"},{"eintrag_id":815,"thema_id":6,"rolle":"neu"},{"eintrag_id":819,"thema_id":14,"rolle":"neu"},{"eintrag_id":819,"thema_id":38,"rolle":"neu"},{"eintrag_id":819,"thema_id":56,"rolle":"neu"},{"eintrag_id":820,"thema_id":14,"rolle":"neu"},{"eintrag_id":820,"thema_id":33,"rolle":"weitergefuehrt"},{"eintrag_id":820,"thema_id":38,"rolle":"neu"},{"eintrag_id":820,"thema_id":56,"rolle":"neu"},{"eintrag_id":821,"thema_id":38,"rolle":"neu"},{"eintrag_id":822,"thema_id":14,"rolle":"neu"},{"eintrag_id":822,"thema_id":38,"rolle":"neu"},{"eintrag_id":822,"thema_id":56,"rolle":"neu"},{"eintrag_id":823,"thema_id":38,"rolle":"neu"},{"eintrag_id":823,"thema_id":56,"rolle":"neu"},{"eintrag_id":824,"thema_id":38,"rolle":"neu"},{"eintrag_id":824,"thema_id":56,"rolle":"neu"},{"eintrag_id":825,"thema_id":14,"rolle":"neu"},{"eintrag_id":825,"thema_id":38,"rolle":"neu"},{"eintrag_id":825,"thema_id":56,"rolle":"neu"},{"eintrag_id":826,"thema_id":14,"rolle":"neu"},{"eintrag_id":826,"thema_id":38,"rolle":"neu"},{"eintrag_id":826,"thema_id":56,"rolle":"neu"},{"eintrag_id":827,"thema_id":14,"rolle":"neu"},{"eintrag_id":828,"thema_id":49,"rolle":"neu"},{"eintrag_id":828,"thema_id":56,"rolle":"neu"},{"eintrag_id":829,"thema_id":49,"rolle":"neu"},{"eintrag_id":829,"thema_id":56,"rolle":"neu"},{"eintrag_id":831,"thema_id":49,"rolle":"neu"},{"eintrag_id":832,"thema_id":49,"rolle":"neu"},{"eintrag_id":833,"thema_id":36,"rolle":"neu"},{"eintrag_id":833,"thema_id":37,"rolle":"neu"},{"eintrag_id":833,"thema_id":49,"rolle":"neu"},{"eintrag_id":834,"thema_id":49,"rolle":"neu"},{"eintrag_id":836,"thema_id":96,"rolle":"neu"},{"eintrag_id":837,"thema_id":96,"rolle":"neu"},{"eintrag_id":838,"thema_id":36,"rolle":"neu"},{"eintrag_id":838,"thema_id":96,"rolle":"neu"},{"eintrag_id":839,"thema_id":36,"rolle":"neu"},{"eintrag_id":841,"thema_id":10,"rolle":"neu"},{"eintrag_id":841,"thema_id":37,"rolle":"neu"},{"eintrag_id":842,"thema_id":37,"rolle":"neu"},{"eintrag_id":843,"thema_id":37,"rolle":"neu"},{"eintrag_id":845,"thema_id":62,"rolle":"neu"},{"eintrag_id":846,"thema_id":62,"rolle":"neu"},{"eintrag_id":852,"thema_id":10,"rolle":"neu"},{"eintrag_id":855,"thema_id":35,"rolle":"neu"},{"eintrag_id":856,"thema_id":35,"rolle":"neu"},{"eintrag_id":857,"thema_id":35,"rolle":"neu"},{"eintrag_id":858,"thema_id":35,"rolle":"neu"},{"eintrag_id":858,"thema_id":97,"rolle":"weitergefuehrt"},{"eintrag_id":859,"thema_id":8,"rolle":"weitergefuehrt"},{"eintrag_id":860,"thema_id":8,"rolle":"weitergefuehrt"},{"eintrag_id":864,"thema_id":30,"rolle":"neu"},{"eintrag_id":865,"thema_id":102,"rolle":"neu"},{"eintrag_id":866,"thema_id":19,"rolle":"neu"},{"eintrag_id":866,"thema_id":30,"rolle":"neu"},{"eintrag_id":868,"thema_id":46,"rolle":"weitergefuehrt"},{"eintrag_id":869,"thema_id":46,"rolle":"weitergefuehrt"},{"eintrag_id":870,"thema_id":46,"rolle":"weitergefuehrt"},{"eintrag_id":872,"thema_id":50,"rolle":"weitergefuehrt"},{"eintrag_id":872,"thema_id":74,"rolle":"neu"},{"eintrag_id":873,"thema_id":98,"rolle":"neu"},{"eintrag_id":874,"thema_id":98,"rolle":"neu"},{"eintrag_id":876,"thema_id":44,"rolle":"neu"},{"eintrag_id":877,"thema_id":44,"rolle":"neu"},{"eintrag_id":878,"thema_id":44,"rolle":"neu"},{"eintrag_id":879,"thema_id":44,"rolle":"neu"},{"eintrag_id":881,"thema_id":91,"rolle":"neu"},{"eintrag_id":882,"thema_id":52,"rolle":"weitergefuehrt"},{"eintrag_id":882,"thema_id":91,"rolle":"neu"},{"eintrag_id":883,"thema_id":91,"rolle":"neu"},{"eintrag_id":885,"thema_id":73,"rolle":"neu"},{"eintrag_id":886,"thema_id":45,"rolle":"neu"},{"eintrag_id":887,"thema_id":73,"rolle":"neu"},{"eintrag_id":888,"thema_id":73,"rolle":"neu"},{"eintrag_id":889,"thema_id":45,"rolle":"neu"},{"eintrag_id":889,"thema_id":47,"rolle":"neu"},{"eintrag_id":891,"thema_id":94,"rolle":"neu"},{"eintrag_id":892,"thema_id":24,"rolle":"weitergefuehrt"},{"eintrag_id":892,"thema_id":71,"rolle":"neu"},{"eintrag_id":893,"thema_id":93,"rolle":"neu"},{"eintrag_id":894,"thema_id":93,"rolle":"neu"},{"eintrag_id":895,"thema_id":26,"rolle":"weitergefuehrt"},{"eintrag_id":895,"thema_id":93,"rolle":"neu"},{"eintrag_id":897,"thema_id":58,"rolle":"neu"},{"eintrag_id":897,"thema_id":95,"rolle":"neu"},{"eintrag_id":898,"thema_id":58,"rolle":"neu"},{"eintrag_id":898,"thema_id":95,"rolle":"neu"},{"eintrag_id":899,"thema_id":81,"rolle":"neu"},{"eintrag_id":900,"thema_id":57,"rolle":"weitergefuehrt"},{"eintrag_id":902,"thema_id":30,"rolle":"neu"},{"eintrag_id":903,"thema_id":102,"rolle":"neu"},{"eintrag_id":904,"thema_id":19,"rolle":"neu"},{"eintrag_id":904,"thema_id":30,"rolle":"neu"},{"eintrag_id":906,"thema_id":46,"rolle":"weitergefuehrt"},{"eintrag_id":907,"thema_id":46,"rolle":"weitergefuehrt"},{"eintrag_id":908,"thema_id":46,"rolle":"weitergefuehrt"},{"eintrag_id":910,"thema_id":50,"rolle":"weitergefuehrt"},{"eintrag_id":910,"thema_id":74,"rolle":"neu"},{"eintrag_id":911,"thema_id":98,"rolle":"neu"},{"eintrag_id":912,"thema_id":98,"rolle":"neu"},{"eintrag_id":914,"thema_id":45,"rolle":"neu"},{"eintrag_id":914,"thema_id":73,"rolle":"neu"},{"eintrag_id":915,"thema_id":45,"rolle":"neu"},{"eintrag_id":916,"thema_id":73,"rolle":"neu"},{"eintrag_id":917,"thema_id":45,"rolle":"neu"},{"eintrag_id":919,"thema_id":94,"rolle":"neu"},{"eintrag_id":920,"thema_id":24,"rolle":"weitergefuehrt"},{"eintrag_id":920,"thema_id":71,"rolle":"neu"},{"eintrag_id":921,"thema_id":93,"rolle":"neu"},{"eintrag_id":922,"thema_id":93,"rolle":"neu"},{"eintrag_id":923,"thema_id":26,"rolle":"weitergefuehrt"},{"eintrag_id":923,"thema_id":93,"rolle":"neu"},{"eintrag_id":925,"thema_id":58,"rolle":"neu"},{"eintrag_id":925,"thema_id":95,"rolle":"neu"},{"eintrag_id":926,"thema_id":58,"rolle":"neu"},{"eintrag_id":926,"thema_id":95,"rolle":"neu"},{"eintrag_id":927,"thema_id":81,"rolle":"neu"},{"eintrag_id":928,"thema_id":57,"rolle":"weitergefuehrt"},{"eintrag_id":930,"thema_id":42,"rolle":"weitergefuehrt"},{"eintrag_id":930,"thema_id":44,"rolle":"neu","etappen":["vierecke"]},{"eintrag_id":930,"thema_id":46,"rolle":"weitergefuehrt"},{"eintrag_id":931,"thema_id":44,"rolle":"neu"},{"eintrag_id":933,"thema_id":46,"rolle":"neu","etappen":["drehung"]},{"eintrag_id":934,"thema_id":46,"rolle":"neu","etappen":["punktspiegelung"]},{"eintrag_id":935,"thema_id":46,"rolle":"neu","etappen":["drehung"]},{"eintrag_id":936,"thema_id":46,"rolle":"neu","etappen":["drehung"]},{"eintrag_id":937,"thema_id":49,"rolle":"neu"},{"eintrag_id":939,"thema_id":91,"rolle":"weitergefuehrt"},{"eintrag_id":940,"thema_id":91,"rolle":"weitergefuehrt"},{"eintrag_id":941,"thema_id":91,"rolle":"weitergefuehrt"},{"eintrag_id":943,"thema_id":32,"rolle":"neu"},{"eintrag_id":944,"thema_id":32,"rolle":"neu"},{"eintrag_id":944,"thema_id":33,"rolle":"neu"},{"eintrag_id":945,"thema_id":32,"rolle":"neu"},{"eintrag_id":945,"thema_id":33,"rolle":"neu"},{"eintrag_id":946,"thema_id":32,"rolle":"neu"},{"eintrag_id":946,"thema_id":33,"rolle":"neu"},{"eintrag_id":947,"thema_id":33,"rolle":"neu"},{"eintrag_id":948,"thema_id":33,"rolle":"neu"},{"eintrag_id":948,"thema_id":74,"rolle":"weitergefuehrt"},{"eintrag_id":950,"thema_id":60,"rolle":"weitergefuehrt"},{"eintrag_id":950,"thema_id":61,"rolle":"neu"},{"eintrag_id":951,"thema_id":61,"rolle":"neu"},{"eintrag_id":953,"thema_id":44,"rolle":"neu"},{"eintrag_id":954,"thema_id":44,"rolle":"neu"},{"eintrag_id":955,"thema_id":44,"rolle":"neu"},{"eintrag_id":956,"thema_id":42,"rolle":"weitergefuehrt"},{"eintrag_id":956,"thema_id":44,"rolle":"neu"},{"eintrag_id":956,"thema_id":46,"rolle":"weitergefuehrt"},{"eintrag_id":957,"thema_id":44,"rolle":"neu"},{"eintrag_id":959,"thema_id":91,"rolle":"neu"},{"eintrag_id":960,"thema_id":91,"rolle":"neu"},{"eintrag_id":962,"thema_id":32,"rolle":"neu"},{"eintrag_id":963,"thema_id":32,"rolle":"neu"},{"eintrag_id":963,"thema_id":33,"rolle":"neu"},{"eintrag_id":964,"thema_id":33,"rolle":"neu"},{"eintrag_id":965,"thema_id":33,"rolle":"neu"},{"eintrag_id":966,"thema_id":33,"rolle":"neu"},{"eintrag_id":968,"thema_id":60,"rolle":"weitergefuehrt"},{"eintrag_id":968,"thema_id":61,"rolle":"neu"},{"eintrag_id":969,"thema_id":61,"rolle":"neu"},{"eintrag_id":971,"thema_id":20,"rolle":"neu"},{"eintrag_id":972,"thema_id":20,"rolle":"neu"},{"eintrag_id":974,"thema_id":47,"rolle":"neu"},{"eintrag_id":975,"thema_id":47,"rolle":"neu"},{"eintrag_id":976,"thema_id":47,"rolle":"neu"},{"eintrag_id":978,"thema_id":54,"rolle":"neu"},{"eintrag_id":979,"thema_id":54,"rolle":"neu"},{"eintrag_id":980,"thema_id":54,"rolle":"neu"},{"eintrag_id":981,"thema_id":54,"rolle":"neu"},{"eintrag_id":982,"thema_id":54,"rolle":"neu"},{"eintrag_id":983,"thema_id":54,"rolle":"neu"},{"eintrag_id":983,"thema_id":55,"rolle":"neu"},{"eintrag_id":985,"thema_id":51,"rolle":"neu"},{"eintrag_id":986,"thema_id":51,"rolle":"neu"},{"eintrag_id":988,"thema_id":33,"rolle":"neu","etappen":["ablesen","wirkung"]},{"eintrag_id":989,"thema_id":33,"rolle":"neu","etappen":["aufstellen"]},{"eintrag_id":990,"thema_id":33,"rolle":"neu","etappen":["zwei_punkte","lage"]},{"eintrag_id":991,"thema_id":33,"rolle":"weitergefuehrt"},{"eintrag_id":991,"thema_id":74,"rolle":"weitergefuehrt"},{"eintrag_id":993,"thema_id":61,"rolle":"neu","etappen":["grosse_zahlen"]},{"eintrag_id":994,"thema_id":61,"rolle":"neu","etappen":["laplace","laplace_pruefen"]},{"eintrag_id":995,"thema_id":61,"rolle":"neu","etappen":["begriffe"]},{"eintrag_id":996,"thema_id":61,"rolle":"neu","etappen":["gegenereignis"]},{"eintrag_id":997,"thema_id":61,"rolle":"neu","etappen":["laplace"]},{"eintrag_id":999,"thema_id":56,"rolle":"neu"},{"eintrag_id":1000,"thema_id":33,"rolle":"weitergefuehrt"},{"eintrag_id":1000,"thema_id":56,"rolle":"neu"},{"eintrag_id":1001,"thema_id":38,"rolle":"neu"},{"eintrag_id":1002,"thema_id":56,"rolle":"neu"},{"eintrag_id":1003,"thema_id":56,"rolle":"neu"},{"eintrag_id":1004,"thema_id":56,"rolle":"neu"},{"eintrag_id":1006,"thema_id":91,"rolle":"neu","etappen":["rotation","axialschnitt"]},{"eintrag_id":1006,"thema_id":92,"rolle":"neu"},{"eintrag_id":1007,"thema_id":92,"rolle":"neu"},{"eintrag_id":1008,"thema_id":52,"rolle":"weitergefuehrt"},{"eintrag_id":1008,"thema_id":92,"rolle":"neu"},{"eintrag_id":1009,"thema_id":51,"rolle":"weitergefuehrt"},{"eintrag_id":1009,"thema_id":53,"rolle":"weitergefuehrt"},{"eintrag_id":1009,"thema_id":92,"rolle":"neu"},{"eintrag_id":1010,"thema_id":92,"rolle":"neu"},{"eintrag_id":1012,"thema_id":37,"rolle":"neu"},{"eintrag_id":1013,"thema_id":37,"rolle":"neu"},{"eintrag_id":1015,"thema_id":62,"rolle":"neu"},{"eintrag_id":1016,"thema_id":62,"rolle":"neu"}]$json$::jsonb);
  raise notice 'LK-S Befüllen RS: % gesetzt, % unverändert, % ohne Zuordnung, unbekannte Etappen: %',
    r->'gesetzt', r->'gleich', jsonb_array_length(r->'ohne_zuordnung'), r->'unbekannte_etappen'; -- ohne Zuordnung: Vorschläge der Prüfung, die nicht (oder nicht so) in der Datenbank stehen (II/III ist nicht eingespielt)
end $$;

-- 4. Schnittstelle
-- Klassen eines Themas: Schulart → Zweig → [{klasse, rolle, rolle_lehrplan, etappen, lernbereiche, stunden}] (p_schulart/p_zweig: nur diese)
create or replace function schule.thema_klassen(p_thema bigint, p_schulart text default null, p_zweig text default null, p_kurz boolean default false)
 returns jsonb language sql stable set search_path to ''
as $function$
  select coalesce(jsonb_object_agg(s.schulart, s.j), '{}'::jsonb) from (
    select z.schulart, jsonb_object_agg(z.zweig, z.j) j from (
      select k.schulart, k.zweig, jsonb_agg(jsonb_strip_nulls(jsonb_build_object('klasse', k.klasse, 'rolle', k.rolle,
               'etappen', to_jsonb(k.etappen),
               'rolle_lehrplan', case when not p_kurz then to_jsonb(k.rolle_lehrplan) end,
               'lernbereiche', case when not p_kurz then k.lernbereiche end,
               'stunden', case when not p_kurz then (select sum((l->>'stunden')::numeric) from jsonb_array_elements(k.lernbereiche) l) end,
               'nur_klasse_fest', case when not p_kurz and k.nur_klasse_fest then true end)) order by k.klasse) j
        from schule.thema_lage_klasse k
       where k.thema_id = p_thema and (p_schulart is null or k.schulart = p_schulart) and (p_zweig is null or k.zweig = p_zweig)
       group by 1, 2) z group by 1) s;
$function$;

-- Abdeckung: Schulart → Zweig → Klasse → {stunden, stunden_abgedeckt, lernbereiche[]}
create or replace function schule.lehrplan_abdeckung_json()
 returns jsonb language sql stable set search_path to ''
as $function$
  select coalesce(jsonb_object_agg(a.schulart, a.j), '{}'::jsonb) from (
    select b.schulart, jsonb_object_agg(b.zweig, b.j) j from (
      select c.schulart, c.zweig, jsonb_object_agg(c.klasse::text, c.j) j from (
        select x.schulart, x.zweig, x.klasse, jsonb_build_object('stunden', sum(x.stunden), 'stunden_abgedeckt', sum(x.stunden_abgedeckt),
                 'lernbereiche', jsonb_agg(jsonb_build_object('eintrag_id', x.eintrag_id, 'pfad', x.pfad, 'titel', x.lernbereich, 'stunden', x.stunden,
                   'punkte', x.punkte, 'punkte_mit_thema', x.punkte_mit_thema, 'stunden_abgedeckt', x.stunden_abgedeckt) order by x.reihenfolge, x.eintrag_id)) j
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
         || jsonb_build_object('abdeckung', schule.lehrplan_abdeckung_json());
end $function$;

-- Thema-Detail ergänzen: klassen, baut_auf, weiter_in; mit Kind: klassen_kind mit Stand je Klasse
create or replace function schule.lehrplan_thema_lk(p_r jsonb, p_thema bigint, p_kind bigint, p_kindsicht boolean)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare v_sa text; v_zw text; v_kk jsonb; v_e bigint := schule.thema_einheit(p_thema); v_alle text[];
begin
  select array_agg(q->>'lernziel' order by o) into v_alle from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality x(q, o) where e.id = v_e;
  if p_kind is not null then
    select coalesce(l.schulart, 'gym_by'), schule.kind_zweig(coalesce(l.schulart, 'gym_by'), l.zweig) into v_sa, v_zw from schule.lernender l where l.id = p_kind;
    select coalesce(jsonb_agg(jsonb_strip_nulls(jsonb_build_object('klasse', k.klasse, 'rolle', k.rolle, 'etappen', to_jsonb(k.etappen),
             'etappen_verlangt', coalesce(cardinality(k.etappen), cardinality(v_alle)),
             'etappen_erledigt', (select count(*) from schule.karte_stand ks where ks.lernender_id = p_kind and ks.einheit_id = v_e
                                   and (ks.sitzt or ks.gesetzt_am is not null) and ks.lernziel = any(coalesce(k.etappen, v_alle))))) order by k.klasse), '[]'::jsonb)
      into v_kk from schule.thema_lage_klasse k where k.thema_id = p_thema and k.schulart = v_sa and k.zweig = v_zw;
  end if;
  if p_kindsicht then
    return p_r || jsonb_build_object('zweig', v_zw, 'klassen_kind', coalesce(v_kk, '[]'::jsonb),
      'baut_auf', (select coalesce(jsonb_agg(jsonb_build_object('thema_id', v.braucht_id, 'titel', tb.unterthema, 'art', v.art,
                     'klasse', (select g.klasse_ab from schule.thema_lage g where g.thema_id = v.braucht_id and g.lernziel is null and g.schulart = v_sa and g.zweig = v_zw)) order by v.braucht_id), '[]'::jsonb)
                     from schule.voraussetzung v join schule.thema tb on tb.id = v.braucht_id where v.thema_id = p_thema));
  end if;
  return p_r || jsonb_strip_nulls(jsonb_build_object(
    'klassen', schule.thema_klassen(p_thema),
    'etappen_titel', (select jsonb_object_agg(q->>'lernziel', q->>'titel') from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) q where e.id = v_e),
    -- Voraussetzungen mit ihrer ersten Klasse je Schulart/Zweig; verstoss: liegt später als dieses Thema
    'baut_auf', (select coalesce(jsonb_agg(jsonb_build_object('thema_id', v.braucht_id, 'titel', tb.unterthema, 'art', v.art,
                   'klassen', (select coalesce(jsonb_object_agg(g.schulart || '/' || g.zweig, g.klasse_ab), '{}'::jsonb) from schule.thema_lage g
                                where g.thema_id = v.braucht_id and g.lernziel is null),
                   'verstoss', (select coalesce(jsonb_agg(g.schulart || '/' || g.zweig order by g.schulart, g.zweig), '[]'::jsonb) from schule.thema_lage g
                                 join schule.thema_lage h on h.thema_id = p_thema and h.lernziel is null and h.schulart = g.schulart and h.zweig = g.zweig
                                where g.thema_id = v.braucht_id and g.lernziel is null and g.klasse_ab > h.klasse_ab)) order by v.braucht_id), '[]'::jsonb)
                   from schule.voraussetzung v join schule.thema tb on tb.id = v.braucht_id where v.thema_id = p_thema),
    -- spätere Klassen mit den Etappen, die dort dazukommen
    'weiter_in', (select coalesce(jsonb_object_agg(w.schulart || '/' || w.zweig, w.j), '{}'::jsonb) from (
                    select k.schulart, k.zweig, jsonb_agg(jsonb_strip_nulls(jsonb_build_object('klasse', k.klasse, 'etappen', to_jsonb(k.etappen))) order by k.klasse) j
                      from schule.thema_lage_klasse k where k.thema_id = p_thema and k.rolle = 'weitergefuehrt' group by 1, 2) w),
    'zweig', v_zw, 'klassen_kind', v_kk));
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
    return schule.lehrplan_matrix_lk(schule.lehrplan_matrix(v_kinder, false), null);   -- LK-S: Klassen je Thema, Abdeckung, Zweig
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
  schule.lehrplan_abdeckung_json(), schule.lehrplan_matrix_lk(jsonb, bigint), schule.lehrplan_thema_lk(jsonb, bigint, bigint, boolean) from public, anon, authenticated;
grant execute on function api.schule_lehrplan_matrix(text, jsonb), api.schule_lehrplan_thema(text, jsonb) to council_mcp;
revoke all on function api.schule_lehrplan_matrix(text, jsonb), api.schule_lehrplan_thema(text, jsonb) from public, anon, authenticated;

-- 5. Teilen eines Themas (Nachtrag „Route“, 22.11.): wiederholbares Verfahren, hier nur angelegt.
-- Plan (jsonb):
--   alt_thema           Thema, das geteilt wird
--   etappen             Lernziel-Schlüssel, die in den neuen Teil gehen (mindestens 3, Regel „ein Flug braucht 3 Etappen“)
--   neu                 {schluessel, unterthema, block, beschreibung, kurz, klasse_fest, lehrplan_reihenfolge, lernbereich, lehrplan, reihenfolge}
--   block_id, block_reihenfolge   Ort des neuen Flugs (Nachbarland), optional
--   neue_einheit_id     Einheit des neuen Teils (vorher mit schule.einheit_importieren angelegt, enthält die Etappen mit denselben Schlüsseln);
--                       ohne sie: nur Schritt 1 (Thema, Texte, Ort, Voraussetzung, Zuordnungen), Lernstand bleibt, Bericht sagt „einheit fehlt“
--   aufgaben_umhaengen  Aufgaben der Etappen in die neue Einheit (Vorgabe true; versuch und Sterne-Bezüge bleiben so gültig)
-- Ablauf: 1. Thema anlegen (über schluessel; vorhanden = wiederverwenden), Kann-Texte kopieren, Ort, Voraussetzung „neu braucht alt“ (hart),
--   Zuordnungen, deren etappen nur aus den Etappen des neuen Teils bestehen, auf das neue Thema. 2. (mit neue_einheit_id) Aufgaben, Karten, Lernziel-Stand,
--   besprochen, Was wackelt (je Etappe), Wiederholungs-Runden, Staffel-Sicherung, abgelegt, Rückmeldungen je Etappe umhängen; Sterne-Bezüge
--   'landung:<einheit>:<lernziel>' und 'wdh:<einheit>:<lernziel>:…' mitziehen (Menge unverändert, kein zweiter Bonus). 3. Vorher/Nachher je Kind:
--   gelandete/gesetzte Etappen beider Teile, Sterne, Flug-Abschlüsse, Plan – muss gleich bleiben, sonst Abbruch. neu_vollstaendig = alle Etappen des
--   neuen Teils erledigt (Nachtrag Stempel/Bonus nach Festlegung 14 macht ein eigener Schritt, nicht diese Funktion).
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

create or replace function schule.thema_teilen_ausfuehren(p_plan jsonb)
 returns jsonb language plpgsql set search_path to ''
as $function$
declare v_alt bigint := (p_plan->>'alt_thema')::bigint; v_et text[] := array(select jsonb_array_elements_text(p_plan->'etappen'));
  v_n jsonb := p_plan->'neu'; v_neu bigint; v_ae bigint; v_ne bigint := nullif(p_plan->>'neue_einheit_id', '')::bigint; v_b bigint := nullif(p_plan->>'block_id', '')::bigint;
  v_tab text; v_cnt int; v_um jsonb := '{}'::jsonb; v_vor jsonb; v_nach jsonb; v_kinder jsonb; v_zu int;
begin
  if v_alt is null or not exists (select 1 from schule.thema where id = v_alt) then raise exception 'alt_thema fehlt oder unbekannt' using errcode = 'P0001'; end if;
  if cardinality(v_et) < 3 then raise exception 'ein Flug braucht mindestens 3 Etappen (%)', cardinality(v_et) using errcode = 'P0001'; end if;
  if coalesce(v_n->>'schluessel', '') = '' or coalesce(v_n->>'unterthema', '') = '' then raise exception 'neu.schluessel und neu.unterthema fehlen' using errcode = 'P0001'; end if;
  v_ae := coalesce(nullif(p_plan->>'alte_einheit_id', '')::bigint, schule.thema_einheit(v_alt));
  if v_ae is null then raise exception 'alte Einheit nicht gefunden' using errcode = 'P0001'; end if;
  if exists (select 1 from unnest(v_et) s where not exists (select 1 from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) q
                                                             where e.id = v_ae and q->>'lernziel' = s)) then
    raise exception 'nicht jede Etappe steht in der alten Einheit %', v_ae using errcode = 'P0001'; end if;

  -- Vorher je Kind (alle Kinder mit Stand in einer der beiden Einheiten)
  v_vor := schule.thema_teilen_stand(v_ae, v_ne, v_et);

  -- 1. Thema, Texte, Ort, Voraussetzung, Zuordnungen
  select id into v_neu from schule.thema where schluessel = v_n->>'schluessel';
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
  update schule.zuordnung z set thema_id = v_neu
   where z.thema_id = v_alt and z.etappen is not null and z.etappen <@ v_et
     and not exists (select 1 from schule.zuordnung y where y.eintrag_id = z.eintrag_id and y.thema_id = v_neu);
  get diagnostics v_zu = row_count;

  -- 2. Lernstand umhängen (nur mit der neuen Einheit)
  if v_ne is not null then
    if not exists (select 1 from schule.einheit e where e.id = v_ne and e.thema_id = v_neu) then raise exception 'neue Einheit % gehört nicht zum neuen Thema %', v_ne, v_neu using errcode = 'P0001'; end if;
    if exists (select 1 from unnest(v_et) s where not exists (select 1 from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) q
                                                               where e.id = v_ne and q->>'lernziel' = s)) then
      raise exception 'nicht jede Etappe steht in der neuen Einheit %', v_ne using errcode = 'P0001'; end if;
    if exists (select 1 from schule.karte_stand k where k.einheit_id = v_ne and k.lernziel = any(v_et)
                 and exists (select 1 from schule.karte_stand a where a.lernender_id = k.lernender_id and a.einheit_id = v_ae and a.lernziel = k.lernziel)) then
      raise exception 'Kind hat schon Stand in beiden Einheiten – bitte prüfen' using errcode = 'P0001'; end if;
    if coalesce((p_plan->>'aufgaben_umhaengen')::boolean, true) then
      update schule.aufgabe set einheit_id = v_ne, thema_id = v_neu where einheit_id = v_ae and variante_gruppe = any(v_et);
      get diagnostics v_cnt = row_count; v_um := v_um || jsonb_build_object('aufgabe', v_cnt);
    end if;
    foreach v_tab in array array['karte_stand', 'lernziel_stand', 'besprochen', 'wdh_runde_etappe', 'wdh_staffel_sicherung', 'rueckmeldung'] loop
      if to_regclass('schule.' || v_tab) is not null then
        execute format('update schule.%I set einheit_id = $1 where einheit_id = $2 and lernziel = any($3)', v_tab) using v_ne, v_ae, v_et;
        get diagnostics v_cnt = row_count; v_um := v_um || jsonb_build_object(v_tab, v_cnt);
      end if;
    end loop;
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

  -- 3. Nachher und Prüfung je Kind
  v_nach := schule.thema_teilen_stand(v_ae, v_ne, v_et);
  if v_vor <> v_nach then
    raise exception 'Vorher/Nachher je Kind verschieden: vorher %, nachher %', v_vor, v_nach using errcode = 'P0001'; end if;
  select coalesce(jsonb_agg(jsonb_build_object('kind', l.lernender_id,
           'neu_vollstaendig', v_ne is not null and (select count(*) from schule.karte_stand k where k.lernender_id = l.lernender_id and k.einheit_id = v_ne
                                                      and k.lernziel = any(v_et) and (k.sitzt or k.gesetzt_am is not null)) = cardinality(v_et),
           'etappen_neu_erledigt', (select count(*) from schule.karte_stand k where k.lernender_id = l.lernender_id and k.einheit_id = coalesce(v_ne, v_ae)
                                     and k.lernziel = any(v_et) and (k.sitzt or k.gesetzt_am is not null))) order by l.lernender_id), '[]'::jsonb)
    into v_kinder from (select distinct lernender_id from schule.karte_stand where einheit_id in (v_ae, coalesce(v_ne, v_ae))) l;
  return jsonb_build_object('ok', true, 'alt_thema', v_alt, 'neu_thema', v_neu, 'alte_einheit', v_ae, 'neue_einheit', v_ne,
    'einheit_fehlt', v_ne is null, 'zuordnungen', v_zu, 'umgehaengt', v_um, 'je_kind', v_vor, 'kinder', v_kinder);
end $function$;

-- Stand je Kind für das Teilen: Summe über beide Einheiten (ändert sich durch das Umhängen nicht)
create or replace function schule.thema_teilen_stand(p_ae bigint, p_ne bigint, p_et text[])
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare v jsonb;
begin
  select coalesce(jsonb_object_agg(l.id, jsonb_build_object(
      'gelandet', (select count(*) from schule.karte_stand k where k.lernender_id = l.id and k.einheit_id in (p_ae, coalesce(p_ne, p_ae)) and k.sitzt),
      'gesetzt', (select count(*) from schule.karte_stand k where k.lernender_id = l.id and k.einheit_id in (p_ae, coalesce(p_ne, p_ae)) and k.gesetzt_am is not null),
      'karten', (select count(*) from schule.karte_stand k where k.lernender_id = l.id and k.einheit_id in (p_ae, coalesce(p_ne, p_ae))),
      'sterne', (select coalesce(sum(s.menge), 0) from schule.sterne s where s.lernender_id = l.id),
      'plan', (select md5(coalesce(string_agg(r::text, '|' order by r::text), '')) from schule.route r where r.lernender_id = l.id))
      || jsonb_build_object('flug_abschluesse', (select count(*) from schule.flug_erstabschluss f where f.lernender_id = l.id))), '{}'::jsonb)
    into v from schule.lernender l
   where exists (select 1 from schule.karte_stand k where k.lernender_id = l.id and k.einheit_id in (p_ae, coalesce(p_ne, p_ae)));
  return v;
end $function$;
revoke all on function schule.thema_teilen(jsonb, boolean), schule.thema_teilen_ausfuehren(jsonb), schule.thema_teilen_stand(bigint, bigint, text[])
  from public, anon, authenticated;

-- Bestand unverändert?
do $mig$
declare v_t text;
begin
  select string_agg(v.t, ', ') into v_t from lk_vorher v join pg_temp.lk_stand() n on n.t = v.t where n.s <> v.s;
  if v_t is not null then raise exception 'LK-S: Bestand verändert (%)', v_t; end if;
  raise notice 'LK-S: Stufen/Plan aller Kinder, Reiseoptionen, Klassen, Lernstand, Sterne, Flug-Abschlüsse, Visum-Regeln, Themen, Voraussetzungen unverändert';
end $mig$;
