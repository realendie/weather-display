import requests
import configparser
from geopy.geocoders import Nominatim
import time

from config.weather_codes import get_weather_info

config = configparser.ConfigParser()
config.read('config/config.ini')

temperature_unit = config.get('CONFIG', 'temperature_unit')
windspeed_unit = config.get('CONFIG', 'windspeed_unit')
precipitation_unit = config.get('CONFIG', 'precipitation_unit')
timezone = config.get('CONFIG', 'timezone')

# Example location: Knoxville, TN
LAT = 35.9606
LON = -83.9207

def cords_to_city(LAT, LON):
    geolocator = Nominatim(user_agent="weather-display")
    time.sleep(1)
    location = geolocator.reverse(f"{LAT},{LON}")

    city = address.get("city", "")
    state = address.get("state", "")
    country = address.get("country", "")



url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": LAT,
    "longitude": LON,
    "current_weather": True,
    "hourly": "precipitation,precipitation_probability,weathercode",
    "temperature_unit": {temperature_unit},
    "windspeed_unit": {windspeed_unit},
    "precipitation_unit": {precipitation_unit},
    "timezone": {timezone}
}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()

data = response.json()

current = data["current_weather"]

current_temp = current["temperature"]
current_wind_speed = current["windspeed"]
current_wind_dir = current["winddirection"]

hourly = data["hourly"]

precip_amount = hourly["precipitation"][0]
precip_probability = hourly["precipitation_probability"][0]
weather_code = hourly["weathercode"][0]
precip_type, intensity = get_weather_info(weather_code)

def display_data():
    if  temperature_unit == "fahrenheit":
        print(f"Temperature: {current_temp} °F")
    elif temperature_unit == "celcius":
        print(f"Temperature: {current_temp} °C")

    print(f"Wind: {current_wind_speed} {windspeed_unit} @ {current_wind_dir}°")

    if intensity is not None:
        print(f"Preciptiation: {intensity} {precip_type}")
    else:
        print("Preciptiation:", precip_type)

    print(f"Chance: {precip_probability}%")

    if precipitation_unit == 'inch':
        print(f"Accumulation: {precip_amount} in")
    elif precipitation_unit == 'centimeter':
        print(f"Accumulation: {precip_amount} cm")

display_data()
