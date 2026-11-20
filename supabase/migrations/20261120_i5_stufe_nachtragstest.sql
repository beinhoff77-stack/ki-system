-- Befund 20.11. 06:00 (Haupt-Chat): schule.thema_stufe übersieht den offenen Nachtragstest.
-- Fall: Flug-Test (blocktest) bestanden, danach neue Pflicht-Etappen, inzwischen gelandet, Nachtragstest (W177) noch nicht geschrieben
-- (lernziel_stand dieser Etappen 'offen'). Bisher: ↻ wiederholung, test_offen false. Jetzt: ▶ dran, test_offen true.
-- Regel: „alle Etappen gelandet, aber Flug-Test noch nicht geschrieben“ gilt auch, wenn der Flug-Test geschrieben ist, aber eine Pflicht-Etappe
-- in lernziel_stand noch 'offen' steht (genau die Bedingung, unter der test_starten_intern seit W177 einen Nachtragstest startet). Nur ungesetzte Flüge (wie bisher).
-- Nach 20261120_lb3_kann_wiederholen.sql. Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE, keine Daten geändert. Wiederholt ausführbar.
do $mig$
declare d text;
  v_alt text := $a$or (v_n > 0 and v_gel = v_n and not exists (select 1 from schule.testsitzung t where t.lernender_id = p_l and t.einheit_id = v_e and t.art = 'blocktest' and t.status = 'abgeschlossen'));$a$;
  v_neu text := $a$or (v_n > 0 and v_gel = v_n and (not exists (select 1 from schule.testsitzung t where t.lernender_id = p_l and t.einheit_id = v_e and t.art = 'blocktest' and t.status = 'abgeschlossen')
                                                 or exists (select 1 from schule.lernziel_stand s where s.lernender_id = p_l and s.einheit_id = v_e and s.pflicht and s.status = 'offen'))); -- I-5: offener Nachtragstest$a$;
begin
  d := pg_get_functiondef('schule.thema_stufe(bigint, bigint)'::regprocedure);
  if position('I-5: offener Nachtragstest' in d) > 0 then return; end if; -- schon eingespielt
  if position(v_alt in d) = 0 then raise exception 'thema_stufe: Stelle nicht gefunden'; end if;
  execute replace(d, v_alt, v_neu);
end $mig$;
