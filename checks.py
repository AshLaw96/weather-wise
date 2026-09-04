from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()


class SelectionChecker:
    """Checks user input and displays styled error messages if invalid."""

    def __init__(self, selections: list[str]):
        self.lower_selections = [str(s).strip().lower() for s in selections]

    def check(self, user_selects: str, error_message: str = "Invalid selection") -> bool:
        """Validates if user selection is in the allowed list."""
        clean_input = str(user_selects).strip().lower()

        if clean_input not in self.lower_selections:
            from helpers import ProgramHelper

            ProgramHelper.remove()

            allowed_str = ", ".join([f"'{s}'" for s in self.selections])
            console.print(
                Panel(
                    f"[bold red]⛔ Error: '{user_selects}' is not valid![/bold red]\n"
                    f"[dim white]Please select one of the following: [bold yellow]{allowed_str}[/bold yellow][/dim white]",
                    title="[bold red]Input Error[/bold red]",
                    border_style="red",
                    expand=False,
                )
            )

            console.print()
            Prompt.ask("[dim]Press [bold white]ENTER[/bold white] to continue[/dim]", default="")
            ProgramHelper.remove()
            return False
        return True


class CheckerFactory:
    """Factory to instantiate validation checkers based on check category."""

    @staticmethod
    def get_checker(type_of_check: str, selections: list[str]) -> SelectionChecker:
        valid_types = {"exit", "level", "amount", "question", "menu"}
        if type_of_check in valid_types:
            return SelectionChecker(selections)
        raise ValueError(f"Unknown checker type: {type_of_check}")
