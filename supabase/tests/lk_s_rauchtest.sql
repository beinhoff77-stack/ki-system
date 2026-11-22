-- Rauchtest LK-S (ein Thema in mehreren Klassen). Nach rs_korrektur_2211.sql und 20261123_lk_s_thema_je_klasse.sql.
-- Transaktion mit Rollback, nur Testkind (Schulart/Zweig nur in der Transaktion), keine Namen. Hängt nicht von Kinderdaten ab;
-- die Lehrplan-Erwartungen (RS 8 I Lernbereich 4 = 40 Std., Thema 33 in RS II/III 8 und 9) kommen aus dem Auftrag.
begin;

do $$
declare v_l bigint; r record; w jsonb; x jsonb; v_s0 text; v_s1 text; v_a bigint; v_ea bigint; v_eb bigint; v_neu bigint; v_n int; v_sum0 bigint;
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
  if w->'abdeckung' is null or not (w->'themen'->0 ? 'titel') then raise exception 'FEHLER 1 Matrix: Abdeckung fehlt oder alte Felder weg'; end if;
  raise notice 'ok 1 Thema % in % % Klasse % (neu) und % (weitergeführt), Matrix mit Abdeckung, alte Felder da', r.thema_id, r.schulart, r.zweig, r.k1, r.k2;

  -- 2 Abdeckung RS 8 Gruppe I, Lernbereich 4 = 40 Std.
  select a.stunden, a.stunden_abgedeckt, a.punkte, a.punkte_mit_thema into r from schule.lehrplan_abdeckung a
   where a.schulart = 'rs_by' and a.zweig = 'rs_I' and a.klasse = 8 and a.pfad = '4';
  if r.stunden is distinct from 40 or r.stunden_abgedeckt is distinct from 40 then raise exception 'FEHLER 2 RS 8 I LB 4: % Std., abgedeckt %', r.stunden, r.stunden_abgedeckt; end if;
  if (w->'abdeckung'->'rs_by'->'rs_I'->'8'->>'stunden') is null then raise exception 'FEHLER 2 Abdeckung in der Matrix fehlt'; end if;
  raise notice 'ok 2 RS 8 I Lernbereich 4: 40 Std., abgedeckt 40 (% von % Punkten mit Thema)', r.punkte_mit_thema, r.punkte;

  -- 3 Testkind Realschule Gruppe II/III: lineare Funktionen (33) in 8 und 9; Gruppe I nicht in 9; Stufen unverändert
  update schule.lernender set schulart = 'rs_by', klasse = 8 where id = v_l;
  select md5(string_agg(t.id || ':' || coalesce(schule.thema_stufe(v_l, t.id)::text, ''), '|' order by t.id)) into v_s0 from schule.thema t;
  update schule.lernender set zweig = 'rs_II_III' where id = v_l;
  select md5(string_agg(t.id || ':' || coalesce(schule.thema_stufe(v_l, t.id)::text, ''), '|' order by t.id)) into v_s1 from schule.thema t;
  if v_s0 <> v_s1 then raise exception 'FEHLER 3 Zweig ändert die Stufen'; end if;
  w := schule.lehrplan_matrix_lk(schule.lehrplan_matrix(array[v_l], true), v_l);
  select t into x from jsonb_array_elements(w->'themen') t where (t->>'thema_id')::bigint = 33;
  if w->>'zweig' <> 'rs_II_III' or (select array_agg((c->>'klasse')::int order by (c->>'klasse')::int) from jsonb_array_elements(x->'klassen_kind') c) @> array[8, 9] is not true
     or x ? 'klassen' then raise exception 'FEHLER 3 II/III: %', x->'klassen_kind'; end if;
  update schule.lernender set zweig = 'rs_I' where id = v_l;
  w := schule.lehrplan_matrix_lk(schule.lehrplan_matrix(array[v_l], true), v_l);
  select t into x from jsonb_array_elements(w->'themen') t where (t->>'thema_id')::bigint = 33;
  if exists (select 1 from jsonb_array_elements(x->'klassen_kind') c where (c->>'klasse')::int = 9) then raise exception 'FEHLER 3 Gruppe I mit Klasse 9: %', x->'klassen_kind'; end if;
  w := schule.lehrplan_thema_lk(schule.lehrplan_thema(33, false), 33, v_l, false);
  if jsonb_typeof(w->'klassen_kind') <> 'array' or not (w ? 'baut_auf') or not (w ? 'weiter_in') or not (w ? 'klassen')
     or exists (select 1 from jsonb_array_elements(w->'klassen_kind') c where not (c ? 'etappen_verlangt' and c ? 'etappen_erledigt')) then
    raise exception 'FEHLER 3 Detail: %', w; end if;
  raise notice 'ok 3 Zweig II/III: Thema 33 in 8 und 9, Gruppe I nur 8; Stufen unverändert; Detail mit Klassen, Stand je Klasse, baut_auf, weiter_in';

  -- 4 Befüllen wiederholbar; fehlende Zuordnung und unbekannte Etappe werden gemeldet
  select z.eintrag_id, z.thema_id into r from schule.zuordnung z where z.bezug = 'haupt' order by z.id limit 1;
  w := schule.lehrplan_rolle_setzen(jsonb_build_array(jsonb_build_object('eintrag_id', r.eintrag_id, 'thema_id', r.thema_id, 'rolle', 'weitergefuehrt', 'etappen', 'gibt_es_nicht'),
                                                      jsonb_build_object('eintrag_id', -1, 'thema_id', r.thema_id, 'rolle', 'neu')));
  if jsonb_array_length(w->'ohne_zuordnung') <> 1 or jsonb_array_length(w->'unbekannte_etappen') <> 1 then raise exception 'FEHLER 4 Meldungen: %', w; end if;
  w := schule.lehrplan_rolle_setzen(jsonb_build_array(jsonb_build_object('eintrag_id', r.eintrag_id, 'thema_id', r.thema_id, 'rolle', 'weitergefuehrt')));
  if (w->>'gleich')::int <> 1 or (w->>'gesetzt')::int <> 0 then raise exception 'FEHLER 4 nicht wiederholbar: %', w; end if;
  raise notice 'ok 4 Befüllen wiederholbar, fehlende Zuordnung und unbekannte Etappe gemeldet';

  -- 5 Teilen eines Themas (Probelauf und echter Lauf in der Transaktion) an einem Test-Thema mit Testkind
  insert into schule.thema (fach, schluessel, block, unterthema, reihenfolge, klasse_fest) values ('Mathematik', 'lk_rauchtest.teil1', 'Test', 'Rauchtest Teil 1', 0, '{}')
  returning id into v_a;
  insert into schule.einheit (thema_id, status, inhalt) values (v_a, 'entwurf',
    jsonb_build_object('etappen', jsonb_build_array(jsonb_build_object('lernziel', 'e1', 'titel', 'E1'), jsonb_build_object('lernziel', 'e2', 'titel', 'E2'),
      jsonb_build_object('lernziel', 'e3', 'titel', 'E3'), jsonb_build_object('lernziel', 'e4', 'titel', 'E4'), jsonb_build_object('lernziel', 'e5', 'titel', 'E5'))))
  returning id into v_ea;
  insert into schule.aufgabe (einheit_id, thema_id, art, antworttyp, frage, loesung, pool, variante_gruppe, stufe, freigegeben)
  select v_ea, v_a, 'uebung', 'zahl', '{"text": "Test"}', '{"wert": 1}', 'uebung', 'e' || i, 1, false from generate_series(1, 5) i;
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am) values (v_l, v_ea, 'e3', true, now()), (v_l, v_ea, 'e4', true, now()), (v_l, v_ea, 'e1', true, now());
  insert into schule.sterne (lernender_id, menge, grund, bezug) values (v_l, 80, 'landung', 'landung:' || v_ea || ':e3');
  select coalesce(sum(menge), 0) into v_sum0 from schule.sterne where lernender_id = v_l;
  -- 5a ohne neue Einheit: Thema, Voraussetzung; Lernstand bleibt
  w := schule.thema_teilen(jsonb_build_object('alt_thema', v_a, 'alte_einheit_id', v_ea, 'etappen', jsonb_build_array('e3', 'e4', 'e5'),
         'neu', jsonb_build_object('schluessel', 'lk_rauchtest.teil2', 'unterthema', 'Rauchtest Teil 2')), false);
  v_neu := (w->>'neu_thema')::bigint;
  if not (w->>'einheit_fehlt')::boolean or v_neu is null or not exists (select 1 from schule.voraussetzung where thema_id = v_neu and braucht_id = v_a and art = 'hart')
     or (select count(*) from schule.karte_stand where einheit_id = v_ea) <> 3 then raise exception 'FEHLER 5a: %', w; end if;
  insert into schule.einheit (thema_id, status, inhalt) values (v_neu, 'entwurf',
    jsonb_build_object('etappen', jsonb_build_array(jsonb_build_object('lernziel', 'e3', 'titel', 'E3'), jsonb_build_object('lernziel', 'e4', 'titel', 'E4'),
      jsonb_build_object('lernziel', 'e5', 'titel', 'E5')))) returning id into v_eb;
  -- 5b Probelauf: Bericht, nichts geändert
  w := schule.thema_teilen(jsonb_build_object('alt_thema', v_a, 'alte_einheit_id', v_ea, 'neue_einheit_id', v_eb, 'etappen', jsonb_build_array('e3', 'e4', 'e5'),
         'neu', jsonb_build_object('schluessel', 'lk_rauchtest.teil2', 'unterthema', 'Rauchtest Teil 2')));
  if not (w->>'probelauf')::boolean or (w->'umgehaengt'->>'karte_stand')::int <> 2 or (w->'umgehaengt'->>'aufgabe')::int <> 3
     or (select count(*) from schule.karte_stand where einheit_id = v_eb) <> 0 then raise exception 'FEHLER 5b Probelauf: %', w; end if;
  -- 5c echter Lauf: Karten, Aufgaben, Sterne-Bezug umgehängt, Summe gleich, kein zweiter Bonus
  w := schule.thema_teilen(jsonb_build_object('alt_thema', v_a, 'alte_einheit_id', v_ea, 'neue_einheit_id', v_eb, 'etappen', jsonb_build_array('e3', 'e4', 'e5'),
         'neu', jsonb_build_object('schluessel', 'lk_rauchtest.teil2', 'unterthema', 'Rauchtest Teil 2')), false);
  select count(*) into v_n from schule.karte_stand where lernender_id = v_l and einheit_id = v_eb and sitzt;
  if (w->>'probelauf')::boolean or v_n <> 2 or (select count(*) from schule.karte_stand where einheit_id = v_ea) <> 1
     or (select count(*) from schule.aufgabe where einheit_id = v_eb and thema_id = v_neu) <> 3
     or not exists (select 1 from schule.sterne where lernender_id = v_l and bezug = 'landung:' || v_eb || ':e3')
     or (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l) <> v_sum0
     or exists (select 1 from jsonb_array_elements(w->'kinder') k where (k->>'kind')::bigint = v_l and (k->>'neu_vollstaendig')::boolean) then
    raise exception 'FEHLER 5c Teilen: %', w; end if;
  if schule.landung_bonus(v_l, v_eb, 'e3') is not null then raise exception 'FEHLER 5c zweiter Landungs-Bonus nach dem Umhängen'; end if;
  -- 5d zu wenig Etappen: abgelehnt
  begin
    perform schule.thema_teilen(jsonb_build_object('alt_thema', v_a, 'alte_einheit_id', v_ea, 'etappen', jsonb_build_array('e1', 'e2'),
              'neu', jsonb_build_object('schluessel', 'lk_rauchtest.teil3', 'unterthema', 'x')), false);
    raise exception 'FEHLER 5d zwei Etappen angenommen';
  exception when sqlstate 'P0001' then null;
  end;
  raise notice 'ok 5 Teilen: Schritt 1 ohne Einheit, Probelauf ändert nichts, echter Lauf hängt Karten/Aufgaben/Sterne-Bezug um (Summe gleich, kein zweiter Bonus), < 3 Etappen abgelehnt';
  raise notice 'LK-S Rauchtest durchgelaufen';
end $$;

rollback;
