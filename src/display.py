import pytermgui as ptg

from backend import current_temp, current_wind_speed, current_wind_dir, precip_type, precip_probability, precip_amount

with ptg.WindowManager() as manager:
    manager.layout.add_slot("body")

    # Create two columns using Splitter
    left_column = ptg.Container(
        ptg.Label(f"Temp: 67", wrap=False),
        ptg.Label("Precipitation: Rain", wrap=False),
    )
    
    right_column = ptg.Container(
        ptg.Label("Winds: 180/16", wrap=False),
        ptg.Label("Chance: 63%", wrap=False),
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
