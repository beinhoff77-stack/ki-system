-- Bau-Auftrag G, Teil 1 (Werkstatt-Wunsch 176, P1): Punkteregel „gelandet“ / „sicher“ ohne Minuspunkte.
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE; kein Lernstand geht verloren, sitzende Etappen bleiben sitzend.
--
-- Regel „gelandet“ (intern weiter sitzt = true), alle Bedingungen:
--   1. eigene_loesungen ≥ ziel (karte_ziel: 6, bei wenigen freien Übungen mindestens 2) – es zählt nur „richtig im 1. Versuch ohne Tipp“
--   2. mindestens 2 verschiedene Aufgabentypen darunter (typen), sofern die Etappe mindestens 2 Typen hat (karte_typen_noetig)
--   3. mindestens 1 Stufe-3-Aufgabe mit Stufe-3-Typ (schwer_ok), sofern vorhanden (karte_schwer_noetig)
--   4. die letzten gewerteten Bordkarten in Folge richtig: folge ≥ min(3, ziel)
-- Fehler (endgültig falsch): keine Abzüge, folge = 0, fehler_folge + 1; nach 2 Fehlern in Folge sinkt die Stufe um 1 (stufe_senkung, höchstens 2).
-- Tipp oder 2. Versuch richtig: zählt nicht, folge bleibt.
-- Eigene Lösung: eigene_loesungen + 1, folge + 1, fehler_folge = 0, stufe_senkung − 1 (mindestens 0).
-- Wiederholung (Etappe sitzt): unverändert (1, 3, 7, 14, 30 Lerntage). Zwei Fehler in der Wiederholung: Etappe ist wieder offen – eigene Lösungen, Typen und die schwere
--   Bordkarte bleiben erhalten, es fehlen nur wieder 3 richtige in Folge (früher: Punkte auf 0).
-- „serie“ bleibt als Spalte und wird weiter geschrieben: serie = least(eigene_loesungen, ziel). So zeigt die alte App (0.75.1) bis zum Wechsel weiter Punkte und läuft ohne Fehler;
--   nur „sitzt“ verlangt jetzt auch Typen und Folge (in der alten App sieht man dann kurz „volle Punkte, noch nicht sitzt“).
-- „sicher“ (nur Anzeige): gelandet + Wiederholung nach 14 Lerntagen bestanden (wdh_stufe ≥ 4) + Nachtest des Flugs bestanden (+ ab Teil 3: Mischkarte richtig).
--
-- Neue Felder für die App: in schule_uebung_pruefen.karte, schule_einheit_lesen.etappen_stand[lernziel] und schule_lernstand.karten[]:
--   eigene_loesungen, folge, folge_ziel, typen_anzahl, typen_noetig, fehler_folge, stufe_senkung, sicher

alter table schule.karte_stand add column if not exists eigene_loesungen int not null default 0;
alter table schule.karte_stand add column if not exists typen text[] not null default '{}';
alter table schule.karte_stand add column if not exists folge int not null default 0;
alter table schule.karte_stand add column if not exists fehler_folge int not null default 0;
alter table schule.karte_stand add column if not exists stufe_senkung smallint not null default 0;
comment on column schule.karte_stand.eigene_loesungen is 'W176: richtig im 1. Versuch ohne Tipp (ohne Mischkarten, ohne Knobel)';
comment on column schule.karte_stand.typen is 'W176: Aufgabentypen der eigenen Lösungen';
comment on column schule.karte_stand.folge is 'W176: gewertete Bordkarten in Folge richtig (Fehler setzt auf 0)';
comment on column schule.karte_stand.fehler_folge is 'W176: endgültige Fehler in Folge (für die Stufensteuerung)';
comment on column schule.karte_stand.stufe_senkung is 'W176: um so viele Stufen leichter (nach je 2 Fehlern in Folge +1, je eigene Lösung −1)';
comment on column schule.karte_stand.serie is 'Seit W176 = least(eigene_loesungen, karte_ziel) – nur noch für alte App-Fassungen';

-- Bestandsübernahme (nur einmal: Zeilen, die noch nicht übernommen sind)
update schule.karte_stand k set
  eigene_loesungen = k.serie,
  folge = least(k.serie, 3),
  typen = coalesce((select array_agg(distinct a.typ order by a.typ) from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                     where v.lernender_id = k.lernender_id and a.einheit_id = k.einheit_id and a.variante_gruppe = k.lernziel and a.pool = 'uebung'
                       and v.testsitzung_id is null and v.richtig and coalesce(v.hilfe, 0) = 0 and coalesce(v.anlauf, 1) = 1 and a.typ is not null), '{}')
 where k.eigene_loesungen = 0 and k.folge = 0 and k.typen = '{}' and (k.serie > 0 or k.sitzt);

-- Typen, die eine Etappe für „gelandet“ braucht: 2, wenn ihre freien Übungen mindestens 2 Typen haben, sonst so viele, wie es gibt
create or replace function schule.karte_typen_noetig(p_einheit bigint, p_lz text)
 returns integer
 language sql
 stable
 set search_path to ''
as $function$
  select least(2, count(distinct a.typ))::int from schule.aufgabe a
   where a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben and a.typ is not null;
$function$;

-- „sicher“: gelandet + Wiederholung nach 14 Lerntagen bestanden + Nachtest des Flugs bestanden
create or replace function schule.karte_sicher(k schule.karte_stand)
 returns boolean
 language sql
 stable
 set search_path to ''
as $function$
  select coalesce(k.sitzt, false) and coalesce(k.wdh_stufe, 0) >= 4
     and exists (select 1 from schule.testsitzung t where t.lernender_id = k.lernender_id and t.einheit_id = k.einheit_id and t.art = 'nachtest' and t.ergebnis = 'bestanden');
$function$;

create or replace function schule.karte_buchen(p_l bigint, p_aufgabe bigint, p_richtig boolean, p_hilfe smallint, p_zeit timestamp with time zone)
 returns void
 language plpgsql
 set search_path to ''
as $function$
declare a schule.aufgabe; k schule.karte_stand; v_ziel int; v_eigen boolean;
  v_abst interval[] := array[interval '1 day', interval '3 days', interval '7 days', interval '14 days', interval '30 days'];
  v_tage smallint[] := array[1, 3, 7, 14, 30];
begin
  select * into a from schule.aufgabe where id = p_aufgabe;
  if a.id is null or a.pool <> 'uebung' then return; end if; -- Knobel (bonus), Test, Sicherung zählen nicht
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) values (p_l, a.einheit_id, a.variante_gruppe) on conflict do nothing;
  select * into k from schule.karte_stand where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe for update;
  v_ziel := schule.karte_ziel(a.einheit_id, a.variante_gruppe);
  v_eigen := p_richtig and coalesce(p_hilfe, 0) = 0;
  if p_richtig then k.richtig := k.richtig + 1; else k.falsch := k.falsch + 1; end if;
  if not k.sitzt then
    if v_eigen then
      k.eigene_loesungen := k.eigene_loesungen + 1; k.folge := k.folge + 1; k.fehler_folge := 0; k.stufe_senkung := greatest(k.stufe_senkung - 1, 0);
      if a.typ is not null and not (a.typ = any(k.typen)) then k.typen := k.typen || a.typ; end if;
      if a.stufe = 3 and (a.typ is null or a.typ in ('rueckwaerts', 'verknuepfen', 'begruenden', 'fehler', 'transfer', 'parameter', 'pruefung')) then k.schwer_ok := true; end if;
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
      if k.wdh_fehler >= 1 then -- zwei Fehler in der Wiederholung: wieder offen, Belege bleiben, es fehlen 3 in Folge
        k.sitzt := false; k.folge := 0; k.fehler_folge := 0; k.wdh_stufe := 0; k.faellig_am := null; k.wdh_fehler := 0; k.wdh_ab := null; k.wdh_lerntage := null;
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
    eigene_loesungen = k.eigene_loesungen, typen = k.typen, folge = k.folge, fehler_folge = k.fehler_folge, stufe_senkung = k.stufe_senkung
   where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;
end $function$;

-- Antworten an die App: die neuen Felder (gezieltes Ersetzen, Stellen im Live-Text vorab geprüft)
do $$
declare d text;
begin
  d := pg_get_functiondef('schule.uebung_pruefen_intern(bigint, jsonb)'::regprocedure);
  if position('''neu_sitzt'', k.sitzt and k.sitzt_am >= now() - interval ''5 seconds'' and k.wdh_stufe = 0, ''wdh_stufe'', k.wdh_stufe)' in d) = 0 then
    raise exception 'Stelle in uebung_pruefen_intern nicht gefunden';
  end if;
  d := replace(d, '''neu_sitzt'', k.sitzt and k.sitzt_am >= now() - interval ''5 seconds'' and k.wdh_stufe = 0, ''wdh_stufe'', k.wdh_stufe)',
    $r$'neu_sitzt', k.sitzt and k.sitzt_am >= now() - interval '5 seconds' and k.wdh_stufe = 0, 'wdh_stufe', k.wdh_stufe,
                'eigene_loesungen', k.eigene_loesungen, 'folge', k.folge, 'folge_ziel', least(3, schule.karte_ziel(k.einheit_id, k.lernziel)),
                'typen_anzahl', coalesce(array_length(k.typen, 1), 0), 'typen_noetig', schule.karte_typen_noetig(k.einheit_id, k.lernziel),
                'fehler_folge', k.fehler_folge, 'stufe_senkung', k.stufe_senkung, 'sicher', schule.karte_sicher(k))$r$);
  execute d;

  d := pg_get_functiondef('schule.etappen_stand(bigint, bigint)'::regprocedure);
  if position('''wdh_stufe'', coalesce(k.wdh_stufe, 0),' in d) = 0 then raise exception 'Stelle in etappen_stand nicht gefunden'; end if;
  d := replace(d, '''wdh_stufe'', coalesce(k.wdh_stufe, 0),',
    $r$'wdh_stufe', coalesce(k.wdh_stufe, 0),
           'eigene_loesungen', coalesce(k.eigene_loesungen, 0), 'folge', coalesce(k.folge, 0), 'folge_ziel', least(3, schule.karte_ziel(p_einheit, z.lz)),
           'typen_anzahl', coalesce(array_length(k.typen, 1), 0), 'typen_noetig', schule.karte_typen_noetig(p_einheit, z.lz),
           'fehler_folge', coalesce(k.fehler_folge, 0), 'stufe_senkung', coalesce(k.stufe_senkung, 0), 'sicher', coalesce(schule.karte_sicher(k), false),$r$);
  execute d;

  d := pg_get_functiondef('api.schule_lernstand(text, jsonb)'::regprocedure);
  if position('''sitzt_am'', k.sitzt_am,' in d) = 0 then raise exception 'Stelle in schule_lernstand nicht gefunden'; end if;
  d := replace(d, '''sitzt_am'', k.sitzt_am,',
    $r$'sitzt_am', k.sitzt_am, 'eigene_loesungen', coalesce(k.eigene_loesungen, 0), 'folge', coalesce(k.folge, 0),
              'typen_anzahl', coalesce(array_length(k.typen, 1), 0), 'sicher', coalesce(schule.karte_sicher(k), false),$r$);
  execute d;
end $$;
