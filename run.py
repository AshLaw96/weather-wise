# Imported from my own created files
from helpers import header, remove, rules, checker
from questions import EASY_QUESTIONS, MED_QUESTIONS, HARD_QUESTIONS

def menu():
    """
    Shows the main menu of the program.
    """
    remove()
    header('weather wise', 'Welcome to an engaging quiz game that tests your knowledge about various weather phenomena, including types of storms, climate patterns, and weather forecasting!')

tests = menu()

print(tests)