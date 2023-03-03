from os import system

print("Welcome to the auction !!!!")

# def find_highest_bidder(bidding_info):
#     highest_bid = 0
#     for bid_value in bidding_info:
#         # print(bidding_info[bid_value])
#         if bidding_info[bid_value] > highest_bid:
#             highest_bid = bidding_info[bid_value]
#             highest_bidder_name = bid_value
#     print(f"The winner is {highest_bidder_name} and highest bid is {highest_bid}")

is_game_on = True
# Creating empty dictionary
bidder_info = {}
# Until bidder is there, this loop continues
while is_game_on:
    # Get user inputs
    name = input("What's your name? ")
    price = int(input("What's your bid? $"))
    any_more_bidder = input("Is there any other bidder? Type 'yes' or 'no' ").lower()
    # Assign bidding value against the bidder name. Save the values in bidder_info dictionary
    bidder_info[name] = price
    # Check if there are any other bidder
    if any_more_bidder == 'no':
        is_game_on = False
        # find_highest_bidder(bidder_info)
        # Find the highest bidder
        highest_bid = 0
        # Loop through all bidders using bidder_info dictionary
        for bid_value in bidder_info:
            # Check if the bidding value is the high
            if bidder_info[bid_value] > highest_bid:
                # Save the bidding value and bidder name
                highest_bid = bidder_info[bid_value]
                highest_bidder_name = bid_value
        print(f"The winner is {highest_bidder_name} and highest bid is {highest_bid}")

    else:
        # Clearing the screen
        system('clear')


