import pytermgui as ptg

with ptg.WindowManager() as manager:
    location = "No Location Specified"
    tempurature = 94

    window = (
        ptg.Window(
            ptg.Splitter(
                ptg.Label(f"[bold]{location}", parent_align=0),
                ptg.Label(f"[bold]Tempurature: {tempurature}"),
            )
        )
        .set_title("weather-display")
        .center()
    )

    manager.add(window)
