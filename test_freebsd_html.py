import pytest
from bs4 import BeautifulSoup

def load_html():
    with open("index.html", "r", encoding="utf-8") as f:
        return BeautifulSoup(f, "html.parser")

def test_language_setting():
    soup = load_html()
    assert soup.html.get("lang") == "hu", "Az oldal nyelve nem magyar."

def test_charset():
    soup = load_html()
    assert soup.meta.get("charset") == "utf-8", "Nem megfelelő karakterkódolás."

def test_title():
    soup = load_html()
    assert soup.title.string == "FreeBSD", "A böngészőfül felirata nem megfelelő."

def test_heading():
    soup = load_html()
    assert soup.h1.string == "FreeBSD", "A főcím nem megfelelő."

def test_bold_freebsd():
    soup = load_html()
    paragraphs = soup.find_all("p")
    assert any("FreeBSD" in p.text and p.find("strong") for p in paragraphs), "A FreeBSD szó nincs félkövérrel jelölve."

def test_bold_italic_bsd():
    soup = load_html()
    paragraph = soup.find(string="Berkeley Software Distribution")  # Use string instead of text
    assert (
        paragraph and 
        paragraph.parent.name == "strong" and  # Közvetlen szülője <strong>
        paragraph.parent.parent.name == "em"  # Annak a szülője pedig <em>
    ), "A BSD szöveg nincs megfelelően formázva."


def test_highlighted_freebsd():
    soup = load_html()
    # Find all occurrences of FreeBSD in the document
    freebsd_elements = soup.find_all(string="FreeBSD")  # Use string instead of text
    highlighted = False

    # Check if any of the occurrences are inside <em> or <strong> tags
    for paragraph in freebsd_elements:
        if paragraph.parent.name in ["em", "strong"]:
            highlighted = True
            break  # Stop as soon as we find a highlighted occurrence
    
    assert highlighted, "A FreeBSD szó nincs kiemelve."


def test_list_formatting():
    soup = load_html()
    paragraphs = soup.find_all("p")
    lists = [p.text for p in paragraphs if "Elérhető asztali környezetek" in p.text or "Ablakkezelők" in p.text]
    assert all("," in lst and lst.strip().endswith(".") for lst in lists), "A felsorolások nem megfelelőek."

def test_footer():
    soup = load_html()
    footer = soup.find("footer")
    assert footer and "Név:" in footer.text and "Dátum:" in footer.text, "A lábléc nem megfelelő."
