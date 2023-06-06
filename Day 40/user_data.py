import requests
""" Below are for satheeshpandianjeganathan """
SHEETY_END_POINT = "https://api.sheety.co/3ceb979d9324df2be9da6d7e6d0e6e8a/flightDeals/users"
SHEETY_HEADERS = {
    "Authorization": "Bearer q1w2e3r4t5y6u7i8o9p0abcd1234efgh5678ijkl90=="
}

class UserData:
    def __init__(self):
        pass

    def post_new_data(self, first_name, last_name, email):

        SHEETY_USER_DATA = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(url=SHEETY_END_POINT, json=SHEETY_USER_DATA, headers=SHEETY_HEADERS)
        print(response.text)
        print(f"OK. You are in the club now")
