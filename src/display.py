import pytermgui as ptg

with ptg.WindowManager() as manager:
    manager.layout.add_slot("body")

    # Create two columns using Splitter
    left_column = ptg.Container(
        ptg.Label("Temp: 67°", wrap=False),
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
