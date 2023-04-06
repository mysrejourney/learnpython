""" Import the required modules """
from turtle import Turtle

""" Turtle's starting position """
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10  # Move the turtle each time for 10 distance
""" Create a class for Turtle object """


class Animal(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)  # Make the turtle to look towards to top

    """ To move the turtle when up arrow key is pressed """
    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)
        # self.forward(MOVE_DISTANCE)

    """ Reset the turtle original position once its reached the finishing line """
    def reset(self):
        self.goto(STARTING_POSITION)