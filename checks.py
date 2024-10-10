import time


class SelectionChecker:
    """
    Check user input and display errors if input is invalid.
    """
    def __init__(self, selections):
        self.selections = selections

    def check(self, user_selects, error_message):
        """
        Check if the user's selection is valid. If not, show an error message.
        """
        from helpers import StyleHelper, ProgramHelper
        if user_selects not in self.selections:
            ProgramHelper.remove()  # Clear the terminal
            print(f"{StyleHelper.RED_BG}{StyleHelper.WHITE_FOREGROUND}{StyleHelper.BRIGHT_STYLING}"
            f"{StyleHelper.CENTER(f'⛔️ Error: {user_selects} is not valid! Please select {self.selections}. ⛔️')}{StyleHelper.BRIGHT_STYLING}")

            time.sleep(0.05)
            print()
            input(f'{StyleHelper.CENTER("Click ENTER to continue")}\n')
            ProgramHelper.remove()
            return False
        return True


class CheckerFactory:
    """
    Provides different types of selection checkers based on input.
    """
    @staticmethod
    def get_checker(type_of_check, selections):
        """
        Return the appropriate checker based on the type of check requested.
        """
        if type_of_check == 'exit':
            return SelectionChecker(selections)
        elif type_of_check == 'level':
            return SelectionChecker(selections)
        elif type_of_check == 'amount':
            return SelectionChecker(selections)
        elif type_of_check == 'question':
            return SelectionChecker(selections)
        elif type_of_check == 'menu':
            return SelectionChecker(selections)
        else:
            raise ValueError(f"Unknown checker type: {type_of_check}")
