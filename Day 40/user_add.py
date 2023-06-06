""" Import required modules """
from user_data import UserData
import os


def user_details():
    print(f"Welcome to Sat's flight club. \nWe find the best flight deals for you and email you.")
    first_name = input(f"What is your first name?\n")
    last_name = input(f"What is your last name?\n")
    email = input(f"What is your email?\n")
    confirm_email = input(f"Type your email again.\n")
    return first_name, last_name, email, confirm_email


is_data_updated = True

while is_data_updated:
    os.system('clear')
    f_name, l_name, email1, email2 = user_details()
    if email1 == email2:
        is_data_updated = False
    elif email1.lower() == 'quit' or email2.lower() == 'quit' or email1.lower() == 'exit' or email2.lower() == 'exit':
        exit()
        is_data_updated = False
    else:
        print("Sorry, your emails are not matching😌. Please try again.")
        f_name, l_name, email1, email2 = user_details()


user_data = UserData()
user_data.post_new_data(f_name, l_name, email1)
