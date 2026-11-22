#!/usr/bin/env bash
# WD-S 3/4, FP-S 2 (ChatGPT 919/921/924): echte Tests mit zwei GLEICHZEITIGEN Transaktionen (zwei Geräte).
#   A) dieselbe fällige Etappe zweimal: genau ein Stufenfortschritt, genau einmal Wiederholungs-Sterne.
#   B) die zwei letzten Pflicht-Etappen der Tagesrunde gleichzeitig: danach ist die Runde fertig (Abschluss unter Sperre, WD-S 4).
#   C) Antwort, während eine andere Sitzung für dasselbe Kind Sterne bucht: die Antwort meldet nur ihre eigenen Sterne (FP-S 2).
#   D) Landung gleichzeitig mit der Nachbuchung: jede Seite meldet genau ihre Sterne, die Summe stimmt (FP-S 2).
# Setzt alle Migrationen bis FP-S 2 voraus.
# NUR auf einer Wegwerf-Datenbank (Kopie/Branch) – das Skript schreibt und behält Daten (Testkind, Hilfstabelle public.wd3_gleich).
# Ergebnis: Exit 0 nur, wenn alle vier Teile „ok“ melden; jedes „FEHLER“ oder ein abgebrochener Prozess beendet mit Exit 1.
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
                 group by 1, 2 having count(*) >= 2 order by 1, 2 limit 6) q;
insert into schule.lerntag (lernender_id, fach, datum, zeitzone)
select distinct g.l, 'Mathematik', schule.heute_tag(g.l) - d, 'Europe/Berlin' from public.wd3_gleich g, generate_series(1, 10) d on conflict do nothing;
insert into schule.karte_stand (lernender_id, einheit_id, lernziel) select l, e, lz from public.wd3_gleich on conflict do nothing;
update schule.karte_stand k set sitzt = true, sitzt_am = now() - interval '30 days', wdh_stufe = 1, wdh_lerntage = 3, wdh_fehler = 0,
       wdh_ab = now() - interval '6 days', faellig_am = now() - interval '3 days' from public.wd3_gleich g
 where k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz and g.nr <= 3;
-- Teil C: Etappe 4 noch nicht gelandet; Teil D: Etappe 5 kurz vor der Landung, Etappe 6 früher gelandet (ohne Bonus, für die Nachbuchung)
update schule.karte_stand k set sitzt = false, gesetzt_am = null, eigene_loesungen = 0, folge = 0, gezaehlt = '{}' from public.wd3_gleich g
 where k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz and g.nr = 4;
update schule.karte_stand k set sitzt = false, gesetzt_am = null, wdh_gesetzt_am = null, gezaehlt = '{}'::jsonb, fehler_folge = 0, schwer_ok = true,
       eigene_loesungen = greatest(schule.karte_ziel(g.e, g.lz) - 1, 0), folge = greatest(least(3, schule.karte_ziel(g.e, g.lz)) - 1, 0),
       typen = coalesce((select array_agg('gl' || i) from generate_series(1, schule.karte_typen_noetig(g.e, g.lz)) i), '{}')
  from public.wd3_gleich g where k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz and g.nr = 5;
update schule.karte_stand k set sitzt = true, sitzt_am = now() - interval '20 days', gesetzt_am = null, landung = null, wdh_stufe = 2, wdh_lerntage = 7, wdh_ab = now()
  from public.wd3_gleich g where k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz and g.nr = 6;
update public.wd3_gleich g set s0 = (select count(*) from schule.sterne s where s.lernender_id = g.l and s.grund = 'wdh');
-- Teil B: Tagesrunde mit genau den Etappen 2 und 3 offen (andere Etappen einer schon vorhandenen Runde gelten als bearbeitet)
insert into schule.wdh_runde (lernender_id, tag, ziel) select l, schule.heute_tag(l), 2 from public.wd3_gleich where nr = 1 on conflict (lernender_id, tag) do update set fertig_am = null;
update schule.wdh_runde_etappe r set bearbeitet_am = coalesce(r.bearbeitet_am, now()) from public.wd3_gleich g where g.nr = 1 and r.lernender_id = g.l and r.tag = schule.heute_tag(g.l);
insert into schule.wdh_runde_etappe (lernender_id, tag, nr, einheit_id, lernziel)
select l, schule.heute_tag(l), 900 + nr, e, lz from public.wd3_gleich where nr in (2, 3)
on conflict (lernender_id, tag, einheit_id, lernziel) do update set bearbeitet_am = null;
update schule.wdh_runde w set fertig_am = null from public.wd3_gleich g where g.nr = 1 and w.lernender_id = g.l and w.tag = schule.heute_tag(g.l);
SQL

antwort() { # $1 = Etappe (nr), $2 = Aufgaben-Spalte, $3 = Gerät, $4 = Wartezeit in der Transaktion; gibt die ganze Antwort aus
  "${P[@]}" <<SQL
begin;
select 'Gerät $3: ' || schule.uebung_pruefen_wd(g.l, jsonb_build_object('aufgabe_id', g.$2, 'client_id', 'gleichzeitig-$3-' || gen_random_uuid(),
         'antwort', jsonb_build_object('index', (select (a.loesung->>'index')::int from schule.aufgabe a where a.id = g.$2))))::text
  from public.wd3_gleich g where g.nr = $1;
select pg_sleep($4);
commit;
SQL
}
zwei() { # zwei Befehle gleichzeitig (der zweite 0,5 s später), jeder Prozess einzeln abgewartet
  ( eval "$1" ) > /tmp/wd3_g1.$$ 2>&1 & local p1=$!
  sleep 0.5
  ( eval "$2" ) > /tmp/wd3_g2.$$ 2>&1 & local p2=$!
  local f=0; wait $p1 || f=1; wait $p2 || f=1
  cat /tmp/wd3_g1.$$ /tmp/wd3_g2.$$
  if [ $f -ne 0 ]; then pruefen "FEHLER: ein Prozess ist abgebrochen"; fi
}

# Teil A: Etappe 1 von zwei Geräten
zwei "antwort 1 a1 A 2" "antwort 1 a2 B 0"
pruefen "$("${P[@]}" <<'SQL'
select case when k.wdh_stufe = 2 and (select count(*) from schule.sterne s where s.lernender_id = g.l and s.grund = 'wdh' and s.bezug like 'wdh:' || g.e || ':' || g.lz || ':%') = 1
            then 'ok A gleichzeitig: genau ein Fortschritt (Stufe 1 → 2), einmal Wiederholungs-Sterne'
            else 'FEHLER A gleichzeitig: Stufe ' || k.wdh_stufe end
  from public.wd3_gleich g join schule.karte_stand k on k.lernender_id = g.l and k.einheit_id = g.e and k.lernziel = g.lz where g.nr = 1;
SQL
)"

# Teil B: die zwei letzten Pflicht-Etappen der Runde gleichzeitig
zwei "antwort 2 a1 C 2" "antwort 3 a1 D 0"
pruefen "$("${P[@]}" <<'SQL'
select case when w.fertig_am is not null and (select count(*) from schule.wdh_runde_etappe r where r.lernender_id = w.lernender_id and r.tag = w.tag and r.bearbeitet_am is null) = 0
            then 'ok B gleichzeitig: Runde fertig (beide letzten Etappen bearbeitet)'
            else 'FEHLER B gleichzeitig: Runde nicht fertig (offen: ' || (select count(*) from schule.wdh_runde_etappe r where r.lernender_id = w.lernender_id and r.tag = w.tag and r.bearbeitet_am is null) || ')' end
  from public.wd3_gleich g join schule.wdh_runde w on w.lernender_id = g.l and w.tag = schule.heute_tag(g.l) where g.nr = 1;
SQL
)"

# Teil C: eine andere Sitzung bucht Sterne für dasselbe Kind, während die Antwort läuft (sie hält die Karte der Etappe 4 gesperrt)
fremd() {
  "${P[@]}" <<'SQL'
begin;
select 1 from schule.karte_stand k join public.wd3_gleich g on g.l = k.lernender_id and g.e = k.einheit_id and g.lz = k.lernziel where g.nr = 4 for update of k;
insert into schule.sterne (lernender_id, menge, grund, bezug) select l, 7, 'bonus', 'gleichzeitig-fremd-' || gen_random_uuid() from public.wd3_gleich where nr = 1;
select pg_sleep(2);
commit;
SQL
}
zwei "fremd" "antwort 4 a1 E 0" > /tmp/wd3_c.$$
cat /tmp/wd3_c.$$
C_STERNE=$(grep -o 'Gerät E: .*' /tmp/wd3_c.$$ | sed 's/^Gerät E: //' | python3 -c 'import sys,json; print(json.loads(sys.stdin.read()).get("sterne"))')
C_SOLL=$("${P[@]}" -c "select schule.sterne_regel('sterne_uebung_richtig')")
if [ "$C_STERNE" = "$C_SOLL" ]; then pruefen "ok C gleichzeitig: Antwort meldet nur ihre eigenen Sterne ($C_STERNE)"; else pruefen "FEHLER C gleichzeitig: Antwort meldet $C_STERNE statt $C_SOLL"; fi

# Teil D: Landung (Etappe 5) gleichzeitig mit der Nachbuchung (bucht Etappe 6; hält die Karte der Etappe 5 gesperrt)
S0=$("${P[@]}" -c "select coalesce(sum(s.menge), 0) from schule.sterne s join public.wd3_gleich g on g.l = s.lernender_id and g.nr = 1")
nach() {
  "${P[@]}" <<'SQL'
begin;
select 'Nachbuchung: ' || coalesce(sum(n.sterne), 0) from public.wd3_gleich g, schule.landung_bonus_nachbuchen(g.l) n where g.nr = 1;
select 1 from schule.karte_stand k join public.wd3_gleich g on g.l = k.lernender_id and g.e = k.einheit_id and g.lz = k.lernziel where g.nr = 5 for update of k;
select pg_sleep(2);
commit;
SQL
}
zwei "nach" "antwort 5 a1 F 0" > /tmp/wd3_d.$$
cat /tmp/wd3_d.$$
D_ANTWORT=$(grep -o 'Gerät F: .*' /tmp/wd3_d.$$ | sed 's/^Gerät F: //' | python3 -c 'import sys,json; j=json.loads(sys.stdin.read()); print(j.get("sterne"), (j.get("landung") or {}).get("bonus"))')
D_NACH=$(grep -o 'Nachbuchung: .*' /tmp/wd3_d.$$ | sed 's/^Nachbuchung: //')
S1=$("${P[@]}" -c "select coalesce(sum(s.menge), 0) from schule.sterne s join public.wd3_gleich g on g.l = s.lernender_id and g.nr = 1")
read -r D_STERNE D_BONUS <<<"$D_ANTWORT"
if [ "$D_BONUS" != "None" ] && [ "$D_STERNE" = "$(( C_SOLL + D_BONUS ))" ] && [ "$D_NACH" -gt 0 ] && [ "$(( S1 - S0 ))" = "$(( D_STERNE + D_NACH ))" ]; then
  pruefen "ok D gleichzeitig: Landung meldet $D_STERNE (Übung + Bonus $D_BONUS), Nachbuchung $D_NACH, Summe +$(( S1 - S0 ))"
else pruefen "FEHLER D gleichzeitig: Antwort $D_ANTWORT, Nachbuchung $D_NACH, Summe +$(( S1 - S0 ))"; fi
rm -f /tmp/wd3_g1.$$ /tmp/wd3_g2.$$ /tmp/wd3_c.$$ /tmp/wd3_d.$$

if grep -q "FEHLER" <<<"$AUSGABE" || [ "$(grep -c '^ok' <<<"$AUSGABE")" -ne 4 ]; then echo "Ergebnis: FEHLER"; exit 1; fi
echo "Ergebnis: ok"
