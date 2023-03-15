from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

""" Creating objects for each class """
drink_names = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    order_name = input(f"What would you like? {drink_names.get_items()}: ").lower()
    # print(order_name)
    """ If the choice is report, then get the details """
    if order_name == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    elif order_name == 'exit':
        """ If the choice is exit, then exit the program """
        is_on = False
    else:
        """ If the choice is drink, then get the drinks """
        """ Check if the drink is available """
        drinkname = drink_names.find_drink(order_name)
        """ If the resources are enough to make the drinks and the money is sufficient to buy it """
        if drinkname != "Sorry" and coffee_maker.is_resource_sufficient(drinkname) and money_machine.make_payment(drinkname.cost):
            """ Prepare the drink """
            coffee_maker.make_coffee(drinkname)