import time
# Imported from my own created files
from game import level_selector
from checks import checker
from helpers import remove, BLUE_FOREGROUND, BRIGHT_STYLING, THICK_LINE_STYLE, CENTER, MAGENTA_FOREGROUND, THIN_LINE_STYLE, exit

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
    
        user_selects = input(f'\nWhich option would you like to select? {BLUE_FOREGROUND}{BRIGHT_STYLING}[1-3]\n\n').strip()
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


def header(title):
    """
    Makes the header section and styles it.
    """
    print(f'{BLUE_FOREGROUND}{BRIGHT_STYLING}{THICK_LINE_STYLE}')
    print(f'{BLUE_FOREGROUND}{BRIGHT_STYLING}{CENTER("⛅ " + title + " 🌧️").upper()}')
    print(f'{BLUE_FOREGROUND}{BRIGHT_STYLING}{THICK_LINE_STYLE}')
    time.sleep(0.10)
    print(CENTER('Welcome to an engaging quiz game that tests your knowledge about various weather phenomena, including types of storms, climate patterns, and weather forecasting!'))
    print(f'{BLUE_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    time.sleep(0.30)


def rules(title):
    """
    Prints instructions on how to play the game.
    """
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    print()
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{CENTER(title + " 📃").upper()}')
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    time.sleep(0.20)
    print()
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

    remove()
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    print()
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{CENTER(title + " 📃").upper()}')
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    print()
    print(CENTER('Once you have chosen your difficulty, '))
    time.sleep(0.05)
    print(CENTER('you will then be asked the amount of questions you would like.'))
    time.sleep(0.05)
    print(CENTER('You can type 1 for 10 questions, '))
    time.sleep(0.05)
    print(CENTER('type 2 for 20 questions'))
    time.sleep(0.05)
    print(CENTER('or type 3 for 30 questions.'))
    time.sleep(0.05)
    print()
    input(f'{CENTER("Click ENTER to continue")}\n')

    remove()
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    print()
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{CENTER(title + " 📃").upper()}')
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    print()
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

    remove()
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    print()
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{CENTER(title + " 📃").upper()}')
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    print()
    print(CENTER('Once you have answered all your questions, '))
    time.sleep(0.05)
    print(CENTER('your score will be added and shown to you.'))
    time.sleep(0.05)
    print(CENTER('You will then be asked to input your name and once inputted, '))
    time.sleep(0.05)
    print(CENTER('Your score, name, difficulty level, amount of questions and'))
    time.sleep(0.05)
    print(CENTER('the time/date you achieved this will be added to a leaderboard.'))
    time.sleep(0.05)
    print()
    input(f'{CENTER("Click ENTER to continue.")}\n')

    remove()
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    print()
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{CENTER(title + " 📃").upper()}')
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    print()
    print(CENTER('You will then be asked if you would like to play again or quit.'))
    time.sleep(0.05)
    print(CENTER('You will have to type y to play again'))
    time.sleep(0.05)
    print(CENTER('or type n to quit.'))
    time.sleep(0.05)
    print(CENTER('If you type y you will be taken back to the difficulty section, '))
    time.sleep(0.05)
    print(CENTER('but if you type n you will go through the quitting process.'))
    time.sleep(0.05)
    print()
    input(f'{CENTER("Click ENTER to continue.")}\n')

    remove()
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    print()
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{CENTER(title + " 📃").upper()}')
    print(f'{MAGENTA_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
    print()
    print(CENTER('If you choose 3 in the main menu you will then be asked if you are sure you want to quit.'))
    time.sleep(0.05)
    print(CENTER('You can either type y in uppercase or lowercase to quit the game'))
    time.sleep(0.05)
    print(CENTER('or type n in uppercase or lowercase for no, which will take you back to the main menu.'))
    time.sleep(0.05)
    print()
    input(f'{CENTER("Click ENTER to return to menu.")}\n')

tests = menu()

print(tests)