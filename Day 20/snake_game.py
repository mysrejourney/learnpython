""" Import the required modules """
from turtle import Screen
from snake import Snake
import time

# TODO 1 - Do the screen setup
""" Screen setup """
screen = Screen()
screen.setup(width=600, height=600)
""" Screen background color is black """
screen.bgcolor("black")
""" Screen title needs to be some string """
screen.title(titlestring="My Snake Game")

""" Tracer method is mandatory to hide the graphics until its updated """
screen.tracer(0)

""" Create the snake object """
snake = Snake()

""" Create listen method, so key inputs will work """
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


is_game_on = True
while is_game_on:
    screen.update()  # As tracer is on, nothing will be shown until it calls update() method.
    time.sleep(0.1)  # Make the snake move fast
    snake.move()

screen.exitonclick()
