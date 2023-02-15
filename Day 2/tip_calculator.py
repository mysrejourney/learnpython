print(f"Welcome to the tip calculator")
# Get the total bill
total_bill = input("What was the total bill? $")
# Get the tip percentage
tip = input("What percentage tip would like to give? 10, 12 or 15? ")
# Get the number of people
number_of_people = input("How many people to split the bill? ")

# calculate total amount = total bill + tip%
total_amount = float(total_bill) + (float(total_bill) * (int(tip) / 100))

# Calculate each share is total amount / number of peope
each_contribution = round(total_amount / int(number_of_people), 2)

# Print each share value
print(f"Each person should pay: ${each_contribution}")