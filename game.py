import random 
from string import ascii_lowercase

from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

from checks import CheckerFactory
from config import SCORE_BANDS
from helpers import ProgramHelper
from leaderboard import LeaderboardDisplay, LeaderboardStore
from models import Difficulty, Question
from questions import EASY_QUESTIONS, MED_QUESTIONS, HARD_QUESTIONS

console = Console()


class QuizGame:
    """
    Manages game state, iteration loops, questions and score
    reporting.
    """

    def __init__(self):
        self.difficulty = Difficulty.EASY
        self.num_questions = 10
        self.total_score = 0
        self.question_pool = {
            Difficulty.EASY: [Question.from_dict(q, Difficulty.EASY) for q in EASY_QUESTIONS],
            Difficulty.MEDIUM: [Question.from_dict(q, Difficulty.MEDIUM) for q in MED_QUESTIONS],
            Difficulty.HARD: [Question.from_dict(q, Difficulty.HARD) for q in HARD_QUESTIONS],
        }

    def start(self) -> None:
        """
        Executes game lifecycle without stack recursion.
        """
        while True:
            if not self.select_difficulty():
                continue
            if not self.select_question_amount():
                continue
            
            self.play()
            
            if not self.ask_play_again():
                break

    def select_difficulty(self) -> bool:
        ProgramHelper.remove()

        content = Text()
        content.append(
            "Choose your difficulty level:\n\n", style="bold white"
        )
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
            default="1"
        )
        checker = CheckerFactory.get_checker(
            'level', ["1", "2", "3"]
        )

        if checker.check(level_selects):
            self.difficulty = Difficulty.from_str(level_selects)
            return True
        return False

    def select_question_amount(self) -> bool:
        ProgramHelper.remove()

        content = Text()
        content.append(
            "How many questions would you like to answer?\n\n",
            style="bold white"
        )
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
            default="1"
        )
        checker = CheckerFactory.get_checker(
            'amount', ["1", "2", "3"]
        )

        if checker.check(amount_selects):
            count_map = {'1': 10, '2': 20, '3': 30}
            self.num_questions = count_map[amount_selects]
            return True
        return False

    def play(self) -> None:
        ProgramHelper.remove()
        ProgramHelper.loading_message(
            "Preparing your weather quiz...", duration=1.0
        )
        ProgramHelper.remove()

        available_questions = self.question_pool[self.difficulty]
        sample_size = min(self.num_questions, len(available_questions))
        selected_questions = random.sample(available_questions, sample_size)
        self.total_score = 0

        for num, qst_obj in enumerate(selected_questions, 1):
            ProgramHelper.remove()
            score_increment = self.ask_question(
                            num, sample_size, qst_obj
                        )
            self.total_score += score_increment

            console.print()
            Prompt.ask(
                "[dim]Press [bold white]ENTER[/bold white] for"
                " next question[/dim]",
                default=""
            )

        self.show_score(sample_size)

    def ask_question(
            self, q_num: int,
            total: int,
            q_obj: Question
    ) -> int:
        sorted_choices = random.sample(q_obj.choices, len(q_obj.choices))
        tag_choice = dict(
            zip(ascii_lowercase[: len(sorted_choices)], sorted_choices)
        )

        q_text = Text()
        q_text.append(f"{q_obj.question}:\n\n", style="bold white")

        for tag, choice_str in tag_choice.items():
            q_text.append(f"  [{tag.upper()}] ", style="bold yellow")
            q_text.append(f"{choice_str}\n", style="bright_white")

        console.print(
            Panel(
                q_text,
                title=f"[bold green]Question {q_num}/{total}[/bold green]"
                f" [dim]({q_obj.difficulty.value.capitalize()})[/dim]",
                subtitle=f"[dim]Current Score: {self.total_score}[/dim]",
                border_style="green",
                padding=(1, 2),
            )
        )
        console.print()

        lower_keys = list(tag_choice.keys())

        while True:
            user_tag = Prompt.ask(
                "[bold yellow]Your Answer[/bold yellow]",
            ).strip().lower()
            if user_tag in lower_keys:
                break
            console.print(
                f"[red]Invalid choice. Please pick ennter a valid option letter.[/red]"
            )

        selected_answer = tag_choice[user_tag]
        console.print()

        if selected_answer.strip().lower() == q_obj.answer.strip().lower():
            console.print(
                Panel(
                    Align.center(
                        f"[bold green]✅ Correct!"
                        f"[/bold green]\n[dim]{q_obj.answer}[/dim]"
                    ),
                    border_style="green",
                )
            )
            return 1
        else:
            console.print(
                Panel(
                    Align.center(
                        f"[bold red]❌ Incorrect![/bold red]\n"
                        f"[white]Your answer: [strike]{selected_answer}"
                        f"[/strike][/white]\n"
                        f"[bold green]Correct answer: {q_obj.answer}"
                        f"[/bold green]"
                    ),
                    border_style="red",
                )
            )
            return 0

    def show_score(self, total_asked: int) -> None:
        ProgramHelper.remove()
        score_pct = (self.total_score / total_asked) * 100 if total_asked > 0 else 0

        eval_msg = SCORE_BANDS[-1]["msg"]
        eval_color = SCORE_BANDS[-1]["color"]

        for band in SCORE_BANDS:
            if score_pct >= band["min_pct"]:
                eval_msg = band["msg"]
                eval_color = band["color"]
                break

        score_box = Text()
        score_box.append(f"🎉 {eval_msg}\n\n", style=f"bold {eval_color}")
        score_box.append("Final Score: ", style="white")
        score_box.append(
            f"{self.total_score} / {total_asked}", style="bold yellow"
        )
        score_box.append(f" ({score_pct:.0f}%)", style="dim white")

        console.print(
            Panel(
                Align.center(score_box),
                title="[bold yellow]🏆 Quiz Results[/bold yellow]",
                border_style=eval_color,
                padding=(1, 2),
            )
        )
        console.print()

        user_name = Prompt.ask(
            "[bold cyan]Enter your name for the leaderboard[/bold cyan]"
        ).strip()
        user_name = "".join(
            ch for ch in user_name if ch.isprintable()
        )[:20].strip() or "Anonymous"

        ProgramHelper.loading_message(
            "Saving score to global leaderboard...",
            duration=1.0
        )

        store = LeaderboardStore()
        if store.add_score(user_name, self.total_score, self.difficulty, total_asked):
            console.print("[bold green]✓ Score successfully saved![/bold green]\n")

        scores = store.fetch_scores(self.difficulty)
        LeaderboardDisplay.render(scores, self.difficulty)

    def ask_play_again(self) -> bool:
        while True:
            again = Prompt.ask(
                "[bold yellow]Would you like to play again?[/bold yellow]",
                default="y",
            ).strip().lower()

            checker = CheckerFactory.get_checker(
                'exit', ['y', 'n']
            )
            if checker.check(again):
                return again == 'y'
