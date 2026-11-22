#!/usr/bin/env bash
# WD-S 3/4 (ChatGPT 919/921): echte Tests mit zwei GLEICHZEITIGEN Transaktionen (zwei Geräte).
#   A) dieselbe fällige Etappe zweimal: genau ein Stufenfortschritt, genau einmal Wiederholungs-Sterne.
#   B) die zwei letzten Pflicht-Etappen der Tagesrunde gleichzeitig: danach ist die Runde fertig (Abschluss unter Sperre, WD-S 4).
# NUR auf einer Wegwerf-Datenbank (Kopie/Branch) – das Skript schreibt und behält Daten (Testkind, Hilfstabelle public.wd3_gleich).
# Ergebnis: Exit 0 nur, wenn beide Teile „ok“ melden; jedes „FEHLER“ beendet mit Exit 1.
# Aufruf:  WD_WEGWERF=ja WD_DB='postgresql://…' bash supabase/tests/wd_s3_gleichzeitig.sh
set -euo pipefail
: "${WD_DB:?WD_DB = psql-Verbindung der Wegwerf-Datenbank}"
[ "${WD_WEGWERF:-}" = "ja" ] || { echo "Abbruch: nur mit WD_WEGWERF=ja (Wegwerf-Datenbank)"; exit 1; }
P=(psql "$WD_DB" -v ON_ERROR_STOP=1 -qtA)
AUSGABE=""
pruefen() { echo "$1"; AUSGABE="$AUSGABE"$'\n'"$1"; }

# Vorbereitung: Testkind, drei Etappen ohne bisherige Antworten (je zwei Auswahl-Aufgaben), Lerntage
"${P[@]}" <<'SQL'
create table if not exists public.wd3_gleich (nr int, l bigint, e bigint, lz text, a1 bigint, a2 bigint, s0 bigint);
truncate public.wd3_gleich;
insert into public.wd3_gleich (nr, l, e, lz, a1, a2)
select row_number() over (order by q.einheit_id, q.lz), l.id, q.einheit_id, q.lz, q.ids[1], q.ids[2]
  from (select id from schule.lernender where ist_test and aktiv order by id limit 1) l,
       lateral (select a.einheit_id, a.variante_gruppe lz, array_agg(a.id order by a.id) ids
                  from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id and e.status = 'freigegeben' and e.id = schule.thema_einheit(e.thema_id)
                 where a.pool = 'uebung' and a.freigegeben and a.antworttyp = 'auswahl' and e.block_id is not null
                   and not exists (select 1 from schule.versuch v join schule.aufgabe b on b.id = v.aufgabe_id
                                    where v.lernender_id = l.id and b.einheit_id = a.einheit_id and b.variante_gruppe = a.variante_gruppe)
                 group by 1, 2 having count(*) >= 2 order by 1, 2 limit 3) q;
insert into schule.lerntag (lernender_id, fach, datum, zeitzone)
select distinct g.l, 'Mathematik', schule.heute_tag(g.l) - d, 'Europe/Berlin' from public.wd3_gleich g, generate_series(1, 10) d on conflict do nothing;
insert into schule.karte_stand (lernender_id, einheit_id, lernziel) select l, e, lz from public.wd3_gleich on conflict do nothing;
update schule.karte_stand k set sitzt = true, sitzt_am = now() - interval '30 days', wdh_stufe = 1, wdh_lerntage = 3, wdh_fehler = 0,
       wdh_ab = now() - interval '6 days', faellig_am = now() - interval '3 days' from public.wd3_gleich g
 where k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz;
update public.wd3_gleich g set s0 = (select count(*) from schule.sterne s where s.lernender_id = g.l and s.grund = 'wdh');
-- Teil B: Tagesrunde mit genau den Etappen 2 und 3 offen (andere Etappen einer schon vorhandenen Runde gelten als bearbeitet)
insert into schule.wdh_runde (lernender_id, tag, ziel) select l, schule.heute_tag(l), 2 from public.wd3_gleich where nr = 1 on conflict (lernender_id, tag) do update set fertig_am = null;
update schule.wdh_runde_etappe r set bearbeitet_am = coalesce(r.bearbeitet_am, now()) from public.wd3_gleich g where g.nr = 1 and r.lernender_id = g.l and r.tag = schule.heute_tag(g.l);
insert into schule.wdh_runde_etappe (lernender_id, tag, nr, einheit_id, lernziel)
select l, schule.heute_tag(l), 900 + nr, e, lz from public.wd3_gleich where nr in (2, 3)
on conflict (lernender_id, tag, einheit_id, lernziel) do update set bearbeitet_am = null;
update schule.wdh_runde w set fertig_am = null from public.wd3_gleich g where g.nr = 1 and w.lernender_id = g.l and w.tag = schule.heute_tag(g.l);
SQL

antwort() { # $1 = Etappe (nr), $2 = Aufgaben-Spalte, $3 = Gerät, $4 = Wartezeit in der Transaktion
  "${P[@]}" <<SQL
begin;
select 'Gerät $3: ' || coalesce((schule.uebung_pruefen_wd(g.l, jsonb_build_object('aufgabe_id', g.$2, 'client_id', 'gleichzeitig-$3-' || gen_random_uuid(),
         'antwort', jsonb_build_object('index', (select (a.loesung->>'index')::int from schule.aufgabe a where a.id = g.$2))))->'wiederholung')::text, 'keine Wiederholung')
  from public.wd3_gleich g where g.nr = $1;
select pg_sleep($4);
commit;
SQL
}

# Teil A: Etappe 1 von zwei Geräten
antwort 1 a1 A 2 &
sleep 0.5
antwort 1 a2 B 0 &
wait
pruefen "$("${P[@]}" <<'SQL'
select case when k.wdh_stufe = 2 and (select count(*) from schule.sterne s where s.lernender_id = g.l and s.grund = 'wdh' and s.bezug like 'wdh:' || g.e || ':' || g.lz || ':%') = 1
            then 'ok A gleichzeitig: genau ein Fortschritt (Stufe 1 → 2), einmal Wiederholungs-Sterne'
            else 'FEHLER A gleichzeitig: Stufe ' || k.wdh_stufe end
  from public.wd3_gleich g join schule.karte_stand k on k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz where g.nr = 1;
SQL
)"

# Teil B: die zwei letzten Pflicht-Etappen der Runde gleichzeitig
antwort 2 a1 C 2 &
sleep 0.5
antwort 3 a1 D 0 &
wait
pruefen "$("${P[@]}" <<'SQL'
select case when w.fertig_am is not null and (select count(*) from schule.wdh_runde_etappe r where r.lernender_id = w.lernender_id and r.tag = w.tag and r.bearbeitet_am is null) = 0
            then 'ok B gleichzeitig: Runde fertig (beide letzten Etappen bearbeitet)'
            else 'FEHLER B gleichzeitig: Runde nicht fertig (offen: ' || (select count(*) from schule.wdh_runde_etappe r where r.lernender_id = w.lernender_id and r.tag = w.tag and r.bearbeitet_am is null) || ')' end
  from public.wd3_gleich g join schule.wdh_runde w on w.lernender_id = g.l and w.tag = schule.heute_tag(g.l) where g.nr = 1;
SQL
)"

if grep -q "FEHLER" <<<"$AUSGABE" || [ "$(grep -c '^ok' <<<"$AUSGABE")" -ne 2 ]; then echo "Ergebnis: FEHLER"; exit 1; fi
echo "Ergebnis: ok"
