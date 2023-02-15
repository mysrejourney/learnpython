# Get the user input of his/her age
age = input("Enter your age : ")
# He lives until 90 years old
total_years = 90

remaining_years = total_years - int(age)
number_of_months_remaining = remaining_years * 12 #  calculating number of months
number_of_weeks_remaining = remaining_years * 52 #  calculating number of weeks
number_of_days_remaining = remaining_years * 365 #  calculating number of days

print(f"You have {number_of_days_remaining} days, {number_of_weeks_remaining} weeks, and {number_of_months_remaining} mnoths left")


