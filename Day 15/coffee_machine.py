
""" Import the required modules """
from data import MENU, resources, logo

# TODO 1 - Print the coffee machine report with available resources
""" To print the resources available """
def print_report():
    # print(f"Water: {resources['water']}, Milk: {resources['milk']}, Coffee: {resources['coffee']} available")
    water, coffee, milk, balance = print_resources()
    print(f"Water: {water} \nMilk: {milk}\nCoffee: {coffee}\nMoney: ${balance}")

# To calculate the total savings in the bank of coffee machine
total_savings = 0


""" To get the resources available """
def print_resources():
    water_quantity = resources['water']
    coffee_quantity = resources['coffee']
    milk_quantity = resources['milk']
    # print(f"Water: {resources['water']} \nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${total_savings}")
    return water_quantity, coffee_quantity, milk_quantity, total_savings


# def update_resources(drink_type, price):
#     if drink_type == 'cappuccino':
#         resources['water'] -= 250
#         resources['coffee'] -= 24
#         resources['milk'] -= 100
#     elif drink_type == 'latte':
#         resources['water'] -= 200
#         resources['coffee'] -= 24
#         resources['milk'] -= 150
#     elif drink_type == 'espresso':
#         resources['water'] -= 50
#         resources['coffee'] -= 18
#     global total_savings
#     total_savings += price
# print(f"Water: {resources['water']} \nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${total_savings}")

# TODO 4 - Update the resource quantity and the savings
""" Update the existing resources """
def update_resources(drink_type, price):

    """ Loop through the items ordered """
    for item in MENU[drink_type]['ingredients']:
        # Reduce the ordered quantity from the resource quantity
        resources[item] -= MENU[drink_type]['ingredients'][item]
    # Update the cost of the drink to the savings
    global total_savings
    total_savings += price
    # Give the coffee to the user
    print(f"Here is your {drink_type} ☕️. Enjoy!")


""" Process the coins """
def calculate_amount(quarter, dime, nickle, pennies, drink_type):
    # Get the drink cost
    price = MENU[drink_type]['cost']

    # Get the total coins value provided by the user
    total = quarter * .25 + dime * .10 + nickle * .05 + pennies * .01

    return price, total

# TODO 3 - Get the coins and evaluate if it is sufficient to buy
""" Get the user coins for the coffee and process them """
def make_coffee(drink_type):
    """ Get the user coins for the coffee """
    print("Please insert coins")
    quarter_coins = float(input("how many quarters?: "))
    dime_coins = float(input("how many dimes?: "))
    nickle_coins = float(input("how many nickles?: "))
    pennies_coins = float(input("how many pennies?: "))

    """ Calculate the total coins provided by the user """
    cost, sum = calculate_amount(quarter_coins, dime_coins, nickle_coins, pennies_coins, drink_type)

    """ Check the coins provided by user is sufficient to give the coffee """
    if sum >= cost:
        change = round(sum - cost, 2)
        print(f"Here is ${change} in change.")
        """ After providing the drink, update the existing resources """
        update_resources(drink_type, cost)
    else:
        print(f"Sorry that's not enough money. Money refunded.")


# def check_required_resources(water_qty, coffee_qty, milk_qty, drink_type):
#     if drink_type != 'espresso':
#         if milk_qty >= MENU[drink_type]['ingredients']['milk']:
#             return True
#         else:
#             print(f"Sorry there is not enough milk")
#             return False
#     if water_qty >= MENU[drink_type]['ingredients']['water']:
#         if coffee_qty >= MENU[drink_type]['ingredients']['coffee']:
#             return True
#         else:
#             print(f"Sorry there is not enough coffee")
#             return False
#     else:
#         print(f"Sorry there is not enough water")
#         return False


def check_required_resources(drink_type):
    for item in MENU[drink_type]['ingredients']:
        if MENU[drink_type]['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


is_working = True
while is_working:
    print(logo)
    # Get the user input
    drink_name = input("What would you like? (espresso/latte/cappuccino/report): ").lower()

    """ If the user wants to see the resource report and money balance """
    if drink_name == 'report':
        print_report()

    elif drink_name == 'exit':
        """ If the user wants to turn off the machine, he give 'exit' as input """
        is_working = False

    elif drink_name not in MENU:
        """ If the user's choice is not in the menu """
        print(f"Invalid selection. Please select valid menu.")

    else:
        """ If the user's choice is in the menu """
        """ Check the resources of water, milk, and coffee """
        # water, coffee, milk, balance = check_resources()
        # TODO 2 - Get the input and check the resource quantity
        """ Check the required resources of water, milk, and coffee to make the drink """
        result = check_required_resources(drink_name)

        """ If enough resources of water, milk, and coffee available, make cofeee """
        if result:
            make_coffee(drink_name)
