-- Rauchtest „gesperrt nach dem Laden“ (18.11.). Erst NACH 20261118_w176_a_gesperrt_pruefen.sql ausführen. Transaktion mit Rollback – es bleibt nichts zurück. Keine Namen.
begin;
do $$
declare v_l bigint; v_a bigint; v_e bigint; r jsonb;
begin
  select id into v_l from schule.lernender where not ist_test and aktiv order by id limit 1;
  -- eine gesperrte Übung in einem freigegebenen Flug
  select a.id into v_a from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
   where a.pool = 'uebung' and not a.freigegeben and e.status = 'freigegeben' and a.antworttyp = 'zahl' order by a.id limit 1;
  if v_l is null or v_a is null then raise notice 'übersprungen: kein Kind oder keine gesperrte Übung'; return; end if;
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_a, 'antwort', jsonb_build_object('wert', '0'), 'client_id', 'rauchtest-gesperrt'));
  if not coalesce((r->>'ok')::boolean, false) then raise exception 'FEHLER 1: %', r; end if;
  raise notice 'ok 1: gesperrte Übung in freigegebenem Flug wird gewertet (richtig = %)', r->>'richtig';
  -- gesperrte Übung in einem Entwurfs-Flug: für ein echtes Kind weiter gesperrt
  select a.id into v_e from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id where a.pool = 'uebung' and not a.freigegeben and e.status = 'entwurf' order by a.id limit 1;
  if v_e is not null then
    begin
      perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_e, 'antwort', jsonb_build_object('wert', '0'), 'client_id', 'rauchtest-entwurf'));
      raise exception 'FEHLER 2: Entwurf für echtes Kind gewertet';
    exception when sqlstate 'P0001' then raise notice 'ok 2: gesperrte Übung im Entwurf bleibt für echte Kinder gesperrt';
    end;
  end if;
end $$;
rollback;
