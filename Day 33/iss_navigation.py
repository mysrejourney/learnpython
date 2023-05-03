""" Import Required modules """
import time
import requests
import datetime as dt
import smtplib

""" Set my location's latitude and longitude """
MY_LAT = 12.971599
MY_LNG = 77.594566

""" Set my username and password for email sending """
my_email = "satheeshpandianj@gmail.com"  # Your email id from where you want to send an email
my_password = "yybwtqphmnsworow"  # Your password for where you want to send an email (App Password)


def is_iss_overhead():  # To check if ISS is overhead on our location
    response = requests.get(url="http://api.open-notify.org/iss-now.json")  # Hit an API and get the response
    response.raise_for_status()  # Raise any issues with status code
    data = response.json()  # Convert the response to dictionary format
    # print(data)
    latitude = float(data["iss_position"]["latitude"])  # Get current latitude position of ISS
    longitude = float(data["iss_position"]["longitude"])  # Get current longitude position of ISS

    """ Check if ISS is overhear on our location """
    if (latitude - 5) <= MY_LAT <= (latitude + 5) and (longitude - 5) <= MY_LNG <= (longitude + 5):
        return True


def is_night():  # To check if the current hour is in nighttime
    """ Creating the parameter to be passed in the API """
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0  # which gives proper time format
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    result = response.json()
    print(result)
    sunrise_hour = int(result["results"]["sunrise"].split("T")[1].split(":")[0])  # Get the hour of sunrise
    sunset_hour = int(result["results"]["sunset"].split("T")[1].split(":")[0])  # Get the hour of sunset
    print(sunrise_hour, sunset_hour)

    now = dt.datetime.now()
    hour = now.hour  # Get the current time hour
    print(hour)

    """ Check if current hour is dark (After sunset and before sunrise ) """
    if hour >= sunset_hour or hour <= sunrise_hour:
        return True


while True:
    time.sleep(60)  # run this every 1 min
    if is_night() and is_iss_overhead():
        """ send an email to below address with the below message """
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg="Sub: ISS Navigation is up in the sky, Look Up\n\n Hey, look up the sky to see ISS navigation")
