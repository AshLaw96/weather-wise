import sys
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.align import Align

from checks import CheckerFactory
from game import QuizGame
from helpers import ProgramHelper

console = Console()


class UIManager:
    """
    Handles terminal interface rendering and main navigation.
    """
    def render_header(self, title: str) -> None:
        """Renders a styled header panel using Rich."""
        header_text = Text()
        header_text.append(f"⛅ {title.upper()} 🌧️\n", style="bold cyan")
        header_text.append(
            "Welcome to Weather Wise - test your knowledge on storms, "
            "climate patterns and forecasting!",
            style="dim white"
        )

        panel = Panel(
            Align.center(header_text),
            border_style="bold blue",
            padding=(1, 2),
        )
        console.print(panel)

    def menu(self) -> None:
        """Displays the interactive manin menu."""
        while True:
            ProgramHelper.remove()
            self.render_header('Weather Wise')
            console.print()

            menu_text = Text()
            menu_text.append("1. ", style="bold bright_blue")
            menu_text.append("Show Rules\n", style="white")
            menu_text.append("2. ", style="bold bright_blue")
            menu_text.append("Play Game\n", style="white")
            menu_text.append("3. ", style="bold bright_blue")
            menu_text.append("Exit Program\n", style="white")

            console.print(
                Panel(
                    menu_text,
                    title="[bold yellow]Main Menu[/bold yellow]",
                    border_style="blue",
                    expand=False,
                )
            )
            console.print()

            user_selects = Prompt.ask(
                "[bold bright_blue]Select an option[/bold bright_blue]",
                choices=["1", "2", "3"],
                default="2",
            )

            checker = CheckerFactory.get_checker('menu', ["1", "2", "3"])
            if checker.check(user_selects, "Invalid menu selection"):
                ProgramHelper.remove()
                if user_selects == '1':
                    self.rules('Rules & Instructions')
                elif user_selects == '2':
                    quiz = QuizGame()
                    quiz.select_difficulty()
                elif user_selects == '3':
                    self.exit_game()

    def rules(self, title: str) -> None:
        """Displays paginated game instructions inside styled panels."""
        pages = [
            (
                "Difficulty Selection",
                ". When starting the game, choose your difficulty level:\n"
                " [bold cyan]1[/bold cyan] - Easy\n"
                " [bold cyan]2[/bold cyan] - Medium\n"
                " [bold cyan]3[/bold cyan] - Hard",
            ),
            (
                "Question Count",
                ". Next, select how many questions you want to answer:\n"
                " [bold cyan]1[/bold cyan] - 10 questions\n"
                " [bold cyan]2[/bold cyan] - 20 questions\n"
                " [bold cyan]3[/bold cyan] - 30 questions",
            ),
            (
                "Answering Questions",
                ". Choose your answers using [bold green]A, B, C, or D[/bold green] "
                "(case-insensitive).\n"
                ". Take your time-accuracy matters for your final score!",
            ),
            (
                "Leaderboard & Results",
                ". After finishing, view your final score and performance summary.\n"
                ". Enter your name to save your score, difficulty and timestamp to the global leaderboard!",
            ),
        ]

        for i, (page_title, content) in enumerate(pages, 1):
            ProgramHelper.remove()
            console.print(
                Panel(
                    f"[white]{content}[/white]",
                    title=f"[bold magenta]📃 {title.upper()} ({i}/{len(pages)}): {page_title}[/bold magenta]",
                    border_style="magenta",
                    padding=(1, 2),
                )
            )
            console.print()
            Prompt.ask(
                "[dim]Press [bold white]ENTER[/bold white] to continue[/dim]",
                default="",
            )

    def exit_game(self) -> None:
        """Handles exit confirmation and graceful shutdown animation."""
        console.print()
        confirm = Prompt.ask(
            "[bold yellow]Are you sure you want to exit?[/bold yellow]",
            choices=["y", "n"],
            default="n",
        ) 

        checker = CheckerFactory.get_checker('exit', ["y", "n"])
        if checker.check(confirm, "Invalid exit selection"):
            ProgramHelper.remove()
            if confirm.lower() == "y":
                console.print()
                for i in range(3, 0, -1):
                    console.print(f"[dim]Exiting in {i} seconds...[/dim]")
                    time.sleep(0.6)

                ProgramHelper.remove()
                console.print(
                    Panel(
                        Align.center(
                            "[bold cyan]Thank you for playing Weather Wise! Goodbye 👋[/bold cyan]"
                        ),
                        border_style="bright_black",
                    )
                )
                time.sleep(1)
                sys.exit()
            else:
                Prompt.ask("[dim]Press [bold white]ENTER[/bold white] to return to main menu[/dim]", default="")


def main():
    ui_manager = UIManager()
    try:
        # Start the program from the menu
        ui_manager.menu()
    except KeyboardInterrupt:
        console.print()
        console.print(
            Panel(
                Align.center("[bold cyan]Thanks for playing Weather Wise! Goodbye 👋[/bold cyan]"),
                border_style="bright_black",
            )
        )
        sys.exit()


if __name__ == '__main__':
    main()
