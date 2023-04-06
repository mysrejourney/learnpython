""" Import the required modules """
from turtle import Turtle

FONT = ("Arial", 30, "normal")
ALIGNMENT="left"
""" Create a class for scoreboard """

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1  # To track the level
        self.show_score()

    """ Just to show the game level """
    def show_score(self):
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    """ Increase the level """
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    """ Game over message """
    def game_over(self):
        self.goto(-100, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
