"""Neunzehnte Runde, Teil A, Klasse 6 (Zweig durchsicht-kl6): Gesamtdurchsicht und Nachbesserung freigegebener Themen.

Jeder bearbeitete Generator hat am Ende einen Abschnitt DURCHSICHT. Er läuft nach allen bisherigen Abschnitten (Umbau, SCHWER, BEFUNDE, LUECKEN).
- Aufgaben: Werkzeug der Dreizehnten Runde (_befunde.Befunde): stufe (nur s), loesung (o/h/w/c), ersetze (neue Frage an derselben Stelle,
  alter Fragetext in die Liste „ersetzt“), neu (zusätzliche Übung hinter der letzten Aufgabe der Lernkarte). Eigener fester Zufallsstart.
- Lernkarten: karte(...) ändert einzelne Felder einer Lernkarte (Lernziel, Titel und Reihenfolge bleiben) und merkt sich „vorher/nachher“.
Nachweis: _durchsicht_kl6_nachweis.py.
"""
import json
from pathlib import Path

from _befunde import Befunde, befunde_anwenden  # noqa: F401

PROTOKOLL = Path('/tmp')


def karte(datei, lz, satz, **felder):
    """Felder einer Lernkarte ersetzen. satz: „vorher → nachher“ in einem Satz (für den Bericht)."""
    assert set(felder) <= {'einstieg', 'woerter', 'bild', 'schritte', 'fehler', 'fehler_bild', 'regel', 'probe'}, felder
    e = next(x for x in datei['inhalt']['etappen'] if x['lernziel'] == lz)
    for k, v in felder.items():
        assert e.get(k) != v, (lz, k, 'unverändert')
        e[k] = v
    p = PROTOKOLL / f'durchsicht_karten_{datei["thema_schluessel"]}.json'
    alt = json.loads(p.read_text()) if p.exists() else {}
    alt[lz] = satz
    p.write_text(json.dumps(alt, ensure_ascii=False, indent=1))
    return e


def schritt_einfuegen(datei, lz, index, schritt, satz):
    e = next(x for x in datei['inhalt']['etappen'] if x['lernziel'] == lz)
    neu = list(e['schritte']); neu.insert(index, schritt)
    return karte(datei, lz, satz, schritte=neu)
