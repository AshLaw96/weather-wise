import os
import sys
import time
from rich.console import Console
from rich.panel import Panel

console = Console()


class StyleHelper:
    """Centralised layout and theme constants for Rich components."""

    # Colours (Rich style tags)
    THEME_PRIMARY = "cyan"
    THEME_SECONDARY = "magenta"
    THEME_SUCCESS = "green"
    THEME_ERROR = "red"
    THEME_WARNING = "yellow"

    @staticmethod
    def center(text: str) -> str:
        """Utility helper to align text centered horizontally."""
        return f"[align=center]{text}[/align]"


class ProgramHelper:
    """General terminal utilities and applicaton helper methods."""

    @staticmethod
    def remove() -> None:
        """Clears the terminal screen cross-platform (Windows / Unix)."""
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def loading_message(description: str = "Loading, please wait...", duration: float = 1.2) -> None:
        """Displays an animated Rich spinner status indicator."""
        with console.status(f"[bold green]{description}[/bold green]", spinner="dots"):
            time.sleep(duration)
