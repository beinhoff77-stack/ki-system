"""Nachweis Einundzwanzigste Runde, Teil A: Was sich gegenüber origin/lernen-app geändert hat, ist genau das Geplante.

Liest die Berichte /tmp/bereinigen_<thema>.json (entstehen beim Bauen). Prüft je geändertem Thema:
- jede alte Aufgabe ist Zeichen für Zeichen noch da, oder sie steht im Bericht als entfallen/weg/ersetzt,
  oder sie ist (bis auf l und t) gleich in ein anderes Thema/eine andere Lernkarte umgezogen;
- jede neue Aufgabe ist alt, umgezogen (gleich bis auf l, t) oder im Bericht als neu/knobel/ersetzt geführt;
- Lernkarten-Texte ändern sich nur bei Karten, die im Bericht unter „karte“ stehen; umgezogene Karten sind gleich.
Aufruf: python3 -I _bereinigen_nachweis.py (im Ordner generatoren, nach dem Bauen)."""
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
BASIS = sys.argv[1] if len(sys.argv) > 1 else 'origin/lernen-app'


def alt(pfad):
    try: return json.loads(subprocess.run(['git', '-C', str(WURZEL), 'show', f'{BASIS}:{pfad}'], capture_output=True, text=True, check=True).stdout)
    except subprocess.CalledProcessError: return None


namen = subprocess.run(['git', '-C', str(WURZEL), 'diff', '--name-only', BASIS, '--', 'inhalte/themen'], capture_output=True, text=True).stdout.split()
namen += subprocess.run(['git', '-C', str(WURZEL), 'ls-files', '-m', '--', 'inhalte/themen'], capture_output=True, text=True).stdout.split()
namen = sorted(set(namen))
ALT, NEU, BER = {}, {}, {}
for n in namen:
    t = Path(n).stem
    ALT[t] = alt(n); NEU[t] = json.loads((WURZEL / n).read_text(encoding='utf-8'))
    bp = Path('/tmp') / f'bereinigen_{t}.json'
    BER[t] = json.loads(bp.read_text()) if bp.exists() else {}

ohne = lambda a: json.dumps({k: v for k, v in a.items() if k not in ('l', 't')}, sort_keys=True, ensure_ascii=False)  # noqa: E731
voll = lambda a: json.dumps(a, sort_keys=True, ensure_ascii=False)  # noqa: E731
alle_alt_ohne = {}
for t, d in ALT.items():
    for a in d['aufgaben']: alle_alt_ohne.setdefault(ohne(a), []).append((t, a['l']))
alle_neu_ohne = {}
for t, d in NEU.items():
    for a in d['aufgaben']: alle_neu_ohne.setdefault(ohne(a), []).append((t, a['l']))

fehler = []
for t in namen:
    t = Path(t).stem
    b = BER[t]
    alt_v = {voll(a) for a in ALT[t]['aufgaben']}
    neu_v = {voll(a) for a in NEU[t]['aufgaben']}
    weg_texte = {x['text'] for x in b.get('weg', [])} | {x for e in b.get('entfaellt', []) for x in e['texte']} | {x['alt'] for x in b.get('ersetzt', [])}
    neu_texte = {x['text'] for k in ('neu', 'knobel') for x in b.get(k, [])} | {x['neu'] for x in b.get('ersetzt', [])}
    for a in ALT[t]['aufgaben']:
        if voll(a) in neu_v: continue
        if a['f']['text'] in weg_texte: continue
        if ohne(a) in alle_neu_ohne: continue  # umgezogen (l/t angepasst)
        fehler.append(f'{t}: alte Aufgabe verändert oder verschwunden: {a["l"]}/{a["p"]} „{a["f"]["text"][:70]}“')
    for a in NEU[t]['aufgaben']:
        if voll(a) in alt_v: continue
        if ohne(a) in alle_alt_ohne: continue  # umgezogen
        if a['f']['text'] in neu_texte: continue
        fehler.append(f'{t}: neue Aufgabe ohne Eintrag im Bericht: {a["l"]}/{a["p"]} „{a["f"]["text"][:70]}“')
    ka = {e['lernziel']: e for e in ALT[t]['inhalt']['etappen']}
    kn = {e['lernziel']: e for e in NEU[t]['inhalt']['etappen']}
    geaendert_ok = {x['lz'] for x in b.get('karte', [])}
    for lz, e in kn.items():
        if lz in ka:
            if voll(e) != voll(ka[lz]) and lz not in geaendert_ok: fehler.append(f'{t}: Lernkarte {lz} geändert ohne Eintrag')
        else:
            q = next((x['quelle'] for x in b.get('karte_her', []) if x['lz'] == lz), None)
            if q is None: fehler.append(f'{t}: neue Lernkarte {lz} ohne Eintrag')
            else:
                eq = next(x for x in (ALT.get(q) or alt(f'inhalte/themen/{q}.json'))['inhalt']['etappen'] if x['lernziel'] == lz)
                if voll(eq) != voll(e) and lz not in geaendert_ok: fehler.append(f'{t}: umgezogene Lernkarte {lz} weicht von {q} ab')
    for k in ('thema_schluessel', 'thema_id', 'block_id', 'klasse'):
        if ALT[t][k] != NEU[t][k]: fehler.append(f'{t}: Feld {k} geändert')
    print(f'{t}: alt {len(ALT[t]["aufgaben"])} → neu {len(NEU[t]["aufgaben"])} Aufgaben, Lernkarten {len(ka)} → {len(kn)}')
print('\n'.join(fehler) if fehler else 'NACHWEIS OK')
sys.exit(1 if fehler else 0)
