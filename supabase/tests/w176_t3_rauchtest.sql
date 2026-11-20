-- Rauchtest W176 Teil 3 (Mischkarten). Erst NACH 20261118_w176_t3_mischkarten.sql ausführen. Transaktion mit Rollback, nur Testkind.
begin;
do $$
declare v_l bigint; v_e bigint; v_lz text; v_a bigint; j jsonb; k schule.karte_stand; v_n int;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  -- Ausgangslage: keine Etappe gelandet → keine Mischkarten
  update schule.karte_stand set sitzt = false where lernender_id = v_l;
  select einheit_id, variante_gruppe into v_e, v_lz from schule.aufgabe where pool = 'uebung' and freigegeben and stufe in (2, 3) order by id limit 1;
  if jsonb_array_length(schule.mischkarten(v_l, v_e)) <> 0 then raise exception 'FEHLER 1: Mischkarten ohne gelandete Etappe'; end if;
  raise notice 'ok 1: ohne gelandete Etappe keine Mischkarte';
  -- eine Etappe gelandet → nur sie liefert Kandidaten, nur Pool uebung, Stufe 2–3, freigegeben
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) values (v_l, v_e, v_lz) on conflict do nothing;
  update schule.karte_stand set sitzt = true, sitzt_am = now(), wdh_stufe = 1, wdh_fehler = 0, faellig_am = now() + interval '3 days', wdh_ab = now(), wdh_lerntage = 3, misch_ok_am = null
   where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  j := schule.mischkarten(v_l, v_e);
  select count(*) into v_n from jsonb_array_elements(j) x join schule.aufgabe a on a.id = (x->>'id')::bigint
   where not (a.einheit_id = v_e and a.variante_gruppe = v_lz) or a.pool <> 'uebung' or a.stufe not in (2, 3) or not a.freigegeben;
  if jsonb_array_length(j) <> 1 or v_n <> 0 then raise exception 'FEHLER 2: %', j; end if;
  raise notice 'ok 2: nur gelandete Etappen, Pool uebung, Stufe 2–3, freigegeben (quelle %)', j->0->>'quelle';
  v_a := (j->0->>'id')::bigint;
  -- richtig als Mischkarte → Beleg, keine Wiederholungsstufe vorgerückt
  if to_regclass('schule.misch_ausgabe') is not null then -- seit Auftrag I (Teil 2/3) zählt eine Mischkarte nur mit Ausgabe
    execute 'insert into schule.misch_ausgabe(lernender_id, aufgabe_id) values ($1, $2) on conflict do nothing' using v_l, v_a;
  end if;
  perform schule.misch_buchen(v_l, v_a, true, 0::smallint, now());
  select * into k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if k.misch_ok_am is null or k.wdh_stufe <> 1 then raise exception 'FEHLER 3: %', row_to_json(k); end if;
  raise notice 'ok 3: richtig → misch_ok_am gesetzt, Wiederholung unverändert';
  -- falsch als Mischkarte → am nächsten Lerntag fällig, keine Abzüge
  if to_regclass('schule.misch_ausgabe') is not null then -- seit Auftrag I (Teil 2/3) zählt eine Mischkarte nur mit Ausgabe
    execute 'insert into schule.misch_ausgabe(lernender_id, aufgabe_id) values ($1, $2) on conflict do nothing' using v_l, v_a;
  end if;
  perform schule.misch_buchen(v_l, v_a, false, 0::smallint, now());
  select * into k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if not k.sitzt or k.wdh_fehler <> 0 or k.wdh_lerntage <> 1 then raise exception 'FEHLER 4: %', row_to_json(k); end if; -- seit H8: Fehler in Mischkarte macht nur fällig, wdh_fehler bleibt
  raise notice 'ok 4: falsch → fällig am nächsten Lerntag (wdh_lerntage 1), wdh_fehler bleibt 0 (H8), Etappe bleibt gelandet, eigene Lösungen % unverändert', k.eigene_loesungen;
  -- Trigger: Versuch mit misch = true bucht über misch_buchen
  if to_regclass('schule.misch_ausgabe') is not null then -- seit Auftrag I (Teil 2/3) zählt eine Mischkarte nur mit Ausgabe
    execute 'insert into schule.misch_ausgabe(lernender_id, aufgabe_id) values ($1, $2) on conflict do nothing' using v_l, v_a;
  end if;
  insert into schule.versuch(lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf, misch)
  values (v_l, v_a, 'rauchtest-misch-' || gen_random_uuid(), '{}'::jsonb, true, 1, 1, 0, 1, 1, true);
  raise notice 'ok 5: Versuch mit misch = true angenommen';
  -- Knobel-Bordkarten und gesperrte Aufgaben nie als Mischkarte
  select count(*) into v_n from jsonb_array_elements(schule.mischkarten(v_l, v_e, 50)) x join schule.aufgabe a on a.id = (x->>'id')::bigint where a.pool <> 'uebung' or not a.freigegeben;
  if v_n <> 0 then raise exception 'FEHLER 6'; end if;
  raise notice 'ok 6: keine Knobel- oder gesperrten Bordkarten';
end $$;
rollback;
