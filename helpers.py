import random
import time
import os
import sys
from string import ascii_lowercase
# Imported from my own created files
from questions import EASY_QUESTIONS, MED_QUESTIONS, HARD_QUESTIONS
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
    print(f'{BLUE_FOREGROUND}{CENTER("⛅ " + title + " 🌧️").upper()}')
    print(f'{BLUE_FOREGROUND}{BRIGHT_STYLING}{THICK_LINE_STYLE}')
    time.sleep(0.10)
    print(CENTER('Welcome to an engaging quiz game that tests your knowledge about various weather phenomena, including types of storms, climate patterns, and weather forecasting!'))
    print(f'{BLUE_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    time.sleep(0.30)


def checker(user_selects, selections):
    """
    Tests whether the user inputted a correct selection, if not shows an error.
    """
    try:
        if user_selects not in selections:
            raise ValueError
    except ValueError:
        remove()
        print(f'{RED_BG}{WHITE_FOREGROUND}{BRIGHT_STYLING}{CENTER(f'⛔️Error: {user_selects} is not valid! Please select {selections}.⛔️')}')
        time.sleep(0.05)
        print()

        input(f'{CENTER("Click ENTER to continue")}\n')
        remove()
        return False

    return True


def remove():
    """
    Remove content from the terminal for easier reading.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def rules(title):
    """
    Prints instructions on how to play the game.
    """
    print(f'{MAGENTA_FOREGROUND}{CENTER(title + " 📃").upper()}')
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    time.sleep(0.20)
    print()
    print(CENTER('When on the main menu screen, when asked what to do you can either choose to'))
    time.sleep(0.05)
    print(CENTER('type 1 which brings you to these rules, '))
    time.sleep(0.05)
    print(CENTER('type 2 which will let you play the game'))
    time.sleep(0.05)
    print(CENTER('or type 3 which will allow you to quit the game.'))
    time.sleep(0.05)
    print()
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
    print()
    input(f'{CENTER("Click ENTER to continue")}\n')

    print(CENTER('Once you have chosen your difficulty, you will then be asked the amount of questions you would like.'))
    time.sleep(0.05)
    print(CENTER('You can type 1 for 10 questions, '))
    time.sleep(0.05)
    print(CENTER('type 2 for 20 questions'))
    time.sleep(0.05)
    print(CENTER('or type 3 for 30 questions.'))
    time.sleep(0.05)
    print()
    input(f'{CENTER("Click ENTER to continue")}\n')

    print(CENTER('When you have chosen the amount of questions, '))
    time.sleep(0.05)
    print(CENTER('you will then start the quiz.'))
    time.sleep(0.05)
    print(CENTER('For the quiz you will have to answer'))
    time.sleep(0.05)
    print(CENTER('a, b, c or d, either in lowercase or uppercase.'))
    time.sleep(0.05)
    print()
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
    print()
    input(f'{CENTER("Click ENTER to return to menu.")}\n')


def exit():
    """
    Closes the program if the user wants to
    """
    time.sleep(0.10)
    print(f'{BLACK_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    print(f'\n{CENTER("are you sure you want to leave?")}\n')
    time.sleep(0.05)

    exit_selects = input(f"{CENTER('type y if you want to leave or type n to stay.\n\n')}")
    exit_selections = ['y', 'n']

    if exit_checker(exit_selects, exit_selections):

        remove()
        # Closes the program
        if exit_selects == 'y':
            time.sleep(0.10)
            print(f"{CENTER('Thankyou for playing, goodbye.')}")
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


def exit_checker(exit_selects, exit_selections):
    """
    Tests whether the user inputted a correct selection, if not shows an error.
    """
    try:
        if exit_selects not in exit_selections:
            raise ValueError
    except ValueError:
        remove()
        print(f'{WHITE_FOREGROUND}{RED_BG}{BRIGHT_STYLING}{CENTER(f'⛔️Error: {exit_selects} is not valid! Please select {exit_selections}.⛔️')}')
        time.sleep(0.05)
        print()

        input(f'{CENTER("Click ENTER to continue.")}\n')
        remove()
        return False

    return True


def level_selector():
    """
    Lets user choose what difficulty of questions that will be asked.
    """
    while True:
        remove()
        print(f'{GREEN_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
        print()
        print("What level of difficulty would you like?")
        print()
        time.sleep(0.10)
        print('1. Easy')
        time.sleep(0.05)
        print('2. Medium')
        time.sleep(0.05)
        print('3. Hard')
        time.sleep(0.10)

        level_selects = input(f'\nWhich option would you like to select? {GREEN_FOREGROUND}[1-3]\n\n').strip()
        level_selections = ['1', '2', '3']

        if level_checker(level_selects, level_selections):

            remove()
            # Choses the easy questions
            if level_selects == '1':
                questions_amount()
            # Choses the medium questions
            elif level_selects == '2':
                questions_amount()
            # Choses the hard questions
            elif level_selects == '3':
                questions_amount()


def level_checker(level_selects, level_selections):
    """
    Tests whether the user inputted a correct selection, if not shows an error.
    """
    try:
        if level_selects not in level_selections:
            raise ValueError
    except ValueError:
        remove()
        print(f'{WHITE_FOREGROUND}{RED_BG}{BRIGHT_STYLING}{CENTER(f'⛔️Error: {level_selects} is not valid! Please select {level_selections}.⛔️')}')
        time.sleep(0.05)
        print()

        input(f'{CENTER("Click ENTER to continue.")}\n')
        remove()
        return False

    return True


def questions_amount():
    """
    Lets user choose the amount of questions they will like.
    """
    while True:
        remove()
        print(f'{GREEN_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')

        print()
        print("How many questions would you like to answer?:\n")
        time.sleep(0.10)
        print()
        print('1. 10')
        time.sleep(0.05)
        print('2. 20')
        time.sleep(0.05)
        print('3. 30')
        time.sleep(0.10)
    
        amount_selects = input(f'\nWhich option would you like to select? {GREEN_FOREGROUND}[1-3]\n\n').strip()
        amount_selections = ['1', '2', '3']

        if amount_checker(amount_selects, amount_selections):
            remove()
            # Maps the users choice to the amount of questions
            question_count = {'1': 10, '2': 20, '3': 30}
            # Calls the function with the selected number of questions
            easy_random_questions(question_count[amount_selects])
            break


def amount_checker(amount_selects, amount_selections):
    """
    Tests whether the user inputted a correct selection, if not shows an error.
    """
    try:
        if amount_selects not in amount_selections:
            raise ValueError
    except ValueError:
        remove()
        print(f'{WHITE_FOREGROUND}{RED_BG}{BRIGHT_STYLING}{CENTER(f'⛔️Error: {amount_selects} is not valid! Please select {amount_selections}.⛔️')}')
        time.sleep(0.05)
        print()

        input(f'{CENTER("Click ENTER to continue.")}\n')
        remove()
        return False

    return True


def easy_random_questions(num_questions):
    """
    shuffles randomly chosen questions from the easy questions list.
    """
    print(f"{GREEN_FOREGROUND}{BRIGHT_STYLING}{CENTER('Loading.....')}")
    time.sleep(3)
    remove()
    total = 0

    # Selects the number of questions requested by the user
    selected_questions = random.sample(EASY_QUESTIONS, num_questions)

    # Loops the selected questions
    for num, qst_data in enumerate(selected_questions):
        question = qst_data['question']
        choices = qst_data['choices']
        answers = qst_data['answer']

        print(f'{GREEN_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
        print()
        print(f'Q{num + 1}: ')

        total += next_easy_qst(question, choices, answers)
        time.sleep(0.5)

        input(f'{CENTER("Click Enter to continue")}\n')
        remove()

    print(f"{GREEN_BG}{WHITE_FOREGROUND}{CENTER(f'🎉 Well done! You scored: {total}/{num_questions} 🎉')}")
    time.sleep(0.10)

    # Option to play again or quit
    print()
    easy_selects = input(f"{CENTER('type y if you want to play again or type n to quit.\n\n')}")
    easy_selections = ['y', 'n']

    if easy_checker(easy_selects, easy_selections):
        remove()
        # Goes back to difficulty section
        if easy_selects == 'y':
            level_selector()
        # Starts the process of exiting the game
        elif easy_selects == 'n':
            exit()


def easy_checker(easy_selects, easy_selections):
    """
    Tests whether the user inputted a correct selection, if not shows an error.
    """
    try:
        if easy_selects not in easy_selections:
            raise ValueError
    except ValueError:
        remove()
        print(f'{WHITE_FOREGROUND}{RED_BG}{BRIGHT_STYLING}{CENTER(f'⛔️Error: {qst_selects} is not valid! Please select {qst_selections}.⛔️')}')
        time.sleep(0.05)
        print()

        input(f'{CENTER("Click ENTER to continue.")}\n')
        remove()
        return False

    return True


def next_easy_qst(qst, choice, right_choice):
    """
    Brings up the next question and checks if the user is correct or incorrect.
    """
    sort_choice = random.sample(choice, len(choice))

    answer = user_answered_select(qst, sort_choice)
    if answer == right_choice:
        print(f"{CENTER('✅Correct!✅')}")
        time.sleep(0.05)
        print()
        return 1
    else:
        print(f"{CENTER('❌Incorrect!❌')}")
        time.sleep(0.05)
        print()
        return 0


def user_answered_select(qst, choice):
    """
    Shows the question and choices, and gets the user's input 
    """
    print(f"{qst}")
    tag_choice = dict(zip(ascii_lowercase, choice))

    for tag, choice_data in tag_choice.items():
        print(f" {tag}) {choice_data}")
    # Handles user errors
    while (
         answer_tag := input(f"{CENTER('Answer?')} ").lower()) not in tag_choice:
        print(f"Please answer one of {', '.join(tag_choice.keys())}")

    return tag_choice[answer_tag]