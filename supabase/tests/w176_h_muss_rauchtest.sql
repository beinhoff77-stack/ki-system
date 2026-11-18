-- Rauchtest Auftrag H (Muss: H1–H4, H9–H11). Nach 20261119_w176_h8_*.sql und 20261119_w176_h_muss.sql ausführen. Rollback, nur Testkind, keine Namen.
-- Läuft über den echten Weg: schule.uebung_pruefen_intern (dahinter Trigger versuch_karte → karte_buchen/misch_buchen/expedition_buchen).
-- api.schule_uebung_pruefen ruft genau diese Funktion nach der Zugriffsprüfung auf; ein Schlüssel gehört nicht in eine Datei.
begin;
do $$
declare v_l bigint; v_e bigint; v_lz text; v_e2 bigint; v_lz2 text; ids bigint[]; ids2 bigint[]; r jsonb; ks schule.karte_stand; v_n int; v_x bigint; v_teil bigint;
  v_t bigint; v_alt bigint; v_neu bigint; a schule.aufgabe;
  datei jsonb := '{"schluessel": "8-handytarif", "klasse": {"gym_by": 8}, "titel": "Handytarif", "autor": "Claude (Bau-Auftrag G, Beispiel)", "einleitung": "Du brauchst einen neuen Handytarif. Tarif A kostet 5 € Grundgebühr im Monat und 0,10 € je telefonierter Minute. Tarif B ist eine Flatrate: 12 € im Monat, egal wie lange du telefonierst. Welcher Tarif lohnt sich für dich?", "voraussetzungen": [{"thema_schluessel": "funktionen.linear", "lernziel": "aufstellen"}, {"thema_schluessel": "funktionen.linear", "lernziel": "graph_ablesen"}, {"thema_schluessel": "gleichungen.ungleichungen", "lernziel": "sachaufgabe"}, {"thema_schluessel": "bruch.prozent_grundwert", "lernziel": "vermehrt"}], "teile": [{"k": "a", "y": "luecken", "f": {"text": "Tarif A: 5 € Grundgebühr und 0,10 € je Minute. Stelle den Term für die Kosten K(x) in Cent auf, wenn du x Minuten telefonierst.", "schablone": "□x + □", "hinweis": "Kosten in Cent: zuerst der Preis je Minute, dann die Grundgebühr"}, "o": {"werte": [10, 500]}, "c": ["0.10 * 100", "5 * 100"], "w": "Je Minute kommen 10 Cent dazu, die Grundgebühr sind 500 Cent: K(x) = 10x + 500.", "h": "Rechne erst beides in Cent um: 1 € = 100 Cent.", "bezug": {"thema_schluessel": "funktionen.linear", "lernziel": "aufstellen"}}, {"k": "b", "y": "auswahl", "f": {"text": "Tarif A in Euro: K(x) = 0,10 · x + 5. Welcher Graph gehört zu Tarif A?", "grafik": {"typ": "koordinaten", "x": [0, 120], "y": [0, 20], "schritt_x": 20, "schritt_y": 5, "name_x": "Minuten", "name_y": "€", "graphen": [{"art": "linear", "m": 0.05, "t": 5.0, "name": "1"}, {"art": "linear", "m": 0.1, "t": 5.0, "name": "2"}, {"art": "linear", "m": 0.1, "t": 0, "name": "3"}]}}, "a": ["Graph 1", "Graph 2", "Graph 3"], "o": {"index": 1}, "w": "Tarif A beginnt bei 5 € (bei 0 Minuten) und steigt in 10 Minuten um 1 €: bei 100 Minuten sind es 15 €. Das ist Graph 2. Graph 3 vergisst die Grundgebühr, Graph 1 steigt nur halb so schnell.", "h": "Wo schneidet der Graph die senkrechte Achse? Und wie viel kosten 100 Minuten?", "bezug": {"thema_schluessel": "funktionen.linear", "lernziel": "graph_ablesen"}}, {"k": "c", "y": "zahl", "f": {"text": "Tarif A kostet 5 € + 0,10 € je Minute, Tarif B 12 € im Monat. Ab wie vielen ganzen Minuten im Monat ist Tarif B günstiger?"}, "o": {"wert": 71}, "c": "(12 - 5) / 0.10 + 1", "w": "B ist günstiger, wenn 5 + 0,10 · x > 12, also 0,10 · x > 7 und x > 70. Ab 71 Minuten ist B günstiger (bei genau 70 Minuten kosten beide 12 €).", "h": "Stelle eine Ungleichung auf: Kosten von A > Kosten von B.", "bezug": {"thema_schluessel": "gleichungen.ungleichungen", "lernziel": "sachaufgabe"}}, {"k": "d", "y": "zahl", "f": {"text": "Tarif B (bisher 12 €) wird 15 % teurer. Tarif A bleibt bei 5 € + 0,10 € je Minute. Ab wie vielen ganzen Minuten ist Tarif B jetzt günstiger?"}, "o": {"wert": 89}, "c": "(12 * 1.15 - 5) / 0.10 + 1", "w": "Neuer Preis von B: 12 € · 1,15 = 13,8 €. B ist günstiger, wenn 5 + 0,10 · x > 13,8, also 0,10 · x > 8,8 und x > 88. Ab 89 Minuten ist B günstiger.", "h": "Rechne zuerst den neuen Preis von B aus (vermehrter Grundwert), dann wie in Teil c.", "bezug": {"thema_schluessel": "bruch.prozent_grundwert", "lernziel": "vermehrt"}}]}'::jsonb;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  -- zwei Etappen mit je ≥ 4 freigegebenen Auswahl-Bordkarten der Stufe 2–3 in freigegebenen Flügen
  select a.einheit_id, a.variante_gruppe into v_e, v_lz from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
   where a.pool = 'uebung' and a.freigegeben and a.antworttyp = 'auswahl' and a.stufe in (2, 3) and e.status = 'freigegeben'
   group by 1, 2 having count(*) >= 4 order by 1, 2 limit 1;
  select a.einheit_id, a.variante_gruppe into v_e2, v_lz2 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
   where a.pool = 'uebung' and a.freigegeben and a.antworttyp = 'auswahl' and a.stufe in (2, 3) and e.status = 'freigegeben' and a.einheit_id <> v_e
   group by 1, 2 having count(*) >= 4 order by 1, 2 limit 1;
  select array_agg(id order by id) into ids from schule.aufgabe where einheit_id = v_e and variante_gruppe = v_lz and pool = 'uebung' and freigegeben and antworttyp = 'auswahl' and stufe in (2, 3);
  select array_agg(id order by id) into ids2 from schule.aufgabe where einheit_id = v_e2 and variante_gruppe = v_lz2 and pool = 'uebung' and freigegeben and antworttyp = 'auswahl' and stufe in (2, 3);
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) values (v_l, v_e, v_lz), (v_l, v_e2, v_lz2) on conflict do nothing;

  -- ---------- H1: gelandet → Flugtest bestanden → 2 Fehler in der Wiederholung → überall offen → 3 in Folge → gelandet ----------
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '10 days', eigene_loesungen = schule.karte_ziel(v_e, v_lz), serie = schule.karte_ziel(v_e, v_lz),
         typen = coalesce((select array_agg(distinct typ) from schule.aufgabe where einheit_id = v_e and variante_gruppe = v_lz and pool = 'uebung' and typ is not null), '{}'),
         schwer_ok = true, folge = 3, wdh_stufe = 2, wdh_fehler = 1, wdh_ab = now(), wdh_lerntage = 1, gezaehlt = '{}'
   where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  insert into schule.lernziel_stand(lernender_id, einheit_id, lernziel, pflicht, status) values (v_l, v_e, v_lz, true, 'nachgewiesen')
    on conflict (lernender_id, einheit_id, lernziel) do update set status = 'nachgewiesen';
  select * into a from schule.aufgabe where id = ids[1];
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', a.id, 'client_id', 'h-1a', 'antwort', jsonb_build_object('index', ((a.loesung->>'index')::int + 1) % jsonb_array_length(a.antworten))));
  if (r->>'richtig')::boolean or (r->'karte'->>'sitzt')::boolean or (r->'karte'->>'fertig')::boolean then raise exception 'FEHLER H1a Antwort: %', r->'karte'; end if;
  r := schule.etappen_stand(v_l, v_e)->v_lz;
  if (r->>'fertig')::boolean or not (r->>'test_nachgewiesen')::boolean or not (r->>'wieder_offen')::boolean then raise exception 'FEHLER H1b etappen_stand: %', r; end if;
  select * into ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if ks.geoeffnet_am is null then raise exception 'FEHLER H1c geoeffnet_am'; end if;
  raise notice 'ok H1a: nach zwei Wiederholungsfehlern überall offen (fertig = false), bestandener Test getrennt sichtbar (test_nachgewiesen)';
  -- dreimal dieselbe bekannte Bordkarte richtig: Folge zählt, Nachweise nicht doppelt
  for v_n in 1..3 loop
    if v_n < 3 then
      r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', a.id, 'client_id', 'h-1r' || v_n, 'antwort', a.loesung));
      if (r->'karte'->>'sitzt')::boolean then raise exception 'FEHLER H1d: landet schon nach % richtigen', v_n; end if;
    else
      r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', a.id, 'client_id', 'h-1r' || v_n, 'antwort', a.loesung));
    end if;
  end loop;
  if not (r->'karte'->>'sitzt')::boolean or not (r->'karte'->>'fertig')::boolean then raise exception 'FEHLER H1e: nicht wieder gelandet: %', r->'karte'; end if;
  if not (schule.etappen_stand(v_l, v_e)->v_lz->>'fertig')::boolean then raise exception 'FEHLER H1f'; end if;
  raise notice 'ok H1b: drei eigene Lösungen in Folge → wieder gelandet, überall fertig';

  -- ---------- H3: dieselbe Aufgabe zählt einmal als Nachweis ----------
  update schule.karte_stand set sitzt = false, sitzt_am = null, eigene_loesungen = 0, serie = 0, typen = '{}', schwer_ok = false, folge = 0, fehler_folge = 0, gezaehlt = '{}'
   where lernender_id = v_l and einheit_id = v_e2 and lernziel = v_lz2;
  select * into a from schule.aufgabe where id = ids2[1];
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', a.id, 'client_id', 'h-3a', 'antwort', a.loesung));
  if not (r->'karte'->>'neu_gezaehlt')::boolean then raise exception 'FEHLER H3a: erste Lösung nicht neu gezählt: %', r->'karte'; end if;
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', a.id, 'client_id', 'h-3b', 'antwort', a.loesung));
  select * into ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e2 and lernziel = v_lz2;
  if (r->'karte'->>'neu_gezaehlt')::boolean or ks.eigene_loesungen <> 1 or ks.folge <> 2 or not (r->'karte'->'gezaehlt' @> to_jsonb(a.id)) then
    raise exception 'FEHLER H3b: %', row_to_json(ks); end if;
  raise notice 'ok H3: zweimal dieselbe Bordkarte → 1 eigene Lösung, Folge 2, Antwort „kennst du schon“ (neu_gezaehlt = false), gezählte Liste an die App';

  -- ---------- H4/H15: „sicher“ nur mit Nachweisen nach der letzten Landung ----------
  update schule.karte_stand set wdh_stufe = 4, misch_ok_am = sitzt_am - interval '1 day' where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  select * into ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if schule.karte_sicher(ks) then raise exception 'FEHLER H4a: sicher mit Mischkarte vor der Landung'; end if;
  update schule.karte_stand set misch_ok_am = now() + interval '1 second' where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  select * into ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if schule.karte_sicher(ks) and not exists (select 1 from schule.testsitzung t join schule.versuch v on v.testsitzung_id = t.id join schule.aufgabe x on x.id = v.aufgabe_id
       where t.lernender_id = v_l and t.einheit_id = v_e and t.art = 'nachtest' and t.ergebnis = 'bestanden' and t.abgeschlossen_am >= ks.sitzt_am and x.variante_gruppe = v_lz and v.richtig) then
    raise exception 'FEHLER H4b: sicher ohne Flug-Nachtest dieser Etappe nach der Landung'; end if;
  raise notice 'ok H4: sicher braucht Mischkarte und Flug-Nachtest dieser Etappe nach der letzten Landung (flug_nachtest getrennt: %)', schule.flug_nachtest(v_l, v_e);

  -- ---------- H10: Mischkarte nur, wenn der Server sie bestätigt ----------
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '2 days', misch_ok_am = null where lernender_id = v_l and einheit_id = v_e2 and lernziel = v_lz2;
  select * into a from schule.aufgabe where id = ids2[2];
  -- a) gültig: gelandete Etappe, anderer aktueller Flug/Lernkarte
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', a.id, 'client_id', 'h-10a', 'antwort', a.loesung, 'misch', true, 'aktuell_einheit', v_e, 'aktuell_lernziel', v_lz));
  if not (select misch from schule.versuch where lernender_id = v_l and client_id = 'h-10a') or (select misch_ok_am from schule.karte_stand where lernender_id = v_l and einheit_id = v_e2 and lernziel = v_lz2) is null then
    raise exception 'FEHLER H10a: gültige Mischkarte nicht gewertet'; end if;
  -- b) ohne aktuelle Etappe (alte App) → normal gebucht
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', ids2[3], 'client_id', 'h-10b', 'antwort', (select loesung from schule.aufgabe where id = ids2[3]), 'misch', true));
  -- c) „Mischkarte“ aus der gerade geübten Etappe → normal gebucht
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', ids2[4], 'client_id', 'h-10c', 'antwort', (select loesung from schule.aufgabe where id = ids2[4]), 'misch', true, 'aktuell_einheit', v_e2, 'aktuell_lernziel', v_lz2));
  -- d) Etappe nicht gelandet → normal gebucht
  update schule.karte_stand set sitzt = false where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', ids[2], 'client_id', 'h-10d', 'antwort', (select loesung from schule.aufgabe where id = ids[2]), 'misch', true, 'aktuell_einheit', v_e2, 'aktuell_lernziel', v_lz2));
  if exists (select 1 from schule.versuch where lernender_id = v_l and client_id in ('h-10b', 'h-10c', 'h-10d') and misch) then raise exception 'FEHLER H10b–d: unbestätigte Mischkarte als Misch gebucht'; end if;
  raise notice 'ok H10: nur bestätigte Mischkarten (gelandet, Stufe 2–3, nicht die aktuelle Etappe) zählen; sonst normale Buchung';

  -- ---------- H9: Expedition nur mit gelandeten Voraussetzungen oder wenn schon begonnen ----------
  r := schule.expedition_importieren(datei); v_x := (r->>'expedition_id')::bigint;
  update schule.karte_stand k set sitzt = false from schule.einheit e, schule.expedition x where x.id = v_x and e.id = k.einheit_id and k.lernender_id = v_l
     and exists (select 1 from jsonb_array_elements(x.voraussetzungen) vv where (vv->>'thema_id')::bigint = e.thema_id and vv->>'lernziel' = k.lernziel);
  select * into a from schule.aufgabe where expedition_id = v_x order by reihenfolge limit 1;
  begin
    perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', a.id, 'client_id', 'h-9a', 'antwort', a.loesung));
    raise exception 'FEHLER H9a: Expedition ohne Voraussetzungen gewertet';
  exception when raise_exception then
    if sqlerrm like 'FEHLER%' then raise; end if;
  end;
  -- begonnen (es gibt schon einen Versuch) → darf trotz Rückfall zu Ende geführt werden
  insert into schule.versuch(lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf) values (v_l, a.id, 'h-9b', '{}', true, 1, 1, 0, 1, 1);
  select * into a from schule.aufgabe where expedition_id = v_x order by reihenfolge offset 1 limit 1;
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', a.id, 'client_id', 'h-9c', 'antwort', a.loesung));
  if not (r->>'ok')::boolean then raise exception 'FEHLER H9b: begonnene Expedition nach Rückfall nicht fortsetzbar'; end if;
  raise notice 'ok H9: ohne Voraussetzungen abgelehnt, begonnene Expedition bleibt fortsetzbar';

  -- ---------- H11: Expedition bucht auf die gelandete Version ----------
  select e.thema_id into v_t from schule.einheit e group by e.thema_id having count(*) > 1 limit 1;
  if v_t is null then raise notice 'übersprungen H11: kein Thema mit zwei Versionen vorhanden';
  else
    select id into v_alt from schule.einheit where thema_id = v_t order by version limit 1;
    select id into v_neu from schule.einheit where thema_id = v_t order by version desc limit 1;
    insert into schule.karte_stand(lernender_id, einheit_id, lernziel, sitzt, sitzt_am) values (v_l, v_alt, 'h11', true, now()), (v_l, v_neu, 'h11', false, null)
      on conflict (lernender_id, einheit_id, lernziel) do update set sitzt = excluded.sitzt, sitzt_am = excluded.sitzt_am;
    select * into a from schule.aufgabe where expedition_id = v_x order by reihenfolge limit 1;
    a.thema_id := v_t; a.einheit_id := v_neu; a.variante_gruppe := 'h11';
    if schule.expedition_etappe(v_l, a) <> v_alt then raise exception 'FEHLER H11: bucht nicht auf die gelandete Version'; end if;
    raise notice 'ok H11: Expedition bucht je Kind auf die gelandete Version (alt gelandet, neu gebunden → alt)';
  end if;
end $$;
rollback;
