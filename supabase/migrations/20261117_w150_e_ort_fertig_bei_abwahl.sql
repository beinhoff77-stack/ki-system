-- Schritt E / P3 (Nachprüfung Phase 2): Ort wird „fertig“, wenn der letzte offene Flug abgewählt wird.
-- Bisher setzt nur der Abschluss eines Tests (schule.test_abschliessen_intern) einen Ort auf „fertig“. Wählt man im Flugplan den letzten offenen Flug ab,
-- meldet schule.ort_stand „abgeschlossen“ (Stempel zählt), der Ort bleibt aber „offen“/„dran“ und die Sterne für den Ort fehlen.
-- Lösung in api.schule_plan_setzen (gezieltes Ersetzen im Live-Text, Stellen vorab geprüft):
--   1. Nach dem Speichern wird jeder Ort des Plans „fertig“, dessen ort_stand „abgeschlossen“ meldet. Der Trigger route_sterne bucht die Sterne einmal
--      (Eindeutigkeit lernender/grund/bezug – kein doppeltes Buchen).
--   2. Umgekehrt: War ein Ort „fertig“ und kommt beim Speichern ein abgewählter Flug zurück in den Plan, der noch nicht erledigt ist, wird der Ort wieder „offen“.
--      Bereits gebuchte Sterne bleiben; beim erneuten „fertig“ werden sie nicht noch einmal gebucht.
-- 3. Einmalig: Orte, die heute schon in diesem Zustand hängen (abgeschlossen, aber nicht „fertig“), werden „fertig“ (nur UPDATE).
-- Kein DROP, kein DELETE.

do $$
declare d text;
begin
  d := pg_get_functiondef('api.schule_plan_setzen(text, jsonb)'::regprocedure);
  if position('v_b bigint; v_r schule.route; v_ids bigint[] := ''{}''; v_n int; v_aus bigint[];' in d) = 0
     or position('      update schule.route set position = v_pos,' in d) = 0
     or position('  insert into schule.route_aenderung(lernender_id, route_id, akteur, anlass, ereignis)' in d) = 0 then
    raise exception 'Stellen in schule_plan_setzen nicht gefunden';
  end if;
  d := replace(d, 'v_b bigint; v_r schule.route; v_ids bigint[] := ''{}''; v_n int; v_aus bigint[];',
                  'v_b bigint; v_r schule.route; v_ids bigint[] := ''{}''; v_n int; v_aus bigint[]; v_wieder bigint[] := ''{}''; v_fertig int; v_offen int;');
  d := replace(d, '      update schule.route set position = v_pos,',
    $r$      -- P3: kommt in einen „fertigen“ Ort ein abgewählter Flug zurück, prüfen wir den Ort nach dem Speichern
      if v_r.status = 'fertig' and v_aus is not null and exists (select 1 from unnest(v_r.ausgelassen) a where not (a = any(v_aus))) then
        v_wieder := v_wieder || v_b;
      end if;
      update schule.route set position = v_pos,$r$);
  d := replace(d, '  insert into schule.route_aenderung(lernender_id, route_id, akteur, anlass, ereignis)',
    $r$  -- P3: Orte, deren geplante Flüge alle erledigt sind (z. B. der letzte offene Flug wurde abgewählt), werden „fertig“ – route_sterne bucht die Sterne einmal
  update schule.route r set status = 'fertig', revision = v_rev + 1, geaendert_von = v_akt, geaendert_am = now()
   where r.lernender_id = v_l and r.art = 'normal' and r.status not in ('fertig', 'entfernt') and r.block_id = any(v_ids)
     and (schule.ort_stand(v_l, r.block_id)->>'abgeschlossen')::boolean;
  get diagnostics v_fertig = row_count;
  -- P3 umgekehrt: ein nicht erledigter Flug ist zurück im Plan → Ort wieder offen (gebuchte Sterne bleiben, werden später nicht doppelt gebucht)
  update schule.route r set status = 'offen', revision = v_rev + 1, geaendert_von = v_akt, geaendert_am = now()
   where r.lernender_id = v_l and r.art = 'normal' and r.status = 'fertig' and r.block_id = any(v_wieder)
     and not coalesce((schule.ort_stand(v_l, r.block_id)->>'abgeschlossen')::boolean, false);
  get diagnostics v_offen = row_count;
  insert into schule.route_aenderung(lernender_id, route_id, akteur, anlass, ereignis)$r$);
  d := replace(d, $r$jsonb_build_object('reihenfolge', to_jsonb(v_ids), 'entfernt', v_n, 'revision', v_rev + 1)$r$,
                  $r$jsonb_build_object('reihenfolge', to_jsonb(v_ids), 'entfernt', v_n, 'revision', v_rev + 1, 'fertig_durch_abwahl', v_fertig, 'wieder_offen', v_offen)$r$);
  execute d;
end $$;

-- 3. Einmalig: hängende Orte nachziehen (abgeschlossen laut ort_stand, aber noch nicht „fertig“). Die Sterne bucht route_sterne.
update schule.route r set status = 'fertig', geaendert_von = 'system', geaendert_am = now(), revision = r.revision + 1
 where r.art = 'normal' and r.status not in ('fertig', 'entfernt') and cardinality(r.ausgelassen) > 0
   and (schule.ort_stand(r.lernender_id, r.block_id)->>'abgeschlossen')::boolean;
