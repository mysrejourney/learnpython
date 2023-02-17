print("Welcome to the python pizza delivery center")
size = input("Enter your pizza size S/M/L: ")
add_pepperoni = input("Do you want to add pepperoni Y/N: ")
extra_cheese = input("Do you want to add extra cheese Y/N: ")
bill = 0
if size.upper() == 'S':
    bill += 15
    if add_pepperoni.upper() == 'Y':
        bill += 2
elif size.upper() == 'M':
    bill += 20
    if add_pepperoni.upper() == 'Y':
        bill += 3
else:
    bill += 25
    if add_pepperoni.upper() == 'Y':
        bill += 2

if extra_cheese.upper() == 'Y':
    bill += 1

print(f" Your final bill is {bill}")