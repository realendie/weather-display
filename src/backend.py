import requests

# Example location: Knoxville, TN
LAT = 35.9606
LON = -83.9207

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": LAT,
    "longitude": LON,
    "current_weather": True,
    "hourly": "precipitation,precipitation_probability,weathercode",
    "temperature_unit": "fahrenheit",   # optional
    "windspeed_unit": "mph",            # optional
    "precipitation_unit": "inch",       # optional
    "timezone": "auto"
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

def interpret_precip_type(code: int) -> str:
    if code in [61, 63, 65, 80, 81, 82]:
        return "Rain"
    elif code in [71, 73, 75, 85, 86]:
        return "Snow"
    elif code in [95, 96, 99]:
        return "Thunderstorm"
    else:
        return "None"

precip_type = interpret_precip_type(weather_code)
print(f"Precip Type: {precip_type}")

