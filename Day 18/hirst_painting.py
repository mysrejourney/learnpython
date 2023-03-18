
############################################################################
#                               First Way                                  #
############################################################################
# import random
# from turtle import Turtle, Screen, colormode
# color = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46),
#          (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121),
#          (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61)
# ]

# colormode(255)
# """ Create the objects and do screen setup"""
# timmy = Turtle()
# screen = Screen()
# screen.screensize(500, 500)
#
# """ Get the turtle current position """
# # print(timmy.pos())
#
# """ Move the turtle to left bottom corner - starting place of the painting """
# timmy.hideturtle()
# timmy.penup()
# timmy.goto(-400, -375)
#
# is_painting_on = True # To track the game, so we can stop at the right time
# is_add_row = 1 # To track the row number
# while is_painting_on:
#     count = 0
#     for count in range(17):
#         """ Create the dot first"""
#         timmy.dot(20, random.choice(color))
#
#         """ Move forward 50 spaces and do this again"""
#         timmy.forward(50)
#     """ Increase the row to decide whether move to left or right """
#     is_add_row += 1
#     timmy.dot(20, random.choice(color))
#
#     """ Turn 90 degree towards up """
#     timmy.setheading(90)
#
#     """ Move 50 spaces to start the next row dots """
#     timmy.forward(50)
#
#     """ If the turtle is in even number of row, then turn left. Else, turn right. Also check the row number is
#     increased or equal to 17 (because we are creating 17 x 17 painting) """
#     if is_add_row % 2 == 0:
#         timmy.left(90)
#     elif is_add_row >= 17:
#         is_painting_on = False
#     else:
#         timmy.right(90)

############################################################################
#                               Second Way                                 #
############################################################################
from turtle import Turtle, Screen, colormode
import random
color = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46),
         (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121),
         (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61)
]
colormode(255)

timmy = Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(400)
timmy.setheading(360)

number_of_dots = 100 # Total number of dots in the picture

# Loop through till 100 and place the dots
for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color))
    timmy.forward(50)
    # After 10 dots it has to start from left again. So making turtle to come to left side
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(360)


screen = Screen()
screen.exitonclick()

