# Nachprüfung Schritt A (Befunde N1–N8), lernen-app 0.74.2

Stand: `origin/lernen-app` 9d092d0 (enthält fc30671 / 5588709), 2026-11-17.
Grundlage: Bericht `inhalte/postfach/bau-phase2.md`, Auftrag in `inhalte/AUFTRAEGE.md` („Bau-Auftrag Phase 2 und 3“), Befunde `NACHPRUEFUNG-2026-11-16.md`.

**Methode**
- `tests/lernen.test.cjs` selbst ausgeführt: 24 von 24 grün. `tests/search.test.cjs` nicht ausgeführt.
- Alle 593 Etappen aus `inhalte/themen/*.json` durch `lernErklaerung` gerendert und gezählt (`nach/n1-zaehlung-v0742.cjs`).
- Echte Etappen in der Abflug-Gestaltung bei 390, 820 und 1280 px gerendert (`nach/bilder-v0742.test.cjs`, Mock aus `tests/lernen.test.cjs`). Bilder: `nach/bilder/v0742-*.jpg`.
- Den „Kurz gesagt“-Ausdruck (alt und neu) auf alle 593 Merksätze angewandt.
- Code-Diff 5742532 → 5588709 gelesen. Keine Kinderdaten, nichts an App oder Datenbank geändert.

## Ergebnis

| Nr. | Urteil | Befund |
|---|---|---|
| N1 | **teilweise** | ✓ **Keine zwei gleichen Bilder:** 416 Etappen mit Schrittbildern, 0 mit Doppelbild. Alle 769 Schrittbilder bringen eine Änderung.<br>✓ **„Was bedeutet eine negative Zahl?“:** 2 286 px auf dem Handy (vorher 3 057, Ziel deutlich unter 3 000). Nur Schritt 1 hat ein Bild.<br>✗ **Graph verschwindet fast (Tag-Gestaltung):** Der Rest wird auf 40 % abgeblendet. Der erste Graph hat die Akzentfarbe (`.graph0` = `--lr-akzent`, Gelb). Abgeblendet ist er auf hellem Grund kaum noch zu sehen. Beispiel Kerze, Schritte 2–4: `v0742-n1-kerze-390.jpg`.<br>✗ **Steigungsdreieck widerspricht dem Text:** Es wird auf 2 Einheiten verbreitert, der Text nennt aber 1 Einheit. Kerze: „Jede Stunde 1,5 cm“, gezeichnet sind 2 h und 3 cm. „Steigung m und Achsenabschnitt t“: „1 km weiter, 2 € mehr“, gezeichnet sind 2 km und 4 €. Betroffen sind 4 Schritte, alle in `funktionen.linear.json`.<br>◐ **Hervorhebung nur in Zeichnungen:** 406 von 769 Schrittbildern haben ein hervorgehobenes neues Element, 363 nicht. 259 davon sind Tabellen- und Stellentafel-Bilder, dort ist keine Hervorhebung gebaut. 70 Zeichnungen haben eine Änderung außerhalb der erkannten Felder. 24 Bilder werden abgeblendet, ohne dass etwas hervorgehoben ist (Bruchstreifen `gefaerbt`, Zahlenstrahl `pfeil`). Sichtbar schadet das bei Bruchstreifen nicht, weil die Füllung selbst die Änderung zeigt (`v0742-n1-bruchteil-390.jpg`). |
| N8 | erfüllt | Bei 820 und 1280 px stehen Nummer, Bild links und Text rechts in einer Zeile (`v0742-n8-kerze-820.jpg`). Auf dem Handy steht das Bild über dem Text. |
| N2 | **nicht erfüllt (neuer Fehler)** | Es wird nicht mehr abgeschnitten, und „z. B.“ beendet keinen Satz mehr. 8 Merksätze sind dadurch richtig. **Aber:** Der neue Ausdruck erkennt ein Satzende nur nach einem Wort mit mindestens 2 Zeichen und nur vor einem Großbuchstaben. Deshalb laufen **87 von 593** „Kurz gesagt“ in den nächsten Satz weiter, z. B. „Löse f(x) = 0. Ungerade Vielfachheit: …“, „… durch P. Der Abstand zu Z …“ oder „… (0 \| a). b > 1: steigt …“. Der Test im Bau prüft nur ein langes Beispiel. Die Zahl im Bericht (116 Merksätze über 90 Zeichen) ist dadurch zu hoch. Mit richtiger Satzerkennung sind es **75**. |
| N3 | erfüllt | Code und Test: Der Komma-Platz ohne Komma ist `komma leer` und hat keine `ab`-Klasse, also keinen gestrichelten Rahmen. |
| N4 | erfüllt | Code und Test: „Erst 1 Wiederholung ›“ (Plural bei mehreren). Nach der Runde steht „Weiter nach Rom ›“ (`n.stadt`). |
| N5 | erfüllt (laut Auftrag) | Der Detektiv kommt an beiden Stellen nur, wenn kein `grund` erkannt wurde. Die Einschränkung auf Kl. 5/6 aus dem Befund-Vorschlag ist nicht gebaut. Der Auftrag verlangte sie nicht. |
| N6 | erfüllt | Kopf „Rom · Natürliche Zahlen“ (`ort.stadt · titelKurz`). Ohne `stadt` wird wie bisher `ctx.titel` gezeigt. |
| N7 | erfüllt, ein Hinweis | Knöpfe im Abflug-Stil, die Reihenfolge stimmt („Erst üben: Zahlenstrahl ›“ → `-ueben-2`, „Verbessern ›“ → Test). Keine `btn`-Klassen mehr. Die richtige Markierung ist mit ✓ eingezeichnet, die falsche rot gestrichelt.<br>**Hinweis:** „Grün“ ist `--lr-gut`. Das ist nur in Dschungel und Nacht grün, in Ozean (#0E7C86) und Wüste (#0F766E) ist es Petrol. Die Antwortkarten haben weiter das alte Kartenlayout (`card`). Auf dem Handy überdeckt das schwebende ≡ Text der Antwortkarte. Beides ist nicht Teil von N7. |

## Nacharbeit (Vorschlag an den Bau-Chat, Schritt A2)

1. **N2:** Satzende wie früher an jedem `.!?` vor einem Leerzeichen oder dem Textende erkennen, aber nicht nach Abkürzungen („z. B.“, „d. h.“, „u. a.“, „bzw.“, „ca.“, „usw.“, „vgl.“). Als Test alle Merksätze aus `inhalte/themen` prüfen: „Kurz gesagt“ ist höchstens ein Satz.
2. **N1, Abblenden:** Den Rest nicht über die Deckkraft zurücknehmen. Stattdessen Graphen und Linien grau zeichnen, mit mindestens 3:1 Kontrast zum Hintergrund. Oder die Deckkraft nur für Gitter und Hilfslinien senken. Abblenden nur, wenn wirklich ein Element `.neu` trägt.
3. **N1, Steigungsdreieck:** Nicht in der App vergrößern, weil Text und Bild sonst nicht mehr übereinstimmen. Die 4 Schritte in `funktionen.linear.json` gehen an einen Inhalts-Chat: Das Dreieck dort selbst 2 Einheiten breit machen und den Text anpassen (z. B. „In 2 Stunden wird sie 3 cm kürzer“). Ob das besser ist als eine 1 Einheit breite, kräftig gezeichnete Variante, ist Geschmackssache. der Nutzer entscheidet.
4. **N1, Tabellen und Stellentafel:** Hervorhebung der geänderten Zelle (`markiert` oder neue Werte), wenn gewünscht. Das ist ein kleiner Ausbau und kein Fehler.
5. **N7 (optional):** Für die richtige Markierung ein festes Grün statt `--lr-gut`, wenn „grün“ wörtlich gemeint ist.

N3, N4, N5, N6, N8: keine Nacharbeit.
