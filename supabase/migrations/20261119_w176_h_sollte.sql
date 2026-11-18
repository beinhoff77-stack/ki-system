-- Bau-Auftrag H (Werkstatt-Wunsch 176): Sollte-Punkte H6 (Tageszähler), H12 (Expeditions-Import härten), H15 (Expedition: abgeschlossen ≠ selbst gelöst).
-- Setzt 20261119_w176_h8_* und 20261119_w176_h_muss.sql voraus. Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE.
--
-- H6  „heute X selbst gelöst“: der Server zählt die bestätigten eigenen Lösungen (richtig, 1. Versuch, ohne Tipp, Übungs-Bordkarten inkl. Mischkarten) am heutigen Tag
--     in der Zeitzone des Kindes (lernender.zeitzone). Neu: schule.heute_selbst; Feld heute_selbst in schule_einheit_lesen und in der karte-Antwort von schule_uebung_pruefen.
-- H12 expedition_importieren prüft vor dem Schreiben: 3–5 Teile mit eigenem Buchstaben, Antworttyp/Frage/Lösung je Teil, ≥ 3 verschiedene Themen, jede Lernkarte gibt es,
--     jeder Bezug steht unter den Voraussetzungen, Status „geprueft“/„freigegeben“ nur mit entsprechend geprüften/freigegebenen Bezugs-Flügen. Sonst Fehler, nichts geschrieben.
-- H15 Expeditionen melden getrennt: teile_erledigt (abgeschlossen, auch mit gezeigter Lösung) und teile_selbst (im 1. Versuch ohne Tipp gelöst = angewandt).

create or replace function schule.heute_selbst(p_l bigint)
 returns integer language sql stable set search_path to ''
as $function$
  select count(*)::int from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id and a.pool = 'uebung' join schule.lernender l on l.id = v.lernender_id
   where v.lernender_id = p_l and v.testsitzung_id is null and v.richtig and coalesce(v.hilfe, 0) = 0 and coalesce(v.anlauf, 1) = 1
     and (v.am at time zone l.zeitzone)::date = (now() at time zone l.zeitzone)::date;
$function$;

-- H12: expedition_importieren (ganze Funktion; Abgleich unverändert, neu nur die Prüfungen vorab)
create or replace function schule.expedition_importieren(p jsonb, p_status text default null)
 returns jsonb
 language plpgsql
 security definer
 set search_path to ''
as $function$
declare v_id bigint; v_vor jsonb := '[]'::jsonb; v jsonb; t jsonb; v_t bigint; v_e bigint; v_a bigint; v_neu int := 0; v_geaendert int := 0; v_gesperrt int; v_ks text[] := '{}'; v_nr int := 0;
  v_alt schule.expedition; v_status text; v_themen text[] := '{}'; v_y text[] := array['zahl', 'auswahl', 'luecken', 'markierung', 'text'];
begin
  if p_status is not null and p_status not in ('entwurf', 'geprueft', 'freigegeben') then raise exception 'p_status: entwurf, geprueft oder freigegeben'; end if;
  if coalesce(p->>'schluessel', '') = '' or jsonb_typeof(p->'teile') is distinct from 'array' then raise exception 'Datei unvollständig (schluessel, teile)'; end if;
  -- H12: Prüfung vor jedem Schreiben – 3–5 Teile, ≥ 3 Themen, gültige Lernkarten, jeder Bezug unter den Voraussetzungen, Freigabe nur mit freigegebenen Bezugs-Flügen
  if jsonb_array_length(p->'teile') not between 3 and 5 then raise exception 'Eine Expedition hat 3 bis 5 Teile (hier %)', jsonb_array_length(p->'teile'); end if;
  if (select count(distinct t->>'k') from jsonb_array_elements(p->'teile') t) <> jsonb_array_length(p->'teile') or exists (select 1 from jsonb_array_elements(p->'teile') t where coalesce(t->>'k', '') = '') then
    raise exception 'Jeder Teil braucht einen eigenen Buchstaben k'; end if;
  if jsonb_typeof(p->'voraussetzungen') is distinct from 'array' or jsonb_array_length(p->'voraussetzungen') = 0 then raise exception 'Voraussetzungen fehlen'; end if;
  for t in select * from jsonb_array_elements(p->'teile') loop
    if not (t->>'y' = any(v_y)) or t->'o' is null or jsonb_typeof(t->'f') is distinct from 'object' then raise exception 'Teil %: Antworttyp, Frage oder Lösung fehlt', t->>'k'; end if;
    if not exists (select 1 from jsonb_array_elements(p->'voraussetzungen') v where v->>'thema_schluessel' = t->'bezug'->>'thema_schluessel' and v->>'lernziel' = t->'bezug'->>'lernziel') then
      raise exception 'Teil %: Bezug %/% steht nicht unter den Voraussetzungen', t->>'k', t->'bezug'->>'thema_schluessel', t->'bezug'->>'lernziel'; end if;
    if not exists (select 1 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id join schule.thema th on th.id = e.thema_id
                    where th.schluessel = t->'bezug'->>'thema_schluessel' and a.variante_gruppe = t->'bezug'->>'lernziel' and a.pool = 'uebung' and e.status <> 'ersetzt') then
      raise exception 'Teil %: Lernkarte %/% gibt es nicht', t->>'k', t->'bezug'->>'thema_schluessel', t->'bezug'->>'lernziel'; end if;
    if not (t->'bezug'->>'thema_schluessel' = any(v_themen)) then v_themen := v_themen || (t->'bezug'->>'thema_schluessel'); end if;
  end loop;
  if coalesce(array_length(v_themen, 1), 0) < 3 then raise exception 'Eine Expedition verbindet mindestens 3 Themen (hier %)', coalesce(array_length(v_themen, 1), 0); end if;
  select * into v_alt from schule.expedition where schluessel = p->>'schluessel';
  v_status := coalesce(p_status, v_alt.status, 'entwurf');
  if v_status in ('geprueft', 'freigegeben') and exists (
       select 1 from jsonb_array_elements(p->'teile') t
        where not exists (select 1 from schule.einheit e join schule.thema th on th.id = e.thema_id where th.schluessel = t->'bezug'->>'thema_schluessel'
                           and e.status = case v_status when 'freigegeben' then 'freigegeben' else e.status end and e.status in ('geprueft', 'freigegeben'))) then
    raise exception 'Status %: alle Bezugs-Flüge müssen % sein', v_status, case v_status when 'freigegeben' then 'freigegeben' else 'geprüft oder freigegeben' end; end if;
  for v in select * from jsonb_array_elements(coalesce(p->'voraussetzungen', '[]'::jsonb)) loop
    select id into v_t from schule.thema where schluessel = v->>'thema_schluessel';
    if v_t is null then raise exception 'Voraussetzung: Thema % gibt es nicht', v->>'thema_schluessel'; end if;
    v_vor := v_vor || jsonb_build_object('thema_schluessel', v->>'thema_schluessel', 'thema_id', v_t, 'lernziel', v->>'lernziel');
  end loop;
  if v_alt.id is null then
    insert into schule.expedition(schluessel, klasse, titel, einleitung, grafik, voraussetzungen, autor, status)
    values (p->>'schluessel', coalesce(p->'klasse', '{}'), p->>'titel', coalesce(p->>'einleitung', ''), p->'grafik', v_vor, p->>'autor', coalesce(p_status, 'entwurf'))
    returning id into v_id;
  else
    v_id := v_alt.id;
    update schule.expedition set klasse = coalesce(p->'klasse', '{}'), titel = p->>'titel', einleitung = coalesce(p->>'einleitung', ''), grafik = p->'grafik', voraussetzungen = v_vor,
           autor = p->>'autor', status = coalesce(p_status, status), version = version + 1, geaendert_am = now()
     where id = v_id and (klasse, titel, einleitung, grafik, voraussetzungen, autor, status) is distinct from
           (coalesce(p->'klasse', '{}'), p->>'titel', coalesce(p->>'einleitung', ''), p->'grafik', v_vor, p->>'autor', coalesce(p_status, status));
  end if;
  for t in select * from jsonb_array_elements(p->'teile') loop
    v_nr := v_nr + 1; v_ks := v_ks || (t->>'k');
    select id into v_t from schule.thema where schluessel = t->'bezug'->>'thema_schluessel';
    if v_t is null then raise exception 'Teil %: Bezug-Thema % gibt es nicht', t->>'k', t->'bezug'->>'thema_schluessel'; end if;
    select e.id into v_e from schule.einheit e where e.thema_id = v_t and e.status <> 'ersetzt'
     order by (e.status in ('freigegeben', 'geprueft')) desc, e.version desc limit 1;
    if v_e is null then raise exception 'Teil %: zum Thema % gibt es keinen Flug', t->>'k', t->'bezug'->>'thema_schluessel'; end if;
    select id into v_a from schule.aufgabe where expedition_id = v_id and teil = t->>'k';
    if v_a is null then
      insert into schule.aufgabe(einheit_id, thema_id, teilfaehigkeit, art, stufe, variante_gruppe, antworttyp, frage, antworten, loesung, tipp, loesungsweg, punkte_max, reihenfolge, pool,
                                 expedition_id, teil, freigegeben)
      values (v_e, v_t, null, 'uebung', null, t->'bezug'->>'lernziel', t->>'y', t->'f', case when t ? 'a' then t->'a' end, t->'o', t->>'h', t->>'w', 1, v_nr, 'expedition', v_id, t->>'k', true);
      v_neu := v_neu + 1;
    else
      update schule.aufgabe set einheit_id = v_e, thema_id = v_t, variante_gruppe = t->'bezug'->>'lernziel', antworttyp = t->>'y', frage = t->'f',
             antworten = case when t ? 'a' then t->'a' end, loesung = t->'o', tipp = t->>'h', loesungsweg = t->>'w', reihenfolge = v_nr, freigegeben = true
       where id = v_a and (einheit_id, thema_id, variante_gruppe, antworttyp, frage, antworten, loesung, tipp, loesungsweg, reihenfolge, freigegeben) is distinct from
             (v_e, v_t, t->'bezug'->>'lernziel', t->>'y', t->'f', case when t ? 'a' then t->'a' end, t->'o', t->>'h', t->>'w', v_nr, true);
      if found then v_geaendert := v_geaendert + 1; end if;
    end if;
  end loop;
  update schule.aufgabe set freigegeben = false where expedition_id = v_id and freigegeben and not (teil = any(v_ks));
  get diagnostics v_gesperrt = row_count;
  return jsonb_build_object('expedition_id', v_id, 'schluessel', p->>'schluessel', 'teile_neu', v_neu, 'teile_geaendert', v_geaendert, 'teile_gesperrt', v_gesperrt,
    'status', (select status from schule.expedition where id = v_id));
end $function$;

do $$
declare d text;
begin
  -- H6: Tageszähler in die Antworten
  d := pg_get_functiondef('schule.einheit_lesen_intern(bigint, bigint)'::regprocedure);
  if position('''etappen_stand'', schule.etappen_stand(p_lernender, p_einheit),' in d) = 0 then raise exception 'Stelle in einheit_lesen_intern nicht gefunden'; end if;
  d := replace(d, '''etappen_stand'', schule.etappen_stand(p_lernender, p_einheit),', '''etappen_stand'', schule.etappen_stand(p_lernender, p_einheit), ''heute_selbst'', schule.heute_selbst(p_lernender),');
  execute d;
  d := pg_get_functiondef('schule.uebung_pruefen_intern(bigint, jsonb)'::regprocedure);
  if position('''flug_nachtest'', schule.flug_nachtest(k.lernender_id, k.einheit_id),' in d) = 0 then raise exception 'Stelle in uebung_pruefen_intern nicht gefunden (erst 20261119_w176_h_muss.sql einspielen)'; end if;
  d := replace(d, '''flug_nachtest'', schule.flug_nachtest(k.lernender_id, k.einheit_id),', '''flug_nachtest'', schule.flug_nachtest(k.lernender_id, k.einheit_id), ''heute_selbst'', schule.heute_selbst(p_lernender),');
  execute d;
  -- H15: selbst gelöste Teile getrennt von abgeschlossenen
  d := pg_get_functiondef('schule.expeditionen_kind(bigint)'::regprocedure);
  if position('''teile_gesamt'', (select count(*) from schule.aufgabe a where a.expedition_id = x.id and a.freigegeben),' in d) = 0 then raise exception 'Stelle in expeditionen_kind nicht gefunden'; end if;
  d := replace(d, '''teile_gesamt'', (select count(*) from schule.aufgabe a where a.expedition_id = x.id and a.freigegeben),',
    $r$'teile_gesamt', (select count(*) from schule.aufgabe a where a.expedition_id = x.id and a.freigegeben),
      'teile_selbst', (select count(*) from schule.aufgabe a where a.expedition_id = x.id and a.freigegeben
                        and exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id and v.testsitzung_id is null and v.richtig and coalesce(v.hilfe, 0) = 0 and coalesce(v.anlauf, 1) = 1)),$r$);
  execute d;
  d := pg_get_functiondef('api.schule_uebersicht(text, jsonb)'::regprocedure);
  if position('''expeditionen'', (select coalesce(jsonb_agg(jsonb_build_object(''id'', x.id, ''zustand'', z.zustand) order by x.id), ''[]''::jsonb)' in d) = 0 then raise exception 'Stelle in schule_uebersicht nicht gefunden'; end if;
  d := replace(d, '''expeditionen'', (select coalesce(jsonb_agg(jsonb_build_object(''id'', x.id, ''zustand'', z.zustand) order by x.id), ''[]''::jsonb)',
    $r$'expeditionen', (select coalesce(jsonb_agg(jsonb_build_object('id', x.id, 'zustand', z.zustand,
                           'teile_gesamt', (select count(*) from schule.aufgabe a where a.expedition_id = x.id and a.freigegeben),
                           'teile_erledigt', (select count(*) from schule.aufgabe a where a.expedition_id = x.id and a.freigegeben and schule.expedition_teil_erledigt(l.id, a.id)),
                           'teile_selbst', (select count(*) from schule.aufgabe a where a.expedition_id = x.id and a.freigegeben
                                             and exists (select 1 from schule.versuch v where v.lernender_id = l.id and v.aufgabe_id = a.id and v.testsitzung_id is null and v.richtig and coalesce(v.hilfe, 0) = 0 and coalesce(v.anlauf, 1) = 1))) order by x.id), '[]'::jsonb)$r$);
  execute d;
end $$;
