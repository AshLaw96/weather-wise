import random
import time
import os
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


def header(title):
    """
    Makes the header section and styles it.
    """
    print(f'{BLUE_FOREGROUND}{BRIGHT_STYLING}{THICK_LINE_STYLE}')
    print(f'{BLUE_FOREGROUND}{CENTER(title).upper()}')
    print(f'{BLUE_FOREGROUND}{BRIGHT_STYLING}{THICK_LINE_STYLE}')
    time.sleep(0.10)
    print(CENTER('Welcome to an engaging quiz game that tests your knowledge about various weather phenomena, including types of storms, climate patterns, and weather forecasting!'))
    print(f'{BLUE_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    time.sleep(0.30)


def remove():
    """
    Remove content from the terminal for easier reading.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def rules(title):
    """
    Prints instructions on how to play the game.
    """
    print(f'{MAGENTA_FOREGROUND}{CENTER(title).upper()}')
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    time.sleep(0.20)
    print('')
    print(CENTER('When on the main menu screen, when asked what to do you can either choose to'))
    time.sleep(0.05)
    print(CENTER('type 1 which brings you to these rules, '))
    time.sleep(0.05)
    print(CENTER('type 2 which will let you play the game'))
    time.sleep(0.05)
    print(CENTER('or type 3 which will allow you to quit the game.'))
    time.sleep(0.05)
    print('')
    input(f'{CENTER("Click ENTER to continue")}\n')

    print(CENTER('When typing 2 into the terminal it will then ask, '))
    time.sleep(0.05)
    print(CENTER('what difficulty level would you like'))
    time.sleep(0.05)
    print(CENTER('type 1 for easy, '))
    time.sleep(0.05)
    print(CENTER('type 2 for medium'))
    time.sleep(0.05)
    print(CENTER('or type 3 for hard.'))
    time.sleep(0.05)
    print('')
    input(f'{CENTER("Click ENTER to continue")}\n')

    print(CENTER('Once you have chosen your difficulty, you will then be asked the amount of questions you would like.'))
    time.sleep(0.05)
    print(CENTER('You can type 1 for 10 questions, '))
    time.sleep(0.05)
    print(CENTER('type 2 for 20 questions'))
    time.sleep(0.05)
    print(CENTER('or type 3 for 30 questions.'))
    time.sleep(0.05)
    print('')
    input(f'{CENTER("Click ENTER to continue")}\n')

    print(CENTER('When you have chosen the amount of questions, '))
    time.sleep(0.05)
    print(CENTER('you will then start the quiz.'))
    time.sleep(0.05)
    print(CENTER('For the quiz you will have to answer'))
    time.sleep(0.05)
    print(CENTER('a, b, c or d, either in lowercase or uppercase.'))
    time.sleep(0.05)
    print('')
    input(f'{CENTER("Click ENTER to continue")}\n')

    print(CENTER('Once you have answered all your questions, '))
    time.sleep(0.05)
    print(CENTER('your score will be added and shown to you.'))
    time.sleep(0.05)
    print(CENTER('You will then be asked if you would like to play again or quit.'))
    time.sleep(0.05)
    print(CENTER('You will have to type 1 to play again'))
    time.sleep(0.05)
    print(CENTER('or type 2 to quit.'))
    time.sleep(0.05)
    print(CENTER('If you type 1 you will be taken back to the main menu, '))
    time.sleep(0.05)
    print(CENTER('but if you type 2 you will be asked again if your sure you want to quit'))
    time.sleep(0.05)
    print(CENTER('and you can either type y in uppercase or lowercase if you do, '))
    time.sleep(0.05)
    print(CENTER("or type n in uppercase or lowercase if you don't"))
    time.sleep(0.05)
    print('')
    input(f'{CENTER("Click ENTER to return to menu")}\n')
    print('')
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')


def exit():
    """
    Closes the program if the user wants to
    """
    time.sleep(0.10)
    print(f'{BLACK_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    print(f'\n{CENTER("are you sure you want to leave?")}\n')
    time.sleep(0.05)

    exit_selects = input(f"{CENTER('type y if you want to leave or type n to stay\n\n')}")
    exit_selections = ['y', 'n']

    if exit_checker(exit_selects, exit_selections):

        remove()
        # Closes the program
        if exit_selects == 'y':
            time.sleep(0.10)
            print(f"{CENTER('Thankyou for playing, goodbye')}")
            print(f'{BLACK_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
            time.sleep(1)
            sys.exit()
        # Returns to menu
        elif exit_selects == 'n':
            time.sleep(0.10)
            print('')
            print(f'{BLACK_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
            print('')
            input(f'{CENTER("Click ENTER to return to menu")}\n')


def checker(user_selects, selections):
    """
    Tests whether the user inputted a correct selection, if not shows an error.
    """
    try:
        if user_selects not in selections:
            raise ValueError
    except ValueError:
        remove()
        print(print(f'{RED_FOREGROUND}{RED_BG}{BRIGHT_STYLING}{THIN_LINE_STYLE}'))
        print(f'{RED_FOREGROUND}{CENTER(f'Error: {user_selects} is not valid! Please select {selections}')}.')
        print(print(f'{RED_FOREGROUND}{RED_BG}{BRIGHT_STYLING}{THIN_LINE_STYLE}'))
        time.sleep(0.05)
        print('')

        input(f'{CENTER("Click ENTER to continue")}\n')
        remove()
        return False

    return True


def exit_checker(exit_selects, exit_selections):
    """
    Tests whether the user inputted a correct selection, if not shows an error.
    """
    try:
        if exit_selects not in exit_selections:
            raise ValueError
    except ValueError:
        remove()
        print(print(f'{RED_BG}{BRIGHT_STYLING}{THIN_LINE_STYLE}'))
        print(f'{RED_FOREGROUND}{CENTER(f'Error: {exit_selects} is not valid! Please select {exit_selections}')}.')
        print(print(f'{RED_BG}{BRIGHT_STYLING}{THIN_LINE_STYLE}'))
        time.sleep(0.05)
        print('')

        input(f'{CENTER("Click ENTER to continue")}\n')
        remove()
        return False

    return True