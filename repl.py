from scraper import *
from time import sleep
import os

if __name__ == '__main__':
    menu = create_menu(URL)

    start_msg = """Welcome to the Menu REPL!"""
    help_msg = """Commands:
    Commands:
    help           -- prints the command menu
    tree           -- prints the menu tree
    pretty-print   -- prettily prints the menu tree"""

    def repl():
        commands = {
            'help': print_commands,
            'tree': print_menu_tree,
            'pretty-print': pretty_print_tree
        }
        print(start_msg)
        print(help_msg)
        while True:
            print('\n')
            user_input = input('Enter a command: ').strip()
            try:
                commands[user_input]()
            except KeyError as e:
                print(f'"{user_input}" is an incorrect command.')

    def print_commands():
        print(help_msg)


    def print_menu_tree(delay=0):
        for dining_hall in menu:
            print('\n'*2, '## ' + dining_hall.get_text().upper() + ' ##')
            for mealtime in dining_hall:
                print('\n','', mealtime)
                sleep(delay)
                for station in mealtime:
                    print('\n', '  ', station)
                    sleep(delay)
                    for food in station:
                        print('\n ', '   ', food)
                        sleep(delay)
            if delay:
                sleep(delay * 100 + 2)
                os.system('clear')

    def pretty_print_tree():
        print_menu_tree(0.03)
        print_commands()

    repl()