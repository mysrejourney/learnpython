""" Import the modules """
import turtle
import pandas
""" Do the screen setup """
screen = turtle.Screen()
screen.title("GUESS THE INDIAN STATE")
image = "indian_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("indian_states.csv")
all_states = data["state"].to_list()
# print(all_states)
guessed_states = []

while len(guessed_states) < 50:
    user_input = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} Guess the state", prompt="What is the another state name? ").title()
    if user_input == "Exit":
        missed_states = []
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("missed_indian_states.csv")
        break
    if user_input in all_states:
        guessed_states.append(user_input)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data["state"] == user_input]
        tim.goto(int(state_data.x), int(state_data.y))


