import requests
from twilio.rest import Client
import os

# API_KEY = "8989b6f87bfe5432fce9d8d7d4f464f0"
API_KEY = os.environ.get("")
parameter = {
    "lat": 12.971599,
    "lon": 77.594566,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameter)
response.raise_for_status()  # Raise any issues with status code
data = response.json()  # Convert the response to dictionary format
weather_hourly_data = data["hourly"][:12]
# print(weather_hourly_data)

will_rain_today = False
for hour in weather_hourly_data:
    if hour["weather"][0]["id"] < 700 or hour["weather"][0]["main"] == "Rain":
        will_rain_today = True


account_sid = "AC6ddc09da7a237c4ccb658b47ee48aeb3"
auth_token = "4be44f8baf74aff7612f025f5e9ac9b8"

if will_rain_today:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It will ⛈ today and bring 🌂",
            from_='+14632238856',
            to='+919986998881'
    )
    # print("It will ⛈ today and bring 🌂")

# --------------------------------------------------------

# import requests
#
# user_data = {
#     "username": "satsqaexperience",
#     "firstName": "Satheesh",
#     "lastName": "SREJourney",
#     "email": "satsqaexperience@gmail.com"
# }
#
# user_headers = {
#     "Content-Type": "application/json"
# }
#
# user_parameter = {
#     "apiKey": "0e27abb314894533b37d57946ee15d9e"
# }
# response = requests.post(url="https://api.spoonacular.com/users/connect", json=user_data, headers=user_headers, params=user_parameter)
# response.raise_for_status()
# data = response.json()
# print(data)
# username = data["username"]
# hash_code = data["hash"]
#
# user_parameter = {
#     "apiKey": "0e27abb314894533b37d57946ee15d9e",
#     "hash": hash_code
# }
# get_meal_plan_response = requests.get(url=f"https://api.spoonacular.com/mealplanner/{username}/week/2020-06-01", params=user_parameter)
# get_meal_plan_response.raise_for_status()
# print(get_meal_plan_response.json())

# -------------------------------------------------------