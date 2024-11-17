# Imports
import FreeSimpleGUI as fsg

# Widgets
label1 = fsg.Text("Select files to compress:")
input1 = fsg.Input()
button1 = fsg.FilesBrowse("Choose")

label2 = fsg.Text("Select destination folder:")
input2 = fsg.Input()
button2 = fsg.FolderBrowse("Choose")

compress_button = fsg.Button("Compress")

# Layout
layout = [
    [label1, input1, button1],
    [label2, input2, button2],
    [compress_button]
]

# Window
window = fsg.Window("File Compressor", layout=layout)

# Logic
window.read()
window.close()
