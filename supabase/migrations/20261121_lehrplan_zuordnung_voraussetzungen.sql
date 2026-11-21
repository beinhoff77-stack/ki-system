-- Dreißigste Runde (21.11.): Lehrplan-Prüfung – Zuordnungen und Voraussetzungen der Themenliste.
-- Quelle: LehrplanPLUS Bayern, abgerufen 21.11.2026; Belege und Annahmen in inhalte/pruefung/lehrplan/runde30.md.
-- Wiederholt ausführbar. Kein DROP, kein DELETE. Fehlen die Themen 102/103, werden ihre Verbindungen übersprungen.
-- Am Ende ein Rauchtest (nur lesen); schlägt er fehl, bricht die Migration mit Fehlermeldung ab.

-- 0) Vergleichsstand für den Rauchtest (Runde 30 c): Reiseoptionen aller Lernenden und Zahl der Visum-Zeilen VOR den Änderungen, nur gelesen und in einer Sitzungs-Einstellung gemerkt.
do $$ begin
  perform set_config('lb30.ro_vorher', coalesce((select jsonb_object_agg(id::text, schule.reiseoptionen(id)) from schule.lernender), '{}'::jsonb)::text, false);
  perform set_config('lb30.visum_vorher', (select count(*) from schule.v_ort_visum)::text, false);
end $$;

-- 1) Kleinste Erweiterung: Kennzeichen „eigenständig“ (Begründung; nicht leer = bewusst ohne Voraussetzung)
alter table schule.thema add column if not exists eigenstaendig text;
comment on column schule.thema.eigenstaendig is 'Begründung, warum das Thema bewusst keine Voraussetzung hat (Dreißigste Runde)';

-- 2) entfällt (Runde 30 b): Thema 12 bekommt keine Gymnasium-Klasse; es ist für das Gymnasium aufgelöst (Etappe reinquadratisch in 8). Reihenfolge Gym 9 bleibt unverändert.

-- 3) Formeln umstellen (4): Lernbereich Gymnasium berichtigt (M8 1 statt M8 4); Reihenfolge bleibt
update schule.thema set lernbereich = coalesce(lernbereich,'{}'::jsonb) || '{"gym_by": "M8 1 Funktion und Term"}'::jsonb where id = 4;

-- 3b) Zuordnung und Funktion (32) im IB nach MYP 3 vor Lineare Funktionen (33), weil 33 hart auf 32 aufbaut (Annahme)
update schule.thema set klasse_fest = coalesce(klasse_fest,'{}'::jsonb) || '{"ib_myp": 3}'::jsonb,
  lernbereich = coalesce(lernbereich,'{}'::jsonb) || '{"ib_myp": "MYP 3 Thinking with models (Funktionen und Modelle)"}'::jsonb,
  lehrplan = coalesce(lehrplan,'{}'::jsonb) || jsonb_build_object('ib_myp', 'Annahme: Zuordnungen schon in MYP 3 vor linearen Funktionen (harte Voraussetzung); Funktionsschreibweise, Definitions- und Wertebereich laut Framework MYP 4–5')
where id = 32;
-- Reihenfolge IB MYP 3 und MYP 4 lückenlos neu
update schule.thema t set lehrplan_reihenfolge = coalesce(t.lehrplan_reihenfolge,'{}'::jsonb) || jsonb_build_object('ib_myp', v.rf)
from (values (30, 1), (102, 2), (29, 3), (94, 4), (32, 5), (33, 6), (46, 7), (44, 8), (51, 9), (52, 10), (92, 11), (47, 12), (54, 13), (83, 14), (103, 1), (19, 2), (20, 3), (69, 4), (3, 5), (4, 6), (31, 7), (5, 8), (93, 9), (12, 10), (8, 11), (9, 12), (71, 13), (72, 14), (84, 15), (6, 16), (35, 17), (36, 18), (34, 19), (65, 20), (55, 21), (56, 22), (45, 23), (91, 24), (95, 25), (63, 26), (62, 27)) v(id, rf)
where t.id = v.id;

-- 3c) Veraltete Verbindungen von und zu aufgelösten Themen (Entwurf ohne freigegebene Einheit) gezielt löschen.
-- Einzige Ausnahme vom Lösch-Verbot (Auftrag „Nachbesserung Dreißigste Runde“, Teil A). Jede Zeile einzeln, nur genau dieses Paar.
-- 8 Quadratische Gleichungen (allgemein) ← 12 Reinquadratische Gleichungen: Quadratische Gleichungen braucht 12: Stoff steht jetzt als Etappe reinquadratisch in 8 selbst; ersetzt durch 8 ← 68
delete from schule.voraussetzung where thema_id = 8 and braucht_id = 12;
-- 12 Reinquadratische Gleichungen ← 68 Elementare Wurzeln: 12 ist aufgelöst (Entwurf ohne freigegebene Einheit)
delete from schule.voraussetzung where thema_id = 12 and braucht_id = 68;
-- 49 Matrizen und Abbildungen mit Matrizen ← 48 Vektoren und Determinanten: Matrizen braucht 48: Vektor-Flug aufgelöst; ersetzt durch 49 ← 46
delete from schule.voraussetzung where thema_id = 49 and braucht_id = 48;
-- 74 Zweireihige Determinanten ← 48 Vektoren und Determinanten: Determinanten brauchen 48: Vektor-Flug aufgelöst; ersetzt durch 74 ← 46 und 74 ← 50
delete from schule.voraussetzung where thema_id = 74 and braucht_id = 48;
-- 76 Reihen ← 41 Folgen: Reihen braucht 41: Folgen stehen jetzt als Etappen in 76; ersetzt durch 76 ← 28
delete from schule.voraussetzung where thema_id = 76 and braucht_id = 41;
-- 72 Zinseszins ← 67 Potenzen als Schreibweise: 72 ist aufgelöst (Stoff in 94 und 37)
delete from schule.voraussetzung where thema_id = 72 and braucht_id = 67;
-- 72 Zinseszins ← 71 Zinsen: 72 ist aufgelöst (Stoff in 94 und 37)
delete from schule.voraussetzung where thema_id = 72 and braucht_id = 71;
-- 77 Umkehrfunktionen ← 32 Zuordnung und Funktion: 77 ist aufgelöst (Stoff in 36)
delete from schule.voraussetzung where thema_id = 77 and braucht_id = 32;
-- 78 Parameter und Funktionenscharen ← 33 Lineare Funktionen: 78 ist aufgelöst (Stoff in 33 und 6)
delete from schule.voraussetzung where thema_id = 78 and braucht_id = 33;
-- 82 Bedingte Wahrscheinlichkeit ← 21 Brüche und Anteile: 82 ist aufgelöst (Stoff in 63 und 62)
delete from schule.voraussetzung where thema_id = 82 and braucht_id = 21;
-- 82 Bedingte Wahrscheinlichkeit ← 23 Rechnen mit rationalen Zahlen: 82 ist aufgelöst (Stoff in 63 und 62)
delete from schule.voraussetzung where thema_id = 82 and braucht_id = 23;
-- 82 Bedingte Wahrscheinlichkeit ← 61 Zufall und Laplace: 82 ist aufgelöst (Stoff in 63 und 62)
delete from schule.voraussetzung where thema_id = 82 and braucht_id = 61;

-- 4) Voraussetzungen (nur einfügen oder Art/Begründung angleichen; vorhandene bleiben)
insert into schule.voraussetzung (thema_id, braucht_id, art, begruendung)
select v.t, v.b, v.art, v.beg from (values
  (8, 68, 'hart', 'Etappe reinquadratisch: x² = a mit der Quadratwurzel lösen (Stoff von 12 steht jetzt hier)'),
  (49, 46, 'empfohlen', 'Verschiebung und Gegenvektor aus den Kongruenzabbildungen (ersetzt 48)'),
  (74, 46, 'empfohlen', 'Verschiebung und Gegenvektor aus den Kongruenzabbildungen (ersetzt 48)'),
  (74, 50, 'empfohlen', 'Determinanten berechnen Flächeninhalte von Parallelogramm und Dreieck'),
  (76, 28, 'empfohlen', 'Term für das n-te Glied (Folgen stehen jetzt in diesem Flug, ersetzt 41)'),
  (2, 28, 'hart', 'Gleichungen bestehen aus Termen mit Variablen'),
  (2, 16, 'empfohlen', 'Lösungen und Umformungen mit negativen Zahlen'),
  (4, 29, 'empfohlen', 'beim Umstellen werden Terme umgeformt'),
  (6, 33, 'empfohlen', 'graphisches Lösen über den Schnittpunkt zweier Geraden'),
  (11, 39, 'empfohlen', 'Nullstellen ganzrationaler Funktionen = Lösungen der Polynomgleichung'),
  (13, 8, 'empfohlen', 'Wurzelgleichungen führen oft auf quadratische Gleichungen'),
  (17, 18, 'empfohlen', 'Teiler und Vielfache beruhen auf Multiplizieren und Dividieren'),
  (18, 15, 'hart', 'Rechnen im Stellenwertsystem mit natürlichen Zahlen'),
  (19, 67, 'hart', 'Potenzbegriff: Basis und Exponent'),
  (19, 22, 'empfohlen', 'kleine Zahlen als Dezimalzahl und als Zehnerpotenz'),
  (20, 68, 'hart', 'Quadratwurzel als Grundbegriff'),
  (21, 18, 'empfohlen', 'Bruch als Teilen; Kürzen und Erweitern durch Multiplizieren und Dividieren'),
  (21, 17, 'empfohlen', 'Kürzen mit gemeinsamen Teilern'),
  (22, 21, 'empfohlen', 'Dezimalzahlen als Zehnerbrüche'),
  (23, 22, 'empfohlen', 'rationale Zahlen auch als Dezimalzahlen'),
  (23, 16, 'empfohlen', 'Vorzeichenregeln der ganzen Zahlen'),
  (24, 22, 'empfohlen', 'Prozentsätze als Dezimalzahl'),
  (25, 18, 'empfohlen', 'Umrechnen durch Multiplizieren und Dividieren mit 10, 100, 1000'),
  (28, 18, 'empfohlen', 'Rechenarten und Rechengesetze in Termen'),
  (29, 102, 'hart', 'Produkte wie a · a² · a³ brauchen das Potenzgesetz'),
  (30, 21, 'empfohlen', 'negativer Exponent bedeutet Kehrbruch'),
  (31, 29, 'hart', 'Zähler und Nenner werden als Terme umgeformt'),
  (34, 32, 'empfohlen', 'Funktionsbegriff, Definitionsmenge'),
  (34, 93, 'empfohlen', 'indirekte Proportionalität führt auf die Hyperbel'),
  (36, 35, 'empfohlen', 'Parabel als erste Potenzfunktion'),
  (37, 103, 'empfohlen', 'Potenzgesetze mit ganzzahligen Exponenten'),
  (43, 42, 'empfohlen', 'Strahl, Scheitel und Gerade'),
  (44, 43, 'empfohlen', 'Winkel messen und zeichnen'),
  (44, 98, 'empfohlen', 'Winkelsumme bei Existenz und Konstruktion von Dreiecken'),
  (44, 46, 'empfohlen', 'Grundkonstruktionen (Mittelsenkrechte, Lot, Winkelhalbierende)'),
  (45, 42, 'empfohlen', 'Kreis, Radius, Gerade'),
  (45, 98, 'empfohlen', 'Satz des Thales wird über die Winkelsumme im Dreieck begründet'),
  (45, 73, 'empfohlen', 'Umkreis und Inkreis über Mittelsenkrechte und Winkelhalbierende'),
  (46, 42, 'empfohlen', 'Gerade, Senkrechte, Koordinatensystem'),
  (50, 42, 'empfohlen', 'Rechteck, Quadrat und Vielecke'),
  (52, 42, 'empfohlen', 'ebene Figuren für Netze und Seitenflächen'),
  (55, 54, 'empfohlen', 'fehlende Seiten mit Pythagoras'),
  (58, 22, 'empfohlen', 'Mittelwerte sind oft Dezimalzahlen'),
  (59, 57, 'empfohlen', 'Daten erfassen und darstellen'),
  (59, 33, 'empfohlen', 'Trendgerade als lineare Funktion'),
  (64, 61, 'hart', 'Zufallsexperiment und relative Häufigkeit'),
  (66, 3, 'empfohlen', 'Bedingungen als lineare Ungleichungen'),
  (66, 33, 'empfohlen', 'Randgeraden zeichnen'),
  (67, 18, 'hart', 'Potenz als wiederholtes Multiplizieren'),
  (68, 67, 'empfohlen', 'Quadratzahlen'),
  (69, 16, 'empfohlen', 'Zahlengerade mit negativen Zahlen'),
  (70, 22, 'empfohlen', 'Runden von Dezimalzahlen'),
  (73, 42, 'hart', 'Kreis, Gerade, Abstand'),
  (75, 32, 'empfohlen', 'Funktionsbegriff'),
  (75, 16, 'empfohlen', 'Betrag einer ganzen Zahl'),
  (81, 57, 'empfohlen', 'Daten erheben und darstellen'),
  (81, 58, 'empfohlen', 'Kenngrößen zum Vergleich von Stichproben'),
  (92, 101, 'empfohlen', 'Pyramide und Kegel im Vergleich zu Prisma und Zylinder'),
  (98, 43, 'empfohlen', 'Winkel messen, Scheitel- und Nebenwinkel'),
  (99, 50, 'empfohlen', 'Flächeninhalt von Rechteck und Quadrat; Zerlegen'),
  (100, 50, 'empfohlen', 'Grundfläche des Quaders'),
  (100, 25, 'empfohlen', 'Einheiten umrechnen'),
  (101, 99, 'empfohlen', 'Grundflächen Dreieck, Trapez, Parallelogramm'),
  (101, 100, 'empfohlen', 'Volumenbegriff und Volumeneinheiten'),
  (101, 51, 'empfohlen', 'Kreisfläche und -umfang für den Zylinder'),
  (102, 30, 'hart', 'Potenzbegriff (Basis, Exponent, Hoch 0)'),
  (102, 28, 'hart', 'Terme mit Variablen'),
  (103, 102, 'hart', 'Potenzgesetze mit natürlichen Exponenten'),
  (103, 30, 'empfohlen', 'negative Exponenten als Kehrbruch'),
  (96, 103, 'empfohlen', 'Potenzgesetze werden auf rationale Exponenten erweitert')
) v(t, b, art, beg)
where exists (select 1 from schule.thema where id = v.t) and exists (select 1 from schule.thema where id = v.b)
on conflict (thema_id, braucht_id) do update set art = excluded.art, begruendung = excluded.begruendung;
update schule.voraussetzung set begruendung = 'Potenzbegriff und negative Exponenten' where thema_id = 96 and braucht_id = 30;

-- 5) Eigenständige Themen
update schule.thema t set eigenstaendig = v.g from (values
  (15, 'Einstieg Klasse 5; setzt nur Grundschulwissen voraus'),
  (42, 'Einstieg Geometrie Klasse 5; setzt nur Grundschulwissen voraus'),
  (57, 'Zählen und Ablesen aus der Grundschule genügen'),
  (60, 'systematisches Zählen; setzt nur Grundschulwissen voraus'),
  (65, 'Entdecker-Insel mit eigenen Begriffen (Knoten, Kanten)'),
  (83, 'Entdecker-Insel; Mengenbegriff wird hier eingeführt'),
  (84, 'Entdecker-Insel; Aussagen und Wahrheitswerte werden hier eingeführt')
) v(id, g) where t.id = v.id and t.eigenstaendig is distinct from v.g;

-- 6) Rauchtest (liest nur)
do $$
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
    select string_agg('Lernender ' || k || ': vorher ' || coalesce(vorher->k, 'null'::jsonb)::text || ' / nachher ' || coalesce(nachher->k, 'null'::jsonb)::text, E'
') into v_txt
      from (select current_setting('lb30.ro_vorher')::jsonb vorher,
                   coalesce((select jsonb_object_agg(id::text, schule.reiseoptionen(id)) from schule.lernender), '{}'::jsonb) nachher) x,
           lateral (select jsonb_object_keys(vorher) k union select jsonb_object_keys(nachher)) ks
     where coalesce(vorher->k, 'null'::jsonb) is distinct from coalesce(nachher->k, 'null'::jsonb);
    if v_txt is not null then raise exception E'Rauchtest j: Reiseoptionen geändert:
%', v_txt; end if;
    raise notice 'Rauchtest j: Reiseoptionen unverändert; v_ort_visum vorher % Zeilen, nachher %', current_setting('lb30.visum_vorher', true), (select count(*) from schule.v_ort_visum);
  end if;
  -- f) Lernbereich 4 berichtigt
  if (select lernbereich->>'gym_by' from schule.thema where id = 4) <> 'M8 1 Funktion und Term' then raise exception 'Rauchtest: Lernbereich 4'; end if;
  raise notice 'Rauchtest Dreißigste Runde bestanden';
end $$;
