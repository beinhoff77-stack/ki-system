-- Nacharbeit aus ChatGPTs Prüfergebnis 907 (AUFTRAEGE.md, 22.11.), Teil bau-lehrer. Neue Datei; die eingespielten Dateien
-- 20261121_ab_s_flug_geschafft_robust.sql und 20261121_lm_s_lehrplan_matrix.sql bleiben unverändert.
--
-- 1. „Flug geschafft“ (flug_erstabschluss) – bekannte Grenze, beim Einspielen ausgeschlossen:
--    Altzustand „Flug war früher fertig (Sitzung mit flug_geschafft NULL oder durch erneutes Lesen false), danach kam eine neue Pflicht-Etappe dazu,
--    und ERST DANN lief der Nachtrag“: Der Nachtrag findet den Flug dann weder fertig noch mit einer Sitzung flug_geschafft = true; der spätere
--    Nachtragstest legt die Zeile an und meldet flug_geschafft = true (ein zweites „Flug geschafft“). Festgelegtes Ergebnis: true.
--    Der Haupt-Chat hat beim Einspielen geprüft, dass es diesen Altzustand im Bestand nicht gibt (4 von 4 Flügen mit Test fertig, Pflichtlisten vollständig).
--    Neue Fälle entstehen nicht mehr, weil jeder fertige Flug-Test/jedes Verbessern die Zeile sofort anlegt.
--    Gewollt: Erneutes Lesen derselben erfolgreichen Sitzung zeigt wieder flug_geschafft = true (derselbe Wert wie beim Abschließen, „Test ansehen“).
--    Rauchtest: supabase/tests/ab_s_nacharbeit_907_rauchtest.sql.
-- 2. Nachtrag: sitzung_id und am kommen jetzt aus derselben – zeitlich ersten – abgeschlossenen Sitzung mit flug_geschafft = true
--    (bisher min(id) und min(abgeschlossen_am) getrennt). Gleiches Ergebnis wie vorher, wenn ids und Zeiten gleich sortiert sind.
-- 3. LM-S: etappe_jetzt = Nummer der ersten noch nicht gelandeten Etappe in Etappen-Reihenfolge (bisher „gelandet + 1“); null, wenn alle gelandet sind.
--    Neue Hilfsfunktion schule.etappe_jetzt(lernender, einheit).
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE, keine Bestandsänderung. Wiederholt ausführbar.

-- 2. Nachtrag: sitzung_id und am aus derselben Zeile
create or replace function schule.flug_erstabschluss_nachtragen(p_l bigint default null)
 returns integer language plpgsql set search_path to ''
as $function$
declare v_n integer;
begin
  insert into schule.flug_erstabschluss (lernender_id, einheit_id, sitzung_id, am)
  select f.lernender_id, f.einheit_id, x.id, coalesce(x.abgeschlossen_am, now())
    from (select s.lernender_id, s.einheit_id from schule.lernziel_stand s
           where (p_l is null or s.lernender_id = p_l)
           group by s.lernender_id, s.einheit_id
          having bool_or(s.pflicht) and bool_and(not s.pflicht or s.status in ('nachgewiesen', 'korrigiert', 'gesichert'))
          union
          select ts.lernender_id, ts.einheit_id from schule.testsitzung ts
           where (p_l is null or ts.lernender_id = p_l) and ts.einheit_id is not null
             and ts.art in ('blocktest', 'korrektur') and ts.status = 'abgeschlossen' and ts.flug_geschafft) f
    left join lateral (select t.id, t.abgeschlossen_am from schule.testsitzung t
                        where t.lernender_id = f.lernender_id and t.einheit_id = f.einheit_id
                          and t.art in ('blocktest', 'korrektur') and t.status = 'abgeschlossen' and t.flug_geschafft
                        order by t.abgeschlossen_am nulls last, t.id limit 1) x on true    -- Nacharbeit 907: eine Zeile, die zeitlich erste
  on conflict (lernender_id, einheit_id) do nothing;
  get diagnostics v_n = row_count;
  return v_n;
end $function$;
revoke all on function schule.flug_erstabschluss_nachtragen(bigint) from public, anon, authenticated;

-- 3. LM-S: erste noch nicht gelandete Etappe (1, 2, …) in Etappen-Reihenfolge
create or replace function schule.etappe_jetzt(p_l bigint, p_e bigint)
 returns integer language sql stable set search_path to ''
as $function$
  select min(et.nr)::int from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality et(x, nr)
   where e.id = p_e
     and not exists (select 1 from schule.karte_stand k where k.lernender_id = p_l and k.einheit_id = e.id and k.lernziel = et.x->>'lernziel' and k.sitzt);
$function$;

do $mig$
declare d text := pg_get_functiondef('schule.lehrplan_matrix(bigint[], boolean)'::regprocedure);
  v_alt text := $a$|| jsonb_build_object('etappe_jetzt', case when s.st->>'stufe' = 'dran' then least(coalesce((s.st->>'gelandet')::int, 0) + 1, greatest(coalesce((s.st->>'etappen')::int, 1), 1)) end)$a$;
  v_neu text := $a$|| jsonb_build_object('etappe_jetzt', case when s.st->>'stufe' = 'dran' then schule.etappe_jetzt(l.id, schule.thema_einheit(t.id)) end) -- Nacharbeit 907$a$;
begin
  if position('schule.etappe_jetzt(' in d) > 0 then return; end if; -- schon eingespielt
  if (length(d) - length(replace(d, v_alt, ''))) / length(v_alt) <> 1 then
    raise exception 'lehrplan_matrix: Stelle etappe_jetzt nicht genau einmal gefunden'; end if;
  execute replace(d, v_alt, v_neu);
end $mig$;
