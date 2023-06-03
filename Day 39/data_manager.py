""" Import the required modules """
import requests

""" Below are for satsqaexperience """
# SHEETY_END_POINT = "https://api.sheety.co/08694382c5f7b971b19fccf6e727db9b/flightDeals/prices"
# sheety_headers = {
#     "Authorization": "Basic c2F0c3FhZXhwZXJpZW5jZTpBZGhpcmFAMjAxMw=="
# }

""" Below are for satheeshpandianj """
SHEETY_END_POINT = "https://api.sheety.co/a4bc9b4e885640fd66ae0defaa3b380c/flightDeals/prices"
sheety_headers = {
    "Authorization": "Basic c2F0aGVlc2hwYW5kaWFuakBnbWFpbC5jb206QWRoaXJhQDIwMTM="
}


class DataManager:  # Create a class for DataManager
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):  # Get the iataCode from the sheet
        response = requests.get(url=SHEETY_END_POINT, headers=sheety_headers)
        results = response.json()
        self.destination_data = results["prices"]
        return self.destination_data

    def update_destination_codes(self):  # Update the iataCode in the sheet
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_END_POINT}/{city['id']}", json=new_data, headers=sheety_headers)