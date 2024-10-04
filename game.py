import random
import time
from string import ascii_lowercase
import gspread
from google.oauth2.service_account import Credentials
import datetime
# Imported from my own created files
from questions import EASY_QUESTIONS, MED_QUESTIONS, HARD_QUESTIONS
from helpers import (
    remove, exit, THIN_LINE_STYLE, GREEN_BG, GREEN_FOREGROUND, CENTER,
    WHITE_FOREGROUND, BRIGHT_STYLING, loading_message, RED_BG
)
from checks import qst_checker, amount_checker, level_checker


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

        level_selects = input(
            f'\nWhich option would you like to select? '
            f'{GREEN_FOREGROUND}{BRIGHT_STYLING}[1-3]\n\n'
        ).strip()

        level_selections = ['1', '2', '3']

        if level_checker(level_selects, level_selections):

            remove()
            # Choses the easy questions
            if level_selects == '1':
                questions_amount(EASY_QUESTIONS, 'easy')
            # Choses the medium questions
            elif level_selects == '2':
                questions_amount(MED_QUESTIONS, 'medium')
            # Choses the hard questions
            elif level_selects == '3':
                questions_amount(HARD_QUESTIONS, 'hard')
            break


def questions_amount(level, difficulty):
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

        amount_selects = input(
            f'\nWhich option would you like to select? '
            f'{GREEN_FOREGROUND}{BRIGHT_STYLING}[1-3]\n\n'
        ).strip()

        amount_selections = ['1', '2', '3']

        if amount_checker(amount_selects, amount_selections):
            remove()
            # Maps the users choice to the amount of questions
            question_count = {'1': 10, '2': 20, '3': 30}
            # Calls the function with the selected number of questions
            random_questions(level, question_count[amount_selects], difficulty)
            break


def random_questions(question_list, num_questions, difficulty):
    """
    Selects and asks the specified number of random questions
    from the given question list.
    """
    loading_message()
    time.sleep(2)
    remove()
    total = 0

    # Selects the number of questions requested by the user
    selected_questions = random.sample(question_list, num_questions)
    # Loop through the selected questions
    for num, qst_data in enumerate(selected_questions):
        question = qst_data['question']
        choices = qst_data['choices']
        answers = qst_data['answer']

        print()
        print(f'{GREEN_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
        print()
        print(f"{GREEN_FOREGROUND}{CENTER('Quiz')}")
        print(f'{GREEN_FOREGROUND}{BRIGHT_STYLING}{THIN_LINE_STYLE}')
        print()
        print(f'Q{num + 1}: ')

        total += next_qst(question, choices, answers)
        time.sleep(0.5)
        print()

        input(f'{CENTER("Click Enter to continue")}\n')
        remove()

    score_percentage = (total / num_questions) * 100
    # Display message based on user's score
    if score_percentage <= 25:
        score_message = f'{CENTER("Try harder! You can do it!")}'
    elif score_percentage <= 50:
        score_message = f'{CENTER("Nice try! Keep improving!")}'
    elif score_percentage <= 75:
        score_message = f'{CENTER("Well done! You are getting there!")}'
    else:
        score_message = f'{CENTER("Outstanding! Excellent performance!")}'

    print()
    print(
        f"{GREEN_BG}{WHITE_FOREGROUND}{BRIGHT_STYLING}"
        f"{CENTER(f'🎉 {score_message}{total}/{num_questions} 🎉')}"
    )
    time.sleep(0.10)

    user_name = input(f'{CENTER("Please enter your name: ")}')
    remove()

    loading_message()

    # Adds users name and points to leaderboard
    time.sleep(0.30)
    remove()
    update_leaderboard(user_name, total, difficulty, num_questions)
    print(f'{CENTER("Your score has been saved to the leaderboard")}')

    # Option to play again or quit
    print()
    qst_selects = input(
        f"{CENTER('Type Y if you want to play again or type N to quit.\n\n')}"
    ).strip().lower()

    qst_selections = ['y', 'n']

    if qst_checker(qst_selects, qst_selections):
        remove()
        # Goes back to difficulty section
        if qst_selects == 'y':
            level_selector()
        # Starts the process of exiting the game
        elif qst_selects == 'n':
            exit()


def next_qst(qst, choice, right_choice):
    """
    Brings up the next question and checks if the user is correct or incorrect.
    """
    sort_choice = random.sample(choice, len(choice))

    answer = user_answered_select(qst, sort_choice)
    if answer == right_choice:
        print(f"{CENTER('✅ Correct! ✅')}")
        time.sleep(0.05)
        print()
        return 1
    else:
        print(f"{CENTER('❌ Incorrect! ❌')}")
        time.sleep(0.05)
        print()
        return 0


def user_answered_select(qst, choice):
    """
    Shows the question and choices, and gets the user's input.
    """
    print(f"{qst}")
    print()
    tag_choice = dict(zip(ascii_lowercase, choice))

    for tag, choice_data in tag_choice.items():
        print(f"{tag}) {choice_data}")
    # Handles user errors
    while True:
        print()
        answer_tag = input(f"{CENTER('Answer?')}").lower()
        if answer_tag in tag_choice:
            break
        else:
            print()
            print(
                f"{RED_BG}{WHITE_FOREGROUND}{BRIGHT_STYLING}"
                f"⛔️ Error: {answer_tag} is not valid. Please answer one of"
                f" {', '.join(tag_choice.keys())} ⛔️"
            )

    return tag_choice[answer_tag]


def auth_g_sheets(difficulty):
    """
    Sets up the Google Sheets API and returns the correct worksheet
    based on the difficulty level
    """
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    # Authenticates using the creds.json file
    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    # Opens the Google Sheets document
    SHEET = GSPREAD_CLIENT.open('Weather-Wise-Leaderboard')

    # Selects the worksheet based on difficulty level
    if difficulty == 'easy':
        return SHEET.worksheet('Easy')
    elif difficulty == 'medium':
        return SHEET.worksheet('Medium')
    elif difficulty == 'hard':
        return SHEET.worksheet('Hard')


def update_leaderboard(name, score, difficulty, num_questions):
    """
    Updates the leaderboard in Google Sheets with the user's name and score.
    """
    scores_sheet = auth_g_sheets(difficulty)

    # Access the current time
    # {%Y: 2024, %m: 01-12, %d: 01-31, %H: 00-23, %M: 00-59, %S: 00-59}
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Add the new row of data
    scores_sheet.append_row([name, score, num_questions, timestamp])
