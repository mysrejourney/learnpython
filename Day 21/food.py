""" Import the required module """
from turtle import Turtle
import random
# TODO 4 - Collision with food
""" Create the food class to place the food for snake in random place """


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")  # Food shape should be circle
        self.penup()
        self.color("blue")
        # Food size should be 10 x 10. By default, it is 20 x 20, so it is reduced as 0.5
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    """ Refresh the food and place it in some place in the screen"""
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
