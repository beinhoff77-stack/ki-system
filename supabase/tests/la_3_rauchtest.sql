-- Rauchtest LA-3 („Besprochen ✓“, Fehlerarten). Nach 20261119_la_3_besprochen.sql ausführen. Rollback, nur Testkind, keine Namen.
begin;
do $$
declare v_l bigint; v_e bigint; v_lz text; v_a bigint; bs schule.besprochen; j jsonb;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  select einheit_id, variante_gruppe, id into v_e, v_lz, v_a from schule.aufgabe where pool = 'uebung' and freigegeben and antworttyp = 'zahl' order by id limit 1;
  insert into schule.besprochen(lernender_id, einheit_id, lernziel, von, am) values (v_l, v_e, v_lz, 'lehrer:Test', now() - interval '1 minute');
  bs := schule.besprochen_aktiv(v_l, v_e, v_lz);
  if bs.am is null then raise exception 'FEHLER 1: besprochen nicht aktiv'; end if;
  -- erster Versuch falsch mit zweiter Chance: holt nicht zurück
  insert into schule.versuch(lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf)
    values (v_l, v_a, 'la3-1', '{"wert": "-1"}', false, 0, 1, 0, 1, 1);
  if (schule.besprochen_aktiv(v_l, v_e, v_lz)).am is null then raise exception 'FEHLER 2: 1. Versuch hat zurückgeholt'; end if;
  -- endgültig falsch: holt zurück
  insert into schule.versuch(lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf)
    values (v_l, v_a, 'la3-2', '{"wert": "-1"}', false, 0, 1, 1, 2, 2);
  if (schule.besprochen_aktiv(v_l, v_e, v_lz)).am is not null then raise exception 'FEHLER 3: neue falsche Antwort holt nicht zurück'; end if;
  raise notice 'ok 1–3: besprochen gilt bis zur nächsten endgültig falschen Antwort';
  j := schule.fehler_gruende(v_l, v_e, v_lz);
  if jsonb_typeof(j) <> 'object' then raise exception 'FEHLER 4: %', j; end if;
  raise notice 'ok 4: Fehlerarten je Etappe: %', j;
end $$;
rollback;
