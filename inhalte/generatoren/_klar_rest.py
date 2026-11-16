"""Verständliche Erklärungen für nachgebaute Themen (Runde 7b, Pflicht seit 15.11.).

Wie _klar_kl6.py, aber für Generatoren mit `baue(...)` aus _nachbau.py: `baue` erzeugt die Aufgaben und schreibt die Datei sofort.
`mit_klar(baue, KLAR)` legt sich um `baue`: Erst werden die Aufgaben mit den ALTEN Beispieltexten erzeugt (baue meidet sie),
dann werden die Felder aus KLAR in die Lernkarten übernommen (geprüft wie in _klar_kl6.klar) und die Datei neu geschrieben.
So bleiben alle Aufgaben wörtlich gleich.
"""
import json

from _klar_kl6 import klar
from _nachbau import THEMEN


def mit_klar(baue, klar_felder):
    def baue_klar(meta, *args, **kwargs):
        d = baue(meta, *args, **kwargs)
        klar(d, klar_felder)
        pfad = THEMEN / f"{meta['thema_schluessel']}.json"
        pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        return d
    return baue_klar
