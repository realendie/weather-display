import pytermgui as ptg

def submit_info(*_):
    manager.stop()

with ptg.WindowManager() as manager:
    manager.layout.add_slot("body")

    city_field = ptg.InputField(prompt="City: ")
    state_field = ptg.InputField(prompt="State: ")
    country_field = ptg.InputField(prompt="Country: ")


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
