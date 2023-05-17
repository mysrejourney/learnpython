"""
Import the required modules
"""
import requests
from twilio.rest import Client
import os

""" API Key from OpenWeatherMap API website for my user """
API_KEY = "8989b6f87bfe5432fce9d8d7d4f464f0"
# Ideally it has to be passed as environmental variable like below
# API_KEY = os.environ.get("OWM_API_KEY")

""" Parameters to be passed as part of API call """
parameter = {
    "lat": 12.971599,
    "lon": 77.594566,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

""" Hit API URL and pass the parameter """
response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameter)
response.raise_for_status()  # Raise any issues with status code
data = response.json()  # Convert the response to dictionary format
""" Just fetch only first 12 hours of data """
weather_hourly_data = data["hourly"][:12]
# print(weather_hourly_data)

will_rain_today = False  # To track if the rain comes today
""" Loop through first 12 hours of data """
for hour in weather_hourly_data:
    if hour["weather"][0]["id"] < 700:  # If the id is less than 700, then rain chances are there as per API documentation
        will_rain_today = True

""" This is twilio account details. We need to create user and along with twilio phone number """
account_sid = "AC6ddc09da7a237c4ccb658b47ee48aeb3"
# auth_token = os.environ.get("AUTH_TOKEN")
auth_token = "4be44f8baf74aff7612f025f5e9ac9b8"

if will_rain_today:
    # create the Client object by passing account id and auth token of twilio account for the user
    client = Client(account_sid, auth_token)
    """ Compose the message body and from/to mobile number. From number is twilio phone number """
    message = client.messages \
        .create(
            body="It will ⛈ today and bring 🌂",
            from_='+14632238856',
            to='+919986998881'
    )
    print(message.status)  # To track the status of the message
