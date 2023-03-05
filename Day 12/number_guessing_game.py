from random import randint

""" Get the user input for level """
EASY_ATTEMPT = 10
HARD_ATTEMPT = 5


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_ATTEMPT
    else:
        return HARD_ATTEMPT


def compare(guess_number, random_number, attempt):
    if guess_number == random_number:
        print("Bulls eye")
    elif guess_number > random_number:
        print("Too high")
        print("Guess again")
        return attempt - 1
    else:
        print("Too low")
        print("Guess again")
        return attempt - 1


print("Welcome to the number guessing game")
print("I am thinking a number between 1 to 100")

random_number = randint(1, 101)
attempt = set_difficulty()
print(f"You have {attempt} attempts to guess the number")

guess_number = 0
while guess_number != random_number and attempt != 0:
    guess_number = int(input("Guess the number: "))
    attempt = compare(guess_number, random_number, attempt)
    print(f"You have {attempt} remaining attempts to guess the number")
