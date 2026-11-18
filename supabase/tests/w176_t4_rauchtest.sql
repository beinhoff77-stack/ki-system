-- Rauchtest W176 Teil 4 (Expeditionen). Erst NACH 20261118_w176_t4_expeditionen.sql (und Teil 1, Teil 3) ausführen.
-- Transaktion mit Rollback: importiert das Beispiel „Handytarif“ als Entwurf, spielt es mit dem Testkind durch und rollt alles zurück. Keine Namen.
begin;
do $$
declare v_l bigint; v_echt bigint; r jsonb; v_x bigint; x schule.expedition; v jsonb; ks schule.karte_stand; -- ks, nicht k: k ist unten Tabellen-Alias a_ids bigint[]; v_n int;
  datei jsonb := '{"schluessel": "8-handytarif", "klasse": {"gym_by": 8}, "titel": "Handytarif", "autor": "Claude (Bau-Auftrag G, Beispiel)", "einleitung": "Du brauchst einen neuen Handytarif. Tarif A kostet 5 € Grundgebühr im Monat und 0,10 € je telefonierter Minute. Tarif B ist eine Flatrate: 12 € im Monat, egal wie lange du telefonierst. Welcher Tarif lohnt sich für dich?", "voraussetzungen": [{"thema_schluessel": "funktionen.linear", "lernziel": "aufstellen"}, {"thema_schluessel": "funktionen.linear", "lernziel": "graph_ablesen"}, {"thema_schluessel": "gleichungen.ungleichungen", "lernziel": "sachaufgabe"}, {"thema_schluessel": "bruch.prozent_grundwert", "lernziel": "vermehrt"}], "teile": [{"k": "a", "y": "luecken", "f": {"text": "Tarif A: 5 € Grundgebühr und 0,10 € je Minute. Stelle den Term für die Kosten K(x) in Cent auf, wenn du x Minuten telefonierst.", "schablone": "□x + □", "hinweis": "Kosten in Cent: zuerst der Preis je Minute, dann die Grundgebühr"}, "o": {"werte": [10, 500]}, "c": ["0.10 * 100", "5 * 100"], "w": "Je Minute kommen 10 Cent dazu, die Grundgebühr sind 500 Cent: K(x) = 10x + 500.", "h": "Rechne erst beides in Cent um: 1 € = 100 Cent.", "bezug": {"thema_schluessel": "funktionen.linear", "lernziel": "aufstellen"}}, {"k": "b", "y": "auswahl", "f": {"text": "Tarif A in Euro: K(x) = 0,10 · x + 5. Welcher Graph gehört zu Tarif A?", "grafik": {"typ": "koordinaten", "x": [0, 120], "y": [0, 20], "schritt_x": 20, "schritt_y": 5, "name_x": "Minuten", "name_y": "€", "graphen": [{"art": "linear", "m": 0.05, "t": 5.0, "name": "1"}, {"art": "linear", "m": 0.1, "t": 5.0, "name": "2"}, {"art": "linear", "m": 0.1, "t": 0, "name": "3"}]}}, "a": ["Graph 1", "Graph 2", "Graph 3"], "o": {"index": 1}, "w": "Tarif A beginnt bei 5 € (bei 0 Minuten) und steigt in 10 Minuten um 1 €: bei 100 Minuten sind es 15 €. Das ist Graph 2. Graph 3 vergisst die Grundgebühr, Graph 1 steigt nur halb so schnell.", "h": "Wo schneidet der Graph die senkrechte Achse? Und wie viel kosten 100 Minuten?", "bezug": {"thema_schluessel": "funktionen.linear", "lernziel": "graph_ablesen"}}, {"k": "c", "y": "zahl", "f": {"text": "Tarif A kostet 5 € + 0,10 € je Minute, Tarif B 12 € im Monat. Ab wie vielen ganzen Minuten im Monat ist Tarif B günstiger?"}, "o": {"wert": 71}, "c": "(12 - 5) / 0.10 + 1", "w": "B ist günstiger, wenn 5 + 0,10 · x > 12, also 0,10 · x > 7 und x > 70. Ab 71 Minuten ist B günstiger (bei genau 70 Minuten kosten beide 12 €).", "h": "Stelle eine Ungleichung auf: Kosten von A > Kosten von B.", "bezug": {"thema_schluessel": "gleichungen.ungleichungen", "lernziel": "sachaufgabe"}}, {"k": "d", "y": "zahl", "f": {"text": "Tarif B (bisher 12 €) wird 15 % teurer. Tarif A bleibt bei 5 € + 0,10 € je Minute. Ab wie vielen ganzen Minuten ist Tarif B jetzt günstiger?"}, "o": {"wert": 89}, "c": "(12 * 1.15 - 5) / 0.10 + 1", "w": "Neuer Preis von B: 12 € · 1,15 = 13,8 €. B ist günstiger, wenn 5 + 0,10 · x > 13,8, also 0,10 · x > 8,8 und x > 88. Ab 89 Minuten ist B günstiger.", "h": "Rechne zuerst den neuen Preis von B aus (vermehrter Grundwert), dann wie in Teil c.", "bezug": {"thema_schluessel": "bruch.prozent_grundwert", "lernziel": "vermehrt"}}]}'::jsonb;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  select id into v_echt from schule.lernender where not ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  r := schule.expedition_importieren(datei);
  v_x := (r->>'expedition_id')::bigint; select * into x from schule.expedition where id = v_x;
  if (r->>'teile_neu')::int <> 4 or x.status <> 'entwurf' then raise exception 'FEHLER 1: %', r; end if;
  raise notice 'ok 1: Import als Entwurf, 4 Teile (%)', r;
  -- Entwurf nur Testkind
  if v_echt is not null and schule.expedition_sichtbar(v_echt, x) then raise exception 'FEHLER 2: Entwurf für ein echtes Kind sichtbar'; end if;
  if not schule.expedition_sichtbar(v_l, x) then raise exception 'FEHLER 2b'; end if;
  raise notice 'ok 2: Entwurf nur für das Testkind sichtbar';
  -- ohne alle Voraussetzungen kein Angebot
  update schule.karte_stand k set sitzt = false from schule.einheit e where e.id = k.einheit_id and k.lernender_id = v_l
     and exists (select 1 from jsonb_array_elements(x.voraussetzungen) vv where (vv->>'thema_id')::bigint = e.thema_id and vv->>'lernziel' = k.lernziel);
  if schule.expedition_zustand(v_l, x) is not null or jsonb_array_length(schule.expeditionen_kind(v_l)) <> 0 then raise exception 'FEHLER 3'; end if;
  -- alle bis auf eine Voraussetzung gelandet → immer noch nicht
  for v in select * from jsonb_array_elements(x.voraussetzungen) loop
    insert into schule.karte_stand(lernender_id, einheit_id, lernziel)
      select v_l, e.id, v->>'lernziel' from schule.einheit e where e.thema_id = (v->>'thema_id')::bigint and e.status <> 'ersetzt' order by e.version desc limit 1 on conflict do nothing;
    update schule.karte_stand k set sitzt = true, sitzt_am = now(), wdh_stufe = 1, wdh_fehler = 0, wdh_ab = now(), wdh_lerntage = 3, faellig_am = now() + interval '3 days', angewandt_am = null
      from schule.einheit e where e.id = k.einheit_id and k.lernender_id = v_l and e.thema_id = (v->>'thema_id')::bigint and k.lernziel = v->>'lernziel';
  end loop;
  update schule.karte_stand k set sitzt = false from schule.einheit e where e.id = k.einheit_id and k.lernender_id = v_l
     and e.thema_id = (x.voraussetzungen->0->>'thema_id')::bigint and k.lernziel = x.voraussetzungen->0->>'lernziel';
  if schule.expedition_zustand(v_l, x) is not null then raise exception 'FEHLER 3b: angeboten ohne alle Voraussetzungen'; end if;
  raise notice 'ok 3: ohne alle Voraussetzungen kein Angebot';
  update schule.karte_stand k set sitzt = true from schule.einheit e where e.id = k.einheit_id and k.lernender_id = v_l
     and e.thema_id = (x.voraussetzungen->0->>'thema_id')::bigint and k.lernziel = x.voraussetzungen->0->>'lernziel';
  if schule.expedition_zustand(v_l, x) <> 'angeboten' then raise exception 'FEHLER 4'; end if;
  raise notice 'ok 4: alle Voraussetzungen gelandet → angeboten';
  select array_agg(id order by reihenfolge) into a_ids from schule.aufgabe where expedition_id = v_x and freigegeben;
  -- Teil a endgültig falsch (2. Versuch) → erledigt, Bezugs-Etappe fällig
  insert into schule.versuch(lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf)
    values (v_l, a_ids[1], 'rauchtest-exp-1', '{}'::jsonb, false, 0, 1, 1, 1, 2);
  select k.* into ks from schule.karte_stand k join schule.aufgabe a on a.einheit_id = k.einheit_id and a.variante_gruppe = k.lernziel where a.id = a_ids[1] and k.lernender_id = v_l;
  if ks.wdh_fehler <> 1 or ks.wdh_lerntage <> 1 or not ks.sitzt then raise exception 'FEHLER 5: %', row_to_json(ks); end if;
  if schule.expedition_zustand(v_l, x) <> 'begonnen' or not schule.expedition_teil_erledigt(v_l, a_ids[1]) then raise exception 'FEHLER 5b'; end if;
  raise notice 'ok 5: Teil falsch → erledigt (Lösung gezeigt), Bezugs-Etappe am nächsten Lerntag fällig, keine Abzüge; Expedition begonnen';
  -- Abbruch: neu laden verliert nichts
  if (select (e->>'teile_erledigt')::int from jsonb_array_elements(schule.expeditionen_kind(v_l)) e where (e->>'id')::bigint = v_x) <> 1 then raise exception 'FEHLER 6'; end if;
  raise notice 'ok 6: nach Abbruch steht Teil a weiter als erledigt da';
  -- Teil b richtig im 1. Versuch → angewandt_am
  insert into schule.versuch(lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf)
    values (v_l, a_ids[2], 'rauchtest-exp-2', '{}'::jsonb, true, 1, 1, 0, 1, 1);
  select k.* into ks from schule.karte_stand k join schule.aufgabe a on a.einheit_id = k.einheit_id and a.variante_gruppe = k.lernziel where a.id = a_ids[2] and k.lernender_id = v_l;
  if ks.angewandt_am is null then raise exception 'FEHLER 7: %', row_to_json(ks); end if;
  raise notice 'ok 7: Teil richtig im 1. Versuch → Beleg „angewandt“';
  -- restliche Teile → geschafft, Sterne einmal
  insert into schule.versuch(lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf)
    select v_l, u, 'rauchtest-exp-' || u, '{}'::jsonb, true, 1, 1, 0, 1, 1 from unnest(a_ids[3:]) u;
  select count(*) into v_n from schule.sterne where lernender_id = v_l and grund = 'expedition' and bezug = 'expedition:' || v_x;
  if schule.expedition_zustand(v_l, x) <> 'geschafft' or v_n <> 1 then raise exception 'FEHLER 8: % / %', schule.expedition_zustand(v_l, x), v_n; end if;
  raise notice 'ok 8: alle Teile erledigt → geschafft, Sterne genau einmal (%), Stempel %', schule.sterne_regel('sterne_expedition_geschafft'), schule.konto(v_l)->'expeditions_stempel';
  -- erneuter Import: nichts geändert; ohne Teil d: Teil d gesperrt, nichts gelöscht
  r := schule.expedition_importieren(datei);
  if (r->>'teile_neu')::int <> 0 or (r->>'teile_geaendert')::int <> 0 then raise exception 'FEHLER 9: %', r; end if;
  r := schule.expedition_importieren(jsonb_set(datei, '{teile}', (datei->'teile') - 3));
  if (r->>'teile_gesperrt')::int <> 1 or (select count(*) from schule.aufgabe where expedition_id = v_x) <> 4 then raise exception 'FEHLER 9b: %', r; end if;
  raise notice 'ok 9: Abgleich ändert nichts ohne Änderung; entfernter Teil wird gesperrt, nicht gelöscht';
end $$;
rollback;
