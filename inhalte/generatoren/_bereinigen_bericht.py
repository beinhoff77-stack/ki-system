"""Listen für den Bericht der Einundzwanzigsten Runde, Teil A (aus /tmp/bereinigen_<thema>.json, entstehen beim Bauen).
Schreibt inhalte/postfach/bereinigen-listen.md. Aufruf nach dem Bauen aller Themen: python3 -I _bereinigen_bericht.py"""
import json
from pathlib import Path

W = Path(__file__).resolve().parent.parent
B = {p.stem.replace('bereinigen_', ''): json.loads(p.read_text()) for p in sorted(Path('/tmp').glob('bereinigen_*.json')) if 'probe' not in p.name}
TH = {p.stem: json.loads(p.read_text(encoding='utf-8')) for p in (W / 'themen').glob('*.json')}
wo = {}
for t, d in TH.items():
    for a in d['aufgaben']: wo.setdefault(a['f']['text'], []).append((t, a['l'], a['p']))
esc = lambda t: str(t).replace('|', '\\|')  # noqa: E731
z = []
z.append('# Listen zur Einundzwanzigsten Runde, Teil A (Zweig bereinigen)\n')
z.append('Erzeugt von `inhalte/generatoren/_bereinigen_bericht.py`. Bericht: `inhalte/postfach/bereinigen.md`.\n')
z.append('## 1. Umgezogene Aufgaben (gleicher Fragetext, neues Thema oder neue Lernkarte)\n')
z.append('Im alten Thema sperren bzw. Lernstand mitnehmen; im neuen Thema als neue Aufgabe einspielen. Fragetext, Lösung, Stufe, Typ unverändert; nur `l` und `t` neu.\n')
z.append('| altes Thema / Lernkarte | neues Thema / Lernkarte | Pool | Stufe/Typ | Fragetext |\n|---|---|---|---|---|')
n = 0
for t, b in B.items():
    for x in b.get('her', []):
        z.append(f"| {x['quelle']} | {t}/{x['lz']} | {x['p']} | {x['s']}/{x['g'] or '–'} | {esc(x['text'])} |"); n += 1
    for x in b.get('innen', []):
        z.append(f"| {t}/{x['von']} | {t}/{x['lz']} | {x['p']} | {x['s']}/{x['g'] or '–'} | {esc(x['text'])} |"); n += 1
z.append(f'\nZusammen: {n} Aufgaben. Ganze Karten, die umgezogen sind, stehen im Bericht (Umzugstabelle) und hier nicht einzeln.\n')
z.append('## 2. Ersetzt (alter Fragetext → neuer Fragetext, Lösung gleich)\n')
z.append('| Thema / Lernkarte | Pool | alt | neu |\n|---|---|---|---|')
n = 0
for t, b in B.items():
    for x in b.get('ersetzt', []): z.append(f"| {t}/{x['lz']} | {x['p']} | {esc(x['alt'])} | {esc(x['neu'])} |"); n += 1
z.append(f'\nZusammen: {n}.\n')
z.append('## 3. Einzeln entfernte Aufgaben (sperren)\n')
z.append('Aufgaben aus Lernkarten, die bleiben. Steht in der letzten Spalte ein Ziel, ist die Aufgabe dorthin umgezogen (Liste 1).\n')
z.append('| Thema / Lernkarte | Pool | Stufe/Typ | Fragetext | jetzt in |\n|---|---|---|---|---|')
n = 0
for t, b in B.items():
    for x in b.get('weg', []):
        jetzt = ', '.join(f'{tt}/{ll}' for tt, ll, pp in wo.get(x['text'], []) if tt != t or ll != x['lz']) or '–'
        z.append(f"| {t}/{x['lz']} | {x['p']} | {x['s']}/{x['g'] or '–'} | {esc(x['text'])} | {jetzt} |"); n += 1
z.append(f'\nZusammen: {n}.\n')
z.append('## 4. Entfallene Lernkarten: Aufgaben, die nirgends mehr stehen (sperren)\n')
z.append('| Thema / Lernkarte | Aufgaben der Karte | davon umgezogen | entfallen |\n|---|---|---|---|')
for t, b in B.items():
    for x in b.get('entfaellt', []):
        um = sum(1 for tx in x['texte'] if tx in wo)
        z.append(f"| {t}/{x['lz']} | {x['aufgaben']} | {um} | {x['aufgaben'] - um} |")
z.append('')
z.append('## 5. Neue Aufgaben\n')
z.append('| Thema / Lernkarte | Pool | Stufe/Typ | Fragetext |\n|---|---|---|---|')
n = 0
for t, b in B.items():
    for k in ('neu', 'knobel'):
        for x in b.get(k, []):
            z.append(f"| {t}/{x['lz']} | {x.get('p', 'bonus' if k == 'knobel' else 'uebung')} | {x['s']}/{x['g'] or '–'} | {esc(x['text'])} |"); n += 1
z.append(f'\nZusammen: {n}.\n')
z.append('## 6. Nur Lösungsweg umformuliert (Fragetext gleich)\n')
for t, b in B.items():
    for x in b.get('loesungsweg', []): z.append(f"- {t}/{x['lz']} ({x['p']}): {esc(x['text'])}")
z.append('\n## 7. Nicht übernommen (beim Zusammenlegen verworfen, Grund)\n')
z.append('| Ziel | aus | Grund | Fragetext |\n|---|---|---|---|')
for t, b in B.items():
    for x in b.get('verworfen', []):
        if any(tt == t for tt, ll, pp in wo.get(x['text'], [])): continue  # später doch übernommen
        z.append(f"| {t}/{x['lz']} | {x['quelle']} | {x['grund']} | {esc(x['text'][:100])} |")
(W / 'postfach' / 'bereinigen-listen.md').write_text('\n'.join(z) + '\n', encoding='utf-8')
print('geschrieben:', len(z), 'Zeilen')
