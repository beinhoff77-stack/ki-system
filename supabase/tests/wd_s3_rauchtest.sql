-- Rauchtest WD-S 3/4 (frische Aufgaben, Mischkarten, „nur selbst“, WD-4b, Nacharbeit 921). Nach 20261122_wd_s_wiederholungen.sql,
-- 20261122_wd_s3_frische_aufgaben.sql, 20261122_wd_4b_stau_strecken.sql und 20261122_wd_s4_nacharbeit_921.sql (fehlt etwas: Abbruch).
-- Transaktion mit Rollback, nur Testkind, keine Namen. Antworten über den echten Antwortweg schule.uebung_pruefen_wd → uebung_pruefen_intern
-- (Auswahl-Aufgaben: richtig = Index der Lösung). „Schon beantwortet“ ohne Buchung legt der Test über eine eigene Testsitzung an.
-- Gewählt werden nur Etappen, auf die das Testkind noch nie geantwortet hat (unabhängig vom Bestand).
begin;

create function pg_temp.w3_karte(p_l bigint, p_e bigint, p_lz text, p_stufe int, p_tage int, p_vor_tagen int) returns void language plpgsql as $f$
begin
  insert into schule.karte_stand (lernender_id, einheit_id, lernziel) values (p_l, p_e, p_lz) on conflict do nothing;
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '200 days', wdh_stufe = p_stufe, wdh_lerntage = p_tage, wdh_fehler = 0,
         wdh_ab = now() - p_vor_tagen * interval '1 day', faellig_am = now() - (p_vor_tagen - p_tage) * interval '1 day', gesetzt_am = null, wdh_gesetzt_am = null
   where lernender_id = p_l and einheit_id = p_e and lernziel = p_lz;
end $f$;
-- Antwort über den echten Weg (Auswahl: Index der Lösung bzw. ein anderer)
create function pg_temp.w3_antwort(p_l bigint, p_a bigint, p_richtig boolean, p_hilfe int, p_anlauf int, p_misch boolean, p_cid text default null,
                                   p_lage_e bigint default null) returns jsonb language plpgsql as $f$
declare a schule.aufgabe; v_i int;
begin
  select * into a from schule.aufgabe where id = p_a;
  v_i := (a.loesung->>'index')::int;
  if not p_richtig then v_i := case when jsonb_typeof(a.antworten) = 'array' and jsonb_array_length(a.antworten) > 1 then (v_i + 1) % jsonb_array_length(a.antworten) else v_i + 1 end; end if;
  return schule.uebung_pruefen_wd(p_l, jsonb_strip_nulls(jsonb_build_object('aufgabe_id', p_a, 'antwort', jsonb_build_object('index', v_i), 'hilfe', p_hilfe,
           'anlauf', p_anlauf::text, 'misch', p_misch, 'client_id', coalesce(p_cid, 'w3-' || gen_random_uuid()))));
end $f$;
-- „beantwortet“ ohne Buchung (Testsitzung): am Zeitpunkt p_am
create function pg_temp.w3_gesehen(p_l bigint, p_a bigint, p_am timestamptz) returns void language plpgsql as $f$
declare v_s bigint; a schule.aufgabe;
begin
  select * into a from schule.aufgabe where id = p_a;
  insert into schule.testsitzung (lernender_id, art, einheit_id, thema_id, aufgaben, status, punkte_max, gestartet_am)
  values (p_l, 'blocktest', a.einheit_id, a.thema_id, array[p_a], 'laeuft', 1, p_am) returning id into v_s;
  insert into schule.versuch (lernender_id, aufgabe_id, testsitzung_id, client_id, richtig, punkte, punkte_max, hilfe, versuch_nr, am)
  values (p_l, p_a, v_s, 'w3-gesehen-' || gen_random_uuid(), true, 1, 1, 0, 1, p_am);
end $f$;

do $$
declare v_l bigint; v_e bigint; v_lz text; v_e2 bigint; v_lz2 text; v_ids bigint[]; r jsonb; w jsonb; v_k schule.karte_stand; v_ab date; v_n int; v_x bigint;
  v_fehler text; v_m bigint;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  update schule.karte_stand set sitzt = false, faellig_am = null, wdh_ab = null, wdh_lerntage = null, wdh_fehler = 0 where lernender_id = v_l;
  insert into schule.lerntag (lernender_id, fach, datum, zeitzone)
  select v_l, 'Mathematik', schule.heute_tag(v_l) - d, coalesce((select zeitzone from schule.lernender where id = v_l), 'UTC') from generate_series(1, 60, 3) d on conflict do nothing;
  -- zwei Etappen (verschiedene Flüge) mit mindestens 4 Auswahl-Aufgaben der Stufen 2–3, die das Testkind nie beantwortet hat
  select q.einheit_id, q.lz into v_e, v_lz from (
    select a.einheit_id, a.variante_gruppe lz from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id and e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id)
     where a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and a.antworttyp = 'auswahl' and e.block_id is not null
     group by 1, 2 having count(*) >= 4
        and not exists (select 1 from schule.versuch v join schule.aufgabe b on b.id = v.aufgabe_id where v.lernender_id = v_l and b.einheit_id = a.einheit_id and b.variante_gruppe = a.variante_gruppe)
     order by 1, 2 limit 1) q;
  select q.einheit_id, q.lz into v_e2, v_lz2 from (
    select a.einheit_id, a.variante_gruppe lz from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id and e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id)
     where a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and a.antworttyp = 'auswahl' and e.block_id is not null and a.einheit_id <> v_e
     group by 1, 2 having count(*) >= 4
        and not exists (select 1 from schule.versuch v join schule.aufgabe b on b.id = v.aufgabe_id where v.lernender_id = v_l and b.einheit_id = a.einheit_id and b.variante_gruppe = a.variante_gruppe)
     order by 1, 2 limit 1) q;
  if v_e2 is null then raise exception 'FEHLER Vorbereitung: keine zwei passenden Etappen'; end if;
  select array_agg(a.id order by a.id) into v_ids from schule.aufgabe a where a.einheit_id = v_e and a.variante_gruppe = v_lz and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and a.antworttyp = 'auswahl';
  -- Nachtrag 22.11.: alle übrigen Übungsaufgaben beider Etappen (andere Stufen/Typen) gestern beantwortet = innerhalb der Sperre.
  -- So rechnet der Test nur mit den Auswahl-Aufgaben der Stufen 2–3 – unabhängig davon, wie die echte Etappe zusammengesetzt ist.
  insert into schule.lerntag (lernender_id, fach, datum, zeitzone)
  values (v_l, 'Mathematik', schule.heute_tag(v_l) - 1, coalesce((select zeitzone from schule.lernender where id = v_l), 'UTC')) on conflict do nothing;
  perform pg_temp.w3_gesehen(v_l, a.id, ((schule.heute_tag(v_l) - 1)::timestamp + interval '12 hours') at time zone coalesce((select zeitzone from schule.lernender where id = v_l), 'UTC'))
     from schule.aufgabe a
    where ((a.einheit_id = v_e and a.variante_gruppe = v_lz) or (a.einheit_id = v_e2 and a.variante_gruppe = v_lz2))
      and a.pool = 'uebung' and a.freigegeben and not (a.stufe in (2, 3) and a.antworttyp = 'auswahl');

  -- 1 Sperre in Lerntagen: heute + die 2 vorigen Lerntage (Tage ohne Lernen zählen nicht)
  v_ab := schule.wdh_sperre_ab(v_l);
  if v_ab <> (select min(q.datum) from (select datum from schule.lerntag where lernender_id = v_l and fach = 'Mathematik' and datum < schule.heute_tag(v_l) order by datum desc limit 2) q) then
    raise exception 'FEHLER 1 Sperre ab %', v_ab; end if;
  raise notice 'ok 1 Sperre ab % (heute %; % Kalendertage, 3 Lerntage)', v_ab, schule.heute_tag(v_l), schule.heute_tag(v_l) - v_ab;

  -- 2 Wiederholung Stufe 0–2: zuerst nie beantwortete; nie aus den letzten 3 Lerntagen; sonst die am längsten zurückliegende; sonst keine
  perform pg_temp.w3_karte(v_l, v_e, v_lz, 1, 3, 9);
  for v_n in 1 .. cardinality(v_ids) - 1 loop perform pg_temp.w3_gesehen(v_l, v_ids[v_n], now() - (20 + v_n) * interval '1 day'); end loop;   -- alle bis auf eine alt beantwortet
  if schule.wdh_aufgabe_waehlen(v_l, v_e, v_lz, false) <> v_ids[cardinality(v_ids)] then raise exception 'FEHLER 2 nicht die frische'; end if;
  perform pg_temp.w3_gesehen(v_l, v_ids[cardinality(v_ids)], (v_ab::timestamp at time zone coalesce((select zeitzone from schule.lernender where id = v_l), 'UTC')) + interval '1 hour');
  v_x := schule.wdh_aufgabe_waehlen(v_l, v_e, v_lz, false);
  if v_x <> v_ids[cardinality(v_ids) - 1] then raise exception 'FEHLER 2 keine frische: nicht die am längsten zurückliegende (%)', v_x; end if;
  for v_n in 1 .. cardinality(v_ids) - 1 loop perform pg_temp.w3_gesehen(v_l, v_ids[v_n], now() - interval '1 minute'); end loop;              -- alle in den letzten 3 Lerntagen
  if schule.wdh_aufgabe_waehlen(v_l, v_e, v_lz, false) is not null or schule.wdh_aufgabe_da(v_l, v_e, v_lz) then raise exception 'FEHLER 2 Aufgabe aus den letzten 3 Lerntagen'; end if;
  r := schule.wiederholung_intern(v_l, '{}'::jsonb, false, schule.heute_tag(v_l) + 7);
  if exists (select 1 from jsonb_array_elements(r->'aufgaben') x where (x->>'einheit_id')::bigint = v_e and x->>'lernziel' = v_lz) or (r->>'faellig')::int < 1 then
    raise exception 'FEHLER 2 Runde: Etappe ohne Aufgabe gezeigt oder nicht mehr fällig'; end if;
  raise notice 'ok 2 Wiederholung: frisch zuerst, dann die am längsten zurückliegende, nie aus den letzten 3 Lerntagen; sonst heute keine (bleibt fällig)';

  -- 3 Mischkarten: frisch, nie aus einer Etappe von heute; offene Ausgabe verfällt bei anderer Antwort; ungültige Mischkarte
  perform pg_temp.w3_karte(v_l, v_e2, v_lz2, 0, 1, 5);                                         -- fällig, noch nie beantwortet
  r := schule.mischkarten_waehlen(v_l, v_e, 50);
  select (x->>'id')::bigint into v_m from jsonb_array_elements(r) x where (x->>'einheit_id')::bigint = v_e2 limit 1;
  if v_m is null or exists (select 1 from schule.versuch v where v.lernender_id = v_l and v.aufgabe_id = v_m) then raise exception 'FEHLER 3 keine frische Mischkarte'; end if;
  insert into schule.misch_ausgabe (lernender_id, aufgabe_id, einheit_id, lernziel) values (v_l, v_m, v_e, v_lz);
  w := pg_temp.w3_antwort(v_l, v_m, true, 0, null, false);                                    -- dieselbe Aufgabe im normalen Üben
  if exists (select 1 from schule.misch_ausgabe where lernender_id = v_l and aufgabe_id = v_m and eingeloest_am is null and verfallen_am is null) then
    raise exception 'FEHLER 3 Ausgabe nicht verfallen'; end if;
  if exists (select 1 from jsonb_array_elements(schule.mischkarten_waehlen(v_l, v_e, 50)) x where (x->>'einheit_id')::bigint = v_e2) then
    raise exception 'FEHLER 3 Mischkarte aus einer Etappe von heute'; end if;
  if exists (select 1 from jsonb_array_elements(schule.wiederholung_intern(v_l, '{}'::jsonb, false, schule.heute_tag(v_l) + 8)->'aufgaben') x where (x->>'id')::bigint = v_m) then
    raise exception 'FEHLER 3 gleiche Aufgabe zweimal am Tag (Wiederholung)'; end if;
  -- als Mischkarte geschickt, ohne gültige Ausgabe: gueltig false, nicht als Wiederholung, Sterne = tatsächlich gebucht
  perform pg_temp.w3_karte(v_l, v_e2, v_lz2, 1, 3, 9);
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e2 and lernziel = v_lz2;
  v_n := (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l);
  w := pg_temp.w3_antwort(v_l, v_m, true, 0, null, true);
  if (w->'misch'->>'gueltig')::boolean is distinct from false or w ? 'wiederholung'
     or (w->'misch'->>'sterne')::int <> (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l) - v_n
     or exists (select 1 from schule.sterne where lernender_id = v_l and grund = 'wdh' and bezug like 'wdh:' || v_e2 || ':' || v_lz2 || ':' || extract(epoch from now() - interval '9 days')::bigint) then
    raise exception 'FEHLER 3 ungültige Mischkarte: %', w; end if;
  if (select wdh_stufe from schule.karte_stand where lernender_id = v_l and einheit_id = v_e2 and lernziel = v_lz2) <> v_k.wdh_stufe
     or not schule.karte_faellig((select k from schule.karte_stand k where lernender_id = v_l and einheit_id = v_e2 and lernziel = v_lz2)) then
    raise exception 'FEHLER 3 ungültige Mischkarte als Wiederholung gebucht'; end if;
  raise notice 'ok 3 Mischkarten: frisch, Ausgabe verfällt nach normaler Antwort, keine Etappe von heute, ungültig → gueltig false, nicht gebucht, Sterne %', w->'misch'->'sterne';

  -- 4 Pool mit nur einer frischen Aufgabe: Mischkarte genau diese, danach keine
  perform pg_temp.w3_karte(v_l, v_e, v_lz, 2, 7, 3);                                          -- nicht fällig
  r := schule.mischkarten_waehlen(v_l, v_e2, 50);
  if exists (select 1 from jsonb_array_elements(r) x where (x->>'einheit_id')::bigint = v_e) then raise exception 'FEHLER 4 Etappe ohne frische Aufgabe trotzdem Mischkarte'; end if;
  raise notice 'ok 4 Pool ohne frische Aufgabe (alle in den letzten 3 Lerntagen): keine Mischkarte';

  insert into schule.lerntag (lernender_id, fach, datum, zeitzone)        -- genug Lerntage für die 30er-Wiederholung (weit zurück, ändert die Sperre nicht)
  select v_l, 'Mathematik', schule.heute_tag(v_l) - d, coalesce((select zeitzone from schule.lernender where id = v_l), 'UTC') from generate_series(61, 120) d on conflict do nothing;
  -- 5 nur selbst (Regel wdh_nur_selbst = true): Stufe 4, richtig mit Tipp / im zweiten Versuch → nicht abgelegt, kein Fortschritt, nächster Lerntag
  select q.einheit_id, q.lz into v_e, v_lz from (
    select a.einheit_id, a.variante_gruppe lz from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id and e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id)
     where a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and a.antworttyp = 'auswahl' and e.block_id is not null and (a.einheit_id, a.variante_gruppe) <> (v_e2, v_lz2)
     group by 1, 2 having count(*) >= 4
        and not exists (select 1 from schule.versuch v join schule.aufgabe b on b.id = v.aufgabe_id where v.lernender_id = v_l and b.einheit_id = a.einheit_id and b.variante_gruppe = a.variante_gruppe)
     order by 1, 2 limit 1) q;
  select array_agg(a.id order by a.id) into v_ids from schule.aufgabe a where a.einheit_id = v_e and a.variante_gruppe = v_lz and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and a.antworttyp = 'auswahl';
  perform pg_temp.w3_karte(v_l, v_e, v_lz, 4, 30, 110);
  w := pg_temp.w3_antwort(v_l, v_ids[1], true, 1, null, false);                               -- mit Tipp
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if (w->'wiederholung'->>'bestanden')::boolean or w ? 'abgelegt' or v_k.wdh_stufe <> 4 or v_k.wdh_lerntage <> 1 or v_k.wdh_fehler <> 0 or schule.karte_faellig(v_k)
     or exists (select 1 from schule.abgelegt where lernender_id = v_l and bezug = 'etappe:' || v_e || ':' || v_lz) then raise exception 'FEHLER 5 mit Tipp: %', w; end if;
  perform pg_temp.w3_karte(v_l, v_e, v_lz, 4, 30, 110);
  w := pg_temp.w3_antwort(v_l, v_ids[2], false, 0, 1, false, 'w3-zweiter');                    -- erster Anlauf falsch
  w := pg_temp.w3_antwort(v_l, v_ids[2], true, 0, 2, false);                                    -- zweiter Anlauf richtig
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if (w->'wiederholung'->>'bestanden')::boolean or w ? 'abgelegt' or v_k.wdh_stufe <> 4 or v_k.wdh_fehler <> 0
     or exists (select 1 from schule.abgelegt where lernender_id = v_l and bezug = 'etappe:' || v_e || ':' || v_lz) then raise exception 'FEHLER 5 zweiter Versuch: %', w; end if;
  if exists (select 1 from schule.sterne where lernender_id = v_l and grund = 'wdh' and bezug like 'wdh:' || v_e || ':' || v_lz || ':%') then raise exception 'FEHLER 5 Wiederholungs-Sterne mit Hilfe'; end if;
  perform pg_temp.w3_karte(v_l, v_e, v_lz, 4, 30, 110);
  w := pg_temp.w3_antwort(v_l, v_ids[3], true, 0, null, false);                                -- selbst
  if not (w->'wiederholung'->>'bestanden')::boolean or not (w ? 'abgelegt') then raise exception 'FEHLER 5 selbst nicht abgelegt: %', w; end if;
  update schule.regel set wert = 'false' where schluessel = 'wdh_nur_selbst';                   -- Umschalten (Sebastians Entscheidung)
  perform pg_temp.w3_karte(v_l, v_e2, v_lz2, 1, 3, 9);
  w := pg_temp.w3_antwort(v_l, (select a.id from schule.aufgabe a where a.einheit_id = v_e2 and a.variante_gruppe = v_lz2 and a.pool = 'uebung' and a.freigegeben and a.antworttyp = 'auswahl'
                                 and not exists (select 1 from schule.versuch v where v.lernender_id = v_l and v.aufgabe_id = a.id) order by a.id limit 1), true, 1, null, false);
  if not (w->'wiederholung'->>'bestanden')::boolean then raise exception 'FEHLER 5 Regel aus: mit Tipp nicht bestanden: %', w; end if;
  update schule.regel set wert = 'true' where schluessel = 'wdh_nur_selbst';
  raise notice 'ok 5 nur selbst: mit Tipp / zweiter Versuch → kein Fortschritt, nicht abgelegt, nächster Lerntag; selbst → abgelegt; Regel aus → mit Tipp bestanden';

  -- 6 Misch-Fehler für die Reihenfolge erst nach endgültiger Wertung
  perform pg_temp.w3_karte(v_l, v_e2, v_lz2, 1, 3, 9);
  select a.id into v_m from schule.aufgabe a where a.einheit_id = v_e2 and a.variante_gruppe = v_lz2 and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3)
     and not exists (select 1 from schule.versuch v where v.lernender_id = v_l and v.aufgabe_id = a.id) order by a.id limit 1;
  insert into schule.misch_ausgabe (lernender_id, aufgabe_id, einheit_id, lernziel) values (v_l, v_m, v_e, v_lz);
  w := pg_temp.w3_antwort(v_l, v_m, false, 0, 1, true, 'w3-misch-1');                           -- erster Anlauf falsch: noch offen
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e2 and lernziel = v_lz2;
  if schule.wdh_fehler(v_k) then raise exception 'FEHLER 6 offener Misch-Fehler zählt schon'; end if;
  w := pg_temp.w3_antwort(v_l, v_m, false, 0, 2, true);                                         -- zweiter Anlauf falsch: endgültig
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e2 and lernziel = v_lz2;
  if not schule.wdh_fehler(v_k) then raise exception 'FEHLER 6 endgültiger Misch-Fehler zählt nicht'; end if;
  raise notice 'ok 6 Misch-Fehler zählt erst nach endgültiger Wertung';

  -- 8 WD-S 4 (ChatGPT 921): Mischkarte beim Einlösen geprüft, mit Hilfe 0 Sterne, 0/1 freie Aufgabe, Lerntage mit Pausen
  if position('WD-S 4' in pg_get_functiondef('schule.misch_gueltig(bigint, schule.aufgabe, jsonb)'::regprocedure)) = 0 then
    raise exception 'FEHLER 8: 20261122_wd_s4_nacharbeit_921.sql fehlt'; end if;
  select q.einheit_id, q.lz into v_e, v_lz from (
    select a.einheit_id, a.variante_gruppe lz from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id and e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id)
     where a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and a.antworttyp = 'auswahl' and e.block_id is not null and (a.einheit_id, a.variante_gruppe) <> (v_e2, v_lz2)
     group by 1, 2 having count(*) >= 5
        and not exists (select 1 from schule.versuch v join schule.aufgabe b on b.id = v.aufgabe_id where v.lernender_id = v_l and b.einheit_id = a.einheit_id and b.variante_gruppe = a.variante_gruppe)
     order by 1, 2 limit 1) q;
  if v_e is null then raise exception 'FEHLER 8 Vorbereitung: keine unbeantwortete Etappe'; end if;
  select array_agg(a.id order by a.id) into v_ids from schule.aufgabe a where a.einheit_id = v_e and a.variante_gruppe = v_lz and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and a.antworttyp = 'auswahl';
  perform pg_temp.w3_gesehen(v_l, a.id, now() - interval '200 days') from schule.aufgabe a                     -- übrige Aufgaben der Etappe: lange her
    where a.einheit_id = v_e and a.variante_gruppe = v_lz and a.pool = 'uebung' and a.freigegeben and not (a.id = any(v_ids));
  -- 8a A ausgeben → B derselben Etappe beantworten → A einlösen: gueltig false, keine Wiederholung
  perform pg_temp.w3_karte(v_l, v_e, v_lz, 1, 3, 9);
  insert into schule.misch_ausgabe (lernender_id, aufgabe_id, einheit_id, lernziel, ausgegeben_am) values (v_l, v_ids[1], v_e2, v_lz2, now() - interval '1 minute');
  w := pg_temp.w3_antwort(v_l, v_ids[2], false, 0, null, false);                                                -- B (falsch, als Übung)
  perform pg_temp.w3_karte(v_l, v_e, v_lz, 1, 3, 9);                                                               -- wieder fällig wie vorher
  v_n := (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l);
  w := pg_temp.w3_antwort(v_l, v_ids[1], true, 0, null, true);                                                  -- A als Mischkarte
  select * into v_k from schule.karte_stand where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;
  if (w->'misch'->>'gueltig')::boolean is distinct from false or w ? 'wiederholung' or v_k.wdh_stufe <> 1 or not schule.karte_faellig(v_k) then
    raise exception 'FEHLER 8a Mischkarte nach anderer Aufgabe der Etappe: %', w; end if;
  if exists (select 1 from schule.sterne where lernender_id = v_l and grund = 'wdh' and bezug like 'wdh:' || v_e || ':' || v_lz || ':%') then raise exception 'FEHLER 8a als Wiederholung vergütet'; end if;
  -- 8b fällige Wiederholung mit Tipp: 0 Sterne (keine Übungs-, keine Wiederholungssterne)
  perform pg_temp.w3_karte(v_l, v_e, v_lz, 1, 3, 9);
  v_n := (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l);
  w := pg_temp.w3_antwort(v_l, v_ids[3], true, 1, null, false);
  if not coalesce((w->'wiederholung'->>'mit_hilfe')::boolean, false) or (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l) <> v_n
     or exists (select 1 from schule.sterne where lernender_id = v_l and bezug = 'aufgabe:' || v_ids[3]) then raise exception 'FEHLER 8b Wiederholung mit Tipp: Sterne %', w; end if;
  -- 8c gültige Mischkarte im zweiten Versuch: möglich, aber 0 Sterne
  perform pg_temp.w3_karte(v_l, v_e, v_lz, 2, 7, 2);                                                               -- nicht fällig
  insert into schule.misch_ausgabe (lernender_id, aufgabe_id, einheit_id, lernziel) values (v_l, v_ids[4], v_e2, v_lz2);
  w := pg_temp.w3_antwort(v_l, v_ids[4], false, 0, 1, true, 'w3-m2-1');                                          -- erster Anlauf falsch
  v_n := (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l);
  w := pg_temp.w3_antwort(v_l, v_ids[4], true, 0, 2, true);                                                       -- zweiter Anlauf richtig
  if (w->'misch'->>'gueltig')::boolean is distinct from true or (select coalesce(sum(menge), 0) from schule.sterne where lernender_id = v_l) <> v_n then
    raise exception 'FEHLER 8c Mischkarte im zweiten Versuch: %', w; end if;
  -- 8d 1 freie Aufgabe → genau diese; 0 freie → keine (deterministisches wdh_aufgabe_da)
  perform pg_temp.w3_gesehen(v_l, a.id, now() - interval '1 minute') from schule.aufgabe a
    where a.einheit_id = v_e and a.variante_gruppe = v_lz and a.pool = 'uebung' and a.freigegeben and a.id <> v_ids[5]
      and not exists (select 1 from schule.versuch v where v.lernender_id = v_l and v.aufgabe_id = a.id and schule.lern_datum(v_l, v.am) >= schule.wdh_sperre_ab(v_l));
  if schule.wdh_aufgabe_waehlen(v_l, v_e, v_lz, false) is distinct from v_ids[5] or not schule.wdh_aufgabe_da(v_l, v_e, v_lz) then raise exception 'FEHLER 8d eine freie'; end if;
  perform pg_temp.w3_gesehen(v_l, v_ids[5], now() - interval '1 minute');
  if schule.wdh_aufgabe_waehlen(v_l, v_e, v_lz, false) is not null or schule.wdh_aufgabe_da(v_l, v_e, v_lz) then raise exception 'FEHLER 8d keine freie'; end if;
  -- 8e Lerntage mit Pausen: am Tag der Sperrgrenze beantwortet = gesperrt, am Tag davor = frei (egal wie viele Kalendertage)
  v_ab := schule.wdh_sperre_ab(v_l);
  select a.id into v_x from schule.aufgabe a where a.einheit_id = v_e2 and a.variante_gruppe = v_lz2 and a.pool = 'uebung' and a.freigegeben
     and not exists (select 1 from schule.versuch v where v.lernender_id = v_l and v.aufgabe_id = a.id) order by a.id limit 1;
  if v_x is not null then
    perform pg_temp.w3_gesehen(v_l, v_x, (v_ab::timestamp + interval '12 hours') at time zone coalesce((select zeitzone from schule.lernender where id = v_l), 'UTC'));
    if schule.lern_datum(v_l, (select max(am) from schule.versuch where lernender_id = v_l and aufgabe_id = v_x)) < schule.wdh_sperre_ab(v_l) then raise exception 'FEHLER 8e an der Grenze frei'; end if;
  end if;
  if exists (select 1 from schule.lerntag t where t.lernender_id = v_l and t.fach = 'Mathematik' and t.datum > v_ab and t.datum < schule.heute_tag(v_l)
               group by t.lernender_id having count(*) <> 1) then raise exception 'FEHLER 8e: zwischen Grenze und heute nicht genau ein Lerntag'; end if;
  raise notice 'ok 8 WD-S 4: Mischkarte nach anderer Aufgabe ungültig; mit Hilfe 0 Sterne (Wiederholung, Mischkarte 2. Versuch); 1/0 freie Aufgabe; Sperre über % Kalendertage = 3 Lerntage', schule.heute_tag(v_l) - v_ab;

  -- 7 WD-4b: offene Runde ausgenommen, belegte Folgetage mitgezählt, Rückweg nur ohne Zwischenübung
  if to_regprocedure('schule.wdh_staffel_strecken(bigint)') is null or to_regprocedure('schule.wdh_staffel_zurueck(bigint)') is null then
    raise exception 'FEHLER 7: WD-4b-Funktionen fehlen (20261122_wd_4b_stau_strecken.sql einspielen)';
  else
    update schule.karte_stand set sitzt = false, faellig_am = null, wdh_ab = null, wdh_lerntage = null, wdh_fehler = 0 where lernender_id = v_l;
    create temp table if not exists wd_regel_alt on commit drop as select wert from schule.regel where schluessel = 'wdh_gesetzt_je_lerntag';   -- WD-5: Standard merken (heute 3, vorher 6)
    update schule.regel set wert = '2' where schluessel = 'wdh_gesetzt_je_lerntag';
    -- 8 gesetzte Etappen auf Stufe 0 heute fällig (Stau), 2 schon für den nächsten Lerntag geplant
    create temp table w3_gesetzt as select row_number() over (order by p.einheit_id, p.lz) nr, p.einheit_id, p.lz from (
      select distinct a.einheit_id, a.variante_gruppe lz from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id and e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id)
       where a.pool = 'uebung' and a.freigegeben and e.block_id is not null) p limit 10;
    perform pg_temp.w3_karte(v_l, g.einheit_id, g.lz, 0, 1, 3) from w3_gesetzt g;
    update schule.karte_stand k set wdh_gesetzt_am = now() - interval '3 days', gesetzt_am = now() - interval '3 days' from w3_gesetzt g
     where k.lernender_id = v_l and k.einheit_id = g.einheit_id and k.lernziel = g.lz;
    update schule.karte_stand k set wdh_ab = now(), wdh_lerntage = 1, faellig_am = now() + interval '1 day' from w3_gesetzt g
     where k.lernender_id = v_l and k.einheit_id = g.einheit_id and k.lernziel = g.lz and g.nr > 8;                       -- Folgetag schon belegt (2 = voll)
    -- offene Runde von heute (Tagesrunde mit 1–2 der gesetzten)
    perform schule.wiederholung_intern(v_l, '{}'::jsonb, false);
    v_n := schule.wdh_staffel_strecken(v_l);
    if exists (select 1 from schule.wdh_runde_etappe r join schule.karte_stand k on k.lernender_id = r.lernender_id and k.einheit_id = r.einheit_id and k.lernziel = r.lernziel
                where r.lernender_id = v_l and r.tag = schule.heute_tag(v_l) and r.bearbeitet_am is null and not schule.karte_faellig(k)) then
      raise exception 'FEHLER 7 Etappe der offenen Runde gestreckt'; end if;
    if (select coalesce(fertig_am is not null, false) from schule.wdh_runde where lernender_id = v_l and tag = schule.heute_tag(v_l)) then raise exception 'FEHLER 7 Runde fälschlich fertig'; end if;
    if exists (select 1 from schule.karte_stand k join w3_gesetzt g on g.einheit_id = k.einheit_id and g.lz = k.lernziel where k.lernender_id = v_l
                group by schule.karte_wdh_in(k) having schule.karte_wdh_in(k) > 0 and count(*) > 2) then raise exception 'FEHLER 7 mehr als 2 je Lerntag (Folgetag mitgezählt)'; end if;
    if exists (select 1 from schule.karte_stand k join w3_gesetzt g on g.einheit_id = k.einheit_id and g.lz = k.lernziel where k.lernender_id = v_l and g.nr <= 8 and schule.karte_wdh_in(k) = 1) then
      raise exception 'FEHLER 7 belegter Folgetag nicht mitgezählt'; end if;
    -- Rückweg: abgelehnt nach einer Zwischenübung, sonst möglich
    select k.einheit_id, k.lernziel into v_x, v_lz from schule.wdh_staffel_sicherung s join schule.karte_stand k on k.lernender_id = s.lernender_id and k.einheit_id = s.einheit_id and k.lernziel = s.lernziel
     where s.lernender_id = v_l limit 1;
    update schule.karte_stand set falsch = falsch + 1 where lernender_id = v_l and einheit_id = v_x and lernziel = v_lz;   -- wie eine Zwischenübung
    begin
      perform schule.wdh_staffel_zurueck(v_l); v_fehler := 'kein Fehler';
    exception when others then v_fehler := sqlerrm; end;
    if v_fehler = 'kein Fehler' then raise exception 'FEHLER 7 Rückweg trotz Zwischenübung'; end if;
    update schule.karte_stand set falsch = falsch - 1 where lernender_id = v_l and einheit_id = v_x and lernziel = v_lz;
    v_x := schule.wdh_staffel_zurueck(v_l);
    if v_x <> v_n or exists (select 1 from schule.karte_stand k join w3_gesetzt g on g.einheit_id = k.einheit_id and g.lz = k.lernziel
                              where k.lernender_id = v_l and g.nr <= 8 and not schule.karte_faellig(k)) then raise exception 'FEHLER 7 Rückweg (% gestreckt, % zurück)', v_n, v_x; end if;
    update schule.regel set wert = (select wert from wd_regel_alt) where schluessel = 'wdh_gesetzt_je_lerntag';   -- WD-5: gemerkten Standard zurück
    raise notice 'ok 7 WD-4b: % gestreckt, offene Runde ausgenommen, Folgetag mitgezählt (2 je Lerntag), Rückweg nach Zwischenübung abgelehnt (%), sonst zurück', v_n, v_fehler;
  end if;
  raise notice 'WD-S 3 Rauchtest durchgelaufen';
end $$;

rollback;
