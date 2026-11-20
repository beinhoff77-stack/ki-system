-- Rauchtest I-4 (Misch-Ausgaben wiederverwenden). Nach 20261120_i4_misch_ausgabe_wieder.sql ausführen. Rollback, nur Testkind, keine Namen.
-- Legt eigene Karten-Stände an (zwei gelandete Etappen); hängt nicht davon ab, wie viele Etappen das Testkind sonst gelandet hat (alle anderen werden im Test auf „nicht gelandet“ gesetzt).
begin;
do $$
declare v_l bigint; v_e1 bigint; v_lz1 text; v_e2 bigint; v_lz2 text; v_f1 bigint; v_f2 bigint; j1 jsonb; j2 jsonb; v_ids1 bigint[]; v_ids2 bigint[]; v_n int; v_a bigint;
begin
  select id into v_l from schule.lernender where ist_test and aktiv order by id limit 1;
  if v_l is null then raise exception 'FEHLER kein Testkind'; end if;
  update schule.karte_stand set sitzt = false where lernender_id = v_l;
  update schule.misch_ausgabe set eingeloest_am = now() where lernender_id = v_l and eingeloest_am is null;
  -- zwei Etappen mit Mischkarten-tauglichen Bordkarten (Stufe 2–3, freigegeben) in zwei verschiedenen freigegebenen Flügen; dazu zwei weitere Flüge zum Lesen
  select a.einheit_id, a.variante_gruppe into v_e1, v_lz1 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
   where a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and e.status = 'freigegeben' group by 1, 2 having count(*) >= 2 order by 1, 2 limit 1;
  select a.einheit_id, a.variante_gruppe into v_e2, v_lz2 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
   where a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3) and e.status = 'freigegeben' and a.einheit_id <> v_e1 group by 1, 2 having count(*) >= 2 order by 1, 2 limit 1;
  select e.id into v_f1 from schule.einheit e where e.status = 'freigegeben' and e.id not in (v_e1, v_e2) order by e.id limit 1;
  select e.id into v_f2 from schule.einheit e where e.status = 'freigegeben' and e.id not in (v_e1, v_e2, v_f1) order by e.id limit 1;
  if v_e2 is null or v_f2 is null then raise exception 'FEHLER: keine passenden Flüge'; end if;
  insert into schule.karte_stand(lernender_id, einheit_id, lernziel) values (v_l, v_e1, v_lz1), (v_l, v_e2, v_lz2) on conflict do nothing;
  update schule.karte_stand set sitzt = true, sitzt_am = now() - interval '3 days' where lernender_id = v_l and ((einheit_id = v_e1 and lernziel = v_lz1) or (einheit_id = v_e2 and lernziel = v_lz2));

  -- 1. zweimal denselben Flug lesen → dieselben Karten, keine neuen Ausgaben
  j1 := schule.mischkarten(v_l, v_f1); j2 := schule.mischkarten(v_l, v_f1);
  select array_agg((x->>'id')::bigint order by (x->>'id')::bigint) into v_ids1 from jsonb_array_elements(j1) x;
  select array_agg((x->>'id')::bigint order by (x->>'id')::bigint) into v_ids2 from jsonb_array_elements(j2) x;
  select count(*) into v_n from schule.misch_ausgabe where lernender_id = v_l and eingeloest_am is null and verfallen_am is null;
  if jsonb_array_length(j1) <> 2 or v_ids1 is distinct from v_ids2 or v_n <> 2 then raise exception 'FEHLER 1: % / % Karten, % offene Ausgaben', jsonb_array_length(j1), jsonb_array_length(j2), v_n; end if;
  raise notice 'ok 1: zweimal gelesen → dieselben 2 Karten, 2 offene Ausgaben';

  -- 2. eine eingelöst → beim nächsten Lesen bleibt die andere, aufgefüllt wird nur für die Etappe ohne offene Karte
  v_a := v_ids1[1];
  perform schule.misch_buchen(v_l, v_a, true, 0::smallint, now());
  j2 := schule.mischkarten(v_l, v_f1);
  select array_agg((x->>'id')::bigint order by (x->>'id')::bigint) into v_ids2 from jsonb_array_elements(j2) x;
  select count(*) into v_n from schule.misch_ausgabe where lernender_id = v_l and eingeloest_am is null and verfallen_am is null;
  if jsonb_array_length(j2) <> 2 or not (v_ids1[2] = any(v_ids2)) or v_n <> 2 then raise exception 'FEHLER 2: %, % offene', v_ids2, v_n; end if;
  raise notice 'ok 2: eingelöste Karte ersetzt (Auffüllen je Etappe), die offene bleibt dieselbe';

  -- 3. anderen Flug lesen → Ausgaben des ersten verfallen (zählen nicht mehr)
  j1 := schule.mischkarten(v_l, v_f2);
  if exists (select 1 from schule.misch_ausgabe where lernender_id = v_l and einheit_id = v_f1 and eingeloest_am is null and verfallen_am is null) then raise exception 'FEHLER 3a: alte Ausgaben nicht verfallen'; end if;
  if schule.misch_gueltig(v_l, (select a from schule.aufgabe a where a.id = v_ids2[1]), jsonb_build_object('misch', true)) and not (v_ids2[1] in (select (x->>'id')::bigint from jsonb_array_elements(j1) x)) then
    raise exception 'FEHLER 3b: verfallene Ausgabe gültig'; end if;
  select count(*) into v_n from schule.misch_ausgabe where lernender_id = v_l and eingeloest_am is null and verfallen_am is null;
  if v_n <> jsonb_array_length(j1) then raise exception 'FEHLER 3c: % offene bei % Karten', v_n, jsonb_array_length(j1); end if;
  raise notice 'ok 3: anderer Flug → alte Ausgaben verfallen (verfallen_am), offene = ausgelieferte (%), keine Zeile gelöscht', v_n;

  -- 4. älter als 24 Stunden → verfällt, Karte wird neu ausgestellt
  update schule.misch_ausgabe set ausgegeben_am = now() - interval '25 hours' where lernender_id = v_l and einheit_id = v_f2 and eingeloest_am is null and verfallen_am is null;
  j2 := schule.mischkarten(v_l, v_f2);
  if exists (select 1 from schule.misch_ausgabe where lernender_id = v_l and eingeloest_am is null and verfallen_am is null and ausgegeben_am < now() - interval '24 hours') then raise exception 'FEHLER 4'; end if;
  raise notice 'ok 4: Ausgaben älter als 24 h verfallen; neu ausgestellt (%)', jsonb_array_length(j2);

  -- 5. Etappe nicht mehr gelandet → ihre Ausgabe verfällt, die Karte kommt nicht wieder
  update schule.karte_stand set sitzt = false where lernender_id = v_l and einheit_id = v_e1 and lernziel = v_lz1;
  j2 := schule.mischkarten(v_l, v_f2);
  if exists (select 1 from jsonb_array_elements(j2) x join schule.aufgabe a on a.id = (x->>'id')::bigint where a.einheit_id = v_e1 and a.variante_gruppe = v_lz1)
     or exists (select 1 from schule.misch_ausgabe m join schule.aufgabe a on a.id = m.aufgabe_id where m.lernender_id = v_l and m.eingeloest_am is null and m.verfallen_am is null
                 and a.einheit_id = v_e1 and a.variante_gruppe = v_lz1) then raise exception 'FEHLER 5'; end if;
  raise notice 'ok 5: Etappe wieder offen → ihre Ausgabe verfällt, keine Karte mehr daraus';
end $$;
rollback;
