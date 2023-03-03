"""
Adding two numbers
"""


def add(first_number, second_number):
    return first_number + second_number


"""
Subtracting  two numbers
"""


def substract(first_number, second_number):
    return first_number - second_number


"""
Multiplying two numbers
"""


def multiply(first_number, second_number):
    return first_number * second_number


"""
Dividing two numbers
"""


def divide(first_number, second_number):
    return first_number / second_number


# Creating dictionary with operations symbol
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

# Get the first number from user
num1 = int(input("What's the first number? "))

# Print all the operation symbols
for symbol in operations:
    print(symbol)

is_right_operand = False
game_continue = True
# Check if the game should continue
while game_continue:
    # Check if the user provided operation symbol is valid one
    while not is_right_operand:
        operands = input("Pick the operation : ")
        count = 0
        # Loop through all the symbols and check with user provided operation
        for symbol in operations:
            # If it's not same, increase count by 1
            if operands != symbol:
                count += 1
        """ Check count is same as dictionary length. If so, it is invalid operand provided by user.
        Then, we use ask them again to enter operation again.
        """
        if count == len(operations):
            print(f"Invalid Operations")
        else:
            is_right_operand = True

    # Get the second number from user
    num2 = int(input("What's the second number? "))

    # Loop through all symbols and compare the user operation
    for index in operations:
        # If it is same, call the respective function
        if index == operands:
            result = operations[index](num1, num2)

    # Ask the user if they wanted to continue
    calc_continue = input(f"Result of {num1} {operands} {num2} = {result}. Type 'y' to continue, or 'n' to stop: ")
    if calc_continue == 'n':
        game_continue = False
    else:
        is_right_operand = False
        num1 = result
