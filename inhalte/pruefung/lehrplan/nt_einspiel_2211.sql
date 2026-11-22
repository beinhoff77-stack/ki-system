-- NT-D (22.11.2026): fehlende Sicherungs-Aufgaben für Nachtests kleiner Flüge (Fehlliste NT-S) und Thema 57 „verzerrte Diagramme berichtigen/verbessern“.
-- Quelle: inhalte/generatoren/_nt_2211.py (Texte selbst formuliert, Lösungen berechnet), Dateien inhalte/themen/*.json. 44 Aufgaben, davon 35 Sicherung.
-- Nur für den Haupt-Chat; NICHT von lehrplan-lb ausgeführt. In EINER Transaktion einspielen (psql -1). Wiederholt ausführbar.
-- Nur INSERT über schule.aufgaben_einfuegen; Einheiten werden nicht verändert. Kein DELETE, kein DROP.
-- Reihenfolge: NACH lk_einspiel_2211.sql (cavalieri und vierecke_konstruieren gibt es erst dann; sonst Abbruch mit Hinweis).
--   Vor oder nach TL-S möglich: Das SQL sucht die Einheit, deren Etappen-Katalog die Etappe enthält (Thema oder Teil über teil_stamm).
--   Empfohlen vor TL-S, dann ziehen die Aufgaben mit ihrer Etappe in den Teil (gleiche Ids).
-- Die neuen Aufgaben sind sofort sichtbar (aufgabe.freigegeben Standard true).

-- Thema 46 (abbildungen.kongruenz), Etappe punktspiegelung: 9 Aufgaben (sicherung)
do $nt$
declare v_e bigint; v_max int; v_auf jsonb; v_n int; v_stamm boolean;
begin
  v_stamm := exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm');
  -- Einheit mit dieser Etappe im Katalog: vor der Teilung die Einheit des Themas, danach die des richtigen Teils
  execute format('select e.id from schule.einheit e join schule.thema t on t.id = e.thema_id
                   where e.status <> %L and (t.id = $1 %s)
                     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->%L, %L::jsonb)) x where x->>%L = $2)
                   order by e.id limit 1', 'ersetzt', case when v_stamm then 'or t.teil_stamm = $1' else '' end, 'etappen', '[]', 'lernziel')
    into v_e using 46::bigint, 'punktspiegelung'::text;
  if v_e is null then raise exception 'Thema 46: keine Einheit mit Etappe punktspiegelung – zuerst lk_einspiel_2211.sql einspielen'; end if;
  if (select schluessel from schule.thema where id = 46) <> 'abbildungen.kongruenz' then raise exception 'Thema 46 ist nicht abbildungen.kongruenz'; end if;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j$[{"l": "punktspiegelung", "t": "punktspiegelung", "p": "sicherung", "s": 2, "y": "luecken", "f": {"text": "Spiegle den Punkt P(5 | 1) am Zentrum Z(2 | 3).", "schablone": "P'(□ | □)", "hinweis": "x-Koordinate, dann y-Koordinate"}, "w": "Z ist die Mitte von P und P': x = 2 · 2 − 5 = −1, y = 2 · 3 − 1 = 5. Also P'(−1 | 5).", "o": {"werte": [-1, 5]}}, {"l": "punktspiegelung", "t": "punktspiegelung", "p": "sicherung", "s": 2, "y": "luecken", "f": {"text": "Spiegle den Punkt P(−3 | 4) am Zentrum Z(1 | −1).", "schablone": "P'(□ | □)", "hinweis": "x-Koordinate, dann y-Koordinate"}, "w": "Z ist die Mitte von P und P': x = 2 · 1 − −3 = 5, y = 2 · −1 − 4 = −6. Also P'(5 | −6).", "o": {"werte": [5, -6]}}, {"l": "punktspiegelung", "t": "punktspiegelung", "p": "sicherung", "s": 2, "y": "luecken", "f": {"text": "Spiegle den Punkt P(0 | −5) am Zentrum Z(−2 | 0).", "schablone": "P'(□ | □)", "hinweis": "x-Koordinate, dann y-Koordinate"}, "w": "Z ist die Mitte von P und P': x = 2 · −2 − 0 = −4, y = 2 · 0 − −5 = 5. Also P'(−4 | 5).", "o": {"werte": [-4, 5]}}, {"l": "punktspiegelung", "t": "punktspiegelung", "p": "sicherung", "s": 2, "y": "luecken", "f": {"text": "Spiegle den Punkt P(7 | −2) am Zentrum Z(3 | 1).", "schablone": "P'(□ | □)", "hinweis": "x-Koordinate, dann y-Koordinate"}, "w": "Z ist die Mitte von P und P': x = 2 · 3 − 7 = −1, y = 2 · 1 − −2 = 4. Also P'(−1 | 4).", "o": {"werte": [-1, 4]}}, {"l": "punktspiegelung", "t": "punktspiegelung", "p": "sicherung", "s": 2, "y": "luecken", "f": {"text": "Spiegle den Punkt P(−6 | −3) am Zentrum Z(−1 | −2).", "schablone": "P'(□ | □)", "hinweis": "x-Koordinate, dann y-Koordinate"}, "w": "Z ist die Mitte von P und P': x = 2 · −1 − −6 = 4, y = 2 · −2 − −3 = −1. Also P'(4 | −1).", "o": {"werte": [4, -1]}}, {"l": "punktspiegelung", "t": "punktspiegelung", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "P(2 | 5) wird an Z gespiegelt und landet bei P'(8 | −1). Welche x-Koordinate hat Z?"}, "w": "Z ist die Mitte von P und P': x = (2 + 8) : 2 = 5.", "o": {"wert": 5}}, {"l": "punktspiegelung", "t": "punktspiegelung", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "P(−4 | 3) und P'(6 | −7) liegen punktsymmetrisch zu Z. Welche y-Koordinate hat Z?"}, "w": "Z ist die Mitte: y = (3 + (−7)) : 2 = −2.", "o": {"wert": -2}}, {"l": "punktspiegelung", "t": "punktspiegelung", "p": "sicherung", "s": 2, "y": "auswahl", "f": {"text": "Eine Strecke AB wird an einem Punkt Z gespiegelt. Wie liegt die Bildstrecke A'B' zu AB?"}, "w": "Die Punktspiegelung ist eine Drehung um 180°: Die Bildstrecke ist gleich lang und parallel zu AB, sie zeigt nur in die Gegenrichtung.", "a": ["parallel und gleich lang", "senkrecht und gleich lang", "parallel und doppelt so lang", "auf derselben Geraden, halb so lang"], "o": {"index": 0}}, {"l": "punktspiegelung", "t": "punktspiegelung", "p": "sicherung", "s": 2, "y": "auswahl", "f": {"text": "Welche dieser Figuren ist immer punktsymmetrisch?"}, "w": "Beim Parallelogramm halbieren sich die Diagonalen; ihr Schnittpunkt ist das Symmetriezentrum. Drachen und gleichschenkliges Trapez sind nur achsensymmetrisch.", "a": ["Drachenviereck", "gleichschenkliges Trapez", "Parallelogramm", "gleichschenkliges Dreieck"], "o": {"index": 2}}]$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  raise notice 'Einheit % (punktspiegelung): % von 9 Aufgaben eingefügt (0 = schon vorhanden)', v_e, v_n;
  if v_n not in (0, 9) then raise exception 'Etappe punktspiegelung: nur % von 9 eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
end $nt$;

-- Thema 91 (raum.schraegbilder), Etappe rotation: 3 Aufgaben (sicherung)
do $nt$
declare v_e bigint; v_max int; v_auf jsonb; v_n int; v_stamm boolean;
begin
  v_stamm := exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm');
  -- Einheit mit dieser Etappe im Katalog: vor der Teilung die Einheit des Themas, danach die des richtigen Teils
  execute format('select e.id from schule.einheit e join schule.thema t on t.id = e.thema_id
                   where e.status <> %L and (t.id = $1 %s)
                     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->%L, %L::jsonb)) x where x->>%L = $2)
                   order by e.id limit 1', 'ersetzt', case when v_stamm then 'or t.teil_stamm = $1' else '' end, 'etappen', '[]', 'lernziel')
    into v_e using 91::bigint, 'rotation'::text;
  if v_e is null then raise exception 'Thema 91: keine Einheit mit Etappe rotation – zuerst lk_einspiel_2211.sql einspielen'; end if;
  if (select schluessel from schule.thema where id = 91) <> 'raum.schraegbilder' then raise exception 'Thema 91 ist nicht raum.schraegbilder'; end if;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j$[{"l": "rotation", "t": "rotation", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Ein Rechteck mit den Seiten 5 cm und 8 cm dreht sich um die 5-cm-Seite. Welchen Radius hat der entstehende Zylinder?"}, "w": "Die 5-cm-Seite liegt auf der Achse und wird zur Höhe; die 8-cm-Seite steht senkrecht dazu und wird zum Radius: r = 8 cm.", "o": {"wert": 8, "einheit": "cm"}}, {"l": "rotation", "t": "rotation", "p": "sicherung", "s": 2, "y": "auswahl", "f": {"text": "Ein Halbkreis dreht sich um seinen Durchmesser. Welcher Körper entsteht?"}, "w": "Jeder Punkt des Bogens beschreibt einen Kreis um die Achse; zusammen ergibt das eine Kugel.", "a": ["ein Kegel", "eine Kugel", "ein Zylinder", "eine Halbkugel"], "o": {"index": 1}}, {"l": "rotation", "t": "rotation", "p": "sicherung", "s": 2, "y": "luecken", "f": {"text": "Ein rechtwinkliges Dreieck mit den Katheten 4 cm und 10 cm dreht sich um die 10-cm-Kathete. Gib Radius und Höhe des Kegels an.", "schablone": "r = □ cm; h = □ cm", "hinweis": "je eine ganze Zahl"}, "w": "Die Kathete auf der Achse (10 cm) wird zur Höhe, die andere (4 cm) zum Radius.", "o": {"werte": [4, 10]}}]$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  raise notice 'Einheit % (rotation): % von 3 Aufgaben eingefügt (0 = schon vorhanden)', v_e, v_n;
  if v_n not in (0, 3) then raise exception 'Etappe rotation: nur % von 3 eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
end $nt$;

-- Thema 91 (raum.schraegbilder), Etappe axialschnitt: 3 Aufgaben (sicherung)
do $nt$
declare v_e bigint; v_max int; v_auf jsonb; v_n int; v_stamm boolean;
begin
  v_stamm := exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm');
  -- Einheit mit dieser Etappe im Katalog: vor der Teilung die Einheit des Themas, danach die des richtigen Teils
  execute format('select e.id from schule.einheit e join schule.thema t on t.id = e.thema_id
                   where e.status <> %L and (t.id = $1 %s)
                     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->%L, %L::jsonb)) x where x->>%L = $2)
                   order by e.id limit 1', 'ersetzt', case when v_stamm then 'or t.teil_stamm = $1' else '' end, 'etappen', '[]', 'lernziel')
    into v_e using 91::bigint, 'axialschnitt'::text;
  if v_e is null then raise exception 'Thema 91: keine Einheit mit Etappe axialschnitt – zuerst lk_einspiel_2211.sql einspielen'; end if;
  if (select schluessel from schule.thema where id = 91) <> 'raum.schraegbilder' then raise exception 'Thema 91 ist nicht raum.schraegbilder'; end if;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j$[{"l": "axialschnitt", "t": "axialschnitt", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Ein Zylinder hat r = 6 cm und h = 10 cm. Wie groß ist der Flächeninhalt seines Axialschnitts?"}, "w": "Der Axialschnitt ist ein Rechteck aus Durchmesser und Höhe: 12 cm · 10 cm = 120 cm².", "o": {"wert": 120, "einheit": "cm²"}}, {"l": "axialschnitt", "t": "axialschnitt", "p": "sicherung", "s": 2, "y": "auswahl", "f": {"text": "Welche Form hat der Axialschnitt eines geraden Kreiskegels?"}, "w": "Der Schnitt durch die Achse trifft die Spitze und einen Durchmesser der Grundfläche: ein gleichschenkliges Dreieck.", "a": ["ein gleichschenkliges Dreieck", "ein Rechteck", "ein Kreis", "ein Trapez"], "o": {"index": 0}}, {"l": "axialschnitt", "t": "axialschnitt", "p": "sicherung", "s": 2, "y": "luecken", "f": {"text": "Ein Zylinder hat r = 3 cm und h = 7 cm. Welche Seitenlängen hat das Rechteck des Axialschnitts?", "schablone": "□ cm × □ cm", "hinweis": "erst die Breite (Durchmesser), dann die Höhe"}, "w": "Eine Seite ist der Durchmesser 2 · 3 = 6 cm, die andere die Höhe 7 cm.", "o": {"werte": [6, 7]}}]$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  raise notice 'Einheit % (axialschnitt): % von 3 Aufgaben eingefügt (0 = schon vorhanden)', v_e, v_n;
  if v_n not in (0, 3) then raise exception 'Etappe axialschnitt: nur % von 3 eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
end $nt$;

-- Thema 101 (messen.prisma_zylinder), Etappe cavalieri: 9 Aufgaben (sicherung)
do $nt$
declare v_e bigint; v_max int; v_auf jsonb; v_n int; v_stamm boolean;
begin
  v_stamm := exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm');
  -- Einheit mit dieser Etappe im Katalog: vor der Teilung die Einheit des Themas, danach die des richtigen Teils
  execute format('select e.id from schule.einheit e join schule.thema t on t.id = e.thema_id
                   where e.status <> %L and (t.id = $1 %s)
                     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->%L, %L::jsonb)) x where x->>%L = $2)
                   order by e.id limit 1', 'ersetzt', case when v_stamm then 'or t.teil_stamm = $1' else '' end, 'etappen', '[]', 'lernziel')
    into v_e using 101::bigint, 'cavalieri'::text;
  if v_e is null then raise exception 'Thema 101: keine Einheit mit Etappe cavalieri – zuerst lk_einspiel_2211.sql einspielen'; end if;
  if (select schluessel from schule.thema where id = 101) <> 'messen.prisma_zylinder' then raise exception 'Thema 101 ist nicht messen.prisma_zylinder'; end if;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j$[{"l": "cavalieri", "t": "cavalieri", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Ein schiefes Prisma hat die Grundfläche G = 18 cm² und die Höhe h = 4 cm. Berechne sein Volumen."}, "w": "Nach Cavalieri gilt auch für schiefe Prismen V = G · h = 18 · 4 = 72 cm³.", "o": {"wert": 72, "einheit": "cm³"}}, {"l": "cavalieri", "t": "cavalieri", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Ein schiefes Prisma hat die Grundfläche G = 25 cm² und die Höhe h = 6 cm. Berechne sein Volumen."}, "w": "Nach Cavalieri gilt auch für schiefe Prismen V = G · h = 25 · 6 = 150 cm³.", "o": {"wert": 150, "einheit": "cm³"}}, {"l": "cavalieri", "t": "cavalieri", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Ein schiefes Prisma hat die Grundfläche G = 9 cm² und die Höhe h = 11 cm. Berechne sein Volumen."}, "w": "Nach Cavalieri gilt auch für schiefe Prismen V = G · h = 9 · 11 = 99 cm³.", "o": {"wert": 99, "einheit": "cm³"}}, {"l": "cavalieri", "t": "cavalieri", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Ein schiefer Zylinder hat das Volumen 96 cm³ und die Grundfläche 12 cm². Wie hoch ist er?"}, "w": "V = G · h, also h = V : G = 96 : 12 = 8 cm.", "o": {"wert": 8, "einheit": "cm"}}, {"l": "cavalieri", "t": "cavalieri", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Ein schiefer Zylinder hat das Volumen 150 cm³ und die Grundfläche 25 cm². Wie hoch ist er?"}, "w": "V = G · h, also h = V : G = 150 : 25 = 6 cm.", "o": {"wert": 6, "einheit": "cm"}}, {"l": "cavalieri", "t": "cavalieri", "p": "sicherung", "s": 2, "y": "auswahl", "f": {"text": "Zwei Körper haben in jeder Höhe gleich große Querschnittsflächen und sind gleich hoch. Was folgt nach Cavalieri?"}, "w": "Das Prinzip von Cavalieri: gleiche Querschnitte in jeder Höhe und gleiche Höhe ergeben gleiches Volumen – die Form darf verschieden sein.", "a": ["Sie haben das gleiche Volumen.", "Sie haben die gleiche Oberfläche.", "Sie sind deckungsgleich.", "Der schiefere Körper hat mehr Volumen."], "o": {"index": 0}}, {"l": "cavalieri", "t": "cavalieri", "p": "sicherung", "s": 2, "y": "auswahl", "f": {"text": "Ein Stapel Münzen wird schräg geschoben. Was bleibt gleich?"}, "w": "Jede Münze behält ihre Fläche und die Stapelhöhe ändert sich nicht. Deshalb bleibt das Volumen gleich, auch wenn der Stapel schief steht.", "a": ["die Oberfläche", "die Länge der Seitenkante", "die Form der Seitenfläche", "das Volumen"], "o": {"index": 3}}, {"l": "cavalieri", "t": "cavalieri", "p": "sicherung", "s": 2, "y": "luecken", "f": {"text": "Ein gerades und ein schiefes Prisma haben beide G = 14 cm² und die Höhe 5 cm. Berechne beide Volumen.", "schablone": "gerade: □ cm³; schief: □ cm³", "hinweis": "je eine ganze Zahl"}, "w": "Beide: V = G · h = 14 · 5 = 70 cm³. Die Schräge ändert das Volumen nicht.", "o": {"werte": [70, 70]}}, {"l": "cavalieri", "t": "cavalieri", "p": "sicherung", "s": 2, "y": "luecken", "f": {"text": "Ein schiefer Zylinder hat den Radius 2 cm und die Höhe 9 cm. Schreibe sein Volumen als Vielfaches von π.", "schablone": "V = □ · π cm³", "hinweis": "eine ganze Zahl"}, "w": "G = π · 2² = 4π cm². V = G · h = 4π · 9 = 36π cm³.", "o": {"werte": [36]}}]$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  raise notice 'Einheit % (cavalieri): % von 9 Aufgaben eingefügt (0 = schon vorhanden)', v_e, v_n;
  if v_n not in (0, 9) then raise exception 'Etappe cavalieri: nur % von 9 eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
end $nt$;

-- Thema 44 (geometrie.konstruktion), Etappe vierecke: 3 Aufgaben (sicherung)
do $nt$
declare v_e bigint; v_max int; v_auf jsonb; v_n int; v_stamm boolean;
begin
  v_stamm := exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm');
  -- Einheit mit dieser Etappe im Katalog: vor der Teilung die Einheit des Themas, danach die des richtigen Teils
  execute format('select e.id from schule.einheit e join schule.thema t on t.id = e.thema_id
                   where e.status <> %L and (t.id = $1 %s)
                     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->%L, %L::jsonb)) x where x->>%L = $2)
                   order by e.id limit 1', 'ersetzt', case when v_stamm then 'or t.teil_stamm = $1' else '' end, 'etappen', '[]', 'lernziel')
    into v_e using 44::bigint, 'vierecke'::text;
  if v_e is null then raise exception 'Thema 44: keine Einheit mit Etappe vierecke – zuerst lk_einspiel_2211.sql einspielen'; end if;
  if (select schluessel from schule.thema where id = 44) <> 'geometrie.konstruktion' then raise exception 'Thema 44 ist nicht geometrie.konstruktion'; end if;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j$[{"l": "vierecke", "t": "vierecke", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "In einem Parallelogramm ist α = 70°. Wie groß ist β?"}, "w": "Benachbarte Winkel im Parallelogramm ergänzen sich zu 180°: β = 180° − 70° = 110°.", "o": {"wert": 110, "einheit": "°"}}, {"l": "vierecke", "t": "vierecke", "p": "sicherung", "s": 2, "y": "auswahl", "f": {"text": "In welchem Viereck stehen die Diagonalen immer senkrecht aufeinander und halbieren sich?"}, "w": "In der Raute halbieren sich die Diagonalen (wie im Parallelogramm) und stehen senkrecht aufeinander (wie im Drachen).", "a": ["Rechteck", "Raute", "Parallelogramm", "Trapez"], "o": {"index": 1}}, {"l": "vierecke", "t": "vierecke", "p": "sicherung", "s": 2, "y": "luecken", "f": {"text": "In einem Parallelogramm ABCD ist α = 65°. Berechne β und γ.", "schablone": "β = □°; γ = □°", "hinweis": "je eine ganze Zahl"}, "w": "β = 180° − 65° = 115° (benachbart), γ = α = 65° (gegenüber).", "o": {"werte": [115, 65]}}]$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  raise notice 'Einheit % (vierecke): % von 3 Aufgaben eingefügt (0 = schon vorhanden)', v_e, v_n;
  if v_n not in (0, 3) then raise exception 'Etappe vierecke: nur % von 3 eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
end $nt$;

-- Thema 44 (geometrie.konstruktion), Etappe vierecke_konstruieren: 3 Aufgaben (sicherung)
do $nt$
declare v_e bigint; v_max int; v_auf jsonb; v_n int; v_stamm boolean;
begin
  v_stamm := exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm');
  -- Einheit mit dieser Etappe im Katalog: vor der Teilung die Einheit des Themas, danach die des richtigen Teils
  execute format('select e.id from schule.einheit e join schule.thema t on t.id = e.thema_id
                   where e.status <> %L and (t.id = $1 %s)
                     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->%L, %L::jsonb)) x where x->>%L = $2)
                   order by e.id limit 1', 'ersetzt', case when v_stamm then 'or t.teil_stamm = $1' else '' end, 'etappen', '[]', 'lernziel')
    into v_e using 44::bigint, 'vierecke_konstruieren'::text;
  if v_e is null then raise exception 'Thema 44: keine Einheit mit Etappe vierecke_konstruieren – zuerst lk_einspiel_2211.sql einspielen'; end if;
  if (select schluessel from schule.thema where id = 44) <> 'geometrie.konstruktion' then raise exception 'Thema 44 ist nicht geometrie.konstruktion'; end if;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j$[{"l": "vierecke_konstruieren", "t": "vierecke_konstruieren", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Ein Viereck hat die Winkel 100°, 75° und 80°. Berechne den vierten Winkel."}, "w": "Die Winkelsumme im Viereck ist 360°: 360° − 100° − 75° − 80° = 105°.", "o": {"wert": 105, "einheit": "°"}}, {"l": "vierecke_konstruieren", "t": "vierecke_konstruieren", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Ein Trapez ABCD hat AB ∥ CD und α = 70°. Wie groß ist δ?"}, "w": "α und δ liegen am selben Schenkel AD zwischen den Parallelen und ergänzen sich zu 180°: δ = 110°.", "o": {"wert": 110, "einheit": "°"}}, {"l": "vierecke_konstruieren", "t": "vierecke_konstruieren", "p": "sicherung", "s": 2, "y": "auswahl", "f": {"text": "Welche Angaben legen ein Rechteck eindeutig fest?"}, "w": "Alle Winkel eines Rechtecks sind 90°. Mit zwei benachbarten Seitenlängen ist es eindeutig konstruierbar.", "a": ["ein Winkel", "eine Seitenlänge", "zwei benachbarte Seitenlängen", "zwei gegenüberliegende Seitenlängen"], "o": {"index": 2}}]$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  raise notice 'Einheit % (vierecke_konstruieren): % von 3 Aufgaben eingefügt (0 = schon vorhanden)', v_e, v_n;
  if v_n not in (0, 3) then raise exception 'Etappe vierecke_konstruieren: nur % von 3 eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
end $nt$;

-- Thema 30 (terme.potenzgesetze), Etappe potenz_begriff: 3 Aufgaben (sicherung)
do $nt$
declare v_e bigint; v_max int; v_auf jsonb; v_n int; v_stamm boolean;
begin
  v_stamm := exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm');
  -- Einheit mit dieser Etappe im Katalog: vor der Teilung die Einheit des Themas, danach die des richtigen Teils
  execute format('select e.id from schule.einheit e join schule.thema t on t.id = e.thema_id
                   where e.status <> %L and (t.id = $1 %s)
                     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->%L, %L::jsonb)) x where x->>%L = $2)
                   order by e.id limit 1', 'ersetzt', case when v_stamm then 'or t.teil_stamm = $1' else '' end, 'etappen', '[]', 'lernziel')
    into v_e using 30::bigint, 'potenz_begriff'::text;
  if v_e is null then raise exception 'Thema 30: keine Einheit mit Etappe potenz_begriff – zuerst lk_einspiel_2211.sql einspielen'; end if;
  if (select schluessel from schule.thema where id = 30) <> 'terme.potenzgesetze' then raise exception 'Thema 30 ist nicht terme.potenzgesetze'; end if;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j$[{"l": "potenz_begriff", "t": "potenz_begriff", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Berechne (−3)³."}, "w": "(−3)³ = (−3) · (−3) · (−3) = −27. Drei Minuszeichen: ungerade Anzahl, also negativ.", "o": {"wert": -27}}, {"l": "potenz_begriff", "t": "potenz_begriff", "p": "sicherung", "s": 2, "y": "auswahl", "f": {"text": "Was bedeutet 5⁴?"}, "w": "Die Hochzahl gibt an, wie oft die Basis mit sich selbst malgenommen wird: 5⁴ = 5 · 5 · 5 · 5 = 625.", "a": ["5 · 5 · 5 · 5", "5 · 4", "4 · 4 · 4 · 4 · 4", "5 + 5 + 5 + 5"], "o": {"index": 0}}, {"l": "potenz_begriff", "t": "potenz_begriff", "p": "sicherung", "s": 2, "y": "luecken", "f": {"text": "Berechne (3/4)².", "schablone": "□/□", "hinweis": "Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt."}, "w": "Zähler und Nenner quadrieren: 3² / 4² = 9/16.", "o": {"werte": [9, 16]}}]$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  raise notice 'Einheit % (potenz_begriff): % von 3 Aufgaben eingefügt (0 = schon vorhanden)', v_e, v_n;
  if v_n not in (0, 3) then raise exception 'Etappe potenz_begriff: nur % von 3 eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
end $nt$;

-- Thema 30 (terme.potenzgesetze), Etappe negativer_exponent: 2 Aufgaben (sicherung)
do $nt$
declare v_e bigint; v_max int; v_auf jsonb; v_n int; v_stamm boolean;
begin
  v_stamm := exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm');
  -- Einheit mit dieser Etappe im Katalog: vor der Teilung die Einheit des Themas, danach die des richtigen Teils
  execute format('select e.id from schule.einheit e join schule.thema t on t.id = e.thema_id
                   where e.status <> %L and (t.id = $1 %s)
                     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->%L, %L::jsonb)) x where x->>%L = $2)
                   order by e.id limit 1', 'ersetzt', case when v_stamm then 'or t.teil_stamm = $1' else '' end, 'etappen', '[]', 'lernziel')
    into v_e using 30::bigint, 'negativer_exponent'::text;
  if v_e is null then raise exception 'Thema 30: keine Einheit mit Etappe negativer_exponent – zuerst lk_einspiel_2211.sql einspielen'; end if;
  if (select schluessel from schule.thema where id = 30) <> 'terme.potenzgesetze' then raise exception 'Thema 30 ist nicht terme.potenzgesetze'; end if;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j$[{"l": "negativer_exponent", "t": "negativer_exponent", "p": "sicherung", "s": 2, "y": "zahl", "f": {"text": "Schreibe 10⁻³ als Dezimalzahl."}, "w": "10⁻³ = 1/10³ = 1/1 000 = 0,001.", "o": {"wert": 0.001}}, {"l": "negativer_exponent", "t": "negativer_exponent", "p": "sicherung", "s": 2, "y": "luecken", "f": {"text": "Berechne 4⁻².", "schablone": "□/□", "hinweis": "Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt."}, "w": "4⁻² = 1/4² = 1/16.", "o": {"werte": [1, 16]}}]$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  raise notice 'Einheit % (negativer_exponent): % von 2 Aufgaben eingefügt (0 = schon vorhanden)', v_e, v_n;
  if v_n not in (0, 2) then raise exception 'Etappe negativer_exponent: nur % von 2 eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
end $nt$;

-- Thema 57 (daten.darstellen), Etappe irrefuehrend: 9 Aufgaben (uebung)
do $nt$
declare v_e bigint; v_max int; v_auf jsonb; v_n int; v_stamm boolean;
begin
  v_stamm := exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm');
  -- Einheit mit dieser Etappe im Katalog: vor der Teilung die Einheit des Themas, danach die des richtigen Teils
  execute format('select e.id from schule.einheit e join schule.thema t on t.id = e.thema_id
                   where e.status <> %L and (t.id = $1 %s)
                     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->%L, %L::jsonb)) x where x->>%L = $2)
                   order by e.id limit 1', 'ersetzt', case when v_stamm then 'or t.teil_stamm = $1' else '' end, 'etappen', '[]', 'lernziel')
    into v_e using 57::bigint, 'irrefuehrend'::text;
  if v_e is null then raise exception 'Thema 57: keine Einheit mit Etappe irrefuehrend – zuerst lk_einspiel_2211.sql einspielen'; end if;
  if (select schluessel from schule.thema where id = 57) <> 'daten.darstellen' then raise exception 'Thema 57 ist nicht daten.darstellen'; end if;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j$[{"l": "irrefuehrend", "t": "irrefuehrend", "p": "uebung", "s": 1, "y": "zahl", "f": {"text": "Du zeichnest ein Säulendiagramm richtig neu: Die Hochachse beginnt bei 0, 1 cm steht für 10 Stimmen. Wie hoch wird die Säule für 40 Stimmen?"}, "w": "40 : 10 = 4, also 4 cm. Weil die Achse bei 0 beginnt, sind die Höhen echt vergleichbar.", "g": "direkt", "h": "Teile den Wert durch 10.", "o": {"wert": 4, "einheit": "cm"}}, {"l": "irrefuehrend", "t": "irrefuehrend", "p": "uebung", "s": 1, "y": "auswahl", "f": {"text": "Die Hochachse eines Säulendiagramms beginnt bei 90, die Werte sind 92 und 98. Wie verbesserst du das Diagramm?"}, "w": "Damit die Säulenhöhen den Werten entsprechen, muss die Achse bei 0 beginnen – oder die Lücke muss deutlich mit einem Achsenbruch markiert werden.", "g": "erkennen", "h": "Wo muss eine Hochachse beginnen?", "a": ["Die Achse bei 0 beginnen lassen.", "Die Säulen breiter machen.", "Die Werte runden.", "Die Säulen farbig machen."], "o": {"index": 0}}, {"l": "irrefuehrend", "t": "irrefuehrend", "p": "uebung", "s": 2, "y": "luecken", "f": {"text": "Zeichne ehrlich neu: Die Achse beginnt bei 0, 1 cm steht für 30 Stück. Wie hoch werden die Säulen für 120 und 150 Stück?", "schablone": "□ cm und □ cm", "hinweis": "je eine ganze Zahl"}, "w": "120 : 30 = 4 cm und 150 : 30 = 5 cm. Jetzt ist die zweite Säule nur 1/4 höher – genau wie die Werte.", "g": "mehrschritt", "h": "Teile jeden Wert durch 30.", "o": {"werte": [4, 5]}}, {"l": "irrefuehrend", "t": "irrefuehrend", "p": "uebung", "s": 2, "y": "zahl", "f": {"text": "Auf einer Zeitachse stehen 2010, 2015, 2016 und 2020 in gleichen Abständen von 5 cm. Richtig wäre 1 cm pro Jahr. Wie lang muss der Abstand von 2015 bis 2016 werden?"}, "w": "Zwischen 2015 und 2016 liegt ein Jahr, also 1 cm (statt 5 cm). Gleiche Abstände für ungleiche Zeiträume verzerren den Verlauf.", "g": "einkleidung", "h": "Wie viele Jahre liegen dazwischen?", "o": {"wert": 1, "einheit": "cm"}}, {"l": "irrefuehrend", "t": "irrefuehrend", "p": "uebung", "s": 2, "y": "auswahl", "f": {"text": "In einem Bilddiagramm soll Laden B doppelt so viel verkaufen wie Laden A. Wie stellst du das ehrlich dar?"}, "w": "Doppelt so viele gleich große Symbole verdoppeln die Fläche genau. Ein Symbol mit doppelter Höhe und Breite hätte die vierfache Fläche.", "g": "darstellung", "h": "Achte auf die Fläche der Bilder.", "a": ["Das Symbol von B wird doppelt so hoch und doppelt so breit.", "B bekommt doppelt so viele gleich große Symbole.", "Das Symbol von B wird dreimal so groß.", "B bekommt eine andere Farbe."], "o": {"index": 1}}, {"l": "irrefuehrend", "t": "irrefuehrend", "p": "uebung", "s": 3, "y": "zahl", "f": {"text": "Lea verbessert ein Diagramm: Achse ab 0, Säule A (80 Punkte) ist 4 cm hoch. Säule B (90 Punkte) zeichnet sie 6 cm hoch. Wie hoch muss B richtig sein?"}, "w": "4 cm stehen für 80, also 1 cm für 20. 90 : 20 = 4,5 cm. Leas 6 cm übertreiben den Unterschied.", "g": "fehler", "h": "Wie viele Punkte stehen für 1 cm?", "o": {"wert": 4.5, "einheit": "cm"}}, {"l": "irrefuehrend", "t": "irrefuehrend", "p": "uebung", "s": 3, "y": "zahl", "f": {"text": "In einem Kreisdiagramm ist ein Anteil von 25 % als Sektor mit 120° gezeichnet. Mit welchem Winkel ist er richtig?"}, "w": "25 % von 360° sind 90°. Der gezeichnete Sektor mit 120° ist zu groß.", "g": "transfer", "h": "Der ganze Kreis hat 360°.", "o": {"wert": 90, "einheit": "°"}}, {"l": "irrefuehrend", "t": "irrefuehrend", "p": "uebung", "s": 3, "y": "auswahl", "f": {"text": "Warum ist ein schräg gekipptes 3D-Kreisdiagramm oft irreführend, und wie verbesserst du es?"}, "w": "Durch das Kippen wirken die vorderen Stücke größer als die hinteren. Ein flaches Kreisdiagramm zeigt die Anteile unverzerrt.", "g": "begruenden", "h": "Welche Stücke sieht man größer?", "a": ["Es hat zu viele Farben – besser grau zeichnen.", "Es ist zu klein – besser größer zeichnen.", "Vordere Stücke wirken größer – besser flach zeichnen.", "Es fehlt eine Hochachse – besser eine ergänzen."], "o": {"index": 2}}, {"l": "irrefuehrend", "t": "irrefuehrend", "p": "uebung", "s": 3, "y": "zahl", "f": {"text": "In einem ehrlich gezeichneten Säulendiagramm steht 1 cm für 20 €. Eine Säule ist 7,5 cm hoch. Welchen Wert zeigt sie?"}, "w": "7,5 · 20 € = 150 €.", "g": "rueckwaerts", "h": "Multipliziere die Höhe mit dem Wert für 1 cm.", "o": {"wert": 150, "einheit": "€"}}]$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  raise notice 'Einheit % (irrefuehrend): % von 9 Aufgaben eingefügt (0 = schon vorhanden)', v_e, v_n;
  if v_n not in (0, 9) then raise exception 'Etappe irrefuehrend: nur % von 9 eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
end $nt$;

-- Rauchtest (liest nur)
do $pruef$
declare v int;
begin
  select count(*) into v from schule.aufgabe a where (a.variante_gruppe = 'punktspiegelung' and a.frage->>'text' in ('Spiegle den Punkt P(5 | 1) am Zentrum Z(2 | 3).', 'Spiegle den Punkt P(−3 | 4) am Zentrum Z(1 | −1).', 'Spiegle den Punkt P(0 | −5) am Zentrum Z(−2 | 0).', 'Spiegle den Punkt P(7 | −2) am Zentrum Z(3 | 1).', 'Spiegle den Punkt P(−6 | −3) am Zentrum Z(−1 | −2).', 'P(2 | 5) wird an Z gespiegelt und landet bei P''(8 | −1). Welche x-Koordinate hat Z?', 'P(−4 | 3) und P''(6 | −7) liegen punktsymmetrisch zu Z. Welche y-Koordinate hat Z?', 'Eine Strecke AB wird an einem Punkt Z gespiegelt. Wie liegt die Bildstrecke A''B'' zu AB?', 'Welche dieser Figuren ist immer punktsymmetrisch?')) or (a.variante_gruppe = 'rotation' and a.frage->>'text' in ('Ein Rechteck mit den Seiten 5 cm und 8 cm dreht sich um die 5-cm-Seite. Welchen Radius hat der entstehende Zylinder?', 'Ein Halbkreis dreht sich um seinen Durchmesser. Welcher Körper entsteht?', 'Ein rechtwinkliges Dreieck mit den Katheten 4 cm und 10 cm dreht sich um die 10-cm-Kathete. Gib Radius und Höhe des Kegels an.')) or (a.variante_gruppe = 'axialschnitt' and a.frage->>'text' in ('Ein Zylinder hat r = 6 cm und h = 10 cm. Wie groß ist der Flächeninhalt seines Axialschnitts?', 'Welche Form hat der Axialschnitt eines geraden Kreiskegels?', 'Ein Zylinder hat r = 3 cm und h = 7 cm. Welche Seitenlängen hat das Rechteck des Axialschnitts?')) or (a.variante_gruppe = 'cavalieri' and a.frage->>'text' in ('Ein schiefes Prisma hat die Grundfläche G = 18 cm² und die Höhe h = 4 cm. Berechne sein Volumen.', 'Ein schiefes Prisma hat die Grundfläche G = 25 cm² und die Höhe h = 6 cm. Berechne sein Volumen.', 'Ein schiefes Prisma hat die Grundfläche G = 9 cm² und die Höhe h = 11 cm. Berechne sein Volumen.', 'Ein schiefer Zylinder hat das Volumen 96 cm³ und die Grundfläche 12 cm². Wie hoch ist er?', 'Ein schiefer Zylinder hat das Volumen 150 cm³ und die Grundfläche 25 cm². Wie hoch ist er?', 'Zwei Körper haben in jeder Höhe gleich große Querschnittsflächen und sind gleich hoch. Was folgt nach Cavalieri?', 'Ein Stapel Münzen wird schräg geschoben. Was bleibt gleich?', 'Ein gerades und ein schiefes Prisma haben beide G = 14 cm² und die Höhe 5 cm. Berechne beide Volumen.', 'Ein schiefer Zylinder hat den Radius 2 cm und die Höhe 9 cm. Schreibe sein Volumen als Vielfaches von π.')) or (a.variante_gruppe = 'vierecke' and a.frage->>'text' in ('In einem Parallelogramm ist α = 70°. Wie groß ist β?', 'In welchem Viereck stehen die Diagonalen immer senkrecht aufeinander und halbieren sich?', 'In einem Parallelogramm ABCD ist α = 65°. Berechne β und γ.')) or (a.variante_gruppe = 'vierecke_konstruieren' and a.frage->>'text' in ('Ein Viereck hat die Winkel 100°, 75° und 80°. Berechne den vierten Winkel.', 'Ein Trapez ABCD hat AB ∥ CD und α = 70°. Wie groß ist δ?', 'Welche Angaben legen ein Rechteck eindeutig fest?')) or (a.variante_gruppe = 'potenz_begriff' and a.frage->>'text' in ('Berechne (−3)³.', 'Was bedeutet 5⁴?', 'Berechne (3/4)².')) or (a.variante_gruppe = 'negativer_exponent' and a.frage->>'text' in ('Schreibe 10⁻³ als Dezimalzahl.', 'Berechne 4⁻².')) or (a.variante_gruppe = 'irrefuehrend' and a.frage->>'text' in ('Du zeichnest ein Säulendiagramm richtig neu: Die Hochachse beginnt bei 0, 1 cm steht für 10 Stimmen. Wie hoch wird die Säule für 40 Stimmen?', 'Die Hochachse eines Säulendiagramms beginnt bei 90, die Werte sind 92 und 98. Wie verbesserst du das Diagramm?', 'Zeichne ehrlich neu: Die Achse beginnt bei 0, 1 cm steht für 30 Stück. Wie hoch werden die Säulen für 120 und 150 Stück?', 'Auf einer Zeitachse stehen 2010, 2015, 2016 und 2020 in gleichen Abständen von 5 cm. Richtig wäre 1 cm pro Jahr. Wie lang muss der Abstand von 2015 bis 2016 werden?', 'In einem Bilddiagramm soll Laden B doppelt so viel verkaufen wie Laden A. Wie stellst du das ehrlich dar?', 'Lea verbessert ein Diagramm: Achse ab 0, Säule A (80 Punkte) ist 4 cm hoch. Säule B (90 Punkte) zeichnet sie 6 cm hoch. Wie hoch muss B richtig sein?', 'In einem Kreisdiagramm ist ein Anteil von 25 % als Sektor mit 120° gezeichnet. Mit welchem Winkel ist er richtig?', 'Warum ist ein schräg gekipptes 3D-Kreisdiagramm oft irreführend, und wie verbesserst du es?', 'In einem ehrlich gezeichneten Säulendiagramm steht 1 cm für 20 €. Eine Säule ist 7,5 cm hoch. Welchen Wert zeigt sie?'));
  if v <> 44 then raise exception 'Rauchtest NT-D: % von 44 Aufgaben', v; end if;
  raise notice 'Rauchtest NT-D bestanden: 44 Aufgaben (35 Sicherung)';
end $pruef$;
