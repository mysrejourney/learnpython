""" Import the required modules """
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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

""" Create the snake object, food object and scoreboard object """
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    """ if the snake eats the food, do the following """
    if snake.head.distance(food) < 15:  # distance method is used to find the distance between snake's head and food
        food.refresh()  # Place the food at random place
        scoreboard.calc_score()  # Increase the score
        snake.extend_snake()  # Extend the snake's tail

    # TODO 6 - Collision with wall
    """ if the snake hits the wall, do the following """
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()  # stop the game
        snake.reset()

    # for segments in snake.segments:
    #     if segments == snake.head:
    #         pass
    #     elif snake.head.distance(segments) < 10:
    #         is_game_on = False
    #         scoreboard.game_over()
    # TODO 7 - Collision with tail
    """ If the snake hits it's wall, then do the following """
    for segments in snake.segments[1:-1]:  # Snake's head is not considered. Because distance method is calculated from head's position
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
