import pytermgui as ptg

with ptg.WindowManager() as manager:
    location = 'NewYork City, NY'
    tempurature = 94
    weather_type = 'Rainy'
    wind = '340/10'

    window = (
        ptg.Window(
            ptg.Label(location, parent_align=0),
            "",
            ptg.Label(f'Tempurature: {tempurature}', parent_align=0),
        )
        .set_title('weather-display')
        .center()
    )

    manager.add(window)
