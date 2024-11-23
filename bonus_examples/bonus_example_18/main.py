# Imports
import FreeSimpleGUI as fsg
import archive_extractor

# Settings
fsg.theme("DarkGrey9")
fsg.set_options(font=("Helvetica", 12))
field_size = (30, 1)
button_size = (10, 1)

# Widgets
file_label = fsg.Text("Select archive:")
file_field = fsg.Input(size=field_size)
file_button = fsg.FileBrowse("Choose", key="file", size=button_size)

folder_label = fsg.Text("Select destination")
folder_field = fsg.Input(size=field_size)
folder_button = fsg.FolderBrowse("Choose", key="folder", size=button_size)

extract_button = fsg.Button("Extract", key="extract", size=button_size)
extract_status = fsg.Text(key="status", text_color="green")


# Layout
layout = [
    [file_label, fsg.Push(), file_field, file_button],
    [folder_label, fsg.Push(), folder_field, folder_button],
    [extract_button, extract_status]
]

# Window
window = fsg.Window("Archive Extractor", layout=layout)

# Logic
while True:
    event, data = window.read()

    match event:
        case "extract":
            archive = data["file"]
            destination = data["folder"]
            archive_extractor.extract_archive(archive, destination)
            window["status"].update("Extraction Successful!")

        case fsg.WINDOW_CLOSED:
            break

window.close()
