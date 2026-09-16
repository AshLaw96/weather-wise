import os

# Quiz Settings
QUESTIONS_PER_GAME = 10
TIME_LIMIT_PER_QUESTION = 15  # seconds

# Leaderboard
LEADERBOARD_SIZE = 10

# Score Evaluation Bands
SCORE_BANDS = [
    {
        "min_pct": 90, "msg": "Outstanding! You are a true Weather Wise Master! 🌩️", "color": "green"
    },
    {
        "min_pct": 75, "msg": "Great job! Your weather knowledge is strong!", "color": "cyan"
    },
    {
        "min_pct": 50, "msg": "Good effort! You've got a baseline understanding.", "color": "yellow"
    },
    {
        "min_pct": 0, "msg": "Keep practicing! Weather forecasting takes time.", "color": "red"
    },
]

# Google Sheets Configuration
SPREADSHEET_NAME = os.getenv("SPREADSHEET_NAME", "Weather-Wise-Leaderboard")
GOOGLE_SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
CREDS_FILE = "creds.json"
