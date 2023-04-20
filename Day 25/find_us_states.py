""" Import the required modules """
from turtle import Turtle, Screen
import pandas

""" Screen object creation """
screen = Screen()

screen.title("Guess the state")  # Set the screen title
""" We can set the image as screen background. To do so, we need to call addshape() method in Screen class """
image = "blank_states_img.gif"
screen.addshape(image)  # adding image as a shape
turtle = Turtle()  # Creating object for Turtle class
turtle.shape(image)  # Adding image as screen background

""" Read csv and store the entire csv in an object """
data = pandas.read_csv("50_states.csv")
""" Convert state column values in to list and store it in a variable """
all_states = data["state"].to_list()
guessed_states = []  # Create an empty list for adding guessed states

""" Check if user guessed all states """
while len(guessed_states) < 50:
    """ Get the user input and convert them into Title case """
    user_state = screen.textinput(title=f"{len(guessed_states)} / {len(all_states)} Guess the state", prompt="What's the state name?").title()

    """ Check if the user input is as Exit, then close the game """
    if user_state == "Exit":
        """ create an empty list for adding the states which are not guessed by user """
        missing_states = []
        for state in all_states:  # Loop through all states
            if state not in guessed_states:  # Compare if the state is in guessed state list
                missing_states.append(state)  # if its not there in guessed state list, add them in missed states
        # print(missing_states)
        df = pandas.DataFrame(missing_states)  # Create a dataframe for missed states
        df.to_csv("states_to_learn.csv")  # Convert the missed states to csv file (1 column table)
        break

    """ if the user state is in all state """
    if user_state in all_states:
        # print(user_state)
        """ Create the turtle and hide, penup"""
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        """ If user state matches the state in CSV, get their x and y coordinates from CSV """
        state_data = data[data["state"] == user_state]
        """ Go to the x, y coordinates """
        turtle.goto(int(state_data.x), int(state_data.y))
        turtle.write(user_state)  # Write the state name
        guessed_states.append(user_state)  # Add the user input into guessed states.


