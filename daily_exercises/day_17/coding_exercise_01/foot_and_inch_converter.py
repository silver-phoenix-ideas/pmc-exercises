# Imports
import FreeSimpleGUI as fsg

# Widgets
foot_label = fsg.Text("Enter feet:")
foot_input = fsg.Input(key="feet")

inch_label = fsg.Text("Enter inches:")
inch_input = fsg.Input(key="inches")

convert_button = fsg.Button("Convert", key="convert")
convert_result = fsg.Text(key="result")

# Layout
layout = [
    [foot_label, foot_input],
    [inch_label, inch_input],
    [convert_button, convert_result]
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

        case fsg.WINDOW_CLOSED:
            break

window.close()
