from scraper import *
from time import sleep
import os
import sys

if __name__ == '__main__':
    menu = create_menu(URL)

    start_msg = """Welcome to the Menu REPL!"""
    help_msg = """Commands:
    help                -- prints the command menu
    tree                -- prints the menu tree
    slideshow           -- prints a slideshow of the menu tree
    quit                -- quits the program
    menu cafe-3         -- prints the menu for a specific dining hall
         clark-kerr
         croads
         foothill"""

    def repl():
        commands = {
            'help': print_commands,
            'tree': print_menu_tree,
            'slideshow': menu_slideshow,
            'menu': print_hall_menu,
            'quit': repl_quit,
            'q': repl_quit,
        }
        print(start_msg)
        print(help_msg)
        while True:
            print('\n')
            try:
                user_input = input('Enter a command: ').strip().split()
                command = user_input[0]
                args = user_input[1:]
                commands[command](*args)
            except (KeyboardInterrupt, EOFError) as e:
                repl_quit() 
            except KeyError as e:
                print(f"\"{' '.join(user_input)}\" is an incorrect command.")
            except IndexError: # user presses Enter key
                pass

    def print_commands(*args):
        print(help_msg)

    def print_menu_tree(*args, menu=menu, delay=0):
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

    def menu_slideshow(*args):
        print_menu_tree(0.03)
        print_commands()
    
    def print_hall_menu(*args):
        if len(args) == 0:
            raise TypeError('At least one argument expected')
        try:
            arg_to_names = {
                'cafe-3': 'Cafe 3',
                'clark-kerr': 'Clark Kerr Campus',
                'croads': 'Crossroads',
                'foothill': 'Foothill',
            } 
            new_args = [arg_to_names.get(arg) for arg in args]
            simple_menu = [dining_hall for dining_hall in menu if dining_hall.get_text() in new_args]
            print_menu_tree(menu=simple_menu) # call print_menu_tree with menu == [dining_hall]
        except TypeError as e:
            print(f"{str(args)} contains an invalid argument")
            print(e)

    def repl_quit(*args):
        print('\nThanks for using the program!')
        sys.exit()

    repl()