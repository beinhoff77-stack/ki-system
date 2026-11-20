-- Rauchtest LB-3 Nachbesserung (Muss 1–3, Sollte 4–6). Nach 20261120_lb3_nachbesserung.sql ausführen.
-- Transaktion mit Rollback, nur Testkind, keine Namen. Weg: schule.plan_setzen_intern (dahinter flug_wdh_setzen / flug_wdh_zuruecknehmen /
-- karten_wiederherstellen), schule.uebung_pruefen_intern (dahinter karte_buchen), schule.thema_stufe, schule.karte_sicher, schule.einheit_lesen_intern.
-- Aus der Datenbank kommen nur Inhalte (Flüge, Etappen, Bordkarten); Karten-Stände, Tests und Ausgaben legt der Test selbst an.
begin;

create function pg_temp.lbn_eintrag(p_block bigint, p_kw bigint[], p_ks bigint[] default '{}') returns jsonb language sql as $f$
  select jsonb_build_array(jsonb_build_object('block_id', p_block, 'kann_wdh_themen', to_jsonb(p_kw), 'kann_schon_themen', to_jsonb(p_ks), 'ausgelassen', '[]'::jsonb));
$f$;
-- Flüge mit genau einem Ort, mindestens 4 Etappen, je Etappe mindestens 2 freigegebene Auswahl-Bordkarten zum Üben
create function pg_temp.lbn_fluege() returns setof bigint language sql as $f$
  select t.id from schule.thema t
   where schule.thema_einheit(t.id) is not null and (select count(*) from schule.block_thema bt where bt.thema_id = t.id) = 1
     and (select count(*) from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') x where e.id = schule.thema_einheit(t.id)) >= 4
     and not exists (select 1 from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') x where e.id = schule.thema_einheit(t.id)
       and (select count(*) from schule.aufgabe a where a.einheit_id = e.id and a.variante_gruppe = x->>'lernziel' and a.pool = 'uebung' and a.freigegeben
              and a.antworttyp = 'auswahl' and jsonb_array_length(coalesce(a.antworten, '[]'::jsonb)) >= 2) < 2)
   order by t.id;
$f$;
-- n-te Auswahl-Bordkarte einer Etappe und eine falsche Antwort dazu
create function pg_temp.lbn_karte(p_e bigint, p_lz text, p_n int) returns schule.aufgabe language sql as $f$
  select a.* from schule.aufgabe a where a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'uebung' and a.freigegeben and a.antworttyp = 'auswahl'
     and jsonb_array_length(coalesce(a.antworten, '[]'::jsonb)) >= 2 order by a.id offset p_n - 1 limit 1;
$f$;
create function pg_temp.lbn_falsch(a schule.aufgabe) returns jsonb language sql as $f$
  select jsonb_build_object('index', ((a.loesung->>'index')::int + 1) % jsonb_array_length(a.antworten));
$f$;

do $$
declare v_l bigint; v_f bigint[]; v_t1 bigint; v_t2 bigint; v_t3 bigint; v_t4 bigint; v_e bigint; v_b bigint; v_lz text[]; r jsonb; v_s1 bigint; v_s2 bigint;
  v_ks schule.karte_stand; v_a schule.aufgabe; v_ok boolean; v_n int; v_versuche int; v_bis timestamptz; v_tz text;
begin
  select id, zeitzone into v_l, v_tz from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  update schule.misch_ausgabe set eingeloest_am = now() where lernender_id = v_l and eingeloest_am is null;
  update schule.versuch set wertung_offen = false where lernender_id = v_l and wertung_offen;
  select array_agg(x) into v_f from pg_temp.lbn_fluege() x;
  if coalesce(cardinality(v_f), 0) < 4 then raise exception 'FEHLER: nicht genug passende Flüge'; end if;
  v_t1 := v_f[1]; v_t2 := v_f[2]; v_t3 := v_f[3]; v_t4 := v_f[4];
  -- Ausgangslage dieser vier Flüge: nichts begonnen
  update schule.karte_stand set sitzt = false, sitzt_am = null, gesetzt_am = null, gesetzt_von = null, wdh_gesetzt_am = null, wdh_stufe = 0, faellig_am = null, wdh_ab = null,
         wdh_lerntage = null, wdh_fehler = 0, eigene_loesungen = 0, serie = 0, typen = '{}', schwer_ok = false, folge = 0, fehler_folge = 0, gezaehlt = '{}', geoeffnet_am = null, misch_ok_am = null
   where lernender_id = v_l and einheit_id in (select schule.thema_einheit(t) from unnest(v_f[1:4]) t);
  update schule.route set kann_wdh_themen = '{}', kann_schon_themen = array(select a from unnest(kann_schon_themen) a where not (a = any(v_f[1:4])))
   where lernender_id = v_l;

  -- ---------- Muss 1: ganzer Flug vorher sicher → nach dem Setzen ↻, Wiederholung am nächsten Lerntag ----------
  v_e := schule.thema_einheit(v_t1); select block_id into v_b from schule.block_thema where thema_id = v_t1;
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) select v_l, v_e, x->>'lernziel' from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') x where e.id = v_e on conflict do nothing;
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '40 days', wdh_stufe = 4, wdh_ab = now() - interval '2 days', wdh_lerntage = 30,
         faellig_am = now() + interval '28 days', misch_ok_am = now() - interval '1 day', eigene_loesungen = 5 where lernender_id = v_l and einheit_id = v_e;
  perform 1 from schule.testsitzung where false; -- (Flug-Test und Nachtest wie selbst geschafft)
  insert into schule.testsitzung(lernender_id, art, block_id, thema_id, einheit_id, aufgaben, status, punkte, punkte_max, abgeschlossen_am)
  select v_l, 'blocktest', e.block_id, e.thema_id, e.id, '{}', 'abgeschlossen', 1, 1, now() - interval '30 days' from schule.einheit e where e.id = v_e;
  with t as (insert into schule.testsitzung(lernender_id, art, block_id, thema_id, einheit_id, nachtest_runde, aufgaben, status, punkte, punkte_max, ergebnis, abgeschlossen_am)
             select v_l, 'nachtest', e.block_id, e.thema_id, e.id, 1, '{}', 'abgeschlossen', 1, 1, 'bestanden', now() - interval '1 day' from schule.einheit e where e.id = v_e returning id)
  insert into schule.versuch(lernender_id, aufgabe_id, testsitzung_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr)
  select v_l, (select a.id from schule.aufgabe a where a.einheit_id = v_e and a.variante_gruppe = x->>'lernziel' order by a.id limit 1), t.id, 'lbn-nt-' || (x->>'lernziel'), null, true, 1, 1, 0, 1
    from t, schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') x where e.id = v_e;
  if schule.thema_stufe(v_l, v_t1)->>'stufe' <> 'komplett' then raise exception 'FEHLER M1 Ausgangslage: %', schule.thema_stufe(v_l, v_t1); end if;
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', pg_temp.lbn_eintrag(v_b, array[v_t1])), 'lehrer:Rauchtest'); v_s1 := (r->>'schritt_id')::bigint;
  if schule.thema_stufe(v_l, v_t1)->>'stufe' <> 'wiederholung' or (schule.thema_stufe(v_l, v_t1)->>'wdh_nr')::int <> 1 then raise exception 'FEHLER M1a: %', schule.thema_stufe(v_l, v_t1); end if;
  if exists (select 1 from schule.karte_stand where lernender_id = v_l and einheit_id = v_e
              and (not sitzt or wdh_stufe <> 0 or wdh_lerntage <> 1 or gesetzt_am is not null or sitzt_am > now() - interval '39 days' or eigene_loesungen <> 5 or misch_ok_am is null)) then
    raise exception 'FEHLER M1b: Landung, Herkunft oder Belege verändert'; end if;
  if exists (select 1 from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = v_e and schule.karte_faellig(k)) then raise exception 'FEHLER M1c: schon heute fällig'; end if;
  update schule.karte_stand set wdh_ab = wdh_ab - interval '1 day', faellig_am = faellig_am - interval '1 day' where lernender_id = v_l and einheit_id = v_e;
  if exists (select 1 from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = v_e and not schule.karte_faellig(k)) then raise exception 'FEHLER M1d: am nächsten Lerntag nicht fällig'; end if;
  update schule.karte_stand set wdh_ab = wdh_ab + interval '1 day', faellig_am = faellig_am + interval '1 day' where lernender_id = v_l and einheit_id = v_e;
  raise notice 'ok M1: vorher sicher (◉) → gesetzt ↻ Wdh 1 von 5, alle Etappen Stufe 1, am nächsten Lerntag fällig; sitzt_am, eigene Lösungen, Mischbeleg bleiben, kein gesetzt_am';
  -- Rückgängig (jüngster Schritt) stellt die Lage davor her
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('rueckgaengig', v_s1, 'eintraege', pg_temp.lbn_eintrag(v_b, '{}')), 'lehrer:Rauchtest');
  if schule.thema_stufe(v_l, v_t1)->>'stufe' <> 'komplett' or exists (select 1 from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and (wdh_stufe <> 4 or wdh_gesetzt_am is not null)) then
    raise exception 'FEHLER M1e: Rückgängig: %', schule.thema_stufe(v_l, v_t1); end if;
  raise notice 'ok M1e: Rückgängig → Wiederholungsstufe 4 zurück, wieder ◉';

  -- ---------- Sollte 4: Rückgängig nur für den jüngsten Schritt ----------
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', pg_temp.lbn_eintrag(v_b, array[v_t1])), 'lehrer:Rauchtest'); v_s1 := (r->>'schritt_id')::bigint;  -- A
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', pg_temp.lbn_eintrag(v_b, '{}')), 'lehrer:Rauchtest'); v_s2 := (r->>'schritt_id')::bigint;             -- B
  v_ok := false;
  begin
    perform schule.plan_setzen_intern(v_l, jsonb_build_object('rueckgaengig', v_s1, 'eintraege', pg_temp.lbn_eintrag(v_b, '{}')), 'lehrer:Rauchtest');
  exception when sqlstate 'P0001' then v_ok := sqlerrm = 'Inzwischen wurde etwas anderes geändert.';
  end;
  if not v_ok then raise exception 'FEHLER S4: Rückgängig eines älteren Schritts angenommen'; end if;
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('rueckgaengig', v_s2, 'eintraege', pg_temp.lbn_eintrag(v_b, array[v_t1])), 'lehrer:Rauchtest');
  raise notice 'ok S4: A setzen → B ändern → A rückgängig abgelehnt („Inzwischen wurde etwas anderes geändert.“); B rückgängig angenommen';
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', pg_temp.lbn_eintrag(v_b, '{}')), 'lehrer:Rauchtest');

  -- ---------- Muss 2: Rücknahme lässt keine unbelegte Landung stehen ----------
  v_e := schule.thema_einheit(v_t2); select block_id into v_b from schule.block_thema where thema_id = v_t2;
  select array_agg(x->>'lernziel' order by nr) into v_lz from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') with ordinality q(x, nr) where e.id = v_e;
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', pg_temp.lbn_eintrag(v_b, array[v_t2])), 'lehrer:Rauchtest');
  if (select count(*) from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and sitzt and gesetzt_am is not null) <> cardinality(v_lz) then raise exception 'FEHLER M2 Ausgangslage'; end if;
  -- Etappe 1: ein endgültiger Fehler (1. und 2. Anlauf falsch)
  v_a := pg_temp.lbn_karte(v_e, v_lz[1], 1);
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_a.id, 'client_id', 'lbn-2a1', 'antwort', pg_temp.lbn_falsch(v_a), 'anlauf', 1));
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_a.id, 'client_id', 'lbn-2a2', 'antwort', pg_temp.lbn_falsch(v_a), 'anlauf', 2));
  -- Etappe 2: offener erster Anlauf (falsch, noch nicht entschieden)
  v_a := pg_temp.lbn_karte(v_e, v_lz[2], 1);
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_a.id, 'client_id', 'lbn-2b1', 'antwort', pg_temp.lbn_falsch(v_a), 'anlauf', 1));
  -- Etappe 3: eine richtige Wiederholung (eine eigene Lösung)
  v_a := pg_temp.lbn_karte(v_e, v_lz[3], 1);
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_a.id, 'client_id', 'lbn-2c1', 'antwort', v_a.loesung, 'anlauf', 1));
  select * into v_ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[3];
  if v_ks.eigene_loesungen <> 1 or v_ks.folge <> 1 then raise exception 'FEHLER M2c: karte_buchen zählt in gesetzten Etappen nicht weiter (eigene %, Folge %)', v_ks.eigene_loesungen, v_ks.folge; end if;
  -- Etappe 4: seit dem Setzen nach der normalen Regel selbst gelandet (Zähler wie nach genug eigenen Lösungen)
  update schule.karte_stand k set eigene_loesungen = schule.karte_ziel(v_e, v_lz[4]), folge = 3, schwer_ok = true,
         typen = array(select distinct a.typ from schule.aufgabe a where a.einheit_id = v_e and a.variante_gruppe = v_lz[4] and a.typ is not null)
   where k.lernender_id = v_l and k.einheit_id = v_e and k.lernziel = v_lz[4];
  select * into v_ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[4];
  if not schule.karte_landet(v_ks) then raise exception 'FEHLER M2 Vorbereitung: Etappe 4 erfüllt die Landeregel nicht'; end if;
  select count(*) into v_versuche from schule.versuch where lernender_id = v_l and client_id like 'lbn-2%';
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', pg_temp.lbn_eintrag(v_b, '{}')), 'lehrer:Rauchtest'); -- Rücknahme
  if exists (select 1 from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = any(v_lz[1:3]) and (sitzt or sitzt_am is not null or gesetzt_am is not null)) then
    raise exception 'FEHLER M2a: unbelegte Landung bleibt nach Rücknahme'; end if;
  if (select eigene_loesungen from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[3]) <> 1 then raise exception 'FEHLER M2b: eigene Lösung verloren'; end if;
  select * into v_ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[4];
  if not v_ks.sitzt or v_ks.gesetzt_am is not null then raise exception 'FEHLER M2d: echte eigene Landung nicht behalten'; end if;
  if (select count(*) from schule.versuch where lernender_id = v_l and client_id like 'lbn-2%') <> v_versuche then raise exception 'FEHLER M2e: Versuche verloren'; end if;
  if schule.thema_stufe(v_l, v_t2)->>'stufe' <> 'dran' then raise exception 'FEHLER M2f: %', schule.thema_stufe(v_l, v_t2); end if;
  raise notice 'ok M2 Rücknahme: Fehler → offen; offener erster Anlauf → offen; eine richtige Wiederholung → offen mit 1 eigener Lösung; echte eigene Landung → bleibt gelandet (Herkunft selbst); Versuche bleiben';
  -- dasselbe über Rückgängig: Setzen → ein Fehler → Rückgängig → offen (früher blieb die gesetzte Landung bei eigenen Versuchen stehen)
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', pg_temp.lbn_eintrag(v_b, array[v_t2])), 'lehrer:Rauchtest'); v_s1 := (r->>'schritt_id')::bigint;
  v_a := pg_temp.lbn_karte(v_e, v_lz[1], 2);
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_a.id, 'client_id', 'lbn-2r1', 'antwort', pg_temp.lbn_falsch(v_a), 'anlauf', 1));
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_a.id, 'client_id', 'lbn-2r2', 'antwort', pg_temp.lbn_falsch(v_a), 'anlauf', 2));
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('rueckgaengig', v_s1, 'eintraege', pg_temp.lbn_eintrag(v_b, '{}')), 'lehrer:Rauchtest');
  if exists (select 1 from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = any(v_lz[1:3]) and (sitzt or gesetzt_am is not null)) then
    raise exception 'FEHLER M2g: Rückgängig lässt unbelegte Landung stehen'; end if;
  if not (select sitzt from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[4]) then raise exception 'FEHLER M2h: selbst gelandete Etappe durch Rückgängig verloren'; end if;
  raise notice 'ok M2 Rückgängig: Setzen → Fehler → Rückgängig → offen; selbst gelandete Etappe bleibt';

  -- ---------- Muss 3: sicher richtet sich nach dem Flug ----------
  v_e := schule.thema_einheit(v_t3); select block_id into v_b from schule.block_thema where thema_id = v_t3;
  select array_agg(x->>'lernziel' order by nr) into v_lz from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') with ordinality q(x, nr) where e.id = v_e;
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) values (v_l, v_e, v_lz[1]) on conflict do nothing;
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '5 days', wdh_stufe = 1, wdh_ab = now() - interval '5 days', wdh_lerntage = 3
   where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[1]; -- selbst gelandet, ohne Nachtest
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', pg_temp.lbn_eintrag(v_b, array[v_t3])), 'lehrer:Rauchtest');
  select * into v_ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[1];
  if v_ks.gesetzt_am is not null or v_ks.wdh_gesetzt_am is null then raise exception 'FEHLER M3 Vorbereitung'; end if;
  update schule.karte_stand set wdh_stufe = 4 where lernender_id = v_l and einheit_id = v_e; -- alle Wiederholungen bis 14 Lerntage bestanden
  if exists (select 1 from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = v_e and not schule.karte_sicher(k)) or schule.thema_stufe(v_l, v_t3)->>'stufe' <> 'komplett' then
    raise exception 'FEHLER M3a: %', schule.thema_stufe(v_l, v_t3); end if;
  -- nur vorgeladene Mischkarte: zählt nicht
  v_a := pg_temp.lbn_karte(v_e, v_lz[1], 1);
  insert into schule.misch_ausgabe(lernender_id, aufgabe_id, einheit_id, lernziel) values (v_l, v_a.id, v_e, null)
  on conflict (lernender_id, aufgabe_id) where eingeloest_am is null do update set ausgegeben_am = now(), verfallen_am = null;
  if not schule.karte_sicher((select k from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = v_e and k.lernziel = v_lz[1])) then raise exception 'FEHLER M3b: vorgeladene Mischkarte zählt'; end if;
  -- eingelöst (falsch beantwortet) seit dem Setzen: erst wieder sicher mit einer richtigen Mischkarte
  update schule.misch_ausgabe set eingeloest_am = now() where lernender_id = v_l and aufgabe_id = v_a.id and eingeloest_am is null;
  if schule.karte_sicher((select k from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = v_e and k.lernziel = v_lz[1])) or schule.thema_stufe(v_l, v_t3)->>'stufe' <> 'wiederholung' then
    raise exception 'FEHLER M3c: eingelöste, nicht richtige Mischkarte übersehen'; end if;
  update schule.karte_stand set misch_ok_am = now() where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[1];
  if schule.thema_stufe(v_l, v_t3)->>'stufe' <> 'komplett' then raise exception 'FEHLER M3d'; end if;
  raise notice 'ok M3: selbst gelandete Etappe ohne Nachtest + gesetzte Etappen, Wiederholungen bestanden → alle sicher, Flug ◉; vorgeladene Mischkarte zählt nicht, eingelöste nur richtig';
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', pg_temp.lbn_eintrag(v_b, '{}')), 'lehrer:Rauchtest');

  -- ---------- Sollte 5: „Kann er komplett“ mit Rückfall ----------
  v_e := schule.thema_einheit(v_t4); select block_id into v_b from schule.block_thema where thema_id = v_t4;
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', pg_temp.lbn_eintrag(v_b, '{}', array[v_t4])), 'lehrer:Rauchtest');
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) select v_l, v_e, x->>'lernziel' from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') x where e.id = v_e limit 1 on conflict do nothing;
  update schule.karte_stand set sitzt = false, sitzt_am = now() - interval '10 days', geoeffnet_am = now() - interval '1 day'
   where lernender_id = v_l and einheit_id = v_e and lernziel = (select x->>'lernziel' from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') x where e.id = v_e limit 1);
  r := schule.thema_stufe(v_l, v_t4);
  if r->>'stufe' <> 'komplett' or r->>'hinweis' is distinct from 'rueckfall' or (r->>'wieder_offen')::int < 1 then raise exception 'FEHLER S5: %', r; end if;
  raise notice 'ok S5: „Kann er komplett“ mit wieder offener Etappe → bleibt ◉, hinweis rueckfall, wieder_offen %', r->>'wieder_offen';

  -- ---------- Sollte 6: heute_bis ----------
  v_bis := (schule.einheit_lesen_intern(v_l, schule.thema_einheit(v_t1))->>'heute_bis')::timestamptz;
  if v_bis is null or v_bis <= now() or v_bis > now() + interval '1 day' or (v_bis at time zone coalesce(v_tz, 'Europe/Berlin'))::time <> '00:00'
     or (v_bis at time zone coalesce(v_tz, 'Europe/Berlin'))::date <> schule.heute_tag(v_l) + 1 then raise exception 'FEHLER S6: %', v_bis; end if;
  raise notice 'ok S6: heute_bis = nächster Tagesbeginn in der Zeitzone des Kindes (%)', v_bis;
end $$;
rollback;
