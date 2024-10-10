import random
import time
from string import ascii_lowercase
import gspread
from google.oauth2.service_account import Credentials
import datetime
from prettytable import PrettyTable
# Imported from own created files
from questions import EASY_QUESTIONS, MED_QUESTIONS, HARD_QUESTIONS
from helpers import StyleHelper, ProgramHelper
from checks import CheckerFactory


class QuizGame:
    """
    Handles all the game functions.
    """
    def __init__(self):
        self.difficulty = None
        self.num_questions = None
        self.total_score = 0

    def select_difficulty(self):
        """
        Lets user choose the difficulty level.
        """
        while True:
            ProgramHelper.remove()
            print(f'{StyleHelper.GREEN_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
                  f'{StyleHelper.THIN_LINE_STYLE}')
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

            level_selects = input(f'\nWhich option would you like '
                                  f'to select? {StyleHelper.GREEN_FOREGROUND}'
                                  f'{StyleHelper.BRIGHT_STYLING}'
                                  f'[1-3]\n\n').strip()
            level_selections = ['1', '2', '3']

            # Use the checker to validate input
            level_checker = CheckerFactory.get_checker(
                'level', level_selections
            )
            if level_checker.check(level_selects, "Invalid menu selection"):
                #  Sets difficulty based on users choice
                if level_selects == '1':
                    self.difficulty = 'easy'
                    self.questions = EASY_QUESTIONS
                elif level_selects == '2':
                    self.difficulty = 'medium'
                    self.questions = MED_QUESTIONS
                elif level_selects == '3':
                    self.difficulty = 'hard'
                    self.questions = HARD_QUESTIONS

                self.select_question_amount()
                break

    def select_question_amount(self):
        """
        Lets the user select how many questions they want.
        """
        while True:
            ProgramHelper.remove()
            print(f'{StyleHelper.GREEN_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
                  f'{StyleHelper.THIN_LINE_STYLE}')
            print()
            print("How many questions would you like to answer?:\n")
            time.sleep(0.10)
            print('1. 10')
            time.sleep(0.05)
            print('2. 20')
            time.sleep(0.05)
            print('3. 30')
            time.sleep(0.10)

            amount_selects = input(f'\nWhich option would you like '
                                   f'to select? {StyleHelper.GREEN_FOREGROUND}'
                                   f'{StyleHelper.BRIGHT_STYLING}'
                                   f'[1-3]\n\n').strip()
            amount_selections = ['1', '2', '3']

            amount_checker = CheckerFactory.get_checker(
                'amount', amount_selections
            )
            if amount_checker.check(amount_selects, "Invalid menu selection"):
                question_count = {'1': 10, '2': 20, '3': 30}
                self.num_questions = question_count[amount_selects]

                self.play()
                break

    def play(self):
        """
        Main game logic to ask random questions and calculate the score.
        """
        ProgramHelper.remove()
        ProgramHelper.loading_message()
        time.sleep(2)
        ProgramHelper.remove()

        selected_questions = random.sample(self.questions, self.num_questions)
        self.total_score = 0

        for num, qst_data in enumerate(selected_questions):
            question = qst_data['question']
            choices = qst_data['choices']
            answer = qst_data['answer']

            print(f'{StyleHelper.GREEN_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
                  f'{StyleHelper.THIN_LINE_STYLE}')
            print()
            print(f"{StyleHelper.CENTER('Quiz')}")
            print(f'{StyleHelper.GREEN_FOREGROUND}{StyleHelper.BRIGHT_STYLING}'
                  f'{StyleHelper.THIN_LINE_STYLE}')
            print()
            print(f'Q{num + 1}: ')
            self.total_score += self.ask_question(question, choices, answer)
            time.sleep(0.5)
            input(f'{StyleHelper.CENTER("Click Enter to continue")}\n')
            ProgramHelper.remove()

        self.show_score()

    def ask_question(self, question, choices, correct_answer):
        """
        Display the question and check the user's answer.
        """
        sorted_choices = random.sample(choices, len(choices))
        user_answer = self.get_user_answer(question, sorted_choices)

        if user_answer == correct_answer:
            print(f"{StyleHelper.CENTER('✅  Correct! ✅')}")
            print()
            return 1
        else:
            print(f"{StyleHelper.CENTER('❌  Incorrect! ❌')}")
            print()
            return 0

    def get_user_answer(self, question, choices):
        """
        Display choices and get the user's answer.
        """
        print(f"{question}")
        print()
        tag_choice = dict(zip(ascii_lowercase, choices))

        for tag, choice_data in tag_choice.items():
            print(f"{tag}) {choice_data}")

        while True:
            print()
            answer_tag = input('Answer?\t').lower()
            if answer_tag in tag_choice:
                return tag_choice[answer_tag]
            else:
                print(
                    f"{StyleHelper.WHITE_FOREGROUND}{StyleHelper.RED_BG}"
                    f"{StyleHelper.BRIGHT_STYLING}"
                    f"{StyleHelper.CENTER(f'⛔️ Error: {answer_tag} is not'
                                          f' valid. Please answer one of'
                                          f' {', '.join(tag_choice.keys())}'
                                          f'. ⛔️')}"
                )

    def show_score(self):
        """
        Display the score and save it to the leaderboard.
        """
        score_percentage = (self.total_score / self.num_questions) * 100

        if score_percentage <= 25:
            score_message = "Try harder! You can do it!"
        elif score_percentage <= 50:
            score_message = "Nice try! Keep improving!"
        elif score_percentage <= 75:
            score_message = "Well done! You are getting there!"
        else:
            score_message = "Outstanding! Excellent performance!"

        print(
            f"{StyleHelper.GREEN_BG}{StyleHelper.WHITE_FOREGROUND}"
            f"{StyleHelper.BRIGHT_STYLING}"
            f"{StyleHelper.CENTER(f'🎉 '
                                  f"{score_message} "
                                  f"{self.total_score}/"
                                  f'{self.num_questions} 🎉')}"
        )

        time.sleep(0.10)

        user_name = input("Please enter your name: ")
        ProgramHelper.remove()
        ProgramHelper.loading_message()
        time.sleep(2)

        ProgramHelper.remove()
        leaderboard = LeaderboardManager()
        leaderboard.update_leaderboard(
            user_name,
            self.total_score,
            self.difficulty,
            self.num_questions
        )
        print()
        print(f'{StyleHelper.CENTER(
            "Your score has been saved to the leaderboard")}'
        )
        leaderboard.show_leaderboard(self.difficulty)

        # Option to play again or quit
        print()
        leave_selects = input(
            f"{StyleHelper.CENTER(
                'Type Y if you want to play again or type N to quit.\n\n')}"
        ).strip().lower()

        leave_selections = ['y', 'n']

        leave_checker = CheckerFactory.get_checker('exit', leave_selections)
        if leave_checker.check(leave_selects, "Invalid menu selection"):
            ProgramHelper.remove()
            # Goes back to difficulty section
            if leave_selects == 'y':
                self.select_difficulty()
            # Starts the process of exiting the game
            elif leave_selects == 'n':
                ProgramHelper.exit()


class LeaderboardManager:
    """
    Handles the leaderboard functions
    """
    def __init__(self):
        self.sheet = None

    def authenticate(self):
        """
        Authenticates to the Google Sheets API and returns the sheet object.
        """
        SCOPE = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]
        CREDS = Credentials.from_service_account_file('creds.json')
        SCOPED_CREDS = CREDS.with_scopes(SCOPE)
        CLIENT = gspread.authorize(SCOPED_CREDS)
        self.sheet = CLIENT.open('Weather-Wise-Leaderboard')

    def get_worksheet(self, difficulty):
        """
        Returns the correct worksheet based on difficulty.
        """
        if difficulty == 'easy':
            return self.sheet.worksheet('Easy')
        elif difficulty == 'medium':
            return self.sheet.worksheet('Medium')
        elif difficulty == 'hard':
            return self.sheet.worksheet('Hard')

    def update_leaderboard(self, name, score, difficulty, num_questions):
        """
        Updates the leaderboard with the user's name and score.
        """
        self.authenticate()
        worksheet = self.get_worksheet(difficulty)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        worksheet.append_row([name, score, num_questions, timestamp])

    def show_leaderboard(self, difficulty):
        """
        Fetches the leaderboard from Google Sheets
         and displays it using PrettyTable.
        """
        self.authenticate()
        worksheet = self.get_worksheet(difficulty)

        # Get all rows from the sheet
        leaderboard_data = worksheet.get_all_values()

        if not leaderboard_data:
            print("No leaderboard data available.")
            return

        # Create a PrettyTable object and set the column names
        table = PrettyTable()
        table.field_names = ["Name", "Score", "Questions-amount", "Timestamp"]

        # Add each row to the table Skipping header row
        for row in leaderboard_data[1:]:
            table.add_row(row)

        # Print the leaderboard table
        print(f"Leaderboard for {difficulty.capitalize()} difficulty:")
        print(table)
