-- Rauchtest WD-S (Stand WD-S 2). Nach 20261122_wd_s_wiederholungen.sql ausführen. Transaktion mit Rollback, nur Testkind, keine Namen in der Ausgabe.
-- Läuft über die inneren Funktionen (die api-Funktionen rufen genau diese nach der Zugriffsprüfung auf – ein Schlüssel gehört nicht in eine Datei):
--   schule.wdh_runde_groesse, schule.wiederholung_intern, schule.wdh_runde_fertig, schule.flug_wdh_setzen, schule.mischkarten_waehlen, schule.konto_wd;
--   Antworten als Versuch (insert in schule.versuch – die Versuch-Trigger buchen wie bei schule.uebung_pruefen_intern), Ergebnis aus schule.wdh_ergebnis.
-- Karten-Stände, Lerntage, Mischkarten-Ausgaben und Lernstände legt der Test für das Testkind selbst an; aus der Datenbank kommen nur Inhalte.
-- Runden anderer Tage: wiederholung_intern / wdh_runde_fertig mit festem Tag (nur im Test; die api-Funktionen nehmen immer heute_tag).
-- Am Ende: Karten, Lernstände, Plan, Sterne, Stufen und Reiseoptionen aller anderen Kinder vorher = nachher.
begin;

-- Testkind-Karte: Stufe s, Abstand t Lerntage, Beginn vor p_vor_tagen Tagen (Lerntage legt der Test an); p_vor_tagen < t: nicht fällig
create function pg_temp.wd_karte(p_l bigint, p_e bigint, p_lz text, p_stufe int, p_tage int, p_fehler int, p_vor_tagen int) returns void language plpgsql as $f$
begin
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel) values (p_l, p_e, p_lz) on conflict do nothing;
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '200 days', wdh_stufe = p_stufe, wdh_lerntage = p_tage, wdh_fehler = p_fehler,
         wdh_ab = now() - p_vor_tagen * interval '1 day', faellig_am = now() - (p_vor_tagen - p_tage) * interval '1 day', gesetzt_am = null, wdh_gesetzt_am = null
   where lernender_id = p_l and einheit_id = p_e and lernziel = p_lz;
end $f$;
-- Antwort als Versuch (wie uebung_pruefen_intern speichert); Ergebnis der Wiederholung (oder null)
create function pg_temp.wd_antwort(p_l bigint, p_aufgabe bigint, p_richtig boolean, p_misch boolean, p_cid text default null) returns jsonb language plpgsql as $f$
declare v jsonb;
begin
  perform set_config('schule.wdh_ergebnis', '', true);
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr, anlauf, misch)
  values (p_l, p_aufgabe, coalesce(p_cid, 'wd-s-' || gen_random_uuid()), null, p_richtig, case when p_richtig then 1 else 0 end, 1, 0, 1, null, p_misch);
  v := nullif(current_setting('schule.wdh_ergebnis', true), '')::jsonb;
  perform set_config('schule.wdh_ergebnis', '', true);
  return v;
end $f$;
create function pg_temp.wd_aufgabe(p_e bigint, p_lz text) returns bigint language sql as $f$
  select a.id from schule.aufgabe a where a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'uebung' and a.freigegeben order by a.stufe in (2, 3) desc, a.id limit 1 $f$;
create function pg_temp.wd_zuruecksetzen(p_l bigint) returns void language sql as $f$
  update schule.karte_stand set sitzt = false, faellig_am = null, wdh_ab = null, wdh_lerntage = null, wdh_fehler = 0 where lernender_id = p_l $f$;

-- Vorher: alle anderen Kinder (Karten, Lernstände, Plan, Sterne, Stufen, Reiseoptionen)
create temp table wd_andere as
  select 'karte' t, md5(coalesce(string_agg(x::text, '|' order by x::text), '')) s from schule.karte_stand x join schule.lernender l on l.id = x.lernender_id where not l.ist_test
  union all select 'lernziel', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.lernziel_stand x join schule.lernender l on l.id = x.lernender_id where not l.ist_test
  union all select 'route', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.route x join schule.lernender l on l.id = x.lernender_id where not l.ist_test
  union all select 'sterne', md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.sterne x join schule.lernender l on l.id = x.lernender_id where not l.ist_test
  union all select 'stufen', md5(coalesce(string_agg(l.id || ':' || t.id || ':' || schule.thema_stufe(l.id, t.id)::text, '|' order by l.id, t.id), ''))
              from schule.lernender l cross join schule.thema t where not l.ist_test and l.aktiv and t.fach = 'Mathematik'
  union all select 'reise', md5(coalesce(string_agg(l.id || ':' || schule.reiseoptionen(l.id)::text, '|' order by l.id), '')) from schule.lernender l where not l.ist_test and l.aktiv;

-- Etappen mit Aufgabe (Inhalte) für die Massen-Fälle
create temp table wd_pool as
  select row_number() over (order by q.einheit_id, q.lernziel) nr, q.einheit_id, q.lernziel from (
    select distinct a.einheit_id, a.variante_gruppe lernziel from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
     where a.pool = 'uebung' and a.freigegeben and e.status in ('geprueft', 'freigegeben') and e.id = schule.thema_einheit(e.thema_id)) q;

do $$
declare v_l bigint; v_e bigint; v_t bigint; v_lz text[]; v_a1 bigint; v_a2 bigint; v_a3 bigint; r jsonb; w jsonb; v_n int; v_k schule.karte_stand;
  v_e3 bigint; v_t3 bigint; v_kl smallint; v_x jsonb; v_tage int[]; v_gold text; v_fall int; v_soll int; v_tag date; v_heute date; v_s0 int; v_fehler text;
  v_xe bigint; v_xlz text; v_ye bigint; v_ylz text;
begin
  select id, klasse into v_l, v_kl from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  v_heute := schule.heute_tag(v_l);
  update schule.lernender set klasse = 8 where id = v_l;
  insert into schule.lerntag (lernender_id, fach, datum, zeitzone)
  select v_l, 'Mathematik', v_heute - d, coalesce((select zeitzone from schule.lernender where id = v_l), 'UTC') from generate_series(1, 120) d on conflict do nothing;
  perform pg_temp.wd_zuruecksetzen(v_l);

  -- 1 WD-1 Rundengröße (Regeln aus schule.regel)
  if array[schule.wdh_runde_groesse(v_l, 0), schule.wdh_runde_groesse(v_l, 5), schule.wdh_runde_groesse(v_l, 6), schule.wdh_runde_groesse(v_l, 7),
           schule.wdh_runde_groesse(v_l, 20), schule.wdh_runde_groesse(v_l, 41), schule.wdh_runde_groesse(v_l, 60), schule.wdh_runde_groesse(v_l, 100)]
     <> array[0, 5, 6, 6, 6, 9, 12, 12] then raise exception 'FEHLER 1 Rundengröße Klasse 8'; end if;
  update schule.lernender set klasse = 6 where id = v_l;
  if schule.wdh_runde_groesse(v_l, 60) <> 10 or schule.wdh_runde_groesse(v_l, 41) <> 9 then raise exception 'FEHLER 1 Rundengröße bis Klasse 6'; end if;
  update schule.lernender set klasse = 8 where id = v_l;
  raise notice 'ok 1 Rundengröße (0/5/6/7/20/41/60/100 → 0/5/6/6/6/9/12/12; Kl. 6: 60 → 10)';

  -- 2 Runde bei 20/41/60/100 fälligen (je ein eigener Tag): Größe, Pflicht zuerst, mindestens ein Drittel für die ältesten – auch wenn die Hälfte Fehler hat
  if (select count(*) from wd_pool) < 100 then raise exception 'FEHLER 2 Vorbereitung: weniger als 100 Etappen mit Aufgabe'; end if;
  foreach v_fall in array array[20, 41, 60, 100] loop
    perform pg_temp.wd_zuruecksetzen(v_l);
    perform pg_temp.wd_karte(v_l, p.einheit_id, p.lernziel, (p.nr % 4)::int, 1, case when p.nr % 2 = 0 then 1 else 0 end, (10 + p.nr)::int)   -- je größer nr, desto älter
      from wd_pool p where p.nr <= v_fall;
    v_tag := date '2001-01-01' + v_fall;
    r := schule.wiederholung_intern(v_l, '{}'::jsonb, false, v_tag);
    v_soll := schule.wdh_runde_groesse(v_l, v_fall);
    if (r->>'faellig')::int <> v_fall or (r->>'runde')::int <> v_soll or (r->>'runde_offen')::int <> v_soll or (r->>'runde_gemacht')::boolean then
      raise exception 'FEHLER 2 (%): %', v_fall, r - 'aufgaben'; end if;
    select count(*) into v_n from jsonb_array_elements(r->'aufgaben') x where (x->>'pflicht')::boolean;
    if v_n <> v_soll or exists (select 1 from jsonb_array_elements(r->'aufgaben') with ordinality x(j, nr)
                                where not (x.j->>'pflicht')::boolean and x.nr <= v_soll) then raise exception 'FEHLER 2 (%): Pflicht zuerst, % statt %', v_fall, v_n, v_soll; end if;
    -- die ceil(runde/3) ältesten (größte nr) sind alle in der Runde
    if exists (select 1 from wd_pool p where p.nr > v_fall - ceil(v_soll / 3.0) and p.nr <= v_fall
                 and not exists (select 1 from schule.wdh_runde_etappe re where re.lernender_id = v_l and re.tag = v_tag and re.einheit_id = p.einheit_id and re.lernziel = p.lernziel)) then
      raise exception 'FEHLER 2 (%): älteste nicht in der Runde', v_fall; end if;
    raise notice 'ok 2 (% fällig): Runde %, Pflicht zuerst, ein Drittel für die ältesten', v_fall, v_soll;
  end loop;
  perform pg_temp.wd_zuruecksetzen(v_l);

  -- Vorbereitung: ein freigegebener Flug mit mindestens 2 Pflicht-Etappen, je mindestens 3 Übungsaufgaben (Stufe 2/3)
  select e.id, e.thema_id into v_e, v_t from schule.einheit e
   where e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id) and e.block_id is not null
     and jsonb_array_length(coalesce(e.inhalt->'bewertung'->'lernziele_pflicht', '[]'::jsonb)) >= 2
     and not exists (select 1 from jsonb_array_elements_text(e.inhalt->'bewertung'->'lernziele_pflicht') p
                      where (select count(*) from schule.aufgabe a where a.einheit_id = e.id and a.variante_gruppe = p and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3)) < 3)
   order by jsonb_array_length(e.inhalt->'bewertung'->'lernziele_pflicht'), e.id limit 1;
  if v_e is null then raise exception 'FEHLER Vorbereitung: kein passender Flug'; end if;
  select array_agg(p order by p) into v_lz from jsonb_array_elements_text((select inhalt->'bewertung'->'lernziele_pflicht' from schule.einheit where id = v_e)) p;
  select p.einheit_id, p.lernziel into v_xe, v_xlz from wd_pool p where p.einheit_id <> v_e order by p.nr limit 1;
  select p.einheit_id, p.lernziel into v_ye, v_ylz from wd_pool p where p.einheit_id <> v_e and (p.einheit_id, p.lernziel) <> (v_xe, v_xlz) order by p.nr limit 1;
  v_a1 := pg_temp.wd_aufgabe(v_e, v_lz[1]); v_a2 := pg_temp.wd_aufgabe(v_e, v_lz[2]);

  -- 3 Runde heute: festgehalten, zwei Geräte, Abbruch mitten in der Runde, neue Fälligkeit, Server setzt „gemacht“, ohne Mischkarten
  perform pg_temp.wd_karte(v_l, v_e, v_lz[1], 1, 3, 0, 8);
  perform pg_temp.wd_karte(v_l, v_e, v_lz[2], 2, 7, 0, 20);
  perform pg_temp.wd_karte(v_l, v_xe, v_xlz, 0, 1, 0, 5);
  r := schule.wiederholung_intern(v_l, '{}'::jsonb, false);
  w := schule.wiederholung_intern(v_l, '{}'::jsonb, false);                                       -- zweites Gerät
  if (r->>'runde')::int <> 3 or (w->>'runde')::int <> 3
     or (select array_agg((x->>'einheit_id') || '/' || (x->>'lernziel') order by 1) from jsonb_array_elements(r->'aufgaben') x)
        <> (select array_agg((x->>'einheit_id') || '/' || (x->>'lernziel') order by 1) from jsonb_array_elements(w->'aufgaben') x) then
    raise exception 'FEHLER 3 zweites Gerät: %', w - 'aufgaben'; end if;
  w := pg_temp.wd_antwort(v_l, v_a1, true, false);                                             -- 1 von 3
  r := schule.wiederholung_intern(v_l, '{}'::jsonb, false);
  if (r->>'runde_offen')::int <> 2 or (r->>'runde_bearbeitet')::int <> 1 or (r->>'runde_gemacht')::boolean then raise exception 'FEHLER 3 Abbruch: %', r - 'aufgaben'; end if;
  if exists (select 1 from jsonb_array_elements(r->'aufgaben') x where (x->>'pflicht')::boolean and x->>'lernziel' = v_lz[1] and (x->>'einheit_id')::bigint = v_e) then
    raise exception 'FEHLER 3 bearbeitete Etappe noch als Pflicht'; end if;
  begin
    r := schule.wdh_runde_fertig(v_l); v_fehler := 'kein Fehler';
  exception when others then v_fehler := sqlerrm; end;
  if v_fehler = 'kein Fehler' then raise exception 'FEHLER 3 runde_fertig ohne alle Aufgaben'; end if;
  perform pg_temp.wd_karte(v_l, v_ye, v_ylz, 0, 1, 0, 4);                                         -- neue Fälligkeit am selben Tag
  r := schule.wiederholung_intern(v_l, '{}'::jsonb, false);
  if (r->>'runde')::int <> 3 or not exists (select 1 from jsonb_array_elements(r->'aufgaben') x where x->>'lernziel' = v_ylz and (x->>'einheit_id')::bigint = v_ye and not (x->>'pflicht')::boolean) then
    raise exception 'FEHLER 3 neue Fälligkeit nicht freiwillig'; end if;
  w := pg_temp.wd_antwort(v_l, v_a2, false, false);                                            -- falsch = bearbeitet, nicht bestanden
  if (w->>'bestanden')::boolean then raise exception 'FEHLER 3 falsch als bestanden'; end if;
  w := pg_temp.wd_antwort(v_l, pg_temp.wd_aufgabe(v_xe, v_xlz), true, false);
  r := schule.wiederholung_intern(v_l, '{}'::jsonb, false);
  if not (r->>'runde_gemacht')::boolean or (r->>'runde_offen')::int <> 0 then raise exception 'FEHLER 3 Server setzt gemacht nicht: %', r - 'aufgaben'; end if;
  r := schule.wdh_runde_fertig(v_l);
  if not (r->>'runde_gemacht')::boolean then raise exception 'FEHLER 3 runde_fertig'; end if;
  raise notice 'ok 3 Runde heute: festgehalten, zweites Gerät gleich, Abbruch → fortsetzen, Ablehnung vor dem Ende (%), neue Fälligkeit freiwillig, Server setzt gemacht', v_fehler;

  -- 3b Tageswechsel = neue Runde; Etappe ohne Aufgabe zählt als bearbeitet; 0 fällige = sofort gemacht
  v_tag := v_heute + 1;
  r := schule.wiederholung_intern(v_l, '{}'::jsonb, false, v_tag);
  if (r->>'runde_gemacht')::boolean or (select fertig_am from schule.wdh_runde where lernender_id = v_l and tag = v_heute) is null then raise exception 'FEHLER 3b Tageswechsel: %', r - 'aufgaben'; end if;
  insert into schule.wdh_runde_etappe (lernender_id, tag, nr, einheit_id, lernziel) values (v_l, v_tag, 99, v_e, 'wd-s-ohne-aufgabe');
  update schule.wdh_runde set ziel = ziel + 1 where lernender_id = v_l and tag = v_tag;
  update schule.wdh_runde_etappe set bearbeitet_am = now() where lernender_id = v_l and tag = v_tag and lernziel <> 'wd-s-ohne-aufgabe';
  v_n := schule.wdh_runde_pruefen(v_l, v_tag);
  if v_n <> 0 or (select fertig_am from schule.wdh_runde where lernender_id = v_l and tag = v_tag) is null then raise exception 'FEHLER 3b ohne Aufgabe (offen %)', v_n; end if;
  perform pg_temp.wd_zuruecksetzen(v_l);
  r := schule.wiederholung_intern(v_l, '{}'::jsonb, false, v_heute + 2);
  if (r->>'runde')::int <> 0 or not (r->>'runde_gemacht')::boolean or not (schule.wdh_runde_fertig(v_l, v_heute + 2)->>'runde_gemacht')::boolean then raise exception 'FEHLER 3b 0 fällige'; end if;
  raise notice 'ok 3b Tageswechsel = neue Runde, Etappe ohne Aufgabe zählt als bearbeitet, 0 fällige = gemacht';

  -- 4 genau ein Fortschritt und eine Vergütung je Fälligkeit (doppelt gesendete Antwort, zweites Gerät)
  perform pg_temp.wd_karte(v_l, v_e, v_lz[1], 1, 3, 0, 9);
  select coalesce(sum(menge), 0) into v_s0 from schule.sterne where lernender_id = v_l;
  w := pg_temp.wd_antwort(v_l, v_a1, true, false, 'wd-s-geraet-1');
  begin
    w := pg_temp.wd_antwort(v_l, v_a1, true, false, 'wd-s-geraet-1'); v_fehler := 'kein Fehler';       -- dieselbe Antwort noch einmal gesendet
  exception when unique_violation then v_fehler := 'abgewiesen'; end;
  w := pg_temp.wd_antwort(v_l, (select a.id from schule.aufgabe a where a.einheit_id = v_e and a.variante_gruppe = v_lz[1] and a.pool = 'uebung' and a.freigegeben
                                 and a.id <> v_a1 order by a.id limit 1), true, false, 'wd-s-geraet-2');   -- zweites Gerät, andere Bordkarte
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[1];
  if v_fehler <> 'abgewiesen' or w is not null or v_k.wdh_stufe <> 2 then raise exception 'FEHLER 4 Fortschritt: Stufe %, zweites Gerät %, doppelt %', v_k.wdh_stufe, w, v_fehler; end if;
  if (select count(*) from schule.sterne where lernender_id = v_l and grund = 'wdh'
        and bezug = 'wdh:' || v_e || ':' || v_lz[1] || ':' || extract(epoch from now() - interval '9 days')::bigint) <> 1
     or (select count(*) from schule.sterne where lernender_id = v_l and grund = 'wdh' and am = now() and bezug like 'wdh:' || v_e || ':' || v_lz[1] || ':%') <> 2 then  -- Runde (3) + diese Fälligkeit
    raise exception 'FEHLER 4 Vergütung'; end if;
  if exists (select 1 from schule.sterne s where s.lernender_id = v_l and s.grund = 'uebung' and s.bezug = 'aufgabe:' || v_a1 and s.am = now()) then raise exception 'FEHLER 4 doppelt gebucht (uebung)'; end if;
  raise notice 'ok 4 je Fälligkeit genau ein Fortschritt (Stufe 1 → 2) und eine Vergütung; doppelt gesendet abgewiesen, zweites Gerät ohne Fortschritt';

  -- 5 Mischkarten: nicht fällig → nur Beleg; falsch aus fälliger → bleibt fällig, öffnet nicht, zählt als Wiederholungs-Fehler; richtig aus fälliger = bestanden
  select a.id into v_a3 from schule.aufgabe a where a.einheit_id = v_e and a.variante_gruppe = v_lz[2] and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) order by a.id limit 1;
  perform pg_temp.wd_karte(v_l, v_e, v_lz[2], 2, 7, 0, 2);                                        -- nicht fällig
  insert into schule.misch_ausgabe (lernender_id, aufgabe_id, einheit_id, lernziel) values (v_l, v_a3, v_e, v_lz[2]);
  w := pg_temp.wd_antwort(v_l, v_a3, true, true);
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[2];
  if w is not null or v_k.wdh_stufe <> 2 or v_k.misch_ok_am is null or v_k.wdh_lerntage <> 7 then raise exception 'FEHLER 5 nicht fällige Mischkarte: %', w; end if;
  perform pg_temp.wd_karte(v_l, v_e, v_lz[2], 1, 3, 0, 6);                                        -- fällig
  insert into schule.misch_ausgabe (lernender_id, aufgabe_id, einheit_id, lernziel) values (v_l, v_a3, v_e, v_lz[2]);
  w := pg_temp.wd_antwort(v_l, v_a3, false, true);
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[2];
  if w is null or (w->>'bestanden')::boolean or not v_k.sitzt or not schule.karte_faellig(v_k) or not schule.wdh_fehler(v_k) then raise exception 'FEHLER 5 falsche Mischkarte: %', w; end if;
  select a.id into v_a3 from schule.aufgabe a where a.einheit_id = v_e and a.variante_gruppe = v_lz[2] and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and a.id <> v_a3 order by a.id limit 1;
  insert into schule.misch_ausgabe (lernender_id, aufgabe_id, einheit_id, lernziel) values (v_l, v_a3, v_e, v_lz[2]);
  w := pg_temp.wd_antwort(v_l, v_a3, true, true);
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[2];
  if w is null or not (w->>'bestanden')::boolean or v_k.wdh_stufe <> 2 or schule.karte_faellig(v_k) then raise exception 'FEHLER 5 richtige Mischkarte: %', w; end if;
  raise notice 'ok 5 Mischkarten: nicht fällig nur Beleg; falsch bleibt fällig und zählt als Fehler; richtig = bestandene Wiederholung';

  -- 6 letzte Stufe: fünfte Wiederholung bestanden → abgelegt; Sterne Wiederholung + 30 (+ 100 für den Flug), je einmal
  for v_n in 1 .. cardinality(v_lz) loop perform pg_temp.wd_karte(v_l, v_e, v_lz[v_n], 4, 30, 0, 40); end loop;
  for v_n in 1 .. cardinality(v_lz) loop
    select coalesce(sum(menge), 0) into v_s0 from schule.sterne where lernender_id = v_l and grund in ('wdh', 'etappe_abgelegt', 'flug_abgelegt');
    w := pg_temp.wd_antwort(v_l, (select a.id from schule.aufgabe a where a.einheit_id = v_e and a.variante_gruppe = v_lz[v_n] and a.pool = 'uebung' and a.freigegeben order by a.id desc limit 1), true, false);
    v_soll := schule.wd_regel('sterne_wdh_richtig', 10) + schule.wd_regel('sterne_etappe_abgelegt', 30) + case when v_n = cardinality(v_lz) then schule.wd_regel('sterne_flug_abgelegt', 100) else 0 end;
    if not coalesce((w->>'bestanden')::boolean, false) or not (w ? 'abgelegt') or (w->'abgelegt' ? 'flug') <> (v_n = cardinality(v_lz))
       or (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l and grund in ('wdh', 'etappe_abgelegt', 'flug_abgelegt')) - v_s0 <> v_soll then
      raise exception 'FEHLER 6 Etappe %: % (Sterne +%, erwartet %)', v_n, w,
        (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l and grund in ('wdh', 'etappe_abgelegt', 'flug_abgelegt')) - v_s0, v_soll; end if;
  end loop;
  v_gold := coalesce(w->'abgelegt'->>'ort_gold', 'nein');
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[1];
  if v_k.faellig_am is not null or v_k.wdh_ab is not null or not v_k.sitzt or schule.karte_faellig(v_k) or schule.karte_wdh_in(v_k) is not null then raise exception 'FEHLER 6 noch im Takt'; end if;
  if coalesce((w->'abgelegt'->>'ort_gold')::boolean, false) <> exists (select 1 from schule.block_thema bt where bt.thema_id = v_t and not exists (
       select 1 from schule.block_thema bt2 where bt2.block_id = bt.block_id and schule.thema_einheit(bt2.thema_id) is not null and bt2.thema_id <> v_t)) then
    raise exception 'FEHLER 6 ort_gold: %', w->'abgelegt'; end if;
  raise notice 'ok 6 letzte Stufe: Wiederholung + 30 je Etappe, + 100 für den Flug, Ort golden %', v_gold;

  -- 7 Rückfall nach dem Ablegen: beim Üben falsch / im Nachtest durchgefallen → nächster Lerntag, Stufe 2; Gold bleibt; zweites Ablegen gibt nichts
  w := pg_temp.wd_antwort(v_l, v_a1, false, false);
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[1];
  if v_k.wdh_stufe <> 2 or v_k.wdh_lerntage <> 1 or v_k.wdh_ab is null or not v_k.sitzt or schule.karte_faellig(v_k) or schule.karte_wdh_in(v_k) <> 1 then
    raise exception 'FEHLER 7 Rückfall beim Üben: Stufe % Lerntage % fällig in %', v_k.wdh_stufe, v_k.wdh_lerntage, schule.karte_wdh_in(v_k); end if;
  insert into schule.lernziel_stand (lernender_id, einheit_id, lernziel, pflicht, status) values (v_l, v_e, v_lz[2], true, 'nachgewiesen')
  on conflict (lernender_id, einheit_id, lernziel) do update set status = 'nachgewiesen';
  update schule.lernziel_stand set status = 'fehler' where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[2];   -- wie ein nicht bestandener Nachtest
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz[2];
  if v_k.wdh_stufe <> 2 or v_k.wdh_lerntage <> 1 or v_k.wdh_ab is null or schule.karte_wdh_in(v_k) <> 1 then raise exception 'FEHLER 7 Rückfall im Nachtest'; end if;
  if (select count(*) from schule.abgelegt where lernender_id = v_l and bezug in ('etappe:' || v_e || ':' || v_lz[1], 'etappe:' || v_e || ':' || v_lz[2], 'flug:' || v_t)) <> 3 then
    raise exception 'FEHLER 7 Gold weg'; end if;
  perform pg_temp.wd_karte(v_l, v_e, v_lz[2], 4, 30, 0, 40);
  select coalesce(sum(menge), 0) into v_s0 from schule.sterne where lernender_id = v_l and grund in ('etappe_abgelegt', 'flug_abgelegt');
  w := pg_temp.wd_antwort(v_l, v_a2, true, false);
  if w ? 'abgelegt' or (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l and grund in ('etappe_abgelegt', 'flug_abgelegt')) <> v_s0 then
    raise exception 'FEHLER 7 zweites Ablegen: %', w; end if;
  raise notice 'ok 7 Rückfall (Üben, Nachtest): nächster Lerntag, Stufe 2, Gold bleibt; zweites Ablegen ohne Sterne und Einblendung';

  -- 8 Konto/Reisepass
  r := schule.konto_wd(v_l);
  select x into v_x from jsonb_array_elements(r->'fluege') x where (x->>'thema_id')::bigint = v_t;
  if v_x is null or not (v_x->>'abgelegt')::boolean or (v_x->>'etappen_abgelegt')::int <> cardinality(v_lz) or (v_x->>'etappen')::int <> cardinality(v_lz) then raise exception 'FEHLER 8 fluege: %', v_x; end if;
  if exists (select 1 from jsonb_array_elements(r->'orte') o where not (o ? 'gold')) then raise exception 'FEHLER 8 orte ohne gold'; end if;
  raise notice 'ok 8 Konto: Flug abgelegt, Etappen %/%', v_x->>'etappen_abgelegt', v_x->>'etappen';

  -- 9 WD-4 gestaffelt: Regel vorübergehend 2 je Lerntag; ein Flug mit mindestens 5 Etappen wird gesetzt
  perform pg_temp.wd_zuruecksetzen(v_l);
  update schule.regel set wert = '2' where schluessel = 'wdh_gesetzt_je_lerntag';
  select e.id, e.thema_id into v_e3, v_t3 from schule.einheit e
   where e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id) and e.id <> v_e and jsonb_array_length(coalesce(e.inhalt->'etappen', '[]'::jsonb)) >= 5
   order by jsonb_array_length(e.inhalt->'etappen'), e.id limit 1;
  if v_e3 is null then raise exception 'FEHLER 9 Vorbereitung: kein Flug mit 5 Etappen'; end if;
  perform schule.flug_wdh_setzen(v_l, v_t3, 'rauchtest');
  select array_agg(n order by d) into v_tage from (select k.wdh_lerntage d, count(*)::int n from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = v_e3 group by 1) q;
  if exists (select 1 from schule.karte_stand k where k.lernender_id = v_l and k.einheit_id = v_e3 group by k.wdh_lerntage having count(*) > 2)
     or (select min(wdh_lerntage) from schule.karte_stand where lernender_id = v_l and einheit_id = v_e3) <> 1 then raise exception 'FEHLER 9 Staffel: %', v_tage; end if;
  if (select count(*) from schule.karte_stand where lernender_id = v_l and einheit_id = v_e3 and sitzt and wdh_stufe = 0) <> jsonb_array_length((select inhalt->'etappen' from schule.einheit where id = v_e3)) then
    raise exception 'FEHLER 9 nicht alle Etappen gesetzt'; end if;
  r := schule.wiederholung_intern(v_l, '{}'::jsonb, false, v_heute + 3);
  if (r->>'gestaffelt')::int <> (select count(*) from schule.karte_stand where lernender_id = v_l and einheit_id = v_e3 and wdh_lerntage > 1) then raise exception 'FEHLER 9 gestaffelt %', r->'gestaffelt'; end if;
  update schule.regel set wert = '6' where schluessel = 'wdh_gesetzt_je_lerntag';
  raise notice 'ok 9 gesetzter Flug gestaffelt (je Lerntag höchstens 2: %), gestaffelt %', v_tage, r->'gestaffelt';

  -- 10 WD-3 Auswahl: fällige Etappen zuerst
  perform pg_temp.wd_karte(v_l, v_e, v_lz[2], 1, 3, 0, 6);
  r := schule.mischkarten_waehlen(v_l, v_e3, 50);
  if jsonb_array_length(r) = 0 or not (r->0->>'faellig')::boolean then raise exception 'FEHLER 10 Mischkarten: erste nicht fällig'; end if;
  if exists (select 1 from jsonb_array_elements(r) with ordinality x(j, nr) where not (x.j->>'faellig')::boolean
               and exists (select 1 from jsonb_array_elements(r) with ordinality y(j, nr) where (y.j->>'faellig')::boolean and y.nr > x.nr)) then raise exception 'FEHLER 10 Reihenfolge'; end if;
  raise notice 'ok 10 Mischkarten-Auswahl: fällige zuerst';
  update schule.lernender set klasse = v_kl where id = v_l;
end $$;

-- 11 alle anderen Kinder unverändert
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
  if v_t is not null then raise exception 'FEHLER 11 andere Kinder verändert: %', v_t; end if;
  raise notice 'ok 11 andere Kinder: Karten, Lernstände, Plan, Sterne, Stufen, Reiseoptionen unverändert';
  raise notice 'WD-S Rauchtest durchgelaufen';
end $$;

rollback;
