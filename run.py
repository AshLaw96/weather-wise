import time
# Imported from my own created files
from helpers import header, remove, rules, checker, exit, BLUE_FOREGROUND
from game import level_selector


def menu():
    """
    Shows the main menu of the program.
    """
    while True:
        remove()
        header('weather wise')

        print()
        print("Here's what you can do:\n")
        time.sleep(0.10)
        print()
        print('1. show rules')
        time.sleep(0.05)
        print('2. play game')
        time.sleep(0.05)
        print('3. exit program')
        time.sleep(0.10)
    
        user_selects = input(f'\nWhich option would you like to select? {BLUE_FOREGROUND}[1-3]\n\n').strip()
        selections = ['1', '2', '3']

        if checker(user_selects, selections):
            remove()
            # Shows rules of game
            if user_selects == '1':
                rules('rules')
            # Starts the process of the game
            elif user_selects == '2':
                level_selector()
            # Starts the process of exiting the game
            elif user_selects == '3':
                exit()


tests = menu()

print(tests)