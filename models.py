from dataclasses import dataclass
from enum import Enum


class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

    @classmethod
    def from_str(cls, label: str) -> "Difficulty":
        clean_label = str(label).strip().lower()
        mapping = {"1": cls.EASY, "2": cls.MEDIUM, "3": cls.HARD}
        if clean_label in mapping:
            return mapping[clean_label]

        for member in cls:
            if member.value == clean_label:
                return member
        return cls.EASY  # Default to EASY if no match found


@dataclass
class Question:
    question: str
    choices: list[str]
    answer: str
    difficulty: Difficulty = Difficulty.EASY

    @classmethod
    def from_dict(
        cls, data: dict, difficulty: Difficulty = Difficulty.EASY
    ) -> "Question":
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
            difficulty=difficulty,
        )
