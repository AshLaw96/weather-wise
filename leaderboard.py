import json
import os
from datetime import datetime

import gspread
from google.oauth2.service_account import Credentials
from rich.console import Console
from rich.table import Table

from config import CREDS_FILE, GOOGLE_SCOPES, LEADERBOARD_SIZE, SPREADSHEET_NAME
from models import Difficulty

console = Console()


class LeaderboardStore:
    """
    Handles Google Sheets API I/O, with one worksheet tab per
    difficulty.
    """

    def __init__(self):
        self.client = None
        self.sheet = None

    def connect(self) -> bool:
        """
        Authenticates with Google Sheets via env variable or
        local credentials file.
        """
        if self.sheet is not None:
            return True

        try:
            if "CREDS" in os.environ:
                creds_dict = json.loads(os.environ["CREDS"])
                creds = Credentials.from_service_account_info(
                    creds_dict, scopes=GOOGLE_SCOPES
                )
            else:
                base_dir = os.path.dirname(os.path.abspath(__file__))
                creds_path = os.path.join(base_dir, CREDS_FILE)
                creds = Credentials.from_service_account_file(
                    creds_path, scopes=GOOGLE_SCOPES
                )

            self.client = gspread.authorize(creds)
            self.spreadsheet = self.client.open(SPREADSHEET_NAME)
            return True
        except Exception as e:
            console.print(f"[bold red]Error connecting to Google Sheets: {e}[/bold red]")
            return False

    def _worksheet(self, difficulty: Difficulty):
        """
        Fetches the tab matching the difficulty (e.g. 'Easy'), 
        failling back to the first sheet if that tab doesn't
        exist yet.
        """
        tab_name = difficulty.value.capitalize()
        try:
            return self.spreadsheet.worksheet(tab_name)
        except gspread.exceptions.WorksheetNotFound:
            return self.spreadsheet.sheet1

    def fetch_scores(self, difficulty: Difficulty) -> list[dict]:
        """
        Fetches all leaderboard records for one difficulty's 
        worksheet.
        """
        if not self.connect():
            return []
        try:
            worksheet = self._worksheet(difficulty)
            return worksheet.get_all_records()
        except Exception:
            return []

    def add_score(self, name: str, score: int, difficulty: Difficulty, num_questions: int) -> bool:
        """
        Adds a new score record to that difficulty's worksheet.
        """
        if not self.connect():
            return False
        try:
            worksheet = self._worksheet(difficulty)
            date_str = datetime.now().strftime("%Y-%m-%d")
            worksheet.append_row([name, score, num_questions, date_str])
            return True
        except Exception as e:
            console.print(f"[bold red]Error saving score:[/bold red] {e}")
            return False


class LeaderboardDisplay:
    """Handles Rich terminal formatting and display."""

    @staticmethod
    def render(scores: list[dict], difficulty: Difficulty) -> None:
        if not scores:
            console.print(
                "[dim white]No leaderboard records available for"
                "this difficulty yet.[/dim white]\n"
            )
            return

        table = Table(
            title=f"🏆 Top {LEADERBOARD_SIZE} Leaderboard - {difficulty.value.capitalize()} Mode",
            header_style="bold cyan",
            border_style="blue",
            expand=True,
        )
        table.add_column(
            "Rank", justify="center", style="dim", width=6
        )
        table.add_column("Player", style="bold white")
        table.add_column("Score", justify="center", style="bold yellow")
        table.add_column("Questions", justify="center", style="dim white")
        table.add_column("Date", justify="right", style="dim cyan")

        def parse_score(record: dict) -> int:
            val = record.get("Score", record.get("score", 0))
            try:
                return int(val)
            except (ValueError, TypeError):
                return 0

        sorted_scores = sorted(
            scores, key=parse_score, reverse=True
        )

        for rank, row in enumerate(sorted_scores[:LEADERBOARD_SIZE], start=1):
            medal = "🥇 " if rank == 1 else "🥈 " if rank == 2 else "🥉 " if rank == 3 else f"{rank}. "
            player = str(row.get("Player", row.get("name", "Anonymous")))
            score_val = str(row.get("Score", row.get("score", 0)))
            questions_val = str(row.get("Questions", row.get("questions", 0)))
            date_val = str(row.get("Date", row.get("date", "")))

            table.add_row(medal, player, score_val, questions_val, date_val)

        console.print(table)
        console.print()
