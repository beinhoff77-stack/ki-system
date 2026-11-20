"""Neunzehnte Runde, Teil A (durchsicht-kl7): Gesamtdurchsicht der Themen der Klasse 7.

Wie die Dreizehnte Runde (_befunde.py): Jede Korrektur wird NACH dem vollständigen Bau (inkl. aller früheren Runden) auf die
fertige Datei angewendet und findet ihre Aufgabe über Lernkarte + genauen Fragetext. Arten:
  stufe(...)   a) nur Feld s ändern
  loesung(...) b) o / h / w / c berichtigen
  ersetze(...) c) Aufgabe durch eine bessere ersetzen (gleiche Stelle, gleicher Pool); alter Fragetext → Liste „ersetzt“
  neu(...)     d) zusätzliche Übung (hinter den bisherigen Aufgaben der Lernkarte)
  karte(...)   e) Felder einer Lernkarte verbessern (einstieg, woerter, schritte, fehler, fehler_bild, regel, probe, bild);
               Lernziel, Titel und Reihenfolge bleiben.
Nachweis: python3 -I inhalte/generatoren/_durchsicht_nachweis.py <thema>
"""
import json
from pathlib import Path

from _befunde import Befunde

THEMEN = Path(__file__).resolve().parent.parent / 'themen'
KARTENFELDER = {'einstieg', 'woerter', 'schritte', 'fehler', 'fehler_bild', 'regel', 'probe', 'bild'}


class Durchsicht(Befunde):
    def __init__(self, thema, seed):
        super().__init__(thema, seed)
        self.karten = []          # (lz, felder, vorher_nachher)

    def karte(self, lz, grund, **felder):
        assert set(felder) <= KARTENFELDER, felder
        self.karten.append((lz, felder, grund))

    def anwenden(self, d):
        for lz, felder, grund in self.karten:
            e = [x for x in d['inhalt']['etappen'] if x['lernziel'] == lz]
            assert len(e) == 1, lz
            for k, v in felder.items():
                if callable(v): v = v(json.loads(json.dumps(e[0].get(k))))  # Änderung relativ zum bisherigen Inhalt
                assert e[0].get(k) != v, (lz, k, 'unverändert')
                e[0][k] = v
            self.zaehler['karten'] += 1
        return super().anwenden(d)


def durchsicht_datei(schluessel, ds):
    pfad = THEMEN / f'{schluessel}.json'
    roh = pfad.read_text(encoding='utf-8')
    d = ds.anwenden(json.loads(roh))
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else ''), encoding='utf-8')
    z = ds.zaehler
    print(f'  DURCHSICHT {schluessel}: umgestuft {z["umgestuft"]}, berichtigt {z["berichtigt"]}, ersetzt {z["ersetzt"]}, neu {z["neu"]}, Lernkarten {z["karten"]}')
    (Path('/tmp') / f'durchsicht_{schluessel}.json').write_text(json.dumps(
        {'ersetzt': ds.ersetzt, 'zaehler': dict(z), 'karten': [(l, sorted(f), g) for l, f, g in ds.karten]}, ensure_ascii=False, indent=1))
    return d
