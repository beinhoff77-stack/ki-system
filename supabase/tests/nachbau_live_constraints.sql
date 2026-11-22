-- Eindeutige Indizes und Constraints der echten Datenbank (schule/api, gelesen 22.11. aus pg_indexes/pg_constraint); fehlende werden lokal ergänzt
do $i$ begin execute $x$CREATE UNIQUE INDEX IF NOT EXISTS aufgabe_expedition_teil ON schule.aufgabe USING btree (expedition_id, teil) WHERE (expedition_id IS NOT NULL)$x$; exception when others then raise warning 'Nachbau: Index nicht ergänzt (%)', sqlerrm; end $i$;
do $i$ begin execute $x$CREATE UNIQUE INDEX IF NOT EXISTS einheit_eine_freigegebene ON schule.einheit USING btree (thema_id) WHERE (status = 'freigegeben'::text)$x$; exception when others then raise warning 'Nachbau: Index nicht ergänzt (%)', sqlerrm; end $i$;
do $i$ begin execute $x$CREATE UNIQUE INDEX IF NOT EXISTS misch_ausgabe_offen_eindeutig ON schule.misch_ausgabe USING btree (lernender_id, aufgabe_id) WHERE (eingeloest_am IS NULL)$x$; exception when others then raise warning 'Nachbau: Index nicht ergänzt (%)', sqlerrm; end $i$;
do $i$ begin execute $x$CREATE UNIQUE INDEX IF NOT EXISTS quelle_familie_idx ON schule.quelle USING btree (familie) WHERE aktiv$x$; exception when others then raise warning 'Nachbau: Index nicht ergänzt (%)', sqlerrm; end $i$;
do $i$ begin execute $x$CREATE UNIQUE INDEX IF NOT EXISTS route_eine_offene_rueckreise ON schule.route USING btree (lernender_id, block_id) WHERE ((art = 'rueckreise'::text) AND (status = ANY (ARRAY['offen'::text, 'laeuft'::text])))$x$; exception when others then raise warning 'Nachbau: Index nicht ergänzt (%)', sqlerrm; end $i$;
do $i$ begin execute $x$CREATE UNIQUE INDEX IF NOT EXISTS versuch_sitzung_aufgabe ON schule.versuch USING btree (testsitzung_id, aufgabe_id) WHERE (testsitzung_id IS NOT NULL)$x$; exception when others then raise warning 'Nachbau: Index nicht ergänzt (%)', sqlerrm; end $i$;
do $i$ begin execute $x$CREATE UNIQUE INDEX IF NOT EXISTS wiederholung_eine_offene ON schule.wiederholung USING btree (lernender_id, aufgabe_id) WHERE (erledigt_am IS NULL)$x$; exception when others then raise warning 'Nachbau: Index nicht ergänzt (%)', sqlerrm; end $i$;
do $i$ begin execute $x$CREATE UNIQUE INDEX IF NOT EXISTS zuordnung_eintrag_id_idx ON schule.zuordnung USING btree (eintrag_id) WHERE (bezug = 'haupt'::text)$x$; exception when others then raise warning 'Nachbau: Index nicht ergänzt (%)', sqlerrm; end $i$;
do $c$
declare r record;
begin
  for r in select * from (values
    ('schule.abgelegt', 'abgelegt_art_check', $$CHECK ((art = ANY (ARRAY['etappe'::text, 'flug'::text, 'ort'::text])))$$),
    ('schule.aufgabe', 'aufgabe_antworttyp_check', $$CHECK ((antworttyp = ANY (ARRAY['auswahl'::text, 'zahl'::text, 'text'::text, 'markierung'::text, 'luecken'::text])))$$),
    ('schule.aufgabe', 'aufgabe_art_check', $$CHECK ((art = ANY (ARRAY['uebung'::text, 'blocktest'::text, 'nachtest'::text])))$$),
    ('schule.aufgabe', 'aufgabe_pool_check', $$CHECK ((pool = ANY (ARRAY['uebung'::text, 'test'::text, 'korrektur'::text, 'sicherung'::text, 'bonus'::text, 'expedition'::text])))$$),
    ('schule.aufgabe', 'aufgabe_stufe_check', $$CHECK (((stufe >= 1) AND (stufe <= 3)))$$),
    ('schule.block', 'block_fach_schluessel_key', $$UNIQUE (fach, schluessel)$$),
    ('schule.block_thema', 'block_thema_block_id_reihenfolge_key', $$UNIQUE (block_id, reihenfolge)$$),
    ('schule.einheit', 'einheit_status_check', $$CHECK ((status = ANY (ARRAY['entwurf'::text, 'geprueft'::text, 'freigegeben'::text, 'ersetzt'::text])))$$),
    ('schule.einheit', 'einheit_thema_id_version_key', $$UNIQUE (thema_id, version)$$),
    ('schule.eintrag', 'eintrag_bearbeitung_check', $$CHECK ((bearbeitung = ANY (ARRAY['originaltitel'::text, 'deutsche_uebertragung'::text, 'zusammenfassung_eigene_worte'::text, 'redaktionelle_zuordnung'::text, 'annahme'::text])))$$),
    ('schule.eintrag', 'eintrag_quelle_id_pfad_key', $$UNIQUE (quelle_id, pfad)$$),
    ('schule.kontinent', 'kontinent_fach_schluessel_key', $$UNIQUE (fach, schluessel)$$),
    ('schule.lernender', 'lernender_schulart_check', $$CHECK ((schulart = ANY (ARRAY['gym_by'::text, 'rs_by'::text, 'ib_myp'::text])))$$),
    ('schule.lernender', 'lernender_stufen_check', $$CHECK ((jsonb_typeof(stufen) = 'object'::text))$$),
    ('schule.lernziel_stand', 'lernziel_stand_status_check', $$CHECK ((status = ANY (ARRAY['offen'::text, 'nachgewiesen'::text, 'fehler'::text, 'korrigiert'::text, 'gesichert'::text])))$$),
    ('schule.route', 'route_art_check', $$CHECK ((art = ANY (ARRAY['normal'::text, 'rueckreise'::text, 'zusatz'::text])))$$),
    ('schule.route', 'route_status_check', $$CHECK ((status = ANY (ARRAY['offen'::text, 'laeuft'::text, 'fertig'::text, 'entfernt'::text])))$$),
    ('schule.sterne', 'sterne_grund_check', $$CHECK ((grund = ANY (ARRAY['uebung'::text, 'test'::text, 'ort'::text, 'einloesung'::text, 'korrektur_hand'::text, 'bonus'::text, 'expedition'::text, 'wdh'::text, 'etappe_abgelegt'::text, 'flug_abgelegt'::text, 'landung'::text])))$$),
    ('schule.sterne', 'sterne_lernender_id_grund_bezug_key', $$UNIQUE (lernender_id, grund, bezug)$$),
    ('schule.testsitzung', 'testsitzung_art_check', $$CHECK ((art = ANY (ARRAY['uebung'::text, 'blocktest'::text, 'korrektur'::text, 'nachtest'::text, 'wiederholung'::text])))$$),
    ('schule.testsitzung', 'testsitzung_ergebnis_check', $$CHECK ((ergebnis = ANY (ARRAY['bestanden'::text, 'wiederholen'::text, 'rueckreise'::text])))$$),
    ('schule.testsitzung', 'testsitzung_status_check', $$CHECK ((status = ANY (ARRAY['laeuft'::text, 'abgeschlossen'::text, 'abgebrochen'::text])))$$),
    ('schule.thema', 'thema_fach_schluessel_key', $$UNIQUE (fach, schluessel)$$),
    ('schule.thema', 'thema_lehrplan_reihenfolge_check', $$CHECK ((jsonb_typeof(lehrplan_reihenfolge) = 'object'::text))$$),
    ('schule.thema', 'thema_pruefstatus_check', $$CHECK ((pruefstatus = ANY (ARRAY['ungeprueft'::text, 'geprueft'::text, 'klaerungsbedarf'::text])))$$),
    ('schule.versuch', 'versuch_lernender_id_client_id_key', $$UNIQUE (lernender_id, client_id)$$),
    ('schule.voraussetzung', 'voraussetzung_art_check', $$CHECK ((art = ANY (ARRAY['hart'::text, 'empfohlen'::text])))$$),
    ('schule.voraussetzung', 'voraussetzung_check', $$CHECK ((thema_id <> braucht_id))$$),
    ('schule.zuordnung', 'zuordnung_bezug_check', $$CHECK ((bezug = ANY (ARRAY['haupt'::text, 'neben'::text])))$$),
    ('schule.zuordnung', 'zuordnung_eintrag_id_thema_id_key', $$UNIQUE (eintrag_id, thema_id)$$),
    ('schule.zuordnung', 'zuordnung_pruefstatus_check', $$CHECK ((pruefstatus = ANY (ARRAY['ungeprueft'::text, 'geprueft'::text, 'klaerungsbedarf'::text])))$$)
  ) v(t, n, d) loop
    if not exists (select 1 from pg_constraint where conname = r.n and conrelid = r.t::regclass)
       and not exists (select 1 from pg_indexes where indexname = r.n) then
      begin
        execute format('alter table %s add constraint %I %s', r.t, r.n, r.d);
      exception when others then raise warning 'Nachbau: % nicht ergänzt (%)', r.n, sqlerrm;
      end;
    end if;
  end loop;
end $c$;
-- Primärschlüssel wie live
do $c$ begin
  if not exists (select 1 from pg_constraint where conrelid = 'schule.voraussetzung'::regclass and contype = 'p') then alter table schule.voraussetzung add primary key (thema_id, braucht_id); end if;
  if not exists (select 1 from pg_constraint where conrelid = 'schule.flug_erstabschluss'::regclass and contype = 'p') then alter table schule.flug_erstabschluss add primary key (lernender_id, einheit_id); end if;
  if not exists (select 1 from pg_constraint where conrelid = 'schule.abgelegt'::regclass and contype = 'p') then alter table schule.abgelegt add primary key (lernender_id, bezug); end if;
  if not exists (select 1 from pg_constraint where conrelid = 'schule.lernziel_stand'::regclass and contype = 'p') then alter table schule.lernziel_stand add primary key (lernender_id, einheit_id, lernziel); end if;
  if not exists (select 1 from pg_constraint where conrelid = 'schule.karte_stand'::regclass and contype = 'p') then alter table schule.karte_stand add primary key (lernender_id, einheit_id, lernziel); end if;
  if not exists (select 1 from pg_constraint where conrelid = 'schule.etappe_text'::regclass and contype = 'p') then alter table schule.etappe_text add primary key (thema_id, lernziel); end if;
  if not exists (select 1 from pg_constraint where conrelid = 'schule.besprochen'::regclass and contype = 'p') then alter table schule.besprochen add primary key (lernender_id, einheit_id, lernziel); end if;
end $c$;
