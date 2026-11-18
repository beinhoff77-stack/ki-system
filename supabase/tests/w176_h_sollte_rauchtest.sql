-- Rauchtest Auftrag H (Sollte: H6, H12, H13 Server-Teil, H14, H15). Nach 20261119_w176_h8_*, _h_muss und _h_sollte ausführen. Rollback, nur Testkind, keine Namen.
-- H14: Expedition über den echten Weg schule.uebung_pruefen_intern (wie api.schule_uebung_pruefen nach der Zugriffsprüfung), nicht über direkte Inserts.
begin;
do $$
declare v_l bigint; r jsonb; v_x bigint; x schule.expedition; ids bigint[]; a schule.aufgabe; v_n int; v_h0 int; ks schule.karte_stand; v_ok boolean;
  datei jsonb := '{"schluessel": "8-handytarif", "klasse": {"gym_by": 8}, "titel": "Handytarif", "autor": "Claude (Bau-Auftrag G, Beispiel)", "einleitung": "Du brauchst einen neuen Handytarif. Tarif A kostet 5 € Grundgebühr im Monat und 0,10 € je telefonierter Minute. Tarif B ist eine Flatrate: 12 € im Monat, egal wie lange du telefonierst. Welcher Tarif lohnt sich für dich?", "voraussetzungen": [{"thema_schluessel": "funktionen.linear", "lernziel": "aufstellen"}, {"thema_schluessel": "funktionen.linear", "lernziel": "graph_ablesen"}, {"thema_schluessel": "gleichungen.ungleichungen", "lernziel": "sachaufgabe"}, {"thema_schluessel": "bruch.prozent_grundwert", "lernziel": "vermehrt"}], "teile": [{"k": "a", "y": "luecken", "f": {"text": "Tarif A: 5 € Grundgebühr und 0,10 € je Minute. Stelle den Term für die Kosten K(x) in Cent auf, wenn du x Minuten telefonierst.", "schablone": "□x + □", "hinweis": "Kosten in Cent: zuerst der Preis je Minute, dann die Grundgebühr"}, "o": {"werte": [10, 500]}, "c": ["0.10 * 100", "5 * 100"], "w": "Je Minute kommen 10 Cent dazu, die Grundgebühr sind 500 Cent: K(x) = 10x + 500.", "h": "Rechne erst beides in Cent um: 1 € = 100 Cent.", "bezug": {"thema_schluessel": "funktionen.linear", "lernziel": "aufstellen"}}, {"k": "b", "y": "auswahl", "f": {"text": "Tarif A in Euro: K(x) = 0,10 · x + 5. Welcher Graph gehört zu Tarif A?", "grafik": {"typ": "koordinaten", "x": [0, 120], "y": [0, 20], "schritt_x": 20, "schritt_y": 5, "name_x": "Minuten", "name_y": "€", "graphen": [{"art": "linear", "m": 0.05, "t": 5.0, "name": "1"}, {"art": "linear", "m": 0.1, "t": 5.0, "name": "2"}, {"art": "linear", "m": 0.1, "t": 0, "name": "3"}]}}, "a": ["Graph 1", "Graph 2", "Graph 3"], "o": {"index": 1}, "w": "Tarif A beginnt bei 5 € (bei 0 Minuten) und steigt in 10 Minuten um 1 €: bei 100 Minuten sind es 15 €. Das ist Graph 2. Graph 3 vergisst die Grundgebühr, Graph 1 steigt nur halb so schnell.", "h": "Wo schneidet der Graph die senkrechte Achse? Und wie viel kosten 100 Minuten?", "bezug": {"thema_schluessel": "funktionen.linear", "lernziel": "graph_ablesen"}}, {"k": "c", "y": "zahl", "f": {"text": "Tarif A kostet 5 € + 0,10 € je Minute, Tarif B 12 € im Monat. Ab wie vielen ganzen Minuten im Monat ist Tarif B günstiger?"}, "o": {"wert": 71}, "c": "(12 - 5) / 0.10 + 1", "w": "B ist günstiger, wenn 5 + 0,10 · x > 12, also 0,10 · x > 7 und x > 70. Ab 71 Minuten ist B günstiger (bei genau 70 Minuten kosten beide 12 €).", "h": "Stelle eine Ungleichung auf: Kosten von A > Kosten von B.", "bezug": {"thema_schluessel": "gleichungen.ungleichungen", "lernziel": "sachaufgabe"}}, {"k": "d", "y": "zahl", "f": {"text": "Tarif B (bisher 12 €) wird 15 % teurer. Tarif A bleibt bei 5 € + 0,10 € je Minute. Ab wie vielen ganzen Minuten ist Tarif B jetzt günstiger?"}, "o": {"wert": 89}, "c": "(12 * 1.15 - 5) / 0.10 + 1", "w": "Neuer Preis von B: 12 € · 1,15 = 13,8 €. B ist günstiger, wenn 5 + 0,10 · x > 13,8, also 0,10 · x > 8,8 und x > 88. Ab 89 Minuten ist B günstiger.", "h": "Rechne zuerst den neuen Preis von B aus (vermehrter Grundwert), dann wie in Teil c.", "bezug": {"thema_schluessel": "bruch.prozent_grundwert", "lernziel": "vermehrt"}}]}'::jsonb;
  falsch jsonb;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;

  -- ---------- H12: Import prüft vorab ----------
  foreach falsch in array array[
      jsonb_set(datei, '{teile}', jsonb_build_array(datei->'teile'->0, datei->'teile'->2)),                                    -- 2 Teile
      jsonb_set(datei, '{teile}', jsonb_build_array(datei->'teile'->0, datei->'teile'->1, datei->'teile'->0 || '{"k": "e"}')), -- nur 1 Thema
      jsonb_set(datei, '{teile,2,bezug,lernziel}', '"gibt_es_nicht"'),                                                         -- Bezug nicht unter den Voraussetzungen
      jsonb_set(jsonb_set(datei, '{teile,2,bezug,lernziel}', '"gibt_es_nicht"'), '{voraussetzungen,2,lernziel}', '"gibt_es_nicht"'), -- Lernkarte gibt es nicht
      jsonb_set(datei, '{teile,1,k}', '"a"')] loop                                                                              -- doppelter Buchstabe
    v_ok := false;
    begin perform schule.expedition_importieren(falsch); exception when others then v_ok := true; end;
    if not v_ok then raise exception 'FEHLER H12: ungültige Datei angenommen: %', left(falsch::text, 120); end if;
  end loop;
  if exists (select 1 from schule.expedition where schluessel = datei->>'schluessel') then raise exception 'FEHLER H12b: ungültiger Import hat geschrieben'; end if;
  raise notice 'ok H12: 2 Teile, 1 Thema, Bezug außerhalb der Voraussetzungen, unbekannte Lernkarte, doppelter Buchstabe → abgelehnt, nichts geschrieben';
  v_ok := false;
  begin
    perform schule.expedition_importieren(
      jsonb_set(jsonb_set(datei, '{teile,3,bezug}', jsonb_build_object('thema_schluessel', (select th.schluessel from schule.thema th join schule.einheit e on e.thema_id = th.id join schule.aufgabe au on au.einheit_id = e.id and au.pool = 'uebung'
                                                                                            where e.status <> 'ersetzt' and not exists (select 1 from schule.einheit e2 where e2.thema_id = th.id and e2.status = 'freigegeben') limit 1),
                                                                        'lernziel', (select au.variante_gruppe from schule.thema th join schule.einheit e on e.thema_id = th.id join schule.aufgabe au on au.einheit_id = e.id and au.pool = 'uebung'
                                                                                     where e.status <> 'ersetzt' and not exists (select 1 from schule.einheit e2 where e2.thema_id = th.id and e2.status = 'freigegeben') limit 1))),
                '{voraussetzungen,3}', (select jsonb_build_object('thema_schluessel', th.schluessel, 'lernziel', au.variante_gruppe) from schule.thema th join schule.einheit e on e.thema_id = th.id join schule.aufgabe au on au.einheit_id = e.id and au.pool = 'uebung'
                                         where e.status <> 'ersetzt' and not exists (select 1 from schule.einheit e2 where e2.thema_id = th.id and e2.status = 'freigegeben') limit 1)),
      'freigegeben');
  exception when others then v_ok := true; end;
  if not v_ok and exists (select 1 from schule.thema th join schule.einheit e on e.thema_id = th.id where e.status <> 'ersetzt' and not exists (select 1 from schule.einheit e2 where e2.thema_id = th.id and e2.status = 'freigegeben')) then
    raise exception 'FEHLER H12c: freigegeben mit nicht freigegebenem Bezugs-Flug angenommen'; end if;
  raise notice 'ok H12c: Status „freigegeben“ nur mit freigegebenen Bezugs-Flügen';
  r := schule.expedition_importieren(datei); v_x := (r->>'expedition_id')::bigint; select * into x from schule.expedition where id = v_x;
  if (r->>'teile_neu')::int <> 4 then raise exception 'FEHLER H12d: gültige Datei nicht importiert: %', r; end if;
  raise notice 'ok H12d: das Beispiel „Handytarif“ (4 Teile, 3 Themen) wird angenommen';

  -- ---------- H14/H15: Expedition über den echten Weg ----------
  for r in select * from jsonb_array_elements(x.voraussetzungen) loop
    insert into schule.karte_stand(lernender_id, einheit_id, lernziel)
      select v_l, e.id, r->>'lernziel' from schule.einheit e where e.thema_id = (r->>'thema_id')::bigint and e.status <> 'ersetzt' order by e.version desc limit 1 on conflict do nothing;
    update schule.karte_stand k set sitzt = true, sitzt_am = now() - interval '3 days', wdh_stufe = 1, wdh_fehler = 0, wdh_ab = now(), wdh_lerntage = 3, faellig_am = now() + interval '3 days', angewandt_am = null
      from schule.einheit e where e.id = k.einheit_id and k.lernender_id = v_l and e.thema_id = (r->>'thema_id')::bigint and k.lernziel = r->>'lernziel';
  end loop;
  select array_agg(id order by reihenfolge) into ids from schule.aufgabe where expedition_id = v_x and freigegeben;
  -- Teil a: zweimal falsch (1. und 2. Versuch)
  select * into a from schule.aufgabe where id = ids[1];
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', a.id, 'client_id', 'hs-a1', 'anlauf', 1, 'antwort', '{"werte": [0, 0]}'::jsonb));
  if not coalesce((r->>'nochmal')::boolean, false) then raise exception 'FEHLER H14a: kein zweiter Versuch: %', r; end if;
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', a.id, 'client_id', 'hs-a2', 'anlauf', 2, 'antwort', '{"werte": [0, 0]}'::jsonb));
  select k.* into ks from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = schule.expedition_etappe(v_l, a) and k.lernziel = a.variante_gruppe;
  if not ks.sitzt or ks.wdh_lerntage <> 1 or not schule.expedition_teil_erledigt(v_l, a.id) then raise exception 'FEHLER H14b: %', row_to_json(ks); end if;
  raise notice 'ok H14a: Teil falsch (beide Versuche) → erledigt, Etappe bleibt gelandet und ist am nächsten Lerntag fällig';
  -- Teile b–d richtig im 1. Versuch
  for v_n in 2..array_length(ids, 1) loop
    select * into a from schule.aufgabe where id = ids[v_n];
    r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', a.id, 'client_id', 'hs-' || v_n, 'anlauf', 1, 'antwort', a.loesung));
    if not (r->>'richtig')::boolean then raise exception 'FEHLER H14c: Teil % mit Lösung nicht richtig: %', v_n, r; end if;
  end loop;
  select k.* into ks from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = schule.expedition_etappe(v_l, a) and k.lernziel = a.variante_gruppe;
  if ks.angewandt_am is null or schule.expedition_zustand(v_l, x) <> 'geschafft' then raise exception 'FEHLER H14d: %', row_to_json(ks); end if;
  r := (select e from jsonb_array_elements(schule.expeditionen_kind(v_l)) e where (e->>'id')::bigint = v_x);
  if (r->>'teile_erledigt')::int <> 4 or (r->>'teile_selbst')::int <> 3 then raise exception 'FEHLER H15: erledigt % / selbst %', r->>'teile_erledigt', r->>'teile_selbst'; end if;
  raise notice 'ok H14b/H15: geschafft; 4 abgeschlossen, davon 3 selbst gelöst (getrennt gemeldet), Beleg „angewandt“ gesetzt';

  -- ---------- H6: Tageszähler aus bestätigten Versuchen in der Zeitzone des Kindes ----------
  v_h0 := schule.heute_selbst(v_l);
  select * into a from schule.aufgabe where pool = 'uebung' and freigegeben and antworttyp = 'auswahl' order by id limit 1;
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', a.id, 'client_id', 'hs-h6a', 'antwort', a.loesung));
  r := schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', a.id, 'client_id', 'hs-h6b', 'hilfe', 1, 'antwort', a.loesung)); -- mit Tipp: zählt nicht
  if schule.heute_selbst(v_l) <> v_h0 + 1 or (r->'karte'->>'heute_selbst')::int <> v_h0 + 1 then raise exception 'FEHLER H6: % → %', v_h0, schule.heute_selbst(v_l); end if;
  update schule.lernender set zeitzone = 'Pacific/Kiritimati' where id = v_l; -- UTC+14: anderer Kalendertag möglich, Zähler folgt dem Tag des Kindes
  raise notice 'ok H6: heute_selbst zählt nur eigene Lösungen (+1, Tipp nicht); Tag des Kindes in Zeitzone % → %', 'UTC+14', schule.heute_selbst(v_l);

  -- ---------- H13: Dosierung der Mischkarten (Server-Teil; Auswahl in der App: tests/lernen.test.cjs „H13“) ----------
  select au.einheit_id into v_n from schule.aufgabe au join schule.einheit e on e.id = au.einheit_id where au.pool = 'uebung' and au.freigegeben and e.status = 'freigegeben' order by au.id limit 1; -- au/xa: a und x sind Variablen
  update schule.lernender set klasse = 5 where id = v_l;
  if (schule.einheit_lesen_intern(v_l, v_n)->>'misch_jede')::int <> 6 then raise exception 'FEHLER H13a: Klasse 5 nicht jede 6.'; end if;
  update schule.lernender set klasse = 8 where id = v_l;
  r := schule.einheit_lesen_intern(v_l, v_n);
  if (r->>'misch_jede')::int <> 4 or (r->>'misch_ab')::int < 3 then raise exception 'FEHLER H13b: Klasse 8: %/%', r->>'misch_jede', r->>'misch_ab'; end if;
  if jsonb_array_length(r->'mischkarten') > 8
     or exists (select 1 from jsonb_array_elements(r->'mischkarten') m join schule.aufgabe xa on xa.id = (m->>'id')::bigint
                 where not xa.freigegeben or xa.pool <> 'uebung' or not exists (select 1 from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = xa.einheit_id and k.lernziel = xa.variante_gruppe and k.sitzt)) then
    raise exception 'FEHLER H13c: Mischkarten: mehr als 8, gesperrt oder aus nicht gelandeter Etappe'; end if;
  raise notice 'ok H13: Klasse 5 → jede 6., Klasse 8 → jede 4., ab % gelandeten; höchstens 8 Mischkarten (hier %), nur freigegeben und aus gelandeten Etappen', r->>'misch_ab', jsonb_array_length(r->'mischkarten');
end $$;
rollback;
