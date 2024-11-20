# Imports
import FreeSimpleGUI as fsg
import archive_creator as ac

# Widgets
files_label = fsg.Text("Select files to compress:")
files_field = fsg.Input()
files_button = fsg.FilesBrowse("Choose", key="files")

folder_label = fsg.Text("Select destination folder:")
folder_field = fsg.Input()
folder_button = fsg.FolderBrowse("Choose", key="folder")

compress_button = fsg.Button("Compress", key="compress")
compress_status = fsg.Text(key="status", text_color="green")

# Layout
layout = [
    [files_label, files_field, files_button],
    [folder_label, folder_field, folder_button],
    [compress_button, compress_status]
]

# Window
window = fsg.Window("Archive Creator", layout=layout)

# Logic
while True:
    event, data = window.read()

    match event:
        case "compress":
            file_paths = data["files"].split(";")
            folder_path = data["folder"]
            ac.make_archive(file_paths, folder_path)
            window["status"].update(value="Compression successful!")

        case fsg.WINDOW_CLOSED:
            break

window.close()
