""" Import required modules """
import requests
from _datetime import datetime
import os

""" Get the API security keys from environment variable """
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEETY_AUTH_TOKEN = os.environ.get("SHEETY_AUTH_TOKEN")

""" Initialize the constant data """
NUTRITIONIX_END_POINT = "https://trackapi.nutritionix.com"
SHEETY_END_POINT = "https://api.sheety.co/08694382c5f7b971b19fccf6e727db9b/myWorkouts/workouts"
GENDER = "male"
WEIGHT = 70
HEIGHT = 166
AGE = 40
""" Get the user input """
exercise_text = input('Tell me which exercises you did: ')

""" Build the workout data to be posted """
workout_data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

""" Configure the headers for NUTRITIONIX_END_POINT """
headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "Content-Type": "application/json"
}
""" Hit the API """
response = requests.post(url=f"{NUTRITIONIX_END_POINT}/v2/natural/exercise", json=workout_data, headers=headers)
result = response.json()
# print(result)
# print(result["exercises"])

""" Get the current date and time """
time_now = datetime.now()
current_date = time_now.strftime("%d/%m/%Y")
current_time = time_now.strftime("%X")
""" Get the exercise name, duration and calories from the response of above end point and build the data to be posted to the next API """
for exercise in result["exercises"]:
    # print(exercise)
    exercise_data = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

""" Configure the Sheety headers for Google sheets """
sheety_headers = {
    "Authorization": SHEETY_AUTH_TOKEN
}
""" Hit the API with above data and headers """
response = requests.post(url=SHEETY_END_POINT, json=exercise_data, headers=sheety_headers)
print(response.text)
