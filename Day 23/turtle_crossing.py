""" Import the required modules """
from turtle import Screen, Turtle
from my_turtle import Animal
from car_manager import CarManager
from scoreboard import Scoreboard
import time

""" Create screen object """
screen = Screen()
""" Do the screen set up """
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off the tracer
screen.listen()  # Listen to the screen for the key events

""" Create turtle animal object """
animal = Animal()
""" Turtle should move up when you press Up arrow key """
screen.onkey(animal.move_up, "Up")

""" Create objects for Car Manager and Scoreboard """
car_manager = CarManager()
scoreboard = Scoreboard()

is_game_on = True  # To Track if the game is still ON
""" Loop through the game until the stop condition met """
while is_game_on:
    time.sleep(0.1)  # refresh the screen every 0.1 seconds
    screen.update()  # Update the screen, so it can show the objects in the screen
    car_manager.create_car()  # Create the cars
    car_manager.car_move()  # Move the cars from right to left side of the screen

    """ Loop through all the cars appears in the screen and check if turtle is collided with any of the car """
    for car in car_manager.all_cars:
        if car.distance(animal) < 20:  # Check turtle is closed to car
            is_game_on = False  # Stop the game
            scoreboard.game_over()  # Print the message in the screen

    """ If the turtle crossed the finishing line, the level and speed should increase. 
    Also, turtle should go to starting place"""
    if animal.ycor() > 280:  # finishing line coordinate is 280 (Y axis)
        scoreboard.increase_score()  # Level is increasing by 1
        animal.reset()  # Turtle should go to starting place
        car_manager.increase_speed()  # Speed is increasing by 5

screen.exitonclick()