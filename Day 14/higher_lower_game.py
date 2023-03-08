""" Importing the required modules """
import random
from os import system
from art import logo, vs
from game_data import data

""" Get the random data from the list """


def get_random_data(data_list):
    get_data = random.choice(data_list)
    name = get_data["name"]
    description = get_data["description"]
    country = get_data["country"]
    follower_count = get_data["follower_count"]
    return name, description, country, follower_count


""" Compare the followers count """


def compare(first_count, second_count):
    if first_count > second_count:
        return 'A'
    else:
        return 'B'


""" To do # 2 - Select any random data from game data """
# Compare A: Dwayne Johnson, a Actor and professional wrestler, from United States
first_celebrity_name, first_celebrity_description, first_celebrity_country, first_celebrity_follower_count = get_random_data(
    data)

""" To do # 4 - Select any random data from game data """
second_celebrity_name, second_celebrity_description, second_celebrity_country, second_celebrity_follower_count = get_random_data(
    data)

# second_celebrity_name, second_celebrity_description, second_celebrity_country, second_celebrity_follower_count = first_celebrity_name, first_celebrity_description, first_celebrity_country, first_celebrity_follower_count

score = 0
is_game_on = True

while is_game_on:

    while first_celebrity_name == second_celebrity_name and first_celebrity_description == second_celebrity_description and first_celebrity_country == second_celebrity_country:
        second_celebrity_name, second_celebrity_description, second_celebrity_country, second_celebrity_follower_count = get_random_data(
            data)

    """ To do # 1 - Display the game logo """
    # Display the game logo
    print(logo)
    if score != 0:
        print(f"You're right!. Your current score {score}")

    print(f"Compare A: {first_celebrity_name}, {first_celebrity_description}, from {first_celebrity_country}")

    """ Todo # 3 - Display the vs logo """
    print(vs)

    print(f"Against B: {second_celebrity_name}, {second_celebrity_description}, from {second_celebrity_country}")

    """ Todo # 5 - Compare the followers count """
    compare_result = compare(first_celebrity_follower_count, second_celebrity_follower_count)

    """ Todo # 6 - Get the user input to check the followers count """
    result = input(f"Who has more followers? Type 'A' or 'B': ")

    """ Todo # 7 - Compare the user input with followers count """
    if result == compare_result:
        # If it is right, increase the score
        score += 1
        first_celebrity_name, first_celebrity_description, first_celebrity_country, first_celebrity_follower_count = second_celebrity_name, second_celebrity_description, second_celebrity_country, second_celebrity_follower_count
        system('clear')
    else:
        """ Todo # 8 - User input is not right, then end the game and display the score """
        print(f"Sorry, that's wrong. Final score: {score}")
        is_game_on = False
