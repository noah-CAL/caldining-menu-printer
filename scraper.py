import requests
from bs4 import BeautifulSoup

from classes import HTMLCollection
# from classes import *

URL = 'https://caldining.berkeley.edu/menus/'

## SETUP TEST CODE ##
# if __name__ == '__main__':
#     with open('example.html', 'r') as f:
#         soup = BeautifulSoup(f, 'html.parser')
# else:
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
## END SETUP ##

def setup(url=URL, test=False):
    dining_hall_collection = HTMLCollection(soup, 'li', 'location-name') 
    for dining_hall in dining_hall_collection:
        test and print('\n'*2, dining_hall.get_text().upper())
        mealtime_collection = HTMLCollection(dining_hall.get_soup(), 'li', 'preiod-name')
        for mealtime in mealtime_collection:
            test and print('\n ', mealtime)
            station_collection = HTMLCollection(
                mealtime.get_soup(), 'div', 'cat-name', 
                key=lambda element: element.get_text() not in HTMLCollection.BANNED_STATIONS
            )
            for station in station_collection:
                test and print('  ', station)
                food_collection = HTMLCollection(station.get_soup(), 'li', 'recip')
                for food in food_collection:
                    test and print('     ', food)

if __name__ == '__main__':
    # URL = 'https://example.html'
    setup(URL, test=True)