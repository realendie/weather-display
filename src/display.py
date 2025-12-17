import pytermgui as ptg

with ptg.WindowManager() as manager:
    location = "No Location Specified"

    window = (
        ptg.Window(
            ptg.Label(f"[bold]{location}")
        )
        .set_title("weather-display")
        .center()
    )

    manager.add(window)
