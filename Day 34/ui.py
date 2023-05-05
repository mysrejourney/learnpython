""" Import Required Modules """
from tkinter import *
from quiz_brain import QuizBrain

# Background color
THEME_COLOR = "#375362"


class QuizInterface:  # Create a class for UI
    def __init__(self, quiz_brain: QuizBrain):  # Get QuizBrain class as an argument to access its method
        self.quiz = quiz_brain  # Create an instance of QuizBrain class to access its methods and variables

        """ Window setup """
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.count = self.quiz.count

        """ Score label setup """
        self.score_label = Label(text=f"Score: {self.count}", highlightthickness=0, fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        """ Canvas setup """
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, text=f"Some questions will come", fill=THEME_COLOR,
                                                font=("Arial", 20, "normal"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        """ Right and Wrong button setup """
        tick_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=tick_image, highlightthickness=0, command=self.true_method)
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.false_method)
        self.true_button.grid(column=0, row=2)
        self.wrong_button.grid(column=1, row=2)

        """ Calling the Method to get the next question """
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):  # Method to get the next question
        self.canvas.config(bg="white")  # Set the background color as white
        if self.quiz.still_has_questions():  # Until the next question is available in the question data
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
        else:  # If no more questions, then it should display the below message with score
            self.canvas.itemconfig(self.question, text=f"No more questions, Quiz over\n Your score is: {self.count}/{len(self.quiz.question_list)}")
            """ Right and wrong button needs to be disabled """
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_method(self):  # Method to check if the answer is true
        self.give_feedback(self.quiz.check_answer("True"))

    def false_method(self):  # Method to check if the answer is false
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    """ Check if the answer is True, change the background color as green and increase the score by 1 """
    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
            self.count += 1
            self.score_label.config(text=f"Score: {self.count}")
        else:
            """ Check if the answer is False, change the background color as red """
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)  # Wait for a second and call get_next_question method
