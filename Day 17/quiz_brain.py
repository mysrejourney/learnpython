class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.count = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_choice = input(f"Q.{self.question_number}: {current_question.text} (True/False)? : ")
        correct_answer = current_question.answer
        self.check_answer(user_choice, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print(f"You got it right!")
            self.count += 1
        else:
            print("Your answer is wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.count}/{self.question_number}")
        print("\n")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)