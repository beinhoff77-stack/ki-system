-- Rauchtest: einheit_abgleichen(…, 'sperren') lässt Expeditions-Teile unberührt. Nach 20261119_abgleich_ohne_expeditionen.sql ausführen. Rollback, keine Namen.
-- Vor der Migration schlägt Schritt 2 fehl (FEHLER 2) – so lässt sich der Fehler auch nachweisen.
begin;
do $$
declare v_e bigint; v_x bigint; datei jsonb; r jsonb; v_teile int; v_frei int; v_uebung_frei int;
begin
  -- ein Flug, an dem freigegebene Expeditions-Teile hängen
  select a.einheit_id into v_e from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
   where a.pool = 'expedition' and a.freigegeben and e.status <> 'ersetzt' and jsonb_array_length(coalesce(e.inhalt->'etappen', '[]'::jsonb)) >= 3
     and e.id = (select e2.id from schule.einheit e2 where e2.thema_id = e.thema_id and e2.status <> 'ersetzt' order by e2.version desc limit 1) -- die Einheit, die der Abgleich trifft
   order by a.einheit_id limit 1;
  if v_e is null then raise exception 'FEHLER Vorbedingung: kein Flug mit freigegebenen Expeditions-Teilen'; end if;
  select count(*), count(*) filter (where freigegeben) into v_teile, v_frei from schule.aufgabe where einheit_id = v_e and pool = 'expedition';
  select count(*) into v_uebung_frei from schule.aufgabe where einheit_id = v_e and pool <> 'expedition' and freigegeben;
  -- Themendatei aus dem Stand der Datenbank: alle Aufgaben außer den Expeditions-Teilen (so steht es in inhalte/themen/*.json)
  select jsonb_build_object('thema_id', t.id, 'thema_schluessel', t.schluessel, 'inhalt', e.inhalt,
           'aufgaben', (select coalesce(jsonb_agg(o.j order by o.r), '[]'::jsonb) from (
                          select a.reihenfolge r, (select jsonb_object_agg(kv.key, kv.value) from jsonb_each(jsonb_build_object('f', a.frage, 'a', a.antworten, 'o', a.loesung, 'h', a.tipp,
                                   'w', a.loesungsweg, 's', a.stufe, 'l', a.variante_gruppe, 't', a.teilfaehigkeit, 'p', a.pool, 'g', a.typ, 'y', a.antworttyp)) kv
                                  where kv.value <> 'null'::jsonb) j -- nur oberste Ebene ohne null (wie in der Datei), Frage/Lösung unverändert
                            from schule.aufgabe a where a.einheit_id = e.id and a.pool <> 'expedition') o))
    into datei from schule.einheit e join schule.thema t on t.id = e.thema_id where e.id = v_e;
  -- 1. Abgleich mit „sperren“
  r := schule.einheit_abgleichen(datei, 'sperren');
  if (r->>'einheit_id')::bigint <> v_e or (r->>'aufgaben_neu')::int <> 0 then raise exception 'FEHLER 1: falsche Einheit oder Datei nicht erkannt: %', r; end if;
  -- 2. Expeditions-Teile unverändert freigegeben, nicht als „nicht mehr in der Datei“ gezählt
  if (select count(*) filter (where freigegeben) from schule.aufgabe where einheit_id = v_e and pool = 'expedition') <> v_frei then
    raise exception 'FEHLER 2: Expeditions-Teile gesperrt (vorher % frei, Antwort %)', v_frei, r; end if;
  if (r->>'nicht_mehr_in_datei')::int <> 0 then raise exception 'FEHLER 3: Expeditions-Teile als fehlend gezählt: %', r; end if;
  if (select count(*) from schule.aufgabe where einheit_id = v_e and pool = 'expedition') <> v_teile then raise exception 'FEHLER 4: Zahl der Teile geändert'; end if;
  raise notice 'ok 1–4: % Expeditions-Teile (davon % freigegeben) bleiben unberührt; nicht mehr in der Datei: %', v_teile, v_frei, r->>'nicht_mehr_in_datei';
  -- 5. Gegenprobe: eine Übung fehlt in der Datei → sie wird gesperrt, die Expeditions-Teile nicht
  if jsonb_array_length(datei->'aufgaben') > 0 then
    r := schule.einheit_abgleichen(jsonb_set(datei, '{aufgaben}', (datei->'aufgaben') - 0), 'sperren');
    if (r->>'nicht_mehr_in_datei')::int <> 1 then raise exception 'FEHLER 5: erwartet 1 fehlende Übung, Antwort %', r; end if;
    if (select count(*) filter (where freigegeben) from schule.aufgabe where einheit_id = v_e and pool = 'expedition') <> v_frei then raise exception 'FEHLER 6: Gegenprobe sperrt Expeditions-Teile'; end if;
    raise notice 'ok 5–6: fehlende Übung gesperrt (Übungen frei vorher %, jetzt %), Expeditions-Teile weiter frei',
      v_uebung_frei, (select count(*) from schule.aufgabe where einheit_id = v_e and pool <> 'expedition' and freigegeben);
  end if;
end $$;
rollback;
