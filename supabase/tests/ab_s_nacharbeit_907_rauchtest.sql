-- Rauchtest Nacharbeit 907, Teil „Flug geschafft“ (nach 20261121_ab_s_flug_geschafft_robust.sql und 20261122_nacharbeit_907.sql).
-- Transaktion mit Rollback, nur Testkind, keine Namen. Sitzungen und Lernstände legt der Test selbst an; aus der Datenbank kommen nur Inhalte.
-- Läuft über schule.test_abschliessen_intern und schule.flug_erstabschluss_nachtragen (die api-Funktion ruft test_abschliessen_intern nach der Zugriffsprüfung auf).
begin;

-- laufende Testsitzung mit einer Bordkarte je Pflicht-Etappe (p_status: nur Etappen mit diesem Stand, null = alle), Antworten richtig/falsch
create function pg_temp.n907_sitzung(p_l bigint, p_e bigint, p_art text, p_richtig boolean, p_status text, p_cid text) returns bigint language plpgsql as $f$
declare v_ids bigint[]; v_sid bigint; e schule.einheit;
begin
  select * into e from schule.einheit where id = p_e;
  select array_agg(q.id order by q.lz) into v_ids from (
    select s.lernziel lz, (select a.id from schule.aufgabe a where a.einheit_id = p_e and a.variante_gruppe = s.lernziel
                            order by (a.pool = case p_art when 'korrektur' then 'korrektur' else 'test' end) desc, a.pool = 'test' desc, a.id limit 1) id
      from schule.lernziel_stand s where s.lernender_id = p_l and s.einheit_id = p_e and s.pflicht and (p_status is null or s.status = p_status)) q;
  if coalesce(cardinality(v_ids), 0) = 0 or array_position(v_ids, null) is not null then raise exception 'FEHLER Vorbereitung (%): keine Bordkarten', p_cid; end if;
  insert into schule.testsitzung(lernender_id, art, block_id, thema_id, einheit_id, aufgaben, status, punkte_max, gestartet_am)
  values (p_l, p_art, e.block_id, e.thema_id, p_e, v_ids, 'laeuft', cardinality(v_ids), now()) returning id into v_sid;
  insert into schule.versuch(lernender_id, aufgabe_id, testsitzung_id, client_id, antwort, richtig, punkte, punkte_max, hilfe, versuch_nr)
  select p_l, x, v_sid, 'n907-' || p_cid || '-' || x, null, p_richtig, case when p_richtig then 1 else 0 end, 1, 0, 1 from unnest(v_ids) x;
  return v_sid;
end $f$;

do $$
declare v_l bigint; v_fe bigint[]; v_e bigint; v_alt bigint; v_s bigint; v_lz text; t jsonb; v_wie text; v_s1 bigint; v_s2 bigint; v_fa schule.flug_erstabschluss;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  -- drei freigegebene Flüge mit mindestens 2 Pflicht-Etappen und Bordkarten, ohne Sitzungen, Lernstände und Einträge des Testkinds
  select array_agg(q.id order by q.id) into v_fe from (
    select e.id from schule.einheit e
     where e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id) and e.block_id is not null
       and jsonb_array_length(coalesce(e.inhalt->'bewertung'->'lernziele_pflicht', '[]'::jsonb)) >= 2
       and not exists (select 1 from jsonb_array_elements_text(e.inhalt->'bewertung'->'lernziele_pflicht') p
                        where (select count(*) from schule.aufgabe a where a.einheit_id = e.id and a.variante_gruppe = p) < 1)
       and not exists (select 1 from schule.testsitzung x where x.lernender_id = v_l and x.einheit_id = e.id)
       and not exists (select 1 from schule.lernziel_stand s where s.lernender_id = v_l and s.einheit_id = e.id)
       and not exists (select 1 from schule.flug_erstabschluss fe where fe.lernender_id = v_l and fe.einheit_id = e.id)
     order by e.id limit 3) q;
  if coalesce(cardinality(v_fe), 0) < 3 then raise exception 'FEHLER Vorbereitung: keine drei passenden Flüge'; end if;

  -- 1 Altzustand: alter bestandener Flug (Sitzung NULL bzw. vorher gelesen → false) → neue Pflicht-Etappe offen → ERST DANN Nachtrag → Nachtragstest.
  --   Festgelegtes Ergebnis: flug_geschafft = true (bekannte Grenze, beim Einspielen im Bestand ausgeschlossen – Kopf von 20261122_nacharbeit_907.sql).
  foreach v_wie in array array['null', 'gelesen'] loop
    v_e := case v_wie when 'null' then v_fe[1] else v_fe[2] end;
    perform schule.lernziele_anlegen(v_l, v_e);
    v_alt := pg_temp.n907_sitzung(v_l, v_e, 'blocktest', true, null, '1-' || v_wie);
    update schule.testsitzung set status = 'abgeschlossen', abgeschlossen_am = now() - interval '30 days', flug_geschafft = null where id = v_alt;
    update schule.lernziel_stand set status = 'nachgewiesen' where lernender_id = v_l and einheit_id = v_e and pflicht;
    if v_wie = 'gelesen' then
      t := schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_alt));            -- vorher gelesen: schreibt false fest
      if (select flug_geschafft from schule.testsitzung where id = v_alt) is distinct from false then raise exception 'FEHLER 1 (%): Lesen schreibt nicht false', v_wie; end if;
    end if;
    select s.lernziel into v_lz from schule.lernziel_stand s where s.lernender_id = v_l and s.einheit_id = v_e and s.pflicht order by s.lernziel limit 1;
    update schule.lernziel_stand set status = 'offen' where lernender_id = v_l and einheit_id = v_e and lernziel = v_lz;   -- neue Pflicht-Etappe offen
    perform schule.flug_erstabschluss_nachtragen(v_l);                                                -- erst jetzt der Nachtrag
    if exists (select 1 from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_e) then raise exception 'FEHLER 1 (%): Nachtrag trägt offenen Flug ein', v_wie; end if;
    v_s := pg_temp.n907_sitzung(v_l, v_e, 'blocktest', true, 'offen', '1n-' || v_wie);
    t := schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_s));
    if not (t->>'einheit_abgeschlossen')::boolean then raise exception 'FEHLER 1 (%) Vorbereitung: Flug nach Nachtragstest nicht fertig', v_wie; end if;
    if not coalesce((t->>'flug_geschafft')::boolean, false) then raise exception 'FEHLER 1 (%): festgelegtes Ergebnis true, ist %', v_wie, t->'flug_geschafft'; end if;
    -- gewollt: erneutes Lesen derselben erfolgreichen Sitzung zeigt wieder true
    t := schule.test_abschliessen_intern(v_l, jsonb_build_object('sitzung_id', v_s));
    if not coalesce((t->>'flug_geschafft')::boolean, false) then raise exception 'FEHLER 1 (%): erneutes Lesen zeigt nicht wieder true', v_wie; end if;
    raise notice 'ok 1 (% ): Altzustand → Nachtrag danach → Nachtragstest: flug_geschafft true (festgelegt); erneutes Lesen wieder true', v_wie;
  end loop;

  -- 2 Nachtrag: sitzung_id und am aus derselben, zeitlich ersten Sitzung (ids und Zeiten absichtlich gegenläufig)
  v_e := v_fe[3];
  perform schule.lernziele_anlegen(v_l, v_e);
  v_s1 := pg_temp.n907_sitzung(v_l, v_e, 'blocktest', true, null, '2a');
  v_s2 := pg_temp.n907_sitzung(v_l, v_e, 'korrektur', true, null, '2b');
  update schule.testsitzung set status = 'abgeschlossen', flug_geschafft = true, abgeschlossen_am = now() - interval '5 days' where id = v_s1;   -- kleinere id, später
  update schule.testsitzung set status = 'abgeschlossen', flug_geschafft = true, abgeschlossen_am = now() - interval '9 days' where id = v_s2;   -- größere id, früher
  perform schule.flug_erstabschluss_nachtragen(v_l);
  select * into v_fa from schule.flug_erstabschluss where lernender_id = v_l and einheit_id = v_e;
  if v_fa.sitzung_id is distinct from v_s2 or v_fa.am is distinct from (select abgeschlossen_am from schule.testsitzung where id = v_s2) then
    raise exception 'FEHLER 2: sitzung_id % / am % nicht aus derselben ersten Sitzung %', v_fa.sitzung_id, v_fa.am, v_s2; end if;
  raise notice 'ok 2 Nachtrag: sitzung_id und am aus derselben, zeitlich ersten Sitzung';
end $$;

rollback;
