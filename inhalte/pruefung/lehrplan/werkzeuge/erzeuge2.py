import json,sys
sys.path.insert(0,'/tmp/lpw'); from db import VOR; import vorschlag as V
P='/tmp/lp/inhalte/themenliste.json'
L=json.load(open(P)); T={x['thema_id']:x for x in L}
# 1) Themenliste wird nicht mehr verändert (Stand liegt im Zweig)
ib4=[i for i in sorted(T,key=lambda i:T[i]['reihenfolge'].get('ib_myp',0)) if T[i]['klasse'].get('ib_myp')==4]
# 2) SQL
q=lambda s:"'"+s.replace("'","''")+"'"
gym9=[]
sql=[]
A=sql.append
A("-- Dreißigste Runde (21.11.): Lehrplan-Prüfung – Zuordnungen und Voraussetzungen der Themenliste.")
A("-- Quelle: LehrplanPLUS Bayern, abgerufen 21.11.2026; Belege und Annahmen in inhalte/pruefung/lehrplan/runde30.md.")
A("-- Wiederholt ausführbar. Kein DROP, kein DELETE. Fehlen die Themen 102/103, werden ihre Verbindungen übersprungen.")
A("-- Am Ende ein Rauchtest (nur lesen); schlägt er fehl, bricht die Migration mit Fehlermeldung ab.")
A("")
A("-- 0) Vergleichsstand für den Rauchtest (Runde 30 c): Reiseoptionen aller Lernenden und Zahl der Visum-Zeilen VOR den Änderungen, nur gelesen und in einer Sitzungs-Einstellung gemerkt.")
A("do $$ begin")
A("  perform set_config('lb30.ro_vorher', coalesce((select jsonb_object_agg(id::text, schule.reiseoptionen(id)) from schule.lernender), '{}'::jsonb)::text, false);")
A("  perform set_config('lb30.visum_vorher', (select count(*) from schule.v_ort_visum)::text, false);")
A("end $$;")
A("")
A("-- 1) Kleinste Erweiterung: Kennzeichen „eigenständig“ (Begründung; nicht leer = bewusst ohne Voraussetzung)")
A("alter table schule.thema add column if not exists eigenstaendig text;")
A("comment on column schule.thema.eigenstaendig is 'Begründung, warum das Thema bewusst keine Voraussetzung hat (Dreißigste Runde)';")
A("")
A("-- 2) entfällt (Runde 30 b): Thema 12 bekommt keine Gymnasium-Klasse; es ist für das Gymnasium aufgelöst (Etappe reinquadratisch in 8). Reihenfolge Gym 9 bleibt unverändert.")
A("")
A("-- 3) Formeln umstellen (4): Lernbereich Gymnasium berichtigt (M8 1 statt M8 4); Reihenfolge bleibt")
A("update schule.thema set lernbereich = coalesce(lernbereich,'{}'::jsonb) || '{\"gym_by\": \"M8 1 Funktion und Term\"}'::jsonb where id = 4;")
A("")
A("-- 3b) Zuordnung und Funktion (32) im IB nach MYP 3 vor Lineare Funktionen (33), weil 33 hart auf 32 aufbaut (Annahme)")
A("update schule.thema set klasse_fest = coalesce(klasse_fest,'{}'::jsonb) || '{\"ib_myp\": 3}'::jsonb,")
A("  lernbereich = coalesce(lernbereich,'{}'::jsonb) || '{\"ib_myp\": \"MYP 3 Thinking with models (Funktionen und Modelle)\"}'::jsonb,")
A("  lehrplan = coalesce(lehrplan,'{}'::jsonb) || jsonb_build_object('ib_myp', "+q(V.IB_TEXT_32)+")")
A("where id = 32;")
A("-- Reihenfolge IB MYP 3 und MYP 4 lückenlos neu")
A("update schule.thema t set lehrplan_reihenfolge = coalesce(t.lehrplan_reihenfolge,'{}'::jsonb) || jsonb_build_object('ib_myp', v.rf)")
A("from (values "+", ".join(f"({i}, {n})" for n,i in enumerate(V.IB_NEU[3],1))+", "+", ".join(f"({i}, {n})" for n,i in enumerate(ib4,1))+") v(id, rf)")
A("where t.id = v.id;")
A("")
A("-- 3c) Veraltete Verbindungen von und zu aufgelösten Themen (Entwurf ohne freigegebene Einheit) gezielt löschen.")
A("-- Einzige Ausnahme vom Lösch-Verbot (Auftrag „Nachbesserung Dreißigste Runde“, Teil A). Jede Zeile einzeln, nur genau dieses Paar.")
for t,b_,g in V.LOESCHEN:
  A(f"-- {t} {T[t]['titel']} ← {b_} {T[b_]['titel']}: {g}")
  A(f"delete from schule.voraussetzung where thema_id = {t} and braucht_id = {b_};")
A("")
A("-- 4) Voraussetzungen (nur einfügen oder Art/Begründung angleichen; vorhandene bleiben)")
rows=[f"({a}, {b}, '{art}', {q(g)})" for a,b,art,g in V.NEU]+[f"({a}, {b}, (select art from schule.voraussetzung where thema_id={a} and braucht_id={b}), {q(g)})" for (a,b),g in V.BEGR_NEU.items()]
A("insert into schule.voraussetzung (thema_id, braucht_id, art, begruendung)")
A("select v.t, v.b, v.art, v.beg from (values")
A(",\n".join("  "+r for r in [f"({a}, {b}, '{art}', {q(g)})" for a,b,art,g in V.NEU]))
A(") v(t, b, art, beg)")
A("where exists (select 1 from schule.thema where id = v.t) and exists (select 1 from schule.thema where id = v.b)")
A("on conflict (thema_id, braucht_id) do update set art = excluded.art, begruendung = excluded.begruendung;")
for (a,b),g in V.BEGR_NEU.items():
  A(f"update schule.voraussetzung set begruendung = {q(g)} where thema_id = {a} and braucht_id = {b};")
A("")
A("-- 5) Eigenständige Themen")
A("update schule.thema t set eigenstaendig = v.g from (values")
A(",\n".join(f"  ({i}, {q(g)})" for i,g in V.EIGEN.items()))
A(") v(id, g) where t.id = v.id and t.eigenstaendig is distinct from v.g;")
A("")
A("-- 6) Rauchtest (liest nur)")
A("""do $$
declare v_n int; v_txt text;
begin
  -- a) Thema 12 (aufgelöst) hat keine Gymnasium-Klasse; der Stoff steht in 8 (Etappe reinquadratisch)
  if schule.thema_jahrgang(12) ? 'gym_by' then raise exception 'Rauchtest: Thema 12 darf keine Gymnasium-Klasse haben'; end if;
  -- i) Neue Regel: keine Verbindung von oder zu einem Thema ohne freigegebene Einheit, außer ausdrücklich begründet (Begründung beginnt mit „Ausnahme:“)
  select string_agg(v.thema_id || '←' || v.braucht_id, ', ') into v_txt from schule.voraussetzung v
   where (not exists (select 1 from schule.einheit e where e.thema_id = v.thema_id and e.status = 'freigegeben')
       or not exists (select 1 from schule.einheit e where e.thema_id = v.braucht_id and e.status = 'freigegeben'))
     and coalesce(v.begruendung, '') not like 'Ausnahme:%';
  if v_txt is not null then raise exception 'Rauchtest: Verbindung von/zu Thema ohne freigegebene Einheit: %', v_txt; end if;
  -- b) jedes Thema mit Klasse und freigegebener Einheit hat Voraussetzungen oder ist ausdrücklich eigenständig
  select count(*), string_agg(t.id::text, ', ') into v_n, v_txt from schule.thema t
   where schule.thema_jahrgang(t.id) <> '{}'::jsonb and t.eigenstaendig is null
     and exists (select 1 from schule.einheit e where e.thema_id = t.id and e.status = 'freigegeben')
     and not exists (select 1 from schule.voraussetzung v where v.thema_id = t.id);
  if v_n > 0 then raise exception 'Rauchtest: Themen ohne Voraussetzung und ohne eigenständig: %', v_txt; end if;
  -- c) keine Kreise
  with recursive w(start, jetzt, pfad) as (
    select thema_id, braucht_id, array[thema_id, braucht_id] from schule.voraussetzung
    union all
    select w.start, v.braucht_id, w.pfad || v.braucht_id from w join schule.voraussetzung v on v.thema_id = w.jetzt
     where not v.braucht_id = any(w.pfad[2:]) and w.jetzt <> w.start)
  select count(*) into v_n from w where jetzt = start;
  if v_n > 0 then raise exception 'Rauchtest: Kreis in den Voraussetzungen'; end if;
  -- d) Reihenfolge je Schulart und Klasse lückenlos und eindeutig
  with z as (select t.id, s.key schulart, (s.value)::int klasse, (t.lehrplan_reihenfolge->>s.key)::int rf
               from schule.thema t, jsonb_each(schule.thema_jahrgang(t.id)) s
              where jsonb_typeof(s.value) = 'number')
  select string_agg(schulart || ' ' || klasse, ', ') into v_txt from (
    select schulart, klasse from z group by schulart, klasse
    having count(rf) <> count(*) or count(distinct rf) <> count(*) or min(rf) <> 1 or max(rf) <> count(*)) f;
  if v_txt is not null then raise exception 'Rauchtest: Reihenfolge nicht lückenlos/eindeutig: %', v_txt; end if;
  -- e) Pflichtverbindungen für die Potenz-Flüge, falls 102/103 vorhanden
  if exists (select 1 from schule.thema where id = 102) and (
       not exists (select 1 from schule.voraussetzung where thema_id = 102 and braucht_id = 30)
    or not exists (select 1 from schule.voraussetzung where thema_id = 29 and braucht_id = 102)) then
    raise exception 'Rauchtest: Verbindung 30 → 102 → 29 fehlt'; end if;
  if exists (select 1 from schule.thema where id = 103) and exists (select 1 from schule.thema where id = 102)
     and not exists (select 1 from schule.voraussetzung where thema_id = 103 and braucht_id = 102) then
    raise exception 'Rauchtest: Verbindung 102 → 103 fehlt'; end if;
  -- g) Regel des Gestalters: keine Voraussetzung liegt in einer späteren Klasse als das Thema (je Schulart)
  select string_agg(v.thema_id || '←' || v.braucht_id || ' ' || a.key, ', ') into v_txt
    from schule.voraussetzung v, jsonb_each(schule.thema_jahrgang(v.thema_id)) a, jsonb_each(schule.thema_jahrgang(v.braucht_id)) b
   where a.key = b.key and jsonb_typeof(a.value) = 'number' and jsonb_typeof(b.value) = 'number' and (b.value)::int > (a.value)::int;
  if v_txt is not null then raise exception 'Rauchtest: Voraussetzung in späterer Klasse: %', v_txt; end if;
  -- h) Regel des Gestalters: Themen 100–103 sind verknüpft (je vorhandenes Thema mindestens eine Voraussetzung)
  select string_agg(t.id::text, ', ') into v_txt from schule.thema t
   where t.id between 100 and 103 and not exists (select 1 from schule.voraussetzung v where v.thema_id = t.id);
  if v_txt is not null then raise exception 'Rauchtest: Themen 100–103 ohne Verbindung: %', v_txt; end if;
  -- j) Runde 30 c: Reiseoptionen jedes vorhandenen Lernenden vorher = nachher (Visum-Regeln dürfen sich für heutige Pläne nicht ändern)
  if current_setting('lb30.ro_vorher', true) is null then
    raise notice 'Rauchtest j übersprungen: kein Vergleichsstand (Abschnitt 0 nicht in derselben Sitzung gelaufen)';
  else
    select string_agg('Lernender ' || k || ': vorher ' || coalesce(vorher->k, 'null'::jsonb)::text || ' / nachher ' || coalesce(nachher->k, 'null'::jsonb)::text, E'\n') into v_txt
      from (select current_setting('lb30.ro_vorher')::jsonb vorher,
                   coalesce((select jsonb_object_agg(id::text, schule.reiseoptionen(id)) from schule.lernender), '{}'::jsonb) nachher) x,
           lateral (select jsonb_object_keys(vorher) k union select jsonb_object_keys(nachher)) ks
     where coalesce(vorher->k, 'null'::jsonb) is distinct from coalesce(nachher->k, 'null'::jsonb);
    if v_txt is not null then raise exception E'Rauchtest j: Reiseoptionen geändert:\n%', v_txt; end if;
    raise notice 'Rauchtest j: Reiseoptionen unverändert; v_ort_visum vorher % Zeilen, nachher %', current_setting('lb30.visum_vorher', true), (select count(*) from schule.v_ort_visum);
  end if;
  -- f) Lernbereich 4 berichtigt
  if (select lernbereich->>'gym_by' from schule.thema where id = 4) <> 'M8 1 Funktion und Term' then raise exception 'Rauchtest: Lernbereich 4'; end if;
  raise notice 'Rauchtest Dreißigste Runde bestanden';
end $$;""")
open('/tmp/lp/supabase/migrations/20261121_lehrplan_zuordnung_voraussetzungen.sql','w').write("\n".join(sql)+"\n")
# 3) Tabelle für den Bericht
tit=lambda i:T[i]['titel']
alle={}
LOE={(t,b) for t,b,_ in V.LOESCHEN}
for a,b,art in VOR:
  if (a,b) not in LOE: alle.setdefault(a,[]).append((b,art,'vorhanden'))
for a,b,art,g in V.NEU: alle.setdefault(a,[]).append((b,art,g))
out=["| Nr | Thema | Gym | RS | IB | direkte Voraussetzungen (Art, Begründung) |","|---|---|---|---|---|---|"]
for i in sorted(T):
  k=T[i]['klasse']
  if i in V.AUF_SET: v="**aufgelöst** (Entwurf ohne freigegebene Einheit) – keine Verbindungen"+("; zusätzlich eigenständig gekennzeichnet" if i in V.EIGEN else "")
  elif i in V.EIGEN: v="**eigenständig** – "+V.EIGEN[i]
  else: v="; ".join(f"{b} {tit(b)} ({art}{', '+g if g!='vorhanden' else ', vorhanden'}{'; Begründung neu: '+V.BEGR_NEU[(i,b)] if (i,b) in V.BEGR_NEU else ''})" for b,art,g in alle.get(i,[]))
  out.append(f"| {i} | {tit(i)} | {k.get('gym_by') or '–'} | {k.get('rs_by') or '–'} | {k.get('ib_myp') or '–'} | {v} |")
open('/tmp/lpw/tabelle.md','w').write("\n".join(out)+"\n")
