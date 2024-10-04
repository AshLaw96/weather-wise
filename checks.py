import time


def checker(user_selects, selections):
    """
    Tests whether the user inputted a correct selection, if not shows an error.
    """
    # Imports from own created files
    from helpers import (
        WHITE_FOREGROUND, RED_BG, BRIGHT_STYLING, CENTER, remove
    )

    try:
        if user_selects not in selections:
            raise ValueError
    except ValueError:
        remove()
        print()
        print(
            f"{RED_BG}{WHITE_FOREGROUND}{BRIGHT_STYLING}"
            f"{CENTER(f'⛔️ Error: {user_selects} is not valid! Please select '
                      f"{selections}. ⛔️")}"
        )
        time.sleep(0.05)
        print()

        input(f'{CENTER("Click ENTER to continue")}\n')
        remove()
        return False

    return True


def exit_checker(exit_selects, exit_selections):
    """
    Tests whether the user inputted a correct selection, if not shows an error.
    """
    # Imports from own created files
    from helpers import (
        WHITE_FOREGROUND, RED_BG, BRIGHT_STYLING, CENTER, remove
    )
    from game import exit

    try:
        if exit_selects not in exit_selections:
            raise ValueError
    except ValueError:
        remove()
        print()
        print(
            f"{WHITE_FOREGROUND}{RED_BG}{BRIGHT_STYLING}"
            f"{CENTER(f'⛔️ Error: {exit_selects} is not valid! Please select'
                      f" {exit_selections}. ⛔️")}"
        )
        time.sleep(0.05)
        print()

        input(f'{CENTER("Click ENTER to continue.")}\n')
        remove()
        return False

    return True


def level_checker(level_selects, level_selections):
    """
    Tests whether the user inputted a correct selection, if not shows an error.
    """
    # Imports from own created files
    from helpers import (
        WHITE_FOREGROUND, RED_BG, BRIGHT_STYLING, CENTER, remove
    )
    from game import level_selector

    try:
        if level_selects not in level_selections:
            raise ValueError
    except ValueError:
        remove()
        print()
        print(
            f"{WHITE_FOREGROUND}{RED_BG}{BRIGHT_STYLING}"
            f"{CENTER(f'⛔️ Error: {level_selects} is not valid! Please select'
                      f" {level_selections}. ⛔️")}"
        )
        time.sleep(0.05)
        print()

        input(f'{CENTER("Click ENTER to continue.")}\n')
        remove()
        return False

    return True


def amount_checker(amount_selects, amount_selections):
    """
    Tests whether the user inputted a correct selection, if not shows an error.
    """
    # Imports from own created files
    from helpers import (
        WHITE_FOREGROUND, RED_BG, BRIGHT_STYLING, CENTER, remove
    )
    from game import questions_amount

    try:
        if amount_selects not in amount_selections:
            raise ValueError
    except ValueError:
        remove()
        print()
        print(
            f"{WHITE_FOREGROUND}{RED_BG}{BRIGHT_STYLING}"
            f"{CENTER(f'⛔️ Error: {amount_selects} is not valid! Please select'
                      f" {amount_selections}. ⛔️")}"
        )
        time.sleep(0.05)
        print()

        input(f'{CENTER("Click ENTER to continue.")}\n')
        remove()
        return False

    return True


def qst_checker(qst_selects, qst_selections):
    """
    Tests whether the user inputted a correct selection, if not shows an error.
    """
    # Imports from own created files
    from helpers import (
        WHITE_FOREGROUND, RED_BG, BRIGHT_STYLING, CENTER, remove
    )
    from game import random_questions

    try:
        if qst_selects not in qst_selections:
            raise ValueError
    except ValueError:
        remove()
        print()
        print(
            f"{WHITE_FOREGROUND}{RED_BG}{BRIGHT_STYLING}"
            f"{CENTER(f'⛔️ Error: {qst_selects} is not valid! Please select'
                      f" {qst_selections}. ⛔️")}"
        )
        time.sleep(0.05)
        print()

        input(f'{CENTER("Click ENTER to continue.")}\n')
        remove()
        return False

    return True
