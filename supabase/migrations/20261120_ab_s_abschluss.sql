-- Bau-Auftrag AB, Teil AB-S (Server): Abschluss nach Etappe, Flug und Ort. Vorgabe inhalte/pruefung/kind/abschluss/umsetzung.md (Abschnitte 1–3, 7).
-- 1. Landung einer Etappe: Zählung (Bordkarten, ziel, endgültige Fehler, mit Tipp, zweite Versuche, Stufe gesenkt, Lerntage, wieder gelandet) und
--    landung_art direkt | sauber | sturm nach den Schwellen in schule.regel. Gespeichert in karte_stand.landung_art / .landung (bei „wieder gelandet“ überschrieben),
--    geliefert in der Antwort auf die Übung (Feld „landung“), gezählt im Reisepass (konto.abzeichen).
-- 2. Flug-Test: sterne_flug, Etappen mit „kann“, kurz, Flug i von k, Ort durch diesen Abschluss geschafft, Ort-Sterne, Flüge des Orts, nächster Flug laut Plan.
-- 3. Texte: thema.kurz und Tabelle schule.etappe_text(thema_id, lernziel, kann) – Ablage für AB-I; geliefert in schule_einheit_lesen und im Test-Ergebnis (fehlt → null).
-- Bestand: schon gelandete Etappen bekommen keine nachträgliche landung_art (nichts erfinden); gesetzte Landungen (LB-3) bekommen keine.
-- Nach 20261120_i5_stufe_nachtragstest.sql (unabhängig davon). Nicht ausgeführt – der Haupt-Chat spielt ein.
-- Kein DROP, kein DELETE, keine Bestandsänderung (nur neue Spalten, neue Tabelle, neue Regeln). Wiederholt ausführbar.

-- ---------- Ablage ----------
alter table schule.karte_stand add column if not exists landung_art text;
alter table schule.karte_stand add column if not exists landung jsonb;
do $c$ begin
  if not exists (select 1 from pg_constraint where conname = 'karte_stand_landung_art_check' and conrelid = 'schule.karte_stand'::regclass) then
    alter table schule.karte_stand add constraint karte_stand_landung_art_check check (landung_art in ('direkt', 'sauber', 'sturm'));
  end if;
end $c$;
comment on column schule.karte_stand.landung_art is 'AB-S: Art der letzten eigenen Landung (direkt | sauber | sturm); null = vor AB-S gelandet oder gesetzt (LB-3)';
comment on column schule.karte_stand.landung is 'AB-S: Zählung der letzten eigenen Landung (schule.landung_zaehlen), Grundlage für landung_art';

alter table schule.testsitzung add column if not exists ort_geschafft boolean;
comment on column schule.testsitzung.ort_geschafft is 'AB-S: Ort durch den Abschluss dieser Sitzung geschafft (einmal beim ersten Lesen nach dem Abschluss festgehalten)';

alter table schule.thema add column if not exists kurz text;
comment on column schule.thema.kurz is 'AB-I: ein Satz, worum es im Flug geht (höchstens 110 Zeichen); null = App nimmt umfang';

create table if not exists schule.etappe_text (
  thema_id bigint not null references schule.thema(id),
  lernziel text not null,
  kann text,
  geaendert_am timestamptz not null default now(),
  primary key (thema_id, lernziel)
);
alter table schule.etappe_text enable row level security;
comment on table schule.etappe_text is 'AB-I: „Du kannst jetzt …“ je Etappe (lernziel aus inhalt.etappen); nicht in einheit.inhalt, weil freigegebene Flüge unveränderlich sind';

insert into schule.regel(schluessel, wert, hinweis)
select x.s, x.w::jsonb, x.h from (values
  ('landung_sauber_fehler_max', '2', 'AB-S: Saubere Landung – höchstens so viele endgültige Fehler'),
  ('landung_sauber_mehr_max', '4', 'AB-S: Saubere Landung – höchstens ziel + n Bordkarten'),
  ('landung_sauber_stufe_gesenkt_max', '0', 'AB-S: Saubere Landung – Stufe höchstens so oft gesenkt'),
  ('landung_sauber_lerntage_max', 'null', 'AB-S: Saubere Landung – höchstens so viele Lerntage; null = keine Grenze (Freigabe 20.11. nennt keine)')
) x(s, w, h)
where not exists (select 1 from schule.regel r where r.schluessel = x.s);

-- ---------- Landung zählen ----------
create or replace function schule.landung_zaehlen(p_l bigint, p_e bigint, p_lz text)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare k schule.karte_stand; w record; v_ab timestamptz; v_tz text; v_wieder boolean; v_ziel int; v_art text; v_tage int;
  n_karten int := 0; n_fehler int := 0; n_tipp int := 0; n_zweit int := 0; n_senk int := 0; v_ff int := 0; v_st int := 0;
  r_fehler int; r_mehr int; r_senk int; r_tage int;
begin
  select * into k from schule.karte_stand where lernender_id = p_l and einheit_id = p_e and lernziel = p_lz;
  if k.lernender_id is null or not k.sitzt or k.sitzt_am is null then return null; end if;
  -- gezählt wird seit dem Beginn bzw. seit dem letzten „wieder offen“ bis zur Landung; nur Übungen dieser Etappe, ohne Mischkarten, Knobel, Expeditionen, Tests
  v_wieder := k.geoeffnet_am is not null and k.geoeffnet_am < k.sitzt_am;
  v_ab := case when v_wieder then k.geoeffnet_am end;
  select coalesce(l.zeitzone, 'UTC') into v_tz from schule.lernender l where l.id = p_l;
  v_tage := 0;
  for w in select v.anlauf, v.hilfe, (v.am at time zone coalesce(v_tz, 'UTC'))::date tag, schule.versuch_wertung(v) z
             from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
            where v.lernender_id = p_l and a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'uebung'
              and v.testsitzung_id is null and not coalesce(v.misch, false)
              and (v_ab is null or v.am > v_ab) and v.am <= k.sitzt_am
            order by v.am, v.id loop
    if coalesce(w.anlauf, 1) = 2 then n_zweit := n_zweit + 1;            -- 2. Anlauf derselben Bordkarte
    else
      n_karten := n_karten + 1;
      if coalesce(w.hilfe, 0) > 0 then n_tipp := n_tipp + 1; end if;
    end if;
    -- Stufe senken wie karte_buchen: jeder zweite endgültige Fehler in Folge senkt (höchstens bis 2), eine eigene Lösung hebt eine Stufe
    if w.z = 'falsch' then
      n_fehler := n_fehler + 1; v_ff := v_ff + 1;
      if v_ff % 2 = 0 and v_st < 2 then v_st := v_st + 1; n_senk := n_senk + 1; end if;
    elsif w.z = 'eigen' then
      v_ff := 0; v_st := greatest(v_st - 1, 0);
    end if;
  end loop;
  select count(distinct (v.am at time zone coalesce(v_tz, 'UTC'))::date) into v_tage
    from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
   where v.lernender_id = p_l and a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'uebung'
     and v.testsitzung_id is null and not coalesce(v.misch, false) and (v_ab is null or v.am > v_ab) and v.am <= k.sitzt_am;
  v_ziel := schule.karte_ziel(p_e, p_lz);
  select (wert #>> '{}')::int into r_fehler from schule.regel where schluessel = 'landung_sauber_fehler_max';
  select (wert #>> '{}')::int into r_mehr from schule.regel where schluessel = 'landung_sauber_mehr_max';
  select (wert #>> '{}')::int into r_senk from schule.regel where schluessel = 'landung_sauber_stufe_gesenkt_max';
  select (wert #>> '{}')::int into r_tage from schule.regel where schluessel = 'landung_sauber_lerntage_max';
  v_art := case
    when v_wieder then 'sauber'                                                     -- „wieder gelandet“: Szene der sauberen Landung
    when n_karten <= v_ziel and n_fehler = 0 and n_tipp = 0 and n_zweit = 0 then 'direkt'
    when n_fehler <= coalesce(r_fehler, 2) and n_senk <= coalesce(r_senk, 0) and n_karten <= v_ziel + coalesce(r_mehr, 4)
         and (r_tage is null or v_tage <= r_tage) then 'sauber'
    else 'sturm' end;
  return jsonb_build_object('landung_art', v_art, 'bordkarten', n_karten, 'ziel', v_ziel, 'fehler_endgueltig', n_fehler, 'mit_tipp', n_tipp,
    'zweite_versuche', n_zweit, 'stufe_gesenkt', n_senk, 'lerntage', v_tage, 'wieder_gelandet', v_wieder,
    'eigene_loesungen', k.eigene_loesungen, 'folge_ziel', least(3, v_ziel), 'am', k.sitzt_am);
end $function$;
comment on function schule.landung_zaehlen(bigint, bigint, text) is 'AB-S: Zählung einer Landung und landung_art (Schwellen in schule.regel landung_sauber_*); nur lesen';

create or replace function schule.landung_speichern(p_l bigint, p_e bigint, p_lz text)
 returns void language plpgsql set search_path to ''
as $function$
declare v jsonb := schule.landung_zaehlen(p_l, p_e, p_lz);
begin
  if v is null then return; end if;
  update schule.karte_stand set landung_art = v->>'landung_art', landung = v
   where lernender_id = p_l and einheit_id = p_e and lernziel = p_lz;
end $function$;
comment on function schule.landung_speichern(bigint, bigint, text) is 'AB-S: landung_art und Zählung einer eigenen Landung festhalten (aus karte_buchen)';

-- ---------- karte_buchen: bei einer eigenen Landung festhalten ----------
do $mig$
declare d text;
begin
  d := pg_get_functiondef('schule.karte_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)'::regprocedure);
  if position('landung_speichern' in d) > 0 then return; end if; -- schon eingespielt
  if position('v_ziel int; v_eigen boolean; v_neu boolean;' in d) = 0
     or position(E'k.wdh_ab := p_zeit; k.wdh_lerntage := v_tage[1];\n    end if;' in d) = 0
     or position(E'   where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;\nend $function$' in d) = 0 then
    raise exception 'karte_buchen: Stelle nicht gefunden';
  end if;
  d := replace(d, 'v_ziel int; v_eigen boolean; v_neu boolean;', 'v_ziel int; v_eigen boolean; v_neu boolean; v_landet boolean := false;');
  d := replace(d, E'k.wdh_ab := p_zeit; k.wdh_lerntage := v_tage[1];\n    end if;',
                  E'k.wdh_ab := p_zeit; k.wdh_lerntage := v_tage[1];\n      v_landet := true; -- AB-S\n    end if;');
  d := replace(d, E'   where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;\nend $function$',
                  E'   where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;\n  if v_landet then perform schule.landung_speichern(p_l, a.einheit_id, a.variante_gruppe); end if; -- AB-S\nend $function$');
  execute d;
end $mig$;

-- ---------- Antwort auf eine Übung: Feld „landung“ (nur in der Antwort, mit der die Etappe landet) ----------
do $mig$
declare d text;
  v_alt text := $a$'loesungsweg', a.loesungsweg,
    'karte', (select jsonb_build_object('serie'$a$;
  v_neu text := $a$'loesungsweg', a.loesungsweg,
    'landung', (select k.landung || jsonb_build_object('kann', (select x.kann from schule.einheit e join schule.etappe_text x on x.thema_id = e.thema_id and x.lernziel = k.lernziel where e.id = k.einheit_id))
                  from schule.karte_stand k where k.lernender_id = p_lernender and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe
                   and k.sitzt and k.sitzt_am = now() and k.wdh_stufe = 0 and k.landung is not null), -- AB-S
    'karte', (select jsonb_build_object('serie'$a$;
begin
  d := pg_get_functiondef('schule.uebung_pruefen_intern(bigint, jsonb)'::regprocedure);
  if position('-- AB-S' in d) > 0 then return; end if;
  if position(v_alt in d) = 0 then raise exception 'uebung_pruefen_intern: Stelle nicht gefunden'; end if;
  execute replace(d, v_alt, v_neu);
end $mig$;

-- ---------- Reisepass: Abzeichen zählen ----------
do $mig$
declare d text;
  v_alt text := $a$    'lerntage', (select count(*) from schule.lerntag where lernender_id = p_lernender),$a$;
  v_neu text := $a$    'lerntage', (select count(*) from schule.lerntag where lernender_id = p_lernender),
    'abzeichen', (select jsonb_build_object('direkt', count(*) filter (where k.landung_art = 'direkt'), 'sauber', count(*) filter (where k.landung_art = 'sauber'),
                                            'sturm', count(*) filter (where k.landung_art = 'sturm'))
                    from schule.karte_stand k where k.lernender_id = p_lernender), -- AB-S$a$;
begin
  d := pg_get_functiondef('schule.konto(bigint)'::regprocedure);
  if position('-- AB-S' in d) > 0 then return; end if;
  if position(v_alt in d) = 0 then raise exception 'konto: Stelle nicht gefunden'; end if;
  execute replace(d, v_alt, v_neu);
end $mig$;

-- ---------- Flug: Nummer im Ort, nächster Flug laut Plan ----------
create or replace function schule.flug_im_ort(p_l bigint, p_block bigint, p_thema bigint)
 returns jsonb language sql stable set search_path to ''
as $function$
  with aus as (select coalesce((select r.ausgelassen from schule.route r where r.lernender_id = p_l and r.block_id = p_block and r.art = 'normal' and r.status <> 'entfernt'
                                 order by r.id limit 1), '{}'::bigint[]) l),
  f as (select bt.thema_id, row_number() over (order by bt.reihenfolge, bt.thema_id) nr
          from schule.block_thema bt, aus where bt.block_id = p_block and not (bt.thema_id = any(aus.l)))
  select jsonb_build_object('nr', (select f.nr from f where f.thema_id = p_thema), 'von', (select count(*) from f));
$function$;
comment on function schule.flug_im_ort(bigint, bigint, bigint) is 'AB-S: „Flug i von k“ eines Flugs in seinem Ort (ohne abgewählte Flüge)';

create or replace function schule.flug_karte(p_l bigint, p_block bigint, p_thema bigint)
 returns jsonb language sql stable set search_path to ''
as $function$
  select jsonb_build_object('thema_id', t.id, 'einheit_id', e.id, 'titel', t.unterthema, 'gebiet', t.block, 'kurz', t.kurz,
           'block_id', b.id, 'ort', b.stadt, 'land', b.land, 'flug', schule.flug_im_ort(p_l, b.id, t.id),
           'etappen', jsonb_array_length(coalesce(e.inhalt->'etappen', '[]'::jsonb)),
           'erste_etappe', (select jsonb_build_object('lernziel', et->>'lernziel', 'titel', et->>'titel') from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality x(et, nr) order by x.nr limit 1))
    from schule.thema t join schule.block b on b.id = p_block
    left join schule.einheit e on e.id = schule.thema_einheit(t.id)
   where t.id = p_thema;
$function$;
comment on function schule.flug_karte(bigint, bigint, bigint) is 'AB-S: Angaben für die Bordkarte eines Flugs (Titel, Gebiet, kurz, Ort, Flug i von k, Etappen, erste Etappe)';

create or replace function schule.naechster_flug(p_l bigint, p_ausser bigint default null)
 returns jsonb language sql stable set search_path to ''
as $function$
  -- Plan-Reihenfolge: Orte nach position, Flüge nach block_thema.reihenfolge; übersprungen: abgewählt, „kann schon“ (Ort oder Flug), „kann er – aber wiederholen“,
  -- ohne geprüften Flug, erledigt, der gerade abgeschlossene Flug. Orte „fertig“ oder „entfernt“ zählen nicht.
  select schule.flug_karte(p_l, n.block_id, n.thema_id)
    from (select r.block_id, bt.thema_id from schule.route r join schule.block_thema bt on bt.block_id = r.block_id
           where r.lernender_id = p_l and r.art = 'normal' and r.status not in ('entfernt', 'fertig') and not r.kann_schon
             and not (bt.thema_id = any(r.ausgelassen)) and not (bt.thema_id = any(r.kann_schon_themen)) and not (bt.thema_id = any(coalesce(r.kann_wdh_themen, '{}')))
             and bt.thema_id is distinct from p_ausser
             and schule.thema_einheit(bt.thema_id) is not null and schule.thema_stand(p_l, bt.thema_id) <> 'erledigt'
           order by r.position, bt.reihenfolge, bt.thema_id limit 1) n;
$function$;
comment on function schule.naechster_flug(bigint, bigint) is 'AB-S: nächster Flug des Kindes laut Plan (Bordkarte) oder null';

-- ---------- Flug-Test: Angaben für „Flug geschafft“, Bordkarte und Orts-Abschluss ----------
create or replace function schule.flug_abschluss(p_l bigint, p_sitzung bigint)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare t schule.testsitzung; v_thema bigint; v_e schule.einheit; v_naechst jsonb; v_kurz text;
begin
  select * into t from schule.testsitzung where id = p_sitzung and lernender_id = p_l;
  if t.id is null then return '{}'::jsonb; end if;
  select * into v_e from schule.einheit where id = t.einheit_id;
  v_thema := coalesce(t.thema_id, v_e.thema_id);
  select x.kurz into v_kurz from schule.thema x where x.id = v_thema;
  v_naechst := schule.naechster_flug(p_l, v_thema);
  return jsonb_build_object(
    'sterne_flug', jsonb_build_object(
      'test', coalesce((select sum(s.menge) from schule.sterne s where s.lernender_id = p_l and s.grund = 'test' and s.bezug = 'sitzung:' || t.id), 0),
      'summe', coalesce((select sum(s.menge) from schule.sterne s
                          where s.lernender_id = p_l and s.grund in ('uebung', 'bonus') and s.bezug ~ '^aufgabe:[0-9]+$'
                            and exists (select 1 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
                                         where a.id = substr(s.bezug, 9)::bigint and e.thema_id = v_thema)), 0)
             + coalesce((select sum(s.menge) from schule.sterne s
                          where s.lernender_id = p_l and s.grund = 'test' and s.bezug ~ '^sitzung:[0-9]+$'
                            and exists (select 1 from schule.testsitzung x left join schule.einheit e on e.id = x.einheit_id
                                         where x.id = substr(s.bezug, 9)::bigint and x.lernender_id = p_l and coalesce(x.thema_id, e.thema_id) = v_thema)), 0)),
    'kurz', v_kurz,
    'flug', schule.flug_karte(p_l, t.block_id, v_thema),
    'etappen', (select coalesce(jsonb_agg(jsonb_build_object('lernziel', et->>'lernziel', 'titel', et->>'titel',
                   'kann', (select x.kann from schule.etappe_text x where x.thema_id = v_thema and x.lernziel = et->>'lernziel')) order by n.nr), '[]'::jsonb)
                  from jsonb_array_elements(coalesce(v_e.inhalt->'etappen', '[]'::jsonb)) with ordinality n(et, nr)),
    'ort_geschafft', coalesce(t.ort_geschafft, false),
    'ort_sterne', case when coalesce(t.ort_geschafft, false)
                       then coalesce((select sum(s.menge) from schule.sterne s where s.lernender_id = p_l and s.grund = 'ort' and s.bezug = 'block:' || t.block_id), 0) else 0 end,
    'ort_fluege', (select coalesce(jsonb_agg(jsonb_build_object('thema_id', th.id, 'titel', th.unterthema, 'zustand', z->>'zustand')
                     order by bt.reihenfolge, th.id), '[]'::jsonb)
                     from jsonb_array_elements(schule.ort_stand(p_l, t.block_id)->'themen') z
                     join schule.thema th on th.schluessel = z->>'thema'
                     join schule.block_thema bt on bt.block_id = t.block_id and bt.thema_id = th.id),
    'naechster_flug', v_naechst,
    'ort_wechsel', case when v_naechst is null then null else (v_naechst->>'block_id')::bigint <> t.block_id end);
end $function$;
comment on function schule.flug_abschluss(bigint, bigint) is 'AB-S: sterne_flug, Etappen mit „kann“, kurz, Flug i von k, ort_geschafft, Ort-Sterne, Flüge des Orts, nächster Flug – Zusatz zum Test-Ergebnis';

do $mig$
declare d text;
  v_alt1 text := $a$  v_ort := schule.ort_stand(p_lernender, t.block_id);$a$;
  v_neu1 text := $a$  v_ort := schule.ort_stand(p_lernender, t.block_id);
  -- AB-S: Ort durch diesen Abschluss geschafft? (vor dem Umstellen der Route auf „fertig“ einmal festgehalten)
  if t.ort_geschafft is null and t.status = 'abgeschlossen' then
    t.ort_geschafft := coalesce((v_ort->>'abgeschlossen')::boolean, false)
      and not exists (select 1 from schule.route ro where ro.lernender_id = p_lernender and ro.block_id = t.block_id and ro.art = 'normal' and ro.status = 'fertig');
    update schule.testsitzung set ort_geschafft = t.ort_geschafft where id = t.id;
  end if;$a$;
  v_alt2 text := $a$'nachtest', schule.nachtest_stand(p_lernender, t.einheit_id));$a$;
  v_neu2 text := $a$'nachtest', schule.nachtest_stand(p_lernender, t.einheit_id)) || schule.flug_abschluss(p_lernender, t.id);$a$;
begin
  d := pg_get_functiondef('schule.test_abschliessen_intern(bigint, jsonb)'::regprocedure);
  if position('flug_abschluss' in d) > 0 then return; end if;
  if position(v_alt1 in d) = 0 or position(v_alt2 in d) = 0 then raise exception 'test_abschliessen_intern: Stelle nicht gefunden'; end if;
  execute replace(replace(d, v_alt1, v_neu1), v_alt2, v_neu2);
end $mig$;

-- ---------- Flug lesen: Texte „kurz“ und „kann“ ----------
do $mig$
declare d text;
  v_alt text := $a$    'inhalt', e.inhalt - 'pruefhinweise', 'uebungen', v_ueb,$a$;
  v_neu text := $a$    'inhalt', e.inhalt - 'pruefhinweise', 'uebungen', v_ueb,
    'kurz', (select t.kurz from schule.thema t where t.id = e.thema_id), -- AB-S
    'kann', (select coalesce(jsonb_object_agg(et->>'lernziel', (select x.kann from schule.etappe_text x where x.thema_id = e.thema_id and x.lernziel = et->>'lernziel')), '{}'::jsonb)
               from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) et where et->>'lernziel' is not null),
    'landungen', (select coalesce(jsonb_object_agg(k.lernziel, k.landung_art), '{}'::jsonb) from schule.karte_stand k
                   where k.lernender_id = p_lernender and k.einheit_id = e.id and k.landung_art is not null),$a$;
begin
  d := pg_get_functiondef('schule.einheit_lesen_intern(bigint, bigint)'::regprocedure);
  if position('-- AB-S' in d) > 0 then return; end if;
  if position(v_alt in d) = 0 then raise exception 'einheit_lesen_intern: Stelle nicht gefunden'; end if;
  execute replace(d, v_alt, v_neu);
end $mig$;
