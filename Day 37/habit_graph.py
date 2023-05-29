""" Import the required modules """
import requests
import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
API_TOKEN = "aXJEfAaUdwVtvFpaUdQq"
USER_NAME = "satsqaexperience"

""" User related data to create the user """
user_data = {
    "token" : API_TOKEN,
    "username" : USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor" : "yes"
}

""" Create the User by hitting this endpoint """
# response = requests.post(url=PIXELA_ENDPOINT, json=user_data)
# print(response.text)  # {"message":"Success. Let's visit https://pixe.la/@satsqaexperience , it is your profile page!","isSuccess":true}

""" Create a new pixelation graph definition """
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"
GRAPH_ID = "satsgraph1"
headers = {
    "X-USER-TOKEN" : API_TOKEN
}

graph_data = {
    "id": GRAPH_ID,
    "name": "Coding graph",
    "unit": "hours",
    "type": "int",
    "color": "shibafu"
}

""" Create the graph by hitting this endpoint """
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_data, headers=headers)
# print(response.text)  # {"message":"Success.","isSuccess":true}

""" Post a value in pixelation graph definition """
VALUE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}"

time_now = datetime.date.today()
# print(time-now)
current_date = time_now.strftime("%Y%m%d")
# print(current_date)

value_data = {
    "date": current_date,
    "quantity": "10"
}

""" Post the value by hitting this endpoint """
response = requests.post(url=VALUE_ENDPOINT, json=value_data, headers=headers)
print(response.text)  # {"message":"Success.","isSuccess":true}

UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{current_date}"
update_data = {
    "quantity": "9"
}
response = requests.put(url=UPDATE_ENDPOINT, headers=headers, json=update_data)
print(response.text)

DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{current_date}"
response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
print(response.text)


