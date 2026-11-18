-- Bau-Auftrag H (Werkstatt-Wunsch 176): Muss-Punkte H1–H4 (Punkteregel) und H9–H11 (Mischkarten, Expeditionen); dazu H15 (Misch-Beleg nach der letzten Landung).
-- Setzt H8 (20261119_w176_h8_*) voraus. Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE. Gelandete Etappen bleiben gelandet, Lernstände bleiben.
--
-- H1  „fertig“ einer Etappe = gelandet (karte_stand.sitzt); ein früher bestandener Test zählt nur, solange die Etappe nie gelandet war (alte Stände ohne Übungsweg).
--     Nach einem Wiederöffnen (sitzt = false, sitzt_am gesetzt) ist die Etappe überall offen; der bestandene Test steht getrennt in test_nachgewiesen.
--     Neu: karte_stand.geoeffnet_am (Zeitpunkt des letzten Wiederöffnens); schule_uebersicht.stand[].wieder_offen je Flug.
-- H2  Bestandsübernahme vom 17.11.: „folge“ offener Etappen aus den zeitlich geordneten endgültigen Versuchen nachgerechnet (nur Zeilen ohne Versuch seit der Übernahme;
--     früher schon einmal gelandete offene Etappen → 0). eigene_loesungen und sitzt unverändert.
-- H3  Für eigene_loesungen, Typen und „schwere“ zählt jede Aufgabe je Etappe nur einmal (karte_stand.gezaehlt = {aufgabe_id: Zeit}); für „in Folge“ zählt jede eigene Lösung.
--     Nach einem Wiederöffnen sind eigene Lösungen/Typen/schwere schon erfüllt; zum Wiederlanden fehlen nur 3 in Folge – dafür zählen auch bekannte Aufgaben. Eine Sonderregel
--     „zählt nach einem Lerntag wieder“ ist deshalb nicht nötig. Antwort an die App: karte.neu_gezaehlt (false = „Die kennst du schon – gut wiederholt.“).
--     Bestand: gezaehlt aus den bisherigen eigenen Lösungen (richtig, 1. Versuch, ohne Tipp) gefüllt.
-- H4  „sicher“ = gelandet + Wiederholung nach 14 Lerntagen bestanden + Mischkarte richtig NACH der letzten Landung (H15) + im Flug-Nachtest NACH der letzten Landung war eine Bordkarte
--     dieser Etappe richtig. Neu getrennt: flug_nachtest (irgendein Nachtest des Flugs bestanden) zur ehrlichen Anzeige.
-- H9  Expeditions-Teil wird nur gewertet, wenn alle Voraussetzungen gelandet sind – oder die Expedition schon begonnen ist (Rückfall danach: zu Ende führen ohne Nachteil).
--     expedition.klasse ist reine Einordnung für Eltern (kein Ausschluss).
-- H10 Misch-Beleg nur, wenn der Server die Mischkarte bestätigt: Pool uebung, Stufe 2–3, freigegeben, Etappe beim Kind gelandet, nicht die gerade geübte Etappe
--     (App schickt aktuell_einheit und aktuell_lernziel). Sonst normale Buchung ohne Misch-Beleg.
-- H11 Expedition bucht je Kind auf die tatsächlich gelandete Version der Etappe (thema_id + Lernkarte), nicht starr auf die beim Import gebundene einheit_id.

alter table schule.karte_stand add column if not exists geoeffnet_am timestamptz;
alter table schule.karte_stand add column if not exists gezaehlt jsonb not null default '{}'::jsonb;
comment on column schule.karte_stand.geoeffnet_am is 'W176 H1: zuletzt durch zwei Fehler in der fälligen Wiederholung wieder geöffnet';
comment on column schule.karte_stand.gezaehlt is 'W176 H3: Aufgaben, die als eigene Lösung gezählt haben {aufgabe_id: Zeit} – jede zählt je Etappe einmal';

-- ---------- H3 Bestand: gezaehlt aus den bisherigen eigenen Lösungen ----------
update schule.karte_stand k set gezaehlt = x.m
  from (select v.lernender_id, a.einheit_id, a.variante_gruppe lz, jsonb_object_agg(a.id::text, v.erst) m
          from (select v.lernender_id, v.aufgabe_id, min(v.am) erst from schule.versuch v
                 where v.testsitzung_id is null and v.richtig and coalesce(v.hilfe, 0) = 0 and coalesce(v.anlauf, 1) = 1 and not v.misch group by 1, 2) v
          join schule.aufgabe a on a.id = v.aufgabe_id and a.pool = 'uebung'
         group by 1, 2, 3) x
 where k.lernender_id = x.lernender_id and k.einheit_id = x.einheit_id and k.lernziel = x.lz and k.gezaehlt = '{}'::jsonb;

-- ---------- H2 Bestand: „folge“ offener Etappen nachrechnen ----------
do $$
declare r record; v record; f int; n_neu int := 0; n_null int := 0; n_gleich int := 0;
begin
  for r in select k.* from schule.karte_stand k
            where not k.sitzt and k.folge > 0
              and not exists (select 1 from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                               where v.lernender_id = k.lernender_id and a.einheit_id = k.einheit_id and a.variante_gruppe = k.lernziel and a.pool = 'uebung'
                                 and v.testsitzung_id is null and v.am > '2026-11-17 15:17:24+00') loop -- Übernahme (w176_t1) eingespielt 17.11. 15:17 UTC
    if r.sitzt_am is not null then f := 0; -- war schon einmal gelandet: Reihenfolge nach dem Öffnen nicht eindeutig → 0
    else
      f := 0;
      for v in select v.richtig, v.hilfe, v.anlauf from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                where v.lernender_id = r.lernender_id and a.einheit_id = r.einheit_id and a.variante_gruppe = r.lernziel and a.pool = 'uebung'
                  and v.testsitzung_id is null and not (coalesce(v.anlauf, 0) = 1 and not v.richtig) order by v.am, v.id loop
        if v.richtig and coalesce(v.hilfe, 0) = 0 and coalesce(v.anlauf, 1) = 1 then f := f + 1;
        elsif not v.richtig then f := 0; end if; -- Tipp/2. Versuch richtig: Folge bleibt
      end loop;
    end if;
    if f = r.folge then n_gleich := n_gleich + 1;
    else
      update schule.karte_stand set folge = f where lernender_id = r.lernender_id and einheit_id = r.einheit_id and lernziel = r.lernziel;
      if f = 0 then n_null := n_null + 1; else n_neu := n_neu + 1; end if;
    end if;
  end loop;
  raise notice 'H2: folge nachgerechnet – % geändert (davon % auf 0), % unverändert', n_neu + n_null, n_null, n_gleich;
end $$;

-- ---------- H1: „fertig“ einer Etappe ----------
create or replace function schule.etappe_fertig(k schule.karte_stand, p_status text)
 returns boolean language sql stable set search_path to ''
as $function$
  select coalesce(k.sitzt, false) or (k.sitzt_am is null and coalesce(p_status in ('nachgewiesen', 'korrigiert', 'gesichert'), false));
$function$;

-- ---------- H4/H15: „sicher“ ----------
create or replace function schule.karte_sicher(k schule.karte_stand)
 returns boolean language sql stable set search_path to ''
as $function$
  select coalesce(k.sitzt, false) and coalesce(k.wdh_stufe, 0) >= 4
     and k.misch_ok_am is not null and k.misch_ok_am >= k.sitzt_am
     and exists (select 1 from schule.testsitzung t join schule.versuch v on v.testsitzung_id = t.id join schule.aufgabe a on a.id = v.aufgabe_id
                  where t.lernender_id = k.lernender_id and t.einheit_id = k.einheit_id and t.art = 'nachtest' and t.ergebnis = 'bestanden'
                    and t.abgeschlossen_am >= k.sitzt_am and a.variante_gruppe = k.lernziel and v.richtig);
$function$;
create or replace function schule.flug_nachtest(p_lernender bigint, p_einheit bigint)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from schule.testsitzung t where t.lernender_id = p_lernender and t.einheit_id = p_einheit and t.art = 'nachtest' and t.ergebnis = 'bestanden');
$function$;

-- ---------- H10: Mischkarte serverseitig bestätigen ----------
create or replace function schule.misch_gueltig(p_lernender bigint, a schule.aufgabe, p jsonb)
 returns boolean language sql stable set search_path to ''
as $function$
  select coalesce(coalesce((p->>'misch')::boolean, false) and a.pool = 'uebung' and a.stufe in (2, 3) and a.freigegeben
     and nullif(p->>'aktuell_einheit', '') is not null and nullif(p->>'aktuell_lernziel', '') is not null
     and not ((p->>'aktuell_einheit')::bigint = a.einheit_id and p->>'aktuell_lernziel' = a.variante_gruppe)
     and exists (select 1 from schule.karte_stand k where k.lernender_id = p_lernender and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe and k.sitzt), false);
$function$;

-- ---------- H1/H3: karte_buchen ----------
create or replace function schule.karte_buchen(p_l bigint, p_aufgabe bigint, p_richtig boolean, p_hilfe smallint, p_zeit timestamp with time zone)
 returns void
 language plpgsql
 set search_path to ''
as $function$
declare a schule.aufgabe; k schule.karte_stand; v_ziel int; v_eigen boolean; v_neu boolean;
  v_abst interval[] := array[interval '1 day', interval '3 days', interval '7 days', interval '14 days', interval '30 days'];
  v_tage smallint[] := array[1, 3, 7, 14, 30];
begin
  select * into a from schule.aufgabe where id = p_aufgabe;
  if a.id is null or a.pool <> 'uebung' then return; end if; -- Knobel (bonus), Expedition, Test, Sicherung zählen nicht
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) values (p_l, a.einheit_id, a.variante_gruppe) on conflict do nothing;
  select * into k from schule.karte_stand where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe for update;
  v_ziel := schule.karte_ziel(a.einheit_id, a.variante_gruppe);
  v_eigen := p_richtig and coalesce(p_hilfe, 0) = 0;
  if p_richtig then k.richtig := k.richtig + 1; else k.falsch := k.falsch + 1; end if;
  if not k.sitzt then
    if v_eigen then
      v_neu := not (k.gezaehlt ? a.id::text); -- H3: jede Aufgabe zählt je Etappe einmal als Nachweis
      k.folge := k.folge + 1; k.fehler_folge := 0; k.stufe_senkung := greatest(k.stufe_senkung - 1, 0);
      if v_neu then
        k.eigene_loesungen := k.eigene_loesungen + 1; k.gezaehlt := k.gezaehlt || jsonb_build_object(a.id::text, p_zeit);
        if a.typ is not null and not (a.typ = any(k.typen)) then k.typen := k.typen || a.typ; end if;
        if a.stufe = 3 and (a.typ is null or a.typ in ('rueckwaerts', 'verknuepfen', 'begruenden', 'fehler', 'transfer', 'parameter', 'pruefung')) then k.schwer_ok := true; end if;
      end if;
    elsif not p_richtig then
      k.folge := 0; k.fehler_folge := k.fehler_folge + 1;
      if k.fehler_folge % 2 = 0 then k.stufe_senkung := least(k.stufe_senkung + 1, 2); end if;
    end if; -- Tipp oder 2. Versuch richtig: zählt nicht, folge bleibt
    k.serie := least(k.eigene_loesungen, v_ziel);
    if k.eigene_loesungen >= v_ziel
       and coalesce(array_length(k.typen, 1), 0) >= schule.karte_typen_noetig(a.einheit_id, a.variante_gruppe)
       and (k.schwer_ok or not schule.karte_schwer_noetig(a.einheit_id, a.variante_gruppe))
       and k.folge >= least(3, v_ziel) then
      k.sitzt := true; k.sitzt_am := p_zeit; k.wdh_stufe := 0; k.faellig_am := p_zeit + v_abst[1]; k.wdh_fehler := 0;
      k.wdh_ab := p_zeit; k.wdh_lerntage := v_tage[1];
    end if;
  else
    if not p_richtig then
      if k.wdh_fehler >= 1 then -- zwei Fehler in der fälligen Wiederholung: wieder offen (H1: überall), Belege bleiben, es fehlen 3 in Folge
        k.sitzt := false; k.geoeffnet_am := p_zeit; k.folge := 0; k.fehler_folge := 0; k.wdh_stufe := 0; k.faellig_am := null; k.wdh_fehler := 0; k.wdh_ab := null; k.wdh_lerntage := null;
      else
        k.wdh_fehler := 1; k.wdh_stufe := greatest(k.wdh_stufe - 1, 0); k.faellig_am := p_zeit + interval '1 day';
        k.wdh_ab := p_zeit; k.wdh_lerntage := 1;
      end if;
    else
      k.wdh_fehler := 0;
      if schule.karte_faellig(k) then
        k.wdh_stufe := least(k.wdh_stufe + 1, 4); k.faellig_am := p_zeit + v_abst[k.wdh_stufe + 1];
        k.wdh_ab := p_zeit; k.wdh_lerntage := v_tage[k.wdh_stufe + 1];
      end if;
    end if;
  end if;
  update schule.karte_stand set serie = k.serie, richtig = k.richtig, falsch = k.falsch, sitzt = k.sitzt, sitzt_am = k.sitzt_am, schwer_ok = k.schwer_ok,
    wdh_stufe = k.wdh_stufe, faellig_am = k.faellig_am, wdh_fehler = k.wdh_fehler, wdh_ab = k.wdh_ab, wdh_lerntage = k.wdh_lerntage, zuletzt = p_zeit,
    eigene_loesungen = k.eigene_loesungen, typen = k.typen, folge = k.folge, fehler_folge = k.fehler_folge, stufe_senkung = k.stufe_senkung,
    gezaehlt = k.gezaehlt, geoeffnet_am = k.geoeffnet_am
   where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;
end $function$;

-- ---------- H11 (+ H8): Expedition bucht auf die gelandete Version der Etappe ----------
create or replace function schule.expedition_etappe(p_l bigint, a schule.aufgabe)
 returns bigint language sql stable set search_path to ''
as $function$
  select coalesce((select k.einheit_id from schule.karte_stand k join schule.einheit e on e.id = k.einheit_id
                    where k.lernender_id = p_l and e.thema_id = a.thema_id and k.lernziel = a.variante_gruppe
                    order by k.sitzt desc, k.sitzt_am desc nulls last, e.version desc limit 1), a.einheit_id);
$function$;

create or replace function schule.expedition_buchen(p_l bigint, p_aufgabe bigint, p_richtig boolean, p_hilfe smallint, p_anlauf smallint, p_zeit timestamp with time zone)
 returns void
 language plpgsql
 set search_path to ''
as $function$
declare a schule.aufgabe; v_e bigint;
begin
  select * into a from schule.aufgabe where id = p_aufgabe;
  if a.id is null or a.pool <> 'expedition' then return; end if;
  v_e := schule.expedition_etappe(p_l, a); -- H11
  if p_richtig then
    if coalesce(p_hilfe, 0) = 0 and coalesce(p_anlauf, 1) = 1 then
      update schule.karte_stand set angewandt_am = p_zeit where lernender_id = p_l and einheit_id = v_e and lernziel = a.variante_gruppe;
    end if;
  else
    perform schule.karte_faellig_machen(p_l, v_e, a.variante_gruppe, p_zeit); -- H8: nur fällig, nie wieder öffnen
  end if;
  if not exists (select 1 from schule.aufgabe t where t.expedition_id = a.expedition_id and t.freigegeben and not schule.expedition_teil_erledigt(p_l, t.id)) then
    insert into schule.sterne(lernender_id, menge, grund, bezug)
    values (p_l, schule.sterne_regel('sterne_expedition_geschafft'), 'expedition', 'expedition:' || a.expedition_id)
    on conflict do nothing;
  end if;
end $function$;

-- ---------- Antworten (gezieltes Ersetzen; Stellen im Live-Text vorab geprüft) ----------
do $$
declare d text;
begin
  -- uebung_pruefen_intern: H10 Misch-Prüfung, H9 Expedition nur mit Voraussetzungen oder begonnen, H1/H3 Felder in karte
  d := pg_get_functiondef('schule.uebung_pruefen_intern(bigint, jsonb)'::regprocedure);
  if (length(d) - length(replace(d, 'coalesce((p_daten->>''misch'')::boolean, false) and a.pool = ''uebung''', ''))) / length('coalesce((p_daten->>''misch'')::boolean, false) and a.pool = ''uebung''') <> 2
     or position('if a.pool = ''expedition'' and not exists (select 1 from schule.expedition x where x.id = a.expedition_id and schule.expedition_sichtbar(p_lernender, x)) then' in d) = 0
     or position('''fehler_folge'', k.fehler_folge, ''stufe_senkung'', k.stufe_senkung, ''sicher'', schule.karte_sicher(k))' in d) = 0 then
    raise exception 'Stellen in uebung_pruefen_intern nicht gefunden';
  end if;
  d := replace(d, 'coalesce((p_daten->>''misch'')::boolean, false) and a.pool = ''uebung''', 'schule.misch_gueltig(p_lernender, a, p_daten)');
  d := replace(d, 'if a.pool = ''expedition'' and not exists (select 1 from schule.expedition x where x.id = a.expedition_id and schule.expedition_sichtbar(p_lernender, x)) then',
    $r$if a.pool = 'expedition' and exists (select 1 from schule.expedition x where x.id = a.expedition_id and schule.expedition_sichtbar(p_lernender, x))
     and not exists (select 1 from schule.expedition x where x.id = a.expedition_id
                      and (schule.expedition_voraussetzungen_ok(p_lernender, x)
                           or exists (select 1 from schule.versuch v join schule.aufgabe t on t.id = v.aufgabe_id where v.lernender_id = p_lernender and t.expedition_id = x.id))) then
    raise exception 'Diese Expedition ist noch nicht offen – es fehlen gelandete Etappen' using errcode = 'P0001'; -- H9
  end if;
  if a.pool = 'expedition' and not exists (select 1 from schule.expedition x where x.id = a.expedition_id and schule.expedition_sichtbar(p_lernender, x)) then$r$);
  d := replace(d, '''fehler_folge'', k.fehler_folge, ''stufe_senkung'', k.stufe_senkung, ''sicher'', schule.karte_sicher(k))',
    $r$'fehler_folge', k.fehler_folge, 'stufe_senkung', k.stufe_senkung, 'sicher', schule.karte_sicher(k),
                'fertig', schule.etappe_fertig(k, (select s.status from schule.lernziel_stand s where s.lernender_id = k.lernender_id and s.einheit_id = k.einheit_id and s.lernziel = k.lernziel)),
                'neu_gezaehlt', v_ri and v_hilfe = 0 and coalesce(v_anlauf, 1) = 1 and k.gezaehlt ? a.id::text
                  and not exists (select 1 from schule.versuch v2 where v2.lernender_id = p_lernender and v2.aufgabe_id = a.id and v2.client_id <> v_cid and v2.testsitzung_id is null
                                   and v2.richtig and coalesce(v2.hilfe, 0) = 0 and coalesce(v2.anlauf, 1) = 1 and not coalesce(v2.misch, false)), 'flug_nachtest', schule.flug_nachtest(k.lernender_id, k.einheit_id),
                'gezaehlt', coalesce((select jsonb_agg(x::bigint) from jsonb_object_keys(k.gezaehlt) x), '[]'::jsonb))$r$);
  execute d;

  -- etappen_stand: H1 fertig, test_nachgewiesen; H4 flug_nachtest
  d := pg_get_functiondef('schule.etappen_stand(bigint, bigint)'::regprocedure);
  if position('''fertig'', coalesce(k.sitzt, false) or coalesce(s.status in (''nachgewiesen'',''korrigiert'',''gesichert''), false)' in d) = 0
     or position('''misch_ok'', k.misch_ok_am is not null,' in d) = 0 then raise exception 'Stellen in etappen_stand nicht gefunden'; end if;
  d := replace(d, '''fertig'', coalesce(k.sitzt, false) or coalesce(s.status in (''nachgewiesen'',''korrigiert'',''gesichert''), false)',
    '''fertig'', schule.etappe_fertig(k, s.status), ''test_nachgewiesen'', coalesce(s.status in (''nachgewiesen'',''korrigiert'',''gesichert''), false), ''wieder_offen'', not coalesce(k.sitzt, false) and k.sitzt_am is not null, ''gezaehlt'', coalesce((select jsonb_agg(x::bigint) from jsonb_object_keys(k.gezaehlt) x), ''[]''::jsonb)');
  d := replace(d, '''misch_ok'', k.misch_ok_am is not null,', '''misch_ok'', k.misch_ok_am is not null and k.misch_ok_am >= coalesce(k.sitzt_am, k.misch_ok_am), ''flug_nachtest'', schule.flug_nachtest(p_lernender, p_einheit),');
  execute d;

  -- schule_lernstand: wieder offen, flug_nachtest, Misch-Beleg nach der letzten Landung
  d := pg_get_functiondef('api.schule_lernstand(text, jsonb)'::regprocedure);
  if position('''misch_ok'', k.misch_ok_am is not null,' in d) = 0 then raise exception 'Stelle in schule_lernstand nicht gefunden'; end if;
  d := replace(d, '''misch_ok'', k.misch_ok_am is not null,', '''misch_ok'', k.misch_ok_am is not null and k.misch_ok_am >= coalesce(k.sitzt_am, k.misch_ok_am), ''wieder_offen'', not coalesce(k.sitzt, false) and k.sitzt_am is not null, ''flug_nachtest'', schule.flug_nachtest(v_l, e.id),');
  execute d;

  -- schule_uebersicht: je Flug Zahl der wieder geöffneten Etappen (Abflugtafel: Flug „wackelt“)
  d := pg_get_functiondef('api.schule_uebersicht(text, jsonb)'::regprocedure);
  if position('''fertig'', g.fertig, ''fehler'', g.fehler, ''gesichert'', g.gesichert,' in d) = 0
     or position('count(*) filter (where s.pflicht and s.status in (''nachgewiesen'',''korrigiert'',''gesichert'')) as fertig' in d) = 0
     or position('from schule.lernziel_stand s where s.lernender_id = l.id group by s.einheit_id' in d) = 0 then raise exception 'Stelle in schule_uebersicht nicht gefunden'; end if;
  -- H1: „fertig“ je Flug zählt gelandete Etappen (wieder geöffnete nicht mehr); Etappen ohne Übungsweg wie bisher über den Test
  d := replace(d, 'count(*) filter (where s.pflicht and s.status in (''nachgewiesen'',''korrigiert'',''gesichert'')) as fertig', 'count(*) filter (where s.pflicht and schule.etappe_fertig(ks, s.status)) as fertig');
  d := replace(d, 'from schule.lernziel_stand s where s.lernender_id = l.id group by s.einheit_id',
    'from schule.lernziel_stand s left join schule.karte_stand ks on ks.lernender_id = s.lernender_id and ks.einheit_id = s.einheit_id and ks.lernziel = s.lernziel where s.lernender_id = l.id group by s.einheit_id');
  d := replace(d, '''fertig'', g.fertig, ''fehler'', g.fehler, ''gesichert'', g.gesichert,',
    '''fertig'', g.fertig, ''fehler'', g.fehler, ''gesichert'', g.gesichert, ''wieder_offen'', (select count(*) from schule.karte_stand k where k.lernender_id = l.id and k.einheit_id = g.einheit_id and not k.sitzt and k.sitzt_am is not null),');
  execute d;
end $$;
