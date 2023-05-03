""" Import required modules """
import pandas
import datetime as dt
import smtplib
import random

NAME="[NAME]"  # String to be replaced in a file
my_email = "satheeshpandianj@gmail.com"  # Your email id from where you want to send an email
my_password = "yybwtqphmnsworow"  # Your password for where you want to send an email (App Password)

# Get the current time now (date time format)
now = dt.datetime.now()
# print(now)
month = now.month  # Get the current month (int format)
day = now.day  # Get the current day (int format, 0 - Sunday, 1- Monday etc.,)

# print(month, day)
data = pandas.read_csv("birthdays.csv")  # Read the CSV file
# print(data)
new_list = data.to_dict(orient="records")  # Convert the CSV to list of dictionaries
# print(new_list)
# print(type(new_list))

for item in new_list:  # Loop through the dictionary
    if item["month"] == month and item["day"] == day:  # check current month and day is matches any of the row in CSV data
        name = item["name"]  # If it matches, get the name from that row
        email = item["email"]  # If it matches, get the email from that row
        # print(name, email)

        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:  # Open any file randomly which are placed in letters_templates folder
            content = file.read()  # Read the entire content and save it
            # print(content)
            replace_name = content.replace(NAME, f"{name}")  # Replace [NAME] with the actual name we have got from the CSV file
            # print(replace_name)
        print(replace_name)

        with smtplib.SMTP("smtp.gmail.com") as connection:  # Open the SMTP connection for gmail (your email server)
            connection.starttls()  # start the secured communication
            connection.login(user=my_email, password=my_password)  # Login to your gmail
            connection.sendmail(from_addr=my_email,
                                to_addrs="amio.praba@gmail.com",
                                msg=f"Sub: Happy Birthday \n\n {replace_name}")  # Send an email mentioned in to_addr



