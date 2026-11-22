-- Rauchtest NT-S (Nachtests bei kleinen Flügen). Nach 20261124_nt_s_nachtest_menge.sql. Transaktion mit Rollback, nur Testkind und eigene Test-Flüge
-- (1, 2, 3 und 5 Pflicht-Etappen, je 16 Sicherungs-Aufgaben). Hängt nicht von Kinderdaten ab; keine Namen.
begin;

do $$
declare v_l bigint; v_n int; v_t bigint; v_e bigint; v_je int; w jsonb; v_s bigint; v_ids bigint[]; v_erg text; v_alt text; v_sel bigint[]; v_sel2 bigint[];
  v_bericht text := ''; v_lz text; v_x int;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER Vorbereitung: kein Testkind'; end if;
  -- Lerntage: zwölf in den letzten zwölf Tagen (der Flug-Test liegt 40 Tage zurück → Nachtest 1 fällig)
  insert into schule.lerntag (lernender_id, fach, datum, zeitzone)
  select v_l, 'Mathematik', current_date - g, 'Europe/Berlin' from generate_series(1, 12) g on conflict do nothing;

  foreach v_n in array array[1, 2, 3, 5] loop
    insert into schule.thema (fach, schluessel, block, unterthema, reihenfolge, klasse_fest)
    values ('Mathematik', 'nt_s_test_' || v_n || '_' || txid_current(), 'X', 'NT-S Test ' || v_n, 0, '{}') returning id into v_t;
    insert into schule.einheit (thema_id, version, status, inhalt)
    values (v_t, 1, 'geprueft', jsonb_build_object('etappen', (select jsonb_agg(jsonb_build_object('lernziel', 'e' || i, 'titel', 'E' || i) order by i) from generate_series(1, v_n) i),
                                                  'bewertung', jsonb_build_object('lernziele_pflicht', (select jsonb_agg('e' || i order by i) from generate_series(1, v_n) i))))
    returning id into v_e;
    insert into schule.aufgabe (einheit_id, thema_id, art, antworttyp, frage, loesung, pool, variante_gruppe, stufe, freigegeben, reihenfolge)
    select v_e, v_t, 'nachtest', 'zahl', jsonb_build_object('text', 'x'), jsonb_build_object('wert', 1), 'sicherung', 'e' || i, 2, true, k
      from generate_series(1, v_n) i, generate_series(1, 16) k;
    perform schule.lernziele_anlegen(v_l, v_e);
    update schule.lernziel_stand set status = 'nachgewiesen' where lernender_id = v_l and einheit_id = v_e;
    insert into schule.testsitzung (lernender_id, art, thema_id, einheit_id, aufgaben, status, gestartet_am, abgeschlossen_am)
    values (v_l, 'blocktest', v_t, v_e, '{}', 'abgeschlossen', now() - interval '40 days', now() - interval '40 days');

    -- 1 Menge: 1 → 5, 2 → je 3, 3 → je 2, 5 → je 1; keine Aufgabe doppelt; jede Etappe genau v_je-mal
    v_je := schule.nachtest_je_etappe(v_n);
    if v_je <> (case v_n when 1 then 5 when 2 then 3 when 3 then 2 else 1 end) then raise exception 'FEHLER 1 Menge je Etappe bei %: %', v_n, v_je; end if;
    w := schule.test_starten_intern(v_l, jsonb_build_object('einheit_id', v_e, 'art', 'nachtest'));
    if not (w->>'ok')::boolean then raise exception 'FEHLER 1 Nachtest startet nicht (% Etappen): %', v_n, w; end if;
    v_s := (w->>'sitzung_id')::bigint;
    select aufgaben into v_ids from schule.testsitzung where id = v_s;
    if cardinality(v_ids) <> v_n * v_je or cardinality(v_ids) < 5 then raise exception 'FEHLER 1 % Etappen: % Aufgaben statt %', v_n, cardinality(v_ids), v_n * v_je; end if;
    if (select count(distinct x) from unnest(v_ids) x) <> cardinality(v_ids) then raise exception 'FEHLER 1 Aufgabe doppelt im Nachtest'; end if;
    if exists (select 1 from schule.aufgabe a where a.id = any(v_ids) group by a.variante_gruppe having count(*) <> v_je) then raise exception 'FEHLER 1 Etappen ungleich verteilt'; end if;

    -- 2 ein Fehler entscheidet bei kleinen Flügen nicht über die Rückreise (Quote und Einstufung unverändert)
    insert into schule.versuch (lernender_id, aufgabe_id, testsitzung_id, client_id, richtig, punkte, punkte_max, hilfe, versuch_nr)
    select v_l, x, v_s, 'nt-s-' || v_s || '-' || x, x <> v_ids[1], case when x <> v_ids[1] then 1 else 0 end, 1, 0, 1 from unnest(v_ids) x;
    w := schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_s));
    v_erg := w->>'nachtest_ergebnis';
    v_alt := schule.nachtest_einstufung(v_n - 1, v_n);   -- bisher: eine Aufgabe je Etappe
    if v_erg = 'rueckreise' then raise exception 'FEHLER 2 % Etappen: ein Fehler → Rückreise', v_n; end if;
    if v_erg <> schule.nachtest_einstufung(cardinality(v_ids) - 1, cardinality(v_ids)) then raise exception 'FEHLER 2 Einstufung verändert'; end if;
    v_bericht := v_bericht || format('%s Etappen: %s Aufgaben, 1 Fehler → %s (bisher %s); ', v_n, cardinality(v_ids), v_erg, v_alt);

    -- 3 nächste Auswahl: keine Wiederholung, solange ungestellte Aufgaben da sind; Vorrat in Runden
    v_sel := schule.nachtest_auswahl(v_l, v_e, 'e1', v_je);
    if v_sel && v_ids then raise exception 'FEHLER 3 Wiederholung trotz ungestellter Aufgaben'; end if;
    w := schule.nachtest_stand(v_l, v_e);
    if (w->>'aufgaben_je_etappe')::int <> v_je then raise exception 'FEHLER 3 nachtest_stand ohne Menge: %', w; end if;
  end loop;

  -- 4 Auffüllen: Etappe mit nur 2 ungestellten Aufgaben bei Menge 5 → 2 ungestellte + 3 gestellte (älteste zuerst), nicht doppelt;
  --   ohne ungestellte Aufgabe → leer (Vorrat erschöpft, wie bisher)
  select e.id into v_e from schule.einheit e join schule.thema t on t.id = e.thema_id where t.schluessel like 'nt_s_test_1_%' order by e.id desc limit 1;
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, richtig, punkte, punkte_max, hilfe, versuch_nr, am)
  select v_l, a.id, 'nt-s-alt-' || a.id, true, 1, 1, 0, 1, now() - (a.reihenfolge || ' days')::interval from schule.aufgabe a
   where a.einheit_id = v_e and a.reihenfolge <= 14
     and not exists (select 1 from schule.versuch v where v.lernender_id = v_l and v.aufgabe_id = a.id);
  v_sel := schule.nachtest_auswahl(v_l, v_e, 'e1', 5);
  select count(*) into v_x from unnest(v_sel) x join schule.aufgabe a on a.id = x where a.reihenfolge > 14;
  if cardinality(v_sel) <> 5 or v_x <> 2 or (select count(distinct x) from unnest(v_sel) x) <> 5 then raise exception 'FEHLER 4 Auffüllen: %', v_sel; end if;
  insert into schule.versuch (lernender_id, aufgabe_id, client_id, richtig, punkte, punkte_max, hilfe, versuch_nr)
  select v_l, a.id, 'nt-s-rest-' || a.id, true, 1, 1, 0, 1 from schule.aufgabe a where a.einheit_id = v_e and a.reihenfolge > 14;
  v_sel2 := schule.nachtest_auswahl(v_l, v_e, 'e1', 5);
  if cardinality(v_sel2) <> 0 then raise exception 'FEHLER 4 ohne ungestellte Aufgabe nicht erschöpft'; end if;

  -- 5 Flüge mit 5 und mehr Pflicht-Etappen: Menge 1 wie bisher
  if schule.nachtest_je_etappe(5) <> 1 or schule.nachtest_je_etappe(8) <> 1 or schule.nachtest_je_etappe(4) <> 2 then raise exception 'FEHLER 5 Regel'; end if;

  raise notice 'NT-S Rauchtest: %', v_bericht;
  raise notice 'NT-S Rauchtest: alles grün';
end $$;

rollback;
