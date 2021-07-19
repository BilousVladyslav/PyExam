import os
import json
from .models import Question, Answer, SimpleExam


class ExamReader:
    path: str

    def __init__(self, path: str):
        self.path = path

    def read_json(self) -> dict:
        with open(self.path, 'rb') as file:
            return json.load(file)

    def to_dataclasses(self) -> SimpleExam:
        base_json = self.read_json()
        exam = SimpleExam(name=base_json['name'], questions=[])
        for question_json in base_json['questions']:
            question = Question(message=question_json['message'], answers=[])

            for answer_json in question_json['answers']:
                question.answers.append(Answer(**answer_json))

            exam.questions.append(question)

        return exam
