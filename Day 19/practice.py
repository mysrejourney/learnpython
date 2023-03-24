""" Import the required modules"""
from turtle import Turtle, Screen, colormode
import random

""" Create the object for Screen class """
screen = Screen()
""" Set the screen size as 500 x 400 """
screen.setup(width=500, height=400)
new_turtle = Turtle()
new_turtle.shape("turtle")
new_turtle.color("red")
new_turtle.goto(-230, 0)
new_turtle.goto(-230, 50)
new_turtle.goto(-230, 150)
new_turtle.goto(-230, -50)
new_turtle.goto(-230, -150)
new_turtle.goto(-150, 50)
print(new_turtle.xcor())

print(-250 < -230)

screen.exitonclick()