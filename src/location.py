import pytermgui as ptg
from geopy.geocoders import Nominatim
import os
from dotenv import load_dotenv, find_dotenv, set_key

dotenv_path = find_dotenv()

if not dotenv_path:
    dotenv_path = ".env"

def submit_info(city, state, country):
    geolocator = Nominatim(user_agent="weather-display")
    location = f"{city}, {state}, {country}"

    location_lat = location.latitude
    location_lon = location.longitude

    set_key(dotenv_path, "weather-display_lat", location_lat)
    set_key(dotenv_path, "weather-display_lon", location_lon)

with ptg.WindowManager() as manager:
    manager.layout.add_slot("body")

    city_field = ptg.InputField(prompt="City: ")
    state_field = ptg.InputField(prompt="State: ")
    country_field = ptg.InputField(prompt="Country: ")

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
