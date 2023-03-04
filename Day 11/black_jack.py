from art import logo
import random
from os import system


# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
def deal_card():
    """ Cards list has to be created with the deck of cards number. For Ace, it is 11 """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Pick any random cards from the deck
    random_card = random.choice(cards)
    return random_card


# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

def calculate_score(card_list):
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score.
    # 0 will represent a blackjack in our game.
    """"""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    # Hint 8: Inside calculate_score() check for an 11 (ace).
    # If the score is already over 21, remove the 11 and replace it with a 1.
    # You might need to look up append() and remove().
    if 11 in card_list:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)


def compare_score(user_score, computer_score):
    if user_score == computer_score:
        print(f"Both has same score. Match drawn")
    elif computer_score == 0:
        print(f"Computer has a black jack and you lose.")
    elif user_score == 0:
        print(f"You have a black jack and you won.")
    elif user_score > 21:
        print(f"You went over 21 and you lose.")
    elif computer_score > 21:
        print(f"Computer went over and you won.")
    elif user_score > computer_score:
        print(f"You won.")
    else:
        print(f"Computer won.")


def play_game():
    # Print the blackjack logo
    print(logo)
    # Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    # Create a variable to track the game status
    should_game_continue = True

    """ Deal first two cards for both user and computer """
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    """ Game status is still True and continuing """
    while should_game_continue:
        # User has to draw the new card (after first two cards are done)
        user_score = calculate_score(user_cards)
        # Computer has to draw the new card (after first two cards are done)
        computer_score = calculate_score(computer_cards)
        """ Revealing user cards and score """
        print(f"Your cards {user_cards} and your score {user_score}")
        """Revealing computer's first card """
        print(f"Computer's first card {computer_cards[0]}")

        # Check the user or computer got black jack or user score went over 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            should_game_continue = False
        else:
            """ Ask user to draw another card from the deck """
            another_card_continue = input("Do you want to draw another card? Type 'y' or 'n': ")
            """ If the user draws it, the score needs to be recalculated """
            if another_card_continue == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                """ If the user not drawing it, the game needs to be ended """
                should_game_continue = False

    """ Check the computer not getting a blackjack and score is less than 17, so it has to play """
    while computer_score != 0 and computer_score < 17:
        """ Computer draws it, the score needs to be recalculated """
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    """ Printing the final cards and score details """
    print(f"Your final hand is {user_cards} and your final score is {user_score}")
    print(f"Computer final hand is {computer_cards} and computer final score is {computer_score}")
    compare_score(user_score, computer_score)


# Starting point
""" Check the user want to play blackjack game """
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    """ Clearing the screen before starting the game """
    system('clear')
    """ Starting the blackjack game """
    play_game()
