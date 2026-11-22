-- Rauchtest WD-S (Wiederholungen dynamisch). Nach 20261122_wd_s_wiederholungen.sql ausführen. Transaktion mit Rollback, nur Testkind, keine Namen in der Ausgabe.
-- Läuft über die inneren Funktionen (die api-Funktionen rufen genau diese nach der Zugriffsprüfung auf – ein Schlüssel gehört nicht in eine Datei):
--   schule.wdh_runde_groesse, schule.wiederholung_intern, schule.wdh_runde_fertig, schule.flug_wdh_setzen, schule.mischkarten_waehlen, schule.konto_wd;
--   Antworten als Versuch (insert in schule.versuch – die Versuch-Trigger buchen wie bei schule.uebung_pruefen_intern), Ergebnis aus schule.wdh_ergebnis.
-- Karten-Stände, Lerntage, Mischkarten-Ausgaben legt der Test für das Testkind selbst an. Aus der Datenbank kommen nur Inhalte.
-- Am Ende: Karten, Lernstände, Plan, Sterne, Stufen und Reiseoptionen aller anderen Kinder vorher = nachher.
begin;

-- Testkind-Karte fällig machen: Stufe s, Abstand t Lerntage, Beginn vor (t + 2) Tagen (Lerntage legt der Test an)
create function pg_temp.wd_karte(p_l bigint, p_e bigint, p_lz text, p_stufe int, p_tage int, p_fehler int, p_vor_tagen int) returns void language plpgsql as $f$
begin
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel) values (p_l, p_e, p_lz) on conflict do nothing;
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '90 days', wdh_stufe = p_stufe, wdh_lerntage = p_tage, wdh_fehler = p_fehler,
         wdh_ab = now() - p_vor_tagen * interval '1 day', faellig_am = now() - (p_vor_tagen - p_tage) * interval '1 day', gesetzt_am = null, wdh_gesetzt_am = null
   where lernender_id = p_l and einheit_id = p_e and lernziel = p_lz;
end $f$;
-- Antwort als Versuch (wie uebung_pruefen_intern speichert); Ergebnis der Wiederholung (oder null)
create function pg_temp.wd_antwort(p_l bigint, p_aufgabe bigint, p_richtig boolean, p_misch boolean) returns jsonb language plpgsql as $f$
declare v jsonb;
begin
  perform set_config('schule.wdh_ergebnis', '', true);
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf, misch)
  values (p_l, p_aufgabe, 'wd-s-' || gen_random_uuid(), null, p_richtig, case when p_richtig then 1 else 0 end, 1, 0, 1, null, p_misch);
  v := nullif(current_setting('schule.wdh_ergebnis', true), '')::jsonb;
  perform set_config('schule.wdh_ergebnis', '', true);
  return v;
end $f$;

-- Vorher: alle anderen Kinder (Karten, Lernstände, Plan, Sterne, Stufen, Reiseoptionen)
create temp table wd_andere as
  select 'karte' t, md5(coalesce(string_agg(x::text, '|' order by x::text), '')) s from schule.karte_stand x join schule.lernender l on l.id = x.lernender_id where not l.ist_test
  union all select 'lernziel', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x join schule.lernender l on l.id = x.lernender_id where not l.ist_test
  union all select 'route', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.route x join schule.lernender l on l.id = x.lernender_id where not l.ist_test
  union all select 'sterne', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x join schule.lernender l on l.id = x.lernender_id where not l.ist_test
  union all select 'stufen', md5(coalesce(string_agg(l.id || ':' || t.id || ':' || schule.thema_stufe(l.id, t.id)::text, '|' order by l.id, t.id), ''))
              from schule.lernender l cross join schule.thema t where not l.ist_test and l.aktiv and t.fach = 'Mathematik'
  union all select 'reise', md5(coalesce(string_agg(l.id || ':' || schule.reiseoptionen(l.id)::text, '|' order by l.id), '')) from schule.lernender l where not l.ist_test and l.aktiv;

do $$
declare v_l bigint; v_e bigint; v_t bigint; v_b bigint; v_lz text[]; v_a1 bigint; v_a2 bigint; v_a3 bigint; r jsonb; w jsonb; v_n int; v_k schule.karte_stand;
  v_e3 bigint; v_t3 bigint; v_kl smallint; v_x jsonb; v_tage int[]; v_gold text;
begin
  select id, klasse into v_l, v_kl from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;

  -- 1 WD-1 Rundengröße (Regeln aus schule.regel)
  update schule.lernender set klasse = 8 where id = v_l;
  if array[schule.wdh_runde_groesse(v_l, 0), schule.wdh_runde_groesse(v_l, 5), schule.wdh_runde_groesse(v_l, 6), schule.wdh_runde_groesse(v_l, 7),
           schule.wdh_runde_groesse(v_l, 20), schule.wdh_runde_groesse(v_l, 41), schule.wdh_runde_groesse(v_l, 60), schule.wdh_runde_groesse(v_l, 100)]
     <> array[0, 5, 6, 6, 6, 9, 12, 12] then raise exception 'FEHLER 1 Rundengröße Klasse 8'; end if;
  update schule.lernender set klasse = 6 where id = v_l;
  if schule.wdh_runde_groesse(v_l, 60) <> 10 or schule.wdh_runde_groesse(v_l, 41) <> 9 then raise exception 'FEHLER 1 Rundengröße bis Klasse 6'; end if;
  update schule.lernender set klasse = v_kl where id = v_l;
  raise notice 'ok 1 Rundengröße (0/5/6/7/20/41/60/100 → 0/5/6/6/6/9/12/12; Kl. 6: 60 → 10)';

  -- Vorbereitung: ein freigegebener Flug mit mindestens 2 Pflicht-Etappen, je mindestens 2 Übungsaufgaben (Stufe 2/3); Testkind ohne eigene Karten
  select e.id, e.thema_id into v_e, v_t from schule.einheit e
   where e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id) and e.block_id is not null
     and jsonb_array_length(coalesce(e.inhalt->'bewertung'->'lernziele_pflicht', '[]'::jsonb)) >= 2
     and not exists (select 1 from jsonb_array_elements_text(e.inhalt->'bewertung'->'lernziele_pflicht') p
                      where (select count(*) from schule.aufgabe a where a.einheit_id = e.id and a.variante_gruppe = p and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3)) < 3)
   order by jsonb_array_length(e.inhalt->'bewertung'->'lernziele_pflicht'), e.id limit 1;
  if v_e is null then raise exception 'FEHLER Vorbereitung: kein passender Flug'; end if;
  select array_agg(p order by p) into v_lz from jsonb_array_elements_text((select inhalt->'bewertung'->'lernziele_pflicht' from schule.einheit where id = v_e)) p;
  update schule.karte_stand set sitzt = false, faellig_am = null, wdh_ab = null, wdh_lerntage = null where lernender_id = v_l; -- nichts anderes fällig
  insert into schule.lerntag (lernender_id, fach, datum, zeitzone)
  select v_l, 'Mathematik', schule.heute_tag(v_l) - d, coalesce((select zeitzone from schule.lernender where id = v_l), 'UTC') from generate_series(1, 45) d on conflict do nothing;

  -- 2 WD-1 Reihenfolge: Fehler zuerst, dann am längsten fällig, dann niedrigste Stufe; Pflicht = die ersten `runde`
  perform pg_temp.wd_karte(v_l, v_e, v_lz[1], 2, 7, 0, 20);   -- länger fällig, Stufe 2
  perform pg_temp.wd_karte(v_l, v_e, v_lz[2], 1, 3, 1, 5);    -- Wiederholungs-Fehler
  r := schule.wiederholung_intern(v_l, '{}'::jsonb, false);
  if (r->>'faellig')::int <> 2 or (r->>'runde')::int <> 2 or jsonb_array_length(r->'aufgaben') <> 2 then raise exception 'FEHLER 2 faellig/runde: %', r - 'aufgaben'; end if;
  if r->'aufgaben'->0->>'lernziel' <> v_lz[2] or r->'aufgaben'->1->>'lernziel' <> v_lz[1] then raise exception 'FEHLER 2 Reihenfolge (Fehler zuerst)'; end if;
  if not ((r->'aufgaben'->0->>'pflicht')::boolean and (r->'aufgaben'->1->>'pflicht')::boolean) then raise exception 'FEHLER 2 pflicht'; end if;
  if (r->>'runde_gemacht')::boolean or not (r ? 'gestaffelt') then raise exception 'FEHLER 2 runde_gemacht/gestaffelt'; end if;
  if jsonb_array_length(schule.wiederholung_intern(v_l, '{"anzahl": 1}'::jsonb, false)->'aufgaben') <> 1 then raise exception 'FEHLER 2 anzahl'; end if;
  raise notice 'ok 2 Reihenfolge, pflicht, anzahl';

  -- 3 WD-2 Merker
  r := schule.wdh_runde_fertig(v_l);
  r := schule.wdh_runde_fertig(v_l);
  if not (schule.wiederholung_intern(v_l, '{}'::jsonb, false)->>'runde_gemacht')::boolean then raise exception 'FEHLER 3 runde_gemacht'; end if;
  raise notice 'ok 3 Merker „Runde heute gemacht“ (zweimal setzen geht)';

  -- 4 WD-5 bestandene Wiederholung: Stufe +1, wdh-Sterne einmal, keine uebung-Sterne für diesen Versuch
  select a.id into v_a1 from schule.aufgabe a where a.einheit_id = v_e and a.variante_gruppe = v_lz[1] and a.pool = 'uebung' and a.freigegeben order by a.id limit 1;
  w := pg_temp.wd_antwort(v_l, v_a1, true, false);
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[1];
  if w is null or not (w->>'bestanden')::boolean or (w->>'stufe_neu')::int <> 3 or (w->>'naechste_in')::int <> 14 or v_k.wdh_stufe <> 3 then raise exception 'FEHLER 4 Wiederholung: %', w; end if;
  if (w->>'sterne')::int <> schule.wd_regel('sterne_wdh_richtig', 10) then raise exception 'FEHLER 4 Sterne %', w->'sterne'; end if;
  if exists (select 1 from schule.sterne s where s.lernender_id = v_l and s.grund = 'uebung' and s.bezug = 'aufgabe:' || v_a1 and s.am = now()) then raise exception 'FEHLER 4 doppelt gebucht (uebung)'; end if;
  if (select count(*) from schule.sterne s where s.lernender_id = v_l and s.grund = 'wdh' and s.bezug like 'wdh:' || v_e || ':' || v_lz[1] || ':%') <> 1 then raise exception 'FEHLER 4 wdh-Sterne'; end if;
  w := pg_temp.wd_antwort(v_l, v_a1, true, false);   -- nicht mehr fällig: keine Wiederholung, normale Übung
  if w is not null then raise exception 'FEHLER 4 nicht fällige Etappe als Wiederholung: %', w; end if;
  raise notice 'ok 4 bestandene Wiederholung (Stufe 2 → 3, % Sterne einmal, keine Doppelbuchung)', schule.wd_regel('sterne_wdh_richtig', 10);

  -- 5 WD-3 Mischkarte: falsch aus fälliger Etappe bleibt fällig und öffnet nicht; richtig im 1. Versuch ohne Tipp = bestandene Wiederholung
  select a.id into v_a2 from schule.aufgabe a where a.einheit_id = v_e and a.variante_gruppe = v_lz[2] and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) order by a.id limit 1;
  select a.id into v_a3 from schule.aufgabe a where a.einheit_id = v_e and a.variante_gruppe = v_lz[2] and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and a.id <> v_a2 order by a.id limit 1;
  insert into schule.misch_ausgabe (lernender_id, aufgabe_id, einheit_id, lernziel) values (v_l, v_a2, v_e, v_lz[2]);
  w := pg_temp.wd_antwort(v_l, v_a2, false, true);
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[2];
  if w is null or (w->>'bestanden')::boolean or not v_k.sitzt or not schule.karte_faellig(v_k) then raise exception 'FEHLER 5 falsche Mischkarte: % sitzt % fällig %', w, v_k.sitzt, schule.karte_faellig(v_k); end if;
  insert into schule.misch_ausgabe (lernender_id, aufgabe_id, einheit_id, lernziel) values (v_l, v_a3, v_e, v_lz[2]);
  w := pg_temp.wd_antwort(v_l, v_a3, true, true);
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[2];
  if w is null or not (w->>'bestanden')::boolean or v_k.wdh_stufe <> 2 or v_k.misch_ok_am is null or schule.karte_faellig(v_k) then raise exception 'FEHLER 5 richtige Mischkarte: %', w; end if;
  raise notice 'ok 5 Mischkarte: falsch bleibt fällig, richtig = bestandene Wiederholung (Stufe 1 → 2, Beleg gesetzt)';

  -- 6 WD-6 Ablegen: beide Pflicht-Etappen bestehen die Wiederholung auf Stufe 4 (30 Lerntage)
  perform pg_temp.wd_karte(v_l, v_e, v_lz[1], 4, 30, 0, 40);
  perform pg_temp.wd_karte(v_l, v_e, v_lz[2], 4, 30, 0, 40);
  w := pg_temp.wd_antwort(v_l, v_a1, true, false);
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[1];
  if not (w->>'bestanden')::boolean or not (w ? 'abgelegt') or (w->'abgelegt'->'etappe'->>'sterne')::int <> schule.wd_regel('sterne_etappe_abgelegt', 30) or w->'abgelegt' ? 'flug' then
    raise exception 'FEHLER 6 Etappe abgelegt: %', w; end if;
  if v_k.faellig_am is not null or v_k.wdh_ab is not null or not v_k.sitzt or schule.karte_faellig(v_k) or schule.karte_wdh_in(v_k) is not null then raise exception 'FEHLER 6 noch im Takt'; end if;
  -- alle übrigen Pflicht-Etappen ablegen; die letzte legt den Flug ab
  for v_n in 2 .. cardinality(v_lz) loop
    perform pg_temp.wd_karte(v_l, v_e, v_lz[v_n], 4, 30, 0, 40);
    w := pg_temp.wd_antwort(v_l, (select a.id from schule.aufgabe a where a.einheit_id = v_e and a.variante_gruppe = v_lz[v_n] and a.pool = 'uebung' and a.freigegeben order by a.id desc limit 1), true, false);
  end loop;
  v_gold := coalesce(w->'abgelegt'->>'ort_gold', 'nein');
  if not (w->'abgelegt' ? 'flug') or (w->'abgelegt'->'flug'->>'sterne')::int <> schule.wd_regel('sterne_flug_abgelegt', 100) then raise exception 'FEHLER 6 Flug abgelegt: %', w; end if;
  if coalesce((w->'abgelegt'->>'ort_gold')::boolean, false) <> exists (select 1 from schule.block_thema bt where bt.thema_id = v_t and not exists (
       select 1 from schule.block_thema bt2 where bt2.block_id = bt.block_id and schule.thema_einheit(bt2.thema_id) is not null and bt2.thema_id <> v_t)) then
    raise exception 'FEHLER 6 ort_gold: %', w->'abgelegt'; end if;
  if (select count(*) from schule.sterne where lernender_id = v_l and grund = 'flug_abgelegt' and bezug = 'flug:' || v_t) <> 1 then raise exception 'FEHLER 6 Flug-Sterne'; end if;
  -- einmalig: wieder in den Takt (z. B. nach einem Fehler) und erneut bestanden → keine neuen Sterne, keine Einblendung
  perform pg_temp.wd_karte(v_l, v_e, v_lz[1], 4, 30, 0, 40);
  w := pg_temp.wd_antwort(v_l, v_a1, true, false);
  if w ? 'abgelegt' or (select count(*) from schule.sterne where lernender_id = v_l and grund = 'etappe_abgelegt' and bezug = 'etappe:' || v_e || ':' || v_lz[1]) <> 1 then
    raise exception 'FEHLER 6 zweites Ablegen: %', w; end if;
  raise notice 'ok 6 abgelegt: Etappe (% Sterne), Flug (% Sterne), Ort golden %, je einmal', schule.wd_regel('sterne_etappe_abgelegt', 30),
    schule.wd_regel('sterne_flug_abgelegt', 100), v_gold;

  -- 7 Konto/Reisepass
  r := schule.konto_wd(v_l);
  select x into v_x from jsonb_array_elements(r->'fluege') x where (x->>'thema_id')::bigint = v_t;
  if v_x is null or not (v_x->>'abgelegt')::boolean or (v_x->>'etappen_abgelegt')::int <> cardinality(v_lz) or (v_x->>'etappen')::int <> cardinality(v_lz) then raise exception 'FEHLER 7 fluege: %', v_x; end if;
  if exists (select 1 from jsonb_array_elements(r->'orte') o where not (o ? 'gold')) then raise exception 'FEHLER 7 orte ohne gold'; end if;
  raise notice 'ok 7 Konto: Flug abgelegt, Etappen %/%', v_x->>'etappen_abgelegt', v_x->>'etappen';

  -- 8 WD-4 gestaffelt: Regel vorübergehend 2 je Lerntag; ein Flug mit mindestens 5 Etappen wird gesetzt
  update schule.regel set wert = '2' where schluessel = 'wdh_gesetzt_je_lerntag';
  select e.id, e.thema_id into v_e3, v_t3 from schule.einheit e
   where e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id) and e.id <> v_e and jsonb_array_length(coalesce(e.inhalt->'etappen', '[]'::jsonb)) >= 5
   order by jsonb_array_length(e.inhalt->'etappen'), e.id limit 1;
  if v_e3 is null then raise exception 'FEHLER 8 Vorbereitung: kein Flug mit 5 Etappen'; end if;
  -- die Karten des Testkinds sind oben zurückgesetzt (nicht gelandet) – flug_wdh_setzen setzt sie neu
  perform schule.flug_wdh_setzen(v_l, v_t3, 'rauchtest');
  select array_agg(n order by d) into v_tage from (select k.wdh_lerntage d, count(*)::int n from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = v_e3 group by 1) q;
  if exists (select 1 from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = v_e3 group by k.wdh_lerntage having count(*) > 2)
     or (select min(wdh_lerntage) from schule.karte_stand where lernender_id = v_l and einheit_id = v_e3) <> 1 then raise exception 'FEHLER 8 Staffel: %', v_tage; end if;
  if (select count(*) from schule.karte_stand where lernender_id = v_l and einheit_id = v_e3 and sitzt and wdh_stufe = 0) <> jsonb_array_length((select inhalt->'etappen' from schule.einheit where id = v_e3)) then
    raise exception 'FEHLER 8 nicht alle Etappen gesetzt'; end if;
  r := schule.wiederholung_intern(v_l, '{}'::jsonb, false);
  if (r->>'gestaffelt')::int <> (select count(*) from schule.karte_stand where lernender_id = v_l and einheit_id = v_e3 and wdh_lerntage > 1) then raise exception 'FEHLER 8 gestaffelt %', r->'gestaffelt'; end if;
  update schule.regel set wert = '6' where schluessel = 'wdh_gesetzt_je_lerntag';
  raise notice 'ok 8 gesetzter Flug gestaffelt (je Lerntag höchstens 2: %), gestaffelt %', v_tage, r->'gestaffelt';

  -- 9 WD-3 Auswahl: fällige Etappen zuerst
  perform pg_temp.wd_karte(v_l, v_e, v_lz[2], 1, 3, 0, 6);
  r := schule.mischkarten_waehlen(v_l, v_e3, 50);
  if jsonb_array_length(r) = 0 or not (r->0->>'faellig')::boolean then raise exception 'FEHLER 9 Mischkarten: erste nicht fällig'; end if;
  if exists (select 1 from jsonb_array_elements(r) with ordinality x(j, nr) where not (x.j->>'faellig')::boolean
               and exists (select 1 from jsonb_array_elements(r) with ordinality y(j, nr) where (y.j->>'faellig')::boolean and y.nr > x.nr)) then raise exception 'FEHLER 9 Reihenfolge'; end if;
  raise notice 'ok 9 Mischkarten-Auswahl: fällige zuerst';
end $$;

-- 10 alle anderen Kinder unverändert
do $$
declare v_t text;
begin
  select string_agg(v.t, ', ') into v_t from wd_andere v where v.s <> (select case v.t
    when 'karte' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.karte_stand x join schule.lernender l on l.id = x.lernender_id where not l.ist_test)
    when 'lernziel' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x join schule.lernender l on l.id = x.lernender_id where not l.ist_test)
    when 'route' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.route x join schule.lernender l on l.id = x.lernender_id where not l.ist_test)
    when 'sterne' then (select md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x join schule.lernender l on l.id = x.lernender_id where not l.ist_test)
    when 'stufen' then (select md5(coalesce(string_agg(l.id || ':' || t.id || ':' || schule.thema_stufe(l.id, t.id)::text, '|' order by l.id, t.id), ''))
                          from schule.lernender l cross join schule.thema t where not l.ist_test and l.aktiv and t.fach = 'Mathematik')
    when 'reise' then (select md5(coalesce(string_agg(l.id || ':' || schule.reiseoptionen(l.id)::text, '|' order by l.id), '')) from schule.lernender l where not l.ist_test and l.aktiv) end);
  if v_t is not null then raise exception 'FEHLER 10 andere Kinder verändert: %', v_t; end if;
  raise notice 'ok 10 andere Kinder: Karten, Lernstände, Plan, Sterne, Stufen, Reiseoptionen unverändert';
  raise notice 'WD-S Rauchtest durchgelaufen';
end $$;

rollback;
