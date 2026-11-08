"""Lädt die Schriften einmalig auf den GitHub-Server und legt sie lokal im Ordner fonts ab.
Besucher deiner Seite laden danach nichts mehr von Google."""
import hashlib, os, re, urllib.request

CSS_URL = ("https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;1,600"
           "&family=Great+Vibes&family=Vazirmatn:wght@400;700&family=Noto+Sans+Sinhala:wght@400;700"
           "&family=Noto+Sans+Georgian:wght@400;700&display=swap")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def hole(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60).read()

def verarbeite(css, lade, ziel="fonts"):
    os.makedirs(ziel, exist_ok=True)
    gesehen = {}
    def ersetze(m):
        url = m.group(1)
        if url not in gesehen:
            name = hashlib.sha1(url.encode()).hexdigest()[:12] + ".woff2"
            with open(os.path.join(ziel, name), "wb") as f:
                f.write(lade(url))
            gesehen[url] = name
        return "url(" + gesehen[url] + ")"
    neu = re.sub(r"url\((https://fonts\.gstatic\.com/[^)]+)\)", ersetze, css)
    if "fonts.gstatic.com" in neu or not gesehen:
        raise SystemExit("Unerwartetes Ergebnis: keine oder nicht ersetzte Schriftdateien")
    with open(os.path.join(ziel, "fonts.css"), "w", encoding="utf-8") as f:
        f.write("/* Automatisch erzeugt von .github/fonts_laden.py – Schriften unter SIL Open Font License 1.1 */\n" + neu)
    with open(os.path.join(ziel, "LIZENZ.txt"), "w", encoding="utf-8") as f:
        f.write("Cormorant Garamond, Great Vibes, Vazirmatn, Noto Sans Sinhala und Noto Sans Georgian stehen unter der SIL Open Font License 1.1 (https://openfontlicense.org). Quelle: Google Fonts.\n")
    return len(gesehen)

if __name__ == "__main__":
    n = verarbeite(hole(CSS_URL).decode("utf-8"), hole)
    print(n, "Schriftdateien gespeichert in fonts/")
