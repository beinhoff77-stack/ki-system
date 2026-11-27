# Arbeitsskripte lehrplan-lb (Stand 25.11.2026)

Diese Skripte haben die Prüf- und Korrekturdateien in `inhalte/pruefung/lehrplan/` erzeugt. Sie lagen bisher nur in der Arbeitsumgebung (`/tmp/lpw`) und sind hier zur Nachvollziehbarkeit abgelegt.
Sie sind **nicht ohne Weiteres lauffähig**: Pfade zeigen auf `/tmp/lp` (Arbeitskopie) und `/tmp/lpw` (Arbeitsordner), und die Lese-Abzüge aus der Datenbank (`lk_db.json`, `db_*.json`, Punkttexte, Lernstand der Kinder, Probestand `mock_lk.sql`) sind bewusst **nicht** im Repo – sie enthalten Kopien der echten Datenbank bzw. Lernstände.

| Skript | wofür | Ergebnis im Repo |
|---|---|---|
| `rs_daten.py`, `rs_erzeuge.py` | LP-RS: Realschul-Lehrplan Punkt für Punkt | `rs_pruefung_2211.*`, `rs_korrektur_2211.sql` |
| `lk_map.py` | Zuordnung jedes Lehrplanpunkts (Gym, RS, IB) zu Thema und Etappen, Format `eid thema etappen [+N] [-X] #notiz` | Grundlage aller LK-Dateien |
| `lk_proc.py` | Rolle, Lage, Verstöße, Kinderstand (nur Nummern), SQL | `lk_pruefung_2211.md`, `lk_daten_2211.json`, `lk_korrektur_2211.sql` |
| `lk2.py`, `lk2_md.py` | Teilung, Zusatz-Regel, Kanten je Schulart, Mehrklassen-Zählung, Kür/Pflicht je Etappe | `lk_teilung_2211.json/.md` |
| `lk_kuer_entscheid.py` | LK-D 4 B1: inhaltliche Pflicht/Kür-Entscheidungen je Etappe und Schulart (Gym, RS I, RS II/III) mit Quellen-Punkt | `status_je_schulart` in `lk_teilung_2211.json` |
| `rev.py` | Prüfliste nicht zugeordneter Etappen je Schulart | – |
| `db.py`, `vorschlag.py`, `erzeuge*.py`, `pruefe*.py`, `reise.py` | ältere Runden (Voraussetzungen, Themenliste, Reise-Aufbau) | `themenliste.json` u. a. |

Lernkarten und Aufgaben-Generatoren stehen nicht hier, sondern in `inhalte/generatoren/` (`_lk_etappen_2211.py`, `_lk_einspiel_2211.py`, `_nt_2211.py`, `_nt_2311.py`).
