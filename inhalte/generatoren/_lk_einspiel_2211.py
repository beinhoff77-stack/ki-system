"""Einspiel-SQL für die neuen Lernkarten aus LK-D (22.11.2026, Auftrag „LK-D Einspiel“).

Liest die Themendateien (inhalte/themen) und Kann-Dateien (inhalte/kann) und schreibt
inhalte/pruefung/lehrplan/lk_einspiel_2211.sql. Nichts wird hier ausgeführt.
"""
import json
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
ZIEL = WURZEL / 'pruefung' / 'lehrplan' / 'lk_einspiel_2211.sql'

# thema_id, Schlüssel, Einheit (Stand echte DB 22.11.), neue Etappen
LISTE = [
    (46, 'abbildungen.kongruenz', 54, ['vektor_koordinaten', 'vektor_drehen']),
    (47, 'abbildungen.aehnlichkeit', 8, ['streckung_vektor']),
    (44, 'geometrie.konstruktion', 57, ['vierecke_konstruieren']),
    (99, 'messen.flaechen_vielecke', 93, ['drachen_raute']),
    (91, 'raum.schraegbilder', 30, ['wahre_groesse', 'koerper_symmetrie', 'raumwinkel']),
    (101, 'messen.prisma_zylinder', 94, ['cavalieri']),
    (29, 'terme.umformen', 3, ['gleichungen_binomisch']),
    (61, 'stochastik.grundbegriffe', 31, ['darstellen']),
    (20, 'zahlen.reell', 45, ['irrational_beweis']),
]


def j(x):
    s = json.dumps(x, ensure_ascii=False, separators=(', ', ': '))
    assert '$lk$' not in s and '$j$' not in s
    return s


def block(t, schl, e, lz):
    d = json.loads((WURZEL / 'themen' / f'{schl}.json').read_text(encoding='utf-8'))
    assert d['thema_id'] == t, (schl, d['thema_id'])
    kann = json.loads((WURZEL / 'kann' / f'{schl}.json').read_text(encoding='utf-8'))['etappen'][lz]
    karte = next(x for x in d['inhalt']['etappen'] if x['lernziel'] == lz)
    tf = next(x for x in d['inhalt']['teilfaehigkeiten'] if x['k'] == lz)
    tf = {'k': tf['k'], 'text': karte['titel'], 'lernziele': tf['lernziele']}
    assert lz in d['inhalt']['bewertung']['lernziele_vertiefung'], (schl, lz)
    auf = [{k: v for k, v in a.items() if k not in ('c', 'zahl')} for a in d['aufgaben'] if a['l'] == lz]
    n = len(auf)
    pools = {}
    for a in auf: pools[a['p']] = pools.get(a['p'], 0) + 1
    return n, f"""
-- Thema {t} ({schl}), Einheit {e}: Etappe {lz} „{karte['titel']}“ – {n} Aufgaben ({', '.join(f'{k} {v}' for k, v in pools.items())})
do $lk$
declare v_status text; v_inhalt jsonb; v_max int; v_auf jsonb; v_n int; v_geteilt boolean;
begin
  select status, inhalt into v_status, v_inhalt from schule.einheit where id = {e} and thema_id = {t};
  if v_status is null then raise exception 'Einheit {e} gehört nicht zu Thema {t}'; end if;
  if (select schluessel from schule.thema where id = {t}) <> '{schl}' then raise exception 'Thema {t} ist nicht {schl}'; end if;
  -- vor der Teilung einspielen: nach TL-S liegt die Etappe in einem anderen Teil
  if exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_von') then
    execute 'select exists (select 1 from schule.thema where (teil_stamm = $1 or id = $1) and teil_von is not null)' into v_geteilt using {t}::bigint;
    if v_geteilt then raise exception 'Thema {t} ist schon geteilt (TL-S) – dieses SQL gehört VOR die Teilung'; end if;
  end if;
  -- 1. Etappe in der Einheit (Lernkarte, Teilfähigkeit, Vertiefung); nur wenn noch nicht da
  if not exists (select 1 from jsonb_array_elements(coalesce(v_inhalt->'etappen', '[]'::jsonb)) x where x->>'lernziel' = '{lz}') then
    if v_status = 'freigegeben' then update schule.einheit set status = 'geprueft' where id = {e}; end if;   -- Schutz nur für diesen Schritt (wie TL-S)
    update schule.einheit set inhalt = jsonb_set(jsonb_set(jsonb_set(inhalt,
        '{{etappen}}', coalesce(inhalt->'etappen', '[]'::jsonb) || jsonb_build_array($j${j(karte)}$j$::jsonb)),
        '{{teilfaehigkeiten}}', coalesce(inhalt->'teilfaehigkeiten', '[]'::jsonb) || jsonb_build_array($j${j(tf)}$j$::jsonb)),
        '{{bewertung,lernziele_vertiefung}}', coalesce(inhalt#>'{{bewertung,lernziele_vertiefung}}', '[]'::jsonb) || to_jsonb('{lz}'::text))
     where id = {e};
    update schule.einheit set status = v_status where id = {e};
    raise notice 'Einheit {e}: Etappe {lz} angelegt';
  else
    raise notice 'Einheit {e}: Etappe {lz} schon vorhanden';
  end if;
  -- 2. Aufgaben aller Pools (nur INSERT; Vorhandenes wird nicht doppelt eingefügt)
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = {e};
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j${j(auf)}$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen({e}, v_auf);
  raise notice 'Einheit {e} ({lz}): % von {n} Aufgaben eingefügt (0 = schon vorhanden)', v_n;
  if v_n not in (0, {n}) then raise exception 'Einheit {e} ({lz}): nur % von {n} eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
  -- 3. Kann-Satz
  insert into schule.etappe_text (thema_id, lernziel, kann, geaendert_am) values ({t}, '{lz}', $j${kann}$j$, now())
  on conflict (thema_id, lernziel) do nothing;
end $lk$;
"""


def main():
    teile, soll, et = [], 0, []
    for t, schl, e, lzs in LISTE:
        for lz in lzs:
            n, b = block(t, schl, e, lz)
            teile.append(b); soll += n; et.append((t, e, lz, n))
    bed = ' or '.join(f"(a.einheit_id = {e} and a.variante_gruppe = '{lz}')" for t, e, lz, n in et)
    bed_e = ' or '.join(f"(e.id = {e} and x->>'lernziel' = '{lz}')" for t, e, lz, n in et)
    bed_k = ' or '.join(f"(thema_id = {t} and lernziel = '{lz}')" for t, e, lz, n in et)
    kopf = f"""-- LK-D Einspiel (22.11.2026): neue Lernkarten aus LK-D in die Datenbank – {len(et)} Etappen, {soll} Aufgaben, {len(et)} Kann-Sätze.
-- Quelle: inhalte/generatoren/_lk_einspiel_2211.py aus inhalte/themen/*.json und inhalte/kann/*.json (Inhalte aus _lk_etappen_2211.py, Lösungen berechnet).
-- Nur für den Haupt-Chat; NICHT von lehrplan-lb ausgeführt. In EINER Transaktion einspielen (psql -1). Wiederholt ausführbar.
--
-- REIHENFOLGE: VOR der Teilung (TL-S), also nach lk_korrektur_2211.sql (und LK-S), vor 20261123_tl_s_teilung.sql.
--   Grund: tl_teilen verteilt die Etappen nach dem Katalog der Einheit (inhalt.etappen); Etappen, die es noch nicht gibt, überspringt es.
--   Vorher eingespielt, ziehen Etappe, Aufgaben (gleiche Ids) und Kann-Satz mit TL-S in den richtigen Teil, und 101 Teil 2 (cavalieri) wird
--   keine leere Hülle. Nach der Teilung bricht dieses SQL je Thema ab (Prüfung auf thema.teil_von).
--
-- Was passiert je Etappe:
--   1. Etappe in der Einheit: Lernkarte an inhalt.etappen, Teilfähigkeit an inhalt.teilfaehigkeiten, Lernziel an bewertung.lernziele_vertiefung.
--      Das ist ein UPDATE der Einheit (anders als aufgaben_frisch_2211.sql): Freigegebene Einheiten sind geschützt (einheit_schutz),
--      deshalb wird die Einheit nur für diesen Schritt kurz auf 'geprueft' und gleich wieder auf den alten Status gesetzt – wie TL-S.
--      Ohne diesen Schritt gibt es keine Lernkarte; nur INSERT ist dafür nicht möglich. Kein DELETE, kein DROP, keine anderen Felder.
--   2. Aufgaben aller Pools (uebung, test, korrektur, sicherung) über schule.aufgaben_einfuegen (nur INSERT, keine Dubletten).
--   3. Kann-Satz in schule.etappe_text (INSERT … on conflict do nothing).
-- Pflicht/Kür: Alle neuen Etappen kommen als Vertiefung (wie in den Dateien) – bestehende Flüge, Tests und Stempel ändern sich dadurch nicht.
--   Pflicht je Schulart setzt danach TL-S über bewertung.pflicht_je_schulart (Daten: lk_teilung_2211.json, status_je_schulart).
--   Hinweis: 20, 47, 99 werden nicht geteilt – ob TL-S pflicht_je_schulart auch dort setzt, klärt bau-lehrer.
-- Die neuen Aufgaben sind sofort sichtbar (aufgabe.freigegeben Standard true).
"""
    pruef = f"""
-- Rauchtest (liest nur)
do $pruef$
declare v_et int; v_auf int; v_k int;
begin
  select count(*) into v_et from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') x where {bed_e};
  select count(*) into v_auf from schule.aufgabe a where {bed};
  select count(*) into v_k from schule.etappe_text where {bed_k};
  if v_et <> {len(et)} then raise exception 'Rauchtest: % von {len(et)} Etappen in den Einheiten', v_et; end if;
  if v_auf <> {soll} then raise exception 'Rauchtest: % von {soll} Aufgaben', v_auf; end if;
  if v_k <> {len(et)} then raise exception 'Rauchtest: % von {len(et)} Kann-Sätzen', v_k; end if;
  if exists (select 1 from schule.einheit where id in ({', '.join(str(e) for e in sorted({x[1] for x in et}))}) and status <> 'freigegeben') then
    raise exception 'Rauchtest: eine Einheit ist nicht mehr freigegeben';
  end if;
  raise notice 'Rauchtest LK-D Einspiel bestanden: {len(et)} Etappen, {soll} Aufgaben, {len(et)} Kann-Sätze';
end $pruef$;
"""
    ZIEL.write_text(kopf + ''.join(teile) + pruef, encoding='utf-8')
    print(ZIEL, len(et), 'Etappen', soll, 'Aufgaben')


if __name__ == '__main__':
    main()
