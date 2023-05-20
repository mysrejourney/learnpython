import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

""" This is alpha vantage api account details. """
ALPHA_VANTAGE_API_KEY = "D8P3PP2U7YVJG5ID"
ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"

""" This is news api account details. """
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "f9327b808cc149309efd604ae686ae6f"

""" This is twilio account details. We need to create user and along with twilio phone number """
TWILIO_ACCOUNT_SID = "AC6ddc09da7a237c4ccb658b47ee48aeb3"
TWILIO_AUTH_TOKEN = "3e121b702f244f75701ddf4d95c2c363"

## STEP : Use https://www.alphavantage.co
# TODO 1 : GET THE DAILY CLOSING DETAILS FOR YESTERDAY
stock_param = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY
}
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&apikey=D8P3PP2U7YVJG5ID#
response = requests.get(url=ALPHA_VANTAGE_ENDPOINT, params=stock_param)
response.raise_for_status()
# print(response.json())
# We need daily stock details
daily_stock_details = response.json()["Time Series (Daily)"]

""" Converting dictionary to list as dictionary key value is dynamic (date). 
So handling list would be easy as it works based on index """
resultList = [value for (key, value) in daily_stock_details.items()]
# print(resultList)

""" Get the closing value for yesterday which is first data """
yesterday_closing_value = resultList[0]["4. close"]
# print(yesterday_closing_value)

# TODO 2 : GET THE DAILY CLOSING DETAILS FOR THE DAY BEFORE

""" Get the closing value for the day before which is first data """
day_before_closing_value = resultList[1]["4. close"]
# print(day_before_closing_value)

# TODO 3 : CALCULATE THE DIFFERENCE

""" Calculate the difference between these two """
difference = float(yesterday_closing_value) - float(day_before_closing_value)
# print(difference)

# TODO 4 : CALCULATE THE PERCENTAGE DIFFERENCE
percentage_difference = round(abs((difference / float(yesterday_closing_value)) * 100))
# print(percentage_difference)
if percentage_difference > 0:
    icon = "🔺"
else:
    icon = "🔻"
# TODO 5 : CHECK THE PERCENTAGE DIFFERENCE
# When STOCK price increase/decreases by 1% between yesterday and the day before yesterday then print("Get News").

if percentage_difference > 1:
    news_parameter = {
        "q": COMPANY_NAME,
        "apiKey": "f9327b808cc149309efd604ae686ae6f"
    }
    """ Hit the news api to get the news details about the company """
    company_response = requests.get(url=NEWS_API_ENDPOINT, params=news_parameter)
    company_response.raise_for_status()
    articles_data = company_response.json()["articles"]
    first_three_articles = articles_data[:3]
    # print(first_three_articles)

    """ Form the message format as author name, title and description for first three articles. So, it can be 
    sent as a sms """
    articles_info = [f"{STOCK}: {icon}{percentage_difference}%, Author : {article['author']}. \nTitle : {article['title']}. \nDescription : {article['description']}"
                     for article in first_three_articles]
    # print(articles_info)

## STEP : Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
    # create the Client object by passing account id and auth token of twilio account for the user
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in articles_info:
        """ Compose the message body and from/to mobile number. From number is twilio phone number """
        message = client.messages.create(
                body=f"{article}",
                from_='+14632238856',
                to='+919986998881'
        )
        print(message.status)  # To track the status of the message

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""



