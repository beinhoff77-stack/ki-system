-- RD-S 2 / Befund 23.11.: Expeditionen nach der Teilung – Voraussetzungen und Teile über die Familie des Themas (teil_stamm).
-- 1) Hilfsfunktionen: Familie eines Themas (Stamm), Thema der Familie, das ein Lernziel enthält.
-- 2) expedition_voraussetzungen_ok und expedition_etappe suchen die Karte in der Familie des genannten Themas – eine künftige Teilung bricht das nicht mehr.
-- 3) Korrektur der Daten: Voraussetzungen und Expeditions-Teile, deren Lernziel nicht (mehr) im genannten Thema liegt, zeigen auf den Teil, der es enthält
--    (heute: „8-schulfest“, laplace/grosse_zahlen → Teil 2 von „Zufall und Laplace“). Keine festen IDs.
-- Läuft vor 20261125_ex_s_expedition.sql (EX-S nutzt schule.thema_familie). Wiederholbar; kein DROP, kein DELETE. Kein Kind betroffen (keine Antworten auf Expeditionen).

create or replace function schule.thema_familie(p_thema bigint)
 returns bigint language sql stable set search_path to ''
as $$ select coalesce((select coalesce(t.teil_stamm, t.id) from schule.thema t where t.id = p_thema), p_thema) $$;
revoke all on function schule.thema_familie(bigint) from public, anon, authenticated;

-- Thema der Familie, dessen aktuelle Einheit das Lernziel als Etappe hat (das genannte Thema zuerst, dann nach Teil)
create or replace function schule.lernziel_thema(p_thema bigint, p_lz text)
 returns bigint language sql stable set search_path to ''
as $$
  select t.id from schule.thema t join schule.einheit e on e.id = schule.thema_einheit(t.id)
   where coalesce(t.teil_stamm, t.id) = schule.thema_familie(p_thema)
     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]')) x where x->>'lernziel' = p_lz)
   order by t.id <> p_thema, coalesce(t.teil_nr, 1), t.id limit 1;
$$;
revoke all on function schule.lernziel_thema(bigint, text) from public, anon, authenticated;

-- Voraussetzungen erfüllt: jede Voraussetzung (Thema + Lernziel) sitzt als Karte irgendwo in der Familie des Themas
create or replace function schule.expedition_voraussetzungen_ok(p_lernender bigint, x schule.expedition)
 returns boolean language sql stable set search_path to ''
as $$
  select jsonb_array_length(x.voraussetzungen) > 0 and not exists (
    select 1 from jsonb_array_elements(x.voraussetzungen) v
     where not exists (select 1 from schule.karte_stand k join schule.einheit e on e.id = k.einheit_id join schule.thema t on t.id = e.thema_id
                        where k.lernender_id = p_lernender and k.sitzt and k.lernziel = v->>'lernziel'
                          and coalesce(t.teil_stamm, t.id) = schule.thema_familie((v->>'thema_id')::bigint)));   -- RD-S 2: Familie statt Thema
$$;

-- Etappe eines Expeditions-Teils: Karte des Kindes in der Familie des Themas (sonst die Einheit der Aufgabe)
create or replace function schule.expedition_etappe(p_l bigint, a schule.aufgabe)
 returns bigint language sql stable set search_path to ''
as $$
  select coalesce((select k.einheit_id from schule.karte_stand k join schule.einheit e on e.id = k.einheit_id join schule.thema t on t.id = e.thema_id
                    where k.lernender_id = p_l and coalesce(t.teil_stamm, t.id) = schule.thema_familie(a.thema_id) and k.lernziel = a.variante_gruppe   -- RD-S 2: Familie
                    order by k.sitzt desc, k.sitzt_am desc nulls last, e.version desc limit 1), a.einheit_id);
$$;

-- Datenkorrektur: Voraussetzungen
do $$
declare v_x record; v_neu jsonb; v_n int := 0;
begin
  for v_x in select x.id, x.voraussetzungen from schule.expedition x loop
    select jsonb_agg(case when z.t is not null and z.t <> (v->>'thema_id')::bigint
                          then v || jsonb_build_object('thema_id', z.t, 'thema_schluessel', (select t.schluessel from schule.thema t where t.id = z.t))
                          else v end order by o)
      into v_neu
      from jsonb_array_elements(v_x.voraussetzungen) with ordinality q(v, o)
      cross join lateral (select schule.lernziel_thema((v->>'thema_id')::bigint, v->>'lernziel') t) z;
    if v_neu is distinct from v_x.voraussetzungen and v_neu is not null then
      update schule.expedition set voraussetzungen = v_neu, geaendert_am = now() where id = v_x.id;
      v_n := v_n + 1;
    end if;
  end loop;
  raise notice 'RD-S 2: % Expeditionen mit umgestellten Voraussetzungen', v_n;
end $$;

-- Datenkorrektur: Expeditions-Teile (Thema und Einheit der Aufgabe) auf den Teil, der das Lernziel enthält
do $$
declare v_n int;
begin
  update schule.aufgabe a set thema_id = z.t, einheit_id = schule.thema_einheit(z.t)
    from (select a2.id, schule.lernziel_thema(a2.thema_id, a2.variante_gruppe) t from schule.aufgabe a2
           where a2.pool = 'expedition' and a2.variante_gruppe is not null) z
   where a.id = z.id and z.t is not null and z.t <> a.thema_id;
  get diagnostics v_n = row_count;
  raise notice 'RD-S 2: % Expeditions-Teile auf den Teil des Lernziels umgestellt', v_n;
end $$;
