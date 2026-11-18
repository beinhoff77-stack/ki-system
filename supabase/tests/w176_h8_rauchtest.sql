-- Rauchtest H8: Fehler in Mischkarte oder Expedition öffnen eine gelandete Etappe nie. Nach 20261119_w176_h8_*.sql ausführen. Rollback, nur Testkind, keine Namen.
begin;
do $$
declare v_l bigint; v_e bigint; v_lz text; v_a bigint; ks schule.karte_stand; r jsonb; v_teil bigint; v_x bigint;
  datei jsonb := '{"schluessel": "8-handytarif", "klasse": {"gym_by": 8}, "titel": "Handytarif", "autor": "Claude (Bau-Auftrag G, Beispiel)", "einleitung": "Du brauchst einen neuen Handytarif. Tarif A kostet 5 € Grundgebühr im Monat und 0,10 € je telefonierter Minute. Tarif B ist eine Flatrate: 12 € im Monat, egal wie lange du telefonierst. Welcher Tarif lohnt sich für dich?", "voraussetzungen": [{"thema_schluessel": "funktionen.linear", "lernziel": "aufstellen"}, {"thema_schluessel": "funktionen.linear", "lernziel": "graph_ablesen"}, {"thema_schluessel": "gleichungen.ungleichungen", "lernziel": "sachaufgabe"}, {"thema_schluessel": "bruch.prozent_grundwert", "lernziel": "vermehrt"}], "teile": [{"k": "a", "y": "luecken", "f": {"text": "Tarif A: 5 € Grundgebühr und 0,10 € je Minute. Stelle den Term für die Kosten K(x) in Cent auf, wenn du x Minuten telefonierst.", "schablone": "□x + □", "hinweis": "Kosten in Cent: zuerst der Preis je Minute, dann die Grundgebühr"}, "o": {"werte": [10, 500]}, "c": ["0.10 * 100", "5 * 100"], "w": "Je Minute kommen 10 Cent dazu, die Grundgebühr sind 500 Cent: K(x) = 10x + 500.", "h": "Rechne erst beides in Cent um: 1 € = 100 Cent.", "bezug": {"thema_schluessel": "funktionen.linear", "lernziel": "aufstellen"}}, {"k": "b", "y": "auswahl", "f": {"text": "Tarif A in Euro: K(x) = 0,10 · x + 5. Welcher Graph gehört zu Tarif A?", "grafik": {"typ": "koordinaten", "x": [0, 120], "y": [0, 20], "schritt_x": 20, "schritt_y": 5, "name_x": "Minuten", "name_y": "€", "graphen": [{"art": "linear", "m": 0.05, "t": 5.0, "name": "1"}, {"art": "linear", "m": 0.1, "t": 5.0, "name": "2"}, {"art": "linear", "m": 0.1, "t": 0, "name": "3"}]}}, "a": ["Graph 1", "Graph 2", "Graph 3"], "o": {"index": 1}, "w": "Tarif A beginnt bei 5 € (bei 0 Minuten) und steigt in 10 Minuten um 1 €: bei 100 Minuten sind es 15 €. Das ist Graph 2. Graph 3 vergisst die Grundgebühr, Graph 1 steigt nur halb so schnell.", "h": "Wo schneidet der Graph die senkrechte Achse? Und wie viel kosten 100 Minuten?", "bezug": {"thema_schluessel": "funktionen.linear", "lernziel": "graph_ablesen"}}, {"k": "c", "y": "zahl", "f": {"text": "Tarif A kostet 5 € + 0,10 € je Minute, Tarif B 12 € im Monat. Ab wie vielen ganzen Minuten im Monat ist Tarif B günstiger?"}, "o": {"wert": 71}, "c": "(12 - 5) / 0.10 + 1", "w": "B ist günstiger, wenn 5 + 0,10 · x > 12, also 0,10 · x > 7 und x > 70. Ab 71 Minuten ist B günstiger (bei genau 70 Minuten kosten beide 12 €).", "h": "Stelle eine Ungleichung auf: Kosten von A > Kosten von B.", "bezug": {"thema_schluessel": "gleichungen.ungleichungen", "lernziel": "sachaufgabe"}}, {"k": "d", "y": "zahl", "f": {"text": "Tarif B (bisher 12 €) wird 15 % teurer. Tarif A bleibt bei 5 € + 0,10 € je Minute. Ab wie vielen ganzen Minuten ist Tarif B jetzt günstiger?"}, "o": {"wert": 89}, "c": "(12 * 1.15 - 5) / 0.10 + 1", "w": "Neuer Preis von B: 12 € · 1,15 = 13,8 €. B ist günstiger, wenn 5 + 0,10 · x > 13,8, also 0,10 · x > 8,8 und x > 88. Ab 89 Minuten ist B günstiger.", "h": "Rechne zuerst den neuen Preis von B aus (vermehrter Grundwert), dann wie in Teil c.", "bezug": {"thema_schluessel": "bruch.prozent_grundwert", "lernziel": "vermehrt"}}]}'::jsonb;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  select einheit_id, variante_gruppe, id into v_e, v_lz, v_a from schule.aufgabe where pool = 'uebung' and freigegeben and stufe in (2, 3) order by id limit 1;
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) values (v_l, v_e, v_lz) on conflict do nothing;
  -- gelandet, schon ein Wiederholungsfehler (wdh_fehler = 1), noch nicht fällig
  update schule.karte_stand set sitzt = true, sitzt_am = now(), wdh_stufe = 2, wdh_fehler = 1, wdh_ab = now(), wdh_lerntage = 7, faellig_am = now() + interval '7 days', misch_ok_am = now()
   where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  -- 1) zwei endgültige Fehler in Mischkarten hintereinander
  insert into schule.versuch(lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf, misch)
    values (v_l, v_a, 'h8-m1', '{}', false, 0, 1, 1, 1, 2, true), (v_l, v_a, 'h8-m2', '{}', false, 0, 1, 1, 2, 2, true);
  select * into ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if not ks.sitzt or ks.wdh_stufe <> 2 or ks.wdh_fehler <> 1 or ks.misch_ok_am is null or ks.wdh_lerntage <> 1 then raise exception 'FEHLER 1: %', row_to_json(ks); end if;
  raise notice 'ok 1: zwei Mischkarten-Fehler → bleibt gelandet, Belege unverändert, am nächsten Lerntag fällig';
  -- 2) Expedition: Teil mit Bezug auf diese Etappe, zwei Fehler; dann gemischt (Mischkarte + Expedition)
  r := schule.expedition_importieren(datei); v_x := (r->>'expedition_id')::bigint;
  select id into v_teil from schule.aufgabe where expedition_id = v_x order by reihenfolge limit 1;
  update schule.aufgabe set einheit_id = v_e, variante_gruppe = v_lz where id = v_teil; -- Bezug im Test auf diese Etappe legen
  perform schule.expedition_buchen(v_l, v_teil, false, 1::smallint, 2::smallint, now());
  perform schule.expedition_buchen(v_l, v_teil, false, 1::smallint, 2::smallint, now());
  perform schule.misch_buchen(v_l, v_a, false, 0::smallint, now());
  select * into ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if not ks.sitzt or ks.wdh_fehler <> 1 or ks.wdh_stufe <> 2 then raise exception 'FEHLER 2: %', row_to_json(ks); end if;
  raise notice 'ok 2: Expedition zweimal falsch und gemischt mit Mischkarte → bleibt gelandet';
  -- 3) Gegenprobe: die fällige Wiederholung darf weiterhin öffnen (zwei Fehler in der Wiederholung)
  perform schule.karte_buchen(v_l, v_a, false, 0::smallint, now());
  select * into ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if ks.sitzt then raise exception 'FEHLER 3: Wiederholung öffnet nicht mehr: %', row_to_json(ks); end if;
  raise notice 'ok 3: Wiederöffnen bleibt der Wiederholung vorbehalten';
end $$;
rollback;
