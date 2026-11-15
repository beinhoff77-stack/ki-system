"""Verständliche Erklärungen, Klasse 5 (Siebte Runde, Pflicht seit 15.11.).

Der Abschnitt KLAR eines Generators überschreibt Felder der Lernkarten ERST NACH dem Erzeugen der Aufgaben.
Grund: Die Generatoren benutzen die alten Beispieltexte (schritte) zum Vermeiden von Dopplungen. Würden die neuen
Texte vorher eingesetzt, könnten sich Aufgaben ändern. So bleiben alle Aufgaben wörtlich gleich (wie _verbot im Muster).
"""
import re

FELDER = {'einstieg', 'woerter', 'schritte', 'regel', 'fehler', 'probe', 'bild'}
VERBOTEN = re.compile(r'\b(offensichtlich|einfach|trivial)\w*', re.I)


def klar(datei, klar_felder):
    etappen = datei['inhalt']['etappen']
    namen = [e['lernziel'] for e in etappen]
    assert sorted(klar_felder) == sorted(namen), ('KLAR passt nicht zu den Lernkarten', sorted(set(namen) ^ set(klar_felder)))
    for e in etappen:
        k = klar_felder[e['lernziel']]
        assert set(k) <= FELDER, (e['lernziel'], set(k) - FELDER)
        assert {'einstieg', 'woerter', 'schritte', 'regel'} <= set(k), (e['lernziel'], 'einstieg, woerter, schritte, regel sind Pflicht')
        assert 3 <= len(k['schritte']) <= 5, (e['lernziel'], '3–5 Schritte')
        assert any('⟦' in s for s in k['schritte']), (e['lernziel'], 'Ergebnis in ⟦…⟧')
        assert '⟦' in k['einstieg'], (e['lernziel'], 'Fachwort am Ende des Einstiegs in ⟦…⟧')
        assert all(len(w) == 2 and w[0] and w[1] for w in k['woerter']), e['lernziel']
        for feld in ('einstieg', *k['schritte']):
            text = k['einstieg'] if feld == 'einstieg' else feld
            assert not VERBOTEN.search(text), (e['lernziel'], text)
        for feld, wert in k.items():
            for t in (wert if isinstance(wert, list) else [wert]):
                t = str(t)
                assert t.count('⟦') == t.count('⟧'), (e['lernziel'], feld, t)
        e.update(k)
    return datei
