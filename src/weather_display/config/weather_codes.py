WEATHER_CODE_MAP = {
    0:  ("Clear", None),
    1:  ("Mostly Clear", None),
    2:  ("Partly Cloudy", None),
    3:  ("Overcast", None),

    45: ("Fog", None),
    48: ("Icy Fog", None),

    51: ("Drizzle", "Light"),
    53: ("Drizzle", "Moderate"),
    55: ("Drizzle", "Heavy"),

    56: ("Freezing Drizzle", "Light"),
    57: ("Freezing Drizzle", "Heavy"),

    61: ("Rain", "Light"),
    63: ("Rain", "Moderate"),
    65: ("Rain", "Heavy"),

    66: ("Freezing Rain", "Light"),
    67: ("Freezing Rain", "Heavy"),

    71: ("Snow", "Light"),
    73: ("Snow", "Moderate"),
    75: ("Snow", "Heavy"),
    77: ("Snow Grains", None),

    80: ("Rain Showers", "Light"),
    81: ("Rain Showers", "Moderate"),
    82: ("Rain Showers", "Heavy"),

    85: ("Snow Showers", "Light"),
    86: ("Snow Showers", "Heavy"),

    95: ("Thunderstorm", None),
    96: ("Thunderstorm with Hail", "Light"),
    99: ("Thunderstorm with Hail", "Heavy"),
}

def get_weather_info(code: int):
    return WEATHER_CODE_MAP.get(code, ("unknown", None))

