-- W150 Eltern E-3 (Bau-Auftrag Phase 2, Schritt C): „✎ Ändern lassen“ überall + „Meine Aufträge“.
-- Die Arten bleiben (Prüfbedingung rueckmeldung_art_check unverändert, kein DROP). Neu ist der Bezug, an dem der Auftrag gegeben wurde:
--   erklaerung · etappe · bordkarte · flug · plan · allgemein
-- Die App sendet ihn als daten.bezug; ohne diese Migration ignoriert die Datenbank das Feld (die App läuft weiter).
-- schule_rueckmeldungen liefert zusätzlich bezug, block_id, lernender_id, kind (Name), flug (Titel) und etappe (Titel der Etappe).

alter table schule.rueckmeldung add column if not exists bezug text
  check (bezug is null or bezug in ('erklaerung', 'etappe', 'bordkarte', 'flug', 'plan', 'allgemein'));
comment on column schule.rueckmeldung.bezug is 'E-3: wo „Ändern lassen“ angetippt wurde (erklaerung, etappe, bordkarte, flug, plan, allgemein)';

create or replace function api.schule_rueckmeldung_geben(p_schluessel text, p_daten jsonb)
 returns jsonb
 language plpgsql
 security definer
 set search_path to ''
as $function$
declare v_id bigint; v_e bigint := nullif(p_daten->>'einheit_id','')::bigint; v_a bigint := nullif(p_daten->>'aufgabe_id','')::bigint;
  v_bezug text := nullif(p_daten->>'bezug','');
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  if v_bezug is not null and v_bezug not in ('erklaerung', 'etappe', 'bordkarte', 'flug', 'plan', 'allgemein') then raise exception 'Unbekannter Bezug' using errcode = 'P0001'; end if;
  if v_a is not null and v_e is null then select einheit_id into v_e from schule.aufgabe where id = v_a; end if;
  insert into schule.rueckmeldung(von, art, text, block_id, einheit_id, lernziel, aufgabe_id, lernender_id, bezug)
  values (coalesce((select i.rolle || ':' || i.name from schule.lern_ich(p_schluessel) i where schule.ist_lern(p_schluessel)), 'eltern:App'),
          coalesce(nullif(p_daten->>'art',''), 'sonstiges'), trim(coalesce(p_daten->>'text','')),
          coalesce(nullif(p_daten->>'block_id','')::bigint, (select block_id from schule.einheit where id = v_e)),
          v_e, nullif(p_daten->>'lernziel',''), v_a, nullif(p_daten->>'lernender_id','')::bigint, v_bezug)
  returning id into v_id;
  return jsonb_build_object('ok', true, 'id', v_id);
end $function$;

create or replace function api.schule_rueckmeldungen(p_schluessel text, p_daten jsonb default null::jsonb)
 returns jsonb
 language plpgsql
 stable security definer
 set search_path to ''
as $function$
begin
  perform schule.wer_tn(p_schluessel);
  if not schule.ist_leiter(p_schluessel) then raise exception 'Nur Eltern/Lehrer' using errcode = 'P0001'; end if;
  return jsonb_build_object('ok', true, 'rueckmeldungen', (select coalesce(jsonb_agg(jsonb_build_object(
      'id', r.id, 'von', r.von, 'art', r.art, 'text', r.text, 'status', r.status, 'antwort', r.antwort, 'am', r.am, 'bearbeitet_am', r.bearbeitet_am,
      'einheit_id', r.einheit_id, 'lernziel', r.lernziel, 'aufgabe_id', r.aufgabe_id, 'block_id', r.block_id, 'lernender_id', r.lernender_id, 'bezug', r.bezug,
      'kind', (select l.anzeigename from schule.lernender l where l.id = r.lernender_id),
      'ort', (select coalesce(b.stadt, b.titel) || ' – ' || b.titel from schule.block b where b.id = r.block_id),
      'flug', (select t.unterthema from schule.einheit e join schule.thema t on t.id = e.thema_id where e.id = r.einheit_id),
      'etappe', (select x->>'titel' from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) x
                  where e.id = r.einheit_id and x->>'lernziel' = r.lernziel limit 1),
      'aufgabe', (select a.frage->>'text' from schule.aufgabe a where a.id = r.aufgabe_id))
    order by (r.status in ('offen','in_arbeit')) desc, r.am desc), '[]'::jsonb)
    from (select * from schule.rueckmeldung order by am desc limit 200) r));
end $function$;

-- Werkstatt-Nachricht nennt den Bezug; beantwortete Aufträge erscheinen in der App unter „Meine Aufträge“.
do $$
declare d text;
begin
  d := pg_get_functiondef('schule.rueckmeldung_an_werkstatt()'::regprocedure);
  if position('new.art || E''\n'' || new.text' in d) = 0 or position('(sichtbar in der App unter Rückmeldungen)' in d) = 0 then
    raise exception 'Stellen in rueckmeldung_an_werkstatt nicht gefunden';
  end if;
  d := replace(d, 'new.art || E''\n'' || new.text', 'new.art || coalesce('' · an: '' || new.bezug, '''') || E''\n'' || new.text');
  d := replace(d, '(sichtbar in der App unter Rückmeldungen)', '(sichtbar in der App unter „Meine Aufträge“)');
  execute d;
end $$;
