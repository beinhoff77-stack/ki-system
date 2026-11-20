-- W177 · Fehler aus dem Betrieb (18.11.): Abflugtafel zeigt „TEST BEREIT“, die Testseite bietet aber keinen Test an.
-- Ursache: Der Flugtest (blocktest) ist schon abgeschlossen; danach kamen neue Pflicht-Etappen in den Flug. Diese stehen in lernziel_stand auf 'offen'.
-- Blocktest gesperrt (schon abgeschlossen), Korrektur nur für 'fehler', Nachtest nur ohne 'offen' → Sackgasse.
-- Regel jetzt: art = 'blocktest' nach abgeschlossenem Flugtest startet einen NACHTRAGSTEST mit je einer Bordkarte für jede offene Pflicht-Etappe
-- (zuerst aus dem Pool 'test', sonst 'korrektur'; nur freigegebene, vom Kind noch nie gesehene). Gibt es keine offene Pflicht-Etappe, bleibt die alte Meldung.
-- Bewertung über den bestehenden Abschluss (test_abschliessen_intern): richtig → 'nachgewiesen', falsch → 'fehler' (dann wie gewohnt „Verbessern“).
-- Kein DROP, kein DELETE, keine Daten geändert. Wiederholt ausführbar.
do $mig$
declare d text;
  v_alt text := $a$      if exists (select 1 from schule.testsitzung where lernender_id = p_lernender and einheit_id = v_einheit and art = 'blocktest' and status = 'abgeschlossen') then
        raise exception 'Der Blocktest ist schon abgeschlossen. Weiter mit Korrektur oder Nachtest.' using errcode = 'P0001';
      end if;
      select coalesce(array_agg(a.id order by a.reihenfolge), '{}') into v_ids from schule.aufgabe a where a.einheit_id = v_einheit and a.pool = 'test';$a$;
  v_neu text := $a$      if exists (select 1 from schule.testsitzung where lernender_id = p_lernender and einheit_id = v_einheit and art = 'blocktest' and status = 'abgeschlossen') then
        -- W177 Nachtragstest: nach dem Flugtest neu hinzugekommene Pflicht-Etappen (Status 'offen') nachträglich testen
        if not exists (select 1 from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = v_einheit and s.pflicht and s.status = 'offen') then
          raise exception 'Der Blocktest ist schon abgeschlossen. Weiter mit Korrektur oder Nachtest.' using errcode = 'P0001';
        end if;
        for r in select s.lernziel from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = v_einheit and s.pflicht and s.status = 'offen' order by s.lernziel loop
          select a.id into v_aid from schule.aufgabe a
            where a.einheit_id = v_einheit and a.variante_gruppe = r.lernziel and a.pool in ('test', 'korrektur') and a.freigegeben
              and not exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id)
              and not exists (select 1 from schule.testsitzung x where x.lernender_id = p_lernender and a.id = any(x.aufgaben))
            order by (a.pool = 'test') desc, a.reihenfolge limit 1;
          if v_aid is null then v_leer := v_leer || r.lernziel; else v_ids := v_ids || v_aid; end if;
          v_aid := null;
        end loop;
        if cardinality(v_leer) > 0 then
          return jsonb_build_object('ok', false, 'grund', 'vorrat_erschoepft', 'vorrat_erschoepft', to_jsonb(v_leer), 'noch_nicht_faellig', '[]'::jsonb);
        end if;
      else
        select coalesce(array_agg(a.id order by a.reihenfolge), '{}') into v_ids from schule.aufgabe a where a.einheit_id = v_einheit and a.pool = 'test';
      end if;$a$;
begin
  d := pg_get_functiondef('schule.test_starten_intern(bigint, jsonb)'::regprocedure);
  if position('W177 Nachtragstest' in d) > 0 then return; end if; -- schon eingespielt
  if position(v_alt in d) = 0 then raise exception 'Stelle in test_starten_intern nicht gefunden'; end if;
  execute replace(d, v_alt, v_neu);
end $mig$;
