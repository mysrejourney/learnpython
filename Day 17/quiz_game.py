from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os

# print(question_data)
question_bank = []

for index in range(0, len(question_data)):
    question = Question(question_data[index]["text"], question_data[index]["answer"])
    question_bank.append(question)

# print(question_bank)
count = 1
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

os.system('clear')
print(f"You have completed the quiz!")
print(f"Your final score is: {quiz.count}/{quiz.question_number}")

