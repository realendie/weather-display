import pytermgui as ptg
from geopy.geocoders import Nominatim

def submit_info(city, state, country):
    geolocator = Nominatim(user_agent="weather-display")
    location = geolocator.geocode(f"{city}, {state}, {country}")

    if location:
        return location.latitude, location.longitude
    else:
        return None

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

    submit_button = ptg.Button("Submit", onclick=submit_info)

    window = (
        ptg.Window(
            location_fields,
            submit_button,
            width=0,
        )
        .set_title("Select Location")
    )

manager.add(window)
