-- Befund 20.11. 05:55 (Haupt-Chat): Jedes Laden eines Flugs stellte neue Mischkarten aus, die alten blieben 24 Stunden offen (viele offene Ausgaben, schwächt H10).
-- Jetzt: schule.mischkarten gibt zuerst die noch offenen, gültigen Ausgaben dieses Kindes für diesen Flug wieder aus (dieselben Karten) und füllt nur auf,
-- wenn weniger als gewünscht offen sind. Offene Ausgaben eines anderen Flugs, älter als 24 Stunden oder nicht mehr gültig (Etappe nicht mehr gelandet,
-- Bordkarte gesperrt) werden beim Ausliefern als verfallen markiert (verfallen_am; nicht löschen). misch_gueltig und misch_buchen zählen verfallene nicht.
-- Nach 20261120_i3_lernregeln_nachpruefung.sql. Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE, keine Bestandsänderung. Wiederholt ausführbar.
-- Hinweis: Der eindeutige Index misch_ausgabe_offen_eindeutig (eingeloest_am is null) bleibt; eine verfallene Ausgabe derselben Bordkarte wird beim erneuten Ausliefern
-- wiederbelebt (ausgegeben_am neu, verfallen_am null) statt eine zweite Zeile anzulegen.

alter table schule.misch_ausgabe add column if not exists verfallen_am timestamptz;
comment on column schule.misch_ausgabe.verfallen_am is 'I-4: beim Ausliefern als verfallen markiert (anderer Flug, älter als 24 h oder nicht mehr gültig); zählt nicht mehr';

create or replace function schule.mischkarten(p_lernender bigint, p_einheit bigint, p_anzahl integer default 8)
 returns jsonb
 language plpgsql
 set search_path to ''
as $function$
declare v_lz text; v_ids bigint[] := '{}'; v_neu jsonb; v_x jsonb; v_etappen text[] := '{}'; v_test boolean;
begin
  select coalesce(l.ist_test, false) into v_test from schule.lernender l where l.id = p_lernender;
  -- 1. verfallen markieren: anderer Flug, älter als 24 Stunden, oder nicht mehr gültig
  update schule.misch_ausgabe m set verfallen_am = now()
   where m.lernender_id = p_lernender and m.eingeloest_am is null and m.verfallen_am is null
     and (m.einheit_id is distinct from p_einheit or m.ausgegeben_am < now() - interval '24 hours'
          or not exists (select 1 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
                          join schule.karte_stand k on k.lernender_id = p_lernender and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe and k.sitzt
                          where a.id = m.aufgabe_id and a.pool = 'uebung' and a.stufe in (2, 3) and a.freigegeben
                            and (e.status in ('geprueft', 'freigegeben') or (e.status = 'entwurf' and v_test))));
  -- 2. dieselben Karten wieder ausgeben (je Etappe höchstens eine, älteste Ausgabe zuerst)
  select coalesce(array_agg(q.aufgabe_id order by q.ausgegeben_am, q.id), '{}'), coalesce(array_agg(q.etappe order by q.ausgegeben_am, q.id), '{}')
    into v_ids, v_etappen
    from (select distinct on (a.einheit_id, a.variante_gruppe) m.id, m.aufgabe_id, m.ausgegeben_am, a.einheit_id || '/' || a.variante_gruppe etappe
            from schule.misch_ausgabe m join schule.aufgabe a on a.id = m.aufgabe_id
           where m.lernender_id = p_lernender and m.einheit_id = p_einheit and m.eingeloest_am is null and m.verfallen_am is null
           order by a.einheit_id, a.variante_gruppe, m.ausgegeben_am, m.id) q;
  if cardinality(v_ids) > p_anzahl then v_ids := v_ids[1:p_anzahl]; end if;
  -- 3. auffüllen, wenn weniger als gewünscht offen sind – nur aus Etappen, die noch keine offene Karte haben
  if cardinality(v_ids) < p_anzahl then
    v_neu := schule.mischkarten_waehlen(p_lernender, p_einheit, 50);
    select et.x->>'lernziel' into v_lz from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality et(x, nr)
     where e.id = p_einheit and not exists (select 1 from schule.karte_stand k where k.lernender_id = p_lernender and k.einheit_id = e.id and k.lernziel = et.x->>'lernziel' and k.sitzt)
     order by et.nr limit 1;
    for v_x in select y.j from jsonb_array_elements(v_neu) with ordinality y(j, nr) order by y.nr loop
      exit when cardinality(v_ids) >= p_anzahl;
      continue when (v_x->>'id')::bigint = any(v_ids)
        or ((v_x->>'einheit_id') || '/' || (select a.variante_gruppe from schule.aufgabe a where a.id = (v_x->>'id')::bigint)) = any(v_etappen);
      v_ids := v_ids || (v_x->>'id')::bigint;
      v_etappen := v_etappen || ((v_x->>'einheit_id') || '/' || (select a.variante_gruppe from schule.aufgabe a where a.id = (v_x->>'id')::bigint));
      insert into schule.misch_ausgabe(lernender_id, aufgabe_id, einheit_id, lernziel) values (p_lernender, (v_x->>'id')::bigint, p_einheit, v_lz)
      on conflict (lernender_id, aufgabe_id) where eingeloest_am is null
      do update set ausgegeben_am = now(), verfallen_am = null, einheit_id = excluded.einheit_id, lernziel = excluded.lernziel;
    end loop;
  end if;
  -- 4. Antwort wie bisher (Anzeige der Bordkarte + einheit_id, quelle, stadt, etappe), sortiert: dieser Flug, dieser Kontinent, älter
  return (select coalesce(jsonb_agg(z.j order by z.rang, z.nr), '[]'::jsonb) from (
    select schule.aufgabe_anzeige(a, true) || jsonb_build_object('einheit_id', a.einheit_id,
             'quelle', case when a.einheit_id = p_einheit then 'flug' when b.kontinent_id = (select b2.kontinent_id from schule.einheit e2 join schule.block b2 on b2.id = e2.block_id where e2.id = p_einheit) then 'kontinent' else 'aelter' end,
             'stadt', b.stadt,
             'etappe', (select et->>'titel' from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) et where et->>'lernziel' = a.variante_gruppe limit 1)) j,
           case when a.einheit_id = p_einheit then 1 when b.kontinent_id = (select b2.kontinent_id from schule.einheit e2 join schule.block b2 on b2.id = e2.block_id where e2.id = p_einheit) then 2 else 3 end rang,
           u.nr
      from unnest(v_ids) with ordinality u(id, nr) join schule.aufgabe a on a.id = u.id join schule.einheit e on e.id = a.einheit_id join schule.block b on b.id = e.block_id) z);
end $function$;

create or replace function schule.misch_gueltig(p_lernender bigint, a schule.aufgabe, p jsonb)
 returns boolean
 language sql
 stable
 set search_path to ''
as $function$
  select coalesce(coalesce((p->>'misch')::boolean, false) and a.pool = 'uebung' and a.stufe in (2, 3) and a.freigegeben
     and exists (select 1 from schule.karte_stand k where k.lernender_id = p_lernender and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe and k.sitzt)
     and exists (select 1 from schule.misch_ausgabe m where m.lernender_id = p_lernender and m.aufgabe_id = a.id and m.eingeloest_am is null and m.verfallen_am is null -- I-4
                   and m.ausgegeben_am >= now() - interval '24 hours'
                   and case when m.einheit_id is not null
                            then not (m.einheit_id = a.einheit_id and m.lernziel is not distinct from a.variante_gruppe) -- I-3: gespeicherte Lage
                            else nullif(p->>'aktuell_einheit', '') is not null and nullif(p->>'aktuell_lernziel', '') is not null
                                 and not ((p->>'aktuell_einheit')::bigint = a.einheit_id and p->>'aktuell_lernziel' = a.variante_gruppe) end), false); -- Ausgabe aus 0.81.1
$function$;

do $mig$
declare d text;
begin
  -- misch_buchen: nur eine nicht verfallene Ausgabe einlösen
  d := pg_get_functiondef('schule.misch_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)'::regprocedure);
  if position('verfallen_am' in d) = 0 then
    if position('where m.lernender_id = p_l and m.aufgabe_id = p_aufgabe and m.eingeloest_am is null' in d) = 0 then raise exception 'misch_buchen: Stelle nicht gefunden'; end if;
    d := replace(d, 'where m.lernender_id = p_l and m.aufgabe_id = p_aufgabe and m.eingeloest_am is null',
                    'where m.lernender_id = p_l and m.aufgabe_id = p_aufgabe and m.eingeloest_am is null and m.verfallen_am is null');
    execute d;
  end if;
end $mig$;
