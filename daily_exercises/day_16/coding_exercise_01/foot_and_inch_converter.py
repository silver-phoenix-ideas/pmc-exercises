# Imports
import FreeSimpleGUI as fsg

# Widgets
foot_label = fsg.Text("Enter feet:")
foot_input = fsg.Input()

inch_label = fsg.Text("Enter inches:")
inch_input = fsg.Input()

convert_button = fsg.Button("Convert")

# Layout
layout = [
    [foot_label, foot_input],
    [inch_label, inch_input],
    [convert_button]
]

# Window
window = fsg. Window("Foot and Inch Converter", layout=layout)

# Logic
window.read()
window.close()
