import requests
from bs4 import BeautifulSoup

from classes import HTMLCollection
from classes import DiningHall, Mealtime, FoodStation, FoodItem
# from classes import *

URL = 'https://caldining.berkeley.edu/menus/'

## SETUP TEST CODE ##

EXAMPLE_HTML = False ## Manually set to True to use the example HTML page
if __name__ == '__main__' and EXAMPLE_HTML: 
    with open('example.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
else:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
## END SETUP ##

def create_menu(url=URL, test=False):
    dining_hall_collection = HTMLCollection(soup, DiningHall, 'li', 'location-name') 
    for dining_hall in dining_hall_collection:
        test and print('\n'*2, dining_hall.get_text().upper())
        mealtime_collection = HTMLCollection(dining_hall.get_soup(), Mealtime, 'li', 'preiod-name')
        for mealtime in mealtime_collection:
            dining_hall.add_mealtime(mealtime)
            test and print('\n ', mealtime)
            station_collection = HTMLCollection(
                mealtime.get_soup(), FoodStation, 'div', 'cat-name', 
                key=lambda element: element.get_text() not in FoodStation.BANNED_STATIONS
            )
            for station in station_collection:
                mealtime.add_station(station)
                test and print('  ', station)
                food_collection = HTMLCollection(station.get_soup(), FoodItem, 'li', 'recip')
                for food in food_collection:
                    test and print('     ', food)
                    station.add_food(food)

    return dining_hall_collection


if __name__ == '__main__':
    # URL = 'https://example.html'
    menu = create_menu(URL, test=False)

    def print_menu_tree():
        for dining_hall in menu:
            print('\n'*2, '## ' + dining_hall.get_text().upper() + ' ##')
            for mealtime in dining_hall:
                print('\n','', mealtime)
                for station in mealtime:
                    print('\n', '  ', station)
                    for food in station:
                        print('\n ', '   ', food)
    print_menu_tree()