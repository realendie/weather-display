import pytermgui as ptg

with ptg.WindowManager() as manager:

    city_field = ptg.InputField(prompt="City: ", wrap=False),
    state_field = ptg.InputField(prompt="State: "),
    country_field = ptg.InputField(prompt="Country: "),

    location_fields = ptg.Container(
        city_field,
        state_field,
        country_field,
    )

    window = (
        ptg.Window(
            location_fields,
            width=0,
        )
        .set_title("Select Location")
    )

    manager.add(window)
