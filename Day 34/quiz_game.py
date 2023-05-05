""" Import Required modules"""
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os
from ui import QuizInterface

# print(question_data)
question_bank = []  # Empty list to store questions

""" Loop through the question data """
for index in range(0, len(question_data)):
    """ Create a tuple with question and correct answer and pass it as an argument to Question class """
    question = Question(question_data[index]["question"], question_data[index]["correct_answer"])
    question_bank.append(question)

# print(question_bank)
""" Initiate an instances for QuizBrain and QuizInterface class"""
quiz = QuizBrain(question_bank)
qz = QuizInterface(quiz)


# for quest in question_data:
#     question_text = quest["question"]
#     question_answer = quest["correct_answer"]
#     question = Question(question_text, question_answer)
#     question_bank.append(question)

# print(question_bank)
count = 1

""" Check if questions are still available """
while quiz.still_has_questions():
    quiz.next_question()

""" Print the score """
# os.system('clear')
# print(f"You have completed the quiz!")
# print(f"Your final score is: {quiz.count}/{quiz.question_number}")

