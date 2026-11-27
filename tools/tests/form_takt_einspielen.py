"""Einspiel-Paket für FT-S (Form-Takt, Teil Datenbank) – prüft sich selbst.

EIN SQL für EINEN Aufruf (eine Sitzung, eine Transaktion). Bei der kleinsten Abweichung: Ausnahme -> alles zurück.
Ablauf:
  1. Vorher-Stand: Definition und Rechte der 17 geänderten und 6 neuen Funktionen; Prüfsummen über schule.karte_stand (alle Kinder; nur md5);
     Übung mit dem Testkind an einer bestehenden Aufgabe (erster Fehlversuch und zweiter Fehlversuch in einer, richtig in einer zweiten
     zurückgerollten Untertransaktion) – Antworten und Karte (md5) festgehalten.
  2. Migration ausführen, dann vollständig noch einmal.
  3. Prüfblock:
     · zweiter Lauf ändert nichts; Rechte der bestehenden Funktionen unverändert; neue Hilfen für anon/authenticated gesperrt; Spalten nullable
       ohne Vorgabe, beide Prüfbedingungen gültig, kein Bestand mit form/zaehlt; Regel form_jede da
     · Mischstand: halb umgestellte Funktion und Funktion in fremder Fassung werden abgewiesen; Gegenprobe: alte Definitionen -> Einbau = neue
     · Bestand: dieselbe Übung antwortet Zeichen für Zeichen wie vorher (bis auf die drei neuen Felder in „karte“), die Karte (md5) ist gleich
     · zaehlt = nein (Aufgaben nur in zurückgerollten Untertransaktionen): bewertet und gespeichert, Karte unverändert (auch eine bestehende Karte),
       Folge weder verlängert noch unterbrochen; form + zaehlt = ja zählt; zwei Anläufe = eine Bearbeitung; Anzeige mit form/zaehlt; form_jede
       und die neuen Felder in einheit_lesen_intern
     · unbekannter form-Wert und zaehlt = folge scheitern an den Prüfbedingungen; aufgaben_einfuegen übernimmt form/zaehlt
     · Sachaufgaben-Pflicht: Lernkarte mit Sachaufgabe landet nach 6 eigenen Lösungen ohne sie NICHT, mit ihr schon; Lernkarte, deren einzige
       Sachaufgabe zaehlt = nein hat, landet ohne
     · Wiederholung und Mischkarte ziehen keine Aufgabe mit zaehlt = nein
     · Nachträge nach Gegenprüfung 1030/1032 (Abschnitte 8–12):
       8  fällige, sitzende Karte: Aufgabe mit zaehlt = nein richtig, endgültig falsch, mit Misch-Wunsch – ganze Kartenzeile gleich, keine
          Wiederholung gebucht; derselbe client_id noch einmal: kein Versuch, kein Taktplatz mehr
       9  Filter als Verhalten: Typ nur in zaehlt = nein -> keine Typen-Pflicht; einzige Stufe-3-Aufgabe zaehlt = nein -> keine Schwer-Pflicht
          (je mit Gegenprobe zaehlt = ja); folge_nachrechnen nach nicht zählendem Fehler = laufende Buchung
       10 Übergänge: Sachaufgabe schon in gezaehlt (Bestand, vor dem Einschalten) -> Pflicht sofort erfüllt; früher gelandete, wieder
          geöffnete Karte landet wieder ohne Sachaufgabe
       11 nicht zählender Versuch schließt einen offenen ersten Fehlversuch einer ANDEREN, zählenden Aufgabe ab (bleibt so)
       12 Schalter anwenden_pflicht: beim Einspielen 0 (aus: Karte landet ohne Sachaufgabe, anwenden_noetig false); Einschalt-Befehl wirkt,
          ein zweiter Lauf der Migration setzt ihn nicht zurück. Stellung „an“ in Abschnitt 6.
       Bearbeitungsstand: Antwort trägt bearbeitungen auch ohne karte (erste nicht zählende Aufgabe einer Lernkarte, Abschnitt 4)
     · 13 schon sitzende Karten: Prüfsummen (sitzt, sitzt_am, eigene_loesungen, gezaehlt, folge und ganze Zeile) am Ende gleich; keine sitzende
       Karte hätte bei eingeschaltetem Schalter eine Sachaufgaben-Pflicht
Ausgegeben werden nur Zählungen, Prüfsummen und die Antworten der Probe-Aufgaben (ohne Lösung) – keine Namen, keine Lerndaten.

Aufruf:  python3 -I tools/tests/form_takt_einspielen.py > ft.sql             (Einspielung)
         python3 -I tools/tests/form_takt_einspielen.py --probe > ft_probe.sql (Probelauf: alles läuft, am Ende wird ALLES zurückgerollt;
                                                                                der Bericht steht in der Fehlermeldung)
Nicht ohne den ausdrücklichen Satz des Nutzers ausführen. Vorher: werkstatt_sperre. Nachher: werkstatt_aenderung. Nur in einer Nutzungspause
(schule.aufgabe ist bis zum Ende der Transaktion gesperrt).
"""
import re
import sys
from pathlib import Path

MIG = Path(__file__).resolve().parent.parent.parent / 'supabase/migrations/20261203_ft_s_form_takt.sql'
NEU = ['schule.aufgabe_zaehlt(schule.aufgabe)', 'schule.aufgabe_anwenden(schule.aufgabe)', 'schule.karte_anwenden_noetig(bigint, text)',
       'schule.karte_anwenden_pflicht(schule.karte_stand, bigint, text)', 'schule.karte_anwenden_ok(schule.karte_stand)', 'schule.karte_bearbeitungen(bigint, bigint, text)']
KOPF = 'do $$\ndeclare\n  f record;'
NEUE_FELDER = " #- '{karte,anwenden_noetig}' #- '{karte,anwenden_ok}' #- '{karte,bearbeitungen}' #- '{bearbeitungen}'"


def arr(xs):
    return 'array[' + ', '.join(f"'{x}'" for x in xs) + ']::text[]'


def F(msg):
    """Fehler anhängen (msg ist ein SQL-Ausdruck vom Typ text)."""
    return f'fehler := fehler || ({msg})::text;'


def zurueck(name):
    """Ende einer Untertransaktion, die immer zurückgerollt wird."""
    return (f"    raise exception using errcode = 'FT999', message = 'zurueck';\n  exception\n    when sqlstate 'FT999' then null;\n"
            f"    when others then {F(chr(39) + name + ': ' + chr(39) + ' || sqlerrm')}\n  end;")


def main():
    probe = '--probe' in sys.argv[1:]
    # eingebettet ohne die ganzzeiligen Kommentare (beginnen in Spalte 0 mit --) und ohne Leerzeilen – sonst Zeichen für Zeichen die Datei
    mig = '\n'.join(z for z in MIG.read_text(encoding='utf-8').split('\n') if z.strip() and not z.startswith('--')) + '\n'
    for marke in ('$ftmig$', '$ftalt$', '$pruef$', '$x$', '$f$', '$chk$', '$m$'):
        assert marke not in mig, marke
    assert mig.count(KOPF) == 1
    i = mig.index(KOPF)
    patch = mig[i:mig.index('end $$;', i) + len('end $$;')]
    assert 'plan constant jsonb' in patch and patch.count('end $$;') == 1
    patch_fn = re.findall(r"jsonb_build_object\('f', '([^']+)'", patch)
    assert len(patch_fn) == 17, len(patch_fn)
    alle = patch_fn + NEU
    k = '(select id from schule.lernender where ist_test order by id limit 1)'
    basis = "(select min(id) from schule.aufgabe where pool = 'uebung' and antworttyp = 'zahl' and freigegeben)"
    kpruef = """(select md5(coalesce(string_agg(concat_ws('|', x.lernender_id, x.einheit_id, x.lernziel, x.sitzt, x.sitzt_am, x.eigene_loesungen, x.gezaehlt, x.folge), '#' order by x.lernender_id, x.einheit_id, x.lernziel), '')) from schule.karte_stand x),
       (select md5(coalesce(string_agg(x::text, '#' order by x.lernender_id, x.einheit_id, x.lernziel), '')) from schule.karte_stand x),
       (select count(*) from schule.karte_stand x where x.sitzt), (select count(*) from schule.aufgabe)"""
    teile = kpruef.split(',\n       ')
    kpruef_n = ',\n       '.join(t + ' as ' + n for t, n in zip(teile, ('spalten', 'ganz', 'sitzend', 'aufgaben')))
    ende = ("raise exception 'PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt): %', (select b::text from ft_bericht);" if probe else '')
    alt = f"""do $x$
declare k bigint := {k}; a schule.aufgabe; o jsonb := '{{}}';
begin
  select * into a from schule.aufgabe where id = {basis};
  if k is null or a.id is null then raise exception 'FT-S: Testkind oder Vergleichsaufgabe fehlt'; end if;
  begin
    perform schule.offene_entscheiden(k);
    o := o || jsonb_build_object('start', jsonb_build_object('m', pg_temp.ft_k(k, a.einheit_id, a.variante_gruppe)));
    o := o || jsonb_build_object('falsch-1', jsonb_build_object('r', pg_temp.ft_ant(k, a.id, false, 1, 'ft-b-1'), 'm', pg_temp.ft_k(k, a.einheit_id, a.variante_gruppe)));
    o := o || jsonb_build_object('falsch-2', jsonb_build_object('r', pg_temp.ft_ant(k, a.id, false, 2, 'ft-b-2'), 'm', pg_temp.ft_k(k, a.einheit_id, a.variante_gruppe)));
    raise exception using errcode = 'FT999', message = 'zurueck';
  exception when sqlstate 'FT999' then null;
  end;
  begin
    perform schule.offene_entscheiden(k);
    o := o || jsonb_build_object('richtig', jsonb_build_object('r', pg_temp.ft_ant(k, a.id, true, 1, 'ft-b-3'), 'm', pg_temp.ft_k(k, a.einheit_id, a.variante_gruppe)));
    raise exception using errcode = 'FT999', message = 'zurueck';
  exception when sqlstate 'FT999' then null;
  end;
  insert into ft_aus values ('PHASE', o);
end $x$;"""
    karte = lambda lz: f"(select x from schule.karte_stand x where x.lernender_id = k and x.einheit_id = v_e and x.lernziel = '{lz}')"
    zeile = lambda lz: f"(select x::text from schule.karte_stand x where x.lernender_id = k and x.einheit_id = v_e and x.lernziel = '{lz}')"
    ohne = lambda x: f"(({x}) - 'loesung' - 'loesungsweg')"
    EIN = "update schule.regel set wert = '1'::jsonb where schluessel = 'anwenden_pflicht';"   # Einschalt-Befehl (Bericht, Abschnitt Nachträge)
    karte_da = lambda lz: f"exists (select 1 from schule.karte_stand x where x.lernender_id = k and x.einheit_id = v_e and x.lernziel = '{lz}')"
    print(f"""-- FT-S Einspiel-Paket (erzeugt von tools/tests/form_takt_einspielen.py{' --probe' if probe else ''}). Ein Aufruf, eine Transaktion. Fehler = alles zurück.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '180s', true);
create temp table ft_mig on commit drop as select m.sql, substr(m.sql, strpos(m.sql, E'do $$\\ndeclare\\n  f record;'), {len(patch)}) as patch, m.alt
from (select $ftmig${mig}$ftmig$::text as sql, $ftalt${alt}$ftalt$::text as alt) m;
do $chk$ begin if (select strpos(patch, 'plan constant jsonb') = 0 or right(patch, 7) <> 'end $$;' or length(patch) <> {len(patch)} from ft_mig) then raise exception 'FT-S: Patch-Block nicht gefunden'; end if; end $chk$;
-- Hilfen nur für diese Sitzung (pg_temp)
create function pg_temp.ft_k(p_k bigint, p_e bigint, p_lz text) returns text language sql stable as $f$
  select coalesce((select md5(x::text) from schule.karte_stand x where x.lernender_id = p_k and x.einheit_id = p_e and x.lernziel = p_lz), 'keine') $f$;
create function pg_temp.ft_ant(p_k bigint, p_id bigint, p_ok boolean, p_anlauf int, p_cid text) returns jsonb language plpgsql as $f$
declare a schule.aufgabe;
begin
  select * into a from schule.aufgabe where id = p_id;
  return schule.uebung_pruefen_wd(p_k, jsonb_build_object('aufgabe_id', p_id, 'client_id', p_cid, 'antwort',
           case when p_ok then jsonb_build_object('wert', replace(a.loesung->>'wert', '.', ',')) else '{{"wert":"987654"}}'::jsonb end)
         || case when p_anlauf is null then '{{}}'::jsonb else jsonb_build_object('anlauf', p_anlauf) end);
end $f$;
create function pg_temp.ft_antx(p_k bigint, p_id bigint, p_ok boolean, p_extra jsonb) returns jsonb language plpgsql as $f$
declare a schule.aufgabe;
begin
  select * into a from schule.aufgabe where id = p_id;
  return schule.uebung_pruefen_wd(p_k, jsonb_build_object('aufgabe_id', p_id, 'antwort',
           case when p_ok then jsonb_build_object('wert', replace(a.loesung->>'wert', '.', ',')) else '{{"wert":"987654"}}'::jsonb end) || p_extra);
end $f$;
create function pg_temp.ft_kopie(p_basis bigint, p_lz text, p_typ text, p_stufe int, p_form text, p_zaehlt text, p_nr int) returns bigint language plpgsql as $f$
declare v bigint;
begin
  execute 'insert into schule.aufgabe (einheit_id, thema_id, teilfaehigkeit, art, stufe, variante_gruppe, antworttyp, frage, antworten, loesung, tipp, loesungsweg,
      punkte_max, reihenfolge, pool, freigegeben, typ, form, zaehlt)
    select einheit_id, thema_id, teilfaehigkeit, art, coalesce($2, stufe), coalesce($3, variante_gruppe), antworttyp, frage || jsonb_build_object(''ft_probe'', $4), antworten,
      loesung, tipp, loesungsweg, punkte_max, 90000 + $4, pool, true, coalesce($5, typ), $6, $7 from schule.aufgabe where id = $1 returning id'
    into v using p_basis, p_stufe, p_lz, p_nr, p_typ, p_form, p_zaehlt;
  return v;
end $f$;
create temp table ft_aus (phase text, o jsonb) on commit drop;
create temp table ft_bericht on commit drop as select null::jsonb as b where false;
create temp table ft_kvor on commit drop as select {kpruef_n};
create temp table ft_vor on commit drop as
  select f, pg_get_functiondef(to_regprocedure(f)) as def, (select proacl::text from pg_proc where oid = to_regprocedure(f)) as acl from unnest({arr(alle)}) f;
do $$ begin execute replace((select alt from ft_mig), 'PHASE', 'vor'); end $$;
do $$ begin execute (select sql from ft_mig); end $$;
create temp table ft_nach1 on commit drop as
  select f, pg_get_functiondef(to_regprocedure(f)) as def, (select proacl::text from pg_proc where oid = to_regprocedure(f)) as acl from unnest({arr(alle)}) f;
do $$ begin execute (select sql from ft_mig); end $$;
do $$ begin execute replace((select alt from ft_mig), 'PHASE', 'nach'); end $$;

-- Prüfblock
do $pruef$
declare
  fehler text[] := '{{}}'; f record; n int; v_txt text; v_c text; i int; v_id bigint; v_id2 bigint; v_ids bigint[] := '{{}}'; v_r jsonb; v_m text; ks schule.karte_stand;
  k constant bigint := {k};
  v_basis constant bigint := {basis};
  a schule.aufgabe; v_e bigint; v_lz text; v_status text; v_patch text := (select patch from ft_mig);
  o jsonb := '{{}}'; p jsonb := '{{}}'; v_vor jsonb; v_nach jsonb; q jsonb := '{{}}'; v_z text; v_n2 int;
begin
  select * into a from schule.aufgabe where id = v_basis; v_e := a.einheit_id; v_lz := a.variante_gruppe;
  select status into v_status from schule.einheit where id = v_e;

  -- 1. zweiter Lauf, Rechte, Spalten, Prüfbedingungen, Regel
  for f in select v.f, v.def as vor, v.acl as acl_vor, n1.def as nach1, n1.acl as acl1, pg_get_functiondef(to_regprocedure(v.f)) as jetzt,
                  (select proacl::text from pg_proc where oid = to_regprocedure(v.f)) as acl_jetzt, v.f = any({arr(NEU)}) as neu from ft_vor v join ft_nach1 n1 using (f) loop
    if f.nach1 is null then {F("f.f || ': fehlt nach der Migration'")}
    elsif not f.neu and f.vor = f.nach1 then {F("f.f || ': erster Lauf hat nichts geändert'")} end if;
    if f.nach1 is distinct from f.jetzt then {F("f.f || ': zweiter Lauf hat die Definition geändert'")} end if;
    if (not f.neu and f.acl_vor is distinct from f.acl_jetzt) or f.acl1 is distinct from f.acl_jetzt then {F("f.f || ': Rechte geändert'")} end if;
    if f.neu and (has_function_privilege('anon', f.f, 'execute') or has_function_privilege('authenticated', f.f, 'execute')) then {F("f.f || ': für App-Rollen aufrufbar'")} end if;
  end loop;
  if (select count(*) from pg_attribute where attrelid = 'schule.aufgabe'::regclass and attname in ('form', 'zaehlt') and not attisdropped and not attnotnull and not atthasdef) <> 2
    then {F("'Spalten form/zaehlt fehlen oder sind nicht nullable ohne Vorgabe'")} end if;
  if (select count(*) from pg_constraint where conrelid = 'schule.aufgabe'::regclass and conname in ('aufgabe_form_check', 'aufgabe_zaehlt_check') and convalidated) <> 2
    then {F("'Prüfbedingungen fehlen'")} end if;
  if exists (select 1 from schule.aufgabe x where x.form is not null or x.zaehlt is not null) then {F("'Bestand hat form/zaehlt'")} end if;
  if not exists (select 1 from schule.regel where schluessel = 'form_jede') then {F("'Regel form_jede fehlt'")} end if;
  if schule.wd_regel('anwenden_pflicht', -1) <> 0 then {F("'Schalter anwenden_pflicht nach dem Einspielen nicht 0: ' || coalesce(schule.wd_regel('anwenden_pflicht', -1)::text, '-')")} end if;
  if (select row(t.*)::text from ft_kvor t) is distinct from (select row({kpruef})::text) then {F("'Karten oder Aufgabenzahl nach der Migration anders als vorher'")} end if;

  -- 2. Mischstand und Gegenprobe
  for i in 1 .. 2 loop
    begin
      v_txt := case i when 1 then pg_get_functiondef('schule.expedition_buchen(bigint, bigint, boolean, smallint, smallint, timestamp with time zone)'::regprocedure) else pg_get_functiondef('schule.karte_ziel(bigint, text)'::regprocedure) end;
      v_c := case i when 1 then replace(v_txt, 'p_zeit) where schule.aufgabe_zaehlt(a); -- H8', 'p_zeit); -- H8')
                    else replace(v_txt, 'where schule.aufgabe_zaehlt(a) and a.einheit_id = p_einheit and', 'where a.einheit_id in (p_einheit) and') end;
      if v_c = v_txt then raise exception using errcode = 'FT998', message = 'Probe-Stelle nicht gefunden'; end if;
      execute v_c;
      execute v_patch;
      raise exception using errcode = 'FT999', message = 'kein Abbruch';
    exception
      when sqlstate 'FT999' then {F("'Mischstand ' || i || ' wurde nicht abgewiesen'")}
      when others then
        if sqlerrm like (case i when 1 then 'FT-S:%halb umgestellt%' else 'FT-S:%weder im alten noch im fertigen%' end) then p := p || jsonb_build_object('mischstand_' || i, 'abgewiesen');
        else {F("'Mischstand ' || i || ' unerwartet: ' || sqlerrm")} end if;
    end;
  end loop;
  begin
    for f in select v.def from ft_vor v where v.def is not null and not (v.f = any({arr(NEU)})) loop execute f.def; end loop;
    execute v_patch;
    select count(*) into n from ft_nach1 n1 where pg_get_functiondef(to_regprocedure(n1.f)) is distinct from n1.def;
    raise exception using errcode = 'FT999', message = 'gegenprobe:' || n;
  exception
    when sqlstate 'FT999' then if sqlerrm = 'gegenprobe:0' then p := p || '{{"gegenprobe":"ok"}}'; else {F("'Gegenprobe: Einbau aus dem alten Stand ergibt nicht die neuen Definitionen (' || sqlerrm || ')'")} end if;
    when others then {F("'Gegenprobe unerwartet: ' || sqlerrm")}
  end;
  if exists (select 1 from ft_nach1 n1 where pg_get_functiondef(to_regprocedure(n1.f)) is distinct from n1.def) then {F("'nach den Proben sind die Definitionen nicht wieder die neuen'")} end if;

  -- 3. Bestand: dieselbe Übung antwortet wie vorher, die Karte bleibt gleich
  select t.o into v_vor from ft_aus t where t.phase = 'vor'; select t.o into v_nach from ft_aus t where t.phase = 'nach';
  if (select count(*) from jsonb_object_keys(coalesce(v_vor, '{{}}')) ) <> 4 or (select count(*) from jsonb_object_keys(coalesce(v_nach, '{{}}'))) <> 4 then {F("'Bestand: Vergleich unvollständig'")}
  else
    for v_txt in select key from jsonb_object_keys(v_vor) key loop
      if v_vor->v_txt->'m' is distinct from v_nach->v_txt->'m' then {F("'Bestand: Karte anders nach ' || v_txt")} end if;
      if (v_vor->v_txt->'r') is distinct from ((v_nach->v_txt->'r'){NEUE_FELDER}) then {F("'Bestand: Antwort anders bei ' || v_txt")} end if;
      if v_nach->v_txt->'r' ? 'karte' and not (v_nach->v_txt->'r'->'karte' ?& array['anwenden_noetig', 'anwenden_ok', 'bearbeitungen']) then {F("'Bestand: neue Felder fehlen in karte bei ' || v_txt")} end if;
      if v_txt in ('falsch-2', 'richtig') and jsonb_typeof(v_nach->v_txt->'r'->'bearbeitungen') is distinct from 'number' then {F("'Bestand: bearbeitungen fehlt außerhalb von karte bei ' || v_txt")} end if;
    end loop;
    if not (v_nach->'falsch-1'->'r' @> '{{"format_ok":true,"richtig":false,"nochmal":true}}') or not (v_nach->'falsch-2'->'r' @> '{{"richtig":false}}') or not (v_nach->'falsch-2'->'r' ? 'loesung')
       or not (v_nach->'richtig'->'r' @> '{{"format_ok":true,"richtig":true}}') then {F("'Bestand: fachlich unerwartete Antwort'")} end if;
  end if;

  -- 4. zaehlt = nein / form + ja / Bearbeitungen / Ausgaben (alles nur in dieser Untertransaktion)
  begin
    perform schule.offene_entscheiden(k);
    v_m := pg_temp.ft_k(k, v_e, v_lz);
    v_id := pg_temp.ft_kopie(v_basis, null, null, null, 'lueckenweg', 'nein', 1);
    o := o || jsonb_build_object('anzeige', (select jsonb_build_object('form', z->'form', 'zaehlt', z->'zaehlt') from (select schule.aufgabe_anzeige(x, true) z from schule.aufgabe x where x.id = v_id) q));
    o := o || jsonb_build_object('nein_richtig', pg_temp.ft_ant(k, v_id, true, 1, 'ft-n-1'));
    if pg_temp.ft_k(k, v_e, v_lz) is distinct from v_m then {F("'zaehlt = nein, richtig: bestehende Karte verändert'")} end if;
    v_id2 := pg_temp.ft_kopie(v_basis, null, null, null, 'fehler_detektiv', 'nein', 2);
    o := o || jsonb_build_object('nein_falsch_1', pg_temp.ft_ant(k, v_id2, false, 1, 'ft-n-2'), 'nein_falsch_2', pg_temp.ft_ant(k, v_id2, false, 2, 'ft-n-3'));
    if pg_temp.ft_k(k, v_e, v_lz) is distinct from v_m then {F("'zaehlt = nein, endgültig falsch: bestehende Karte verändert'")} end if;
    if (select count(*) from schule.versuch v where v.lernender_id = k and v.aufgabe_id in (v_id, v_id2)) <> 3 then {F("'zaehlt = nein: Versuche nicht gespeichert'")} end if;
    -- neue Lernkarte: nein richtig, ja richtig, nein zweimal falsch
    v_ids := array[pg_temp.ft_kopie(v_basis, 'ft-probe-d', null, null, 'zwei_wege', 'nein', 3), pg_temp.ft_kopie(v_basis, 'ft-probe-d', 'direkt', 1, 'umkehren', 'ja', 4),
                   pg_temp.ft_kopie(v_basis, 'ft-probe-d', null, null, 'bruecke', 'nein', 5)];
    v_r := pg_temp.ft_ant(k, v_ids[1], true, 1, 'ft-d-1');
    if not (v_r @> '{{"format_ok":true,"richtig":true}}') or {karte_da('ft-probe-d')} then {F("'zaehlt = nein auf neuer Karte: ' || left(v_r::text, 200)")} end if;
    p := p || jsonb_build_object('ohne_karte', jsonb_build_object('karte', v_r ? 'karte', 'bearbeitungen', v_r->'bearbeitungen'));
    if v_r ? 'karte' or (v_r->>'bearbeitungen')::int is distinct from 1 then {F("'Schnittstelle: erste nicht zählende Aufgabe ohne Kartenzeile liefert bearbeitungen nicht (1 erwartet): ' || left(v_r::text, 200)")} end if;
    o := o || jsonb_build_object('ja_richtig', pg_temp.ft_ant(k, v_ids[2], true, 1, 'ft-d-2'));
    ks := {karte('ft-probe-d')}; v_m := pg_temp.ft_k(k, v_e, 'ft-probe-d');
    if ks.lernender_id is null or ks.eigene_loesungen <> 1 or ks.folge <> 1 or not ks.gezaehlt ? v_ids[2]::text or ks.gezaehlt ? v_ids[1]::text then {F("'form + zaehlt = ja zählt nicht wie erwartet'")} end if;
    perform pg_temp.ft_ant(k, v_ids[3], false, 1, 'ft-d-3'); perform pg_temp.ft_ant(k, v_ids[3], false, 2, 'ft-d-4');
    if pg_temp.ft_k(k, v_e, 'ft-probe-d') is distinct from v_m then {F("'zaehlt = nein, falsch: Folge oder Karte verändert'")} end if;
    p := p || jsonb_build_object('bearbeitungen_d', schule.karte_bearbeitungen(k, v_e, 'ft-probe-d'));
    if schule.karte_bearbeitungen(k, v_e, 'ft-probe-d') <> 3 then {F("'Bearbeitungen: ' || schule.karte_bearbeitungen(k, v_e, 'ft-probe-d') || ' statt 3'")} end if;
    v_r := schule.einheit_lesen_intern(k, v_e);
    p := p || jsonb_build_object('form_jede', v_r->'form_jede', 'uebung_form', (select jsonb_build_object('form', u->'form', 'zaehlt', u->'zaehlt') from jsonb_array_elements(v_r->'uebungen') u where (u->>'id')::bigint = v_ids[2]),
                                 'etappen_felder', (select count(*) from jsonb_each(v_r->'etappen_stand') s where s.value ?& array['anwenden_noetig', 'anwenden_ok', 'bearbeitungen']),
                                 'etappen', (select count(*) from jsonb_each(v_r->'etappen_stand')));
    if (v_r->>'form_jede')::int is distinct from schule.wd_regel('form_jede', -1) or p->'uebung_form' is distinct from '{{"form":"umkehren","zaehlt":"ja"}}'::jsonb
       or (p->>'etappen_felder')::int <> (p->>'etappen')::int or (p->>'etappen')::int = 0 then {F("'einheit_lesen_intern: form_jede oder neue Felder fehlen: ' || left(p::text, 300)")} end if;
{zurueck('zaehlt-Proben')}
  if o->'anzeige' is distinct from '{{"form":"lueckenweg","zaehlt":"nein"}}'::jsonb then {F("'Anzeige ohne form/zaehlt: ' || coalesce((o->'anzeige')::text, 'leer')")} end if;
  if not (o->'nein_richtig' @> '{{"format_ok":true,"richtig":true}}') or not (o->'nein_falsch_1' @> '{{"nochmal":true}}') or not (o->'nein_falsch_2' ? 'loesung')
     or not (o->'ja_richtig' @> '{{"richtig":true,"bearbeitungen":2,"karte":{{"eigene_loesungen":1,"bearbeitungen":2}}}}') then {F("'zaehlt-Proben: unerwartete Antworten: ' || left(o::text, 400)")} end if;

  -- 5. Prüfbedingungen
  for i in 1 .. 2 loop
    v_c := null;
    begin
      perform pg_temp.ft_kopie(v_basis, 'ft-probe-x', null, null, case i when 1 then 'quatsch' end, case i when 2 then 'folge' end, 40 + i);
      raise exception using errcode = 'FT999', message = 'angenommen';
    exception
      when check_violation then get stacked diagnostics v_c = constraint_name;
      when sqlstate 'FT999' then v_c := 'angenommen';
      when others then v_c := 'unerwartet: ' || sqlerrm;
    end;
    if v_c is distinct from (case i when 1 then 'aufgabe_form_check' else 'aufgabe_zaehlt_check' end) then {F("'Prüfbedingung ' || i || ': ' || coalesce(v_c, '-')")}
    else p := p || jsonb_build_object('pruefbedingung_' || i, v_c); end if;
  end loop;
  begin
    n := schule.aufgaben_einfuegen(v_e, jsonb_build_array(jsonb_build_object('t', a.teilfaehigkeit, 'p', 'uebung', 's', 2, 'l', 'ft-probe-e', 'y', a.antworttyp, 'f', a.frage || '{{"ft_probe":50}}',
           'o', a.loesung, 'h', 'Probe', 'w', 'Probe', 'r', 90050, 'g', 'umkehr', 'form', 'umkehren', 'zaehlt', 'nein') || jsonb_strip_nulls(jsonb_build_object('a', a.antworten))));
    p := p || jsonb_build_object('einfuegen', n, 'einfuegen_ok', exists (select 1 from schule.aufgabe x where x.einheit_id = v_e and x.variante_gruppe = 'ft-probe-e' and x.form = 'umkehren' and x.zaehlt = 'nein'));
{zurueck('aufgaben_einfuegen')}
  if not coalesce((p->>'einfuegen_ok')::boolean, false) or (p->>'einfuegen')::int <> 1 then {F("'aufgaben_einfuegen übernimmt form/zaehlt nicht'")} end if;

  -- 6. Sachaufgaben-Pflicht, Schalter AN (Einschalt-Befehl): A mit Sachaufgabe (zählt), B mit Sachaufgabe zaehlt = nein
  begin
    perform schule.offene_entscheiden(k);
    {EIN}
    for i in 1 .. 6 loop
      v_ids[i] := pg_temp.ft_kopie(v_basis, 'ft-probe-a', case when i <= 3 then 'direkt' else 'mehrschritt' end, case when i <= 3 then 1 else 2 end, null, null, 10 + i);
      v_ids[6 + i] := pg_temp.ft_kopie(v_basis, 'ft-probe-b', case when i <= 3 then 'direkt' else 'mehrschritt' end, case when i <= 3 then 1 else 2 end, null, null, 20 + i);
    end loop;
    v_id := pg_temp.ft_kopie(v_basis, 'ft-probe-a', 'einkleidung', 2, 'anwenden', 'ja', 17);
    perform pg_temp.ft_kopie(v_basis, 'ft-probe-b', 'einkleidung', 2, 'anwenden', 'nein', 27);
    for i in 1 .. 6 loop v_r := pg_temp.ft_ant(k, v_ids[i], true, 1, 'ft-a-' || i); end loop;
    p := p || jsonb_build_object('a_ohne', (v_r->'karte') - 'gezaehlt');
    v_r := pg_temp.ft_ant(k, v_id, true, 1, 'ft-a-7');
    p := p || jsonb_build_object('a_mit', (v_r->'karte') - 'gezaehlt');
    for i in 7 .. 12 loop v_r := pg_temp.ft_ant(k, v_ids[i], true, 1, 'ft-b-' || i); end loop;
    p := p || jsonb_build_object('b', (v_r->'karte') - 'gezaehlt');
{zurueck('Sachaufgaben-Pflicht')}
  if not (p->'a_ohne' @> '{{"sitzt":false,"eigene_loesungen":6,"anwenden_noetig":true,"anwenden_ok":false}}') then {F("'Pflicht: Karte ohne Sachaufgabe: ' || coalesce((p->'a_ohne')::text, 'leer')")} end if;
  if not (p->'a_mit' @> '{{"sitzt":true,"anwenden_ok":true}}') then {F("'Pflicht: Karte mit Sachaufgabe: ' || coalesce((p->'a_mit')::text, 'leer')")} end if;
  if not (p->'b' @> '{{"sitzt":true,"anwenden_noetig":false,"ziel":6}}') then {F("'Pflicht entfällt nicht (Sachaufgabe zaehlt = nein): ' || coalesce((p->'b')::text, 'leer')")} end if;

  -- 7. Wiederholung und Mischkarte ziehen keine Aufgabe mit zaehlt = nein
  begin
    v_id := pg_temp.ft_kopie(v_basis, 'ft-probe-c', null, 2, 'bruecke', 'nein', 30);
    p := p || jsonb_build_object('wdh_nur_nein', jsonb_build_array(schule.wdh_aufgabe_waehlen(k, v_e, 'ft-probe-c', false), schule.wdh_aufgabe_waehlen(k, v_e, 'ft-probe-c', true),
                                 schule.wdh_aufgabe_da(k, v_e, 'ft-probe-c'), schule.wdh_aufgabe_da(v_e, 'ft-probe-c')));
    v_id2 := pg_temp.ft_kopie(v_basis, 'ft-probe-c', null, 2, null, null, 31);
    p := p || jsonb_build_object('wdh_mit_ja', jsonb_build_array(schule.wdh_aufgabe_waehlen(k, v_e, 'ft-probe-c', false) = v_id2, schule.wdh_aufgabe_waehlen(k, v_e, 'ft-probe-c', true) = v_id2,
                                 schule.wdh_aufgabe_da(k, v_e, 'ft-probe-c'), schule.wdh_aufgabe_da(v_e, 'ft-probe-c')));
{zurueck('Wiederholung')}
  if p->'wdh_nur_nein' is distinct from '[null, null, false, false]'::jsonb
     or p->'wdh_mit_ja' is distinct from (case when v_status in ('geprueft', 'freigegeben') then '[true, true, true, true]' else '[true, true, false, false]' end)::jsonb
    then {F("'Wiederholung/Mischkarte: ' || coalesce((p->'wdh_nur_nein')::text, '-') || ' / ' || coalesce((p->'wdh_mit_ja')::text, '-')")} end if;

  -- 8. Fällige, sitzende Karte: Aufgabe mit zaehlt = nein ändert die ganze Kartenzeile nicht (richtig, endgültig falsch, Misch-Wunsch);
  --    derselbe client_id noch einmal: kein zweiter Versuch, kein zusätzlicher Taktplatz
  begin
    perform schule.offene_entscheiden(k);
    for i in 1 .. 6 loop v_ids[i] := pg_temp.ft_kopie(v_basis, 'ft-probe-f', case when i <= 3 then 'direkt' else 'mehrschritt' end, case when i <= 3 then 1 else 2 end, null, null, 100 + i); end loop;
    v_id := pg_temp.ft_kopie(v_basis, 'ft-probe-f', 'direkt', 2, 'lueckenweg', 'nein', 107);
    for i in 1 .. 6 loop v_r := pg_temp.ft_ant(k, v_ids[i], true, 1, 'ft-f-' || i); end loop;
    update schule.karte_stand x set faellig_am = now() - interval '2 days', wdh_ab = now() - interval '3 days'
     where x.lernender_id = k and x.einheit_id = v_e and x.lernziel = 'ft-probe-f';
    ks := {karte('ft-probe-f')}; v_z := {zeile('ft-probe-f')}; n := schule.karte_bearbeitungen(k, v_e, 'ft-probe-f');
    q := q || jsonb_build_object('f_aufbau', jsonb_build_object('sitzt', ks.sitzt, 'faellig', schule.karte_faellig(ks), 'wdh_stufe', ks.wdh_stufe, 'folge', ks.folge, 'bearbeitungen', n));
    if not coalesce(ks.sitzt, false) or not coalesce(schule.karte_faellig(ks), false) then {F("'8: Aufbau fällige sitzende Karte misslungen: ' || (q->'f_aufbau')::text")} end if;
    v_r := pg_temp.ft_ant(k, v_id, true, 1, 'ft-f-n1'); q := q || jsonb_build_object('f_richtig', {ohne('v_r')});
    if {zeile('ft-probe-f')} is distinct from v_z then {F("'8: zaehlt = nein richtig hat die fällige Karte verändert'")} end if;
    q := q || jsonb_build_object('f_falsch_1', {ohne("pg_temp.ft_ant(k, v_id, false, 1, 'ft-f-n2')")});
    v_r := pg_temp.ft_ant(k, v_id, false, 2, 'ft-f-n3'); q := q || jsonb_build_object('f_falsch_2', {ohne('v_r')});
    if {zeile('ft-probe-f')} is distinct from v_z then {F("'8: zaehlt = nein endgültig falsch hat die fällige Karte verändert'")} end if;
    v_r := pg_temp.ft_antx(k, v_id, true, jsonb_build_object('client_id', 'ft-f-n4', 'anlauf', 1, 'misch', true)); q := q || jsonb_build_object('f_misch', {ohne('v_r')});
    if {zeile('ft-probe-f')} is distinct from v_z then {F("'8: zaehlt = nein mit Misch-Wunsch hat die fällige Karte verändert'")} end if;
    v_n2 := schule.karte_bearbeitungen(k, v_e, 'ft-probe-f');
    select count(*) into i from schule.versuch v where v.lernender_id = k and v.aufgabe_id = v_id;
    v_r := pg_temp.ft_ant(k, v_id, true, 1, 'ft-f-n1'); q := q || jsonb_build_object('f_nochmal', {ohne('v_r')});
    if {zeile('ft-probe-f')} is distinct from v_z then {F("'8: derselbe client_id hat die fällige Karte verändert'")} end if;
    if (select count(*) from schule.versuch v where v.lernender_id = k and v.aufgabe_id = v_id) <> i or i <> 4 then {F("format('8: Versuche %s statt 4 bzw. derselbe client_id hat einen zweiten Versuch angelegt', i)")} end if;
    if schule.karte_bearbeitungen(k, v_e, 'ft-probe-f') <> v_n2 or v_n2 <> n + 3 then {F("format('8: Taktplätze vorher %s, nach drei Antworten %s (erwartet +3), nach Wiederholung des client_id %s', n, v_n2, schule.karte_bearbeitungen(k, v_e, 'ft-probe-f'))")} end if;
    if not (q->'f_nochmal' @> '{{"wiederholt":true,"richtig":true}}') or not (q->'f_richtig' @> '{{"richtig":true}}') or not (q->'f_falsch_1' @> '{{"nochmal":true}}')
       or (q->'f_richtig'->>'bearbeitungen')::int is distinct from n + 1 or (q->'f_falsch_2'->>'bearbeitungen')::int is distinct from n + 2
       or (q->'f_misch'->>'bearbeitungen')::int is distinct from n + 3 or coalesce((q->'f_misch'->'misch'->>'gueltig')::boolean, false)
       or q->'f_richtig' ? 'wiederholung' or q->'f_falsch_2' ? 'wiederholung' or q->'f_misch' ? 'wiederholung'
      then {F("'8: unerwartete Antworten: ' || left(q::text, 600)")} end if;
{zurueck('fällige Karte')}

  -- 9. Filter als Verhalten: Typen-Pflicht, Schwer-Pflicht, Folge nachrechnen
  begin
    perform schule.offene_entscheiden(k);
    for i in 1 .. 6 loop v_ids[i] := pg_temp.ft_kopie(v_basis, 'ft-probe-g', 'direkt', 1, null, null, 110 + i); end loop;
    v_id := pg_temp.ft_kopie(v_basis, 'ft-probe-g', 'umkehr', 1, 'umkehren', 'nein', 117);   -- einziger Träger des zweiten Typs
    v_id2 := pg_temp.ft_kopie(v_basis, 'ft-probe-g', 'direkt', 3, 'bruecke', 'nein', 118);   -- einzige Stufe-3-Aufgabe
    q := q || jsonb_build_object('g_nein', jsonb_build_array(schule.karte_ziel(v_e, 'ft-probe-g'), schule.karte_typen_noetig(v_e, 'ft-probe-g'), schule.karte_schwer_noetig(v_e, 'ft-probe-g')));
    update schule.aufgabe set zaehlt = 'ja' where id = v_id;
    q := q || jsonb_build_object('g_gegen_typ', schule.karte_typen_noetig(v_e, 'ft-probe-g'));
    update schule.aufgabe set zaehlt = 'nein' where id = v_id; update schule.aufgabe set zaehlt = 'ja' where id = v_id2;
    q := q || jsonb_build_object('g_gegen_schwer', schule.karte_schwer_noetig(v_e, 'ft-probe-g'));
    update schule.aufgabe set zaehlt = 'nein' where id = v_id2;
    if q->'g_nein' is distinct from '[6, 1, false]'::jsonb or (q->>'g_gegen_typ')::int <> 2 or not (q->>'g_gegen_schwer')::boolean then {F("'9: Ziel/Typen/Schwer mit nicht zählenden Aufgaben: ' || left(q::text, 300)")} end if;
    for i in 1 .. 6 loop v_r := pg_temp.ft_ant(k, v_ids[i], true, 1, 'ft-g-' || i); end loop;
    q := q || jsonb_build_object('g_karte', (v_r->'karte') - 'gezaehlt');
    if not (v_r->'karte' @> '{{"sitzt":true,"typen_anzahl":1,"typen_noetig":1,"schwer_noetig":false,"schwer_ok":false,"ziel":6}}') then {F("'9: Karte landet nicht ohne den nicht zählenden Typ/die nicht zählende Stufe 3: ' || coalesce((q->'g_karte')::text, 'leer')")} end if;
    for i in 1 .. 4 loop v_ids[6 + i] := pg_temp.ft_kopie(v_basis, 'ft-probe-h', 'direkt', 1, null, null, 120 + i); end loop;
    v_id := pg_temp.ft_kopie(v_basis, 'ft-probe-h', 'direkt', 1, 'fehler_detektiv', 'nein', 125);
    perform pg_temp.ft_ant(k, v_ids[7], true, 1, 'ft-h-1'); perform pg_temp.ft_ant(k, v_ids[8], true, 1, 'ft-h-2');
    perform pg_temp.ft_ant(k, v_id, false, 1, 'ft-h-3'); perform pg_temp.ft_ant(k, v_id, false, 2, 'ft-h-4');
    perform pg_temp.ft_ant(k, v_ids[9], true, 1, 'ft-h-5');
    ks := {karte('ft-probe-h')};
    q := q || jsonb_build_object('h_folge', jsonb_build_object('buchung', ks.folge, 'nachgerechnet', schule.folge_nachrechnen(k, v_e, 'ft-probe-h', null::timestamptz), 'sitzt', ks.sitzt));
    if q->'h_folge' is distinct from '{{"buchung":3,"nachgerechnet":3,"sitzt":false}}'::jsonb then {F("'9: Folge nach nicht zählendem Fehler: ' || (q->'h_folge')::text")} end if;
{zurueck('Filter')}

  -- 10. Übergänge (Schalter erst aus, dann mit dem Einschalt-Befehl an)
  begin   -- 10a: Sachaufgabe (Bestand, zaehlt leer) schon in gezaehlt, bevor die Pflicht greift -> sofort erfüllt
    perform schule.offene_entscheiden(k);
    for i in 1 .. 6 loop v_ids[i] := pg_temp.ft_kopie(v_basis, 'ft-probe-i', case when i <= 3 then 'direkt' else 'mehrschritt' end, case when i <= 3 then 1 else 2 end, null, null, 130 + i); end loop;
    v_id := pg_temp.ft_kopie(v_basis, 'ft-probe-i', 'einkleidung', 2, null, null, 137);
    perform pg_temp.ft_ant(k, v_id, true, 1, 'ft-i-0');
    for i in 1 .. 4 loop perform pg_temp.ft_ant(k, v_ids[i], true, 1, 'ft-i-' || i); end loop;
    ks := {karte('ft-probe-i')};
    if ks.sitzt or ks.eigene_loesungen <> 5 or not ks.gezaehlt ? v_id::text then {F("format('10a: Aufbau (sitzt %s, eigene %s)', ks.sitzt, ks.eigene_loesungen)")} end if;
    {EIN}
    q := q || jsonb_build_object('i_vor', jsonb_build_array(schule.karte_anwenden_pflicht(ks, v_e, 'ft-probe-i'), schule.karte_anwenden_ok(ks)));
    v_r := pg_temp.ft_ant(k, v_ids[5], true, 1, 'ft-i-5');
    q := q || jsonb_build_object('i_nach', (v_r->'karte') - 'gezaehlt');
    if q->'i_vor' is distinct from '[true, true]'::jsonb or not (v_r->'karte' @> '{{"sitzt":true,"anwenden_ok":true,"eigene_loesungen":6}}') then {F("'10a: Sachaufgabe aus dem Bestand erfüllt die Pflicht nicht sofort: ' || left(q::text, 400)")} end if;
{zurueck('Übergang Bestand')}
  begin   -- 10b: früher (ohne Sachaufgabe) gelandet, wieder geöffnet -> landet wieder ohne neue Sachaufgabe
    perform schule.offene_entscheiden(k);
    for i in 1 .. 6 loop v_ids[i] := pg_temp.ft_kopie(v_basis, 'ft-probe-j', case when i <= 3 then 'direkt' else 'mehrschritt' end, case when i <= 3 then 1 else 2 end, null, null, 140 + i); end loop;
    v_id := pg_temp.ft_kopie(v_basis, 'ft-probe-j', 'einkleidung', 2, 'anwenden', 'ja', 147);
    for i in 1 .. 6 loop v_r := pg_temp.ft_ant(k, v_ids[i], true, 1, 'ft-j-' || i); end loop;
    if not (v_r->'karte' @> '{{"sitzt":true}}') then {F("'10b: Karte landet bei Schalter aus nicht: ' || left(coalesce((v_r->'karte')::text, 'leer'), 300)")} end if;
    {EIN}
    perform pg_temp.ft_ant(k, v_ids[1], false, null, 'ft-j-7'); perform pg_temp.ft_ant(k, v_ids[1], false, null, 'ft-j-8');
    ks := {karte('ft-probe-j')};
    q := q || jsonb_build_object('j_offen', jsonb_build_object('sitzt', ks.sitzt, 'sitzt_am', ks.sitzt_am is not null, 'geoeffnet', ks.geoeffnet_am is not null,
                                 'pflicht', schule.karte_anwenden_pflicht(ks, v_e, 'ft-probe-j'), 'ok', schule.karte_anwenden_ok(ks)));
    if q->'j_offen' is distinct from '{{"sitzt":false,"sitzt_am":true,"geoeffnet":true,"pflicht":false,"ok":false}}'::jsonb then {F("'10b: Wiederöffnen: ' || (q->'j_offen')::text")} end if;
    for i in 2 .. 4 loop v_r := pg_temp.ft_ant(k, v_ids[i], true, 1, 'ft-j-' || (7 + i)); end loop;
    q := q || jsonb_build_object('j_wieder', (v_r->'karte') - 'gezaehlt');
    if not (v_r->'karte' @> '{{"sitzt":true,"anwenden_noetig":false,"anwenden_ok":false}}') then {F("'10b: wieder geöffnete Karte landet nicht ohne Sachaufgabe: ' || coalesce((q->'j_wieder')::text, 'leer')")} end if;
{zurueck('Übergang Wiederlandung')}

  -- 11. Nicht zählender Versuch schließt einen offenen ersten Fehlversuch an einer ANDEREN, zählenden Aufgabe ab
  begin
    perform schule.offene_entscheiden(k);
    v_id := pg_temp.ft_kopie(v_basis, 'ft-probe-k', 'direkt', 1, null, null, 150);
    v_id2 := pg_temp.ft_kopie(v_basis, 'ft-probe-k', 'direkt', 1, 'lueckenweg', 'nein', 151);
    v_r := pg_temp.ft_ant(k, v_id, false, 1, 'ft-k-1');
    q := q || jsonb_build_object('k_vor', jsonb_build_object('nochmal', v_r->'nochmal', 'offen', (select v.wertung_offen from schule.versuch v where v.lernender_id = k and v.client_id = 'ft-k-1'),
                                 'karte', {karte_da('ft-probe-k')}));
    v_r := pg_temp.ft_ant(k, v_id2, true, 1, 'ft-k-2');
    ks := {karte('ft-probe-k')};
    q := q || jsonb_build_object('k_nach', jsonb_build_object('offen', (select v.wertung_offen from schule.versuch v where v.lernender_id = k and v.client_id = 'ft-k-1'),
                                 'wertung', (select v.wertung_fest from schule.versuch v where v.lernender_id = k and v.client_id = 'ft-k-1'),
                                 'falsch', ks.falsch, 'fehler_folge', ks.fehler_folge, 'eigene', ks.eigene_loesungen, 'bearbeitungen', v_r->'bearbeitungen'));
    if q->'k_vor' is distinct from '{{"nochmal":true,"offen":true,"karte":false}}'::jsonb
       or q->'k_nach' is distinct from '{{"offen":false,"wertung":"falsch","falsch":1,"fehler_folge":1,"eigene":0,"bearbeitungen":2}}'::jsonb
      then {F("'11: offener Fehlversuch wird durch nicht zählende Aufgabe nicht wie bisher abgeschlossen: ' || left(q::text, 400)")} end if;
{zurueck('offener Fehlversuch')}

  -- 12. Schalter anwenden_pflicht: Stellung AUS (Vorgabe) -> Karte mit Sachaufgabe landet ohne sie; Einschalten wirkt und überlebt einen zweiten Lauf
  begin
    perform schule.offene_entscheiden(k);
    for i in 1 .. 6 loop v_ids[i] := pg_temp.ft_kopie(v_basis, 'ft-probe-l', case when i <= 3 then 'direkt' else 'mehrschritt' end, case when i <= 3 then 1 else 2 end, null, null, 160 + i); end loop;
    perform pg_temp.ft_kopie(v_basis, 'ft-probe-l', 'einkleidung', 2, 'anwenden', 'ja', 167);
    for i in 1 .. 5 loop v_r := pg_temp.ft_ant(k, v_ids[i], true, 1, 'ft-l-' || i); end loop;
    q := q || jsonb_build_object('l_aus_5', (v_r->'karte') - 'gezaehlt');
    v_r := pg_temp.ft_ant(k, v_ids[6], true, 1, 'ft-l-6');
    q := q || jsonb_build_object('l_aus_6', (v_r->'karte') - 'gezaehlt',
                                 'l_etappe', (select s.value - 'gezaehlt' from jsonb_each(schule.einheit_lesen_intern(k, v_e)->'etappen_stand') s where s.key = 'ft-probe-l'));
    if not (q->'l_aus_5' @> '{{"sitzt":false,"anwenden_noetig":false}}') or not (q->'l_aus_6' @> '{{"sitzt":true,"anwenden_noetig":false,"anwenden_ok":false}}')
      then {F("'12: Schalter aus wirkt nicht: ' || left(q::text, 400)")} end if;
    {EIN}
    q := q || jsonb_build_object('l_an', schule.wd_regel('anwenden_pflicht', -1));
    execute (select sql from ft_mig);
    q := q || jsonb_build_object('l_an_nach_lauf', schule.wd_regel('anwenden_pflicht', -1));
    if (q->>'l_an')::int <> 1 or (q->>'l_an_nach_lauf')::int <> 1 then {F("'12: Einschalten wirkt nicht oder zweiter Lauf setzt zurück: ' || left(q::text, 200)")} end if;
{zurueck('Schalter')}
  if exists (select 1 from schule.karte_stand x where x.lernender_id = k and x.lernziel like 'ft-probe-%') or schule.wd_regel('anwenden_pflicht', -1) <> 0 then {F("'Nachträge: Probe-Karten oder Schalter nicht zurückgerollt'")} end if;

  -- 13. Am Ende: Karten (alle Kinder) und Aufgabenzahl wie vorher; keine sitzende Karte mit Sachaufgaben-Pflicht
  if (select row(t.*)::text from ft_kvor t) is distinct from (select row({kpruef})::text) then {F("'Karten oder Aufgabenzahl am Ende anders als vorher'")} end if;
  begin
    {EIN}
    select count(*) into n from schule.karte_stand x where x.sitzt and schule.karte_anwenden_pflicht(x, x.einheit_id, x.lernziel);
{zurueck('sitzende Karten')}
  if n <> 0 then {F("n || ' sitzende Karten hätten eine Sachaufgaben-Pflicht'")} end if;
  if exists (select 1 from schule.aufgabe x where x.variante_gruppe like 'ft-probe-%' or x.frage ? 'ft_probe') then {F("'Probe-Aufgaben sind nicht zurückgerollt'")} end if;

  if array_length(fehler, 1) > 0 then raise exception 'FT-S ABBRUCH, alles zurückgerollt: %', array_to_string(fehler, ' | '); end if;
  insert into ft_bericht select jsonb_build_object('ergebnis', 'FT-S eingespielt, alle Prüfungen bestanden', 'funktionen_geaendert', {len(patch_fn)}, 'funktionen_neu', {len(NEU)},
    'karten', (select count(*) from schule.karte_stand), 'karten_sitzend', (select t.sitzend from ft_kvor t), 'pruefsumme_karten', (select t.spalten from ft_kvor t),
    'anwenden_pflicht', schule.wd_regel('anwenden_pflicht', -1), 'proben', p, 'nachtraege', q, 'antworten', (select jsonb_object_agg(key, value - 'loesung' - 'loesungsweg') from jsonb_each(o) where jsonb_typeof(value) = 'object'));
  {ende}
end $pruef$;
select b from ft_bericht;""")


if __name__ == '__main__':
    main()
