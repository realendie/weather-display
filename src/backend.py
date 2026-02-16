import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

temperature_unit = config.get('CONFIG', 'temperature_unit')
windspeed_unit = config.get('CONFIG', 'windspeed_unit')
precipitation_unit = config.get('CONFIG', 'precipitation_unit')
timezone = config.get('CONFIG', 'timezone')

# Example location: Knoxville, TN
LAT = 35.9606
LON = -83.9207

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

print(f"Temperature: {current_temp} °F")
print(f"Wind: {current_wind_speed} mph @ {current_wind_dir}°")

hourly = data["hourly"]

precip_amount = hourly["precipitation"][0]
precip_probability = hourly["precipitation_probability"][0]
weather_code = hourly["weathercode"][0]

print(f"Precipitation: {precip_amount} in")
print(f"Chance: {precip_probability}%")
print(f"Weather Code: {weather_code}")

