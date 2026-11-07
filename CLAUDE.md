# Regeln für Claude – Website „Mit Mehran unterwegs“

Besitzer: Mehran (Fotograf, Video-Creator, Schriftsteller). Antworte auf Deutsch, kurz und Schritt für Schritt; er arbeitet meist am Handy.

## Aufbau
- index.html: die gesamte Seite (Fotos und Logo eingebettet). Nur gezielt ändern, Bilddaten nie löschen.
- reisen.json: alle Länder, Reisen, Orte, Links. Hier werden neue Inhalte gepflegt.
- impressum.html, datenschutz.html: Vorlagen, nicht ohne Rückfrage ändern.
- sitemap.xml, robots.txt, og-image.jpg, favicon.png: SEO und Vorschau.

## Design (nicht ändern ohne Rückfrage)
- Warme Farben: Safrangold, Terrakotta, Espresso-Braun, Creme, Olivgrün.
- Persische Kalligrafie unten im Logo bleibt unverändert.
- Pins: besucht = Terrakotta, geplant = Olivgrün, Video online = Gold mit ▶.
- Sprachen: de, en, fa, ar, el, es, id, vi, fr, si, ka; fa und ar laufen von rechts nach links.

## Arbeitsweise
- Änderungen auf einem eigenen Branch, dann Pull Request; nie ungefragt auf main.
- Nach jeder Änderung an reisen.json: python3 .github/check_reisen.py ausführen.
- Neue Reisen: Land per Ländercode (cc), Titel (t), Datum (d, z. B. 05.2027), Link (u). Orte als [Name, Breite, Länge, optionaler Video-Link].
- SEO beachten: Titel, Beschreibung, Open Graph, sitemap.xml aktuell halten.
- Keine Passwörter, Zugangsdaten oder Tokens in Dateien schreiben.
- Offene Punkte stehen im Projektstand-Dokument.
