""" Import required module """
import html


class QuizBrain:  # Create a class
    def __init__(self, question_list):
        self.question_number = 0  # To hold the question number
        self.question_list = question_list  # Contains the list of questions
        self.count = 0  # to count the score
        self.current_question = None  # To hold current question and answer

    def next_question(self):  # Method to get the next question
        self.current_question = self.question_list[self.question_number]  # Hold the next question
        self.question_number += 1  # Increase the question number
        self.current_question.text = html.unescape(self.current_question.text)  # Remove the unescaped characters
        # user_choice = input(f"Q.{self.question_number}: {current_question.text} (True/False)? : ")
        # self.check_answer(user_choice)
        return f"Q.{self.question_number}: {self.current_question.text}"  # Return question number and question text

    def check_answer(self, user_answer):  # Check if the answer is right
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():  # If the answer is right, increase the score by 1
            self.count += 1
            return True  # Return True if the answer is right
        else:
            return False  # Return False if the answer is wrong

    def still_has_questions(self):  # Method to check if any more questions are there in the list
        return self.question_number < len(self.question_list)
