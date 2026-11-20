"""Nachweis „Inhaltliche Prüfung der neuen Aufgaben“, Klasse 6 (Zweig stufen-kl6).

python3 -I inhalte/generatoren/_stufen_kl6_pruefung_nachweis.py <thema> [stand] [vor_runde]

stand     = Vergleichsstand (Standard origin/lernen-app)
vor_runde = Stand vor der Zwanzigsten Runde (Standard 4eda8cb). „Neu“ ist eine Übung/Knobel-Bordkarte, deren Fragetext es
            dort in keiner Themendatei gab; „alt“ ist jede andere Aufgabe.

Geprüft gegen <stand>:
1. Kopf und Lernkarten unverändert. Ausnahme: das Feld „klasse“, wenn es jetzt genau dem Eintrag in inhalte/themenliste.json
   entspricht (der Generator liest die Themenliste; die Datei auf lernen-app war dort veraltet).
2. Gleiche Zahl und Reihenfolge der Aufgaben; an jeder Stelle gleiche Lernkarte, gleicher Pool, gleiche Stufe s, gleicher Typ g.
3. Jede alte Aufgabe ist Zeichen für Zeichen gleich (alle Felder).
4. Geänderte Aufgaben sind neue Aufgaben (Übung oder Bonus); ihr neuer Fragetext ist kein alter Fragetext.
5. tools/inhalt_pruefen.py: OK und 0 Gruppen „gleich gebaut hintereinander“ – für die Datei und für die Kopie ohne
   überzählige Übungen (Übungen ohne g, Stand „nach dem Sperren“).
Ausgabe: Zahl der neuen Aufgaben, Zahl der geänderten, Liste der geänderten Fragetexte (vorher → nachher, gekürzt).
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]


def git_json(stand, pfad):
    return json.loads(subprocess.run(['git', '-C', str(WURZEL), 'show', f'{stand}:{pfad}'], capture_output=True, check=True, text=True).stdout)


def alte_texte(stand):
    namen = subprocess.run(['git', '-C', str(WURZEL), 'ls-tree', '--name-only', stand, 'inhalte/themen/'],
                           capture_output=True, check=True, text=True).stdout.split()
    S = set()
    for n in namen:
        if not n.endswith('.json') or n.endswith('themenliste.json'):
            continue
        try:
            d = git_json(stand, n)
        except Exception:
            continue
        for a in d.get('aufgaben', []) if isinstance(d, dict) else []:
            S.add(a['f']['text'])
    return S


def pruefskript(d, name):
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / name
        p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding='utf-8')
        r = subprocess.run([sys.executable, '-I', str(WURZEL / 'tools/inhalt_pruefen.py'), str(p)], capture_output=True, text=True)
    gruppen = [z for z in r.stdout.splitlines() if 'Gruppen „gleich gebaut hintereinander“' in z]
    null = bool(gruppen) and gruppen[-1].strip().endswith(': 0')
    kopf = [z for z in r.stdout.splitlines() if z.startswith('==')]
    return r.returncode == 0 and null, (kopf or [''])[0][:160]


def main(thema, stand='origin/lernen-app', vor_runde='4eda8cb'):
    pfad = f'inhalte/themen/{thema}.json'
    alt = git_json(stand, pfad)
    neu = json.loads((WURZEL / pfad).read_text(encoding='utf-8'))
    S = alte_texte(vor_runde)
    liste = {x['thema_schluessel']: x for x in json.loads((WURZEL / 'inhalte/themenliste.json').read_text(encoding='utf-8'))}
    F = []
    kopf_a = {k: v for k, v in alt.items() if k not in ('aufgaben', 'klasse')}
    kopf_n = {k: v for k, v in neu.items() if k not in ('aufgaben', 'klasse')}
    if kopf_a != kopf_n:
        F.append('Kopf oder Lernkarten geändert')
    if alt.get('klasse') != neu.get('klasse') and neu.get('klasse') != liste[thema]['klasse']:
        F.append('Feld klasse geändert und nicht gleich der Themenliste')
    A, N = alt['aufgaben'], neu['aufgaben']
    if len(A) != len(N):
        F.append(f'Zahl der Aufgaben {len(A)} → {len(N)}')
    zahl_neu = sum(1 for a in A if a['p'] in ('uebung', 'bonus') and a['f']['text'] not in S)
    geaendert = []
    for i, (a, b) in enumerate(zip(A, N)):
        for k in ('l', 'p', 's', 'g'):
            if a.get(k) != b.get(k):
                F.append(f'Stelle {i}: Feld {k} {a.get(k)!r} → {b.get(k)!r} ({a["f"]["text"][:50]})')
        if a == b:
            continue
        if a['f']['text'] in S or a['p'] not in ('uebung', 'bonus'):
            F.append(f'alte Aufgabe geändert: {a["l"]}: {a["f"]["text"][:70]}')
            continue
        if b['f']['text'] != a['f']['text'] and b['f']['text'] in S:
            F.append(f'neuer Fragetext ist ein alter Fragetext: {b["f"]["text"][:70]}')
        geaendert.append((a, b))
    ok, z = pruefskript(neu, f'{thema}.json')
    print('  Datei: ' + z)
    if not ok:
        F.append('Prüfskript nicht OK oder Gruppen „gleich gebaut hintereinander“ ≠ 0')
    kopie = dict(neu, aufgaben=[a for a in N if not (a['p'] == 'uebung' and 'g' not in a)])
    ok2, z2 = pruefskript(kopie, f'{thema}.json')
    print('  ohne überzählige: ' + z2)
    if not ok2:
        F.append('Prüfskript (ohne überzählige) nicht OK oder Gruppen ≠ 0')
    print(f'{thema}: neue Aufgaben {zahl_neu}, davon geändert {len(geaendert)}')
    for a, b in geaendert:
        felder = [k for k in sorted(set(a) | set(b)) if a.get(k) != b.get(k) and k != 'f'] + \
                 [f'f.{k}' for k in sorted(set(a['f']) | set(b['f'])) if a['f'].get(k) != b['f'].get(k)]
        print(f'  ~ {a["l"]} S{a["s"]} {a.get("g")}: {a["f"]["text"][:80]}  [{", ".join(felder)}]')
    if F:
        print('FEHLER:')
        for f in F:
            print('  ' + f)
        return 1
    print('NACHWEIS OK')
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
