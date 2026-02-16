import configparser
import pytermgui as ptg

from config.weather_codes import get_weather_info

config = configparser.ConfigParser()
config.read('config/config.ini')

temperature_unit = config.get('CONFIG', 'temperature_unit')
windspeed_unit = config.get('CONFIG', 'windspeed_unit')
precipitation_unit = config.get('CONFIG', 'precipitation_unit')
timezone = config.get('CONFIG', 'timezone')

from backend import current_temp, current_wind_speed, current_wind_dir, precip_type, precip_probability, precip_amount, intensity

with ptg.WindowManager() as manager:
    manager.layout.add_slot("body")

    if temperature_unit == "fahrenheit":
        temp_display_unit = "°F"
    elif temp_display_unit == "celcius":
        temp_display_unit = "°C"

    if intensity is not None:
        precip_display = f"Precipitation: {intensity} {precip_type}"
    else:
        precip_display = f"Precipitation: {precip_type}"
    # Create two columns using Splitter
    left_column = ptg.Container(
        ptg.Label(f"Tempurature: {current_temp} {temp_display_unit}", wrap=False),
        ptg.Label(f"Wind: {current_wind_speed} {windspeed_unit} @ {current_wind_dir}", wrap=False),
    )
    
    if precipitation_unit == 'inch':
        precip_unit_display = "in"
    elif precipitation_unit == "centimeters":
        precip_unit_display = "cm"

    right_column = ptg.Container(
        ptg.Label(precip_display),
        ptg.Label(f"Chance: {precip_probability}", wrap=False),
        ptg.Label(f"Accumulation: {precip_amount} {precip_unit_display}")
    )

    # Splitter will create two columns
    splitter = ptg.Splitter(left_column, right_column)

    window = (
        ptg.Window(
            splitter,
            width=0,  # Auto-size
        )
        .set_title("weather-display")
    )

    manager.add(window, assign="body")
