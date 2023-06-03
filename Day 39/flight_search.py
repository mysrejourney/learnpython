""" Import the required modules """
import requests
from flight_data import FlightData

""" TEQUILA API DETAILS """
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "zlTDj65ycy93_FHD9HtSPR4kgDJ10hVW"


class FlightSearch:  # Create Flight search class

    def get_destination_code(self, city_name):  # Get the destination code for each city in the google sheet
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        tequila_headers = {
            "apikey": TEQUILA_API_KEY
        }
        tequila_data = {
            'term': city_name,
            'locale': 'en-US',
            'location_types': 'city'
        }
        """ Hit the API """
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=tequila_data, headers=tequila_headers)
        results = response.json()["locations"]
        code = results[0]['code']
        return code

    """ Check the flight details """
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        tequila_headers = {
            "apikey": TEQUILA_API_KEY
        }
        tequila_data = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        """ Hit the API """
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/search", params=tequila_data, headers=tequila_headers)
        try:  # Get the first data from the response
            data = response.json()['data'][0]
        except IndexError:
            """ If there is not data, print the message """
            print(f"No data is found for the destination : {destination_city_code}")
            return None
        """ Save all the values in an object """
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["cityCodeFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["cityCodeTo"],
            out_date='03/06/2023',
            return_date='05/06/2023'
        )
        return flight_data
