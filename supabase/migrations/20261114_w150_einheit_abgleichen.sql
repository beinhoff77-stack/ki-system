-- W150 (Claude): Bestehende Einheit mit ihrer Themen-Datei abgleichen (Korrekturen aus Prüfungen, Toleranz, neue Aufgaben).
-- Erklärungen (inhalt) werden ersetzt; Aufgaben werden über Frage + Antworten wiedererkannt:
--   vorhanden -> Lösung, Tipp, Lösungsweg, Stufe aktualisieren; neu -> einfügen; in der Datei nicht mehr vorhanden -> nur zählen
--   (p_fehlende = 'sperren': zusätzlich freigegeben = false, also nur noch fürs Testkind sichtbar;
--    p_fehlende = 'loeschen': entfernen – nur erlaubt, solange die Einheit Entwurf ist, und nur Aufgaben, die noch nie jemand bearbeitet hat).
-- Status der Einheit und Lernstände bleiben unverändert.
create or replace function schule.einheit_abgleichen(p jsonb, p_fehlende text default 'lassen') returns jsonb
language plpgsql security definer set search_path to '' as $$
declare v_t bigint := (p->>'thema_id')::bigint; v_e bigint; v_status text; v_neu int; v_geaendert int; v_fehlend int; v_weg int := 0; v_auf jsonb; v_max int;
begin
  if p_fehlende not in ('lassen', 'sperren', 'loeschen') then raise exception 'p_fehlende: lassen, sperren oder loeschen'; end if;
  select e.id, e.status into v_e, v_status from schule.einheit e join schule.thema t on t.id = e.thema_id
   where e.thema_id = v_t and t.schluessel = p->>'thema_schluessel' and e.status <> 'ersetzt' order by e.version desc limit 1;
  if v_e is null then raise exception 'Keine Einheit für Thema %', p->>'thema_schluessel'; end if;
  if jsonb_array_length(coalesce(p->'inhalt'->'etappen', '[]'::jsonb)) < 3 then raise exception 'Datei unvollständig'; end if;
  update schule.einheit e set inhalt = (e.inhalt - 'etappen' - 'abschnitte' - 'merke' - 'ziel' - 'teilfaehigkeiten') || ((p->'inhalt') - 'quellen' - 'bewertung')
    || jsonb_build_object('bewertung', coalesce(e.inhalt->'bewertung', '{}'::jsonb) || coalesce(p->'inhalt'->'bewertung', '{}'::jsonb))
   where e.id = v_e;
  with q as (select a from jsonb_array_elements(p->'aufgaben') a)
  update schule.aufgabe b set loesung = q.a->'o', tipp = q.a->>'h', loesungsweg = q.a->>'w', stufe = (q.a->>'s')::smallint,
         variante_gruppe = q.a->>'l', teilfaehigkeit = q.a->>'t'
    from q where b.einheit_id = v_e and b.frage = q.a->'f' and b.antworten is not distinct from (case when q.a ? 'a' then q.a->'a' end) and b.pool = q.a->>'p'
     and (b.loesung, b.tipp, b.loesungsweg, b.stufe, b.variante_gruppe) is distinct from (q.a->'o', q.a->>'h', q.a->>'w', (q.a->>'s')::smallint, q.a->>'l');
  get diagnostics v_geaendert = row_count;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg((x.a - 'c' - 'zahl') || jsonb_build_object('r', v_max + x.nr)) into v_auf from (
    select a, row_number() over (order by ord) nr from jsonb_array_elements(p->'aufgaben') with ordinality q(a, ord)
     where not exists (select 1 from schule.aufgabe b where b.einheit_id = v_e and b.frage = a->'f' and b.antworten is not distinct from (case when a ? 'a' then a->'a' end))) x;
  v_neu := case when v_auf is null then 0 else schule.aufgaben_einfuegen(v_e, v_auf) end;
  select count(*) into v_fehlend from schule.aufgabe b where b.einheit_id = v_e
     and not exists (select 1 from jsonb_array_elements(p->'aufgaben') a where b.frage = a->'f' and b.antworten is not distinct from (case when a ? 'a' then a->'a' end));
  if p_fehlende = 'sperren' and v_fehlend > 0 then
    update schule.aufgabe b set freigegeben = false where b.einheit_id = v_e
       and not exists (select 1 from jsonb_array_elements(p->'aufgaben') a where b.frage = a->'f' and b.antworten is not distinct from (case when a ? 'a' then a->'a' end));
  elsif p_fehlende = 'loeschen' and v_fehlend > 0 then
    if v_status <> 'entwurf' then raise exception 'Löschen nur bei Entwürfen (Einheit % ist %)', v_e, v_status; end if;
    delete from schule.aufgabe b where b.einheit_id = v_e
       and not exists (select 1 from jsonb_array_elements(p->'aufgaben') a where b.frage = a->'f' and b.antworten is not distinct from (case when a ? 'a' then a->'a' end))
       and not exists (select 1 from schule.versuch v where v.aufgabe_id = b.id);
    get diagnostics v_weg = row_count;
  end if;
  return jsonb_build_object('einheit_id', v_e, 'thema', p->>'thema_schluessel', 'aufgaben_geaendert', v_geaendert, 'aufgaben_neu', v_neu, 'nicht_mehr_in_datei', v_fehlend, 'entfernt', v_weg);
end $$;
revoke all on function schule.einheit_abgleichen(jsonb, text) from public, anon, authenticated;
