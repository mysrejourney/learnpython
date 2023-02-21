import random
from hangman_word import word_list
from hangman_art import stages, logo

print(f"{logo}")
# Step 1 - Create a word list
# word_list = ["Satheesh", "Pandian", "Adhira"]
# Step 2 - Randomly choose any word from word list
random_word = random.choice(word_list).lower()
# Step 3 - Print the randomly chosen word
# print(f"Given word: {random_word}")

display = []
for _ in random_word:
    # chosen_word.append("_")
    display += '_'
print(f"Word in blanks: {display}")

repeated_letter = []
wrong_attempt = 6
game_over = False
while not game_over:
    # Step 4 - Ask user input to guess a letter
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter not in repeated_letter:
        # Step 6 - Check the guessed letter presents in the randomly chosen word
        for position in range(len(random_word)):
            char = random_word[position]
            if char == guess_letter:
                display[position] = char

        if guess_letter not in random_word:
            print(f" Your guessed letter : {guess_letter} is not in the word")
            wrong_attempt -= 1
            print(stages[wrong_attempt])

        repeated_letter.append(guess_letter)
        print(f" repeated_letter : {repeated_letter}.")

        # if display.count('_') <= 0:
        if "_" not in display:
            game_over = True
            print("You Win!!!")
        elif wrong_attempt == 0:
            game_over = True
            print("You Lost!!!")
            print(f"The actual word is {random_word}")

        print(f"{' '.join(display)}")
    else:
        print(f" Your already guessed letter : {guess_letter}. Please guess another one")