-- Nachtrag zu AB-S aus ChatGPTs Prüfergebnis 885 (AUFTRAEGE.md, „Nachträge aus ChatGPTs Prüfergebnis 885“, An bau-lehrer, Punkt 3).
-- Befund (Live-Text gelesen, 20.11.): schule.test_abschliessen_intern hängt schule.flug_abschluss(...) an JEDE Antwort an – auch bei nicht bestandenem
-- Flug-Test, bei Verbessern (korrektur), beim Nachtragstest, beim Nachtest und beim erneuten Aufruf. Dann kommen flug, etappen, kurz, sterne_flug,
-- naechster_flug, ort_wechsel, ort_fluege mit, obwohl kein Flug geschafft wurde.
-- Neu: testsitzung.flug_geschafft – einmal festgehalten, wenn DIESER Aufruf die Sitzung abschließt und es der erste abgeschlossene Flug-Test (blocktest) des Flugs
-- ist und der Flug damit fertig ist (alle Pflicht-Etappen nachgewiesen/korrigiert/gesichert). Verbessern, Nachtragstest (späterer blocktest), Nachtest und
-- vor dem Einspielen abgeschlossene Sitzungen: false.
-- Antwort: immer 'flug_geschafft' (bool). Die Abschluss-Felder (flug_abschluss) nur bei flug_geschafft oder ort_geschafft (Ort durch diesen Abschluss geschafft,
-- AB-S) – auch beim erneuten Aufruf derselben Sitzung (dasselbe Ergebnis, „Test ansehen“).
-- Nach 20261120_ab_s_abschluss.sql. Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE, keine Bestandsänderung. Wiederholt ausführbar.

alter table schule.testsitzung add column if not exists flug_geschafft boolean;
comment on column schule.testsitzung.flug_geschafft is 'AB-S Nachtrag: dieser Flug-Test hat den Flug erstmals abgeschlossen (beim Abschließen festgehalten); null = vor dem Einspielen';

do $mig$
declare d text; v_a1 text; v_a2 text; v_a3 text; v_a4 text;
begin
  d := pg_get_functiondef('schule.test_abschliessen_intern(bigint, jsonb)'::regprocedure);
  if position('flug_geschafft' in d) > 0 then return; end if; -- schon eingespielt
  v_a1 := 'v_quote numeric; v_ergebnis text; v_route schule.route; v_pos int;';
  v_a2 := E'  if t.status = ''laeuft'' then\n';
  v_a3 := E'  if t.ort_geschafft is null and t.status = ''abgeschlossen'' then';
  v_a4 := '|| schule.flug_abschluss(p_lernender, t.id);';
  if position(v_a1 in d) = 0 or position(v_a2 in d) = 0 or position(v_a3 in d) = 0 or position(v_a4 in d) = 0 then
    raise exception 'test_abschliessen_intern: Stellen nicht gefunden'; end if;
  d := replace(d, v_a1, v_a1 || ' v_jetzt boolean := false;');
  d := replace(d, v_a2, v_a2 || E'    v_jetzt := true; -- AB-S Nachtrag: dieser Aufruf schließt die Sitzung ab\n');
  d := replace(d, v_a3, E'  -- AB-S Nachtrag: Flug durch diesen Flug-Test erstmals geschafft? (nur beim Abschließen, einmal festgehalten)\n'
    || E'  if t.flug_geschafft is null and t.status = ''abgeschlossen'' then\n'
    || E'    t.flug_geschafft := v_jetzt and t.art = ''blocktest'' and coalesce(v_einheit_fertig, false)\n'
    || E'      and not exists (select 1 from schule.testsitzung x where x.lernender_id = p_lernender and x.einheit_id = t.einheit_id and x.art = ''blocktest''\n'
    || E'                       and x.status = ''abgeschlossen'' and x.id <> t.id and x.id < t.id);\n'
    || E'    update schule.testsitzung set flug_geschafft = t.flug_geschafft where id = t.id;\n'
    || E'  end if;\n' || v_a3);
  d := replace(d, v_a4, $a$|| jsonb_build_object('flug_geschafft', coalesce(t.flug_geschafft, false))
    || case when coalesce(t.flug_geschafft, false) or coalesce(t.ort_geschafft, false) then schule.flug_abschluss(p_lernender, t.id) else '{}'::jsonb end; -- AB-S Nachtrag$a$);
  execute d;
end $mig$;
