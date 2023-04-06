""" Import the required modules """
import random
from turtle import Turtle

# Car colors from the list
COLORS = ['red', 'green', 'orange', 'violet', 'blue', 'yellow', 'pink', 'purple']
MOVE_DISTANCE = 10  # Car moving distance each time

""" Creating class for Car Manager """

class CarManager():
    def __init__(self):
        super().__init__()
        self.all_cars = []  # Create a list to add all the cars
        self.speed = MOVE_DISTANCE  # Track the speed

    """ Creating the car"""
    def create_car(self):
        random_create = random.randint(1, 6)  # Making cars to create little slow 1 in 6 times
        if random_create == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)  # Random starting point for the newly created car
            new_car.goto(250, random_y)
            self.all_cars.append(new_car)  # Add newly created car in to the list

    """ Move all the cars in the list from right to left """
    def car_move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    """ Increase the car speed when the level goes up """
    def increase_speed(self):
        self.speed += 5