-- Nacharbeit aus ChatGPTs Prüfergebnis 907 (22.11.) zur Dreißigsten Runde (Lehrplan-Zuordnungen und Voraussetzungen).
-- Fassung c (22.11., ChatGPT 919 MUSS 4): Löschschutz auch für Einheiten im Status geprueft (für Kinder sichtbar), Rauchtest m;
-- Rauchtest l nur für die zehn stillgelegten Themen; Regeln b und i zählen geprueft wie freigegeben.
-- Fassung b (22.11. abends): Test-Lernender ohne feste id (ids GENERATED ALWAYS), N2 aufgelöste Themen ohne RS/IB-Klasse und
-- -Reihenfolge (Abschnitt 3d, Rauchtest l), N3 „eigenständig“ für 83 entfernt.
-- Ersetzt die eingespielte Datei 20261121_lehrplan_zuordnung_voraussetzungen.sql NICHT, sondern ist ihre berichtigte Fassung:
-- gleicher Inhalt (Runden 30, 30 b, 30 c; 102 ← 30 bleibt hart, Entscheidung des Nutzers), dazu
--   * Rauchtest j: fehlt der Vorherstand der Reiseoptionen, bricht er mit EXCEPTION ab (statt still zu überspringen);
--   * vor jeder gezielten Löschung (Abschnitt 3c) wird geprüft, dass das aufgelöste Thema keine für Kinder sichtbare Einheit
--     (geprueft oder freigegeben) hat, sonst Abbruch;
--   * Rauchtest k: Testfall „Zielort offen, Voraussetzungs-Ort fehlt“ für die harte Kante 102 ← 30 (mit einem erfundenen Test-Lernenden,
--     der in einem Unterblock angelegt und sofort wieder zurückgerollt wird; keine echten Kinderdaten).
-- Quelle: LehrplanPLUS Bayern, abgerufen 21.11.2026; Belege und Annahmen in inhalte/pruefung/lehrplan/runde30.md.
-- Wiederholt ausführbar und in EINER Transaktion einzuspielen: Abschnitt 0 merkt den Vorherstand transaktionslokal (set_config … true);
-- ohne Transaktion fehlt er im Rauchtest j, der dann mit EXCEPTION abbricht (gewollt, kein stilles Überspringen, kein veralteter Stand).
-- Auf der Datenbank mit eingespielter Runde 30 c ändert ein Lauf nur N2/N3 (Abschnitt 3d, 83 eigenständig); alles andere ist schon erfüllt.
-- Reiseoptionen ändern sich nicht (Rauchtest j); keine Verbindung und kein Visum ist betroffen.
-- Kein DROP. DELETE nur in Abschnitt 3c: genau die zwölf einzeln aufgezählten veralteten Verbindungen zu aufgelösten Themen
-- (ausdrücklich erlaubt im Auftrag „Nachbesserung Dreißigste Runde und LM-S“, Teil A); jede Löschung nur nach Prüfung.
-- Seit 21.11. sind die Themen 102/103 in der Datenbank; der Schutz für fehlende Themen bleibt, greift aber nicht mehr.
-- Am Ende ein Rauchtest (liest nur, außer dem zurückgerollten Testfall k); schlägt er fehl, bricht die Migration mit Fehlermeldung ab.

-- 0) Vergleichsstand für den Rauchtest (Runde 30 c): Reiseoptionen aller Lernenden und Zahl der Visum-Zeilen VOR den Änderungen, nur gelesen und in einer Sitzungs-Einstellung gemerkt.
do $$ begin
  perform set_config('lb30.ro_vorher', coalesce((select jsonb_object_agg(id::text, schule.reiseoptionen(id)) from schule.lernender), '{}'::jsonb)::text, true);
  perform set_config('lb30.visum_vorher', (select count(*) from schule.v_ort_visum)::text, true);
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

-- 3c) Veraltete Verbindungen von und zu aufgelösten Themen gezielt löschen – jede einzeln, jede erst nach Prüfung:
--     Das aufgelöste Thema der Zeile hat weiter keine für Kinder sichtbare Einheit (Status geprueft oder freigegeben). Sonst Abbruch, nichts gelöscht.
--   8 Quadratische Gleichungen (allgemein) ← 12 Reinquadratische Gleichungen: Quadratische Gleichungen braucht 12: Stoff steht jetzt als Etappe reinquadratisch in 8 selbst; ersetzt durch 8 ← 68
--   12 Reinquadratische Gleichungen ← 68 Elementare Wurzeln: 12 ist aufgelöst (Entwurf ohne freigegebene Einheit)
--   49 Matrizen und Abbildungen mit Matrizen ← 48 Vektoren und Determinanten: Matrizen braucht 48: Vektor-Flug aufgelöst; ersetzt durch 49 ← 46
--   74 Zweireihige Determinanten ← 48 Vektoren und Determinanten: Determinanten brauchen 48: Vektor-Flug aufgelöst; ersetzt durch 74 ← 46 und 74 ← 50
--   76 Reihen ← 41 Folgen: Reihen braucht 41: Folgen stehen jetzt als Etappen in 76; ersetzt durch 76 ← 28
--   72 Zinseszins ← 67 Potenzen als Schreibweise: 72 ist aufgelöst (Stoff in 94 und 37)
--   72 Zinseszins ← 71 Zinsen: 72 ist aufgelöst (Stoff in 94 und 37)
--   77 Umkehrfunktionen ← 32 Zuordnung und Funktion: 77 ist aufgelöst (Stoff in 36)
--   78 Parameter und Funktionenscharen ← 33 Lineare Funktionen: 78 ist aufgelöst (Stoff in 33 und 6)
--   82 Bedingte Wahrscheinlichkeit ← 21 Brüche und Anteile: 82 ist aufgelöst (Stoff in 63 und 62)
--   82 Bedingte Wahrscheinlichkeit ← 23 Rechnen mit rationalen Zahlen: 82 ist aufgelöst (Stoff in 63 und 62)
--   82 Bedingte Wahrscheinlichkeit ← 61 Zufall und Laplace: 82 ist aufgelöst (Stoff in 63 und 62)
-- Löschschutz als Sitzungsfunktion (pg_temp: verschwindet mit der Sitzung, kein DROP nötig), damit Rauchtest m ihn prüfen kann.
-- Geschützt ist jedes Thema mit einer für Kinder sichtbaren Einheit: Status geprueft oder freigegeben (wie in der App).
create or replace function pg_temp.lb907_loeschen() returns int language plpgsql as $f$
declare r record; v_n int := 0; v_k int;
begin
  for r in select * from (values
    (8, 12, 12),
    (12, 68, 12),
    (49, 48, 48),
    (74, 48, 48),
    (76, 41, 41),
    (72, 67, 72),
    (72, 71, 72),
    (77, 32, 77),
    (78, 33, 78),
    (82, 21, 82),
    (82, 23, 82),
    (82, 61, 82)
  ) v(thema_id, braucht_id, aufgeloest) loop
    if exists (select 1 from schule.einheit e where e.thema_id = r.aufgeloest and e.status in ('geprueft', 'freigegeben')) then
      raise exception 'Abbruch vor Löschung %←%: Thema % hat eine für Kinder sichtbare Einheit (geprueft oder freigegeben)', r.thema_id, r.braucht_id, r.aufgeloest;
    end if;
    delete from schule.voraussetzung where thema_id = r.thema_id and braucht_id = r.braucht_id;
    get diagnostics v_k = row_count; v_n := v_n + v_k;
  end loop;
  return v_n;
end $f$;
select pg_temp.lb907_loeschen() as geloeschte_zeilen;

-- 3d) N2 (Nachprüfung Gestalter): Die zehn aufgelösten Themen (keine freigegebene Einheit) verlieren Klasse und Reihenfolge
--     für Realschule und IB (für das Gymnasium hatten sie schon keine). Klasse über klasse_fest = null, weil thema_jahrgang
--     klasse_fest über die Zuordnung legt und danach Nullen entfernt. Lernbereich- und Lehrplantexte bleiben als Herkunft stehen.
--   12: vorher rs_by Kl. 9 / Stelle 3, ib_myp Kl. 4 / Stelle 10
--   27: vorher ib_myp Kl. 2 / Stelle 4
--   40: vorher rs_by Kl. 9 / Stelle 12, ib_myp Kl. 5 / Stelle 6
--   41: vorher ib_myp Kl. 5 / Stelle 4
--   48: vorher rs_by Kl. 7 / Stelle 5
--   72: vorher ib_myp Kl. 4 / Stelle 14
--   77: vorher rs_by Kl. 10 / Stelle 8, ib_myp Kl. 5 / Stelle 10
--   78: vorher rs_by Kl. 8 / Stelle 7
--   82: vorher ib_myp Kl. 5 / Stelle 17
--   83: vorher ib_myp Kl. 3 / Stelle 14
update schule.thema
   set klasse_fest = coalesce(klasse_fest, '{}'::jsonb) || '{"gym_by": null, "rs_by": null, "ib_myp": null}'::jsonb,
       lehrplan_reihenfolge = coalesce(lehrplan_reihenfolge, '{}'::jsonb) - 'gym_by' - 'rs_by' - 'ib_myp'
 where id in (12, 27, 40, 41, 48, 72, 77, 78, 82, 83)
   and not exists (select 1 from schule.einheit e where e.thema_id = schule.thema.id and e.status in ('geprueft', 'freigegeben'));
-- Reihenfolgen je Schulart und Klasse lückenlos nachziehen (die übrigen Themen rücken auf; Reihenfolge untereinander gleich)
update schule.thema t set lehrplan_reihenfolge = coalesce(t.lehrplan_reihenfolge, '{}'::jsonb) || v.rf
from (values
  (2, '{"rs_by": 11}'::jsonb),
  (3, '{"rs_by": 13}'::jsonb),
  (6, '{"rs_by": 9, "ib_myp": 14}'::jsonb),
  (8, '{"rs_by": 11, "ib_myp": 10}'::jsonb),
  (9, '{"ib_myp": 11}'::jsonb),
  (10, '{"rs_by": 9}'::jsonb),
  (13, '{"rs_by": 12}'::jsonb),
  (14, '{"ib_myp": 10}'::jsonb),
  (25, '{"ib_myp": 5}'::jsonb),
  (26, '{"ib_myp": 4}'::jsonb),
  (29, '{"rs_by": 10}'::jsonb),
  (34, '{"ib_myp": 17}'::jsonb),
  (35, '{"rs_by": 10, "ib_myp": 15}'::jsonb),
  (36, '{"ib_myp": 16}'::jsonb),
  (37, '{"rs_by": 8, "ib_myp": 7}'::jsonb),
  (38, '{"ib_myp": 8}'::jsonb),
  (39, '{"ib_myp": 6}'::jsonb),
  (44, '{"rs_by": 7}'::jsonb),
  (45, '{"rs_by": 9, "ib_myp": 21}'::jsonb),
  (47, '{"rs_by": 3}'::jsonb),
  (49, '{"ib_myp": 11}'::jsonb),
  (51, '{"rs_by": 6}'::jsonb),
  (54, '{"rs_by": 4}'::jsonb),
  (55, '{"rs_by": 5, "ib_myp": 19}'::jsonb),
  (56, '{"ib_myp": 20}'::jsonb),
  (58, '{"rs_by": 17, "ib_myp": 8}'::jsonb),
  (59, '{"ib_myp": 13}'::jsonb),
  (60, '{"ib_myp": 11}'::jsonb),
  (61, '{"rs_by": 13, "ib_myp": 9}'::jsonb),
  (62, '{"rs_by": 10, "ib_myp": 25}'::jsonb),
  (63, '{"rs_by": 14, "ib_myp": 24}'::jsonb),
  (64, '{"rs_by": 15, "ib_myp": 10}'::jsonb),
  (65, '{"ib_myp": 18}'::jsonb),
  (66, '{"ib_myp": 9}'::jsonb),
  (69, '{"rs_by": 12}'::jsonb),
  (71, '{"rs_by": 15, "ib_myp": 12}'::jsonb),
  (73, '{"rs_by": 8}'::jsonb),
  (74, '{"rs_by": 5}'::jsonb),
  (75, '{"ib_myp": 5}'::jsonb),
  (76, '{"ib_myp": 4}'::jsonb),
  (79, '{"ib_myp": 12}'::jsonb),
  (80, '{"ib_myp": 14}'::jsonb),
  (81, '{"rs_by": 19, "ib_myp": 7}'::jsonb),
  (84, '{"ib_myp": 13}'::jsonb),
  (91, '{"ib_myp": 22}'::jsonb),
  (92, '{"rs_by": 8}'::jsonb),
  (93, '{"rs_by": 16}'::jsonb),
  (94, '{"rs_by": 14}'::jsonb),
  (95, '{"rs_by": 18, "ib_myp": 23}'::jsonb),
  (98, '{"rs_by": 6, "ib_myp": 6}'::jsonb),
  (101, '{"rs_by": 7}'::jsonb)
) v(id, rf) where t.id = v.id;

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
  (84, 'Entdecker-Insel; Aussagen und Wahrheitswerte werden hier eingeführt')
) v(id, g) where t.id = v.id and t.eigenstaendig is distinct from v.g;
-- N3 (Nachprüfung Gestalter): 83 Mengen ist aufgelöst (kein freigegebener Flug) – Kennzeichnung entfernen
update schule.thema set eigenstaendig = null where id = 83 and eigenstaendig is not null;

-- 6) Rauchtest (liest nur)
do $$
declare v_n int; v_txt text;
begin
  -- a) Thema 12 (aufgelöst) hat keine Gymnasium-Klasse; der Stoff steht in 8 (Etappe reinquadratisch)
  if schule.thema_jahrgang(12) ? 'gym_by' then raise exception 'Rauchtest: Thema 12 darf keine Gymnasium-Klasse haben'; end if;
  -- i) Neue Regel: keine Verbindung von oder zu einem Thema ohne freigegebene Einheit, außer ausdrücklich begründet (Begründung beginnt mit „Ausnahme:“)
  select string_agg(v.thema_id || '←' || v.braucht_id, ', ') into v_txt from schule.voraussetzung v
   where (not exists (select 1 from schule.einheit e where e.thema_id = v.thema_id and e.status in ('geprueft', 'freigegeben'))
       or not exists (select 1 from schule.einheit e where e.thema_id = v.braucht_id and e.status in ('geprueft', 'freigegeben')))
     and coalesce(v.begruendung, '') not like 'Ausnahme:%';
  if v_txt is not null then raise exception 'Rauchtest: Verbindung von/zu Thema ohne freigegebene Einheit: %', v_txt; end if;
  -- b) jedes Thema mit Klasse und freigegebener Einheit hat Voraussetzungen oder ist ausdrücklich eigenständig
  select count(*), string_agg(t.id::text, ', ') into v_n, v_txt from schule.thema t
   where schule.thema_jahrgang(t.id) <> '{}'::jsonb and t.eigenstaendig is null
     and exists (select 1 from schule.einheit e where e.thema_id = t.id and e.status in ('geprueft', 'freigegeben'))
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
  if coalesce(current_setting('lb30.ro_vorher', true), '') = '' then
    raise exception 'Rauchtest j: kein Vorherstand der Reiseoptionen (Abschnitt 0 lief nicht in derselben Transaktion) – Datei in einer Transaktion einspielen';
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
  -- k) Testfall „Zielort offen, Voraussetzungs-Ort fehlt“ für die harte Kante 102 ← 30:
  --    Ziel-Ort = Ort von 102 (Potenzgesetze), Voraussetzungs-Ort = Ort von 30 (Potenzen). Ein erfundener Test-Lernender
  --    (ist_test, kein echtes Kind) wird in einem Unterblock angelegt und am Ende zurückgerollt.
  --    k1: Ziel-Ort offen, Voraussetzungs-Ort nicht auf der Route  → Ziel-Ort angeboten, visum_fehlt nennt den Voraussetzungs-Ort.
  --    k2: Ziel-Ort offen, Voraussetzungs-Ort offen               → ebenso.
  --    k3: Ziel-Ort offen, Voraussetzungs-Ort fertig              → visum_fehlt nennt ihn nicht.
  --    Klasse 5 und Ziel-Ort in Klasse 7: kein Rückstand, Modus frei, damit der Ort sicher angeboten wird.
  declare
    v_ziel bigint; v_vor bigint; v_vor_titel text; v_lid bigint; v_rid bigint; v_ro jsonb; v_opt jsonb; v_fehler text := null;
  begin
    select bt.block_id into v_ziel from schule.block_thema bt where bt.thema_id = 102 order by bt.block_id limit 1;
    select bt.block_id into v_vor from schule.block_thema bt where bt.thema_id = 30 order by bt.block_id limit 1;
    if v_ziel is null or v_vor is null or v_ziel = v_vor then
      raise exception 'Rauchtest k: Orte von 102/30 nicht gefunden oder gleich (Ziel %, Voraussetzung %)', v_ziel, v_vor;
    end if;
    if not exists (select 1 from schule.v_ort_visum where ort_id = v_ziel and braucht_ort_id = v_vor) then
      raise exception 'Rauchtest k: v_ort_visum enthält % → % nicht (Kante 102 ← 30 nicht hart?)', v_ziel, v_vor;
    end if;
    select titel into v_vor_titel from schule.block where id = v_vor;
    begin
      -- ids sind GENERATED ALWAYS: keine feste id, sondern vergeben lassen (returning)
      insert into schule.lernender (anzeigename, klasse, ist_test, schulart) values ('Rauchtest 102←30 (wird zurückgerollt)', 5, true, 'gym_by') returning id into v_lid;
      insert into schule.route (lernender_id, block_id, position, art, status) values (v_lid, v_ziel, 1, 'normal', 'offen');
      -- k1
      v_ro := schule.reiseoptionen(v_lid);
      select o into v_opt from jsonb_array_elements(v_ro->'optionen') o where (o->>'ort_id')::bigint = v_ziel;
      if v_opt is null then v_fehler := 'k1: Ziel-Ort nicht angeboten: ' || v_ro::text;
      elsif not exists (select 1 from jsonb_array_elements(v_opt->'visum_fehlt') f where f->>'ort' = v_vor_titel) then
        v_fehler := 'k1: visum_fehlt nennt den Voraussetzungs-Ort nicht: ' || v_opt::text; end if;
      -- k2
      if v_fehler is null then
        insert into schule.route (lernender_id, block_id, position, art, status) values (v_lid, v_vor, 2, 'normal', 'offen') returning id into v_rid;
        v_ro := schule.reiseoptionen(v_lid);
        select o into v_opt from jsonb_array_elements(v_ro->'optionen') o where (o->>'ort_id')::bigint = v_ziel;
        if v_opt is null or not exists (select 1 from jsonb_array_elements(v_opt->'visum_fehlt') f where f->>'ort' = v_vor_titel) then
          v_fehler := 'k2: Sperre fehlt bei offenem Voraussetzungs-Ort: ' || coalesce(v_opt::text, v_ro::text); end if;
      end if;
      -- k3 (Status direkt einfügen statt ändern, damit kein Sterne-Auslöser läuft)
      if v_fehler is null then
        insert into schule.route (lernender_id, block_id, position, art, status) values (v_lid, v_vor, 3, 'normal', 'fertig');
        update schule.route set art = 'zusatz' where id = v_rid;
        v_ro := schule.reiseoptionen(v_lid);
        select o into v_opt from jsonb_array_elements(v_ro->'optionen') o where (o->>'ort_id')::bigint = v_ziel;
        if v_opt is null or exists (select 1 from jsonb_array_elements(v_opt->'visum_fehlt') f where f->>'ort' = v_vor_titel) then
          v_fehler := 'k3: Sperre bleibt trotz fertigem Voraussetzungs-Ort: ' || coalesce(v_opt::text, v_ro::text); end if;
      end if;
      raise exception using errcode = 'P0001', message = 'lb907_zurueckrollen';
    exception when sqlstate 'P0001' then
      if sqlerrm <> 'lb907_zurueckrollen' then raise; end if;
    end;
    if v_fehler is not null then raise exception 'Rauchtest k: %', v_fehler; end if;
    if exists (select 1 from schule.lernender where anzeigename like 'Rauchtest 102←30%') then
      raise exception 'Rauchtest k: Test-Lernender nicht zurückgerollt'; end if;
    raise notice 'Rauchtest k: 102 ← 30 sperrt den Ziel-Ort, solange der Voraussetzungs-Ort fehlt oder offen ist, und gibt ihn frei, wenn er fertig ist';
  end;
  -- l) N2/N3: nur die zehn stillgelegten Themen (nicht jedes nicht freigegebene) – ohne Klasse, Reihenfolge, „eigenständig“
  select string_agg(t.id::text, ', ') into v_txt from schule.thema t
   where t.id in (12, 27, 40, 41, 48, 72, 77, 78, 82, 83)
     and not exists (select 1 from schule.einheit e where e.thema_id = t.id and e.status in ('geprueft', 'freigegeben'))
     and (schule.thema_jahrgang(t.id) <> '{}'::jsonb
          or coalesce(t.lehrplan_reihenfolge, '{}'::jsonb) ?| array['gym_by', 'rs_by', 'ib_myp']
          or t.eigenstaendig is not null);
  if v_txt is not null then raise exception 'Rauchtest l: stillgelegte Themen tragen noch Klasse, Reihenfolge oder eigenständig: %', v_txt; end if;
  -- m) Löschschutz greift auch bei Status geprueft (und freigegeben): je eine Test-Einheit für das stillgelegte Thema 48 in einem
  --    Unterblock anlegen, den Löschschutz aufrufen – er muss abbrechen –, danach alles zurückrollen. Ohne Test-Einheit (m0)
  --    läuft er durch. Echte Einheiten werden nicht verändert.
  declare
    v_status text; v_meldung text; v_vers int; v_vor int; v_nach int;
  begin
    select count(*) into v_vor from schule.voraussetzung;
    if exists (select 1 from schule.einheit e where e.thema_id = 48 and e.status in ('geprueft', 'freigegeben')) then
      raise exception 'Rauchtest m: Thema 48 hat schon eine sichtbare Einheit – Testvoraussetzung fehlt';
    end if;
    perform pg_temp.lb907_loeschen();  -- m0: ohne sichtbare Einheit kein Abbruch
    foreach v_status in array array['geprueft', 'freigegeben'] loop
      v_meldung := null;
      begin
        select coalesce(max(version), 0) + 1000 into v_vers from schule.einheit where thema_id = 48;
        insert into schule.einheit (thema_id, version, status, inhalt, erstellt_von)
          values (48, v_vers, v_status, '{}'::jsonb, 'Rauchtest m (wird zurückgerollt)');
        begin
          perform pg_temp.lb907_loeschen();
        exception when others then
          v_meldung := sqlerrm;
        end;
        raise exception using errcode = 'P0001', message = 'lb907m_zurueckrollen';
      exception when sqlstate 'P0001' then
        if sqlerrm <> 'lb907m_zurueckrollen' then raise; end if;
      end;
      if v_meldung is null or v_meldung not like 'Abbruch vor Löschung %' then
        raise exception 'Rauchtest m: Löschschutz greift nicht bei Status % (Meldung: %)', v_status, coalesce(v_meldung, 'keine');
      end if;
    end loop;
    select count(*) into v_nach from schule.voraussetzung;
    if v_nach <> v_vor or exists (select 1 from schule.einheit where erstellt_von like 'Rauchtest m%') then
      raise exception 'Rauchtest m: Testzustand nicht zurückgerollt'; end if;
    raise notice 'Rauchtest m: Löschschutz bricht bei geprueft und bei freigegeben ab, ohne sichtbare Einheit läuft er';
  end;
  raise notice 'Rauchtest Dreißigste Runde (Nacharbeit 907 c) bestanden';
end $$;
