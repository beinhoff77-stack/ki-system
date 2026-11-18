"""Nachweis Korrektur neuer Aufgaben Klasse 8 (18.11.): gegen origin/lernen-app
- alle Felder außer 'aufgaben' unverändert;
- alte Aufgaben (Fragetext gab es schon im Commit 4eda8cb) Zeichen für Zeichen unverändert;
- geänderte Aufgaben behalten Lernkarte, Pool, Stufe, Typ und Antwortform (Mengen je (l, p, s, g, y) gleich).
Aufruf: python3 -I inhalte/generatoren/_korrektur_kl8_nachweis.py <thema>"""
import collections, json, subprocess, sys
from pathlib import Path

thema = sys.argv[1]
pfad = f'inhalte/themen/{thema}.json'
git = lambda ref: subprocess.run(['git', 'show', ref], capture_output=True, text=True, check=True).stdout
vorher = json.loads(git(f'origin/lernen-app:{pfad}'))
nachher = json.loads(Path(pfad).read_text(encoding='utf-8'))
alt_texte = set()
for f in subprocess.run(['git', 'ls-tree', '--name-only', '4eda8cb', 'inhalte/themen/'], capture_output=True, text=True, check=True).stdout.split():
    if f.endswith('.json'):
        alt_texte |= {a['f']['text'] for a in json.loads(git(f'4eda8cb:{f}')).get('aufgaben', [])}
for k in set(vorher) | set(nachher):
    if k != 'aufgaben': assert vorher.get(k) == nachher.get(k), f'Feld {k} geändert'
voll = lambda a: json.dumps(a, ensure_ascii=False, sort_keys=True)
art = lambda a: (a['l'], a['p'], a['s'], a.get('g'), a['y'])
assert collections.Counter(map(art, vorher['aufgaben'])) == collections.Counter(map(art, nachher['aufgaben'])), 'Lernkarte/Pool/Stufe/Typ/Antwortform verschoben'
alt_v = collections.Counter(voll(a) for a in vorher['aufgaben'] if a['f']['text'] in alt_texte)
alt_n = collections.Counter(voll(a) for a in nachher['aufgaben'] if a['f']['text'] in alt_texte)
assert alt_v == alt_n, f'alte Aufgabe geändert: {list((alt_v - alt_n).elements())[:1] or list((alt_n - alt_v).elements())[:1]}'
v = collections.Counter(map(voll, vorher['aufgaben'])); n = collections.Counter(map(voll, nachher['aufgaben']))
geaendert = sum((v - n).values())
print(f'NACHWEIS OK {thema}: alte Aufgaben unverändert ({sum(alt_n.values())}), geänderte neue Aufgaben {geaendert}')
