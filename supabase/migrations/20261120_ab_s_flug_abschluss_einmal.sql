-- Nachtrag zu AB-S aus ChatGPTs Prüfergebnis 885 (AUFTRAEGE.md, „Nachträge aus ChatGPTs Prüfergebnis 885“, An bau-lehrer, Punkt 3).
-- Befund (Live-Text gelesen, 20.11.): schule.test_abschliessen_intern hängt schule.flug_abschluss(...) an JEDE Antwort an – auch bei nicht bestandenem
-- Flug-Test, bei Verbessern (korrektur), beim Nachtragstest, beim Nachtest und beim erneuten Aufruf. Dann kommen flug, etappen, kurz, sterne_flug,
-- naechster_flug, ort_wechsel, ort_fluege mit, obwohl kein Flug geschafft wurde.
-- Neu: testsitzung.flug_geschafft – einmal festgehalten, wenn DIESER Aufruf die Sitzung abschließt und der Flug dadurch ZUM ERSTEN MAL fertig wird
-- (alle Pflicht-Etappen nachgewiesen/korrigiert/gesichert) – über den Flug-Test (blocktest) oder über Verbessern (korrektur)
-- (Nachträge 20.11. nachmittags, Teil A: Entscheidung Haupt-Chat). „Zum ersten Mal“: vorher nicht fertig und keine frühere abgeschlossene
-- Flug-Test-/Verbessern-Sitzung dieses Flugs, die ihn schon fertig gemacht hat: flug_geschafft true – oder flug_geschafft null (vor dem Einspielen) UND der Flug war
-- nach dieser Sitzung fertig (schule.flug_fertig_nach: je Pflicht-Etappe ist das letzte Test-Ergebnis bis zu dieser Sitzung ganz richtig). Eine alte nicht bestandene
-- Sitzung sperrt also keinen späteren ersten Abschluss mehr (Nachträge aus ChatGPT 888, Muss 1).
-- false: nicht bestandener Test, Nachtragstest (der Flug war schon einmal fertig), Nachtest, alles nach dem ersten Fertigwerden, vor dem Einspielen abgeschlossene
-- Sitzungen (beim ersten Lesen festgehalten).
-- Antwort: immer 'flug_geschafft' (bool). Die Abschluss-Felder (flug_abschluss) nur bei flug_geschafft oder ort_geschafft (Ort durch diesen Abschluss geschafft,
-- AB-S) – auch beim erneuten Aufruf derselben Sitzung (dasselbe Ergebnis, „Test ansehen“).
-- Nach 20261120_ab_s_abschluss.sql. Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE, keine Bestandsänderung. Wiederholt ausführbar.

alter table schule.testsitzung add column if not exists flug_geschafft boolean;

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
  d := replace(d, v_a1, v_a1 || ' v_jetzt boolean := false; v_vorher_fertig boolean := true;');
  d := replace(d, v_a2, v_a2 || E'    v_jetzt := true; -- AB-S Nachtrag: dieser Aufruf schließt die Sitzung ab\n'
    || E'    v_vorher_fertig := exists (select 1 from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = t.einheit_id)\n'
    || E'      and not exists (select 1 from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = t.einheit_id\n'
    || E'                       and s.pflicht and s.status not in (''nachgewiesen'',''korrigiert'',''gesichert''));\n');
  d := replace(d, v_a3, E'  -- AB-S Nachtrag: Flug durch diesen Flug-Test erstmals geschafft? (nur beim Abschließen, einmal festgehalten)\n'
    || E'  if t.flug_geschafft is null and t.status = ''abgeschlossen'' then\n'
    || E'    t.flug_geschafft := v_jetzt and t.art in (''blocktest'', ''korrektur'') and coalesce(v_einheit_fertig, false) and not v_vorher_fertig\n'
    || E'      and not exists (select 1 from schule.testsitzung x where x.lernender_id = p_lernender and x.einheit_id = t.einheit_id and x.art in (''blocktest'', ''korrektur'')\n'
    || E'                       and x.status = ''abgeschlossen'' and x.id < t.id\n'
    || E'                       and (x.flug_geschafft or (x.flug_geschafft is null and schule.flug_fertig_nach(p_lernender, t.einheit_id, x.id))));\n'
    || E'    update schule.testsitzung set flug_geschafft = t.flug_geschafft where id = t.id;\n'
    || E'  end if;\n' || v_a3);
  d := replace(d, v_a4, $a$|| jsonb_build_object('flug_geschafft', coalesce(t.flug_geschafft, false))
    || case when coalesce(t.flug_geschafft, false) or coalesce(t.ort_geschafft, false) then schule.flug_abschluss(p_lernender, t.id) else '{}'::jsonb end; -- AB-S Nachtrag$a$);
  execute d;
end $mig$;
