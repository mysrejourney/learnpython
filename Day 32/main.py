# import smtplib
#
# # ndipiutiwndgwejm
# my_email = "satheeshpandianj@gmail.com"
# my_password = "yybwtqphmnsworow"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=my_password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs="satsqaexperience@gmail.com",
#                     msg="Hello, Sats")
# connection.close()

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="satheeshpandianj@gmail.com",
#                         msg="Hello, Sats")

# ---------------------------------------------------------------
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(year)
# print(type(now))
# month = now.month
# print(month)
# day_of_week = now.day
# print(day_of_week)
# ----------------------------------------------------------

import datetime as dt
import random
import smtplib

now = dt.datetime.now()
print(now.weekday())  # 0 - Monday, 1 - Tuesday etc.,
if now.weekday() == 1:  # If the day is Tuesday, the read the quote and send an email
    with open("quotes.txt", "r") as data:
        file = data.readlines()
        random_quote = random.choice(file)
        # print(random_quote)
    print(random_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        my_email = "satheeshpandianj@gmail.com"
        my_password = "yybwtqphmnsworow"

        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="satsqaexperience@gmail.com",
                            msg=f"Sub: Quote of the day \n\n {random_quote}")