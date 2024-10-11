import time
import sys
from checks import CheckerFactory
from helpers import StyleHelper, ProgramHelper
from game import QuizGame


class UIManager:
    """
    Handles the starting functions so the program can run.
    """
    def __init__(self):
        pass

    def menu(self):
        """
        Shows the main menu of the program.
        """
        while True:
            ProgramHelper.remove()
            self.header('weather wise')

            print()
            print("Here's what you can do:\n")
            time.sleep(0.10)

            print('1. Show rules')
            time.sleep(0.05)
            print('2. Play game')
            time.sleep(0.05)
            print('3. Exit program')
            time.sleep(0.10)

            user_selects = input(
                f'\nWhich option would you like to select? '
                f'{StyleHelper.BLUE_FOREGROUND}'
                f'{StyleHelper.BRIGHT_STYLING}[1-3]\n\n'
            ).strip()

            selections = ['1', '2', '3']

            # Get the correct checker
            checker = CheckerFactory.get_checker('menu', selections)
            if checker.check(user_selects, "Invalid menu selection"):
                ProgramHelper.remove()
                if user_selects == '1':
                    self.rules('rules')
                elif user_selects == '2':
                    quiz = QuizGame()
                    quiz.select_difficulty()
                elif user_selects == '3':
                    self.exit_game()

    def header(self, title):
        """
        Makes the header section and styles it.
        """
        print(
            f'{StyleHelper.BLUE_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.THICK_LINE_STYLE}'
        )
        print(
            f'{StyleHelper.BLUE_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.CENTER("⛅ " + title + " 🌧️").upper()}'
        )
        print(
            f'{StyleHelper.BLUE_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.THICK_LINE_STYLE}'
        )
        time.sleep(0.10)
        print(
            StyleHelper.CENTER(
                'Welcome to an engaging quiz game that tests your knowledge '
                'about various weather phenomena, including types of storms, '
                'climate patterns, and weather forecasting!'
            )
        )
        print(
            f'{StyleHelper.BLUE_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.THIN_LINE_STYLE}'
        )
        time.sleep(0.30)

    def rules(self, title):
        """
        Prints instructions on how to play the game.
        """
        print(
            f'{StyleHelper.MAGENTA_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.THIN_LINE_STYLE}'
        )
        print()
        print(
            f'{StyleHelper.MAGENTA_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.CENTER(title + " 📃").upper()}'
        )
        print(
            f'{StyleHelper.MAGENTA_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.THIN_LINE_STYLE}'
        )
        time.sleep(0.20)
        print()
        print(
            StyleHelper.CENTER(
                'When typing 2 into the terminal it will then ask, '
            )
        )
        time.sleep(0.05)
        print(StyleHelper.CENTER('what difficulty level would you like '))
        time.sleep(0.05)
        print(StyleHelper.CENTER('type 1 for easy, '))
        time.sleep(0.05)
        print(StyleHelper.CENTER('type 2 for medium '))
        time.sleep(0.05)
        print(StyleHelper.CENTER('or type 3 for hard.'))
        time.sleep(0.05)
        print()
        input(f'{StyleHelper.CENTER("Click ENTER to continue")}\n')

        ProgramHelper.remove()
        print(
            f'{StyleHelper.MAGENTA_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.THIN_LINE_STYLE}'
        )
        print()
        print(
            f'{StyleHelper.MAGENTA_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.CENTER(title + " 📃").upper()}'
        )
        print(
            f'{StyleHelper.MAGENTA_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.THIN_LINE_STYLE}'
        )
        print()
        print(
            StyleHelper.CENTER(
                'Once you have chosen your difficulty, you will then be asked '
            )
        )
        time.sleep(0.05)
        print(StyleHelper.CENTER('the amount of questions you would like.'))
        time.sleep(0.05)
        print(StyleHelper.CENTER(' You can type 1 for 10 questions, '))
        time.sleep(0.05)
        print(StyleHelper.CENTER('type 2 for 20 questions '))
        time.sleep(0.05)
        print(StyleHelper.CENTER('or type 3 for 30 questions.'))
        time.sleep(0.05)
        print()
        input(f'{StyleHelper.CENTER("Click ENTER to continue")}\n')

        ProgramHelper.remove()
        print(
            f'{StyleHelper.MAGENTA_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.THIN_LINE_STYLE}'
        )
        print()
        print(
            f'{StyleHelper.MAGENTA_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.CENTER(title + " 📃").upper()}'
        )
        print(
            f'{StyleHelper.MAGENTA_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.THIN_LINE_STYLE}'
        )
        print()
        print(
            StyleHelper.CENTER(
                'When you have chosen the amount of questions, '
            )
        )
        time.sleep(0.05)
        print(StyleHelper.CENTER('you will then start the quiz. '))
        time.sleep(0.05)
        print(StyleHelper.CENTER('For the quiz you will have to answer '))
        time.sleep(0.05)
        print(StyleHelper.CENTER(
            'a, b, c or d, either in lowercase or uppercase.'))
        time.sleep(0.05)
        print()
        input(f'{StyleHelper.CENTER("Click ENTER to continue")}\n')

        ProgramHelper.remove()
        print(
            f'{StyleHelper.MAGENTA_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.THIN_LINE_STYLE}'
        )
        print()
        print(
            f'{StyleHelper.MAGENTA_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.CENTER(title + " 📃").upper()}'
        )
        print(
            f'{StyleHelper.MAGENTA_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.THIN_LINE_STYLE}'
        )
        print()
        print(
            StyleHelper.CENTER(
                'Once you have answered all your'
                ' questions, '
            )
        )
        time.sleep(0.05)
        print(StyleHelper.CENTER(
                  'your score will be added and shown to you. '
            )
        )
        time.sleep(0.05)
        print(
            StyleHelper.CENTER(
                'You will then be asked to input your name and once inputted, '
            )
        )
        time.sleep(0.05)
        print(
            StyleHelper.CENTER(
                'Your score, name, difficulty level, amount of questions, '
            )
        )
        time.sleep(0.05)
        print(StyleHelper.CENTER(
                  'and when you achieved the result '
            )
        )
        time.sleep(0.05)
        print(StyleHelper.CENTER(
                  'will be added to a leaderboard.'
            )
        )
        time.sleep(0.05)
        print()
        input(f'{StyleHelper.CENTER("Click ENTER to continue.")}\n')

        ProgramHelper.remove()
        print(
            f'{StyleHelper.MAGENTA_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.THIN_LINE_STYLE}'
        )
        print()
        print(
            f'{StyleHelper.MAGENTA_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.CENTER(title + " 📃").upper()}'
        )
        print(
            f'{StyleHelper.MAGENTA_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.THIN_LINE_STYLE}'
        )
        print()
        print(
            StyleHelper.CENTER(
                'You will then be asked if you would'
                ' like to play again or quit.'
            )
        )
        time.sleep(0.05)
        print(
            StyleHelper.CENTER(
                ' You will have to type y to play again'
                ' in uppercase or lowercase'
            )
        )
        time.sleep(0.05)
        print(
            StyleHelper.CENTER(' or type n to quit in lowercase or uppercase.')
        )
        time.sleep(0.05)
        print(
            StyleHelper.CENTER(
                'If you type y you will be taken back'
                ' to the difficulty section, '
            )
        )
        time.sleep(0.05)
        print(
            StyleHelper.CENTER(
                'but if you type n you will go through the quitting process.'
            )
        )
        time.sleep(0.05)
        print()
        input(f'{StyleHelper.CENTER("Click ENTER to continue.")}\n')

    def exit_game(self):
        """
        Exits the game after confirmation.
        """
        time.sleep(0.10)
        print(
            f'{StyleHelper.BLACK_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
            f'{StyleHelper.THIN_LINE_STYLE}'
        )
        print(f'\n{StyleHelper.CENTER("Are you sure you want to leave?")}\n')
        time.sleep(0.05)

        exit_selects = input(
            f"{StyleHelper.CENTER('Type Y to leave or N to stay.\n\n')}"
        ).strip().lower()

        exit_selections = ['y', 'n']

        checker = CheckerFactory.get_checker('exit', exit_selections)
        if checker.check(exit_selects, "Invalid exit selection"):
            ProgramHelper.remove()

            if exit_selects == 'y':
                time.sleep(0.10)
                print()

                for i in range(3, 0, -1):
                    print(f"Exiting in {i} seconds...")
                    time.sleep(1)
                    
                ProgramHelper.remove()
                print(f"{StyleHelper.CENTER(
                    'Thank you for playing, goodbye. 👋')}")
                print(
                    f'{StyleHelper.BLACK_FOREGROUND}'
                    f'{StyleHelper.BRIGHT_STYLING}'
                    f'{StyleHelper.THIN_LINE_STYLE}'
                )
                time.sleep(1)
                sys.exit()
            elif exit_selects == 'n':
                time.sleep(0.10)
                print()
                print(
                    f'{StyleHelper.BLACK_FOREGROUND}'
                    f'{StyleHelper.BRIGHT_STYLING}'
                    f'{StyleHelper.THIN_LINE_STYLE}'
                )
                print()
                input(f'{StyleHelper.CENTER(
                      "Click ENTER to return to menu.")}\n')


def main():
    """
    Runs the entire program.
    """
    ui_manager = UIManager()
    # Start the program from the menu
    ui_manager.menu()


if __name__ == '__main__':
    main()
