from dataclasses import dataclass


@dataclass
class Answer:
    message: str
    is_correct: bool = False


@dataclass
class Question:
    message: str
    answers: list[Answer]


@dataclass
class SimpleExam:
    name: str
    questions: list[Question]
