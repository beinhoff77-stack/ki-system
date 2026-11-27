# Vorgabe WW: „Was wackelt?" – Voranalyse statt Rohdaten

Designer, 27.11.2026, **Fassung 1**. Stand `lernen-app` a3ebdad.
Betrifft `viewWackelt` und `lernWackeltListe` in `lernen.js` sowie die Stile `.wk-*` und `.ls-*` in `style.css`.
Kein App-Code, keine Datenbank. Klickmuster: `entwurf/wackelt.html` (eine Datei, kein Netz; gebaut mit `entwurf/bauen.py` aus `entwurf/teile/`).
Alle Zahlen, Aufgaben und Antworten im Klickmuster sind **erfunden**; das steht auch oben auf der Seite.

**[G]** gesichert · **[A]** Annahme von mir · **[E]** Entscheidung des Nutzers nötig

---

## 0. Wozu die Seite da ist

Ein Satz, an dem sich jede Entscheidung unten messen lässt:

> Der Lehrer hat fünf Minuten. Er will wissen, **worüber er mit dem Nutzer reden soll** und **was genau schiefging** – ohne vorher etwas anzutippen.

Alles, was diesen Satz nicht bedient, gehört nicht auf die erste Bildschirmhöhe.

## 1. Was heute fehlt [G – an `lernen-app` a3ebdad gemessen]

Bilder des heutigen Standes: `bilder/ist-400-hell.jpg`, `ist-820-hell.jpg`, `ist-1280-hell.jpg` (mit erfundenen Daten aufgenommen).

| # | Mangel | Wirkung |
|---|---|---|
| 1 | **Die Fehler sind zugeklappt.** Die falschen Antworten stehen hinter „Bordkarte und Antwort ▸". | Das Wichtigste ist unsichtbar. Bei drei Themen sind es drei Klicks, bevor der Lehrer etwas Besprechbares sieht. |
| 2 | **Keine Deutung.** Es steht „10 Fehler · gestern" – nicht, *was* falsch war. | Der Lehrer muss selbst suchen, was die Fehler gemeinsam haben. |
| 3 | **Die Fehlerart wird nicht gezeigt**, obwohl der Server sie liefert (`fehler_gruende`: Vorzeichen, Komma, vertauscht, gerundet, falsche Einheit). | Die beste vorhandene Information liegt brach – sie steht nur in der zugeklappten Tabelle „Je Etappe". |
| 4 | **Die Reihenfolge ist unbegründet.** Die Liste ist sortiert, sagt aber nicht, wonach. | Wirkt beliebig; der Lehrer weiß nicht, ob oben wirklich das Dringendste steht. |
| 5 | **Knöpfe sind so laut wie der Inhalt.** Drei Knöpfe je Eintrag, immer sichtbar. | Bei 400 px brauchen die Knöpfe mehr Platz als der Text. |
| 6 | **Dieselben Daten dreimal**: Arbeitsliste, „Je Etappe (7)", „Alle Etappen mit Stand (8)". | Der Lehrer weiß nicht, wo er hinsehen soll. |
| 7 | **Breite ungenutzt.** Bei 1280 px steht rechts die halbe Seite leer. | Am Rechner passt alles nebeneinander, was heute untereinander versteckt ist. |

## 2. Der neue Aufbau [G]

Von oben nach unten, am Handy einspaltig, ab 760 px die Karte innen zweispaltig.

```
┌──────────────────────────────────────────┐
│ Was wackelt?            Stand: heute 9:00│   ← Die Lage
│ 3 Themen wackeln – zusammen 22 falsche   │
│ Antworten, die älteste vor 6 Tagen.      │
│ Am häufigsten: Vorzeichen (8×).          │
│ [46 Bordkarten][67 % richtig][7 Tipp][4] │
│ ↗ Dasselbe Muster in mehreren Themen …   │
└──────────────────────────────────────────┘
ZU BESPRECHEN  3
┌──────────────────────────────────────────┐
│ ① Brüche                                 │   ← Rang und Begründung
│   Lissabon · Bruch zu Dezimalzahl        │
│   6 falsche Antworten, 5 richtige        │
│   [wieder offen] [2 neu seit …]          │
│   ████████▓▓▓▓▓▓▓▓  5 richtig · 6 falsch │   ← Balken
│ ┌───────────────┬──────────────────────┐ │
│ │ DAS MUSTER    │ DIE LETZTEN FALSCHEN │ │
│ │ [Komma]       │ ANTWORTEN (3 von 6)  │ │
│ │ Fast immer    │ 3/4 als Dezimalzahl  │ │
│ │ dasselbe: …   │ geantwortet 0,34     │ │
│ │ │ Kurz gesagt:│ richtig 0,75         │ │
│ │   Zähler durch│ gestern              │ │
│ │   Nenner …    │ … zwei weitere …     │ │
│ └───────────────┴──────────────────────┘ │
│ [✓ Besprochen][Nur beobachten] Erklärung…│
└──────────────────────────────────────────┘
BEOBACHTEN 1 · BESPROCHEN 1  (gleich gebaut, ohne Rangziffer)
▸ Alle Etappen mit Stand (23)
```

## 3. Die Voranalyse – was die Seite rechnet [G]

**Grundsatz: Es wird nichts geraten.** Jede Zeile unten lässt sich aus dem ausrechnen, was `schule_lernstand` und `schule_wackelt_lesen` **heute schon liefern**. Keine neue Serverfunktion, keine KI. Die Rechnung steht im Klickmuster in `entwurf/teile/befund.js`.

### 3.1 Die Lage (Kopf)
- Zahl der Themen in „Zu besprechen"; Summe ihrer falschen Antworten; Alter des ältesten Fehlers.
- Häufigster Grund über alle offenen Themen, **erst ab 2 Treffern** genannt.
- Zusatzzeile „↗ Dasselbe Muster taucht in mehreren Themen auf", wenn derselbe Grund in **mindestens zwei** Themen vorkommt. Das ist die wertvollste Zeile der Seite: Sie macht aus drei Gesprächen eines.
- Die vier Zahlen rechts (Bordkarten, Anteil richtig, Tipps, Lerntage) kommen unverändert aus `woche` und `lerntage`.

### 3.2 Der Befund je Thema – Wortlaut
Aus `fehler_gruende` aller Etappen des Themas, summiert. `{n}` = Treffer des häufigsten Grundes, `{m}` = alle falschen Antworten im Thema.

| Grund | eingesetzter Satzteil |
|---|---|
| `vorzeichen` | das Vorzeichen kippt – richtiger Betrag, falsches Vorzeichen |
| `komma` | das Komma sitzt falsch – richtige Ziffern an der falschen Stelle |
| `vertauscht` | richtig gerechnet, aber verdreht |
| `gerundet` | falsch gerundet – dicht daneben |
| `falsche_einheit` | richtige Zahl, falsche Einheit |

**Der Satz sagt nur so viel, wie die Zahlen hergeben:**

| Anteil `{n}/{m}` | Satz |
|---|---|
| ab ⅔ | „Fast immer dasselbe: **‹Satzteil›**. {n} von {m} falschen Antworten." |
| ⅓ bis ⅔ | „Oft, aber nicht immer: **‹Satzteil›**. {n} von {m} falschen Antworten – die übrigen {m−n} liegen anders daneben." |
| unter ⅓ | „Ein kleinerer Teil der Fehler passt zusammen: **‹Satzteil›** ({n} von {m}). Für ein Muster ist das noch wenig." – **ohne** farbige Marke |
| kein Grund ≥ 2 | „Kein Muster: Die {m} falschen Antworten liegen jede anders daneben. Hier helfen die Aufgaben selbst mehr als eine Regel." |

Die farbige Marke neben „DAS MUSTER" (Vorzeichen · Komma · vertauscht · gerundet · Einheit) erscheint **nur ab ⅓**.

### 3.3 Reihenfolge und Begründung
Punkte, nur innerhalb von „Zu besprechen", Rangziffer ① ② ③:

| Bedingung | Punkte | Begründungszeile unter dem Titel |
|---|---|---|
| Grundwert | `falsch × 2` | „{falsch} falsche Antworten" |
| `wieder_offen` | +100 | „{falsch} falsche Antworten, {richtig} richtige" (die Marke sagt schon „wieder offen") |
| sonst `falsch ≥ 3` **und** `falsch > richtig` | +50 | „mehr falsch als richtig: {falsch} von {falsch+richtig}" |
| `fehler_neu > 0` | +20 | – (die Marke sagt es) |
| letzter Fehler heute oder gestern | +10 | – |

Die Begründung steht **immer sichtbar** unter dem Titel. Damit ist die Reihenfolge nachprüfbar statt geraten.

### 3.4 Die falschen Aufgaben – immer offen [G]
Das Herzstück. Je Aufgabe ein Kasten:
- Etappenname klein darüber – **nur wenn das Thema mehrere Etappen hat**;
- die Aufgabe in Festbreitenschrift, 15 px, fett;
- darunter in einer Zeile: `GEANTWORTET` + Antwort des Nutzers (rot, durchgestrichen) · `RICHTIG` + Lösung (grün);
- darunter „gestern" / „vor 3 Tagen".

Sortiert nach Datum, neueste zuerst. **Drei** sind offen, der Rest hinter „▾ Alle {n} gespeicherten Antworten zeigen".

**Überschrift sagt die Wahrheit über die Menge:** Gespeichert sind nur die letzten falschen Antworten, nicht alle. Darum heißt es „**Die letzten falschen Antworten (4 von 6)**", sobald weniger gespeichert sind als insgesamt falsch waren – sonst „Diese Aufgaben waren falsch (3)". Ohne diesen Zusatz hält der Lehrer 4 für die ganze Wahrheit.

### 3.5 „Kurz gesagt"
Die Regel der Etappe mit den **meisten Fehlern** im Thema (nicht der ersten). Bei mehreren Etappen ist das der Unterschied zwischen der passenden und einer beliebigen Regel.

## 4. Maße, Farben, Schrift [G]

Alle Farben sind die vorhandenen Werte aus `style.css` (`body[data-area="lernen"]`), hell und dunkel:

| Rolle | hell | dunkel |
|---|---|---|
| Fläche / Seite | `#fff` / `#f4f6f8` | `#192330` / `#101721` |
| Text / leise | `#172437` / `#526174` | `#f1f5f9` / `#b3bfcd` |
| Linie | `#dce3ea` | `#354255` |
| Akzent (Knopf, „Kurz gesagt") | `#087f72` | `#62d8c4` |
| falsch (Rand, Antwort, Rangziffer) | `#a72e37` auf `#fbe9eb` | `#f2909a` auf `#3a2027` |
| richtig (Lösung, besprochen) | `#25663a` auf `#e7f4eb` | `#7fd79b` auf `#1b3326` |
| beobachten | `#855e41` auf `#faf0e3` | `#e0b68c` auf `#33281d` |
| Querverweis-Zeile | `#275d98` auf `#e8f1fc` | `#8fbdf0` auf `#1c2b3d` |

- Schrift: Space Grotesk (Fließtext), JetBrains Mono für **alle Zahlen, Aufgaben und Antworten**.
- **Kleinste Schrift 13 px**, auch bei Marken und Datumsangaben (gemessen, siehe Prüfliste).
- Ecken: Karte 14 px, Kästen innen 10 px, Knöpfe und Marken rund (999 px).
- Linker Rand der Themenkarte 4 px in der Farbe des Zustands – das ist die einzige Stelle, an der der Zustand als Fläche erscheint.
- Balken: 9 px hoch, grün = richtig, rot = falsch, Breite im Verhältnis der Zahlen.
- Ab **760 px**: `DAS MUSTER` und `DIE LETZTEN FALSCHEN ANTWORTEN` nebeneinander, Spalten 1 : 1,3, oben ausgerichtet.

## 5. Texte wörtlich [G]

| Stelle | Text |
|---|---|
| Überschrift | `Was wackelt?` |
| Gruppen | `Zu besprechen` · `Beobachten` · `Besprochen` |
| Kopfzeilen in der Karte | `DAS MUSTER` · `DIE LETZTEN FALSCHEN ANTWORTEN (n von m)` · `Diese Aufgaben waren falsch (n)` |
| In der Aufgabe | `GEANTWORTET` · `RICHTIG` |
| Knöpfe | `✓ Besprochen` · `Nur beobachten` · `Doch besprechen` · `Wieder aufnehmen` · `Erklärung ansehen ›` · `Im Lehrplan ›` |
| Marken | `wieder offen` · `n neu seit dem letzten Blick` · `besprochen` |
| Querverweis | `↗ Dasselbe Muster taucht in mehreren Themen auf. Ein Gespräch darüber hilft allen drei Themen auf einmal.` |
| Nichts offen | `Nichts zu besprechen.` + ` Seit dem letzten Blick ist keine Antwort falsch gewesen.` |
| Gruppe leer | `Nichts zu besprechen.` · `Nichts im Auge zu behalten.` · `Noch nichts besprochen.` |
| Fuß | `Neue falsche Antworten holen ein Thema von selbst zurück nach „Zu besprechen". „Besprochen ✓" nimmt es heraus, bis wieder etwas falsch ist.` |
| Zugeklappt unten | `Alle Etappen mit Stand (n)` |

Kein Name eines Kindes auf der Seite: im Klickmuster steht „der Nutzer"; in der App steht dort der Name, den der Lehrer ohnehin schon im Kopf der Seite sieht.

## 6. Was ich nicht entschieden habe [E]

1. **Eine echte Deutung** („der Nutzer verwechselt Kürzen mit Erweitern") ist aus den heutigen Daten **nicht** ableitbar. Dafür bräuchte es entweder eine Liste typischer Fehler je Etappe vom Mathe-Profi oder eine KI, die die falschen Antworten liest. Der Entwurf kommt bewusst ohne aus. **Soll das kommen – und von wem?**
2. **Mehr gespeicherte Fehler.** Heute kommen nur die letzten falschen Antworten mit (im Beispiel 4 von 6). Für ein Muster wären alle besser. Das ist eine Frage an den Programmierer.
3. **Gesprächsvorschlag.** Ein Satz „Fang mit dieser Aufgabe an" wäre möglich (die jüngste falsche Antwort der Etappe mit den meisten Fehlern – in `befund.js` als `aufhaenger` vorbereitet, aber nicht eingebaut). **Will der Nutzer das?**
4. **Die drei Listen.** Ich habe „Je Etappe" ganz entfernt und nur „Alle Etappen mit Stand" zugeklappt gelassen. Falls der Lehrer die Tabelle mit „häufigster Fehler" vermisst, kommt sie dort hinein.

## 7. Prüfliste

**Muss**
- [ ] Die falschen Aufgaben stehen offen da, ohne Antippen.
- [ ] Je Thema ein Befundsatz, dessen Stärke zum Anteil passt (⅔ / ⅓ / darunter / keins).
- [ ] Die Reihenfolge ist unter jedem Titel begründet.
- [ ] Steht nicht alles in der Liste, sagt die Überschrift „(n von m)".
- [ ] Kleinste Schrift 13 px; kein Querrollen bei 360, 400, 820, 1280 px; hell und dunkel.
- [ ] Kein Name eines Kindes im Entwurf.

**Soll**
- [ ] Ab 760 px Muster und Aufgaben nebeneinander.
- [ ] Querverweis-Zeile, wenn derselbe Grund in mindestens zwei Themen steckt.
- [ ] „Kurz gesagt" gehört zur Etappe mit den meisten Fehlern.

**Kann**
- [ ] Gesprächsvorschlag (Punkt 6.3).
- [ ] Drucken oder Weitergeben des Befunds für das Gespräch.

## 8. Nicht geprüft

- Kein echtes Gerät, kein Safari, kein Firefox; Kontraste nicht gemessen.
- Ob ein Lehrer in fünf Minuten wirklich schneller zum Gespräch kommt – nicht erprobt.
- Die Seite ist mit **erfundenen** Daten gebaut; wie sie mit 15 wackelnden Themen oder sehr langen Aufgabentexten aussieht, ist offen.
- **JetBrains Mono hat kein Wurzelzeichen `√`** (gemessen: fällt auf eine Ersatzschrift zurück). In Aufgaben der Klassen 9 und 10 kommt es vor; dort steht es dann in anderer Schrift neben den Ziffern.
- Die dunkle Gestaltung des **heutigen** Standes konnte ich nicht aufnehmen – in meinem Aufbau kam zweimal dasselbe helle Bild heraus. Die Bilder `ist-*-dunkel` fehlen deshalb.
