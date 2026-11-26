"""Mathe-Profi, Auftrag 14 Teil A: stabile Kennungen für die 14 Rechenregeln und die 28 tragenden Ideen.

Aufruf: python3 -I inhalte/mathe-profi/regeln-uebersicht/kennungen.py
Schreibt kennungen.json. Die Kennung ist ein sprechender Schlüssel, keine Nummer: Sie hängt weder an der Reihenfolge
der Übersicht noch an den alten Etikett-Nummern. Eine Kennung wird nie geändert und nie neu vergeben.
Das Programm erzwingt das: Gibt es kennungen.json schon, muss jede dort stehende Kennung weiter vorkommen
(Regel- wie Fehlbild-Kennung); sonst bricht es ab. Neue dürfen dazukommen.
"""
import importlib.util
import io
import contextlib
import json
import os
import sys

sys.dont_write_bytecode = True
HIER = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("gesetzbuch", os.path.join(HIER, "gesetzbuch.py"))
gb = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(gb)
LISTE = gb.LISTE

# Rechenregeln: alte Etikett-Nummer → Kennung
RR = {13: "rr.stellenwert", 1: "rr.plusminus", 2: "rr.vorzeichen", 3: "rr.reihenfolge", 6: "rr.tauschen", 4: "rr.ausmultiplizieren", 5: "rr.minusklammer",
      12: "rr.potenz", 10: "rr.kuerzen", 11: "rr.bruchrechnen", 14: "rr.verhaeltnis", 8: "rr.gegenrechnung", 7: "rr.waage", 15: "rr.nullprodukt"}
# Tragende Ideen: Kurzname → Kennung
ID = {"Zahlengerade": "id.zahlen.zahlengerade", "Bündeln in Zehnern": "id.zahlen.buendeln", "Bausteine": "id.zahlen.bausteine", "Schreibweisen": "id.zahlen.schreibweisen", "Hoch und zurück": "id.zahlen.hoch_zurueck",
      "Term": "id.algebra.term", "Erlaubte Zahlen": "id.algebra.erlaubte_zahlen", "Gleichung lösen": "id.algebra.gleichung_loesen", "Höherer Grad": "id.algebra.hoeherer_grad",
      "Größe": "id.verhaeltnisse.groesse", "Wert für eins": "id.verhaeltnisse.wert_fuer_eins", "Prozent als Faktor": "id.verhaeltnisse.prozent",
      "Winkel an Geraden": "id.geometrie.winkel", "Gleicher Abstand": "id.geometrie.abstand", "Deckungsgleich": "id.geometrie.deckungsgleich", "Ähnlich": "id.geometrie.aehnlich", "Rechtwinkliges Dreieck": "id.geometrie.rechtwinklig",
      "Auslegen und zählen": "id.flaeche_raum.auslegen", "Aus dem Rechteck": "id.flaeche_raum.aus_dem_rechteck", "Aus dem Quader": "id.flaeche_raum.aus_dem_quader", "Haut des Körpers": "id.flaeche_raum.haut",
      "Zuordnung": "id.funktionen.zuordnung", "Wachstum": "id.funktionen.wachstum", "Gleichung und Form": "id.funktionen.gleichung_form",
      "Kennzahl": "id.daten.kennzahl", "Vom Teil aufs Ganze": "id.daten.teil_ganzes", "Anteil": "id.daten.anteil", "Stufen": "id.daten.stufen"}
# Fehlbilder, die an der Antwort sicher erkennbar sind: Kennung der Regel → [(Kennung des Fehlbilds, ein Satz)]
FB = {
 "rr.stellenwert": [("fb.stellenwert.null_angehaengt", "Bei mal 10 wird eine Null angehängt, auch wenn ein Komma da ist (2,5 · 10 = 2,50)."),
                    ("fb.stellenwert.eine_stelle_daneben", "Die Ziffern stimmen, das Ergebnis ist aber zehnmal zu groß oder zu klein.")],
 "rr.plusminus": [("fb.plusminus.doppelminus_uebersehen", "a − (−b) wird wie a − b gerechnet."),
                  ("fb.plusminus.zeichen_des_ergebnisses", "Der Betrag stimmt, das Vorzeichen des Ergebnisses ist falsch (3 − 8 = 5).")],
 "rr.vorzeichen": [("fb.vorzeichen.falsches_zeichen", "Bei Mal oder Geteilt stimmt der Betrag, das Vorzeichen ist falsch.")],
 "rr.reihenfolge": [("fb.reihenfolge.links_nach_rechts", "Strich wird vor Punkt gerechnet, weil er weiter links steht (2 + 3 · 4 = 20)."),
                    ("fb.reihenfolge.mal_vor_hoch", "Mal wird vor Hoch gerechnet (2 · 3² = 36)."),
                    ("fb.reihenfolge.minus_ins_quadrat", "Das Minus vor einer Potenz wird mitquadriert (−3² = 9).")],
 "rr.tauschen": [("fb.tauschen.minus_getauscht", "Bei Minus oder Geteilt werden die Zahlen vertauscht (3 − 8 gerechnet als 8 − 3, ohne das Zeichen mitzunehmen)."),
                 ("fb.tauschen.ungleiches_zusammengefasst", "Verschiedene Buchstabenteile werden zusammengefasst (3a + 4b = 7ab).")],
 "rr.ausmultiplizieren": [("fb.ausmultiplizieren.nur_erster_summand", "Der Faktor trifft nur den ersten Summanden (3 · (x + 2) = 3x + 2)."),
                          ("fb.ausmultiplizieren.hoch_verteilt", "Das Quadrat wird auf die Summanden verteilt ((a + b)² = a² + b²).")],
 "rr.minusklammer": [("fb.minusklammer.nur_erstes_zeichen", "Nur das erste Vorzeichen in der Klammer wechselt (a − (b − c) = a − b − c).")],
 "rr.potenz": [("fb.potenz.basis_mal_hochzahl", "Basis und Hochzahl werden malgenommen (2³ = 6)."),
               ("fb.potenz.hochzahlen_malgenommen", "Beim Malnehmen gleicher Basen werden die Hochzahlen malgenommen statt addiert (x² · x³ = x⁶)."),
               ("fb.potenz.negative_hochzahl_als_minus", "Eine negative Hochzahl wird als negatives Ergebnis gelesen (2⁻¹ = −2).")],
 "rr.kuerzen": [("fb.kuerzen.aus_summe", "Aus einer Summe wird gekürzt ((x + 6) : (x + 2) = 3)."),
                ("fb.kuerzen.nur_zaehler_oder_nenner", "Nur der Zähler oder nur der Nenner wird malgenommen oder geteilt.")],
 "rr.bruchrechnen": [("fb.bruchrechnen.zaehler_und_nenner_addiert", "Beim Addieren werden Zähler und Nenner je für sich addiert (½ + ⅓ = 2/5)."),
                     ("fb.bruchrechnen.falscher_kehrwert", "Beim Teilen wird der erste statt des zweiten Bruchs umgedreht oder gar keiner.")],
 "rr.verhaeltnis": [("fb.verhaeltnis.addiert_statt_malgenommen", "Statt mit dem Wert für eins zu rechnen, wird ein fester Betrag dazugezählt."),
                    ("fb.verhaeltnis.falsche_richtung", "Es wird malgenommen, wo geteilt werden muss, oder umgekehrt.")],
 "rr.gegenrechnung": [("fb.gegenrechnung.gleiche_rechnung", "Statt der Gegenrechnung wird dieselbe Rechnung noch einmal gemacht (□ + 7 = 3, also □ = 10)."),
                      ("fb.gegenrechnung.reihenfolge_nicht_umgekehrt", "Die Schritte werden in derselben statt in umgekehrter Reihenfolge zurückgenommen."),
                      ("fb.gegenrechnung.zweite_loesung_fehlt", "Bei x² = a wird nur die positive Lösung genannt.")],
 "rr.waage": [("fb.waage.nur_ein_summand", "Beim Malnehmen oder Teilen einer Seite wird nur ein Summand verändert."),
              ("fb.waage.zeichen_nicht_gedreht", "Bei einer Ungleichung wird mit einer negativen Zahl malgenommen oder geteilt, ohne das Zeichen umzudrehen."),
              ("fb.waage.nur_eine_seite", "Die Rechnung wird nur auf einer Seite ausgeführt.")],
 "rr.nullprodukt": [("fb.nullprodukt.andere_zahl", "Die Regel wird angewendet, obwohl rechts nicht null steht."),
                    ("fb.nullprodukt.vorzeichen_der_loesung", "Aus x − 2 = 0 wird x = −2 gemacht.")],
 "id.zahlen.zahlengerade": [("fb.zahlengerade.nach_betrag_geordnet", "Negative Zahlen werden nach ihrem Betrag geordnet (−30 größer als −10).")],
 "id.zahlen.buendeln": [("fb.buendeln.abgeschnitten_statt_gerundet", "Beim Runden wird immer abgerundet.")],
 "id.zahlen.bausteine": [("fb.bausteine.eins_als_primzahl", "Die 1 wird als Primzahl gezählt."),
                         ("fb.bausteine.nicht_zu_ende_zerlegt", "In der Zerlegung bleibt ein Faktor stehen, der keine Primzahl ist."),
                         ("fb.bausteine.endziffer_statt_quersumme", "Die Teilbarkeit durch 3 oder 9 wird an der Endziffer abgelesen."),
                         ("fb.bausteine.aus_drei_folgt_neun", "Aus „durch 3 teilbar“ wird „durch 9 teilbar“ gefolgert.")],
 "id.zahlen.schreibweisen": [("fb.schreibweisen.zaehler_komma_nenner", "Zähler und Nenner werden als Kommazahl geschrieben (¼ = 1,4 oder 0,4).")],
 "id.zahlen.hoch_zurueck": [("fb.hoch_zurueck.wurzel_halbiert", "Die Wurzel wird wie „geteilt durch 2“ gerechnet (√16 = 8).")],
 "id.algebra.term": [],
 "id.algebra.erlaubte_zahlen": [("fb.erlaubte_zahlen.nullstelle_des_nenners_als_loesung", "Eine Zahl, die den Nenner null macht, wird als Lösung genannt.")],
 "id.algebra.gleichung_loesen": [("fb.gleichung_loesen.grenze_mitgezaehlt", "Bei < oder > wird die Grenze selbst als Lösung genannt oder mitgezählt."),
                                 ("fb.gleichung_loesen.klammer_falsch_herum", "Die Intervallklammer zeigt bei ≤ oder ≥ von der Zahl weg oder bei < oder > zur Zahl hin.")],
 "id.algebra.hoeherer_grad": [("fb.hoeherer_grad.durch_x_geteilt", "Es wird durch x geteilt; die Lösung 0 geht verloren.")],
 "id.verhaeltnisse.groesse": [("fb.groesse.flaeche_mit_zehn", "Flächeneinheiten werden mit 10 und Raumeinheiten mit 10 oder 100 umgerechnet."),
                              ("fb.groesse.falsche_richtung", "Beim Wechsel in die kleinere Einheit wird geteilt statt malgenommen.")],
 "id.verhaeltnisse.wert_fuer_eins": [],
 "id.verhaeltnisse.prozent": [("fb.prozent.falscher_grundwert", "Der Prozentsatz wird auf den neuen statt auf den alten Wert bezogen."),
                              ("fb.prozent.prozente_addiert", "Aufeinanderfolgende Änderungen werden addiert (plus 20 % und minus 20 % ergeben 0 %).")],
 "id.geometrie.winkel": [("fb.winkel.neben_statt_scheitel", "Nebenwinkel und Scheitelwinkel werden verwechselt (α statt 180° − α oder umgekehrt)."),
                         ("fb.winkel.teil_der_drehung", "Der falsche Teil der vollen Drehung wird genommen (360° − α statt α).")],
 "id.geometrie.abstand": [("fb.abstand.koordinaten_vertauscht", "x- und y-Koordinate werden vertauscht."),
                          ("fb.abstand.nur_eine_seite", "Bei einem festen Abstand wird nur eine der beiden Seiten gefunden."),
                          ("fb.abstand.halbe_laenge_statt_mitte", "Statt der Mitte zwischen zwei Punkten wird die halbe Streckenlänge genannt.")],
 "id.geometrie.deckungsgleich": [("fb.deckungsgleich.falsche_koordinate_gespiegelt", "Beim Spiegeln wird das Vorzeichen der falschen Koordinate geändert."),
                                 ("fb.deckungsgleich.an_koordinatenachse_gespiegelt", "Es wird an der x- oder y-Achse gespiegelt statt an der genannten Achse."),
                                 ("fb.deckungsgleich.drehrichtung", "Es wird in die falsche Richtung gedreht."),
                                 ("fb.deckungsgleich.diagonale_als_achse", "Die Diagonalen eines Rechtecks oder Parallelogramms werden als Symmetrieachsen gezählt.")],
 "id.geometrie.aehnlich": [("fb.aehnlich.flaeche_mit_k", "Die Fläche wird mit k statt mit k² vergrößert.")],
 "id.geometrie.rechtwinklig": [("fb.rechtwinklig.ohne_quadrate", "Die Seitenlängen werden addiert statt ihre Quadrate (a + b = c)."),
                               ("fb.rechtwinklig.kathete_als_hypotenuse", "Eine Kathete wird wie die Hypotenuse behandelt.")],
 "id.flaeche_raum.auslegen": [("fb.auslegen.umfang_statt_flaeche", "Statt der Fläche wird der Umfang berechnet oder umgekehrt.")],
 "id.flaeche_raum.aus_dem_rechteck": [("fb.aus_dem_rechteck.halbieren_vergessen", "Beim Dreieck fehlt das „geteilt durch 2“."),
                                      ("fb.aus_dem_rechteck.durchmesser_statt_radius", "In die Kreisformel wird der Durchmesser statt des Radius eingesetzt.")],
 "id.flaeche_raum.aus_dem_quader": [("fb.aus_dem_quader.drittel_vergessen", "Bei Pyramide oder Kegel fehlt das Drittel.")],
 "id.flaeche_raum.haut": [("fb.haut.nur_drei_flaechen", "Bei der Oberfläche des Quaders werden nur drei statt sechs Flächen gezählt.")],
 "id.funktionen.zuordnung": [("fb.zuordnung.x_und_y_vertauscht", "Beim Ablesen oder Einsetzen werden x und y vertauscht.")],
 "id.funktionen.wachstum": [("fb.wachstum.plus_statt_mal", "Bei exponentiellem Wachstum wird in jedem Schritt derselbe Betrag addiert.")],
 "id.funktionen.gleichung_form": [("fb.gleichung_form.falsche_richtung_verschoben", "y = (x − 3)² wird als Verschiebung nach links gelesen.")],
 "id.daten.kennzahl": [("fb.kennzahl.median_ungeordnet", "Der Median wird aus der ungeordneten Liste abgelesen.")],
 "id.daten.teil_ganzes": [],
 "id.daten.anteil": [("fb.anteil.guenstig_durch_unguenstig", "Günstige werden durch ungünstige statt durch alle möglichen Ergebnisse geteilt.")],
 "id.daten.stufen": [("fb.stufen.addiert_statt_malgenommen", "Entlang eines Pfades wird addiert statt malgenommen."),
                     ("fb.stufen.ohne_zuruecklegen_uebersehen", "Beim Ziehen ohne Zurücklegen bleibt die zweite Stufe unverändert.")],
}
SCHULE = ("gym_by", "rs_by", "ib_myp")


def klassen(themen):
    return {s: sorted({LISTE[t]["klasse"].get(s) for t in themen} - {None}) for s in SCHULE}


eintraege = []
for i, r in enumerate(gb.sonne.R, 1):
    themen = sorted({t for _, _, t, _, _ in r["bsp"]})
    eintraege.append(dict(kennung=RR[r["nr"]], art="rechenregel", ort="Sonne", name=r["name"], nr_in_der_uebersicht=i, etikett_alt=r["nr"],
                          merksatz=r["spruch"].replace("<br>", " "), genau=r["merk"], klassen=klassen(themen), klassen_grundlage="Themen der Beispiele in sonne.md", themen=themen))
for planet, ideen in gb.IDEEN.items():
    for i, (kurz, genau, ns) in enumerate(ideen, 1):
        themen = sorted({t for n in ns for t in next(g for ab in gb.P.values() for _, gs in ab for g in gs if g[0] == n)[2]})
        eintraege.append(dict(kennung=ID[kurz], art="idee", ort=planet, name=kurz, nr_in_der_uebersicht=i, etikett_alt=None,
                              merksatz=gb.IDEE_SPRUCH[kurz][0], genau=genau, klassen=klassen(themen), klassen_grundlage="Themen der zugeordneten Regeln", themen=themen))
for e in eintraege:
    e["fehlbilder"] = [dict(kennung=k, beschreibung=b) for k, b in FB[e["kennung"]]]
alle = [e["kennung"] for e in eintraege]
fb_alle = [f["kennung"] for e in eintraege for f in e["fehlbilder"]]
assert len(alle) == len(set(alle)) == 42 and sorted(FB) == sorted(alle)
assert len(fb_alle) == len(set(fb_alle))
for e in eintraege:
    stamm = e["kennung"].split(".")[-1]
    assert all(f["kennung"].startswith("fb." + stamm + ".") for f in e["fehlbilder"]), e["kennung"]
ziel = os.path.join(HIER, "kennungen.json")
if os.path.exists(ziel):                                   # nie ändern, nie neu vergeben: Altes muss bleiben
    alt = json.load(open(ziel, encoding="utf-8"))
    for a in alt["kennungen"]:
        neu = next((e for e in eintraege if e["kennung"] == a["kennung"]), None)
        assert neu is not None and neu["art"] == a["art"] and neu["name"] == a["name"], f"Kennung geändert oder entfernt: {a['kennung']}"
        assert {f["kennung"] for f in a["fehlbilder"]} <= {f["kennung"] for f in neu["fehlbilder"]}, f"Fehlbild-Kennung entfernt bei {a['kennung']}"
json.dump({"stand": "2026-11-26",
           "hinweis": "Stabile Kennungen des Regel-Universums. Eine Kennung wird nie geändert und nie neu vergeben; kommt eine Regel dazu, bekommt sie eine neue. "
                      "Merksatz, Name und Nummer in der Übersicht dürfen sich ändern, die Kennung nicht. Klassen stammen aus inhalte/themenliste.json, nicht aus dem Lehrplan an der Quelle. "
                      "Fehlbilder: nur solche, die an einer Antwort sicher erkennbar sind; eine leere Liste ist Absicht.",
           "ohne_kennung": {"Arbeitsweisen": "Probe, Überschlag, Einheiten, Skizze, Ansatz, Begründen, Ablesen und Darstellen, Formel anwenden – keine Regeln, deshalb hier ohne Kennung. Das alte Etikett 9 „Einsetzen und Probe“ gehört hierher."},
           "kennungen": eintraege}, open(ziel, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(alle)} Kennungen (14 Rechenregeln, 28 Ideen), {len(fb_alle)} Fehlbilder; ohne Fehlbild: {sum(1 for e in eintraege if not e['fehlbilder'])}")
print("OK")
