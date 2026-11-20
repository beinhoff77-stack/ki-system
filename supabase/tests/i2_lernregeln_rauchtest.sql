-- Rauchtest Bau-Auftrag I, Teil 2 (H10, H2, H6, H12 sowie Tests zu H4, H11, H14). Nach 20261120_i2_lernregeln.sql ausführen.
-- Transaktion mit Rollback, nur Testkind, keine Namen. Legt Karten-Stände, Versuche, eine Test-Expedition, eine zweite Flug-Version und einen
-- Nachtest selbst an; aus der Datenbank kommen nur Inhalte (Flüge, Bordkarten). Läuft über die innere Funktion schule.uebung_pruefen_intern
-- (dahinter Trigger versuch_karte); api.schule_uebung_pruefen ruft genau diese Funktion nach der Zugriffsprüfung auf – ein Schlüssel gehört nicht in eine Datei.
begin;
do $$
declare v_l bigint; v_e1 bigint; v_lz1 text; v_e2 bigint; v_lz2 text; v_e3 bigint; v_lz3 text; v_ids1 bigint[]; v_ids3 bigint[]; v_ag schule.aufgabe;
  r jsonb; j jsonb; v_ks schule.karte_stand; v_n int; v_mid bigint; v_falsch jsonb;
  v_ts text[]; v_lzs text[]; v_es bigint[]; v_th bigint[]; v_exp jsonb; v_x bigint; v_neu bigint; v_teil bigint; v_ok boolean; v_ts_id bigint; v_vid bigint;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  update schule.karte_stand set sitzt = false where lernender_id = v_l; -- Ausgangslage: nichts gelandet
  update schule.misch_ausgabe set eingeloest_am = now() where lernender_id = v_l and eingeloest_am is null;

  -- drei Etappen mit je ≥ 4 freigegebenen Auswahl-Bordkarten (Stufe 2–3) in freigegebenen Flügen; Etappe 1 in einem Flug mit weiteren Etappen
  select q.einheit_id, q.variante_gruppe into v_e1, v_lz1 from (
    select a.einheit_id, a.variante_gruppe from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
     where a.pool = 'uebung' and a.freigegeben and a.antworttyp = 'auswahl' and a.stufe in (2, 3) and e.status = 'freigegeben'
     group by 1, 2 having count(*) >= 4) q
   where exists (select 1 from schule.aufgabe a2 where a2.einheit_id = q.einheit_id and a2.variante_gruppe <> q.variante_gruppe and a2.pool in ('sicherung', 'test', 'uebung'))
   order by 1, 2 limit 1;
  select a.einheit_id, a.variante_gruppe into v_e2, v_lz2 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
   where a.pool = 'uebung' and a.freigegeben and a.antworttyp = 'auswahl' and a.stufe in (2, 3) and e.status = 'freigegeben' and a.einheit_id <> v_e1
   group by 1, 2 having count(*) >= 4 order by 1, 2 limit 1;
  select a.einheit_id, a.variante_gruppe into v_e3, v_lz3 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
   where a.pool = 'uebung' and a.freigegeben and a.antworttyp = 'auswahl' and e.status = 'freigegeben' and a.einheit_id not in (v_e1, v_e2)
     and (select count(*) from jsonb_array_elements(coalesce(a.antworten, '[]'::jsonb))) >= 3
   group by 1, 2 having count(*) >= 4 order by 1, 2 limit 1;
  if v_e1 is null or v_e2 is null or v_e3 is null then raise exception 'FEHLER: keine passenden Etappen'; end if;
  select array_agg(id order by id) into v_ids1 from schule.aufgabe where einheit_id = v_e1 and variante_gruppe = v_lz1 and pool = 'uebung' and freigegeben and antworttyp = 'auswahl' and stufe in (2, 3);
  select array_agg(id order by id) into v_ids3 from schule.aufgabe where einheit_id = v_e3 and variante_gruppe = v_lz3 and pool = 'uebung' and freigegeben and antworttyp = 'auswahl'
     and (select count(*) from jsonb_array_elements(coalesce(antworten, '[]'::jsonb))) >= 3;
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) values (v_l, v_e1, v_lz1), (v_l, v_e3, v_lz3) on conflict do nothing;
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '2 days', misch_ok_am = null, wdh_stufe = 1, wdh_fehler = 0
   where lernender_id = v_l and einheit_id = v_e1 and lernziel = v_lz1;

  -- ---------- H10 Negativ: gefälschter Kontext ohne Ausgabe → kein Misch-Beleg, normale Buchung ----------
  select * into v_ag from schule.aufgabe where id = v_ids1[1];
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i2-10a', 'antwort', v_ag.loesung, 'misch', true, 'aktuell_einheit', v_e2, 'aktuell_lernziel', v_lz2));
  if (select misch from schule.versuch where lernender_id = v_l and client_id = 'i2-10a') or r ? 'misch'
     or (select misch_ok_am from schule.karte_stand where lernender_id = v_l and einheit_id = v_e1 and lernziel = v_lz1) is not null then
    raise exception 'FEHLER H10a: gefälschte Mischkarte gewertet: %', r; end if;
  -- Ausgabe älter als 24 Stunden zählt nicht
  insert into schule.misch_ausgabe(lernender_id, aufgabe_id, ausgegeben_am) values (v_l, v_ids1[2], now() - interval '25 hours');
  select * into v_ag from schule.aufgabe where id = v_ids1[2];
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i2-10b', 'antwort', v_ag.loesung, 'misch', true, 'aktuell_einheit', v_e2, 'aktuell_lernziel', v_lz2));
  if (select misch from schule.versuch where lernender_id = v_l and client_id = 'i2-10b') then raise exception 'FEHLER H10b: Ausgabe von vor 25 Stunden gewertet'; end if;
  raise notice 'ok H10a: gefälschter Kontext (misch, aktuell_*) ohne Ausgabe bzw. mit Ausgabe älter als 24 h → normale Buchung, kein Misch-Beleg';

  -- ---------- H10 Positiv: echter Ablauf – Flug 2 lesen, Mischkarte aus Etappe 1 ausgegeben, beantwortet, eingelöst ----------
  j := schule.mischkarten(v_l, v_e2);
  if jsonb_array_length(j) <> 1 or (select variante_gruppe from schule.aufgabe where id = (j->0->>'id')::bigint) <> v_lz1 then raise exception 'FEHLER H10c: Mischkarten %', j; end if;
  select * into v_ag from schule.aufgabe where id = (j->0->>'id')::bigint;
  if not exists (select 1 from schule.misch_ausgabe where lernender_id = v_l and aufgabe_id = v_ag.id and eingeloest_am is null) then raise exception 'FEHLER H10d: Ausgabe nicht gemerkt'; end if;
  if jsonb_array_length(schule.einheit_lesen_intern(v_l, v_e2)->'mischkarten') <> 1 then raise exception 'FEHLER H10e: einheit_lesen liefert keine Mischkarte'; end if;
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i2-10f', 'antwort', v_ag.loesung, 'misch', true, 'aktuell_einheit', v_e2, 'aktuell_lernziel', v_lz2));
  if not (r ? 'misch') or not (r->'misch'->>'ok')::boolean or not (select misch from schule.versuch where lernender_id = v_l and client_id = 'i2-10f')
     or (select misch_ok_am from schule.karte_stand where lernender_id = v_l and einheit_id = v_e1 and lernziel = v_lz1) is null then
    raise exception 'FEHLER H10f: echte Mischkarte nicht gewertet: %', r; end if;
  if exists (select 1 from schule.misch_ausgabe where lernender_id = v_l and aufgabe_id = v_ag.id and eingeloest_am is null) then raise exception 'FEHLER H10g: Ausgabe nicht eingelöst'; end if;
  -- dieselbe Karte noch einmal als „Mischkarte“ → schon eingelöst → normale Buchung
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i2-10h', 'antwort', v_ag.loesung, 'misch', true, 'aktuell_einheit', v_e2, 'aktuell_lernziel', v_lz2));
  if (select misch from schule.versuch where lernender_id = v_l and client_id = 'i2-10h') then raise exception 'FEHLER H10h: eingelöste Mischkarte zweimal gewertet'; end if;
  raise notice 'ok H10b: ausgegeben (einheit_lesen/mischkarten) → beantwortet → Misch-Beleg, Antwort mit misch.ok, Ausgabe eingelöst; zweites Mal kein Beleg';

  -- ---------- H2 Negativ: falscher 1. Anlauf, Kind geht ohne 2. Anlauf weiter → endgültig falsch, Folge bricht ----------
  update schule.karte_stand set sitzt = false, sitzt_am = null, eigene_loesungen = 0, serie = 0, typen = '{}', schwer_ok = false, folge = 0, fehler_folge = 0, gezaehlt = '{}', geoeffnet_am = null
   where lernender_id = v_l and einheit_id = v_e3 and lernziel = v_lz3;
  for v_n in 1..2 loop
    select * into v_ag from schule.aufgabe where id = v_ids3[v_n];
    perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i2-2r' || v_n, 'antwort', v_ag.loesung, 'anlauf', 1));
  end loop;
  select * into v_ag from schule.aufgabe where id = v_ids3[3];
  v_falsch := jsonb_build_object('index', ((v_ag.loesung->>'index')::int + 1) % jsonb_array_length(v_ag.antworten));
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i2-2f', 'antwort', v_falsch, 'anlauf', 1));
  select * into v_ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e3 and lernziel = v_lz3;
  if not (r->>'nochmal')::boolean or v_ks.folge <> 2 or not (select wertung_offen from schule.versuch where lernender_id = v_l and client_id = 'i2-2f') then
    raise exception 'FEHLER H2a: erster falscher Anlauf: folge %, %', v_ks.folge, r; end if;
  -- weiter mit einer anderen Bordkarte, richtig
  select * into v_ag from schule.aufgabe where id = v_ids3[4];
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i2-2w', 'antwort', v_ag.loesung, 'anlauf', 1));
  select * into v_ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e3 and lernziel = v_lz3;
  if v_ks.folge <> 1 or v_ks.fehler_folge <> 0 or (select wertung_offen from schule.versuch where lernender_id = v_l and client_id = 'i2-2f') then
    raise exception 'FEHLER H2b: Folge % statt 1 (der liegengelassene Fehler muss die Folge brechen)', v_ks.folge; end if;
  if schule.folge_nachrechnen(v_l, v_e3, v_lz3, now() - interval '1 millisecond') <> v_ks.folge then raise exception 'FEHLER H2c: Nachrechnung % ≠ Buchung %', schule.folge_nachrechnen(v_l, v_e3, v_lz3, now() - interval '1 millisecond'), v_ks.folge; end if;
  raise notice 'ok H2a: 2 richtig, 1. Anlauf falsch und liegengelassen, dann richtig → folge 1 (vorher wäre es 3 gewesen); Nachrechnung = Buchung';
  -- falscher 1. Anlauf, dann 2. Anlauf richtig → ersetzt, Folge bleibt
  select * into v_ag from schule.aufgabe where id = v_ids3[1];
  v_falsch := jsonb_build_object('index', ((v_ag.loesung->>'index')::int + 1) % jsonb_array_length(v_ag.antworten));
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i2-2g', 'antwort', v_falsch, 'anlauf', 1));
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i2-2h', 'antwort', v_ag.loesung, 'anlauf', 2));
  select * into v_ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e3 and lernziel = v_lz3;
  if v_ks.folge <> 1 or schule.folge_nachrechnen(v_l, v_e3, v_lz3, now() - interval '1 millisecond') <> 1
     or schule.versuch_wertung((select x from schule.versuch x where lernender_id = v_l and client_id = 'i2-2g')) <> 'ersetzt' then
    raise exception 'FEHLER H2d: 2. Anlauf richtig: folge %', v_ks.folge; end if;
  -- ohne zweite Chance (kein anlauf) falsch → sofort endgültig
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i2-2i', 'antwort', v_falsch));
  select * into v_ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e3 and lernziel = v_lz3;
  if v_ks.folge <> 0 or schule.folge_nachrechnen(v_l, v_e3, v_lz3, now() - interval '1 millisecond') <> 0 then raise exception 'FEHLER H2e: falsch ohne zweite Chance: folge %', v_ks.folge; end if;
  raise notice 'ok H2b: 1. Anlauf falsch + 2. Anlauf richtig → Folge bleibt (ersetzt); ohne zweite Chance falsch → Folge 0; Nachrechnung jeweils gleich';

  -- ---------- H6: Tag des Kindes vom Server ----------
  if schule.heute_tag(v_l) <> (now() at time zone coalesce((select zeitzone from schule.lernender where id = v_l), 'Europe/Berlin'))::date
     or (schule.einheit_lesen_intern(v_l, v_e3)->>'heute_tag')::date <> schule.heute_tag(v_l) then raise exception 'FEHLER H6'; end if;
  select * into v_ag from schule.aufgabe where id = v_ids3[2];
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i2-6', 'antwort', v_ag.loesung, 'anlauf', 1));
  if (r->'karte'->>'heute_tag')::date <> schule.heute_tag(v_l) then raise exception 'FEHLER H6b: %', r->'karte'; end if;
  raise notice 'ok H6: heute_tag (% ) in einheit_lesen und in der Antwort, Zeitzone des Kindes', schule.heute_tag(v_l);

  -- ---------- H4: Nachtest mit 80 % bestanden, aber diese Etappe falsch → nicht „sicher“ ----------
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '1 second', wdh_stufe = 4, misch_ok_am = now() where lernender_id = v_l and einheit_id = v_e1 and lernziel = v_lz1;
  insert into schule.testsitzung(lernender_id, art, block_id, thema_id, einheit_id, nachtest_runde, aufgaben, status, punkte, punkte_max, quote, ergebnis, abgeschlossen_am)
  select v_l, 'nachtest', e.block_id, e.thema_id, e.id, 1, '{}', 'abgeschlossen', 4, 5, 0.8, 'bestanden', now() from schule.einheit e where e.id = v_e1 returning id into v_ts_id;
  insert into schule.versuch(lernender_id, aufgabe_id, testsitzung_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr)
  select v_l, q.id, v_ts_id, 'i2-4-' || q.id, null, true, 1, 1, 0, 1 from (select a.id from schule.aufgabe a where a.einheit_id = v_e1 and a.variante_gruppe <> v_lz1 order by a.id limit 4) q;
  insert into schule.versuch(lernender_id, aufgabe_id, testsitzung_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr)
  values (v_l, v_ids1[3], v_ts_id, 'i2-4-falsch', null, false, 0, 1, 0, 1) returning id into v_vid;
  select * into v_ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e1 and lernziel = v_lz1;
  if schule.karte_sicher(v_ks) then raise exception 'FEHLER H4a: sicher, obwohl die Etappe im bestandenen Nachtest falsch war'; end if;
  update schule.versuch set richtig = true where id = v_vid; -- Gegenprobe
  if not schule.karte_sicher(v_ks) then raise exception 'FEHLER H4b: Gegenprobe – mit richtiger Antwort nicht sicher'; end if;
  raise notice 'ok H4: Nachtest bestanden (4/5), diese Etappe falsch → nicht sicher; Gegenprobe richtig → sicher';

  -- ---------- H12: Voraussetzung auf die Lernkarte prüfen; danach Test-Expedition für H11/H14 ----------
  select array_agg(q.ts order by q.th), array_agg(q.lz order by q.th), array_agg(q.ein order by q.th), array_agg(q.th order by q.th) into v_ts, v_lzs, v_es, v_th from (
    select distinct on (th.id) th.id th, th.schluessel ts, a.variante_gruppe lz, e.id ein from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id join schule.thema th on th.id = e.thema_id
     where a.pool = 'uebung' and a.freigegeben and e.status = 'freigegeben' order by th.id, a.variante_gruppe limit 3) q;
  if cardinality(v_ts) <> 3 then raise exception 'FEHLER: keine drei Themen'; end if;
  v_exp := jsonb_build_object('schluessel', 'rauchtest-i2', 'klasse', '{"gym_by": 5}'::jsonb, 'titel', 'Rauchtest I-2', 'einleitung', 'Test', 'autor', 'Rauchtest',
    'voraussetzungen', (select jsonb_agg(jsonb_build_object('thema_schluessel', v_ts[i], 'lernziel', v_lzs[i])) from generate_series(1, 3) i),
    'teile', (select jsonb_agg(jsonb_build_object('k', chr(96 + i), 'y', 'zahl', 'f', jsonb_build_object('text', i || ' + 1 = ?'), 'o', jsonb_build_object('wert', i + 1), 'w', 'Rechnen.', 'h', 'Zähle.',
                 'bezug', jsonb_build_object('thema_schluessel', v_ts[i], 'lernziel', v_lzs[i]))) from generate_series(1, 3) i));
  v_ok := false;
  begin
    perform schule.expedition_importieren(jsonb_set(v_exp, '{voraussetzungen}', (v_exp->'voraussetzungen') || jsonb_build_object('thema_schluessel', v_ts[1], 'lernziel', 'gibt_es_nicht_i2')));
  exception when raise_exception then
    if sqlerrm like 'Voraussetzung: Lernkarte%' then v_ok := true; else raise; end if;
  end;
  if not v_ok then raise exception 'FEHLER H12: Voraussetzung mit unbekannter Lernkarte angenommen'; end if;
  if exists (select 1 from schule.expedition where schluessel = 'rauchtest-i2') then raise exception 'FEHLER H12b: trotz Fehler geschrieben'; end if;
  r := schule.expedition_importieren(v_exp); v_x := (r->>'expedition_id')::bigint;
  raise notice 'ok H12: zusätzliche Voraussetzung mit unbekannter Lernkarte abgelehnt, nichts geschrieben; gültige Datei importiert (Expedition %)', v_x;

  -- ---------- H11: zwei Versionen eines Themas – über die ganze Buchung ----------
  insert into schule.einheit(thema_id, block_id, version, status, inhalt)
  select e.thema_id, e.block_id, (select max(e2.version) + 1 from schule.einheit e2 where e2.thema_id = e.thema_id), 'entwurf', e.inhalt from schule.einheit e where e.id = v_es[1]
  returning id into v_neu;
  update schule.aufgabe set einheit_id = v_neu where expedition_id = v_x and teil = 'a'; -- wie nach einem Neu-Import auf die neue Version
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) select v_l, v_es[i], v_lzs[i] from generate_series(1, 3) i on conflict do nothing;
  update schule.karte_stand k set sitzt = true, sitzt_am = now() - interval '3 days', angewandt_am = null
   where k.lernender_id = v_l and (k.einheit_id, k.lernziel) in (select v_es[i], v_lzs[i] from generate_series(1, 3) i);

  -- ---------- H14: Expedition unterbrochen und fortgesetzt ----------
  if schule.expedition_zustand(v_l, (select x from schule.expedition x where x.id = v_x)) <> 'angeboten' then raise exception 'FEHLER H14a: nicht angeboten'; end if;
  select * into v_ag from schule.aufgabe where expedition_id = v_x and teil = 'a';
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i2-14a', 'antwort', v_ag.loesung));
  if (select angewandt_am from schule.karte_stand where lernender_id = v_l and einheit_id = v_es[1] and lernziel = v_lzs[1]) is null
     or exists (select 1 from schule.karte_stand where lernender_id = v_l and einheit_id = v_neu and angewandt_am is not null) then
    raise exception 'FEHLER H11: Teil a nicht auf die gelandete (alte) Version gebucht'; end if;
  raise notice 'ok H11: Expedition-Teil zeigt auf die neue Version, gebucht wird über uebung_pruefen_intern auf die gelandete alte Version';
  if schule.expedition_zustand(v_l, (select x from schule.expedition x where x.id = v_x)) <> 'begonnen' or (r->'expedition'->>'geschafft')::boolean
     or exists (select 1 from schule.sterne where lernender_id = v_l and grund = 'expedition' and bezug = 'expedition:' || v_x) then raise exception 'FEHLER H14b: nach Teil a'; end if;
  -- Unterbrechung: anderes geübt, Etappe 1 inzwischen wieder offen (Rückfall) – die begonnene Expedition bleibt fortsetzbar
  update schule.karte_stand set sitzt = false where lernender_id = v_l and einheit_id = v_es[2] and lernziel = v_lzs[2];
  for v_teil in select id from schule.aufgabe where expedition_id = v_x and teil in ('b', 'c') order by teil loop
    select * into v_ag from schule.aufgabe where id = v_teil;
    r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i2-14' || v_ag.teil, 'antwort', v_ag.loesung));
  end loop;
  if not (r->'expedition'->>'geschafft')::boolean or schule.expedition_zustand(v_l, (select x from schule.expedition x where x.id = v_x)) <> 'geschafft' then
    raise exception 'FEHLER H14c: nach Fortsetzung nicht geschafft: %', r; end if;
  select count(*) into v_n from schule.sterne where lernender_id = v_l and grund = 'expedition' and bezug = 'expedition:' || v_x;
  -- Teil a noch einmal → keine zweiten Sterne
  select * into v_ag from schule.aufgabe where expedition_id = v_x and teil = 'a';
  perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ag.id, 'client_id', 'i2-14a2', 'antwort', v_ag.loesung));
  if v_n <> 1 or (select count(*) from schule.sterne where lernender_id = v_l and grund = 'expedition' and bezug = 'expedition:' || v_x) <> 1 then raise exception 'FEHLER H14d: Sterne % ', v_n; end if;
  raise notice 'ok H14: Teil a → begonnen; Unterbrechung mit Rückfall einer Voraussetzung; b, c → geschafft, Sterne einmal (auch nach Wiederholung von a)';
end $$;
rollback;
