from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("My Ping Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.tracer(0)
screen.listen()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 330 and ball.distance(right_paddle) < 50 or ball.xcor() < -330 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_update_score()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.right_update_score()

screen.exitonclick()
