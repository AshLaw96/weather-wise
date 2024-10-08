import time
import sys
# Imports from own created file
from checks import CheckerFactory
# Allows colour to be added to python code
import colorama
from colorama import Fore, Back, Style
# Resets colour after every use
colorama.init(autoreset=True)


class StyleHelper:
    """
    Handles all the styling operations and definitions.
    """
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


class ProgramHelper:
    """
    Handles all the helper functions.
    """
    def remove():
        """
        Remove content from the terminal for easier reading.
        """
        print('\033c')

    def exit():
        """
        Closes the program if the user wants to
        """
        time.sleep(0.10)
        print(f'{StyleHelper.BLACK_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
              f'{StyleHelper.THIN_LINE_STYLE}')
        print()
        print(f'\n{StyleHelper.CENTER("Are you sure you want to leave?")}\n')
        time.sleep(0.05)

        exit_selects = input(
            f"{StyleHelper.CENTER(
                'Type Y if you want to leave or type N to stay.\n\n')}"
        ).strip().lower()

        exit_selections = ['y', 'n']

        exit_checker = CheckerFactory.get_checker('exit', exit_selections)
        if exit_checker.check(exit_selects, "Invalid menu selection"):
            ProgramHelper.remove()
            # Closes the program
            if exit_selects == 'y':
                time.sleep(0.10)
                print()
                print(f"{StyleHelper.CENTER(
                    'Thank you for playing, goodbye. 👋')}")
                print(f'{StyleHelper.BLACK_FOREGROUND}'
                      f'{StyleHelper.BRIGHT_STYLING}'
                      f'{StyleHelper.THIN_LINE_STYLE}')
                time.sleep(1)
                sys.exit()
            # Returns to menu
            elif exit_selects == 'n':
                time.sleep(0.10)
                print()
                print(f'{StyleHelper.BLACK_FOREGROUND}'
                      f'{StyleHelper.BRIGHT_STYLING}'
                      f'{StyleHelper.THIN_LINE_STYLE}')
                print()

                input(f'{StyleHelper.CENTER(
                    "Click ENTER to return to menu.")}\n')

    def loading_message():
        """
        Displays a 'Loading, please wait...' message with dots
        appearing one by one.
        """
        message = (
            f'{StyleHelper.GREEN_FOREGROUND}'
            f'{StyleHelper.BRIGHT_STYLING}Loading, please wait'
        )
        dots = '...'

        # prints the text first
        sys.stdout.write(message)
        # Ensures immediate display
        sys.stdout.flush()

        for dot in dots:
            time.sleep(0.40)
            # Makes dot stay on same line
            sys.stdout.write(f'{StyleHelper.GREEN_FOREGROUND}'
                             f'{StyleHelper.BRIGHT_STYLING}{dot}')
            sys.stdout.flush()

        print()
