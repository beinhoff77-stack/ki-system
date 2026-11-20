-- Bau-Auftrag LB (LB-1/LB-2/LB-5, App 0.82.0): Felder für die Lehrplan-Ansicht „Nach Klasse“. Nach 20261120_lb3_kann_wiederholen.sql.
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE, keine Bestandsänderung (neue Spalten bleiben leer, befüllt werden sie aus LB-4). Wiederholt ausführbar.
--
-- schule.thema.lernbereich  jsonb  {"gym_by": "M8 1 Funktion und Term", "rs_by": "…", "ib_myp": "…"}   (Überschrift je Lernbereich, LB-4)
-- schule.thema.lehrplan     jsonb  {"gym_by": "…", "rs_by": "…", "ib_myp": "…"}                         (Lehrplan-Bezug / Kompetenzerwartungen, LB-4)
-- Die Reihenfolge je Schulart liegt schon in schule.thema.lehrplan_reihenfolge.
-- schule_plan_lesen.orte[].themen[] zusätzlich: beschreibung, lernbereich, lehrplan, etappen [{lernziel, titel}]
-- schule_lehrplan_uebersicht.themen[] zusätzlich: lernbereich, lehrplan, lehrplan_reihenfolge

alter table schule.thema add column if not exists lernbereich jsonb;
alter table schule.thema add column if not exists lehrplan jsonb;
comment on column schule.thema.lernbereich is 'LB-4: Lernbereich/Kapitel je Schulart (gym_by, rs_by, ib_myp) als Überschrift im Lehrplan „Nach Klasse“';
comment on column schule.thema.lehrplan is 'LB-4: Lehrplan-Bezug (Kompetenzerwartungen, kurz) je Schulart';

do $mig$
declare d text;
begin
  d := pg_get_functiondef('api.schule_plan_lesen(text, jsonb)'::regprocedure);
  if position('''lernbereich''' in d) = 0 then
    if position('''kann_wdh'', schule.thema_kann_wdh(v_l, t.id), ''stufe'', schule.thema_stufe(v_l, t.id),' in d) = 0 then raise exception 'schule_plan_lesen: Stelle nicht gefunden (LB-3 eingespielt?)'; end if;
    d := replace(d, '''kann_wdh'', schule.thema_kann_wdh(v_l, t.id), ''stufe'', schule.thema_stufe(v_l, t.id),',
      '''kann_wdh'', schule.thema_kann_wdh(v_l, t.id), ''stufe'', schule.thema_stufe(v_l, t.id),
                                 ''beschreibung'', t.beschreibung, ''lernbereich'', t.lernbereich, ''lehrplan'', t.lehrplan,
                                 ''etappen'', (select coalesce(jsonb_agg(jsonb_build_object(''lernziel'', q.x->>''lernziel'', ''titel'', q.x->>''titel'') order by q.nr), ''[]''::jsonb)
                                               from schule.einheit e2, jsonb_array_elements(coalesce(e2.inhalt->''etappen'', ''[]''::jsonb)) with ordinality q(x, nr)
                                              where e2.id = (select e3.id from schule.einheit e3 where e3.thema_id = t.id order by (e3.status in (''geprueft'',''freigegeben'')) desc, e3.version desc limit 1)),');
    execute d;
  end if;
  d := pg_get_functiondef('api.schule_lehrplan_uebersicht(text, jsonb)'::regprocedure);
  if position('''lernbereich''' in d) = 0 then
    if position('''jahrgang'', schule.thema_jahrgang(t.id), ''beschreibung'', t.beschreibung,' in d) = 0 then raise exception 'schule_lehrplan_uebersicht: Stelle nicht gefunden'; end if;
    d := replace(d, '''jahrgang'', schule.thema_jahrgang(t.id), ''beschreibung'', t.beschreibung,',
      '''jahrgang'', schule.thema_jahrgang(t.id), ''beschreibung'', t.beschreibung, ''lernbereich'', t.lernbereich, ''lehrplan'', t.lehrplan, ''lehrplan_reihenfolge'', t.lehrplan_reihenfolge,');
    execute d;
  end if;
end $mig$;
