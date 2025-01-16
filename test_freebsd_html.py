import pytest
from bs4 import BeautifulSoup
from datetime import datetime

# HTML generálása a megadott feladatok szerint
def create_html():
    html_content = """<!DOCTYPE html>
<html lang="hu">
<head>
<meta charset="utf-8" />
<title>FreeBSD</title>
</head>
<body>
<h1>FreeBSD</h1>
<p><!-- FreeBSD -->A <strong>FreeBSD</strong> egy nyílt forráskódú operációs rendszer,
a <strong><em>Berkeley Software Distribution</em></strong> rendszerből létrehozva.
Az első FreeBSD 1993-ban jelent meg. A BSD rendszerek között
a legnépszerűbb nyílt forráskódú operációs rendszer.</p>
<p><!-- hasonlóság -->A <strong>FreeBSD</strong> hasonlít a Linuxra rendszerekre, de van két
fő különbség. Az első a terjesztési engedély. A <em>FreeBSD</em> egy komplett operációs rendszert tart fenn,
kernelt, eszközillesztőket, felhasználói programokat,
dokumentációt. Ezzel szemben a Linux csak egy kernel
és illesztőprogramok.</p>
<p><!-- engedély -->A FreeBSD forráskódja általában megengedő BSD licenc,
szemben a Linux által használt GPL-lel.</p>
<p><!-- asztali környezet -->Elérhető asztali környezetek: GNOME, KDE, Xfce.<br />
Ablakkezelők: openbox, fluxbox, dwm, bspwm.</p>
<footer>Az oldal készítője: Teszt Elek, dátum: {datetime.now().strftime('%Y-%m-%d')}</footer>
</body>
</html>"""
    with open("freebsd.html", "w", encoding="utf-8") as f:
        f.write(html_content)

# Ellenőrzések Pytesttel
def test_html_file():
    with open("freebsd.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Nyelv ellenőrzése
    assert soup.html["lang"] == "hu"

    # Karakterkódolás ellenőrzése
    assert soup.meta["charset"].lower() == "utf-8"

    # Cím ellenőrzése
    assert soup.title.string == "FreeBSD"

    # Fejezetcím ellenőrzése
    assert soup.h1.string == "FreeBSD"

    # "hasonlóság" szekció félkövér FreeBSD ellenőrzés
    assert soup.find("p", string=lambda x: x and "FreeBSD hasonlít" in x).find("strong").string == "FreeBSD"

    # Felsorolás tagolása
    assert "GNOME, KDE, Xfce." in soup.text
    assert "openbox, fluxbox, dwm, bspwm." in soup.text

    # Kiemelés ellenőrzése
    assert soup.find("em", string="FreeBSD") is not None

    # "Berkeley Software Distribution" félkövér és dőlt ellenőrzés
    assert soup.find("strong").find("em", string="Berkeley Software Distribution") is not None

    # Footer ellenőrzése
    footer = soup.footer
    assert footer is not None
    assert "Teszt Elek" in footer.text
    assert datetime.now().strftime("%Y-%m-%d") in footer.text

if __name__ == "__main__":
    create_html()
    pytest.main()
