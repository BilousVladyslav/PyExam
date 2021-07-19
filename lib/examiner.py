import random
from datetime import datetime
from .models import SimpleExam, Question, Answer


class Examiner:
    data: SimpleExam
    score: int = 0
    wrong_questions: list[dict] = list()

    def __init__(self, exam_data: SimpleExam):
        self.data = exam_data
        random.shuffle(self.data.questions)
        for i in range(len(self.data.questions)):
            random.shuffle(self.data.questions[i].answers)

    def print_question(self, question: Question, number: int):
        print(f'{number}. {question.message}', end='\n\n')
        for index, answer in enumerate(question.answers):
            print(f'    {index + 1}).  {answer.message}')
        print()

    def total(self):
        print(f'\n----------------------------\n {self.score}/{len(self.data.questions)}')
        if self.score == self.data.questions:
            print('Congratulations, all tests are correct!')
        else:
            print('You have wrong answers:', end='\n\n')
            for item in self.wrong_questions:
                print(item['question'].message)
                print(f'    Correct: {item["correct"].message}')
                print(f'    Your: {item["answered"].message}', end='\n\n')

    def start(self):
        start_date = datetime.now()
        print(f'Start date: {start_date.strftime("%Y-%m-%d %H:%M:%S")}')
        print(
            f'{self.data.name} started. {len(self.data.questions)} questions. Good luck!',
            end='\n\n---------------------------------------------\n\n'
        )
        for index, question in enumerate(self.data.questions):
            self.print_question(question, index + 1)
            answer_number = 0
            while answer_number not in [str(number) for number in range(1, len(question.answers) + 1)]:
                answer_number = input('Enter your answer number: ')
            if question.answers[int(answer_number) - 1].is_correct:
                self.score += 1
                print('Correct!')
            else:
                wrong_question = {
                    'question': question,
                    'answered': question.answers[int(answer_number) - 1],
                }
                for answer in question.answers:
                    if answer.is_correct:
                        wrong_question['correct'] = answer
                        break
                self.wrong_questions.append(wrong_question)
                print('Wrong.')
        print(f'Exam duration: {str(datetime.now() - start_date)[:-7]}')
