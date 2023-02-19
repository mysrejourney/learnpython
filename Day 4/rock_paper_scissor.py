# import random module
import random

# Set the image icon for each caegory
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Save the images in the list
game = [rock, paper, scissors]
# print(game)

# Get the user input and convert them as an integer
user_choice = int(input("What do you choice? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

# Validate if it is invalid user input
if user_choice > 2 or user_choice < 0:
    print("Invalid input. Please correct it")
else:
    # Print user input image
    print("Your choice \n")
    print(game[user_choice])    
    
    # Generate computer choice as a random number
    computer_choice = random.randint(0,2)
    # Print computer input image
    print("computer choice \n")
    print(game[computer_choice])

    # Validate the game rules
    if user_choice == 1 and computer_choice == 2:
        print("Computer wins !!")
    elif user_choice == 1 and computer_choice == 0:
        print("You  win !!")
    elif user_choice == 0 and computer_choice == 1:
        print("Computer win !!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win !!")
    else:
        print("Match tie")


