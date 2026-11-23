-- NT-D 3 (23.11.2026): Vorrat für Nachtests auffüllen – drei Runden ohne Wiederholung (91 Teil 1 RS II/III; Vorsorge 31 RS, 1 Gym).
-- Quelle: inhalte/generatoren/_nt_2311.py (Texte selbst formuliert, Lösungen berechnet), Dateien inhalte/themen/*.json. 14 Aufgaben, davon 14 Sicherung.
-- Nur für den Haupt-Chat; NICHT von lehrplan-lb ausgeführt. In EINER Transaktion einspielen (psql -1). Wiederholt ausführbar.
-- Nur INSERT über schule.aufgaben_einfuegen; Einheiten werden nicht verändert. Kein DELETE, kein DROP.
-- Reihenfolge: unabhängig von TL-S; das SQL sucht die Einheit, deren Etappen-Katalog die Etappe enthält (Thema oder Teil über teil_stamm).
--   Abbruch mit Hinweis, wenn eine Etappe in keiner Einheit steht. Nach NT-S 2 einspielen (wirkt sonst nur als Vorrat).
-- Die neuen Aufgaben sind sofort sichtbar (aufgabe.freigegeben Standard true).

-- Thema 91 (raum.schraegbilder), Etappe pyramide: 3 Aufgaben (sicherung)
do $nt$
declare v_e bigint; v_max int; v_auf jsonb; v_n int; v_stamm boolean;
begin
  v_stamm := exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm');
  -- Einheit mit dieser Etappe im Katalog: vor der Teilung die Einheit des Themas, danach die des richtigen Teils
  execute format('select e.id from schule.einheit e join schule.thema t on t.id = e.thema_id
                   where e.status <> %L and (t.id = $1 %s)
                     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->%L, %L::jsonb)) x where x->>%L = $2)
                   order by e.id limit 1', 'ersetzt', case when v_stamm then 'or t.teil_stamm = $1' else '' end, 'etappen', '[]', 'lernziel')
    into v_e using 91::bigint, 'pyramide'::text;
  if v_e is null then raise exception 'Thema 91: keine Einheit mit Etappe pyramide – zuerst lk_einspiel_2211.sql einspielen'; end if;
  if (select schluessel from schule.thema where id = 91) <> 'raum.schraegbilder' then raise exception 'Thema 91 ist nicht raum.schraegbilder'; end if;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j$[{"l": "pyramide", "t": "pyramide", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Die Grundfläche einer Pyramide ist ein Siebeneck. Wie viele Kanten hat die Pyramide?"}, "w": "7 Kanten in der Grundfläche und 7 Seitenkanten zur Spitze: 7 + 7 = 14.", "o": {"wert": 14}}, {"l": "pyramide", "t": "pyramide", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Eine Pyramide hat 10 Kanten. Wie viele Flächen hat sie?"}, "w": "Bei einem n-Eck als Grundfläche hat die Pyramide 2n Kanten: n = 10 : 2 = 5. Flächen: Grundfläche + 5 Seitenflächen = 6.", "o": {"wert": 6}}, {"l": "pyramide", "t": "pyramide", "p": "sicherung", "s": 2, "y": "luecken", "f": {"text": "Die Grundfläche einer Pyramide ist ein Neuneck. Gib die Anzahl der Ecken, Kanten und Flächen an.", "schablone": "Ecken □ · Kanten □ · Flächen □", "hinweis": "je eine ganze Zahl"}, "w": "Ecken: 9 + Spitze = 10. Kanten: 9 unten + 9 zur Spitze = 18. Flächen: 9 Seitenflächen + Grundfläche = 10.", "o": {"werte": [10, 18, 10]}}]$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  raise notice 'Einheit % (pyramide): % von 3 Aufgaben eingefügt (0 = schon vorhanden)', v_e, v_n;
  if v_n not in (0, 3) then raise exception 'Etappe pyramide: nur % von 3 eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
end $nt$;

-- Thema 91 (raum.schraegbilder), Etappe wahre_groesse: 3 Aufgaben (sicherung)
do $nt$
declare v_e bigint; v_max int; v_auf jsonb; v_n int; v_stamm boolean;
begin
  v_stamm := exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm');
  -- Einheit mit dieser Etappe im Katalog: vor der Teilung die Einheit des Themas, danach die des richtigen Teils
  execute format('select e.id from schule.einheit e join schule.thema t on t.id = e.thema_id
                   where e.status <> %L and (t.id = $1 %s)
                     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->%L, %L::jsonb)) x where x->>%L = $2)
                   order by e.id limit 1', 'ersetzt', case when v_stamm then 'or t.teil_stamm = $1' else '' end, 'etappen', '[]', 'lernziel')
    into v_e using 91::bigint, 'wahre_groesse'::text;
  if v_e is null then raise exception 'Thema 91: keine Einheit mit Etappe wahre_groesse – zuerst lk_einspiel_2211.sql einspielen'; end if;
  if (select schluessel from schule.thema where id = 91) <> 'raum.schraegbilder' then raise exception 'Thema 91 ist nicht raum.schraegbilder'; end if;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j$[{"l": "wahre_groesse", "t": "wahre_groesse", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Im Schrägbild mit q = 0,5 ist eine Kante nach hinten 4,5 cm lang gezeichnet. Wie lang ist sie in Wirklichkeit?"}, "w": "Nach hinten wird halbiert, also zurückrechnen: 4,5 cm : 0,5 = 9 cm.", "o": {"wert": 9, "einheit": "cm"}}, {"l": "wahre_groesse", "t": "wahre_groesse", "p": "sicherung", "s": 2, "y": "auswahl", "f": {"text": "Ein Würfel wird als Schrägbild mit q = 0,5 und 45° gezeichnet. Welche Kanten erscheinen in wahrer Länge?"}, "w": "Kanten parallel zur Zeichenebene (Breite und Höhe) bleiben in wahrer Länge; nur die Kanten nach hinten werden mit q verkürzt.", "a": ["die Kanten nach rechts und nach oben", "nur die Kanten nach hinten", "alle Kanten", "keine Kante"], "o": {"index": 0}}, {"l": "wahre_groesse", "t": "wahre_groesse", "p": "sicherung", "s": 2, "y": "luecken", "f": {"text": "Ein Quader ist 8 cm breit, 3 cm hoch und 6 cm tief. Zeichne ihn mit q = 0,5. Wie lang werden Breite, Höhe und Tiefe gezeichnet?", "schablone": "Breite □ cm · Höhe □ cm · Tiefe □ cm", "hinweis": "je eine ganze Zahl"}, "w": "Breite und Höhe bleiben: 8 cm und 3 cm. Die Tiefe geht nach hinten: 6 cm · 0,5 = 3 cm.", "o": {"werte": [8, 3, 3]}}]$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  raise notice 'Einheit % (wahre_groesse): % von 3 Aufgaben eingefügt (0 = schon vorhanden)', v_e, v_n;
  if v_n not in (0, 3) then raise exception 'Etappe wahre_groesse: nur % von 3 eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
end $nt$;

-- Thema 31 (terme.bruchterme), Etappe definitionsmenge: 1 Aufgaben (sicherung)
do $nt$
declare v_e bigint; v_max int; v_auf jsonb; v_n int; v_stamm boolean;
begin
  v_stamm := exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm');
  -- Einheit mit dieser Etappe im Katalog: vor der Teilung die Einheit des Themas, danach die des richtigen Teils
  execute format('select e.id from schule.einheit e join schule.thema t on t.id = e.thema_id
                   where e.status <> %L and (t.id = $1 %s)
                     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->%L, %L::jsonb)) x where x->>%L = $2)
                   order by e.id limit 1', 'ersetzt', case when v_stamm then 'or t.teil_stamm = $1' else '' end, 'etappen', '[]', 'lernziel')
    into v_e using 31::bigint, 'definitionsmenge'::text;
  if v_e is null then raise exception 'Thema 31: keine Einheit mit Etappe definitionsmenge – zuerst lk_einspiel_2211.sql einspielen'; end if;
  if (select schluessel from schule.thema where id = 31) <> 'terme.bruchterme' then raise exception 'Thema 31 ist nicht terme.bruchterme'; end if;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j$[{"l": "definitionsmenge", "t": "definitionsmenge", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Für welche Zahl ist der Term 12/(3x − 9) nicht definiert?"}, "w": "Der Nenner darf nicht 0 sein: 3x − 9 = 0, also x = 3. Für x = 3 ist der Term nicht definiert.", "o": {"wert": 3}}]$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  raise notice 'Einheit % (definitionsmenge): % von 1 Aufgaben eingefügt (0 = schon vorhanden)', v_e, v_n;
  if v_n not in (0, 1) then raise exception 'Etappe definitionsmenge: nur % von 1 eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
end $nt$;

-- Thema 31 (terme.bruchterme), Etappe termwert: 1 Aufgaben (sicherung)
do $nt$
declare v_e bigint; v_max int; v_auf jsonb; v_n int; v_stamm boolean;
begin
  v_stamm := exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm');
  -- Einheit mit dieser Etappe im Katalog: vor der Teilung die Einheit des Themas, danach die des richtigen Teils
  execute format('select e.id from schule.einheit e join schule.thema t on t.id = e.thema_id
                   where e.status <> %L and (t.id = $1 %s)
                     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->%L, %L::jsonb)) x where x->>%L = $2)
                   order by e.id limit 1', 'ersetzt', case when v_stamm then 'or t.teil_stamm = $1' else '' end, 'etappen', '[]', 'lernziel')
    into v_e using 31::bigint, 'termwert'::text;
  if v_e is null then raise exception 'Thema 31: keine Einheit mit Etappe termwert – zuerst lk_einspiel_2211.sql einspielen'; end if;
  if (select schluessel from schule.thema where id = 31) <> 'terme.bruchterme' then raise exception 'Thema 31 ist nicht terme.bruchterme'; end if;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j$[{"l": "termwert", "t": "termwert", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Berechne T(4) für T(x) = (3x − 2)/(x + 6)."}, "w": "Einsetzen: (3 · 4 − 2)/(4 + 6) = 10/10 = 1.", "o": {"wert": 1}}]$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  raise notice 'Einheit % (termwert): % von 1 Aufgaben eingefügt (0 = schon vorhanden)', v_e, v_n;
  if v_n not in (0, 1) then raise exception 'Etappe termwert: nur % von 1 eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
end $nt$;

-- Thema 1 (gleichungen.einfach), Etappe zwei_schritte: 3 Aufgaben (sicherung)
do $nt$
declare v_e bigint; v_max int; v_auf jsonb; v_n int; v_stamm boolean;
begin
  v_stamm := exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm');
  -- Einheit mit dieser Etappe im Katalog: vor der Teilung die Einheit des Themas, danach die des richtigen Teils
  execute format('select e.id from schule.einheit e join schule.thema t on t.id = e.thema_id
                   where e.status <> %L and (t.id = $1 %s)
                     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->%L, %L::jsonb)) x where x->>%L = $2)
                   order by e.id limit 1', 'ersetzt', case when v_stamm then 'or t.teil_stamm = $1' else '' end, 'etappen', '[]', 'lernziel')
    into v_e using 1::bigint, 'zwei_schritte'::text;
  if v_e is null then raise exception 'Thema 1: keine Einheit mit Etappe zwei_schritte – zuerst lk_einspiel_2211.sql einspielen'; end if;
  if (select schluessel from schule.thema where id = 1) <> 'gleichungen.einfach' then raise exception 'Thema 1 ist nicht gleichungen.einfach'; end if;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j$[{"l": "zwei_schritte", "t": "umkehren", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Löse 6 · x + 17 = 95."}, "w": "Rückwärts: erst − 17: 95 − 17 = 78, dann : 6: 78 : 6 = 13.", "o": {"wert": 13}}, {"l": "zwei_schritte", "t": "umkehren", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Löse 9 · x + 25 = 97."}, "w": "Rückwärts: erst − 25: 97 − 25 = 72, dann : 9: 72 : 9 = 8.", "o": {"wert": 8}}, {"l": "zwei_schritte", "t": "umkehren", "p": "sicherung", "s": 2, "y": "auswahl", "f": {"text": "Welcher Rechenweg löst x · 4 − 15 = 33?"}, "w": "Rückwärts rechnen heißt: die letzte Rechnung zuerst umkehren. Erst + 15 (33 + 15 = 48), dann : 4 (48 : 4 = 12).", "a": ["erst : 4, dann + 15", "erst − 15, dann · 4", "erst + 15, dann : 4", "erst · 4, dann − 15"], "o": {"index": 2}}]$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  raise notice 'Einheit % (zwei_schritte): % von 3 Aufgaben eingefügt (0 = schon vorhanden)', v_e, v_n;
  if v_n not in (0, 3) then raise exception 'Etappe zwei_schritte: nur % von 3 eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
end $nt$;

-- Thema 1 (gleichungen.einfach), Etappe probe: 3 Aufgaben (sicherung)
do $nt$
declare v_e bigint; v_max int; v_auf jsonb; v_n int; v_stamm boolean;
begin
  v_stamm := exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm');
  -- Einheit mit dieser Etappe im Katalog: vor der Teilung die Einheit des Themas, danach die des richtigen Teils
  execute format('select e.id from schule.einheit e join schule.thema t on t.id = e.thema_id
                   where e.status <> %L and (t.id = $1 %s)
                     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->%L, %L::jsonb)) x where x->>%L = $2)
                   order by e.id limit 1', 'ersetzt', case when v_stamm then 'or t.teil_stamm = $1' else '' end, 'etappen', '[]', 'lernziel')
    into v_e using 1::bigint, 'probe'::text;
  if v_e is null then raise exception 'Thema 1: keine Einheit mit Etappe probe – zuerst lk_einspiel_2211.sql einspielen'; end if;
  if (select schluessel from schule.thema where id = 1) <> 'gleichungen.einfach' then raise exception 'Thema 1 ist nicht gleichungen.einfach'; end if;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j$[{"l": "probe", "t": "verstehen", "p": "sicherung", "s": 2, "y": "auswahl", "f": {"text": "So wurde 3 · x + 8 = 35 gelöst: Schritt 1: 35 − 8 = 27. Schritt 2: 27 · 3 = 81. Ergebnis: x = 81. Wo steckt der Fehler?"}, "w": "In Schritt 2 muss geteilt werden: 27 : 3 = 9. Probe: 3 · 9 + 8 = 35 ✓. Mit 81 wäre 3 · 81 + 8 = 251.", "a": ["In Schritt 1: Es muss 35 + 8 heißen.", "In Schritt 2: Es muss 27 : 3 heißen.", "Es gibt keinen Fehler.", "Beide Schritte sind falsch."], "o": {"index": 1}}, {"l": "probe", "t": "verstehen", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Bei x : 4 − 6 = 9 hat jemand x = 12 herausbekommen. Die Probe geht nicht auf. Wie heißt die richtige Lösung?"}, "w": "Probe: 12 : 4 − 6 = −3, nicht 9. Richtig rückwärts: 9 + 6 = 15, 15 · 4 = 60. Probe: 60 : 4 − 6 = 9 ✓.", "o": {"wert": 60}}, {"l": "probe", "t": "verstehen", "p": "sicherung", "s": 2, "y": "auswahl", "f": {"text": "Welche Zahl ist die Lösung von 5 · x − 12 = 43? Mache die Probe."}, "w": "Probe mit 11: 5 · 11 − 12 = 55 − 12 = 43 ✓. Die anderen Zahlen ergeben nicht 43.", "a": ["9", "12", "11", "6"], "o": {"index": 2}}]$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  raise notice 'Einheit % (probe): % von 3 Aufgaben eingefügt (0 = schon vorhanden)', v_e, v_n;
  if v_n not in (0, 3) then raise exception 'Etappe probe: nur % von 3 eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
end $nt$;

-- Rauchtest (liest nur)
do $pruef$
declare v int; v_f text := 'id';
begin
  -- nur Aufgaben der eigenen Themen (bzw. ihrer Teile nach TL-S) zählen – gleiche Texte in anderen Themen sind erlaubt
  if exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm') then
    v_f := 'teil_stamm';
  end if;
  execute format($q$select count(*) from schule.aufgabe a where (a.variante_gruppe = 'pyramide' and a.thema_id in (select x.id from schule.thema x where x.id = 91 or x.%1$I = 91) and a.frage->>'text' in ('Die Grundfläche einer Pyramide ist ein Siebeneck. Wie viele Kanten hat die Pyramide?', 'Eine Pyramide hat 10 Kanten. Wie viele Flächen hat sie?', 'Die Grundfläche einer Pyramide ist ein Neuneck. Gib die Anzahl der Ecken, Kanten und Flächen an.')) or (a.variante_gruppe = 'wahre_groesse' and a.thema_id in (select x.id from schule.thema x where x.id = 91 or x.%1$I = 91) and a.frage->>'text' in ('Im Schrägbild mit q = 0,5 ist eine Kante nach hinten 4,5 cm lang gezeichnet. Wie lang ist sie in Wirklichkeit?', 'Ein Würfel wird als Schrägbild mit q = 0,5 und 45° gezeichnet. Welche Kanten erscheinen in wahrer Länge?', 'Ein Quader ist 8 cm breit, 3 cm hoch und 6 cm tief. Zeichne ihn mit q = 0,5. Wie lang werden Breite, Höhe und Tiefe gezeichnet?')) or (a.variante_gruppe = 'definitionsmenge' and a.thema_id in (select x.id from schule.thema x where x.id = 31 or x.%1$I = 31) and a.frage->>'text' in ('Für welche Zahl ist der Term 12/(3x − 9) nicht definiert?')) or (a.variante_gruppe = 'termwert' and a.thema_id in (select x.id from schule.thema x where x.id = 31 or x.%1$I = 31) and a.frage->>'text' in ('Berechne T(4) für T(x) = (3x − 2)/(x + 6).')) or (a.variante_gruppe = 'zwei_schritte' and a.thema_id in (select x.id from schule.thema x where x.id = 1 or x.%1$I = 1) and a.frage->>'text' in ('Löse 6 · x + 17 = 95.', 'Löse 9 · x + 25 = 97.', 'Welcher Rechenweg löst x · 4 − 15 = 33?')) or (a.variante_gruppe = 'probe' and a.thema_id in (select x.id from schule.thema x where x.id = 1 or x.%1$I = 1) and a.frage->>'text' in ('So wurde 3 · x + 8 = 35 gelöst: Schritt 1: 35 − 8 = 27. Schritt 2: 27 · 3 = 81. Ergebnis: x = 81. Wo steckt der Fehler?', 'Bei x : 4 − 6 = 9 hat jemand x = 12 herausbekommen. Die Probe geht nicht auf. Wie heißt die richtige Lösung?', 'Welche Zahl ist die Lösung von 5 · x − 12 = 43? Mache die Probe.'))$q$, v_f) into v;
  if v <> 14 then raise exception 'Rauchtest NT-D: % von 14 Aufgaben', v; end if;
  raise notice 'Rauchtest NT-D bestanden: 14 Aufgaben (14 Sicherung)';
end $pruef$;
