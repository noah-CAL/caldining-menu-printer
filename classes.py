import bs4
from bs4 import BeautifulSoup

class HTMLElement:
    """Data Abstraction that stores the HTML and plaintext of an HTML tag"""

    def __init__(self, soup):
        self.soup = soup
        self.text = soup.find('span').get_text()
    
    def __str__(self):
        return self.text

class HTMLCollection:
    """Data Abstraction that contains groups of HTMLElements of a specific type (i.e. DiningHalls, Menus, etc.)"""
    def __init__(self, soup, tag, class_):
        assert isinstance(soup, bs4.element.Tag), f'soup {soup} must be of type soup!'
        self.collection = [HTMLElement(el) for el in soup.find_all(tag, class_=class_)]
    
    def __str__(self):
        return '\n'.join([str(el) for el in self.collection])