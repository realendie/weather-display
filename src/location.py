print ('Loading...')

import pytermgui as ptg
from geopy.geocoders import Nominatim
import os
import configparser
import time

config = configparser.ConfigParser()
config.read('config/config.ini')

LAT = config.get('LOCATION', 'location_lat')
LON = config.get('LOCATION', 'location_lon')

def cords_to_city(LAT, LON):
    global city
    global state
    global country

    geolocator = Nominatim(user_agent="weather-display")
    time.sleep(1)
    location = geolocator.reverse(f"{LAT},{LON}")

    address = location.raw.get('address', {})

    city = address.get("city", "")
    state = address.get("state", "")
    country = address.get("country", "")

def submit_info(city, state, country):
    geolocator = Nominatim(user_agent="weather-display")
    location = f"{city}, {state}, {country}"

    location_lat = location.latitude
    location_lon = location.longitude

    set_key(dotenv_path, "weather-display_lat", location_lat)
    set_key(dotenv_path, "weather-display_lon", location_lon)

with ptg.WindowManager() as manager:
    manager.layout.add_slot("body")

    cords_to_city(LAT, LON)

    city_field = ptg.InputField(f"{city}", prompt="City: ")
    state_field = ptg.InputField(f"{state}", prompt="State: ")
    country_field = ptg.InputField(f"{country}", prompt="Country: ")

    city = city_field.value
    state = state_field.value
    country = country_field.value

    location_fields = ptg.Container(
        city_field,
        state_field,
        country_field,
    )

    submit_button = ptg.Button("Submit", onclick=lambda *_: submit_info(city, state, country))

    window = (
        ptg.Window(
            location_fields,
            submit_button,
            width=0,
        )
        .set_title("Select Location")
    )

    manager.add(window)
