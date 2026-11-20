-- Rauchtest Bau-Auftrag I, Teil 3 (Nachprüfung ChatGPT 878). Nach 20261120_i2_lernregeln.sql und 20261120_i3_lernregeln_nachpruefung.sql ausführen.
-- Transaktion mit Rollback, nur Testkind, keine Namen. Legt Karten-Stände, Versuche und Ausgaben selbst an; aus der Datenbank kommen nur Inhalte.
-- Weg: schule.uebung_pruefen_intern (dahinter Trigger versuch_karte), schule.einheit_lesen_intern, schule.test_starten_intern, schule.offene_entscheiden,
-- schule.mischkarten, schule.misch_buchen, schule.misch_gueltig. Der äußere Zugang (api.*, Schlüssel) ist hier nicht getestet.
-- Echte Gleichzeitigkeit (zwei Tabs) lässt sich in einem Rauchtest nicht erzeugen; geprüft wird, dass zweimaliges Entscheiden derselben Zeile einmal bucht.
begin;
do $$
declare v_l bigint; v_e1 bigint; v_lz1 text; v_e2 bigint; v_lz2 text; v_e3 bigint; v_lz3 text; v_ids1 bigint[]; v_ids3 bigint[]; v_ag schule.aufgabe;
  r jsonb; j jsonb; v_ks schule.karte_stand; v_n int; v_falsch_vorher int; v_ok boolean; v_pid bigint; v_fx jsonb; v_lage schule.misch_ausgabe;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  update schule.karte_stand set sitzt = false where lernender_id = v_l;
  update schule.misch_ausgabe set eingeloest_am = now() where lernender_id = v_l and eingeloest_am is null;
  update schule.versuch set wertung_offen = false where lernender_id = v_l and wertung_offen; -- Ausgangslage: nichts offen

  select a.einheit_id, a.variante_gruppe into v_e1, v_lz1 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
   where a.pool = 'uebung' and a.freigegeben and a.antworttyp = 'auswahl' and a.stufe in (2, 3) and e.status = 'freigegeben'
   group by 1, 2 having count(*) >= 3 order by 1, 2 limit 1;
  select a.einheit_id, a.variante_gruppe into v_e2, v_lz2 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
   where a.pool = 'uebung' and a.freigegeben and e.status = 'freigegeben' and a.einheit_id <> v_e1
   group by 1, 2 order by 1, 2 limit 1;
  select a.einheit_id, a.variante_gruppe into v_e3, v_lz3 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
   where a.pool = 'uebung' and a.freigegeben and a.antworttyp = 'auswahl' and e.status = 'freigegeben' and a.einheit_id not in (v_e1, v_e2)
     and (select count(*) from jsonb_array_elements(coalesce(a.antworten, '[]'::jsonb))) >= 3
   group by 1, 2 having count(*) >= 4 order by 1, 2 limit 1;
  if v_e1 is null or v_e2 is null or v_e3 is null then raise exception 'FEHLER: keine passenden Etappen'; end if;
  select array_agg(id order by id) into v_ids1 from schule.aufgabe where einheit_id = v_e1 and variante_gruppe = v_lz1 and pool = 'uebung' and freigegeben and antworttyp = 'auswahl' and stufe in (2, 3);
  select array_agg(id order by id) into v_ids3 from schule.aufgabe where einheit_id = v_e3 and variante_gruppe = v_lz3 and pool = 'uebung' and freigegeben and antworttyp = 'auswahl'
     and (select count(*) from jsonb_array_elements(coalesce(antworten, '[]'::jsonb))) >= 3;
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) values (v_l, v_e1, v_lz1), (v_l, v_e3, v_lz3) on conflict do nothing;
  update schule.karte_stand set sitzt = false, sitzt_am = null, eigene_loesungen = 0, serie = 0, typen = '{}', schwer_ok = false, folge = 0, fehler_folge = 0, gezaehlt = '{}', geoeffnet_am = null
   where lernender_id = v_l and einheit_id = v_e3 and lernziel = v_lz3;

  -- ---------- Muss 1: endgültige Wertung bleibt (genau der Fall aus 878) ----------
  for v_n in 1..2 loop
    select * into v_ag from schule.aufgabe where id = v_ids3[v_n];
    perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i3-1r' || v_n, 'antwort', v_ag.loesung, 'anlauf', 1));
  end loop;
  select * into v_ag from schule.aufgabe where id = v_ids3[3];
  v_fx := jsonb_build_object('index', ((v_ag.loesung->>'index')::int + 1) % jsonb_array_length(v_ag.antworten));
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i3-1x1', 'antwort', v_fx, 'anlauf', 1));      -- X 1. Anlauf falsch
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ids3[4], 'client_id', 'i3-1y', 'antwort', (select loesung from schule.aufgabe where id = v_ids3[4]), 'anlauf', 1)); -- Y richtig
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i3-1x2', 'antwort', v_ag.loesung, 'anlauf', 2)); -- X 2. Anlauf doch noch richtig
  select * into v_ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e3 and lernziel = v_lz3;
  if v_ks.folge <> 1 or schule.folge_nachrechnen(v_l, v_e3, v_lz3, now() - interval '1 millisecond') <> 1
     or (select wertung_fest from schule.versuch where lernender_id = v_l and client_id = 'i3-1x1') <> 'falsch'
     or (select wertung_fest from schule.versuch where lernender_id = v_l and client_id = 'i3-1x2') <> 'neutral' then
    raise exception 'FEHLER M1a: Buchung %, Nachrechnung %', v_ks.folge, schule.folge_nachrechnen(v_l, v_e3, v_lz3, now() - interval '1 millisecond'); end if;
  raise notice 'ok M1a: 2 richtig, X falsch (1. Anlauf), Y richtig, X im 2. Anlauf richtig → Buchung 1 = Nachrechnung 1 (vorher 1 ≠ 3); X bleibt „falsch“, der 2. Anlauf „neutral“';
  -- Gegenstück: der späte 2. Anlauf ist falsch → bucht keinen zweiten Fehler
  v_falsch_vorher := v_ks.falsch;
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ids3[1], 'client_id', 'i3-1z1', 'antwort',
     jsonb_build_object('index', ((select loesung->>'index' from schule.aufgabe where id = v_ids3[1])::int + 1) % (select jsonb_array_length(antworten) from schule.aufgabe where id = v_ids3[1])), 'anlauf', 1));
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ids3[2], 'client_id', 'i3-1w', 'antwort', (select loesung from schule.aufgabe where id = v_ids3[2]), 'anlauf', 1));
  select * into v_ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e3 and lernziel = v_lz3;
  v_n := v_ks.folge; v_falsch_vorher := v_ks.falsch;
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ids3[1], 'client_id', 'i3-1z2', 'antwort',
     jsonb_build_object('index', ((select loesung->>'index' from schule.aufgabe where id = v_ids3[1])::int + 1) % (select jsonb_array_length(antworten) from schule.aufgabe where id = v_ids3[1])), 'anlauf', 2));
  select * into v_ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e3 and lernziel = v_lz3;
  if v_ks.folge <> v_n or v_ks.falsch <> v_falsch_vorher or schule.folge_nachrechnen(v_l, v_e3, v_lz3, now() - interval '1 millisecond') <> v_ks.folge then
    raise exception 'FEHLER M1b: später falscher 2. Anlauf hat gebucht (folge % → %)', v_n, v_ks.folge; end if;
  raise notice 'ok M1b: später falscher 2. Anlauf nach endgültigem Fehler bucht nichts; Buchung = Nachrechnung (%)', v_ks.folge;

  -- ---------- Muss 2: Nachbuchen genau einmal ----------
  select * into v_ag from schule.aufgabe where id = v_ids3[2];
  v_fx := jsonb_build_object('index', ((v_ag.loesung->>'index')::int + 1) % jsonb_array_length(v_ag.antworten));
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i3-2p', 'antwort', v_fx, 'anlauf', 1));
  select id into v_pid from schule.versuch where lernender_id = v_l and client_id = 'i3-2p';
  update schule.versuch set am = am - interval '31 minutes' where id = v_pid; -- Zeit abgelaufen
  select falsch into v_falsch_vorher from schule.karte_stand where lernender_id = v_l and einheit_id = v_e3 and lernziel = v_lz3;
  if schule.offene_entscheiden(v_l) <> 1 or schule.offene_entscheiden(v_l) <> 0 then raise exception 'FEHLER M2a: nicht genau einmal entschieden'; end if;
  if (select falsch from schule.karte_stand where lernender_id = v_l and einheit_id = v_e3 and lernziel = v_lz3) <> v_falsch_vorher + 1
     or (select wertung_offen from schule.versuch where id = v_pid) or (select wertung_fest from schule.versuch where id = v_pid) <> 'falsch' then
    raise exception 'FEHLER M2b: Fehler nicht genau einmal gebucht'; end if;
  raise notice 'ok M2: zweimal entschieden → einmal gebucht (falsch +1, wertung_offen = false, wertung_fest = falsch)';

  -- ---------- Sollte 5: abgelaufene erste Anläufe beim Lesen des Flugs und beim Teststart ----------
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i3-5a', 'antwort', v_fx, 'anlauf', 1));
  update schule.versuch set am = am - interval '31 minutes' where lernender_id = v_l and client_id = 'i3-5a';
  perform schule.einheit_lesen_intern(v_l, v_e3);
  if (select wertung_offen or wertung_fest is distinct from 'falsch' from schule.versuch where lernender_id = v_l and client_id = 'i3-5a') then raise exception 'FEHLER S5a: beim Lesen nicht entschieden'; end if;
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i3-5b', 'antwort', v_fx, 'anlauf', 1));
  update schule.versuch set am = am - interval '31 minutes' where lernender_id = v_l and client_id = 'i3-5b';
  perform schule.test_starten_intern(v_l, jsonb_build_object('einheit_id', v_e3, 'art', 'korrektur'));
  if (select wertung_offen or wertung_fest is distinct from 'falsch' from schule.versuch where lernender_id = v_l and client_id = 'i3-5b') then raise exception 'FEHLER S5b: beim Teststart nicht entschieden'; end if;
  -- noch nicht abgelaufen → bleibt offen
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i3-5c', 'antwort', v_fx, 'anlauf', 1));
  perform schule.einheit_lesen_intern(v_l, v_e3);
  if not (select wertung_offen from schule.versuch where lernender_id = v_l and client_id = 'i3-5c') then raise exception 'FEHLER S5c: frischer erster Anlauf zu früh entschieden'; end if;
  update schule.versuch set wertung_offen = false where lernender_id = v_l and client_id = 'i3-5c';
  raise notice 'ok S5: über 30 Minuten alte erste Anläufe werden beim Lesen des Flugs und beim Teststart entschieden, frische nicht';

  -- ---------- Sollte 3: Einlösen atomar, eindeutig, konfliktfest ----------
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '2 days', misch_ok_am = null, wdh_stufe = 1, wdh_fehler = 0 where lernender_id = v_l and einheit_id = v_e1 and lernziel = v_lz1;
  perform schule.misch_buchen(v_l, v_ids1[1], true, 0::smallint, now()); -- ohne Ausgabe
  select * into v_ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e1 and lernziel = v_lz1;
  if v_ks.misch_ok_am is not null then raise exception 'FEHLER S3a: Beleg ohne Ausgabe'; end if;
  -- LB-3 Nachbesserung, Sollte 7: unabhängig vom Zufall der Kartenauswahl – eine schon vorhandene (auch verfallene) offene Ausgabe wird übernommen
  insert into schule.misch_ausgabe(lernender_id, aufgabe_id) values (v_l, v_ids1[1])
  on conflict (lernender_id, aufgabe_id) where eingeloest_am is null do update set ausgegeben_am = now(), verfallen_am = null, einheit_id = null, lernziel = null;
  v_ok := false;
  begin
    insert into schule.misch_ausgabe(lernender_id, aufgabe_id) values (v_l, v_ids1[1]);
  exception when unique_violation then v_ok := true;
  end;
  if not v_ok then raise exception 'FEHLER S3b: zweite offene Ausgabe derselben Bordkarte angenommen'; end if;
  perform schule.misch_buchen(v_l, v_ids1[1], true, 0::smallint, now());
  if (select misch_ok_am from schule.karte_stand where lernender_id = v_l and einheit_id = v_e1 and lernziel = v_lz1) is null
     or exists (select 1 from schule.misch_ausgabe where lernender_id = v_l and aufgabe_id = v_ids1[1] and eingeloest_am is null) then raise exception 'FEHLER S3c: Einlösen mit Ausgabe'; end if;
  -- seit I-4: zweimal ausliefern gibt dieselben Karten wieder aus (unabhängig davon, wie viele Etappen das Testkind gelandet hat)
  j := schule.mischkarten(v_l, v_e2); r := schule.mischkarten(v_l, v_e2);
  select count(*) into v_n from schule.misch_ausgabe where lernender_id = v_l and eingeloest_am is null and verfallen_am is null;
  if jsonb_array_length(j) < 1 or v_n <> jsonb_array_length(r)
     or (select array_agg((x->>'id')::bigint order by (x->>'id')::bigint) from jsonb_array_elements(j) x) is distinct from (select array_agg((x->>'id')::bigint order by (x->>'id')::bigint) from jsonb_array_elements(r) x)
  then raise exception 'FEHLER S3d: % / % Karten, % offene Ausgaben nach zweimal Ausliefern', jsonb_array_length(j), jsonb_array_length(r), v_n; end if;
  raise notice 'ok S3: ohne Ausgabe kein Beleg (normale Buchung); höchstens eine offene Ausgabe je Bordkarte; zweimal ausgeliefert → dieselben Karten, keine neuen Ausgaben';

  -- ---------- Sollte 4: Ausgabe an die Lage gebunden ----------
  select * into v_lage from schule.misch_ausgabe where lernender_id = v_l and eingeloest_am is null and verfallen_am is null and einheit_id = v_e2 order by id limit 1;
  if v_lage.einheit_id is distinct from v_e2 then raise exception 'FEHLER S4a: Lage nicht gespeichert: %', row_to_json(v_lage); end if;
  select * into v_ag from schule.aufgabe where id = v_lage.aufgabe_id;
  -- Gerät behauptet, gerade genau diese Etappe zu üben – zählt trotzdem, weil der Server die Lage (Flug %) kennt
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i3-4a', 'antwort', v_ag.loesung, 'misch', true, 'aktuell_einheit', v_ag.einheit_id, 'aktuell_lernziel', v_ag.variante_gruppe));
  if not (select misch from schule.versuch where lernender_id = v_l and client_id = 'i3-4a') then raise exception 'FEHLER S4b: Geräte-Angabe statt gespeicherter Lage geprüft'; end if;
  -- gespeicherte Lage = Etappe der Karte selbst → keine Mischkarte, auch wenn das Gerät etwas anderes sagt
  insert into schule.misch_ausgabe(lernender_id, aufgabe_id, einheit_id, lernziel) values (v_l, v_ag.id, v_ag.einheit_id, v_ag.variante_gruppe)
  on conflict (lernender_id, aufgabe_id) where eingeloest_am is null do update set ausgegeben_am = now(), verfallen_am = null, einheit_id = excluded.einheit_id, lernziel = excluded.lernziel;
  if schule.misch_gueltig(v_l, v_ag, jsonb_build_object('misch', true, 'aktuell_einheit', v_e2, 'aktuell_lernziel', v_lz2)) then raise exception 'FEHLER S4c: Lage der Karte selbst gewertet'; end if;
  raise notice 'ok S4: Ausgabe merkt Flug % und Etappe %; misch_gueltig prüft die gespeicherte Lage, nicht die Angaben des Geräts', v_lage.einheit_id, coalesce(v_lage.lernziel, '(alle gelandet)');
end $$;
rollback;
