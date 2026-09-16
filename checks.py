from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from helpers import ProgramHelper

console = Console()


class SelectionChecker:
    """
    Validates user terminal choices and renders styled error
    panels.
    """

    def __init__(self, selections: list[str]):
        self.selections = selections
        self.lower_selections = [str(s).strip().lower() for s in selections]

    def check(self, user_selects: str) -> bool:
        clean_input = str(user_selects).strip().lower()

        if clean_input not in self.lower_selections:
            ProgramHelper.remove()
            allowed_str = ", ".join([f"'{s}'" for s in self.selections])
            console.print(
                Panel(
                    f"[bold red]⛔ Error: '{user_selects}' is not valid!"
                    f"[/bold red]\n"
                    f"[dim white]Please select one of: "
                    f"[bold yellow]{allowed_str}[/bold yellow][/dim white]",
                    title="[bold red]Input Error[/bold red]",
                    border_style="red",
                    expand=False,
                )
            )
            console.print()
            Prompt.ask(
                "[dim]Press [bold white]ENTER[/bold white] to continue[/dim]",
                default=""
            )
            ProgramHelper.remove()
            return False
        return True


class CheckerFactory:
    """
    Instantiates validation checkers based on input category.
    """

    @staticmethod
    def get_checker(
        type_of_check: str, selections: list[str]
    ) -> SelectionChecker:
        valid_types = {"exit", "level", "amount", "question", "menu"}
        if type_of_check in valid_types:
            return SelectionChecker(selections)
        raise ValueError(f"Unknown checker type: {type_of_check}")
