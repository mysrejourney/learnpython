import requests
import datetime as dt

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)  # O/P: <Response [200]>
# print(response.status_code)  # 200
# print(response.text)  # {"message": "success", "timestamp": 1683080716, "iss_position": {"latitude": "-38.9215", "longitude": "154.6791"}}
# print(type(response.text))  # <class 'str'>
# print(response.json())  # {"message": "success", "timestamp": 1683080716, "iss_position": {"latitude": "-38.9215", "longitude": "154.6791"}}
# print(type(response.json()))  # <class 'dict'>
response.raise_for_status()
result = response.json()
latitude = result["iss_position"]["latitude"]
longitude = result["iss_position"]["longitude"]
iss_position = (longitude, latitude)
# print(iss_position)
# print(type(iss_position))
# print(type(latitude))
# print(type(longitude))

parameter = {
    "lat": latitude,
    "lng": longitude,
    "formatted": 0
}
print(parameter)
response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)


now = dt.datetime.now()
print(now.hour)