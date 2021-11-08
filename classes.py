from types import FunctionType
import bs4
from bs4 import BeautifulSoup

class HTMLElement:
    """Data Abstraction that stores the HTML and plaintext of an HTML tag"""

    def __init__(self, soup):
        self.soup = soup
        self.text = soup.find('span').get_text()
    
    def get_soup(self):
        return self.soup
    
    def get_text(self):
        return self.text

    def __str__(self):
        return self.text

class HTMLCollection:
    """Data Abstraction that contains groups of HTMLElements of a specific type (i.e. DiningHalls, Menus, etc.)"""
    def __init__(self, soup, tag, class_, key: FunctionType=None):
        """Creats a container of HTMLElements for which key(HTMLelement) is true (or key=None by default)"""
        assert isinstance(soup, bs4.element.Tag), f'soup {soup} must be of type soup!'
        self.collection = list(filter(key, [HTMLElement(el) for el in soup.find_all(tag, class_=class_)]))
    
    def get_elements(self):
        return self.collection

    def __str__(self):
        return '\n'.join([str(el) for el in self.collection])
    
    def __iter__(self):
        return iter(self.collection)
    
    BANNED_STATIONS = [
        # CAFE 3
        'HOT CEREAL',
        'PASTRIES',
        'FRUIT',
        'KOSHER DELI',
        'KOSHER DELI (Per Request)',
        'SALADS',
        'DESSERT',
        'SOUPS',
        # CLARK KERR CAMPUS
        'SOUP & SALAD'
        # CROSSROADS
        'HOT MORNING GRAINS',
        'BREAKFAST BREAD',
        'DAILY RICE',
        'BEAR FIT',
        'SALADS',
        'DELI',
        # FOOTHILL
        'DAILY RICE',
        'DAILY HOT GRAINS',
        'FIT BOWL',
        'DELI',
        'FIT BOWL',
        'MAIN LINE VEGGIE',
    ]