from turtle import Turtle, Screen, colormode
import random

screen = Screen()
timmy = Turtle()
colormode(255)
# timmy_the_turtle.shape("turtle")
# timmy.color("red")

""" Draw the square """
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)


""" Draw the dashed line """
# for _ in range(15):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)



def random_color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    return (R,G,B)

""" Draw the square to octagon shape """
# colour = ["red", "blue", "black", "green", "brown", "violet", "yellow"]
# angle = [0, 90, 180, 270]
# for page in range(3,11):
#     number_of_lines = int(360 / page)
#     timmy.color(random.choice(colour))
#     for _ in range(page):
#         timmy.forward(100)
#         timmy.right(number_of_lines)

""" Draw the random walk """
# timmy.width(15)
# timmy.speed(10)

# for _ in range(200):
#     # timmy.color(random.choice(colour))
#     timmy.color(random_color())
#     timmy.setheading(random.choice(angle))
#     timmy.forward(50)

timmy.speed("fastest")
degree_to_tilt = 10
""" Draw a spirograph"""
for _ in range(int(360 / degree_to_tilt)):
    # timmy.color(random.choice(colour))
    timmy.color(random_color())
    timmy.setheading(timmy.heading() + degree_to_tilt)
    timmy.circle(100)

screen.exitonclick()