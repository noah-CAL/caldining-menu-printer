## SETUP ##
import requests
from bs4 import BeautifulSoup

from classes import HTMLCollection
# from classes import *

URL = 'https://caldining.berkeley.edu/menus/'

if __name__ == '__main__':
    with open('example.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
else:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
## END SETUP ##

def setup(url=URL, test=False):
    dining_hall_collection = HTMLCollection(soup, 'li', 'location-name') 
    print(dining_hall_collection)

if __name__ == '__main__':
    URL = 'https://example.html'
    setup(URL, test=True)