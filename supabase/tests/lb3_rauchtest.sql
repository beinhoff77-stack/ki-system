-- Rauchtest LB-3 („Kann er – aber wiederholen“, „Wieder in die Wiederholung“, Sammelschritt, Rückgängig, 4 Stufen).
-- Nach 20261120_lb3_kann_wiederholen.sql ausführen. Transaktion mit Rollback, nur Testkind, keine Namen.
-- Läuft über schule.plan_setzen_intern (api.schule_plan_setzen ruft genau diese Funktion nach der Zugriffsprüfung auf – ein Schlüssel gehört nicht in eine Datei),
-- schule.uebung_pruefen_intern, schule.test_starten_intern, schule.einheit_lesen_intern, schule.mischkarten. Aus der Datenbank kommen nur Inhalte (Flüge, Etappen, Bordkarten).
begin;

-- Hilfe nur für diesen Test (pg_temp, verschwindet mit der Sitzung): Einträge für plan_setzen_intern aus Orten und Flug-Listen
create function pg_temp.lb3_eintraege(p_bloecke bigint[], p_kw bigint[], p_ks bigint[], p_ww bigint[]) returns jsonb language sql as $f$
  select jsonb_agg(jsonb_build_object('block_id', b.id,
           'kann_wdh_themen', coalesce((select jsonb_agg(x.t) from unnest(p_kw) x(t) join schule.block_thema bt on bt.thema_id = x.t and bt.block_id = b.id), '[]'::jsonb),
           'kann_schon_themen', coalesce((select jsonb_agg(x.t) from unnest(p_ks) x(t) join schule.block_thema bt on bt.thema_id = x.t and bt.block_id = b.id), '[]'::jsonb),
           'wieder_wdh_themen', coalesce((select jsonb_agg(x.t) from unnest(p_ww) x(t) join schule.block_thema bt on bt.thema_id = x.t and bt.block_id = b.id), '[]'::jsonb))
         order by b.nr)
  from unnest(p_bloecke) with ordinality b(id, nr);
$f$;

do $$
declare v_l bigint; v_t7 bigint[]; v_ta bigint; v_tb bigint; v_bloecke bigint[]; v_es bigint[]; v_e bigint; r jsonb; v_sa bigint; v_sf bigint; v_n int; v_m int;
  v_st0 int; v_tx bigint; v_ex bigint; v_lzx text; v_ax schule.aufgabe; v_tr bigint; v_pre_e bigint; v_pre_lz text; v_ok boolean; v_ts bigint; v_lz text; v_ks schule.karte_stand;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  update schule.karte_stand set sitzt = false where lernender_id = v_l; -- Ausgangslage: nichts gelandet
  update schule.misch_ausgabe set eingeloest_am = now() where lernender_id = v_l and eingeloest_am is null;
  select coalesce(sum(menge) filter (where grund <> 'ort'), 0) into v_st0 from schule.sterne where lernender_id = v_l;

  -- 6 Flüge aus Gym 7 (je genau ein Ort, mit Inhalt), ein Flug aus Gym 8 für „Kann er komplett“, einer aus Gym 8 als „selbst geschafft“
  select array_agg(q.id order by q.id) into v_t7 from (
    select t.id from schule.thema t where (schule.thema_jahrgang(t.id)->>'gym_by')::int = 7 and schule.thema_einheit(t.id) is not null
       and (select count(*) from schule.block_thema bt where bt.thema_id = t.id) = 1 order by t.id limit 6) q;
  select t.id into v_ta from schule.thema t where (schule.thema_jahrgang(t.id)->>'gym_by')::int = 8 and schule.thema_einheit(t.id) is not null
     and (select count(*) from schule.block_thema bt where bt.thema_id = t.id) = 1 order by t.id limit 1;
  select t.id into v_tb from schule.thema t where (schule.thema_jahrgang(t.id)->>'gym_by')::int = 8 and schule.thema_einheit(t.id) is not null and t.id <> v_ta
     and (select count(*) from schule.block_thema bt where bt.thema_id = t.id) = 1
     and not exists (select 1 from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) x where e.id = schule.thema_einheit(t.id)
                      and not exists (select 1 from schule.aufgabe a where a.einheit_id = e.id and a.variante_gruppe = x->>'lernziel'))
     order by t.id limit 1;
  if cardinality(v_t7) <> 6 or v_ta is null or v_tb is null then raise exception 'FEHLER: nicht genug passende Flüge'; end if;
  select array_agg(distinct bt.block_id) into v_bloecke from schule.block_thema bt where bt.thema_id = any(v_t7 || v_ta || v_tb);
  select array_agg(schule.thema_einheit(t)) into v_es from unnest(v_t7) t;
  update schule.karte_stand set sitzt = false, sitzt_am = null, gesetzt_am = null, gesetzt_von = null, wdh_stufe = 0, faellig_am = null, wdh_ab = null, wdh_lerntage = null
   where lernender_id = v_l and einheit_id = any(v_es || schule.thema_einheit(v_ta) || schule.thema_einheit(v_tb));
  -- eine Etappe des ersten Flugs ist schon selbst gelandet – sie muss unberührt bleiben
  select e.id, x->>'lernziel' into v_pre_e, v_pre_lz from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') x where e.id = v_es[1] limit 1;
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) values (v_l, v_pre_e, v_pre_lz) on conflict do nothing;
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '5 days', wdh_stufe = 2, wdh_ab = now() - interval '5 days', wdh_lerntage = 7
   where lernender_id = v_l and einheit_id = v_pre_e and lernziel = v_pre_lz;

  -- ---------- 1. Sammelschritt: 6 Flüge Gym 7 in EINEM Aufruf auf „Kann er – aber wiederholen“ ----------
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', pg_temp.lb3_eintraege(v_bloecke, v_t7, '{}', '{}')), 'lehrer:Rauchtest');
  v_sa := (r->>'schritt_id')::bigint;
  select count(*) into v_n from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) x where e.id = any(v_es);
  select count(*) into v_m from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = any(v_es) and k.sitzt
     and k.lernziel in (select x->>'lernziel' from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') x where e.id = k.einheit_id);
  if v_m <> v_n then raise exception 'FEHLER 1a: % von % Etappen gelandet', v_m, v_n; end if;
  if (select count(*) from schule.karte_stand where lernender_id = v_l and einheit_id = any(v_es) and gesetzt_am is not null) <> v_n - 1 then raise exception 'FEHLER 1b: Herkunft „gesetzt“'; end if;
  select * into v_ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_pre_e and lernziel = v_pre_lz;
  if v_ks.gesetzt_am is not null or v_ks.wdh_stufe <> 2 or v_ks.sitzt_am > now() - interval '4 days' then raise exception 'FEHLER 1c: selbst gelandete Etappe verändert'; end if;
  if exists (select 1 from unnest(v_t7) t where schule.thema_stufe(v_l, t)->>'stufe' <> 'wiederholung' or schule.thema_stufe(v_l, t)->>'gesetzt' <> 'wiederholen' or schule.thema_stand(v_l, t) <> 'erledigt') then
    raise exception 'FEHLER 1d: Stufe %', schule.thema_stufe(v_l, v_t7[2]); end if;
  if exists (select 1 from schule.karte_stand ks where ks.lernender_id = v_l and ks.gesetzt_am is not null and schule.karte_faellig(ks)) then raise exception 'FEHLER 1e: schon heute fällig'; end if;
  update schule.karte_stand set wdh_ab = wdh_ab - interval '1 day', faellig_am = faellig_am - interval '1 day' where lernender_id = v_l and gesetzt_am is not null; -- ein Tag später
  if exists (select 1 from schule.karte_stand ks where ks.lernender_id = v_l and ks.gesetzt_am is not null and not schule.karte_faellig(ks)) then raise exception 'FEHLER 1f: am nächsten Lerntag nicht fällig'; end if;
  raise notice 'ok 1: 6 Flüge in einem Schritt (Schritt %) → % Etappen gelandet (% gesetzt, 1 selbst gelandete unberührt), Stufe ↻, am nächsten Lerntag fällig', v_sa, v_n, v_n - 1;

  -- ---------- 2. kein Flug-Test, kein Nachtest ----------
  r := schule.test_starten_intern(v_l, jsonb_build_object('einheit_id', v_es[1], 'art', 'blocktest'));
  if (r->>'ok')::boolean or not coalesce((r->>'gesetzt')::boolean, false) then raise exception 'FEHLER 2a: Flug-Test gestartet: %', r; end if;
  if schule.nachtest_stand(v_l, v_es[1])->>'grund' <> 'gesetzt' or schule.flug_nachtest(v_l, v_es[1]) is not null
     or not (schule.einheit_lesen_intern(v_l, v_es[1])->>'ohne_test')::boolean then raise exception 'FEHLER 2b'; end if;
  raise notice 'ok 2: kein Flug-Test (ok=false, gesetzt), kein Nachtest (grund gesetzt), flug_nachtest entfällt (null), einheit_lesen.ohne_test';

  -- ---------- 3. Mischkarte möglich ----------
  r := schule.mischkarten(v_l, schule.thema_einheit(v_ta), 20);
  if jsonb_array_length(r) = 0 then raise notice 'Info 3: keine Bordkarte der Stufe 2–3 in diesen Flügen – Mischkarte nicht geprüft';
  elsif exists (select 1 from jsonb_array_elements(r) x join schule.aufgabe a on a.id = (x->>'id')::bigint where not (a.einheit_id = any(v_es))) then raise exception 'FEHLER 3';
  else raise notice 'ok 3: % Mischkarten aus gesetzten Etappen', jsonb_array_length(r); end if;

  -- ---------- 4. zwei Fehler in der Wiederholung → wieder offen (▶) ----------
  select a.* into v_ax from schule.aufgabe a where a.einheit_id = any(v_es) and a.pool = 'uebung' and a.freigegeben and a.antworttyp = 'auswahl'
     and (select count(*) from jsonb_array_elements(coalesce(a.antworten, '[]'::jsonb))) >= 2 and a.einheit_id <> v_pre_e order by a.id limit 1;
  if v_ax.id is null then raise exception 'FEHLER: keine Auswahl-Bordkarte in den Flügen'; end if;
  v_ex := v_ax.einheit_id; v_lzx := v_ax.variante_gruppe; select e.thema_id into v_tx from schule.einheit e where e.id = v_ex;
  for v_n in 1..2 loop
    perform schule.uebung_pruefen_intern(v_l, jsonb_build_object('aufgabe_id', v_ax.id, 'client_id', 'lb3-f' || v_n,
      'antwort', jsonb_build_object('index', ((v_ax.loesung->>'index')::int + 1) % jsonb_array_length(v_ax.antworten))));
  end loop;
  select * into v_ks from schule.karte_stand where lernender_id = v_l and einheit_id = v_ex and lernziel = v_lzx;
  if v_ks.sitzt or v_ks.sitzt_am is null or schule.thema_stufe(v_l, v_tx)->>'stufe' <> 'dran' or (schule.thema_stufe(v_l, v_tx)->>'wieder_offen')::int < 1
     or schule.thema_stand(v_l, v_tx) <> 'laeuft' then raise exception 'FEHLER 4: %', schule.thema_stufe(v_l, v_tx); end if;
  raise notice 'ok 4: zwei Fehler in der Wiederholung → Etappe wieder offen, Flug ▶ (wieder_offen), thema_stand „läuft“';

  -- ---------- 5. Rücknahme eines Flugs (Zustand ohne ihn) ----------
  select t into v_tr from unnest(v_t7) t where t <> v_tx and schule.thema_einheit(t) <> v_pre_e limit 1;
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', pg_temp.lb3_eintraege(v_bloecke, array(select t from unnest(v_t7) t where t <> v_tr), '{}', '{}')), 'lehrer:Rauchtest');
  if exists (select 1 from schule.karte_stand where lernender_id = v_l and einheit_id = schule.thema_einheit(v_tr) and (sitzt or gesetzt_am is not null))
     or schule.thema_stufe(v_l, v_tr)->>'stufe' <> 'kommt' then raise exception 'FEHLER 5: %', schule.thema_stufe(v_l, v_tr); end if;
  raise notice 'ok 5: Rücknahme eines Flugs → gesetzte Landungen aufgehoben (ohne eigene Versuche), Stufe ○';

  -- ---------- 6. Rückgängig des ganzen Sammelschritts ----------
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('rueckgaengig', v_sa, 'eintraege', pg_temp.lb3_eintraege(v_bloecke, '{}', '{}', '{}')), 'lehrer:Rauchtest');
  if exists (select 1 from schule.karte_stand where lernender_id = v_l and einheit_id = any(v_es) and gesetzt_am is not null) then raise exception 'FEHLER 6a: gesetzt bleibt'; end if;
  if exists (select 1 from schule.karte_stand where lernender_id = v_l and einheit_id = any(v_es) and sitzt and not (einheit_id = v_pre_e and lernziel = v_pre_lz)) then raise exception 'FEHLER 6b: Landung bleibt'; end if;
  if not (select sitzt from schule.karte_stand where lernender_id = v_l and einheit_id = v_pre_e and lernziel = v_pre_lz) then raise exception 'FEHLER 6c: selbst gelandete Etappe verloren'; end if;
  if (select richtig + falsch from schule.karte_stand where lernender_id = v_l and einheit_id = v_ex and lernziel = v_lzx) < 2 then raise exception 'FEHLER 6d: eigene Versuche verloren'; end if;
  raise notice 'ok 6: Rückgängig (% Karten zurück) → keine gesetzte Landung mehr, selbst gelandete Etappe und eigene Versuche bleiben', r->>'karten_zurueck';

  -- ---------- 7. Einstellungen schließen einander aus ----------
  v_ok := false;
  begin
    perform schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', pg_temp.lb3_eintraege(v_bloecke, array[v_t7[1]], array[v_t7[1]], '{}')), 'lehrer:Rauchtest');
  exception when sqlstate 'P0001' then v_ok := sqlerrm like 'Ein Flug kann nur eine Einstellung haben%';
  end;
  if not v_ok then raise exception 'FEHLER 7: doppelte Einstellung angenommen'; end if;
  raise notice 'ok 7: Flug zugleich „wiederholen“ und „komplett“ → abgelehnt';

  -- ---------- 8. „Kann er komplett“ (◉) → „Wieder in die Wiederholung“ ----------
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', pg_temp.lb3_eintraege(v_bloecke, '{}', array[v_ta], '{}')), 'lehrer:Rauchtest');
  if schule.thema_stufe(v_l, v_ta)->>'stufe' <> 'komplett' then raise exception 'FEHLER 8a'; end if;
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', pg_temp.lb3_eintraege(v_bloecke, '{}', array[v_ta], array[v_ta])), 'lehrer:Rauchtest');
  if schule.thema_stufe(v_l, v_ta)->>'stufe' <> 'wiederholung' or not schule.thema_kann_wdh(v_l, v_ta) or schule.thema_kann_schon(v_l, v_ta)
     or exists (select 1 from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') x where e.id = schule.thema_einheit(v_ta)
                 and not exists (select 1 from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = e.id and k.lernziel = x->>'lernziel' and k.sitzt and k.wdh_lerntage = 1))
  then raise exception 'FEHLER 8b: %', schule.thema_stufe(v_l, v_ta); end if;
  raise notice 'ok 8: „Kann er komplett“ → Wieder in die Wiederholung = „wiederholen“: alle Etappen gelandet, Stufe 1, ↻';

  -- ---------- 9. selbst geschafft (◉) → „Wieder in die Wiederholung“ und Rückgängig ----------
  v_e := schule.thema_einheit(v_tb);
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) select v_l, v_e, x->>'lernziel' from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') x where e.id = v_e on conflict do nothing;
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '40 days', wdh_stufe = 4, wdh_ab = now() - interval '2 days', wdh_lerntage = 30, faellig_am = now() + interval '28 days',
         misch_ok_am = now() - interval '1 day', gesetzt_am = null where lernender_id = v_l and einheit_id = v_e;
  insert into schule.testsitzung(lernender_id, art, block_id, thema_id, einheit_id, aufgaben, status, punkte, punkte_max, abgeschlossen_am) -- Flug-Test geschrieben
  select v_l, 'blocktest', e.block_id, e.thema_id, e.id, '{}', 'abgeschlossen', 1, 1, now() - interval '30 days' from schule.einheit e where e.id = v_e;
  insert into schule.testsitzung(lernender_id, art, block_id, thema_id, einheit_id, nachtest_runde, aufgaben, status, punkte, punkte_max, ergebnis, abgeschlossen_am)
  select v_l, 'nachtest', e.block_id, e.thema_id, e.id, 1, '{}', 'abgeschlossen', 1, 1, 'bestanden', now() - interval '1 day' from schule.einheit e where e.id = v_e returning id into v_ts;
  for v_lz in select x->>'lernziel' from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') x where e.id = v_e loop
    insert into schule.versuch(lernender_id, aufgabe_id, testsitzung_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr)
    select v_l, a.id, v_ts, 'lb3-nt-' || a.id, null, true, 1, 1, 0, 1 from schule.aufgabe a where a.einheit_id = v_e and a.variante_gruppe = v_lz order by a.id limit 1;
  end loop;
  if schule.thema_stufe(v_l, v_tb)->>'stufe' <> 'komplett' then raise exception 'FEHLER 9a: %', schule.thema_stufe(v_l, v_tb); end if;
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('eintraege', pg_temp.lb3_eintraege(v_bloecke, array[v_ta], '{}', array[v_tb])), 'lehrer:Rauchtest');
  v_sf := (r->>'schritt_id')::bigint;
  if schule.thema_stufe(v_l, v_tb)->>'stufe' <> 'wiederholung' or (schule.thema_stufe(v_l, v_tb)->>'wdh_nr')::int <> 1 or schule.thema_kann_wdh(v_l, v_tb)
     or exists (select 1 from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and (not sitzt or wdh_stufe <> 0 or sitzt_am > now() - interval '39 days')) then
    raise exception 'FEHLER 9b: %', schule.thema_stufe(v_l, v_tb); end if;
  if schule.nachtest_stand(v_l, v_e)->>'grund' = 'gesetzt' then raise exception 'FEHLER 9c: Nachtests eines selbst geschafften Flugs abgeschaltet'; end if;
  r := schule.plan_setzen_intern(v_l, jsonb_build_object('rueckgaengig', v_sf, 'eintraege', pg_temp.lb3_eintraege(v_bloecke, array[v_ta], '{}', '{}')), 'lehrer:Rauchtest');
  if schule.thema_stufe(v_l, v_tb)->>'stufe' <> 'komplett' or exists (select 1 from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and wdh_stufe <> 4) then
    raise exception 'FEHLER 9d: Rückgängig: %', schule.thema_stufe(v_l, v_tb); end if;
  raise notice 'ok 9: selbst geschafft ◉ → Wieder in die Wiederholung: gelandet bleibt, Stufe 1, ↻ (Wdh 1 von 5), Nachtests laufen weiter; Rückgängig → wieder ◉';

  -- ---------- 10. keine Geschenk-Sterne ----------
  if (select coalesce(sum(menge) filter (where grund <> 'ort'), 0) from schule.sterne where lernender_id = v_l) <> v_st0 then raise exception 'FEHLER 10: Sterne außer Ort-Sternen gebucht'; end if;
  raise notice 'ok 10: keine Sterne für gesetzte Landungen (Ort-Sterne wie bei „kann schon“: %)', (select count(*) from schule.sterne where lernender_id = v_l and grund = 'ort');
end $$;
rollback;
