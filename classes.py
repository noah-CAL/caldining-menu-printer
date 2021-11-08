from types import FunctionType
import bs4
from bs4 import BeautifulSoup

class HTMLElement:
    """Data Abstraction that stores the HTML and plaintext of an HTML tag"""

    def __init__(self, soup):
        self.soup = soup
        self.text = soup.find('span').get_text().strip()
    
    def get_soup(self):
        return self.soup
    
    def get_text(self):
        return self.text

    def __str__(self):
        return self.text

class HTMLCollection:
    """Data Abstraction that contains groups of HTMLElements of a specific type (i.e. DiningHalls, Menus, etc.)"""
    def __init__(self, soup, Subclass, tag, class_, key: FunctionType=None):
        """Creats a container of HTMLElements for which key(HTMLelement) is true (or key=None by default)"""
        assert isinstance(soup, bs4.element.Tag), f'soup {soup} must be of type soup!'
        assert issubclass(Subclass, HTMLElement), f'class {Subclass} is not a subclass of HTMLElement'
        self.collection = list(filter(key, [Subclass(el) for el in soup.find_all(tag, class_=class_)]))
    
    def get_elements(self):
        return self.collection

    def __str__(self):
        return '\n'.join([str(el) for el in self.collection])
    
    def __iter__(self):
        return iter(self.collection)

class DiningHall(HTMLElement):
    def __init__(self, soup):
        super().__init__(soup)
        self.mealtimes = {'Breakfast': None, 'Lunch': None, 'Dinner': None, 'Brunch': None}
    
    def add_mealtime(self, mealtime):
        assert isinstance(mealtime, Mealtime), f'mealtime {mealtime} is not of class Mealtime'
        if mealtime.get_text() not in self.mealtimes.keys():
            raise KeyError(f'Invalid time! {mealtime.get_text} -- {mealtime.get_text()} must be Breakfast, Lunch, Dinner, or Brunch')
        else:
            self.mealtimes[mealtime.get_text()] = mealtime
    
    def get_mealtime(self, time):
        """Returns a mealtime specified by TIME -- 'breakfast' 'lunch' 'dinner' 'brunch'"""
        try:
            return self.mealtimes[time]
        except KeyError as e:
            raise e(f'Invalid time! {time} must be Breakfast, Lunch, Dinner, or Brunch')

    def get_mealtimes(self) -> list:
        """Returns a dictionary of the dining hall's mealtime menus"""
        return self.mealtimes
    
    def __iter__(self):
        return iter([mealtime for mealtime in self.mealtimes.values() if mealtime != None])

class Mealtime(HTMLElement):
    def __init__(self, soup):
        super().__init__(soup)
        self.stations = []
    
    def add_station(self, station) -> None:
        assert isinstance(station, FoodStation), f'Invalid station -- {station} must be class of FoodStation'
        self.stations.append(station)

    def get_stations(self):
        """Returns a list of food stations"""
        return self.stations
    
    def __iter__(self):
        return iter(self.stations)

class FoodStation(HTMLElement):
    def __init__(self, soup):
        super().__init__(soup)
        self.foods = []
    
    def add_food(self, food):
        assert isinstance(food, FoodItem), f'Invalid food -- {food} must be of class FoodItem'
        self.foods.append(food)
    
    def get_foods(self):
        """Returns a list of every food in the station"""
        return self.foods
    
    def filter_foods(self, key=lambda: True):
        """Returns a list of all the foods that pass a certain filter (e.g. vegetarian options)."""
        #TODO
        return [food for food in self.foods if key(food)]
    
    def __iter__(self):
        return iter(self.foods)

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

class FoodItem(HTMLElement):
    def __init__(self, soup):
        super().__init__(soup)
        self.tags = []

    #TODO -- implement tagging feature on foods to store vegetarian, low-CO2, etc.
    def get_tags(self):
        pass 
    