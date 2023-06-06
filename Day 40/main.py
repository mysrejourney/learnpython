""" Import the required modules """
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

""" ORIGIN CITY """
ORIGIN_CITY_IATA = "LON"
""" Create objects of the class """
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
""" Get the destination data from the google sheet """
sheet_data = data_manager.get_destination_data()

""" In the sheet, if iataCode is empty, then get the iataCode for that city from TEQUILA API """
for row in sheet_data:
    if row['iataCode'] == '':
        row["iataCode"] = flight_search.get_destination_code(row['city'])

""" Assign the updated sheet data to destination data """
data_manager.destination_data = sheet_data
""" Update the iataCode in the google sheet """
data_manager.update_destination_codes()
""" Now, read the updated google sheet which has iataCode for respective city """
sheet_data = data_manager.get_destination_data()

""" Get the date and time for tomorrow and after 180 days """
tomorrow = datetime.now() + timedelta(days=1)  # 2023-06-04 17:36:43.531206
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))  # 2023-11-30 17:36:43.531251
""" Loop through the sheet """
for destination in sheet_data:
    """ Get the flight price for each city for next 6 months """
    updated_price = flight_search.check_flights(ORIGIN_CITY_IATA,destination['iataCode'], from_time=tomorrow, to_time=six_month_from_today)

    if updated_price is None:
        continue
    # print(f"{destination['city']}: {destination['lowestPrice']}, {updated_price.destination_city}: {updated_price.price}")
    """ If the flight price is less than the price mentioned in google sheet, send the message """
    if destination["lowestPrice"] > updated_price.price:
        message = f"Low price alert! Only £{updated_price.price} to fly from {updated_price.origin_city} - " \
                    f"{updated_price.origin_airport} to {updated_price.destination_city} - {updated_price.destination_airport}", \
                    f" from {updated_price.out_date} to {updated_price.return_date}"
        if updated_price.stop_overs > 0:
            message += f"\nFlight has {updated_price.stop_overs} stop over, via {updated_price.via_city}."
            print(message)
        status = notification_manager.send_notification(alert_message=message)
        print(f"Status : {status}")

