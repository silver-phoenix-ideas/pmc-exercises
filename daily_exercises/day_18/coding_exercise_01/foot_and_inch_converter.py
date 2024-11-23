# Imports
import FreeSimpleGUI as fsg

# Settings
fsg.theme("Black")
fsg.set_options(font=("Helvetica", 12))
field_size = (30, 1)
button_size = (10, 1)

# Widgets
foot_label = fsg.Text("Enter feet:")
foot_input = fsg.Input(key="feet", size=field_size)

inch_label = fsg.Text("Enter inches:")
inch_input = fsg.Input(key="inches", size=field_size)

convert_button = fsg.Button("Convert", key="convert", size=button_size)
convert_result = fsg.Text(key="result")

exit_button = fsg.Button("Exit", key="exit", size=button_size)

# Layout
layout = [
    [foot_label, fsg.Push(), foot_input],
    [inch_label, fsg.Push(), inch_input],
    [convert_button, convert_result, fsg.Push(), exit_button]
]

# Window
window = fsg. Window("Foot and Inch Converter", layout=layout)

# Logic
while True:
    event, data = window.read()

    match event:
        case "convert":
            feet = float(data["feet"])
            inches = float(data["inches"])
            meters = feet * 0.3048 + inches * 0.0254
            window["result"].update(value=f"{meters} m")

        case "exit" | fsg.WINDOW_CLOSED:
            break

window.close()
