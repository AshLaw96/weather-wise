import time
import sys
# Imports from own created file
from checks import exit_checker
# Allows colour to be added to python code
import colorama
from colorama import Fore, Back, Style
# Resets colour after every use
colorama.init(autoreset = True)

# Creates 80 character length lines
THICK_LINE_STYLE = '━' * 80
THIN_LINE_STYLE = '_' * 80

# Horizontally centers 80 characters wide 
CENTER = '{:^80}'.format

# All colours in Colorama library
RED_FOREGROUND = Fore.RED
RED_BG = Back.RED

GREEN_FOREGROUND = Fore.GREEN
GREEN_BG = Back.GREEN

YELLOW_FOREGROUND = Fore.YELLOW
YELLOW_BG = Back.YELLOW

BLUE_FOREGROUND = Fore.BLUE
BLUE_BG = Back.BLUE

MAGENTA_FOREGROUND = Fore.MAGENTA
MAGENTA_BG = Back.MAGENTA

CYAN_FOREGROUND = Fore.CYAN
CYAN_BG = Back.CYAN

WHITE_FOREGROUND = Fore.WHITE
WHITE_BG = Back.WHITE

BLACK_FOREGROUND = Fore.BLACK
BLACK_BG = Back.BLACK

DIM_STYLING = Style.DIM
NORM_STYLING = Style.NORMAL
BRIGHT_STYLING = Style.BRIGHT

def remove():
    """
    Remove content from the terminal for easier reading.
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def exit():
    """
    Closes the program if the user wants to
    """
    time.sleep(0.10)
    print(f'{BLACK_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    print(f'\n{CENTER("Are you sure you want to leave?")}\n')
    time.sleep(0.05)

    exit_selects = input(f"{CENTER('Type Y if you want to leave or type N to stay.\n\n')}").strip().lower()
    exit_selections = ['y', 'n']

    if exit_checker(exit_selects, exit_selections):

        remove()
        # Closes the program
        if exit_selects == 'y':
            time.sleep(0.10)
            print()
            print(f"{CENTER('Thank you for playing, goodbye.')}")
            print(f'{BLACK_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
            time.sleep(1)
            sys.exit()
        # Returns to menu
        elif exit_selects == 'n':
            time.sleep(0.10)
            print()
            print(f'{BLACK_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
            print()

            input(f'{CENTER("Click ENTER to return to menu.")}\n')


def loading_message():
    """
    Displays a 'Loading, please wait...' message with dots
    appearing one by one.
    """
    message = f'{GREEN_FOREGROUND}{BRIGHT_STYLING}Loading, please wait'
    dots = '...'

    # prints the text first
    sys.stdout.write(message)
    # Ensures immediate display
    sys.stdout.flush()

    for dot in dots:
        time.sleep(0.10)
        # Makes dot stay on same line
        sys.stdout.write(f'{GREEN_FOREGROUND}{BRIGHT_STYLING}{dot}')
        sys.stdout.flush()

    print()
