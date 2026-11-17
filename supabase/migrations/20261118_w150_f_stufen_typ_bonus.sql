-- Bau-Auftrag F (Werkstatt #150): Aufgabentyp je Bordkarte („g“ → schule.aufgabe.typ) und Bonus-Bordkarten (Pool „bonus“, Knobel).
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP von Tabellen, Spalten oder Funktionen, kein DELETE.
-- Einzige Ausnahme: zwei CHECK-Bedingungen werden ersetzt (aufgabe_pool_check um 'bonus', sterne_grund_check um 'bonus' erweitert).
-- Das geht in Postgres nur mit „drop constraint … add constraint“ in einem Befehl; dabei gehen keine Daten verloren.
--
-- Was die App danach bekommt:
--   aufgabe_anzeige (alle Bordkarten an das Kind): zusätzlich typ und bei Bonus-Bordkarten bonus: true
--   schule_einheit_lesen: neu „bonus“ = Knobel-Bordkarten der Einheit (nur freigegebene) mit versuche, geloest, geloest_erst (richtig im ersten Versuch)
--   schule_uebung_pruefen: nimmt Bonus-Bordkarten an; Antwort dann { ok, format_ok, richtig, bonus: true, erster_versuch, sterne (30 oder 0), knobel_sterne, loesung, loesungsweg } –
--                          kein „nochmal“, kein karte-Stand, zählt nicht für „sitzt“, Wiederholung oder Test (karte_buchen bucht nur pool = 'uebung')
--   schule_konto: konto.knobel_sterne (Zahl der Bonus-Bordkarten richtig im ersten Versuch) und knobel_tag = eine Knobel-Bordkarte aus einer sitzenden Etappe
--                 (heute noch nicht versucht, je Tag fest gewählt; null, wenn das Kind heute schon geknobelt hat oder es keine gibt)
--   schule_lernstand: je Etappe knobel_gesamt und knobel_geloest
--   schule_inhalt_lesen: je Aufgabe typ
-- Abgleich: schule.aufgaben_einfuegen und schule.einheit_abgleichen übernehmen a->>'g' nach typ (auch für vorhandene Aufgaben mit gleicher Frage) und legen Pool „bonus“ mit art 'uebung' an.
-- Hinweis: Aufgaben freigegebener Einheiten schützt der Trigger aufgabe_schutz weiterhin – dort scheitert ein Abgleich wie bisher.

-- 1. Spalte typ und erlaubte Werte
alter table schule.aufgabe add column if not exists typ text;
comment on column schule.aufgabe.typ is 'Aufgabentyp („Gedanke“, Feld g der Themen-Datei): Stufe 1 direkt|erkennen, Stufe 2 mehrschritt|einkleidung|umkehr|darstellung, Stufe 3 rueckwaerts|verknuepfen|begruenden|fehler|transfer|parameter|pruefung, Bonus knobel';
do $$
begin
  if not exists (select 1 from pg_constraint where conname = 'aufgabe_typ_check' and conrelid = 'schule.aufgabe'::regclass) then
    alter table schule.aufgabe add constraint aufgabe_typ_check check (typ is null or typ in ('direkt', 'erkennen', 'mehrschritt', 'einkleidung', 'umkehr', 'darstellung',
      'rueckwaerts', 'verknuepfen', 'begruenden', 'fehler', 'transfer', 'parameter', 'pruefung', 'knobel'));
  end if;
  if not exists (select 1 from pg_constraint where conname = 'aufgabe_bonus_check' and conrelid = 'schule.aufgabe'::regclass) then
    alter table schule.aufgabe add constraint aufgabe_bonus_check check (pool <> 'bonus' or (typ = 'knobel' and stufe = 3));
  end if;
end $$;
alter table schule.aufgabe drop constraint if exists aufgabe_pool_check,
  add constraint aufgabe_pool_check check (pool = any (array['uebung', 'test', 'korrektur', 'sicherung', 'bonus']));
alter table schule.sterne drop constraint if exists sterne_grund_check,
  add constraint sterne_grund_check check (grund = any (array['uebung', 'test', 'ort', 'einloesung', 'korrektur_hand', 'bonus']));
insert into schule.regel(schluessel, wert, hinweis) values ('sterne_bonus_richtig', '30'::jsonb, 'Knobel-Bordkarte richtig im ersten Versuch (je Aufgabe einmal)')
  on conflict (schluessel) do nothing;

-- 2. Einfügen: typ übernehmen, Bonus als art 'uebung'
create or replace function schule.aufgaben_einfuegen(p_e bigint, p jsonb)
 returns integer
 language sql
 set search_path to ''
as $function$
with q as (select value x from jsonb_array_elements(p)), ins as (
insert into schule.aufgabe(einheit_id, thema_id, teilfaehigkeit, art, stufe, variante_gruppe, antworttyp, frage, antworten, loesung, tipp, loesungsweg, punkte_max, reihenfolge, pool, typ)
select p_e, (select thema_id from schule.einheit where id = p_e), x->>'t', case x->>'p' when 'uebung' then 'uebung' when 'bonus' then 'uebung' when 'test' then 'blocktest' else 'nachtest' end,
  (x->>'s')::smallint, x->>'l', x->>'y', x->'f', case when x ? 'a' then x->'a' end, x->'o', x->>'h', x->>'w', 1, (x->>'r')::int, x->>'p', x->>'g' from q
where not exists (select 1 from schule.aufgabe b where b.einheit_id = p_e and b.frage = x->'f' and b.antworten is not distinct from (case when x ? 'a' then x->'a' end))
returning 1) select count(*)::int from ins $function$;

-- 3. Anzeige einer Bordkarte: typ und Bonus-Kennzeichen
create or replace function schule.aufgabe_anzeige(a schule.aufgabe, p_mit_tipp boolean)
 returns jsonb
 language sql
 immutable
 set search_path to ''
as $function$
  select jsonb_strip_nulls(jsonb_build_object('id', a.id, 'lernziel', a.variante_gruppe, 'stufe', a.stufe, 'antworttyp', a.antworttyp,
    'frage', a.frage, 'antworten', a.antworten, 'einheit', a.loesung->>'einheit',
    'tipp', case when p_mit_tipp then a.tipp end, 'typ', a.typ, 'bonus', case when a.pool = 'bonus' then true end));
$function$;

-- 4. Sterne aus einem Versuch: Bonus-Bordkarte nur richtig im ersten Versuch (30 Sterne, Grund „bonus“, je Aufgabe einmal); sonst wie bisher
create or replace function schule.sterne_aus_versuch()
 returns trigger
 language plpgsql
 set search_path to ''
as $function$
declare v_pool text;
begin
  if new.richtig and new.testsitzung_id is null then
    select pool into v_pool from schule.aufgabe where id = new.aufgabe_id;
    if v_pool = 'bonus' then
      if coalesce(new.versuch_nr, 1) = 1 then
        insert into schule.sterne(lernender_id, menge, grund, bezug)
        values (new.lernender_id, schule.sterne_regel('sterne_bonus_richtig'), 'bonus', 'aufgabe:' || new.aufgabe_id)
        on conflict do nothing;
      end if;
    else
      insert into schule.sterne(lernender_id, menge, grund, bezug)
      values (new.lernender_id, schule.sterne_regel('sterne_uebung_richtig'), 'uebung', 'aufgabe:' || new.aufgabe_id)
      on conflict do nothing;
    end if;
  end if;
  return new;
end $function$;

-- 5. Gezieltes Ersetzen in bestehenden Funktionen (Stellen im Live-Text vorab geprüft)
do $$
declare d text;
begin
  -- einheit_abgleichen: typ übernehmen (auch bei vorhandenen Aufgaben), Bonus als art 'uebung'
  d := pg_get_functiondef('schule.einheit_abgleichen(jsonb, text)'::regprocedure);
  if position('teilfaehigkeit = q.a->>''t'', pool = q.a->>''p'',' in d) = 0
     or position('art = case q.a->>''p'' when ''uebung'' then ''uebung'' when ''test''' in d) = 0
     or position('(b.loesung, b.tipp, b.loesungsweg, b.stufe, b.variante_gruppe, b.pool) is distinct from (q.a->''o'', q.a->>''h'', q.a->>''w'', (q.a->>''s'')::smallint, q.a->>''l'', q.a->>''p'')' in d) = 0 then
    raise exception 'Stellen in einheit_abgleichen nicht gefunden';
  end if;
  d := replace(d, 'teilfaehigkeit = q.a->>''t'', pool = q.a->>''p'',', 'teilfaehigkeit = q.a->>''t'', pool = q.a->>''p'', typ = q.a->>''g'',');
  d := replace(d, 'art = case q.a->>''p'' when ''uebung'' then ''uebung'' when ''test''', 'art = case q.a->>''p'' when ''uebung'' then ''uebung'' when ''bonus'' then ''uebung'' when ''test''');
  d := replace(d, '(b.loesung, b.tipp, b.loesungsweg, b.stufe, b.variante_gruppe, b.pool) is distinct from (q.a->''o'', q.a->>''h'', q.a->>''w'', (q.a->>''s'')::smallint, q.a->>''l'', q.a->>''p'')',
                  '(b.loesung, b.tipp, b.loesungsweg, b.stufe, b.variante_gruppe, b.pool, b.typ) is distinct from (q.a->''o'', q.a->>''h'', q.a->>''w'', (q.a->>''s'')::smallint, q.a->>''l'', q.a->>''p'', q.a->>''g'')');
  execute d;

  -- uebung_pruefen_intern: Bonus-Bordkarten annehmen – ohne „nochmal“ und ohne Karten-Stand
  d := pg_get_functiondef('schule.uebung_pruefen_intern(bigint, jsonb)'::regprocedure);
  if position('if a.id is null or a.pool <> ''uebung'' then raise exception ''Keine Übungsaufgabe''' in d) = 0
     or position('  b := schule.antwort_bewerten(a, p_daten->''antwort'');' in d) = 0
     or position('  return jsonb_strip_nulls(jsonb_build_object(''ok'', true, ''format_ok'', true, ''richtig'', v_ri, ''grund'', b->>''grund'', ''loesung'', a.loesung, ''loesungsweg'', a.loesungsweg,' in d) = 0 then
    raise exception 'Stellen in uebung_pruefen_intern nicht gefunden';
  end if;
  d := replace(d, 'if a.id is null or a.pool <> ''uebung'' then raise exception ''Keine Übungsaufgabe''', 'if a.id is null or a.pool not in (''uebung'', ''bonus'') then raise exception ''Keine Übungsaufgabe''');
  d := replace(d, '  b := schule.antwort_bewerten(a, p_daten->''antwort'');', '  if a.pool = ''bonus'' then v_anlauf := null; end if; -- Bonus: kein zweiter Anlauf
  b := schule.antwort_bewerten(a, p_daten->''antwort'');');
  d := replace(d, '  return jsonb_strip_nulls(jsonb_build_object(''ok'', true, ''format_ok'', true, ''richtig'', v_ri, ''grund'', b->>''grund'', ''loesung'', a.loesung, ''loesungsweg'', a.loesungsweg,',
    $r$  if a.pool = 'bonus' then
    return jsonb_strip_nulls(jsonb_build_object('ok', true, 'format_ok', true, 'richtig', v_ri, 'bonus', true, 'grund', b->>'grund', 'loesung', a.loesung, 'loesungsweg', a.loesungsweg,
      'erster_versuch', not exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id and v.client_id <> v_cid),
      'sterne', coalesce((select s.menge from schule.sterne s where s.lernender_id = p_lernender and s.grund = 'bonus' and s.bezug = 'aufgabe:' || a.id
                          and exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.client_id = v_cid and v.richtig and coalesce(v.versuch_nr, 1) = 1)), 0),
      'knobel_sterne', (select count(*) from schule.sterne s where s.lernender_id = p_lernender and s.grund = 'bonus')));
  end if;
  return jsonb_strip_nulls(jsonb_build_object('ok', true, 'format_ok', true, 'richtig', v_ri, 'grund', b->>'grund', 'loesung', a.loesung, 'loesungsweg', a.loesungsweg,$r$);
  execute d;

  -- karte_buchen: die schwere Bordkarte für „sitzt“ muss einen Stufe-3-Typ haben (ohne typ wie bisher: Stufe 3)
  d := pg_get_functiondef('schule.karte_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)'::regprocedure);
  if position('if a.stufe = 3 then k.schwer_ok := true; end if;' in d) = 0 then raise exception 'Stelle in karte_buchen nicht gefunden'; end if;
  d := replace(d, 'if a.stufe = 3 then k.schwer_ok := true; end if;',
    'if a.stufe = 3 and (a.typ is null or a.typ in (''rueckwaerts'', ''verknuepfen'', ''begruenden'', ''fehler'', ''transfer'', ''parameter'', ''pruefung'')) then k.schwer_ok := true; end if;');
  execute d;

  -- einheit_lesen_intern: Knobel-Bordkarten der Einheit
  d := pg_get_functiondef('schule.einheit_lesen_intern(bigint, bigint)'::regprocedure);
  if position('''inhalt'', e.inhalt - ''pruefhinweise'', ''uebungen'', v_ueb,' in d) = 0 then raise exception 'Stelle in einheit_lesen_intern nicht gefunden'; end if;
  d := replace(d, '''inhalt'', e.inhalt - ''pruefhinweise'', ''uebungen'', v_ueb,',
    $r$'inhalt', e.inhalt - 'pruefhinweise', 'uebungen', v_ueb,
    'bonus', (select coalesce(jsonb_agg(schule.aufgabe_anzeige(a, true) || jsonb_build_object(
        'versuche', (select count(*) from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id and v.testsitzung_id is null),
        'geloest', exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id and v.testsitzung_id is null and v.richtig),
        'geloest_erst', exists (select 1 from schule.sterne s where s.lernender_id = p_lernender and s.grund = 'bonus' and s.bezug = 'aufgabe:' || a.id))
        order by a.variante_gruppe, a.reihenfolge), '[]'::jsonb)
      from schule.aufgabe a where a.einheit_id = p_einheit and a.pool = 'bonus'
       and (a.freigegeben or exists (select 1 from schule.lernender l where l.id = p_lernender and l.ist_test))),$r$);
  execute d;

  -- schule_inhalt_lesen (Eltern/Lehrer): typ je Aufgabe
  d := pg_get_functiondef('api.schule_inhalt_lesen(text, jsonb)'::regprocedure);
  if position('''id'', a.id, ''lernziel'', a.variante_gruppe, ''pool'', a.pool, ''stufe'', a.stufe,' in d) = 0 then raise exception 'Stelle in schule_inhalt_lesen nicht gefunden'; end if;
  d := replace(d, '''id'', a.id, ''lernziel'', a.variante_gruppe, ''pool'', a.pool, ''stufe'', a.stufe,', '''id'', a.id, ''lernziel'', a.variante_gruppe, ''pool'', a.pool, ''stufe'', a.stufe, ''typ'', a.typ,');
  execute d;

  -- schule_lernstand: je Etappe Knobel x von y
  d := pg_get_functiondef('api.schule_lernstand(text, jsonb)'::regprocedure);
  if position('''sitzt_am'', k.sitzt_am,' in d) = 0 then raise exception 'Stelle in schule_lernstand nicht gefunden'; end if;
  d := replace(d, '''sitzt_am'', k.sitzt_am,',
    $r$'sitzt_am', k.sitzt_am,
              'knobel_gesamt', (select count(*) from schule.aufgabe a where a.einheit_id = e.id and a.pool = 'bonus' and a.freigegeben and a.variante_gruppe = et->>'lernziel'),
              'knobel_geloest', (select count(*) from schule.aufgabe a where a.einheit_id = e.id and a.pool = 'bonus' and a.variante_gruppe = et->>'lernziel'
                                  and exists (select 1 from schule.versuch v where v.lernender_id = v_l and v.aufgabe_id = a.id and v.richtig)),$r$);
  execute d;

  -- schule.konto: Knobel-Sterne
  d := pg_get_functiondef('schule.konto(bigint)'::regprocedure);
  if position('''lerntage'', (select count(*) from schule.lerntag where lernender_id = p_lernender),' in d) = 0 then raise exception 'Stelle in schule.konto nicht gefunden'; end if;
  d := replace(d, '''lerntage'', (select count(*) from schule.lerntag where lernender_id = p_lernender),',
    $r$'lerntage', (select count(*) from schule.lerntag where lernender_id = p_lernender),
    'knobel_sterne', (select count(*) from schule.sterne where lernender_id = p_lernender and grund = 'bonus'),$r$);
  execute d;

  -- api.schule_konto: „Knobeln des Tages“ aus einer sitzenden Etappe (heute fest gewählt; null, wenn heute schon geknobelt)
  d := pg_get_functiondef('api.schule_konto(text, jsonb)'::regprocedure);
  if position('''look'', (select jsonb_build_object(''stil'', stil, ''welt'', welt) from schule.lernender where id = v_l),' in d) = 0 then raise exception 'Stelle in api.schule_konto nicht gefunden'; end if;
  d := replace(d, '''look'', (select jsonb_build_object(''stil'', stil, ''welt'', welt) from schule.lernender where id = v_l),',
    $r$'knobel_tag', case when not exists (select 1 from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                                           where v.lernender_id = v_l and a.pool = 'bonus' and v.am::date = current_date) then
      (select schule.aufgabe_anzeige(a, true) || jsonb_build_object('einheit_id', a.einheit_id, 'stadt', b.stadt,
                'etappe', (select et->>'titel' from jsonb_array_elements(e.inhalt->'etappen') et where et->>'lernziel' = a.variante_gruppe limit 1))
         from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id join schule.block b on b.id = e.block_id
         join schule.karte_stand k on k.lernender_id = v_l and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe and k.sitzt
        where a.pool = 'bonus' and a.freigegeben and e.status in ('geprueft', 'freigegeben')
          and not exists (select 1 from schule.versuch v where v.lernender_id = v_l and v.aufgabe_id = a.id)
        order by md5(current_date::text || a.id::text) limit 1) end,
    'look', (select jsonb_build_object('stil', stil, 'welt', welt) from schule.lernender where id = v_l),$r$);
  execute d;
end $$;
