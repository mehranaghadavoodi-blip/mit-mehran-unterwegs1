# Mit Mehran unterwegs – Anleitung

## Dateien
- index.html – die komplette Seite (Fotos und Logo sind eingebettet)
- reisen.json – deine Länder, Reisen, Orte und Links (hier pflegst du Inhalte)
- favicon.png, og-image.jpg – Symbol und Vorschaubild für Google/WhatsApp
- robots.txt, sitemap.xml – für die Suchmaschinen
- impressum.html, datenschutz.html – Vorlagen (ausfüllen!)
- .nojekyll – Hinweis für GitHub Pages

## Online stellen mit GitHub Pages
1. Auf GitHub ein neues öffentliches Repository anlegen, z. B. mit-mehran-unterwegs.
2. „Add file → Upload files“, alle Dateien dieses Ordners hochladen, „Commit changes“.
3. Settings → Pages → Branch „main“, Ordner „/ (root)“ → Save.
4. Nach etwa 1 Minute ist die Seite erreichbar unter https://BENUTZERNAME.github.io/mit-mehran-unterwegs/
5. Ersetze in index.html, robots.txt und sitemap.xml überall `https://DEINE-DOMAIN.de` durch deine echte Adresse.
6. Impressum und Datenschutz ausfüllen.
7. Eigene Domain später: Settings → Pages → Custom domain.

## Inhalte pflegen
Variante A (am einfachsten): Auf GitHub reisen.json öffnen, Stift-Symbol, Text ändern, „Commit changes“. Nach etwa 1 Minute ist es online.
Variante B: Seite mit `/#admin` am Ende der Adresse öffnen, Reise oder Ort mit dem Formular eintragen, „Kopieren“, den Text in reisen.json einfügen und speichern.
Koordinaten eines Ortes: in Google Maps den Ort lang drücken und die Zahlen kopieren, z. B. 39.7863, 19.7064.

## Suchmaschinen
Die Seite in der Google Search Console anmelden und sitemap.xml einreichen.
