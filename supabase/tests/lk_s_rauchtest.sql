-- Rauchtest LK-S / LK-S 2 (ein Thema in mehreren Klassen). Nach rs_korrektur_2211.sql, lk_korrektur_2211.sql und 20261123_lk_s_thema_je_klasse.sql.
-- Transaktion mit Rollback, nur Testkind (Schulart/Zweig nur in der Transaktion) und Test-Themen, keine Namen. Hängt nicht von Kinderdaten ab;
-- Einträge des Tests mit bearbeitung = 'annahme' (erlaubte Werte laut eintrag_bearbeitung_check). Lehrplan-Erwartungen aus dem Auftrag: RS 8 I Lernbereich 4 = 40 Std.; Thema 33 in RS II/III 8 und 9; Thema 61 in RS I 8 und 9 (klasse_fest 9).
begin;

do $$
declare v_t2 bigint; v_t3 bigint; v_e2 bigint; v_e3 bigint; v_er bigint; v_l bigint; r record; w jsonb; x jsonb; v_s0 text; v_s1 text; v_a bigint; v_ea bigint; v_eb bigint; v_neu bigint; v_n int; v_sum0 bigint;
  v_t bigint; v_te bigint; v_q8 bigint; v_q9 bigint; v_q10 bigint; v_k8 bigint; v_k9 bigint; v_k10 bigint; v_plan jsonb; v_alt text[];
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER Vorbereitung: kein Testkind'; end if;

  -- 1 ein Thema in zwei Klassen (neu + weitergeführt) erscheint in beiden – in der Sicht und in der Matrix
  select k.schulart, k.zweig, k.thema_id, min(k.klasse) k1, max(k.klasse) k2 into r from schule.thema_lage_klasse k
   group by 1, 2, 3 having count(*) >= 2 and bool_or(k.rolle = 'neu') and bool_or(k.rolle = 'weitergefuehrt') order by 3, 1, 2 limit 1;
  if r.thema_id is null then raise exception 'FEHLER 1 kein Thema in zwei Klassen'; end if;
  w := schule.lehrplan_matrix_lk(schule.lehrplan_matrix(array[v_l], false), null);
  select t into x from jsonb_array_elements(w->'themen') t where (t->>'thema_id')::bigint = r.thema_id;
  if not exists (select 1 from jsonb_array_elements(x->'klassen'->r.schulart->r.zweig) c where (c->>'klasse')::int = r.k1 and c->>'rolle' = 'neu')
     or not exists (select 1 from jsonb_array_elements(x->'klassen'->r.schulart->r.zweig) c where (c->>'klasse')::int = r.k2 and c->>'rolle' = 'weitergefuehrt') then
    raise exception 'FEHLER 1 Thema % (% %) nicht in Klasse % und %: %', r.thema_id, r.schulart, r.zweig, r.k1, r.k2, x->'klassen'; end if;
  if w->'lehrplan_zuordnung' is null or not (w->'themen'->0 ? 'titel') then raise exception 'FEHLER 1 Matrix: Lehrplan-Zuordnung fehlt oder alte Felder weg'; end if;
  raise notice 'ok 1 Thema % in % % Klasse % (neu) und % (weitergeführt), Matrix mit Lehrplan-Zuordnung, alte Felder da', r.thema_id, r.schulart, r.zweig, r.k1, r.k2;

  -- 2 Lehrplan-Zuordnung (Stunden mit Themenzuordnung) RS 8 Gruppe I, Lernbereich 4 = 40 Std.
  select a.stunden, a.stunden_zugeordnet, a.punkte, a.punkte_mit_thema into r from schule.lehrplan_abdeckung a
   where a.schulart = 'rs_by' and a.zweig = 'rs_I' and a.klasse = 8 and a.pfad = '4';
  if r.stunden is distinct from 40 or r.stunden_zugeordnet is distinct from 40 then raise exception 'FEHLER 2 RS 8 I LB 4: % Std., zugeordnet %', r.stunden, r.stunden_zugeordnet; end if;
  if (w->'lehrplan_zuordnung'->'rs_by'->'rs_I'->'8'->>'stunden_zugeordnet') is null then raise exception 'FEHLER 2 Lehrplan-Zuordnung in der Matrix fehlt'; end if;
  raise notice 'ok 2 RS 8 I Lernbereich 4: 40 Std., davon 40 mit Themenzuordnung (% von % Punkten)', r.punkte_mit_thema, r.punkte;

  -- 3 B1: Thema 61 in RS I in 8 und 9 – Klasse 8 nicht verschluckt; klasse_fest (9) bleibt Start der Route, Klassen (thema_jahrgang) unverändert
  if (select array_agg(k.klasse order by k.klasse) from schule.thema_lage_klasse k where k.thema_id = 61 and k.schulart = 'rs_by' and k.zweig = 'rs_I') @> array[8, 9] is not true
     or (select k.rolle from schule.thema_lage_klasse k where k.thema_id = 61 and k.schulart = 'rs_by' and k.zweig = 'rs_I' and k.klasse = 8) <> 'neu'
     or (select k.klasse_route from schule.thema_lage_klasse k where k.thema_id = 61 and k.schulart = 'rs_by' and k.zweig = 'rs_I' limit 1) <> 9
     or (schule.thema_jahrgang(61)->>'rs_by')::int <> 9 then
    raise exception 'FEHLER 3 Thema 61: %', (select jsonb_agg(to_jsonb(k) - 'lernbereiche') from schule.thema_lage_klasse k where k.thema_id = 61 and k.schulart = 'rs_by');
  end if;
  w := schule.thema_klassen(61, 'rs_by', 'rs_I');
  if not exists (select 1 from jsonb_array_elements(w->'rs_by'->'rs_I') c where (c->>'klasse')::int = 9 and (c->>'route_start')::boolean) then
    raise exception 'FEHLER 3 route_start fehlt: %', w; end if;
  raise notice 'ok 3 Thema 61 in RS I 8 (neu) und 9 (Start der Route, klasse_fest), Klasse laut thema_jahrgang weiter 9';

  -- 4 Testkind Realschule Gruppe II/III: lineare Funktionen (33) in 8 und 9; Gruppe I nicht in 9; Stufen durch den Zweig unverändert
  update schule.lernender set schulart = 'rs_by', klasse = 8 where id = v_l;
  select md5(string_agg(t.id || ':' || coalesce(schule.thema_stufe(v_l, t.id)::text, ''), '|' order by t.id)) into v_s0 from schule.thema t;
  update schule.lernender set zweig = 'rs_II_III' where id = v_l;
  select md5(string_agg(t.id || ':' || coalesce(schule.thema_stufe(v_l, t.id)::text, ''), '|' order by t.id)) into v_s1 from schule.thema t;
  if v_s0 <> v_s1 then raise exception 'FEHLER 4 Zweig ändert die Stufen'; end if;
  w := schule.lehrplan_matrix_lk(schule.lehrplan_matrix(array[v_l], true), v_l);
  select t into x from jsonb_array_elements(w->'themen') t where (t->>'thema_id')::bigint = 33;
  if w->>'zweig' <> 'rs_II_III' or (select array_agg((c->>'klasse')::int order by (c->>'klasse')::int) from jsonb_array_elements(x->'klassen_kind') c) @> array[8, 9] is not true
     or x ? 'klassen' then raise exception 'FEHLER 4 II/III: %', x->'klassen_kind'; end if;
  update schule.lernender set zweig = 'rs_I' where id = v_l;
  w := schule.lehrplan_matrix_lk(schule.lehrplan_matrix(array[v_l], true), v_l);
  select t into x from jsonb_array_elements(w->'themen') t where (t->>'thema_id')::bigint = 33;
  if exists (select 1 from jsonb_array_elements(x->'klassen_kind') c where (c->>'klasse')::int = 9) then raise exception 'FEHLER 4 Gruppe I mit Klasse 9: %', x->'klassen_kind'; end if;
  w := schule.lehrplan_thema_lk(schule.lehrplan_thema(33, false), 33, v_l, false);
  if jsonb_typeof(w->'klassen_kind') <> 'array' or not (w ? 'baut_auf') or not (w ? 'weiter_in') or not (w ? 'klassen') then raise exception 'FEHLER 4 Detail: %', w; end if;
  raise notice 'ok 4 Zweig II/III: Thema 33 in 8 und 9, Gruppe I nur 8; Stufen unverändert; Detail mit klassen, klassen_kind, baut_auf, weiter_in';

  -- 5 B2: Stand je Klasse nach den genannten Etappen (Test-Thema in RS I 8/9/10): „2 von 3“, „1 von 3“, Klasse mit unbekannten Etappen ohne Zahl
  select lz.quelle_id into v_q8 from schule.lehrplan_zweig lz where lz.schulart = 'rs_by' and lz.zweig = 'rs_I' and lz.klasse = 8 order by 1 limit 1;
  select lz.quelle_id into v_q9 from schule.lehrplan_zweig lz where lz.schulart = 'rs_by' and lz.zweig = 'rs_I' and lz.klasse = 9 order by 1 limit 1;
  select lz.quelle_id into v_q10 from schule.lehrplan_zweig lz where lz.schulart = 'rs_by' and lz.zweig = 'rs_I' and lz.klasse = 10 order by 1 limit 1;
  if v_q8 is null or v_q9 is null or v_q10 is null then raise exception 'FEHLER 5 Vorbereitung: RS-I-Quellen 8/9/10 fehlen'; end if;
  insert into schule.thema (fach, schluessel, block, unterthema, reihenfolge, klasse_fest) values ('Mathematik', 'lk_rauchtest.lage', 'Test', 'Rauchtest Lage', 0, '{}') returning id into v_t;
  insert into schule.einheit (thema_id, status, inhalt) values (v_t, 'geprueft', jsonb_build_object('etappen',
    (select jsonb_agg(jsonb_build_object('lernziel', 'l' || i, 'titel', 'L' || i) order by i) from generate_series(1, 6) i))) returning id into v_te;
  insert into schule.eintrag (quelle_id, pfad, art, text, reihenfolge, bearbeitung) values (v_q8, 'lk-test/k1', 'kompetenz', 'Test', 9999, 'annahme') returning id into v_k8;
  insert into schule.eintrag (quelle_id, pfad, art, text, reihenfolge, bearbeitung) values (v_q9, 'lk-test/k1', 'kompetenz', 'Test', 9999, 'annahme') returning id into v_k9;
  insert into schule.eintrag (quelle_id, pfad, art, text, reihenfolge, bearbeitung) values (v_q10, 'lk-test/k1', 'kompetenz', 'Test', 9999, 'annahme') returning id into v_k10;
  insert into schule.zuordnung (eintrag_id, thema_id, bezug, pruefstatus) values (v_k8, v_t, 'haupt', 'geprueft'), (v_k9, v_t, 'haupt', 'geprueft'), (v_k10, v_t, 'haupt', 'geprueft');
  w := schule.lehrplan_rolle_setzen(jsonb_build_array(jsonb_build_object('eintrag_id', v_k8, 'thema_id', v_t, 'rolle', 'neu', 'etappen', jsonb_build_array('l1', 'l2', 'l3')),
                                                      jsonb_build_object('eintrag_id', v_k9, 'thema_id', v_t, 'rolle', 'weitergefuehrt', 'etappen', 'l4, l5, l6')));
  if (w->>'gesetzt')::int <> 2 then raise exception 'FEHLER 5 Befüllen: %', w; end if;
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am) values (v_l, v_te, 'l1', true, now()), (v_l, v_te, 'l3', true, now()), (v_l, v_te, 'l6', true, now());
  w := schule.thema_klassen_kind(v_t, v_l)->'klassen_kind';
  if (select (c->>'etappen_verlangt')::int || '/' || (c->>'etappen_erledigt')::int from jsonb_array_elements(w) c where (c->>'klasse')::int = 8) <> '3/2'
     or (select (c->>'etappen_verlangt')::int || '/' || (c->>'etappen_erledigt')::int from jsonb_array_elements(w) c where (c->>'klasse')::int = 9) <> '3/1'
     or (select c from jsonb_array_elements(w) c where (c->>'klasse')::int = 10) ?| array['etappen_verlangt', 'etappen_erledigt', 'etappen']
     or not ((select c from jsonb_array_elements(w) c where (c->>'klasse')::int = 10)->>'etappen_unbekannt')::boolean then
    raise exception 'FEHLER 5 Stand je Klasse: %', w; end if;
  if (select g.klasse_ab from schule.thema_lage g where g.thema_id = v_t and g.schulart = 'rs_by' and g.zweig = 'rs_I' and g.lernziel = 'l4') <> 9
     or (select g.klasse_ab from schule.thema_lage g where g.thema_id = v_t and g.schulart = 'rs_by' and g.zweig = 'rs_I' and g.lernziel = 'l1') <> 8 then
    raise exception 'FEHLER 5 Etappe ab Klasse'; end if;
  perform schule.lehrplan_rolle_setzen(jsonb_build_array(jsonb_build_object('eintrag_id', v_k10, 'thema_id', v_t, 'ganzes_thema', true)));   -- ganzes Thema nur ausdrücklich
  w := schule.thema_klassen_kind(v_t, v_l)->'klassen_kind';
  if (select (c->>'etappen_verlangt')::int || '/' || (c->>'etappen_erledigt')::int from jsonb_array_elements(w) c where (c->>'klasse')::int = 10) <> '6/3' then
    raise exception 'FEHLER 5 ganzes Thema: %', w; end if;
  raise notice 'ok 5 Stand je Klasse nach genannten Etappen (8: 2 von 3, 9: 1 von 3), unbekannt ohne Zahl, ganzes Thema nur ausdrücklich (3 von 6)';

  -- 6 B5: unbekannte Etappe, leere Liste und „*“ mit anderen lassen die Zuordnung unverändert; Befüllen wiederholbar
  w := schule.lehrplan_rolle_setzen(jsonb_build_array(
         jsonb_build_object('eintrag_id', v_k8, 'thema_id', v_t, 'rolle', 'weitergefuehrt', 'etappen', jsonb_build_array('l1', 'gibt_es_nicht')),
         jsonb_build_object('eintrag_id', v_k9, 'thema_id', v_t, 'etappen', jsonb_build_array()),
         jsonb_build_object('eintrag_id', v_k10, 'thema_id', v_t, 'etappen', jsonb_build_array('*', 'l1')),
         jsonb_build_object('eintrag_id', -1, 'thema_id', v_t, 'rolle', 'neu')));
  if jsonb_array_length(w->'ohne_zuordnung') <> 1 or jsonb_array_length(w->'unbekannte_etappen') <> 3
     or (select rolle || ':' || array_to_string(etappen, ',') from schule.zuordnung where eintrag_id = v_k8 and thema_id = v_t) <> 'neu:l1,l2,l3' then
    raise exception 'FEHLER 6 Meldungen/unverändert: %', w; end if;
  w := schule.lehrplan_rolle_setzen(jsonb_build_array(jsonb_build_object('eintrag_id', v_k8, 'thema_id', v_t, 'rolle', 'neu', 'etappen', jsonb_build_array('l1', 'l2', 'l3'))));
  if (w->>'gleich')::int <> 1 or (w->>'gesetzt')::int <> 0 then raise exception 'FEHLER 6 nicht wiederholbar: %', w; end if;
  raise notice 'ok 6 unbekannte/leere Etappen: Zuordnung unverändert und gemeldet; Befüllen wiederholbar';

  -- 7 Teilen nach der Teilungsregel (22.11.): drei Teile ohne Mindestzahl (Teil 1: e1–e2, Teil 2: e3, Teil 3: e4–e6), alte Einheit freigegeben
  insert into schule.thema (fach, schluessel, block, unterthema, reihenfolge, klasse_fest) values ('Mathematik', 'lk_rauchtest.teil1', 'Test', 'Rauchtest', 0, '{}')
  returning id into v_a;
  insert into schule.einheit (thema_id, status, inhalt) values (v_a, 'entwurf', jsonb_build_object(
    'etappen', (select jsonb_agg(jsonb_build_object('lernziel', 'e' || i, 'titel', 'E' || i) order by i) from generate_series(1, 6) i),
    'bewertung', jsonb_build_object('lernziele_pflicht', jsonb_build_array('e1', 'e2', 'e3', 'e4', 'e5', 'e6'))))
  returning id into v_ea;
  insert into schule.aufgabe (einheit_id, thema_id, art, antworttyp, frage, loesung, pool, variante_gruppe, stufe, freigegeben)
  select v_ea, v_a, 'uebung', 'zahl', '{"text": "Test"}', '{"wert": 1}', 'uebung', 'e' || i, 2, true from generate_series(1, 6) i;
  update schule.einheit set status = 'freigegeben' where id = v_ea;
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am) values (v_l, v_ea, 'e1', true, now()), (v_l, v_ea, 'e3', true, now()), (v_l, v_ea, 'e4', true, now());
  insert into schule.sterne (lernender_id, menge, grund, bezug) values (v_l, 80, 'landung', 'landung:' || v_ea || ':e4');
  insert into schule.flug_erstabschluss (lernender_id, einheit_id, am) values (v_l, v_ea, now() - interval '1 day');
  insert into schule.misch_ausgabe (lernender_id, aufgabe_id, einheit_id, lernziel)
  select v_l, a.id, null, null from schule.aufgabe a where a.einheit_id = v_ea and a.variante_gruppe = 'e5';
  select coalesce(sum(menge), 0) into v_sum0 from schule.sterne where lernender_id = v_l;
  v_plan := jsonb_build_object('alt_thema', v_a, 'alte_einheit_id', v_ea, 'untertitel', 'Anfang', 'teile', jsonb_build_array(
              jsonb_build_object('etappen', jsonb_build_array('e3'), 'untertitel', 'Mitte', 'neu', jsonb_build_object('schluessel', 'lk_rauchtest.teil2')),
              jsonb_build_object('etappen', jsonb_build_array('e4', 'e5', 'e6'), 'neu', jsonb_build_object('schluessel', 'lk_rauchtest.teil3'))));
  -- 7a Bedingungen: leerer Teil, Etappe in zwei Teilen, Teil 1 leer – abgelehnt
  v_n := 0;
  begin perform schule.thema_teilen(jsonb_set(v_plan, '{teile,0,etappen}', '[]'), false); exception when sqlstate 'P0001' then v_n := v_n + 1; end;
  begin perform schule.thema_teilen(jsonb_set(v_plan, '{teile,0,etappen}', '["e3", "e4"]'), false); exception when sqlstate 'P0001' then v_n := v_n + 1; end;
  begin perform schule.thema_teilen(jsonb_set(v_plan, '{teile,0,etappen}', '["e1", "e2", "e3"]'), false); exception when sqlstate 'P0001' then v_n := v_n + 1; end;
  if v_n <> 3 then raise exception 'FEHLER 7a Bedingungen: nur % von 3 abgelehnt', v_n; end if;
  -- 7b ohne Einheiten: Themen, Benennung „Teil k von 3“, Voraussetzungs-Kette; Lernstand bleibt
  w := schule.thema_teilen(v_plan, false);
  v_t2 := (w->'themen'->>1)::bigint; v_t3 := (w->'themen'->>2)::bigint;
  if not (w->>'einheiten_fehlen')::boolean or (w->>'teile')::int <> 3
     or (select unterthema from schule.thema where id = v_a) <> 'Rauchtest – Teil 1 von 3 · Anfang'
     or (select unterthema from schule.thema where id = v_t2) <> 'Rauchtest – Teil 2 von 3 · Mitte'
     or (select unterthema from schule.thema where id = v_t3) <> 'Rauchtest – Teil 3 von 3'
     or not exists (select 1 from schule.voraussetzung where thema_id = v_t2 and braucht_id = v_a and art = 'hart')
     or not exists (select 1 from schule.voraussetzung where thema_id = v_t3 and braucht_id = v_t2 and art = 'hart')
     or (select count(*) from schule.karte_stand where einheit_id = v_ea) <> 3 then
    raise exception 'FEHLER 7b: %', w; end if;
  -- 7c Einheiten: Rest-Version (e1–e2), Teil 2 (e3), Teil 3 zunächst ohne e6 – abgelehnt; freigegebene alte Einheit ohne Rest-Version – abgelehnt
  insert into schule.einheit (thema_id, version, status, inhalt) values (v_a, 2, 'entwurf', '{"etappen": [{"lernziel": "e1"}, {"lernziel": "e2"}]}') returning id into v_er;
  insert into schule.einheit (thema_id, status, inhalt) values (v_t2, 'entwurf', '{"etappen": [{"lernziel": "e3"}]}') returning id into v_e2;
  insert into schule.einheit (thema_id, status, inhalt) values (v_t3, 'entwurf', '{"etappen": [{"lernziel": "e4"}, {"lernziel": "e5"}]}') returning id into v_e3;
  v_plan := jsonb_set(jsonb_set(v_plan, '{teile,0,einheit_id}', to_jsonb(v_e2)), '{teile,1,einheit_id}', to_jsonb(v_e3));
  v_n := 0;
  begin perform schule.thema_teilen(v_plan || jsonb_build_object('rest_einheit_id', v_er), false); exception when sqlstate 'P0001' then v_n := v_n + 1; end;
  update schule.einheit set inhalt = '{"etappen": [{"lernziel": "e4"}, {"lernziel": "e5"}, {"lernziel": "e6"}]}' where id = v_e3;
  begin perform schule.thema_teilen(v_plan, false); exception when sqlstate 'P0001' then v_n := v_n + 1; end;
  if v_n <> 2 then raise exception 'FEHLER 7c: nur % von 2 abgelehnt', v_n; end if;
  v_plan := v_plan || jsonb_build_object('rest_einheit_id', v_er);
  -- 7d Probelauf: Bericht mit Vorher/Nachher je Kind und Stand je Teil, nichts geändert
  w := schule.thema_teilen(v_plan);
  x := (select k from jsonb_array_elements(w->'kinder') k where (k->>'kind')::bigint = v_l);
  if not (w->>'probelauf')::boolean or (w->'umgehaengt'->>'karte_stand_3')::int <> 1 or (w->'umgehaengt'->>'karte_stand_1')::int <> 1
     or not (x->'bericht_nachher' ?& array['stufen', 'reiseoptionen', 'misch_offen'])
     or not (w->'fest_je_kind'->(v_l::text)->'fest' ?& array['etappen', 'lernziel_stand', 'sterne', 'abgelegt', 'plan', 'flug_abschluesse'])
     or (select string_agg((t->>'etappen_erledigt') || '/' || (t->>'etappen'), ' ' order by (t->>'teil')::int) from jsonb_array_elements(x->'teile') t) <> '1/2 1/1 1/3'
     or (select status from schule.einheit where id = v_ea) <> 'freigegeben' or (select count(*) from schule.karte_stand where einheit_id = v_ea) <> 3 then
    raise exception 'FEHLER 7d Probelauf: %', w; end if;
  -- 7e echter Lauf: alte Einheit ersetzt (Aufgaben bleiben dort), Lernstand in den Teil-Einheiten, Flug-Abschluss zu Teil 1, Sterne-Bezug mitgezogen, Summe gleich
  w := schule.thema_teilen(v_plan, false);
  if (w->>'probelauf')::boolean or (select status from schule.einheit where id = v_ea) <> 'ersetzt'
     or (select count(*) from schule.aufgabe where einheit_id = v_ea) <> 6
     or (select count(*) from schule.karte_stand where lernender_id = v_l and sitzt and ((einheit_id = v_er and lernziel = 'e1') or (einheit_id = v_e2 and lernziel = 'e3') or (einheit_id = v_e3 and lernziel = 'e4'))) <> 3
     or (select count(*) from schule.karte_stand where einheit_id = v_ea) <> 0
     or not exists (select 1 from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_er)
     or not exists (select 1 from schule.sterne where lernender_id = v_l and bezug = 'landung:' || v_e3 || ':e4')
     or (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l) <> v_sum0
     or exists (select 1 from schule.misch_ausgabe m join schule.aufgabe a on a.id = m.aufgabe_id where a.einheit_id = v_ea and m.verfallen_am is null and m.eingeloest_am is null) then
    raise exception 'FEHLER 7e Teilen: %', w; end if;
  if schule.landung_bonus(v_l, v_e3, 'e4') is not null then raise exception 'FEHLER 7e zweiter Landungs-Bonus nach dem Umhängen'; end if;
  raise notice 'ok 7 Teilen in 3 Teile (2 + 1 + 3 Etappen): Bedingungen, „Teil k von 3“, Kette; Probelauf ändert nichts; echter Lauf: alte Einheit ersetzt, Lernstand je Teil, Flug-Abschluss bei Teil 1, Sterne gleich';
  raise notice 'LK-S Rauchtest durchgelaufen';
end $$;

rollback;
