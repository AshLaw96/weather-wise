import random
from string import ascii_lowercase

import gspread
from google.oauth2.service_account import Credentials
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text

from checks import CheckerFactory
from helpers import ProgramHelper
from questions import EASY_QUESTIONS, MED_QUESTIONS, HARD_QUESTIONS

console = Console()


class QuizGame:
    """Handles core gameplay flow, question loop, scoring and navigation."""

    def __init__(self):
        self.difficulty = None
        self.questions = []
        self.num_questions = 0
        self.total_score = 0

    def select_difficulty(self):
        """Prompts the user to select quiz difficulty level."""
        while True:
            ProgramHelper.remove()

            content = Text()
            content.append("Choose your difficulty level:\n\n", style="bold white")
            content.append("1. ", style="bold green")
            content.append("Easy\n", style="white")
            content.append("2. ", style="bold yellow")
            content.append("Medium\n", style="white")
            content.append("3. ", style="bold red")
            content.append("Hard", style="white")

            console.print(
                Panel(
                    content,
                    title="[bold cyan]🎯 Select Difficulty[/bold cyan]",
                    border_style="cyan",
                    expand=False,
                )
            )
            console.print()

            level_selects = Prompt.ask(
                "[bold cyan]Select difficulty[/bold cyan]",
                choices=["1", "2", "3"],
                default="1"
            )

            # Use the checker to validate input
            checker = CheckerFactory.get_checker(
                'level', ["1", "2", "3"]
            )
            if checker.check(level_selects, "Invalid selection"):
                mapping = {
                    '1': ('easy', EASY_QUESTIONS), 
                    '2': ('medium', MED_QUESTIONS), 
                    '3': ('hard', HARD_QUESTIONS),
                }
                self.difficulty, self.questions = mapping[level_selects]
                self.select_question_amount()
                break

    def select_question_amount(self) -> None:
        """Prompts the user to select question length."""
        while True:
            ProgramHelper.remove()

            content = Text()
            content.append("How many questions would you like to answer?\n\n", style="bold white")
            content.append("1. ", style="bold cyan")
            content.append("10 Questions\n", style="white")
            content.append("2. ", style="bold cyan")
            content.append("20 Questions\n", style="white")
            content.append("3. ", style="bold cyan")
            content.append("30 Questions", style="white")

            console.print(
                Panel(
                    content,
                    title="[bold cyan]❓ Question Count[/bold cyan]",
                    border_style="cyan",
                    expand=False,
                )
            )
            console.print()

            amount_selects = Prompt.ask(
                "[bold cyan]Select amount[/bold cyan]",
                choices=["1", "2", "3"],
                default="1"
            )

            checker = CheckerFactory.get_checker(
                'amount', ["1", "2", "3"]
            )
            if checker.check(amount_selects, "Invalid selection"):
                count_map = {'1': 10, '2': 20, '3': 30}
                self.num_questions = count_map[amount_selects]
                self.play()
                break

    def play(self) -> None:
        """Main quiz execution loop."""
        ProgramHelper.remove()
        ProgramHelper.loading_message("Preparing your weather quiz...", duration=1.0)
        ProgramHelper.remove()

        # Limit sample to available question count if pool is smaller than selection
        sample_size = min(self.num_questions, len(self.questions))
        selected_questions = random.sample(self.questions, sample_size)
        self.total_score = 0

        for num, qst_data in enumerate(selected_questions, 1):
            ProgramHelper.remove()

            question = qst_data['question']
            choices = qst_data['choices']
            answer = qst_data['answer']

            score_increment = self.ask_question(num, sample_size, question, choices, answer)
            self.total_score += score_increment

            console.print()
            Prompt.ask("[dim]Press [bold white]ENTER[/bold white] for next question[/dim]", default="")

        self.show_score()

    def ask_question(self, q_num: int, total: int, question: str, choices: list[str], correct_answer: str) -> int:
        """Renders individual question card and evaluates choice."""
        sorted_choices = random.sample(choices, len(choices))
        tag_choice = dict(zip(ascii_lowercase[: len(sorted_choices)], sorted_choices))

        q_text = Text()
        q_text.append(f"{question}:\n\n", style="bold white")

        for tag, choice_str in tag_choice.items():
            q_text.append(f"  [{tag.upper()}] ", style="bold yellow")
            q_text.append(f"{choice_str}\n", style="bright_white")

        console.print(
            Panel(
                q_text,
                title=f"[bold green]Question {q_num}/{total}[/bold green] [dim]({self.difficulty.capitalize()})[/dim]",
                subtitle=f"[dim]Current Score: {self.total_score}[/dim]",
                border_style="green",
                padding=(1, 2),
            )
        )
        console.print()

        valid_keys = list(tag_choice.keys())
        user_tag = Prompt.ask(
            "[bold yellow]Your Answer[/bold yellow]",
            choices=valid_keys,
            show_choices=False
        ).lower()

        selected_answer = tag_choice[user_tag]
        console.print()

        if selected_answer == correct_answer:
            console.print(
                Panel(
                    Align.center(f"[bold green]✅ Correct! Excellent job.[/bold green]\n[dim]{correct_answer}[/dim]"),
                    border_style="green",
                )
            )
            return 1
        else:
            console.print(
                Panel(
                    Align.center(
                        f"[bold red]❌ Incorrect![/bold red]\n"
                        f"[white]Your answer: [strike]{selected_answer}[/strike][/white]\n"
                        f"[bold green]Correct answer: {correct_answer}[/bold green]"
                    ),
                    border_style="red",
                )
            )
            return 0

    def show_score(self) -> None:
        """Displays final score summary and triggers leaderboard upload."""
        ProgramHelper.remove()
        score_pct = (self.total_score / self.num_questions) * 100

        if score_pct <= 25:
            msg = "Keep practicing! Weather forecasting takes time."
            color = "red"
        elif score_pct <= 50:
            msg = "Good effort! You've got a baseline understanding."
            color = "yellow"
        elif score_pct <= 75:
            msg = "Great job! Your weather knowledge is strong!"
            color = "cyan"
        else:
            msg = "Outstanding! You are a true Weather Wise Master! 🌩️"
            color = "green"

        score_box = Text()
        score_box.append(f"🎉 {msg}\n\n", style=f"bold {color}")
        score_box.append("Final Score: ", style="white")
        score_box.append(f"{self.total_score} / {self.num_questions}", style="bold yellow")
        score_box.append(f" ({score_pct:.0f}%)", style="dim white")

        console.print(
            Panel(
                Align.center(score_box),
                title="[bold yellow]🏆 Quiz Results[/bold yellow]",
                border_style=color,
                padding=(1, 2),
            )
        )
        console.print()

        user_name = Prompt.ask("[bold cyan]Enter your name for the leaderboard[/bold cyan]").strip()
        if not user_name:
            user_name = "Anonymous"

        ProgramHelper.loading_message("Saving score to global leaderboard...", duration=1.2)

        leaderboard = LeaderboardManager()
        leaderboard.update_leaderboard(user_name, self.total_score, self.difficulty, self.num_questions)

        console.print("[bold green]✓ Score successfully saved![/bold green]\n")

        again = Prompt.ask(
            "[bold yellow]Would you like to play again?[/bold yellow]",
            choices=["y", "n"],
            default="y",
        )

        if again.lower() == "y":
            self.select_difficulty()
        else:
            from run import UIManager

            UIManager().exit_game()


class LeaderboardManager:
    """Manages Google Sheets authentication and Rich leaderboard table display."""

    def __init__(self):
        self.sheet = None

    def authenticate(self):
        """
        Authenticates with Google Sheets using local file or
        Heroku CREDS environment variable.
        """
        if self.sheet is not None:
            return

        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]
        try:
            import os
            import json

            if "CREDS" in os.environ:
                creds_dict = json.loads(os.environ.get("CREDS"))
                creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
            else:
                base_dir = os.path.dirname(os.path.abspath(__file__))
                creds_path = os.path.join(base_dir, "creds.json")
                creds = Credentials.from_service_account_file(creds_path, scopes=scopes)

            client = gspread.authorize(creds)
            self.sheet = client.open("Weather-Wise-Leaderboard")
        except Exception as e:
            console.print(f"[bold red]Failed to connect to Google Sheets leaderboard:[/bold red] {e}")

    def get_worksheet(self, difficulty: str):
        """Fetches sheet tab corresponding to difficulty level."""
        sheet_map = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}
        tab_name = sheet_map.get(difficulty.lower(), "Easy")
        return self.sheet.worksheet(tab_name)

    def update_leaderboard(self, name: str, score: int, difficulty: str, num_questions: int) -> None:
        """Appends a new score record row to Google Sheets and displays top 10."""
        try:
            self.authenticate()
            if not self.sheet:
                return

            worksheet = self.get_worksheet(difficulty)

            # 1. Append new score to Google Sheets
            from datetime import datetime
            current_date = datetime.now().strftime("%Y-%m-%d")
            worksheet.append_row([name, score, num_questions, current_date])

            # 2. Fetch updated dataset
            raw_data = worksheet.get_all_values()

            if len(raw_data) <= 1:
                console.print("[dim]No leaderboard records available for this difficulty yet.[/dim]")
                return

            records = raw_data[1:]  # Skip header row
            parsed_records = []

            for row in records:
                try:
                    parsed_records.append([row[0], int(row[1]), row[2], row[3]])
                except (ValueError, IndexError):
                    continue

            parsed_records.sort(key=lambda x: x[1], reverse=True)
            top_10 = parsed_records[:10]

            table = Table(
                title=f"🏆 Top 10 Leaderboard — {difficulty.capitalize()} Mode",
                header_style="bold cyan",
                border_style="blue",
                expand=True,
            )

            table.add_column("Rank", justify="center", style="dim", width=6)
            table.add_column("Player Name", style="bold white")
            table.add_column("Score", justify="center", style="bold yellow")
            table.add_column("Questions", justify="center", style="dim white")
            table.add_column("Date", justify="right", style="dim cyan")

            for rank, row in enumerate(top_10, 1):
                medal = "🥇 " if rank == 1 else "🥈 " if rank == 2 else "🥉 " if rank == 3 else f"{rank}. "
                table.add_row(
                    f"{medal}",
                    row[0],
                    str(row[1]),
                    str(row[2]),
                    row[3],
                )

            console.print(table)

        except Exception as e:
            console.print(f"[bold red]Error rendering leaderboard:[/bold red] {e}")
