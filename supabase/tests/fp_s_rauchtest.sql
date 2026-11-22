-- Rauchtest FP-S / FP-S 2 (faire Punkte). Nach WD-S 2, WD-S 3, WD-4b, WD-S 4, 20261122_fp_s_faire_punkte.sql und 20261122_fp_s2_nacharbeit_924.sql. Transaktion mit Rollback, nur Testkind, keine Namen.
-- Antworten über den echten Antwortweg schule.uebung_pruefen_wd → uebung_pruefen_intern (Auswahl-Aufgaben: richtig = Index der Lösung).
-- Unabhängig von der Zusammensetzung echter Etappen: nur Etappen, auf die das Testkind nie geantwortet hat; die Landung wird vorbereitet, indem der Test
-- die Karte des Testkinds kurz vor die Landeschwelle setzt (eine eigene Lösung fehlt) – die Landung selbst passiert über den echten Weg.
begin;

create function pg_temp.fp_antwort(p_l bigint, p_a bigint, p_richtig boolean, p_hilfe int default 0, p_anlauf int default null) returns jsonb language plpgsql as $f$
declare a schule.aufgabe; v_i int;
begin
  select * into a from schule.aufgabe where id = p_a;
  v_i := (a.loesung->>'index')::int;
  if not p_richtig then v_i := case when jsonb_typeof(a.antworten) = 'array' and jsonb_array_length(a.antworten) > 1 then (v_i + 1) % jsonb_array_length(a.antworten) else v_i + 1 end; end if;
  return schule.uebung_pruefen_wd(p_l, jsonb_strip_nulls(jsonb_build_object('aufgabe_id', p_a, 'antwort', jsonb_build_object('index', v_i), 'hilfe', p_hilfe,
           'anlauf', p_anlauf::text, 'client_id', 'fp-' || gen_random_uuid())));
end $f$;
-- Karte kurz vor die Landung setzen (eine eigene Lösung und eine in Folge fehlen; Typen und schwere Aufgabe erfüllt)
create function pg_temp.fp_fast(p_l bigint, p_e bigint, p_lz text) returns void language plpgsql as $f$
declare v_ziel int := schule.karte_ziel(p_e, p_lz); v_typen int := schule.karte_typen_noetig(p_e, p_lz);
begin
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel) values (p_l, p_e, p_lz) on conflict do nothing;
  update schule.karte_stand set sitzt = false, gesetzt_am = null, wdh_gesetzt_am = null, eigene_loesungen = greatest(v_ziel - 1, 0), folge = greatest(least(3, v_ziel) - 1, 0),
         typen = coalesce((select array_agg('fp' || i) from generate_series(1, v_typen) i), '{}'), schwer_ok = true, gezaehlt = '{}'::jsonb, fehler_folge = 0
   where lernender_id = p_l and einheit_id = p_e and lernziel = p_lz;
end $f$;

create temp table fp_andere as
  select 'karte' t, md5(coalesce(string_agg(x::text, '|' order by x::text), '')) s from schule.karte_stand x join schule.lernender l on l.id = x.lernender_id where not l.ist_test
  union all select 'lernziel', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x
  union all select 'sterne', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x join schule.lernender l on l.id = x.lernender_id where not l.ist_test
  union all select 'stufen', md5(coalesce(string_agg(l.id || ':' || t.id || ':' || schule.thema_stufe(l.id, t.id)::text, '|' order by l.id, t.id), ''))
              from schule.lernender l cross join schule.thema t where not l.ist_test and l.aktiv and t.fach = 'Mathematik';

do $$
declare v_fehler_soll int[] := array[0, 0, 2, 3]; v_bonus_soll int[] := array[0, 80, 40, 10]; v_stufe_soll text[] := array['', 'ohne', 'wenig', 'sonst'];
  v_l bigint; v_et record; v_e bigint[] := '{}'; v_lz text[] := '{}'; v_ids bigint[]; w jsonb; v_n int; v_i int; v_s0 bigint; r record;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  -- neun Etappen mit mindestens 6 Auswahl-Aufgaben (Stufe 2–3), die das Testkind nie beantwortet hat
  for v_et in select a.einheit_id, a.variante_gruppe lz from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id and e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id)
               where a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and a.antworttyp = 'auswahl' and e.block_id is not null
               group by 1, 2 having count(*) >= 6
                  and not exists (select 1 from schule.versuch v join schule.aufgabe b on b.id = v.aufgabe_id where v.lernender_id = v_l and b.einheit_id = a.einheit_id and b.variante_gruppe = a.variante_gruppe)
                  and not exists (select 1 from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe)
               order by 1, 2 limit 9 loop
    v_e := v_e || v_et.einheit_id; v_lz := v_lz || v_et.lz;
  end loop;
  if cardinality(v_e) < 9 then raise exception 'FEHLER Vorbereitung: keine neun passenden Etappen'; end if;

  -- 1 Regel 1: 10 selbst, 5 mit Tipp, 5 im zweiten Versuch, 0 für eine schon belohnte Aufgabe
  select array_agg(a.id order by a.id) into v_ids from schule.aufgabe a where a.einheit_id = v_e[1] and a.variante_gruppe = v_lz[1] and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and a.antworttyp = 'auswahl';
  w := pg_temp.fp_antwort(v_l, v_ids[1], true);
  if (w->>'sterne')::int <> schule.wd_regel('sterne_uebung_richtig', 10) then raise exception 'FEHLER 1 selbst: %', w; end if;
  w := pg_temp.fp_antwort(v_l, v_ids[2], true, 1);
  if (w->>'sterne')::int <> schule.wd_regel('sterne_uebung_mit_hilfe', 5) then raise exception 'FEHLER 1 mit Tipp: %', w; end if;
  w := pg_temp.fp_antwort(v_l, v_ids[3], false, 0, 1);
  if (w->>'sterne')::int <> 0 then raise exception 'FEHLER 1 erster Anlauf falsch: %', w; end if;
  w := pg_temp.fp_antwort(v_l, v_ids[3], true, 0, 2);
  if (w->>'sterne')::int <> schule.wd_regel('sterne_uebung_mit_hilfe', 5) then raise exception 'FEHLER 1 zweiter Versuch: %', w; end if;
  w := pg_temp.fp_antwort(v_l, v_ids[1], true);
  if (w->>'sterne')::int <> 0 then raise exception 'FEHLER 1 zweimal belohnt: %', w; end if;
  raise notice 'ok 1 Übung: selbst 10, mit Tipp 5, zweiter Versuch 5, dieselbe Aufgabe noch einmal 0';

  -- 2 Landungs-Bonus 80 / 40 / 10 (0 / 2 / 3 endgültige Fehler vor der Landung), Sterne in der Antwort = Übung + Bonus
  for v_i in 2 .. 4 loop
    select array_agg(a.id order by a.id) into v_ids from schule.aufgabe a where a.einheit_id = v_e[v_i] and a.variante_gruppe = v_lz[v_i] and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and a.antworttyp = 'auswahl';
    for v_n in 1 .. v_fehler_soll[v_i] loop
      w := pg_temp.fp_antwort(v_l, v_ids[v_n], false);                                         -- endgültig falsch (ohne zweiten Anlauf)
    end loop;
    perform pg_temp.fp_fast(v_l, v_e[v_i], v_lz[v_i]);
    w := pg_temp.fp_antwort(v_l, v_ids[6], true);
    if not exists (select 1 from schule.karte_stand where lernender_id = v_l and einheit_id = v_e[v_i] and lernziel = v_lz[v_i] and sitzt) then raise exception 'FEHLER 2 Vorbereitung: nicht gelandet'; end if;
    if (w->'landung'->>'bonus')::int is distinct from v_bonus_soll[v_i]
       or w->'landung'->>'stufe' is distinct from v_stufe_soll[v_i]
       or (w->'landung'->>'fehler')::int is distinct from v_fehler_soll[v_i]
       or (w->>'sterne')::int <> (w->'landung'->>'bonus')::int + schule.wd_regel('sterne_uebung_richtig', 10) then
      raise exception 'FEHLER 2 Etappe %: %', v_i, w; end if;
  end loop;
  raise notice 'ok 2 Landungs-Bonus 80 (ohne Fehler) / 40 (2 Fehler) / 10 (3 Fehler); Antwort-Sterne = Übung + Bonus';

  -- 3 genau einmal: erneuter Aufruf (Bonus, Landung speichern, Nachbuchung) bucht nichts
  if schule.landung_bonus(v_l, v_e[2], v_lz[2]) is not null then raise exception 'FEHLER 3 zweiter Bonus'; end if;
  perform schule.landung_speichern(v_l, v_e[2], v_lz[2]);
  if (select count(*) from schule.sterne where lernender_id = v_l and grund = 'landung' and bezug = 'landung:' || v_e[2] || ':' || v_lz[2]) <> 1 then raise exception 'FEHLER 3 mehrfach gebucht'; end if;
  raise notice 'ok 3 Bonus je Etappe genau einmal';

  -- 4 gesetzte Etappe („Kann er“) bekommt keinen Bonus, auch nicht in der Nachbuchung
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel) values (v_l, v_e[5], v_lz[5]) on conflict do nothing;
  update schule.karte_stand set sitzt = true, sitzt_am = now(), gesetzt_am = now(), gesetzt_von = 'rauchtest', landung = null where lernender_id = v_l and einheit_id = v_e[5] and lernziel = v_lz[5];
  if schule.landung_bonus(v_l, v_e[5], v_lz[5]) is not null then raise exception 'FEHLER 4 gesetzte Etappe mit Bonus'; end if;

  -- 5 Nachbuchung: eine früher (ohne Bonus) gelandete Etappe; zweiter Lauf = nichts
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel) values (v_l, v_e[6], v_lz[6]) on conflict do nothing;
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '20 days', gesetzt_am = null, landung = null where lernender_id = v_l and einheit_id = v_e[6] and lernziel = v_lz[6];
  select coalesce(sum(menge), 0) into v_s0 from schule.sterne where lernender_id = v_l;
  select * into r from schule.landung_bonus_nachbuchen(v_l);
  if r.etappen is null or r.etappen < 1 or (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l) - v_s0 <> r.sterne then raise exception 'FEHLER 5 Nachbuchung: %', r; end if;
  if (select menge from schule.sterne where lernender_id = v_l and grund = 'landung' and bezug = 'landung:' || v_e[6] || ':' || v_lz[6]) <> 80 then raise exception 'FEHLER 5 Bonus der Etappe ohne Fehler'; end if;
  if exists (select 1 from schule.sterne where lernender_id = v_l and grund = 'landung' and bezug = 'landung:' || v_e[5] || ':' || v_lz[5]) then raise exception 'FEHLER 5 gesetzte Etappe nachgebucht'; end if;
  select count(*) into v_n from schule.landung_bonus_nachbuchen(v_l);
  if v_n <> 0 or (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l) - v_s0 <> r.sterne then raise exception 'FEHLER 5 zweiter Lauf bucht'; end if;
  if (select etappen from schule.landung_nachbuchung where lernender_id = v_l) <> r.etappen then raise exception 'FEHLER 5 Hinweis für die App'; end if;
  raise notice 'ok 4–5 gesetzte Etappe ohne Bonus; Nachbuchung (% Etappen, % Sterne), zweiter Lauf bucht nichts', r.etappen, r.sterne;

  -- 8 FP-S 2: 1 Fehler, Tipp, zweiter Versuch (vor der Landung), Mischkarte mit Tipp, Fehler nach der Landung, Wiederlandung
  -- 8a 1 endgültiger Fehler → 40 'wenig'; 8b Tipp ist kein Fehler → 80; 8c zweiter Versuch (erster falsch, zweiter richtig) ist kein Fehler → 80
  for v_i in 7 .. 9 loop
    select array_agg(a.id order by a.id) into v_ids from schule.aufgabe a where a.einheit_id = v_e[v_i] and a.variante_gruppe = v_lz[v_i] and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and a.antworttyp = 'auswahl';
    if v_i = 7 then w := pg_temp.fp_antwort(v_l, v_ids[1], false); end if;
    if v_i = 8 then w := pg_temp.fp_antwort(v_l, v_ids[1], true, 1); end if;
    if v_i = 9 then w := pg_temp.fp_antwort(v_l, v_ids[1], false, 0, 1); w := pg_temp.fp_antwort(v_l, v_ids[1], true, 0, 2); end if;
    perform pg_temp.fp_fast(v_l, v_e[v_i], v_lz[v_i]);
    w := pg_temp.fp_antwort(v_l, v_ids[6], true);
    if (w->'landung'->>'bonus')::int is distinct from (array[40, 80, 80])[v_i - 6] or (w->'landung'->>'fehler')::int is distinct from (array[1, 0, 0])[v_i - 6]
       or w->'landung'->>'stufe' is distinct from (array['wenig', 'ohne', 'ohne'])[v_i - 6]
       or (w->>'sterne')::int <> schule.wd_regel('sterne_uebung_richtig', 10) + (w->'landung'->>'bonus')::int then raise exception 'FEHLER 8 Etappe %: %', v_i, w; end if;
  end loop;
  -- 8d Mischkarte mit Tipp aus einer gelandeten Etappe: 0 Sterne (Antwort und Konto gleich)
  select a.id into v_n from schule.aufgabe a where a.einheit_id = v_e[2] and a.variante_gruppe = v_lz[2] and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3)
     and a.antworttyp = 'auswahl' and not exists (select 1 from schule.versuch v where v.lernender_id = v_l and v.aufgabe_id = a.id) order by a.id limit 1;
  insert into schule.misch_ausgabe (lernender_id, aufgabe_id, einheit_id, lernziel) values (v_l, v_n, v_e[3], v_lz[3]);
  select coalesce(sum(menge), 0) into v_s0 from schule.sterne where lernender_id = v_l;
  w := schule.uebung_pruefen_wd(v_l, jsonb_build_object('aufgabe_id', v_n, 'misch', true, 'hilfe', 1, 'client_id', 'fp-m-' || gen_random_uuid(),
         'antwort', jsonb_build_object('index', (select (a.loesung->>'index')::int from schule.aufgabe a where a.id = v_n))));
  if (w->'misch'->>'gueltig')::boolean is distinct from true or (w->>'sterne')::int <> 0 or (w->'misch'->>'sterne')::int <> 0
     or (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l) <> v_s0 then raise exception 'FEHLER 8d Mischkarte mit Tipp: %', w; end if;
  -- 8e Fehler nach der Landung ändert den Bonus nicht
  select array_agg(a.id order by a.id) into v_ids from schule.aufgabe a where a.einheit_id = v_e[2] and a.variante_gruppe = v_lz[2] and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and a.antworttyp = 'auswahl';
  w := pg_temp.fp_antwort(v_l, v_ids[1], false);
  if (w->>'sterne')::int <> 0 or (select count(*) || ':' || sum(menge) from schule.sterne where lernender_id = v_l and grund = 'landung' and bezug = 'landung:' || v_e[2] || ':' || v_lz[2]) <> '1:80' then
    raise exception 'FEHLER 8e Fehler nach der Landung: %', w; end if;
  -- 8f Wiederlandung (Etappe wieder offen, erneut gelandet): kein zweiter Bonus
  update schule.karte_stand set sitzt = false, geoeffnet_am = now() - interval '1 minute', wdh_ab = null, wdh_lerntage = null, faellig_am = null
   where lernender_id = v_l and einheit_id = v_e[3] and lernziel = v_lz[3];
  perform pg_temp.fp_fast(v_l, v_e[3], v_lz[3]);
  select array_agg(a.id order by a.id) into v_ids from schule.aufgabe a where a.einheit_id = v_e[3] and a.variante_gruppe = v_lz[3] and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and a.antworttyp = 'auswahl'
     and not exists (select 1 from schule.versuch v where v.lernender_id = v_l and v.aufgabe_id = a.id);
  w := pg_temp.fp_antwort(v_l, v_ids[1], true);
  if not exists (select 1 from schule.karte_stand where lernender_id = v_l and einheit_id = v_e[3] and lernziel = v_lz[3] and sitzt) then raise exception 'FEHLER 8f Vorbereitung: nicht wieder gelandet'; end if;
  if coalesce(w->'landung', '{}'::jsonb) ? 'bonus' or (w->>'sterne')::int <> schule.wd_regel('sterne_uebung_richtig', 10)
     or (select count(*) from schule.sterne where lernender_id = v_l and grund = 'landung' and bezug = 'landung:' || v_e[3] || ':' || v_lz[3]) <> 1 then raise exception 'FEHLER 8f Wiederlandung: %', w; end if;
  -- 8h Misch-Gültigkeit einmal entschieden: misch_gueltig übernimmt die Entscheidung des Aufrufs für genau diese Aufgabe
  select a.id into v_n from schule.aufgabe a where a.einheit_id = v_e[2] and a.variante_gruppe = v_lz[2] and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3)
     and a.antworttyp = 'auswahl' and not exists (select 1 from schule.versuch v where v.lernender_id = v_l and v.aufgabe_id = a.id) order by a.id limit 1;
  insert into schule.misch_ausgabe (lernender_id, aufgabe_id, einheit_id, lernziel) values (v_l, v_n, v_e[3], v_lz[3]);
  if not schule.misch_gueltig(v_l, (select a from schule.aufgabe a where a.id = v_n), '{"misch": true}') then raise exception 'FEHLER 8h Vorbereitung: Ausgabe nicht gültig'; end if;
  perform set_config('schule.misch_entscheid', v_n || ':f', true);
  if schule.misch_gueltig(v_l, (select a from schule.aufgabe a where a.id = v_n), '{"misch": true}') then raise exception 'FEHLER 8h Entscheidung nicht übernommen'; end if;
  perform set_config('schule.misch_entscheid', '', true);
  -- 8g Nachbuchungs-Hinweis gesehen (Server)
  w := schule.landung_nachbuchung_gesehen(v_l);
  if (w->>'gesehen_am') is null or (select gesehen_am from schule.landung_nachbuchung where lernender_id = v_l) is null then
    raise exception 'FEHLER 8g gesehen'; end if;
  raise notice 'ok 8 FP-S 2: 1 Fehler 40, Tipp 80, zweiter Versuch 80, Mischkarte mit Tipp 0, Fehler nach der Landung ohne Wirkung, Wiederlandung ohne zweiten Bonus, Misch-Gültigkeit einmal entschieden, Hinweis gesehen';

  -- 6 Regeln für die App
  if not (schule.sterne_regeln() ?& array['sterne_uebung_richtig', 'sterne_uebung_mit_hilfe', 'sterne_landung_ohne_fehler', 'sterne_landung_wenig_fehler', 'sterne_landung_sonst', 'landung_wenig_fehler_max']) then
    raise exception 'FEHLER 6 Regeln'; end if;
  raise notice 'ok 6 Regeln für die App';
end $$;

-- 7 Lernstände, Stufen, Karten und Sterne der anderen Kinder unverändert
do $$
declare v_t text;
begin
  select string_agg(v.t, ', ') into v_t from fp_andere v where v.s <> (select case v.t
    when 'karte' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x join schule.lernender l on l.id = x.lernender_id where not l.ist_test)
    when 'lernziel' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x)
    when 'sterne' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x join schule.lernender l on l.id = x.lernender_id where not l.ist_test)
    when 'stufen' then (select md5(coalesce(string_agg(l.id || ':' || t.id || ':' || schule.thema_stufe(l.id, t.id)::text, '|' order by l.id, t.id), ''))
                          from schule.lernender l cross join schule.thema t where not l.ist_test and l.aktiv and t.fach = 'Mathematik') end);
  if v_t is not null then raise exception 'FEHLER 7 verändert: %', v_t; end if;
  raise notice 'ok 7 Lernstände (alle Kinder), Stufen, Karten, Sterne der anderen Kinder unverändert';
  raise notice 'FP-S Rauchtest durchgelaufen';
end $$;

rollback;
