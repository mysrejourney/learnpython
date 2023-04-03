""" Import the required module """
from turtle import Turtle

""" Keep the constant variable """
ALIGNMENT = 'center'  # Align the text in the center position
FONT = ('Arial', 30, 'normal')  # Text format and style for the font

# TODO 5 - Increase the score
""" Create the scoreboard class to track the score. Make sure the class should have all the methods and properties 
of the Turtle class. """


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()  # Hide the turtle
        self.penup()  # Remove the pen
        self.color("white")  # scoreboard color is white, so it is visible in the screen
        self.goto(0, 270)  # Move the score text to the top of the screen
        self.score = 0
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    """ Calculate the score by increasing one when snake eats food """
    def calc_score(self):
        self.score += 1
        self.clear()  # score needs to be clear each time, else it is overlapped
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    """ When the game is ended, the text needs to be shown at the center """
    def game_over(self):
        self.goto(0, 0)  # Go to center position
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
