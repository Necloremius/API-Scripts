import requests

zipcode = input("Enter in your zip code nerd: ")
response = requests.get(f"http://api.weatherapi.com/v1/current.json?key=*redacted*&q={zipcode}").json()

print(f"""Current Weather:

Time last updated: {response["current"]["last_updated"]}
Temperature (Celsius): {response["current"]["temp_c"]}
Temperature (Fahrenheit): {response["current"]["temp_f"]}
Feels like (Celsius): {response["current"]["feelslike_c"]}
Feels like (Fahrenheit): {response["current"]["feelslike_f"]}
Weather condition: {response["current"]["condition"]["text"]}
Wind speed (mph): {response["current"]["wind_mph"]}
Wind speed (kph): {response["current"]["wind_kph"]}
Wind direction: {response["current"]["wind_dir"]}
Pressure (millibars): {response["current"]["pressure_mb"]}
Precipitation (millimeters): {response["current"]["precip_mm"]}
Precipitation (precip_in): {response["current"]["precip_in"]}
Humidity (percentage): {response["current"]["humidity"]}
Cloud coverage(percentage): {response["current"]["cloud"]}
UV index: {response["current"]["uv"]}
Wind gust (mph): {response["current"]["gust_mph"]}
Wind gust (kph): {response["current"]["gust_kph"]}
""")
