import pytest
from bs4 import BeautifulSoup
from datetime import datetime

def create_html():
    today_date = datetime.now().replace(year=2025).strftime("%Y-%m-%d")
    footer_text = "Ez egy példa lábléc szöveg"
    html_content = f"""<!DOCTYPE html>
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
<footer>{footer_text}, {today_date}</footer>
</body>
</html>"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

# Teszt függvények
def test_language():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    assert soup.html["lang"] == "hu"

def test_charset():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    assert soup.meta["charset"].lower() == "utf-8"

def test_title():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    assert soup.title.string == "FreeBSD"

def test_heading():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    assert soup.h1.string == "FreeBSD"

def test_similarity_section():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    similarity_section = None
    for p in soup.find_all("p"):
        if "hasonlít" in p.get_text():
            similarity_section = p
            break
    assert similarity_section is not None, "Nem található a 'hasonlóság' szekció."

def test_bold_freebsd_in_similarity():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    
    similarity_section = None
    for p in soup.find_all("p"):
        if "hasonlít" in p.get_text():
            similarity_section = p
            break

    assert similarity_section is not None, "Nem található a 'hasonlóság' szekció."
    
    bold_freebsd = similarity_section.find("strong", string="FreeBSD")
    assert bold_freebsd is not None, "A 'FreeBSD' szó nem félkövér a 'hasonlóság' szekcióban."

def test_lists():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    assert "GNOME, KDE, Xfce." in soup.text
    assert "openbox, fluxbox, dwm, bspwm." in soup.text

def test_em_freebsd():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    assert soup.find("em", string="FreeBSD") is not None

def test_bsd_emphasis():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    bsd_section = soup.find("strong", string=lambda x: x and "Berkeley Software Distribution" in x)
    assert bsd_section is not None, "'Berkeley Software Distribution' nincs félkövér és dőlt kiemeléssel."

def test_footer():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    footer = soup.footer
    assert footer is not None
    assert "2025" in footer.text

# Tesztek futtatása
if __name__ == "__main__":
    create_html()
    pytest.main()
