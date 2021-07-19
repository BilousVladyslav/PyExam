import os
from lib.reader import ExamReader
from lib.examiner import Examiner

PATH = './sources/se_master.json'

reader = ExamReader(PATH)

data = reader.to_dataclasses()

data.questions = data.questions[:3]

examiner = Examiner(data)

examiner.start()
examiner.total()

input('----------------------------------------------\nExam completed')
