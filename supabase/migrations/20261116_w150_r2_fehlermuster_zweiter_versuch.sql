-- W150 Rückmeldung & Lernweg, Paket R2 (inhalte/pruefung/rueckmeldung/umsetzung.md):
-- V3: antwort_bewerten erkennt Fehlermuster (grund: vorzeichen, komma, vertauscht, gerundet; falsche_einheit gab es schon), uebung_pruefen_intern gibt grund weiter.
-- V2: zweiter Versuch vor der Lösung. Die App schickt anlauf = 1 (erster Versuch) bzw. 2. Bei falsch im 1. Anlauf kommt keine Lösung zurück
--     und die Lernkarte wird nicht gebucht (Serie bleibt). Im 2. Anlauf zählt eine richtige Antwort wie „mit Hilfe“: Die Serie steigt nicht.
--     Ohne anlauf (Wiederholen, ältere App) bleibt alles wie bisher.
alter table schule.versuch add column if not exists anlauf smallint;
comment on column schule.versuch.anlauf is '1 = erster Versuch mit zweiter Chance (bei falsch keine Buchung auf die Lernkarte), 2 = zweiter Versuch, null = ohne zweite Chance';

create or replace function schule.versuch_karte() returns trigger language plpgsql set search_path to '' as $function$
begin
  if new.testsitzung_id is null and not (coalesce(new.anlauf, 0) = 1 and not new.richtig) then
    perform schule.karte_buchen(new.lernender_id, new.aufgabe_id, new.richtig, new.hilfe, now());
  end if;
  return new;
end $function$;

create or replace function schule.antwort_bewerten(p_aufgabe schule.aufgabe, p_antwort jsonb)
 returns jsonb
 language plpgsql
 immutable
 set search_path to ''
as $function$
declare s text; e text; n int; v numeric; w numeric; tol numeric; i int; v_soll jsonb; v_ok boolean := true; v_grund text;
  v_ant numeric[] := '{}'; v_sol numeric[] := '{}';
begin
  if p_aufgabe.antworttyp = 'luecken' then
    v_soll := p_aufgabe.loesung->'werte';
    if jsonb_typeof(p_antwort->'werte') is distinct from 'array' or jsonb_array_length(p_antwort->'werte') <> jsonb_array_length(v_soll) then
      return jsonb_build_object('format_ok', false, 'hinweis', 'Bitte fülle alle Felder aus.');
    end if;
    for i in 0 .. jsonb_array_length(v_soll) - 1 loop
      s := regexp_replace(coalesce(p_antwort->'werte'->>i, ''), '[\s  ]', '', 'g');
      s := replace(replace(s, '−', '-'), '–', '-');
      if left(s, 1) = '+' then s := substr(s, 2); end if;
      if s = '' then return jsonb_build_object('format_ok', false, 'hinweis', 'Bitte fülle alle Felder aus. Fehlt ein Glied, trage 0 ein.'); end if;
      if position('.' in s) > 0 or position(',' in s) > 0 then
        return jsonb_build_object('format_ok', false, 'hinweis', 'In jedes Feld gehört eine ganze Zahl mit Vorzeichen, zum Beispiel −3.');
      end if;
      if s !~ '^-?\d+$' then return jsonb_build_object('format_ok', false, 'hinweis', 'In jedes Feld gehört eine ganze Zahl mit Vorzeichen, zum Beispiel −3.'); end if;
      if s::numeric <> (v_soll->>i)::numeric then v_ok := false; end if;
      v_ant := v_ant || s::numeric; v_sol := v_sol || (v_soll->>i)::numeric;
    end loop;
    if v_ok then return jsonb_build_object('format_ok', true, 'richtig', true); end if;
    -- Fehlermuster: richtige Zahlen in falscher Reihenfolge; oder nur Vorzeichen falsch
    if (select array_agg(x order by x) from unnest(v_ant) x) = (select array_agg(x order by x) from unnest(v_sol) x) then v_grund := 'vertauscht';
    elsif (select bool_and(abs(a.x) = abs(b.x)) from unnest(v_ant) with ordinality a(x, o) join unnest(v_sol) with ordinality b(x, o) using (o)) then v_grund := 'vorzeichen';
    end if;
    return jsonb_strip_nulls(jsonb_build_object('format_ok', true, 'richtig', false, 'grund', v_grund));
  end if;

  if p_aufgabe.antworttyp in ('auswahl','markierung') then
    if coalesce(p_antwort->>'index','') !~ '^\d+$' then
      return jsonb_build_object('format_ok', false, 'hinweis', 'Bitte wähle eine Antwort aus.');
    end if;
    n := (p_antwort->>'index')::int;
    if p_aufgabe.antworttyp = 'auswahl' and n >= jsonb_array_length(p_aufgabe.antworten) then
      return jsonb_build_object('format_ok', false, 'hinweis', 'Bitte wähle eine Antwort aus.');
    end if;
    if p_aufgabe.antworttyp = 'markierung' and n > coalesce((p_aufgabe.frage->'grafik'->>'abschnitte')::int, 0) then
      return jsonb_build_object('format_ok', false, 'hinweis', 'Bitte tippe eine Markierung an.');
    end if;
    return jsonb_build_object('format_ok', true, 'richtig', n = (p_aufgabe.loesung->>'index')::int);
  end if;

  s := regexp_replace(coalesce(p_antwort->>'wert',''), '[\s  ]', '', 'g');
  if s = '' then
    return jsonb_build_object('format_ok', false, 'hinweis', 'Bitte gib eine Antwort ein.');
  end if;
  if p_aufgabe.antworttyp = 'text' then
    return jsonb_build_object('format_ok', true, 'richtig', upper(s) = upper(p_aufgabe.loesung->>'text'));
  end if;
  if position('.' in s) > 0 then
    return jsonb_build_object('format_ok', false, 'hinweis', 'Bitte schreibe Dezimalzahlen mit Komma und Tausender mit Leerzeichen, zum Beispiel 4,5 oder 1 200.');
  end if;
  e := p_aufgabe.loesung->>'einheit';
  if e = '€' and position('%' in s) > 0 then return jsonb_build_object('format_ok', true, 'richtig', false, 'grund', 'falsche_einheit'); end if;
  if e = '%' and position('€' in s) > 0 then return jsonb_build_object('format_ok', true, 'richtig', false, 'grund', 'falsche_einheit'); end if;
  if e is not null then s := replace(s, e, ''); end if;
  s := replace(replace(s, '−', '-'), ',', '.');
  if s !~ '^-?\d+(\.\d+)?$' then
    return jsonb_build_object('format_ok', false, 'hinweis', 'Bitte gib nur die Zahl ein.');
  end if;
  v := s::numeric; w := (p_aufgabe.loesung->>'wert')::numeric;
  tol := greatest(1e-9, coalesce((p_aufgabe.loesung->>'toleranz')::numeric, 0));
  if abs(v - w) <= tol then return jsonb_build_object('format_ok', true, 'richtig', true); end if;
  -- Fehlermuster bei Zahlen: Vorzeichen, Komma verrutscht (Faktor 10/100/1000), gerundet (±1 % oder auf weniger Stellen gerundet)
  if abs(abs(v) - abs(w)) <= tol then v_grund := 'vorzeichen';
  elsif v <> 0 and w <> 0 and (v / w) in (10, 100, 1000, 0.1, 0.01, 0.001) then v_grund := 'komma';
  elsif (w <> 0 and abs(v - w) <= abs(w) * 0.01) or (scale(v) < scale(w) and round(w, scale(v)) = v) then v_grund := 'gerundet';
  end if;
  return jsonb_strip_nulls(jsonb_build_object('format_ok', true, 'richtig', false, 'grund', v_grund));
end $function$;

create or replace function schule.uebung_pruefen_intern(p_lernender bigint, p_daten jsonb)
 returns jsonb
 language plpgsql
 set search_path to ''
as $function$
declare a schule.aufgabe; b jsonb; v_cid text := coalesce(nullif(p_daten->>'client_id',''), 'srv:' || gen_random_uuid()); v_alt schule.versuch;
  v_anlauf smallint := case p_daten->>'anlauf' when '1' then 1 when '2' then 2 end; v_ri boolean;
  v_hilfe smallint := least(greatest(coalesce((p_daten->>'hilfe')::smallint, 0), 0), 2);
begin
  select * into a from schule.aufgabe where id = (p_daten->>'aufgabe_id')::bigint;
  if a.id is null or a.pool <> 'uebung' then raise exception 'Keine Übungsaufgabe' using errcode = 'P0001'; end if;
  if not a.freigegeben and not exists (select 1 from schule.lernender l where l.id = p_lernender and l.ist_test) then
    raise exception 'Diese Aufgabe ist noch nicht freigegeben' using errcode = 'P0001';
  end if;
  if p_daten ? 'client_id' then
    select * into v_alt from schule.versuch where lernender_id = p_lernender and client_id = v_cid;
    if v_alt.id is not null then
      if coalesce(v_alt.anlauf, 0) = 1 and not v_alt.richtig then
        return jsonb_build_object('ok', true, 'format_ok', true, 'richtig', false, 'nochmal', true, 'wiederholt', true);
      end if;
      return jsonb_build_object('ok', true, 'format_ok', true, 'richtig', v_alt.richtig, 'loesung', a.loesung, 'loesungsweg', a.loesungsweg, 'wiederholt', true);
    end if;
  end if;
  b := schule.antwort_bewerten(a, p_daten->'antwort');
  if not (b->>'format_ok')::boolean then
    return jsonb_build_object('ok', true, 'format_ok', false, 'hinweis', b->>'hinweis');
  end if;
  v_ri := (b->>'richtig')::boolean;
  if v_anlauf = 2 then v_hilfe := greatest(v_hilfe, 1::smallint); end if; -- richtig im 2. Versuch: Serie steigt nicht
  insert into schule.versuch(lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf)
  values (p_lernender, a.id, v_cid, p_daten->'antwort', v_ri, case when v_ri then 1 else 0 end, 1, v_hilfe,
          (select count(*) + 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id), v_anlauf);
  if v_anlauf = 1 and not v_ri then
    -- erster Fehlversuch: keine Lösung, nur das erkannte Fehlermuster; das Kind darf noch einmal
    return jsonb_strip_nulls(jsonb_build_object('ok', true, 'format_ok', true, 'richtig', false, 'nochmal', true, 'grund', b->>'grund'));
  end if;
  return jsonb_strip_nulls(jsonb_build_object('ok', true, 'format_ok', true, 'richtig', v_ri, 'grund', b->>'grund', 'loesung', a.loesung, 'loesungsweg', a.loesungsweg,
    'karte', (select jsonb_build_object('serie', k.serie, 'ziel', schule.karte_ziel(k.einheit_id, k.lernziel), 'sitzt', k.sitzt,
                'neu_sitzt', k.sitzt and k.sitzt_am >= now() - interval '5 seconds' and k.wdh_stufe = 0, 'wdh_stufe', k.wdh_stufe)
              from schule.karte_stand k where k.lernender_id = p_lernender and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe)));
end $function$;
