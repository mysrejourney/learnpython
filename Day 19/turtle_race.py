""" Import the required modules"""
from turtle import Turtle, Screen
import random

""" Create the object for Screen class """
screen = Screen()
""" Set the screen size as 500 x 400 """
screen.setup(width=500, height=400)

is_race_on = False


def user_bet():
    """ Get the user bet - Ask them to enter the turtle color that they think it will win """
    user_color = screen.textinput(title="Make a bet", prompt="Who will win the race? Enter the color: ")
    print(f"user_color is {user_color}")
    return user_color


""" Create colors list for each turtle """
colors = ["violet", "black", "blue", "green", "yellow", "orange", "red"]

""" Turtle size is 40px x 40px. So center of the turtle is 20px. So it should be subtracted from 500/2 """
x = -230

""" Y starting position """
y = 150

""" Create empty list to store all turtles """
all_turtles = []

user_bet = user_bet()


""" Check if the user enter the bet """
if user_bet:
    if user_bet in colors:
        is_race_on = True

        """ Create 7 different color turtles and move them to different starting points """
        for index in range(7):
            new_turtle = Turtle()
            new_turtle.shape("turtle")
            new_turtle.color(colors[index])
            new_turtle.penup()
            new_turtle.goto(x, y)
            y -= 50
            all_turtles.append(new_turtle)
    else:
        print(f"Your bet color is not present. Sorry, you can't continue the game! ")
        screen.title("Your bet color is not present. Sorry, you can't continue the game!")

""" The game is started """
while is_race_on:

    """ Loop through all the turtles and move them some random distance """
    for turtle in all_turtles:
        """ move them some random distance """
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        """ Check if any of the turtle reached the destination which x= 230 """
        if turtle.xcor() > 230:
            """ Get the turtle pencolor who reached the destination """
            winning_color = turtle.pencolor()

            """ Check the winning turtle color against user bet """
            if winning_color == user_bet:
                print(f"You've won!. The {winning_color} color turtle wins the race")
            else:
                print(f"You've lost!. The {winning_color} color turtle wins the race")
            is_race_on = False

screen.exitonclick()