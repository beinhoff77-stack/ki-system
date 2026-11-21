-- AB-S Nachtrag „flug_geschafft robust“ (Nachträge aus ChatGPT 888, Muss 1; Postfach antworten.md 21.11. 04:25).
-- Baut die schon eingespielte schule.test_abschliessen_intern um (Stand nach 20261120_ab_s_flug_abschluss_einmal.sql, md5 der Datei f79c1701…):
-- Eine frühere abgeschlossene Flug-Test-/Verbessern-Sitzung mit flug_geschafft NULL (vor dem Einspielen) zählt nur noch als früherer Abschluss, wenn der Flug
-- nach ihr fertig war (schule.flug_fertig_nach). Alte Bedingung: x.flug_geschafft is distinct from false → neu: x.flug_geschafft or (null und fertig danach).
-- Alles andere bleibt (dieser Aufruf schließt ab, nur blocktest/korrektur, Flug vorher nicht fertig, Wert einmal festgehalten).
-- Wiederholt ausführbar (Funktion create or replace; Umbau nur, wenn die alte Stelle noch da ist). Kein DROP, kein DELETE, keine Bestandsänderung.
-- Bestand (lesend, 21.11.): kein betroffener Fall (alle alten Sitzungen gehören zu fertigen Flügen). Nicht ausgeführt – der Haupt-Chat spielt ein.

-- War der Flug nach Sitzung p_sitzung fertig? Je Pflicht-Etappe zählt das letzte Ergebnis in einem abgeschlossenen Flug-Test, Verbessern oder Nachtest
-- bis einschließlich dieser Sitzung (alle Antworten der Etappe richtig). Eine Pflicht-Etappe ohne Ergebnis bis dahin → nicht fertig.
create or replace function schule.flug_fertig_nach(p_l bigint, p_e bigint, p_sitzung bigint)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from schule.lernziel_stand s where s.lernender_id = p_l and s.einheit_id = p_e and s.pflicht)
     and not exists (
       select 1 from schule.lernziel_stand s
        where s.lernender_id = p_l and s.einheit_id = p_e and s.pflicht
          and not coalesce((
            select bool_and(v.richtig) from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
             where a.variante_gruppe = s.lernziel
               and v.testsitzung_id = (select max(x.id) from schule.testsitzung x
                                        where x.lernender_id = p_l and x.einheit_id = p_e and x.art in ('blocktest', 'korrektur', 'nachtest')
                                          and x.status = 'abgeschlossen' and x.id <= p_sitzung
                                          and exists (select 1 from schule.versuch v2 join schule.aufgabe a2 on a2.id = v2.aufgabe_id
                                                       where v2.testsitzung_id = x.id and a2.variante_gruppe = s.lernziel))), false));
$function$;
comment on function schule.flug_fertig_nach(bigint, bigint, bigint) is 'AB-S Nachtrag (ChatGPT 888): Flug nach dieser Testsitzung fertig? – für alte Sitzungen ohne flug_geschafft';

do $mig$
declare d text; v_alt text; v_neu text;
begin
  d := pg_get_functiondef('schule.test_abschliessen_intern(bigint, jsonb)'::regprocedure);
  if position('flug_fertig_nach' in d) > 0 then return; end if; -- schon umgebaut
  v_alt := $a$and x.status = 'abgeschlossen' and x.id < t.id and x.flug_geschafft is distinct from false);$a$;
  v_neu := $a$and x.status = 'abgeschlossen' and x.id < t.id
                       and (x.flug_geschafft or (x.flug_geschafft is null and schule.flug_fertig_nach(p_lernender, t.einheit_id, x.id)))); -- robust (ChatGPT 888)$a$;
  if (length(d) - length(replace(d, v_alt, ''))) / length(v_alt) <> 1 then
    raise exception 'test_abschliessen_intern: Stelle nicht genau einmal gefunden (ist 20261120_ab_s_flug_abschluss_einmal.sql eingespielt?)'; end if;
  execute replace(d, v_alt, v_neu);
end $mig$;
