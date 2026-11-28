#!/usr/bin/env python3
"""RB-S: Regel und Fehlbilder der Vorrats-Aufgaben (inhalte/mathe-profi/rollend-*/) für die Datenbank (Tabellen schule.aufgabe_regel,
schule.aufgabe_fehlbild aus der Migration 20261204_rb_s_regelbezug.sql).

Aufruf:  python3 -I tools/regelbezug_sql.py [--runden 1,2,3,4 | 5 | alle]          -> Übersicht, Zählungen, Abweichungsliste (schreibt nichts)
         python3 -I tools/regelbezug_sql.py --runden 5 --sql > x.sql             -> Nachtrags-Paket für die SCHON EINGESPIELTEN Aufgaben der Runden
         python3 -I tools/regelbezug_sql.py --runden 5 --sql --probe > x.sql     -> dasselbe, rollt am Ende absichtlich zurück (Bericht in der Meldung)
         --json                                                                   -> Zählungen als JSON (für inhalte/plan/regelbezug.md)
Vorgabe für --runden wie tools/rollend_sql.py (1,2,3,4). Je Runde ein Paket (Größe); die Reihenfolge ist egal, ein zweiter Lauf ändert nichts.

ZUORDNUNG Repo-Aufgabe -> Datenbank-Aufgabe (es gibt in der Datenbank keine Kennung):
  1. Einheit und Reihenfolge-Nummer r rechnet tools/rollend_sql.sammeln genau wie beim Einspielen (Runden 1-4: max_r + Platz unter allen Aufgaben
     der Einheit in den Runden 1-4; Runde R >= 5: max_r + 1000·R + Platz in der Runde; Pool uebung).
  2. Gegen das, was WIRKLICH eingespielt wurde: die Pakete tools/tests/aus/rollend*_einspielen.sql (Einheit, r, Aufgaben-JSON). Stimmt die Aufgabe
     an (Einheit, r) im Paket nicht mit der Datei überein, wird in derselben Einheit nach genau einer Paket-Zeile mit gleichem Fragetext gesucht
     (falls sich Plätze verschoben haben). Inhaltliche Abweichung (Frage, Antworten, Lösung, Typ, Lernkarte) -> Fehlbilder NICHT übernommen,
     Regel schon (Regel hängt an der Lernkarte, nicht an den Zahlen); steht in der Abweichungsliste. Nur Tipp/Lösungsweg/Form anders -> nur gemeldet.
  3. In der Datenbank prüft das Paket je Aufgabe: genau EINE Übungsaufgabe der Einheit mit dieser Reihenfolge-Nummer; md5 des Fragetexts
     (frage->>'text') = md5 des EINGESPIELTEN Texts; Antworttyp und Lernkarte gleich; bei Auswahl md5 der Antwort-Liste gleich; die Lösung
     (Wert/Index/Lückenwerte, Einheit, Toleranz: ganzes loesung-JSON) gleich dem eingespielten (jsonb-Gleichheit). Jede Abweichung
     -> Abbruch des ganzen Pakets (alles zurück), mit Liste der Kennungen.
  4. Nach dem Einfügen: jedes Fehlbild wird mit schule.fehlbild_probeantwort als Antwort nachgebaut; schule.antwort_bewerten muss sie als gültig
     und falsch bewerten, schule.fehlbild_finden muss genau dieses Fehlbild finden. Sonst Abbruch.
  Schon vorhandene Zeilen (zweiter Lauf) werden nicht geändert; weichen sie ab -> Abbruch.

FEHLBILDER: übernommen wird nur, was an einer Antwort eindeutig erkennbar ist:
  zahl: Wert ist eine Zahl, nicht die Lösung, kein zweites Fehlbild derselben Aufgabe mit gleichem Wert.
  auswahl: index gültig, nicht die richtige Option, Text der Option = „antwort“, nicht doppelt.
  luecken: luecke 1..n, ganze Zahl (Lücken nehmen nur ganze Zahlen an), nicht der richtige Wert dieser Lücke, nicht doppelt.
  text: nicht die Lösung, nicht doppelt.   bedingung: keine Fehlbilder.
Für künftige Runden bringt tools/rollend_sql.py --sql Regel und Fehlbilder gleich mit (Funktion block() unten; Abgleich gegen die Datei selbst).
Nicht ohne den ausdrücklichen Satz des Nutzers ausführen; Voraussetzung: Migration RB-S eingespielt.
"""
import glob
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WURZEL / 'tools'))
import rollend_sql  # noqa: E402

AUS = WURZEL / 'tools/tests/aus'
ZEILE = re.compile(r"\((\d+), '([\w.]+)', (\d+), (\d+), \$auf\$(.*?)\$auf\$::jsonb\)", re.S)
INHALT = ('f', 'a', 'o', 'y', 'l')        # Abweichung hier -> Fehlbilder passen evtl. nicht mehr
KENNUNG = re.compile(r'^(rr|id)\.[a-z0-9_.]+$')
FB_KENNUNG = re.compile(r'^fb\.[a-z0-9_.]+$')


def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def zahl(x):
    """Zahl normiert wie in der Datenbank-Spalte wert (Punkt, ohne Exponent, ohne überflüssige Nullen)."""
    d = Decimal(str(x))
    t = format(d.normalize(), 'f') if d == d.to_integral_value() else format(d, 'f')
    if '.' in t: t = t.rstrip('0').rstrip('.')
    return '0' if t in ('-0', '') else t


def eingespielt():
    """(einheit_id, r) -> Aufgaben-JSON, wie es in den Paketen unter tools/tests/aus steht (das, was in der Datenbank ist)."""
    aus, quelle = {}, {}
    for p in sorted(AUS.glob('rollend*_einspielen.sql')):
        for eid, schl, max_r, soll, js in ZEILE.findall(p.read_text(encoding='utf-8')):
            for row in json.loads(js):
                k = (int(eid), int(row['r']))
                if k in aus: raise SystemExit(f'{p.name}: Einheit {eid} Platz {row["r"]} steht in zwei Paketen ({quelle[k]})')
                aus[k], quelle[k] = row, p.name
    return aus, quelle


def repo_eintraege():
    """Kennung -> Eintrag der Aufgaben-Datei (mit regel, fehlbilder)."""
    out = {}
    for p in sorted(glob.glob(str(WURZEL / 'inhalte/mathe-profi/rollend-*/*.json'))):
        for e in json.loads(Path(p).read_text(encoding='utf-8'))['aufgaben']:
            out[e['kennung']] = e
    return out


def fehlbilder(e, row):
    """Liste der übernehmbaren Fehlbilder und Zählung der übrigen nach Grund. row = Aufgaben-JSON (wie eingespielt bzw. Datei)."""
    y, o, gut, weg = row['y'], row.get('o') or {}, [], Counter()
    schluessel = Counter()
    kand = []
    for nr, fb in enumerate(e.get('fehlbilder') or [], 1):
        w, grund, art, luecke = fb.get('antwort'), None, None, None
        if y == 'zahl':
            art = 'zahl'
            if isinstance(w, bool) or not isinstance(w, (int, float)): grund = 'kein Zahlwert'
            elif abs(Decimal(str(w)) - Decimal(str(o['wert']))) <= Decimal(str(max(1e-9, o.get('toleranz') or 0))): grund = 'gleich der Lösung'
            else: w = zahl(w)
        elif y in ('auswahl', 'markierung'):
            art, i = 'index', fb.get('index')
            if not isinstance(i, int) or i < 0 or (y == 'auswahl' and i >= len(row.get('a') or [])): grund = 'Index fehlt oder ungültig'
            elif i == o.get('index'): grund = 'gleich der Lösung'
            elif y == 'auswahl' and row['a'][i] != w: grund = 'Optionstext passt nicht zum Index'
            else: w = str(i)
        elif y == 'luecken':
            art, luecke, soll = 'luecke', fb.get('luecke'), o.get('werte') or []
            if not isinstance(luecke, int) or not 1 <= luecke <= len(soll): grund = 'Lücke fehlt oder ungültig'
            elif isinstance(w, bool) or not isinstance(w, (int, float)): grund = 'kein Zahlwert'
            elif Decimal(str(w)) != Decimal(str(w)).to_integral_value(): grund = 'keine ganze Zahl (Lücken nehmen nur ganze Zahlen)'
            elif Decimal(str(w)) == Decimal(str(soll[luecke - 1])): grund = 'gleich der Lösung'
            else: w = zahl(w)
        elif y == 'text':
            art = 'text'
            if not isinstance(w, str) or not w.strip(): grund = 'kein Text'
            elif re.sub(r'\s', '', w).upper() == re.sub(r'\s', '', str(o.get('text', ''))).upper(): grund = 'gleich der Lösung'
        else:
            grund = f'Antworttyp {y}'
        if grund is None:
            for feld, rx in (('fehlbild', FB_KENNUNG), ('regel_des_fehlbilds', KENNUNG)):
                if fb.get(feld) is not None and not rx.match(fb[feld]): grund = f'{feld} „{fb[feld]}“ ungültig'
            if not (fb.get('beschreibung') or '').strip(): grund = 'Beschreibung fehlt'
            elif len(fb['beschreibung']) > 600: grund = 'Beschreibung zu lang'
        if grund:
            weg[grund] += 1; continue
        key = (art, luecke or 0, re.sub(r'\s', '', w).upper() if art == 'text' else w)
        schluessel[key] += 1
        kand.append((key, {'nr': nr, 'art': art, 'luecke': luecke, 'wert': w, 'text': fb['beschreibung'].strip(),
                           'fehlbild': fb.get('fehlbild'), 'regel': fb.get('regel_des_fehlbilds')}))
    for key, f in kand:
        if schluessel[key] > 1: weg['mehrdeutig (gleiche Antwort bei zwei Fehlbildern)'] += 1
        else: gut.append(f)
    return gut, weg


def sammeln(runden, ohne=()):
    """Je gewählter Aufgabe ein Datensatz für das Paket, plus Zählungen und Abweichungsliste."""
    plan, je, fehler, *_rest = rollend_sql.sammeln(True, runden, ohne)
    if fehler: raise SystemExit('rollend_sql meldet Fehler:\n' + '\n'.join(fehler[:20]))
    aus, quelle = eingespielt()
    rep = repo_eintraege()
    je_einheit_text = defaultdict(lambda: defaultdict(list))   # einheit_id -> md5(text) -> [r]
    for (eid, r), row in aus.items():
        je_einheit_text[eid][md5(row['f'].get('text', ''))].append(r)
    zeilen, abw, fehlt, z = [], [], [], Counter()
    weg = Counter()
    je_typ = defaultdict(Counter)
    for t, rows in je.items():
        eid = plan['einheiten'][t]['id']
        for k, row in rows:
            e = rep[k]
            z['aufgaben'] += 1
            r = row['r']
            ein = aus.get((eid, r))
            verschoben = None
            if ein is None or md5(ein['f'].get('text', '')) != md5(row['f'].get('text', '')):
                kand = je_einheit_text[eid].get(md5(row['f'].get('text', '')), [])
                if len(kand) == 1 and kand[0] != r:
                    verschoben, r, ein = r, kand[0], aus[(eid, kand[0])]
            if ein is None:
                fehlt.append(f'{k}: an Einheit {eid} ({t}) Platz {r} ist nichts eingespielt'); z['nicht_eingespielt'] += 1; continue
            if verschoben is not None:
                abw.append(f'{k}: Platz {verschoben} laut Datei, eingespielt auf Platz {r} (gleicher Fragetext) – zugeordnet über den Text')
            anders = [f for f in INHALT if json.dumps(ein.get(f), sort_keys=True) != json.dumps(row.get(f), sort_keys=True)]
            sonst = [f for f in set(ein) | set(row) if f not in INHALT and f != 'r' and json.dumps(ein.get(f), sort_keys=True) != json.dumps(row.get(f), sort_keys=True)]
            regel = e.get('regel') or None
            if regel and not KENNUNG.match(regel): raise SystemExit(f'{k}: Regel „{regel}“ ist keine Kennung')
            n_fb = len(e.get('fehlbilder') or [])
            z['fehlbilder'] += n_fb
            z['fehlbilder_mit_kennung'] += sum(1 for f in e.get('fehlbilder') or [] if f.get('fehlbild'))
            if anders:
                abw.append(f'{k} (Einheit {eid}, Platz {r}): Datei weicht vom Eingespielten ab in {", ".join(anders)} – Fehlbilder ({n_fb}) NICHT übernommen'
                           + (', Regel übernommen' if regel else ''))
                fb, w = [], Counter({'Aufgabe nach dem Einspielen geändert': n_fb})
                z['abweichend'] += 1
            else:
                fb, w = fehlbilder(e, ein)
                if sonst: abw.append(f'{k} (Einheit {eid}, Platz {r}): nur {", ".join(sorted(sonst))} anders – Fehlbilder übernommen'); z['abweichend_sonst'] += 1
            weg.update(w)
            y = ein['y']
            je_typ[y]['aufgaben'] += 1
            je_typ[y]['fehlbilder'] += n_fb
            je_typ[y]['eindeutig'] += len(fb)
            z['mit_regel'] += bool(regel)
            z['fb_uebernommen'] += len(fb)
            z['fb_uebernommen_mit_kennung'] += sum(1 for f in fb if f['fehlbild'])
            if not regel and not fb: z['ohne_beides'] += 1; continue
            zeilen.append({'k': k, 'e': eid, 'r': r, 'mt': md5(ein['f'].get('text', '')), 'y': y, 'l': ein['l'],
                           'ma': md5('\n'.join(ein['a'])) if y == 'auswahl' else None, 'o': ein.get('o'), 'regel': regel, 'fb': fb})
    return zeilen, abw, fehlt, z, weg, je_typ


# Runde 14 ist am 28.11.2026 ohne Regel eingespielt worden (tools/tests/aus/rollend14_einspielen.sql, md5 b2d081b8da216e6d45691f55d0e73569: 640 Fehlbilder,
# 0 Regeln). Die Regel-Kennung steht seit dem Nachtrag in den Dateien (inhalte/mathe-profi/rollend-14/regeln.py), kommt aber nur über rb_nachtrag_r14.sql
# in die Datenbank. Damit das alte Paket bei jedem Neuerzeugen byteidentisch bleibt, lässt zeilen_neu die Regel dieser Kennungen weg.
REGEL_ERST_IM_NACHTRAG = ('R14-',)
FEHLBILD_NUR_LESEN_RUNDEN = (14,)   # Nachtrag dieser Runden schreibt keine Fehlbilder (sie sind mit der Runde eingespielt), vergleicht sie nur lesend


def zeilen_neu(plan, je):
    """Für ein Einspiel-Paket von rollend_sql: Regel und Fehlbilder der Aufgaben, wie sie in der Datei stehen (= wie sie gerade eingefügt werden)."""
    rep, zeilen = repo_eintraege(), []
    for t, rows in je.items():
        for k, row in rows:
            e = rep[k]
            regel = None if k.startswith(REGEL_ERST_IM_NACHTRAG) else (e.get('regel') or None)
            if regel and not KENNUNG.match(regel): raise SystemExit(f'{k}: Regel „{regel}“ ist keine Kennung')
            fb, _ = fehlbilder(e, row)
            if not regel and not fb: continue
            zeilen.append({'k': k, 'e': plan['einheiten'][t]['id'], 'r': row['r'], 'mt': md5(row['f'].get('text', '')), 'y': row['y'], 'l': row['l'],
                           'ma': md5('\n'.join(row['a'])) if row['y'] == 'auswahl' else None, 'o': row.get('o'), 'regel': regel, 'fb': fb})
    return zeilen


def q(s):
    return 'null' if s is None else "'" + str(s).replace("'", "''") + "'"


def block(zeilen, titel, probe=False, fb_lesen=False):
    """SQL-Block: prüft Zuordnung, fügt ein (on conflict nichts), prüft jedes Fehlbild an der Datenbank. Eine Transaktion (ein Aufruf).
    fb_lesen (nur Runde 14, FEHLBILD_NUR_LESEN_RUNDEN): schreibt NICHTS in schule.aufgabe_fehlbild; die Fehlbilder (schon mit der Runde eingespielt) werden nur
    gelesen und feldweise mit dem Soll verglichen (fehlend, zusätzlich oder abweichend = Abbruch, alles zurück, auch die Regeln). Neue Regeln: nur alle (Erstlauf)
    oder keine (vollständige Wiederholung); ein Teilvorbestand bricht ab."""
    werte = []
    for x in zeilen:
        js = json.dumps(x['fb'], ensure_ascii=False)
        jo = json.dumps(x['o'], ensure_ascii=False)
        assert '$rbf$' not in js + jo
        werte.append(f"    ({q(x['k'])}, {x['e']}, {x['r']}, {q(x['mt'])}, {q(x['y'])}, {q(x['l'])}, {q(x['ma'])}, $rbf${jo}$rbf$::jsonb, {q(x['regel'])}, $rbf${js}$rbf$::jsonb)")
    n_regel = sum(1 for x in zeilen if x['regel'])
    n_fb = sum(len(x['fb']) for x in zeilen)
    ende = ("  raise exception 'PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt): % Aufgaben, % Regeln neu, % Fehlbilder neu', "
            "array_length(v_ids, 1), n_regel_neu, n_fb_neu;\n" if probe else '')
    text = f"""-- RB-S Regelbezug: {titel}: {len(zeilen)} Aufgaben, {n_regel} Regeln, {n_fb} Fehlbilder. Ein Aufruf, eine Transaktion; Abweichung = alles zurück.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '120s', true);
do $rbnach$
declare z record; a schule.aufgabe; n int; f jsonb; b jsonb; v jsonb; fehler text[] := '{{}}'; v_ids bigint[] := '{{}}'; v_alt schule.aufgabe_fehlbild;
  n_regel_neu int := 0; n_fb_neu int := 0; c int;
begin
  if to_regclass('schule.aufgabe_fehlbild') is null or to_regclass('schule.aufgabe_regel') is null
     or to_regprocedure('schule.fehlbild_finden(schule.aufgabe, jsonb)') is null or to_regprocedure('schule.fehlbild_probeantwort(schule.aufgabe, text, integer, text)') is null then
    raise exception 'RB-S Regelbezug: erst die Migration 20261204_rb_s_regelbezug.sql einspielen'; end if;
  for z in select * from (values
{(',' + chr(10)).join(werte)}
  ) x(k, e, r, mt, y, l, ma, o, regel, fb) loop
    select count(*) into n from schule.aufgabe where einheit_id = z.e and pool = 'uebung' and reihenfolge = z.r;
    if n <> 1 then fehler := fehler || format('%s: %s Übungsaufgaben an Einheit %s, Platz %s', z.k, n, z.e, z.r); continue; end if;
    select * into a from schule.aufgabe where einheit_id = z.e and pool = 'uebung' and reihenfolge = z.r;
    if md5(coalesce(a.frage->>'text', '')) <> z.mt or a.antworttyp is distinct from z.y or a.variante_gruppe is distinct from z.l
       or (z.ma is not null and md5(coalesce((select string_agg(t.x, E'\\n' order by t.o) from jsonb_array_elements_text(a.antworten) with ordinality t(x, o)), '')) <> z.ma) then
      fehler := fehler || format('%s: Aufgabe %s (Einheit %s, Platz %s) ist nicht die erwartete (Fragetext/Typ/Lernkarte/Antworten)', z.k, a.id, z.e, z.r); continue; end if;
    -- Lösung samt Einheit und Toleranz wie eingespielt (jsonb-Gleichheit: Zahlen werden als Zahlen verglichen, 12 = 12.0)
    if a.loesung is distinct from z.o then
      fehler := fehler || format('%s: Aufgabe %s (Einheit %s, Platz %s): Lösung %s statt %s wie eingespielt', z.k, a.id, z.e, z.r, a.loesung, z.o); continue; end if;
    if a.id = any(v_ids) then fehler := fehler || format('%s: Aufgabe %s doppelt zugeordnet', z.k, a.id); continue; end if;
    v_ids := v_ids || a.id;
    if z.regel is not null then
      insert into schule.aufgabe_regel (aufgabe_id, regel) values (a.id, z.regel) on conflict do nothing;
      get diagnostics c = row_count; n_regel_neu := n_regel_neu + c;
      if (select r.regel from schule.aufgabe_regel r where r.aufgabe_id = a.id) is distinct from z.regel then
        fehler := fehler || format('%s: Aufgabe %s hat schon eine andere Regel', z.k, a.id); end if;
    end if;
    for f in select * from jsonb_array_elements(z.fb) loop
      insert into schule.aufgabe_fehlbild (aufgabe_id, nr, art, luecke, wert, beschreibung, fehlbild, regel)
      values (a.id, (f->>'nr')::smallint, f->>'art', (f->>'luecke')::smallint, f->>'wert', f->>'text', f->>'fehlbild', f->>'regel') on conflict do nothing;
      get diagnostics c = row_count; n_fb_neu := n_fb_neu + c;
      select * into v_alt from schule.aufgabe_fehlbild x where x.aufgabe_id = a.id and x.nr = (f->>'nr')::smallint;
      if v_alt.nr is null or (v_alt.art, v_alt.luecke, v_alt.wert, v_alt.beschreibung, v_alt.fehlbild, v_alt.regel)
           is distinct from (f->>'art', (f->>'luecke')::smallint, f->>'wert', f->>'text', f->>'fehlbild', f->>'regel') then
        fehler := fehler || format('%s: Fehlbild %s steht schon anders da (oder gleicher Schlüssel unter anderer Nummer)', z.k, f->>'nr'); continue; end if;
      v := schule.fehlbild_probeantwort(a, f->>'art', (f->>'luecke')::int, f->>'wert');
      b := schule.antwort_bewerten(a, v);
      if not coalesce((b->>'format_ok')::boolean, false) or coalesce((b->>'richtig')::boolean, true) then
        fehler := fehler || format('%s: Fehlbild %s – Antwort %s wird nicht als gültig und falsch bewertet (%s)', z.k, f->>'nr', v, b); continue; end if;
      if schule.fehlbild_finden(a, v) is distinct from (f->>'nr')::smallint then
        fehler := fehler || format('%s: Fehlbild %s wird an der Antwort %s nicht wiedererkannt', z.k, f->>'nr', v); end if;
    end loop;
    if (select count(*) from schule.aufgabe_fehlbild x where x.aufgabe_id = a.id) <> jsonb_array_length(z.fb) then
      fehler := fehler || format('%s: Aufgabe %s hat andere Fehlbilder in der Datenbank als im Paket', z.k, a.id); end if;
  end loop;
  if array_length(fehler, 1) > 0 then raise exception 'RB-S Regelbezug ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler[1:40], ' | '); end if;
  if coalesce(array_length(v_ids, 1), 0) <> {len(zeilen)}
     or (select count(*) from schule.aufgabe_regel where aufgabe_id = any(v_ids)) <> {n_regel}
     or (select count(*) from schule.aufgabe_fehlbild where aufgabe_id = any(v_ids)) <> {n_fb} then
    raise exception 'RB-S Regelbezug ABBRUCH: Zählung stimmt nicht (Aufgaben %, erwartet {len(zeilen)})', array_length(v_ids, 1); end if;
{ende}  raise notice 'RB-S Regelbezug: % Aufgaben, % Regeln neu, % Fehlbilder neu (zweiter Lauf: 0 und 0)', array_length(v_ids, 1), n_regel_neu, n_fb_neu;
end $rbnach$;
"""
    if not fb_lesen:
        return text
    teile = [
        ("""      insert into schule.aufgabe_fehlbild (aufgabe_id, nr, art, luecke, wert, beschreibung, fehlbild, regel)
      values (a.id, (f->>'nr')::smallint, f->>'art', (f->>'luecke')::smallint, f->>'wert', f->>'text', f->>'fehlbild', f->>'regel') on conflict do nothing;
      get diagnostics c = row_count; n_fb_neu := n_fb_neu + c;
""", ""),
        ("Fehlbild %s steht schon anders da (oder gleicher Schlüssel unter anderer Nummer)", "Fehlbild %s fehlt oder weicht vom Soll ab (nur lesender Vergleich, es wird nichts geschrieben)"),
        ("  if coalesce(array_length(v_ids, 1), 0) <> ",
         "  if n_regel_neu not in (0, " + str(n_regel) + ") then\n    raise exception 'RB-S Regelbezug ABBRUCH: % Regeln neu, erlaubt sind nur 0 (Wiederholung) oder " + str(n_regel) + " (Erstlauf) – Teilvorbestand', n_regel_neu; end if;\n"
         "  if coalesce(array_length(v_ids, 1), 0) <> "),
        ("-- RB-S Regelbezug: " + titel + ":", "-- RB-S Regelbezug (Fehlbilder nur lesend verglichen, nicht geschrieben): " + titel + ":"),
    ]
    for alt, neu in teile:
        assert text.count(alt) == 1, alt[:60]
        text = text.replace(alt, neu)
    assert 'insert into schule.aufgabe_fehlbild' not in text
    return text


def main():
    argv = sys.argv[1:]
    runden, ohne = rollend_sql.optionen(argv)
    zeilen, abw, fehlt, z, weg, je_typ = sammeln(runden, ohne)
    if '--json' in argv:
        print(json.dumps({'runden': runden, 'zahlen': z, 'nicht_uebernommen': weg, 'je_typ': je_typ,
                          'abweichungen': abw, 'nicht_eingespielt': fehlt}, ensure_ascii=False, indent=1)); return
    if '--sql' in argv:
        if fehlt:
            print('ABBRUCH: Aufgaben ohne eingespieltes Gegenstück:\n' + '\n'.join(fehlt), file=sys.stderr); sys.exit(1)
        if not zeilen:
            print('ABBRUCH: nichts zu übernehmen', file=sys.stderr); sys.exit(1)
        for a in abw: print('Abweichung:', a, file=sys.stderr)
        print(block(zeilen, f'Nachtrag rollend-{",".join(map(str, runden))}', '--probe' in argv, fb_lesen=all(r in FEHLBILD_NUR_LESEN_RUNDEN for r in runden)), end='')
        return
    print(f'Runden {",".join(map(str, runden))}: {z["aufgaben"]} Aufgaben, mit Regel {z["mit_regel"]}; Fehlbilder {z["fehlbilder"]} '
          f'(mit Kennung {z["fehlbilder_mit_kennung"]}), übernehmbar {z["fb_uebernommen"]} (mit Kennung {z["fb_uebernommen_mit_kennung"]}); '
          f'ohne Regel und ohne Fehlbild {z["ohne_beides"]}; Paket: {len(zeilen)} Aufgaben')
    for y, c in sorted(je_typ.items()):
        print(f'  {y:9} {c["aufgaben"]:5} Aufgaben, {c["fehlbilder"]:5} Fehlbilder, davon eindeutig zuordenbar {c["eindeutig"]}')
    if weg:
        print('Nicht übernommen:', '; '.join(f'{g}: {n}' for g, n in weg.most_common()))
    print(f'Abweichungen Datei <-> eingespielt: {len(abw)}')
    for a in abw: print('  ' + a)
    if fehlt:
        print(f'Nicht eingespielt: {len(fehlt)}')
        for a in fehlt: print('  ' + a)


if __name__ == '__main__':
    main()
